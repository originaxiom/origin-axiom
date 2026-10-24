#!/usr/bin/env python3
"""W151 — the two-object route: a constant-ratio pair of sections against the nine's target's pattern, the pair
lemma on the catalogue, and the triples that reach its class (the rule: W151_RULE.md, committed and pushed before
this script).

  The catalogue: W146's twelve record forms (R, dR, F_a) and their conjugates, 24 objects; along tau = iy the
  conjugate's value is the complex conjugate of the form's. Lines l1 = x, l3 = y - iz, l7 = y + iz (W146.lines).
  A rate is read as -(ln|f(8i)| - ln|f(6i)|) / (2 pi * 2) and rounded to (1/24)Z; every rate below is in 24ths.

  Q1  each object's (rho1, rho3, rho7) against the rule's hand table; the largest distance from the lattice, in rate
      units, below 1e-6; rho1 = 3 and both null rates = 1 mod 4
  Q2  the 300 bilinears X.Y: identically zero when |X.Y| < 1e-45 |X||Y| at y = 6, 7 and 8; the zero set against
      the rule's hand list of 20 (R.R, R.F2, F2.F2, R.dR, F2.dR, F-2.dR, F10.dR, F-10.F14, F-6.F10, F-2.F6 and the
      conjugates)
  Q3  every unordered pair (276): line rates the componentwise minima; D = rho1 - min(rho3, rho7);
      E = rate(h.h) - 2 min(rho1, rho3, rho7), rate(h.h) the least rate among the nonzero bilinears (E = inf when
      every bilinear vanishes); the lemma: 0 < D < 6 implies E >= min(2D, 6)
  Q4  the pairs with 0 < D < 6 against the hand list of 20 (each D = 2, E = 4); the pairs with E = 0 and D > 0
      against the hand list of 15 (each D >= 6); no pair in the box (D in {2, 3}, E in {-1, 0, 1}); and
      h = A + kappa B at kappa = 0.37 + 0.81i evaluated directly, E from ln(|h.h| / |h|^2) at y = 6 and 8, rounded,
      against the census's E on every pair with E finite
  Q5  every unordered triple (2 024), the same way with its six bilinears: the triples in the box against the hand
      list of 22 (each D = 2, E = 0), (conj R, R, F-2) among them
  R   read-outs: the (D, E) distribution over the pairs and over the triples; the pairs with E = 0 and their D;
      the pairs with D in {2, 3} and their E; on B1743's ten rows (W146's sha-checked target at REV_MAIN)
      |eps + delta^2/2| / (|delta|^2/2); across the eight L2 rows the largest distance from the mean of delta^2/2
      and of eps + delta^2/2; the L2 slope of ln|delta| and the lemma's bound on the ln I slope there

    python3 -B the_two_object_route.py      # writes the_two_object_route.json beside itself
"""
import contextlib
import hashlib
import io
import itertools
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_invariant_dichotomy as W146  # noqa: E402  (record_form, lines, dot, nrm2, conj, W143, the pin)

OUT = HERE / "the_two_object_route.json"
mp.mp.dps = 60
PI = mp.pi
YS = (6, 7, 8)
ZERO = mp.mpf(10) ** -45
KAPPA = mp.mpc("0.37", "0.81")
BOX_D, BOX_E = (2, 3), (-1, 0, 1)


def s(x, n=6):
    return mp.nstr(x, n)


def bar(n):
    return n[5:] if n.startswith("conj ") else "conj " + n


def objects():
    names = list(W146.RECORD) + ["conj " + n for n in W146.RECORD]
    vals = {}
    for n in W146.RECORD:
        vals[n] = {y: W146.record_form(n, mp.mpc(0, y)) for y in YS}
        vals[bar(n)] = {y: W146.conj(vals[n][y]) for y in YS}
    return names, vals


def rate24(f6, f8):
    r = -(mp.log(abs(f8)) - mp.log(abs(f6))) / (2 * PI * 2) * 24
    k = int(mp.nint(r))
    return k, abs(r - k) / 24


