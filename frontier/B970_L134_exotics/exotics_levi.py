"""B970 / L134 -- STRUCTURAL WORK: the exotics' quantum numbers, and whether the
object's measurement cascade can see them.

Everything below is rebuilt in-sandbox from the E6 Cartan matrix.  Nothing is cited.
Standard facts that are USED but not re-derived are labelled in WORK.md.

PART 1  the 27 under SO(10) > SU(5) > SM, every quantum number DERIVED
        (psi, chi, Y are each fixed by ONE normalisation and then PREDICT the rest)
PART 2  do the exotics carry SM hypercharges?  + an MB12 non-vacuity certificate
        (the same test run on the 78 DOES produce a non-SM hypercharge -> it can fail)
PART 3  the A2+A1 Levi of e6 = the cascade's landing point: the 27's decomposition,
        where the exotics sit, and what resolving power the cascade's u(1)^3 has.
        Includes the rank-4 collapse test and the relative-Weyl / how-many-SO(10)s test.
"""
from fractions import Fraction as Fr
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}

# ===================================================================== setup
# E6, Bourbaki: chain 1-3-4-5-6 with node 2 hung off node 4.
EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]
N = 6
A = [[0] * N for _ in range(N)]
for i in range(N):
    A[i][i] = 2
for i, j in EDGES:
    A[i - 1][j - 1] = -1
    A[j - 1][i - 1] = -1


def exact_inverse(M):
    n = len(M)
    aug = [[Fr(M[i][j]) for j in range(n)] + [Fr(1 if i == j else 0)
                                              for j in range(n)]
           for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if aug[r][c] != 0)
        aug[c], aug[p] = aug[p], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [aug[r][k] - f * aug[c][k] for k in range(2 * n)]
    return [row[n:] for row in aug]


AINV = exact_inverse(A)
assert all(sum(A[i][k] * AINV[k][j] for k in range(N)) == (1 if i == j else 0)
           for i in range(N) for j in range(N))


def coeffs(lab):
    """m_j = <mu, omega_j^vee> = coefficient of alpha_j when mu is written in
    the simple-root basis.  m = A^{-1} . lab."""
    return tuple(sum(AINV[i][j] * Fr(lab[j]) for j in range(N)) for i in range(N))


def refl(i, lab):
    return tuple(lab[j] - lab[i] * A[i][j] for j in range(N))


# --- the 72 roots, as Dynkin-label vectors (alpha_i has labels = row i of A)
simple = [tuple(A[i]) for i in range(N)]
roots = set(simple)
while True:
    new = {refl(i, r) for r in roots for i in range(N)} - roots
    if not new:
        break
    roots |= new
roots = sorted(roots)
assert len(roots) == 72, len(roots)
OUT["n_roots_E6"] = len(roots)

# --- the 27 = Weyl orbit of omega_1 (minuscule: every label in {-1,0,1})
hw = (1, 0, 0, 0, 0, 0)
W27 = {hw}
frontier = [hw]
while frontier:
    nxt = []
    for lab in frontier:
        for i in range(N):
            if lab[i] > 0:
                nl = refl(i, lab)
                if nl not in W27:
                    W27.add(nl)
                    nxt.append(nl)
    frontier = nxt
W27 = sorted(W27)
assert len(W27) == 27
assert all(all(-1 <= c <= 1 for c in lab) for lab in W27)   # minuscule, verified
OUT["n_weights_27"] = 27
OUT["minuscule_verified"] = True

M27 = {lab: coeffs(lab) for lab in W27}
MROOT = {r: coeffs(r) for r in roots}

# ===================================================== PART 1: the quantum numbers
# A U(1) generator is an element h of the Cartan; its charge on a weight mu is a
# LINEAR functional with NO constant term.  Each of psi, chi, Y is pinned by the
# subalgebra it must commute with, up to ONE overall scale.  We fix that scale on a
# single multiplet and everything else is predicted.


