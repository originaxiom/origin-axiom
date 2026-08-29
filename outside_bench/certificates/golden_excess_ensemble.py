#!/usr/bin/env python3
"""MEMO-145 CELL: IS THE GOLDEN EXCESS REAL? — the open lead memo 144
registered, tested against a proper slope-and-window ensemble with the
commensurability confound removed.

THE LEAD.  memo 144 found an odd-index asymmetry of 6 for the golden
slope against 2-3 for four other Sturmian slopes at N = 1597, and
registered the excess as an OPEN LEAD, explicitly declining to claim
distinctiveness on four controls.

THE CONFOUND THAT MUST BE REMOVED FIRST, and memo 144 did not:
N = 1597 IS A FIBONACCI NUMBER.  It is a continued-fraction convergent
denominator OF THE GOLDEN SLOPE and of no other slope tested.  Comparing
every slope at a window commensurate with ONE of them is not a fair
ensemble — it hands the golden case its own natural window and the others
an arbitrary one.  THE FIX: give EVERY slope its OWN natural windows, the
denominators of ITS OWN convergents, and compare like with like.

THE MEASUREMENT.  For a slope alpha and a window N:
  R = the Sturmian word of slope alpha, length N
  L = reverse(R) with sites {0,1} flipped   (exactly the odd-index defect
      memo 144 verified the Fibonacci case to have)
  asymmetry = |edge_count(R) - edge_count(L)|
with edge_count the reflection-symmetric detector of memo 143 (localized,
in a gap, centre of mass within 5% of EITHER end).

THE PREREGISTERED TWO-OUTCOME:
  G-EXCESS  the golden slope's asymmetries sit at or near the TOP of the
            ensemble at its own natural windows (say, above the 90th
            percentile of the pooled distribution) => the excess is real
            and memo 144's lead is upgraded to a finding.
  G-NOISE   the golden values sit INSIDE the ensemble spread => memo 144's
            4-control reading was small-sample noise, and the lead closes
            negatively.
Also reported, because it is the honest diagnostic either way: whether
the asymmetry depends on the PARITY of the convergent index, which is the
structure memo 143's theorem predicts (even index => reversal-closed =>
forced tie; odd index => the defect is real).
Gate 5 untouched: tight-binding spectra on Sturmian chains; no measured
value anywhere.
"""
import numpy as np
from math import floor
from fractions import Fraction
from scipy.linalg import eigh_tridiagonal

def sturm(al, N):
    return [1.0 if floor((n + 1) * al + al) - floor(n * al + al) else 0.0
            for n in range(N)]

def edge_count(w, frac=0.05):
    N = len(w)
    E, V = eigh_tridiagonal(np.array(w), np.ones(N - 1))
    p = V ** 2
    PR = 1.0 / (p ** 2).sum(axis=0)
    com = (p * np.arange(N)[:, None]).sum(axis=0)
    o = np.argsort(E); Es = E[o]; sp = np.diff(Es); med = np.median(sp)
    gs = np.zeros(N)
    for j, idx in enumerate(o):
        lo = sp[j - 1] if j > 0 else np.inf
        hi = sp[j] if j < N - 1 else np.inf
        gs[idx] = min(lo, hi)
    return int(((PR < N / 10.0) &
                ((com < frac * N) | (com > (N - 1) - frac * N)) &
                (gs > 10.0 * med)).sum())

def asym(al, N):
    R = sturm(al, N)
    L = R[::-1].copy()
    for k in (0, 1):
        L[k] = 1.0 - L[k]
    return abs(edge_count(R) - edge_count(L))

def convergent_denoms(al, lo, hi, maxterms=40):
    """denominators of alpha's own continued-fraction convergents in [lo,hi],
    with the convergent INDEX (parity matters: memo 143's theorem)."""
    x = al; a = []
    for _ in range(maxterms):
        ai = floor(x); a.append(int(ai))
        fr = x - ai
        if fr < 1e-13: break
        x = 1.0 / fr
    out = []
    h0, h1, k0, k1 = 1, a[0], 0, 1
    for i in range(1, len(a)):
        h0, h1 = h1, a[i] * h1 + h0
        k0, k1 = k1, a[i] * k1 + k0
        if lo <= k1 <= hi:
            out.append((i, k1))
    return out

