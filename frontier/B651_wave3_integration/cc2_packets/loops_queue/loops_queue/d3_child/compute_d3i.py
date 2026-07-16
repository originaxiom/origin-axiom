#!/usr/bin/env python3
"""
D3 track (i) -- the classical child family via SnapPy.

Sealed prereg: d3_child/PREREG_D3.md (sha 75d69af3). Track (i) ONLY (track (ii),
the stage-side twisted-bundle family, belongs to another agent; track (iii) is
the priced ledger, written separately as PRICED_LEDGER.md).

Protocol (verbatim from the prereg):
  1. M = snappy.Manifold('4_1'); bank the parent's volume as the sanity gate.
  2. For p in {5,6,7}: N = snappy.Manifold('4_1'); N.dehn_fill((p,1)); bank
     volume (high precision), chern_simons, shortest/core geodesics
     (length_spectrum(0.8)), homology (expect Z/p). Confirm p<=4 are
     exceptional (Thurston-classical; NOT computed as hyperbolic).
  3. SEALED comparison list (a)-(d), look-elsewhere denominator = 4:
     (a) CS arithmetic across p=5,6,7 (exact rational patterns?)
     (b) vol(p,1)/vol(parent) vs {log(phi), 1/phi, phi^-2} at 1e-6
     (c) shortest-geodesic real length vs 2*log(phi) at 1e-6
     (d) any exact identity among the three fillings' banked numbers
         (integer relations via mpmath pslq on small combinations)
  4. Honest verdict: any hit is NOTICED at most (n=3, denominator 4);
     NO-DISTINCTION is a fine outcome.

Run: <seat-workdir>/seat-work/.venv/bin/python compute_d3i.py
     (writes d3i_results.json; stdout redirected to d3i_run.log by caller)
"""
import datetime
import json
import sys
import warnings

warnings.filterwarnings('ignore')  # silence plink's tkinter-GUI UserWarning on import

import mpmath as mp
import snappy

mp.mp.dps = 50  # 50 decimal digits of working precision for pslq etc.

TOL = 1e-6          # the prereg's stated NOTICED tolerance for (b)/(c); reused for (a)/(d)
LOOK_ELSEWHERE_DENOM = 4   # SEALED: 4 sub-comparisons (a)-(d)
N_FILLINGS = 3             # SEALED: p in {5,6,7}

results = {}


