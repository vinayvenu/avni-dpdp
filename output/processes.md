# DPDP Operational Processes — Samanvay

This document defines the operational processes that Samanvay must have in place for DPDP compliance. Each process is either new (must be created) or existing (must be documented and formalised).

**Deadline:** All processes must be documented and operational before **13 May 2027**.

---

## P1 — Breach Response SoP

**Status:** Does not exist. Must be created from scratch.

**Legal basis:** Act S.8(6); Rules Rule 7(1), Rule 7(2)(a), Rule 7(2)(b); Contract G.1(e), G.2(h)

**Why this matters:** Rule 7 imposes a two-stage Board notification with the first stage being "without delay." Without a defined process, the time spent figuring out who does what during an actual breach directly eats into the NGO's notification window.

### Process

**Stage 1 — Detection and Classification (Samanvay internal)**

1. Any Samanvay team member who suspects a personal data breach (unauthorised access, data exposure, data loss, system compromise) reports it immediately to the **Samanvay Breach Lead** (to be designated — name and backup to be documented).
2. The Breach Lead assesses whether the event qualifies as a "personal data breach" under Act S.2(u): *any unauthorised processing, accidental disclosure, acquisition, sharing, use, alteration, destruction or loss of access to personal data that compromises confidentiality, integrity or availability.*
3. If **yes** or **uncertain**, proceed to Stage 2 immediately. Do not wait for full investigation.
4. If **no** (e.g., infrastructure event with no personal data exposure), document the assessment and close.

**Open question:** Who is the Breach Lead? Is there a backup? This must be a named individual, not a role.

**Stage 2 — NGO Notification (Samanvay → NGO, within 24 hours)**

5. The Breach Lead notifies the affected NGO(s) within **24 hours** of becoming aware. Notification must include:
   - Description of the breach (nature, extent, timing)
   - Personal data categories affected
   - Initial assessment of impact
   - Measures being taken to contain and remediate
6. Notification is sent to the NGO's **designated DPDP contact** (to be collected from each NGO — see open question below).
7. Notification channel: email to designated contact + Freshdesk ticket for tracking.

**Open question:** Does Samanvay have a designated DPDP contact for each NGO? This must be collected and maintained.

**Stage 3 — Board and Data Principal Notification (NGO responsibility)**

8. The NGO is solely responsible for:
   - **Preliminary Board notification** — "without delay" upon becoming aware (Rule 7(2)(a)). This may mean within hours, not days.
   - **Detailed Board notification** — within 72 hours of becoming aware (Rule 7(2)(b)).
   - **Data Principal notification** — without delay, in concise and plain language (Rule 7(1)).
9. Samanvay's role in Stage 3: provide facts and technical details as requested by the NGO. Samanvay does **not** file with the Board on the NGO's behalf.

**Open question:** How does the NGO file with the Board? The Board is a digital office — the filing mechanism (portal, form, email) will be published by the Board. This should be tracked and communicated to NGOs once available.

**Stage 4 — Investigation and Remediation (Samanvay)**

10. The Breach Lead conducts a full investigation and documents:
    - Root cause
    - Full scope of affected data and Data Principals
    - Remedial measures taken to prevent recurrence
11. Investigation report is shared with the NGO within **7 days** of the initial notification (or earlier if required by the NGO for its Board submission).
12. All breach records (detection, classification, notification, investigation, remediation) are retained for a minimum of **3 years**.

**Open questions for SoP completion:**
- Who is the Breach Lead (name + backup)?
- What is the designated DPDP contact at each NGO?
- What is the Board's filing mechanism?
- Should Samanvay provide a template to NGOs for the Board notification?
- Should Samanvay assist NGOs in notifying beneficiaries (e.g., providing affected beneficiary lists with contact details)?

---

## P2 — Erasure Fulfilment

**Status:** Freshdesk ticket mechanism exists. Process needs to be documented with DPDP-specific steps and SLA tracking.

**Legal basis:** Act S.8(7)(a), S.8(7)(b), S.12(3); Contract G.1(f); Rules Rule 8(3)

### Process

1. NGO raises a **Freshdesk ticket** with subject "Erasure Request" specifying:
   - Beneficiary identifier(s) (Avni subject UUID or equivalent)
   - Reason: consent withdrawal, Data Principal erasure request (S.12), or purpose expiry
   - Any legal hold or retention exception the NGO is aware of
