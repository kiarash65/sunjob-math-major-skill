# Roadmap

This roadmap describes the intended evolution of SUNJOB Math Major Skill. It records planned work; it does not claim that future capabilities already exist.

## Current

- Persian-first decision-support workflow for Iranian mathematics-track students.
- Canonical `SKILL.md` entry point.
- ChatGPT adaptation in `chatgpt/`.
- Structured model: `SELF × BIAS × CAREER × REALITY → DECISION`.
- Decision-safety specification.
- Behavior-focused evaluation benchmark and scenario suite.
- Offline repository validation and GitHub Actions checks.
- Contributor, issue, PR, security, and maintainer documentation.
- Conceptual architecture for country and education-system adapters.

## Next

### 1. Country adapters
Define a clear adapter contract for jurisdiction-specific:

- admissions and eligibility rules;
- education pathways;
- program/major catalogs;
- official evidence sources;
- local terminology;
- local evaluation cases.

No country should be marked as supported until its adapter has been implemented and tested.

### 2. Reproducible evaluation
Build a repeatable way to run the benchmark across supported model configurations and store the evaluation protocol and results without presenting unverified scores as facts.

### 3. More behavioral cases
Expand coverage for:

- accessibility constraints;
- location and migration trade-offs;
- non-traditional education paths;
- conflicting family and personal constraints;
- changing interests over time;
- uncertainty after a preliminary recommendation.

### 4. Multilingual support
Separate language and cultural adaptation from the core decision logic so additional languages can be evaluated without silently changing the methodology.

### 5. Evidence tooling
Explore lightweight tooling for source capture, freshness checks, citation handling, and country-specific evidence packs while keeping the core Skill usable without network dependencies.

## Future

- Empirical studies of decision quality and user outcomes.
- Broader support for career exploration beyond university major selection.
- Researcher-friendly evaluation exports and comparison tooling.
- Community-maintained country and education-system adapters.
- Additional integrations for AI assistants that support open instruction/skill formats.

## Principles for roadmap changes

1. Preserve user agency.
2. Keep recommendations proportional to evidence.
3. Prefer current primary sources for current rules and facts.
4. Treat psychometric results as evidence, not deterministic prescriptions.
5. Validate meaningful behavior changes with cases or benchmarks.
6. Never manufacture adoption, usage, benchmark results, or impact metrics.
