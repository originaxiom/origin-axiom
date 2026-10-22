#!/usr/bin/env python3
"""W122 — the closed universes (the script; `W122_RULE.md` was committed and pushed before it).

Every orientable once-punctured torus bundle b++w and b+-w over the primitive cyclic words w in L and R with both
letters, of length 2 to 6, Dehn filled at every primitive slope (p, q) with 0 <= q <= 7 and |p| <= 7 (once up to sign;
q = 0 means p = 1), in SnapPy's own cusp basis. A filling is certified hyperbolic when its solution type is "all
tetrahedra positively oriented" and its volume agrees at high precision within 1e-9.

    python3 -B the_closed_universes.py      # writes the_closed_universes.json and the_closed_universes_run.txt
"""
import json
import math
from pathlib import Path

import snappy

HERE = Path(__file__).resolve().parent
out, log = {"arc": "W122", "rule": "W122_RULE.md"}, []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    log.append(s)


def lyndon(n):
    res = []
    for k in range(2 ** n):
        w = "".join("R" if (k >> i) & 1 else "L" for i in range(n))
        rots = [w[i:] + w[:i] for i in range(n)]
        if "L" in w and "R" in w and w == min(rots) and len(set(rots)) == n:
            res.append(w)
    return res


words = [w for n in range(2, 7) for w in lyndon(n)]
bundles = [p + w for w in words for p in ("b++", "b+-")]
slopes = [(1, 0)] + [(p, q) for q in range(1, 8) for p in range(-7, 8) if math.gcd(abs(p), q) == 1]
say("census:", len(words), "words,", len(bundles), "bundles,", len(slopes), "slopes")

rows, bvol = [], {}
for b in bundles:
    B = snappy.Manifold(b)
    bvol[b] = {"orientable": B.is_orientable(), "volume": float(B.volume()), "solution": B.solution_type()}
    for (p, q) in slopes:
        r = {"bundle": b, "slope": [p, q]}
        try:
            M = snappy.Manifold(b)
            M.dehn_fill((p, q))
            st = M.solution_type()
            r["solution"] = st
            if st == "all tetrahedra positively oriented":
                v = float(M.volume())
                H = M.high_precision()
                vh = float(H.volume())
                r["volume"] = v
                r["certified"] = abs(v - vh) < 1e-9
            else:
                r["certified"] = False
        except Exception as e:  # recorded, not hidden
            r["error"] = repr(e)
            r["certified"] = False
        rows.append(r)

cert = [r for r in rows if r["certified"]]
notc = [r for r in rows if not r["certified"]]
types = {}
for r in notc:
    k = r.get("solution", "error")
    types[k] = types.get(k, 0) + 1
say("fillings:", len(rows), "| certified:", len(cert), "| not certified:", len(notc), types)

vals = sorted({round(r["volume"], 9) for r in cert})
by = {}
for r in cert:
    by.setdefault(round(r["volume"], 9), []).append(r)
five = []
for v in vals[:5]:
    rs = by[v]
    M = snappy.Manifold(rs[0]["bundle"])
    M.dehn_fill(tuple(rs[0]["slope"]))
    try:
        name = [str(x) for x in M.identify()]
    except Exception as e:
        name = [repr(e)]
    five.append({"volume": v, "fillings": [[r["bundle"], r["slope"]] for r in rs],
                 "bundles": sorted({r["bundle"] for r in rs}), "identified as": name})
    say("  %.10f" % v, "bundles", sorted({r["bundle"] for r in rs}), "slopes", [r["slope"] for r in rs][:6],
        "identified as", name[:3])

least = five[0]
R1 = {"least volume": least["volume"], "bundles": least["bundles"], "identified as": least["identified as"],
      "holds": abs(least["volume"] - 0.9427073628) < 1e-8 and least["bundles"] == ["b+-LR"]
      and any(n.startswith("m003(-3,1)") for n in least["identified as"])}
second = five[1]
R2 = {"second volume": second["volume"], "bundles": second["bundles"],
      "holds": abs(second["volume"] - 0.9813688289) < 1e-8 and second["bundles"] == ["b++LR", "b+-LR"]}
below = [r for r in cert if r["volume"] >= bvol[r["bundle"]]["volume"] - 1e-12]
R3 = {"fillings at or above their bundle's volume": [[r["bundle"], r["slope"], r["volume"]] for r in below],
      "holds": not below}
per = sorted(((min(r["volume"] for r in cert if r["bundle"] == b), b) for b in bundles
              if any(r["bundle"] == b for r in cert)))
R4 = {"counts": {"fillings": len(rows), "certified": len(cert), "not certified": len(notc), "types": types},
      "five least": five, "each bundle's least filling, in order": [[b, v] for v, b in per[:12]],
      "bundles with no certified filling": [b for b in bundles if not any(r["bundle"] == b for r in cert)]}
say("R1", R1["least volume"], R1["bundles"], R1["identified as"][:2], "->", R1["holds"])
say("R2", R2["second volume"], R2["bundles"], "->", R2["holds"])
say("R3 fillings at or above their bundle's volume:", len(below), "->", R3["holds"])
say("R4 each bundle's least filling, first twelve:", [[b, round(v, 6)] for v, b in per[:12]])
out.update({"census": {"words": words, "bundles": bvol, "slopes": slopes}, "R1": R1, "R2": R2, "R3": R3, "R4": R4,
            "rows": rows, "verdict": {"R1": R1["holds"], "R2": R2["holds"], "R3": R3["holds"]}})
say("verdict", out["verdict"])
(HERE / "the_closed_universes.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
(HERE / "the_closed_universes_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
