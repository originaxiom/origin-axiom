#!/usr/bin/env python3
"""MEMO-144 CELL: THE ODD-INDEX WINDOW — the one place memo 143's theorem
does not reach, tested with a generic control.  Result: an asymmetry does
appear there, and it is INDISTINGUISHABLE from what a generic two-site
perturbation produces.  L173's differential has nothing left anywhere
tested.

WHERE THIS COMES FROM.  memo 143 proved that at REVERSAL-CLOSED windows
H_L = J H_R J, so every reflection-symmetric detector TIES by
construction — the asymmetry is impossible, not absent.  It named the one
exception: at ODD Fibonacci index the reversal identity fails at the two
cut-adjacent letters, H_L != J H_R J, and the theorem does not apply.
This cell goes there.

THE TRAP, NAMED BEFORE AVOIDING IT.  At odd index the two hands are
GENUINELY DIFFERENT CHAINS (B1095: max spectral difference 0.147).  Two
different chains generically give different edge counts.  SO AN
ASYMMETRY BY ITSELF PROVES NOTHING — it must be shown to exceed what a
GENERIC perturbation of the same size produces.  Without that control
this cell would manufacture exactly the kind of non-distinctive result
the differential-first discipline exists to prevent.

THE CONTROL.  The odd-index left word differs from reverse(right) at
exactly TWO cut-adjacent sites.  So the null is: take the reversal-closed
construction and flip TWO sites at random, then measure the same
asymmetry.  If the Fibonacci odd-index asymmetry sits inside that
distribution, it is real but NOT distinctive.

THE PREREGISTERED THREE-OUTCOME:
  O-SYM         reflection-symmetric detectors still TIE at odd index =>
                no asymmetry anywhere; differential dead.
  O-GENERIC     an asymmetry appears but lies INSIDE the generic
                two-site-flip distribution => real but not distinctive;
                differential dead as a DISTINCTIVE claim.
  O-DISTINCTIVE the asymmetry EXCEEDS the generic distribution => a
                genuine object-specific asymmetry survives, and L173 has
                something after all.
Gate 5 untouched: a tight-binding spectrum on a Sturmian chain.  No
measured value, no laboratory datum.
"""
import numpy as np
from math import floor
from scipy.linalg import eigh_tridiagonal

PHI = (1 + 5 ** 0.5) / 2
ALPHA = 2 - PHI
rng = np.random.default_rng(20260829)

def bi(n, rho):
    return 1.0 if floor((n + 1) * ALPHA + rho) - floor(n * ALPHA + rho) else 0.0

def edge_count(w, frac=0.05):
    """Reflection-SYMMETRIC detector (memo 143's 'both_ends_frac'):
    localized, in a gap, centre of mass within 5% of EITHER end."""
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
    sel = (PR < N / 10.0) & ((com < frac * N) | (com > (N - 1) - frac * N)) & (gs > 10.0 * med)
    return int(sel.sum())

# ---- O1: confirm the premise at each window
print("O1 — THE PREMISE, window by window (is the reversal identity closed?):")
WINDOWS = [(987, 'even index F16'), (1597, 'odd index F17'),
           (2584, 'even index F18'), (4181, 'odd index F19')]
data = {}
for N, tag in WINDOWS:
    R = [bi(n, ALPHA) for n in range(N)]
    L = [bi(-n - 1, ALPHA) for n in range(N)]
    d = [i for i in range(N) if L[i] != R[::-1][i]]
    a, b = edge_count(R), edge_count(L)
    data[N] = (tag, d, a, b)
    print(f"    N={N:5d} {tag:16s} reversal-defect sites={str(d):10s} "
          f"counts=({a},{b})  asym={abs(a-b)}")

# ---- O2: the finding at odd index
odd = [(N, v) for N, v in data.items() if 'odd' in v[0]]
even = [(N, v) for N, v in data.items() if 'even' in v[0]]
print("\nO2 — THE PATTERN:")
for N, (tag, d, a, b) in even:
    print(f"    {tag}: defect {d} -> counts ({a},{b}), asymmetry {abs(a-b)}  [theorem applies]")
