# DPDP Security Requirements for Avni

**Legal basis:** DPDP Rules 2025, Rule 6 (Reasonable Security Safeguards) and Rule 7 (Breach Notification). These apply to the implementing NGO as Data Fiduciary and to Samanvay as Data Processor. Rule 6 specifies a **minimum mandatory list** — all items under Rule 6(a)–(g) are legal obligations, not recommendations.

**Architecture context:** Avni is a multi-tenant field data collection platform. Field workers use an Android app (offline, Realm DB) or browser-based Data Entry App. All data syncs to Samanvay's AWS Mumbai cloud (PostgreSQL + S3). Tenant isolation is at the PostgreSQL DB-user level.

---

## Implementation Deadline

**All security requirements must be implemented by 13 May 2027** — 18 months from the notification of the DPDP Rules on 13 November 2025, when Rules 5–16 (including Rule 6 and Rule 7) come into force.

*Today is 1 April 2026. Approximately 13 months remain.*

**Security requirements are fully retrospective.** Rule 6 requires the Data Fiduciary to protect "personal data in its possession or under its control" — it makes no distinction between data collected before or after commencement. Every beneficiary record currently in Avni is subject to all security safeguards (M1–M8) from 13 May 2027.

| Milestone | Date |
|-----------|------|
| DPDP Rules notified | 13 November 2025 |
| Board constituted | 13 November 2025 |
| Board enforcement powers over Data Fiduciaries operational (Section 27) | 13 May 2027 |
| **All security obligations (Rule 6, Rule 7) enforceable** | **13 May 2027** |

---

## MUST HAVE
*Legally mandatory under DPDP Rules 2025. Non-compliance is a direct breach of Rule 6 or Rule 7.*

---

### M1 — Mandatory mobile encryption
**Rule 6(a):** *"securing of personal data through encryption..."*

The Realm database AES-256 encryption is currently **optional per organisation**. Since Avni collects sensitive personal data (health, social background), encryption at rest on field worker devices is not optional under DPDP — it is a minimum legal requirement.

**Gap:** Some NGO deployments may have unencrypted Realm databases on personal phones that cannot be remotely wiped.

**Action:** Enforce AES-256 Realm encryption as mandatory for all Avni deployments. Remove the option to disable it. Document this as a platform-level baseline, not an NGO configuration choice.

---

### M2 — Application-level access audit logs
**Rule 6(c):** *"visibility on the accessing of such personal data, through appropriate logs, monitoring and review, for enabling detection of unauthorised access, its investigation and remediation..."*

Cloudwatch provides infrastructure/server logs. There is no confirmed application-level audit trail recording **which authenticated user accessed or modified which beneficiary's record**. Server logs alone do not satisfy Rule 6(c) — the law requires visibility on access to *personal data specifically*.

**Gap:** Cannot currently answer "which field worker viewed beneficiary X's record on date Y."

**Action:** Implement application-level audit logging: user ID, timestamp, action (view/create/edit/void), and subject/entity identifier — stored tamper-proof and retained for minimum 1 year.

---

### M3 — Confirmed 1-year log retention
**Rule 6(e):** *"retain such logs and personal data for a period of one year..."*
**Rule 8(3):** *"retain...personal data, associated traffic data and other logs of the processing for a minimum period of one year..."*

Current Cloudwatch log retention period is unconfirmed. It must be set to a minimum of 1 year across all log groups (application, infrastructure, access logs).

**Action:** Audit and set all Cloudwatch log group retention policies to ≥ 1 year. Document the configuration.

**Note — Rule 6(e) also requires personal data retention:** Rule 6(e) mandates retention of both *logs* and *personal data* for a minimum of one year — not just logs. This has a direct implication for the erasure workflow: personal data involved in a breach cannot be immediately erased; it must be retained for at least one year for investigation purposes, even where consent has been simultaneously withdrawn. Erasure workflows must account for this carve-out.

**Note — Rule 8(3) Seventh Schedule conditioning:** Rule 8(3)'s 1-year minimum retention obligation applies "for the purposes as specified in the Seventh Schedule." The Seventh Schedule should be reviewed to confirm that Avni's specific data processing use cases are covered. This does not diminish the Rule 6(e) obligation (which is unconditional for logs), but is relevant for personal data retention claims based on Rule 8(3).

---

### M4 — Restrict PII-exposing report creation in Metabase/Superset
**Rule 6(b):** *"appropriate measures to control access to the computer resources..."*

The BI layer (Metabase/Superset) currently allows users to write new reports. Custom reports can expose raw beneficiary PII without RBAC constraints. This is not currently restricted — it is configurable per tenant but not enforced.

**Gap:** An authorised BI user can currently write an unrestricted query accessing all beneficiary data for their tenant.

**Action:** Enforce report-writing restrictions for all tenants by default. Only designated admin roles should be able to create new reports. This must be a default platform posture, not a per-tenant opt-in.

---

### M5 — PII protection on bulk data exports
**Rule 6(a):** *"securing of personal data through encryption, obfuscation, masking..."*

