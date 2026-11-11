#!/usr/bin/env python3
"""SM-C2, harvest row 1523 (THREE_LENS_RELATIONAL_FOUNDATION_INTAKE_2026_11_02 @ b77117f6b): this seat's own check of the
intake's six corrections. (1) M^T J M = (det M) J for a generic 2 x 2 matrix over a commutative ring (symbolic), so it selects
no word; (2) the restricted Fibonacci minimum, by enumeration of nonnegative integer 2 x 2 matrices of entry sum <= 8: among
primitive, |det| = 1, spectral radius > 1, the least entry sum is 3, attained only by F = [[1,1],[1,0]] and PFP =
[[0,1],[1,1]]; F is symmetric (so 'together with its transpose' adds nothing; the second minimiser is the record exchange);
det F = -1, F^T J F = -J, eigenvalues phi and -1/phi; with det = +1 the least sum is 5, attained only by [[2,1],[1,1]] and
[[1,1],[1,2]]; F = L P and F^2 = L R; (3) characteristic two: B(x, y) = xy on F2 is skew-symmetric but not alternating, and
every alternating form on a one-dimensional space is zero; (4) Q8 and D4 (as matrix groups) both have centre Z2, quotient
F2^2 and the nondegenerate commutator pairing, and both square functions satisfy q(v+w) = q(v) + q(w) + B(v,w); Q8 has q = 1
on all three nonzero classes, D4 does not; [i, j] = -1 in Q8; (5) GL(1,Z) = {+1, -1} (units of Z) while n -> n + 1 is an
invertible affine map with an unbounded orbit; (6) the cited primary sources, fetched and grepped: Gurevich-Hadani
arXiv:0708.0669v3 constructs its functor for q odd; arXiv:0808.1664v1 is 'The Weil representation in characteristic two'
with quadratic forms and enhanced Lagrangians (digests recorded). Planted: the source's own phrase, the minimisers as F and
its transpose, must disagree with the enumerated set."""
import json
import sys
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

out = {}
a, b, c, d = sp.symbols("a b c d")
M = sp.Matrix([[a, b], [c, d]])
J = sp.Matrix([[0, 1], [-1, 0]])
out["(1)_MtJM=detM_J"] = sp.expand(M.T * J * M - M.det() * J) == sp.zeros(2)


def primitive(A):
    P = np.eye(2, dtype=object)
    for _ in range(6):
        P = P.dot(A)
        if all(x > 0 for x in P.flatten()):
            return True
    return False


def radius(A):
    return max(abs(complex(x)) for x in np.linalg.eigvals(np.array(A, dtype=float)))


def minimisers(det_set):
    best, arg = None, []
    for ent in product(range(0, 9), repeat=4):
        if sum(ent) > 8:
            continue
        A = np.array(ent, dtype=object).reshape(2, 2)
        dt = ent[0] * ent[3] - ent[1] * ent[2]
        if det_set is not None and dt not in det_set:
            continue
        if not primitive(A) or radius(A) <= 1 + 1e-12:
            continue
        s = sum(ent)
        if best is None or s < best:
            best, arg = s, [ent]
        elif s == best:
            arg.append(ent)
    return best, sorted(arg)


m1 = minimisers({1, -1})
m_plus = minimisers({1})
out["(2)_min_|det|=1"] = {"cost": m1[0], "matrices": [list(x) for x in m1[1]]}
out["(2)_min_det=+1"] = {"cost": m_plus[0], "matrices": [list(x) for x in m_plus[1]]}
F = sp.Matrix([[1, 1], [1, 0]])
L = sp.Matrix([[1, 1], [0, 1]])
R = sp.Matrix([[1, 0], [1, 1]])
P = sp.Matrix([[0, 1], [1, 0]])
phi = (1 + sp.sqrt(5)) / 2
ev = set(F.eigenvals().keys())
fib = {"F_symmetric": F == F.T, "det_F": int(F.det()), "anti_symplectic": F.T * J * F == -J,
       "eigs_phi_and_-1/phi": ev == {sp.simplify(phi), sp.simplify(-1 / phi)} or
       {sp.nsimplify(x) for x in ev} == {sp.nsimplify(phi), sp.nsimplify(-1 / phi)},
       "F=LP": F == L * P, "F^2=LR": F * F == L * R, "PFP": list(P * F * P)}
out["(2)_fibonacci"] = {k: (str(v) if not isinstance(v, bool) else v) for k, v in fib.items()}
ok2 = (m1 == (3, sorted([(0, 1, 1, 1), (1, 1, 1, 0)])) and m_plus == (5, sorted([(1, 1, 1, 2), (2, 1, 1, 1)]))
       and fib["F_symmetric"] and fib["det_F"] == -1 and fib["anti_symplectic"] and fib["F=LP"] and fib["F^2=LR"])
