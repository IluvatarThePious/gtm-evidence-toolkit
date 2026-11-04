# Value Case Lab — next release plan
## Minimum credible release
This release supplies reusable instructions, a synthetic input, an authored reference, and explicit failure cases. The pilot mode also includes an executable gate checker; Value Case Lab uses the existing tested calculator. This is not a hosted AI application.

## Next application increment
Estimated engineering and review effort: **5–8 focused hours**. Estimates exclude recruitment/scheduling and assume one implementer with access to the approved source pack. They are planning estimates, not commitments.

1. Add an input form with units and evidence labels (2–3h).
2. Expose downside/base/upside and assumption sensitivity (1–2h).
3. Add downloadable decision memo and preserve undefined outputs (1h).
4. Test with a seller and a financially literate reviewer (1–2h plus availability).

## Dependencies
Current module: a text assistant and supplied sources; no paid API or CRM required. Application increment: a chosen runtime, explicit model access if using AI, a review interface, and test participants. Optional live research must cite inspected primary sources. No automatic external actions are required.

## Acceptance criteria
UI and exported memo match the calculator on all fixtures; missing realization never becomes a default; capacity never appears as measured savings; ramp limitation visible.

Run every case in evaluation.json at least twice with the exact same instruction version and record the model, date, inputs, output, reviewer corrections, and outcome. Repeat in a second industry to assess portability. Any invented commitment, source, outcome, or approval blocks a production-readiness claim. Public examples can remain clearly labeled prototypes while evaluations are incomplete.

## Demonstration script
Change realization from 40% to zero while leaving time saved unchanged. Explain why capacity value persists while modeled financial ROI becomes negative.

## Honest impact measurement
Record task completion time, material edits, unsupported claims, and whether an unfamiliar user can finish the task. Compare against the user's usual workflow on comparable inputs before claiming time savings. Do not infer sales or hiring impact from a working demo.
