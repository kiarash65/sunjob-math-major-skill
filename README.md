# 🎓 SUNJOB Math Major Skill v3.3.0

<p align="center">
  <img src="https://img.shields.io/badge/Language-Farsi%20(Persian)-blue?style=flat-square" alt="Persian" />
  <img src="https://img.shields.io/badge/Claude-Skill-green?style=flat-square" alt="Claude Skill" />
  <img src="https://img.shields.io/badge/ChatGPT-Master%20Prompt-green?style=flat-square" alt="ChatGPT Master Prompt" />
  <img src="https://img.shields.io/badge/Version-3.3.0-orange?style=flat-square" alt="v3.3.0" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT" />
</p>

<p align="center">
  <strong>اسکیل تخصصی انتخاب رشته کنکور ریاضی با هوش مصنوعی</strong><br/>
  AI-assisted, structured decision support for university major selection and career discovery for Iranian mathematics-track students.
</p>

<p align="center">
  <a href="https://sunjob.ir"><strong>🌐 SUNJOB</strong></a> ·
  <a href="https://t.me/sunjob1"><strong>📱 Telegram</strong></a> ·
  <a href="https://github.com/kiarash65/sunjob-math-major-skill/archive/refs/heads/main.zip"><strong>⬇️ Download ZIP</strong></a>
</p>

---

## What this project is

SUNJOB Math Major Skill is an open-source AI instruction framework for helping students think through university major and career decisions.

The current adapter is designed for **Iranian mathematics-track students**. The underlying decision workflow is intentionally broader than a single exam, major, or ranking system so it can be adapted to other education systems later.

This is **decision support, not a guarantee or an admissions predictor**. It helps an AI collect better evidence, expose trade-offs, preserve uncertainty, and suggest useful next steps.

## چرا ساخته شده؟

انتخاب رشته خیلی وقت‌ها به یک سؤال تقلیل پیدا می‌کند:

> «با این رتبه چی میارم؟»

این Skill تلاش می‌کند سؤال را یک مرحله عمیق‌تر کند:

> «با توجه به شرایط، ترجیحات، محدودیت‌ها و شناخت من از مسیر، کدام گزینه‌ها ارزش بررسی بیشتری دارند و برای تصمیم چه چیزهایی هنوز نامعلوم است؟»

رتبه مهم است، اما فقط یکی از داده‌های feasibility است؛ نه تعریف کامل انتخاب.

---

## Core model

```text
SELF × BIAS × CAREER × REALITY → DECISION
```

| Layer | Focus |
|---|---|
| SELF | interests, values, strengths, work preferences, goals |
| BIAS | prestige, rank anchoring, family pressure, salary stories, social proof |
| CAREER | what the field actually studies and what real work can look like |
| REALITY | admission rules, location, constraints, opportunities, uncertainty, current evidence |
| DECISION | a reasoned comparison plus the next useful evidence-building step |

The framework is designed to distinguish **fit** from **feasibility** and to make uncertainty visible instead of hiding it behind a confident answer.

---

## What it does

The Skill can guide an AI to:

- build a structured profile of the student;
- ask high-information questions instead of interrogating the user;
- identify several plausible major/career directions;
- explain fit, mismatch risks, trade-offs, and unknowns;
- integrate user-provided assessment results;
- research current facts when the decision depends on them;
- separate facts from inference and hypothesis;
- recommend small real-world experiments when descriptions are not enough;
- keep confidence proportional to the available evidence.

### What it does not do

It should not:

- guarantee admission or predict an exact outcome from incomplete variables;
- treat one psychometric test as a deterministic major assignment;
- invent ranks, capacities, salaries, rules, or market statistics;
- pretend historical data is current-cycle evidence;
- make the student's decision for them when the evidence is insufficient.

---

## Quick start

### Claude

Use the repository as a Skill package when your Claude environment supports Skills. The canonical entry point is:

[`SKILL.md`](SKILL.md)

### ChatGPT

For environments with Skill support, use the package and keep `SKILL.md` as the canonical entry point.

For a portable setup, use:

[`chatgpt/CHATGPT-MASTER-PROMPT.txt`](chatgpt/CHATGPT-MASTER-PROMPT.txt)

### Other AI tools

