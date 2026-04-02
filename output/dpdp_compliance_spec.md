# DPDP Compliance for Avni — Spec

## Primary Goals / Motivation

The Digital Personal Data Protection Act 2023 (DPDP Act) and DPDP Rules 2025 impose legally binding obligations on organisations that collect and process personal data. Avni is used by NGOs (Data Fiduciaries) to collect sensitive beneficiary data — health records, social background, personal identifiers — through field workers using mobile devices. Samanvay hosts the platform as Data Processor.

The substantive obligations come into force on **13 May 2027**. Consent collection and erasure mechanisms must be ready significantly earlier (target: August 2026) because NGO customers are evaluating DPDP compliance posture now.

**Current limitations:**
- No consent collection mechanism exists. Field workers collect data without structured, legally defensible consent.
- Void (soft delete) is the only deletion mechanism. It does not erase personal data — the record remains in the cloud DB, on Android devices, in S3, and in ETL tables.
- No application-level access audit logging exists. The server tracks who created/modified an entity but not who viewed it.
- Bulk exports have no logging, no role restrictions, and no PII redaction.
- There is no way to mark a concept as PII for downstream redaction.
- Compliance reporting does not exist.

**What this delivers:**
A complete consent lifecycle (collection, tracking, withdrawal, erasure), security controls (audit logging, export restrictions, PII marking), and compliance reporting — all built as core Avni platform features.

---

## Feature Description

### 1. Consent Entity and Data Model

A new **Consent** entity is introduced as a first-class, independently synced entity with a **weak link** to the subject (stores subject UUID, no foreign key constraint). The subject may be deleted while the consent record persists — this is by design, as consent evidence must survive erasure.

**Consent record fields:**
- `uuid` — primary key
- `subject_uuid` — weak reference to the subject (no FK)
- `subject_type_uuid` — reference to subject type
- `address_id` — for sync scoping (follows same catchment rules as subjects)
- `status` — one of: `Unknown`, `Given`, `Withdrawn`
- `consent_method` — one of: `Audio`, `SignedForm`, `External`, `null` (null when Unknown)
- `consent_artifact` — S3 reference to the audio recording or signed form image (null when External or Unknown)
- `external_reference_id` — optional reference ID when consent was collected externally
- `notice_version` — version identifier of the DPDP notice text shown at time of consent
- `consent_given_at` — timestamp when consent was given
- `consent_withdrawn_at` — timestamp when consent was withdrawn
- `purged_at` — timestamp when subject data was actually erased (set by server after erasure completes)
- `cancellation_window_end` — computed from `consent_withdrawn_at` + system-level window duration
- `field_worker_id` — who collected/withdrew consent
- Standard audit fields (created_by, last_modified_by, timestamps)
- `organisation_id` — for multi-tenancy

**Key design decisions:**
- Consent syncs independently from the subject, on its own sync endpoint.
- Consent follows the same sync scope as subjects (address_id-based catchment).
- One consent record per subject (not per program enrolment).
- No history of consent events — only current state, with timestamps for when consent was given and when it was withdrawn.

### 2. Subject Type Configuration

A new flag **`requires_consent`** is added to the SubjectType entity (in the `settings` JSON or as an explicit column). When enabled:

- Registration forms for this subject type gain a mandatory consent step as page 0 (before any personal data fields).
- A background job creates consent records with status `Unknown` for all existing subjects of that type.
- The default consent method can be configured at the subject type level, but all methods remain available to the field worker.

### 3. Consent Collection at Registration

When a subject type requires consent, the registration wizard gains a new **page 0** — the consent step — which appears before the existing page 1 (name, DOB, etc.).

**Page 0 behaviour:**
- Displays the DPDP-compliant notice text (configurable per organisation, versioned).
- Offers consent collection via one of three methods:
  - **Audio recording**: Field worker reads the notice aloud and records the beneficiary's verbal consent. Uses the existing audio recording capability. The recording is a mandatory field — the form cannot proceed without it.
  - **Signed form + image capture**: Field worker presents a printed notice form; beneficiary signs; field worker photographs the signed form. Uses existing image capture. The image is mandatory.
  - **External**: Consent was collected outside Avni. An optional reference ID field is provided. A checkbox confirms consent was collected.
- If the beneficiary **refuses consent**, registration is abandoned entirely. No subject record is created.
- If consent is given, registration proceeds normally. A consent record with status `Given` is created alongside the subject.

**The same flow applies to the webapp Data Entry App.**

### 4. Consent Collection via CSV

Bulk consent operations are supported via CSV upload:

