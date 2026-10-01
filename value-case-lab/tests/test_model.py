import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('value_model', Path(__file__).resolve().parents[1] / 'model.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
calculate = module.calculate


class ValueModelTests(unittest.TestCase):
    def setUp(self):
        self.inputs = dict(people=10, hours_per_week=4, weeks_per_year=48, hourly_cost=60,
                           time_reduction=.5, adoption=.75, realization=.4, annual_cost=12000, setup_cost=3000)

    def test_hand_calculated_base(self):
        self.assertEqual(calculate(self.inputs), dict(
            annual_capacity_hours=720, annual_capacity_value=43200,
            modeled_annual_financial_benefit=17280, year_one_cost=15000,
            year_one_net_value=2280, year_one_roi_percent=15.2,
            steady_state_payback_months=6.82))

    def test_capacity_is_not_cash(self):
        self.inputs['realization'] = 0
        result = calculate(self.inputs)
        self.assertEqual(result['annual_capacity_value'], 43200)
        self.assertEqual(result['modeled_annual_financial_benefit'], 0)
        self.assertEqual(result['year_one_roi_percent'], -100)
        self.assertIsNone(result['steady_state_payback_months'])

    def test_zero_cost_roi_undefined(self):
        self.inputs.update(annual_cost=0, setup_cost=0)
        self.assertIsNone(calculate(self.inputs)['year_one_roi_percent'])
        self.assertEqual(calculate(self.inputs)['steady_state_payback_months'], 0)

    def test_zero_adoption(self):
        self.inputs['adoption'] = 0
        result = calculate(self.inputs)
        self.assertEqual(result['annual_capacity_hours'], 0)
        self.assertEqual(result['year_one_net_value'], -15000)

    def test_no_payback_when_recurring_cost_equals_benefit(self):
        self.inputs['annual_cost'] = 17280
        self.assertIsNone(calculate(self.inputs)['steady_state_payback_months'])

    def test_invalid_inputs(self):
        for key, bad in [('adoption', 1.1), ('realization', -1), ('hourly_cost', float('nan')),
                         ('people', True), ('people', '10'), ('weeks_per_year', 53),
                         ('setup_cost', float('inf')), ('hours_per_week', 169)]:
            with self.subTest(key=key, bad=bad):
                values = copy.deepcopy(self.inputs)
                values[key] = bad
                with self.assertRaises(ValueError):
                    calculate(values)
        del self.inputs['realization']
        with self.assertRaises(ValueError):
            calculate(self.inputs)

    def test_more_adoption_improves_value_without_changing_cost(self):
        before = calculate(self.inputs)
        self.inputs['adoption'] = 1
        after = calculate(self.inputs)
        self.assertGreater(after['year_one_net_value'], before['year_one_net_value'])
        self.assertEqual(after['year_one_cost'], before['year_one_cost'])


if __name__ == '__main__':
    unittest.main()