2. Samanvay acknowledges the ticket within **2 business days**.
3. Samanvay executes erasure in the following order:

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Erase personal data fields from production database (retain audit log of erasure event) | Within 7 days of ticket |
| 2 | Erase associated files and images from S3 | Within 7 days of ticket |
| 3 | Confirm that beneficiary data will be cleared from field worker devices on next sync | Within 7 days of ticket |
| 4 | PITR backups containing the data expire naturally | 35 days from production erasure |
| 5 | Mark erasure complete and send written confirmation to NGO | After 35-day backup window |

4. The **30-day contractual SLA** is measured from ticket receipt to production erasure completion (Steps 1–3). Backup expiry (Step 4) falls within the window.
5. If a legal hold prevents erasure (e.g., data involved in an ongoing breach investigation per Rule 6(1)(e)), Samanvay informs the NGO within the acknowledgement period and documents the reason. Erasure resumes when the hold is lifted.
6. Written confirmation (Step 5) is sent via the same Freshdesk ticket and email to the NGO's designated contact.
7. Samanvay maintains a log of all erasure requests: NGO name, ticket number, date received, date production erasure completed, date backup window passed, date confirmation sent. This log is compliance evidence under Rule 6(1)(f).

**What the platform handles automatically (once F7/F8 are built):**
- Consent withdrawal and void events in Avni trigger the erasure workflow within the platform — production DB erasure, S3 deletion, and Realm cleanup on next sync happen through the application.
- The Freshdesk ticket process described above is for cases where the NGO needs to issue a **manual written instruction** outside the platform workflow (e.g., bulk erasure, edge cases, or before the platform features are live).

---

## P3 — Data Principal Rights Handling

**Status:** Will be handled through platform features (F8, F10). Light process documentation needed for the field-to-platform path.

**Legal basis:** Act S.11(1), S.12(1)–(3); Rules Rule 14

### Process

This is primarily the **NGO's responsibility** as Data Fiduciary. Samanvay's role is to provide the platform tools.

1. A beneficiary makes a request (access, correction, erasure) to a **field worker** during a visit, or to the NGO through any other channel.
2. The field worker or NGO admin logs the request in Avni using the **Data Principal Rights Request Log (F10)**.
3. For **access requests** (S.11): the field worker or NGO admin retrieves the beneficiary's data from Avni and provides a summary to the beneficiary.
4. For **correction requests** (S.12(2)): the field worker updates the record in Avni directly.
5. For **erasure requests** (S.12(3)):
   - If the consent workflow (F7) is live: the field worker initiates consent withdrawal through the platform, which triggers the erasure workflow automatically.
   - If the consent workflow is not yet live: the NGO raises a Freshdesk ticket per P2 above.
6. The NGO tracks resolution through F10 and responds to the beneficiary.

**Samanvay does not interact with beneficiaries directly.** All Data Principal requests flow through the NGO.

---

## P4 — Device Loss Response

**Status:** Will be handled through Freshdesk. Process needs to be documented.

**Legal basis:** Rules Rule 6(1)(b); Contract G.2(c)

### Process

1. Field worker reports device loss/theft to their **NGO supervisor** immediately.
2. NGO supervisor raises a **Freshdesk ticket** with subject "Device Loss — User Revocation" specifying:
   - Field worker name and Avni user ID
   - Date and time of loss/suspected theft
   - Whether the device had Realm encryption enabled
   - Whether any unsynced data was on the device
3. Samanvay revokes the user account within **24 hours** of receiving the ticket.
4. Samanvay logs the event as a potential data incident.
5. **Breach assessment:** If the device had Realm encryption enabled, the risk of personal data exposure is low (encrypted at rest). If encryption was **not** enabled, this is a potential personal data breach and must be escalated through **P1 (Breach Response)**. The Breach Lead makes the classification decision.
6. Samanvay confirms revocation to the NGO via the Freshdesk ticket.

**The contractual SLA is 48 hours** (NGO must request revocation within 48 hours of becoming aware). Samanvay should act faster — target 24 hours from ticket receipt.

---

## P5 — Sub-Processor Change Notification

**Status:** Does not exist. Must be created.

**Legal basis:** Contract G.1(g); Rules Rule 6(1)(f)

