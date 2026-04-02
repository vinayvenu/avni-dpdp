# DPDP-Required and DPDP-Supporting Features for Avni

This document consolidates all platform features required or recommended for DPDP compliance, drawn from the full analysis across `consent.md`, `security_requirements.md`, `contract_changes.md`, `hosting_support_changes.md`, and `dpdp_addendum.md`.

Features are organized by functional area. Priority classification:
- **MUST** — legally required or directly necessary to meet a DPDP obligation
- **SHOULD** — strongly recommended; absence creates legal or operational risk
- **COULD** — good practice; relevant when becoming a Significant Data Fiduciary or as the platform matures

**Deadline:** All MUST features must be ready before **13 May 2027**. Consent collection and erasure workflows (F2–F8) are accelerated — target delivery by **end of August 2026** — because customers are evaluating DPDP compliance posture now and the consent flow is the core product obligation.

---

## 1. Consent Collection

### F1 — OTP-Based Consent Flow
**Priority:** COULD
**Legal basis:** Act Section 6(1); Aadhaar Guidelines Section 10, 13, Annexure A.13
**Current status:** Not available
**Target:** Post August 2026 — build only if customers request it

The strongest legally defensible consent method for assisted mode. An OTP is sent to the beneficiary's registered mobile number; the beneficiary reads it aloud and the field worker enters it in Avni. The affirmative action is traceable to the beneficiary's device and cannot be performed by the field worker.

However, OTP is not always feasible in Avni's field context:
- Many field workers use shared phones, which makes it impossible to establish phone ownership by the beneficiary
- Network connectivity may be unavailable at the point of enrollment

F2 (audio recording) and F3 (signed form) are the primary consent methods and fully satisfy the legal requirement. OTP has no compliance advantage over these methods for Avni's deployment context. It will not be built as part of the August 2026 goal; it can be added later if a specific customer requests it.

The OTP and consent event must be stored linked to the beneficiary record with a timestamp.

---

### F2 — Field Worker Audio Reading + Beneficiary Verbal Consent Recording
**Priority:** MUST
**Legal basis:** Act Section 6(1); IT Act Section 65B; Aadhaar Guidelines Section 7, 8, Annexure A.11
**Current status:** Partially available (audio recording exists; not formalized as a structured consent flow)
**Target:** End of July 2026

The field worker reads the DPDP-compliant notice text aloud in the local language and records themselves doing so, capturing both the notice delivery and the beneficiary's verbal consent ("I consent" or equivalent) in a single audio recording. This approach handles language diversity and cultural constraints — no pre-recorded system audio in every language is required; the field worker reads naturally in whatever dialect or language the beneficiary understands.

The recording must be timestamped, linked to the beneficiary record and the specific notice text version shown on screen, and stored tamper-proof. This must be a structured form step with a required recording, not an ad-hoc audio attachment.

Legal counsel should confirm adequacy before deployment — the Aadhaar Guidelines endorse audio notice but do not explicitly list field-worker-read verbal consent recording as a primary consent practice. It is inferred from the electronic records framework (IT Act Section 65B).

---

### F3 — Signed Physical Form + Image Capture Consent Flow
**Priority:** MUST
**Legal basis:** Act Section 6(1), 6(10); Indian Evidence Act Section 73, 65B; Aadhaar Guidelines Section 8, 10, 11
**Current status:** Partially available (image capture exists; not formalized as a structured consent step)
**Target:** End of July 2026

The field worker presents a printed DPDP-compliant notice form; the beneficiary signs or thumb-prints it; the field worker photographs the signed form and the image is automatically linked to the beneficiary record with a timestamp. The notice text version used must be stored alongside the image.

The current image capture is generic — this needs to be a specific consent-form capture step in the registration workflow, not a free-form attachment.

---

### F4 — Mandatory Notice Delivery Step in Registration
**Priority:** MUST
**Legal basis:** Act Section 5; Rules 2025, Rule 3
**Current status:** Not enforced
**Target:** End of July 2026

Notice delivery must precede data collection. The registration form should require a notice step — displayed text, field worker recording, or signed form capture — before the beneficiary's personal data fields become accessible. The form should not allow submission without the notice step being completed and logged.

This makes compliant registration the only path, rather than an optional add-on.

---

### F5 — Consent Status Per Beneficiary Record
**Priority:** MUST
**Legal basis:** Act Section 6(1), 6(10)
**Current status:** Not confirmed
**Target:** End of July 2026 (data model design in June; migration strategy for existing records required)

