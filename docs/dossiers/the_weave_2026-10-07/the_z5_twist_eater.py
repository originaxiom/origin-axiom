#!/usr/bin/env python3
"""W31 of the weave: THE Z5 FLUX IN E8 > (SU(5)_g x SU(5)_b)/Z5. The rule is W31_RULE.md, committed before this ran
(55c26b10). The object is chosen, not forced, so every claim is conditional: if the shared fibre carried a Z5 flux.
SU(5)_g is the gauge factor (it contains the Standard Model); SU(5)_b is the bundle factor (the Standard Model's
centraliser), where the clock C5 and the shift S5 live, embedded as diag(h, 1) in W25's SU(6)'.

  F1 the group <C5, S5> in SU(5)_b: order, centre, commutator, irreducibility, type; the lemma;
  F2 the centraliser in E8 by W25's chi248 at diag(h, 1), and the code check against the explicit SU(5)_g x SU(5)_b
     character on every element;
  F3 the matter: the multiplicities of the 5's type and of Lambda^2 5's type in the 248, and their indicators;
  F4 the flux as a hypercharge rotation (exact), the centre kernel, and the moves on the flux class for every flux;
     the Wilson-line argument is the rule's, not computed;
  F5 the moves at the puncture (flux zeta): projective order, commutant, the pieces, golden traces, the reflections,
     the bare -I, Lambda^2;
  F6 the counts for every flux zeta^m: n(10) and n(5-bar), the SU(5)^3-free counts, under the moves and under locality;
  F7 the verdict.

    python3 the_z5_twist_eater.py   ->  the_z5_twist_eater.json beside it
"""
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_six_dimensional_census as SC  # noqa: E402  (commutants)
import the_self_conjugate_weave as SW  # noqa: E402  (chi248, closure, Frobenius-Schur, averages)
import the_z6_twist_eater as Z  # noqa: E402  (compound matrices, isotypic components, subset sums)
import the_z6_twist_eater_posthoc as ZP  # noqa: E402  (eigenspaces)
import the_order_three_flux as OT  # noqa: E402  (intertwiners, det-1 lifts, projective closure, reflections, moves)

ZETA = np.exp(2j * np.pi / 5)
PHI = (1 + 5 ** 0.5) / 2
C5 = np.diag([ZETA ** k for k in range(5)])
S5 = np.zeros((5, 5), dtype=complex)
for _k in range(5):
    S5[(_k + 1) % 5, _k] = 1
I5 = np.eye(5, dtype=complex)
inv = np.linalg.inv
EXPECTED_F6 = {  # the rule's table: n(10) under the moves, under locality; the SU(5)^3-free counts, moves, locality
    1: ([-1, 1, 2, 4], [-1, 4], [-1, 2], []),
    2: ([-2, 0, 1, 3], [-2, 3], [-2, 1], []),
    3: ([-3, -1, 0, 2], [-3, 2], [-1, 2], []),
    4: ([-4, -2, -1, 1], [-4, 1], [-2, 1], [])}


def close(P, Q, tol=1e-8):
    return bool(np.allclose(P, Q, atol=tol))


def embed(h):
    """h in SU(5)_b as diag(h, 1) in SU(6)'"""
    g = np.eye(6, dtype=complex)
    g[:5, :5] = h
    return g


def chi_explicit(h):
    """the 248 at (1, h) in SU(5)_g x SU(5)_b: tr h tr h^-1 + 23 + 10 (tr h + tr h^-1) + 5 (tr L2 h + tr L2 h^-1),
    with tr L2 M = ((tr M)^2 - tr M^2) / 2"""
    hi = inv(h)
    t, ti = np.trace(h), np.trace(hi)
    e2, e2i = (t ** 2 - np.trace(h @ h)) / 2, (ti ** 2 - np.trace(hi @ hi)) / 2
    return complex(t * ti + 23 + 10 * (t + ti) + 5 * (e2 + e2i))


def mean_chi(chis, weights):
    """the mean of chi248 times the conjugate weight over the group (as SW.average, on precomputed values)"""
    s = sum(c * np.conj(w) for c, w in zip(chis, weights)) / len(chis)
    return round(float(s.real), 6), round(float(s.imag), 6)


