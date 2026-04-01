# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a knowledge repository for understanding and implementing compliance with India's **Digital Personal Data Protection (DPDP) Act** within the AVNI platform ecosystem. It contains no code — only legal documents, expert analysis articles, compliance templates, and reference materials organized for AVNI's data protection compliance work.

## Repository Structure

- **`law/`** — Primary legal sources: the DPDP Act itself and the DPDP Rules 2025. Start here for authoritative definitions and requirements.
- **`articles/`** — Expert analysis on DPDP implications specifically for nonprofits and social sector organizations.
- **`templates/`** — Ready-to-use compliance document templates (privacy policies, consent forms, data processing agreements, data breach notifications, cookie policies, etc.). `aadhaar_guidelines.pdf` is fully compliant with the DPDP Act and Rules and can be used directly without modification.
- **`avni_contracts/`** — Contract templates for AVNI's vendor/hosting relationships.
- **`videos`** — YouTube links to educational DPDP resources.
- **`video/`** — Transcripts of these videos

- Root-level PDF: Draft analysis of DPDP implications for NPOs by Centre for Advancement of Philanthropy.

## Key Context

Avni is a field data collection application that is used by field-workers in non-profits to collect data of beneficiaries. Information collected can include health information, education, social background etc. 

Field workers can have either an offline Android application which has a local Realm database, or use the Data Entry Application - a browser-based version of it. 

Avni is connected to the Avni cloud, which is maintained by an organisation called Samanvay. All data is stored here. The Avni cloud resides in the AWS data center in Mumbai. All files - images etc, are stored in S3. 

The DPDP materials are collected to guide AVNI's compliance posture. When answering questions or drafting documents:
- Articles and templates in this repo are tailored to the **nonprofit/social sector** interpretation of DPDP.
- The DPDP Rules 2025 (`law/rules.pdf`) are the most recent regulatory guidance and take precedence over older analysis.
- `articles/DPDP_Rules_2025_English_only.pdf` is a cleaner English-only extract of the rules.
