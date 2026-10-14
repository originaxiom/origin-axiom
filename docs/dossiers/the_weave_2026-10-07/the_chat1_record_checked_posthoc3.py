"""W86, POST HOC 3 (labelled; written after the Oct-6 auditor's interim report, committed before its one run). The third
A-grade finding re-checked on this seat's own code: chat1's reading of its first-background table.

  A3  chat1, relays/chat1_2026-10-06_first_background/FINDINGS.md (l.1 and l.50-52) and its relay (l.8): "level 3 is
      what the short words do -- every decided root of length <= 4 except ILLR has its first background at 3, none
      earlier", and "long words fire earlier". Re-checked from the committed counts alone; no census is re-run.
        A3a  chat1's own counts (control, family, orbit_law, recheck_zeros and the four heavy files, at 9fbab9f5e): each
             root's first level with a generation background, or "open" if none up to its last computed level. Roots
             are signed words (golden, silver, bronze = LR, LLRR, LLLRRR; a leading I is the sign -).
        A3b  main's B1439 (census_by_slope_0..3.json at c1e006b43; primes above 2 * 10^9): the same per signed word
             state; and the agreement with chat1 on every cell both hold (backgrounds exactly; firing exactly, chat1's
             disclosed bad-prime file heavy_LLLRRR_3.json reported apart from its re-run at p > 20000).
        A3c  the reading tested on the primitive roots (a power such as LRLR = (LR)^2 is a level of another root):
             (i) every decided root with at most 4 letters, ILLR aside, has its first background at level 3; (ii) every
             root with at least 5 letters has it at level 1 or 2. Each is tested on chat1's counts alone, then with
             B1439 deciding chat1's open roots, with the sign I not counted as a letter and then counted.
      A3 holds (the auditor's A finding confirmed) if, on chat1's own counts and under both letter conventions, (i) or
      (ii) fails, and chat1 and B1439 agree on the backgrounds of every shared cell.

Run: python3 the_chat1_record_checked_posthoc3.py  ->  the_chat1_record_checked_posthoc3.json beside it.
"""
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_chat1_record_checked_posthoc3.json"
CHAT1 = "9fbab9f5e"
MAIN = "c1e006b43"
FB = "relays/chat1_2026-10-06_first_background/"
FILES = ["control.json", "family.json", "orbit_law.json", "recheck_zeros.json", "heavy_LLRR_4.json",
         "heavy_LLLRRR_3_p20000.json", "heavy_ILLLRRR_3.json"]
BAD = "heavy_LLLRRR_3.json"
NAMES = {"golden": "LR", "silver": "LLRR", "bronze": "LLLRRR"}


def show(rev, path):
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, check=True,
                         text=True).stdout.strip()
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=top, capture_output=True, check=True,
                          text=True).stdout


def rows_of(d):
    if isinstance(d, list):
        return d
    for v in d.values():
        if isinstance(v, list) and v and isinstance(v[0], dict) and "n" in v[0]:
            return v
    return [d]


def state(root):
    for k, w in NAMES.items():
        if root == k + "+":
            return "+" + w
        if root == k + "-":
            return "-" + w
    return ("-" + root[1:]) if root.startswith("I") else ("+" + root)