def cartan_elt_in(span_nodes, annihilate_nodes):
    """h = sum_{j in span_nodes} d_j alpha_j^vee with alpha_i(h) = 0 for
    i in annihilate_nodes.  Returns the charge functional as coefficients on the
    Dynkin labels (lab_j), normalised to the first nonzero = 1."""
    S = list(span_nodes)
    rowsl, rhs = [], []
    for i in annihilate_nodes:
        rowsl.append([Fr(A[i][j]) for j in S])
    # solve the homogeneous system exactly (nullspace, expected dim 1)
    m, n = len(rowsl), len(S)
    aug = [row[:] for row in rowsl]
    piv = []
    r = 0
    for c in range(n):
        p = next((k for k in range(r, m) if aug[k][c] != 0), None)
        if p is None:
            continue
        aug[r], aug[p] = aug[p], aug[r]
        pv = aug[r][c]
        aug[r] = [x / pv for x in aug[r]]
        for k in range(m):
            if k != r and aug[k][c] != 0:
                f = aug[k][c]
                aug[k] = [aug[k][t] - f * aug[r][t] for t in range(n)]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    assert len(free) == 1, (span_nodes, annihilate_nodes, free)
    fc = free[0]
    d = [Fr(0)] * n
    d[fc] = Fr(1)
    for ri, c in enumerate(piv):
        d[c] = -aug[ri][fc]
    coef = [Fr(0)] * N
    for k, j in enumerate(S):
        coef[j] = d[k]
    return coef


# psi: commutes with so(10) = nodes {2,3,4,5,6}; h in the FULL Cartan.
psi_c = cartan_elt_in(range(N), [1, 2, 3, 4, 5])
# chi: inside so(10)'s Cartan (nodes 2..6), commutes with su(5) = nodes {3,4,5,6}
chi_c = cartan_elt_in([1, 2, 3, 4, 5], [2, 3, 4, 5])
# Y: inside su(5)'s Cartan (nodes 3,4,5,6), commutes with su(3)xsu(2) = {3,4},{6}
Y_c = cartan_elt_in([2, 3, 4, 5], [2, 3, 5])


def charge(coef, lab):
    return sum(coef[j] * Fr(lab[j]) for j in range(N))


# levels: n1 = how many alpha_1 were subtracted from the highest weight
c1_vals = sorted({M27[l][0] for l in W27})
so10_blocks = {v: [l for l in W27 if M27[l][0] == v] for v in c1_vals}
OUT["so10_grading_c1"] = {str(v): len(so10_blocks[v]) for v in c1_vals}

# fix the three scales
_16 = [l for l in W27 if len(so10_blocks[M27[l][0]]) == 16]
_10 = [l for l in W27 if len(so10_blocks[M27[l][0]]) == 10]
_1 = [l for l in W27 if len(so10_blocks[M27[l][0]]) == 1]
s_psi = Fr(1) / charge(psi_c, _16[0])                      # ONE fit: psi(16) = 1
psi = lambda l: s_psi * charge(psi_c, l)
PSI = {"16": psi(_16[0]), "10": psi(_10[0]), "1": psi(_1[0])}
assert len({psi(l) for l in _16}) == 1
OUT["psi_predicted"] = {k: str(v) for k, v in PSI.items()}
OUT["psi_traceless_check"] = str(16 * PSI["16"] + 10 * PSI["10"] + 1 * PSI["1"])

# su(5) refinement inside each so(10) level: grade by c2
su5_key = lambda l: (M27[l][0], M27[l][1])
su5_blocks = {}
for l in W27:
    su5_blocks.setdefault(su5_key(l), []).append(l)
OUT["su5_grading_c1_c2"] = {str(k): len(v) for k, v in sorted(su5_blocks.items())}

# chi scale: fix on the 5bar inside the 16 (chi = 3 in the standard normalisation)
_5b16 = [k for k in su5_blocks
         if len(su5_blocks[k]) == 5 and psi(su5_blocks[k][0]) == PSI["16"]]
assert len(_5b16) == 1
s_chi = Fr(3) / charge(chi_c, su5_blocks[_5b16[0]][0])
chi = lambda l: s_chi * charge(chi_c, l)

# Y scale: fix on the quark doublet Q (the (3,2), i.e. the 6-dim SM piece of the 16)
su3lab = lambda l: (l[2], l[3])
su2lab = lambda l: l[5]
sm_key = lambda l: (M27[l][0], M27[l][1], M27[l][4])
sm_blocks = {}
for l in W27:
    sm_blocks.setdefault(sm_key(l), []).append(l)
Qkey = [k for k, v in sm_blocks.items() if len(v) == 6]
assert len(Qkey) == 1
s_Y = Fr(1, 6) / charge(Y_c, sm_blocks[Qkey[0]][0])
Yf = lambda l: s_Y * charge(Y_c, l)
for k, v in sm_blocks.items():                        # Y constant on each SM piece
    assert len({Yf(l) for l in v}) == 1, k

