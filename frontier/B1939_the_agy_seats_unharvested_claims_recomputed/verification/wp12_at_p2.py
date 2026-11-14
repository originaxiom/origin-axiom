#!/usr/bin/env python3
"""WP-1.2 at p = 2: own-code verification of agy-002's second derivation (claims 1-5 of the task).

Exact arithmetic only: free-group words as tuples of ints, Gaussian integers as pairs of ints, integer matrices,
sympy for the symbolic family and the intertwiner nullspaces. No repository code imported or run.
Definitions: see EXPECTATIONS.md (sources docs/seats/agy-002.md:296-302, TERMINOLOGY.md:980, GENESIS.md:147).
"""
import itertools, json, sys
from collections import Counter

RESULTS = {}
CHECKS = []          # (name, passed, detail)
PLANTS = []          # (name, check_failed_as_required, detail)


def check(name, passed, detail=""):
    CHECKS.append((name, bool(passed), detail))
    print(("PASS " if passed else "FAIL ") + name + (": " + str(detail) if detail != "" else ""))
    return bool(passed)


def plant(name, check_passed_on_plant, detail=""):
    caught = not check_passed_on_plant
    PLANTS.append((name, caught, detail))
    print(("PLANT CAUGHT " if caught else "PLANT MISSED ") + name + (": " + str(detail) if detail != "" else ""))
    return caught


# ----------------------------------------------------------------------------------------------------------------
# Free group F2: letters a=1, a^-1=-1, b=2, b^-1=-2
# ----------------------------------------------------------------------------------------------------------------
LET = (1, -1, 2, -2)
NAME = {1: "a", -1: "A", 2: "b", -2: "B"}


def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inv(w):
    return tuple(-x for x in reversed(w))


def mul(*ws):
    return red(tuple(itertools.chain(*ws)))


def s(w):
    return "".join(NAME[x] for x in w) if w else "1"


def reduced_words(maxlen):
    """All reduced words of length 0..maxlen, by DFS (yields word tuples)."""
    stack = [()]
    while stack:
        w = stack.pop()
        yield w
        if len(w) < maxlen:
            for x in LET:
                if not w or w[-1] != -x:
                    stack.append(w + (x,))


