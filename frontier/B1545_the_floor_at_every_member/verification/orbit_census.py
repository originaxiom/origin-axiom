#!/usr/bin/env python3
"""B1545 -- the census for Corollary G: on sm:B1538's four room-3 covers, every invariant character zeta of K with zeta^M = 1 (M | 24):
zeta(l_x) is constant on pi-orbits, the product over all punctures is 1, and if zeta^4 is a puncture character then zeta is
trivial on the punctures of at most two of the four cusps (so a member nu over a puncture character has m_A <= 2)."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
B1538V = ROOT / "frontier/B1538_the_puncture_characters/verification"
sys.path.insert(0, str(B1538V))
import punct_four as FO  # noqa: E402,F401
import punct_covers as F  # noqa: E402
WANT = {"m135.D8.2-0-4.w1": ("-LLRR", (2, 0, 4), 1), "m135.D8.4-0-2.w4": ("-LLRR", (4, 0, 2), 4),
        "m136.D8.2-0-4.w3": ("+LLRR", (2, 0, 4), 3), "m136.D8.4-0-2.w5": ("+LLRR", (4, 0, 2), 5)}
out = {}
for cid, (sw, lat, w) in WANT.items():
    C = F.Cover(F.State(sw), lat, w)
    M = 24
    chars = C.characters(M)
    orbit_const = prod_one = True
    worst = 0
    n4p = 0
    for ez in chars:
        pv = C.puncture_values(ez, M)
        if any(len({pv[x] for x in O}) > 1 for O in C.orbits):
            orbit_const = False
        if sum(pv) % M != 0:
            prod_one = False
        if any(4 * v % M for v in pv):                      # zeta^4 is a puncture character
            n4p += 1
            triv = sum(1 for O in C.orbits if all(pv[x] == 0 for x in O))
            worst = max(worst, triv)
    out[cid] = {"characters (zeta^24 = 1)": len(chars), "with zeta^4 a puncture character": n4p,
                "zeta(l_x) constant on pi-orbits": orbit_const, "product over the punctures = 1": prod_one,
                "most cusps whose punctures zeta kills, when zeta^4 is a puncture character": worst, "cusps": len(C.orbits)}
    print(cid, json.dumps(out[cid]), flush=True)
(Path(__file__).resolve().parent / "orbit_census.json").write_text(json.dumps(out, indent=1) + "\n")