def primitive(w):
    n = len(w)
    return not any(n % p == 0 and w == w[:p] * (n // p) for p in range(1, n))


def first_levels(cells):
    """cells: state -> {level: backgrounds}; first level with a background, else ('open', last level)"""
    out = {}
    for s, lv in cells.items():
        hit = sorted(k for k, b in lv.items() if b > 0)
        out[s] = hit[0] if hit else ("open", max(lv))
    return out


def test(first, count_sign):
    def letters(s):
        return len(s[1:]) + (1 if count_sign and s[0] == "-" else 0)
    short = {s: f for s, f in first.items() if primitive(s[1:]) and letters(s) <= 4 and s != "-LLR"}
    long_ = {s: f for s, f in first.items() if primitive(s[1:]) and letters(s) >= 5}
    bad_i = {s: f for s, f in short.items() if not isinstance(f, tuple) and f != 3}
    bad_ii = {s: f for s, f in long_.items() if not isinstance(f, tuple) and f > 2}
    return {"(i) roots with at most 4 letters, -LLR aside, decided": {s: f for s, f in short.items()
                                                                        if not isinstance(f, tuple)},
            "(i) holds": not bad_i, "(i) exceptions": bad_i,
            "(ii) roots with at least 5 letters, decided": {s: f for s, f in long_.items() if not isinstance(f, tuple)},
            "(ii) holds": not bad_ii, "(ii) exceptions": bad_ii}


def main():
    c1, c1_firing, inconsistent = {}, {}, []
    for f in FILES:
        for r in rows_of(json.loads(show(CHAT1, FB + f))):
            s, k, b = state(r["root"]), int(r["n"]), int(r["generation_backgrounds"])
            if k in c1.get(s, {}) and c1[s][k] != b:
                inconsistent.append([s, k, f])
            c1.setdefault(s, {})[k] = b
            c1_firing.setdefault(s, {})[k] = int(r["firing"])
    bad = rows_of(json.loads(show(CHAT1, FB + BAD)))[0]
    m = {}
    m_firing = {}
    for i in range(4):
        path = f"frontier/B1439_the_census_by_slope/verification/census_by_slope_{i}.json"
        for r in json.loads(show(MAIN, path)):
            m.setdefault(r["state"], {})[int(r["k"])] = int(r["generation_backgrounds"])
            m_firing.setdefault(r["state"], {})[int(r["k"])] = int(r["firing"])
    shared = [(s, k) for s in c1 for k in c1[s] if k in m.get(s, {})]
    bg_diff = [[s, k, c1[s][k], m[s][k]] for s, k in shared if c1[s][k] != m[s][k]]
    fi_diff = [[s, k, c1_firing[s][k], m_firing[s][k]] for s, k in shared if c1_firing[s][k] != m_firing[s][k]]
    f1 = first_levels(c1)
    filled = {}
    for s, f in f1.items():
        if isinstance(f, tuple) and s in m:
            fm = first_levels({s: m[s]})[s]
            filled[s] = fm
        else:
            filled[s] = f
    out = {"status": "W86 post hoc 3 (labelled): chat1's first-background reading re-checked from the committed counts",
           "A3a": {"roots (signed word states)": len(c1),
                   "first level per root, chat1's counts": {
                       s: (f if not isinstance(f, tuple) else "open through level %d" % f[1])
                       for s, f in sorted(f1.items(), key=lambda t: (len(t[0]), t[0]))},
                   "cells repeated across chat1's files with different backgrounds": inconsistent},
           "A3b": {"shared cells": len(shared), "background differences": bg_diff, "firing differences": fi_diff,
                   "chat1's bad-prime cell (heavy_LLLRRR_3.json)": {"backgrounds": bad["generation_backgrounds"],
                                                                     "firing": bad["firing"],
                                                                     "B1439 firing": m_firing["+LLLRRR"][3]},
                   "chat1's open roots decided by B1439": {s: filled[s] for s, f in f1.items()
                                                           if isinstance(f, tuple) and s in m}},
           "A3c": {"chat1's counts, sign not a letter": test(f1, False),
                   "chat1's counts, sign a letter": test(f1, True),
                   "with B1439, sign not a letter": test(filled, False),
                   "with B1439, sign a letter": test(filled, True)}}
    fails = [not (out["A3c"][k]["(i) holds"] and out["A3c"][k]["(ii) holds"])
             for k in ("chat1's counts, sign not a letter", "chat1's counts, sign a letter")]
    out["A3 holds"] = bool(all(fails) and not bg_diff)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, out["A3 holds"])


if __name__ == "__main__":
    main()