def lifts(A, B):
    """the det-1 lifts on C^5 of the moves L, R and the bare -I at the pair (A, B)"""
    return (OT.det1(OT.intertwiners(A, B, A, A @ B)[0]), OT.det1(OT.intertwiners(A, B, A @ B, B)[0]),
            OT.det1(OT.intertwiners(A, B, inv(A), inv(B))[0]))


def keeps(U, P):
    return bool(close(U @ P, P @ U))


def run():
    res = {"rule": "W31_RULE.md (committed 55c26b10 before this ran)",
           "the object": "chosen, not forced: every claim is conditional on the shared fibre carrying a Z5 flux (a "
                         "weave-type computation, joint over the moves, on a hand-picked structure)"}
    # ---------------------------------------------------------------------------------------------------------- F1
    H = SW.closure([C5, S5], 5, cap=1000)
    scal = [h for h in H if close(h, h[0, 0] * I5)]
    lemma = all(sp.simplify(sp.exp(2 * sp.pi * sp.I * w / 5) - 1) != 0 for w in range(1, 5))
    k1 = SC.commutant([C5, S5], 5)[0]
    fs5 = SW.fs(H)
    res["F1 the group"] = {
        "det C5, det S5": [round(float(np.real(np.linalg.det(C5))), 9), round(float(np.real(np.linalg.det(S5))), 9)],
        "order of <C5, S5>": len(H),
        "its scalars (the centre)": len(scal),
        "C5 S5 C5^-1 S5^-1 = zeta 1": close(OT.comm(C5, S5), ZETA * I5),
        "commutant on C^5 (1 = irreducible)": k1,
        "Frobenius-Schur indicator of the 5 (0 = complex)": fs5,
        "lemma: zeta^w != 1 for w = 1..4, so an invariant subspace has dimension 0 or 5 (exact)": bool(lemma),
        "so no U(1) of SU(5)_b commutes with the pair (Schur)": bool(lemma and k1 == 1),
        "as the rule stated (125; centre 5; irreducible; indicator 0)": bool(
            len(H) == 125 and len(scal) == 5 and k1 == 1 and fs5 == 0.0)}
    # ---------------------------------------------------------------------------------------------------------- F2
    chis = [SW.chi248(embed(h)) for h in H]
    cdim = mean_chi(chis, [1.0] * len(H))[0]
    via_sw = SW.average([embed(h) for h in H])[0]
    diff = max(abs(c - chi_explicit(h)) for c, h in zip(chis, H))
    res["F2 the centraliser in E8"] = {
        "the mean of chi248 at diag(h, 1) over the 125 (W25's chi248)": cdim,
        "the same by SW.average itself": via_sw,
        "at h = 1, both forms": [round(SW.chi248(embed(I5)).real, 6), round(chi_explicit(I5).real, 6)],
        "the code check: chi248(diag(h, 1)) minus the explicit SU(5)_g x SU(5)_b form, largest over the 125": float(diff),
        "they agree on every element (one expression; a check of the code, not a second route)": bool(diff < 1e-9),
        "exactly SU(5)_g (24), as the rule stated": bool(abs(cdim - 24) < 1e-6 and abs(via_sw - 24) < 1e-6)}
    # ---------------------------------------------------------------------------------------------------------- F3
    m5 = mean_chi(chis, [np.trace(h) for h in H])[0]
    m5b = mean_chi(chis, [np.conj(np.trace(h)) for h in H])[0]
    L2H = [Z.compound(h, 2) for h in H]
    comp2 = Z.components([Z.compound(C5, 2), Z.compound(S5, 2)], 10)
    st2 = sorted((d, mm) for _, d, mm in comp2)
    Q2t, d2t, mult2t = comp2[0]                         # the rule: one component, (5, 2)
    ty2 = [Q2t.conj().T @ M @ Q2t for M in L2H]
    m2 = mean_chi(chis, [np.trace(M) / mult2t for M in ty2])[0]
    m2b = mean_chi(chis, [np.conj(np.trace(M)) / mult2t for M in ty2])[0]
    fs2 = round(SW.fs(ty2) / mult2t, 9)
    cc2 = Z.root_label(Z.scalar_on(Q2t, Z.compound(ZETA * I5, 2)), 5)
    # the 248 accounted for: the 25 one-dimensional characters chi_(a,b)(z C5^x S5^y) = zeta^(a x + b y) (trivial on
    # the centre) and the four 5-dimensional types (the 5, Lambda^2 5's type, their conjugates), each of dimension 5.
    # (x, y) of h = z C5^x S5^y: column 0 of h is non-zero in row y alone (z zeta^(x y)), column 1 in row y + 1 alone
    # (z zeta^(x (y + 1))), so their ratio is zeta^x
    xy = []
    for h in H:
        y = int(np.flatnonzero(abs(h[:, 0]) > 1e-6)[0])
        xy.append((Z.root_label(h[(y + 1) % 5, 1] / h[y, 0], 5), y))
    ones = {}
    for a in range(5):
        for b in range(5):
            ones[(a, b)] = mean_chi(chis, [ZETA ** (a * x + b * y) for x, y in xy])[0]
    one_dim = sum(ones.values())
    accounted = one_dim + 5 * (m5 + m5b + m2 + m2b)
    res["F3 the matter"] = {
        "multiplicity of the 5 in the 248 (the 10 of SU(5)_g)": m5,
        "of the 5-bar (the 10-bar)": m5b,
        "Lambda^2 5 under <C5, S5>: [(dimension, multiplicity)]": st2,
        "its type's central character (zeta^e on zeta 1), e": cc2,
        "multiplicity of Lambda^2 5's type in the 248 (the 5-bar of SU(5)_g, twice)": m2,
        "of its conjugate type (the 5 of SU(5)_g, twice)": m2b,
        "Frobenius-Schur indicators: the 5's type, Lambda^2 5's type (0 = complex)": [fs5, fs2],
        "a check of the code: the 248 accounted for (the one-dimensional characters' multiplicities [trivial, the "
        "others summed] and 5 x the four types')": [ones[(0, 0)], round(one_dim - ones[(0, 0)], 6), accounted],
        "as the rule stated (10 and 10; two copies of one type; complex: complete SU(5) generations, 10 + 5-bar)": bool(
            m5 == 10.0 and m5b == 10.0 and m2 == 10.0 and m2b == 10.0 and st2 == [(5, 2)] and fs5 == 0.0
            and fs2 == 0.0 and abs(accounted - 248) < 1e-6)}
    # ---------------------------------------------------------------------------------------------------------- F4
    Ysym = [sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2
    exact = all((sp.Rational(6 * j, 5) * y + sp.Rational(2 * j, 5)).is_integer for j in range(1, 5) for y in Ysym)
    Yf = np.array([float(y) for y in Ysym])
    numeric = all(close(np.diag(np.exp(2j * np.pi * (6 * j / 5) * Yf)), ZETA ** (-2 * j) * I5) for j in range(1, 5))
    nality = {"(24, 1)": (0, 0), "(1, 24)": (0, 0), "(10, 5)": (2, 1), "(10-bar, 5-bar)": (3, 4),
              "(5-bar, 10)": (4, 2), "(5, 10-bar)": (1, 3)}
    dims = {"(24, 1)": 24, "(1, 24)": 24, "(10, 5)": 50, "(10-bar, 5-bar)": 50, "(5-bar, 10)": 50, "(5, 10-bar)": 50}
    kernel = all((ng - 2 * nb) % 5 == 0 for ng, nb in nality.values())
    flux_is_y = all((3 * m - (-2 * m)) % 5 == 0 and (m - 6 * m) % 5 == 0 for m in range(1, 5))
    centre_chars = []
    for m in range(1, 5):
        via6 = SW.chi248(embed(ZETA ** m * I5))
        viay = sum(dims[k] * ZETA ** (nality[k][0] * 3 * m) for k in dims)
        centre_chars.append(bool(abs(via6 - viay) < 1e-9))
    expected = {"L": 1, "R": 1, "-I": 1, "P (the swap)": 0, "P o K (the swap with complex conjugation)": 1}
    moves_rows = {}
    ok_moves = True
    for m in range(1, 5):
        A = np.linalg.matrix_power(C5, m)
        row = {}
        for nm, (pa, pb) in OT.moves_of(A, S5).items():
            cm = OT.comm(pa, pb)
            cls = ("zeta^%d" % m if close(cm, ZETA ** m * I5) else
                   "zeta^-%d" % m if close(cm, ZETA ** (-m) * I5) else "other")
            row[nm] = {"commutator of the image pair": cls,
                       "intertwiners (dimension)": len(OT.intertwiners(A, S5, pa, pb))}
        moves_rows["zeta^%d" % m] = row
        ok_moves &= {nm: v["intertwiners (dimension)"] for nm, v in row.items()} == expected
        ok_moves &= row["P (the swap)"]["commutator of the image pair"] == "zeta^-%d" % m
    res["F4 the flux, the hypercharge and the orientation"] = {
        "exp(2 pi i (6j/5) Y) = zeta^(-2j) 1 on SU(5)_g's 5, Y = diag(-1/3 x3, 1/2 x2), j = 1..4 (exact: every exponent "
        "difference an integer)": bool(exact),
        "... numerically": bool(numeric),
        "the centre kernel (zeta, zeta^-2) acts trivially on every term of the 248 (N-alities, exact)": bool(kernel),
        "so the flux zeta^m in SU(5)_b is zeta^(3m) = zeta^(-2m) in Z(SU(5)_g), a hypercharge rotation (exact)": bool(
            flux_is_y),
        "a check of the code: chi248 at diag(zeta^m 1, 1) equals the branching's character at that hypercharge "
        "rotation, m = 1..4": centre_chars,
        "the moves on the flux class (every flux)": moves_rows,
        "L, R and -I keep the flux (one intertwiner each); P sends it to its conjugate (none); P o K keeps it (one); "
        "every flux": bool(ok_moves),
        "the moves force trivial hypercharge Wilson lines (up to mu_5, a centre twist of the pair)":
            "PROVED by the rule's argument (W31_RULE.md, F4); nothing is computed",
        "as the rule stated": bool(exact and numeric and kernel and flux_is_y and all(centre_chars) and ok_moves)}
    # ---------------------------------------------------------------------------------------------------------- F5
    missing = {f: [nm for nm in ("L", "R", "-I") if r[nm]["intertwiners (dimension)"] == 0]
               for f, r in moves_rows.items()}
    if any(missing.values()):
        res["F5 the moves at the puncture (flux zeta)"] = {"a move has no lift on C^5 (by flux)": missing}
        return res
    UL, UR, UI = lifts(C5, S5)
    G_lr = OT.projective_closure([UL, UR])
    G_lri = OT.projective_closure([UL, UR, UI], cap=5000)
    k_lr = SC.commutant([UL, UR], 5)[0]
    k_lri = SC.commutant([UL, UR, UI], 5)[0]
    comps = Z.components([UL, UR], 5)
    st5 = sorted((d, mm) for _, d, mm in comps)
    W2 = np.linalg.matrix_power(UL @ inv(UR) @ UL, 2)
    sp_w2 = ZP.eigenspaces(W2)
    sp_ui = ZP.eigenspaces(UI)
    pieces = [Q @ Q.conj().T for Q, _, _ in comps]
    w2_are_pieces = len(sp_w2) == len(pieces) == 2 and all(any(close(P, Pc) for Pc in pieces) for P in sp_w2)
    ui_are_pieces = len(sp_ui) == len(pieces) == 2 and all(any(close(P, Pc) for Pc in pieces) for P in sp_ui)
    spin = sorted(round(x, 6) + 0.0 for x in (-2, -PHI, -1, -1 / PHI, 0, 1 / PHI, 1, PHI, 2))
    if st5 == [(2, 1), (3, 1)]:
        Qp = {d: Q for Q, d, _ in comps}
        tr2 = sorted({round(abs(np.trace(Qp[2].conj().T @ g @ Qp[2])) ** 2, 6) for g in G_lr.values()})
        tr3 = sorted({round(abs(np.trace(Qp[3].conj().T @ g @ Qp[3])) ** 2, 6) for g in G_lr.values()})
        golden = all(any(abs(v - t) < 1e-5 for t in tr2) for v in (PHI ** 2, PHI ** -2))
        P2 = OT.projective_closure([Qp[2].conj().T @ U @ Qp[2] for U in (UL, UR)])
        P3 = OT.projective_closure([Qp[3].conj().T @ U @ Qp[3] for U in (UL, UR)])
        M2 = [Qp[2].conj().T @ U @ Qp[2] for U in (UL, UR)]
        M2 = [M / np.sqrt(np.linalg.det(M)) for M in M2]
        G2 = SW.closure(M2, 2, cap=1000)
        trs2 = sorted({round(float(np.trace(g).real), 6) + 0.0 for g in G2})
        real2 = all(abs(np.trace(g).imag) < 1e-9 for g in G2)
    else:                                               # the structure differs from the rule's: nothing piece-wise
        tr2 = tr3 = trs2 = "not read: the structure is not 3 + 2"
        golden = real2 = False
        P2 = P3 = G2 = {}
    spin_and_a5 = bool(len(G2) == 120 and real2 and trs2 == spin and len(P2) == 60 and len(P3) == 60)
    L2lifts = [Z.compound(UL, 2), Z.compound(UR, 2)]
    st10 = sorted((d, mm) for _, d, mm in Z.components(L2lifts, 10))
    res["F5 the moves at the puncture (flux zeta)"] = {
        "projective order of the lifts of L and R (SL(2, F5) = 2I: 120)": len(G_lr),
        "their commutant on C^5": k_lr,
        "their isotypic structure [(dimension, multiplicity)]": st5,
        "|tr|^2 on the 2-piece over the 120": tr2,
        "phi^2 and phi^-2 among them (golden)": bool(golden),
        "|tr|^2 on the 3-piece over the 120": tr3,
        "projective order on the 2-piece, on the 3-piece (A5: 60 each)": [len(P2), len(P3)],
        "the 2-piece: the lifts normalised to det 1 there generate (2I: 120)": len(G2),
        "... with traces (real)": [trs2, bool(real2)],
        "... the spin representation of 2I (traces 0, +-1, +-phi, +-phi^-1, +-2)": bool(
            len(G2) == 120 and real2 and trs2 == spin),
        "the 2-piece is 2I's spin representation and the 3-piece factors through A5 (projective order 60 there)": bool(
            spin_and_a5),
        "the lift of (L R^-1 L)^2: a phase times the reflection k -> c - k, with c": OT.reflection_centre(W2, 5),
        "... its eigenspace dimensions": sorted(int(round(np.trace(P).real)) for P in sp_w2),
        "... its eigenspaces are the pieces": bool(w2_are_pieces),
        "the bare -I's lift: a phase times the reflection k -> c - k, with c": OT.reflection_centre(UI, 5),
        "... the bare -I's eigenspace dimensions": sorted(int(round(np.trace(P).real)) for P in sp_ui),
        "... the bare -I's eigenspaces are the pieces": bool(ui_are_pieces),
        "the lifts of L and R keep the bare -I's eigenspaces": bool(all(keeps(U, P) for U in (UL, UR) for P in sp_ui)),
        "with the bare -I added: commutant": k_lri,
        "with the bare -I added: projective order": len(G_lri),
        "on Lambda^2 C^5 the lifts' structure [(dimension, multiplicity)]": st10,
        "as the rule stated (120; commutant 2, split 3 + 2; golden on the 2-piece, 2I's spin representation, the "
        "3-piece through A5; reflections 4 and 0, the first's "
        "eigenspaces the pieces, the second's not; with -I: commutant 1, order 3000; Lambda^2 = [1, 3, 6])": bool(
            len(G_lr) == 120 and k_lr == 2 and st5 == [(2, 1), (3, 1)] and golden and spin_and_a5
            and OT.reflection_centre(W2, 5) == 4 and w2_are_pieces and OT.reflection_centre(UI, 5) == 0
            and not ui_are_pieces and k_lri == 1 and len(G_lri) == 3000 and st10 == [(1, 1), (3, 1), (6, 1)])}
    # ---------------------------------------------------------------------------------------------------------- F6
    table = {}
    ok6 = True
    free_all = []
    loc10_three, loc5b_three = [], []
    for m in range(1, 5):
        A = np.linalg.matrix_power(C5, m)
        uL, uR, _ = lifts(A, S5)
        s5 = sorted((d, mm) for _, d, mm in Z.components([uL, uR], 5))
        s10 = sorted((d, mm) for _, d, mm in Z.components([Z.compound(uL, 2), Z.compound(uR, 2)], 10))
        D5, D10 = Z.subset_sums(s5), Z.subset_sums(s10)
        shift10 = 2 * ((2 * m) % 5)                     # 10 {2m/5}
        n10 = [-m + d for d in D5]
        n10_loc = [-m + d for d in (0, 5)]
        n5b = [-shift10 + d for d in D10]
        n5b_loc = [-shift10 + d for d in (0, 10)]
        free = sorted(set(n10) & set(n5b))
        free_loc = sorted(set(n10_loc) & set(n5b_loc))
        free_all += free + free_loc
        if 3 in map(abs, n10_loc):
            loc10_three.append(m)
        if 3 in map(abs, n5b_loc):
            loc5b_three.append(m)
        row = {"projective order of the lifts": len(OT.projective_closure([uL, uR])),
               "structure on the 5, on Lambda^2 5": [s5, s10],
               "d5 (move-invariant)": D5, "d10 (move-invariant)": D10,
               "n(10) = -m + d5: under the moves": n10, "n(10) under locality": n10_loc,
               "n(5-bar) = -10 {2m/5} + d10: under the moves": n5b, "n(5-bar) under locality": n5b_loc,
               "the SU(5)^3-free counts (n(10) = n(5-bar)): under the moves": free,
               "the SU(5)^3-free counts under locality": free_loc}
        table["zeta^%d" % m] = row
        ok6 &= (n10, n10_loc, free, free_loc) == EXPECTED_F6[m]
    three_free = any(abs(n) == 3 for n in free_all)
    res["F6 the counts, every flux"] = {
        "the table": table,
        "as the rule's table": bool(ok6),
        "an anomaly-free three (|n| = 3 with n(10) = n(5-bar)) for some flux, under the moves or under locality": bool(
            three_free),
        "under locality, three 10s (|n(10)| = 3) occur for the fluxes zeta^m, m": loc10_three,
        "under locality, three 5-bars (|n(5-bar)| = 3) occur for m": loc5b_three}
    # ---------------------------------------------------------------------------------------------------------- F7
    w30 = json.load(open(HERE / "the_order_three_flux.json"))
    lemma30 = w30["Q1 no order-3 flux from the forced rank-2 data (order of the puncture's image at most 2)"]
    swap_conj = all(moves_rows["zeta^%d" % m]["P (the swap)"]["intertwiners (dimension)"] == 0 for m in range(1, 5))
    gives = (res["F3 the matter"]["as the rule stated (10 and 10; two copies of one type; complex: complete SU(5) "
                                  "generations, 10 + 5-bar)"]
             and res["F4 the flux, the hypercharge and the orientation"]["as the rule stated"]
             and len(G_lr) == 120 and golden)
    res["F7 the verdict"] = {
        "what it gives (conditional): complete SU(5) generations, the hypercharge inside SU(5)_g, the moves acting "
        "through 2I with golden traces (F3, F4, F5)": bool(gives),
        "NEGATIVE: no anomaly-free three for any Z5 flux, under the moves or under locality (F6)": bool(not three_free),
        "NEGATIVE: SU(5)_g, the whole centraliser (F2), is not broken to the Standard Model by anything forced (F4: "
        "the moves force trivial hypercharge Wilson lines)": bool(abs(cdim - 24) < 1e-6),
        "NEGATIVE: an unbroken SU(5) is not the Standard Model; F-MC's derived cascade skips SU(5) (SMT, B892; its "
        "B1237 addendum corrects the landing to su(3) + su(2) + u(1)^3 and leaves the skip; B874: a statement over R)":
            "cited",
        "NEGATIVE: the flux is not forced: the forced point's puncture has order at most 2 (W30's Q1, re-read), so "
        "no flux of any order above 2 comes from the forced data": bool(lemma30),
        "... the record's order-5 structures are properties of the modulus or of threads (B206: the shadow group is "
        "a property of the modulus; the golden-covers dossier: not a golden selection)": "cited",
        "NEGATIVE: the swap sends every Z5 flux to its conjugate (F4), so it is a common point only on the swap's fork "
        "(GENESIS GM5c)": bool(swap_conj),
        "the Z5 route closes: NEGATIVE as a derivation": bool(
            gives and not three_free and abs(cdim - 24) < 1e-6 and lemma30 and swap_conj)}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_z5_twist_eater.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
