"""Illustrative annual capacity model. Standard library only; no external calls."""
import json
import math
import sys

FIELDS = (
    'people', 'hours_per_week', 'weeks_per_year', 'hourly_cost',
    'time_reduction', 'adoption', 'realization', 'annual_cost', 'setup_cost'
)


def calculate(inputs):
    """Convert an explicit scenario to capacity value and modeled economics.

    realization is the assumed share of capacity value that becomes incremental
    financial benefit. It is not measured savings, and is never inferred.
    """
    values = {}
    for key in FIELDS:
        value = inputs.get(key)
        if isinstance(value, bool) or not isinstance(value, (float, int)):
            raise ValueError(f'{key}: provide a number')
        try:
            value = float(value)
        except (ValueError, OverflowError):
            raise ValueError(f'{key}: provide a finite number') from None
        if not math.isfinite(value) or value < 0:
            raise ValueError(f'{key}: must be finite and nonnegative')
        values[key] = value
    for key in ('time_reduction', 'adoption', 'realization'):
        if values[key] > 1:
            raise ValueError(f'{key}: must be between 0 and 1')
    if values['weeks_per_year'] > 52:
        raise ValueError('weeks_per_year: must not exceed 52')
    if values['hours_per_week'] > 168:
        raise ValueError('hours_per_week: must not exceed 168 per person')
    v = values
    hours = v['people'] * v['hours_per_week'] * v['weeks_per_year'] * v['time_reduction'] * v['adoption']
    capacity = hours * v['hourly_cost']
    benefit = capacity * v['realization']
    cost = v['annual_cost'] + v['setup_cost']
    net = benefit - cost
    recurring_net = benefit - v['annual_cost']
    # Steady-state approximation assumes equal monthly benefit and recurring cost.
    payback = v['setup_cost'] / (recurring_net / 12) if recurring_net > 0 else None
    result = {
        'annual_capacity_hours': hours,
        'annual_capacity_value': capacity,
        'modeled_annual_financial_benefit': benefit,
        'year_one_cost': cost,
        'year_one_net_value': net,
        'year_one_roi_percent': net / cost * 100 if cost > 0 else None,
        'steady_state_payback_months': payback,
    }
    if any(x is not None and not math.isfinite(x) for x in result.values()):
        raise ValueError('scenario exceeds supported numeric range')
    return {k: round(x, 2) if x is not None else None for k, x in result.items()}


def main():
    if len(sys.argv) != 2:
        raise ValueError('Usage: python3 model.py scenario-file.json')
    with open(sys.argv[1], encoding='utf-8') as source:
        data = json.load(source)
    scenarios = data['scenarios']
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError('scenarios: provide a nonempty list')
    output = [{'name': s['name'], 'result': calculate(s['inputs'])} for s in scenarios]
    print(json.dumps({'status': 'illustrative assumptions; not measured savings', 'scenarios': output}, indent=2, allow_nan=False))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'Input error: {error}', file=sys.stderr)
        sys.exit(2)