def hand_rates(name):
    conj = name.startswith("conj ")
    base = bar(name) if conj else name
    if base in ("R", "dR"):
        r = (3, 9, -3)
    else:
        a = int(base[1:])
        r = (3 + 2 * a, 3 - a, 15 - a) if W146.W143.eps_of(a) == 1 else (3 + 2 * a, 15 - a, 3 - a)
    return (r[0], r[2], r[1]) if conj else r


def label(names, members):
    return " + ".join(names[i] for i in sorted(members))


# ---------------------------------------------------------------- Q1

def Q1(names, vals):
    rates, table, worst, ok_table = {}, {}, mp.mpf(0), True
    for i, n in enumerate(names):
        l6, l8 = W146.lines(vals[n][6]), W146.lines(vals[n][8])
        rr = []
        for k in range(3):
            v, miss = rate24(l6[k], l8[k])
            rr.append(v)
            worst = max(worst, miss)
        rates[i] = tuple(rr)
        h = hand_rates(n)
        ok_table = ok_table and rates[i] == h
        table[n] = {"read (rho1, rho3, rho7)": list(rr), "hand": list(h), "agree": rates[i] == h}
    ok_res = all(r[0] % 4 == 3 and r[1] % 4 == 1 and r[2] % 4 == 1 for r in rates.values())
    res = {"objects": table, "every read rate equals the hand table": ok_table,
           "largest distance from the lattice (rate units)": s(worst, 3),
           "rho1 = 3 and null rates = 1 mod 4 (24ths)": ok_res}
    return res, bool(ok_table and worst < 1e-6 and ok_res), rates


# ---------------------------------------------------------------- Q2

HOLO_ZEROS = (("R", "R"), ("R", "F2"), ("F2", "F2"), ("R", "dR"), ("F2", "dR"), ("F-2", "dR"), ("F10", "dR"),
              ("F-10", "F14"), ("F-6", "F10"), ("F-2", "F6"))


def Q2(names, vals):
    idx = {n: i for i, n in enumerate(names)}
    B, zeros, mixed = {}, [], []
    least_nonzero, largest_zero, worst_miss = None, mp.mpf(0), mp.mpf(0)
    for i, j in itertools.combinations_with_replacement(range(len(names)), 2):
        X, Y = names[i], names[j]
        b, rel = {}, {}
        for y in YS:
            b[y] = W146.dot(vals[X][y], vals[Y][y])
            rel[y] = abs(b[y]) / mp.sqrt(W146.nrm2(vals[X][y]) * W146.nrm2(vals[Y][y]))
        below = [rel[y] < ZERO for y in YS]
        if all(below):
            B[(i, j)] = None
            zeros.append((i, j))
            largest_zero = max(largest_zero, max(rel.values()))
            continue
        if any(below):
            mixed.append(label(names, (i, j)))
        k, miss = rate24(b[6], b[8])
        B[(i, j)] = k
        worst_miss = max(worst_miss, miss)
        if least_nonzero is None or rel[6] < least_nonzero[0]:
            least_nonzero = (rel[6], X + " . " + Y)
    hand = set()
    for p in HOLO_ZEROS:
        hand.add(tuple(sorted(idx[n] for n in p)))
        hand.add(tuple(sorted(idx[bar(n)] for n in p)))
    read = set(zeros)
    res = {"bilinears": len(B), "identically zero": len(zeros),
           "the zeros": [names[i] + " . " + names[j] for i, j in sorted(read)],
           "zero set equals the hand list of 20": read == hand and len(hand) == 20,
           "read but not in the hand list": [names[i] + " . " + names[j] for i, j in sorted(read - hand)],
           "in the hand list but not read": [names[i] + " . " + names[j] for i, j in sorted(hand - read)],
           "below the threshold at some y only": mixed,
           "largest zero, relative to |X||Y|": s(largest_zero, 3),
           "least nonzero at y = 6, relative to |X||Y|": [s(least_nonzero[0], 3), least_nonzero[1]],
           "largest distance of a nonzero bilinear's rate from the lattice (rate units)": s(worst_miss, 3)}
    return res, bool(read == hand and len(hand) == 20), B


# ---------------------------------------------------------------- the census