Each beneficiary record should store: consent status (given / not given / withdrawn), consent method used (OTP / signed form / audio recording), date and time, field worker who collected it, and notice text version shown. This is the data that feeds the Consent Registry Report (R1 below) and is the primary evidence in a Board proceeding.

---

## 2. Notice Delivery to Existing Beneficiaries

### F6 — Retrospective Notice Delivery Tracking
**Priority:** MUST
**Legal basis:** Act Section 5(2)
**Current status:** Not available
**Target:** November 2026 — must be ready early enough for NGOs to run field campaigns before May 2027

Section 5(2) requires fiduciaries to deliver DPDP-compliant notice to all existing beneficiaries who gave consent before 13 May 2027. For field programs with no digital channel to beneficiaries, this means a physical revisit by field workers — a significant operational undertaking.

Avni needs a flag per beneficiary record indicating whether retrospective DPDP notice has been delivered, and a workflow for field workers to mark delivery when they visit. This feeds the Outstanding Retrospective Notice Report (R2).

---

## 3. Erasure and Data Lifecycle

### F7 — Erasure Workflow on Consent Withdrawal
**Priority:** MUST
**Legal basis:** Act Section 8(7)(a)/(b); Section 6(6)
**Current status:** Not available — void is the only current mechanism and is a soft-delete only
**Target:** End of August 2026 (design week in June required before development begins)

The new consent workflow (F2–F5) will introduce dedicated mechanisms for consent withdrawal and erasure. Void remains the only available mechanism today and should trigger erasure in the interim. Once the consent workflow is in place, consent withdrawal through that workflow must be the primary trigger for erasure — the void-based path remains as a fallback.

In both cases, the withdrawal event must become the start of an erasure workflow, not a terminal event. The workflow must track completion of each step:

| Step | Action | Legal basis |
|------|--------|-------------|
| 1 | Erase personal data fields from cloud DB (retain audit log of void event) | Act S.8(7)(a) |
| 2 | Erase associated files and images from S3 | Act S.8(7)(a) |
| 3 | Clear beneficiary data from Realm on Android devices on next sync | Act S.6(6) |
| 4 | Allow PITR backups to expire naturally (35-day window) | Act S.8(7)(b) |
| 5 | Confirm erasure to NGO in writing once backup window has passed | Contract G.1(f) / Clause 3.3 |

The workflow must have a 30-day deadline (per contract) and must be trackable by NGO admins (R5).

**Backup deletion approach — requires infra sign-off before development:**
AWS RDS Point-in-Time Recovery (PITR) backups are continuous snapshots — surgical deletion of a single beneficiary's data from a backup is not possible. The compliant approach is:
- Erase from production DB and S3 on the day of the void (Steps 1–2 above)
- PITR backups then contain data that no longer exists in production; these age out and are automatically deleted after 35 days
- The 30-day contractual erasure SLA is met because production erasure happens immediately; backup expiry falls within the window
- The erasure workflow tracker (R5) must not mark a request "complete" until the 35-day backup window has passed
- Retain only the void event audit log — not the personal data — in perpetuity for compliance evidence

The Samanvay infrastructure team must validate this approach and confirm the PITR retention period before development begins.

---

### F8 — Erasure on Written Instruction (Data Principal Rights)
**Priority:** MUST
**Legal basis:** Act Section 12; Act Section 8(7)
**Current status:** Not available
**Target:** End of August 2026 (same workflow as F7; implement together)

Separate from consent withdrawal, a beneficiary may request erasure of their data under Section 12. The NGO must be able to issue a written erasure instruction to Samanvay. Avni should provide a mechanism for the NGO admin to initiate this, which flows into the same erasure workflow as F7.

---

### F9 — Purpose Expiry Detection
**Priority:** SHOULD
**Legal basis:** Act Section 8(7)(a)
**Current status:** Not available
**Target:** Q1 2027

Section 8(7)(a) requires erasure when the specified purpose is no longer being served — not only on consent withdrawal. Avni should flag beneficiaries whose program has ended or who have been inactive beyond a configurable threshold, prompting the NGO admin to decide: retain with documented justification, or initiate erasure.

---

## 4. Data Principal Rights

### F10 — Data Principal Rights Request Log
**Priority:** MUST
**Legal basis:** Act Section 11 (access), Section 12 (erasure/correction)
**Current status:** Not available
**Target:** November 2026

