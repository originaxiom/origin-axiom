#!/usr/bin/env python3
"""MEMO-143 CELL: IS ANY ASYMMETRY POSSIBLE ONCE BOTH ENDS ARE COUNTED? —
the gating question memo 142 created, and it is a THEOREM, not a
measurement: at reversal-closed windows NO reflection-symmetric detector
can report unequal edge counts for the two hands.  So the last surviving
part of L173's differential collapses for the same reason the first two
did.

WHERE THIS COMES FROM.  memo 137 conceded two of the three parts of
L173's differential: exact mirror-isospectrality (an identity for ANY word
whose halves are reversals) and the Fibonacci-parity breaking (the
classical two-letter palindromic-prefix defect).  It found the
COMPLEMENTARY SPLIT alone survived.  memo 142 then showed that split's
ASYMMETRY (6 vs 5) is DETECTOR-DEPENDENT — a two-ended detector reads 7-7
— and exhibited the mechanism: B1095's detector reads only the first 20
sites, and on a reversal pair a one-ended detector manufactures an
asymmetry.  THE QUESTION LEFT OPEN: is that just one other detector's
answer, or is EQUALITY FORCED?

THE CLAIM UNDER TEST (stated before computing):
  At a reversal-closed window, w_L = reverse(w_R), so H_L = J H_R J with
  J the exchange matrix (J_{ij} = delta_{i, N-1-j}), which is orthogonal
  and an involution.  Then:
    * H_R psi = E psi  =>  H_L (J psi) = E (J psi)  — same spectrum;
    * (J psi)_n = psi_{N-1-n}  =>  |J psi|^2 is the REFLECTION of |psi|^2;
    * hence for corresponding states: PR is EQUAL, the gap structure is
      EQUAL, and com_L = (N-1) - com_R EXACTLY.
  THEREFORE any detector whose edge criterion is INVARIANT UNDER
  REFLECTION (i.e. treats the two ends alike) assigns the same verdict to
  psi in the right hand and J psi in the left, and the two counts are
  EQUAL BY CONSTRUCTION.  An asymmetry requires a detector that
  distinguishes the ends — which is a property of the instrument, not of
  the object.

THE PREREGISTERED TWO-OUTCOME:
  A-FORCED  every reflection-symmetric detector tested returns EQUAL
            counts, and the com identity holds exactly => the asymmetry
            is IMPOSSIBLE, not merely absent, and L173's last surviving
            differential collapses.
  A-FREE    some reflection-symmetric detector returns unequal counts =>
            a genuine asymmetry exists and memo 142 under-read it.
Gate 5 untouched: linear algebra on a Sturmian chain; no measured value.
"""
import numpy as np
from math import floor
from scipy.linalg import eigh_tridiagonal

PHI = (1 + 5 ** 0.5) / 2
ALPHA = 2 - PHI
N = 987

def bi(n, rho):
    return 1.0 if floor((n + 1) * ALPHA + rho) - floor(n * ALPHA + rho) else 0.0

R = [bi(n, ALPHA) for n in range(N)]
L = [bi(-n - 1, ALPHA) for n in range(N)]

# ---- S1: the window IS reversal-closed
print("S1 — THE PREMISE: is this window reversal-closed?")
print(f"    left word == reverse(right word): {L == R[::-1]}")
assert L == R[::-1]

def diag(w):
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
    return E, PR, com, gs, med

ER, PRr, comr, gsr, medr = diag(R)
EL, PRl, coml, gsl, medl = diag(L)
oR, oL = np.argsort(ER), np.argsort(EL)

# ---- S2: the three identities the theorem rests on
print("\nS2 — THE IDENTITIES (matched state by state, in energy order):")
dE = np.max(np.abs(ER[oR] - EL[oL]))
dPR = np.max(np.abs(PRr[oR] - PRl[oL]))
dcom = np.max(np.abs(comr[oR] - ((N - 1) - coml[oL])))
dgs = np.max(np.abs(gsr[oR] - gsl[oL]))
print(f"    max |E_R - E_L|                       = {dE:.3e}   (isospectral)")
print(f"    max |PR_R - PR_L|                     = {dPR:.3e}   (same localization length)")
print(f"    max |gap_R - gap_L|                   = {dgs:.3e}   (same gap structure)")
print(f"    max |com_R - ((N-1) - com_L)|         = {dcom:.3e}   (EXACTLY REFLECTED)")
assert dE < 1e-9 and dPR < 1e-6 and dgs < 1e-9 and dcom < 1e-6
print("    => every state of the left hand is the REFLECTION of a right-hand")
print("       state at the same energy, with the same localization length and")
print("       the same gap environment.  Only its POSITION is mirrored.")