### Process

1. When Samanvay plans to add or materially change a sub-processor that handles personal data (e.g., changing cloud provider, adding a monitoring service that accesses production data), the **Samanvay operations lead** initiates the notification process.
2. Samanvay sends written notification to **all active NGO customers** at least **30 days** before the change takes effect. Notification must include:
   - Name of the new/changed sub-processor
   - Nature of processing the sub-processor will perform
   - Location of processing (country/region)
   - Date the change will take effect
3. Notification is sent via email to each NGO's designated contact and recorded in a tracking log.
4. If an NGO objects to the change, the NGO must raise the objection in writing within the 30-day window. Samanvay and the NGO will discuss alternatives. If no resolution is reached, the NGO's options are governed by the termination provisions of the contract.
5. If no objection is received within 30 days, the change proceeds.
6. Samanvay maintains a log of all sub-processor change notifications: date sent, sub-processor details, NGO responses.

**Current sub-processors:** Amazon Web Services (AWS) — cloud infrastructure and storage, Mumbai region. This is documented in the contract.

---

## P6 — Annual Security Review

**Status:** Does not exist. Must be created.

**Legal basis:** Rules Rule 6(1)(g); Contract G.1(i)

### Process

1. **Annually**, or upon written request from an NGO (maximum once per year per NGO), Samanvay prepares a security summary covering:
   - Current encryption standards (at rest, in transit)
   - Access control measures
   - Log retention status (confirmation of ≥1 year)
   - Backup status (PITR, retention period, encryption)
   - Sub-processor list
   - Summary of any security audits or penetration tests conducted in the period
   - Summary of any personal data breaches in the period and remediation status
   - Any material changes to security posture since last review
2. The summary is prepared by the **Samanvay infrastructure/security lead** (to be designated).
3. If an NGO requests the summary, Samanvay responds within **30 days** (per contract).
4. If Samanvay conducts a third-party security audit or penetration test, the summary or report (with sensitive details redacted if necessary) is made available to requesting NGOs.
5. Samanvay maintains a log of all security review requests and responses.

**Open questions:**
- Who within Samanvay is responsible for preparing the annual summary?
- Will Samanvay conduct annual third-party security audits proactively, or only on demand? (security_requirements.md recommends annual audits — S2.)
- What format — a structured questionnaire (e.g., SIG Lite), a narrative report, or a simple checklist?

---

## P7 — Addendum Tracking for Existing Customers

**Status:** Process is understood informally (operations team owns, account manager escalates). Needs to be written down and tracked.

**Legal basis:** Rules Rule 6(1)(f); dpdp_addendum.md operational notes

### Process

1. The **operations team** owns outreach to all existing customers for addendum signing.
2. The operations team maintains a tracking log with: customer name, original contract date, addendum sent date, addendum signed date, follow-up dates.
3. Priority order for outreach (per dpdp_addendum.md):
   - **Priority 1:** Customers whose contracts expire after May 2027 and will not naturally renew before then — the addendum is the only path to compliance.
   - **Priority 2:** Customers renewing between now and May 2027 — sign addendum alongside renewal, or receive updated H&S template.
   - **Priority 3:** Customers renewing after May 2027 — will receive updated H&S template at renewal, but addendum covers the gap.
4. If a customer has not signed within **30 days** of the addendum being sent, the **account manager** follows up.
5. If a customer has not signed within **60 days**, the account manager escalates to the Samanvay director.
6. If a customer has not signed by **1 March 2027** (10 weeks before enforcement), the director directly contacts the customer's leadership.
7. **All customers must have signed before 13 May 2027.** An unsigned addendum on that date means the DF–DP relationship is non-compliant under Rule 6(1)(f) regardless of what Samanvay does operationally.
8. The tracking log itself is compliance evidence and must be retained.

---

## P8 — Ongoing Compliance Monitoring

**Status:** Does not exist. Must be created.

**Legal basis:** Rules Rule 6(1)(g); Act S.8(4)

### Process

**Quarterly internal review:**

1. Every quarter, the designated **Samanvay compliance owner** (to be assigned) reviews:
   - Log retention: are all CloudWatch log groups set to ≥1 year?
   - Encryption: is Realm encryption enabled for all active organisations? Are any exceptions documented?
   - Access controls: are BI report-creation restrictions in place for all tenants?
   - Bulk export controls: are export logging and role restrictions operational?
   - Sub-processor list: any changes since last review?
   - Erasure log: are all erasure requests within SLA? Any overdue?
   - Addendum tracking: any unsigned customers? (Until all are signed)
