# DPDP-Required Changes: Hosting & Support Contract Template

This document identifies every change required to the Hosting & Support Contract Template to meet DPDP obligations. The H&S contract is signed at annual renewal after the first year. It does not include an NDA — the NDA from the original Service & Support Contract remains operative (and should be confirmed as perpetual per the changes in `contract_changes.md`).

**Legal basis for all changes:** DPDP Act 2023 and DPDP Rules 2025, effective 13 May 2027.

---

## 1. Additional Terms — Data Privacy

### Current wording
> *"[Customer Name] undertakes to comply with the requirements of the roles of Data Fiduciary and Consent Manager as provided in the Digital Personal Data Protection Act, 2023 while Samanvay undertakes to comply with the requirements of a Data Processor as defined in the act."*

### Problems
Same as the Service & Support Contract: "Consent Manager" is incorrect for the NGO, and Samanvay's Data Processor role is named without any corresponding obligations.

Additionally, the H&S contract has no NDA appendix and does not reference the original contract's NDA. Given the H&S contract stands as a renewed annual agreement, it should explicitly confirm the continuing legal relationship and data processing arrangement.

### Suggested replacement

> **Data Privacy and Data Processing**
>
> **1.** The parties confirm that the confidentiality and non-disclosure obligations under the NDA (Appendix A of the original Service & Support Contract dated [Original Contract Date]) remain in full force and effect and are not affected by the signing of this Hosting & Support Contract.
>
> **2.** [Customer Name] is the **Data Fiduciary** as defined under Section 2(i) of the Digital Personal Data Protection Act, 2023 (the "Act") and undertakes to comply with all obligations of a Data Fiduciary under the Act and the Digital Personal Data Protection Rules, 2025 (the "Rules"), including obligations relating to notice, consent, Data Principal rights, and data erasure.
>
> **3.** [Customer Name] may, at its discretion, appoint or engage a **Consent Manager** as defined under Section 2(g) of the Act to facilitate consent collection and management on its behalf. Samanvay's obligations under this contract are unaffected by whether or not [Customer Name] uses a Consent Manager.
>
> **4.** Samanvay Technologies Private Limited is the **Data Processor** as defined under Section 2(k) of the Act and shall process personal data only on the documented instructions of [Customer Name] and solely for the purposes of providing the hosting and support services described in this contract. Samanvay's data processing obligations are set out in the Data Security section below.

---

## 2. Additional Terms — Data Security

### Current wording (Samanvay obligations)
> *(a) All data stored encrypted on disk; (b) data in transit encrypted via TLS; (c) only authorised users allowed access; (d) audit details including created/modified dates stored for all entities.*

### Problems
Identical to the Service & Support Contract — obligations are too narrow for DPDP Rule 6 compliance. The H&S contract additionally lacks:
- Breach notification SLA (critical — by the time the H&S contract is operative, May 2027 enforcement may be live)
- Erasure obligation on instruction
- Log retention commitment
- Sub-processor transparency

### Suggested replacement

