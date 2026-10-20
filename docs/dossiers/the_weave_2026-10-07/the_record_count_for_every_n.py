"""W109: the checks of the proof of B1677 for every n >= 3 (main's ask, relay of 2026-10-20). The proof,
W109_PROOF.md, was committed before this script (2d10142d3). One run. The proof does not rest on these checks.

C1  Fricke's identity and its triple form, Cayley-Hamilton at trace 0 and the polarisation xy + yx = tr(xy) I for
    traceless x, y, exact (sympy, generic 2 x 2 matrices).
C2  R_ij^-1 = R_ik^-1 R_kj^-1 R_ik R_kj and L_ij^-1 = L_ik^-1 L_kj^-1 L_ik L_kj on the generators of F_3 and F_4.
C3  n = 2: the characters fixed by R (a -> ab) and L (b -> ab); their images under the inversion and the swap.
C4  n = 3, independent of the proof's test words: a trace reducer (Fricke's identities on words) checked against
    random SL(2, C) matrices; each move on the seven coordinates and the relation of z; a Groebner basis of the fixed
    equations for the six R_ij, the six L_ij and all twelve.
C5  Aut, Inn and the solvability of Out for Q8, 2T, 2O, 2I and Dic_m (3 <= m <= 12), by brute force, with W108's
    group helpers.

Run: python3 the_record_count_for_every_n.py -> the_record_count_for_every_n.json and _run.txt beside it.
"""
import importlib.util
import itertools
import json
import math
import random
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_record_count_for_every_n.json"
RUN = HERE / "the_record_count_for_every_n_run.txt"
LINES = []

_spec = importlib.util.spec_from_file_location("w108", HERE / "the_icosahedral_common_point.py")
W108 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(W108)


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LINES.append(s)


# ---------------------------------------------------------------- words and automorphisms of F_n

def inv(w):
    return tuple(-x for x in reversed(w))


def free(w):
    st = []
    for x in w:
        if st and st[-1] == -x:
            st.pop()
        else:
            st.append(x)
    return tuple(st)


