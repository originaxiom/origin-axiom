"""Reporting supplement only: frozen R77 mathematics is imported unchanged."""
import importlib.util
import json
from pathlib import Path


def normalize(groups):
    answer = {}
    for key, group in groups.items():
        out = dict(group)
        checks = {}
        for name, value in group['checks'].items():
            if type(value) is bool:
                checks[name] = value
            elif (type(value).__module__ == 'sympy.logic.boolalg'
                  and type(value).__name__ in {'BooleanTrue', 'BooleanFalse'}):
                checks[name] = bool(value)
            else:
                raise TypeError('non-ground/non-boolean check: '+name)
        out['checks'] = checks
        answer[key] = out
    flags = [b for group in answer.values() for b in group['checks'].values()]
    return {'groups': answer, 'passed': sum(flags), 'total': len(flags),
            'all_checks_pass': all(flags),
            'scope': 'ADDED relaxed classical source model; no physical admission or TOE'}


def native():
    path = Path(__file__).with_name('source_core.py')
    spec = importlib.util.spec_from_file_location('r77_frozen_native', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run():
    m = native()
    return normalize({name: function() for name, function in (
        ('image', m.image_controls), ('action', m.action_controls),
        ('localization', m.localization_controls), ('profiles', m.profile_controls),
        ('duality', m.duality_controls))})


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, sort_keys=True, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
