# DPDP-Required Changes: Service & Support Contract Template

This document identifies every change required to the Service & Support Contract Template to meet DPDP obligations. Changes are organised by existing section. Suggested replacement or additional wording is provided for each.

**Legal basis for all changes:** DPDP Act 2023 and DPDP Rules 2025, effective 13 May 2027.

---

## 1. Section F — Data Privacy

### Current wording
> *"[Customer Name] undertakes to comply with the requirements of the roles of Data Fiduciary and Consent Manager as provided in the Digital Personal Data Protection Act, 2023 while Samanvay undertakes to comply with the requirements of a Data Processor as defined in the act."*

### Problems
- "Consent Manager" is a specific registered entity under Section 2(g) of the Act — a third-party platform that manages consent on behalf of Data Principals. The NGO is not a Consent Manager; it is the Data Fiduciary.
- Samanvay's role as Data Processor is named but carries no corresponding obligations in this clause.
- No reference to what Data Processor obligations actually entail.

### Suggested replacement
> **F. Data Privacy and Data Processing**
>
> **F.1** [Customer Name] is the **Data Fiduciary** as defined under Section 2(i) of the Digital Personal Data Protection Act, 2023 (the "Act") and undertakes to comply with all obligations of a Data Fiduciary under the Act and the Digital Personal Data Protection Rules, 2025 (the "Rules"), including obligations relating to notice, consent, Data Principal rights, and data erasure.
>
> **F.2** [Customer Name] may, at its discretion, appoint or engage a **Consent Manager** as defined under Section 2(g) of the Act to facilitate consent collection and management on its behalf. Samanvay's obligations under this contract are unaffected by whether or not [Customer Name] uses a Consent Manager.
>
> **F.3** Samanvay Technologies Private Limited is the **Data Processor** as defined under Section 2(k) of the Act and shall process personal data only on the documented instructions of [Customer Name] and solely for the purposes described in this contract. Samanvay's obligations as Data Processor are set out in Section G below.

---

## 2. Section G — Data Security

### Current wording (Samanvay obligations)
> *(a) All data will be stored encrypted on disk; (b) data in transit encrypted via TLS; (c) only authorised users will be allowed access; (d) audit details including created/modified dates stored for all entities.*

### Problems
- Obligations are too narrow relative to DPDP Rules 2025, Rule 6(a)–(g).
- No breach notification obligation or timeline.
- No erasure obligation on Samanvay when instructed by the NGO (required under Act Section 8(7)(b)).
- No log retention period specified (Rule 6(e) requires minimum 1 year).
- No application-level access audit log obligation (Rule 6(c)).
- No sub-processor disclosure.
- No audit rights for the customer.

### Suggested replacement

