#!/usr/bin/env python3
"""B1519 -- GENESIS v1.2: this seat's own checks of what the amendment states.

K1  B14's square roots, completely: by Cayley-Hamilton every X in GL(2,Z) with X^2 = A satisfies A = tr(X) X - det(X) I, so
    X = (A + det(X) I) / tr(X) with tr(X)^2 = tr(A) + 2 det(X) (tr X = 0 would give X^2 = -det(X) I, not hyperbolic). This
    enumerates every integer square root, not a box of them. On L^a R^b (a, b = 1..8): a det -1 root exists exactly when a = b,
    it is +-L^a P, and no det +1 root exists.  For LR: the roots are +-LP only (B14's statement).
K2  B469's identity, symbolically in m: X_m = [[m, 1], [1, 0]] = L^m P has X_m^2 = [[m^2 + 1, m], [m, 1]] = L^m R^m and
    det X_m = -1, so every metallic bundle of L^m R^m double-covers the non-orientable bundle of L^m P.
K3  The swap on the root's monodromy (B16's finding, made explicit): P LR P^-1 = RL, which is not (LR)^-1. The conjugators of
    LR to its inverse, of each determinant, in a box.
K4  B1234's base rate: the amphichiral manifolds among the first 200 orientable one-cusped census manifolds, named; and the
    cusp counts of the orientation double covers of the first 40 non-orientable ones.
K5  The audit lane's R78 at -(LR)^2: the bundles of LR, (LR)^2, -(LR)^2 and (LR)^4 identified, with H1; -(LR)^2 is neither a
    state nor a level of any state (proof in FINDINGS section 3, checked here on every trace-7 candidate); and the number of
    matrices in B1516 C9's box whose reduction is a signed power -u^k with k even.
K6  Main's v1.1 at SE2 (from B1234): pi_1(m000) has the same 48 surjections onto 2T = SL(2, F_3) as pi_1(m004). Counted here
    by brute force over SnapPy's presentations: every assignment of the generators to SL(2, F_3) that satisfies the relators
    and generates the whole group.
K7  Main's B1327 (OPEN), its one computation, at GENESIS FK3: the eight isometries of m004 act on the cusp's (meridian,
    longitude) by diag(s_m, s_l); each of the four sign pairs occurs twice, and the orientation sign det = s_m s_l. B1327
    reads s_m as the arrow and s_l as the swap: the mirror is the swap times the arrow, three named bits with one relation.
Core convention (GENESIS section 2): L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]].
Usage: python3 genesis_v12_checks.py  (writes genesis_v12_checks.json beside it)"""
import importlib.util
import itertools
import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("b1516_foundations", ROOT / "frontier" / "B1516_genesis_v1" / "verification"
                                              / "foundations_checks.py")
F = importlib.util.module_from_spec(spec)
spec.loader.exec_module(F)
L, R, P, I2 = F.L, F.R, F.P, F.I2
mul, det, tr, neg, inv, word = F.mul, F.det, F.tr, F.neg, F.inv, F.word


def mpow(A, n):
    M = I2
    for _ in range(n):
        M = mul(M, A)
    return M


def isqrt_exact(n):
    if n < 0:
        return None
    r = int(round(n ** 0.5))
    for s in (r - 1, r, r + 1):
        if s >= 0 and s * s == n:
            return s
    return None


