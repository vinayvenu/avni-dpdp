Avni is a field data collection application that is used by field-workers in non-profits to collect data of beneficiaries. Information collected can include health information, education, social background etc.

Field workers can have either an offline Android application which has a local Realm database, or use the Data Entry Application - a browser-based version of it.

Avni is connected to the Avni cloud, which is maintained by an organisation called Samanvay. All data is stored here. The Avni cloud resides in the AWS data center in Mumbai. All files - images etc, are stored in S3.

---

## Clarification Questions

The following questions need to be answered to complete the DPDP security requirements analysis. They are grouped by the component or area they relate to.

### Mobile App (Android / Realm)

1. **Mobile encryption enforcement**: The infrastructure doc states AES-256 encryption for the Realm database "needs to be enabled for an organisation." Is this enforced as mandatory for all NGO partners, or left to each NGO's discretion? If optional, who is responsible for ensuring it is turned on before an NGO goes live?

2. **Device management**: Are there any MDM (Mobile Device Management) controls on field worker Android devices? Specifically — what happens to the Realm database and its data when a field worker's device is lost, stolen, or when the field worker leaves the NGO?
   > **Answer:** No MDM. Most field workers use personal phones; NGOs do not have funds for dedicated devices, making MDM impractical. If a device is lost or stolen, the user account can be revoked (cutting off server sync), but the Realm database on the device cannot be remotely wiped.

3. **App update enforcement**: Can field workers continue using older versions of the Android app that may have known vulnerabilities? Is there a mechanism to force app updates?

### Monitoring & Observability Tools (NewRelic, Bugsnag, Firebase)

4. **PII in monitoring tools**: The infrastructure doc says no beneficiary information is shared with NewRelic, Bugsnag, or Firebase. However, Bugsnag captures "stack traces, username, phone characteristics" and NewRelic captures "base URLs." Could beneficiary identifiers (e.g., names, IDs, phone numbers) appear in API URL paths (e.g., `/api/subject/12345`), request payloads in stack traces, or error messages? Is there a scrubbing or masking mechanism in place for these tools?
   > **Answer:** PII does not leak into NewRelic or Bugsnag. ✓

5. **Firebase Analytics scope**: Firebase captures "performance of page views, events." Does this include any event properties that reference beneficiary records (e.g., form IDs tied to a beneficiary)?

### Logging & Audit (Cloudwatch)

6. **Cloudwatch log retention period**: What is the current log retention period configured in Cloudwatch? DPDP Rules 2025, Rule 6(e) requires a minimum of 1 year. Rule 8(3) also requires 1-year minimum retention of processing logs.

7. **Application-level access logs**: Cloudwatch covers infrastructure and server logs. Are there separate application-level audit logs that record which authenticated user (field worker / admin) accessed or modified which specific beneficiary's record? Rule 6(c) specifically requires "visibility on the accessing of such personal data" — server logs alone may not satisfy this.

8. **Breach detection / alerting**: Is there any automated alerting on access log anomalies — e.g., bulk data exports by a single user, repeated failed login attempts, access from unusual geographies or times?

### Bulk Data Export & Reporting

9. **Spreadsheet export access controls**: The infrastructure doc explicitly notes "no additional protection of PII or any other sensitive information once downloaded from the system in the form of spreadsheets." Which user roles have permission to perform bulk data exports? Is there a log of who exported what data and when?

10. **BI layer (Metabase / Superset) security**: Do the Metabase and Superset dashboards enforce the same RBAC and catchment-based data restrictions as the main Avni app? Can a BI user access raw beneficiary PII through a custom query? Are these dashboards accessible from outside the VPC?
    > **Answer:** Access controls exist at the report level (by report name). Writing new reports (which could expose raw PII) can be restricted, but this is not currently enforced — it can be added on a per-tenant basis.

### Integration Server

11. **External integrations**: What external systems does the Integration Server connect to? Does it transmit personal data (including beneficiary data) to any external system? If so, are data processing agreements in place with those systems?

### Breach Response

12. **Breach notification responsibility**: Rule 7 of DPDP Rules 2025 requires notifying affected Data Principals "without delay" and the Data Protection Board within 72 hours of becoming aware of a breach. Who within Samanvay or the implementing NGO is responsible for triggering this process? Is there a documented incident response plan?

13. **Breach detection to notification pipeline**: How does Samanvay currently detect a breach? Is there a documented process from detection → internal escalation → NGO notification → Board notification?

### Multi-tenancy & Tenant Isolation

14. **Multi-tenant isolation**: Avni serves multiple NGOs on shared infrastructure. Is tenant isolation enforced at the PostgreSQL database level (e.g., separate schemas or row-level policies), or only at the application layer (RBAC)? A breach of the application layer could potentially expose data across tenants if isolation is only application-level.
    > **Answer:** Isolation is at the PostgreSQL level — each tenant has a separate DB user with access restricted to their own tenant's data only. ✓

### Security Audits

15. **Audit cadence and scope**: The infrastructure doc mentions security audits are performed "on demand." Is there a plan to move to periodic audits (e.g., annual)? Do the audits cover the Android app as well as the web app and server, or only specific deployments?

### Data Entry App (Web / Browser)

16. **Session management**: Does the browser-based Data Entry Application terminate sessions on browser close or tab close, or do JWT tokens persist? Given field workers may share devices, this is relevant to unauthorized access risk.