def cyc(w):
    w = free(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    return w


def apply(phi, w):
    out = []
    for x in w:
        out.extend(phi.get(x, (x,)) if x > 0 else inv(phi.get(-x, (-x,))))
    return free(out)


def compose(phi, psi, n):
    """(phi psi)(a) = phi(psi(a))"""
    return {a: apply(phi, psi.get(a, (a,))) for a in range(1, n + 1)}


def full(phi, n):
    return {a: free(phi.get(a, (a,))) for a in range(1, n + 1)}


def R(i, j):
    return {i: (i, j)}


def Rinv(i, j):
    return {i: (i, -j)}


def L(i, j):
    return {i: (j, i)}


def Linv(i, j):
    return {i: (-j, i)}


# ---------------------------------------------------------------- C1

def c1():
    a, b, c, d, e, f, g, h, p, q, r, s = sp.symbols("a b c d e f g h p q r s")
    x, y, z = sp.Matrix([[a, b], [c, d]]), sp.Matrix([[e, f], [g, h]]), sp.Matrix([[p, q], [r, s]])
    tr = lambda m: m.trace()
    fricke = sp.expand(tr(x * y) + tr(x * y.adjugate()) - tr(x) * tr(y))
    triple = sp.expand(tr(x * y * z) + tr(x * z * y) - (tr(x) * tr(y * z) + tr(y) * tr(x * z) + tr(z) * tr(x * y)
                                                       - tr(x) * tr(y) * tr(z)))
    x0, y0 = sp.Matrix([[a, b], [c, -a]]), sp.Matrix([[e, f], [g, -e]])
    ch0 = sp.expand(x0 * x0 + x0.det() * sp.eye(2))
    pol = sp.expand(x0 * y0 + y0 * x0 - tr(x0 * y0) * sp.eye(2))
    res = {"Fricke tr(xy) + tr(x adj y) - tr x tr y": str(fricke),
           "triple identity residual": str(triple),
           "Cayley-Hamilton at trace 0, x^2 + det(x) I": str(list(ch0)),
           "polarisation xy + yx - tr(xy) I": str(list(pol))}
    ok = fricke == 0 and triple == 0 and all(v == 0 for v in ch0) and all(v == 0 for v in pol)
    say("C1", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- C2

def c2():
    res, ok = {}, True
    for n in (3, 4):
        bad = {"R": [], "L": []}
        count = 0
        for i, j, k in itertools.permutations(range(1, n + 1), 3):
            count += 1
            lhs = full(Rinv(i, j), n)
            rhs = compose(Rinv(i, k), compose(Rinv(k, j), compose(R(i, k), R(k, j), n), n), n)
            if lhs != rhs:
                bad["R"].append([i, j, k, str(rhs)])
            lhs = full(Linv(i, j), n)
            rhs = compose(Linv(i, k), compose(Linv(k, j), compose(L(i, k), L(k, j), n), n), n)
            if lhs != rhs:
                bad["L"].append([i, j, k, str(rhs)])
        res[f"n = {n}"] = {"ordered triples": count, "R failures": bad["R"][:5], "L failures": bad["L"][:5],
                           "R failure count": len(bad["R"]), "L failure count": len(bad["L"])}
        ok = ok and not bad["R"] and not bad["L"]
    say("C2", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- the trace reducer (n <= 3)

X1, X2, X3, Y12, Y13, Y23, Z = sp.symbols("x1 x2 x3 y12 y13 y23 z")
XS = (X1, X2, X3)
YS = {(1, 2): Y12, (1, 3): Y13, (2, 3): Y23}
P = X1 * Y23 + X2 * Y13 + X3 * Y12 - X1 * X2 * X3
Q = (X1 ** 2 + X2 ** 2 + X3 ** 2 + Y12 ** 2 + Y13 ** 2 + Y23 ** 2 - X1 * X2 * Y12 - X1 * X3 * Y13 - X2 * X3 * Y23
     + Y12 * Y13 * Y23 - 4)
REL = sp.expand(Z ** 2 - P * Z + Q)
MEMO = {}


def T(w):
    """tr of a word in a_1, a_2, a_3 as a polynomial in x_i = tr a_i, y_ij = tr a_i a_j, z = tr a_1 a_2 a_3"""
    w = cyc(w)
    if not w:
        return sp.Integer(2)
    w = min(w[r:] + w[:r] for r in range(len(w)))
    if w in MEMO:
        return MEMO[w]
    neg = [p for p, x in enumerate(w) if x < 0]
    if neg:
        p = neg[0]
        v = w[p + 1:] + w[:p + 1]
        U, a = v[:-1], -v[-1]
        res = XS[a - 1] * T(U) - T(U + (a,))
    else:
        seen, rep = {}, None
        for p, x in enumerate(w):
            if x in seen:
                rep = (seen[x], p)
                break
            seen[x] = p
        if rep:
            p, q = rep
            v = w[p:] + w[:p]
            q -= p
            a, Xw, Yw = v[0], v[1:q], v[q + 1:]
            res = T((a,) + Xw) * T((a,) + Yw) - T(Xw + inv(Yw))
        elif len(w) == 1:
            res = XS[w[0] - 1]
        elif len(w) == 2:
            res = YS[tuple(sorted(w))]
        elif len(w) == 3:
            res = Z if w in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else P - Z
        else:
            raise ValueError(w)
    res = sp.expand(res)
    MEMO[w] = res
    return res


def rand_sl2(rng):
    m = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    return m / np.sqrt(np.linalg.det(m))


def word_matrix(w, g):
    m = np.eye(2, dtype=complex)
    for x in w:
        m = m @ (g[x - 1] if x > 0 else np.linalg.inv(g[-x - 1]))
    return m


# ---------------------------------------------------------------- C3

def c3():
    x, y, z = sp.symbols("x y z")
    eqs = [z - x, y * z - x - z, z - y, x * z - y - z]
    sols = sp.solve(eqs, [x, y, z], dict=True)
    pts = sorted(tuple(int(s[v]) for v in (x, y, z)) for s in sols)
    inv_ok = all((a, b, a * b - c) == (a, b, c) for a, b, c in pts)
    swap_ok = all((b, a, c) == (a, b, c) for a, b, c in pts)
    # the reducer at n = 2 against the hand formulas: R = R_12 (a -> ab), L = L_21 (b -> ab)
    coords = [(1,), (2,), (1, 2)]
    imR = [T(apply(R(1, 2), w)) for w in coords]
    imL = [T(apply(L(2, 1), w)) for w in coords]
    handR = [Y12, X2, sp.expand(X2 * Y12 - X1)]
    handL = [X1, Y12, sp.expand(X1 * Y12 - X2)]
    red_ok = [sp.expand(u - v) for u, v in zip(imR, handR)] == [0] * 3 and \
        [sp.expand(u - v) for u, v in zip(imL, handL)] == [0] * 3
    ok = pts == [(0, 0, 0), (2, 2, 2)] and inv_ok and swap_ok and red_ok
    res = {"fixed points of R and L": pts, "fixed by the inversion": inv_ok, "fixed by the swap": swap_ok,
           "the reducer's R and L equal the hand formulas": red_ok,
           "R by the reducer": [str(u) for u in imR], "L by the reducer": [str(u) for u in imL]}
    say("C3", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- C4

def c4():
    rng = np.random.default_rng(20261020)
    random.seed(20261020)
    VARS = [X1, X2, X3, Y12, Y13, Y23, Z]
    coords = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    # the reducer against matrices
    worst, worst_rel, nwords = 0.0, 0.0, 0
    for _ in range(6):
        g = [rand_sl2(rng) for _ in range(3)]
        val = {v: complex(np.trace(word_matrix(w, g))) for v, w in zip(VARS, coords)}
        worst_rel = max(worst_rel, abs(complex(REL.subs(val))) / (1 + abs(val[Z]) ** 2))
        for _ in range(400):
            ln = random.randint(1, 10)
            w = tuple(random.choice((1, 2, 3)) * random.choice((1, -1)) for _ in range(ln))
            num = complex(np.trace(word_matrix(w, g)))
            poly = complex(T(w).subs(val))
            worst = max(worst, abs(num - poly) / (1 + abs(num)))
            nwords += 1
    reducer_ok = worst < 1e-7 and worst_rel < 1e-7
    say("C4 reducer:", nwords, "random words; worst relative error", f"{worst:.2e}",
        "; the relation of z, worst residual", f"{worst_rel:.2e}")
    pairs = list(itertools.permutations((1, 2, 3), 2))
    sets = {"six R_ij": [R(i, j) for i, j in pairs], "six L_ij": [L(i, j) for i, j in pairs]}
    sets["all twelve"] = sets["six R_ij"] + sets["six L_ij"]
    actions = {}
    for (i, j) in pairs:
        actions[f"R_{i}{j}"] = [str(T(apply(R(i, j), w))) for w in coords]
        actions[f"L_{i}{j}"] = [str(T(apply(L(i, j), w))) for w in coords]
    res = {"random words": nwords, "worst relative error": worst, "relation residual": worst_rel,
           "the moves on (x1, x2, x3, y12, y13, y23, z)": actions, "move sets": {}}
    ok = reducer_ok
    for name, moves in sets.items():
        eqs = [REL]
        for phi in moves:
            eqs += [sp.expand(T(apply(phi, w)) - v) for v, w in zip(VARS, coords)]
        eqs = [e for e in eqs if e != 0]
        G = sp.groebner(eqs, *VARS, order="lex")
        sols = sp.solve(list(G.exprs), VARS, dict=True)
        pts = sorted(tuple(str(s.get(v, v)) for v in VARS) for s in sols)
        good = pts == [tuple("2" for _ in VARS)]
        res["move sets"][name] = {"equations": len(eqs), "Groebner basis": [str(b) for b in G.exprs],
                                  "points": pts, "only (2, ..., 2)": good}
        say("C4", name, ":", len(eqs), "equations; Groebner basis", [str(b) for b in G.exprs], "; points", pts)
        ok = ok and good
    # the proof's t = 0 frames: on the variety, and moved by R_12
    frames = {}
    for zz in (2, -2):
        pt = {X1: 0, X2: 0, X3: 0, Y12: 0, Y13: 0, Y23: 0, Z: zz}
        on = REL.subs(pt) == 0
        img = [T(apply(R(1, 2), w)).subs(pt) for w in coords]
        frames[f"z = {zz}"] = {"on the variety": bool(on), "image under R_12": [str(u) for u in img],
                               "moved": img != [pt[v] for v in VARS]}
    res["the t = 0 frames"] = frames
    fr_ok = all(f["on the variety"] and f["moved"] for f in frames.values())
    ok = ok and fr_ok
    say("C4 frames:", frames)
    say("C4", "held" if ok else "FAILED")
    return ok, res


# ---------------------------------------------------------------- C5

def perm_mul(a, b):
    """(a b)(x) = a(b(x))"""
    return a[b]


def perm_inv(a):
    out = np.empty_like(a)
    out[a] = np.arange(len(a))
    return out


def closure(gens, n):
    ident = tuple(range(n))
    S = {ident}
    fr = [np.arange(n)]
    gens = [np.asarray(g) for g in gens]
    while fr:
        nx = []
        for x in fr:
            for g in gens:
                y = perm_mul(g, x)
                t = tuple(int(v) for v in y)
                if t not in S:
                    S.add(t)
                    nx.append(y)
        fr = nx
    return S


def derived(S, n):
    arr = [np.array(s) for s in S]
    comms = set()
    for a in arr:
        ai = perm_inv(a)
        for b in arr:
            c = perm_mul(perm_mul(a, b), perm_mul(ai, perm_inv(b)))
            comms.add(tuple(int(v) for v in c))
    return closure([np.array(c) for c in comms], n)


def c5():
    i_, j_, w_ = (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.5, 0.5, 0.5, 0.5)
    u_ = (W108.PHI / 2, 1 / (2 * W108.PHI), 0.5, 0.0)
    o_ = (1 / math.sqrt(2), 1 / math.sqrt(2), 0.0, 0.0)
    groups = {"Q8": ([i_, j_], 24, 4), "2T": ([i_, w_], 24, 12), "2O": ([i_, w_, o_], 48, 24),
              "2I": ([i_, w_, u_], 120, 60)}
    for m in range(3, 13):
        groups[f"Dic_{m}"] = ([(math.cos(math.pi / m), math.sin(math.pi / m), 0.0, 0.0), j_],
                              2 * m * int(sp.totient(2 * m)), 2 * m)
    res, ok = {}, True
    for name, (gens, want_aut, want_inn) in groups.items():
        G = W108.Group(W108.quat_closure(gens), name)
        pair = next((s, t) for s in range(G.N) for t in range(G.N) if len(G.gen([s, t])) == G.N)
        auts = W108.automorphisms(G, *pair)
        inns = W108.inner(G)
        A = {tuple(int(v) for v in m) for m in auts}
        I = {tuple(int(v) for v in m) for m in inns}
        series, D, solvable, abelian_out = [len(A)], A, False, False
        for k in range(8):
            if D <= I:
                solvable = True
                abelian_out = (k <= 1)
                break
            D2 = derived(D, G.N)
            if D2 == D:
                break
            D = D2
            series.append(len(D))
        row = {"order": G.N, "|Aut|": len(A), "|Inn|": len(I), "|Out|": len(A) // max(len(I), 1),
               "Inn inside Aut": I <= A, "derived series of Aut (orders)": series,
               "Out solvable": solvable, "Out abelian": abelian_out,
               "|Aut| as expected": len(A) == want_aut, "|Inn| as expected": len(I) == want_inn}
        res[name] = row
        say("C5", name, row)
        ok = ok and solvable and I <= A
    orders_ok = all(r["|Aut| as expected"] and r["|Inn| as expected"] for r in res.values())
    say("C5 solvability", "held" if ok else "FAILED", "; the orders", "held" if orders_ok else "FAILED")
    return ok, orders_ok, res


def main():
    out = {"status": "one run", "proof": "W109_PROOF.md (2d10142d3)", "cells": {}}
    for name, fn in (("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4)):
        ok, res = fn()
        out["cells"][name] = bool(ok)
        out[name] = res
    ok, orders_ok, res = c5()
    out["cells"]["C5 solvability"] = bool(ok)
    out["cells"]["C5 orders"] = bool(orders_ok)
    out["C5"] = res
    say("cells:", out["cells"])
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    RUN.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
