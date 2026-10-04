"""Sealed exact controls and read-only recombination of pinned branch data."""
import hashlib
import json
import re
import subprocess
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[2]
PIN = '7de10c131229efca4437bd6445ab5e95632e275f'
B1471 = 'frontier/B1471_the_cancellation_is_a_theorem_of_amphichirality/verification'
B1473 = 'frontier/B1473_the_three_kinds_cover_a_third_at_most/verification'
t, v = s.symbols('t v', nonzero=True)


def clean(m):
    return m.applyfunc(s.cancel)


def word(w, rep):
    ans = s.eye(2)
    for c in w:
        ans = clean(ans * (rep[c] if c.islower() else rep[c.lower()].inv()))
    return ans


def fox(w, rep):
    pre, terms = s.eye(2), {g:s.zeros(2) for g in rep}
    for c in w:
        g = c.lower()
        if c.islower():
            terms[g] = clean(terms[g]+pre)
            pre = clean(pre*rep[g])
        else:
            pre = clean(pre*rep[g].inv())
            terms[g] = clean(terms[g]-pre)
    return terms


def unit(f):
    num, den = s.fraction(s.cancel(f))
    pn, pd = s.Poly(num,t), s.Poly(den,t)
    assert len(pn.terms()) == len(pd.terms()) == 1, ('not monomial',f)
    sign = s.cancel(pn.LC()/pd.LC())
    assert sign in (s.Integer(1),s.Integer(-1)), ('not a torsion unit',f)
    k = pn.degree()-pd.degree()
    assert s.cancel(f-sign*t**k) == 0
    return {'sign':int(sign),'power':int(k)}


@lru_cache(None)
def wada_check():
    u = v/(v**2+1)
    A = s.Matrix([[u,1],[-1,0]])
    B = s.Matrix([[0,v],[-1/v,1-u**2]])
    relator = 'babbbabAA'
    assert s.cancel(A.det()-1) == s.cancel(B.det()-1) == 0
    expected = t+2*(u**2-1)/u+1/t
    results, raw = [], []
    for sign in (1,-1):
        rep = {'a':sign*A,'b':B}
        assert word(relator,rep) == s.eye(2)
        twisted = {'a':t*rep['a'],'b':rep['b']}
        assert word(relator,twisted) == s.eye(2)
        F = fox(relator,twisted)
        assert clean(sum((F[g]*(twisted[g]-s.eye(2)) for g in rep),s.zeros(2))) == s.zeros(2)
        R = s.cancel(F['b'].det()/(twisted['a']-s.eye(2)).det())
        target = t+sign*2*(u**2-1)/u+1/t
        factor = unit(R/target)
        assert s.cancel(target-target.subs(t,1/t)) == 0
        assert s.cancel(R-factor['sign']*t**factor['power']*(target+1)) != 0
        results.append({'lift_a_sign':sign,'raw_to_normalized_unit':factor})
        raw.append(R)
    assert s.cancel(raw[1]-raw[0].subs(t,-t)) == 0
    return {'checks':'PASS','population':'DFJ m003 rational representation family',
            'u':'v/(v^2+1)','normalized_torsion':str(s.factor(expected)),
            'lifts':results,'changed_formula_detected':True,'twist_substitution_exact':True}


def coefficient_conjugate(f):
    return s.conjugate(f).subs(s.conjugate(t),t)


def circle_conjugate(f):
    return coefficient_conjugate(f).subs(t,1/t)


@lru_cache(None)
def diagnostic_checks():
    u0 = (1+s.I*s.sqrt(3))/2
    c = s.simplify(2*(u0**2-1)/u0)
    assert c == 2*s.I*s.sqrt(3)
    Tp, Tm = t+c+1/t, t-c+1/t
    assert s.simplify(Tm-coefficient_conjugate(Tp)) == 0
    zero_residual = s.simplify(Tp-circle_conjugate(Tm))
    contrast = s.simplify((Tp-Tm)/(2*s.I))
    assert zero_residual == 0 and contrast == 2*s.sqrt(3)
    assert s.simplify(Tp-circle_conjugate(Tm+1)) == -1
    raw_residual = s.expand(t**2*Tp-circle_conjugate(t**2*Tm))
    assert s.simplify(raw_residual-(t**2-t**-2)*Tp) == 0
    z = s.Rational(3,5)+s.I*s.Rational(4,5)
    assert s.simplify(z*s.conjugate(z)) == 1
    point = s.simplify(raw_residual.subs(t,z))
    assert point != 0
    assert s.simplify(Tp*circle_conjugate(Tp)-Tm*circle_conjugate(Tm)) == 0
    # Real-coefficient FIX comparator: even an invariant sector can acquire
    # an imaginary raw phase from an unremoved allowed even monomial unit.
    fixed = t+3+1/t
    assert s.simplify(fixed-circle_conjugate(fixed)) == 0
    assert s.simplify((t**2*fixed-circle_conjugate(t**2*fixed)).subs(t,z)) != 0
    return {'checks':'PASS','supplied_character':str(u0),'T_plus':str(Tp),
            'T_minus':str(Tm),'spin_contrast':str(contrast),
            'normalized_symmetry_residual':str(zero_residual),
            'raw_residual_after_common_t_squared':str(raw_residual),
            'raw_residual_at_3_plus_4i_over_5':str(point),
            'equal_moduli':True,'perturbed_partner_detected':True,'fixed_control_detects_unit':True}


