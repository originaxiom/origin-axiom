"""chat1, 2026-10-28: the relay's question 3 (a consistency condition that selects the line class), the design reading's
checks. Post hoc and labelled: written after W175's record (the SM seat, 63aec1ac0), which listed the classes' stored
potentials. No data are read.
  A  exact arithmetic on the slope-2/5 lines to order 60:
     (i)   strict compatibility with the fibre's elliptic involution, the lift commuting with hypercharge: each holonomy
           squares to 1 on every charge q in {1, -4, 2, -3, 6, 3}, so 2a and 2b are integers;
     (ii)  the same up to SU(5)'s centre: each holonomy squares into Z/5 (it depends on q only mod 5), so 10a and 10b are
           integers;
     (iii) the line breaks SU(5) to the Standard Model's group: some holonomy is not central, so 5a or 5b is not an
           integer.
     The classes (T-orbits) meeting (ii) and (iii), against the record's carriers (B1755: the odd tenths at order 10;
     B1786: 12 lines at orders 25 and 30).
  B  the frame's one-loop potential (the SM seat's W175 instrument, unchanged): the least V* over the orbit coordinate X,
     for the class representatives b = 0, 1/60, 1/50, 1/45, 1/40, 1/35, 1/30, 1/25, 1/20, 1/15 and 1/10, at Im tau 2.5,
     3.0 and 3.5. Is any SU(5)-breaking class singled out, or does V* fall toward the SU(5)-preserving class?
Run:  python3 -B selector_checks.py <SM seat's checkout, at 0722f0ad5 or later>"""
import sys, io, json, math, contextlib, pathlib, time
from fractions import Fraction as Fr
SM = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
A = Fr(2, 5)
CARRIERS_25_30 = [Fr(k, 25) for k in (3, 4, 11, 12, 17, 19, 21, 23)] + [Fr(1, 6), Fr(13, 30), Fr(23, 30), Fr(5, 6)]


def order(a, b): return math.lcm(a.denominator, b.denominator)


def orbit(b):
    out, x = set(), b % 1
    for _ in range(60): out.add(x); x = (x - A) % 1
    return frozenset(out)


def partA():
    lines = sorted({Fr(k, N) for N in range(1, 61) for k in range(N)})
    strict = [b for b in lines if (2 * A).denominator == 1 and (2 * b).denominator == 1]
    centre = [b for b in lines if (10 * A).denominator == 1 and (10 * b).denominator == 1]
    breaks = [b for b in centre if (5 * A).denominator != 1 or (5 * b).denominator != 1]
    classes = sorted({orbit(b) for b in breaks}, key=lambda o: min(o))
    return {"strict_parity_lines_on_slope_2_5": [str(b) for b in strict],
            "parity_up_to_centre_lines": [str(b) for b in centre],
            "and_breaking_SU5_lines": [str(b) for b in breaks],
            "their_classes": [sorted(str(x) for x in o) for o in classes],
            "B1786_carriers_meeting_ii_and_iii": [str(b) for b in CARRIERS_25_30 if b in breaks],
            "odd_tenths_meeting_ii_and_iii": [str(Fr(k, 10)) for k in (1, 3, 5, 7, 9) if Fr(k, 10) in breaks]}


def partB():
    d = SM / "docs" / "dossiers" / "the_weave_2026-10-07"; sys.path.insert(0, str(d))
    with contextlib.redirect_stdout(io.StringIO()):
        import the_potential_off_the_mirror as W175
    wv = W175.W72.weights(1.0); out = {}
    for y in (2.5, 3.0, 3.5):
        row = []
        for b in [Fr(0), Fr(1, 60), Fr(1, 50), Fr(1, 45), Fr(1, 40), Fr(1, 35), Fr(1, 30), Fr(1, 25), Fr(1, 20), Fr(1, 15), Fr(1, 10)]:
            m, _ = W175.x_minimum(b, y, wv); row.append({"b": str(b), "order": order(A, b), "V*": m["V*"], "X*": m["X*"]})
        out[str(y)] = row
    return out


if __name__ == "__main__":
    t0 = time.time(); res = {"A": partA()}
    a = res["A"]
    print("A (i) strict parity on slope 2/5: lines", a["strict_parity_lines_on_slope_2_5"], "(slope 2/5 has 2a = 4/5, not an integer)")
    print("A (ii)+(iii) lines:", a["and_breaking_SU5_lines"]); print("A their classes:", a["their_classes"])
    print("A B1786's carriers meeting (ii)+(iii):", a["B1786_carriers_meeting_ii_and_iii"], "| odd tenths meeting them:", a["odd_tenths_meeting_ii_and_iii"], flush=True)
    res["B"] = partB()
    for y, row in res["B"].items():
        print("B Im tau %s:" % y, "  ".join("b=%s(o%d) V*=%.6f" % (r["b"], r["order"], r["V*"]) for r in row))
        vs = [r["V*"] for r in row]; print("   V* increasing with the class's distance from b = 0:", all(vs[i] < vs[i + 1] for i in range(len(vs) - 1)))
    (HERE / "selector_checks.json").write_text(json.dumps(res, indent=1, default=str))
    print("selector_checks exit 0 (%.0f s)" % (time.time() - t0))