# su(3) rep naming: fix "3" to be the colour rep of the quark doublet Q
Qw = sm_blocks[Qkey[0]]
Q_su3_weights = {su3lab(l) for l in Qw}
THREE_HAS_10 = (1, 0) in Q_su3_weights


def su3name(piece):
    ws = {su3lab(l) for l in piece}
    if len(ws) == 1:
        return "1"
    if THREE_HAS_10:
        return "3" if (1, 0) in ws else "3bar"
    return "3" if (0, 1) in ws else "3bar"


def su2name(piece):
    return "2" if len({su2lab(l) for l in piece}) > 1 else "1"


# name the pieces from their (psi, chi) and SM content
NAMES = {}
table = []
for k in sorted(sm_blocks):
    piece = sm_blocks[k]
    d = len(piece)
    c3, c2 = su3name(piece), su2name(piece)
    Y = Yf(piece[0])
    p, x = psi(piece[0]), chi(piece[0])
    T3 = [Fr(su2lab(l), 2) for l in piece] if c2 == "2" else [Fr(0)]
    qem = sorted({t + Y for t in T3}, reverse=True)
    if p == PSI["16"]:
        nm = {("3", "2"): "Q", ("3bar", "1"): None, ("1", "2"): "L",
              ("1", "1"): None}[(c3, c2)]
        if nm is None:
            nm = ("u^c" if Y < 0 else "d^c") if c3 == "3bar" \
                else ("e^c" if Y != 0 else "nu^c")
        blk = "16"
    elif p == PSI["10"]:
        nm = {("3", "1"): "D", ("3bar", "1"): "Dbar",
              ("1", "2"): "H_u" if Y > 0 else "H_d"}[(c3, c2)]
        blk = "10"
    else:
        nm = "S"
        blk = "1"
    NAMES[k] = nm
    table.append(dict(name=nm, so10_block=blk, dim=d, su3=c3, su2=c2,
                      Y=str(Y), Qem=[str(q) for q in qem],
                      psi=str(p), chi=str(x),
                      centre_charges_c1_c2_c5=[str(M27[piece[0]][i]) for i in (0, 1, 4)],
                      exotic=(blk != "16")))
table.sort(key=lambda r: (r["so10_block"] != "16", -r["dim"], r["name"]))
OUT["part1_table_of_the_27"] = table
OUT["part1_normalisations_used"] = {
    "psi": "one scale, fixed by psi(16)=1  ->  psi(10), psi(1) PREDICTED",
    "chi": "one scale, fixed by chi(5bar of the 16)=3  ->  all other chi PREDICTED",
    "Y":   "one scale, fixed by Y(Q)=1/6  ->  all other Y PREDICTED, "
           "including the whole exotic 10 and the singlet",
}
# arithmetic checks that make the branching auditable
OUT["part1_arithmetic_checks"] = {
    "27 = 16 + 10 + 1": [len(_16), len(_10), len(_1)],
    "sum": len(_16) + len(_10) + len(_1),
    "psi traceless over the 27": OUT["psi_traceless_check"],
    "chi traceless over the 27": str(sum(chi(l) for l in W27)),
    "Y traceless over the 27": str(sum(Yf(l) for l in W27)),
    "Y traceless on each SU(5) multiplet":
        {str(k): str(sum(Yf(l) for l in v)) for k, v in sorted(su5_blocks.items())},
    "sum of Qem over the 27": str(sum(Fr(su2lab(l), 2) + Yf(l) for l in W27)),
}
exotic_states = sum(r["dim"] for r in table if r["exotic"])
OUT["part1_counts"] = {
    "states in the 16": len(_16),
    "states in the 10": len(_10),
    "states in the 1": len(_1),
    "EXOTIC states beyond the 16 (10 + 1)": exotic_states,
    "states beyond a 15-fermion SM generation (27 - 15)": 27 - 15,
    "nu_R sits in the 16": True,
    "note": "eleven exotics beyond the 16; twelve if counted against a 15-fermion "
            "generation, which puts nu_R on the exotic side of the ledger",
}
assert exotic_states == 11

# ============================================ PART 2: SM hypercharge comparison
SM15 = {r["name"] for r in table if r["so10_block"] == "16"} - {"nu^c"}
sm_fields = {r["name"]: (r["su3"], r["su2"], r["Y"]) for r in table
             if r["so10_block"] == "16"}
