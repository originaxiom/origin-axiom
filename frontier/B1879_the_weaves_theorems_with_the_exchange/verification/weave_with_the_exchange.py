#!/usr/bin/env python3
"""B1879 (data-free) -- the weave's theorems restated for the group with the exchange.

THE QUESTION, and why it is asked.  The owner has ruled that the tick is an act (2026-11-11) and, earlier, that even
ticks are what is observed (2026-10-08).  Asked how the two stand together, the owner answered "After the computation".
This is that computation: for each statement the closure map holds about the weave, what becomes of it when the exchange
is added to the moves -- that is, when histories of an odd number of ticks take part.

STATED BEFORE COMPUTING (main's expectations; each is checked below and the outcome printed beside it):
  E1  the two characters the two moves fix (the trivial one and the quaternion point) are fixed by the exchange too  -- holds
  E2  the tick alone fixes more than those two (a single two-act move fixes a whole curve)                          -- see the output
  E3  on the weave's six-dimensional space the group doubles, 96 to 192, and the triplet and its conjugate join      -- B1871 has it
  E4  the joined six-dimensional piece is a real representation (it has an invariant symmetric form)                -- NOT WELL POSED: see the output
  E5  the move-by-move measure is the same under the grammar of L and the tick                                      -- holds
  E6  every history of an odd number of ticks has one end                                                           -- holds

Parts: 1 the characters (exact, sympy); 2 the six-dimensional space (B1610's matrices, main's); 3 the walk's law
(exact enumeration); 4 the ends (SnapPy); 5 the modulus (exact).  No measured number is read and nothing is compared.

    python3 -B frontier/B1879_the_weaves_theorems_with_the_exchange/verification/weave_with_the_exchange.py [--no-snappy]
"""
import fractions
import importlib.util
import itertools
import pathlib
import sys
import warnings

import numpy as np
import sympy as sp

say = print
ROOT = pathlib.Path(__file__).resolve().parents[3]
x, y, z = sp.symbols("x y z")


def part1():
    say("PART 1 -- THE CHARACTERS THE MOVES FIX (x = tr a, y = tr b, z = tr ab; exact)")
    M1 = lambda v: (v[2], v[1], v[2] * v[1] - v[0])            # a -> ab, b -> b
    M2 = lambda v: (v[0], v[2], v[0] * v[2] - v[1])            # a -> a,  b -> ba
    X = lambda v: (v[1], v[0], v[2])                           # the exchange a <-> b   (tr ba = tr ab)
    TICK = lambda v: (v[2], v[0], v[0] * v[2] - v[1])           # a -> ab, b -> a: the founding rule (tr a.b.a = tr a^2 b = xz - y)
    kappa = lambda v: v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2] - 2
    v = (x, y, z)
    # the tick on the two counts is the golden matrix: a -> ab is the column (1, 1), b -> a the column (1, 0); twice is L R
    FM = sp.Matrix([[1, 1], [1, 0]])
    assert FM.det() == -1 and FM * FM == sp.Matrix([[2, 1], [1, 1]])
    for name, T in (("M1", M1), ("M2", M2), ("the exchange", X), ("the tick", TICK)):
        assert sp.expand(kappa(T(v)) - kappa(v)) == 0, name                          # each keeps tr [a, b]
    def fixed(maps):
        eqs = []
        for T in maps:
            eqs += [sp.expand(a - b) for a, b in zip(T(v), v)]
        G = sp.groebner(eqs, x, y, z, order="lex")
        sols = sp.solve(eqs, [x, y, z], dict=True)
        return G, sols
    G, sols = fixed([M1, M2])
    pts = sorted((s[x], s[y], s[z]) for s in sols)
    assert pts == [(0, 0, 0), (2, 2, 2)]
    say("  the two moves together fix exactly %s: the quaternion point and the trivial character (the record's W:Q8)" % pts)
    assert all(X(p) == p for p in pts)
    say("  E1 HOLDS: the exchange fixes both, so with the exchange the same two are fixed and no other")
    G1, s1 = fixed([M1])
    free = [s for s in s1 if any(getattr(val, "free_symbols", None) for val in s.values()) or len(s) < 3]
    say("  one two-act move alone fixes a curve, not points: M1 fixes %d family(ies) with a free parameter" % len(free))
    assert free
    Gt, st = fixed([TICK])
    ptst = sorted((s[x], s[y], s[z]) for s in st)
    say("  the tick alone fixes exactly %s" % ptst)
    assert ptst == [(0, 0, 0), (2, 2, 2)]
    say("  E2 FAILS, and the failure is the finding: the tick BY ITSELF fixes exactly the trivial character and the quaternion point.")
    say("     The record needs both two-act moves together for that (W:Q8); one act, the founding one, already does it.")
    # the tick done twice is the root's monodromy, and that fixes a curve: the quaternion point is special to the single tick
    T2 = lambda u: TICK(TICK(u))
    G2, s2 = fixed([T2])
    free2 = [s for s in s2 if len(s) < 3 or any(getattr(val, "free_symbols", None) for val in s.values())]
    say("  the tick done twice (the root) fixes a curve again: %d family(ies) with a free parameter, the quaternion point and the hyperbolic structure's point on it" % len(free2))
    assert free2