- **Bulk consent addition**: CSV contains subject identifiers + consent method + date + optional external reference ID. Creates or updates consent records to status `Given` for existing subjects.
- **Bulk consent withdrawal**: CSV contains subject identifiers + withdrawal date. Updates consent records to status `Withdrawn`, triggering the cancellation window and eventual erasure workflow.

### 5. Consent Withdrawal and Cancellation Window

Consent can be withdrawn by a field worker (mobile or webapp) or via CSV bulk upload. The withdrawal triggers a **cancellation window** — a system-level configurable duration (e.g., 7 days) during which anyone can cancel the withdrawal, preventing accidental erasure.

**Withdrawal flow:**
1. Field worker or admin marks consent as withdrawn. `consent_withdrawn_at` is set. Status becomes `Withdrawn`.
2. During the cancellation window, the withdrawal can be reversed by any user. Status returns to `Given`.
3. After the cancellation window expires, the server begins the erasure workflow. No manual trigger is needed — a scheduled job checks for expired windows.

### 6. Erasure Workflow

When the cancellation window expires, the server executes a hard delete of all subject data:

**Server-side erasure:**
1. Delete the subject row from the `individual` table. This cascades to: program enrolments, encounters, program encounters, checklists, checklist items, group subjects, individual relationships, comments, approval statuses, user subject assignments.
2. Delete all associated S3 objects (media files from observations across all cascaded entities, profile pictures).
3. Set `purged_at` timestamp on the consent record. This is the evidence that erasure occurred and when.
4. The consent record itself is **retained** — it is the audit trail proving consent was given and later withdrawn, and that erasure was performed.

**Client-side erasure (mobile):**
- The consent record syncs to the client with status `Withdrawn`.
- While within the cancellation window, the client takes no destructive action (the subject remains in Realm).
- When the consent record syncs with `purged_at` set (meaning server-side erasure is complete), the client deletes the subject and all related entities from Realm, and removes associated media files from the filesystem.
- The consent record remains in Realm.

**Race condition handling:** A client may revoke the withdrawal (cancel it) and sync to the server while the server has already deleted the subject. The server must detect this conflict: if `purged_at` is already set, the cancellation is rejected and the client is informed that erasure has already occurred.

**ETL purge:** On the next ETL run after server-side erasure, the ETL detects that the subject no longer exists in the source DB and deletes corresponding rows from ETL tables (Registration_*, Enrolment_*, Encounter_* tables).

**PITR backups:** AWS RDS backups are continuous snapshots. Surgical deletion from backups is not possible. The compliant approach: erase from production immediately; PITR backups age out and are automatically deleted after the configured retention period (currently 35 days).

**Integration service:** Out of scope for this spec. External system notification is not included.

### 7. Retrospective Notice Tracking

When a subject type is marked as requiring consent, the background job creates consent records with status `Unknown` for all existing subjects. This serves dual purpose:

- Tracks which subjects still need consent collection (status remains `Unknown`).
- Tracks which subjects have received retrospective DPDP notice delivery.

A separate `notice_delivered_at` field on the consent record tracks when the retrospective notice was delivered, independent of whether consent was given. Field workers mark notice delivery during revisits.

### 8. PII Concept Marking

A new **`is_pii`** boolean flag is added to the Concept entity. Since concepts are per-organisation, each org marks which of their concepts contain personally identifiable information. This flag drives:

- PII redaction/masking in exports for users without PII access permission.
- Future use in access logging, pseudonymisation, and data minimisation.

Core fields on the Individual entity (first_name, last_name, date_of_birth, profile_picture) are implicitly PII and always treated as such, regardless of concept-level marking.

### 9. Application-Level Access Audit Logging

A new audit log records every access to personal data at the application level:

- **What is logged:** authenticated user ID, timestamp, action (view / create / edit / void / export), entity type, entity identifier.
- **Scope:** All API requests that return or modify personal data. This includes: subject detail views, encounter views, search results, sync data pulls, and exports.
- **Retention:** Minimum 1 year, tamper-evident storage.
- **Storage:** A dedicated audit_log table, not inline on entities.

### 10. Bulk Export Controls

**PII access permission:** A new permission controls whether a user can access PII data. This applies initially to bulk exports and will extend to other areas over time.

**Export restrictions:**
- All bulk export events are logged: user identity, timestamp, data scope, approximate record count.
- Users without PII access permission receive exports with PII fields **masked** (e.g., `J*** D***` for names, `****1234` for phone numbers). Masking applies to concepts marked `is_pii` and to implicit PII fields (names, DOB, profile picture).
- Export logging feeds the Bulk Export Log Report (R3).