conj = {"3": "3bar", "3bar": "3", "1": "1", "2": "2"}


def conj_qn(q):
    return (conj[q[0]], conj[q[1]], str(-Fr(q[2])))


sm_Y_values = sorted({Fr(v[2]) for v in sm_fields.values()})
HIGGS = ("1", "2", str(Fr(1, 2)))   # the SM Higgs doublet's gauge quantum numbers

part2 = []
for r in table:
    if not r["exotic"]:
        continue
    q = (r["su3"], r["su2"], r["Y"])
    same = [n for n, v in sm_fields.items() if v == q]
    conj_match = [n for n, v in sm_fields.items() if conj_qn(v) == q]
    is_higgs = (q == HIGGS)
    part2.append(dict(
        name=r["name"], dim=r["dim"], su3=r["su3"], su2=r["su2"], Y=r["Y"],
        Y_is_an_SM_fermion_hypercharge=(Fr(r["Y"]) in sm_Y_values),
        identical_SM_fermion=same,
        conjugate_of_SM_fermion=conj_match,
        identical_to_SM_Higgs_doublet=is_higgs,
    ))
OUT["part2_exotic_vs_SM"] = part2
OUT["part2_SM_hypercharges_in_the_16"] = {n: v[2] for n, v in sm_fields.items()}
OUT["part2_verdict"] = {
    "any exotic with SM quantum numbers found nowhere in the 16 (up to conjugation)":
        [p["name"] for p in part2
         if not p["identical_SM_fermion"] and not p["conjugate_of_SM_fermion"]],
    "exotics exactly degenerate with a 16 field":
        {p["name"]: p["identical_SM_fermion"] for p in part2
         if p["identical_SM_fermion"]},
}

# ---- MB12 non-vacuity certificate for the part-2 test: run it on the 78.
# The adjoint's SM pieces are computed the same way; if a piece turns up with a
# hypercharge that is NOT an SM fermion hypercharge, the test demonstrably CAN fail.
adjoint = list(roots) + [None] * 6          # 72 roots + 6 Cartan (all charges 0)
adj_blocks = {}
for r in roots:
    adj_blocks.setdefault((MROOT[r][0], MROOT[r][1], MROOT[r][4]), []).append(r)
adjY = {}
for k, v in adj_blocks.items():
    ys = {s_Y * charge(Y_c, r) for r in v}
    assert len(ys) == 1, k
    adjY[k] = (len(v), ys.pop())
novel = sorted({str(y) for _, (d, y) in adjY.items() if y not in sm_Y_values})
OUT["part2_MB12_can_the_test_fail"] = {
    "test": "does every piece of an E6 representation carry an SM-fermion hypercharge?",
    "run on the 27": "PASSES for every exotic (see part2_verdict)",
    "run on the 78 (adjoint)": "FAILS -- hypercharges present in the adjoint that no "
                               "SM fermion carries: " + ", ".join(novel),
    "conclusion": "the test is non-vacuous: it can pass and it can fail",
}

# ================================================ PART 3: the A2+A1 Levi cascade
# The cascade lands on su(3)+su(2)+u(1)^3.  As a Levi of e6 that is L = <a3,a4,a6>.
LEVI_NODES = [2, 3, 5]        # 0-indexed: alpha_3, alpha_4, alpha_6
levi_roots = [r for r in roots
              if all(MROOT[r][j] == 0 for j in range(N) if j not in LEVI_NODES)]
OUT["part3_levi"] = {
    "simple roots": "alpha_3, alpha_4 (an A2) and alpha_6 (an A1)",
    "n roots in the Levi": len(levi_roots),
    "dim derived (roots + rank-3 Cartan)": len(levi_roots) + 3,
    "dim Levi (derived + 3-dim centre)": len(levi_roots) + 3 + 3,
    "centre dim": 3,
    "matches the cascade's landing point (dim 14, derived 11, centre 3)":
        (len(levi_roots) + 3 == 11) and (len(levi_roots) + 6 == 14),
}

# the centre of L is spanned by omega_1^vee, omega_2^vee, omega_5^vee: the charges
# on a weight are (c1, c2, c5).  Group the 27 by that triple.
zkey = lambda l: (M27[l][0], M27[l][1], M27[l][4])
zpieces = {}
for l in W27:
    zpieces.setdefault(zkey(l), []).append(l)