> **Data Security**
>
> **Samanvay's obligations as Data Processor**
>
> Samanvay will, in accordance with DPDP Rules 2025, Rule 6:
>
> (a) **Encryption:** Store all personal data encrypted at rest using AES-256 and encrypt all data in transit outside the data centre using TLS 1.2 or above.
>
> (b) **Access controls:** Ensure that access to personal data is restricted to authorised Samanvay personnel only, on a need-to-know basis. All Samanvay personnel with access to production data remain bound by the NDA referenced above.
>
> (c) **Access logs:** Maintain application-level logs recording access to personal data, including at minimum: timestamp, user identifier, and action performed. These logs shall be retained for a minimum of **one year** from the date of each log entry, stored in a tamper-evident manner.
>
> (d) **Backups and continuity:** Maintain Point-in-Time Recovery (PITR) backups for a minimum of 35 days, encrypted to the same standard as primary data.
>
> (e) **Breach notification:** On becoming aware of any personal data breach, Samanvay shall notify [Customer Name] **within 24 hours** of becoming aware, providing: a description of the breach including its nature, extent and timing; the personal data affected; initial assessment of impact; and measures being taken to contain and remediate. This timeline is designed to allow [Customer Name] to fulfil its obligations under DPDP Rules 2025, Rule 7(2), which requires: (i) a preliminary notification to the Data Protection Board of India *without delay* upon becoming aware of the breach (Rule 7(2)(a)); and (ii) a detailed follow-up notification to the Board within 72 hours of becoming aware (Rule 7(2)(b)). **Note:** The initial Board notification under Rule 7(2)(a) must be made "without delay" — this may be interpreted as within hours, not days. [Customer Name] should not wait for the 72-hour deadline before making initial contact with the Board.
>
> (f) **Erasure on instruction:** On written instruction from [Customer Name], Samanvay shall erase specified personal data from all production systems, backups, and associated storage (including S3) within a reasonable time not exceeding **30 days**, unless retention is required under applicable law. Samanvay shall confirm erasure in writing to [Customer Name] upon completion. This obligation covers erasure requests arising from withdrawal of consent by a Data Principal under Section 6(4) of the Act, as well as requests under Section 12 (right to erasure).
>
> (g) **Sub-processors:** Samanvay currently uses the following sub-processors that may handle personal data: Amazon Web Services (AWS) — cloud infrastructure and storage, Mumbai region. Samanvay shall notify [Customer Name] of any addition or change to sub-processors at least 30 days in advance.
>
> (h) **Data residency:** All personal data shall be stored and processed within AWS data centres in the Mumbai (ap-south-1) region and shall not be transferred outside India without prior written consent of [Customer Name].
>
> (i) **Audit rights:** [Customer Name] may request, no more than once per year, a written summary of Samanvay's security measures or the results of any security audit conducted by Samanvay. Samanvay shall respond within 30 days.
>
> (j) **Scope of Samanvay's obligations:** Samanvay's obligations as Data Processor under this contract extend to personal data stored and processed on Samanvay's own infrastructure (AWS Mumbai cloud, including databases, S3, and backups). Samanvay is not responsible for the security of personal data on field worker devices (including the Realm database on Android devices), which are operated by and under the control of [Customer Name]. [Customer Name] remains solely responsible for implementing appropriate security controls on all devices and systems outside Samanvay's infrastructure.
>
> (k) **Integration Server:** Where [Customer Name] uses the Avni Integration Server to connect Avni to external systems not operated by Samanvay, Samanvay's data protection obligations under this contract extend only to personal data within Samanvay's own infrastructure. Samanvay is not responsible for the data protection practices, security, or compliance of any external system receiving data via the Integration Server. [Customer Name] is responsible for ensuring that any external system to which personal data is transmitted via the Integration Server complies with applicable law, including the Act, and for executing any required data processing agreements with the operators of those external systems.
>
> **[Customer Name]'s obligations as Data Fiduciary**
>
> [Customer Name] will ensure that:
>
> (a) **Mobile encryption:** The AES-256 encryption feature for the Avni Android application (Realm database) is enabled for all field workers. [Customer Name] acknowledges that operating the app without encryption enabled may constitute a breach of DPDP Rules 2025, Rule 6(a). Samanvay shall bear no liability for any loss, breach, or unauthorised access to personal data stored on field worker devices where [Customer Name] has not enabled the encryption feature made available by Samanvay.
>
> (b) **User credentials:** User IDs are not shared between individuals. Passwords meet minimum complexity requirements.
>
> (c) **Device loss:** If a field worker's device is lost or stolen, [Customer Name] shall notify Samanvay and request revocation of the affected user account within **48 hours** of becoming aware of the loss.
>
> (d) **Reporting and BI access:** Report-writing access in Metabase/Superset is restricted to authorised personnel only. [Customer Name] shall request Samanvay to configure report-creation restrictions appropriate to its deployment.
>
> (e) **Bulk data exports:** PII downloaded from the system shall be shared only with authorised personnel, handled in accordance with the Act, and deleted from personal devices when no longer required.
>
> (f) **Consent management:** [Customer Name] is solely responsible for obtaining, recording, and managing consent from Data Principals in accordance with the Act, including the obligation under Section 5(2) of the Act to issue retrospective notices to Data Principals who gave consent before the commencement of the Act. **Note:** Section 5(2) applies only where consent was previously given — it does not cover Data Principals whose data was collected without any prior consent. For those individuals, Section 5(2) does not apply; fresh DPDP-compliant consent must be obtained before 13 May 2027, or processing must be justified under Section 7 of the Act.
>
> (g) **Data Principal rights:** [Customer Name] is responsible for receiving and processing requests from Data Principals for access, correction, and erasure of their personal data. Where erasure requires Samanvay to delete data, [Customer Name] shall issue a written erasure instruction to Samanvay as described in (f) above.
>
> (h) **Breach notification:** [Customer Name] is solely responsible for notifying affected Data Principals and the Data Protection Board of India of any personal data breach in accordance with DPDP Rules 2025, Rule 7. Samanvay's obligation is limited to notifying [Customer Name] as described above.
>
> (i) **Unrooted devices:** Phones used for field work must not be rooted or jailbroken.
>
> **Remedies for non-compliance**
>
> In case of non-compliance with [Customer Name]'s obligations above, Samanvay has the right to suspend or terminate access or usage rights of the non-compliant users and/or remove non-compliant information.

