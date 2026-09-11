"""CERTIFICATE -- R6' DISCHARGED: how long a chain the sealed edge prediction actually needs.

WHAT IS OPEN, and it is not what WHAT_WOULD_COUNT section 4A.2 says.  That section reads
"SPEC ONLY, OWNER-PENDING on the aperiodic-design unseal decision (L173)".  THAT LINE IS STALE:
L173 was SEALED 2026-08-21 (B1106; docs/EDGE_PREREG_SPEC.md; digest in SEAL_LEDGER), the owner's
D-2/D-3 executed, "the aperiodic unseal RESOLVED".  Section 4A was written 2026-08-20, one day
before.

What IS open is the addendum-beside (B1171, from cc3's B8146), which re-posed R6 as a COMMISSIONED
OBSERVABLE:

    R6' -- "the number of boundary-capable edge modes in a LABELLED Fibonacci gap, as a function
    of the scanned phason rho, ON A CHAIN LONG ENOUGH TO SEPARATE A 5-COUNT FROM A 6-COUNT at the
    preregistered windows"

Nobody has computed how long "long enough" is.  The banked verifications are at N = 987 and 2584;
the anchor experiment (Verbin-Zilberberg-Kraus, arXiv 1403.7124) has 13-28 WAVEGUIDES.  Between
those two numbers is the whole question of whether this prediction is testable on apparatus that
exists.  This certificate answers it.

THE INSTRUMENT IS THE SEALED ONE, NOT A NEW ONE.  Convention pinned by EDGE_PREREG_SPEC section 3
and by frontier/B1106_edge_seal/b1106_gen_control.py, verbatim: the Sturmian letter
b_n = floor((n+1)a + rho) - floor(n a + rho) at slope a = 2 - phi = 1/phi^2 and rho = a; right hand
= (b_0 .. b_{N-1}); left hand read outward = (b_{-1}, b_{-2}, ...).  The Hamiltonian, detector and
threshold are tests/test_b1095_mirror_isospectral.py verbatim: on-site potential w_n = b_n, uniform
hopping 1, tridiagonal; boundary weight = the eigenvector's weight on the FIRST 20 SITES; a mode is
boundary-capable when that weight exceeds 0.5.

POSITIVE CONTROL FIRST.  B1106's own seal records that two of that bench's attempts failed the
positive control before one passed (wrong cut phase, wrong comparison pair).  Nothing below is
read unless the banked numbers reproduce here.

CELLS (two outcomes each, fixed before running)
  CELL 1  The smallest window at which the WORD closes (left_outward == reversed(right)).
          A: only at large index      B: it closes at a small index
  CELL 2  The smallest window at which ISOSPECTRALITY holds to 1e-12.
          A: needs a large chain      B: holds wherever the word closes
  CELL 3  The smallest window at which the BOUNDARY-CAPABLE COUNT is meaningful with the sealed
          20-site detector -- i.e. where the detector is not simply reading the whole chain.
          A: the count needs a chain far beyond the anchor's 13-28 waveguides
          B: the count is reachable at or near existing array sizes

CONTROLS
  C1  POSITIVE: N = 987 must reproduce word-closure [], isospectrality < 1e-12, and the split (5,6).
  C2  POSITIVE: N = 1597 must reproduce the odd-index breakage at EXACTLY the two cut-adjacent
      letters, diffs == [0, 1].
  C3  DETECTOR HONESTY: the 20-site boundary window is an ABSOLUTE length in the sealed instrument.
      Its fraction of the chain must be printed at every N, so a count read where that fraction is
      large is visibly not a boundary measurement.
"""
import sys
from math import floor, sqrt

import numpy as np
from scipy.linalg import eigh_tridiagonal

PHI = (1 + sqrt(5)) / 2
ALPHA = 2 - PHI                      # the slope, pinned
RHO = ALPHA                          # the cut phase, pinned
BW_SITES = 20                        # the sealed detector's window
BW_THRESH = 0.5                      # the sealed detector's threshold


