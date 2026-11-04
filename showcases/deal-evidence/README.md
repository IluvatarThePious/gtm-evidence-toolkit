# Deal Evidence Copilot
**Turn a call into a source-linked decision record and an honest follow-up.**

Audience: Enterprise sellers and sales managers; recruiters can inspect how uncertainty is handled.

## Try it in five minutes
1. Read [the fictional input](example-input.md).
2. Paste [the reusable instructions](instructions.md) and that input into your chosen assistant.
3. Compare its result with [the authored reference](reference-output.md).
4. Check the [failure cases](evaluation.json). These expectations are not recorded model results.

## Why this belongs in the portfolio
Discovery discipline, clear customer communication, and coaching others to distinguish interest from commitment.

The key judgment: **A tentative Friday conversation must remain a proposal; a buyer describing a pain does not prove budget approval.**

## From one-off work to reusable workflow
Generalizes the transcript-to-follow-up workflow and privately configured sales-analysis assistant. This is an extension of the published Call to Commitment project.

Existing foundation: The repository already contains a vendor-neutral prompt, synthetic call, reference response, and manual failure cases in call-to-commitment/.

Reusable pipeline: Number source lines → extract attributed claims → reconcile conflicts → classify commitments → identify one coaching opportunity → draft a follow-up → check every promise and date.

Required inputs: Required: transcript or substantive call notes with speaker labels; seller and buyer identities; audience. Optional: call date/timezone, approved resources, approved product capabilities, desired email style. If speaker attribution is absent, mark it unknown.

## What is delivered
Independent reusable instructions, a fictional source pack, an authored reference answer, five evaluation fixtures, and a [concrete build plan](BUILD_PLAN.md). No original customer records, GPT attachments, or employer templates are included.

## Contribution and limits
Peter selected the original commercial problems and supplied the task direction. AI assisted reconstruction, generalization, code, examples, and documentation. This work demonstrates an approach; it does not establish customer deployment, measured outcomes, formal people-management history, or independent model quality. See [release provenance](../PROVENANCE.md).
