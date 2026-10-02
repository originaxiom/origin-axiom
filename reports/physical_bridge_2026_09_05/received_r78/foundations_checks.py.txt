"""B1516 -- GENESIS v1: the foundation facts re-derived with this seat's own code.

python3 foundations_checks.py --record   ->  foundations_checks_run.txt (JSON)

Each check re-derives a banked fact that GENESIS.md rests on, or the one extension it adds. Nothing here is an open
outcome: the statements are theorems (cited) or banked results (cited); the code verifies them independently.

  C1  the records route (docs/UNIQUENESS_THEOREM.md): on the positive 12 x 12 grid all 144 first mixed closures are
      hyperbolic; the torsion-free filter (A5) alone and the minimal-trace filter (A6) alone each leave (1, 1); without
      positivity the torsion-free hyperbolic solutions are (1, 1) and (-1, -1), and B(-1, -1) is SL(2,Z)-conjugate to LR.
  C2  the torsion selector (CLAIMS C3, extended to orientation-reversing monodromy): for every hyperbolic B in GL(2,Z) in
      a box, |tors H1(mapping torus)| = |det(B - I)|, which is |2 - tr B| for det 1 and |tr B| for det -1; the
      torsion-free ones are exactly the classes of LR (det 1) and of the golden matrix G = LP or its inverse (det -1),
      each matched to its normal form by an explicit integer conjugator.
  C3  the order bit (A7): LR and RL are SL(2,Z)-conjugate by L (not by the swap P, whose determinant is -1); their
      based Moebius fixed-point polynomials differ (tau^2 - tau - 1 against tau^2 + tau - 1).
  C4  the word census: signed cyclic words in L and R with both letters, primitive, up to rotation and the L<->R swap,
      lengths 2 to 12 -- per-length counts against main's B1439 (2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 340; 758 in all);
      torsion |2 - eps tr w| at every state; exactly one state is torsion-free (+LR); minimal trace by length.
  C5  SnapPy: the 24 states to length 6 and their census names; word length = number of tetrahedra; every
      non-orientable bundle b-+w / b--w to length 6 and which of them is torsion-free (only the Gieseking manifold).
  C6  the tower (LR)^n: torsion |2 - tr A^n| for n <= 12 and SnapPy names for n <= 6; the Gieseking manifold m000 and its
      orientation double cover m004; G = LP, G^2 = LR; m003 = -LR with torsion 5; the double covers of +LR and -LR coincide.
  C7  m004's fillings: (1,0) has trivial pi1 after simplification (S^3; SnapPy's m004 framing agrees with 4_1's up to
      sign), (0,1) is degenerate with H1 = Z (the Sol torus bundle), (+-5,1) volume 0.98137 with H1 = Z/5 (Meyerhoff).
  C8  each input of the root is needed: without aperiodicity (GM3) the order-6 monodromy (trace 1) and the parabolic
      ones (trace 2, primitive B - I) also give torsion-free H1; without the punctured-torus carrier (GM4) the closed
      torus bundle of LR is torsion-free but Sol (C7's (0,1) filling) and every knot complement in S^3 has H1 = Z
      (SnapPy: 5_2, hyperbolic); without SE2 the Gieseking manifold remains (C5, C6); without SE1 every state remains (C4).
  C9  the unit shears generate every state (GM2): every hyperbolic det-1 matrix in the box is conjugate, by a path of
      L^+-1 and R^+-1 conjugations, to plus or minus a positive word with both letters, and that word's state is in C4's
      census.
  C10 P000's metallic family M_m = [[m,1],[1,0]] = L^m P: (L^m P)^2 = L^m R^m; the torsion of H1 is Z/m for the bundle of
      M_m and (Z/m)^2 for the bundle of its square (B126's fact (A)), so SE1 selects m = 1 in the family; SnapPy b++L^mR^m.
Core convention (UNIQUENESS A4): L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]]; LR = [[2,1],[1,1]].
"""
import itertools
import json
import sys
import time
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECORD = HERE / "foundations_checks_run.txt"

L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))
P = ((0, 1), (1, 0))
I2 = ((1, 0), (0, 1))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def tr(A):
    return A[0][0] + A[1][1]


