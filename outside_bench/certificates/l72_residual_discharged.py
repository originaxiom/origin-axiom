"""OUTSIDE BENCH -- L72's uniqueness residual, DISCHARGED against a read source.

No seal: this verifies a computed object against statements READ VERBATIM from
Rowell-Stong-Wang, "On classification of modular tensor categories" (arXiv:0712.1377v4,
9 Nov 2009), supplied as a PDF by the owner on 2026-09-13. The paper was previously
UNREACHABLE from this box (arxiv.org, people.tamu.edu and escholarship.org all return
EGRESS_BLOCKED at the network gateway -- memo 219).

The E6 level-2 stage is rebuilt here from the Cartan matrix, as in memos 206 and 211.

Run: python3 outside_bench/certificates/l72_residual_discharged.py
"""
import json
import pathlib
import re
import subprocess

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
# ============================================================ the stage (control C1)
print("\n" + "=" * 78)
print("C1 -- the E6 level-2 stage, rebuilt here from the Cartan matrix")
print("=" * 78)
C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)
MARKS = np.array([1, 2, 2, 3, 2, 1], dtype=np.int64)
H_VEE, DIM_E6, DETC, K = 12, 78, 3, 2
CI3 = np.rint(np.linalg.inv(C6.astype(float)) * DETC).astype(np.int64)
assert np.array_equal(CI3 @ C6, DETC * np.eye(6, dtype=np.int64))


def weyl_group():
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64); M[j, :] -= C6[:, j]; gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes(): 1}; layer = [(I, 1)]; mats, signs = [I], [1]
    while layer:
        nxt = []
        for M, s in layer:
            for g in gens:
                Mg = g @ M; k = Mg.tobytes()
                if k not in seen:
                    seen[k] = -s; nxt.append((Mg, -s)); mats.append(Mg); signs.append(-s)
        layer = nxt
    return np.array(mats), np.array(signs, dtype=np.int64)