### 11. BI Layer Report-Creation Restriction

Report creation in Metabase/Superset is restricted to designated admin roles as a **platform-wide default**. This is a configuration enforcement — not a new feature — but must be applied across all tenants.

### 12. Compliance Reporting

Built as **core avni-webapp screens** (not Metabase reports), so they work regardless of which BI tool is deployed.

**R1 — Consent Registry Report:**
Per-beneficiary report showing: consent status, method, notice version, date/time collected, field worker. Filterable by program, catchment, date range, consent method. Exportable.

**R2 — Outstanding Retrospective Notice Report:**
List of subjects where retrospective DPDP notice has not been delivered (consent status is `Unknown` and `notice_delivered_at` is null). Used by field workers to plan revisit schedules.

**R3 — Bulk Export Log Report:**
Log of all bulk exports: user, timestamp, data scope, record count. Accessible to org admins.

**R4 — Access Audit Report:**
Surfacing of application-level access logs. Filterable by user, date range, entity. For supervisors to spot unexpected access patterns.

**R5 — Erasure Workflow Status Report:**
Tracks consent withdrawals: withdrawal date, cancellation window status, erasure completion, `purged_at` timestamp, PITR backup expiry countdown. Visible to org admins.

### 13. Purpose Expiry Detection

Flags subjects whose program has ended or who have been inactive beyond a configurable threshold. Prompts the org admin to decide: retain with documented justification, or initiate erasure. Presented as a report (R6).

### 14. Periodic OTP Re-Authentication

Requires OTP re-authentication once per month on the Android app. Between OTP events, a long-lived refresh token (stored in Android Keystore) issues short-lived access tokens (1 hour). Refresh token rotation on each use limits exposure of compromised tokens.

### 15. Session Timeout for Data Entry App

Enforces session timeout on browser inactivity for the webapp Data Entry App. Terminates sessions on tab/window close. Complements the existing 1-hour JWT expiry.

### 16. Breach Detection and Anomaly Alerting

Automated alerting on:
- Bulk export by a single user within a short time window
- Repeated failed login attempts
- Access from unusual geographies or hours
- Access to a disproportionately large number of beneficiary records in a session

### 17. In-App Consent Withdrawal Mechanism (Post May 2027)

A lightweight web form allowing a beneficiary or their representative to submit a consent withdrawal request. Creates a pending task for the NGO.

### 18. Pseudonymisation / Tokenisation (Post May 2027)

Replace beneficiary names and phone numbers with internal tokens in exports, logs, and BI reports.

---

## Overall Technical Approach

### Repositories Affected

| Repository | Scope |
|------------|-------|
| **avni-server** | Consent entity, API endpoints, sync endpoint, CSV import, erasure workflow (scheduled job), audit logging, export controls, PII permission, background job for consent row creation |
| **avni-webapp** | Subject type consent config, consent step in Data Entry App registration, consent management UI, CSV upload for consent, compliance report screens, PII concept marking UI, export permission UI |
| **avni-client** | Consent Realm schema, consent sync, consent step in registration wizard (page 0), client-side erasure on purged_at, audio/image consent capture |
| **avni-models** | Consent model class, PII flag on Concept, SubjectType consent settings |
| **avni-etl** | Purge subjects from ETL tables when source row is deleted, consent data in ETL schema |

### Data Model Changes

**New table: `consent`**
- Independent entity, own sync lifecycle
- Weak link to subject (UUID, no FK)
- Contains `address_id` for sync scoping
- Contains S3 references for consent artifacts
- Multi-tenant via `organisation_id`

**New table: `audit_log`**
- Dedicated access audit logging
- High-volume, append-only
- Retained minimum 1 year

**Modified: `subject_type`**
- New: `requires_consent` flag (in settings JSON or explicit column)
- New: `default_consent_method` setting

**Modified: `concept`**
- New: `is_pii` boolean column

**New Realm schema: `Consent`**
- Mirrors server consent entity
- Synced independently

### Key Design Decisions

1. **Consent is a separate entity, not part of the subject.** This allows consent evidence to survive subject erasure, enables independent sync, and cleanly separates the consent lifecycle from the subject lifecycle.

2. **Hard delete, not soft delete, for erasure.** The DPDP Act requires actual erasure, not flagging. The subject row and all cascaded entities are physically deleted. Only the consent record survives.

3. **Server-driven erasure with client following.** The server performs the hard delete after the cancellation window. The client learns about it via the `purged_at` field on the synced consent record and then purges locally.

