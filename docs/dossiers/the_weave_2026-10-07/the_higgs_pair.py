#!/usr/bin/env python3
"""W147 — what assigns the Higgs pair? Every pair of the twisted spaces GENESIS PF1-W admits, against a common
three-generation condition, a pair term T and S allow, W132's closure of the moves' SU(2) remainder, and whether the
weave can tell H_u from H_d (the rule: W147_RULE.md, committed and pushed before this script).

  P0  the inputs: the admissible twists from W133's condition (N(F) carries chi_eta^(21 + 3r), admissible iff it is
      chi_eta^9), their nonzero spaces at n in {0, 1} from W127's committed dimensions, and W127's committed index
  P1  the census of the ten unordered pairs: (a) a common condition with |I| = 3 for both; (b) r + r' = 0 mod 24;
      (c) r = r'; and their intersections
  P2  W132's closure: its G5 recomputed on B1674's four assignments, against every admissible pair's r + r'
  P3  the order: each condition symmetric under the exchange; W140's C1 recomputed (the moves fix only the trivial
      line); the 266 lines by order, and those on which 6Y = +3 and -3 differ (N not dividing 6)
  P4  read-outs: W143's lines and multiplicities in each space; the conjugate twist -r; where the e1-led lines fall

    python3 -B the_higgs_pair.py      # writes the_higgs_pair.json beside itself
"""
import contextlib
import io
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_hypercharge_line as W140  # noqa: E402  (C1, the 266 lines, the 6Y labels)
    import the_twenty_fourths as W132  # noqa: E402  (G5, B1674's four)

OUT = HERE / "the_higgs_pair.json"
CONDS = ("0", "V2", "V4", "L6")
TWISTS = (0, 4, 8, 12, 16, 20)


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def P0():
    w127 = load("the_field_at_the_end.json")
    dims = w127["h(r, n) exact, by N"]["6"]
    index = w127["the index I(cond, r, n)"]
    admissible = [r for r in TWISTS if (21 + 3 * r - 9) % 24 == 0]
    spaces = [(r, n) for r in admissible for n in (0, 1) if dims["r=%d n=%d" % (r, n)] > 0]
    I = {(r, n): {c: int(round(index[c][str(r)][str(n)])) for c in CONDS} for (r, n) in spaces}
    res = {"admissible twists": admissible, "spaces (r, n) with h > 0": [list(s) for s in spaces],
           "dimensions": {"%d,%d" % s: dims["r=%d n=%d" % s] for s in spaces},
           "index at (0, V2, V4, L6)": {"%d,%d" % s: [I[s][c] for c in CONDS] for s in spaces}}
    ok = admissible == [4, 12, 20] and spaces == [(4, 0), (4, 1), (12, 1), (20, 1)]
    ok &= [res["dimensions"][k] for k in ("4,0", "4,1", "12,1", "20,1")] == [1, 4, 3, 3]
    return res, bool(ok), spaces, I


def label(s):
    return "%d%s" % (s[0], "" if s[0] != 4 else "_%d" % s[1])


def cond_a(A, B, I):
    return [c for c in CONDS if abs(I[A][c]) == 3 and abs(I[B][c]) == 3]


def P1(spaces, I):
    pairs = list(itertools.combinations_with_replacement(spaces, 2))
    rows = {}
    for A, B in pairs:
        rows["{%s, %s}" % (label(A), label(B))] = {
            "(a) common three-generation conditions": cond_a(A, B, I),
            "(b) r + r' = 0 mod 24": (A[0] + B[0]) % 24 == 0,
            "(c) r = r'": A[0] == B[0]}
    a = sorted(k for k, v in rows.items() if v["(a) common three-generation conditions"])
    b = sorted(k for k, v in rows.items() if v["(b) r + r' = 0 mod 24"])
    c = sorted(k for k, v in rows.items() if v["(c) r = r'"])
    ab = sorted(set(a) & set(b))
    abc = sorted(set(ab) & set(c))
    two = rows["{12, 20}"]
    res = {"pairs": rows, "(a)": a, "(b)": b, "(c)": c, "(a) and (b)": ab, "(a), (b) and (c)": abc,
           "TWO_HIGGS {12, 20}": two}
    ok = (a == sorted(["{12, 12}", "{20, 20}", "{12, 20}", "{4_1, 4_1}", "{4_1, 12}"])
          and rows["{12, 12}"]["(a) common three-generation conditions"] == ["0", "L6"]
          and rows["{12, 20}"]["(a) common three-generation conditions"] == ["0"]
          and rows["{4_1, 12}"]["(a) common three-generation conditions"] == ["L6"]
          and b == sorted(["{12, 12}", "{4_0, 20}", "{4_1, 20}"])
          and c == sorted(["{4_0, 4_0}", "{4_0, 4_1}", "{4_1, 4_1}", "{12, 12}", "{20, 20}"])
          and ab == ["{12, 12}"] and abc == ["{12, 12}"]
          and two["(a) common three-generation conditions"] == ["0"] and not two["(b) r + r' = 0 mod 24"]
          and not two["(c) r = r'"])
    return res, bool(ok), pairs


