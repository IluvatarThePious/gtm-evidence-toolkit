# Value Case Lab
**Make the economics inspectable before asking a buyer to believe them.**

Audience: CFOs, CEOs, sales leaders, and enterprise sellers developing a business case.

## Try it in five minutes
1. Read [the fictional input](example-input.md).
2. Paste [the reusable instructions](instructions.md) and that input into your chosen assistant.
3. Compare its result with [the authored reference](reference-output.md).
4. Check the [failure cases](evaluation.json). These expectations are not recorded model results.

## Why this belongs in the portfolio
Quantitative value selling, financial clarity, sensitivity analysis, and a willingness to reject an unsupported ROI story.

The key judgment: **Released labor capacity is not automatically cash savings. A realization assumption is a scenario input, not evidence of savings.**

## From one-off work to reusable workflow
Generalizes ROI-briefing work into the already published deterministic value-case-lab calculator. This release adds an assistant contract and an evaluation/build plan.

Existing foundation: Python calculator, explicit input template, three synthetic scenarios, seven automated tests, prompt, and evaluation cases.

Reusable pipeline: Map the buyer workflow → classify all inputs → check units and period → run value-case-lab/model.py → inspect conservative/base/upside scenarios → explain the break-even driver → write a decision memo.

Required inputs: Required for numeric output: people, hours_per_week, weeks_per_year, hourly_cost, time_reduction, adoption, realization, annual_cost, setup_cost; common currency and annual period; evidence/assumption label for every input. Optional: measured redeployment mechanism and ramp schedule. Without realization evidence, keep it an explicit scenario assumption or leave financial ROI unavailable.

## What is delivered
Independent reusable instructions, a fictional source pack, an authored reference answer, five evaluation fixtures, and a [concrete build plan](BUILD_PLAN.md). No original customer records, GPT attachments, or employer templates are included.

## Contribution and limits
Peter selected the original commercial problems and supplied the task direction. AI assisted reconstruction, generalization, code, examples, and documentation. This work demonstrates an approach; it does not establish customer deployment, measured outcomes, formal people-management history, or independent model quality. See [release provenance](../PROVENANCE.md).
