# Consent Collection Options for Avni Field Programs

**Context:** Avni is used by field workers (operators) to collect data about beneficiaries (Data Principals). The beneficiary does not interact with the app directly. This is classified as **"Physical Medium – Assisted Mode"** by the Aadhaar Notice and Consent Guidelines (UIDAI, March 2022), defined as: *"a person is helping fill an electronic form on his device, in this process personal data is collected and filled in the application."*

---

## Implementation Deadline and Retrospective Applicability

### Deadline: 13 May 2027

The substantive consent obligations — DPDP Act Sections 3–17, including all of Section 6 (consent) and Section 5 (notice) — come into force **18 months after the Rules were notified on 13 November 2025**, i.e., **13 May 2027**.

*Today is 1 April 2026. Approximately 13 months remain.*

| Milestone | Date |
|-----------|------|
| DPDP Rules notified | 13 November 2025 |
| Board constituted | 13 November 2025 |
| Board enforcement powers over Data Fiduciaries operational (Section 27) | 13 May 2027 |
| **All consent and notice obligations enforceable** | **13 May 2027** |

### Are the obligations retrospective?

**Partially — and the distinction matters for implementation planning.**

The Act explicitly addresses pre-commencement data in **Section 5(2)**:

> *"Where a Data Principal has given her consent for the processing of her personal data before the date of commencement of this Act — (a) the Data Fiduciary shall, as soon as it is reasonably practicable, give to the Data Principal a notice informing her of [the data, purpose, rights, and how to complain]. (b) the Data Fiduciary may continue to process the personal data until and unless the Data Principal withdraws her consent."*

| Scenario | Fresh consent required? | Consent mechanism needed by May 2027? |
|----------|:-----------------------:|:-------------------------------------:|
| **New beneficiaries enrolled after 13 May 2027** | Yes | **Yes — must be ready at commencement** |
| **Existing beneficiaries where consent was collected** | No — grandfathered under Section 5(2) | No (notice delivery only) |
| **Existing beneficiaries where NO consent was ever collected** | Arguably yes — Section 5(2) grandfathering only applies where consent *was* given; Section 7(a) (voluntary data provision) may provide limited cover | **Yes — proactively before May 2027** |

### Key implication for Avni

Consent collection mechanisms must be **ready and deployed before 13 May 2027** so that:
1. All new beneficiary enrollments from that date are DPDP-compliant.
2. Any existing beneficiaries for whom no consent was formally recorded can be covered before enforcement begins.

A **separate notice-delivery exercise** is also required for all existing beneficiaries (regardless of consent status) — informing them of what data is held, why, and how to withdraw. For field programs with no digital channel to beneficiaries, this means a physical revisit by field workers, which is a significant operational undertaking.

---

## Consent Options Table

| # | Method | Description | Legal Strength | Available in Avni | Notes |
|---|--------|-------------|:--------------:|:-----------------:|-------|
| 1 | **OTP sent to beneficiary's phone** | Notice is shown/read; OTP is sent to beneficiary's registered mobile; beneficiary reads OTP aloud; field worker enters it in Avni | **Strongest** | **No** | Beneficiary performs the affirmative action (OTP entry traceable to their device). Gold standard for assisted mode. |
| 2 | **Signed physical form + image capture** | Field worker shows/reads a printed notice form; beneficiary signs it; field worker photographs the signed form and attaches it to the Avni record | **Strong** | **Yes** (image capture) | Physical signature is admissible under Section 73, Indian Evidence Act. Photo creates a linked electronic record. |
| 3 | **Audio notice (Avni) + audio recording of verbal consent** | Avni plays the notice aloud in local language; field worker records beneficiary saying "I consent" (with timestamp and beneficiary ID in the record) | **Moderate** | **Yes** (audio notice + audio recording) | Audio is an admissible electronic record under IT Act 2000. Coercion risk is higher than OTP/signature. Requires tamper-proof storage linked to beneficiary record. |
| 4 | **Audio notice (Avni) + field worker checkbox** | Avni plays the notice aloud; field worker checks consent checkbox in Avni as a record of verbal agreement | **Weak** | **Yes** (audio notice available; checkbox available) | Checkbox is clicked by field worker, not beneficiary — fails the "clear affirmative action by Data Principal" standard. Audio notice strengthens the notice side but does not fix the consent side. |
| 5 | **Field worker checkbox alone** | Field worker reads notice verbally (no script, no recording) and checks consent checkbox | **Weakest / Legally Risky** | **Yes** (but not recommended) | No evidence that notice was given or that beneficiary consented. Explicitly flagged as problematic in Aadhaar Guidelines (Section 6.2). Burden of proof under DPDP Act Section 6(10) cannot be met. |