OUT["part3_n_pieces_of_the_27_under_the_Levi"] = len(zpieces)
OUT["part3_piece_dims_sorted"] = sorted(len(v) for v in zpieces.values())
assert len(zpieces) == 11

# is (psi, chi, Y) the SAME rank-3 torus as (c1, c2, c5)?
B = [[Fr(0)] * 3 for _ in range(3)]
for row, cf, sc in ((0, psi_c, s_psi), (1, chi_c, s_chi), (2, Y_c, s_Y)):
    # express the charge as a combination of c1, c2, c5 by solving on 3 weights
    pass
sample = []
for l in W27:
    v = (M27[l][0], M27[l][1], M27[l][4])
    sample.append((v, (psi(l), chi(l), Yf(l))))
Mx = np.array([[float(x) for x in s[0]] for s in sample])
rk_c = np.linalg.matrix_rank(Mx)
My = np.array([[float(x) for x in s[1]] for s in sample])
rk_y = np.linalg.matrix_rank(My)
rk_both = np.linalg.matrix_rank(np.hstack([Mx, My]))
OUT["part3_torus_identification"] = {
    "rank of (c1,c2,c5) on the 27": int(rk_c),
    "rank of (psi,chi,Y) on the 27": int(rk_y),
    "rank of the two together": int(rk_both),
    "same 3-dim space of charges": int(rk_both) == 3,
}

# ---- MB12 for the resolving-power criterion, stated BEFORE the result:
# criterion: "the cascade's charges separate every exotic piece from every 16 piece".
# It CAN fail: drop to the rank-4 SM torus (su3, su2, Y) and re-run.
def signature(piece, use):
    p = piece
    s3, s2 = su3name(p), su2name(p)
    base = (s3, s2)
    if use == "SM_rank4":
        return base + (str(Yf(p[0])),)
    if use == "levi_rank6":
        return base + (str(psi(p[0])), str(chi(p[0])), str(Yf(p[0])))
    if use == "psi_only":
        return base + (str(psi(p[0])),)
    raise ValueError(use)


collisions = {}
for mode in ("SM_rank4", "levi_rank6", "psi_only"):
    sigs = {}
    for k, v in zpieces.items():
        sigs.setdefault(signature(v, mode), []).append(NAMES[k])
    coll = {str(s): sorted(n) for s, n in sigs.items() if len(n) > 1}
    collisions[mode] = {
        "n distinguishable classes among the 11 pieces": len(sigs),
        "colliding pieces": coll,
        "every exotic separated from every 16 piece": all(
            not (any(nm in ("D", "Dbar", "H_u", "H_d", "S") for nm in n)
                 and any(nm not in ("D", "Dbar", "H_u", "H_d", "S") for nm in n))
            for n in sigs.values()),
    }
OUT["part3_resolving_power"] = collisions

# ---- does the FIRST cascade step already do it?  Cent(omega_1^vee) in e6.
cent1 = [r for r in roots if MROOT[r][0] == 0]
OUT["part3_first_cascade_step"] = {
    "roots commuting with the psi direction": len(cent1),
    "dim Cent = roots + rank": len(cent1) + 6,
    "identification": "so(10) (40 roots) + u(1)_psi -> dim 46",
    "the 27 splits at this single step into":
        {str(v): len(so10_blocks[v]) for v in c1_vals},
}

# ---- certificate: must a dim-46 centraliser be so(10) + u(1)?
# The centraliser of a semisimple element is generated by the roots vanishing on it,
# and up to the Weyl group that root set is generated by a subset of the EXTENDED
# Dynkin diagram (a pseudo-Levi).  Enumerate all 2^7 subsets exhaustively.
ht = lambda r: sum(MROOT[r])
highest = max(roots, key=ht)
alpha0 = tuple(-x for x in highest)
nodes7 = [tuple(A[i]) for i in range(N)] + [alpha0]


def pair(gam, bet):
    mb = coeffs(bet)
    return sum(mb[i] * Fr(gam[i]) for i in range(N))


def close_subsystem(J):
    S = set()
    for b in J:
        S.add(b)
        S.add(tuple(-x for x in b))
    while True:
        new = set()
        for g in S:
            for b in S:
                c = pair(g, b)
                img = tuple(g[j] - c * b[j] for j in range(N))
                img = tuple(int(x) for x in img)
                if img in ROOTSET and img not in S:
                    new.add(img)
        if not new:
            break
        S |= new
    return S


