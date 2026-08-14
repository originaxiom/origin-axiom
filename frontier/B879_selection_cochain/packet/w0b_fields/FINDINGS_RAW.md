# W0b — THE FIELD TABLE — FINDINGS (raw)

Seat cc3, SELECTION & QUANTUM-COCHAIN CAMPAIGN, cell W0b. Sealed prereg: `PREREG_SCC.md`.
Code: `w0b_fields.py`. Full per-class data: `w0b_table.json`. Run transcript:
`w0b_run.log`. Repo `origin-axiom` was not touched (read-only per rules);
W0a's output was **not** read or depended on — the word family below was
regenerated independently from the family definition in the prereg.

All arithmetic is exact (Python arbitrary-precision integers); trial-division
factorization and primality tests, no floating point anywhere.

---

## 0. The word family (regenerated independently)

Matrices: `R = [[1,1],[0,1]]`, `L = [[1,0],[1,1]]` (both in SL(2,Z), det 1).
A word `w = w_1...w_n` maps to `M(w) = M(w_1)·M(w_2)···M(w_n)`. Trace is
invariant under cyclic rotation of the word (`tr(ABC) = tr(BCA)`), so a
canonical representative per rotation-class is enough to fix the trace.

Enumeration = primitive (aperiodic) binary necklaces over `{R,L}`, length
2..12, one canonical (lexicographically-least-rotation) representative per
necklace. Counted two independent ways that must agree, and did:

1. Brute force: generate all 2^n words per length, keep the ones that are
   both (i) their own lexicographically-smallest rotation, and (ii) aperiodic
   (no proper divisor `d | n, d<n` with `s[i] = s[i mod d]` for all i).
2. Moreau's necklace-counting formula (independent closed form):
   `M(n,2) = (1/n) · sum_{d|n} mu(d)·2^(n/d)`.

Per-length counts (both methods agree for every length):

| length | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| count | 1 | 2 | 3 | 6 | 9 | 18 | 30 | 56 | 99 | 186 | 335 |

**TOTAL = 745 primitive cyclic {R,L}-words, length 2..12, up to rotation.**

All 745 have det(A)=1 (checked, exact) and trace > 2 strictly — i.e. every
class is genuinely hyperbolic (trace != 2, in fact trace > 2 with no
exceptions). Zero classes were excluded as parabolic; the "hyperbolic
classes only" filter turned out to be automatically satisfied by every
primitive word of length >= 2 in this family (expected: any word using both
letters at least once, with strictly positive matrix entries, cannot be
parabolic unless it's a pure power of a single-letter word, which primitivity
already excludes for n>=2). This was verified computationally, not assumed.

**Note on the count vs. W0a:** this run did not read W0a's table (its output
directory was empty at the time of this run). 745 is the count implied by the
family definition alone (binary necklaces, primitive, length 2..12, up to
rotation only) — cross-checked twice above — and should match W0a's count
under the same definition. If W0a reports a different number, the
discrepancy is in the family definition, not in the counting method (both
methods here agree with each other independently).

Also confirmed: `tr^2 - 4` is never a perfect square for any trace value
occurring here (checked implicitly — no `d = 1` ever appears; algebraically,
`tr^2 - m^2 = 4` for integers `tr > 2, m >= 0` forces `(tr-m)(tr+m)=4` with no
solution besides the excluded `tr=2,m=0`). So every one of the 745 classes
gives a genuine real quadratic field, never a rational (split) eigenvalue.

---

## 1. Quadratic subfields of Q(zeta_24) — derivation

Used the conductor–discriminant fact for quadratic fields: for squarefree
`m != 0,1`, define `disc(m) = m` if `m ≡ 1 (mod 4)`, else `disc(m) = 4m`.
Then `Q(sqrt m) ⊆ Q(zeta_n)` **iff** `disc(m)` divides `n` (a Dirichlet
character of conductor c factors through `(Z/nZ)^*` iff `c | n`, and the
quadratic character attached to `Q(sqrt m)` has conductor `|disc(m)|`).

Computed by brute-force scan (`quadratic_subfields_of_zeta_n(24)` in the
code): every squarefree `m` in `[-24, 24]` with `disc(m) | 24`. Result —
**exactly 7** quadratic subfields, confirmed independently against the
group-theory count (`Gal(Q(zeta_24)/Q) ≅ (Z/24Z)^* ≅ (Z/2Z)^3`, which has
`2^3 - 1 = 7` subgroups of index 2, hence exactly 7 quadratic subfields):

| m | disc | field |
|---|---|---|
| -1 | -4 | Q(i) |
| -2 | -8 | Q(sqrt -2) |
| 2 | 8 | Q(sqrt 2) |
| -3 | -3 | Q(sqrt -3) |
| 3 | 12 | Q(sqrt 3) |
| -6 | -24 | Q(sqrt -6) |
| 6 | 24 | Q(sqrt 6) |

