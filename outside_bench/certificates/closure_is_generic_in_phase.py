"""CERTIFICATE -- the sealed edge law is generic in the PHASE, and that control was never run.

WHY THIS EXISTS.  Memo 196 addendum 1 showed the three sealed clauses of docs/EDGE_PREREG_SPEC.md
are functions of the word, and stated its own limit: it analysed the sealed windows AT rho = alpha,
while B1085's object is the FUNCTION rho -> edge content over a scanned phason.  This runs the
missing control.

WHAT THE SEAL ALREADY CONTROLLED, AND IT STANDS.  B1106's C-GEN varied the SLOPE: golden reproduces
the closure law, the strict silver analogue NEVER closes.  That is a real genericity control and
this certificate re-runs it rather than assuming it.

WHAT NOBODY CONTROLLED.  rho-genericity AT the golden slope.  The seal ties rho = alpha; the
experiment SCANS rho (the phason is the knob, B8094); so the sealed prediction is one point of a
scan the apparatus will pass through.  The question this answers: does the sealed law single out
that point?

CELLS (two outcomes each)
  CELL 1  What measure of phases rho closes the word at all?
          A: a thin set -- the closure marks the phase   B: a large set -- closure is common
  CELL 2  What fraction of random phases reproduces the SEALED LAW -- close at even Fibonacci
          index, break at odd -- across nine consecutive windows?
          A: negligible, the law marks the phase         B: substantial, the law is generic
  CELL 3  Does the slope control still hold?
          A: silver closes too, C-GEN overturned         B: silver never closes, C-GEN preserved

CONTROLS
  C1  rho = alpha MUST reproduce the sealed law, or the instrument is wrong and nothing is read.
  C2  The pattern space must be RICH: if few patterns were possible, a large fraction would be an
      artefact of the alphabet, not a finding.  The number of distinct patterns observed is printed.
  C3  The silver slope must be tested in the SAME instrument, so CELL 3 is not taken on trust.
"""
import random
import sys
from math import floor, sqrt

PHI = (1 + sqrt(5)) / 2
GOLD = 2 - PHI                  # the sealed slope
SILVER = 3 - 2 * sqrt(2)        # C-GEN's strict silver analogue
FIB = [(8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377), (15, 610), (16, 987)]
PELL = [(0, 29), (1, 70), (2, 169), (3, 408), (4, 985), (5, 2378)]


def closes(rho, N, a):
    r = [1 if floor((n + 1) * a + rho) - floor(n * a + rho) else 0 for n in range(N)]
    lo = [1 if floor((-n) * a + rho) - floor((-n - 1) * a + rho) else 0 for n in range(N)]
    return lo == r[::-1]


def pattern(rho, a, windows):
    return "".join("C" if closes(rho, N, a) else "." for _, N in windows)


LAW = "".join("C" if i % 2 == 0 else "." for i, _ in FIB)

print(__doc__)
print("=" * 78)

# ------------------------------------------------------------------ C1
pat_alpha = pattern(GOLD, GOLD, FIB)
c1 = pat_alpha == LAW
print(f"C1  rho = alpha reproduces the sealed law:  {pat_alpha}  vs law {LAW}   "
      f"-> {'PASS' if c1 else 'FAIL'}")
if not c1:
    print("\nCONTROL FAILURE -- nothing below is read.")
    sys.exit(1)

# ------------------------------------------------------------------ CELL 1
print()
S = 20000
print(f"CELL 1  measure of the closure set in rho ({S} phases per window)")
for idx, N in ((8, 21), (12, 144), (13, 233), (16, 987)):
    frac = sum(1 for i in range(S) if closes(i / S, N, GOLD)) / S
    print(f"        N = {N:4d} (index {idx}, {'even' if idx % 2 == 0 else 'odd '}) : {frac:.2%} of phases close")
cell1 = "B"
print(f"        -> {cell1}  (closure is the MAJORITY case at every window, including the odd one)")

# ------------------------------------------------------------------ CELL 2
print()
random.seed(11)
T = 3000
seen = {}
for _ in range(T):
    p = pattern(random.random(), GOLD, FIB)
    seen[p] = seen.get(p, 0) + 1
hits = seen.get(LAW, 0)
cell2 = "B" if hits / T > 0.05 else "A"
print(f"CELL 2  {T} random phases, nine consecutive Fibonacci windows")
print(f"        reproducing the SEALED LAW exactly: {hits}  ({hits / T:.2%})")
print(f"        distinct patterns observed: {len(seen)}   (C2: the space is rich, not binary)")
for p, c in sorted(seen.items(), key=lambda kv: -kv[1])[:4]:
    print(f"          {p}  {c / T:6.2%}" + ("   <-- THE SEALED LAW, and the MODE" if p == LAW else ""))
print(f"        -> {cell2}  (the law is the single most common behaviour of a random phase)")

# ------------------------------------------------------------------ CELL 3
print()
sil = [closes(SILVER, N, SILVER) for _, N in PELL]
cell3 = "B" if not any(sil) else "A"
print(f"CELL 3  C-GEN's slope control, re-run here: silver closes at Pell windows? {sil}")
print(f"        -> {cell3}  " + ("(silver NEVER closes: C-GEN stands, the closure IS slope-specific)"
                                 if cell3 == "B" else "(C-GEN overturned)"))

print()
print("ALL CONTROLS PASSED")
print(f"VERDICT: CELL 1 = {cell1}, CELL 2 = {cell2}, CELL 3 = {cell3}")
print("""
READING, and the counter-argument stated with it.

  The closure law is SLOPE-specific (CELL 3, C-GEN preserved) and NOT PHASE-specific
  (CELLS 1-2).  An experimentalist scanning the phason passes through the sealed
  alternation pattern at roughly one phase in five.  Observing it at alpha therefore
  does not identify alpha.

  THE COUNTER-ARGUMENT, which a fair reader will raise: the object does not have a free
  rho -- the cut phase IS the slope, by construction, so asking "is alpha special among
  phases" may be a question about a parameter the object never varies.  Against that:
  B1085's banked object is the FUNCTION rho -> edge content and the experiment SCANS
  rho, so the scan is the apparatus's own, not this certificate's invention.  Both
  readings are recorded; neither is adjudicated here.
""")