def P2(pairs):
    g5, g5_ok, _ = W132.G5()
    allowed = {k: set(v) for k, v in g5["m_u + m_d that close SU(2) and gravity, on B1674's four"].items()}
    sums = sorted({(A[0] + B[0]) % 24 for A, B in pairs})
    closing = [k for k, v in allowed.items() if v & set(sums)]
    res = {"W132's G5 checks hold": bool(g5_ok),
           "allowed m_u + m_d, per B1674 assignment": {k: sorted(v) for k, v in allowed.items()},
           "admissible pair sums r + r' mod 24": sums,
           "every admissible twist is 4 mod 8": all(A[0] % 8 == 4 and B[0] % 8 == 4 for A, B in pairs),
           "assignments an admissible pair closes": closing}
    ok = (g5_ok and sums == [0, 8, 16] and not closing and res["every admissible twist is 4 mod 8"]
          and sorted(sorted(v) for v in allowed.values()) == [[], [], [12], [12]])
    return res, bool(ok)


def P3(pairs, I):
    sym = all(cond_a(A, B, I) == cond_a(B, A, I) and ((A[0] + B[0]) % 24 == (B[0] + A[0]) % 24) and
              ((A[0] == B[0]) == (B[0] == A[0])) for A, B in pairs)
    c1, c1_ok = W140.C1()
    lines = W140.lines_up_to_sign()
    by_order = {}
    for v in lines:
        by_order[W140.line_order(v)] = by_order.get(W140.line_order(v), 0) + 1
    hu, hd = W140.Q6["Hu"], W140.Q6["Hd"]
    tell = sum(cnt for N, cnt in by_order.items() if (hu - hd) % N != 0)
    blind = sum(cnt for N, cnt in by_order.items() if (hu - hd) % N == 0)
    blind_orders = sorted(N for N in by_order if (hu - hd) % N == 0)
    res = {"each condition symmetric under the exchange": bool(sym),
           "W140's C1 (only the trivial line fixed)": bool(c1_ok),
           "lines": len(lines), "lines by order": {str(k): v for k, v in sorted(by_order.items())},
           "6Y labels (H_u, H_d)": [hu, hd], "lines that tell H_u from H_d": tell, "lines that do not": blind,
           "orders that do not": blind_orders}
    ok = sym and c1_ok and len(lines) == 266 and tell == 246 and blind == 20 and blind_orders == [1, 2, 3, 6]
    return res, bool(ok)


def P4(spaces):
    w143 = load("the_zero_free_higgs_signs.json")
    lines = {k: v["members"] for k, v in w143["H1"].items()}
    e1 = {k: v["the non-null-led members"] for k, v in w143["H3"].items()}
    conj = {"%d" % r: (-r) % 24 for r in sorted({s[0] for s in spaces})}
    return {"lines in each space (W143)": lines, "multiplicities (W143's H2)": w143["H2"],
            "e1-led lines (W143's H3)": e1, "the conjugate twist -r mod 24": conj,
            "(b) read as: H_u in the twist of H_d's conjugate": {"{12, 12}": conj["12"] == 12,
                                                                 "{4, 20}": conj["4"] == 20}}


def main():
    out = {"arc": "W147", "rule": "W147_RULE.md", "status": "one run", "python": sys.version.split()[0]}
    out["P0"], ok0, spaces, I = P0()
    out["P1"], ok1, pairs = P1(spaces, I)
    out["P2"], ok2 = P2(pairs)
    out["P3"], ok3 = P3(pairs, I)
    out["P4"] = P4(spaces)
    out["cells"] = {"P0 (the inputs)": bool(ok0), "P1": bool(ok1), "P2": bool(ok2), "P3": bool(ok3)}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])


if __name__ == "__main__":
    main()