def square_roots(A):
    """every X in GL(2,Z) with X^2 = A, for hyperbolic A (Cayley-Hamilton; complete)"""
    roots = []
    for d in (1, -1):
        s = isqrt_exact(tr(A) + 2 * d)
        if not s:
            continue
        for t in (s, -s):
            num = ((A[0][0] + d, A[0][1]), (A[1][0], A[1][1] + d))
            if all(x % t == 0 for row in num for x in row):
                X = tuple(tuple(x // t for x in row) for row in num)
                if det(X) == d and mul(X, X) == A:
                    roots.append(X)
    return roots


# ------------------------------------------------------------------------------------------------ K1
def k1(nmax=8):
    out, ok = {}, True
    LR = mul(L, R)
    rLR = square_roots(LR)
    LP = mul(L, P)
    out["roots of LR"] = [list(map(list, X)) for X in rLR]
    ok &= sorted(rLR) == sorted([LP, neg(LP)])
    # the bounded brute force agrees with the closed form on LR
    brute = [X for X in (((a, b), (c, d)) for a, b, c, d in itertools.product(range(-6, 7), repeat=4))
             if det(X) in (1, -1) and mul(X, X) == LR]
    out["roots of LR by brute force, entries in [-6, 6]"] = len(brute)
    ok &= sorted(brute) == sorted(rLR)
    table = {}
    for a in range(1, nmax + 1):
        for b in range(1, nmax + 1):
            A = mul(mpow(L, a), mpow(R, b))
            rts = square_roots(A)
            dets = sorted(det(X) for X in rts)
            table[f"{a},{b}"] = dets
            if a == b:
                LaP = mul(mpow(L, a), P)
                ok &= sorted(rts) == sorted([LaP, neg(LaP)]) and dets == [-1, -1]
            else:
                ok &= rts == []
    out["L^a R^b, a, b = 1..%d: determinants of all integer square roots" % nmax] = table
    out["a det -1 root exists exactly when a = b, and it is +-L^a P; no det +1 root"] = ok
    out["passed"] = ok
    return out


# ------------------------------------------------------------------------------------------------ K2
def k2():
    import sympy as sp
    m = sp.symbols("m", integer=True, positive=True)
    X = sp.Matrix([[m, 1], [1, 0]])
    Lm = sp.Matrix([[1, m], [0, 1]])
    Rm = sp.Matrix([[1, 0], [m, 1]])
    Pm = sp.Matrix([[0, 1], [1, 0]])
    sq = sp.simplify(X * X)
    out = {"X_m = L^m P": sp.simplify(Lm * Pm - X) == sp.zeros(2, 2),
           "X_m^2": str(sq.tolist()),
           "X_m^2 = L^m R^m": sp.simplify(sq - Lm * Rm) == sp.zeros(2, 2),
           "det X_m": str(X.det())}
    out["passed"] = out["X_m = L^m P"] and out["X_m^2 = L^m R^m"] and X.det() == -1
    return out


# ------------------------------------------------------------------------------------------------ K3
def k3(bound=4):
    LR, RL = mul(L, R), mul(R, L)
    out = {"P LR P^-1": list(map(list, mul(mul(P, LR), inv(P)))), "RL": list(map(list, RL)),
           "(LR)^-1": list(map(list, inv(LR)))}
    out["P LR P^-1 = RL"] = mul(mul(P, LR), inv(P)) == RL
    out["RL = (LR)^-1"] = RL == inv(LR)
    conj = {1: [], -1: []}
    for x in itertools.product(range(-bound, bound + 1), repeat=4):
        X = ((x[0], x[1]), (x[2], x[3]))
        d = det(X)
        if d in (1, -1) and mul(X, LR) == mul(inv(LR), X):
            conj[d].append(X)
    out["conjugators X LR X^-1 = (LR)^-1 with entries in [-%d, %d]: det +1" % (bound, bound)] = [list(map(list, X)) for X in conj[1]]
    out["the same, det -1"] = [list(map(list, X)) for X in conj[-1]]
    out["P among them"] = P in conj[-1]
    out["passed"] = out["P LR P^-1 = RL"] and not out["RL = (LR)^-1"] and not out["P among them"]
    return out


# ------------------------------------------------------------------------------------------------ K4
def k4():
    import snappy
    out = {}
    amph = []
    errors = 0
    first = snappy.OrientableCuspedCensus(cusps=1)[:200]
    names = []
    for M in first:
        names.append(M.name())
        try:
            if M.symmetry_group().is_amphicheiral():
                amph.append(M.name())
        except Exception:
            errors += 1
    out["population: first and last names, size"] = [names[0], names[-1], len(names)]
    out["amphichiral among them"] = amph
    out["symmetry-group errors"] = errors
    cusps = {}
    amph_cov = 0
    for N in snappy.NonorientableCuspedCensus[:40]:
        C = N.orientation_cover()
        cusps[C.num_cusps()] = cusps.get(C.num_cusps(), 0) + 1
        amph_cov += bool(C.symmetry_group().is_amphicheiral())
    out["orientation covers of the first 40 non-orientable census manifolds: cusp counts"] = {str(k): v for k, v in sorted(cusps.items())}
    out["of them amphichiral"] = amph_cov
    out["passed"] = (amph == ["m003", "m004", "m135", "m136", "m206", "m207"] and errors == 0 and amph_cov == 40)
    return out


# ------------------------------------------------------------------------------------------------ K5
def k5():
    import snappy
    out = {}
    A = mul(L, R)

    def ident(M):
        try:
            return [str(x) for x in M.identify()]
        except Exception:
            return []
    rows = {}
    for label, name in (("+LR", "b++LR"), ("+(LR)^2", "b++LRLR"), ("-(LR)^2", "b+-LRLR"), ("+(LR)^4", "b++LRLRLRLR")):
        M = snappy.Manifold(name)
        rows[label] = {"identify": ident(M), "H1": str(M.homology()), "cusps": M.num_cusps()}
    out["bundles"] = rows
    m207 = snappy.Manifold("m207")
    out["b+-LRLR is isometric to m207"] = bool(snappy.Manifold("b+-LRLR").is_isometric_to(m207))
    # -(LR)^2 is no level: a level of the state (eps, u) is (eps A(u))^n. Its trace is +-7 only if tr(u^n) = 7; a positive word
    # with both letters of length l has trace >= l + 1, so tr(u) <= 7 bounds len(u) <= 6, and n <= 2 (tr(u^2) = tr(u)^2 - 2).
    target = neg(mpow(A, 2))
    cands = []
    for l in range(2, 7):
        for p in itertools.product("LR", repeat=l):
            u = "".join(p)
            if "L" not in u or "R" not in u or not F.primitive(u) or F.canon_state(u) != u:
                continue
            for eps in (1, -1):
                for n in (1, 2, 3):
                    M = mpow(word(u) if eps == 1 else neg(word(u)), n)
                    if tr(M) == tr(target):
                        cands.append({"state": ("+" if eps == 1 else "-") + u, "n": n,
                                      "H1 torsion": F.coker_minus_identity(M)[1]})
    mins = {}
    for l in range(2, 13):
        mins[str(l)] = min(tr(word("".join(p))) for p in itertools.product("LR", repeat=l) if "L" in p and "R" in p)
    out["minimal trace of a positive word with both letters, by length"] = mins
    out["levels with trace -7 (state, n, H1 torsion)"] = cands
    tgt_tors = F.coker_minus_identity(target)[1]
    out["-(LR)^2: H1 torsion"] = tgt_tors
    out["no level has the torsion of -(LR)^2"] = all(c["H1 torsion"] != tgt_tors for c in cands)
    # B1516 C9's box: which reductions are signed powers -u^k with k even
    signed_even = []
    for a, b, c, d in itertools.product(range(-5, 6), repeat=4):
        B = ((a, b), (c, d))
        if a * d - b * c != 1 or abs(a + d) <= 2:
            continue
        eps, w = F.to_positive_word(B)
        root = next(w[:k] for k in range(1, len(w) + 1) if len(w) % k == 0 and w == w[:k] * (len(w) // k))
        k = len(w) // len(root)
        if eps == -1 and k % 2 == 0:
            signed_even.append({"B": [[a, b], [c, d]], "word": w, "k": k, "trace": a + d})
    out["C9 box: matrices reducing to -u^k with k even"] = signed_even
    ok = (rows["+LR"]["identify"][:1] == ["m004(0,0)"] and rows["+(LR)^2"]["identify"][:1] == ["m206(0,0)"]
          and "m207(0,0)" in rows["-(LR)^2"]["identify"] and rows["-(LR)^2"]["H1"] == "Z/3 + Z/3 + Z"
          and out["b+-LRLR is isometric to m207"] and out["no level has the torsion of -(LR)^2"]
          and all(v == int(l) + 1 for l, v in mins.items())
          and len(signed_even) == 4 and all(s["trace"] == -7 and s["k"] == 2 for s in signed_even))
    out["passed"] = ok
    return out


# ------------------------------------------------------------------------------------------------ K6
def k6():
    import snappy
    p = 3
    els = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(p), repeat=4) if (a * d - b * c) % p == 1]

    def m(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % p for j in range(2)) for i in range(2))

    def minv(A):
        (a, b), (c, d) = A
        return ((d % p, -b % p), (-c % p, a % p))

    ident = ((1, 0), (0, 1))

    def generated(gens):
        seen, frontier = {ident}, [ident]
        while frontier:
            nxt = []
            for x in frontier:
                for g in gens:
                    y = m(x, g)
                    if y not in seen:
                        seen.add(y)
                        nxt.append(y)
            frontier = nxt
        return len(seen)

    out = {"|SL(2, F_3)|": len(els)}
    for name in ("m000", "m004"):
        G = snappy.Manifold(name).fundamental_group()
        rels = G.relators(as_int_list=True)
        n = G.num_generators()
        count = 0
        for assign in itertools.product(els, repeat=n):
            img = {i + 1: assign[i] for i in range(n)}
            img.update({-(i + 1): minv(assign[i]) for i in range(n)})
            ok = True
            for r in rels:
                X = ident
                for g in r:
                    X = m(X, img[g])
                if X != ident:
                    ok = False
                    break
            if ok and generated(list(assign)) == len(els):
                count += 1
        out[f"{name}: generators, relators, surjections onto SL(2, F_3)"] = [n, len(rels), count]
    out["passed"] = (len(els) == 24 and out["m000: generators, relators, surjections onto SL(2, F_3)"][2] == 48
                     and out["m004: generators, relators, surjections onto SL(2, F_3)"][2] == 48)
    return out


def k7():
    import collections
    import snappy
    M = snappy.Manifold("m004")
    G = M.symmetry_group()
    isos = M.is_isometric_to(M, return_isometries=True)
    triples, diagonal = collections.Counter(), True
    for iso in isos:
        cm = iso.cusp_maps()[0]
        a, b, c, d = int(cm[0, 0]), int(cm[0, 1]), int(cm[1, 0]), int(cm[1, 1])
        diagonal = diagonal and b == 0 and c == 0
        triples[(a, d, a * d - b * c)] += 1
    out = {"symmetry group, order": [str(G), G.order()], "amphichiral": G.is_amphicheiral(),
           "isometries": len(isos), "cusp maps diagonal": diagonal,
           "(s_m, s_l, det) with multiplicity": sorted([list(k) + [v] for k, v in triples.items()], reverse=True)}
    out["det = s_m s_l on every isometry"] = all(dt == sm * sl for (sm, sl, dt) in triples)
    out["passed"] = (len(isos) == 8 and diagonal and out["det = s_m s_l on every isometry"] and len(triples) == 4
                     and set(triples.values()) == {2})
    return out


def main():
    t0 = time.time()
    rec = {}
    for name, fn in (("K1 B14: every integer square root of L^a R^b", k1), ("K2 B469: X_m^2 = L^m R^m, det -1", k2),
                     ("K3 the swap on LR", k3), ("K4 B1234's base rate, named", k4), ("K5 R78 at -(LR)^2", k5),
                     ("K6 surjections onto 2T (main v1.1, B1234)", k6),
                     ("K7 three bits, one relation (main B1327)", k7)):
        t = time.time()
        rec[name] = fn()
        print("%-48s passed: %s (%.1f s)" % (name, rec[name]["passed"], time.time() - t), flush=True)
    rec["all passed"] = all(v["passed"] for v in rec.values() if isinstance(v, dict))
    (HERE / "genesis_v12_checks.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(rec, indent=1, ensure_ascii=False))
    print("ALL PASSED: %s (%.1f s)" % (rec["all passed"], time.time() - t0))


if __name__ == "__main__":
    main()
