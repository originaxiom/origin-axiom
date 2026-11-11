#!/usr/bin/env python3
"""SM-C2, harvest row 1528 (ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL @ f5f1042d6): this seat's own exact check of
(a) section 2: B_Z J5 = E5/sqrt10; with U = diag(I5, J5): U E U^-1 = I2 x E5, U G U^-1 = sigma_x x E5, U H U^-1 = I2 x H5;
E_+- = (E +- G)/2 and H_+- = [E_+-, E_+-^dag] are two commuting sl2 triples, H_+ + H_- = H, each of rank 4 on the ten;
(b) section 3: the whole 248 from the 240 E8 roots and 8 Cartans, split into D5 (45,1), A3 (1,15), cross (10,6), half
(16,4) + (16bar,4bar), and each source decomposed into V_j x V_k under the two triples (their joint eigenvalues on the
ten, read from the matrices, fix their Cartan coordinates up to the D5 Weyl group); the diagonal recovery 24V0 + 11V1 +
21V2 + 11V3 + V4, also from row 1525's grading vector w directly; (c) section 5: the line formula (4) with b(a) and H(d,F)
giving the module table, the flat lines from QY = dot(T/2, root), T = (5,5,5,-3,-3,-3,-3,-3), and Q_em = (2/3)(e1+e2+e3);
(d) section 6's roster per spin and the totals 63/87 chiral, 9 vectors, 72/96 left zeros.
Planted: b(a) = floor(a/2) for every a (the a >= 1 branch dropped) must change the table."""
import json
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import sympy as sp

out = {}
# ---------- (a) the matrices ----------
H5 = sp.diag(-4, -2, 0, 2, 4)
E5 = sp.zeros(5)
for i, c in enumerate([2, sp.sqrt(6), sp.sqrt(6), 2]):
    E5[i + 1, i] = c
BZ = sp.zeros(5)
for (i, j, c) in [(1, 4, sp.sqrt(sp.Rational(2, 5))), (2, 3, -sp.sqrt(sp.Rational(3, 5)))]:
    BZ[i, j] += c
    BZ[j, i] -= c
J5 = sp.zeros(5)
for i, s in enumerate([1, -1, 1, -1, 1]):
    J5[i, 4 - i] = s
Z5 = sp.zeros(5)
blk = lambda A, B, C, D: sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))
E = blk(E5, Z5, Z5, -E5.T)
H = blk(H5, Z5, Z5, -H5)
G = sp.sqrt(10) * (blk(Z5, BZ, Z5, Z5) + blk(Z5, Z5, J5 * BZ * J5, Z5))
z = lambda M: sp.simplify(M) == sp.zeros(*M.shape)
comm = lambda A, B: A * B - B * A
U = blk(sp.eye(5), Z5, Z5, J5)
Ui = U.inv()
sx = sp.Matrix([[0, 1], [1, 0]])
kron = lambda A, B: sp.kronecker_product(A, B)
a_checks = {
    "BZ_J5_eq_E5_over_sqrt10": z(BZ * J5 - E5 / sp.sqrt(10)),
    "UEU^-1=I2xE5": z(U * E * Ui - kron(sp.eye(2), E5)),
    "UGU^-1=sigmax_x_E5": z(U * G * Ui - kron(sx, E5)),
    "UHU^-1=I2xH5": z(U * H * Ui - kron(sp.eye(2), H5)),
}
Ep, Em = (E + G) / 2, (E - G) / 2
Hp, Hm = comm(Ep, Ep.H), comm(Em, Em.H)
a_checks.update({
    "[Hp,Ep]=2Ep": z(comm(Hp, Ep) - 2 * Ep), "[Hm,Em]=2Em": z(comm(Hm, Em) - 2 * Em),
    "[Ep,Em]=0": z(comm(Ep, Em)), "[Ep,Em^dag]=0": z(comm(Ep, Em.H)), "[Hp,Hm]=0": z(comm(Hp, Hm)),
    "[Hp,Em]=0": z(comm(Hp, Em)), "[Hm,Ep]=0": z(comm(Hm, Ep)), "Hp+Hm=H": z(Hp + Hm - H),
    "rank_Ep=4": Ep.rank() == 4, "rank_Em=4": Em.rank() == 4,
})
# joint eigenvalues of (Hp, Hm) on the ten: diagonalise Hp + 10 Hm (generic combination of commuting Hermitian matrices)
P, Dg = (Hp + 10 * Hm).diagonalize()
joint = []
for k in range(10):
    v = P[:, k]
    hp = sp.simplify((Hp * v)[list(v).index(next(x for x in v if x != 0))] / next(x for x in v if x != 0))
    hm = sp.simplify((Hm * v)[list(v).index(next(x for x in v if x != 0))] / next(x for x in v if x != 0))
    joint.append((int(hp), int(hm)))
