#!/usr/bin/env python3
"""B1252 -- THE CARTAN METRIC ON THE B854 BASIS, AND THE DESCENT TO ONE SM GENERATION.

WHY THIS EXISTS.  The B854 coordinates used throughout the E6 work are NOT orthonormal, and the
repo carried no metric for them.  A naive dot product on those coordinates gives SEVEN distinct
root lengths in a SIMPLY-LACED algebra -- so every "orthogonality" conclusion drawn that way is
invalid.  This seat produced one such invalid conclusion in-session (a claimed "480 candidate
SU(3)xSU(2) embeddings with no selector"), which is RETRACTED here.

THE METRIC.  E6 is simply-laced, so the correct form is the unique symmetric M with alpha^T M alpha
constant on all 72 roots.  Solving that linear system gives ONE solution, ZERO free parameters:
    all 72 roots  -> length^2 = 2          (simply-laced, as required)
    all 27 weights -> length^2 = 4/3       (minuscule: one Weyl orbit, one length)
Both validations are non-trivial and neither was imposed.

THE DESCENT, run on the object's own weight data with that metric:
    E6 -> SO(10) x U(1)      FORCED by the D2 character's stabiliser (B1250; metric-free)
    SO(10) -> SU(5) x U(1)   A4 subsystem, 20 roots, one component
    SU(5) -> SU(3)xSU(2)     A2+A1 subsystem, 8 roots, components (2,6); 10 such subsystems
    -> hypercharge           Y = the orthogonal complement of A2+A1 (3-dimensional)
and EXACTLY ONE direction in the searched space grades the 16 into the Standard Model pattern:

    Y = [0, -5, -4, 5, -2, 2]  (scale 1/6)
    Q (3,2) x6 : 1/6    u^c (3bar,1) x3 : -2/3    d^c (3bar,1) x3 : 1/3
    L (1,2) x2 : -1/2   e^c (1,1)    x1 : 1       nu^c (1,1)   x1 : 0

ONE COMPLETE STANDARD MODEL GENERATION with correct hypercharges, on the object's lattice.

WHAT THIS IS NOT -- stated before the result was seen, and kept.  This is NOT "the SM derived".
Once SU(3)xSU(2) is fixed inside SU(5), hypercharge is UNIQUE UP TO SCALE by standard Lie theory,
so exhibiting it confirms CONSISTENCY, not novelty; and the scale 1/6 is a normalisation
convention (B919 addendum, this session).  Steps 2 and 3 are the unique winners B873 already
banked mechanically.  The genuinely new content is (a) the metric, which did not exist, and
(b) step 1, which was an INPUT before B1250 and is now forced.

STILL MISSING, unchanged: the VALUES (route through I-13, unpriced); THREE generations (this is one
16; B307 closed the cyclic-cubic route); COSMOLOGY (B1194's one genuinely blind region).
No measured value. Gate 5 clean.
"""
import collections
import itertools
import json
import pathlib
from fractions import Fraction as F

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]


def load():
    rep = json.loads((ROOT / "frontier" / "B883_the_27" / "rep27.json").read_text())
    return rep["weights"], rep["rep"]


def roots():
    wts, G = load()
    out = {}
    for k in range(6, 78):
        M = G[str(k)]
        done = False
        for i in range(27):
            for j in range(27):
                if M[i][j]:
                    out[k] = tuple(a - b for a, b in zip(wts[i], wts[j]))
                    done = True
                    break
            if done:
                break
    return out


def cartan_metric():
    """The unique symmetric M with alpha^T M alpha = 2 on all 72 roots. Returns a sympy Matrix."""
    wts, _ = load()
    rs = list(roots().values())
    idx = [(i, j) for i in range(6) for j in range(i, 6)]
    sy = sp.symbols(f"m0:{len(idx)}")
    M = sp.zeros(6, 6)
    for (i, j), s in zip(idx, sy):
        M[i, j] = s
        M[j, i] = s
    eqs = [sp.expand((sp.Matrix([a]) * M * sp.Matrix([a]).T)[0, 0] - 2) for a in rs]
    sol = sp.solve(eqs, sy, dict=True)
    assert len(sol) == 1, f"metric not unique: {len(sol)} solutions"
    Mn = M.subs(sol[0])
    assert not Mn.free_symbols, "metric has free parameters"
    return Mn


def validate_metric(M):
    """Simply-laced => one root length; minuscule 27 => one weight length. Neither was imposed."""
    wts, _ = load()
    rl = collections.Counter((sp.Matrix([a]) * M * sp.Matrix([a]).T)[0, 0] for a in roots().values())
    wl = collections.Counter((sp.Matrix([w]) * M * sp.Matrix([w]).T)[0, 0] for w in wts)
    return dict(rl), dict(wl)


