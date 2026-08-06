r"""Nullspace projection test: does a mult-2 eigenspace HIDE a parent form?

cc's standing PREDICTION (relay, stated before this test):
    r = 8.863405 is the parent's k=2 eigenvalue (V1 sector); its
    Weyl position W*r^3 = 1.989 sits 0.18% from the parent's k=2 slot,
    and the V1 budget expects ~1.75 parent eigenvalues in [7.3, 10]
    where cc3 currently labels zero.

The generic-null-vector S-invariance test CANNOT decide this for
multiplicity-2 eigenvalues: the SVD returns an arbitrary vector in the
2-dim eigenspace, and a generic mix of {parent form, newform} breaks
S-invariance even when a parent direction exists (cc3's registered
caveat; cc's scope concession "sigma_min never determines sector").

THE TEST. At each mult-2 eigenvalue take the TWO smallest right
singular vectors v1, v2 of the collocation matrix, reconstruct
f_c = c1 f1 + c2 f2, and minimize the S-invariance defect over the
projective line of (c1, c2):

    D_ij = sum_p (f_i(Sp) - f_i(p)) conj(f_j(Sp) - f_j(p))
    N_ij = sum_p [ f_i(p) conj(f_j(p)) + f_i(Sp) conj(f_j(Sp)) ]
    generalized eigenproblem  D c = mu N c
    dev_min = sqrt(mu_min), dev_max = sqrt(mu_max)

dev_min ~ 0 with dev_max ~ O(1)  => a parent direction EXISTS in the
eigenspace (prediction confirmed for that r).
dev_min ~ O(1)                   => no parent direction (refuted).

CONTROLS built in: (a) every mult-2 eigenvalue BELOW r = 7.072 must
show dev_min O(1) — the parent has nothing below its ground state, so
any near-zero dev_min there would expose the test as broken;
(b) the mult-1 parent at 7.072 must show dev ~ 1e-9 (known);
(c) mult-1 newforms must show dev O(1).

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from eigenvalues_final import S_BIANCHI, eval_f  # noqa: E402
from hejhal_m004 import (K_table, Lattice, System, apply_m, build_moves,
                        find_cusp_lattice, reduce_pt)  # noqa: E402

OUTDIR = 'frontier/B792_maass_m004_eigenvalues'

eigs = []
with open(f"{OUTDIR}/eigenvalues_final.json") as f:
    eigs += [(e['r'], e['multiplicity']) for e in
             json.load(f)['eigenvalues']]
with open(f"{OUTDIR}/scanD_refined.json") as f:
    eigs += [(e['r'], e['multiplicity']) for e in
             json.load(f)['eigenvalues']]
eigs.sort()

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()
print("Building system (Y = 0.75, rmax 10.1) ...")
S1 = System(lat, moves, 0.75, 10.1)
print(f"  {len(S1.mus)} modes / {len(S1.zs)} pts", flush=True)

# fixed evaluation-point set (pairs p, Sp both reduced, heights >= 0.7)
rng = np.random.default_rng(5)
pairs = []
while len(pairs) < 36:
    z = complex(rng.uniform(-0.5, 0.5), rng.uniform(-1.7, 1.7))
    t = rng.uniform(0.8, 1.1)
    z1, t1, _ = reduce_pt(lat, moves, z, t)
    zs_, ts_ = apply_m(S_BIANCHI, z, t)
    z2, t2, _ = reduce_pt(lat, moves, zs_, ts_)
    if min(t1, t2) >= 0.7:
        pairs.append(((z1, t1), (z2, t2)))

print(f"  {len(pairs)} evaluation pairs")
print()
print(f"{'r':>13} {'mult':>4} {'dev_min':>9} {'dev_max':>9}  verdict")

results = []
for r, mult in eigs:
    KT = K_table(S1.args, S1.ts, S1.wts, [r], [])
    KT = KT.reshape(len(S1.norms), len(S1.heights))
    V = ((S1.Y * KT[S1.nrm_idx, 0])[None, :] * S1.P0
         - (S1.tstar[:, None] * KT[S1.nrm_idx, 1:].T) * S1.P1)
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    k = max(mult, 1)
    basis = [Vh[-(i + 1)].conj() / cn for i in range(k)]

    F = np.zeros((k, len(pairs)), dtype=complex)   # f_i(p)
    G = np.zeros((k, len(pairs)), dtype=complex)   # f_i(Sp)
    for i, a in enumerate(basis):
        for j, ((z1, t1), (z2, t2)) in enumerate(pairs):
            F[i, j] = eval_f(S1, a, r, z1, t1)
            G[i, j] = eval_f(S1, a, r, z2, t2)
    Dm = (G - F) @ (G - F).conj().T
    Nm = F @ F.conj().T + G @ G.conj().T
    if k == 1:
        mu = [abs(Dm[0, 0] / Nm[0, 0])]
    else:
        w = np.linalg.eigvals(np.linalg.solve(Nm, Dm))
        mu = sorted(abs(w))
    dev_min, dev_max = np.sqrt(mu[0]), np.sqrt(mu[-1])
    if dev_min < 1e-3:
        verdict = 'PARENT DIRECTION EXISTS' if k > 1 else 'PARENT (V1)'
    else:
        verdict = 'no parent component'
    flag = '  <-- cc PREDICTION TARGET' if abs(r - 8.8634) < 1e-3 else ''
    below = '  [control: below parent ground state]' if r < 7.0 and dev_min < 1e-3 else ''
    print(f"{r:>13.8f} {mult:>4} {dev_min:>9.1e} {dev_max:>9.1e}  "
          f"{verdict}{flag}{below}", flush=True)
    results.append({'r': r, 'mult': mult, 'dev_min': float(dev_min),
                    'dev_max': float(dev_max), 'verdict': verdict})

print()
tgt = [x for x in results if abs(x['r'] - 8.8634) < 1e-3][0]
low_ok = all(x['dev_min'] > 1e-3 for x in results if x['r'] < 7.0)
parent_ok = [x for x in results if abs(x['r'] - 7.072) < 1e-3][0]['dev_min'] < 1e-6
print(f"CONTROLS: all below-ground-state eigenspaces parent-free: {low_ok}; "
      f"7.072 reads parent: {parent_ok}")
print()
if tgt['dev_min'] < 1e-3:
    print("cc's PREDICTION CONFIRMED: the r = 8.8634 eigenspace contains an")
    print("S-invariant (parent, V1) direction — the parent's k=2 eigenvalue")
    print("hides inside the mult-2 space. cc3's 'zero old forms in scanD'")
    print("label is corrected; the V1 Weyl budget deficit resolves.")
else:
    print("cc's PREDICTION REFUTED: no S-invariant direction at r = 8.8634")
    print(f"(dev_min = {tgt['dev_min']:.1e}). The V1 budget z = -1.32 stands.")

with open(f"{OUTDIR}/sector_projection_results.json", 'w') as f:
    json.dump({'pairs': len(pairs), 'controls_ok': bool(low_ok and parent_ok),
               'results': results}, f, indent=1)
print("Saved sector_projection_results.json")
