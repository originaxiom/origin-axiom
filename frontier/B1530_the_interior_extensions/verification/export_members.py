#!/usr/bin/env python3
"""B1530 export (written after the run; no reading in the file): the members whose readings this arc banks, given so that
main's own class index can read them blind, as a second bench.

For m135 = -LLRR and m136 = +LLRR the file gives:
  - the bundle presentation (generators a, b, t; relators t g T = phi(g); the cusp words abAB and t' = abt or t);
  - the exact holonomy in PGL(2, Q(i)), each entry a Gaussian rational [re, im] (sm:B1529's reader; m136 with its sign set
    to +), with the relators checked exactly on the four before writing;
  - the four's convention: H -> g H g^* / |det g| on H = [[x1, x3 + i x4], [x3 - i x4, x2]], coordinates (x1, x2, x3, x4);
  - the members: the character nu by its values on a, b and t (each +-1), its fibre part u and its twist kappa = nu(t');
  - the frame: V = nu (x) four, L = nu^-4 = 1, W1 = [[V, c], [0, 1]] with c a class of H^1(V) (at m135's members the interior
    class, unique up to scale and coboundaries; at m136's, the only class), W2 the opposite order.
No class, index, cohomology dimension or reading of any kind is written.
Usage: python3 export_members.py -> members_for_main.json"""
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import exact_states as S  # noqa: E402
import post_run_e136 as P136  # noqa: E402


def gaussian(x):
    """a Q(zeta_8) number of sm:B1529's reader, read as a Gaussian rational [re, im] (asserted: no sqrt 2 part)"""
    c = x.c                                   # c0 + c1 z + c2 z^2 + c3 z^3, z = e^{i pi/4}, z^2 = i
    assert c[1] == 0 and c[3] == 0, c
    return [str(c[0]), str(c[2])]


def main():
    P = S.load(S.B1529, "post_run_exact_m135", "b1529_post_run_exact_m135")
    holo = {"-LLRR": P.exact_sl2(), "+LLRR": P136.m136_sl2()[1]}
    members = {"-LLRR": [((Fraction(0), Fraction(1, 2)), Fraction(0)), ((Fraction(1, 2), Fraction(0)), Fraction(0))],
               "+LLRR": [((Fraction(0), Fraction(1, 2)), Fraction(1, 2)), ((Fraction(1, 2), Fraction(0)), Fraction(1, 2))]}
    out = {"what": "B1530's members, for a blind second route (no readings)", "four": "H -> g H g^* / |det g| on "
           "H = [[x1, x3 + i x4], [x3 - i x4, x2]], coordinates (x1, x2, x3, x4)",
           "frame": "V = nu (x) four, L = nu^-4 = 1, W1 = [[V, c], [0, 1]] at a class c of H^1(V); W2 the opposite order; "
                    "the dictionary is sm:B1509's",
           "states": {}}
    for state, g2 in holo.items():
        sign, word = state[0], state[1:]
        G, img, chars, D = S.group(sign, word)
        sl2 = {g: [[S.E.from_z8(x) for x in row] for row in g2[g]] for g in "abt"}
        assert S.four_module(sl2).check(G.rels)
        rows = []
        for u, kt in members[state]:
            ch = S.nu(sign, u, kt)
            vals = {}
            for g in "abt":
                v = ch[g]
                vals[g] = 1 if v == S.E.ONE else (-1 if v == -S.E.ONE else str(v))
            rows.append({"u (fibre part)": [str(u[0]), str(u[1])], "kappa = nu(t')": "1" if kt == 0 else "-1",
                         "nu on a, b, t": vals})
        out["states"][state] = {"SnapPy": "m135" if state == "-LLRR" else "m136", "generators": G.gens,
                                "relators": G.rels, "cusp words": list(G.cusp),
                                "holonomy (PGL(2, Q(i)); entries [re, im])": {g: [[gaussian(x) for x in row]
                                                                                for row in g2[g]] for g in "abt"},
                                "members": rows}
    raw = json.dumps(out, indent=1)
    for key in ('"I"', "I(W", "h1", "interior", '"n"', "reading", "-1, -1", "generation"):
        assert key not in raw.replace("(no readings)", ""), key
    (HERE / "members_for_main.json").write_text(raw)
    print(raw[:1500])


if __name__ == "__main__":
    main()