> **G. Data Security**
>
> **G.1 Samanvay's obligations as Data Processor**
>
> Samanvay will, in accordance with DPDP Rules 2025, Rule 6:
>
> (a) **Encryption:** Store all personal data encrypted at rest using AES-256 and encrypt all data in transit outside the data centre using TLS 1.2 or above.
>
> (b) **Access controls:** Ensure that access to personal data is restricted to authorised Samanvay personnel only, on a need-to-know basis. Samanvay personnel with access to production data are bound by the NDA in Appendix A of this contract.
>
> (c) **Access logs:** Maintain application-level logs recording access to personal data, including at minimum: timestamp, user identifier, and action performed. These logs shall be retained for a minimum period of **one year** from the date of each log entry. Logs shall be stored in a tamper-evident manner.
>
> (d) **Backups and continuity:** Maintain Point-in-Time Recovery (PITR) backups for a minimum of 35 days. Backups shall be encrypted to the same standard as primary data.
>
> (e) **Breach notification:** On becoming aware of any personal data breach, Samanvay shall notify [Customer Name] **within 24 hours** of becoming aware, providing: a description of the breach including its nature, extent and timing; the personal data affected; initial assessment of impact; and measures being taken to contain and remediate. This timeline is designed to allow [Customer Name] sufficient time to fulfil its obligations under DPDP Rules 2025, Rule 7(2), which requires: (i) a preliminary notification to the Data Protection Board of India *without delay* upon becoming aware of the breach (Rule 7(2)(a)); and (ii) a detailed follow-up notification to the Board within 72 hours of becoming aware (Rule 7(2)(b)). **Note:** The initial Board notification under Rule 7(2)(a) must be made "without delay" — this may be interpreted as within hours, not days. [Customer Name] should not wait for the 72-hour deadline before making initial contact with the Board.
>
> (f) **Erasure on instruction:** On written instruction from [Customer Name], Samanvay shall erase specified personal data from all production systems, backups, and associated storage (including S3) within a reasonable time not exceeding **30 days**, unless retention is required under applicable law. Samanvay shall confirm erasure in writing to [Customer Name] upon completion.
>
> (g) **Sub-processors:** Samanvay currently uses the following sub-processors that may handle personal data: Amazon Web Services (AWS) — cloud infrastructure and storage, Mumbai region. Samanvay shall notify [Customer Name] of any addition or change to sub-processors at least 30 days in advance.
>
> (h) **Data residency:** All personal data shall be stored and processed within AWS data centres in the Mumbai (ap-south-1) region and shall not be transferred outside India without prior written consent of [Customer Name].
>
> (i) **Audit rights:** [Customer Name] may request, no more than once per year, a written summary of Samanvay's security measures or the results of any security audit conducted by Samanvay. Samanvay shall respond within 30 days.
>
> (j) **Scope of Samanvay's obligations:** Samanvay's obligations as Data Processor under this Section G extend to personal data stored and processed on Samanvay's own infrastructure (AWS Mumbai cloud, including databases, S3, and backups). Samanvay is not responsible for the security of personal data on field worker devices (including the Realm database on Android devices), which are operated by and under the control of [Customer Name]. [Customer Name] remains solely responsible for implementing appropriate security controls on all devices and systems outside Samanvay's infrastructure.
>
> (k) **Integration Server:** Where [Customer Name] uses the Avni Integration Server to connect Avni to external systems not operated by Samanvay, Samanvay's data protection obligations under this contract extend only to personal data within Samanvay's own infrastructure. Samanvay is not responsible for the data protection practices, security, or compliance of any external system receiving data via the Integration Server. [Customer Name] is responsible for ensuring that any external system to which personal data is transmitted via the Integration Server complies with applicable law, including the Act, and for executing any required data processing agreements with the operators of those external systems.
>
> **G.2 [Customer Name]'s obligations as Data Fiduciary**
>
> [Customer Name] will ensure that:
>
> (a) **Mobile encryption:** The AES-256 encryption feature for the Avni Android application (Realm database) is enabled for all field workers before deployment. [Customer Name] acknowledges that operating the Android app without encryption enabled may constitute a breach of DPDP Rules 2025, Rule 6(a). Samanvay shall bear no liability for any loss, breach, or unauthorised access to personal data stored on field worker devices where [Customer Name] has not enabled the encryption feature made available by Samanvay.
>
> (b) **User credentials:** User IDs are not shared between individuals. Passwords meet minimum complexity requirements. Users are trained on credential security.
>
> (c) **Device loss:** If a field worker's device is lost or stolen, [Customer Name] shall notify Samanvay and request revocation of the affected user account within **48 hours** of becoming aware of the loss.
>
> (d) **Reporting and BI access:** Report-writing access in Metabase/Superset is restricted to authorised personnel only. [Customer Name] shall request Samanvay to configure report-creation restrictions appropriate to its deployment before granting BI access to any user.
>
> (e) **Bulk data exports:** PII downloaded from the system in the form of reports or spreadsheets shall be shared only with authorised personnel, handled in accordance with the Act, and deleted from personal devices when no longer required. [Customer Name] shall maintain a log of who downloaded bulk data exports and when.
>
> (f) **Consent management:** [Customer Name] is solely responsible for obtaining, recording, and managing consent from Data Principals in accordance with the Act. Samanvay provides no consent collection mechanism and bears no liability for [Customer Name]'s consent practices.
>
> (g) **Data Principal rights:** [Customer Name] is responsible for receiving and processing requests from Data Principals for access, correction, and erasure of their personal data. Where fulfilment of an erasure request requires Samanvay to delete data, [Customer Name] shall issue a written erasure instruction to Samanvay as described in G.1(f).
>
> (h) **Breach notification:** [Customer Name] is solely responsible for notifying affected Data Principals and the Data Protection Board of India of any personal data breach in accordance with DPDP Rules 2025, Rule 7. Samanvay's obligation is limited to notifying [Customer Name] as described in G.1(e).
>
> (i) **Unrooted devices:** Phones used for field work must not be rooted or jailbroken.
>
> (j) **No unlawful content:** [Customer Name] will not use the platform to host, upload, transmit or share content that violates applicable law.
>
> **G.3 Remedies for non-compliance**
>
> In case of non-compliance with G.2 above, Samanvay has the right to suspend or terminate the access or usage rights of the non-compliant users and/or remove non-compliant information, as the case may be.

---

## 3. Section G — G.4 Grievance and Incident Reporting

### Current wording
> *"Any victim of a cyber security incident can make a complaint either through the Contact Us option on the Samanvay website (https://www.samanvayfoundation.org/about-us#contact-us-1) or through the email linked in the privacy policy of Avni app (hello@samanvayfoundation.org). This will reach the Grievance Officer at Samanvay who will take necessary action within the time stipulated by the IT Guidelines."*

### Problem
This clause references "the IT Guidelines" — i.e., the IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 — but does not reference DPDP Rule 7, which governs breach notification obligations from May 2027 onwards. The clause could create confusion about which obligations apply and which timelines govern.