This also matches a second, purely structural derivation: `Q(zeta_24) =
Q(zeta_8)·Q(zeta_3)` (compositum, since 24 = 8·3, coprime), `Q(zeta_8) ⊇
{Q(i), Q(sqrt2), Q(sqrt-2)}` and `Q(zeta_3) = Q(sqrt-3)`. The Galois group is
elementary abelian of rank 3 with generators corresponding to `sqrt(-1),
sqrt(2), sqrt(-3)`; the 7 nontrivial products of these generators (mod
squares) are exactly `-1, 2, -3, -2(=(-1)(2)), 3(=(-1)(-3)), -6(=(2)(-3)),
6(=(-1)(2)(-3))` — the same 7 fields.

**Correction to the prereg's working list**: the prereg text lists "Q(i),
Q(sqrt2), Q(sqrt-2), Q(sqrt3), Q(sqrt-3), Q(sqrt6), Q(sqrt-6), Q(sqrt-1)" —
eight names, but `Q(sqrt-1) = Q(i)` are literally the same field, so that
list actually names only 7 distinct fields, matching the derivation exactly
(no discrepancy in substance, just a repeated final entry in the prereg's
prose).

**Since every d in our word family is positive** (all fields here are real,
`tr^2-4 > 0`), only the **real** subfields matter for intersection:

> **Real quadratic subfields of Q(zeta_24): d ∈ {2, 3, 6}. Nothing else.**

Because `Q(sqrt d)` is degree 2 over Q, "linearly disjoint from Q(zeta_24)"
is exactly equivalent to "not a subfield of Q(zeta_24)" (a quadratic field
has no proper nontrivial subfields, so its intersection with any Galois
extension is either itself or Q). So for our family:

> `Q(sqrt d)` is linearly disjoint from Q(zeta_24)'s quadratic subfields
> **iff `d ∉ {2, 3, 6}`.**

---

## 2. Classification of every d in the family

Computed per class (see `w0b_table.json`, field `classes`, one entry per
word): `trace`, `disc_D = tr^2-4`, exact factorization of D, `squarefree_d`,
`conductor_f` (D = f²·d), `field_discriminant` (d if d≡1 mod4, else 4d),
`ramified_primes`, `is_golden` (d=5), `is_silver` (d ∈ {2,3,6}),
`in_Qzeta24_quadratic_subfields`, `linearly_disjoint_from_Qzeta24`,
`field_discriminant_is_prime`.

- **Golden class** (d=5): 16 of the 745 words land here. Ramification
  character: `5 ≡ 1 mod 4` ⟹ disc = 5 itself (prime, single ramified prime
  {5}). Smallest-trace representative: word `LR`, length 2, trace 3 — the
  canonical tr=3 word that the rest of the campaign is built around.
- **Silver classes** (d ∈ {2,3,6}, i.e. squarefree with prime factors ⊆
  {2,3}): d=3 has 18 words (the single largest degeneracy class in the whole
  table), d=2 has 17 words, d=6 has 12 words. All three ARE subfields of
  Q(zeta_24) (confirmed above), matching the prereg's "cyclotomically
  entangled" expectation exactly.
- **Ramification character (mod 4)**: of the 146 distinct d values, those
  with `d ≡ 1 (mod 4)` have field discriminant = d itself; all others
  (d ≡ 2 or 3 mod 4) have field discriminant = 4d. A field discriminant of
  the form 4d is **never** prime (4d ≥ 8 always has factor 4), so **prime
  field discriminant is only possible when d ≡ 1 mod 4 and d itself is
  prime** — this collapses condition (b) of the golden question (below) to
  a clean number-theoretic test.
- All other d values (140 of the 146) are neither golden nor silver — d's
  range from 7 up to 71285, most composite, most with 2+ distinct prime
  factors, spanning both ramification classes.

---

## 3. Field degeneracy

**146 distinct eigenvalue fields Q(sqrt d)** among the 745 classes (so most
fields are hit by more than one word — massive degeneracy is the norm, not
the exception).

Largest degeneracy classes (d : how many of the 745 words share it):

| d | field | word count | smallest-\|trace\| representative |
|---|---|---|---|---|
| 3 | Q(sqrt3) | 18 | `LRR` (length 3, trace 4) |
| 2 | Q(sqrt2) | 17 | `LLRR` (length 4, trace 6) |
| 5 | Q(sqrt5) | 16 | `LR` (length 2, trace 3) |
| 21 | Q(sqrt21) | 16 | `LRRR` (length 4, trace 5) |
| 15 | Q(sqrt15) | 14 | `LLRRR` (length 5, trace 8) |
| 6 | Q(sqrt6) | 12 | `LRLRR` (length 5, trace 10) |
| 34 | Q(sqrt34) | 12 | (length 10, trace 70) |
| 35 | Q(sqrt35) | 12 | `LLRRRRR` (length 7, trace 12) |
| 39 | Q(sqrt39) | 12 | (length 9, trace 50) |