def neg(A):
    return tuple(tuple(-x for x in row) for row in A)


def inv(A):
    d = det(A)
    assert d in (1, -1)
    return ((A[1][1] * d, -A[0][1] * d), (-A[1][0] * d, A[0][0] * d))


def word(w):
    M = I2
    for c in w:
        M = mul(M, L if c == "L" else R)
    return M


def hyperbolic(B):
    d = det(B)
    if d == 1:
        return abs(tr(B)) > 2
    return tr(B) != 0          # det -1: real eigenvalues; hyperbolic unless the eigenvalues are +-1 (trace 0)


def torsion(B):
    """|tors H1(mapping torus of B on the once-punctured torus)| = |det(B - I)| (H1 = Z + coker(B - I))."""
    return abs(det(((B[0][0] - 1, B[0][1]), (B[1][0], B[1][1] - 1))))


def mobius_fixed_poly(A):
    """tau = (a tau + b)/(c tau + d)  <=>  c tau^2 + (d - a) tau - b = 0; returned as integer coefficients."""
    (a, b), (c, d) = A
    return (c, d - a, -b)


# ---------------------------------------------------------------------------------------------- C1
def check_records_route():
    out = {}
    grid = [(a, b) for a in range(1, 13) for b in range(1, 13)]
    B = {ab: mul(((1, ab[0]), (0, 1)), ((1, 0), (ab[1], 1))) for ab in grid}
    out["positive grid size"] = len(grid)
    out["all hyperbolic"] = all(hyperbolic(m) for m in B.values())
    a5 = [ab for ab in grid if torsion(B[ab]) == 1]
    tmin = min(tr(m) for m in B.values())
    a6 = [ab for ab in grid if tr(B[ab]) == tmin]
    out["A5 alone (torsion-free)"] = a5
    out["A6 alone (minimal trace)"] = a6
    out["A5 and A6 each select (1,1)"] = a5 == [(1, 1)] and a6 == [(1, 1)]
    out["B(1,1) = LR = [[2,1],[1,1]]"] = B[(1, 1)] == ((2, 1), (1, 1)) == mul(L, R)
    signed = [(a, b) for a in range(-12, 13) for b in range(-12, 13) if a != 0 and b != 0]
    Bs = {ab: mul(((1, ab[0]), (0, 1)), ((1, 0), (ab[1], 1))) for ab in signed}
    tf = sorted(ab for ab in signed if hyperbolic(Bs[ab]) and torsion(Bs[ab]) == 1)
    out["without positivity: torsion-free hyperbolic"] = tf
    X = find_conjugator(Bs[(-1, -1)], mul(L, R), det_req=1, bound=6)
    out["B(-1,-1) SL(2,Z)-conjugate to LR"] = X is not None
    out["ab = -1 is elliptic (trace 1)"] = all(tr(Bs[ab]) == 1 for ab in signed if ab[0] * ab[1] == -1)
    out["passed"] = (out["all hyperbolic"] and out["A5 and A6 each select (1,1)"] and out["B(1,1) = LR = [[2,1],[1,1]]"]
                     and tf == [(-1, -1), (1, 1)] and X is not None and out["ab = -1 is elliptic (trace 1)"])
    return out


def find_conjugator(B, target, det_req, bound):
    """X with X B X^-1 = target, det X = det_req (or +-1 if det_req is None), entries in [-bound, bound]."""
    rng = range(-bound, bound + 1)
    for x in itertools.product(rng, repeat=4):
        X = ((x[0], x[1]), (x[2], x[3]))
        d = det(X)
        if d not in (1, -1) or (det_req is not None and d != det_req):
            continue
        if mul(X, B) == mul(target, X):
            return X
    return None


