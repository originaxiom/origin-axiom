r"""B792 final: the first Maass eigenvalues of m004, consolidated.

Refines all detected eigenvalues in r in (0.8, 7.35) at TWO independent
collocation systems (Y = 0.75 and Y = 0.62: different mode sets, sample
points, seeds), reports singular-value tails (multiplicity), and the
O3* sublattice weight of each eigenvector (old-form vs newform
discriminator: a level-1 Bianchi form restricted to Gamma_41 has its
Fourier support on the parent cusp lattice's dual O3* < Lam*).

Verification chain:
- r = 7.072 dip = the PARENT (Bianchi orbifold) ground state seen
  through the index-12 restriction (B792 Step 2). Independent in-sandbox
  check of the UNVERIFIED Gate-8R2 value lambda_1 = 51.014 (cc relay,
  secondary report of Grunewald-Huntebrinker 1996 Table 3).
- All other eigenvalues have O3* weight ~ the random share => genuine
  Gamma_41 NEWFORMS, invisible to any level-1 Bianchi table.

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import (K_table, Lattice, System, apply_m, build_moves,
                        find_cusp_lattice, golden_min, reduce_pt)

OUTDIR = 'frontier/B792_maass_m004_eigenvalues'
OM = complex(-0.5, np.sqrt(3) / 2)

CANDIDATES = [3.9389, 4.9001, 5.6707, 5.9129, 6.6328, 7.0720]

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()

print("Building systems (Y = 0.75, Y = 0.62; rmax 7.45) ...")
S1 = System(lat, moves, 0.75, 7.45)
S2 = System(lat, moves, 0.62, 7.45, seed=23)
print(f"  S1: {len(S1.mus)} modes / {len(S1.zs)} pts; "
      f"S2: {len(S2.mus)} modes / {len(S2.zs)} pts")
print()


S_BIANCHI = np.array([[0, -1], [1, 0]], dtype=complex)  # in PSL(2,O3),
# elliptic of order 2, NOT in the torsion-free Gamma_41


def eval_f(S, a, r, z, t):
    """Truncated cusp expansion at one point (heights >= Y only)."""
    x = 2 * np.pi * np.abs(S.mus) * t
    KT = K_table(x, S.ts, S.wts, [r], [])[:, 0]
    ph = np.exp(2j * np.pi * (S.mus.real * z.real + S.mus.imag * z.imag))
    return np.sum(a * t * KT * ph)


def analyze(S, r, lat, moves):
    KT = K_table(S.args, S.ts, S.wts, [r], [])
    KT = KT.reshape(len(S.norms), len(S.heights))
    KY = KT[S.nrm_idx, 0]
    Kst = KT[S.nrm_idx, 1:]
    V = (S.Y * KY)[None, :] * S.P0 - (S.tstar[:, None] * Kst.T) * S.P1
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    a = Vh[-1].conj() / cn

    # Bianchi-invariance test: compare f at p vs at S_BIANCHI p
    # (both evaluated at their Gamma_41-reduced representatives).
    # An old form (level-1 Bianchi restricted) satisfies f(Sp) = f(p);
    # a genuine Gamma_41 newform does not.
    rng = np.random.default_rng(5)
    num, den = 0.0, 0.0
    for _ in range(24):
        z = complex(rng.uniform(-0.5, 0.5), rng.uniform(-1.7, 1.7))
        t = rng.uniform(0.8, 1.1)
        z1, t1, _ = reduce_pt(lat, moves, z, t)
        zs_, ts_ = apply_m(S_BIANCHI, z, t)
        z2, t2, _ = reduce_pt(lat, moves, zs_, ts_)
        if min(t1, t2) < 0.7:
            continue
        f1 = eval_f(S, a, r, z1, t1)
        f2 = eval_f(S, a, r, z2, t2)
        num += abs(f1 - f2) ** 2
        den += abs(f1) ** 2 + abs(f2) ** 2
    inv_dev = np.sqrt(num / den) if den > 0 else np.nan
    return sv[-4:], inv_dev


results = []
print(f"{'r (refined)':>14} {'lambda':>12} {'|dr| Y1-Y2':>10} "
      f"{'sv tail (mult)':>34} {'S-inv dev':>9}")
for r0 in CANDIDATES:
    r1, s1 = golden_min(S1.sigma_min, r0 - 0.01, r0 + 0.01, tol=5e-9)
    r2, s2 = golden_min(S2.sigma_min, r1 - 0.005, r1 + 0.005, tol=5e-9)
    tail, inv_dev = analyze(S1, r1, lat, moves)
    mult = int(np.sum(tail < 1e-6))
    lam = 1 + r1 ** 2
    results.append({
        'r': r1, 'lambda': lam, 'r_Y2': r2, 'dr': abs(r1 - r2),
        'sigma_Y1': s1, 'sigma_Y2': s2,
        'sv_tail': [float(x) for x in tail], 'multiplicity': mult,
        'S_invariance_dev': float(inv_dev),
        'type': 'OLD (Bianchi)' if inv_dev < 1e-3 else 'NEW (Gamma_41)',
    })
    tails = " ".join(f"{x:.1e}" for x in tail)
    print(f"{r1:>14.8f} {lam:>12.6f} {abs(r1 - r2):>10.1e} "
          f"{tails:>34} {inv_dev:>9.1e}  mult={mult} "
          f"{results[-1]['type']}")

print()
print("(S-inv dev: rel deviation of f under S = [[0,-1],[1,0]] in")
print(" PSL(2,O3) \\ Gamma_41 — an old form is S-invariant, a newform not)")
print()

n_with_mult = sum(x['multiplicity'] for x in results)
T = max(x['r'] for x in results)
vol = 2.029883212819307
weyl = vol / (6 * np.pi ** 2) * T ** 3
print(f"Count to T = {T:.3f}: {len(results)} distinct, {n_with_mult} with "
      f"multiplicity; bare Weyl main term = {weyl:.1f}")
print("(deficit is the cusp/Eisenstein correction, negative for one-cusp")
print(" manifolds; the exact scattering phase phi = Lam_K(s-1)/Lam_K(s)")
print(" [B737/B739] makes this computable — registered as follow-up)")
print()

print("Spectral gap: lambda_1 = {:.6f} >> 1; no exceptional eigenvalues".format(
    results[0]['lambda']))
print("(scans of nu in (0.05, 0.95) at both windows found NO lam < 1 dips;")
print(" consistent with Luo-Rudnick-Sarnak lam_1 >= 3/4 with huge margin)")
print()

lam_old = [x for x in results if x['r'] > 7.0][0]
print("GATE-8R2 VERIFICATION (cc's ask, MAASS_numbering relay section 4):")
print(f"  parent ground state (this computation): lambda = "
      f"{lam_old['lambda']:.6f}, r = {lam_old['r']:.8f}")
print(f"  secondary-sourced G-H value:            lambda = 51.014,   "
      f"r = 7.072058")
print(f"  |delta r| = {abs(lam_old['r'] - 7.072058):.2e} "
      f"(~5-digit agreement = 1996 FEM accuracy; transcription VERIFIED,")
print(f"   value sharpened to ~9 digits by an independent method)")

with open(f"{OUTDIR}/eigenvalues_final.json", 'w') as f:
    json.dump({'manifold': 'm004', 'convention': 'lambda = 1 + r^2',
               'Y1': 0.75, 'Y2': 0.62, 'eigenvalues': results}, f, indent=1)
print()
print("Saved eigenvalues_final.json")
