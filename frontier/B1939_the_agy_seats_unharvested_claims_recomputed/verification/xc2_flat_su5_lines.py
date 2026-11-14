"""X-C2 (harvest row 1464), main's independent recomputation. Exact integer / rational arithmetic only.

Definitions: EXPECTATIONS.md (same folder), D1-D9. Written from the mathematical statements; no code of any seat is
imported or copied.

A line p = (p1, p2) in (Q/Z)^2 is held as integers (i, j) over a common denominator D.  Fibre holonomies
h(p_k) = exp(2 pi i p_k T) with T = diag(weights).  A flat bundle on the mapping torus of M with these commuting fibre
holonomies exists iff one base holonomy g carries the pair (h(p1), h(p2)) to (h(q1), h(q2)), q = M^T p, in the
admissibility class (I, O, Z, ZO).  Decided by the joint spectrum (D5), and separately by the linear condition and by the
per-generator test.

Run:  OMP_NUM_THREADS=1 nice -n 10 python3 -B xc2_check.py
"""
import json
import sys
from fractions import Fraction as Fr
from itertools import product
from math import gcd, lcm

W6Y = (-2, -2, -2, 3, 3)                 # 6Y on the 5 of SU(5) (D3)
M_STD = ((2, 1), (1, 1))                 # LR with L = [[1,1],[0,1]], R = [[1,0],[1,1]] (D1)
M_ALT = ((1, 1), (1, 2))                 # the web seat's "LR" (the other naming), conjugate by the swap
J_TICK = ((1, 1), (1, 0))                # the tick, det -1, J^2 = M_STD (D2)
M_TR4 = ((3, 1), (2, 1))                 # PLANT P1/P5: trace 4, det 1
T_WEYL = (1, -1, 0, 0, 0)                # PLANT P2: a Weyl-symmetric generator
OUT = {}


def det(A): return A[0][0] * A[1][1] - A[0][1] * A[1][0]
def tr(A): return A[0][0] + A[1][1]
def T(A): return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))
def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def app(A, p, D): return ((A[0][0] * p[0] + A[0][1] * p[1]) % D, (A[1][0] * p[0] + A[1][1] * p[1]) % D)
def neg(p, D): return ((-p[0]) % D, (-p[1]) % D)


def lines_exact(n):
    """all (i, j) mod n of exact order n"""
    return [(i, j) for i in range(n) for j in range(n) if gcd(gcd(i, j), n) == 1]