The infrastructure doc explicitly states: *"There is no additional protection of PII or any other sensitive information once downloaded from the system in the form of spreadsheets by an authenticated and authorised user."* Once exported, data is uncontrolled.

**Gap:** Bulk exports containing full beneficiary PII (names, health data, addresses) leave the system without any controls.

**Action (minimum):** Log all bulk export events with user identity, timestamp, and data scope. Restrict bulk export permissions to specific roles. Consider field-level redaction (e.g., masking phone numbers in exports) for roles that don't need full PII.

---

### M6 — Documented breach notification process
**Rule 7(1):** Notify each affected Data Principal *"without delay"* of a breach.
**Rule 7(2)(a):** Notify the Data Protection Board *"without delay"* with a preliminary notification upon becoming aware of a breach. This is an immediate obligation — there is no grace period.
**Rule 7(2)(b):** Provide a detailed follow-up notification to the Board **within 72 hours** of becoming aware, containing full particulars of the breach.

Rule 7 is therefore a **two-stage** Board notification obligation, not a single 72-hour deadline. The 72-hour window applies to the detailed report, but the preliminary notification to the Board must be made "without delay" — which may mean within hours of becoming aware.

There is no documented incident response plan or breach notification process. In a breach scenario, responsibility must be clearly defined between Samanvay (who operates the infrastructure and detects the breach) and the implementing NGO (who is the Data Fiduciary legally responsible for notification).

**Gap:** No documented process, no assigned owner, no defined escalation chain.