def hr(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Step 1 -- parent sanity gate
# ---------------------------------------------------------------------------
hr("STEP 1 -- parent gate: M = snappy.Manifold('4_1')")
M = snappy.Manifold('4_1')
vol_parent = float(M.volume())
vol_parent_hp = M.high_precision().volume()
EXPECTED_PARENT_VOL = 2.029883212819307
gate_pass = abs(vol_parent - EXPECTED_PARENT_VOL) < 1e-9
print(f"snappy version         : {getattr(snappy, '__version__', 'n/a')}")
print(f"M.volume()             : {vol_parent}")
print(f"M.high_precision().vol : {vol_parent_hp}")
print(f"expected (bank)        : {EXPECTED_PARENT_VOL}")
print(f"SANITY GATE            : {'PASS' if gate_pass else 'FAIL'}")
assert gate_pass, "PARENT SANITY GATE FAILED -- halting (per prereg discipline)"

results['parent'] = {
    'manifold': '4_1',
    'volume': vol_parent,
    'volume_high_precision': str(vol_parent_hp),
    'expected_volume': EXPECTED_PARENT_VOL,
    'sanity_gate_pass': gate_pass,
}

# ---------------------------------------------------------------------------
# Step 2 -- confirm p<=4 are exceptional (Thurston-classical; NOT hyperbolic)
# ---------------------------------------------------------------------------
hr("STEP 2 -- p<=4 exceptional confirmation (known/Thurston-classical, NOT computed as hyperbolic)")
exceptional = {}
for p in [1, 2, 3, 4]:
    N = snappy.Manifold('4_1')
    N.dehn_fill((p, 1))
    st = N.solution_type()
    is_hyperbolic_solution = (st == 'all tetrahedra positively oriented')
    exceptional[p] = {
        'slope': f'({p},1)',
        'solution_type': st,
        'is_hyperbolic_solution': is_hyperbolic_solution,
    }
    print(f"  p={p}: dehn_fill(({p},1)) -> solution_type = {st!r}  "
          f"(hyperbolic solution? {is_hyperbolic_solution})")
    assert not is_hyperbolic_solution, (
        f"p={p} unexpectedly returned a hyperbolic solution type -- "
        "this would contradict the Thurston-classical exceptional-filling fact"
    )
print("All four (p=1,2,3,4) confirmed NON-hyperbolic solution types -- consistent with the "
      "known/Thurston-classical fact that 4_1's ten exceptional slopes are the integers -4..4. "
      "No volume/CS is banked for these (never treated as hyperbolic).")
results['exceptional_p_le_4_confirmation'] = exceptional

# ---------------------------------------------------------------------------
# Step 3 -- the three hyperbolic fillings p = 5, 6, 7
# ---------------------------------------------------------------------------
hr("STEP 3 -- fillings 4_1(p,1) for p = 5, 6, 7")
fillings = {}
phi = (1 + mp.sqrt(5)) / 2
log_phi = mp.log(phi)

for p in [5, 6, 7]:
    print(f"\n  --- p = {p} ---")
    # double precision manifold; seed chern_simons() on the CUSPED manifold first
    # (SnapPy quirk: chern_simons() on a filled manifold raises "isn't currently
    # known" unless a base value has been established on the cusped manifold).
    N = snappy.Manifold('4_1')
    N.chern_simons()
    N.dehn_fill((p, 1))
    st = N.solution_type()
    vol = float(N.volume())
    cs = float(N.chern_simons())
    hom = str(N.homology())

    # high precision copy: same seeding trick, done on the cusped hp manifold
    Nhp_cusped = snappy.Manifold('4_1').high_precision()
    Nhp_cusped.chern_simons()
    Nhp = Nhp_cusped
    Nhp.dehn_fill((p, 1))
    vol_hp = Nhp.volume()
    cs_hp = Nhp.chern_simons()

    ls = N.length_spectrum(0.8)
    ls_hp = Nhp.length_spectrum(0.8)
    geodesics = []
    for i, g in enumerate(ls):
        ghp = ls_hp[i]
        geodesics.append({
            'multiplicity': g.multiplicity,
            'topology': g.topology,
            'parity': g.parity,
            'length_real': float(g.length.real),
            'length_imag': float(g.length.imag),
            'length_real_hp': str(ghp.length.real),
            'length_imag_hp': str(ghp.length.imag),
        })

    shortest = min(geodesics, key=lambda r: r['length_real'])

    print(f"  solution_type          : {st}")
    print(f"  volume                 : {vol}")
    print(f"  volume (hp)            : {vol_hp}")
    print(f"  chern_simons           : {cs}")
    print(f"  chern_simons (hp)      : {cs_hp}")
    print(f"  homology               : {hom}  (expected Z/{p} -- elementary fact |H_1(4_1(p,1))|=p, stated not discovered)")
    print(f"  length_spectrum(0.8)   : {len(geodesics)} geodesic(s) within cutoff 0.8")
    for g in geodesics:
        print(f"      mult={g['multiplicity']} len={g['length_real']:.6f}+{g['length_imag']:.6f}i "
              f"topology={g['topology']} parity={g['parity']}")
    print(f"  shortest geodesic real length: {shortest['length_real']:.10f}")

    expected_hom = f"Z/{p}"
    hom_ok = (hom == expected_hom)
    if not hom_ok:
        print(f"  ! NOTE: homology {hom} does not textually match expected {expected_hom} "
              f"(check group presentation form)")

    fillings[p] = {
        'slope': f'({p},1)',
        'solution_type': st,
        'volume': vol,
        'volume_hp': str(vol_hp),
        'chern_simons': cs,
        'chern_simons_hp': str(cs_hp),
        'homology': hom,
        'homology_matches_Zp': hom_ok,
        'geodesics_within_0.8': geodesics,
        'shortest_geodesic': shortest,
        'volume_ratio_to_parent': vol / vol_parent,
    }

results['fillings'] = fillings

# ---------------------------------------------------------------------------
# Step 4 -- SEALED comparison list (a)-(d)
# ---------------------------------------------------------------------------
hr("STEP 4 -- SEALED comparison list (a)-(d); tolerance 1e-6; look-elsewhere denominator 4")

comparisons = {}

# --- (a) CS arithmetic across p=5,6,7: exact rational patterns? multiples of 1/24, 1/12? ---
print("\n--- (a) Chern-Simons arithmetic across p=5,6,7 ---")


def closest_fraction(x, max_denom=24):
    best = None
    for b in range(1, max_denom + 1):
        a = round(x * b)
        val = a / b
        err = abs(x - val)
        if best is None or err < best[2]:
            best = (a, b, err)
    return best


a_results = {}
for p in [5, 6, 7]:
    cs_hp_val = mp.mpf(fillings[p]['chern_simons_hp'])
    a, b, err = closest_fraction(float(cs_hp_val), max_denom=24)
    hit = err < TOL
    print(f"  CS({p},1) = {fillings[p]['chern_simons']:.10f}  closest a/b (b<=24): {a}/{b} = {a/b:.10f}  "
          f"err={err:.3e}  {'HIT' if hit else 'no match'}")
    a_results[p] = {'cs': fillings[p]['chern_simons'], 'closest_fraction': f"{a}/{b}", 'error': err, 'hit_at_1e-6': hit}

# pairwise differences / sums, and check vs multiples of 1/24, 1/12
pairs = [(5, 6), (5, 7), (6, 7)]
a_pairwise = {}
for (p, q) in pairs:
    diff = fillings[p]['chern_simons'] - fillings[q]['chern_simons']
    a_, b_, err_ = closest_fraction(diff, max_denom=24)
    hit = err_ < TOL
    print(f"  CS({p},1) - CS({q},1) = {diff:.10f}  closest a/b (b<=24): {a_}/{b_}  err={err_:.3e}  {'HIT' if hit else 'no match'}")
    a_pairwise[f'{p}-{q}'] = {'diff': diff, 'closest_fraction': f"{a_}/{b_}", 'error': err_, 'hit_at_1e-6': hit}

any_a_hit = any(v['hit_at_1e-6'] for v in a_results.values()) or any(v['hit_at_1e-6'] for v in a_pairwise.values())
comparisons['a_cs_arithmetic'] = {
    'individual': a_results, 'pairwise': a_pairwise,
    'method': 'closest fraction a/b with b<=24 (covers 1/24, 1/12, 1/6, 1/4, 1/3, 1/2 and combinations); '
              'tolerance 1e-6 (reused from the prereg\'s (b)/(c) tolerance for consistency)',
    'any_hit': any_a_hit,
}
print(f"  (a) verdict: {'NOTICED (candidate exact/rational pattern)' if any_a_hit else 'NO-DISTINCTION (no rational pattern within tolerance)'}")

# --- (b) vol(p,1)/vol(parent) vs golden quantities at 1e-6 ---
print("\n--- (b) vol(p,1)/vol(parent) vs {log(phi), 1/phi, phi^-2} at 1e-6 ---")
golden_targets = {
    'log(phi)': float(log_phi),
    '1/phi': float(1 / phi),
    'phi^-2': float(phi ** -2),
}
print(f"  targets: log(phi)={golden_targets['log(phi)']:.10f}  1/phi={golden_targets['1/phi']:.10f}  "
      f"phi^-2={golden_targets['phi^-2']:.10f}")
b_results = {}
any_b_hit = False
for p in [5, 6, 7]:
    ratio = fillings[p]['volume_ratio_to_parent']
    row = {}
    for name, target in golden_targets.items():
        err = abs(ratio - target)
        hit = err < TOL
        any_b_hit = any_b_hit or hit
        row[name] = {'target': target, 'error': err, 'hit_at_1e-6': hit}
        flag = 'HIT' if hit else ('close but no cigar' if err < 1e-2 else 'no')
        print(f"  p={p}: ratio={ratio:.10f}  vs {name}={target:.10f}  err={err:.3e}  [{flag}]")
    b_results[p] = {'ratio': ratio, 'comparisons': row}
comparisons['b_volume_ratio_golden'] = {'results': b_results, 'any_hit': any_b_hit}
print(f"  (b) verdict: {'NOTICED' if any_b_hit else 'NO-DISTINCTION (no ratio within 1e-6 of a golden quantity)'}")

# --- (c) shortest-geodesic real length vs 2*log(phi) at 1e-6 ---
print("\n--- (c) shortest-geodesic real length vs 2*log(phi) at 1e-6 ---")
two_log_phi = float(2 * log_phi)
print(f"  target 2*log(phi) = {two_log_phi:.10f}")
c_results = {}
any_c_hit = False
for p in [5, 6, 7]:
    L = fillings[p]['shortest_geodesic']['length_real']
    err = abs(L - two_log_phi)
    hit = err < TOL
    any_c_hit = any_c_hit or hit
    c_results[p] = {'shortest_length_real': L, 'target': two_log_phi, 'error': err, 'hit_at_1e-6': hit}
    print(f"  p={p}: shortest Re(length)={L:.10f}  err vs 2log(phi)={err:.3e}  {'HIT' if hit else 'no match'}")
comparisons['c_geodesic_vs_2logphi'] = {'results': c_results, 'any_hit': any_c_hit,
                                         'note': 'primary child is p=5 (first hyperbolic slope); p=6,7 checked for completeness'}
print(f"  (c) verdict: {'NOTICED' if any_c_hit else 'NO-DISTINCTION (no shortest length within 1e-6 of 2log(phi))'}")

# --- (d) integer relations via mpmath.pslq on small combinations ---
print("\n--- (d) integer relations (mpmath.pslq), documenting every attempt ---")

MAXCOEFF = 10 ** 4  # bound on relation coefficients: keeps the search meaningful
                    # (any finite-precision tuple admits SOME relation if coefficients
                    # are allowed to grow ~10^(precision/#terms); we only count relations
                    # with small, human-legible integer coefficients as candidate hits)

vol5, vol6, vol7 = (mp.mpf(fillings[p]['volume_hp']) for p in [5, 6, 7])
cs5, cs6, cs7 = (mp.mpf(fillings[p]['chern_simons_hp']) for p in [5, 6, 7])
len5 = mp.mpf(fillings[5]['shortest_geodesic']['length_real_hp'])
len6 = mp.mpf(fillings[6]['shortest_geodesic']['length_real_hp'])
len7 = mp.mpf(fillings[7]['shortest_geodesic']['length_real_hp'])
volP = mp.mpf(str(vol_parent_hp))
sqrt5 = mp.sqrt(5)

attempts = [
    ("CS(5) vs {1}",                 [cs5, mp.mpf(1)]),
    ("CS(6) vs {1}",                 [cs6, mp.mpf(1)]),
    ("CS(7) vs {1}",                 [cs7, mp.mpf(1)]),
    ("CS(5),CS(6),CS(7) vs {1}",     [cs5, cs6, cs7, mp.mpf(1)]),
    ("vol(5),vol(6),vol(7) vs vol(parent)", [vol5, vol6, vol7, volP]),
    ("vol(5),vol(6),vol(7),vol(parent) vs {1}", [vol5, vol6, vol7, volP, mp.mpf(1)]),
    ("len(5),len(6),len(7) vs {1}",  [len5, len6, len7, mp.mpf(1)]),
    ("len(5) vs 2log(phi)",          [len5, log_phi, mp.mpf(1)]),
    ("len(6) vs 2log(phi)",          [len6, log_phi, mp.mpf(1)]),
    ("len(7) vs 2log(phi)",          [len7, log_phi, mp.mpf(1)]),
    ("vol(5)/volP vs log(phi)",      [vol5 / volP, log_phi, mp.mpf(1)]),
    ("vol(6)/volP vs log(phi)",      [vol6 / volP, log_phi, mp.mpf(1)]),
    ("vol(7)/volP vs log(phi)",      [vol7 / volP, log_phi, mp.mpf(1)]),
    ("CS(5),vol(5) vs {1}",          [cs5, vol5, mp.mpf(1)]),
    ("CS(6),vol(6) vs {1}",          [cs6, vol6, mp.mpf(1)]),
    ("CS(7),vol(7) vs {1}",          [cs7, vol7, mp.mpf(1)]),
    ("vol(5),vol(6),vol(7) vs sqrt5,1", [vol5, vol6, vol7, sqrt5, mp.mpf(1)]),
    ("len(5),len(6),len(7) vs sqrt5,1", [len5, len6, len7, sqrt5, mp.mpf(1)]),
]

d_results = []
any_d_hit = False
for label, vec in attempts:
    rel = mp.pslq(vec, maxcoeff=MAXCOEFF, maxsteps=10 ** 5)
    if rel is not None:
        # sanity-check the residual at working precision
        residual = sum(mp.mpf(c) * v for c, v in zip(rel, vec))
        genuine = abs(residual) < mp.mpf(10) ** (-(mp.mp.dps - 5))
        any_d_hit = any_d_hit or genuine
        print(f"  [{label}] -> relation {rel}  residual={mp.nstr(residual, 5)}  "
              f"{'GENUINE (small coeffs, residual~0)' if genuine else 'SPURIOUS (precision artifact)'}")
        d_results.append({'label': label, 'relation': [int(c) for c in rel],
                           'residual': mp.nstr(residual, 10), 'genuine': genuine})
    else:
        print(f"  [{label}] -> no relation found (maxcoeff={MAXCOEFF})")
        d_results.append({'label': label, 'relation': None, 'genuine': False})

comparisons['d_pslq_integer_relations'] = {
    'maxcoeff': MAXCOEFF, 'working_precision_dps': mp.mp.dps,
    'attempts': d_results, 'any_genuine_hit': any_d_hit,
}
print(f"  (d) verdict: {'NOTICED (a genuine small-coefficient relation found)' if any_d_hit else 'NO-DISTINCTION (no genuine small-coefficient integer relation found)'}")

results['comparisons'] = comparisons

# ---------------------------------------------------------------------------
# Step 5 -- honest verdict
# ---------------------------------------------------------------------------
hr("STEP 5 -- honest verdict")
hit_flags = {
    'a': comparisons['a_cs_arithmetic']['any_hit'],
    'b': comparisons['b_volume_ratio_golden']['any_hit'],
    'c': comparisons['c_geodesic_vs_2logphi']['any_hit'],
    'd': comparisons['d_pslq_integer_relations']['any_genuine_hit'],
}
n_hits = sum(hit_flags.values())
print(f"hits per sub-comparison: {hit_flags}  (n_hits = {n_hits} of {LOOK_ELSEWHERE_DENOM})")
print(f"n fillings tested: {N_FILLINGS}; look-elsewhere denominator: {LOOK_ELSEWHERE_DENOM}")

if n_hits == 0:
    verdict = "NO-DISTINCTION"
    verdict_text = ("No sub-comparison (a)-(d) produced a hit at tolerance 1e-6 / small-coefficient "
                     "pslq relation. This is a fine, honest outcome per the prereg. The known facts "
                     "(p=5 is the first hyperbolic integer slope; H_1(4_1(5,1))=Z/5) remain context, "
                     "not findings. NO PROMOTION (n=3 fillings, regardless of outcome).")
else:
    verdict = "NOTICED"
    verdict_text = (f"{n_hits} of {LOOK_ELSEWHERE_DENOM} sub-comparisons produced a hit at the stated "
                     "tolerance. Per the SEALED prereg, this banks at NOTICED at most, discounted by the "
                     f"look-elsewhere denominator ({LOOK_ELSEWHERE_DENOM}) and the small sample (n=3 "
                     "fillings). NO PROMOTION from this cell regardless of outcome.")
print(verdict_text)

results['verdict'] = {
    'hit_flags': hit_flags, 'n_hits': n_hits,
    'n_fillings': N_FILLINGS, 'look_elsewhere_denominator': LOOK_ELSEWHERE_DENOM,
    'label': verdict, 'text': verdict_text,
}

results['meta'] = {
    'prereg': 'd3_child/PREREG_D3.md',
    'prereg_sha_stated': '75d69af3',
    'run_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'snappy_version': getattr(snappy, '__version__', 'unknown'),
    'mpmath_dps': mp.mp.dps,
    'python': sys.version,
}

with open('d3i_results.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)

hr("DONE -- wrote d3i_results.json")
