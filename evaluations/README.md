# Evaluation Workflow

The evaluation set is designed to test behavior, not just formatting.

## Scenario suite

`../examples/scenarios.md` contains 14 realistic conversations covering:

- premature major fixation;
- family pressure;
- prestige and rank anchoring;
- income-only decisions;
- returned psychometric results;
- contradictions between values and interests;
- rank-based feasibility questions;
- uncertainty and low confidence;
- requests for binary answers;
- disagreement with the assistant;
- final decision moments.

## How to evaluate

Run each scenario in a fresh conversation unless the scenario explicitly says to continue. Judge the response against:

1. the expected behavior;
2. critical failure conditions;
3. the release gate in `RELEASE-GATE.md`.

## What a strong response should demonstrate

A strong response should:

- use the available context;
- ask only the next useful question;
- separate fit from feasibility;
- combine multiple evidence sources;
- surface trade-offs and contradictions;
- calibrate confidence;
- use current sources for current facts;
- avoid invented numbers and deterministic psychological claims;
- leave the student with a useful next step.

## Automated checks

The repository includes `scripts/validate_repository.py` for offline structural and basic safety validation. It does not pretend to evaluate model quality by itself; the conversation scenarios remain the behavioral evaluation set.
