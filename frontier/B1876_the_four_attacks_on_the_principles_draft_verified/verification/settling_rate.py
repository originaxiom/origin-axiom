#!/usr/bin/env python3
"""B1876, main's addition (POST HOC, labelled; data-free) -- how fast a departure's own invariants settle in a long golden ground.

The advisor seat reported, post hoc, that the Chern-Simons invariant of the run of 6 settles as periods of the ground are
added, each step "about 4.79 times smaller than the one before", and claimed nothing for the number.  Main asks what 4.79 is.

  EXACT   the root's monodromy acts on the characters of the fibre's group, (x, y, z) = (tr a, tr b, tr ab).  Its fixed
          points form a curve; the point of that curve where the puncture is parabolic (tr [a, b] = -2) is the hyperbolic
          structure's.  The derivative of the action there has characteristic polynomial (t - 1)(t^2 - 5t + 1).
  SEEN    for three departures the steps of the excess volume and of the Chern-Simons invariant shrink by a ratio that
          tends to the larger root, (5 + sqrt 21)/2 = 4.791288.

The exact part is a computation.  That the ratio of settling IS that eigenvalue is observed to four digits on three
departures and is not proved here.

    python3 -B frontier/B1876_the_four_attacks_on_the_principles_draft_verified/verification/settling_rate.py [--no-snappy]
"""
import sys
import warnings

import sympy as sp

say = print
x, y, z, t = sp.symbols("x y z t")
T1 = lambda v: (v[2], v[1], v[2] * v[1] - v[0])                   # a -> ab, b -> b   on (tr a, tr b, tr ab)
T2 = lambda v: (v[0], v[2], v[0] * v[2] - v[1])                   # a -> a, b -> ba
kappa = lambda v: v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2] - 2      # tr [a, b]


def exact():
    img = [sp.expand(e) for e in T1(T2((x, y, z)))]
    assert sp.expand(kappa(img) - kappa((x, y, z))) == 0                            # the action keeps tr [a, b]
    # control: on the abelianisation the two maps are the two acts, and their product has trace 3 (the root)
    A1, A2 = sp.Matrix([[1, 0], [1, 1]]), sp.Matrix([[1, 1], [0, 1]])
    assert (A1 * A2).trace() == 3 and (A1 * A2).det() == 1
    J = sp.Matrix(img).jacobian([x, y, z])
    assert sp.simplify(J.det()) == 1
    fixed = {x: z / (z - 1), y: z}                                                   # the curve of fixed points, by its parameter z
    assert all(sp.simplify(e.subs(fixed) - v.subs(fixed)) == 0 for e, v in zip(img, (x, y, z)))
    k = sp.together(sp.simplify(kappa((fixed[x], fixed[y], z)) + 2))
    num = sp.factor(sp.numer(k))
    assert sp.expand(num - z ** 2 * (z ** 2 - 3 * z + 3)) == 0                       # parabolic puncture: z^2 - 3z + 3 = 0 (z = 0 is not a point of the curve's hyperbolic part)
    z0 = (3 + sp.sqrt(3) * sp.I) / 2
    assert sp.simplify(z0 ** 2 - 3 * z0 + 3) == 0
    Jp = J.subs(fixed).subs(z, z0)
    cp = sp.factor(sp.simplify(Jp.charpoly(t).as_expr()))
    assert sp.expand(cp - (t - 1) * (t ** 2 - 5 * t + 1)) == 0, cp
    x0 = sp.simplify(z0 / (z0 - 1))
    assert sp.simplify(x0 - sp.conjugate(z0)) == 0
    say("EXACT  the fixed characters of the root's monodromy form a curve; where the puncture is parabolic its parameter satisfies z^2 - 3z + 3 = 0: the traces are tr b = tr ab = (3 + i sqrt 3)/2 and tr a its conjugate")
    say("       the derivative of the action there has characteristic polynomial (t - 1)(t^2 - 5t + 1); its larger root is (5 + sqrt 21)/2 = %.6f" % float((5 + sp.sqrt(21)) / 2))
    return float((5 + sp.sqrt(21)) / 2)


def seen(rate):
    warnings.filterwarnings("ignore")
    import snappy
    V4 = float(snappy.Manifold("m004").volume())
    worst = 0.0
    for name, head, base in (("the run of 6", "LLLLLLR", 1), ("(2,2,2)", "LLRRLLR", 2), ("(3,4,3)", "LLLRRRRLLLR", 2)):
        vol, cs = [], []
        for k in range(0, 9):
            M = snappy.Manifold("b++" + head + "LR" * k)
            vol.append(float(M.volume()) - (k + base) * V4)
            cs.append(float(M.chern_simons()))
        rv = [(vol[i + 1] - vol[i]) / (vol[i + 2] - vol[i + 1]) for i in range(5)]
        rc = [(cs[i + 1] - cs[i]) / (cs[i + 2] - cs[i + 1]) for i in range(5)]
        say("SEEN   %-13s excess volume settles at %.6f, step ratios %s; Chern-Simons at %+.6f, step ratios %s" % (
            name, vol[-1], " ".join("%.3f" % r for r in rv), cs[-1], " ".join("%.3f" % r for r in rc)))
        assert abs(rv[-1] - rate) < 0.003 and abs(rc[-1] - rate) < 0.003, (name, rv[-1], rc[-1])
        worst = max(worst, abs(rv[-1] - rate), abs(rc[-1] - rate))
    say("       on all three the last ratio is within %.4f of (5 + sqrt 21)/2; observed, not proved" % worst)


if __name__ == "__main__":
    r = exact()
    if "--no-snappy" not in sys.argv:
        seen(r)
    say("ALL CHECKS PASS")
