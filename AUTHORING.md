# Skill Authoring Guide

This document is for maintainers developing future SUNJOB Skill releases.

## Core contract

The Skill must remain:

- evidence-aware;
- Persian-first for the intended audience;
- conversational rather than questionnaire-heavy;
- multi-turn and context-preserving;
- calibrated about uncertainty;
- non-deterministic in psychometric interpretation;
- careful with time-sensitive admission and labor-market facts.

## Decision model

Preserve the four-layer structure:

`SELF × BIAS × CAREER × REALITY → DECISION`

Do not let rank, prestige, salary, a single test, or a single user statement silently replace the other layers.

## Research contract

For current facts, prefer authoritative primary sources. Historical admission data must remain labeled as historical. Never turn estimates into guarantees.

## Psychometric contract

Tests are evidence about constructs, not verdicts about identity or destiny. Changes to test interpretation should be accompanied by evaluation scenarios showing the intended behavior.

## Release hygiene

Before a release:

1. update `CHANGELOG.md`;
2. update version metadata consistently;
3. review compatibility documentation;
4. run the repository validator;
5. review evaluation scenarios for regressions;
6. inspect the diff for secrets and unrelated changes.