---

## Notes on Legal Validity by Method

### Method 1 — OTP

- **DPDP Act, Section 6(1):** Consent must include "a clear affirmative action." The beneficiary providing the OTP is that action — it is unambiguous, traceable to the individual's phone, and not performable by the field worker.
- **Aadhaar Guidelines, Section 10 & 13 (Assisted Mode):** "SMS/Email based OTP submission" is listed as a valid consent practice for Assisted Mode and rated Free, Specific, Informed, Affirmative, and Easily Withdrawn — the highest-rated method for this scenario.
- **Aadhaar Guidelines, Annexure A.13:** OTP notice and consent flow specifically illustrated for Assisted Mode. *"User to read the text and provide OTP as consent."*

---

### Method 2 — Signed Physical Form + Image Capture

- **DPDP Act, Section 6(1):** A physical signature on a notice-bearing form constitutes an unambiguous affirmative action by the Data Principal.
- **DPDP Act, Section 6(10):** The data fiduciary must be able to prove notice was given and consent obtained. A signed form provides direct documentary evidence.
- **Aadhaar Guidelines, Section 8 (Legally Admissible Methods):** *"Section 73 of the Indian Evidence Act provides the legal basis for admissibility of signature or finger impression in ink."* A photographed signed form is an electronic record admissible under Section 65B of the Evidence Act.
- **Aadhaar Guidelines, Section 10 & 11 (Physical Medium — A Form is Filled):** "Signature in ink on the form" listed as a primary consent practice. Evidence: *"The signed form wherein notice was provided, and consent was taken either in the form of a Signature / thumb impression to be preserved either electronically or physically."*
- **Aadhaar Guidelines, Section 13:** Rated Free, Informed, Affirmative, and Easily Withdrawn.

---

### Method 3 — Audio Notice + Audio Recording of Verbal Consent

- **DPDP Act, Section 6(1):** Verbal "yes" is arguably an affirmative action, but it is weaker than a physical signature or OTP because it is harder to prove was "free and unconditional" when a field worker is present. The Act does not rule it out but does not explicitly endorse it either.
- **Aadhaar Guidelines, Section 8 (Legally Admissible Methods):** *"Electronic record is defined under IT Act 2008 — electronic records include data, **sound**, image generated or recorded and sent or received in electronic form. Indian Evidence Act permits the admissibility of electronic records."* A voice recording is therefore a valid electronic record.
- **IT Act 2000, Section 65B (Indian Evidence Act):** Electronic records including audio are admissible as evidence if accompanied by a certificate about the manner of production and identity of the record.
- **Aadhaar Guidelines, Section 7 & Annexure A.11 (Automated Voice Recording):** Audio playback of notice is explicitly recommended for Assisted Mode. *"The application has the functionality to read out the notice text to the user in preferred language."* This covers the notice requirement under DPDP Act Section 5.
- **Aadhaar Guidelines, Section 11 (IVR-based consent, Medium 7):** The closest analog — IVR plays notice, user presses a key to confirm. Evidence includes *"Electronic record of IVR recording"* and *"Log of User's affirmative action."* A voice recording of verbal consent follows the same evidentiary logic.
- **Caveat:** The Aadhaar Guidelines do not explicitly list "audio recording of beneficiary's verbal consent" as a primary consent practice. It is inferred from the electronic records framework. Legal counsel should confirm adequacy before deployment.

---

### Method 4 — Audio Notice + Checkbox

- **DPDP Act, Section 6(1):** The affirmative action (checkbox click) is performed by the field worker, not the Data Principal. This does not satisfy the requirement that consent be given by the Data Principal.
- **Aadhaar Guidelines, Section 6.2 (Challenges — Assisted Mode):** *"Difficult to ascertain if the operator asked the user to tick the consent."* Directly flags this as an evidentiary problem.
- The audio notice strengthens the notice side (DPDP Act Section 5 / DPDP Rules 2025, Rule 3) but does not cure the consent side. A checkbox clicked by the operator cannot stand as evidence that the Data Principal gave a clear affirmative consent.

---

### Method 5 — Field Worker Checkbox Alone

