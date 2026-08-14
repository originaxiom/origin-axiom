# W0a THE SELECTION TABLE — FINDINGS (RAW)

Cell W0a, selection/cochain campaign, seat cc3. Enumeration: all primitive cyclic
words in {R,L}, length 2..12, up to cyclic rotation. R=[[1,1],[0,1]],
L=[[1,0],[1,1]]. Word w1...wn -> matrix product M(w1)*...*M(wn). Canonical
class rep = lexicographically minimal rotation ('L' < 'R'). Exact integer
arithmetic throughout (Python ints, trial-division factorization, Euler's
criterion for Legendre symbols, mod-8 rule for the p=2 Kronecker symbol).
No floats anywhere in this file or in w0a_table.json.

Full data: `w0a_table.json`. Code: `w0a_criteria.py`. Run log: `w0a_run.log`.

## 1. THE FALSIFIER — VERDICT: SURVIVES

Criteria checked per hyperbolic (mixed-letter, primitive) class: (a)
amphichiral by the word criterion (canonical(swap(reverse(w))) == w,
computed directly from the letters, not assumed from any other column),
(b) unit_det: |det(A-I)| = |2-tr| = 1, (c) prime_conductor: disc = tr^2-4
is prime.

- Golden word (RL): canonical rep `LR`, length 2, trace 3, disc 5 (prime).
  amphichiral=True, unit_det=True (det(A-I)=-1), prime_conductor=True.
- Classes checked: 745 hyperbolic primitive classes (lengths 2..12).
- Classes other than LR satisfying all three (a)+(b)+(c) simultaneously: **0**.
- **FALSIFIER STATUS: SURVIVES on the enumerated family (length 2..12).**
  No violation found.

## 2. NEAR-MISSES (exactly two of the three criteria)

**Count: 0.** No hyperbolic class in the length 2..12 family has exactly
two of {amphichiral, unit_det, prime_conductor} true.

This is not a coincidence of the search range but forced by an identity
visible directly in the table: disc = tr^2-4 = (tr-2)(tr+2). Every
hyperbolic class has trace >= 3 (minimum realized only by LR), so tr-2 >= 1
and tr+2 >= 5. disc is prime only if the smaller factor tr-2 equals 1,
i.e. tr = 3 — which among the 745 enumerated classes is realized by
exactly one class, LR itself. Consequently, on this table:
- unit_det is True for exactly 1 class: `LR`.
- prime_conductor is True for exactly 1 class: `LR`.
- these are the *same* class in every case observed (1 word each, identical word).

Because unit_det and prime_conductor coincide (both reduce to tr=3, and
only LR has tr=3 in the range checked), no class can have exactly one of
{unit_det, prime_conductor} true while lacking the other, and no class can
combine one of them with amphichiral to make exactly 2/3 without also
having the third (since the one class with tr=3, LR, has all three, and no
other class has either of the tr=3-linked properties at all). Hence the
near-miss bucket is structurally empty for this table, not merely
observed-empty.

## 3. AMPHICHIRALITY vs UNIT-DET: computed honestly, columns DIFFER

Per the prereg instruction, amphichirality was computed strictly from the
word criterion (reversal + R<->L swap, canonical form), independent of the
unit-det column. The two columns are **not** the same:

- amphichiral=True count: **53** classes (out of 745).
- unit_det=True count: **1** class (`LR` only).
- Mismatch count (amphichiral != unit_det): **52** classes — all of them
  amphichiral=True, unit_det=False (there are zero classes with
  unit_det=True, amphichiral=False, since the one unit_det class, LR, is
  itself amphichiral).

So amphichirality is a much weaker, more common condition than
unit-det(A-I); the golden word LR is simply the unique class where the
(rare) unit-det/prime-conductor condition and the (comparatively common)
amphichiral condition coincide.

Necessary condition observed directly from the word criterion: amphichiral
classes only occur at even length (2,4,6,8,10,12 — none at length
3,5,7,9,11). Reason visible in the table: swap(reverse(w)) has the R-count
and L-count of w exchanged; for the class to equal itself the R-count must
equal the L-count, forcing length even. This is necessary but not
sufficient — not all balanced (equal R/L count) primitive words at a given
even length are amphichiral.

