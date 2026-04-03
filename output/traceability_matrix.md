# DPDP Traceability Matrix — Avni/Samanvay

This document maps every substantive clause of the DPDP Act 2023 and DPDP Rules 2025 to the current state of the Avni platform and Samanvay contracts, and to the proposed changes.

**Structure:**
- **Part 1 — Forward Traceability Matrix:** Each Act/Rules clause → current state → proposed changes
- **Part 2 — Reverse Traceability Matrix:** Each proposed change → clauses it addresses
- **Part 3 — Clauses with No Proposed Changes:** Clauses that are not applicable or require no action

---

## Part 1 — Forward Traceability Matrix

### DPDP Act 2023

| Clause | Obligation Summary | Applies To | Current State | Proposed Change | Source |
|--------|-------------------|------------|---------------|-----------------|--------|
| **S.4(1)** | Personal data may only be processed for a lawful purpose, with consent or for legitimate uses | NGO (DF) | No structured consent mechanism. Data collected by field workers without formal legal basis documented per beneficiary. | **F2, F3, F4, F5**: Structured consent flows (audio/signed form), mandatory notice step, consent status stored per beneficiary. **Contract G.2(f), H&S Customer (f)**: Customer contractually responsible for consent. | features.md; contract_changes.md; hosting_support_changes.md |
| **S.5(1)** | Notice must accompany or precede consent request, informing: (i) data & purpose, (ii) how to exercise rights under S.6(4) & S.13, (iii) how to complain to Board | NGO (DF) | No structured notice delivery. Field workers collect data without a mandatory notice step. | **F4**: Mandatory notice delivery step in registration — blocks data entry until notice is completed. **F2/F3**: Consent flows that include notice delivery (audio reading / printed form). **Contract G.2(f), H&S Customer (f)**: Customer solely responsible for notice & consent. | features.md (F2, F3, F4); contract_changes.md G.2(f); hosting_support_changes.md Customer (f) |
| **S.5(2)** | For Data Principals who gave consent before commencement: DF must give retrospective notice as soon as reasonably practicable; may continue processing until consent is withdrawn | NGO (DF) | No mechanism to track retrospective notice delivery to existing beneficiaries. | **F6**: Retrospective notice delivery tracking — per-beneficiary flag indicating DPDP notice delivered, with field worker workflow. **R2**: Outstanding Retrospective Notice Report. **Contract G.2(f), H&S Customer (f)**: Retrospective notice obligation explicitly stated including S.5(2) applicability limits. **Addendum 4.5**: Existing customer notice obligations with clear guidance on S.5(2) scope. | features.md (F6, R2); contract_changes.md G.2(f); hosting_support_changes.md Customer (f); dpdp_addendum.md 4.5 |
| **S.5(3)** | Notice must be available in English or any Eighth Schedule language | NGO (DF) | No notice text management in Avni. | **F4**: Notice delivery step will display configurable notice text. Language is the NGO's responsibility; F2 (audio) naturally handles language diversity as the field worker reads in local language. | features.md (F2, F4) |
| **S.6(1)** | Consent must be free, specific, informed, unconditional, unambiguous, with clear affirmative action, limited to necessary data | NGO (DF) | No consent mechanism. Field worker checkbox (if used) fails the "clear affirmative action by Data Principal" standard. | **F2**: Audio recording — field worker reads notice, records beneficiary's verbal consent. **F3**: Signed form — beneficiary signs/thumb-prints printed notice, field worker photographs it. Both constitute clear affirmative action by the Data Principal. **F1** (COULD): OTP-based consent for strongest legal defensibility, built on request only. | features.md (F1, F2, F3); consent.md |
| **S.6(3)** | Consent request must be in clear and plain language, with option for English or Eighth Schedule language, and DPO/contact details | NGO (DF) | No structured consent request. No DPO contact published. | **F4**: Notice step presents configurable text. **R9** (via S.8(9)): Contact info publishing. Language is NGO's responsibility; F2 audio reading handles dialect diversity. | features.md (F4); contract_changes.md G.2(f) |
| **S.6(4)** | Data Principal has right to withdraw consent; ease of withdrawal must be comparable to ease of giving | NGO (DF) | Void (soft delete) is the only mechanism. Requires field worker physical visit — arguably comparable ease since consent also requires field worker visit. | **F7**: Consent withdrawal through the new consent workflow (primary path). Void remains as fallback. **F11** (COULD): In-app/web consent withdrawal form for direct beneficiary access — strengthens "ease of withdrawal" compliance. | features.md (F7, F11); consent.md |
| **S.6(5)–(6)** | Consequences of withdrawal borne by Data Principal. On withdrawal, DF must cease and cause DPs to cease processing within reasonable time, unless processing is authorised by other law. | NGO (DF), Samanvay (DP) | Void stops active use but data remains stored (storage = processing under S.2(x)). No instruction to Samanvay to cease processing. | **F7**: Erasure workflow triggered by consent withdrawal — erases from cloud DB, S3, Realm on next sync. **Contract G.1(f), H&S Samanvay (f)**: Samanvay must erase on written instruction within 30 days. **Addendum 3.3**: Same erasure obligation for existing customers. | features.md (F7); contract_changes.md G.1(f); hosting_support_changes.md Samanvay (f); dpdp_addendum.md 3.3 |
| **S.6(7)–(9)** | Data Principal may use a Consent Manager to give/manage/review/withdraw consent. Consent Manager must be registered with the Board. | NGO (DF) | Original contracts incorrectly labelled the NGO as "Consent Manager." | **Contract F.2, H&S §3**: Corrected — NGO may optionally engage a Consent Manager; Samanvay's obligations unaffected. **Addendum 1.2**: Same correction for existing contracts. | contract_changes.md F.2; hosting_support_changes.md §3; dpdp_addendum.md 1.2 |
| **S.6(10)** | Burden of proof on Data Fiduciary to prove notice was given and consent was obtained | NGO (DF) | No evidence of notice or consent exists. A field-worker-ticked checkbox provides no proof. | **F2**: Audio recording — timestamped, linked to beneficiary and notice version. **F3**: Signed form photograph — timestamped, linked to beneficiary. **F5**: Consent status per record (method, date, field worker, notice version). **R1**: Consent Registry Report — primary document in Board proceedings. | features.md (F2, F3, F5, R1); consent.md |
| **S.7** | Legitimate uses — voluntary provision of data without indication of non-consent | NGO (DF) | May provide limited cover for existing beneficiaries who voluntarily provided data but gave no formal consent. | No platform change. **Addendum 4.5, H&S Customer (f)**: Guidance that S.7(a) may provide limited cover for pre-commencement data where no consent was collected, but fresh DPDP consent is recommended before May 2027. | dpdp_addendum.md 4.5; hosting_support_changes.md Customer (f); consent.md |
| **S.8(1)** | Data Fiduciary responsible for complying with the Act in respect of processing by it or by a Data Processor on its behalf | NGO (DF) | Responsibility acknowledged in existing contracts but not DPDP-specific. | **Contract F.1, H&S §2**: NGO explicitly identified as Data Fiduciary with full DPDP obligations. **Addendum 1.1**: Same for existing contracts. | contract_changes.md F.1; hosting_support_changes.md §2; dpdp_addendum.md 1.1 |
| **S.8(2)** | Data Fiduciary may engage Data Processor only under a valid contract | NGO (DF), Samanvay (DP) | Contract exists but does not contain DPDP-specific obligations. | **Contract F.3, H&S §4**: Samanvay identified as Data Processor, processing only on documented instructions. **Full G.1/G.2 sections**: Detailed DPDP obligations in contract. **Addendum 1.3 + Clause 3**: Same for existing contracts. | contract_changes.md F.3, G.1, G.2; hosting_support_changes.md §4; dpdp_addendum.md 1.3, Clause 3 |
| **S.8(3)** | Where data is used for decisions affecting DP or disclosed to another DF, DF must ensure completeness, accuracy and consistency | NGO (DF) | Data accuracy is operationally managed by field workers and supervisors. No DPDP-specific mechanism. | No platform change proposed. Accuracy is an operational responsibility of the NGO as Data Fiduciary. | — |
| **S.8(4)** | DF must implement appropriate technical and organisational measures for effective observance | NGO (DF), Samanvay (DP) | Security measures exist but are not comprehensive per DPDP. | All proposed features (F2–F20) and contract changes collectively address this. **Contract G.1(a)–(k)**: Samanvay's technical measures. **Contract G.2(a)–(j)**: NGO's organisational measures. | features.md; contract_changes.md G.1, G.2; hosting_support_changes.md; security_requirements.md |
| **S.8(5)** | DF must protect personal data by taking reasonable security safeguards to prevent breach | NGO (DF), Samanvay (DP) | Encryption at rest (AES-256) and in transit (TLS) exist. Realm encryption optional. No access audit logs. No bulk export controls. | **F12**: Application-level access audit logging. **F14**: BI report-creation restriction. **F15**: Bulk export logging and role restrictions. **M1** (security_requirements): Mandatory Realm encryption. **Contract G.1(a)–(c)**: Encryption, access controls, access logs. **Contract G.2(a)**: NGO must enable mobile encryption. | features.md (F12, F14, F15); security_requirements.md (M1–M5); contract_changes.md G.1(a)–(c), G.2(a) |
| **S.8(6)** | On breach, DF must notify Board and each affected Data Principal in prescribed form and manner | NGO (DF) | No documented breach notification process. No assigned owner or escalation chain. | **M6** (security_requirements): Documented breach notification process. **Contract G.1(e), H&S Samanvay (e)**: Samanvay notifies NGO within 24 hours. **Contract G.2(h), H&S Customer (h)**: NGO solely responsible for notifying Board and Data Principals. **Addendum 3.1**: Same for existing customers. **Contract G.4**: Updated grievance/incident reporting clause. | security_requirements.md (M6); contract_changes.md G.1(e), G.2(h), G.4; hosting_support_changes.md Samanvay (e), Customer (h); dpdp_addendum.md 3.1 |
| **S.8(7)(a)** | DF must erase personal data on consent withdrawal or when specified purpose is no longer served, whichever is earlier | NGO (DF), Samanvay (DP) | Void is soft-delete only — data remains in cloud DB, Realm, S3, and backups. No erasure workflow. | **F7**: Erasure workflow on consent withdrawal — erases from production DB, S3, Realm on next sync; PITR backups expire in 35 days. **F9** (SHOULD): Purpose expiry detection — flags inactive beneficiaries for review. **R5**: Erasure Workflow Status Report. **R6** (SHOULD): Data Retention / Purpose Expiry Report. | features.md (F7, F9, R5, R6); consent.md |
| **S.8(7)(b)** | DF must cause its Data Processor to erase personal data | NGO (DF), Samanvay (DP) | No mechanism for NGO to instruct Samanvay to erase. No erasure obligation in contract. | **F8**: Erasure on written instruction from NGO — same workflow as F7. **Contract G.1(f), H&S Samanvay (f)**: Samanvay must erase within 30 days on written instruction, confirm in writing. **Addendum 3.3**: Same for existing customers. | features.md (F8); contract_changes.md G.1(f); hosting_support_changes.md Samanvay (f); dpdp_addendum.md 3.3 |
| **S.8(8)** | Purpose deemed no longer served if DP does not approach DF or exercise rights for prescribed period | NGO (DF) | No purpose expiry tracking. | **F9** (SHOULD): Purpose expiry detection — flags beneficiaries whose program has ended or who have been inactive beyond configurable threshold. **R6** (SHOULD): Data Retention / Purpose Expiry Report. | features.md (F9, R6) |
| **S.8(9)** | DF must publish business contact info of DPO or authorised person | NGO (DF) | Not confirmed whether NGOs publish this. Samanvay has contact info on website. | No platform change. Operational obligation of each NGO as Data Fiduciary. Contract implicitly requires this as part of DPDP compliance obligations. | — |
| **S.8(10)** | DF must establish effective grievance redressal mechanism | NGO (DF) | No specific DPDP grievance mechanism in Avni. | **F10**: Data Principal rights request log — intake log for access, correction, erasure requests. Not a full grievance system but provides the minimum mechanism. | features.md (F10) |
| **S.9(1)** | Before processing a child's data, DF must obtain verifiable consent of parent/lawful guardian | NGO (DF) | No age verification or parental consent mechanism. | No platform change proposed. NGOs processing children's data in healthcare contexts may be exempt under Rule 12 / Fourth Schedule. Each NGO must assess applicability. | consent.md (G3 note) |
| **S.9(2)–(3)** | Must not process data detrimental to child's well-being. Must not track, behaviourally monitor, or target-advertise to children. | NGO (DF) | Avni does not engage in behavioural monitoring or targeted advertising. | No change required. Avni's use case (field data collection for service delivery) does not involve these activities. | — |
| **S.11(1)** | Data Principal has right to obtain: (a) summary of data being processed, (b) identities of all DFs/DPs data shared with, (c) other prescribed info | NGO (DF) | No mechanism for beneficiaries to request access to their data. | **F10**: Data Principal rights request log — captures access requests. The NGO is responsible for fulfilling requests. **Contract G.2(g), H&S Customer (g)**: NGO responsible for processing Data Principal rights requests. **Addendum 4.6**: Same for existing customers. | features.md (F10); contract_changes.md G.2(g); hosting_support_changes.md Customer (g); dpdp_addendum.md 4.6 |
| **S.12(1)–(3)** | Data Principal has right to correction, completion, updating and erasure. DF must correct on request. DF must erase on request unless retention needed for specified purpose or law. | NGO (DF), Samanvay (DP) | Correction/update possible through field worker. No erasure mechanism (void is soft-delete). No formal request tracking. | **F8**: Erasure on written instruction (Data Principal rights request → NGO → Samanvay). **F10**: Data Principal rights request log — tracks correction and erasure requests. **Contract G.2(g), H&S Customer (g)**: NGO processes rights requests; issues erasure instructions to Samanvay per G.1(f). **Addendum 4.6**: Same for existing customers. | features.md (F8, F10); contract_changes.md G.2(g), G.1(f); hosting_support_changes.md Customer (g), Samanvay (f); dpdp_addendum.md 4.6, 3.3 |
| **S.13(1)–(3)** | Data Principal has right to grievance redressal. DF must respond within prescribed period. DP must exhaust DF grievance mechanism before approaching Board. | NGO (DF) | Samanvay has a grievance email (hello@samanvayfoundation.org). No DPDP-specific mechanism at NGO level. | **Contract G.4**: Updated grievance and incident reporting clause — aligned with DPDP Rule 7 instead of IT Guidelines. **F10**: Data Principal rights request log provides a basic intake mechanism. NGOs must establish their own grievance redressal process. | contract_changes.md G.4; features.md (F10) |
| **S.16(1)** | Central Government may restrict transfer of personal data to notified countries | NGO (DF), Samanvay (DP) | All data in AWS Mumbai (ap-south-1). No cross-border transfer. | **Contract G.1(h), H&S Samanvay (h)**: Data residency clause — all data in Mumbai region, no transfer outside India without written consent. **Addendum 3.6**: Same for existing customers. | contract_changes.md G.1(h); hosting_support_changes.md Samanvay (h); dpdp_addendum.md 3.6 |
| **S.33 + Schedule** | Penalties: up to ₹250 Cr for security breach (S.8(5)), ₹200 Cr for breach notification failure (S.8(6)), ₹50 Cr for other breaches | NGO (DF) | Existing contract liability cap is ₹1 lakh or annual contract value (whichever lower). No DPDP regulatory liability acknowledgement. | **Contract NDA Liability note**: Clarification that contractual indemnity cap does not limit DPDP regulatory liability to the Board. NGO bears direct regulatory exposure. **Addendum**: Existing customers made aware through addendum process. | contract_changes.md §7 (NDA Liability) |