def cyc_red(w):
    w = red(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    return w


def canon(w):
    """Canonical representative of the conjugacy class: min over rotations of the cyclic reduction."""
    c = cyc_red(w)
    if not c:
        return ()
    return min(c[i:] + c[:i] for i in range(len(c)))


a, A, b, B = (1,), (-1,), (2,), (-2,)
COMM = mul(a, b, A, B)                       # [a, b] = a b a^-1 b^-1


def make_move(img_a, img_b):
    ia, ib = red(img_a), red(img_b)
    table = {1: ia, -1: inv(ia), 2: ib, -2: inv(ib)}

    def phi(w):
        return red(tuple(itertools.chain(*(table[x] for x in w))))
    phi.images = (ia, ib)
    return phi


MOVES = {
    "R1 a->ab": make_move(mul(a, b), b),
    "R2 a->ba": make_move(mul(b, a), b),
    "R3 b->ba": make_move(a, mul(b, a)),
    "R4 b->ab": make_move(a, mul(a, b)),
    "S swap (a,b)->(b,a)": make_move(b, a),
    "T tick (a,b)->(ab,a)": make_move(mul(a, b), a),
}
RECORD = [k for k in MOVES if k[0] == "R"]


def is_conj(u, v):
    return canon(u) == canon(v)


# ----------------------------------------------------------------------------------------------------------------
# Section B (claim 1)
# ----------------------------------------------------------------------------------------------------------------
def section_B(conj_test=is_conj, record=None, record_moves=None):
    """Return the sorted list of classes (canonical reps) of length <= 8 kept by every move in record_moves."""
    record_moves = record_moves if record_moves is not None else [MOVES[k] for k in RECORD]
    classes = set()
    for w in reduced_words(8):
        classes.add(canon(w))
    kept = sorted((c for c in classes if all(conj_test(phi(c), c) for phi in record_moves)), key=lambda c: (len(c), c))
    if record is not None:
        record["n_classes_len_le_8"] = len(classes)
    return kept, classes


def literal_equal(u, v):          # PLANTED wrong conjugacy test: word equality after reduction
    return red(u) == red(v)


def run_B():
    out = {}
    nwords = sum(1 for _ in reduced_words(8))
    check("B: number of reduced words of length <= 8 is 1 + 2(3^8 - 1) = 13121", nwords == 13121 == 1 + 2 * (3 ** 8 - 1), nwords)
    out["n_reduced_words_le_8"] = nwords
    # sentence 1 and 2
    check("B1: [a,b] is trivial in Z^2 (exponent sums 0,0)",
          (sum(1 if x == 1 else -1 if x == -1 else 0 for x in COMM), sum(1 if x == 2 else -1 if x == -2 else 0 for x in COMM)) == (0, 0))
    for k in RECORD:
        check(f"B2: {k} sends [a,b] to a conjugate of itself", is_conj(MOVES[k](COMM), COMM), s(MOVES[k](COMM)))
    for k in ("S swap (a,b)->(b,a)", "T tick (a,b)->(ab,a)"):
        check(f"B2: {k} sends [a,b] to a conjugate of its inverse", is_conj(MOVES[k](COMM), inv(COMM)), s(MOVES[k](COMM)))
    check("B2: [a,b]^-1 is not conjugate to [a,b]", not is_conj(inv(COMM), COMM))
    # sentence 3, reading (i): classes whose shortest member has length <= 8
    kept, classes = section_B(record=out)
    out["kept_classes_including_empty"] = [s(c) for c in kept]
    out["kept_classes_nonempty"] = [s(c) for c in kept if c]
    c2 = mul(COMM, COMM)
    expected = sorted([(), canon(COMM), canon(inv(COMM)), canon(c2), canon(inv(c2))], key=lambda c: (len(c), c))
    check("B3 (literal, empty word included): exactly five classes kept: 1, [a,b], [a,b]^-1, [a,b]^2, [a,b]^-2",
          kept == expected, [s(c) for c in kept])
    check("B3 (non-empty): exactly four classes kept, [a,b]^{+-1}, [a,b]^{+-2}",
          [c for c in kept if c] == [c for c in expected if c])
    # reading (ii): the classes of words, not of shortest members (same classes by construction; count them)
    cr = set(canon(w) for w in reduced_words(8) if cyc_red(w) == w)
    check("B3: the classes of cyclically reduced words <= 8 are the classes of all reduced words <= 8", cr == classes, len(cr))
    # set-wise reading: the largest set of classes of length <= 8 carried into itself by the four moves
    S = set(classes)
    changed = True
    while changed:
        changed = False
        for c in list(S):
            if any(canon(MOVES[k](c)) not in S for k in RECORD):
                S.discard(c)
                changed = True
    check("B3 (set-wise reading): the largest invariant set of classes <= 8 is the same five", sorted(S, key=lambda c: (len(c), c)) == expected,
          [s(c) for c in sorted(S, key=lambda c: (len(c), c))])
    # the escape of a class: b^n [a,b] b^-n lengths under iterating R2
    w, lens = COMM, []
    for _ in range(5):
        lens.append(len(w)); w = MOVES["R2 a->ba"](w)
    out["R2_iterates_of_[a,b]_word_lengths"] = lens
    check("B (looseness): iterating a->ba on the word [a,b] gives words of length 4,6,8,10,12 (the class is not a set of short words)",
          lens == [4, 6, 8, 10, 12], lens)
    # controls on the filter's liveness: under {R1, R2} only, how many classes kept
    kept12, _ = section_B(record_moves=[MOVES["R1 a->ab"], MOVES["R2 a->ba"]])
    out["kept_under_R1_R2_only"] = len(kept12)
    # PLANT PC-1: literal word equality as the conjugacy test
    keptP, _ = section_B(conj_test=literal_equal)
    plant("PC-1: literal word equality in place of conjugacy; check 'five classes kept' must fail",
          keptP == expected, [s(c) for c in keptP])
    # PLANT PC-1b: the swap counted among the record moves
    keptS, _ = section_B(record_moves=[MOVES[k] for k in RECORD] + [MOVES["S swap (a,b)->(b,a)"]])
    plant("PC-1b: swap added to the record moves; check 'five classes kept' must fail", keptS == expected, [s(c) for c in keptS])
    RESULTS["B"] = out


# ----------------------------------------------------------------------------------------------------------------
# Exact matrix arithmetic
# ----------------------------------------------------------------------------------------------------------------
# Gaussian integers as (re, im)
def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mmul(M, N, mult, add, zero):
    n = len(M)
    return tuple(tuple(
        (lambda acc: acc)(
            __import__("functools").reduce(add, (mult(M[i][k], N[k][j]) for k in range(n)), zero))
        for j in range(n)) for i in range(n))


def gm(M, N):
    return mmul(M, N, gmul, gadd, (0, 0))


def im(M, N):
    return mmul(M, N, lambda x, y: x * y, lambda x, y: x + y, 0)


G0, G1, GI, GmI, Gm1 = (0, 0), (1, 0), (0, 1), (0, -1), (-1, 0)
GID = ((G1, G0), (G0, G1))


class Rep:
    """A representation of F2 by exact matrices: generators and inverses, a multiplication, an identity."""

    def __init__(self, name, ga, gA, gb, gB, mult, ident):
        self.name, self.mult, self.I = name, mult, ident
        self.gen = {1: ga, -1: gA, 2: gb, -2: gB}
        assert mult(ga, gA) == ident and mult(gA, ga) == ident, name
        assert mult(gb, gB) == ident and mult(gB, gb) == ident, name

    def ev(self, w):
        M = self.I
        for x in w:
            M = self.mult(M, self.gen[x])
        return M


# the quaternion point over Z[i]: a = diag(i, -i), b = [[0, 1], [-1, 0]]
Q_a = ((GI, G0), (G0, GmI)); Q_A = ((GmI, G0), (G0, GI))
Q_b = ((G0, G1), (Gm1, G0)); Q_B = ((G0, Gm1), (G1, G0))
QUAT = Rep("quaternion point over Z[i]", Q_a, Q_A, Q_b, Q_B, gm, GID)

# the same point as abstract quaternion units (sign, unit); a -> i, b -> j
_QT = {("1", "1"): (1, "1"), ("1", "i"): (1, "i"), ("1", "j"): (1, "j"), ("1", "k"): (1, "k"),
       ("i", "1"): (1, "i"), ("i", "i"): (-1, "1"), ("i", "j"): (1, "k"), ("i", "k"): (-1, "j"),
       ("j", "1"): (1, "j"), ("j", "i"): (-1, "k"), ("j", "j"): (-1, "1"), ("j", "k"): (1, "i"),
       ("k", "1"): (1, "k"), ("k", "i"): (1, "j"), ("k", "j"): (-1, "i"), ("k", "k"): (-1, "1")}


def qmul(x, y):
    sg, u = _QT[(x[1], y[1])]
    return (x[0] * y[0] * sg, u)


Q8U = Rep("Q8 as quaternion units", (1, "i"), (-1, "i"), (1, "j"), (-1, "j"), qmul, (1, "1"))

# integral Heisenberg: a = I + E12, b = I + E23
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
H_a = ((1, 1, 0), (0, 1, 0), (0, 0, 1)); H_A = ((1, -1, 0), (0, 1, 0), (0, 0, 1))
H_b = ((1, 0, 0), (0, 1, 1), (0, 0, 1)); H_B = ((1, 0, 0), (0, 1, -1), (0, 0, 1))
HEIS = Rep("integral Heisenberg H3(Z)", H_a, H_A, H_b, H_B, im, I3)

# Sanov pair
I2 = ((1, 0), (0, 1))
SAN = Rep("Sanov pair", ((1, 2), (0, 1)), ((1, -2), (0, 1)), ((1, 0), (2, 1)), ((1, 0), (-2, 1)), im, I2)
# PLANT for PC-2: L, R (not free)
LR = Rep("L, R (planted, not free)", ((1, 1), (0, 1)), ((1, -1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (-1, 1)), im, I2)

# abelianisation Z^2 as a "representation" (PLANT for PC-5a): vectors added
AB = Rep("abelianisation Z^2 (planted as 'Heisenberg')", (1, 0), (-1, 0), (0, 1), (0, -1),
         lambda x, y: (x[0] + y[0], x[1] + y[1]), (0, 0))


def trivial_by_length(rep, maxlen):
    """Count trivial reduced words by length, DFS with prefix products. Returns Counter and list of trivial words."""
    cnt, triv = Counter(), []
    stack = [((), rep.I)]
    while stack:
        w, M = stack.pop()
        if M == rep.I:
            cnt[len(w)] += 1
            triv.append(w)
        if len(w) < maxlen:
            for x in LET:
                if not w or w[-1] != -x:
                    stack.append((w + (x,), rep.mult(M, rep.gen[x])))
    return cnt, triv


def gtr(M):
    return gadd(M[0][0], M[1][1])


def run_C():
    out = {}
    # first point
    ab = gm(Q_a, Q_b)
    check("C: tr a = tr b = tr ab = 0 at the quaternion point", gtr(Q_a) == G0 and gtr(Q_b) == G0 and gtr(ab) == G0)
    cq = QUAT.ev(COMM)
    check("C: [a,b] = -I at the quaternion point", cq == ((Gm1, G0), (G0, Gm1)))
    for g in (a, b, A, B):
        check(f"C: [[a,b], {s(g)}] = I at the quaternion point", QUAT.ev(mul(COMM, g, inv(COMM), inv(g))) == GID)
    # Heisenberg
    check("C: [a,b] != I in H3(Z)", HEIS.ev(COMM) != I3, HEIS.ev(COMM))
    for g in (a, b, A, B):
        check(f"C: [[a,b], {s(g)}] = I in H3(Z)", HEIS.ev(mul(COMM, g, inv(COMM), inv(g))) == I3)
    # Sanov
    tc = SAN.ev(mul(COMM, a, inv(COMM), A))
    out["sanov_[[a,b],a]"] = tc
    check("C: [[a,b], a] != I at the Sanov pair", tc != I2, tc)
    cntS, trivS = trivial_by_length(SAN, 8)
    out["sanov_trivial_by_length_le_8"] = dict(sorted(cntS.items()))
    check("C last clause, LITERAL: 'no reduced word of length <= 8 is trivial' at the Sanov pair",
          sum(cntS.values()) == 0, dict(cntS))
    check("C last clause, with NON-EMPTY: no non-empty reduced word of length <= 8 is trivial at the Sanov pair",
          sum(v for k, v in cntS.items() if k > 0) == 0, dict(cntS))
    check("C: the empty word is the only trivial reduced word <= 8 at the Sanov pair (it evaluates to I)",
          trivS == [()] and SAN.ev(()) == I2)
    # PLANT PC-2: L, R in place of the Sanov pair
    cntL, trivL = trivial_by_length(LR, 8)
    out["LR_plant_trivial_by_length_le_8"] = dict(sorted(cntL.items()))
    plant("PC-2: L, R in place of the Sanov pair; check 'no non-empty word <= 8 trivial' must fail",
          sum(v for k, v in cntL.items() if k > 0) == 0, {"counts": dict(sorted(cntL.items())), "shortest": s(min((w for w in trivL if w), key=len))})
    RESULTS["C"] = out


def run_5():
    """Claim (5): Heisenberg-trivial words of length <= 8 (and to 10) are trivial at the quaternion point."""
    out = {}
    cntH, trivH = trivial_by_length(HEIS, 10)
    out["H3_trivial_by_length_le_10"] = dict(sorted(cntH.items()))
    trivH8 = [w for w in trivH if len(w) <= 8]
    check("5: H3(Z)-trivial reduced words of length <= 8: the empty word and exactly 64 of length 8, none of length 1..7",
          Counter(len(w) for w in trivH8) == Counter({0: 1, 8: 64}), dict(Counter(len(w) for w in trivH8)))
    bad = [w for w in trivH8 if QUAT.ev(w) != GID]
    check("5: every one of the 65 H3-trivial words of length <= 8 is I at the quaternion point (2x2 over Z[i])", not bad, len(bad))
    bad2 = [w for w in trivH8 if Q8U.ev(w) != (1, "1")]
    check("5: the same by quaternion units (independent evaluation)", not bad2, len(bad2))
    badall = [w for w in trivH if QUAT.ev(w) != GID]
    check("5: extended to length 10: every H3-trivial word of length <= 10 is I at the quaternion point", not badall,
          {"n_H3_trivial_le_10": len(trivH), "bad": len(badall)})
    # each of the 64 lies in gamma_3: its image in H3 is I (by construction) and it is a product of triple commutators?
    # (structural: H3(Z) = F2/gamma_3(F2); not recomputed here). Show the 64 are 16 classes? record their canonical classes.
    nonempty8 = [w for w in trivH8 if w]
    out["H3_trivial_len8_examples"] = [s(w) for w in sorted(nonempty8)[:6]]
    out["H3_trivial_len8_n_conjugacy_classes"] = len(set(canon(w) for w in nonempty8))
    # Q8 trivial words by length, two evaluations agreeing word by word
    cntQ, trivQ = trivial_by_length(QUAT, 8)
    cntU, trivU = trivial_by_length(Q8U, 8)
    out["quaternion_point_trivial_by_length_le_8"] = dict(sorted(cntQ.items()))
    check("5: the two evaluations of the quaternion point agree on every trivial word <= 8", sorted(trivQ) == sorted(trivU),
          {"Z[i]": sum(cntQ.values()), "units": sum(cntU.values())})
    check("5: the converse fails: some words trivial at the quaternion point are not trivial in H3 (e.g. a^4)",
          QUAT.ev(a * 4) == GID and HEIS.ev(a * 4) != I3)
    # PLANT PC-5a: abelianisation in place of H3
    cntAb, trivAb = trivial_by_length(AB, 8)
    badAb = [w for w in trivAb if QUAT.ev(w) != GID]
    plant("PC-5a: Z^2 in place of H3(Z); check 'every word trivial there is trivial at Q8' must fail", not badAb,
          {"n_trivial_in_Z2": len(trivAb), "not_trivial_at_Q8": len(badAb), "first": s(min(badAb, key=len)) if badAb else None})
    # PLANT PC-5b: Sanov in place of the quaternion point
    badS = [w for w in trivH8 if SAN.ev(w) != I2]
    plant("PC-5b: the Sanov pair in place of the quaternion point; check must fail", not badS, {"not_trivial_at_Sanov": len(badS)})
    RESULTS["5"] = out


# ----------------------------------------------------------------------------------------------------------------
# Section D (claim 3)
# ----------------------------------------------------------------------------------------------------------------
def run_D():
    out = {}
    census = []
    for g in range(0, 4):
        for r in range(1, 6):
            if 2 - 2 * g - r == -1:
                census.append(("orientable", g, r))
    for c in range(1, 5):
        for r in range(1, 6):
            if 2 - c - r == -1:
                census.append(("non-orientable", c, r))
    out["census_chi_-1_connected"] = census
    check("D: connected compact surfaces with non-empty boundary and chi = -1 (pi1 free of rank 2): four",
          sorted(census) == sorted([("orientable", 1, 1), ("orientable", 0, 3), ("non-orientable", 1, 2), ("non-orientable", 2, 1)]), census)

    def ab(w):
        return (sum({1: 1, -1: -1}.get(x, 0) for x in w), sum({2: 1, -2: -1}.get(x, 0) for x in w))
    x, y = a, b
    boundaries = {
        "torus, 1 hole (boundary [a,b])": [COMM],
        "sphere, 3 holes (a, b, (ab)^-1)": [a, b, inv(mul(a, b))],
        "projective plane, 2 holes (x^2 d1 d2 = 1; x=a, d1=b, d2=(x^2 d1)^-1)": [b, inv(mul(a, a, b))],
        "Klein bottle, 1 hole (x^2 y^2 d = 1)": [inv(mul(x, x, y, y))],
    }
    nulls = {k: all(ab(w) == (0, 0) for w in v) for k, v in boundaries.items()}
    out["boundary_classes_null_in_H1"] = nulls
    out["boundary_classes"] = {k: [ab(w) for w in v] for k, v in boundaries.items()}
    check("D: every boundary curve null in H1(Z) on the one-holed torus only", [k for k, v in nulls.items() if v] == ["torus, 1 hole (boundary [a,b])"], nulls)
    # presentation-independence: a word's membership in [F2,F2] is kept by every move and by every composite to depth 3
    words = [w for w in reduced_words(5)]
    ok = True
    for seq in itertools.product(list(MOVES), repeat=3):
        for w in words[:400]:
            v = w
            for k in seq:
                v = MOVES[k](v)
            if (ab(v) == (0, 0)) != (ab(w) == (0, 0)):
                ok = False
    check("D (qualifier): membership in the commutator subgroup is kept by every composite of three moves on 400 words", ok)
    # integral orbits vs mod 2
    mats = {k: None for k in MOVES}

    def act(k, v):
        ia, ib = MOVES[k].images
        A_ = ab(ia); B_ = ab(ib)
        return (v[0] * A_[0] + v[1] * B_[0], v[0] * A_[1] + v[1] * B_[1])
    sizes = {}
    for v0 in [(1, 0), (0, 1), (1, 1), (2, -1), (0, 0)]:
        orb, frontier = {v0}, {v0}
        for step in range(8):
            frontier = {act(k, v) for v in frontier for k in MOVES} - orb
            orb |= frontier
        sizes[str(v0)] = len(orb)
    out["integral_orbit_sizes_after_8_steps_all_six_moves"] = sizes
    check("D: non-zero integral classes have growing orbits (> 20 after 8 steps); the zero class is fixed",
          all(v > 20 for k, v in sizes.items() if k != "(0, 0)") and sizes["(0, 0)"] == 1, sizes)
    mod2 = {(1, 0), (0, 1), (1, 1)}
    img = {k: {(act(k, v)[0] % 2, act(k, v)[1] % 2) for v in mod2} for k in MOVES}
    check("D (integral needed): mod 2 the three non-zero classes are a finite set every move carries to itself",
          all(img[k] == mod2 for k in MOVES))
    RESULTS["D"] = out


# ----------------------------------------------------------------------------------------------------------------
# Claim (4): the prime 2, linear vs projective
# ----------------------------------------------------------------------------------------------------------------
import sympy as sp

X = sp.Matrix([[0, 1], [1, 0]])
Zc = sp.Matrix([[1, 0], [0, -1]])
QA = sp.Matrix([[sp.I, 0], [0, -sp.I]])
QB = sp.Matrix([[0, 1], [-1, 0]])


def ev_sym(pair, w):
    Ma, Mb = pair
    gen = {1: Ma, -1: Ma.inv(), 2: Mb, -2: Mb.inv()}
    M = sp.eye(Ma.shape[0])
    for x in w:
        M = M * gen[x]
    return sp.simplify(M)


def pulled(pair, k):
    ia, ib = MOVES[k].images
    return (ev_sym(pair, ia), ev_sym(pair, ib))


def intertwiners(src, dst):
    """Space of g with g src(x) = dst(x) g for x = a, b. Returns nullspace basis (list of matrices)."""
    n = src[0].shape[0]
    gs = sp.symbols(f"g0:{n*n}")
    G = sp.Matrix(n, n, gs)
    eqs = []
    for S_, D_ in zip(src, dst):
        eqs += list(G * S_ - D_ * G)
    Mx, _ = sp.linear_eq_to_matrix(eqs, gs)
    ns = Mx.nullspace()
    return [sp.Matrix(n, n, list(v)) for v in ns]


def linearly_carried(pair, k):
    """True iff rho∘phi_k ≅ rho (an invertible intertwiner from rho to rho∘phi exists)."""
    basis = intertwiners(pair, pulled(pair, k))
    if not basis:
        return False, None
    if len(basis) == 1:
        g = basis[0]
        return (sp.simplify(g.det()) != 0), g
    # generic combination
    ts = sp.symbols(f"t0:{len(basis)}")
    g = sum((t * m for t, m in zip(ts, basis)), sp.zeros(*basis[0].shape))
    return (sp.simplify(g.det()) != 0), g


def projectively_carried(pair, k, scalars):
    """True iff rho∘phi_k ≅ rho ⊗ chi for some chi with chi(a), chi(b) in `scalars`."""
    img = pulled(pair, k)
    for ca in scalars:
        for cb in scalars:
            tw = (img[0] * ca, img[1] * cb)
            basis = intertwiners(pair, tw)
            if basis and any(sp.simplify(m.det()) != 0 for m in basis):
                return True, (ca, cb)
    return False, None


def run_4():
    out = {}
    CS = (X, Zc)
    one = sp.eye(2)
    check("4: clock-and-shift at p=2: [a,b] = -I", ev_sym(CS, COMM) == -one)
    check("4: clock-and-shift: a^2 = I, b^2 = I, (ab)^2 = -I",
          ev_sym(CS, a * 2) == one and ev_sym(CS, b * 2) == one and ev_sym(CS, mul(a, b, a, b)) == -one)
    lin = {}
    for k in MOVES:
        ok, g = linearly_carried(CS, k)
        img = pulled(CS, k)
        lin[k] = {"carried": bool(ok), "intertwiner": str(g.tolist()) if g is not None else None,
                  "image_a_squared": str((img[0] ** 2).tolist()), "image_b_squared": str((img[1] ** 2).tolist())}
    out["clock_and_shift_linear"] = lin
    check("4: LINEAR: the tick does NOT carry clock-and-shift to itself (image of a is ab, squaring to -I)",
          lin["T tick (a,b)->(ab,a)"]["carried"] is False and ev_sym(CS, mul(a, b, a, b)) == -one)
    check("4: LINEAR: among the six moves only the swap carries clock-and-shift to itself",
          [k for k in MOVES if lin[k]["carried"]] == ["S swap (a,b)->(b,a)"], [k for k in MOVES if lin[k]["carried"]])
    H = sp.Matrix([[1, 1], [1, -1]])
    check("4: the swap's intertwiner can be the Hadamard matrix: H X H^-1 = Z, H Z H^-1 = X",
          H * X * H.inv() == Zc and H * Zc * H.inv() == X)
    # PC-4c two-sided: solver finds the swap (positive) and not the tick (negative) — recorded above; and a plant:
    plant("PC-4a: assert clock-and-shift is linearly carried by all six moves; must fail",
          all(lin[k]["carried"] for k in MOVES), [k for k in MOVES if not lin[k]["carried"]])
    # direct sum with its conjugate (real entries: conjugate = itself)
    CS2 = (sp.diag(X, X), sp.diag(Zc, Zc))
    ok2, _ = linearly_carried(CS2, "T tick (a,b)->(ab,a)")
    check("4: LINEAR: the tick does not carry rho ⊕ conj(rho) = rho ⊕ rho at p=2 either", ok2 is False)
    # projective
    mu4 = [1, sp.I, -1, -sp.I]
    proj = {}
    for k in MOVES:
        ok, chi = projectively_carried(CS, k, mu4)
        proj[k] = {"carried": bool(ok), "twist_chi(a),chi(b)": str(chi)}
    out["clock_and_shift_projective"] = proj
    check("4: PROJECTIVE: every one of the six moves carries clock-and-shift to itself up to a character twist",
          all(proj[k]["carried"] for k in MOVES), {k: proj[k]["twist_chi(a),chi(b)"] for k in MOVES})
    # the quaternion point: carried linearly by all six, explicit intertwiners
    Q = (QA, QB)
    check("4: quaternion point: a^2 = b^2 = (ab)^2 = -I, [a,b] = -I",
          ev_sym(Q, a * 2) == -one and ev_sym(Q, b * 2) == -one and ev_sym(Q, mul(a, b, a, b)) == -one and ev_sym(Q, COMM) == -one)
    qlin = {}
    for k in MOVES:
        ok, g = linearly_carried(Q, k)
        good = False
        if ok:
            img = pulled(Q, k)
            good = sp.simplify(g * QA * g.inv() - img[0]) == sp.zeros(2) and sp.simplify(g * QB * g.inv() - img[1]) == sp.zeros(2)
        qlin[k] = {"carried": bool(ok and good), "intertwiner": str(g.tolist()) if g is not None else None}
    out["quaternion_linear"] = qlin
    check("4: LINEAR: the quaternion point is carried to itself by all six moves (explicit g, g rho g^-1 = rho∘phi verified)",
          all(qlin[k]["carried"] for k in MOVES))
    # the four sign representations
    sign_reps = {}
    for sa, sb in itertools.product([1, -1], repeat=2):
        # normal form with a^2 = sa, b^2 = sb, ab = -ba
        Ma = sp.Matrix([[0, sa], [1, 0]])
        Mb = sp.diag(sp.sqrt(sb), -sp.sqrt(sb))
        sign_reps[(sa, sb)] = (Ma, Mb)
    for key, pr in sign_reps.items():
        assert ev_sym(pr, COMM) == -one and ev_sym(pr, a * 2) == key[0] * one and ev_sym(pr, b * 2) == key[1] * one

    def label(pr):
        return (int(sp.simplify((pr[0] ** 2)[0, 0])), int(sp.simplify((pr[1] ** 2)[0, 0])))
    orbit = {}
    for key, pr in sign_reps.items():
        orbit[str(key)] = {}
        for k in MOVES:
            img = pulled(pr, k)
            orbit[str(key)][k] = str(label(img))
    out["sign_reps_move_table"] = orbit
    fixed = [key for key in sign_reps if all(orbit[str(key)][k] == str(key) for k in MOVES)]
    check("4: of the four sign representations (a^2, b^2) = (+-1, +-1), only (-1,-1) is fixed by all six", fixed == [(-1, -1)], fixed)
    others = {(1, 1), (-1, 1), (1, -1)}
    orb, front = {(1, 1)}, {(1, 1)}
    while front:
        front = {eval(orbit[str(k0)][k]) for k0 in front for k in MOVES} - orb
        orb |= front
    out["orbit_of_clock_and_shift_signs"] = sorted(orb)
    check("4: the other three sign representations are one orbit of the moves (the orbit of clock-and-shift (1,1))",
          orb == others, sorted(orb))
    # is (-1,-1) sign rep the quaternion point (iso)?
    basis = intertwiners(sign_reps[(-1, -1)], Q)
    check("4: the fixed sign representation (-1,-1) is isomorphic to the quaternion point",
          bool(basis) and any(sp.simplify(m.det()) != 0 for m in basis))
    basis = intertwiners(sign_reps[(1, 1)], CS)
    check("4: the sign representation (1,1) is isomorphic to clock-and-shift", bool(basis) and any(sp.simplify(m.det()) != 0 for m in basis))
    # the whole family over C^*: a^2 = alpha, b^2 = beta
    al, sg = sp.symbols("alpha s", nonzero=True)
    fam = (sp.Matrix([[0, al], [1, 0]]), sp.diag(sg, -sg))
    be = sg ** 2
    check("4: family: [a,b] = -I, a^2 = alpha, b^2 = beta = s^2, (ab)^2 = -alpha*beta",
          sp.simplify(ev_sym(fam, COMM) + one) == sp.zeros(2) and sp.simplify(ev_sym(fam, a * 2) - al * one) == sp.zeros(2)
          and sp.simplify(ev_sym(fam, b * 2) - be * one) == sp.zeros(2)
          and sp.simplify(ev_sym(fam, mul(a, b, a, b)) + al * be * one) == sp.zeros(2))
    act = {}
    for k in MOVES:
        img = pulled(fam, k)
        act[k] = (sp.factor(sp.simplify((img[0] ** 2)[0, 0])), sp.factor(sp.simplify((img[1] ** 2)[0, 0])))
    out["family_action_on_(alpha,beta=s^2)"] = {k: str(v) for k, v in act.items()}
    A_, B_ = sp.symbols("A B", nonzero=True)
    eqs = []
    for k in MOVES:
        na, nb = act[k]
        eqs += [sp.Eq(na.subs(sg ** 2, B_).subs(al, A_), A_), sp.Eq(nb.subs(sg ** 2, B_).subs(al, A_), B_)]
    sol = sp.solve(eqs, [A_, B_], dict=True)
    out["family_fixed_points"] = str(sol)
    check("4: over all (alpha, beta) in (C^*)^2 the only point fixed by all six moves is (-1, -1), the quaternion point",
          sol == [{A_: -1, B_: -1}], sol)
    # PC-4b: a mis-written 'quaternion point' with b = [[0,1],[1,0]]
    Qbad = (QA, sp.Matrix([[0, 1], [1, 0]]))
    allfix = all(linearly_carried(Qbad, k)[0] for k in MOVES)
    plant("PC-4b: b = [[0,1],[1,0]] in place of the quaternion b; check 'fixed by all six' must fail", allfix)
    RESULTS["4"] = out


def run_4_odd():
    """Projective clause at odd p: the commutator scalar under the swap and the tick. Exponents mod p (exact)."""
    out = {}
    for p in (2, 3, 5, 7):
        # monomial matrices as (perm, exps): M e_j = zeta^{exps[j]} e_{perm[j]}
        def mono_mul(M, N):
            # (M N) e_j = M (zeta^{N.e[j]} e_{N.p[j]}) = zeta^{N.e[j] + M.e[N.p[j]]} e_{M.p[N.p[j]]}
            return (tuple(M[0][N[0][j]] for j in range(p)), tuple((N[1][j] + M[1][N[0][j]]) % p for j in range(p)))
        ident = (tuple(range(p)), (0,) * p)
        sh = (tuple((j + 1) % p for j in range(p)), (0,) * p)
        shI = (tuple((j - 1) % p for j in range(p)), (0,) * p)
        cl = (tuple(range(p)), tuple(j % p for j in range(p)))
        clI = (tuple(range(p)), tuple((-j) % p for j in range(p)))
        R = Rep(f"clock-shift p={p}", sh, shI, cl, clI, mono_mul, ident)
        c = R.ev(COMM)
        scal = c[1][0] if c[0] == ident[0] and len(set(c[1])) == 1 else None
        res = {"[a,b]_scalar_exponent": scal}
        for k in MOVES:
            ia, ib = MOVES[k].images
            Rk = Rep("pulled", R.ev(ia), R.ev(inv(ia)), R.ev(ib), R.ev(inv(ib)), mono_mul, ident)
            ck = Rk.ev(COMM)
            res[k] = ck[1][0] if ck[0] == ident[0] and len(set(ck[1])) == 1 else None
        out[p] = res
        keep_single = all(res[k] == scal for k in MOVES)
        keep_pair = all(res[k] in (scal, (-scal) % p) for k in MOVES)
        check(f"4 (projective, p={p}): [a,b] scalar zeta^{scal}; single sector kept by all six: {keep_single}; pair kept: {keep_pair}",
              (keep_single == (p == 2)) and keep_pair and scal not in (None, 0))
    RESULTS["4_odd"] = out


if __name__ == "__main__":
    run_B()
    run_C()
    run_5()
    run_D()
    run_4()
    run_4_odd()
    n_fail = sum(1 for c in CHECKS if not c[1])
    n_missed = sum(1 for p in PLANTS if not p[1])
    print(f"\nCHECKS: {len(CHECKS)}, failing: {n_fail}; PLANTS: {len(PLANTS)}, caught: {len(PLANTS) - n_missed}, missed: {n_missed}")
    RESULTS["checks"] = [{"name": n, "passed": p, "detail": str(d)} for n, p, d in CHECKS]
    RESULTS["plants"] = [{"name": n, "caught": c, "detail": str(d)} for n, c, d in PLANTS]
    with open(sys.argv[1] if len(sys.argv) > 1 else "wp12_verify.json", "w") as f:
        json.dump(RESULTS, f, indent=1, default=str)