# ---------------------------------------------------------------- relaxers: per-weight exponent shifts (units 1/D)
def centre_relaxers(D, weights):
    """the centre Z/5 of SU(5): scalars zeta^k, k = 0..4 (shift k/5 on every eigenvalue)"""
    assert D % 5 == 0
    return [tuple([k * D // 5] * len(weights)) for k in range(5)]


def mu10_relaxers(D, weights):
    """PLANT P3: 'centre' taken as h(m/10), m = 0..9, inside U(1)_Y (not central: h(1/2) = diag(1,1,1,-1,-1))"""
    assert D % 10 == 0
    return [tuple((w * m * D // 10) % D for w in weights) for m in range(10)]


def trivial_relaxers(D, weights): return [tuple([0] * len(weights))]


def joint_spec(p, D, weights, r1=None, r2=None):
    r1 = r1 or [0] * len(weights); r2 = r2 or [0] * len(weights)
    return tuple(sorted(((w * p[0] + r1[j]) % D, (w * p[1] + r2[j]) % D) for j, w in enumerate(weights)))


def gen_spec(c, D, weights, r=None):
    r = r or [0] * len(weights)
    return tuple(sorted((w * c + r[j]) % D for j, w in enumerate(weights)))


def admissible_joint(p, D, M, weights, outer, relaxers):
    q = app(T(M), p, D)
    target = joint_spec(q, D, weights)
    for s in ((1, -1) if outer else (1,)):
        ps = p if s == 1 else neg(p, D)
        for r1 in relaxers:
            for r2 in relaxers:
                if joint_spec(ps, D, weights, r1, r2) == target:
                    return True
    return False


def admissible_pergen(p, D, M, weights, outer, relaxers):
    q = app(T(M), p, D)
    for s in ((1, -1) if outer else (1,)):
        ps = p if s == 1 else neg(p, D)
        ok = all(any(gen_spec(ps[k], D, weights, r) == gen_spec(q[k], D, weights) for r in relaxers) for k in (0, 1))
        if ok:
            return True
    return False


def admissible_linear(p, D, M, outer, centre):
    """the Fact-2 shortcut: (s M^T - I) p in C mod 1, C = 0 or (1/5 Z/Z)^2"""
    MT = T(M)
    for s in ((1, -1) if outer else (1,)):
        q = app(MT, p, D); q = q if s == 1 else neg(q, D)
        d = ((q[0] - p[0]) % D, (q[1] - p[1]) % D)
        if centre:
            if all((5 * x) % D == 0 for x in d):
                return True
        elif d == (0, 0):
            return True
    return False


def is_central(p, D, weights):
    """the holonomies are scalars: every weight gives the same exponent, on both generators"""
    return all(len({(w * p[k]) % D for w in weights}) == 1 for k in (0, 1))


CLASSES = {"I": (False, False), "O": (True, False), "Z": (False, True), "ZO": (True, True)}


def census(M, weights, nmax, relax="centre", method="joint"):
    """every line of exact order n <= nmax; per class: the admitted lines (as Fractions) with central flag and order"""
    res = {c: [] for c in CLASSES}
    for n in range(1, nmax + 1):
        base = lcm(n, 10 if relax == "mu10" else 5)
        for (i, j) in lines_exact(n):
            p = (i * base // n, j * base // n)
            for cname, (outer, cen) in CLASSES.items():
                if method == "joint":
                    rel = (mu10_relaxers if relax == "mu10" else centre_relaxers)(base, weights) if cen else trivial_relaxers(base, weights)
                    ok = admissible_joint(p, base, M, weights, outer, rel)
                elif method == "pergen":
                    rel = (mu10_relaxers if relax == "mu10" else centre_relaxers)(base, weights) if cen else trivial_relaxers(base, weights)
                    ok = admissible_pergen(p, base, M, weights, outer, rel)
                else:
                    ok = admissible_linear(p, base, M, outer, cen)
                if ok:
                    res[cname].append((Fr(i, n), Fr(j, n), n, is_central(p, base, weights)))
    return res


def summarise(res, levels=(5, 10, 25)):
    s = {}
    for c, L in res.items():
        row = {"all": [len(L), sum(1 for x in L if not x[3])],
               "orders": sorted({x[2] for x in L}),
               "noncentral_orders": sorted({x[2] for x in L if not x[3]})}
        for N in levels:
            sub = [x for x in L if N % x[2] == 0]
            row["level_%d" % N] = [len(sub), sum(1 for x in sub if not x[3])]
            ex = [x for x in L if x[2] == N]
            row["exact_%d" % N] = [len(ex), sum(1 for x in ex if not x[3])]
        s[c] = row
    return s


def separation_holds(summ):
    """the claim: no non-central line in I, O, Z; some in ZO"""
    return summ["I"]["all"][1] == 0 and summ["O"]["all"][1] == 0 and summ["Z"]["all"][1] == 0 and summ["ZO"]["all"][1] > 0


def counts_as_claimed(summ):
    return ([summ[c]["all"] for c in ("I", "O", "Z", "ZO")] == [[1, 0], [5, 0], [25, 0], [125, 100]]
            and summ["ZO"]["noncentral_orders"] == [25])


# ---------------------------------------------------------------- Fact 2
def fact2_injective(weights, nmax):
    seen = {}
    for n in range(1, nmax + 1):
        for i in range(n):
            if gcd(i, n) != 1:
                continue
            c = Fr(i, n)
            key = tuple(sorted((w * c) % 1 for w in weights))
            if key in seen and seen[key] != c:
                return False, (str(seen[key]), str(c))
            seen[key] = c
    return True, len(seen)


# ---------------------------------------------------------------- Fact 3
def mpow(M, k, N):
    R = ((1, 0), (0, 1))
    for _ in range(k):
        R = tuple(tuple(x % N for x in row) for row in mul(R, M))
    return R


def order_mod(M, N):
    R, k = tuple(tuple(x % N for x in row) for row in M), 1
    while R != ((1 % N, 0), (0, 1 % N)):
        R = tuple(tuple(x % N for x in row) for row in mul(R, M)); k += 1
    return k


def least_k(M, v, N, sign, cap):
    target = v if sign == 1 else neg(v, N)
    w = app(M, v, N); k = 1
    while k <= cap:
        if w == target:
            return k
        w = app(M, w, N); k += 1
    return None


def fact3(M, Ns=(2, 5, 10, 25, 30), exact=True):
    t = {}
    for N in Ns:
        o = order_mod(M, N)
        vs = lines_exact(N) if exact else [(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0)]
        plus = sorted({least_k(M, v, N, 1, o) for v in vs})
        minus = sorted({k for k in (least_k(M, v, N, -1, o) for v in vs) if k is not None})
        nonemin = sum(1 for v in vs if least_k(M, v, N, -1, o) is None)
        t[N] = {"order": o, "n_lines": len(vs), "least_k_plus": plus, "least_k_minus": minus, "lines_without_minus": nonemin}
    return t


def fact3_as_claimed(t):
    want = {2: (3, [3], [3]), 5: (10, [2, 10], [1, 5]), 10: (30, [6, 30], [3, 15]), 25: (50, [10, 50], [5, 25]),
            30: (60, [12, 60], [])}
    return all((t[N]["order"], t[N]["least_k_plus"], t[N]["least_k_minus"]) == want[N] for N in want)


def ks_of(M, line, sign):
    n = lcm(line[0].denominator, line[1].denominator)
    v = (int(line[0] * n) % n, int(line[1] * n) % n)
    return least_k(M, v, n, sign, order_mod(M, n))


# ================================================================ run
if __name__ == "__main__":
    # 0. charges (D3)
    w = W6Y
    lam2 = sorted(w[i] + w[j] for i in range(5) for j in range(i + 1, 5))
    fivebar = sorted(-x for x in w)
    OUT["charges"] = {"Lambda2_5": lam2, "fivebar": fivebar, "five": sorted(w), "traceless": sum(w) == 0,
                      "frame_set_matches": sorted(set(lam2) | set(fivebar) | {3}) == sorted({1, -4, 2, -3, 6, 3})}

    # 1. Fact 1
    OUT["fact1"] = {n: {"det(M-I)": det(((M[0][0] - 1, M[0][1]), (M[1][0], M[1][1] - 1))),
                        "det(M+I)": det(((M[0][0] + 1, M[0][1]), (M[1][0], M[1][1] + 1))), "tr": tr(M), "det": det(M)}
                    for n, M in (("M_STD", M_STD), ("M_ALT", M_ALT), ("J", J_TICK), ("PLANT_TR4", M_TR4))}

    # 2. Fact 2 (exact, denominators <= 200) and its plant P2
    OUT["fact2"] = {"6Y": fact2_injective(W6Y, 200), "PLANT_P2_Tweyl": fact2_injective(T_WEYL, 200)}

    # 3. the four classes, lines of exact order <= 60, three methods
    NMAX = 60
    res = {}
    for name, M in (("M_STD", M_STD), ("M_ALT", M_ALT), ("M_STD_bflip", ((2, -1), (-1, 1)))):
        r_joint = census(M, W6Y, NMAX, method="joint")
        r_pg = census(M, W6Y, NMAX, method="pergen")
        r_lin = census(M, W6Y, NMAX, method="linear")
        same = all({x[:2] for x in r_joint[c]} == {x[:2] for x in r_pg[c]} == {x[:2] for x in r_lin[c]} for c in CLASSES)
        sm = summarise(r_joint)
        on25 = [x for x in r_joint["ZO"] if not x[3] and x[0] in (Fr(2, 5), Fr(3, 5))]
        in25 = all((25 * x[0]).denominator == 1 and (25 * x[1]).denominator == 1 for c in CLASSES for x in r_joint[c])
        res[name] = {"summary": sm, "three_methods_agree": same, "separation_holds": separation_holds(sm),
                     "counts_as_claimed": counts_as_claimed(sm), "ZO_noncentral_on_slope_2_5": len(on25),
                     "all_solutions_in_(1/25)^2": in25,
                     "O_lines": sorted((str(x[0]), str(x[1])) for x in r_joint["O"]),
                     "ZO_noncentral_examples": [(str(x[0]), str(x[1])) for x in r_joint["ZO"] if not x[3]][:3]}
        # ZO group structure: elements by exact order
        res[name]["ZO_by_order"] = {n: sum(1 for x in r_joint["ZO"] if x[2] == n) for n in sorted({x[2] for x in r_joint["ZO"]})}
    OUT["census_order_le_60"] = res

    # 4. the aside: J's mapping torus (the det -1 tick)
    rJ = census(J_TICK, W6Y, NMAX, method="joint")
    OUT["J_aside"] = {"summary": summarise(rJ), "separation_holds": separation_holds(summarise(rJ))}

    # 5. PLANTS for the separation claim
    r1 = census(M_TR4, W6Y, 30, method="joint")
    r2 = census(M_STD, T_WEYL, 30, method="joint")
    r3 = census(M_STD, W6Y, 30, relax="mu10", method="joint")
    OUT["plants_separation"] = {
        "P1_trace4": {"summary": summarise(r1), "separation_holds": separation_holds(summarise(r1)),
                      "I_noncentral": [(str(x[0]), str(x[1]), x[2]) for x in r1["I"] if not x[3]]},
        "P2_Tweyl": {"summary": summarise(r2), "separation_holds": separation_holds(summarise(r2)),
                     "I_noncentral": [(str(x[0]), str(x[1]), x[2]) for x in r2["I"] if not x[3]][:6]},
        "P3_mu10_centre": {"summary": summarise(r3), "separation_holds": separation_holds(summarise(r3)),
                           "Z_noncentral_orders": summarise(r3)["Z"]["noncentral_orders"]},
    }

    # 6. Fact 3 and its plants
    f3 = {n: fact3(M) for n, M in (("M_STD", M_STD), ("M_ALT", M_ALT))}
    OUT["fact3"] = {n: {"table": t, "as_claimed": fact3_as_claimed(t)} for n, t in f3.items()}
    p4 = fact3(M_STD, exact=False); p5 = fact3(M_TR4)
    OUT["plants_fact3"] = {"P4_all_nonzero_vectors": {"N10_plus": p4[10]["least_k_plus"], "as_claimed": fact3_as_claimed(p4)},
                           "P5_trace4": {"orders": {N: p5[N]["order"] for N in p5}, "as_claimed": fact3_as_claimed(p5)}}

    # 7. the counted class (2/5, odd tenths) and the mark's order-10 halves
    counted = [(Fr(2, 5), Fr(k, 10)) for k in (1, 3, 5, 7, 9)]
    OUT["counted_class"] = {n: {"plus": [ks_of(M, v, 1) for v in counted], "minus": [ks_of(M, v, -1) for v in counted]}
                            for n, M in (("M_STD", M_STD), ("M_ALT", M_ALT))}
    mark_line = [(Fr(k, 5), Fr(2 * k % 5, 5)) for k in range(1, 5)]
    # the mark line is ker(M + I) mod 5 and, with 0, the class-O set
    ker = sorted((Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5)
                 if (i, j) != (0, 0) and app(M_STD, (i, j), 5) == neg((i, j), 5))
    sm_mark = (Fr(2, 5), Fr(4, 5))
    sm_halves = [((sm_mark[0] / 2 + Fr(e1, 2)) % 1, (sm_mark[1] / 2 + Fr(e2, 2)) % 1) for e1 in (0, 1) for e2 in (0, 1)]
    all_halves = sorted({((m[0] / 2 + Fr(e1, 2)) % 1, (m[1] / 2 + Fr(e2, 2)) % 1) for m in mark_line for e1 in (0, 1) for e2 in (0, 1)})
    order = lambda v: lcm(v[0].denominator, v[1].denominator)
    adm = {c: {(x[0], x[1]) for x in res_c} for c, res_c in census(M_STD, W6Y, 10, method="joint").items()}
    halves10 = [v for v in all_halves if order(v) == 10]
    k6_lines = sorted((Fr(i, 10), Fr(j, 10)) for (i, j) in lines_exact(10) if least_k(M_STD, (i, j), 10, 1, 30) == 6)
    OUT["mark"] = {
        "mark_line_equals_ker(M+I)_mod5": sorted(mark_line) == ker,
        "O_set_equals_0_plus_mark_line": sorted(res["M_STD"]["O_lines"]) == sorted([("0", "0")] + [(str(a), str(b)) for a, b in mark_line]),
        "sm_halves": [{"line": (str(v[0]), str(v[1])), "order": order(v), "k_plus": ks_of(M_STD, v, 1), "k_minus": ks_of(M_STD, v, -1),
                       "admissible_in": [c for c in CLASSES if v in adm[c]]} for v in sm_halves],
        "all_order10_halves": len(halves10),
        "all_halves_k": sorted({(ks_of(M_STD, v, 1), ks_of(M_STD, v, -1)) for v in halves10}),
        "halves_are_exactly_the_k6_order10_lines": sorted(halves10) == k6_lines,
        "any_half_admissible": any(v in adm[c] for v in halves10 for c in CLASSES),
        "J_k_of_halves": sorted({(ks_of(J_TICK, v, 1), ks_of(J_TICK, v, -1)) for v in halves10}),
        # second reading of the mark (the twin (1/5, 2/5) as the mark): its halves are among all_halves already
        "twin_halves": [(str(v[0]), str(v[1]), order(v)) for v in sorted({((Fr(1, 10) + Fr(e1, 2)) % 1, (Fr(1, 5) + Fr(e2, 2)) % 1) for e1 in (0, 1) for e2 in (0, 1)})],
    }

    # 8. identification dependence of the counted class (g in GL(2, Z), entries in [-3, 3])
    splits = {}
    for a, b, c, d in product(range(-3, 4), repeat=4):
        if abs(a * d - b * c) != 1:
            continue
        g = ((a, b), (c, d))
        gi = tuple(tuple(x * (a * d - b * c) for x in row) for row in ((d, -b), (-c, a)))
        Mg = mul(mul(gi, M_STD), g)
        splits.setdefault(tuple(sorted(ks_of(Mg, v, 1) for v in counted)), 0)
        splits[tuple(sorted(ks_of(Mg, v, 1) for v in counted))] += 1
    OUT["counted_class_splits_over_GL2Z"] = {str(k): v for k, v in sorted(splits.items())}

    # 9. verdicts and plant verdicts
    V = {
        "fact1": OUT["fact1"]["M_STD"]["det(M-I)"] in (1, -1) and abs(OUT["fact1"]["M_STD"]["det(M+I)"]) == 5,
        "fact2_6Y_injective": OUT["fact2"]["6Y"][0],
        "counts_as_claimed_all_conventions": all(res[n]["counts_as_claimed"] for n in res),
        "separation_holds_all_conventions": all(res[n]["separation_holds"] for n in res),
        "three_methods_agree": all(res[n]["three_methods_agree"] for n in res),
        "fact3_as_claimed": all(OUT["fact3"][n]["as_claimed"] for n in OUT["fact3"]),
        "PLANT_P1_trace4_separation_FAILS": not OUT["plants_separation"]["P1_trace4"]["separation_holds"],
        "PLANT_P2_Tweyl_separation_FAILS": not OUT["plants_separation"]["P2_Tweyl"]["separation_holds"],
        "PLANT_P2_Tweyl_fact2_FAILS": not OUT["fact2"]["PLANT_P2_Tweyl"][0],
        "PLANT_P3_mu10_separation_FAILS": not OUT["plants_separation"]["P3_mu10_centre"]["separation_holds"],
        "PLANT_P4_fact3_FAILS": not OUT["plants_fact3"]["P4_all_nonzero_vectors"]["as_claimed"],
        "PLANT_P5_fact3_FAILS": not OUT["plants_fact3"]["P5_trace4"]["as_claimed"],
    }
    OUT["VERDICTS"] = V
    json.dump(OUT, open("xc2_out.json", "w"), indent=1, default=str)
    for k, v in V.items():
        print("%-45s %s" % (k, v))
    print("exit 0" if all(V.values()) else "SOME CHECK FALSE")
