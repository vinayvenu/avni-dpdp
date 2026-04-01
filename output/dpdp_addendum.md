# DPDP Compliance Addendum to Existing Contracts

## Purpose

This document is a template for a short addendum to be sent to all existing Avni customers whose contracts were signed before the DPDP-compliant contract templates were adopted. It must be signed by all customers **before 13 May 2027**, when the substantive obligations of the Digital Personal Data Protection Act, 2023 and the Digital Personal Data Protection Rules, 2025 come into force.

This addendum supplements — and does not replace — the existing contract between the parties.

---

## Template Addendum

---

**ADDENDUM TO SERVICE CONTRACT**
**Digital Personal Data Protection Act, 2023 — Compliance Amendment**

This Addendum ("Addendum") is entered into on [Date] by and between:

**[Customer Name]**, [Customer Address] (hereinafter "the Customer"); AND

**Samanvay Technologies Private Limited**, #20, T.P. Venugopal Layout, Anand Nagar, Bangalore 560024 (hereinafter "Samanvay");

together referred to as "the Parties."

**WHEREAS** the Parties entered into a Service & Support Contract / Hosting & Support Contract dated **[Original Contract Date]** (the "Original Contract");

**WHEREAS** the Digital Personal Data Protection Act, 2023 (the "Act") and the Digital Personal Data Protection Rules, 2025 (the "Rules") impose obligations on parties engaged in the processing of personal data, which come into full force on 13 May 2027;

**WHEREAS** the Parties wish to amend the Original Contract to reflect their respective obligations under the Act and Rules;

**NOW THEREFORE**, the Parties agree as follows:

---

### 1. Roles of the Parties

**1.1** The Customer is the **Data Fiduciary** as defined under Section 2(i) of the Act and is solely responsible for all obligations of a Data Fiduciary under the Act and Rules, including notice to Data Principals, consent collection, management of Data Principal rights, and data erasure upon consent withdrawal.

**1.2** The Customer may, at its discretion, appoint or engage a **Consent Manager** as defined under Section 2(g) of the Act. Samanvay's obligations under this Addendum are unaffected by whether or not the Customer does so.

**1.3** Samanvay is the **Data Processor** as defined under Section 2(k) of the Act and shall process personal data only on the documented instructions of the Customer and solely for the purposes described in the Original Contract.

---

### 2. NDA — Survival

**2.1** The confidentiality and non-disclosure obligations under the NDA (Appendix A of the Original Contract, or as separately executed between the Parties) shall remain in full force **indefinitely** and shall survive the termination or expiry of the Original Contract and this Addendum.

**2.2** The NDA obligations extend to all personal data of Data Principals processed by Samanvay on behalf of the Customer, until such time as all such data has been erased or returned in accordance with Clause 4 below or as required by applicable law.

**2.3** The reference in the NDA to applicable data protection law is amended to include the Digital Personal Data Protection Act, 2023 and the Digital Personal Data Protection Rules, 2025, in addition to the laws already referenced therein.

---

### 3. Samanvay's Obligations as Data Processor

In addition to its existing obligations under the Original Contract, Samanvay shall:

**3.1 Breach notification:** On becoming aware of any personal data breach, notify the Customer **within 24 hours** of becoming aware, providing: a description of the breach including its nature, extent and timing; the personal data categories affected; an initial assessment of impact; and measures being taken to contain and remediate. This timeline is designed to allow the Customer sufficient time to fulfil its obligations under Rule 7(2) of the Rules, which are two-stage: (a) a **preliminary notification** to the Data Protection Board of India *without delay* upon becoming aware of the breach (Rule 7(2)(a)); and (b) a **detailed follow-up notification** to the Board within 72 hours of becoming aware (Rule 7(2)(b)). The Customer acknowledges that the initial Board notification under Rule 7(2)(a) must be made "without delay" and should not be deferred until the 72-hour deadline.

**3.2 Erasure on instruction:** On written instruction from the Customer, erase specified personal data from all production systems, backups, and associated storage (including Amazon S3) within **30 days**, unless retention is required under applicable law. Samanvay shall confirm erasure in writing to the Customer upon completion. This obligation covers erasures arising from Data Principal consent withdrawal (Act Section 6(4)) and erasure requests (Act Section 12).

**3.3 Access logs:** Maintain application-level logs recording access to personal data, including at minimum: timestamp, user identifier, and action performed. Such logs shall be retained for a minimum of **one year** from the date of each log entry, stored in a tamper-evident manner.