### DPDP Rules 2025

| Clause | Obligation Summary | Applies To | Current State | Proposed Change | Source |
|--------|-------------------|------------|---------------|-----------------|--------|
| **Rule 3(a)–(c)** | Notice must be: (a) independently understandable, (b) itemised description of data and purposes in clear language, (c) include link/means for withdrawal, rights exercise, and Board complaint | NGO (DF) | No notice mechanism. | **F4**: Mandatory notice delivery step — configurable notice text displayed before data collection. **F2/F3**: Notice delivered via audio reading or printed form. Notice content is NGO's responsibility but platform enforces the step. | features.md (F2, F3, F4) |
| **Rule 6(1)(a)** | Encryption, obfuscation, masking, or virtual tokens for personal data | Samanvay (DP), NGO (DF) | Cloud: AES-256 at rest, TLS in transit. Realm encryption optional per org. No masking on exports. | **M1** (security_requirements): Mandatory Realm encryption as platform default. **F15**: Bulk export role restrictions and potential field-level redaction. **F20** (COULD): Pseudonymisation/tokenisation. **Contract G.1(a), G.2(a)**: Encryption obligations + NGO liability for not enabling mobile encryption. | security_requirements.md (M1, M5, C1); features.md (F15, F20); contract_changes.md G.1(a), G.2(a) |
| **Rule 6(1)(b)** | Access controls on computer resources used by DF or DP | Samanvay (DP), NGO (DF) | Auth exists (username/password). BI layer not restricted by default. No bulk export role restrictions. Passwords not technically enforceable. | **F14**: BI report-creation restricted to admin roles as default. **F15**: Bulk export restricted to specific roles. **F16** (SHOULD): Periodic OTP re-auth + token model. **F17** (SHOULD): Web session timeout. **M8** (security_requirements): Device loss SOP (48hr revocation). **Contract G.1(b), G.2(b)–(d)**: Access controls + credential + BI + device obligations. | features.md (F14, F15, F16, F17); security_requirements.md (M4, M8, S0, S5); contract_changes.md G.1(b), G.2(b)–(d) |
| **Rule 6(1)(c)** | Logs, monitoring and review for detecting unauthorised access, investigation, and remediation | Samanvay (DP) | Infrastructure logs (CloudWatch) exist. No application-level user-action audit logs confirmed. No anomaly alerting. | **F12**: Application-level access audit logging (user ID, timestamp, action, entity). **R4**: Access Audit Report for NGO admins. **F19** (SHOULD): Breach detection and anomaly alerting. **Contract G.1(c)**: Minimum 1-year tamper-evident log retention. | features.md (F12, F19, R4); security_requirements.md (M2, S1); contract_changes.md G.1(c) |
| **Rule 6(1)(d)** | Backups and continuity measures (e.g., data-backups) in event of compromise | Samanvay (DP) | PITR backups exist (35-day window). Encrypted status unconfirmed. | **Contract G.1(d), H&S Samanvay (d)**: PITR backups minimum 35 days, encrypted to same standard as primary data. **Addendum 3.2**: Same for existing customers. | contract_changes.md G.1(d); hosting_support_changes.md Samanvay (d); dpdp_addendum.md 3.2 |
| **Rule 6(1)(e)** | Retain logs and personal data for minimum 1 year for detection, investigation, remediation, and continuity | Samanvay (DP) | CloudWatch log retention unconfirmed. | **M3** (security_requirements): Audit and set all log retention to ≥1 year. **Contract G.1(c)**: 1-year minimum log retention, tamper-evident. **Addendum 3.4**: Same for existing customers. | security_requirements.md (M3); contract_changes.md G.1(c); dpdp_addendum.md 3.4 |
| **Rule 6(1)(f)** | Contract between DF and DP must include appropriate security safeguard provisions | NGO (DF), Samanvay (DP) | Existing contract has basic security clauses (encryption, TLS, access, audit dates). Does not cover DPDP-specific obligations. | **Contract G.1 (full section)**: Comprehensive security obligations — encryption, access controls, logs, backups, breach notification, erasure, sub-processors, data residency, audit rights, scope limitation. **H&S Data Security (full section)**: Same for H&S contract. **Addendum Clause 3 (full)**: Same for existing customers. **NDA updates**: Survival clause, DPDP statutory reference, liability clarification. | contract_changes.md G.1; hosting_support_changes.md Data Security; dpdp_addendum.md Clause 3; contract_changes.md §5–§7 (NDA) |
| **Rule 6(1)(g)** | Appropriate technical and organisational measures for effective observance of security safeguards | Samanvay (DP), NGO (DF) | Security audits on demand only. No periodic review. | **S2** (security_requirements): Annual security audits. **Contract G.1(i)**: Audit rights — NGO may request annual summary of security measures. All proposed features and contract changes collectively constitute technical and organisational measures. | security_requirements.md (S2); contract_changes.md G.1(i) |
| **Rule 7(1)** | On breach, notify each affected Data Principal without delay: description, consequences, measures taken, safety measures they can take, contact info | NGO (DF) | No breach notification process documented. | **M6** (security_requirements): Documented breach notification process. **Contract G.2(h), H&S Customer (h)**: NGO solely responsible for notifying Data Principals per Rule 7. **Addendum 4.7**: Same for existing customers. | security_requirements.md (M6); contract_changes.md G.2(h); hosting_support_changes.md Customer (h); dpdp_addendum.md 4.7 |
| **Rule 7(2)(a)** | Notify Board without delay — preliminary description of breach | NGO (DF) | No process. | **Contract G.1(e), H&S Samanvay (e)**: Samanvay notifies NGO within 24 hours (to enable NGO's immediate Board notification). **Contract G.2(h)**: NGO responsible for Board notification. **Addendum 3.1, 4.7**: Same for existing customers. Note in contracts: "without delay" may mean within hours. | contract_changes.md G.1(e), G.2(h); hosting_support_changes.md Samanvay (e), Customer (h); dpdp_addendum.md 3.1, 4.7 |
| **Rule 7(2)(b)** | Detailed follow-up notification to Board within 72 hours: updated description, broad facts, measures, findings re: cause, remedial measures, report on Data Principal notifications | NGO (DF) | No process. | Same as Rule 7(2)(a) above. The 24-hour Samanvay→NGO SLA gives the NGO ~48 hours for investigation and detailed Board submission. | contract_changes.md G.1(e); dpdp_addendum.md 3.1 |
| **Rule 8(1)–(2)** | Erasure when purpose expires per Third Schedule; 48-hour pre-erasure notice to Data Principal | NGO (DF) | No purpose expiry tracking. No pre-erasure notification. | **F9** (SHOULD): Purpose expiry detection. **R6** (SHOULD): Data Retention / Purpose Expiry Report. Third Schedule details (specific time periods by class of DF) not yet published — implementation will depend on whether NGOs are classified. | features.md (F9, R6) |
| **Rule 8(3)** | Retain personal data and processing logs for minimum 1 year from date of processing, for Seventh Schedule purposes; erase after unless required by other law | Samanvay (DP), NGO (DF) | Log retention unconfirmed. No explicit post-retention erasure process. | **M3** (security_requirements): 1-year log retention. **Contract G.1(c)**: 1-year minimum for access logs. Erasure workflow (F7) accounts for this — logs retained even after personal data erased. | security_requirements.md (M3); contract_changes.md G.1(c); features.md (F7) |
| **Rule 9** | Publish DPO or contact person info prominently on website/app and in every rights-related response | NGO (DF) | Samanvay publishes contact info. NGOs' compliance unconfirmed. | No platform change. Operational obligation of each NGO. Contract implicitly requires DPDP compliance. | — |
| **Rule 14(1)–(3)** | DF must publish means for Data Principals to exercise rights. Grievance system must respond within 90 days. | NGO (DF) | No published rights exercise mechanism. No DPDP-specific grievance system. | **F10**: Data Principal rights request log. Each NGO must publish the means for beneficiaries to exercise rights (operational, not a platform feature). | features.md (F10) |
| **Rule 15** | Personal data may be transferred outside India subject to Central Government requirements for foreign state access | NGO (DF), Samanvay (DP) | All data in AWS Mumbai. No cross-border transfer. | **Contract G.1(h), H&S Samanvay (h)**: Data residency clause. **Addendum 3.6**: Same for existing customers. | contract_changes.md G.1(h); hosting_support_changes.md Samanvay (h); dpdp_addendum.md 3.6 |

---

## Part 2 — Reverse Traceability Matrix

### Platform Features

| Change ID | Change Description | Source Document | DPDP Clause(s) Addressed |
|-----------|-------------------|-----------------|--------------------------|
| **F1** | OTP-based consent flow (COULD — build on request) | features.md | Act S.6(1) |
| **F2** | Field worker audio reading + beneficiary verbal consent recording | features.md | Act S.5(1), S.5(3), S.6(1), S.6(10); Rules Rule 3(a)–(c) |
| **F3** | Signed physical form + image capture consent flow | features.md | Act S.5(1), S.5(3), S.6(1), S.6(10); Rules Rule 3(a)–(c) |
| **F4** | Mandatory notice delivery step in registration | features.md | Act S.4(1), S.5(1), S.5(3), S.6(3); Rules Rule 3(a)–(c) |
| **F5** | Consent status stored per beneficiary record | features.md | Act S.6(1), S.6(10) |
| **F6** | Retrospective notice delivery tracking | features.md | Act S.5(2) |
| **F7** | Erasure workflow on consent withdrawal | features.md | Act S.6(4), S.6(6), S.8(7)(a); Rules Rule 8(3) |
| **F8** | Erasure on written instruction (Data Principal rights request) | features.md | Act S.8(7)(b), S.12(1), S.12(3) |
| **F9** | Purpose expiry detection (SHOULD) | features.md | Act S.8(7)(a), S.8(8); Rules Rule 8(1)–(2) |
| **F10** | Data Principal rights request log | features.md | Act S.8(10), S.11(1), S.12(1)–(3), S.13(1); Rules Rule 14(1)–(3) |
| **F11** | In-app consent withdrawal mechanism (COULD) | features.md | Act S.6(4) |
| **F12** | Application-level access audit logging | features.md | Act S.8(5); Rules Rule 6(1)(c), Rule 6(1)(e) |
| **F14** | BI report-creation restriction as platform default | features.md | Act S.8(5); Rules Rule 6(1)(b) |
| **F15** | Bulk export logging and role restrictions | features.md | Act S.8(5); Rules Rule 6(1)(a), Rule 6(1)(b) |
| **F16** | Periodic OTP re-auth + token model (SHOULD) | features.md | Rules Rule 6(1)(b) |
| **F17** | Session timeout for Data Entry App (SHOULD) | features.md | Rules Rule 6(1)(b) |
| **F19** | Breach detection and anomaly alerting (SHOULD) | features.md | Rules Rule 6(1)(c) |
| **F20** | Pseudonymisation / tokenisation (COULD) | features.md | Rules Rule 6(1)(a) |

### Reports

| Change ID | Change Description | Source Document | DPDP Clause(s) Addressed |
|-----------|-------------------|-----------------|--------------------------|
| **R1** | Consent Registry Report | features.md | Act S.6(10) |
| **R2** | Outstanding Retrospective Notice Report | features.md | Act S.5(2) |
| **R3** | Bulk Export Log Report | features.md | Rules Rule 6(1)(a) |
| **R4** | Access Audit Report | features.md | Rules Rule 6(1)(c) |
| **R5** | Erasure Workflow Status Report | features.md | Act S.8(7)(a), S.8(7)(b); Contract G.1(f) |
| **R6** | Data Retention / Purpose Expiry Report (SHOULD) | features.md | Act S.8(7)(a), S.8(8); Rules Rule 8(1) |
| **R8** | DPDP Compliance Dashboard for NGO Admins (SHOULD) | features.md | General compliance posture |

### Security Requirements (Operational)

| Change ID | Change Description | Source Document | DPDP Clause(s) Addressed |
|-----------|-------------------|-----------------|--------------------------|
| **M1** | Mandatory mobile (Realm) encryption | security_requirements.md | Rules Rule 6(1)(a) |
| **M2** | Application-level access audit logs | security_requirements.md | Rules Rule 6(1)(c) |
| **M3** | 1-year log retention (CloudWatch) | security_requirements.md | Rules Rule 6(1)(e), Rule 8(3) |
| **M4** | Restrict PII report creation in BI layer | security_requirements.md | Rules Rule 6(1)(b) |
| **M5** | Controls on bulk PII exports | security_requirements.md | Rules Rule 6(1)(a) |
| **M6** | Documented breach notification process | security_requirements.md | Act S.8(6); Rules Rule 7(1), Rule 7(2)(a), Rule 7(2)(b) |
| **M7** | Security obligations in Samanvay contract | security_requirements.md | Rules Rule 6(1)(f) |
| **M8** | Device loss/revocation SOP | security_requirements.md | Rules Rule 6(1)(b) |
| **S0** | Periodic OTP re-auth + token model (SHOULD) | security_requirements.md | Rules Rule 6(1)(b) |
| **S1** | Breach detection / anomaly alerting (SHOULD) | security_requirements.md | Rules Rule 6(1)(c) |
| **S2** | Periodic security audits (SHOULD) | security_requirements.md | Rules Rule 6(1)(g) |

### Contract Changes — Service & Support Contract

| Change ID | Change Description | Source Document | DPDP Clause(s) Addressed |
|-----------|-------------------|-----------------|--------------------------|
| **F.1** | NGO identified as Data Fiduciary | contract_changes.md | Act S.2(i), S.8(1) |
| **F.2** | Optional Consent Manager engagement clarified | contract_changes.md | Act S.2(g), S.6(7)–(9) |
| **F.3** | Samanvay identified as Data Processor, processing on instructions only | contract_changes.md | Act S.2(k), S.8(2) |
| **G.1(a)** | Encryption obligations (AES-256 at rest, TLS 1.2+ in transit) | contract_changes.md | Rules Rule 6(1)(a) |
| **G.1(b)** | Access controls — need-to-know, NDA-bound personnel | contract_changes.md | Rules Rule 6(1)(b) |
| **G.1(c)** | Access logs — 1-year retention, tamper-evident | contract_changes.md | Rules Rule 6(1)(c), Rule 6(1)(e) |
| **G.1(d)** | PITR backups — 35 days, encrypted | contract_changes.md | Rules Rule 6(1)(d) |
| **G.1(e)** | Breach notification — 24 hours to NGO | contract_changes.md | Act S.8(6); Rules Rule 7(2)(a), Rule 7(2)(b) |
| **G.1(f)** | Erasure on instruction — 30 days, written confirmation | contract_changes.md | Act S.8(7)(b), S.12(3) |
| **G.1(g)** | Sub-processor disclosure (AWS) — 30-day advance notice of changes | contract_changes.md | Rules Rule 6(1)(f); Act S.8(2) |
| **G.1(h)** | Data residency — AWS Mumbai only, no transfer without consent | contract_changes.md | Act S.16(1); Rules Rule 15 |
| **G.1(i)** | Audit rights — annual security summary on request | contract_changes.md | Rules Rule 6(1)(g) |
| **G.1(j)** | Scope limitation — Samanvay not responsible for field worker devices | contract_changes.md | Rules Rule 6(1)(a) (scope clarification) |
| **G.1(k)** | Integration Server — Samanvay not responsible for external systems | contract_changes.md | Rules Rule 6(1)(f); Act S.8(2) |
| **G.2(a)** | NGO must enable mobile encryption; Samanvay not liable if not enabled | contract_changes.md | Rules Rule 6(1)(a); Act S.8(5) |
| **G.2(b)** | User credential obligations (no sharing, complexity) | contract_changes.md | Rules Rule 6(1)(b) |
| **G.2(c)** | Device loss — 48-hour revocation SLA | contract_changes.md | Rules Rule 6(1)(b) |
| **G.2(d)** | BI access restrictions | contract_changes.md | Rules Rule 6(1)(b) |
| **G.2(e)** | Bulk export handling obligations | contract_changes.md | Rules Rule 6(1)(a) |
| **G.2(f)** | Consent management — NGO solely responsible | contract_changes.md | Act S.4(1), S.5(1), S.5(2), S.6(1) |
| **G.2(g)** | Data Principal rights — NGO responsible, erasure via G.1(f) | contract_changes.md | Act S.11(1), S.12(1)–(3) |
| **G.2(h)** | Breach notification — NGO solely responsible for Board and DP notification | contract_changes.md | Act S.8(6); Rules Rule 7(1), Rule 7(2) |
| **G.2(i)** | Unrooted devices | contract_changes.md | Rules Rule 6(1)(b) |
| **G.4** | Grievance/incident reporting — aligned with DPDP Rule 7 | contract_changes.md | Act S.13(1); Rules Rule 7 |
| **NDA Survival** | NDA survives contract termination indefinitely | contract_changes.md §5 | Act S.8(7) (data obligations persist beyond contract) |
| **NDA Statutory Ref** | Add DPDP Act 2023 and Rules 2025 to statutory references | contract_changes.md §6 | General compliance |
| **NDA Liability Note** | Clarification that contractual cap does not limit DPDP regulatory liability | contract_changes.md §7 | Act S.33 + Schedule |

### Contract Changes — Hosting & Support Contract

| Change ID | Change Description | Source Document | DPDP Clause(s) Addressed |
|-----------|-------------------|-----------------|--------------------------|
| **H&S Data Privacy §1** | NDA continuity confirmation | hosting_support_changes.md | Act S.8(7) |
| **H&S Data Privacy §2–4** | DF/DP/CM terminology corrected (mirrors Service Contract F.1–F.3) | hosting_support_changes.md | Act S.2(g), S.2(i), S.2(k), S.8(1), S.8(2) |
| **H&S Samanvay (a)–(k)** | Full security obligations (mirrors Service Contract G.1(a)–(k)) | hosting_support_changes.md | Rules Rule 6(1)(a)–(g), Rule 7; Act S.8(5), S.8(6), S.8(7)(b), S.16(1) |
| **H&S Customer (a)–(i)** | Full NGO obligations (mirrors Service Contract G.2(a)–(j)) | hosting_support_changes.md | Rules Rule 6(1)(a), Rule 6(1)(b); Act S.5(2), S.6, S.8(7), S.11, S.12, S.13 |
| **H&S Applicable Law** | DPDP Act and Rules added as governing law | hosting_support_changes.md | General compliance |

### DPDP Addendum (for Existing Contracts)

| Change ID | Change Description | Source Document | DPDP Clause(s) Addressed |
|-----------|-------------------|-----------------|--------------------------|
| **Addendum 1.1–1.3** | Roles defined (DF/DP/optional CM) | dpdp_addendum.md | Act S.2(g), S.2(i), S.2(k), S.8(1), S.8(2) |
| **Addendum 2.1–2.3** | NDA survival + DPDP statutory reference | dpdp_addendum.md | Act S.8(7); General compliance |
| **Addendum 3.1** | Breach notification — 24 hours | dpdp_addendum.md | Act S.8(6); Rules Rule 7 |
| **Addendum 3.2** | PITR backups — 35 days, encrypted | dpdp_addendum.md | Rules Rule 6(1)(d) |
| **Addendum 3.3** | Erasure on instruction — 30 days | dpdp_addendum.md | Act S.8(7)(b), S.12(3) |
| **Addendum 3.4** | Access logs — 1-year retention | dpdp_addendum.md | Rules Rule 6(1)(c), Rule 6(1)(e) |
| **Addendum 3.5** | Sub-processor disclosure (AWS) | dpdp_addendum.md | Rules Rule 6(1)(f); Act S.8(2) |
| **Addendum 3.6** | Data residency — Mumbai only | dpdp_addendum.md | Act S.16(1); Rules Rule 15 |
| **Addendum 3.7** | Audit rights — annual | dpdp_addendum.md | Rules Rule 6(1)(g) |
| **Addendum 3.8** | Scope limitation — Samanvay infra only | dpdp_addendum.md | Rules Rule 6(1)(a) (scope) |
| **Addendum 3.9** | Integration Server scope limitation | dpdp_addendum.md | Rules Rule 6(1)(f); Act S.8(2) |
| **Addendum 4.1** | NGO mobile encryption obligation | dpdp_addendum.md | Rules Rule 6(1)(a); Act S.8(5) |
| **Addendum 4.2** | Device loss — 48 hours | dpdp_addendum.md | Rules Rule 6(1)(b) |
| **Addendum 4.3** | BI access controls | dpdp_addendum.md | Rules Rule 6(1)(b) |
| **Addendum 4.4** | Bulk export handling | dpdp_addendum.md | Rules Rule 6(1)(a) |
| **Addendum 4.5** | Consent and notice obligations (including S.5(2) scope) | dpdp_addendum.md | Act S.4(1), S.5(1), S.5(2), S.6(1), S.7 |
| **Addendum 4.6** | Data Principal rights | dpdp_addendum.md | Act S.11(1), S.12(1)–(3) |
| **Addendum 4.7** | Breach notification to Board and Data Principals | dpdp_addendum.md | Act S.8(6); Rules Rule 7(1), Rule 7(2) |

---

## Part 3 — Clauses with No Proposed Changes

These clauses are either not applicable to the Avni/NGO context, require no action, or are administrative/procedural provisions of the Act that do not create obligations on Data Fiduciaries or Data Processors.

### Not Applicable to Avni

| Clause | Summary | Reason |
|--------|---------|--------|
| **Act S.7(b)–(h)** | Legitimate uses: State instrumentalities, law enforcement, legal compliance, medical emergency, epidemic, disaster, employment | These are alternative grounds for processing available to specific actors (State, employers, etc.). Not the basis for NGO field data collection. |
| **Act S.9(4)–(5)** | Central Government may exempt certain DFs from child consent obligations; may notify age-based exemptions for verifiably safe processing | Depends on future Central Government notification. Not actionable now. |
| **Act S.10** | Additional obligations of Significant Data Fiduciary: DPO, data auditor, DPIA, periodic audit | Avni-implementing NGOs are unlikely to be notified as Significant Data Fiduciaries. If notified, obligations would apply. |
| **Act S.14** | Right to nominate another individual to exercise rights on death/incapacity | Operational responsibility of the NGO. No platform change needed — nomination is a legal relationship, not a data model feature. |
| **Act S.15** | Duties of Data Principal (no impersonation, no suppression, no false grievances) | Obligations on the beneficiary, not on the DF or DP. No action required. |
| **Act S.17(1)(a)–(f)** | Exemptions from Chapter II (except S.8(1),(5)) and Chapter III: legal rights enforcement, judicial processing, offence prevention, offshore contracts, mergers, loan defaults | Exemptions available in specific circumstances. Not the general basis of Avni's processing. |
| **Act S.17(2)(a)** | Exemption for State instrumentalities notified for sovereignty/security | Not applicable to NGOs. |
| **Act S.17(3)** | Central Government may exempt certain DFs (including startups) from S.5, S.8(3), S.8(7), S.10, S.11 | Depends on future notification. Not actionable now. |
| **Act S.17(4)** | For State processing: S.8(7) and S.12(3) may not apply; where no individual-level decision is made, S.12(2) also may not apply | Not applicable to NGOs. |
| **Rule 4** | Consent Manager registration and obligations | Avni/Samanvay is not a Consent Manager. NGOs may optionally engage one. |
| **Rule 5** | Processing by State/instrumentalities for subsidy, benefit, service, etc. | Not applicable to NGOs. |
| **Rule 10** | Verifiable consent for processing child's data (identity/age verification of parent) | May apply to NGOs processing children's data. Exemptions may apply under Rule 12 / Fourth Schedule for healthcare. Each NGO must assess. No platform change proposed. |
| **Rule 11** | Verifiable consent for persons with disability (lawful guardian verification) | Similar to Rule 10 — may apply to specific NGO programs. Operational assessment required per NGO. |
| **Rule 12** | Exemptions from child consent obligations for specified DF classes and purposes (Fourth Schedule) | Healthcare-related exemptions may apply. Each NGO must confirm. |
| **Rule 13** | SDF obligations: annual DPIA, audit, algorithmic due diligence, data localisation | Not applicable unless an NGO is notified as SDF. |

### Procedural/Administrative Provisions (No Action Required)

| Clause | Summary |
|--------|---------|
| **Act S.1** | Short title and commencement |
| **Act S.2** | Definitions |
| **Act S.3** | Application of Act (territorial scope) |
| **Act S.18–26** | Data Protection Board: establishment, composition, appointment, salary, disqualification, resignation, proceedings, officers, powers of Chairperson |
| **Act S.27–28** | Board powers, functions, and inquiry procedure |
| **Act S.29–32** | Appeal to Appellate Tribunal, alternate dispute resolution, voluntary undertaking |
| **Act S.34** | Penalties credited to Consolidated Fund |
| **Act S.35** | Good faith protection for government/Board |
| **Act S.36** | Central Government power to call for information |
| **Act S.37** | Central Government power to issue blocking directions |
| **Act S.38** | Consistency with other laws |
| **Act S.39** | Bar of civil court jurisdiction |
| **Act S.40–43** | Rule-making, laying of rules, amendment of Schedule, power to remove difficulties |
| **Act S.44** | Amendments to TRAI Act, IT Act, RTI Act |
| **Rule 1–2** | Short title, commencement, definitions |
| **Rule 16** | Exemption for research/archiving/statistical purposes (may apply to program evaluation — see consent.md G6 note) |
| **Rule 17–21** | Board appointment, salary, procedure, digital office, officers |
| **Rule 22** | Appeal to Appellate Tribunal |
| **Rule 23** | Central Government calling for information from DF/intermediary |

### Applicable but Requiring Operational Action Only (No Platform or Contract Change)

| Clause | Summary | Required Action |
|--------|---------|----------------|
| **Act S.8(3)** | Data accuracy and consistency | NGO operational responsibility — field worker training, supervisor review |
| **Act S.8(9)** | Publish DPO/contact info | Each NGO must publish on its own website/communications |
| **Act S.9(1)–(3)** | Child data: verifiable parental consent, no detrimental processing, no tracking/advertising | Verifiable consent: operational per NGO (healthcare exemption may apply). No tracking/advertising: Avni's use case inherently compliant. |
| **Rule 9** | Prominently publish contact info on website/app | Each NGO must publish. Samanvay publishes on its own site. |
| **Rule 14** | Publish means for Data Principals to exercise rights; 90-day grievance response | Each NGO must publish and establish response process |
| **Act S.17(2)(b)** | Research/statistical exemption | Each NGO must assess whether program evaluation qualifies |
