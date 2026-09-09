"""B1265 -- THE REAL FORM IS DERIVED, AND THE FORK IS INNER vs OUTER.

MAIN_GOAL JOIN 3.  B1140 banked the fork as a brute fact: "the fork's two real forms split
the world with NOTHING SHARED -- E6(-14) took the charges (Y-selection, sin^2θ_W, the
generation table, the anomaly zeros, B-L), E6(-26) took the geometry (Lorentz, compact
colour, the graviton)."  No arc crosses it, and B1263/B1264 localised I-10 and I-11 to it,
pricing it at 2 units on B1261's scoreboard.  This arc asks whether the fork is FORCED or an
artifact of a choice -- and the answer is neither: it is a rank obstruction.

(1) THE REAL FORM IS DERIVED, NOT CHOSEN.  Real forms of a complex simple Lie algebra
    correspond (Cartan) to involutions up to conjugacy, labelled by the SIGNATURE
    dim p - dim k with k the fixed subalgebra.  D2 -- the object's OWN twist (B916's 11-flip,
    decoded by B1250 as the SO(10) grading) -- IS an involution, and computed here on the
    adjoint by conjugation, entry (i,j) -> sgn_i sgn_j (i,j):

        dim k = 46  (= so(10) + u(1) = 45 + 1)      dim p = 32      46 + 32 = 78
        SIGNATURE = 32 - 46 = -14

    and E6(-14) IS BY DEFINITION the real form of signature -14.  So the object's own D2
    SELECTS E6(-14) uniquely among the five real forms.  The charge branch is DERIVED.

(2) AND THE FORK IS A RANK OBSTRUCTION.  D2 is conjugation by a torus element (a sign
    character on the weights), hence INNER -- and inner involutions reach only the EQUAL-RANK
    real forms (rank k = rank e6 = 6):

        E6(-78) compact  k = e6            rank 6   INNER
        E6(-14)          k = so(10)+u(1)   rank 6   INNER   <- where D2 lands
        E6(2)            k = su(6)+su(2)   rank 6   INNER
        E6(-26)          k = f4            rank 4   OUTER
        E6(6) split      k = sp(4)         rank 4   OUTER

    E6(-26) -- the branch that took LORENTZ, COMPACT COLOUR and the GRAVITON -- has k = f4 of
    RANK 4.  NO torus element of E6 can reach it.  So B1140's "nothing shared" is not a
    coincidence of two campaigns: it is that one branch is INNER and the other is OUTER, and
    no inner map reaches an outer form.

(3) WHAT WOULD CROSS IT, NAMED EXACTLY.  Only an OUTER involution, i.e. one using E6's
    diagram automorphism -- which is precisely THETA, the 27 <-> 27bar swap the corpus banks
    as the object's own symmetry.  So JOIN 3's blocker is not "find a bridge" but "does the
    object's theta act as an outer involution here, and with which fixed subalgebra".

FENCED, and this is where the arc stops.  That theta IS E6's outer automorphism is standard
(the E6 diagram's Z/2 exchanges the two 27s).  That the OBJECT's theta is that automorphism,
and that it can serve as the required Cartan involution, is NOT established here -- and the
corpus's own theta facts cut both ways: the object is theta-symmetric, but "theta is trivial
on the character variety" (it fixes every SL(2) trace), which is a reason to doubt it carries
geometric content.  NOTHING here earns I-10 or I-11; the price stays at 14.  What changes is
that JOIN 3's blocker is now a NAMED rank obstruction with a NAMED unique candidate crossing.

CONTROLS (MB12, both directions):
  - the eigenspace split is COMPUTED from the object's 78 generators, not read off B1250 --
    and every generator is asserted D2-homogeneous, which would fail loudly if D2 were not
    an involution acting diagonally on the root spaces;
  - dim k + dim p = 78 is checked;
  - the signature test can come out otherwise: all five real forms are tabulated with their
    signatures, and -14 selects exactly one row;
  - the inner/outer split is decided by rank(k) vs rank(e6) = 6, tabulated for all five.
"""
import json, os

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
W13 = [1, 0, -1, 0, 1, -1]
FORMS = [("E6(-78) compact", "e6", 78, 6), ("E6(-14)", "so(10)+u(1)", 46, 6),
         ("E6(2)", "su(6)+su(2)", 38, 6), ("E6(-26)", "f4", 52, 4),
         ("E6(6) split", "sp(4)", 36, 4)]
RANK_E6 = 6


def load():
    R = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    rep = [[[int(v) for v in row] for row in R["rep"][str(k)]] for k in range(78)]
    WT = [tuple(rep[i][a][a] for i in range(6)) for a in range(27)]
    sgn = [(-1) ** (sum(a * b for a, b in zip(W13, WT[t])) + 1) for t in range(27)]
    return rep, sgn


def d2_signature():
    rep, sgn = load()
    plus = minus = 0
    for k in range(78):
        X = rep[k]
        signs = {sgn[i] * sgn[j] for i in range(27) for j in range(27) if X[i][j]}
        assert len(signs) == 1, f"generator {k} not D2-homogeneous: {signs}"
        if signs == {1}:
            plus += 1
        else:
            minus += 1
    return plus, minus


def selftest():
    print("B1265 -- the real form is derived; the fork is inner vs outer (selftest)")
    k, p = d2_signature()
    print(f"  [D2  ] on the adjoint: dim k = {k}, dim p = {p}, total {k+p}")
    assert k + p == 78 and (k, p) == (46, 32)
    sig = p - k
    print(f"  [sig ] signature = {p} - {k} = {sig}")

    match = [f for f in FORMS if 78 - 2 * f[2] == sig]
    print(f"  [form] real forms with signature {sig}: {[f[0] for f in match]}")
    assert len(match) == 1 and match[0][0] == "E6(-14)"
    print(f"         => the object's own D2 SELECTS {match[0][0]}, k = {match[0][1]} -- DERIVED")

    print(f"  [ctl ] all five real forms, signature and rank(k) (rank e6 = {RANK_E6}):")
    for nm, kk, dk, rk in FORMS:
        print(f"           {nm:16} k = {kk:14} dim {dk:2}  sig {78-2*dk:4}  rank {rk}"
              f"  {'INNER' if rk == RANK_E6 else 'OUTER'}")
    inner = [f[0] for f in FORMS if f[3] == RANK_E6]
    outer = [f[0] for f in FORMS if f[3] != RANK_E6]
    assert "E6(-14)" in inner and "E6(-26)" in outer

    print(f"  [KILL] D2 is conjugation by a torus element => INNER => reaches only {inner}")
    print(f"         E6(-26) (k = f4, rank 4) is OUTER: NO torus element reaches it.")
    print("         That is why B1140's two branches share nothing -- a RANK obstruction.")
    print("  [next] only an OUTER involution crosses it, i.e. E6's diagram automorphism = theta.")
    print("         FENCED: that the OBJECT's theta is that automorphism, and can serve as the")
    print("         Cartan involution, is NOT established here. Price unchanged at 14.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