**Action:** Define and document:
- How Samanvay detects and classifies a breach
- SLA for Samanvay to notify the NGO (must be short enough to support the NGO's immediate preliminary Board notification obligation under Rule 7(2)(a))
- Who within the NGO is responsible for the preliminary Board notification (without delay) and the detailed follow-up (within 72 hours)
- Template for beneficiary notification (required to be in plain language per Rule 7(1))
- This process must be reflected in the Samanvay contract (see contract requirements file — to be created)

---

### M7 — Security obligations in Samanvay contract
**Rule 6(f):** *"appropriate provision in the contract entered into between such Data Fiduciary and such a Data Processor...for taking reasonable security safeguards"*

The existing contract with Samanvay includes an NDA. This does not satisfy Rule 6(f), which requires the contract to specifically include security safeguard obligations consistent with Rule 6(a)–(g).

**Gap:** Current contract does not bind Samanvay to DPDP-specific security requirements.

**Action:** Update the Samanvay contract to include DPDP Rule 6 security obligations. (Detailed in the forthcoming contracts file.)

---

### M8 — User revocation SOP for lost/stolen devices
**Rule 6(b):** Access controls on computer resources.

Field workers use personal phones with no MDM. Remote wipe is not possible. When a device is lost or stolen, the Realm database (which may contain unsynced beneficiary data) remains on the device. The only mitigation available is user account revocation.

**Gap:** No documented standard operating procedure (SOP) for device loss — no defined response time or escalation path.

**Action:** Document and enforce a device-loss SOP: NGO must revoke the user account within [X hours] of a field worker reporting a lost/stolen device. Train NGO supervisors on this process. Consider adding Realm encryption enforcement (M1) as the paired technical control.

---

## SHOULD HAVE
*Not explicitly mandated as specific line items but required to demonstrate "reasonable security safeguards" (Rule 6(g)) and good-faith compliance. Absence creates legal and operational risk.*

---

### S1 — Breach detection / alerting on access logs
**Rule 6(c)** requires logs for "detection of unauthorised access, its investigation and remediation."

Logs alone don't detect breaches — active monitoring does. Currently no automated alerting is confirmed on Cloudwatch or NewRelic for anomalous access patterns.

**Action:** Implement alerts for: bulk export by a single user in a short window, repeated failed login attempts, access from unusual geographies or hours, and access to a disproportionately large number of beneficiary records.

---

### S2 — Periodic security audits
**Rule 6(g):** *"appropriate technical and organisational measures to ensure effective observance of security safeguards."*

Security audits are currently "on demand." A single point-in-time audit does not constitute ongoing effective observance.

**Action:** Move to annual security audits covering both Android app and web/server components. Audit reports should be available to NGO partners on request.

---

### S3 — Field worker device loss notification requirement for NGOs
Complementary to M8. NGOs should be contractually required to notify Samanvay when a field worker device is lost or stolen, to allow timely user revocation and logging of the event as a potential data incident.

**Action:** Add to NGO onboarding documentation and Samanvay terms of service.

---

### S4 — Data minimisation controls on Android sync
The Android app syncs all data for a field worker's catchment to the Realm database. In a lost/stolen device scenario, all locally-synced beneficiary data for that catchment is exposed.

**Action:** Evaluate whether the sync scope can be narrowed — e.g., sync only records accessed within the last N days, or limit the number of records cached locally.

---

### S5 — Session timeout for Data Entry App (web)
JWT tokens have a 1-hour expiry. However, on the browser-based Data Entry App, if a field worker shares a device (common given personal phone usage), a session left open exposes all accessible data.

**Action:** Enforce session timeout on browser inactivity and terminate sessions on tab/window close for the web app.

---

### S6 — Defined process for ETL/Integration Server data flows
The Integration Server connects Avni to external systems. Any external transmission of personal data creates a data processor relationship requiring a contract and security controls.

**Action:** Document all external systems connected via the Integration Server, classify whether personal data is transmitted, and ensure data processing agreements are in place for each.

---

## COULD HAVE
*Good practice, aligned with DPDP spirit, but not immediately mandated. Implement as maturity grows or when becoming a Significant Data Fiduciary.*

---

### C1 — Pseudonymisation / tokenisation of beneficiary identifiers
**Rule 6(a)** mentions "use of virtual tokens mapped to that personal data" as an example of appropriate data security. Replacing beneficiary names/phone numbers with internal tokens in logs and exports would limit exposure in a breach.

---

### C2 — Data Protection Impact Assessment (DPIA)
**DPDP Rules 2025, Rule 13(1):** Mandatory only for **Significant Data Fiduciaries** (notified by the Central Government). Avni implementing NGOs are unlikely to qualify initially, but conducting a DPIA is a recognised best practice and demonstrates proactive compliance posture.

---

### C3 — Automated data erasure workflows triggered by consent withdrawal
Currently, voiding a record is a manual action that does not trigger erasure (see `consent.md` gap). An automated pipeline — void → scheduled erasure → Samanvay notification → S3 deletion — would bring the erasure process fully in line with DPDP Act Section 8(7).

---

### C4 — In-app consent withdrawal mechanism
Currently consent withdrawal requires a field worker to physically visit and void the record. An in-app request mechanism (even a simple form submission) would make withdrawal more directly accessible to beneficiaries, strengthening the "ease of withdrawal" requirement under DPDP Act Section 6(4).

---

## Summary Table

| ID | Requirement | Priority | DPDP Basis | Current Status |
|----|-------------|:--------:|------------|----------------|
| M1 | Mandatory mobile (Realm) encryption | MUST | Rule 6(a) | Optional per org — gap |
| M2 | Application-level access audit logs | MUST | Rule 6(c) | Not confirmed — gap |
| M3 | 1-year log retention (Cloudwatch) | MUST | Rule 6(e), Rule 8(3) | Unconfirmed — needs audit |
| M4 | Restrict PII report creation in BI layer | MUST | Rule 6(b) | Possible but not enforced — gap |
| M5 | Controls on bulk PII exports | MUST | Rule 6(a) | No controls — gap |
| M6 | Breach notification process (72hr Board) | MUST | Rule 7 | Not documented — gap |
| M7 | Security obligations in Samanvay contract | MUST | Rule 6(f) | NDA only — gap |
| M8 | Device loss/revocation SOP | MUST | Rule 6(b) | Not documented — gap |
| S1 | Breach detection / access anomaly alerting | SHOULD | Rule 6(c) | Not confirmed |
| S2 | Periodic security audits (annual) | SHOULD | Rule 6(g) | On demand only |
| S3 | NGO obligation to report device loss | SHOULD | Rule 6(b) | Not in place |
| S4 | Narrowed Android sync scope | SHOULD | Rule 6(a) | Full catchment synced |
| S5 | Web app session timeout on inactivity | SHOULD | Rule 6(b) | Not confirmed |
| S6 | External integration data flow documentation | SHOULD | Rule 6(f) | Not documented |
| C1 | Pseudonymisation / tokenisation | COULD | Rule 6(a) | Not in place |
| C2 | Data Protection Impact Assessment | COULD | Rule 13 | Not conducted |
| C3 | Automated erasure pipeline on void | COULD | Act S.8(7) | Not in place |
| C4 | In-app consent withdrawal mechanism | COULD | Act S.6(4) | Not in place |

---

## Key Statutory References

| Document | Section | Requirement |
|----------|---------|-------------|
| DPDP Rules 2025 | Rule 6(a) | Encryption, obfuscation, masking of personal data |
| DPDP Rules 2025 | Rule 6(b) | Access controls on all computer resources |
| DPDP Rules 2025 | Rule 6(c) | Logs and monitoring for detecting unauthorised access to personal data |
| DPDP Rules 2025 | Rule 6(d) | Backups and continuity measures |
| DPDP Rules 2025 | Rule 6(e) | Minimum 1-year log retention |
| DPDP Rules 2025 | Rule 6(f) | Security obligations must be in the Data Processor contract |
| DPDP Rules 2025 | Rule 6(g) | Technical and organisational measures for ongoing compliance |
| DPDP Rules 2025 | Rule 7 | Breach notification — without delay to Data Principals, within 72 hours to Board |
| DPDP Rules 2025 | Rule 8(3) | Minimum 1-year retention of processing logs |
| DPDP Act 2023 | Section 6(4) | Ease of consent withdrawal must match ease of giving |
| DPDP Act 2023 | Section 8(7) | Erasure of personal data upon consent withdrawal |