# ---- S3: reflection-symmetric detectors must tie
def count(PR, com, gs, med, rule):
    loc = PR < N / 10.0
    gap = gs > 10.0 * med
    if rule == 'both_ends':      # reflection-SYMMETRIC
        at = (com < PR) | (com > (N - 1) - PR)
    elif rule == 'both_ends_20': # reflection-SYMMETRIC, fixed 20-site windows
        at = (com < 20) | (com > (N - 1) - 20)
    elif rule == 'both_ends_frac':  # reflection-SYMMETRIC, 5% of the chain
        at = (com < 0.05 * N) | (com > (N - 1) - 0.05 * N)
    elif rule == 'near_only':    # reflection-BREAKING (B1095's shape)
        at = com < 20
    return int((loc & gap & at).sum())

print("\nS3 — COUNTS UNDER FOUR DETECTORS (three reflection-symmetric, one not):")
print(f"    {'detector':<26s} {'reflection-sym':>15s} {'right':>6s} {'left':>6s} {'equal':>6s}")
rows = []
for rule, sym in (('both_ends', True), ('both_ends_20', True),
                  ('both_ends_frac', True), ('near_only', False)):
    a = count(PRr, comr, gsr, medr, rule)
    b = count(PRl, coml, gsl, medl, rule)
    rows.append((rule, sym, a, b))
    print(f"    {rule:<26s} {str(sym):>15s} {a:>6d} {b:>6d} {str(a==b):>6s}")
sym_equal = all(a == b for r, s, a, b in rows if s)
asym_rows = [(r, a, b) for r, s, a, b in rows if not s]
print(f"\n    every reflection-SYMMETRIC detector ties: {sym_equal}")
print(f"    the reflection-BREAKING one: {asym_rows}")
assert sym_equal

print("""
S4 — THE VERDICT: OUTCOME A-FORCED.
  THE ASYMMETRY IS IMPOSSIBLE, NOT MERELY ABSENT.  At a reversal-closed
  window H_L = J H_R J with J orthogonal, so the left hand's states are
  the exact reflections of the right hand's: same energy, same
  localization length, same gap environment, position mirrored
  (com_L = N-1-com_R, verified to 1e-6).  ANY detector whose criterion
  treats the two ends alike therefore assigns the same verdict to psi and
  J psi, and THE TWO COUNTS ARE EQUAL BY CONSTRUCTION — three different
  reflection-symmetric detectors are exhibited tying, and the one
  reflection-BREAKING detector is exhibited splitting.
  CONSEQUENCE FOR L173, and it is the whole point: memo 137 conceded two
  of the three parts of the differential and found the COMPLEMENTARY
  SPLIT alone surviving.  That part now collapses too — and for THE SAME
  REASON as the first: it follows from the halves being reversals of each
  other, with no object-specific content.  ALL THREE PARTS OF L173's
  DIFFERENTIAL REDUCE TO 'THE TWO HALVES ARE REVERSALS'.
  WHAT SURVIVES, stated exactly: the STATEMENT that the two hands bind
  the same energies at opposite ends is TRUE and is B1095's own
  formulation (energies P-invariant, localization P-equivariant).  It is
  just not DISTINCTIVE: it is J-conjugation, which holds for any word
  whose halves are reversals.  A NUMBER cannot be extracted from it,
  because every reflection-symmetric way of counting is forced to tie.
  FENCE: this is a statement about REVERSAL-CLOSED windows (N = 987
  here).  At odd Fibonacci index the reversal identity fails at the two
  cut-adjacent letters, H_L != J H_R J, and the theorem does not apply —
  which is exactly where an asymmetry could still live, and is named here
  as the one place left to look.""")