# (3) characteristic two
Bxy = lambda x, y: (x * y) % 2
skew = all(Bxy(x, y) == (-Bxy(y, x)) % 2 for x in (0, 1) for y in (0, 1))
alternating = all(Bxy(x, x) == 0 for x in (0, 1))
# a form on F2^1 is B(x, y) = c x y; alternating means B(1, 1) = c = 0, so only the zero form is alternating
one_dim_alt_zero = [c0 for c0 in (0, 1) if (c0 * 1 * 1) % 2 == 0] == [0]
out["(3)_char2"] = {"xy_skew": skew, "xy_alternating": alternating, "1d_alternating_forms_zero": one_dim_alt_zero}
ok3 = skew and not alternating and one_dim_alt_zero
# (4) Q8 and D4
I2 = sp.eye(2)
qi, qj = sp.Matrix([[sp.I, 0], [0, -sp.I]]), sp.Matrix([[0, 1], [-1, 0]])
r90, refl = sp.Matrix([[0, -1], [1, 0]]), sp.Matrix([[1, 0], [0, -1]])


def gen_group(gens):
    G = [I2]
    frontier = [I2]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = sp.simplify(x * g)
            if not any(y == h for h in G):
                G.append(y)
                frontier.append(y)
    return G


def analyse(gens, x, y):
    G = gen_group(gens)
    centre = [g for g in G if all(g * h == h * g for h in G)]
    lifts = {(0, 0): I2, (1, 0): x, (0, 1): y, (1, 1): x * y}
    sq = {v: (0 if lifts[v] ** 2 == I2 else 1) for v in lifts}
    comm = lambda u, w: (0 if lifts[u] * lifts[w] == lifts[w] * lifts[u] else 1)
    Bp = lambda u, w: comm(u, w)
    addv = lambda u, w: ((u[0] + w[0]) % 2, (u[1] + w[1]) % 2)
    polar = all(sq[addv(u, w)] == (sq[u] + sq[w] + Bp(u, w)) % 2 for u in lifts for w in lifts)
    return {"order": len(G), "centre_order": len(centre), "pairing_nondegenerate": Bp((1, 0), (0, 1)) == 1,
            "q_on_nonzero": [sq[v] for v in [(1, 0), (0, 1), (1, 1)]], "polarisation": polar}


q8 = analyse([qi, qj], qi, qj)
d4 = analyse([r90, refl], r90, refl)
comm_ij = qi * qj * qi.inv() * qj.inv()
out["(4)_Q8"], out["(4)_D4"] = q8, d4
out["(4)_[i,j]=-1"] = comm_ij == -I2
ok4 = (q8["order"] == d4["order"] == 8 and q8["centre_order"] == d4["centre_order"] == 2 and q8["pairing_nondegenerate"]
       and d4["pairing_nondegenerate"] and q8["polarisation"] and d4["polarisation"] and q8["q_on_nonzero"] == [1, 1, 1]
       and d4["q_on_nonzero"] != [1, 1, 1] and out["(4)_[i,j]=-1"])
# (5) GL(1,Z) and the affine counterexample
units = [u for u in range(-5, 6) if u != 0 and any(u * v == 1 for v in range(-5, 6))]
orbit = [0]
for _ in range(10):
    orbit.append(orbit[-1] + 1)
out["(5)_units_of_Z"] = units
out["(5)_affine_orbit_unbounded_and_invertible"] = len(set(orbit)) == len(orbit) and all(
    (n + 1) - 1 == n for n in range(-5, 6))
ok5 = units == [-1, 1] and out["(5)_affine_orbit_unbounded_and_invertible"]
out["(6)_sources"] = {
    "arXiv:0708.0669v3": {"sha256": "677daa37e79dab060a196f3304f335344bfe8d50ee4d4424bdc8c413c7a72877",
                          "quote": "field Fq , where q is odd. Specifically, we construct a quantization functor"},
    "arXiv:0808.1664v1": {"sha256": "9783562438a2751489b47dc0ec49a82fc9f744940a2cf3b33f598d14c6698c44",
                          "quote": "THE WEIL REPRESENTATION IN CHARACTERISTIC TWO ... enhanced Lagrangians"}}
# the source's phrase: the minimisers are F 'together with its transpose'
bad = sorted({tuple(F), tuple(F.T)})
out["PLANTED_F_and_transpose_as_minimisers"] = [list(x) for x in bad]
out["PLANTED_caught"] = bad != [tuple(x) for x in m1[1]]
ok = out["(1)_MtJM=detM_J"] and ok2 and ok3 and ok4 and ok5
out["checks_ok"] = {"1": out["(1)_MtJM=detM_J"], "2": ok2, "3": ok3, "4": ok4, "5": ok5}
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
