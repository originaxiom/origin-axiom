"""B1879, a dated addition (2026-11-11): which short histories fix exactly the two universal characters?

The advisor seat checked B1879 with its own code (its verify_b1879/ @ 7726eeed) and put one question more, post hoc: every
history fixes the trivial character and the quaternion point; which histories fix nothing else?  Its answer: among the
thirteen histories of at most five letters in the grammar of L (add) and F (the tick), the tick alone.  This is main's own
check of that answer.  Exact: Groebner bases over the rationals in the traces (x, y, z) = (tr a, tr b, tr ab).

    L: a -> a,  b -> ab      (x, y, z) -> (x, z, xz - y)
    F: a -> ab, b -> a       (x, y, z) -> (z, x, xz - y)

A history is a cyclic word in L and F with at least one F that is not a power of a shorter word.  Words related by a cyclic
shift give conjugate maps, whose fixed sets correspond under an invertible map of the trace space; so one word a class.
"""
import itertools
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
x, y, z = sp.symbols("x y z")
MAPS = {"L": (x, z, x * z - y), "F": (z, x, x * z - y)}
TWO = {(2, 2, 2), (0, 0, 0)}


def apply(word, p):
    """the trace map of the word, letters applied left to right"""
    for ch in word:
        m = MAPS[ch]
        p = tuple(sp.expand(q.subs({x: p[0], y: p[1], z: p[2]}, simultaneous=True)) for q in m)
    return p


def classes(nmax):
    seen, out = set(), []
    for n in range(1, nmax + 1):
        for w in itertools.product("LF", repeat=n):
            w = "".join(w)
            if "F" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0):
                continue
            rep = min(w[i:] + w[:i] for i in range(n))
            if rep not in seen:
                seen.add(rep); out.append(rep)
    return out


def fixed(word):
    """('finite', the set of points) or ('positive dimension', None) for the characters the word's trace map fixes"""
    p = apply(word, (x, y, z))
    eqs = [sp.expand(p[0] - x), sp.expand(p[1] - y), sp.expand(p[2] - z)]
    G = sp.groebner(eqs, x, y, z, order="lex")
    if not G.is_zero_dimensional:
        return "positive dimension", None
    sols = sp.solve(eqs, [x, y, z], dict=True)
    return "finite", {tuple(sp.nsimplify(s[v]) for v in (x, y, z)) for s in sols}


def main():
    out = []
    P = lambda *a: (out.append(" ".join(str(q) for q in a)), print(*a))
    P("WHICH HISTORIES OF AT MOST FIVE LETTERS FIX EXACTLY THE TRIVIAL CHARACTER AND THE QUATERNION POINT?")
    ws = classes(5)
    P("histories (cyclic words in L and F with at least one F, not a power): %d" % len(ws))
    only, extra, curve = [], [], []
    for w in ws:
        kind, pts = fixed(w)
        ticks = w.count("F")
        if kind == "finite":
            assert TWO <= {tuple(int(v) if v.is_integer else v for v in q) for q in pts} or TWO <= pts, (w, pts)
            rest = sorted(str(q) for q in pts if q not in TWO)
            (only if not rest else extra).append(w)
            P("   %-6s (%d tick%s): finitely many, %d; besides the two: %s" % (w, ticks, "" if ticks == 1 else "s", len(pts), ", ".join(rest) or "none"))
        else:
            # the two are still fixed: check by substitution
            p = apply(w, (x, y, z))
            assert all(tuple(q.subs({x: a, y: b, z: c}) for q in p) == (a, b, c) for (a, b, c) in TWO)
            curve.append(w)
            P("   %-6s (%d tick%s): a set of positive dimension" % (w, ticks, "" if ticks == 1 else "s"))
    P("")
    P("exactly the two: %s" % ", ".join(only))
    P("the two and finitely many more: %s" % (", ".join(extra) or "none"))
    P("a set of positive dimension: %d of %d" % (len(curve), len(ws)))
    ok = only == ["F"]
    P("the tick alone is the only history of at most five letters that fixes exactly the two: %s" % ok)
    (HERE / "only_the_tick_run.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    return ok, len(ws), only, extra, len(curve)


if __name__ == "__main__":
    raise SystemExit(0 if main()[0] else 1)