- **DPDP Act, Section 6(1):** Fails the "clear affirmative action" requirement — no action is taken by the Data Principal at all.
- **DPDP Act, Section 6(10):** *"The Data Fiduciary shall be obliged to prove that a notice was given by her to the Data Principal and consent was given by such Data Principal."* A field-worker-ticked checkbox provides no evidence of either.
- **Aadhaar Guidelines, Section 6.2:** *"Operator controls the device and inputs the information for the user and hence there is no assurance that the notice has been understood by the user and an informed consent has been provided."* Also: *"Problem in demonstrating evidence of an informed consent."*
- **DPDP Rules 2025, Rule 3:** Notice must be *"presented and understandable independently"* and in *"clear and plain language."* With no documented notice delivery, this requirement also fails.

---

## Gap: Consent Withdrawal via Void (Soft Delete)

### Current Avni Behaviour

When a beneficiary withdraws consent, the current mechanism is to **void** (soft delete) their record in Avni — marking it inactive without removing the underlying data.

### Why This is Insufficient

The DPDP Act distinguishes between **ceasing processing** (Section 6(6)) and **erasing data** (Section 8(7)). A void partially addresses the former but fails the latter.

**DPDP Act, Section 2(x)** defines "processing" to explicitly include **storage**:
> *"...includes operations such as collection, recording, organisation, structuring, **storage**, adaptation, retrieval, use..."*

A soft-deleted record remains stored in the Avni cloud DB, on Android devices (Realm), in S3 (images/files), and in backups. This means processing (storage) continues after the void.

**DPDP Act, Section 8(7)(a):**
> *"A Data Fiduciary shall... **erase personal data**, upon the Data Principal withdrawing her consent..."*

A void is not erasure. The law requires actual deletion of personal data, not just a flag.

**DPDP Act, Section 8(7)(b):**
> *"...and **cause its Data Processor to erase** any personal data that was made available by the Data Fiduciary for processing to such Data Processor."*

Samanvay, as the cloud host, is the Data Processor. A void in the Avni application does not trigger any instruction to Samanvay to erase data from the cloud infrastructure or backups.

### What the Void Gets Right

- **Section 6(5):** All processing done before withdrawal remains lawful — the void does not retrospectively invalidate past data collection.
- **Section 6(4):** Ease of withdrawal (via field worker) is arguably comparable to ease of giving consent (also via field worker) — this requirement may be met.
- The void event creates a timestamped audit record, which is useful evidence of the withdrawal.
- It stops active further data collection and service delivery — partially satisfying Section 6(6).

### What Needs to Change

For a void to constitute a legally complete consent withdrawal, it must **trigger an erasure workflow**, not be a terminal event in itself:

| Step | Action Required | Legal Basis |
|------|----------------|-------------|
| 1 | Erase personal data fields from Avni cloud DB after voiding (retain audit log of the void event) | DPDP Act S.8(7)(a) |
| 2 | Instruct Samanvay (Data Processor) to erase from cloud infrastructure and backups | DPDP Act S.8(7)(b) |
| 3 | Clear beneficiary data from Realm on Android devices on next sync | DPDP Act S.6(6) |
| 4 | Delete associated files and images from S3 | DPDP Act S.8(7)(a) |
| 5 | Retain processing logs for minimum 1 year (personal data erased, logs kept) | DPDP Rules 2025, Rule 8(3) |
| 6 | Document any legal retention exceptions if applicable law requires keeping certain records | DPDP Act S.8(7) proviso |

The obligation to cause Samanvay to erase (Step 2) needs to be reflected in Avni's contract with Samanvay — this will be addressed separately.

### Statutory References for this Gap

| Document | Section | Relevance |
|----------|---------|-----------|
| DPDP Act 2023 | Section 2(x) | Definition of processing — explicitly includes storage |
| DPDP Act 2023 | Section 6(4) | Ease of withdrawal must be comparable to ease of giving consent |
| DPDP Act 2023 | Section 6(5) | Past processing before withdrawal remains lawful |
| DPDP Act 2023 | Section 6(6) | Data Fiduciary must cease and cause Data Processors to cease processing within reasonable time |
| DPDP Act 2023 | Section 8(7)(a) | Data Fiduciary must erase personal data upon consent withdrawal |
| DPDP Act 2023 | Section 8(7)(b) | Data Fiduciary must cause its Data Processor to also erase |
| DPDP Rules 2025 | Rule 8(3) | Processing logs must be retained for minimum 1 year even after data erasure |

