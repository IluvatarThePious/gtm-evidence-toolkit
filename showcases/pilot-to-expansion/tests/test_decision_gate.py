import copy
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pilot_gate", ROOT / "decision_gate.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DecisionGateTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / "example.json").read_text())

    def test_readiness_blocks_successful_pilot(self):
        result = MODULE.assess(self.record)
        self.assertEqual(result["decision"], "REVISE")
        self.assertEqual(result["failed_gates"], ["delivery_readiness"])

    def test_supported_all_pass_is_recommendation(self):
        self.record["delivery_readiness"]["value"] = True
        result = MODULE.assess(self.record)
        self.assertEqual(result["decision"], "EXPAND")
        self.assertIn("human decision", result["reasons"][0])

    def test_unknown_cannot_expand(self):
        for gate in (*MODULE.GATES, "hard_stop"):
            with self.subTest(gate=gate):
                record = copy.deepcopy(self.record)
                record[gate]["value"] = None
                self.assertEqual(MODULE.assess(record)["decision"], "INSUFFICIENT_EVIDENCE")

    def test_missing_source_cannot_pass(self):
        self.record["delivery_readiness"]["value"] = True
        self.record["customer_acceptance"]["source"] = "   "
        self.assertEqual(MODULE.assess(self.record)["decision"], "INSUFFICIENT_EVIDENCE")

    def test_hard_stop_dominates_unknown_and_success(self):
        self.record["hard_stop"] = {"value": True, "source": "incident record"}
        self.record["customer_acceptance"]["value"] = None
        self.assertEqual(MODULE.assess(self.record)["decision"], "STOP")
        self.record["hard_stop"]["source"] = ""
        self.assertEqual(MODULE.assess(self.record)["decision"], "STOP")

    def test_missing_fields_remain_unknown(self):
        self.assertEqual(MODULE.assess({})["decision"], "INSUFFICIENT_EVIDENCE")

    def test_strings_numbers_and_unknown_fields_rejected(self):
        for bad in ("true", "false", 1, 0, [], {}):
            with self.subTest(bad=bad):
                record = copy.deepcopy(self.record)
                record["customer_acceptance"]["value"] = bad
                with self.assertRaises(ValueError):
                    MODULE.assess(record)
        record = copy.deepcopy(self.record)
        record["customer_acceptence"] = record.pop("customer_acceptance")
        with self.assertRaises(ValueError):
            MODULE.assess(record)

    def test_exhaustive_gate_states_never_expand_with_gap(self):
        for values in itertools.product((True, False, None), repeat=len(MODULE.GATES)):
            record = {k: {"value": v, "source": "fixture"} for k, v in zip(MODULE.GATES, values)}
            record["hard_stop"] = {"value": False, "source": "fixture"}
            expands = MODULE.assess(record)["decision"] == "EXPAND"
            self.assertEqual(expands, all(v is True for v in values))

    def test_cli_contract_and_malformed_input(self):
        result = subprocess.run([sys.executable, str(ROOT / "decision_gate.py"), str(ROOT / "example.json")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["decision"], "REVISE")
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "bad.json"
            p.write_text('{"hard_stop":')
            bad = subprocess.run([sys.executable, str(ROOT / "decision_gate.py"), str(p)], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 2)
            self.assertIn("Input error", bad.stderr)


if __name__ == "__main__":
    unittest.main()