There is currently no mechanism in Avni for an NGO to receive, log, and track requests from beneficiaries for access to, correction of, or erasure of their personal data. Even a minimal intake log — request date, type, beneficiary identifier, and resolution date — is needed for the fiduciary to demonstrate they are processing rights requests as legally required.

---

### F11 — In-App Consent Withdrawal Mechanism
**Priority:** COULD
**Legal basis:** Act Section 6(4)
**Current status:** Requires field worker physical visit to void
**Target:** Post May 2027

Currently, consent withdrawal requires a field worker to physically visit and void the record. A lightweight in-app or web form allowing a beneficiary (or their representative) to submit a withdrawal request would strengthen the "ease of withdrawal must equal ease of giving" requirement under Section 6(4). Even a simple submission that creates a pending task for the NGO is better than the current process.

---

## 5. Security and Access Controls

### F12 — Application-Level Access Audit Logging
**Priority:** MUST
**Legal basis:** Rules 2025, Rule 6(c), Rule 6(e)
**Current status:** Not confirmed — infrastructure logs exist but application-level user-action logs are unconfirmed
**Target:** November 2026

Every access to a beneficiary record must be logged at the application level: authenticated user ID, timestamp, action (view / create / edit / void), and entity identifier. Logs must be retained for a minimum of one year in a tamper-evident manner.

CloudWatch infrastructure logs do not satisfy this requirement — Rule 6(c) requires visibility on access to personal data specifically, not just server-level events.

---


### F14 — BI Layer Report-Creation Restriction as Platform Default
**Priority:** MUST
**Legal basis:** Rules 2025, Rule 6(b)
**Current status:** Configurable per tenant but not enforced as a default
**Target:** June 2026 (configuration enforcement; quick win)

Metabase/Superset currently allows any authenticated user to write new reports, which can expose raw beneficiary PII through custom queries. Report-creation must be restricted to designated admin roles as a platform-wide default, not a per-tenant opt-in. NGOs must request Samanvay to configure these restrictions before granting BI access to any user.

---

### F15 — Bulk Export Logging and Role Restrictions
**Priority:** MUST
**Legal basis:** Rules 2025, Rule 6(a)
**Current status:** No controls — gap
**Target:** August 2026

Currently there is no additional protection on data once downloaded as a spreadsheet. Required controls:
- Log all bulk export events: user identity, timestamp, data scope, approximate record count
- Restrict bulk export permissions to specific roles (not all authenticated users)
- Consider field-level redaction for roles that do not require full PII (e.g., masking phone numbers)

---

### F16 — Periodic OTP Re-Authentication with Token Model
**Priority:** SHOULD (MUST for health/sensitive data deployments)
**Legal basis:** Rules 2025, Rule 6(b)
**Current status:** Password-only — gap
**Target:** Q1 2027

Password-based authentication cannot be technically enforced for strength. Proposed approach:
- Require OTP re-authentication once per month
- Issue a long-lived refresh token stored securely on device between OTP events
- Use short-lived access tokens (1 hour) for all server communication, generated from the refresh token
- Implement refresh token rotation on each use to limit the exposure window of a compromised token

Applies to Android app. The browser-based Data Entry App requires equivalent treatment (see F17).

---

### F17 — Session Timeout for Data Entry App (Web)
**Priority:** SHOULD
**Legal basis:** Rules 2025, Rule 6(b)
**Current status:** Not confirmed
**Target:** Q1 2027

JWT tokens expire after 1 hour, but a browser session left open on a shared device exposes all accessible data. Enforce session timeout on browser inactivity and terminate sessions on tab/window close.

---


### F19 — Breach Detection and Anomaly Alerting
**Priority:** SHOULD
**Legal basis:** Rules 2025, Rule 6(c)
**Current status:** Not confirmed
**Target:** Q1 2027

Logs alone do not detect breaches. Implement automated alerting on CloudWatch or equivalent for:
- Bulk export by a single user within a short time window
- Repeated failed login attempts
- Access from unusual geographies or hours
- Access to a disproportionately large number of beneficiary records in a session

---

### F20 — Pseudonymisation / Tokenisation in Exports and Logs
**Priority:** COULD
**Legal basis:** Rules 2025, Rule 6(a)
**Current status:** Not in place
**Target:** Post May 2027