def combo(members, rates, B):
    r = [min(rates[m][k] for m in members) for k in range(3)]
    lead, m = min(r[1], r[2]), min(r)
    D = r[0] - lead
    bl = [B[(a, b)] for a, b in itertools.combinations_with_replacement(sorted(members), 2)]
    nz = [x for x in bl if x is not None]
    E = min(nz) - 2 * m if nz else None
    return {"rates": r, "D": D, "E": E}


def census(names, rates, B, n):
    return {c: combo(c, rates, B) for c in itertools.combinations(range(len(names)), n)}


def in_box(c):
    return c["D"] in BOX_D and c["E"] is not None and c["E"] in BOX_E


def as_sets(names, members_list):
    return {frozenset(names.index(n) for n in ms) for ms in members_list}


# ---------------------------------------------------------------- Q3

def Q3(names, pairs):
    tested, broken = 0, []
    for c, v in pairs.items():
        if 0 < v["D"] < 6:
            tested += 1
            if v["E"] is not None and v["E"] < min(2 * v["D"], 6):
                broken.append([label(names, c), v["D"], v["E"]])
    res = {"pairs": len(pairs), "pairs with 0 < D < 6": tested, "pairs breaking the lemma": broken}
    return res, bool(len(pairs) == 276 and not broken)


# ---------------------------------------------------------------- Q4

def Q4(names, vals, pairs):
    d2_hand = as_sets(names, [(x, z) for xs, zs in ((("R", "conj R", "dR", "conj dR", "F6", "conj F6"),
                                                     ("F-2", "conj F-2")),
                                                    (("F14", "conj F14"), ("F-6", "conj F-6")),
                                                    (("F22", "conj F22"), ("F-10", "conj F-10")))
                              for x in xs for z in zs])
    e0_hand = as_sets(names, [(x, y) for x in ("conj R", "conj dR", "F6") for y in ("R", "dR", "conj F6")]
                      + [("F%d" % a, "conj F%d" % a) for a in (2, 10, 14, 18, 22, 26)])
    small = {frozenset(c): v for c, v in pairs.items() if 0 < v["D"] < 6}
    e0 = {frozenset(c): v for c, v in pairs.items() if v["E"] == 0 and v["D"] > 0}
    box = [label(names, c) for c, v in pairs.items() if in_box(v)]
    ok_small = set(small) == d2_hand and len(d2_hand) == 20 and all(v["D"] == 2 and v["E"] == 4
                                                                    for v in small.values())
    ok_e0 = set(e0) == e0_hand and len(e0_hand) == 15 and all(v["D"] >= 6 for v in e0.values())
    mism, worst = [], mp.mpf(0)
    for c, v in pairs.items():
        if v["E"] is None:
            continue
        a, b = c
        lnI = {}
        for y in (6, 8):
            h = [vals[names[a]][y][k] + KAPPA * vals[names[b]][y][k] for k in range(3)]
            lnI[y] = mp.log(abs(W146.dot(h, h))) - mp.log(W146.nrm2(h))
        r = -(lnI[8] - lnI[6]) / (2 * PI * 2) * 24
        k = int(mp.nint(r))
        worst = max(worst, abs(r - k) / 24)
        if k != v["E"]:
            mism.append([label(names, c), v["E"], k])
    res = {"pairs with 0 < D < 6": sorted([label(names, c), v["D"], v["E"]] for c, v in small.items()),
           "equal the hand list of 20, each D = 2, E = 4": ok_small,
           "pairs with E = 0 and D > 0": sorted([label(names, c), v["D"]] for c, v in e0.items()),
           "equal the hand list of 15, each D >= 6": ok_e0,
           "pairs in the target's box": box,
           "direct E at kappa = 0.37 + 0.81i: mismatches": mism,
           "direct E: largest distance from the lattice (rate units)": s(worst, 3)}
    return res, bool(ok_small and ok_e0 and not box and not mism)


# ---------------------------------------------------------------- Q5