### Suggested replacement

> **G.4 Grievance and incident reporting**
>
> Any person affected by a data security incident may report it to Samanvay's Grievance Officer at hello@samanvayfoundation.org or through the contact details on the Samanvay website. Samanvay shall acknowledge and address grievances in accordance with the timelines required by applicable law. Samanvay's obligations in respect of personal data breaches are governed by Clause G.1(e) above. [Customer Name]'s obligations to notify affected Data Principals and the Data Protection Board of India of any personal data breach are governed by Clause G.2(h) and DPDP Rules 2025, Rule 7.

---

## 5. Appendix A — NDA: Survival Clause

### Current wording
The NDA has no explicit survival or duration clause. It is tied implicitly to the contract period.

### Problem
If the NDA expires with the contract, there is no ongoing obligation on Samanvay to protect beneficiary data after the contract ends — which conflicts with DPDP data retention and erasure requirements that may extend beyond the contract period.

### Addition
Add the following clause at the end of the NDA, before the signature block:

> **Duration and Survival**
>
> This Agreement shall remain in force **indefinitely** and shall **survive the termination or expiry** of any service, support, or hosting contract between the parties. Obligations of confidentiality with respect to personal data of Data Principals shall continue until such time as all such personal data has been erased or returned in accordance with the "Return and/or Destruction of Confidential Information" clause above or as required by applicable law.

---

## 6. Appendix A — NDA: Update Statutory Reference

### Current wording
> *"To comply with all statutory laws/rules/legislations related to data protection including but not limited to Information Technology Act, 2000 and Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011."*

### Suggested replacement
> *"To comply with all statutory laws, rules, and regulations related to data protection, including but not limited to the Information Technology Act, 2000, the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, the **Digital Personal Data Protection Act, 2023**, and the **Digital Personal Data Protection Rules, 2025**, as amended from time to time."*

---

## 7. Appendix A — NDA: Liability Cap

### Current wording
> *"The Receiving Party agrees to indemnify the Disclosing Party against any and all actual losses, damages, claims, or expenses incurred, or suffered by the Disclosing Party as a result of the Receiving Party's breach of this Agreement, not exceeding the amount of **one lakh rupees or the annual value of the contract, whichever is lower**."*

### Note
This cap is very low. However, note that under the DPDP Act, **[Customer Name] as Data Fiduciary** bears direct regulatory liability to the Data Protection Board (penalties up to ₹250 crore under Section 8(5) read with the Schedule to the Act, enforced through Section 33). Samanvay's contractual indemnity under the NDA is a separate matter from regulatory liability and does not cap [Customer Name]'s exposure to the Board. This cap may be acceptable for the NDA as a bilateral instrument, but [Customer Name] should be aware it does not offset DPDP regulatory risk.

No change required, but recommend adding the following note:

> *"For the avoidance of doubt, this indemnity limit applies only to claims between the parties under this Agreement and does not limit any party's obligations or liability to the Data Protection Board of India or any Data Principal under the Digital Personal Data Protection Act, 2023 (including penalties under Section 8(5) read with the Schedule to the Act)."*

---

## Summary of Changes

| Section | Change Type | DPDP Basis |
|---------|-------------|------------|
| F — Data Privacy | Replace: fix Data Fiduciary/Processor/Consent Manager terminology | Act S.2(g), S.2(i), S.2(k) |
| G.1 — Samanvay obligations | Replace/expand: add breach notification (24hr), erasure, 1-yr log retention, sub-processors, audit rights, data residency | Rules 6(a)–(g), Rule 7, Act S.8(7)(b) |
| G.1(j) — Scope limitation | Add: Samanvay's obligations extend only to its own infrastructure; field worker devices are NGO's responsibility | Rule 6(a), general principle |
| G.1(k) — Integration Server | Add: Samanvay not responsible for external systems connected via Integration Server; NGO responsible for compliance of those systems | Rule 6(f), Act S.8(2) |
| G.2(a) — Mobile encryption liability | Add: Samanvay bears no liability for device-side breaches where NGO has not enabled available encryption | Rule 6(a), Act S.8(5) |
| G.2 — Customer obligations | Replace/expand: add mobile encryption, device loss SOP (48hr), BI restriction, export controls, consent responsibility, Data Principal rights | Rules 6(a), 6(b), Act S.6, S.8(7) |
| G.4 — Grievance and incident reporting | Update: align with DPDP Rule 7; replace IT Guidelines reference with DPDP obligations | Rule 7, Act S.8(7) |
| Appendix A NDA — Duration | Add: survival clause (perpetual, survives contract termination) | Act S.8(7), general principle |
| Appendix A NDA — Statutory ref | Update: add DPDP Act 2023 and Rules 2025 | General compliance obligation under the Act |
| Appendix A NDA — Liability | Add: clarification note on DPDP regulatory liability | Act S.8(5) and Schedule (enforced via S.33) |