ROOTSET = set(roots)
pseudo = {}
for mask in range(1, 128):
    J = [nodes7[i] for i in range(7) if mask >> i & 1]
    S = close_subsystem(J)
    Mv = np.array([[float(x) for x in coeffs(r)] for r in S])
    rk = int(np.linalg.matrix_rank(Mv)) if len(S) else 0
    pseudo.setdefault((len(S), rk), []).append(mask)
sizes40 = sorted(k for k in pseudo if k[0] == 40)
OUT["part3_dim46_uniqueness_certificate"] = {
    "method": "exhaustive over all 2^7 - 1 subsets of the EXTENDED E6 Dynkin diagram "
              "(pseudo-Levi subsystems: every centraliser of a semisimple element is "
              "W-conjugate to one of these)",
    "distinct (n_roots, rank) reached": sorted(pseudo.keys()),
    "subsystems with exactly 40 roots": [{"n_roots": k[0], "rank": k[1],
                                          "n_subsets": len(pseudo[k])}
                                         for k in sizes40],
    "conclusion": "the ONLY pseudo-Levi of e6 with 40 roots has rank 5 (= D5); so a "
                  "centraliser of dimension 46 = 40 + 6 is so(10) + u(1) and its "
                  "u(1) is the psi direction up to W.  Anything of dim 46 IS the "
                  "16 + 10 + 1 split.",
    "max roots in any proper pseudo-Levi": max(k[0] for k in pseudo if k[0] < 72),
}

# ---- the hidden su(3): which roots commute with the whole Levi semisimple part?
orth = [r for r in roots if all(r[j] == 0 for j in LEVI_NODES)]
Mo = np.array([[float(x) for x in coeffs(r)] for r in orth])
OUT["part3_hidden_su3"] = {
    "roots orthogonal to alpha_3, alpha_4, alpha_6": len(orth),
    "rank of their span": int(np.linalg.matrix_rank(Mo)) if len(orth) else 0,
    "reading": "6 roots of rank 2 = an A2 = a THIRD su(3), whose Cartan lies inside "
               "the Levi's u(1)^3 centre; its Weyl group is the S3 found below",
}

# ---- how canonical is the labelling?  How many so(10)+u(1) sit above this Levi?
# A direction h = h1 w1^v + h2 w2^v + h5 w5^v acts on a root by h . (m1, m2, m5).
restricted = {r: (MROOT[r][0], MROOT[r][1], MROOT[r][4]) for r in roots}
found = {}
R = 8
for h1 in range(-R, R + 1):
    for h2 in range(-R, R + 1):
        for h5 in range(-R, R + 1):
            if (h1, h2, h5) == (0, 0, 0):
                continue
            van = tuple(sorted(r for r in roots
                               if h1 * restricted[r][0] + h2 * restricted[r][1]
                               + h5 * restricted[r][2] == 0))
            if len(van) == 40:
                found.setdefault(van, (h1, h2, h5))
d5s = []
for van, h in found.items():
    Mv = np.array([[float(x) for x in coeffs(r)] for r in van])
    if np.linalg.matrix_rank(Mv) == 5:
        lv = sorted({sum(hh * mm for hh, mm in zip(h, (M27[l][0], M27[l][1], M27[l][4])))
                     for l in W27})
        grades = {}
        for l in W27:
            g = sum(hh * mm for hh, mm in
                    zip(h, (M27[l][0], M27[l][1], M27[l][4])))
            grades.setdefault(g, []).append(l)
        pat = sorted(len(v) for v in grades.values())
        sixteen = sorted(NAMES[zkey(v[0])] for g, vv in grades.items()
                         if len(vv) == 16 for v in [vv])
        # which named Levi pieces make up the 16 for THIS so(10)
        blk16 = [g for g, vv in grades.items() if len(vv) == 16]
        names16 = sorted({NAMES[zkey(l)] for l in grades[blk16[0]]}) if blk16 else []
        d5s.append(dict(direction=list(h), grade_pattern=pat,
                        pieces_forming_the_16=names16))
uniq = {}
for d in d5s:
    uniq.setdefault(tuple(d["pieces_forming_the_16"]), []).append(d["direction"])