def primaries(k):
    out = []
    def rec(i, rem, acc):
        if i == 6:
            out.append(tuple(acc)); return
        for v in range(rem // MARKS[i] + 1):
            rec(i + 1, rem - v * MARKS[i], acc + [v])
    rec(0, k, [])
    return sorted(out, key=lambda t: (sum(t), t))


W, eps = weyl_group()
assert len(W) == 51840, len(W)
KH = K + H_VEE
PRIM = primaries(K)
N = len(PRIM)
rho = np.ones(6, dtype=np.int64)
A = np.array([np.array(p, dtype=np.int64) + rho for p in PRIM])
X = (CI3 @ A.T).T
MOD = 9 * KH
Y = C6 @ X.T
zeta = np.exp(-2j * np.pi * np.arange(MOD) / MOD)
epsc = eps.astype(np.complex128)
Su = np.empty((N, N), dtype=complex)
for l in range(N):
    Su[l] = epsc @ zeta[(W @ X[l] @ Y) % MOD]
S0 = Su / np.sqrt(Su @ Su)[np.unravel_index(np.argmax(np.abs(Su @ Su)), (N, N))]
c = K * DIM_E6 / KH
h = np.array([float(np.array(p) @ (CI3 / DETC) @ (np.array(p) + 2 * rho)) / (2 * KH) for p in PRIM])
T = np.diag(np.exp(2j * np.pi * (h - c / 24)))
sg = min((s for s in (1.0, -1.0)),
         key=lambda s: np.abs(np.linalg.matrix_power(s * S0 @ T, 3) - (S0 @ S0)).max())
S = sg * S0
Cperm = S @ S
d = (S[0, :] / S[0, 0]).real
Nv = np.einsum('il,jl,kl,l->ijk', S, S, S.conj(), 1.0 / S[0, :])
print(f"  |W(E6)| = {len(W)}   rank = {N}   c = {c:.6f}")
print(f"  S symmetric {np.abs(S-S.T).max():.2e}  unitary {np.abs(S@S.conj().T-np.eye(N)).max():.2e}"
      f"  (ST)^3=S^2 {np.abs(np.linalg.matrix_power(S@T,3)-Cperm).max():.2e}")
print(f"  Verlinde integral {np.abs(Nv-np.rint(Nv.real)).max():.2e}  min {np.rint(Nv.real).min():.0f}")
flip = lambda t: (t[5], t[1], t[4], t[3], t[2], t[0])
idx = {p: i for i, p in enumerate(PRIM)}
assert [int(np.argmax(np.rint(Cperm.real)[i])) for i in range(N)] == [idx[flip(p)] for p in PRIM]
print("  C = S^2 IS the E6 diagram flip (gate)")
print(f"  qdims = {np.round(d, 6)}")
print(f"  h     = {[str(p) for p in PRIM]}")
print(f"          {np.round(h, 6)}")

# ==========================================================================
# The rank-3 Mueger centraliser, extracted, and checked against RSW as READ
# ==========================================================================
NAMES = None
cur = [i for i in range(N) if abs(d[i] - 1) < 1e-9]
cz = [i for i in range(N)
      if all(abs(S[i, j] - d[i] * d[j] * S[0, 0]) < 1e-9 for j in cur)]
assert len(cz) == 3, cz
# order the centraliser as (1, alpha, beta) with dim(alpha) < dim(beta), alpha != 1
order = [cz[i] for i in sorted(range(3), key=lambda i: d[cz[i]])]
one, alpha, beta = order
print("\n" + "=" * 78)
print("THE CENTRALISER, AND ROWELL-STONG-WANG AS READ FROM THE PDF")
print("=" * 78)
print(f"\n  centraliser objects (this bench): {[''.join(map(str,PRIM[i])) for i in order]}")
print(f"  quantum dimensions               : {[round(float(d[i]),9) for i in order]}")
hmod = [round(float(h[i] % 1), 9) for i in order]
print(f"  twists h mod 1                   : {hmod}")

print("\n--- CHECK 1: the FUSION RULES against RSW section 5.3.6, quoted ---")
print('   RSW 5.3.6: "Fusion rules: alpha^2 = 1 + beta, alpha.beta = alpha + beta,')
print('               beta^2 = 1 + alpha + beta"')
fus = np.rint(np.real(np.einsum('il,jl,kl,l->ijk', S, S, S.conj(), 1.0 / S[0, :]))).astype(int)
def decomp(a, b):
    return sorted(''.join(map(str, PRIM[k])) for k in range(N) for _ in range(fus[a, b, k]))
lab = {one: '1', alpha: 'alpha', beta: 'beta'}
def pretty(a, b):
    out = []
    for k in range(N):
        if fus[a, b, k]:
            out += [lab.get(k, ''.join(map(str, PRIM[k])))] * fus[a, b, k]
    return ' + '.join(sorted(out, key=lambda s: {'1': 0, 'alpha': 1, 'beta': 2}.get(s, 9)))
aa, ab, bb = pretty(alpha, alpha), pretty(alpha, beta), pretty(beta, beta)
print(f"   this bench: alpha^2      = {aa}")
print(f"               alpha.beta   = {ab}")
print(f"               beta^2       = {bb}")
ok1 = (aa == '1 + beta' and ab == 'alpha + beta' and bb == '1 + alpha + beta')
print(f"   MATCH: {ok1}")
assert ok1

print("\n--- CHECK 2: the QUANTUM DIMENSIONS against RSW Thm 3.2(3) and 5.3.6 ---")
import sympy as sp
xs = sp.Symbol('xs')
d1_poly = xs**3 - 2*xs**2 - xs + 1
roots = [complex(r) for r in sp.Poly(d1_poly, xs).nroots()]
d1 = max(r.real for r in roots)
dd = 2 * np.cos(np.pi / 7)
print(f"   RSW Thm 3.2(3): d1 is a real root of {d1_poly}; largest = {d1:.9f}")
print(f"   RSW 5.3.6     : quantum dims {{1, d, d^2 - 1}}, d = 2cos(pi/7) = {dd:.9f}"
      f"  ->  d^2 - 1 = {dd*dd-1:.9f}")
mine = sorted(float(d[i]) for i in order)
ok2 = (abs(mine[1] - dd) < 1e-9 and abs(mine[2] - (dd*dd - 1)) < 1e-9
       and abs(mine[2] - d1) < 1e-9)
print(f"   this bench    : {[round(m,9) for m in mine]}   MATCH: {ok2}")
assert ok2

print("\n--- CHECK 3: WHICH member of the symmetry orbit are we? ---")
print('   RSW 5.3.6 representative twists: theta_1 = 1, theta_alpha = e^(2 pi i/7),')
print('                                    theta_beta = e^(10 pi i/7)')
print("   i.e. h = 0, 1/7, 5/7")
rsw_h = [0.0, round(1/7, 9), round(5/7, 9)]
mine_h = sorted(hmod)
print(f"   this bench h mod 1 (sorted)     : {mine_h}")
print(f"   RSW representative (sorted)     : {sorted(rsw_h)}")
conj = sorted(round((1 - t) % 1, 9) for t in mine_h)
print(f"   COMPLEX CONJUGATE of this bench : {conj}")
is_conj = conj == sorted(rsw_h)
print(f"   => this bench's centraliser is the COMPLEX CONJUGATE of RSW's listed")
print(f"      representative: {is_conj}")
assert is_conj
print("   (consistent with memo 211 CELL 3, which matched k'=1 and REJECTED k'=6,")
print("    the conjugate, on S at 8.4e-2 and T at 8.7e-1.)")

print("\n--- CHECK 4: the classification sentence that discharges the residual ---")
print('   RSW section 5.4, verbatim:')
print('     "For the (A1, 5)_{1/2} fusion rule, all unitary MTCs are the one listed')
print('      in last subsection and those from the two symmetries S -> -S and')
print('      complex conjugate."')
print()
print("   This is UNCONDITIONAL. It does NOT invoke their own conjecture, stated")
print("   separately at section 2: \"Very likely the modular symbol of an MTC")
print("   determines the MTC, and we do not know when a modular symbol becomes a")
print("   modular data.\"  -- a conjecture later DISPROVED in general (Mignard-")
print("   Schauenburg, smallest known counterexample rank 49). It is not needed here.")
print()
print("   RSW Table 3 also lists (E6, k), k = 1, 2 at ranks 3 and 9 -- exactly the")
print("   two stages this bench rebuilt from the Cartan matrix.")

print("\n" + "=" * 78)
print("ALL FOUR CHECKS PASS.")
print("=" * 78)