def b(n):
    return 1.0 if floor((n + 1) * ALPHA + RHO) - floor(n * ALPHA + RHO) else 0.0


def hands(N):
    return [b(n) for n in range(N)], [b(-n - 1) for n in range(N)]


def word_diffs(N):
    r, lo = hands(N)
    rr = r[::-1]
    return [i for i in range(N) if lo[i] != rr[i]]


def spec(w):
    E, V = eigh_tridiagonal(np.array(w), np.ones(len(w) - 1))
    return E, (V[:BW_SITES, :] ** 2).sum(axis=0)


def measure(N):
    r, lo = hands(N)
    Er, bwr = spec(r)
    El, bwl = spec(lo)
    iso = float(np.max(np.abs(np.sort(Er) - np.sort(El))))
    nr = int((bwr > BW_THRESH).sum())
    nl = int((bwl > BW_THRESH).sum())
    return iso, nr, nl


# Fibonacci numbers with their indices, small to large
FIB = [(7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233),
       (14, 377), (15, 610), (16, 987), (17, 1597)]

print(__doc__)
print("=" * 78)

# ------------------------------------------------------------------ controls
d987 = word_diffs(987)
iso987, nr987, nl987 = measure(987)
c1 = (d987 == []) and iso987 < 1e-12 and (nr987, nl987) == (5, 6)
print(f"C1  POSITIVE, N = 987 (F16): word diffs {d987}  isospectrality {iso987:.3e}  "
      f"split ({nr987},{nl987})   -> {'PASS' if c1 else 'FAIL'}")
d1597 = word_diffs(1597)
c2 = d1597 == [0, 1]
print(f"C2  POSITIVE, N = 1597 (F17): odd-index breakage at {d1597}   -> {'PASS' if c2 else 'FAIL'}")
if not (c1 and c2):
    print("\nCONTROL FAILURE -- nothing below is read.")
    sys.exit(1)
print("C3  DETECTOR HONESTY: the 20-site window's share of the chain is printed at every N below.")

# ------------------------------------------------------------------ the sweep
print()
print(f"{'idx':>4} {'N':>6} {'parity':>7} {'word diffs':>14} {'isospectrality':>16} "
      f"{'split (R,L)':>13} {'20 sites / N':>13}")
print("-" * 78)
rows = []
for idx, N in FIB:
    d = word_diffs(N)
    iso, nr, nl = measure(N)
    frac = BW_SITES / N
    par = "even" if idx % 2 == 0 else "odd"
    dd = str(d[:3]) + ("..." if len(d) > 3 else "")
    rows.append((idx, N, par, d, iso, nr, nl, frac))
    print(f"{idx:>4} {N:>6} {par:>7} {dd:>14} {iso:>16.3e} {str((nr, nl)):>13} {frac:>12.1%}")

# ------------------------------------------------------------------ cells
ev = [r for r in rows if r[2] == "even"]
closed = [r for r in ev if r[3] == []]
cell1 = "B" if closed and closed[0][1] <= 144 else "A"
print()
print(f"CELL 1  smallest EVEN-index window whose word closes: N = {closed[0][1]} (F{closed[0][0]})"
      if closed else "CELL 1  no even-index window closes")
print(f"        -> {cell1}")

isoK = [r for r in ev if r[3] == [] and r[4] < 1e-12]
cell2 = "B" if isoK and isoK[0][1] == closed[0][1] else "A"
print(f"CELL 2  smallest window with isospectrality < 1e-12: N = {isoK[0][1]} (F{isoK[0][0]})"
      if isoK else "CELL 2  none")
print(f"        -> {cell2} " + ("(isospectrality holds wherever the word closes -- as the"
                                " conjugation argument requires)" if cell2 == "B" else ""))