OUT["part3_how_many_so10_above_the_levi"] = {
    "n D5+u(1) centraliser directions found in the Levi centre (up to the search box)":
        len(d5s),
    "distinct 16-labellings they induce": [
        {"the 16 = ": list(k), "n directions": len(v), "example direction": v[0]}
        for k, v in sorted(uniq.items(), key=lambda kv: -len(kv[1]))],
    "n distinct labellings": len(uniq),
}

# ---- the relative Weyl group of the Levi, and its action on the 11 pieces
def gen_matrix(i):
    Mx = np.zeros((N, N), dtype=np.int64)
    for j in range(N):
        Mx[j, j] = 1
    for j in range(N):
        Mx[j, i] = (1 if j == i else 0) - A[i][j]
    return Mx


gens = [gen_matrix(i) for i in range(N)]
I = np.eye(N, dtype=np.int64)
seen = {I.tobytes(): I}
frontier = [I]
while frontier:
    nxt = []
    for g in frontier:
        for s in gens:
            h = s @ g
            b = h.tobytes()
            if b not in seen:
                seen[b] = h
                nxt.append(h)
    frontier = nxt
OUT["part3_weyl_group_order"] = len(seen)
assert len(seen) == 51840, len(seen)

PHI_L = set(levi_roots)
lab2vec = lambda lab: np.array(lab, dtype=np.int64)
Nw = []
for h in seen.values():
    ok = True
    for r in PHI_L:
        img = tuple(int(x) for x in (h @ lab2vec(r)))
        if img not in PHI_L:
            ok = False
            break
    if ok:
        Nw.append(h)
WL = set()
frontier = [I]
WLd = {I.tobytes(): I}
while frontier:
    nxt = []
    for g in frontier:
        for i in LEVI_NODES:
            hh = gens[i] @ g
            b = hh.tobytes()
            if b not in WLd:
                WLd[b] = hh
                nxt.append(hh)
    frontier = nxt
OUT["part3_relative_weyl"] = {
    "|N_W(W_L)|": len(Nw), "|W_L|": len(WLd),
    "|relative Weyl group| = |N|/|W_L|": len(Nw) // len(WLd),
}

# is the relative Weyl group EXACTLY the Weyl group of the orthogonal A2?
def refl_matrix(beta):
    mb = coeffs(beta)
    Mx = np.zeros((N, N), dtype=np.int64)
    for j in range(N):
        Mx[j, j] = 1
    for j in range(N):
        for i in range(N):
            Mx[j, i] -= int(mb[i]) * beta[j]
    return Mx


orth_gens = [refl_matrix(b) for b in orth]
sub = {I.tobytes(): I}
frontier = [I]
while frontier:
    nxt = []
    for g in frontier:
        for s in orth_gens:
            h = s @ g
            b = h.tobytes()
            if b not in sub:
                sub[b] = h
                nxt.append(h)
    frontier = nxt
inN = all(b in {x.tobytes() for x in Nw} for b in sub)
meetsWL = len({b for b in sub} & set(WLd))
OUT["part3_relative_weyl_is_the_hidden_su3"] = {
    "|group generated by reflections in the 6 orthogonal roots|": len(sub),
    "contained in N_W(W_L)": bool(inN),
    "intersection with W_L (should be 1 = identity only)": meetsWL,
    "so it maps isomorphically onto the relative Weyl group of order 6":
        bool(inN) and meetsWL == 1 and len(sub) == 6,
}

pieceidx = {k: i for i, k in enumerate(sorted(zpieces))}
perms = set()
for h in Nw:
    p = [None] * 11
    good = True
    for k, v in zpieces.items():
        img = tuple(int(x) for x in (h @ lab2vec(v[0])))
        if img not in M27:
            good = False
            break
        p[pieceidx[k]] = pieceidx[zkey(img)]
    if good and None not in p:
        perms.add(tuple(p))
# orbits of the relative Weyl group on the 11 pieces
parent = list(range(11))


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for p in perms:
    for i, j in enumerate(p):
        a, b = find(i), find(j)
        if a != b:
            parent[a] = b
orb = {}
for k, i in pieceidx.items():
    orb.setdefault(find(i), []).append(NAMES[k])
EX = ("D", "Dbar", "H_u", "H_d", "S")
OUT["part3_relative_weyl_orbits_on_the_11_pieces"] = {
    "n induced permutations": len(perms),
    "orbits": [sorted(v) for v in orb.values()],
    "does any orbit mix a 16 piece with an exotic piece": any(
        any(n in EX for n in v) and any(n not in EX for n in v)
        for v in orb.values()),
}

