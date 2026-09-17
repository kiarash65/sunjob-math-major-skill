# AGENTS.md

## Project purpose
SUNJOB Math Major Skill is an open-source, evidence-informed decision-support framework for university major and career exploration. It currently focuses on Iranian mathematics-track students and is designed to support future country-specific adapters.

## Repository principles
- Decision support, not deterministic career assignment.
- Separate evidence, inference, uncertainty, and user preference.
- Never fabricate admission rules, ranks, capacities, salaries, employment statistics, or test results.
- Historical data must be labeled historical.
- Psychometric assessments are supporting evidence, never destiny.
- Prefer primary/current sources when claims are time-sensitive.
- Surface trade-offs and missing information.

## Before changing the core skill
1. Read `SKILL.md` and the relevant files under `references/`.
2. Preserve the decision model and safety constraints unless the change explicitly updates them.
3. Add or update an evaluation case for meaningful behavioral changes.
4. Run the repository validator.
5. Update `CHANGELOG.md` when behavior or public interfaces change.

## Validation
Use the offline validator when available:

```bash
python scripts/validate_repository.py
```

Do not add network-dependent tests to the required local validation path.

## Evaluation
Behavioral changes should be checked against the scenarios in `evaluations/`. Prefer reproducible cases with explicit expected behaviors over subjective claims that an answer is "better".

## Contributions
Keep pull requests focused. Explain the problem, the proposed behavior, evaluation evidence, and any changes to assumptions or references.

## Security
Do not commit API keys, credentials, private student data, or other secrets. Treat user-provided educational and career information as sensitive. Review changes to instructions for prompt-injection and unsafe recommendation risks.