---

## Additional Notes

### G3 — Healthcare/Children Exemption (Rule 12 + Fourth Schedule)

Rule 12 and the Fourth Schedule to the DPDP Rules 2025 create exemptions from certain obligations, including verifiable parental consent requirements under Section 9. Specifically, the Fourth Schedule lists clinical establishments, mental health establishments, and healthcare professionals as entities that are exempt from the Section 9 obligation to obtain verifiable parental consent before processing a child's personal data.

**Relevance for Avni:** NGOs operating health programs (clinics, maternal health, mental health) may qualify for this exemption and may not need to implement verifiable parental consent mechanisms for child beneficiaries in healthcare contexts. Each implementing NGO should confirm whether it falls within the Fourth Schedule categories before assuming the standard child-consent regime applies.

---

### G6 — Section 17 Research and Statistical Exemption

Section 17(2)(b) and Rule 16 of the DPDP Rules 2025 exempt the processing of personal data for research, archiving, or statistical purposes from several provisions of the Act — including, to the extent consistent with the purpose, certain consent obligations — **provided no individual-level decisions are taken** on the basis of that processing and personal data is not published in identifiable form.

**Relevance for Avni:** Program evaluation, impact assessment, and aggregate statistics generated from beneficiary data may qualify under this exemption. Where an NGO processes beneficiary data solely for research or statistical purposes (and not for delivering individual services), the consent burden may be reduced. Legal counsel should confirm applicability to each specific program design.

---

### G8 — Section 6(6) Cessation Carve-Out

The obligation in Section 6(6) to cease processing personal data after consent withdrawal is qualified. The Data Fiduciary is required to cease processing "unless such processing without her consent is required or authorised under the provisions of this Act or the rules or any other law in force in India."

**Relevance for Avni:** If applicable law (e.g., a state government health scheme mandate) requires retention or continued processing of a beneficiary's record despite consent withdrawal, processing may lawfully continue. NGOs should identify any statutory data retention obligations applicable to their programs before implementing erasure workflows.

---

### G9 — Section 8(7)(a) Dual Erasure Trigger

Section 8(7)(a) requires a Data Fiduciary to erase personal data not only upon consent withdrawal but also "as soon as it is reasonably practicable to assume that the specified purpose is no longer being served" — whichever of these two triggers occurs earlier.

**Relevance for Avni:** Where a beneficiary completes a program and the specified purpose of data collection is no longer being served (e.g., program closed, beneficiary graduated), erasure is required even absent an explicit withdrawal of consent. NGOs should consider whether their program lifecycle creates automatic erasure obligations independent of consent withdrawal.

---

## Key Statutory References

| Document | Section | Relevance |
|----------|---------|-----------|
| DPDP Act 2023 | Section 5 | Notice requirement — must accompany or precede every consent request |
| DPDP Act 2023 | Section 6(1) | Consent must be free, specific, informed, unconditional, unambiguous, with clear affirmative action |
| DPDP Act 2023 | Section 6(3) | Consent request must be in clear and plain language, in English or 8th Schedule language |
| DPDP Act 2023 | Section 6(4) | Right to withdraw consent; ease of withdrawal must equal ease of giving |
| DPDP Act 2023 | Section 6(10) | Burden of proof on Data Fiduciary to prove notice was given and consent was obtained — this obligation is triggered when a question arises in a Board proceeding |
| DPDP Rules 2025 | Rule 3 | Notice must be independently understandable, itemised, and include withdrawal mechanism |
| Aadhaar Guidelines | Section 5 | Defines Assisted Mode — exactly the Avni field worker scenario |
| Aadhaar Guidelines | Section 6.2 | Challenges specific to Assisted Mode, including operator-ticked consent problems |
| Aadhaar Guidelines | Section 8 | Legally admissible evidence: signatures (Evidence Act s.73), electronic records including audio (IT Act / Evidence Act s.65B) |
| Aadhaar Guidelines | Section 10 | Consent practices matrix by medium |
| Aadhaar Guidelines | Section 11 | Evidence requirements for each consent practice |
| Aadhaar Guidelines | Section 12 | Elements of valid consent: Free, Informed, Specific, Clear/Affirmative, Withdraw |
| Aadhaar Guidelines | Section 13 | Best-practice ratings table for notice + consent combinations by medium |
| IT Act 2000 | Section 65B (Evidence Act) | Admissibility of electronic records including audio/sound recordings |
