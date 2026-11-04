"""Conservative demonstration policy for a human-reviewed expansion decision.

This checks declared evidence states; it does not verify source truth or extract
facts. Standard library only. Unknown evidence must never become a passing gate.
"""
import json
import sys

GATES = (
    "baseline_and_criteria", "results_achieved", "customer_acceptance",
    "delivery_readiness", "economics_reviewed", "decision_authority",
)


def assess(record):
    if not isinstance(record, dict):
        raise ValueError("input must be an object")
    allowed = set(GATES) | {"hard_stop", "description"}
    extra = set(record) - allowed
    if extra:
        raise ValueError("unexpected fields: " + ", ".join(sorted(extra)))
    evaluated = {}
    for name in (*GATES, "hard_stop"):
        item = record.get(name, {"value": None, "source": ""})
        if not isinstance(item, dict) or set(item) - {"value", "source"}:
            raise ValueError(f"{name}: expected value/source object")
        value = item.get("value")
        if value is not None and type(value) is not bool:
            raise ValueError(f"{name}: value must be true, false, or null")
        source = item.get("source", "")
        if not isinstance(source, str):
            raise ValueError(f"{name}: source must be a string")
        source = source.strip()
        evaluated[name] = {"value": value, "source": source,
                           "supported": value is not None and bool(source)}

    unknown = [name for name, item in evaluated.items() if not item["supported"]]
    failed = [name for name in GATES if evaluated[name]["value"] is False
              and evaluated[name]["supported"]]
    stop = evaluated["hard_stop"]
    # A reported hard stop is conservative even before supporting detail arrives.
    if stop["value"] is True:
        decision = "STOP"
        reasons = ["hard_stop reported; resolve before considering expansion"]
    elif unknown:
        decision = "INSUFFICIENT_EVIDENCE"
        reasons = ["unknown or unreferenced gate: " + name for name in unknown]
        reasons += ["known failed gate: " + name for name in failed]
    elif failed:
        decision = "REVISE"
        reasons = ["failed gate: " + name for name in failed]
    else:
        decision = "EXPAND"
        reasons = ["all declared gates pass with source locators; human decision required"]
    return {"policy": "demonstration-v1", "decision": decision,
            "reasons": reasons, "unknown_gates": unknown,
            "failed_gates": failed, "evidence": evaluated,
            "limitation": "Declared states only; source truth and business suitability are not verified."}


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 decision_gate.py input.json")
    with open(sys.argv[1], encoding="utf-8") as stream:
        record = json.load(stream)
    print(json.dumps(assess(record), indent=2, allow_nan=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, TypeError) as error:
        print(f"Input error: {error}", file=sys.stderr)
        sys.exit(2)