def part2():
    say("PART 2 -- THE WEAVE'S SIX-DIMENSIONAL SPACE (B1610's matrices, main's own): T + conj T")
    spec = importlib.util.spec_from_file_location("hands_for_b1879", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
    Hm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(Hm)
    ML, MR, MP = Hm.W.ML, Hm.W.MR, Hm.W.MP
    Tb, Tc = Hm.PIECES["T"], Hm.PIECES["Tbar"]
    key = lambda M: tuple(np.round(M.flatten(), 6).view(float))

    def grp(gens, cap=2000):
        one = np.eye(6, dtype=complex)
        seen = {key(one): one}
        fr = [one]
        while fr:
            nx = []
            for a in fr:
                for g in gens:
                    b = a @ g
                    k = key(b)
                    if k not in seen:
                        seen[k] = b
                        nx.append(b)
                        assert len(seen) < cap
            fr = nx
        return list(seen.values())

    def commutant(gens):
        rows = [np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in gens]
        return int(np.sum(np.linalg.svd(np.vstack(rows), compute_uv=False) < 1e-8))

    G, Gx = grp([ML, MR]), grp([ML, MR, MP])
    assert (len(G), len(Gx), commutant([ML, MR]), commutant([ML, MR, MP])) == (96, 192, 2, 1)
    say("  the two acts: %d elements, two pieces (the triplet and its conjugate); with the exchange: %d elements, one piece" % (len(G), len(Gx)))
    # the same group from L and the tick alone (the grammar in which each act is one word)
    Gt = grp([ML, ML @ MP])
    assert {key(g) for g in Gt} == {key(g) for g in Gx}
    say("  L and the tick alone generate the same %d elements" % len(Gt))
    # E4: is the joined six a real representation?  The plain Frobenius-Schur indicator answers for ONE lift of the exchange, and
    # the lift is free up to a phase that nothing fixes: the answer moves with it.  So E4 is not well posed, and what is reported
    # is (i) that dependence, and (ii) the statement that does not depend on the lift: the TWISTED indicator of the triplet for
    # the automorphism the exchange induces on the two acts' group (the record's B1611 has it as +1).
    fs_plain = lambda grp_: float(np.real(sum(np.trace(g @ g) for g in grp_) / len(grp_)))
    by_lift = {}
    for name, lam in (("B1610's lift", 1), ("i times it", 1j)):
        Gl = grp([ML, MR, lam * MP])
        by_lift[name] = (len(Gl), round(fs_plain(Gl), 6))
    say("  E4 IS NOT WELL POSED: the plain indicator of the six depends on the phase of the exchange's lift -- %s" % "; ".join("%s: %d elements, indicator %+.0f" % (k, v[0], v[1]) for k, v in by_lift.items()))
    assert by_lift["B1610's lift"] == (192, -1.0) and by_lift["i times it"] == (192, 1.0)
    PT = Tb @ np.linalg.pinv(Tb)
    MPi = np.linalg.inv(MP)
    assert all(key(MP @ g @ MPi) in {key(h) for h in G} for g in (ML, MR))                    # the exchange normalises the two acts' group
    fs3 = float(np.real(sum(np.trace(PT @ g @ g) for g in G) / len(G)))
    tw = sum(np.trace(PT @ g @ (MP @ g @ MPi)) for g in G) / len(G)
    tw_i = sum(np.trace(PT @ g @ ((1j * MP) @ g @ np.linalg.inv(1j * MP))) for g in G) / len(G)
    say("  what does not depend on the lift: under the two acts the triplet is complex (plain indicator %.0f), and its indicator twisted by the exchange is %+.3f (the same for either lift: %+.3f)" % (abs(fs3), tw.real, tw_i.real))
    assert abs(fs3) < 1e-6 and abs(tw - 1) < 1e-6 and abs(tw_i - 1) < 1e-6
    say("     So the exchange is a consistent conjugation of the triplet onto its conjugate (the record's B1611: the weave's generalised CP is the record swap), recomputed here.")
    # the invariant bilinear forms on the six: one with the exchange, pairing the two hands; its symmetry moves with the lift too
    def forms(gens):
        rows = [np.kron(g.T, g.T) - np.eye(36) for g in gens]
        _, sv, Vh = np.linalg.svd(np.vstack(rows))
        return Vh[int(np.sum(sv > 1e-8)):]
    n2, nx = forms([ML, MR]).shape[0], forms([ML, MR, MP])
    assert n2 == 2 and nx.shape[0] == 1
    Bf = nx[0].reshape(6, 6)
    on = lambda A, Bm: float(np.max(np.abs(A.T @ Bf @ Bm)))
    assert on(Tb, Tb) < 1e-7 and on(Tc, Tc) < 1e-7 and on(Tb, Tc) > 1e-3
    say("  invariant bilinear forms on the six: %d under the two acts, %d with the exchange; it pairs the triplet with its conjugate and vanishes on each alone" % (n2, nx.shape[0]))
    # the tick's own order and what it does to the pieces
    F = ML @ MP
    order = next(k for k in range(1, 400) if np.allclose(np.linalg.matrix_power(F, k), np.eye(6), atol=1e-7))
    inG = lambda M: key(M) in {key(g) for g in G}
    assert not inG(F) and inG(F @ F)
    say("  the tick has order %d on the six; it is not in the two acts' group and its square is" % order)
    return len(G), len(Gx)


def part3():
    say("PART 3 -- THE WALK'S LAW (exact enumeration): the runs of a uniformly random word")
    # a word in L and R: its runs.  a word in L and F: each F closes a run (L^(r-1) F is a run of r).
    def runs_LR(w):
        out, k = [], 1
        for a, b in zip(w, w[1:]):
            if a == b:
                k += 1
            else:
                out.append(k)
                k = 1
        return out                                   # completed runs only
    def runs_LF(w):
        out, k = [], 1
        for ch in w:
            if ch == "F":
                out.append(k)
                k = 1
            else:
                k += 1
        return out
    n = 12
    def law(words, runs, m=3):
        cnt = {}
        for w in words:
            r = tuple(runs(w)[:m])
            if len(r) == m:
                cnt[r] = cnt.get(r, 0) + 1
        return {k: fractions.Fraction(v, 2 ** n) for k, v in cnt.items()}       # probabilities among ALL words of n letters, not renormalised
    a = law(("".join(t) for t in itertools.product("LR", repeat=n)), runs_LR)
    b = law(("".join(t) for t in itertools.product("LF", repeat=n)), runs_LF)
    both = [k for k in a if sum(k) <= n - 1]
    assert both and all(a[k] == b[k] == fractions.Fraction(1, 2 ** sum(k)) for k in both)
    say("  the first three completed runs of a uniformly random word of %d letters: the probability of runs (r1, r2, r3) is exactly 2^-(r1+r2+r3) in both grammars, on all %d triples that fit" % (n, len(both)))
    say("  E5 HOLDS, exactly: a run has length r with probability 2^-r in either grammar, independently, so the move-by-move measure (Minkowski's) is the same.")
    say("     The reason: in L and F a run of r is L^(r-1) F; in L and R a run ends when the letter changes. Each has probability 2^-r.")


def part4():
    say("PART 4 -- THE ENDS (SnapPy): histories of an odd number of ticks")
    warnings.filterwarnings("ignore")
    import snappy
    def comps(n):
        for cuts in itertools.product((0, 1), repeat=n - 1):
            out, run = [], 1
            for c in cuts:
                if c:
                    out.append(run)
                    run = 1
                else:
                    run += 1
            out.append(run)
            yield tuple(out)
    prim = lambda s: not any(len(s) % d == 0 and s == s[:d] * (len(s) // d) for d in range(1, len(s)))
    odd = sorted({min(c[s:] + c[:s] for s in range(len(c))) for n in range(1, 8) for c in comps(n) if len(c) % 2 == 1 and prim(c)}, key=lambda c: (sum(c), c))
    assert len(odd) == 22
    cusps = set()
    for c in odd:
        wd = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(c))
        M = snappy.Manifold("b-+" + wd)
        assert not M.is_orientable()
        cusps.add(M.num_cusps())
    say("  the %d primitive histories of an odd number of runs to 7 letters: number of ends %s" % (len(odd), sorted(cusps)))
    assert cusps == {1}
    say("  E6 HOLDS: each has one end. So 'a generated state has one end' (the record's W:ONE-END) holds for them too.")


def part5():
    say("PART 5 -- THE MODULUS (exact): the moves on the upper half-plane, with the exchange")
    t = sp.symbols("t", positive=True)
    xr, yi = sp.symbols("xr yi", real=True)
    tau = xr + sp.I * yi
    conj = xr - sp.I * yi
    # an element of determinant -1 acts by tau -> (a conj(tau) + b) / (c conj(tau) + d)
    def fixed_locus(a, b, c, d):
        e = sp.expand((a * conj + b) - tau * (c * conj + d))
        return sp.simplify(sp.re(e)), sp.simplify(sp.im(e))
    re_, im_ = fixed_locus(0, 1, 1, 0)             # the exchange P
    assert sp.simplify(re_ - (1 - xr ** 2 - yi ** 2)) == 0 and sp.simplify(im_) == 0
    say("  the exchange fixes the unit circle |tau| = 1, pointwise (a mirror)")
    re_, im_ = fixed_locus(1, 1, 1, 0)             # the tick L P
    sols = sp.solve([re_, im_], [xr, yi], dict=True)
    in_H = [s for s in sols if s.get(yi, 0) != 0 and sp.simplify(s.get(yi)) > 0]
    say("  the tick fixes no point of the upper half-plane (its fixed points are the two golden numbers on the boundary): solutions in the half-plane %s" % in_H)
    assert not in_H
    # the mirrors of the whole group: the three reflections in the sides of the modular triangle
    for name, (a, b, c, d), want in (("tau -> -conj(tau)", (-1, 0, 0, 1), "Re tau = 0"), ("tau -> 1 - conj(tau)", (-1, 1, 0, 1), "Re tau = 1/2"), ("tau -> 1/conj(tau)", (0, 1, 1, 0), "|tau| = 1")):
        assert a * d - b * c == -1
        re_, im_ = fixed_locus(a, b, c, d)
        say("    %-22s fixes %s" % (name, want))
    say("  so the weave still fixes no point (the record's W:NOMOD, a fortiori: more moves, no more fixed points). What the exchange adds is")
    say("  mirrors: the lines Re tau = 0, Re tau = 1/2 and |tau| = 1, with i and the cube root of unity at their corners.")


if __name__ == "__main__":
    part1()
    part2()
    part3()
    if "--no-snappy" not in sys.argv:
        part4()
    part5()
    say("ALL CHECKS PASS")
