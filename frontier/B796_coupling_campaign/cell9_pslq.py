r"""CELL 9 RUNG (i) — the sealed PSLQ stage (prereg v3 169e9042, D-4).

Runs AFTER the eigenvalue runs deliver their certified JSONs. Per the
sealed power box: max-normalized residual convention; tolerance = 10x
the propagated noise floor from the OBSERVED |dr|_stab; runtime-
licensed H via N_eff = 25 - log10(dynamic range); boxes with
H_max < 10 declared UNPOWERED (logged, excluded, not run silently);
50 surrogates per (box, target-class), hit requires surrogate rate
< 0.02. d = NUMBER OF ENTRIES of the test vector (the degree
convention's H_max is also logged for boundary cases).

VERDICT SEMANTICS (sealed): rung (i) is instrument validation + the
first power step — NOT the campaign falsifier (that is the 100-digit
B798 box). A negative = "no relation within the POWERED boxes at 25
digits", with the powered boxes enumerated. Any hit -> cc adversarial
re-derivation BEFORE any use.

Usage: python cell9_pslq.py  (reads all cell9_rung1_v3_*.json,
skips shakedowns)

Gate 5-Q.
"""
import glob
import json

import mpmath as mp
import numpy as np

mp.mp.dps = 40
OUT = 'frontier/B796_coupling_campaign'
RNG = np.random.default_rng(97)
PSLQ_COEFF = 1.43  # BSV one-point calibration (per seal; estimate)

sqrt5 = mp.sqrt(5)
phi = (1 + sqrt5) / 2

BASES = {
    'B1 Q(sqrt5)':   ([mp.mpf(1), sqrt5], None),
    'B2 Q(sqrt3)':   ([mp.mpf(1), mp.sqrt(3)], None),
    'B3 Q(sqrt15)':  ([mp.mpf(1), mp.sqrt(15)], None),
    'B4 Q(zeta15+)': ([mp.mpf(1)] + [(2 * mp.cos(2 * mp.pi / 15)) ** k
                                     for k in (1, 2, 3)], None),
    'B5 Q(zeta20+)': ([mp.mpf(1)] + [mp.sqrt(2 + phi) ** k
                                     for k in (1, 2, 3)], None),
    'B6 Q(sqrt-phi)': ([mp.mpf(1)] + [mp.sqrt(phi) ** k
                                      for k in (1, 2, 3)], None),
    'MINPOLY':       ('minpoly', None),
}


def load_targets():
    tgts = []
    for f in sorted(glob.glob(f'{OUT}/cell9_rung1_v3_*.json')):
        d = json.load(open(f))
        if d.get('shakedown'):
            continue
        if not d.get('stab_ok'):
            print(f"  SKIP {f}: stab_ok False")
            continue
        r = mp.mpf(d['r_refined'])
        dr_stab = mp.mpf(d['dr_stab'])
        tgts.append({'name': f"r={d['r_certified']}", 'r': r,
                     'lam': 1 + r * r, 'dr_stab': dr_stab,
                     'src': f})
    return tgts


def vector_for(basis_key, x):
    if basis_key == 'MINPOLY':
        return [x ** k for k in range(5)]           # [1, x, x^2, x^3, x^4]
    basis, _ = BASES[basis_key]
    return [x] + basis


def analyze(basis_key, x, dx, digits=25):
    vec = vector_for(basis_key, x)
    d = len(vec)
    # exact per-entry derivative magnitudes
    if basis_key == 'MINPOLY':
        dv = [k * abs(x) ** (k - 1) if k > 0 else mp.mpf(0)
              for k in range(5)]
    else:
        dv = [mp.mpf(1)] + [mp.mpf(0)] * (d - 1)
    vmax = max(abs(v) for v in vec)
    noise = max(dv) * dx / vmax
    tol = 10 * noise
    dyn = float(mp.log10(vmax / min(abs(v) for v in vec if abs(v) > 0)))
    n_eff = digits - dyn
    h_terms = mp.mpf(10) ** (n_eff / (PSLQ_COEFF * d))
    h_deg = mp.mpf(10) ** (n_eff / (PSLQ_COEFF * (d - 1)))
    h_max = min(float(h_terms), 1e4 if d <= 3 else 1e3)
    powered = h_max >= 10
    return {'d_terms': d, 'noise': float(noise), 'tol': float(tol),
            'dyn_range_digits': dyn, 'n_eff': n_eff,
            'H_max_terms': float(h_terms), 'H_max_degree': float(h_deg),
            'H_licensed': h_max, 'powered': bool(powered), 'vec': vec}