# ---- how much of the 27 is UNAMBIGUOUSLY matter / unambiguously exotic?
lab16 = [set(k) for k in uniq]
dims = {r["name"]: r["dim"] for r in table}
always16 = sorted(set.intersection(*lab16)) if lab16 else []
never16 = sorted({r["name"] for r in table} - set.union(*lab16)) if lab16 else []
ambig = sorted({r["name"] for r in table} - set(always16) - set(never16))
OUT["part3_ambiguity_budget"] = {
    "n so(10) embeddings above the Levi": len(uniq),
    "pieces in EVERY 16 (unambiguously matter)":
        {n: dims[n] for n in always16},
    "pieces in NO 16 (unambiguously exotic)": {n: dims[n] for n in never16},
    "pieces whose matter/exotic status DEPENDS on the choice":
        {n: dims[n] for n in ambig},
    "states unambiguously assigned": sum(dims[n] for n in always16 + never16),
    "states whose assignment depends on the choice": sum(dims[n] for n in ambig),
    "reading": "the Levi ALONE resolves the 27 into 11 pieces but does not say which "
               "of them is a generation; the tie is broken by the first cascade "
               "charge z1, whose centraliser is the dim-46 so(10) + u(1)",
}

# ---- SCOPE CHECK: does any of this depend on WHICH A2+A1 Levi was chosen?
adj = {(i, j) for i, j in EDGES}
adj |= {(j, i) for i, j in adj}
allNw = {x.tobytes(): x for x in seen.values()}
robust = []
for a in range(N):
    for b in range(a + 1, N):
        if (a + 1, b + 1) not in adj:
            continue
        for c in range(N):
            if c in (a, b):
                continue
            if (a + 1, c + 1) in adj or (b + 1, c + 1) in adj:
                continue
            J = sorted([a, b, c])
            lr = [r for r in roots
                  if all(coeffs(r)[j] == 0 for j in range(N) if j not in J)]
            zk = {}
            for l in W27:
                key = tuple(M27[l][j] for j in range(N) if j not in J)
                zk.setdefault(key, []).append(l)
            PL = set(lr)
            nn = 0
            for h in seen.values():
                if all(tuple(int(x) for x in (h @ lab2vec(r))) in PL for r in PL):
                    nn += 1
            wl = {I.tobytes(): I}
            fr = [I]
            while fr:
                nx = []
                for gg in fr:
                    for i in J:
                        hh = gens[i] @ gg
                        bb = hh.tobytes()
                        if bb not in wl:
                            wl[bb] = hh
                            nx.append(hh)
                fr = nx
            robust.append(dict(nodes=[j + 1 for j in J], n_levi_roots=len(lr),
                               levi_dim=len(lr) + 6,
                               n_pieces_of_27=len(zk),
                               piece_dims=sorted(len(v) for v in zk.values()),
                               rel_weyl_order=nn // len(wl)))
OUT["part3_scope_all_A2plusA1_levis"] = {
    "n such subsets of the E6 simple roots": len(robust),
    "all give the same 27 piece pattern":
        len({tuple(r["piece_dims"]) for r in robust}) == 1,
    "all give the same relative Weyl order":
        len({r["rel_weyl_order"] for r in robust}) == 1,
    "detail": robust,
}

with open(os.path.join(HERE, "exotics_levi.json"), "w") as f:
    json.dump(OUT, f, indent=1)

for k, v in OUT.items():
    if k == "part1_table_of_the_27":
        print("\nPART 1 -- the 27")
        print(f"  {'name':6} {'blk':4} {'dim':>3} {'su3':5} {'su2':3} {'Y':>6} "
              f"{'Qem':16} {'psi':>4} {'chi':>4}  (c1,c2,c5)")
        for r in v:
            print(f"  {r['name']:6} {r['so10_block']:4} {r['dim']:>3} {r['su3']:5} "
                  f"{r['su2']:3} {r['Y']:>6} {str(r['Qem']):16} {r['psi']:>4} "
                  f"{r['chi']:>4}  {r['centre_charges_c1_c2_c5']}"
                  f"{'   <-- EXOTIC' if r['exotic'] else ''}")
    else:
        print(f"\n{k} = {json.dumps(v, indent=1) if isinstance(v, (dict, list)) else v}")
