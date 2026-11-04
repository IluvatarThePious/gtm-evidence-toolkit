# GTM Evidence Studio — portable assistant configuration
**One assistant, five focused modes.** This is an implementation-ready configuration package, not an installed or published custom GPT.

## Configuration contract
- Name: GTM Evidence Studio.
- Description: Turn supplied commercial evidence into honest follow-ups, value cases, pilot decisions, customer proof, and buyer messaging.
- Base instructions: [instructions.md](instructions.md).
- Required knowledge: each selected mode's instructions.md; the public fictional examples and evaluation cases as reference material.
- Optional tools: Python execution for the calculator and gate checker; read-only research for approved public sources. No actions, credentials, CRM writeback, or email sending are needed.
- Conversation starters: “Review this call and separate proposals from commitments”; “Pressure-test this capacity case”; “Should this pilot expand?”; “Which claims can this source pack support?”; “Build a buyer-value framework from these sources.”

## Setup without a platform dependency
Paste the chosen mode's instructions and its input into any suitable text assistant. The individual modules are self-contained. Alternatively, configure an assistant with the router and make the five mode files retrievable. Keep the deterministic Python files available in an execution environment when numerical checks are needed. Platform-specific import/install and GPT publication have not been performed.

## Knowledge-file policy
Keep seller product notes in separate labeled packs with seller, offering, version/date, source, and permitted audience. Load only the current seller's pack. Leave original private GPT attachments, customer transcripts, employer templates, and internal roadmaps out of public knowledge. Supplied synthetic records are the default demo data.

## Portability and failure behavior
The common schema is source ID → attributed claim → classification → decision → output. This generalizes across industries without assuming the same buyer roles, sales stages, metrics, or approval rules. Each mode asks for its own minimum input. Missing evidence yields a question or a visible gap, not invented detail. Conflicting sources remain unresolved until the responsible reviewer selects a supported interpretation.

## Evaluation before calling it production-ready
Run all 25 mode fixtures and repeat across two industries. Record prompt/module version, model/version, date, raw output, human corrections, and verdict. Keep authored references separate from actual model outputs. Any invented source, buyer agreement, outcome, or publication approval is a critical failure. Assess a second reviewer’s agreement on the judgments. Complete at least one observed user task before claiming usability.