def run_pslq(vec, tol, maxcoeff):
    try:
        rel = mp.pslq([mp.mpf(v) for v in vec], tol=mp.mpf(tol),
                      maxcoeff=int(maxcoeff), maxsteps=500000)
    except Exception:
        return None
    if rel is None or all(c == 0 for c in rel):
        return None
    # max-normalized residual check
    terms = [c * v for c, v in zip(rel, vec)]
    res = abs(sum(terms)) / max(abs(t) for t in terms if t != 0)
    return {'relation': list(rel), 'residual_maxnorm': float(res)}


def main():
    tgts = load_targets()
    if not tgts:
        print("No certified non-shakedown targets found — nothing to run.")
        return
    print(f"targets: {[t['name'] for t in tgts]}")
    results = []
    for t in tgts:
        for xname, x in [('r', t['r']), ('lam', t['lam'])]:
            dx = t['dr_stab'] if xname == 'r' else 2 * t['r'] * t['dr_stab']
            for bkey in BASES:
                box = analyze(bkey, x, dx)
                rec = {'target': t['name'], 'x': xname, 'box': bkey, **{
                    k: v for k, v in box.items() if k != 'vec'}}
                if not box['powered']:
                    rec['verdict'] = 'UNPOWERED (excluded, logged)'
                    results.append(rec)
                    print(f"  {t['name']}.{xname} {bkey}: UNPOWERED "
                          f"(H_max = {box['H_licensed']:.1f})")
                    continue
                hit = run_pslq(box['vec'], box['tol'], box['H_licensed'])
                if hit and hit['residual_maxnorm'] < box['tol']:
                    # surrogate null: 50 random values, same magnitude
                    cnt = 0
                    for _ in range(50):
                        xs = mp.mpf(float(x)) * (1 + mp.mpf(
                            RNG.uniform(-0.3, 0.3)))
                        sv = vector_for(bkey, xs)
                        sh = run_pslq(sv, box['tol'], box['H_licensed'])
                        if sh and sh['residual_maxnorm'] < box['tol']:
                            cnt += 1
                    p_null = cnt / 50
                    gated = p_null < 0.02
                    rec.update(hit, p_null=p_null, gated=bool(gated))
                    rec['verdict'] = ('** GATED HIT — cc adversarial '
                                      're-derivation REQUIRED **'
                                      if gated else 'fails base rate')
                    print(f"  {t['name']}.{xname} {bkey}: RELATION "
                          f"{hit['relation']} p_null={p_null} "
                          f"{'GATED' if gated else 'not gated'}")
                else:
                    rec['verdict'] = 'no relation in powered box'
                    print(f"  {t['name']}.{xname} {bkey}: clean "
                          f"(H <= {box['H_licensed']:.0f})")
                results.append(rec)
    with open(f'{OUT}/cell9_pslq_results.json', 'w') as f:
        json.dump(results, f, indent=1, default=str)
    n_hit = sum(1 for r in results if 'GATED' in str(r.get('verdict', '')))
    n_pow = sum(1 for r in results if r.get('powered'))
    print(f"\nVERDICT: {n_hit} gated hits across {n_pow} powered "
          f"(box, target) combinations. "
          f"{'-> cc re-derivation required' if n_hit else 'Clean at 25 digits in the powered boxes (rung-(i) scope: instrument validation + first power step; NOT the campaign falsifier).'}")
    print("Saved cell9_pslq_results.json")


if __name__ == '__main__':
    main()