Rule 6(a) specifically mentions "use of virtual tokens mapped to that personal data" as an example of appropriate security. Replacing beneficiary names and phone numbers with internal tokens in exports, logs, and BI reports would limit exposure in a breach scenario and limit what can be inferred from a stolen export.

---

## 6. Reporting and Compliance Dashboard

### R1 — Consent Registry Report
**Priority:** MUST
**Legal basis:** Act Section 6(10)
**Current status:** Not available
**Target:** August 2026 (depends on F5)

Per-beneficiary report showing: consent status, method used, notice text version, date and time collected, and field worker identity. This is the primary document a fiduciary produces in response to a Board enquiry about consent practices.

Must be exportable and filterable by program, catchment, date range, and consent method.

---

### R2 — Outstanding Retrospective Notice Report
**Priority:** MUST
**Legal basis:** Act Section 5(2)
**Current status:** Not available
**Target:** November 2026 (depends on F6)

List of all beneficiaries for whom retrospective DPDP notice has not yet been delivered. Field workers use this to plan revisit schedules. Updated as deliveries are recorded. Tracks progress toward the Section 5(2) obligation deadline.

---

### R3 — Bulk Export Log Report
**Priority:** MUST
**Legal basis:** Rules 2025, Rule 6(a); Contract G.2(e)
**Current status:** Not available
**Target:** August 2026 (depends on F15)

Log of all bulk data exports: user, timestamp, data scope, record count. Accessible to NGO admins. Serves as internal control and evidence of compliance with bulk export obligations.

---

### R4 — Access Audit Report
**Priority:** MUST
**Legal basis:** Rules 2025, Rule 6(c)
**Current status:** Not available (depends on F12 being implemented)
**Target:** November 2026 (depends on F12)

Surfacing of application-level access logs (F12) for NGO admins. Filterable by user, date range, and beneficiary. Enables supervisors to spot unexpected access patterns and supports investigation in a breach scenario.

---

### R5 — Erasure Workflow Status Report
**Priority:** MUST
**Legal basis:** Act Section 8(7); Contract G.1(f) / Clause 3.3
**Current status:** Not available
**Target:** August 2026 (depends on F7/F8; must show backup expiry status)

Tracks all active and completed erasure workflows (F7, F8): void date, 30-day deadline, steps completed, steps pending, and written confirmation of completion to the NGO. Both NGO admins and Samanvay need visibility on this.

---

### R6 — Data Retention / Purpose Expiry Report
**Priority:** SHOULD
**Legal basis:** Act Section 8(7)(a)
**Current status:** Not available
**Target:** Q1 2027 (depends on F9)

List of beneficiaries whose program has ended or who have been inactive beyond a configurable threshold. Prompts the NGO to review whether continued retention is justified or whether erasure should be initiated.

---


### R8 — DPDP Compliance Dashboard for NGO Admins
**Priority:** SHOULD
**Legal basis:** General compliance posture
**Current status:** Not available
**Target:** Q1 2027

Aggregate view for NGO programme administrators showing compliance posture at a glance:
- % of active beneficiaries with consent recorded, by method
- Retrospective notice delivery progress (% complete)
- Open Data Principal rights requests and their age
- Pending erasure requests and 30-day deadline status
- Recent device incidents

Not individual beneficiary data — aggregate indicators only.

---

## Delivery Roadmap

Consent collection and erasure workflows are accelerated to August 2026 because customers are evaluating DPDP compliance posture now and may not onboard onto systems that cannot demonstrate a compliance plan. The addendum should be sent to existing customers in parallel, starting May 2026 — it does not require features to be ready at signing.

### Wave 1 — June 2026 (Quick wins, no feature development needed)
- **F14**: Enforce BI report-creation restrictions as platform default — configuration enforcement
- Begin sending addendum to highest-priority existing customers

### Wave 2 — July 2026 (Core consent flows)
- **F2**: Formalized audio notice + audio recording consent flow
- **F3**: Signed form + image capture consent flow
- **F4**: Mandatory notice delivery step in enrollment
- **F5**: Consent status stored per beneficiary record (data model; requires migration design in June)

### Wave 3 — August 2026 (Erasure, OTP consent, first reports)
- **F7**: Erasure workflow triggered by void — *design must happen in June before development; infra sign-off on backup expiry approach required*
- **F8**: Erasure on written instruction (same workflow as F7)
- **F15**: Bulk export logging and role restrictions
- **R1**: Consent Registry Report (depends on F5)
- **R3**: Bulk Export Log Report (depends on F15)
- **R5**: Erasure Workflow Status Report (depends on F7/F8; must show backup expiry countdown)