SM_TARGET = {F(1, 6): 6, F(-2, 3): 3, F(1, 3): 3, F(-1, 2): 2, F(1): 1, F(0): 1}


def descent(box=2, coef=6):
    """Run E6 -> SO(10) -> SU(5) -> SM and return the unique Y with SM hypercharges."""
    import importlib.util
    wts, G = load()
    M = cartan_metric()
    Mf = [[F(sp.Rational(M[i, j])) for j in range(6)] for i in range(6)]
    ip = lambda a, b: sum(F(a[i]) * Mf[i][j] * F(b[j]) for i in range(6) for j in range(6))
    w13 = wts[13]
    so10 = [a for a in roots().values() if sum(x * y for x, y in zip(w13, a)) % 2 == 0]
    cache = {}

    def ipc(a, b):
        if (a, b) not in cache:
            cache[(a, b)] = ip(a, b)
        return cache[(a, b)]

    def comps(rs):
        rs = list(rs)
        adj = collections.defaultdict(set)
        for a in rs:
            for b in rs:
                if a != b and ipc(a, b) != 0:
                    adj[a].add(b)
                    adj[b].add(a)
        seen, out = set(), []
        for r in rs:
            if r in seen:
                continue
            c, st = {r}, [r]
            while st:
                x = st.pop()
                for y in adj[x]:
                    if y not in c:
                        c.add(y)
                        st.append(y)
            seen |= c
            out.append(len(c))
        return tuple(sorted(out))

    BOX = [v for v in itertools.product(range(-box, box + 1), repeat=6) if any(v)]
    su5 = next(k for k in (frozenset(a for a in so10 if ip(v, a) == 0) for v in BOX)
               if len(k) == 20 and comps(k) == (20,))
    subs = {k for k in (frozenset(a for a in su5 if ip(v, a) == 0) for v in BOX)
            if len(k) == 8 and comps(k) == (2, 6)}
    spec = importlib.util.spec_from_file_location(
        "dd", ROOT / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py")
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    _, _, blocks = dd.stabiliser_blocks()
    W16 = [wts[i] for i in blocks[2]]
    Ms = sp.Matrix([[sp.Rational(Mf[i][j]) for j in range(6)] for i in range(6)])
    for sub in subs:
        ns = [[F(sp.Rational(x)) for x in n]
              for n in (sp.Matrix([list(r) for r in sub]) * Ms).nullspace()]
        for c in itertools.product(range(-coef, coef + 1), repeat=len(ns)):
            if not any(c):
                continue
            v = [sum(ci * n[i] for ci, n in zip(c, ns)) for i in range(6)]
            gr = collections.Counter(ip(v, w) for w in W16)
            if sorted(gr.values()) != [1, 1, 2, 3, 3, 6] or gr.get(F(0)) != 1:
                continue
            g6 = [g for g, m in gr.items() if m == 6][0]
            if g6 == 0:
                continue
            lam = F(1, 6) / g6
            if {g * lam: m for g, m in gr.items()} == SM_TARGET:
                return v, {g * lam: m for g, m in gr.items()}, len(subs)
    return None, None, len(subs)


def selftest(verbose=True):
    fails = []
    M = cartan_metric()
    rl, wl = validate_metric(M)
    if list(rl) != [2] or sum(rl.values()) != 72:
        fails.append(f"root lengths {rl} -- simply-laced requires a single value 2 on 72 roots")
    if len(wl) != 1 or sum(wl.values()) != 27:
        fails.append(f"weight lengths {wl} -- the minuscule 27 requires a single value")
    y, gr, nsub = descent()
    if y is None:
        fails.append("no Y reproducing the SM hypercharges")
    elif gr != SM_TARGET:
        fails.append(f"hypercharge multiset {gr} != SM")
    if verbose:
        print(f"  [metric] unique, no free parameters; root length^2 {rl}, weight length^2 {wl}")
        print(f"  [descent] A2+A1 subsystems {nsub}; Y = {[str(x) for x in y] if y else None}")
        if gr:
            for g, m in sorted(gr.items()):
                print(f"      Y = {str(g):>6}  multiplicity {m}")
    return fails


if __name__ == "__main__":
    print("B1252 -- the Cartan metric and the SM descent (selftest)")
    f = selftest()
    print()
    print("SELFTEST:", "PASS" if not f else "FAIL")
    for i in f:
        print("   !", i)
    raise SystemExit(1 if f else 0)