**3.4 Sub-processors:** Samanvay currently uses Amazon Web Services (AWS), Mumbai region, as a sub-processor for cloud infrastructure and storage. Samanvay shall notify the Customer at least **30 days** in advance of any addition or material change to sub-processors.

**3.5 Data residency:** All personal data shall remain stored and processed within AWS data centres in the Mumbai (ap-south-1) region and shall not be transferred outside India without the Customer's prior written consent.

**3.6 Audit rights:** The Customer may request, no more than once per year, a written summary of Samanvay's security measures or the results of any security audit conducted by Samanvay. Samanvay shall respond within 30 days.

---

### 4. Customer's Obligations as Data Fiduciary

In addition to its existing obligations under the Original Contract, the Customer shall:

**4.1 Mobile encryption:** Ensure the AES-256 encryption feature for the Avni Android application (Realm database) is enabled for all field workers. The Customer acknowledges that operating the app without this encryption enabled may constitute a breach of DPDP Rules 2025, Rule 6(a).

**4.2 Device loss:** Notify Samanvay and request revocation of the affected user account within **48 hours** of becoming aware that a field worker's device has been lost or stolen.

**4.3 BI access controls:** Request Samanvay to configure report-creation restrictions in Metabase/Superset before granting BI access to any user, to prevent unauthorised access to raw personal data through custom queries.

**4.4 Bulk exports:** Ensure that personal data downloaded from the system in the form of reports or spreadsheets is handled in accordance with the Act, shared only with authorised personnel, and deleted from personal devices when no longer required.

**4.5 Consent and notice:** Ensure that:
  - All new Data Principals enrolled from 13 May 2027 onwards are provided with a DPDP-compliant notice and have given consent before their personal data is collected.
  - All Data Principals who gave consent before 13 May 2027 are provided with a retrospective notice as required under Section 5(2) of the Act, as soon as reasonably practicable after that date.
  - For Data Principals whose data was collected before 13 May 2027 without any prior consent, Section 5(2) does not apply. Fresh DPDP-compliant consent must be obtained before 13 May 2027, or continued processing must be justified under Section 7 of the Act.

**4.6 Data Principal rights:** Process all requests from Data Principals for access, correction, and erasure of personal data in accordance with the Act. Where erasure requires Samanvay to delete data from its systems, issue a written erasure instruction to Samanvay as described in Clause 3.2.

**4.7 Breach notification:** Notify affected Data Principals and the Data Protection Board of India of any personal data breach in accordance with Rule 7 of the Rules. Samanvay's obligation is limited to notifying the Customer as described in Clause 3.1.

---

### 5. No Other Changes

Except as expressly amended by this Addendum, all terms and conditions of the Original Contract remain in full force and effect. In the event of any conflict between this Addendum and the Original Contract on matters relating to data protection, this Addendum shall prevail.

---

### 6. Effective Date

This Addendum is effective from the date of signing by both Parties and shall remain in force for the duration of the Original Contract and any subsequent renewals between the Parties.

---

**FOR THE CUSTOMER**

Name: ___________________________
Designation: ___________________________
Date: ___________________________

**FOR SAMANVAY TECHNOLOGIES PRIVATE LIMITED**

Name: Arjun Khandelwal
Designation: Director
Date: ___________________________

---

## Operational Notes for Samanvay

**Who needs to sign this?**
Every existing customer whose contract does not already contain the updated DPDP clauses from `contract_changes.md` or `hosting_support_changes.md`.

**When must it be signed?**
Before **13 May 2027**. Rule 6(f) requires security obligations to be in the contract with the Data Processor from the date the Rules come into force. An unsigned addendum on that date means the legal relationship is non-compliant regardless of what Samanvay does operationally.

**Priority order for outreach:**
1. Customers whose contracts expire after May 2027 and will not naturally renew before then — these customers will not sign a new contract in time, so the addendum is the only path to compliance.
2. Customers renewing between now and May 2027 — can sign the addendum alongside the renewal, or receive the updated H&S template directly.
3. Customers renewing after May 2027 — will receive the updated H&S template at renewal, but the addendum should still be signed for the intervening period.

**Tracking:**
Maintain a log of: customer name, original contract date, addendum sent date, addendum signed date. This log is itself evidence of compliance with Rule 6(f) if questioned by the Board.
