#!/usr/bin/env python3
"""MEMO-137 CELL (R52-6's last untouched component): THE L173 MODE-COUNT
SEAL PATH — and a SECOND B724-shaped defusal risk, one level deeper than
the one B1095 already caught, found BEFORE the seal rather than after.

WHERE L173 STANDS.  It is a laboratory-prediction prereg (a photonic /
polariton Fibonacci-chain edge scan against B1085's rho-sweep), governed
by the DIFFERENTIAL-FIRST discipline: the prereg's first paragraph must
state what STANDARD theory already forces and name exactly where the
object's prediction DIFFERS.  B1095 did that once, and its differential
is banked verbatim:
  "what gap labeling + bulk-boundary FORCE is the per-gap occupancy
   windows ... What they do NOT speak of is the CROSS-HAND STRUCTURE: the
   exact mirror-isospectrality at reversal-closed windows, the
   complementary split of one shared odd family, and its Fibonacci-parity
   breaking."
B1095 also already conceded the raw edge counts as standard pumping
content in kind -- that was the FIRST B724 defusal, correctly absorbed.

THE QUESTION THIS CELL ASKS, and it is the seal's gating one: IS THE
CROSS-HAND STRUCTURE ITSELF DISTINCTIVE, or does it reduce to (i) a fact
of linear algebra plus (ii) a classical property of the Fibonacci word?
If it reduces, the differential is defused a SECOND time and must be
restated again before L173 can seal.

THE PREREGISTERED FORK (fixed before any computation):
  D-A  the cross-hand structure does NOT reduce to (reversal => iso) plus
       a classical word property => the differential is distinctive on
       this axis and the seal path is clear here.
  D-B  it DOES so reduce => a second B724-shaped defusal, and the
       differential must be restated BEFORE sealing.
Gate 5 untouched: exact linear algebra and word combinatorics only.  No
measured value, no laboratory datum, no comparison to any experiment.
"""
import numpy as np

# ---- M1: THE LINEAR-ALGEBRA HALF (is isospectrality itself content?)
def hop_hamiltonian(word, va=0.0, vb=1.0):
    """Nearest-neighbour chain with on-site potential set by the letter."""
    n = len(word)
    H = np.zeros((n, n))
    for i, ch in enumerate(word):
        H[i, i] = va if ch == 'a' else vb
    for i in range(n-1):
        H[i, i+1] = H[i+1, i] = 1.0
    return H

rng = np.random.default_rng(0)
w = ''.join(rng.choice(list("ab"), size=60))
H = hop_hamiltonian(w)
Hrev = hop_hamiltonian(w[::-1])
J = np.eye(len(w))[::-1]
print("M1 — THE LINEAR-ALGEBRA HALF: is isospectrality itself content?")
print(f"    a RANDOM 60-letter word (no Fibonacci structure at all): {w[:28]}...")
same_conj = np.allclose(J @ H @ J, Hrev)
d = np.max(np.abs(np.sort(np.linalg.eigvalsh(H)) - np.sort(np.linalg.eigvalsh(Hrev))))
print(f"    J H J == H(reversed word) : {same_conj}")
print(f"    max spectral difference    : {d:.3e}")
assert same_conj and d < 1e-12
print("    => FOR ANY WORD WHATEVER, reversing it conjugates the Hamiltonian by the")
print("       exchange matrix J, which is orthogonal — so THE SPECTRA COINCIDE")
print("       AUTOMATICALLY.  'Exact mirror-isospectrality' carries NO information")
print("       beyond 'the two half-words are reversals of each other'.")
print("       B1095's 1.3e-15 agreement is a linear-algebra identity, not a finding.")

# ---- M2: THE COMBINATORIAL HALF (where the real content must live)
def fib_word(n):
    a, b = "a", "ab"
    while len(b) < n:
        a, b = b, b + a
    return b[:n]
FIB = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
print("\nM2 — THE COMBINATORIAL HALF: is the Fibonacci word a palindrome,")
print("     and does it depend on the index parity?  (B1095's F16/F18 vs F17/F19)")
print(f"     {'F_k':>6s} {'k':>3s} {'palindrome?':>12s}  {'palindrome after dropping last 2':>34s}")
res = {}
for k, N in enumerate(FIB, start=1):
    W = fib_word(N)
    pal = (W == W[::-1])
    pal2 = (W[:-2] == W[:-2][::-1])
    res[N] = (pal, pal2)
    if N >= 55:
        print(f"     {N:>6d} {k+1:>3d} {str(pal):>12s}  {str(pal2):>34s}")