out["joint_eigs_on_ten_(H+,H-)"] = sorted(joint)
a_checks["joint_on_ten"] = sorted(joint) == sorted([(4, 0), (-4, 0), (2, 0), (-2, 0), (0, 4), (0, -4), (0, 2), (0, -2),
                                                     (0, 0), (0, 0)])
out["section2"] = a_checks
# Cartan coordinates (m-units = eigenvalue/2): the ten's weights are +-c_i, so pair them
cp, cm = (2, 1, 0, 0, 0), (0, 0, 2, 1, 0)
ten_from_c = sorted([(s * cp[i] * 2, s * cm[i] * 2) for i in range(5) for s in (1, -1)])
a_checks["cartan_pairing_reproduces_ten"] = ten_from_c == sorted(joint)

# ---------- (b) E8 and the 248 ----------
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si, sj in product((1, -1), repeat=2):
            v = [F(0)] * 8
            v[i], v[j] = F(si), F(sj)
            roots.append(tuple(v))
for signs in product((1, -1), repeat=8):
    if signs.count(-1) % 2 == 0:
        roots.append(tuple(F(s, 2) for s in signs))
assert len(roots) == 240


def source(r):
    first, last = r[:3], r[3:]
    if any(x.denominator == 2 for x in r):
        return "16,4" if sum(1 for x in last if x < 0) % 2 == 0 else "16b,4b"
    if all(x == 0 for x in first):
        return "45,1"
    if all(x == 0 for x in last):
        return "1,15"
    return "10,6"


dot = lambda a, b: sum(x * y for x, y in zip(a, b))
by_src = {}
for r in roots:
    by_src.setdefault(source(r), []).append(r)
counts = {k: len(v) for k, v in by_src.items()}
out["root_counts_by_source"] = counts
dims = {"45,1": counts["45,1"] + 5, "1,15": counts["1,15"] + 3, "10,6": counts["10,6"], "16,4": counts["16,4"],
        "16b,4b": counts["16b,4b"]}
out["dims_by_source"] = dims


def peel2(weights):
    """decompose a multiset of joint weights (m+, m-) into V_j x V_k multiplicities"""
    n = Counter(weights)
    res = Counter()
    keys = sorted({(a, b) for a, b in n if a >= 0 and b >= 0}, key=lambda t: (-t[0] - t[1], -t[0]))
    while any(v for v in n.values()):
        top = max((k for k, v in n.items() if v > 0), key=lambda t: (t[0] + t[1], t[0]))
        mult = n[top]
        j, k = top
        res[(str(j), str(k))] += mult
        mj = [j - t for t in range(int(2 * j) + 1)]
        mk = [k - t for t in range(int(2 * k) + 1)]
        for a in mj:
            for b in mk:
                n[(a, b)] -= mult
                assert n[(a, b)] >= 0, "not a sum of V_j x V_k"
    return dict(res)


def peel1(weights):
    n = Counter(weights)
    res = Counter()
    while any(v for v in n.values()):
        top = max(k for k, v in n.items() if v > 0)
        mult = n[top]
        res[str(top)] += mult
        for t in range(int(2 * top) + 1):
            n[top - t] -= mult
            assert n[top - t] >= 0
    return dict(res)