---

## 3. Addition: Statutory Reference Update

The H&S contract currently contains no reference to applicable data protection law beyond the brief Data Privacy clause. Add the following at the end of the Additional Terms section:

> **Applicable Law**
>
> This contract and the parties' data processing obligations shall be governed by and construed in accordance with the laws of India, including the Digital Personal Data Protection Act, 2023 and the Digital Personal Data Protection Rules, 2025, as amended from time to time.

---

## Key Difference from Service & Support Contract

The H&S contract is the operative instrument for all customers who are past their first year. By the time DPDP enforcement begins on **13 May 2027**, most established Avni customers will be on H&S contracts. This makes the H&S contract the higher-priority document for DPDP compliance — the updated clauses above must be in all H&S renewals signed after May 2027, and ideally in renewals signed before that date as well.

Additionally, the H&S contract should reference the retrospective notice obligation (G.2(f) above) because by renewal time, the NGO should already be executing its Section 5(2) notice delivery to existing beneficiaries.

---

## Summary of Changes

| Section | Change Type | DPDP Basis |
|---------|-------------|------------|
| Data Privacy | Replace: fix terminology (Data Fiduciary, Data Processor, optional Consent Manager); add NDA continuity reference | Act S.2(g), S.2(i), S.2(k) |
| Data Security — Samanvay | Replace/expand: add breach notification (24hr), erasure (30 days), 1-yr log retention, sub-processors, audit rights, data residency | Rules 6(a)–(g), Rule 7, Act S.8(7)(b) |
| Data Security — Samanvay (j) | Add: scope limitation — Samanvay's obligations extend only to its own infrastructure | Rule 6(a), general principle |
| Data Security — Samanvay (k) | Add: Integration Server — Samanvay not responsible for external systems; NGO responsible for compliance of connected systems | Rule 6(f), Act S.8(2) |
| Data Security — Customer (a) | Add: Samanvay bears no liability for device-side breaches where NGO has not enabled available encryption | Rule 6(a), Act S.8(5) |
| Data Security — Customer | Replace/expand: add mobile encryption, device loss SOP (48hr), BI restriction, export controls, consent + retrospective notice responsibility (S.5(2) applies only where consent was previously given), Data Principal rights | Rules 6(a), 6(b), Act S.5(2), S.6, S.7, S.8(7), S.12 |
| Applicable Law | Add: reference to DPDP Act 2023 and Rules 2025 | General compliance obligation under the Act |