4. **Cancellation window prevents accidental erasure.** A system-level configurable duration during which withdrawal can be reversed by anyone.

5. **Compliance reports are core webapp features.** Built into avni-webapp, not as BI reports, so they work with any BI tool deployment.

6. **PII marking on concepts enables progressive redaction.** Starting with export masking, extending to other areas over time.

### Constraints and Non-Goals

- **Breach notification process, SOPs, and contract changes** are out of scope — these are operational/legal deliverables, not engineering.
- **Integration service data propagation** is out of scope — external system erasure notification is not included.
- **OTP-based consent (F1)** is deferred — built only if a customer requests it.
- **Realm encryption** remains per-org configuration — enforcement is contractual, not a platform code change.
- **No enforcement date for existing subjects** — Avni shows subjects without consent; the tenant works to collect consent as needed.

---

## Stories (to be written)

### avni-models
1. Add Consent model class with schema definition
2. Add `is_pii` boolean to Concept model
3. Add `requiresConsent` and `defaultConsentMethod` to SubjectType model/settings

### avni-server

**Consent data model & API:**
4. Create consent table migration and entity
5. Consent CRUD API endpoints (create, update, read)
6. Consent sync endpoint (independent sync lifecycle, scoped by address_id)
7. Background job: create Unknown consent rows when subject type is marked as requiring consent
8. System-level configuration for consent withdrawal cancellation window

**Consent collection:**
9. CSV import support for bulk consent addition
10. CSV import support for bulk consent withdrawal

**Erasure workflow:**
11. Scheduled job: detect expired cancellation windows and trigger erasure
12. Erasure service: hard delete subject and all cascaded entities
13. Erasure service: delete all S3 objects linked to subject (observations across all entities + profile picture)
14. Set `purged_at` on consent record after successful erasure
15. Handle race condition: reject cancellation if `purged_at` is already set

**PII & access controls:**
16. Add `is_pii` column to concept table
17. PII access permission (new privilege)
18. Bulk export logging (user, timestamp, scope, record count)
19. PII masking in exports for users without PII access permission

**Audit logging:**
20. Create audit_log table and entity
21. Intercept API requests that access personal data and write audit log entries
22. Audit log retention policy (minimum 1 year)

**Security:**
23. Periodic OTP re-authentication endpoint and refresh/access token model
24. Breach detection alerting rules (CloudWatch or equivalent)

### avni-webapp

**Subject type configuration:**
25. Add `requires_consent` toggle and `default_consent_method` selector to subject type admin UI
26. Add `is_pii` toggle to concept configuration UI

**Consent in Data Entry App:**
27. Consent step (page 0) in registration form for consent-required subject types
28. Consent withdrawal UI for existing subjects
29. CSV upload support for consent (addition and withdrawal)

**Access controls:**
30. PII access permission configuration in role management UI
31. BI report-creation restriction enforcement as platform default

**Compliance reports:**
32. R1 — Consent Registry Report screen
33. R2 — Outstanding Retrospective Notice Report screen
34. R3 — Bulk Export Log Report screen
35. R4 — Access Audit Report screen
36. R5 — Erasure Workflow Status Report screen

**Security:**
37. Session timeout on inactivity for Data Entry App

### avni-client

**Consent model & sync:**
38. Add Consent Realm schema
39. Consent sync service (independent sync, scoped by address_id)

**Registration flow:**
40. Consent step (page 0) in registration wizard for consent-required subject types
41. Audio recording consent capture (mandatory recording in consent step)
42. Signed form image capture consent capture (mandatory image in consent step)
43. External consent capture (checkbox + optional reference ID)
44. Abandon registration if consent is refused

**Erasure:**
45. Client-side subject purge when consent syncs with `purged_at` set
46. Delete subject-linked media files from filesystem on purge

**Security:**
47. OTP re-authentication flow (monthly) with refresh/access token model

### avni-etl
48. Purge subject rows from ETL tables when source subject no longer exists in main DB
49. Include consent data in ETL schema for compliance reporting

### Post May 2027 (deferred)
50. F11 — In-app consent withdrawal web form for beneficiaries
51. F20 — Pseudonymisation/tokenisation in exports and logs
52. F1 — OTP-based consent flow (on customer request)

### Later scope (not stories yet)
- R6 — Data Retention / Purpose Expiry Report (depends on F9, target Q1 2027)
- R8 — DPDP Compliance Dashboard for NGO Admins (aggregate view, target Q1 2027)