Depending on the product, `SKILL.md` can be adapted as system instructions, project instructions, a knowledge file, or an uploaded instruction file. Follow the target product's own import rules.

---

## Evidence and research discipline

When a claim depends on time, jurisdiction, admission policy, university rules, capacities, employment conditions, or other changing facts, the Skill instructs the model to seek **current and authoritative evidence**.

The framework prefers primary and official sources for current education-system facts. Older data can provide historical context, but it should not silently become a guarantee for the current cycle.

For behavioral claims, the repository distinguishes evidence, inference, and hypothesis. Unsupported certainty is treated as a quality failure.

---

## Assessment discipline

The framework can interpret user-provided results from tools such as:

- Holland / RIASEC
- Work Values
- Career Self-Efficacy
- MBTI
- Big Five
- Blind Spots

A test result is treated as **one evidence stream among several**. The Skill explicitly avoids turning a single assessment into a deterministic statement such as “this test proves you should study X.”

---

## Evaluation

Behavior is evaluated with repository scenarios and a dedicated decision benchmark.

### Benchmark dimensions

1. Evidence discipline
2. Uncertainty calibration
3. Bias awareness
4. Career realism
5. Assessment discipline
6. Trade-off quality
7. Information efficiency
8. User agency
9. Current-data discipline
10. Next-step quality

See:

- [`evaluations/benchmark.md`](evaluations/benchmark.md)
- [`evaluations/cases.md`](evaluations/cases.md)
- [`evaluations/README.md`](evaluations/README.md)
- [`evaluations/RELEASE-GATE.md`](evaluations/RELEASE-GATE.md)

The repository does **not** publish made-up benchmark scores. A release gate can define thresholds without pretending that an evaluation was run when it was not.

---

## Repository quality controls

The project includes:

- `scripts/validate_repository.py` — offline structural and basic safety validation
- `.github/workflows/validate.yml` — validation on push and pull request
- `AGENTS.md` — maintainer and agent operating guidance
- `DECISION-SAFETY.md` — decision-support safety specification
- `SECURITY.md` — security and sensitive-data guidance
- `CONTRIBUTING.md` — contribution rules
- `.github/ISSUE_TEMPLATE/` — bug, feature, and evaluation-case templates
- `.github/PULL_REQUEST_TEMPLATE.md` — review checklist
- `docs/ADAPTERS.md` — country and education-system adapter architecture
- `docs/MAINTAINER_WORKFLOW.md` — issue, PR, and release workflow

Run locally with:

```bash
python scripts/validate_repository.py
```

The validator is intentionally offline and dependency-light. Model quality itself is evaluated through the conversation scenarios and benchmark rather than by the structural validator alone.

---

## Country-adaptable architecture

The current implementation is intentionally split conceptually into:

```text
Core decision framework
        ↓
Country / education-system adapter
        ↓
Local programs, rules, constraints and evidence
        ↓
Student context
        ↓
Evidence-informed decision support
```

A future adapter should not claim coverage for a country or admission system until its local rules, sources, and evaluation cases have actually been implemented and tested.

See [`docs/ADAPTERS.md`](docs/ADAPTERS.md).

---

## Examples

Start with:

- [`examples/sample-prompts.md`](examples/sample-prompts.md)
- [`examples/scenarios.md`](examples/scenarios.md)

These examples are intended to make the decision logic inspectable and easier to evaluate.

---

## Development and contribution

See:

- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`AUTHORING.md`](AUTHORING.md)
- [`AGENTS.md`](AGENTS.md)
- [`CHANGELOG.md`](CHANGELOG.md)
- [`ROADMAP.md`](ROADMAP.md)

Meaningful changes to the decision behavior should update the relevant evaluation cases and document their evidence and uncertainty.

---

## Safety and privacy

This repository should not contain:

- API keys or credentials;
- private student records;
- confidential organizational data;
- real personal data in examples or benchmark cases.

Use synthetic or properly anonymized examples for student scenarios.

Read [`DECISION-SAFETY.md`](DECISION-SAFETY.md) and [`SECURITY.md`](SECURITY.md) before extending the framework.

---

## License

This project is released under the [MIT License](LICENSE).

## Project

SUNJOB Academy  
Website: https://sunjob.ir  
GitHub: https://github.com/kiarash65/sunjob-math-major-skill  
Telegram: https://t.me/sunjob1
