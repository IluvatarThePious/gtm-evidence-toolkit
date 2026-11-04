# Pilot-to-Expansion
**Connect commercial promise to evidence, delivery readiness, and an explicit expansion decision.**

Audience: Sales directors, VPs of Sales, CEOs, and cross-functional deployment teams.

## Try it in five minutes
1. Read [the fictional input](example-input.md).
2. Paste [the reusable instructions](instructions.md) and that input into your chosen assistant.
3. Compare its result with [the authored reference](reference-output.md).
4. Check the [failure cases](evaluation.json). These expectations are not recorded model results.

## Why this belongs in the portfolio
Management judgment, qualification, operational coordination, and disciplined expansion planning. This is a proposed operating approach, not proof of prior direct-report management.

The key judgment: **A successful pilot at one site does not establish readiness to expand at another site.**

## From one-off work to reusable workflow
Generalizes robotics GTM and buyer-entry planning. The companion enterprise-gtm-ai-portfolio repository already contains qualification, charter, and management-cadence templates.

Existing foundation: Published pilot templates and proposed manager cadence; this release adds a fictional decision case and a runnable evidence-gate checker.

Reusable pipeline: Define scope → compare results with agreed criteria → assess measurement/acceptance → check next-site delivery → check economics/authority → run the gate checker → recommend expand/revise/stop/insufficient evidence → assign the next evidence request.

Required inputs: Required: pilot scope and decision, success criteria, baseline evidence, observed results, customer acceptance, delivery readiness, economics review, decision authority, and blockers. Each gate is true/false/null with a source locator. Optional: agreed decision date, costs, adoption, incident log, next-site constraints. Unknown gates remain null.

## What is delivered
Independent reusable instructions, a fictional source pack, an authored reference answer, five evaluation fixtures, and a [concrete build plan](BUILD_PLAN.md). No original customer records, GPT attachments, or employer templates are included.

## Contribution and limits
Peter selected the original commercial problems and supplied the task direction. AI assisted reconstruction, generalization, code, examples, and documentation. This work demonstrates an approach; it does not establish customer deployment, measured outcomes, formal people-management history, or independent model quality. See [release provenance](../PROVENANCE.md).
