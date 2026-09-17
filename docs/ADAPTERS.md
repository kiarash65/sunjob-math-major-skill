# Country Adapter Architecture

SUNJOB Math Major Skill currently focuses on Iranian mathematics-track students. The decision framework is intentionally separated from country-specific admission and education data so that future contributors can adapt it to other systems.

## Separation of concerns

### Core
The core contains reusable decision-support behavior:

- self-discovery and preference elicitation;
- bias and contradiction detection;
- career/work analysis;
- assessment interpretation discipline;
- evidence and uncertainty handling;
- recommendation calibration;
- experience-first validation;
- safety requirements.

### Adapter
A country or education-system adapter should contain only local assumptions and data such as:

- education pathways;
- admission terminology;
- official admission authorities;
- geographic constraints;
- qualification structures;
- current rules and program availability.

## Adapter contract

An adapter should document:

1. scope and target population;
2. authoritative primary sources;
3. variables required for feasibility analysis;
4. time-sensitive fields;
5. historical-data policy;
6. known limitations;
7. examples and evaluation cases.

The core must not assume that an Iranian admission rule, exam, quota, degree structure, or terminology applies elsewhere.

## Planned expansion

```text
Core decision framework
        ↓
Country / education-system adapter
        ↓
Local programs + rules + constraints
        ↓
Student context
        ↓
Evidence-informed decision support
```

The existence of this architecture does not imply support for a country until a tested adapter and appropriate primary sources exist.