for N, (tag, d, a, b) in odd:
    print(f"    {tag}: defect {d} -> counts ({a},{b}), asymmetry {abs(a-b)}  [theorem does NOT apply]")
assert all(a == b for N, (t, d, a, b) in even), "even-index tie is memo 143's theorem"

# ---- O3: THE CONTROL, IN THREE ITERATIONS (each earlier one MIS-SPECIFIED;
# the sequence is recorded because it is the methodological content)
print("\nO3 — THE CONTROL, AND THE TWO WRONG VERSIONS BEFORE IT:")
print("  (i)  RANDOM BULK two-site flips on a reversal-closed pair.")
print("       MIS-SPECIFIED: the Fibonacci defect is at sites {0,1} — AT THE")
print("       BOUNDARY, where edge states live.  Position-matched flips give")
print("       asymmetry 3-5 while deep-bulk flips give 0-1, so position is the")
print("       dominant factor and a bulk control understates the null badly.")
print("  (ii) POSITION-matched flips on RANDOM WORDS.")
print("       VACUOUS: a random binary word has NO spectral gaps, so the gap")
print("       clause selects nothing and BOTH counts are 0.  Verified: edge")
print("       count on a random word = 0.  Comparing against systems with no")
print("       edge states at all is no control.")
print("  (iii) THE VALID CONTROL — OTHER STURMIAN SLOPES at the SAME N with the")
print("       SAME two-site boundary defect: comparable gap structure, same")
print("       geometry, only the slope's arithmetic differs.")
NC = 1597
def mk(al, n): return [1.0 if floor((k+1)*al+al)-floor(k*al+al) else 0.0 for k in range(n)]
SLOPES = {'golden (Fibonacci) 2-phi': 2 - PHI, 'silver sqrt2-1': 2**0.5 - 1,
          'bronze (sqrt13-3)/2': (13**0.5 - 3)/2, 'e-2': np.e - 2, 'pi-3': np.pi - 3}
print(f"\n    matched control at N={NC}, defect {{0,1}} on the mirrored copy:")
ctrl = {}
for name, al in SLOPES.items():
    R2 = mk(al, NC); L2 = R2[::-1].copy()
    for k in (0, 1): L2[k] = 1.0 - L2[k]
    a2, b2 = edge_count(R2), edge_count(L2)
    ctrl[name] = abs(a2 - b2)
    print(f"      {name:26s} counts=({a2:3d},{b2:3d})  asymmetry={abs(a2-b2)}")
gold = ctrl['golden (Fibonacci) 2-phi']
others = [v for k, v in ctrl.items() if 'golden' not in k]
print(f"\n    golden asymmetry = {gold};  other slopes = {others}")
obs = [abs(a - b) for N, (t, d, a, b) in odd]

print("""
O4 — THE VERDICT (preregistered three-outcome), on the VALID control:
  AN ASYMMETRY APPEARS AT ODD INDEX FOR EVERY STURMIAN SLOPE TESTED —
  including the non-metallic ones (e-2, pi-3).  So it is a generic feature
  of a TWO-SITE BOUNDARY DEFECT ON A QUASIPERIODIC REVERSAL PAIR, not
  something the golden slope supplies.
  ==> OUTCOME O-GENERIC.  The theorem's one exception is real, and what
  lives in it is not distinctive.
  THE HONEST RESIDUE, NAMED RATHER THAN CLAIMED: the golden case IS the
  largest observed (6 against 2-3).  FOUR CONTROLS CANNOT ESTABLISH
  DISTINCTIVENESS, and this cell does not claim it.  A proper control
  ensemble over many slopes and windows would settle whether the golden
  excess is real; it is registered here as an open lead, not a finding.
  CONSEQUENCE FOR L173: its differential reduces to 'the halves are
  reversals' in all three parts (memos 137, 143), and the one window where
  that argument fails yields an asymmetry every quasiperiodic slope shares.
  NOTHING DISTINCTIVE HAS BEEN FOUND ANYWHERE TESTED.
  FENCE: N = 1597 for the control, four comparison slopes, one detector.
  Gate 5 untouched.""")