Only **1 of the 146 fields is a singleton** (hit by exactly one word out of
745): **d = 65**, realized only by the length-12 word `LLRLRLRRLRLR`
(trace 258). Every other field is shared by at least 2 words. (Full grouping
— all 146 d-values, every member word, smallest-trace representative for
each — is in `w0b_table.json` → `field_degeneracy.groups`.)

Note: the golden field (d=5, 16 words) is comfortably mid-pack in
degeneracy rank (3rd largest), *not* uniquely singled out by degeneracy
count — its distinction (below) is purely arithmetic (prime discriminant +
zeta-24-disjointness), not a "rarity of realization" effect.

---

## 4. THE GOLDEN QUESTION — sealed, answered, NOT softened

**Question:** is d=5 the only d in the family whose field is (a) linearly
disjoint from Q(zeta_24)'s quadratic subfields AND (b) has prime field
discriminant?

**Condition (a)** — linearly disjoint from Q(zeta_24): d ∉ {2,3,6}.
Satisfied by **143 of the 146** d-values (everything except the 3 silver
values 2, 3, 6).

**Condition (b)** — prime field discriminant. Since disc = 4d is never
prime, this reduces to: d ≡ 1 (mod 4) **and** d itself prime. Scanning all
146 d-values, the set satisfying this is:

> **{5, 13, 17, 29, 37, 53, 173, 229} — 8 values, not 1.**

**Joint (a) AND (b):** since none of {2,3,6} appear in the prime-discriminant
set anyway (2 and 3 are prime but 2≡2, 3≡3 mod 4, so their discriminants are
8 and 12, not d itself; 6 isn't prime), the joint set equals the condition-(b)
set exactly:

> **Joint set = {5, 13, 17, 29, 37, 53, 173, 229}. 8 values.**

### Verdict: **NO — the golden claim as stated is FALSIFIED.**

d = 5 is *not* the only value satisfying both conditions in this word
family. Seven other values do, each with realizing words:

| d | disc | word count | smallest-trace representative | trace |
|---|---|---|---|---|
| 5 | 5 | 16 | `LR` | 3 |
| 13 | 13 | 7 | `LLLRRR` | 11 |
| 17 | 17 | 7 | `LLLRLRRRLR` | 66 |
| 29 | 29 | 3 | `LLLRRRLR` | 27 |
| 37 | 37 | 6 | `LLRRLRRLRLR` | 146 |
| 53 | 53 | 4 | `LLLRRRRLLR` | 51 |
| 173 | 173 | 2 | `LLLRLRRRLRLR` | 171 |
| 229 | 229 | 2 | `LLRRLLRRLRLR` | 227 |

**What is still true, and may be the intended finer claim:** d=5 is the
*smallest* value in this set, and by a wide margin the *most realized*
(16 words vs. 2–7 for the others) and the one with the smallest-magnitude
representative trace (3, vs. 11 for the next, d=13). If the sealed claim is
read as "d=5 is the smallest / minimal / most-common such field" rather than
literally "the only one," that narrower claim **holds** in this data: 5 is
the minimum of the joint set, and its word-count (16) strictly dominates
every other member's word-count. But the literal "ONLY" claim as posed does
not survive — this should be reported to D-B synthesis (Wave 1) without
softening, per the prereg's falsifier instruction. Whether some *additional*
constraint beyond "(a) disjoint + (b) prime discriminant" (e.g. minimality
of trace, or a bound on word length shorter than 12, or an additional
selection criterion from the W0a table such as amphichirality/unit-det) is
what actually pins down d=5 uniquely is a question for Wave-1 D-B synthesis,
which has the full W0a criteria table to cross the two.

---

## Anomalies / things worth Wave-1's attention

1. **The golden-question falsifier above** — the literal "only d=5" claim is
   false in the length ≤ 12 window; 7 counterexamples exist, growing sparser
   with length (d=173, 229 need length-12 words; d=29 only 3 realizations).
   This looks like it could be an artifact of the length cutoff (12) — the
   density of {prime ≡ 1 mod 4, disjoint from zeta_24} discriminants
   realized by short words may just be low, and d=5's dominance may be a
   "smallest / shortest word" phenomenon rather than a true field-theoretic
   uniqueness. Recommend Wave-1 check whether the *other* W0a criteria
   (amphichirality, unit-det, prime-conductor) intersected with this set
   still leaves only d=5 — i.e. the uniqueness may live in the conjunction
   of *all* the selection criteria, not the eigenvalue-field criterion alone.
2. **d=65 is the only totally non-degenerate field** (single realizing word,
   length 12) — worth flagging in case Wave-1 wants a "generic vs.
   exceptional" split independent of the golden question.
3. Field degeneracy is very high overall (146 distinct fields across 745
   words, average ~5.1 words/field) — the eigenvalue field is a coarse
   invariant; most of the combinatorial richness of the word family is
   invisible at this level and only shows up in conductor / word-length /
   trace data (already recorded per-class in the JSON for Wave-1's use).
