# Value Case Lab

A small, inspectable calculator and prompt for an early business case. Its purpose is to expose the assumptions that make a purchase look attractive.

Run from the repository root:

```sh
python3 value-case-lab/model.py value-case-lab/example.json
python3 -m unittest discover -s value-case-lab/tests -v
```

Requires Python 3.10 or later, no dependencies. Results print to your terminal. [example-results.json](example-results.json) contains the supplied scenario outputs. All figures are fictional USD assumptions.

## Formula

Annual capacity hours = people × hours per person per week × weeks per year × time reduction × adoption.

Capacity value = capacity hours × hourly cost. Modeled financial benefit = capacity value × realization. Realization is an explicit assumption about how much capacity becomes incremental financial benefit; it is not proof that payroll falls or revenue rises.

Year-one ROI = (modeled annual financial benefit − annual recurring cost − setup cost) / (annual recurring cost + setup cost).

Payback = setup cost / monthly net recurring benefit. This assumes immediate steady-state adoption, evenly distributed benefits and monthly recurring costs. It is not a cash-flow forecast for annual prepayment. No positive recurring net benefit means no modeled payback (null). Zero total cost makes ROI undefined (null).

## Base example

The base scenario frees 720 annual capacity hours worth $43,200 at the assumed labor rate. At 40% financial realization, modeled benefit is $17,280. Against $15,000 year-one cost, modeled net value is $2,280 and ROI is 15.2%. The distinction between $43,200 capacity value and $17,280 modeled financial benefit is the central teaching point.

Do not add capacity value to financial benefit: they describe overlapping value. Include review, training, integration and administration in the relevant costs. If no financial realization mechanism is defensible, set realization to zero and report capacity separately.

## Limits

No tax, discounting, revenue uplift, risk avoidance, churn, implementation delays, monthly ramp or financing is modeled. These scenarios are judgments, not calibrated probabilities. The tool is not a certified or third-party-endorsed economic impact study. Spreadsheet or model outputs do not establish causality.

Use [intake.md](intake.md) to collect evidence and [prompt.md](prompt.md) to turn results into a brief. Build a form and sensitivity view only after users can correctly explain capacity versus financial benefit. Before a public app, run the [manual evaluation cases](evaluation.md) for missing inputs, zero-cost cases, negative returns and conflicting baselines.
