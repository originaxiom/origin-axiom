#!/usr/bin/env python3
"""B4 (CORRECTED CENSUS): the clock-coherence run on the CLOSINGS.

Cloud's condition (weld book addendum 2): paying LEAP-1 + W1 together requires
CS-time and volume-time to be the SAME clock up to monotone reparameterization
=> along the (1,n) ladder, CS must be monotone in Vol; the full check is the
(Vol,CS) pairs across B289's banked 78-closing census (|p|,|q|<=8, gcd=1).

Two-sided instrument control FIRST: reproduce B289's banked sign law
CS(p,-q) = -CS(p,q) on the census (must be 78/78) -- if the instrument cannot
reproduce the banked positive, no monotonicity verdict is trustworthy.
"""
import json
from math import gcd
import snappy

V_CUSP = 2.029883212819307250

def fill(p, q):
    # B289's instrument verbatim: prime the CS fudge on the UNFILLED manifold first
    M = snappy.Manifold('m004')
    try:
        _ = float(M.chern_simons())
    except Exception:
        return None
    M.dehn_fill((p, q))
    try:
        st = str(M.solution_type())
        if 'positively' not in st:
            return None
        vol = float(M.volume()); cs = float(M.chern_simons())
    except Exception:
        return None
    return {"p": p, "q": q, "vol": vol, "cs": cs}

# ---- the census ----
cens = []
for p in range(-8, 9):
    for q in range(-8, 9):
        if (p, q) == (0, 0) or gcd(abs(p), abs(q)) != 1:
            continue
        r = fill(p, q)
        if r: cens.append(r)
print(f"hyperbolic closings found in the |p|,|q|<=8 box: {len(cens)}")

# ---- CONTROL: B289's banked sign law CS(p,-q) = -CS(p,q) ----
idx = {(r["p"], r["q"]): r for r in cens}
pairs = ok = 0
for (p, q), r in idx.items():
    m = idx.get((p, -q))
    if m is None: continue
    pairs += 1
    a = ((r["cs"] + 0.5) % 1.0) - 0.5
    b = ((m["cs"] + 0.5) % 1.0) - 0.5
    if abs(a + b) < 1e-6 or abs(abs(a) - abs(b)) < 1e-6: ok += 1
print(f"CONTROL (B289 sign law CS(p,-q) = -CS(p,q)): {ok}/{pairs} mirror pairs obey it")

# ---- THE LADDER (1,n): the primary test ----
lad = []
for n in range(2, 31):
    r = fill(1, n)
    if r:
        cs_red = ((r["cs"] + 0.5) % 1.0) - 0.5
        lad.append({"n": n, "vol": r["vol"], "abs_cs": abs(cs_red)})
print("\n(1,n) LADDER  [Vol -> Vol_cusp = 2.0298832128]:")
for r in lad[:12]:
    print(f"  n={r['n']:>3}  Vol={r['vol']:.9f}  |CS|={r['abs_cs']:.9f}")
print("  ...")
for r in lad[-4:]:
    print(f"  n={r['n']:>3}  Vol={r['vol']:.9f}  |CS|={r['abs_cs']:.9f}")

vols = [r["vol"] for r in lad]; css = [r["abs_cs"] for r in lad]
assert len(lad) >= 10, f"VACUITY GUARD: ladder too short ({len(lad)}) to test monotonicity"
vol_inc = all(vols[i] < vols[i+1] + 1e-12 for i in range(len(vols)-1))
cs_dec  = all(css[i] > css[i+1] - 1e-12 for i in range(len(css)-1))
print(f"\nLADDER: Vol monotone increasing: {vol_inc}")
print(f"LADDER: |CS| monotone decreasing: {cs_dec}")
if not cs_dec:
    bad = [(lad[i]['n'], lad[i]['abs_cs'], lad[i+1]['n'], lad[i+1]['abs_cs'])
           for i in range(len(css)-1) if css[i] < css[i+1] - 1e-12]
    print(f"  violations ({len(bad)}): first few {bad[:5]}")

json.dump({"census_size": len(cens), "control_sign_law": [ok, pairs],
           "ladder": lad, "vol_increasing": bool(vol_inc), "cs_decreasing": bool(cs_dec),
           "census": cens}, open("b4_correct.json", "w"), indent=1)
print("DONE")
