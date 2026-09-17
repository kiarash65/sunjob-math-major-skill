# Maintainer Workflow

## Issue triage

Prioritize reports that affect factual correctness, unsafe behavior, reproducibility, or core decision quality. Label feature requests separately from behavioral defects.

## Pull request review

Review in this order:

1. correctness;
2. safety and uncertainty;
3. evaluation coverage;
4. documentation;
5. maintainability.

Behavior changes should include a reproducible scenario whenever practical.

## Release checklist

- [ ] validator passes
- [ ] critical evaluation cases reviewed
- [ ] no secrets or private data
- [ ] current-data claims are sourced and dated
- [ ] user-visible behavior documented
- [ ] changelog updated
- [ ] version and release notes agree

## Versioning

Use semantic versioning for public releases. Patch releases fix documentation or non-behavioral defects; minor releases add backward-compatible capabilities; major releases may change the public behavior or structure in incompatible ways.