# ---------------------------------------------------------------------------------------------- C2
def check_torsion_selector(box=5, bound=6):
    out = {}
    G = mul(L, P)
    rng = range(-box, box + 1)
    mats = [((a, b), (c, d)) for a, b, c, d in itertools.product(rng, repeat=4) if a * d - b * c in (1, -1)]
    hyp = [B for B in mats if hyperbolic(B)]
    formula_ok = all(torsion(B) == (abs(2 - tr(B)) if det(B) == 1 else abs(tr(B))) for B in hyp)
    tf = [B for B in hyp if torsion(B) == 1]
    inv_set = sorted({(det(B), tr(B)) for B in tf})
    matched, unmatched = 0, []
    for B in tf:
        if det(B) == 1:
            X = find_conjugator(B, mul(L, R), det_req=1, bound=bound)
        else:
            X = find_conjugator(B, G, det_req=None, bound=bound) or find_conjugator(B, inv(G), det_req=None, bound=bound)
        if X is None:
            unmatched.append(B)
        else:
            matched += 1
    out["box"] = f"entries in [-{box}, {box}]"
    out["unimodular matrices"] = len(mats)
    out["hyperbolic"] = len(hyp)
    out["torsion = |2 - tr| (det 1), |tr| (det -1) on every hyperbolic matrix"] = formula_ok
    out["torsion-free hyperbolic matrices"] = len(tf)
    out["their (det, trace)"] = inv_set
    out["each conjugate to LR (det 1) or to G or G^-1 (det -1), conjugator found"] = matched
    out["unmatched"] = [list(map(list, B)) for B in unmatched]
    out["G = LP = [[1,1],[1,0]] and G^2 = LR"] = G == ((1, 1), (1, 0)) and mul(G, G) == mul(L, R)
    out["passed"] = (formula_ok and inv_set == [(-1, -1), (-1, 1), (1, 3)] and not unmatched
                     and out["G = LP = [[1,1],[1,0]] and G^2 = LR"])
    return out


# ---------------------------------------------------------------------------------------------- C3
def check_order_bit():
    LR, RL = mul(L, R), mul(R, L)
    out = {
        "L^-1 (LR) L = RL": mul(mul(inv(L), LR), L) == RL,
        "det L": det(L),
        "P (LR) P = RL": mul(mul(P, LR), P) == RL,
        "det P": det(P),
        "Moebius fixed-point polynomial of LR (c, d-a, -b)": mobius_fixed_poly(LR),
        "Moebius fixed-point polynomial of RL (c, d-a, -b)": mobius_fixed_poly(RL),
    }
    out["passed"] = (out["L^-1 (LR) L = RL"] and out["det L"] == 1 and out["P (LR) P = RL"] and out["det P"] == -1
                     and mobius_fixed_poly(LR) == (1, -1, -1) and mobius_fixed_poly(RL) == (1, 1, -1))
    return out


# ---------------------------------------------------------------------------------------------- C4
MAIN_B1439 = [2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 340]


def canon_state(w):
    """a state up to cyclic rotation and the L<->R swap"""
    sw = w.translate(str.maketrans("LR", "RL"))
    return min(min(x[i:] + x[:i] for i in range(len(x))) for x in (w, sw))


def primitive(w):
    n = len(w)
    return not any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n))


def check_census(maxlen=12):
    states = {}
    for n in range(2, maxlen + 1):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if "L" in w and "R" in w and primitive(w):
                states.setdefault(n, set()).add(canon_state(w))
    per_len = [2 * len(states[n]) for n in range(2, maxlen + 1)]
    rows = []
    for n in range(2, maxlen + 1):
        for w in sorted(states[n]):
            t = tr(word(w))
            for eps in (1, -1):
                rows.append({"state": ("+" if eps == 1 else "-") + w, "length": n, "trace": eps * t,
                             "torsion": abs(2 - eps * t)})
    tf = [r["state"] for r in rows if r["torsion"] == 1]
    min_tr = {n: min(tr(word(w)) for w in states[n]) for n in states}
    out = {"states per length (signed)": per_len, "main B1439": MAIN_B1439, "total": sum(per_len),
           "agrees with main": per_len == MAIN_B1439, "torsion-free states": tf,
           "minimal |trace| by length (positive words)": {str(k): v for k, v in min_tr.items()},
           "minimal trace is length + 1": all(min_tr[n] == n + 1 for n in min_tr)}
    out["passed"] = out["agrees with main"] and tf == ["+LR"] and out["minimal trace is length + 1"]
    return out, rows


