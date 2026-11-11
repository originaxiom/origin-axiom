#!/usr/bin/env python3
"""An addition by the advisor seat to its check of B1879, written after that check ran (post hoc, labelled).

B1879: "the tick alone fixes exactly two characters: the trivial one and the quaternion point", and "it is special to
the single tick". Question put here: among histories, which fix ONLY those two? Every history fixes both (they are
fixed by both moves and by the exchange). Exact: Groebner bases over the rationals.
    python3 -B which_histories_fix_only_the_two.py"""
import itertools, pathlib
import sympy as sp
x, y, z = sp.symbols("x y z")
LAM = lambda v: (v[0], v[2], sp.expand(v[0] * v[2] - v[1]))        # a -> a,  b -> ab      (add)
TK  = lambda v: (v[2], v[0], sp.expand(v[0] * v[2] - v[1]))        # a -> ab, b -> a       (add, and the sides change roles)
out = []
def say(s=""):
    out.append(s); print(s, flush=True)
def trace_map(word):                    # a word in L (add) and F (the tick), applied letter by letter
    v = (x, y, z)
    for ch in word: v = (LAM if ch == "L" else TK)(v)
    return v
def fixed(word):
    w = trace_map(word)
    eqs = [e for e in (sp.expand(w[0] - x), sp.expand(w[1] - y), sp.expand(w[2] - z)) if e != 0]
    G = sp.groebner(eqs, x, y, z, order="lex")
    if not G.is_zero_dimensional: return None
    pts = set()
    for s in sp.solve(eqs, [x, y, z], dict=True):
        pts.add(tuple(sp.nsimplify(sp.simplify(s.get(q, q))) for q in (x, y, z)))
    return pts
def necklaces(n):
    seen = set()
    for w in itertools.product("LF", repeat=n):
        w = "".join(w); k = min(w[i:] + w[:i] for i in range(n))
        if k in seen or "F" not in w: continue
        seen.add(k)
        if any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n)): continue
        yield k
say("which histories fix only the trivial character (2,2,2) and the quaternion point (0,0,0)?")
say("a history is a cyclic word in L (add) and F (the tick); 'odd' = an odd number of ticks")
say("%-8s %-5s %-34s %s" % ("word", "ticks", "its fixed characters", "only the two?"))
only = []
for n in range(1, 6):
    for w in necklaces(n):
        m = w.count("F"); pts = fixed(w)
        if pts is None:
            say("%-8s %-5s %-34s %s" % (w, "odd" if m % 2 else "even", "a set of positive dimension", "no"))
        else:
            two = pts == {(0, 0, 0), (2, 2, 2)}
            if two: only.append(w)
            say("%-8s %-5s %-34s %s" % (w, "odd" if m % 2 else "even", "%d point(s)%s" % (len(pts), "" if len(pts) > 4 else ": " + str(sorted(pts, key=str))), "YES" if two else "no"))
say("\nhistories of at most 5 letters that fix only the two: %s" % only)
pathlib.Path(__file__).with_name("which_histories_fix_only_the_two_out.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
