"""B892: the walls on the line of the second measurement AT EACH OF THE CUBIC'S THREE REAL ROOTS (main, 2026-11-11).

WHY.  The advisor seat's sixth re-audit accepted the mend of the audit's finding E5 and added a note: main's instrument,
walls_on_the_line.py, takes s1 at the smallest of the cubic's three real roots, while the structure paper's skeleton says
of the same line that no real point of nullity 14 exists "at all three Galois roots".  The dimensions are the same at
conjugate roots.  Whether a wall is real is not: it has to be computed at each.  The seat ran its own code at the other
two roots as a read-out.  This is main's instrument at all three.

EXPECTATIONS, WRITTEN BEFORE THIS FILE FIRST RAN.  NOT BLIND: main had read the seat's table.
 R1  the cubic has three real roots, and at each the counts are 46 vanishing weights of s1, 30 of them on x16, 12 on both.
 R2  at each root the finite walls are sixteen weights at four points, all purely imaginary: two of six weights (nullity
     18) and two of two (nullity 14), in conjugate pairs.  So at no root is there a real point of nullity 14 on the line.
 R3  a direct rank computation agrees at every wall, beside it, and at three real points.
 R4  the wall values are the seat's, to nine digits: 0.0464130116 and 0.0515261607; 0.0339621153 and 0.0304159681;
     0.0057855638 and 0.2158521452.

WHAT COULD FAIL.  A wall with a real part at one of the other two roots: the skeleton's sentence would then be false there.
"""
import collections
import importlib.util
import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("walls_on_the_line_for_three_roots", HERE / "walls_on_the_line.py")
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)
SEAT = {0: (0.0464130116, 0.0515261607), 1: (0.0339621153, 0.0304159681), 2: (0.0057855638, 0.2158521452)}    # (nullity 18, nullity 14)
OUT, RES = [], {}


def P(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)


def check(name, ok, detail=""):
    RES[name] = bool(ok)
    P("   [%s] %s%s" % ("ok" if ok else "FAILS", name, (" -- " + str(detail)) if detail else ""))


def at_root(root):
    DIM, X, Bal, W, info = w.joint_weights(root)
    sc = {k: np.abs(v).max() for k, v in W.items()}
    zero = lambda k, i: abs(W[k][i]) < 1e-7 * sc[k]
    Z = [i for i in range(DIM) if zero("s1", i)]
    gen = [i for i in Z if zero("x14", i) and zero("x16", i)]
    plane = [i for i in Z if zero("x16", i)]
    ts = [(-W["x14"][i] / W["x16"][i]) for i in Z if i not in plane]
    groups = collections.defaultdict(list)
    for t in ts:
        groups[(1 if t.imag > 0 else -1, float("%.7g" % abs(t)))].append(t)
    walls = sorted((float(np.mean([t.imag for t in m])), len(m), 12 + len(m)) for m in groups.values())
    real_part = max(abs(t.real) / abs(t) for t in ts) if ts else None
    ok = True
    for t0, mult, want in walls:
        ok = ok and w.nullity_direct(Bal, 1j * t0, DIM)[0] == want and w.nullity_direct(Bal, 1j * t0 * 1.001, DIM)[0] == 12
    for tr in (0.3, -0.05, 2.0):
        ok = ok and w.nullity_direct(Bal, tr, DIM)[0] == 12
    return dict(t=float(info["t1"]), commutator=float(info["commutator"]), residual=float(info["residual"]), counts=[len(Z), len(plane), len(gen)],
                walls=[[t, m, n] for t, m, n in walls], largest_real_part_over_modulus=float(real_part), direct_ranks_agree=bool(ok))


def main():
    roots = sorted(r.real for r in np.roots(w.CUBIC) if abs(r.imag) < 1e-9 * abs(r))
    P("B892: THE WALLS ON THE LINE OF THE SECOND MEASUREMENT AT EACH OF THE CUBIC'S THREE REAL ROOTS")
    got = [at_root(r) for r in roots]
    for k, g in enumerate(got):
        P("   root %d: t = 13 x the root = %+.8f; weights that vanish on s1, on x16 too, on both: %s; commutator %.1e, off-diagonal part %.1e"
          % (k + 1, g["t"], g["counts"], g["commutator"], g["residual"]))
        for t, m, n in g["walls"]:
            P("        wall at t = %+.10f i: %d weights, nullity %d" % (t, m, n))
        P("        largest real part of a wall over its modulus: %.1e; direct ranks agree: %s" % (g["largest_real_part_over_modulus"], g["direct_ranks_agree"]))
    check("R1 three real roots, and at each the counts are 46, 30, 12", len(roots) == 3 and all(g["counts"] == [46, 30, 12] for g in got))
    check("R2 at each root the finite walls are four purely imaginary points, two of six weights and two of two, in conjugate pairs",
          all(sorted((m, n) for _, m, n in g["walls"]) == [(2, 14), (2, 14), (6, 18), (6, 18)] and g["largest_real_part_over_modulus"] < 1e-9
              and abs(sum(t for t, _, _ in g["walls"])) < 1e-9 for g in got),
          "largest real part over modulus at the three roots: %s" % ", ".join("%.1e" % g["largest_real_part_over_modulus"] for g in got))
    check("R3 a direct rank computation agrees at every wall, beside it, and at three real points, at each root", all(g["direct_ranks_agree"] for g in got))
    def near(g, k):
        w18 = max(t for t, m, n in g["walls"] if n == 18); w14 = max(t for t, m, n in g["walls"] if n == 14)
        return abs(w18 - SEAT[k][0]) < 1e-9 and abs(w14 - SEAT[k][1]) < 1e-9
    check("R4 the wall values are the advisor seat's, to nine digits, at all three roots", all(near(g, k) for k, g in enumerate(got)))
    RES["roots"] = got
    n = sum(1 for v in RES.values() if isinstance(v, bool)); bad = [k for k, v in RES.items() if v is False]
    P(""); P("CHECKS: %d, FAILING: %d%s" % (n, len(bad), (" -- " + "; ".join(bad)) if bad else ""))
    (HERE / "walls_at_the_three_roots.json").write_text(json.dumps(RES, indent=1) + "\n", encoding="utf-8")
    (HERE / "walls_at_the_three_roots_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
