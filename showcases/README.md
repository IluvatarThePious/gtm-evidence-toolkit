# Five commercial decisions, five work samples
**Peter Ryther · Enterprise sales and practical AI workflows**

These work samples show how I turn ambiguous sales work into inspectable decisions. Each includes a reusable assistant configuration, fictional input, worked reference, evaluation cases, and an application build plan.

| Start here | Business decision | What to inspect |
|---|---|---|
| [Deal Evidence Copilot](deal-evidence/README.md) | What did the buyer actually agree to? | Tentative meeting versus confirmed action |
| [Value Case Lab](value-case/README.md) | Is the economic case supported? | Capacity versus modeled financial benefit |
| [Pilot-to-Expansion](pilot-to-expansion/README.md) | Should a successful pilot expand? | Delivery readiness and decision evidence |
| [Customer Proof Sprint](customer-proof/README.md) | Which customer claims can we defend? | Bounded metrics and rejected claims |
| [Buyer Value Framework](buyer-value-framework/README.md) | Why should a buyer investigate this? | Buyer outcomes, neutral criteria, and fair differentiation |

**For recruiters:** start with Deal Evidence and inspect one source-to-output decision. **For sales leaders:** start with Pilot-to-Expansion and its coaching example. **For CEOs:** start with Value Case Lab, then Buyer Value Framework.

## Try the reusable assistant
Use the [shared router](../reusable-assistant/instructions.md) with one selected mode's instructions and its fictional input. Each mode is also self-contained. The [configuration guide](../reusable-assistant/README.md) defines knowledge boundaries and setup.

## Run the deterministic examples
Python 3.10+; standard library only. Run from the repository root:
```sh
python3 value-case-lab/model.py value-case-lab/example.json
python3 showcases/pilot-to-expansion/decision_gate.py showcases/pilot-to-expansion/example.json
python3 -m unittest discover -s value-case-lab/tests -v
python3 -m unittest discover -s showcases/pilot-to-expansion/tests -v
```

The text references are authored examples, not live model benchmarks. The code evaluates numeric inputs and gate states; it does not extract facts or verify the truth of source documents. All scenarios are synthetic. [Validation](VALIDATION.md) · [Provenance](PROVENANCE.md) · [Build sequence](ROADMAP.md).

This release extends existing public workflow kits. It is five curated work samples, not five recovered production applications or five new customer wins.