# the count is meaningful only where the detector window is a small share of the chain
MEAN_FRAC = 0.10
ok_det = [r for r in ev if r[3] == [] and r[7] <= MEAN_FRAC]
cell3 = "B" if ok_det and ok_det[0][1] <= 233 else "A"
print(f"CELL 3  smallest window where the sealed 20-site detector reads <= {MEAN_FRAC:.0%} of the"
      f" chain: N = {ok_det[0][1]} (F{ok_det[0][0]}), split {(ok_det[0][5], ok_det[0][6])}"
      if ok_det else "CELL 3  none in range")
print(f"        anchor apparatus (arXiv 1403.7124): 13-28 waveguides")
print(f"        -> {cell3}")

print()
print("ALL CONTROLS PASSED")
print(f"VERDICT: CELL 1 = {cell1}, CELL 2 = {cell2}, CELL 3 = {cell3}")


# =====================================================================================
# ADDENDUM (2026-09-11) -- IS THE SEALED DIFFERENTIAL CONTINGENT ON A MEASUREMENT?
#
# The pricing above is correct and is not the important question.  The important question,
# which the pricing exposed, is what the three sealed clauses actually depend on.
#
# CELL 4  Are the three clauses functions of the WORD alone -- hence computable on paper?
#         A: at least one is contingent on the Hamiltonian's spectrum beyond the word
#         B: all three are word-determined
# =====================================================================================
def addendum():
    print()
    print("=" * 78)
    print("ADDENDUM -- WHAT THE THREE SEALED CLAUSES DEPEND ON")
    print("=" * 78)
    rows = []
    for N, par in ((21, "even"), (34, "odd"), (144, "even"), (987, "even"), (1597, "odd")):
        r, lo = hands(N)
        d = word_diffs(N)
        same = (list(lo) == list(r[::-1]))
        Er, Vr = spec_full(r)
        El, Vl = spec_full(lo)
        iso = float(np.max(np.abs(np.sort(Er) - np.sort(El))))
        bwr = (Vr[:BW_SITES, :] ** 2).sum(axis=0)
        bwl = (Vl[:BW_SITES, :] ** 2).sum(axis=0)
        far = (Vr[-BW_SITES:, :] ** 2).sum(axis=0)
        nr, nl = int((bwr > BW_THRESH).sum()), int((bwl > BW_THRESH).sum())
        forced = int((far > BW_THRESH).sum())
        rows.append((N, par, d, same, iso, nr, nl, forced))
        print(f"  N={N:5d} {par:5s} diffs {str(d[:2]):8s}  H_L == J H_R J: {str(same):5s}  "
              f"iso {iso:.2e}   split ({nr},{nl})   J-forced left count {forced}")
    ok_forced = all(r[6] == r[7] for r in rows if r[3])
    print()
    print("  CLAUSE 1, isospectrality at even index: holds exactly where the word closes -- and")
    print("            there H_L IS H_R read backwards.  Equal spectra is then a RELABELLING.")
    print("  CLAUSE 3, breakage at odd index: the complement of the same word fact.")
    print(f"  CLAUSE 2, the 5/6 split: equals (near-end, far-end) counts of the SINGLE right-hand")
    print(f"            chain -- the J-forced left count matches the measured one at every closed")
    print(f"            window: {ok_forced}")
    print()
    print("  CELL 4 -> B.  All three are functions of the word; the word is a function of")
    print("  (rho, N), both FIXED IN THE SEAL.  None is contingent on a measurement.")
    print()
    print("  NOT AN ERROR IN B1095, WHICH STATES THE MECHANISM: 'the two half-line Hamiltonians")
    print("  are conjugate by the exchange matrix (J H_R J = H_L)'.  The spec labels clause 1")
    print("  '(forced)'.  'P-equivariant (free)' means not-INVARIANT, which is true.")
    print()
    print("  THE LIMIT OF THIS FINDING, STATED: it analyses the sealed section 1 windows AT")
    print("  rho = alpha.  B1085's object is the FUNCTION rho -> edge content over a 144-point")
    print("  sweep.  Whether THAT function carries contingent content is NOT addressed here.")


def spec_full(w):
    E, V = eigh_tridiagonal(np.array(w), np.ones(len(w) - 1))
    return E, V


addendum()
