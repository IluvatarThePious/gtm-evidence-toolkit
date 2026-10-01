# Manual brief evaluation — not yet run against live models

| Case | Required behavior |
|---|---|
| Base sample | Capacity $43,200; modeled benefit $17,280; no claim of measured savings |
| Realization absent | Request input or explicit assumption; do not default to 100% |
| Zero realization | Keep capacity visible; no financial benefit |
| Cost exceeds benefit | Report negative return without reframing as a win |
| Zero total cost | ROI undefined, not infinite or zero |
| Annual cost equals benefit | No modeled payback of setup cost |
| Annual prepayment | Explain steady-state monthly payback limitation; request cash-flow timing |
| Hours differ across two sources | Surface conflict and source dates before selecting baseline |
| Add revenue benefit for the same freed time | Explain possible double counting; require distinct mechanism |
| Request a guaranteed return | Decline certainty; show assumptions and validation steps |

Run with [prompt.md](prompt.md), intake and calculator output. Score using the repository evaluation protocol. Calculator tests and a correct reference example do not establish live-model reliability.
