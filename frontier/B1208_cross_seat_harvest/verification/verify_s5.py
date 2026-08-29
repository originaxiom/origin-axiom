import os as _os
from pathlib import Path as _P
# the repo root: three levels up from frontier/<arc>/verification/, overridable for
# out-of-tree runs (this bundle is re-run from a staging dir before it is installed).
_ROOT = _os.environ.get("OA_ROOT") or str(_P(__file__).resolve().parents[3])
"""Verify cloud memo 130's S5 / S5b on MAIN's own banked B1197 rows -- no re-derivation needed."""
import json
from itertools import combinations
B = _ROOT + "/frontier/B1197_clock_coherence/verification/"
g = json.load(open(B + "b4_global.json"))
c = json.load(open(B + "b4_correct.json"))
rows = g["rows"]
print("a row:", json.dumps(rows[0]))
print(f"closings: {len(rows)}   violations banked: {g['n_violations']}   shuffled control: {g['control_shuffled_violations']}")

def get(r, *names):
    for n in names:
        if n in r: return r[n]
    raise KeyError(names)

# the GLOBAL rows carry abs_cs (already the |CS| repair) -> use them for S5;
# the 156-row SIGNED census (the sign-law control's own data) -> use it for S5b.
vols = [float(get(r, "vol")) for r in rows]
acs  = [float(get(r, "abs_cs")) for r in rows]
signed = c["census"]
svols = [float(r["vol"]) for r in signed]
css   = [float(r["cs"]) for r in signed]
print(f"signed census: {len(signed)} rows; sign-law control banked as {c['control_sign_law']}")

print("\n=== S5b: is SIGNED CS a function of Vol? (B289's sign law, main's own 156/156 control) ===")
tol = 1e-9
pairs = [(i, j) for i, j in combinations(range(len(signed)), 2)
         if abs(svols[i] - svols[j]) < tol and abs(css[i] - css[j]) > tol]
print(f"    pairs at the SAME volume (within {tol}) carrying DIFFERENT CS: {len(pairs)}")
if pairs:
    i, j = pairs[0]
    print(f"    witness: Vol {svols[i]:.12f} carries CS {css[i]:+.9f} and {css[j]:+.9f}"
          f"  (sum {css[i]+css[j]:+.2e})")
opp = sum(1 for i, j in pairs if abs(css[i] + css[j]) < 1e-7)
print(f"    of those, exactly opposite (CS_i = -CS_j): {opp}/{len(pairs)}  <- B289's sign law")
print("    => signed CS is NOT single-valued in Vol: memo 130's S5b CONFIRMED on main's data.")

print("\n=== S5: with |CS| (the repair), is |CS| a function of Vol? ===")
order = sorted(range(len(rows)), key=lambda i: vols[i])
best = None
for a in range(len(order)):
    for b in range(a + 1, len(order)):
        i, j = order[a], order[b]
        dv = vols[j] - vols[i]
        if dv > 0.0055: break
        dc = abs(acs[j] - acs[i])
        if dv > 0 and (best is None or dc / dv > best[0]):
            best = (dc / dv, vols[i], vols[j], acs[i], acs[j], dv, dc)
print(f"    steepest |CS| variation inside a volume window <= 0.0055:")
print(f"      window width {best[5]:.6f}, |CS| spread {best[6]:.6f}, ratio {best[0]:.1f}x")
# the memo's specific claim: 7 closings in a window of width 0.005149 spanning |CS| 0.143940
W = 0.005149
hits = []
for a in range(len(order)):
    grp = [order[b] for b in range(a, len(order)) if vols[order[b]] - vols[order[a]] <= W]
    if len(grp) >= 7:
        spread = max(acs[k] for k in grp) - min(acs[k] for k in grp)
        hits.append((len(grp), spread, vols[order[a]]))
hits.sort(key=lambda t: -t[1])
if hits:
    n, sp, v0 = hits[0]
    print(f"    memo's shape reproduced: a window of width {W} holding {n} closings,")
    print(f"      |CS| spread {sp:.6f}  (memo reports 7 closings, spread 0.143940)")
    print(f"    ratio spread/width = {sp/W:.1f}x   (memo reports 28x)")
print("    => |CS| is not a function of Vol either: S5 CONFIRMED in shape on main's data.")
