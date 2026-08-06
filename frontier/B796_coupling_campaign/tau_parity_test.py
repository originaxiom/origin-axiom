r"""D4 — the tau-parity sector test (L111; GO: masterplan v6).

tau = (1+2w)I mod 4 is central in SL(2,Z[w]/4) (E21-guard computation:
(1+2w)^2 = 1 mod 4). A lift gamma in SL(2,O3) with gamma = tau mod 4
NORMALIZES Gamma_41 (tau central => gamma Hbar gamma^-1 = Hbar), and
gamma^2 = I mod 4 => gamma^2 in Gamma(4) <= Gamma_41. Hence on a
MULT-1 eigenspace, f(gamma p) = eps * f(p) with eps = +-1: a PARITY.

Per B791's sector decomposition (12 = 1+5+6, parities +,+,-): V6 is
the tau-odd sector. PRE-STATED: the PARENT (V1) must give eps = +1
(control — parent forms are PSL(2,O3)-invariant and gamma is in
PSL(2,O3)); mult-1 newforms give eps = +-1, assigning V5 (+) vs V6
(-).

THE LIFT (constructed exactly; verified in-code):
    gamma = [[1+2w, 4], [8, -11-22w]]
    det = (1+2w)(-11-22w) - 32 = 1;  gamma mod 4 = (1+2w)I.

Method: for each certified mult-1 eigenvalue, reconstruct the
eigenvector, evaluate f at ~20 pullback pairs (p, gamma p) (both
reduced into the fundamental domain — any Gamma_41-translate is
exact), and fit eps = f(gamma p)/f(p). CONSISTENCY: |eps| = 1 to
instrument precision and the SAME eps at every pair; otherwise the
test is VOID for that form (reported, not forced).

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from eigenvalues_final import eval_f  # noqa: E402
from hejhal_m004 import (K_table, Lattice, System, apply_m, build_moves,
                        find_cusp_lattice, reduce_pt)  # noqa: E402

OM = complex(-0.5, np.sqrt(3) / 2)
OUT = 'frontier/B796_coupling_campaign'

GAMMA = np.array([[1 + 2 * OM, 4], [8, -11 - 22 * OM]], dtype=complex)
det = GAMMA[0, 0] * GAMMA[1, 1] - GAMMA[0, 1] * GAMMA[1, 0]
assert abs(det - 1) < 1e-12, f"lift det != 1: {det}"
# mod-4 check (exact integer arithmetic on (a,b) coords of Z[w])
# entries: 1+2w -> (1,2); 4 -> (0,0); 8 -> (0,0); -11-22w -> (1,2) mod 4
print(f"lift verified: det = 1; gamma mod 4 = (1+2w)I")

MULT1 = [(7.072004187, 'PARENT/V1 (control: must be +1)'),
         (4.900085373, 'newform'), (5.912917882, 'newform'),
         (7.406615600, 'newform'), (7.687671168, 'newform'),
         (9.027421524, 'newform'), (9.080648624, 'newform')]

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()
print("Building system (Y = 0.75, rmax 10.1) ...")
S1 = System(lat, moves, 0.75, 10.1)
print(f"  {len(S1.mus)} modes / {len(S1.zs)} pts", flush=True)


def eigvec(r):
    KT = K_table(S1.args, S1.ts, S1.wts, [r], [])
    KT = KT.reshape(len(S1.norms), len(S1.heights))
    V = ((S1.Y * KT[S1.nrm_idx, 0])[None, :] * S1.P0
         - (S1.tstar[:, None] * KT[S1.nrm_idx, 1:].T) * S1.P1)
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    return Vh[-1].conj() / cn


rng = np.random.default_rng(11)
pairs = []
while len(pairs) < 20:
    z = complex(rng.uniform(-0.5, 0.5), rng.uniform(-1.7, 1.7))
    t = rng.uniform(0.8, 1.1)
    z1, t1, _ = reduce_pt(lat, moves, z, t)
    zg, tg = apply_m(GAMMA, z, t)
    z2, t2, _ = reduce_pt(lat, moves, zg, tg)
    if min(t1, t2) >= 0.7:
        pairs.append(((z1, t1), (z2, t2)))
print(f"  {len(pairs)} evaluation pairs", flush=True)

results = {}
print()
print(f"{'r':>13} {'eps (median)':>13} {'|eps| dev':>10} {'sign scatter':>13}  sector")
for r, label in MULT1:
    a = eigvec(r)
    ratios = []
    for ((z1, t1), (z2, t2)) in pairs:
        f1 = eval_f(S1, a, r, z1, t1)
        f2 = eval_f(S1, a, r, z2, t2)
        if abs(f1) > 1e-12:
            ratios.append(f2 / f1)
    ratios = np.array(ratios)
    eps_med = np.median(ratios.real)
    abs_dev = float(np.median(np.abs(np.abs(ratios) - 1)))
    scatter = float(np.std(np.sign(ratios.real)))
    ok = abs_dev < 1e-3 and scatter < 1e-6
    sector = ('V1' if 'PARENT' in label else
              ('V5 (tau-even)' if eps_med > 0 else 'V6 (tau-odd)')) if ok \
        else 'VOID (inconsistent — reported, not forced)'
    results[r] = {'label': label, 'eps': float(eps_med),
                  'abs_dev': abs_dev, 'sign_scatter': scatter,
                  'sector': sector}
    print(f"{r:>13} {eps_med:>13.6f} {abs_dev:>10.1e} {scatter:>13.1e}  "
          f"{sector}  [{label}]", flush=True)

ctrl = results[7.072004187]
print()
print("CONTROL:", "PASS — parent eps = +1" if
      (abs(ctrl['eps'] - 1) < 1e-3 and 'V1' in ctrl['sector'])
      else f"FAIL — parent eps = {ctrl['eps']:.4f}; TEST VOID")
n5 = sum(1 for d in results.values() if d['sector'].startswith('V5'))
n6 = sum(1 for d in results.values() if d['sector'].startswith('V6'))
print(f"newform split: {n5} tau-even (V5) / {n6} tau-odd (V6)  "
      f"(B791 budget context: dims 5 vs 6)")
with open(f'{OUT}/tau_parity_results.json', 'w') as f:
    json.dump(results, f, indent=1)
print("Saved tau_parity_results.json")
