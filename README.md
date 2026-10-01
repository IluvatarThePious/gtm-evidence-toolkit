# GTM Evidence Toolkit

**Turn a sales call into clear next steps. Pressure-test a business case. Answer career questions with evidence.**

Three practical workflows for enterprise sellers and GTM teams, with fictional examples you can inspect in five minutes and a Python calculator you can run without API keys.

**Start without installing anything:** [Read the call](call-to-commitment/example-input.md) → [see the reviewed follow-up](call-to-commitment/reference-output.md).

Prepared by Peter Ryther with AI assistance. These are newly generalized editions of workflows developed through enterprise-sales and career-preparation work. All examples are fictional. They demonstrate workflow design and commercial reasoning, not measured customer results or production deployments.

| Workflow | Try it | What it demonstrates |
|---|---|---|
| Call to Commitment | [Start here](call-to-commitment/README.md) | Separating what a buyer agreed to from what a seller proposes |
| Value Case Lab | [Start here](value-case-lab/README.md) | Transparent assumptions, conservative value math, and sensitivity |
| Career Evidence Companion | [Start here](career-evidence/README.md) | Accurate attribution, concise storytelling, and explicit experience gaps |

## Five-minute tour

1. Read the Call to Commitment fictional transcript and compare its evidence ledger with its email.
2. Run the Value Case Lab with Python 3.10 or later; no packages or API keys are required.
3. Try the Career Evidence prompt with its fictional record and a difficult question.

```sh
python3 value-case-lab/model.py value-case-lab/example.json
python3 -m unittest discover -s value-case-lab/tests -v
```

The prompts can be pasted into an AI assistant alongside their example inputs. Review outputs before use. They do not automatically send email, modify CRM records, or retrieve private files.

## What is ready

This release contains copyable prompts, structured intake templates, worked examples, a runnable calculator, automated arithmetic/input tests, and manual evaluation cases. Prompt quality has not been benchmarked across live models. The worked text outputs are authored reference answers, not recorded model runs. See [evaluation protocol](EVALUATION.md) and [provenance](PROVENANCE.md).

## Design choices

- Preserve source references next to claims.
- Keep missing information visible rather than filling it with plausible detail.
- Separate proposed actions from confirmed commitments.
- Keep time capacity, accounting savings, and revenue separate.
- Provide a useful result even when the right answer is “not established.”

## A decision worth checking

In the fictional value case, **$43,200 of capacity value becomes $17,280 of modeled financial benefit**, after an explicit 40% realization assumption. The result is **15.2% modeled year-one ROI**, not a claim of measured savings. [Inspect the inputs and formulas](value-case-lab/README.md).

## Help improve the workflows

Try one synthetic example and [open an issue](https://github.com/IluvatarThePious/gtm-evidence-toolkit/issues/new) with the workflow, what you expected, what happened, and the smallest fictional example that reproduces it. Especially useful feedback: an invented commitment, a confusing assumption, or a step that requires explanation. Please do not include customer transcripts, credentials, or private career records.

Next priorities: source-linked review for Call to Commitment, an input form for Value Case Lab, and an approved-evidence record for Career Evidence Companion. These are planned improvements, not available application features.

For pilot qualification and expansion planning, see the companion [Enterprise GTM & AI Portfolio](https://github.com/IluvatarThePious/enterprise-gtm-ai-portfolio).

Start with synthetic records. Only use real records you are authorized to process with your chosen assistant. This repository includes no employer collateral, customer transcripts, original GPT knowledge files, or personal résumé records.

This is a portable workflow kit, not an installable plugin or hosted application. Productizing it requires the acceptance checks in each project. No third-party framework endorsement is claimed. No open-source license is granted in this edition; inspect the examples, and contact the owner for reuse permission beyond applicable rights.
