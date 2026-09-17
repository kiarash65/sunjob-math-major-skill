# Changelog

All notable changes to SUNJOB Math Major Skill are documented here.

## 3.3.0 — 2026-09-17

### Added
- Decision-safety specification and maintainer guidance for high-impact educational decision support.
- Behavior-focused decision benchmark and compact evaluation cases.
- Offline repository validator with structural, metadata, and basic secret-pattern checks.
- GitHub Actions validation on push and pull request.
- Issue templates for bugs, feature requests, and evaluation cases.
- Pull request review checklist.
- Country/education-system adapter architecture documentation.
- Maintainer workflow documentation.
- Security policy and citation metadata for public use.
- Roadmap documenting current, next, and future work.

### Improved
- README rewritten around the actual project contract, evaluation approach, safety boundaries, and contribution workflow.
- Validator changed from a hard-coded version check to semantic-version-aware validation based on `manifest.json`.
- Manifest and citation metadata updated to `3.3.0`.
- Documentation now explicitly distinguishes decision support from admissions prediction or guaranteed outcomes.

### Quality rules
- No fabricated adoption, usage, benchmark results, rankings, capacities, salary figures, or current-cycle claims.
- No deterministic major recommendation from a single psychometric assessment.
- Current education-system claims require current authoritative evidence.

## 3.2.0 — 2026-08-31

### Added
- Persian-first conversational major-selection workflow for Iranian mathematics-track students.
- Multi-turn continuity and opening-introduction discipline.
- Structured decision model: `SELF × BIAS × CAREER × REALITY → DECISION`.
- Recommendation confidence calibration.
- Psychometric interpretation discipline across Holland, Work Values, Career Self-Efficacy, MBTI, and Big Five.
- Minimum-variable protocol for rank and admission questions.
- Current-cycle research protocol with source hierarchy and historical-cutoff safeguards.
- Bias and contradiction detection.
- Experience-first guidance and evidence-building suggestions.
- ChatGPT-specific adaptation in `chatgpt/`.
- Evaluation scenarios, rubric, and launch checklist.

### Packaging
- Canonical entry point: `SKILL.md`.
- Machine-readable metadata: `manifest.json`.
- Public MIT license.

## Release policy

Patch releases (`3.3.x`) should preserve the core workflow and avoid breaking changes. Minor/major changes should be documented here with migration notes when the instruction contract changes.
