# Avni and DPDP Compliance — What You Need to Know

**Date:** April 2026
**From:** Samanvay Technologies (Avni Platform Team)
**For:** All Avni customers

---

## Background

India's Digital Personal Data Protection Act (DPDP) and Rules come into full force on **13 May 2027**. As an organisation that collects personal data of beneficiaries using Avni, you are a **Data Fiduciary** under this law. Samanvay, which hosts and maintains the Avni platform, is your **Data Processor**.

Both of us have obligations under DPDP. This note explains where Avni stands today, what we are building, and what you should start doing now.

---

## 1. Where Avni Stands Today

**What is already in place:**

- All data is stored encrypted at rest (AES-256) and in transit (TLS)
- Data resides exclusively in AWS Mumbai — no data leaves India
- Access is restricted to authenticated, authorised users only
- Basic audit trails exist (who created or modified a record)
- Android app encryption (Realm database) is available and can be enabled per organisation

**What is not yet in place:**

- No structured consent collection mechanism — field workers collect data without a formal, legally defensible consent step
- No erasure capability — "voiding" a record hides it but does not delete the underlying data
- No application-level access audit logging (who *viewed* a record is not tracked)
- No controls on bulk data exports (no logging, no role restrictions)
- No compliance reporting (consent status, erasure tracking, etc.)

---

## 2. Our Compliance Roadmap

We are building DPDP compliance into Avni as a core platform capability. All legally required features will be ready well before May 2027. Consent and erasure — the most critical pieces — are prioritised for completion by August 2026.

### June 2026 — Immediate controls
- Restrict report-creation access in the BI layer (Metabase/Superset) as a platform-wide default to prevent unauthorised access to raw personal data
- Begin sending the DPDP compliance addendum to existing customers for signature

### July 2026 — Consent collection
- Structured consent step during beneficiary registration — no data can be collected without completing this step first
- Two consent methods suited to field conditions:
  - **Audio recording** — field worker reads the notice aloud, records the beneficiary's verbal consent
  - **Signed form** — beneficiary signs a printed notice, field worker photographs the signed form
- Every consent is timestamped, linked to the beneficiary record, and stored with the notice version used

### August 2026 — Erasure and export controls
- Full data erasure workflow when consent is withdrawn — personal data is permanently deleted from cloud databases, file storage, Android devices, and analytics tables
- Erasure on written instruction from you (for rights requests from beneficiaries)
- Bulk export logging and role-based restrictions
- First compliance reports: Consent Registry, Export Log, and Erasure Status

### September–November 2026 — Rights management and audit logging
- Tracking tool for retrospective notice delivery to existing beneficiaries
- Log for Data Principal rights requests (access, correction, erasure)
- Application-level access audit logging (who viewed what, when)
- Reports: Outstanding Notice Delivery, Access Audit

### Q1 2027 — Security hardening
- Stronger authentication (periodic OTP verification for field workers)
- Session timeout controls for the web application
- Automated breach detection alerts
- Data retention monitoring (flagging records where the original purpose may no longer apply)
- Compliance dashboard for programme administrators

---

## 3. What You Should Start Doing Today

DPDP compliance is a shared responsibility. The platform will provide the tools, but several obligations fall directly on you as the Data Fiduciary. Here is what you can act on now:

### Sign the DPDP addendum
We will send you a compliance addendum to your existing contract. This formally establishes the Data Fiduciary / Data Processor relationship and each party's obligations under DPDP. **This must be signed before 13 May 2027.** We encourage you to review and sign it promptly.

### Enable Android encryption
If you haven't already, request us to enable AES-256 encryption for the Avni Android app (Realm database) for your organisation. Operating without this encryption may constitute a non-compliance with DPDP Rules.

### Prepare your privacy notice
Draft a DPDP-compliant notice that explains to your beneficiaries: what personal data you collect, why you collect it, and their rights under the law. This notice will be read aloud or presented as a printed form during the consent step in Avni. We can share a template to help you get started.

### Plan for retrospective notice delivery
All existing beneficiaries whose data was collected before May 2027 must receive a DPDP-compliant notice. For field programmes, this means physical revisits. Start planning the operational logistics — field schedules, worker assignments, geographic coverage — so you are ready to execute once the tracking tool is available in Avni (November 2026).

### Tighten BI and export access
Review who in your organisation has access to Metabase/Superset and bulk data exports. Ask us to configure report-creation restrictions before granting BI access to any new user. Ensure downloaded data is handled securely and deleted when no longer needed.

### Establish a device loss protocol
Set up an internal process so that if a field worker's device is lost or stolen, you notify us and request account revocation within 48 hours.

### Designate a DPDP point person
Identify someone in your organisation who will be responsible for DPDP compliance — handling rights requests from beneficiaries, coordinating notice delivery, and managing consent records. This does not need to be a full-time role, but it needs to be someone's explicit responsibility.

---

## Questions?

If you have questions about any of this, or need help getting started with any of the steps above, reach out to us. We are committed to making DPDP compliance as straightforward as possible for you and for the communities you serve.