def Q5(names, triples):
    hand = as_sets(names, [(x, y, z) for x in ("conj R", "conj dR", "F6") for y in ("R", "dR", "conj F6")
                           for z in ("F-2", "conj F-2")]
                   + [("F14", "conj F14", z) for z in ("F-6", "conj F-6")]
                   + [("F22", "conj F22", z) for z in ("F-10", "conj F-10")])
    box = {frozenset(c): v for c, v in triples.items() if in_box(v)}
    key = frozenset(names.index(n) for n in ("conj R", "R", "F-2"))
    ok = (set(box) == hand and len(hand) == 22 and all(v["D"] == 2 and v["E"] == 0 for v in box.values())
          and key in box)
    res = {"triples": len(triples),
           "triples in the target's box": sorted([label(names, c), v["D"], v["E"]] for c, v in box.items()),
           "equal the hand list of 22, each D = 2, E = 0": set(box) == hand and len(hand) == 22,
           "(conj R, R, F-2) among them": key in box}
    return res, bool(ok and len(triples) == 2024)


# ---------------------------------------------------------------- R

def dist(cs):
    cnt = Counter((v["D"], "inf" if v["E"] is None else v["E"]) for v in cs.values())
    return sorted(([d, e, k] for (d, e), k in cnt.items()), key=lambda r: (r[0], 10 ** 9 if r[1] == "inf" else r[1]))


def target():
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, text=True,
                               check=True).stdout.strip())
    raw = subprocess.run(["git", "show", "%s:%s" % (W146.REV_MAIN, W146.TARGET)], cwd=root, capture_output=True,
                         check=True).stdout
    sha = hashlib.sha256(raw).hexdigest()
    opt = json.loads(raw.decode("utf-8"))["optima"]
    rows, half, dec, L2 = [], [], [], []
    for o in opt:
        d, e = complex(*o["delta"]), complex(*o["epsilon"])
        c = e + d * d / 2
        rows.append({"hor": o["hor"], "tau": o["tau"], "|delta|^2/2": round(abs(d) ** 2 / 2, 5),
                     "|eps + delta^2/2|": round(abs(c), 5),
                     "|eps + delta^2/2| / (|delta|^2/2)": round(abs(c) / (abs(d) ** 2 / 2), 4)})
        if o["hor"].replace("_", "").replace("₂", "2").upper() == "L2":
            half.append(d * d / 2)
            dec.append(c)
            L2.append((float(o["tau"][1]), np.log(abs(d))))

    def spread(v):
        m = sum(v) / len(v)
        return round(max(abs(x - m) for x in v), 5)

    slope = float(np.polyfit([y for y, _ in L2], [v for _, v in L2], 1)[0])
    Dt = -slope / (2 * np.pi)
    return {"target sha256 as pinned": sha == W146.TARGET_SHA, "rows": rows, "L2 rows": len(half),
            "L2: largest distance from the mean of delta^2/2": spread(half),
            "L2: largest distance from the mean of eps + delta^2/2": spread(dec),
            "L2 slope of ln|delta|": round(slope, 4), "the target's D (rate units)": round(Dt, 4),
            "the lemma's bound on the ln I slope there": round(-2 * np.pi * min(2 * Dt, 0.25), 4)}


def readouts(names, pairs, triples):
    return {"(D, E, count) over the pairs": dist(pairs), "(D, E, count) over the triples": dist(triples),
            "pairs with E = 0 and their D": sorted([label(names, c), v["D"]] for c, v in pairs.items()
                                                    if v["E"] == 0),
            "pairs with D in {2, 3} and their E": sorted([label(names, c), v["E"]] for c, v in pairs.items()
                                                          if v["D"] in BOX_D),
            "the target": target()}


def main():
    out = {"arc": "W151", "rule": "W151_RULE.md", "status": "one run", "python": sys.version.split()[0],
           "dps": mp.mp.dps}
    names, vals = objects()
    out["Q1"], ok1, rates = Q1(names, vals)
    out["Q2"], ok2, B = Q2(names, vals)
    pairs = census(names, rates, B, 2)
    triples = census(names, rates, B, 3)
    out["Q3"], ok3 = Q3(names, pairs)
    out["Q4"], ok4 = Q4(names, vals, pairs)
    out["Q5"], ok5 = Q5(names, triples)
    out["R"] = readouts(names, pairs, triples)
    out["cells"] = {"Q1": ok1, "Q2": ok2, "Q3": ok3, "Q4": ok4, "Q5": ok5}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])


if __name__ == "__main__":
    main()