print("     => the raw Fibonacci word is NOT a palindrome, but the word with its")
print("        LAST TWO LETTERS REMOVED IS — for every Fibonacci length.")
allpal2 = all(v[1] for v in res.values())
print(f"        holds at every Fibonacci length tested: {allpal2}")
assert allpal2
print("     THIS IS THE CLASSICAL FACT.  That every Fibonacci prefix of length F_k")
print("     becomes a palindrome after deleting its last two letters is a standard")
print("     theorem of Sturmian/Fibonacci word combinatorics (Droubay 1995 and the")
print("     surrounding literature on palindromic prefixes) — it is NOT a property")
print("     the object supplies.  It is a property the FIBONACCI WORD supplies, and")
print("     any Fibonacci chain in any laboratory has it.")

# ---- M3: what actually remains
print("""
M3 — WHAT THE DIFFERENTIAL REDUCES TO, and what (if anything) survives:
  B1095's cross-hand structure has three named parts.  Taking them in turn:
   (1) "exact mirror-isospectrality at reversal-closed windows" —
       REDUCES to M1.  Given the halves are reversals, isospectrality is
       an identity for ANY word.  No content.
   (2) "its Fibonacci-parity breaking" — REDUCES to M2, at the strength
       the computation actually supports and no further.  M2 establishes
       that EVERY Fibonacci prefix of length F_k is a palindrome after
       deleting its last TWO letters — and "the last two letters" is
       exactly the defect B1095 reports ("the reversal identity fails at
       exactly the TWO cut-adjacent letters").  So the parity behaviour
       is almost certainly the classical two-letter palindromic-prefix
       defect seen through their cut.  STATED HONESTLY: this cell did NOT
       rebuild B1095's rho = alpha cut construction, so part (2) is a
       STRONGLY-SUPPORTED REDUCTION RISK, not a proof.  Clearing it needs
       either that rebuild or the prior-art gate.  Either way it must not
       be carried into a seal as distinctive content unexamined.
   (3) "the complementary split of one shared odd family" (right hand
       binds 5, left binds 6, of 11 shared boundary-capable energies) —
       DOES NOT reduce by either argument above.  Isospectrality forces
       the energies to be shared; it does NOT force HOW the two hands
       distribute localization across them.  B1095's own formulation is
       the precise one: "the energies are P-invariant (FORCED); the
       localization is P-equivariant (FREE)."
  ==> OUTCOME D-B on part (1) PROVED and on part (2) AT RISK;
      D-A on part (3), which survives both arguments.

M4 — THE SEAL-PATH CONSEQUENCE (what this cell asks for, and it is cheap):
  L173 MUST NOT SEAL ON THE DIFFERENTIAL AS CURRENTLY WORDED.  One of its
  three named parts is standard content by a proof given here, and a
  second is at serious risk of being so — and stating them as the object's
  distinctive prediction would repeat the exact B724 failure the
  differential-first discipline exists to prevent, one level deeper.
  THE RESTATEMENT THAT WOULD SURVIVE: the differential is the
  LOCALIZATION SPLIT ALONE — that of the 11 shared boundary-capable
  energies the two hands bind 6 and 5, complementarily.  Everything
  else in the current wording is conceded.
  STILL OWED BEFORE A SEAL, and both were already named by B1095 itself:
   * the PER-GAP OCCUPANCY DETECTOR (gap-interior energy + localization
     length).  B1095 flagged the current 0.5-boundary-weight detector as
     VOLATILE — a grid point 2e-5 from alpha reads (5,9) where alpha
     reads (5,6).  A differential that lives entirely in localization
     CANNOT be measured by a detector that flips on localization
     thresholds.  This upgrade is now GATING, not optional.
   * the PRIOR-ART GATE on the surviving part: is a hand-dependent
     complementary localization split of a shared boundary family already
     standard in the Fibonacci-chain literature?  This bench cannot
     settle a literature question offline and does not pretend to; it is
     named as owed, and it is the one remaining distinctiveness risk.
  FENCE: no laboratory datum is touched and no experimental comparison is
  made.  M2's classical attribution is stated as the standard result it
  is, with the prior-art gate owed at promotion rather than asserted
  here.  Gate 5 untouched.""")