Amphichiral class count by length:
- length 2: 1  (LR)
- length 4: 1  (LLRR)
- length 6: 3  (LLLRRR, LLRLRR, LLRRLR)
- length 8: 6
- length 10: 15
- length 12: 27
(full word lists in w0a_table.json / symmetry_orbits)

## 4. SUMMARY STATS

### Classes per length (hyperbolic primitive / parabolic / excluded-periodic-mixed)

| length | hyperbolic | parabolic | excluded (periodic, non-primitive mixed) |
|---|---|---|---|
| 2  | 1   | 2 | 0  |
| 3  | 2   | 2 | 0  |
| 4  | 3   | 2 | 1  |
| 5  | 6   | 2 | 0  |
| 6  | 9   | 2 | 3  |
| 7  | 18  | 2 | 0  |
| 8  | 30  | 2 | 4  |
| 9  | 56  | 2 | 2  |
| 10 | 99  | 2 | 7  |
| 11 | 186 | 2 | 0  |
| 12 | 335 | 2 | 15 |

Totals: **745 hyperbolic primitive classes**, **22 parabolic classes**
(11 lengths x 2, all-R and all-L), **32 excluded** non-primitive mixed
necklaces (periodic words such as (RL)^2, (RRL)^2, etc. — mixed-letter but
not primitive, so not part of the primitive-word family; tallied, not
detailed). Hyperbolic per-length counts match the Mobius primitive-necklace
formula (1/n) sum_{d|n} mu(d) 2^(n/d) exactly for every length 2..12.

Parabolic classes (R^n, L^n for n=2..12): trace=2, disc=0 for all; these
are excluded from every hyperbolic-analysis column (no conductor
primality, no character table — disc=0 has no prime factors; det(A-I)=0,
not a unit).

### Trace value distribution

- Distinct trace values among the 745 hyperbolic classes: **163**.
- Minimum trace: 3 (LR only). Traces grow quickly with length; most trace
  values are shared by 2, 4, 6, ... classes (average ~4.6 classes per
  distinct trace value); see `summary.classes_per_trace` in the JSON for
  the full histogram (163 entries).

### Which traces admit amphichiral classes

27 distinct trace values host at least one amphichiral class:
3, 6, 11, 15, 18, 27, 38, 39, 43, 63, 66, 70, 83, 87, 99, 102, 111, 147,
155, 162, 171, 183, 210, 227, 258, 259, 267.
(53 amphichiral classes total spread across these 27 trace values; e.g.
trace 102 hosts 5 distinct amphichiral classes, trace 63 hosts 4.)

### Prime-conductor classes

Count: **1** (`LR`, disc=5). No other class among the 745 has prime disc,
for the algebraic reason given in section 2 (disc=(tr-2)(tr+2), prime only
when tr=3).

## 5. Character table (Legendre/Kronecker), kappa = 4..15

Computed per hyperbolic class for every prime p | disc, via Euler's
criterion pow(kappa mod p, (p-1)//2, p) for odd p, and the mod-8
supplementary rule for p=2 ((kappa|2) = 0 if kappa even, +1 if kappa = +-1
mod 8, -1 if kappa = +-3 mod 8). Full compact tables are in
`w0a_table.json` under each class's `character_table` field, keyed by
prime then kappa.

Golden word LR (disc=5), verified by hand against known QRs mod 5
({1,4} are residues, {2,3} are non-residues):

kappa:      4  5  6  7  8  9 10 11 12 13 14 15
(kappa|5):  +1 0 +1 -1 -1 +1  0 +1 -1 -1 +1  0

This matches exactly (silent/zero at kappa in {5,10,15}, i.e. kappa
divisible by 5).

## 6. Anomalies / notes

- No violations of the falsifier were found. The golden-uniqueness claim
  (amphichiral + unit-det + prime-conductor jointly singling out RL)
  **survives** across all 745 primitive hyperbolic classes of length 2..12.
- The amphichiral column and the unit-det column are genuinely different
  predicates on this family (53 vs 1 true), computed independently per
  the prereg instruction; they coincide only at LR.
- All amphichiral classes found have equal R-count and L-count (forced by
  the swap step of the criterion), hence occur only at even lengths.
- Enumeration and per-length hyperbolic counts independently cross-checked
  against the closed-form Mobius primitive-necklace formula for every
  length 2..12 — exact match.
- Scope limit: this is an exhaustive check over length 2..12 only, as
  prereg-scoped. No claim is made here about lengths > 12.
