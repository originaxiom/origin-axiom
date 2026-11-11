#!/usr/bin/env python3
"""SM-C2, harvest row 1525 (EXACT_ORDER_THREE_ELECTROWEAK_BRANCH @ e181282de): this seat's own check, exact (sympy), of
(a) section 2's root arithmetic in E8 coordinates (w-grades of alpha, beta, gamma, delta; no difference of squared length
2; the Cartan sum = H/10 with H = 2w), (b) section 3's D5 realisation in the 10 x 10 block form X = [[A, B], [C, -A^T]]:
E = diag(E5, -E5^T), H = diag(H5, -H5), h_- = [[0, B_Z], [0, 0]], h_+ = [[0, 0], [J5 B_Z J5, 0]] -- [E, Y0] = 0,
[H, Y0] = 2 Y0, [Y0, Y0^dag] = H/10, kappa = (1/2) Tr, kappa(E^dag E) = kappa(G^dag G) = 20, kappa(E^dag G) = 0,
[E, E^dag] = H, [E, G] = 0, and (c) the vacuum equation (6): F/dvol + [q, q^dag] + [r, r^dag] = (-1 + |a|^2 + |b|^2) H/(4 l^2).
Z = sqrt(2/5) b1^b4 - sqrt(3/5) b2^b3 (0-based, the grade-2 pairs of H5 = diag(-4,-2,0,2,4)). Planted: the opposite
relative sign in Z (not a highest vector) must break [E, Y0] = 0."""
import json
import sys
from pathlib import Path

import sympy as sp

out = {}
# (a) roots
e = lambda *idx: sp.Matrix([1 if i + 1 in idx else 0 for i in range(8)])
w = sp.Matrix([0, 0, 0, -1, 1, -2, 0, 2])
alpha, beta = e(4) + e(8), e(5) + e(7)
gamma, delta = -(e(5) + e(6)), -(e(4) + e(7))
roots = {"alpha": alpha, "beta": beta, "gamma": gamma, "delta": delta}
out["grades"] = {k: int((v.T * w)[0]) for k, v in roots.items()}
names = list(roots)
out["difference_sq_lengths"] = {f"{a}-{b}": int(((roots[a] - roots[b]).T * (roots[a] - roots[b]))[0])
                                for i, a in enumerate(names) for b in names[i + 1:]}
cart = sp.Rational(2, 5) * (alpha + gamma) + sp.Rational(3, 5) * (beta + delta)
out["cartan_minus_H_over_10"] = [str(x) for x in (cart - 2 * w / 10)]
roots_ok = (all(g == 1 for g in out["grades"].values()) and all(d in (4, 6) for d in out["difference_sq_lengths"].values())
            and all(x == 0 for x in (cart - 2 * w / 10)))


# (b) D5 matrices
def build(sign=-1):
    H5 = sp.diag(-4, -2, 0, 2, 4)
    E5 = sp.zeros(5)
    for i, c in enumerate([2, sp.sqrt(6), sp.sqrt(6), 2]):
        E5[i + 1, i] = c                       # raising: b_i -> c_i b_(i+1)
    BZ = sp.zeros(5)
    def wedge(i, j, c):
        BZ[i, j] += c
        BZ[j, i] -= c
    wedge(1, 4, sp.sqrt(sp.Rational(2, 5)))
    wedge(2, 3, sign * sp.sqrt(sp.Rational(3, 5)))
    J5 = sp.zeros(5)
    for i, s in enumerate([1, -1, 1, -1, 1]):
        J5[i, 4 - i] = s
    Z5 = sp.zeros(5)
    blk = lambda A, B, C, D: sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))
    E = blk(E5, Z5, Z5, -E5.T)
    H = blk(H5, Z5, Z5, -H5)
    hm = blk(Z5, BZ, Z5, Z5)
    hp = blk(Z5, Z5, J5 * BZ * J5, Z5)
    return E, H, hm, hp, E5, BZ


comm = lambda A, B: A * B - B * A
dag = lambda A: A.H
kappa = lambda A, B: sp.simplify((A * B).trace() / 2)
E, H, hm, hp, E5, BZ = build()
Y0 = hp + hm
G = sp.sqrt(10) * Y0
z = lambda M: sp.simplify(M) == sp.zeros(*M.shape)
checks = {
    "E5_on_Z_highest": z(E5 * BZ + BZ * E5.T),
    "[E,h-]=0": z(comm(E, hm)), "[E,h+]=0": z(comm(E, hp)), "[E,Y0]=0": z(comm(E, Y0)),
    "[H,Y0]=2Y0": z(comm(H, Y0) - 2 * Y0), "[Y0,Y0dag]=H/10": z(comm(Y0, dag(Y0)) - H / 10),
    "[G,Gdag]=H": z(comm(G, dag(G)) - H), "[H,G]=2G": z(comm(H, G) - 2 * G), "[E,G]=0": z(comm(E, G)),
    "[E,Edag]=H": z(comm(E, dag(E)) - H),
    "kappa(Edag E)=20": kappa(dag(E), E) == 20, "kappa(Gdag G)=20": kappa(dag(G), G) == 20,
    "kappa(Edag G)=0": kappa(dag(E), G) == 0, "kappa(Y0dag Y0)=2": kappa(dag(Y0), Y0) == 2,
    "root_norm_one": kappa(dag(hm), hm) == 1,
}
out["d5_checks"] = checks
top = sp.simplify(comm(Y0, dag(Y0))[:5, :5])
out["top_block_of_[Y0,Y0dag]"] = [str(top[i, i]) for i in range(5)]
# (c) the vacuum equation with symbolic a, b, ell (F/dvol = -H/(4 l^2))
a, b = sp.symbols("a b")
l = sp.Symbol("ell", positive=True)
q = a * E / (2 * l)
r = b * G / (2 * l)
lhs = -H / (4 * l ** 2) + comm(q, dag(q)) + comm(r, dag(r))
target = (-1 + a * sp.conjugate(a) + b * sp.conjugate(b)) * H / (4 * l ** 2)
checks["vacuum_eq6"] = z(sp.expand(lhs - target))
checks["[q,r]=0"] = z(comm(q, r))
ok = roots_ok and all(checks.values())
E2, H2, hm2, hp2, *_ = build(sign=+1)
out["PLANTED_wrong_sign_in_Z_breaks_[E,Y0]"] = not z(comm(E2, hp2 + hm2))
out["roots_ok"] = roots_ok
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_wrong_sign_in_Z_breaks_[E,Y0]"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