# ---------------------------------------------------------------------------------------------- C5, C6, C7 (SnapPy)
def snappy_checks():
    warnings.filterwarnings("ignore")
    try:
        import snappy
    except Exception as exc:                       # the record says so; the lock requires SnapPy only for the slow test
        return {"skipped": f"snappy unavailable: {exc}"}
    out = {"snappy": snappy.__version__}

    def ident(M):
        try:
            return [str(x).replace("(0,0)", "") for x in M.identify()]
        except Exception:
            return []

    # C5: the 24 orientable states to length 6, and every non-orientable bundle to length 6
    names, tet_ok = {}, True
    for n in range(2, 7):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if not ("L" in w and "R" in w and primitive(w)) or canon_state(w) != w:
                continue
            for pre, s in (("b++", "+"), ("b+-", "-")):
                M = snappy.Manifold(pre + w)
                names[s + w] = (ident(M) or ["?"])[0]
                tet_ok &= M.num_tetrahedra() == len(w)
    out["C5 orientable states to length 6"] = len(names)
    out["C5 distinct census names"] = len(set(names.values()))
    out["C5 names"] = names
    out["C5 word length = tetrahedra"] = tet_ok
    nonor = {}
    for n in range(1, 7):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if not primitive(w) or min(w[i:] + w[:i] for i in range(n)) != w:
                continue
            for pre in ("b-+", "b--"):
                M = snappy.Manifold(pre + w)
                h = M.homology()
                tf = all(c == 0 for c in h.elementary_divisors())   # torsion-free iff every divisor is 0 (a Z summand)
                nonor[pre + w] = {"name": (ident(M) or ["?"])[0], "torsion-free": tf,
                                  "orientable": M.is_orientable()}
    tf_names = sorted({v["name"] for v in nonor.values() if v["torsion-free"]})
    out["C5 non-orientable bundles read (to length 6)"] = len(nonor)
    out["C5 all non-orientable"] = not any(v["orientable"] for v in nonor.values())
    out["C5 torsion-free non-orientable bundles"] = tf_names

    # C6: the tower and the relatives
    tower = {}
    for n in range(1, 7):
        M = snappy.Manifold("b++" + "LR" * n)
        tower[n] = {"name": (ident(M) or ["?"])[0], "H1": str(M.homology())}
    A = mul(L, R)
    tors = []
    An = I2
    for n in range(1, 13):
        An = mul(An, A)
        tors.append(torsion(An))
    G0 = snappy.Manifold("m000")
    cov = G0.orientation_cover()
    out["C6 tower names (n = 1..6)"] = tower
    out["C6 tower torsion |2 - tr A^n| (n = 1..12)"] = tors
    out["C6 m000 orientable"] = G0.is_orientable()
    out["C6 m000 volume"] = round(float(G0.volume()), 6)
    out["C6 m000 H1"] = str(G0.homology())
    out["C6 orientation cover of m000"] = (ident(cov) or ["?"])[0]
    out["C6 m003 = -LR, H1"] = str(snappy.Manifold("b+-LR").homology())
    out["C6 (+LR)^2 and (-LR)^2 bundles"] = [(ident(snappy.Manifold("b++LRLR")) or ["?"])[0],
                                             "same matrix: (-A)^2 = A^2"]

    # C7: fillings of m004
    fill = {}
    for s in ((1, 0), (0, 1), (5, 1), (-5, 1)):
        M = snappy.Manifold("m004")
        M.dehn_fill(s)
        fill[str(s)] = {"solution": M.solution_type(), "volume": round(float(M.volume()), 6), "H1": str(M.homology()),
                        "pi1 generators after simplification": M.fundamental_group().num_generators()}
    out["C7 fillings of m004"] = fill

    # C8: a knot complement outside the carrier; C10: the metallic squares
    K = snappy.Manifold("5_2")
    out["C8 5_2: H1, solution, volume"] = [str(K.homology()), K.solution_type(), round(float(K.volume()), 6)]
    out["C10 b++L^mR^m: H1 (m = 1..5)"] = {str(m): str(snappy.Manifold("b++" + "L" * m + "R" * m).homology())
                                         for m in range(1, 6)}
    out["passed"] = (len(names) == 24 and len(set(names.values())) == 24 and tet_ok and out["C5 all non-orientable"]
                     and tf_names == ["m000"]
                     and [tower[n]["name"] for n in range(1, 7)] == ["m004", "m206", "s961", "t12839", "o10_150696", "otet12_00013"]
                     and tors[:6] == [1, 5, 16, 45, 121, 320]
                     and not out["C6 m000 orientable"] and out["C6 orientation cover of m000"] == "m004"
                     and fill["(1, 0)"]["H1"] == "0" and fill["(1, 0)"]["pi1 generators after simplification"] == 0
                     and fill["(0, 1)"]["H1"] == "Z" and fill["(5, 1)"]["H1"] == fill["(-5, 1)"]["H1"] == "Z/5"
                     and abs(fill["(5, 1)"]["volume"] - 0.981369) < 1e-5 and abs(fill["(-5, 1)"]["volume"] - 0.981369) < 1e-5
                     and out["C8 5_2: H1, solution, volume"][0] == "Z"
                     and out["C8 5_2: H1, solution, volume"][1] == "all tetrahedra positively oriented"
                     and out["C10 b++L^mR^m: H1 (m = 1..5)"] == {"1": "Z", "2": "Z/2 + Z/2 + Z", "3": "Z/3 + Z/3 + Z",
                                                                 "4": "Z/4 + Z/4 + Z", "5": "Z/5 + Z/5 + Z"})
    return out


