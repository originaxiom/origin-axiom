"""Pinned synthetic readout diagnostic; no cover population calculation."""
import hashlib
import json
import subprocess

PIN = '0762032d9fc20f62dba5779c8ed15f33bd2fb868'
SOURCE = 'frontier/B1538_the_puncture_characters/verification/read_out.py'
DIGEST = '20fa46968da38fa0ed3c44cb8e4d89147fa9983af179007844225c79359edf02'


def run():
    raw = subprocess.check_output(['git', 'show', PIN + ':' + SOURCE])
    assert hashlib.sha256(raw).hexdigest() == DIGEST
    scope = {'__name__': 'pinned_readout_diagnostic', '__file__': SOURCE}
    exec(compile(raw, SOURCE, 'exec'), scope)
    evaluate = scope['evaluate']
    ident = {'identity holds': True}
    base = {'cover': 'synthetic.one', 'chunks': 1, 'chunk': 0, 'read': True,
            'hits': [], 'state': 'm004',
            'route P': {'reads': 1, 'disagree': []},
            'route T': {'reads': 0, 'skipped': 0, 'disagree': []}}
    candidate = dict(base, hits=[{'n': 2}], **{
        'route T': {'reads': 1, 'skipped': 0, 'disagree': []}})
    member = {'member': True, 'h1 R': 1, 'h1 P4': 1,
              'R': {'capW': 2, 'capL2': 2},
              'P4': {'capW': 2, 'capL2': 2}}
    low = dict(member, R={'capW': 2, 'capL2': 1},
               P4={'capW': 2, 'capL2': 1})
    cases = {
        'empty_part_L': ([], None, None),
        'one_recorded_cover': ([base], None, None),
        'missing_chunk': ([dict(base, chunks=2)], None, None),
        'candidate_F_absent': ([candidate], None, None),
        'candidate_F_empty': ([candidate], [], None),
        'explicit_counterexample': ([candidate], [member], None),
        'recorded_low_capacity': ([candidate], [low], None),
        'H_expected_cover_missing': ([base], None, {
            'synthetic.missing': {'ez': [1, 1], 'm': 2,
                                  'acts on Q8 as the identity': False}}),
    }
    results = {}
    for name, (L, F, hcov) in cases.items():
        out = evaluate(ident, L, F, say=lambda _: None, hcov=hcov)
        results[name] = out
        print(json.dumps({'case': name, 'result': out}, sort_keys=True))
    p = lambda name: results[name]['predictions']
    checks = {
        'empty_L_reports_every_cover': results['empty_part_L']['every cover read'],
        'one_recorded_cover_reports_every_cover': results['one_recorded_cover']['every cover read'],
        'missing_chunk_detected': not results['missing_chunk']['every cover read'],
        'missing_chunk_still_reports_P8': p('missing_chunk')['P8'] is True,
        'candidate_F_absent_withheld': p('candidate_F_absent')['P7'] is None and p('candidate_F_absent')['P8'] is None,
        'candidate_F_empty_reports_negative': p('candidate_F_empty')['P7'] is True and p('candidate_F_empty')['P8'] is True,
        'counterexample_detected': p('explicit_counterexample')['P7'] is False and p('explicit_counterexample')['P8'] is False,
        'low_capacity_control': p('recorded_low_capacity')['P7'] is True and p('recorded_low_capacity')['P8'] is True,
        'H_missing_cover_withheld': p('H_expected_cover_missing')['P9'] is None and p('H_expected_cover_missing')['P10'] is None,
    }
    out = {'pin': PIN, 'sha256': DIGEST, 'checks': checks,
           'all_expected_diagnostic_behaviors': all(checks.values()),
           'scope': 'synthetic readout behavior only; not a mathematical population verdict'}
    print(json.dumps(out, sort_keys=True))
    return out


if __name__ == '__main__':
    raise SystemExit(0 if run()['all_expected_diagnostic_behaviors'] else 1)