### Wave 4 — September–November 2026 (Rights management, audit logging, retrospective notice)
- **F6**: Retrospective notice delivery tracking — must be ready early enough for NGOs to run field campaigns before May 2027
- **F10**: Data Principal rights request log
- **F12**: Application-level access audit logging
- **R2**: Outstanding Retrospective Notice Report (depends on F6)
- **R4**: Access Audit Report (depends on F12)

### Wave 5 — Q1 2027 (Security hardening, remaining reporting)
- **F16**: Periodic OTP re-auth + token model (Android app)
- **F17**: Session timeout for Data Entry App (web)
- **F19**: Breach detection and anomaly alerting
- **F9**: Purpose expiry detection
- **R6**: Data Retention / Purpose Expiry Report
- **R8**: DPDP Compliance Dashboard for NGO Admins

### Post May 2027
- **F11**: In-app consent withdrawal mechanism
- **F20**: Pseudonymisation / tokenisation

---

### Critical path dependencies

| Dependency | Blocks |
|-----------|--------|
| F5 (consent status data model) | R1 (Consent Registry Report) |
| F6 (retrospective notice tracking) | R2 (Retrospective Notice Report); NGO field campaign |
| F7/F8 (erasure workflows) | R5 (Erasure Status Report) |
| F12 (access audit logging) | R4 (Access Audit Report) |
| Infra sign-off on backup expiry approach (June) | F7/F8 development (July–August) |

---

## Summary Table

| ID | Feature | Area | Priority | Target | Current Status |
|----|---------|------|:--------:|--------|---------------|
| F14 | BI report-creation restriction as platform default | Security | MUST | Jun 2026 | Per-tenant only |
| F2 | Field worker audio reading + beneficiary verbal consent recording | Consent | MUST | Jul 2026 | Partial — needs formalization |
| F3 | Signed form + image capture consent flow | Consent | MUST | Jul 2026 | Partial — needs formalization |
| F4 | Mandatory notice delivery step in registration | Consent | MUST | Jul 2026 | Not enforced |
| F5 | Consent status stored per beneficiary record | Consent | MUST | Jul 2026 | Not confirmed |
| F7 | Erasure workflow on consent withdrawal | Erasure | MUST | Aug 2026 | Not available — void is soft-delete only |
| F8 | Erasure on written instruction (rights request) | Erasure | MUST | Aug 2026 | Not available |
| F15 | Bulk export logging and role restrictions | Security | MUST | Aug 2026 | No controls |
| R1 | Consent Registry Report | Reporting | MUST | Aug 2026 | Not available |
| R3 | Bulk Export Log Report | Reporting | MUST | Aug 2026 | Not available |
| R5 | Erasure Workflow Status Report | Reporting | MUST | Aug 2026 | Not available |
| F6 | Retrospective notice delivery tracking | Notice | MUST | Nov 2026 | Not available |
| F10 | Data Principal rights request log | Rights | MUST | Nov 2026 | Not available |
| F12 | Application-level access audit logging | Security | MUST | Nov 2026 | Not confirmed |
| R2 | Outstanding Retrospective Notice Report | Reporting | MUST | Nov 2026 | Not available |
| R4 | Access Audit Report | Reporting | MUST | Nov 2026 | Depends on F12 |
| F1 | OTP-based consent flow | Consent | COULD | Post Aug 2026 (on request) | Not available |
| F9 | Purpose expiry detection | Erasure | SHOULD | Q1 2027 | Not available |
| F16 | Periodic OTP re-auth + token model | Security | SHOULD (MUST: sensitive data) | Q1 2027 | Not in place |
| F17 | Session timeout for Data Entry App (web) | Security | SHOULD | Q1 2027 | Not confirmed |
| F19 | Breach detection and anomaly alerting | Security | SHOULD | Q1 2027 | Not confirmed |
| R6 | Data Retention / Purpose Expiry Report | Reporting | SHOULD | Q1 2027 | Not available |
| R8 | DPDP Compliance Dashboard for NGO Admins | Reporting | SHOULD | Q1 2027 | Not available |
| F11 | In-app consent withdrawal mechanism | Rights | COULD | Post May 2027 | Requires field worker visit |
| F20 | Pseudonymisation / tokenisation | Security | COULD | Post May 2027 | Not in place |