# ---------------------------------------------------------------------------------------------- C8, C9, C10 (integer)
def coker_minus_identity(B):
    """the cokernel of B - I as (free rank, torsion invariants), by the Smith normal form of a 2 x 2 integer matrix"""
    from math import gcd
    M = ((B[0][0] - 1, B[0][1]), (B[1][0], B[1][1] - 1))
    d1 = gcd(gcd(abs(M[0][0]), abs(M[0][1])), gcd(abs(M[1][0]), abs(M[1][1])))
    D = abs(det(M))
    if d1 == 0:
        return 2, []
    if D == 0:
        return 1, [d1] if d1 > 1 else []
    return 0, [x for x in (d1, D // d1) if x > 1]


def check_necessity(box=4):
    out = {}
    rng = range(-box, box + 1)
    mats = [((a, b), (c, d)) for a, b, c, d in itertools.product(rng, repeat=4) if a * d - b * c == 1]
    nonhyp_tf = {}
    for B in mats:
        if abs(tr(B)) > 2:
            continue
        rank, tors = coker_minus_identity(B)
        if not tors:
            nonhyp_tf.setdefault(tr(B), 0)
            nonhyp_tf[tr(B)] += 1
    order6 = ((1, -1), (1, 0))
    o6 = I2
    order = None
    for k in range(1, 13):
        o6 = mul(o6, order6)
        if o6 == I2:
            order = k
            break
    out["without GM3: non-hyperbolic det-1 matrices with torsion-free H1, by trace"] = {str(k): v for k, v in sorted(nonhyp_tf.items())}
    out["the trace-1 monodromy [[1,-1],[1,0]]: order, H1 of its mapping torus"] = [order, "Z" if coker_minus_identity(order6) == (0, []) else "?"]
    out["the parabolic L: H1 of its mapping torus"] = "Z + Z" if coker_minus_identity(L) == (1, []) else "?"
    out["the closed torus bundle of LR: coker(LR - I)"] = coker_minus_identity(mul(L, R))
    passed = (set(nonhyp_tf) == {1, 2} and order == 6 and coker_minus_identity(L) == (1, [])
              and coker_minus_identity(mul(L, R)) == (0, []))
    out["passed"] = passed
    return out


def to_positive_word(B, max_nodes=50000, max_entry=400):
    """plus or minus a positive word in L and R conjugate to the hyperbolic det-1 matrix B (BFS over conjugations)"""
    from collections import deque
    eps = 1 if tr(B) > 0 else -1
    B0 = B if eps == 1 else neg(B)
    gens = [L, inv(L), R, inv(R)]
    seen = {B0}
    q = deque([B0])
    while q and len(seen) < max_nodes:
        M = q.popleft()
        if all(x >= 0 for row in M for x in row):
            M0, w = M, []
            while M != I2:
                (a, b), (c, d) = M
                if a >= c and b >= d:
                    w.append("L"); M = ((a - c, b - d), (c, d))
                elif c >= a and d >= b:
                    w.append("R"); M = ((a, b), (c - a, d - b))
                else:
                    return None
            assert word("".join(w)) == M0                       # the factorisation reproduces the conjugate
            return eps, "".join(w)
        for X in gens:
            N = mul(mul(X, M), inv(X))
            if N not in seen and max(abs(x) for row in N for x in row) <= max_entry:
                seen.add(N)
                q.append(N)
    return None


def check_generation(census_rows, box=5):
    rng = range(-box, box + 1)
    mats = [((a, b), (c, d)) for a, b, c, d in itertools.product(rng, repeat=4)
            if a * d - b * c == 1 and abs(a + d) > 2]
    states = {r["state"] for r in census_rows}
    found, missing, failed = 0, [], []
    for B in mats:
        res = to_positive_word(B)
        if res is None:
            failed.append(B)
            continue
        eps, w = res
        target = word(w) if eps == 1 else neg(word(w))
        ok_word = ("L" in w and "R" in w and tr(target) == tr(B)
                   and find_conjugator(B, target, det_req=1, bound=7) is not None)   # an explicit SL(2,Z) conjugator
        root = w
        for d in range(1, len(w) + 1):              # the primitive root of w (a power w = u^k is the state u's level k)
            if len(w) % d == 0 and w == w[:d] * (len(w) // d):
                root = w[:d]
                break
        k = len(w) // len(root)
        st = ("+" if eps ** 1 == 1 else "-") + canon_state(root)
        # the state of B is (eps, root) at level k; level-1 words must be census states
        if k == 1 and st not in states:
            missing.append((B, eps, w))
        elif ok_word:
            found += 1
    out = {"box": f"entries in [-{box}, {box}]", "hyperbolic det-1 matrices": len(mats),
           "reduced to +-(positive word with both letters), explicit SL(2,Z) conjugator found": found,
           "not reduced": len(failed),
           "level-1 words missing from the census": len(missing)}
    out["passed"] = not failed and not missing and found == len(mats)
    return out


def check_metallic(mmax=6):
    rows = {}
    ok = True
    for m in range(1, mmax + 1):
        Lm = ((1, m), (0, 1))
        Rm = ((1, 0), (m, 1))
        Mm = mul(Lm, P)
        sq = mul(Mm, Mm)
        rows[str(m)] = {"M_m": Mm, "M_m^2 = L^m R^m": sq == mul(Lm, Rm),
                        "H1 torsion of the M_m bundle": coker_minus_identity(Mm)[1],
                        "H1 torsion of the M_m^2 bundle": coker_minus_identity(sq)[1]}
        ok &= (Mm == ((m, 1), (1, 0)) and sq == mul(Lm, Rm)
               and coker_minus_identity(Mm) == (0, [m] if m > 1 else [])
               and coker_minus_identity(sq) == (0, [m, m] if m > 1 else []))
    return {"rows": rows, "SE1 selects m = 1": ok, "passed": ok}


def main():
    t0 = time.time()
    rec = {"C1 records route": check_records_route(), "C2 torsion selector": check_torsion_selector(),
           "C3 order bit": check_order_bit()}
    c4, rows = check_census()
    rec["C4 word census"] = c4
    rec["C8 necessity (integer part)"] = check_necessity()
    rec["C9 the unit shears generate every state"] = check_generation(rows)
    rec["C10 the metallic family"] = check_metallic()
    rec["C5-C7 SnapPy"] = snappy_checks()
    rec["all passed"] = all(v.get("passed", False) for v in rec.values() if isinstance(v, dict))
    rec["seconds"] = round(time.time() - t0, 1)
    summary = {k: (v.get("passed") if isinstance(v, dict) else v) for k, v in rec.items()}
    print(json.dumps(summary, indent=1))
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return rec


if __name__ == "__main__":
    main()
