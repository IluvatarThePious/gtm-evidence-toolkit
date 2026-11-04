# Validation record — November 3, 2026

## Checks executed

- Existing Value Case Lab: **7 tests passed**. Coverage includes hand-calculated base output, zero realization/adoption, undefined zero-cost ROI, nonpayback, invalid numbers, and sensitivity to adoption.
- New Pilot-to-Expansion checker: **9 tests passed**. Coverage includes failed readiness, all-pass, unknown values, missing evidence, hard stops, absent fields, rejected malformed types, and CLI behavior.
- One pilot test exhaustively checks **729 combinations** of six true/false/unknown gates with a supported false hard stop. Expansion is possible only when all six gates are true. Hard-stop precedence is tested separately.
- Ran both command-line examples. The fictional value base case yields 720 capacity hours, $43,200 capacity value, $17,280 modeled financial benefit, and 15.2% year-one ROI. The pilot fixture yields REVISE due to delivery readiness.

Commands from the repository root:
```sh
python3 -m unittest discover -s value-case-lab/tests -v
python3 -m unittest discover -s showcases/pilot-to-expansion/tests -v
python3 value-case-lab/model.py value-case-lab/example.json
python3 showcases/pilot-to-expansion/decision_gate.py showcases/pilot-to-expansion/example.json
```

## What these checks do not establish

The Python code checks arithmetic and declared gate states. It does not verify source authenticity, extract facts from transcripts, prove ROI, or approve an expansion. A source locator's presence is not proof of its truth. The authored demonstration gate policy is not a universal rule for every company.

The five text reference outputs are authored examples. **The 25 AI evaluation fixtures have not been executed against live models.** No prompt reliability benchmark, independent user trial, customer adoption, time-savings outcome, or hiring result is claimed.

To evaluate the assistant, record the model/version, exact module, input, raw output, reviewer corrections, and verdict for every fixture. Critical failures are invented evidence, commitments, customer outcomes, permissions, or cross-seller capabilities. Resolve these before describing the assistant as production-ready.