cpF = tuple(F(x) for x in (0, 0, 0) + cp)
cmF = tuple(F(x) for x in (0, 0, 0) + cm)
modules = {}
for k, rs in by_src.items():
    ws = [(dot(cpF, r), dot(cmF, r)) for r in rs]
    ncart = {"45,1": 5, "1,15": 3}.get(k, 0)
    ws += [(F(0), F(0))] * ncart
    mult = {"45,1": 1, "1,15": 15, "10,6": 6, "16,4": 4, "16b,4b": 4}[k]
    dec = peel2(ws)
    modules[k] = {f"({a},{b})": v // mult for (a, b), v in dec.items()}
    assert all(v % mult == 0 for v in dec.values())
out["two_triple_modules_per_A3_component"] = modules
expected = {"45,1": {"(1,0)": 1, "(3,0)": 1, "(0,1)": 1, "(0,3)": 1, "(2,2)": 1}, "1,15": {"(0,0)": 1},
            "10,6": {"(2,0)": 1, "(0,2)": 1}, "16,4": {"(3/2,3/2)": 1}, "16b,4b": {"(3/2,3/2)": 1}}
b_ok = modules == expected and sum(dims.values()) == 248 and dims == {"45,1": 45, "1,15": 15, "10,6": 60, "16,4": 64,
                                                                       "16b,4b": 64}
diag = [dot(cpF, r) + dot(cmF, r) for r in roots] + [F(0)] * 8
diag_dec = peel1(diag)
w = tuple(F(x) for x in (0, 0, 0, -1, 1, -2, 0, 2))
diag_w = peel1([dot(w, r) for r in roots] + [F(0)] * 8)
out["diagonal_from_two_triples"], out["diagonal_from_row1525_w"] = diag_dec, diag_w
b_ok = b_ok and diag_dec == diag_w == {"0": 24, "1": 11, "2": 21, "3": 11, "4": 1}
out["section3_ok"] = b_ok


# ---------- (c) line counts ----------
def bfun(a, planted=False):
    if planted:
        return a // 2
    return a // 2 if a <= 0 else -(-a // 2) - 1


def Hd(d, trivial):
    return 0 if d < 0 else (d if d > 0 else int(trivial))


# characters: eta in {0 (trivial), 1 (order two)}, L as an exponent of chi mod 3; eta^a L trivial iff both parts trivial
def h0(a, Lexp, eta, planted=False):
    trivial = (Lexp % 3 == 0) and ((eta * a) % 2 == 0)
    return Hd(bfun(a, planted), trivial)


def N(j, k, Lexp, eta, planted=False):
    J = j + k
    return (h0(int(J + 2), -Lexp, eta, planted) + h0(int(1 + j - k), Lexp, eta, planted)
            + h0(int(1 - j + k), Lexp, eta, planted))


def vec(j, k, Lexp, eta):
    return Hd(0, (Lexp % 3 == 0)) if (j, k) == (0, 0) else 0


table = {}
for (j, k) in [(0, 0), (1, 0), (3, 0), (2, 0), (2, 2), (F(3, 2), F(3, 2))]:
    table[f"({j},{k})"] = {f"L=chi^{L},eta={'triv' if e == 0 else 'nontriv'}": N(j, k, L, e) for L in (0, 1)
                           for e in (0, 1)}
out["module_table"] = table
exp_formula = {"(0,0)": lambda L, e: int(L == 0) + 2 * int(L == 0 and e == 0),
               "(1,0)": lambda L, e: 1 + 2 * int(L == 0), "(3,0)": lambda L, e: 3, "(2,0)": lambda L, e: 2,
               "(2,2)": lambda L, e: 2 + 2 * int(L == 0 and e == 0),
               "(3/2,3/2)": lambda L, e: 2 + 2 * int(L == 0 and e == 0)}
c_ok = all(table[m][f"L=chi^{L},eta={'triv' if e == 0 else 'nontriv'}"] == f(L, e) for m, f in exp_formula.items()
           for L in (0, 1) for e in (0, 1))
# flat lines and EM charges per source component
T = tuple(F(x) for x in (5, 5, 5, -3, -3, -3, -3, -3))
qy = lambda r: dot(T, r) / 2
qem = lambda r: F(2, 3) * (r[0] + r[1] + r[2])
lines = {}
for k, rs in by_src.items():
    for r in rs:
        key = (k, str(qem(r)))
        lines.setdefault(key, set()).add(int(qy(r)) % 3)
out["flat_line_exponents_by_source_and_Qem"] = {f"{a}|Qem={b}": sorted(v) for (a, b), v in sorted(lines.items())}
single_valued = all(len(v) == 1 for v in lines.values())
d5_qy = sorted({int(qy(r)) for r in by_src["45,1"]})
out["D5_root_QY_charges"] = d5_qy
c_ok = c_ok and single_valued and set(d5_qy) <= {0, 3, -3}


# ---------- (d) the roster ----------
def roster(eta):
    # colour/EM content of each A3 component, from the roots: 15 -> 8_0 + 1_0 + 3_(-4/3) + 3b_(4/3) etc.
    R = Counter()
    vecs = 0
    # 45 (A3 singlet, Qem = 0, L = O)
    for m, mult in expected["45,1"].items():
        j, k = [F(x) for x in m.strip("()").split(",")]
        R["1_0"] += N(j, k, 0, eta)
    # (1,15): the (0,0) module times the 15: unbroken nine (Qem 0, L = O) and the charged six
    Lq = {q: lines[("1,15", q)] for q in {b for (a, b) in lines if a == "1,15"}}
    n_unbroken = sum(1 for r in by_src["1,15"] if qem(r) == 0) + 3
    R["adj8+1_(from 15)"] += N(0, 0, 0, eta) * n_unbroken
    vecs += vec(0, 0, 0, eta) * n_unbroken
    for r in by_src["1,15"]:
        if qem(r) != 0:
            R[f"Qem={qem(r)}_(from 15)"] += N(0, 0, int(qy(r)), eta)
            vecs += vec(0, 0, int(qy(r)), eta)
    for src in ("10,6", "16,4", "16b,4b"):
        mods = expected[src]
        comp = Counter()
        for r in by_src[src]:
            comp[(qem(r), int(qy(r)) % 3)] += 1
        # per A3 component: divide the root count by the D5-side dimension (10 or 16)
        d5dim = 10 if src == "10,6" else 16
        for (q, L), cnt in comp.items():
            assert cnt % d5dim == 0
            ncomp = cnt // d5dim
            for m in mods:
                j, k = [F(x) for x in m.strip("()").split(",")]
                R[f"Qem={q}"] += ncomp * N(j, k, L, eta)
    return R, vecs


ros = {}
for eta, name in [(1, "nontrivial"), (0, "trivial")]:
    R, vecs = roster(eta)
    neutral_singlets = R["1_0"]
    n15 = R["adj8+1_(from 15)"]
    kappa = 1 + 2 * (eta == 0)
    adj8 = 8 * kappa
    one0 = neutral_singlets + kappa
    up = R[f"Qem={F(2, 3)}"]
    upb = R[f"Qem={F(-2, 3)}"]
    dn = R[f"Qem={F(-1, 3)}"]
    dnb = R[f"Qem={F(1, 3)}"]
    lp, lm = R["Qem=1"], R["Qem=-1"]
    charged15 = R[f"Qem={F(-4, 3)}_(from 15)"] + R[f"Qem={F(4, 3)}_(from 15)"]
    total = adj8 + one0 + up + upb + dn + dnb + lp + lm + charged15
    ros[name] = {"8_0_mult": kappa, "1_0": one0, "3_(2/3)_per_colour": up // 3, "3b_(-2/3)_per_colour": upb // 3,
                 "3_(-1/3)_per_colour": dn // 3, "3b_(1/3)_per_colour": dnb // 3, "1_(+1)": lp, "1_(-1)": lm,
                 "charged_15_modes": charged15, "N_chiral": total, "N_vector": vecs, "dim_ker_M_left": total + vecs,
                 "check_15_sum": n15 == adj8 + kappa}
out["roster"] = ros
d_ok = (ros["nontrivial"] == {"8_0_mult": 1, "1_0": 15, "3_(2/3)_per_colour": 4, "3b_(-2/3)_per_colour": 4,
                              "3_(-1/3)_per_colour": 2, "3b_(1/3)_per_colour": 2, "1_(+1)": 2, "1_(-1)": 2,
                              "charged_15_modes": 0, "N_chiral": 63, "N_vector": 9, "dim_ker_M_left": 72,
                              "check_15_sum": True}
        and ros["trivial"] == {"8_0_mult": 3, "1_0": 19, "3_(2/3)_per_colour": 4, "3b_(-2/3)_per_colour": 4,
                               "3_(-1/3)_per_colour": 2, "3b_(1/3)_per_colour": 2, "1_(+1)": 4, "1_(-1)": 4,
                               "charged_15_modes": 0, "N_chiral": 87, "N_vector": 9, "dim_ker_M_left": 96,
                               "check_15_sum": True})
out["checks_ok"] = {"a": all(a_checks.values()), "b": b_ok, "c": c_ok, "d": d_ok}
planted = {m: N(*[F(x) for x in m.strip("()").split(",")], 1, 1, planted=True) for m in table}
out["PLANTED_b_floor_everywhere_table"] = planted
out["PLANTED_caught"] = any(planted[m] != table[m]["L=chi^1,eta=nontriv"] for m in table)
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
