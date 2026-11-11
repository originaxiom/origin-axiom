#!/usr/bin/env python3
"""SM-C2, harvest row 1520 (FULL_FLAT_FAMILY_METRIC_AND_DISCONNECTED_CENTRALIZER @ 609c21c5b): this seat's own exact check
of (a) J5 X J5^-1 = -X^T for X = H, E, E^dag of the principal five, J5^2 = 1; (b) dim C(principal triple) = 24 from the
248's grading by row 1525's w (24 V0 + 11 V1 + 21 V2 + 11 V3 + V4), matching the branching (24,1) + (1,24) + 2(10,5) +
2(5,10bar) with 5 -> V2, 10 -> V1 + V3, 24 -> V1 + V2 + V3 + V4; (c) the fixed algebra of theta(X) = -X^T on su5 is so5
(dim 10); (d) (5) the one-form norm (2 pi)^2/tau2 |dv - tau du|^2 from the flat metric |dx + tau dy|^2, and det M_tau = 1;
(e) the SM stratum: 8 - 6 = 2 dimensions, 25 SU5 points (5p, 5q integers), (2/7, 0) not among them; (f) (12): no element of
S5 acts as -1 on the sum-zero four-space (trace = fixed points - 1 >= -1 > -4). The component-group count itself (K =
SU5_g x| Z2) is the cited Di Bella-de Graaf Table 5 (arXiv:2407.11801v1, printed p. 18): read here, E8 orbit A4, c'1 = A4,
dim t = 0, component group S2 -- applied, as the lane says, not reproduced. Planted: J = antidiag(1,1,1,1,1) must fail (a)."""
import json
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import sympy as sp

out = {}
H5 = sp.diag(-4, -2, 0, 2, 4)
E5 = sp.zeros(5)
for i, c in enumerate([2, sp.sqrt(6), sp.sqrt(6), 2]):
    E5[i + 1, i] = c


def Jmat(signs):
    J = sp.zeros(5)
    for i, s in enumerate(signs):
        J[i, 4 - i] = s
    return J


def test_J(J):
    return all(sp.simplify(J * X * J.inv() + X.T) == sp.zeros(5) for X in (H5, E5, E5.H)) and J * J == sp.eye(5)


J = Jmat([1, -1, 1, -1, 1])
out["(a)_J_X_J^-1=-X^T"] = test_J(J)
# (b) the 248 graded by w
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si, sj in product((1, -1), repeat=2):
            v = [F(0)] * 8
            v[i], v[j] = F(si), F(sj)
            roots.append(v)
for s in product((1, -1), repeat=8):
    if s.count(-1) % 2 == 0:
        roots.append([F(x, 2) for x in s])
w = [0, 0, 0, -1, 1, -2, 0, 2]
n = Counter(sum(F(a) * b for a, b in zip(w, r)) for r in roots)
n[F(0)] += 8
mult = {j: n[F(j)] - n[F(j + 1)] for j in range(0, 6)}
out["(b)_V_j_multiplicities"] = {str(k): v for k, v in mult.items() if v}
branch = Counter()
branch[0] += 24                                  # (24,1)
for j in (1, 2, 3, 4):
    branch[j] += 1                               # (1,24)
branch[2] += 2 * 10                              # (10,5) + (10bar,5bar)
for j in (1, 3):
    branch[j] += 2 * 5                           # (5,10bar) + (5bar,10)
out["(b)_from_branching"] = {str(k): v for k, v in sorted(branch.items())}
out["(b)_ok"] = {k: v for k, v in mult.items() if v} == dict(branch) and mult[0] == 24
# (c) fixed algebra of theta on su5: X anti-Hermitian traceless with -X^T = X  <=>  X real antisymmetric
basis = []
for a in range(5):
    for b in range(a + 1, 5):
        M = sp.zeros(5)
        M[a, b], M[b, a] = sp.I, sp.I            # i(E_ab + E_ba)
        basis.append(M)
        M = sp.zeros(5)
        M[a, b], M[b, a] = 1, -1                 # E_ab - E_ba
        basis.append(M)
for a in range(4):
    M = sp.zeros(5)
    M[a, a], M[a + 1, a + 1] = sp.I, -sp.I
    basis.append(M)
assert len(basis) == 24
vecs = sp.Matrix([[sp.re(x) for x in (-B.T - B)] + [sp.im(x) for x in (-B.T - B)] for B in basis])
fixed_dim = 24 - vecs.rank()
out["(c)_fixed_dim"] = fixed_dim
# (d) one-form norm
t1 = sp.Symbol("tau1", real=True)
t2 = sp.Symbol("tau2", positive=True)
du, dv = sp.symbols("du dv", real=True)
g = sp.Matrix([[1, t1], [t1, t1 ** 2 + t2 ** 2]])     # |dx + tau dy|^2, tau = t1 + i t2
norm = (2 * sp.pi) ** 2 * (sp.Matrix([[du, dv]]) * g.inv() * sp.Matrix([du, dv]))[0] * sp.sqrt(g.det())
tau = t1 + sp.I * t2
rhs = (2 * sp.pi) ** 2 / t2 * sp.expand_complex((dv - tau * du) * (dv - sp.conjugate(tau) * du))
Mtau = sp.Matrix([[t1 ** 2 + t2 ** 2, -t1], [-t1, 1]]) / t2
out["(d)_norm_ok"] = sp.simplify(norm - rhs) == 0
out["(d)_det_Mtau"] = str(sp.simplify(Mtau.det()))
# (e) the stratum
out["(e)_stratum_dim"] = 8 - (2 * 2 + 1 * 2)
QY = [-2, -2, -2, 3, 3]
su5_pts = [(F(a, 5), F(b, 5)) for a, b in product(range(5), repeat=2)]
example = (F(2, 7), F(0))
out["(e)_SU5_points"] = len(su5_pts)
out["(e)_example_restores_SU5"] = all((5 * x).denominator == 1 for x in example)
# (f) S5 on the sum-zero subspace
traces = sorted({sum(1 for i in range(5) if p[i] == i) - 1 for p in permutations(range(5))})
out["(f)_traces_on_sum_zero"] = traces
ok = (out["(a)_J_X_J^-1=-X^T"] and out["(b)_ok"] and fixed_dim == 10 and out["(d)_norm_ok"]
      and out["(d)_det_Mtau"] == "1" and out["(e)_stratum_dim"] == 2 and len(su5_pts) == 25
      and not out["(e)_example_restores_SU5"] and min(traces) == -1)
out["cited_table"] = {"source": "arXiv:2407.11801v1, Table 5, printed p. 18", "row": "A4 | c'1 = A4 | dim t = 0 | "
                      "c'2 = A4 | A = S2", "pdf_sha256": "bd02e6b023550e9b7b6bdfda20c71f0b222133e6b00594d2a1d32480e28bafe7"}
out["PLANTED_all_plus_J_fails"] = not test_J(Jmat([1, 1, 1, 1, 1]))
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_all_plus_J_fails"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