PHI = (1 + 5 ** 0.5) / 2
SLOPES = {
    'golden 2-phi': 2 - PHI,
    'silver sqrt2-1': 2 ** 0.5 - 1,
    'bronze (sqrt13-3)/2': (13 ** 0.5 - 3) / 2,
    'sqrt3-1': 3 ** 0.5 - 1,
    'sqrt5-2': 5 ** 0.5 - 2,
    'sqrt7-2': 7 ** 0.5 - 2,
    'e-2': np.e - 2,
    'pi-3': np.pi - 3,
    'log2': np.log(2),
    '1/pi': 1 / np.pi,
    'sqrt2/2': 2 ** 0.5 / 2,
    'euler-gamma': 0.5772156649015329,
    'ln3-1': np.log(3) - 1,
    '2^(1/3)-1': 2 ** (1/3) - 1,
    '3^(1/3)-1': 3 ** (1/3) - 1,
}
LO, HI = 600, 2700
print("E1 — EACH SLOPE AT ITS OWN NATURAL WINDOWS (convergent denominators),")
print(f"     window range [{LO}, {HI}].  The commensurability confound is removed:")
print(f"     {'slope':<22s} {'(conv index, N)':>34s}")
plan = {}
for name, al in SLOPES.items():
    cs = convergent_denoms(al, LO, HI)
    plan[name] = cs
    print(f"     {name:<22s} {str(cs):>34s}")

rows = []
print("\nE2 — THE MEASUREMENT (asymmetry at each slope's own windows):")
print(f"     {'slope':<22s} {'idx':>4s} {'N':>6s} {'asym':>5s} {'idx parity':>11s}")
for name, cs in plan.items():
    for (i, N) in cs:
        a = asym(SLOPES[name], N)
        rows.append((name, i, N, a, 'even' if i % 2 == 0 else 'odd'))
        print(f"     {name:<22s} {i:>4d} {N:>6d} {a:>5d} {('even' if i%2==0 else 'odd'):>11s}")

gold = [r for r in rows if r[0].startswith('golden')]
other = [r for r in rows if not r[0].startswith('golden')]
ga = np.array([r[3] for r in gold], float)
oa = np.array([r[3] for r in other], float)
print(f"\nE3 — THE ENSEMBLE:")
print(f"     golden windows: {len(ga)}   values {ga.astype(int).tolist()}")
print(f"     other  windows: {len(oa)}   mean={oa.mean():.2f} sd={oa.std():.2f} "
      f"median={np.median(oa):.1f} max={oa.max():.0f}")
for g in ga:
    pct = float((oa >= g).mean())
    print(f"       golden asymmetry {g:.0f}: P(other >= it) = {pct:.3f}  "
          f"(percentile {100*(1-pct):.0f})")
p_all = float((oa >= ga.max()).mean())

print("\nE4 — THE VERDICT (preregistered):")
if p_all < 0.10:
    print(f"     ==> OUTCOME G-EXCESS.  The golden slope's largest asymmetry")
    print(f"         sits above the 90th percentile of the ensemble")
    print(f"         (P(other >= it) = {p_all:.3f}).  memo 144's lead is upgraded.")
else:
    print(f"     ==> OUTCOME G-NOISE.  The golden values sit INSIDE the ensemble")
    print(f"         spread (P(other >= max golden) = {p_all:.3f}).  memo 144's")
    print(f"         four-control reading was SMALL-SAMPLE NOISE, and the lead")
    print(f"         CLOSES NEGATIVELY.  The bench registered it as a lead and")
    print(f"         declined to claim it; that caution is now vindicated.")

ev = np.array([r[3] for r in rows if r[4] == 'even'], float)
od = np.array([r[3] for r in rows if r[4] == 'odd'], float)
print(f"\nE5 — THE PARITY DIAGNOSTIC (memo 143's theorem predicts a split):")
print(f"     even convergent index: n={len(ev)} mean={ev.mean():.2f} zeros={(ev==0).sum()}")
print(f"     odd  convergent index: n={len(od)} mean={od.mean():.2f} zeros={(od==0).sum()}")
print("     (the theorem says reversal-closure — hence a forced tie — belongs")
print("      to the closed windows; this reports whether the ensemble agrees.)")
print("\nFENCE: one detector, one defect position, windows in a bounded range,")
print("15 slopes.  Gate 5 untouched.")