2. Findings are documented in a brief internal checklist (not a formal report). Any gaps are raised as Freshdesk tickets or internal tasks.

**Annual review:**

3. Once per year (aligned with P6 — Annual Security Review), the compliance owner also reviews:
   - Whether any new DPDP notifications have been issued (Third Schedule publication, SDF designations, new exemptions, Board guidance)
   - Whether contract templates need updating
   - Whether any platform features need changes based on regulatory developments
   - Whether the breach response SoP (P1) needs updating based on any incidents in the period
4. The annual review is documented and shared with the Samanvay director.

**Regulatory monitoring:**

5. The compliance owner subscribes to / periodically checks:
   - MeitY gazette notifications (for new DPDP rules, schedules, and amendments)
   - Data Protection Board of India website (for guidance, registration requirements, filing mechanisms)
   - Legal news sources covering DPDP developments
6. Any material regulatory change is flagged to the Samanvay director within **1 week** of publication, with an assessment of impact on Samanvay's processes and contracts.

**Open questions:**
- Who is the compliance owner? Is this a dedicated role or an addition to an existing person's responsibilities?
- What is the cadence for the first year (May 2027–May 2028) — should quarterly reviews be monthly during the initial enforcement period?

---

## Processes That Are the NGO's Responsibility (Not Samanvay's)

The following are operational obligations of the NGO as Data Fiduciary. Samanvay does not own these processes but should communicate them clearly to NGOs through the contract, addendum, and customer DPDP note.

| Process | Owner | Notes |
|---------|-------|-------|
| **Consent collection training** — training field workers on the audio/signed form consent flow | NGO | The notice text, language, and field worker training are entirely the NGO's responsibility. Avni provides the platform mechanism (F2, F3, F4). |
| **Notice text management** — drafting, translating, and version-controlling the DPDP notice | NGO | The notice is not provided by Avni. Each NGO must draft a notice appropriate to its programs. Avni stores the notice version identifier linked to each consent record. |
| **Retrospective notice campaign** — planning and executing S.5(2) notice delivery to existing beneficiaries | NGO | This is a field campaign. Avni provides tracking (F6) and reporting (R2). The planning, prioritisation, and execution are the NGO's operational responsibility. |
| **Beneficiary notification on breach** — notifying affected Data Principals per Rule 7(1) | NGO | Samanvay provides the facts (P1). The NGO decides how to reach beneficiaries — field worker revisit, phone call, etc. |
| **Publishing DPO/contact info** — prominently on website per Act S.8(9), Rule 9 | NGO | Each NGO must publish its own contact. |
| **Grievance redressal mechanism** — per Act S.8(10), S.13, Rule 14(3) | NGO | Avni provides F10 (rights request log) as a tracking tool. The NGO must establish and publicise the mechanism. |

---

## Summary

| ID | Process | Status | Owner | Priority |
|----|---------|--------|-------|----------|
| **P1** | Breach Response SoP | Must be created | Samanvay (Breach Lead — to be designated) | High — must be ready before May 2027 |
| **P2** | Erasure Fulfilment | Freshdesk exists; needs DPDP documentation | Samanvay operations | Medium — document alongside F7/F8 delivery |
| **P3** | Data Principal Rights Handling | Platform features handle it; light documentation | NGO (primary), Samanvay (platform) | Medium — document alongside F10 delivery |
| **P4** | Device Loss Response | Freshdesk exists; needs documentation | NGO (reports), Samanvay (revokes) | Medium — document and communicate to NGOs |
| **P5** | Sub-Processor Change Notification | Must be created | Samanvay operations | Low — only triggered by infra changes |
| **P6** | Annual Security Review | Must be created | Samanvay (security lead — to be designated) | Medium — first review due within 12 months of May 2027 |
| **P7** | Addendum Tracking | Informally understood; needs documentation | Samanvay operations (account manager escalation) | High — outreach should begin now |
| **P8** | Ongoing Compliance Monitoring | Must be created | Samanvay (compliance owner — to be designated) | Medium — quarterly reviews start Q1 2027 |
