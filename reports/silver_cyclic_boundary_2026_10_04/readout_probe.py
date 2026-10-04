"""Synthetic audit of the repaired readout; no actual population is read."""
import copy
import hashlib
import json
import subprocess
from functools import lru_cache

PIN = '090ac4c08bb58811f54ee27ddf5e39018e83ac37'
SOURCE = 'frontier/B1538_the_puncture_characters/verification/read_out.py'
DIGEST = '86337ef29abb55e5beea55d0513c6cec65d0d158c47bd13c4b0ca0b122b6ca04'


@lru_cache(None)
def run():
    raw = subprocess.check_output(['git','show',PIN+':'+SOURCE])
    assert hashlib.sha256(raw).hexdigest() == DIGEST
    scope = {'__name__':'repaired_readout_diagnostic','__file__':SOURCE}
    exec(compile(raw,SOURCE,'exec'),scope)
    evaluate = scope['evaluate']
    ident = {'identity holds':True}
    mf = {'synthetic.one':{'chunks':1,'puncture orbits':10}}
    base = {'cover':'synthetic.one','chunks':1,'chunk':0,'read':True,'hits':[],
            'state':'m135','puncture orbits':10,'puncture characters':30,
            'route P':{'reads':20,'disagree':[]},
            'route T':{'reads':0,'skipped':0,'disagree':[]}}
    chi = {'zeta':[1,0],'m':3,'s':[1,6],'n':2}
    candidate = dict(base,hits=[chi],**{'route T':{'reads':1,'skipped':0,'disagree':[]}})
    header = {'kind':'candidate','cover':'synthetic.one','chi':chi,'fourth roots':1,'planned':4}
    def reading(t):
        return {'kind':'reading','cover':'synthetic.one','chi':chi,
                'nu':{'zeta':[1,0],'m':12,'s':[1+6*t,24]},
                'h1 R':1,'h1 P4':1,'member':True,
                'R':{'capW':2,'capL2':1},'P4':{'capW':2,'capL2':1}}
    full = [header]+[reading(t) for t in range(4)]
    bad_route = copy.deepcopy(full); bad_route[1]['h1 P4'] = 2
    bad_root = copy.deepcopy(full); bad_root[1]['nu']['zeta'] = [2,0]
    refute = copy.deepcopy(full); refute[1]['R']['capL2'] = 2; refute[1]['P4']['capL2'] = 2
    bad_p = copy.deepcopy(base); bad_p['route P']['disagree'] = ['synthetic mismatch']
    cases = {
        'complete_no_hits':([base],None,mf),
        'empty_L':([],None,mf),
        'no_manifest':([base],None,None),
        'missing_cover':([base],None,dict(mf,missing={'chunks':1,'puncture orbits':10})),
        'missing_chunk':([dict(base,chunks=2)],None,{'synthetic.one':{'chunks':2,'puncture orbits':20}}),
        'duplicate_chunk':([base,base],None,mf),
        'short_orbits':([dict(base,**{'puncture orbits':9})],None,mf),
        'empty_F':([candidate],[],mf),
        'short_F':([candidate],full[:-1],mf),
        'duplicate_F':([candidate],full+[full[1]],mf),
        'complete_F':([candidate],full,mf),
        'zero_roots_header':([candidate],[dict(header,planned=0,**{'fourth roots':0})],mf),
        'counterexample':([candidate],refute,mf),
        'counterexample_incomplete_F':([candidate],refute[:2],mf),
        'F_route_disagreement':([candidate],bad_route,mf),
        'L_route_disagreement':([bad_p],None,mf),
        'inconsistent_header_count':([candidate],[dict(header,planned=0)],mf),
        'wrong_fourth_root':([candidate],bad_root,mf),
        'duplicate_masks_counterexample':([candidate,base],None,mf),
    }
    results = {}
    for name,(L,F,manifest) in cases.items():
        out = evaluate(ident,L,F,say=lambda _:None,manifest=manifest)
        results[name] = out
        print(json.dumps({'case':name,'result':out},sort_keys=True),flush=True)
    pred = lambda key:results[key]['predictions']
    repaired = ('empty_L','no_manifest','missing_cover','missing_chunk','duplicate_chunk','short_orbits')
    checks = {key:pred(key)['P8'] is None for key in repaired}
    checks.update({key:pred(key)['P7'] is None and pred(key)['P8'] is None
                   for key in ('empty_F','short_F','duplicate_F')})
    checks.update({
        'positive_controls':all(pred(key)['P8'] is True for key in ('complete_no_hits','complete_F','zero_roots_header')),
        'refutations_survive_missing_F':all(pred(key)['P8'] is False for key in ('counterexample','counterexample_incomplete_F')),
        'F_disagreement_separate_from_P8':results['F_route_disagreement']['Part F']['routes agree'] is False
                                         and pred('F_route_disagreement')['P8'] is True,
        'L_disagreement_separate_from_P8':pred('L_route_disagreement')['P2'] is False
                                         and pred('L_route_disagreement')['P8'] is True,
        'inconsistent_header_not_validated':pred('inconsistent_header_count')['P8'] is True,
        'wrong_root_not_validated':pred('wrong_fourth_root')['P8'] is True,
        'duplicate_counterexample_withheld_not_false':pred('duplicate_masks_counterexample')['P5'] is None,
    })
    result = {'pin':PIN,'sha256':DIGEST,'checks':checks,'all_expected_behaviors':all(checks.values()),
              'scope':'synthetic acceptance boundaries, not a puncture population or corruption claim'}
    print(json.dumps(result,sort_keys=True),flush=True)
    return result


if __name__ == '__main__':
    raise SystemExit(0 if run()['all_expected_behaviors'] else 1)