def linear(cols,x):
    out = 0
    for j,c in enumerate(cols):
        if (x >> j)&1:
            out ^= c
    return out


@lru_cache(None)
def affine_checks():
    rows = []
    for n in (1,2,3):
        q, maps, origins, moved_with_fixed = 1 << n, 0, 0, 0
        for cols in product(range(q),repeat=n):
            if len({linear(cols,x) for x in range(q)}) != q:
                continue
            image = {x ^ linear(cols,x) for x in range(q)}
            for delta in range(q):
                fixed = {x for x in range(q) if linear(cols,x)^delta == x}
                assert bool(fixed) == (delta in image)
                maps += 1
                moved_with_fixed += bool(delta and fixed)
                for b in range(q):
                    rebased = delta ^ linear(cols,b) ^ b
                    new_fixed = {x for x in range(q) if linear(cols,x)^rebased == x}
                    assert new_fixed == {x ^ b for x in fixed}
                    assert (rebased in image) == (delta in image)
                    origins += 1
        rows.append({'dimension':n,'affine_bijections':maps,'basepoint_checks':origins,
                     'moving_origin_but_fixed_points':moved_with_fixed})
    swap, delta = (2,1), 3
    assert linear(swap,0)^delta == 3
    assert {x for x in range(4) if linear(swap,x)^delta == x} == {1,2}
    assert not {x for x in range(4) if linear((1,2),x)^1 == x}
    assert {x for x in range(4) if linear((1,2),x) == x} == set(range(4))
    return {'checks':'PASS','rows':rows,'moving_origin_with_two_fixed_points':True,
            'pure_translation_no_fixed_points':True,'identity_fixes_all':True}


def source(path, hashes):
    data = subprocess.check_output(['git','show',PIN+':'+path],cwd=ROOT)
    hashes[path] = hashlib.sha256(data).hexdigest()
    return json.loads(data)


def unique(rows):
    out = {r['id']:r for r in rows}
    assert len(out) == len(rows), 'duplicate source IDs'
    return out


def normalized(text):
    text = text.translate(str.maketrans({'’':"'",'‘':"'",'“':'"','”':'"'}))
    return re.sub(r'\s+',' ',text).strip().lower()


@lru_cache(None)
def branch_checks():
    hashes = {}
    kg = source('frontier/B738_pathfinder_compiler/kill_graph.json',hashes)
    empty = [r for r in kg if not r.get('claim_killed')]
    kills = [r for r in kg if r.get('claim_killed')]
    assert len(kg)==803 and len(empty)==343 and len(kills)==460
    assert all(r.get('priority')=='FACE-ONLY' for r in empty)
    assert all(r.get('priority')!='FACE-ONLY' for r in kills)
    batches, readings = [], []
    for i in range(8):
        batches.extend(source(f'{B1473}/readers/batch_{i}.json',hashes))
        readings.extend(source(f'{B1473}/readers/out_{i}.json',hashes))
    batch = unique([r for r in batches if r.get('claim_killed')])
    reads = unique([r for r in readings if r['id'] in batch])
    assert set(batch)==set(reads)==set(unique(kills))
    for i,r in reads.items():
        corpus = '\n'.join(batch[i].get(k) or '' for k in ('claim_killed','kill_form','hatch'))
        quote = r.get('quote','').strip()
        assert (quote and normalized(quote) in normalized(corpus)) or (not quote and r['kind']=='OTHER')
    counts = Counter(r['kind'] for r in reads.values())
    assert counts=={'OTHER':306,'PAIRING':24,'FLATNESS':32,'NON-UNIQUENESS':98}
    second = unique(source(f'{B1473}/readers/verified_0.json',hashes)+source(f'{B1473}/readers/verified_1.json',hashes))
    candidates = {i for i,r in reads.items() if r['kind']!='OTHER'}
    assert set(second)==candidates and len(candidates)==154
    confirmed = Counter(reads[i]['kind'] for i,r in second.items() if r['verdict']=='CONFIRM')
    fitted = [i for i,r in second.items() if r['verdict']!='CONFIRM' and any(w in r['kind'].lower() for w in ('numerolog','fit','catalogue'))]
    assert confirmed=={'PAIRING':16,'FLATNESS':17,'NON-UNIQUENESS':51}
    assert len(fitted)==19 and sum(confirmed.values())==84
    chars = source(f'{B1471}/odd_characters.json',hashes)
    matches = {name:{n:len(rows) for n,rows in data['matches'].items()} for name,data in chars.items()}
    assert matches['s955']=={'1':2,'3':2}
    assert matches['s957']=={'1':2,'3':2}
    assert matches['s960']=={'1':3,'3':3}
    return {'checks':'PASS','main_pin':PIN,'kill_entries':len(kills),'face_only':len(empty),
            'first_reader_counts':dict(counts),'second_confirmed':dict(confirmed),
            'fitted_disagreements':len(fitted),'matching_character_counts':matches,
            'qualification':'arithmetic and quote audit, not semantic reclassification or geometric action',
            'source_sha256':hashes}


if __name__=='__main__':
    for name,fn in [('m003_fox',wada_check),('spin_diagnostic',diagnostic_checks),
                    ('affine_torsors',affine_checks),('branch_receipts',branch_checks)]:
        print(json.dumps({'cell':name,**fn()},sort_keys=True),flush=True)
