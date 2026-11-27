# CLAIM CARD — the line class (2/5, odd/10) is one cusp: b odd/10 is forced; α = 2/5 over 1/5 is one chosen Galois bit

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: negative
- touches: P-384 (with P-373's "a principle for α = 2/5, b odd/10"), P-845
- effect: conditions — P-384: the offset within the class is not a separate input; the slope's 2/5 over 1/5 is one
  bit that no unit-invariant object on record fixes, declared CHOSEN; order 10 rests on a minimality postulate
- scope: frame: no frame, the lines alone, with no rate or row of any frame computed; object: which rules in B1934's
  terms select the class among the 266 lines of order <= 12; reach: class; hypotheses: B1733's row convention
  (T acts as (a, b) -> (a, b - a)), and the cusp reading of the offsets is an inference for frame C only (SM-C23)
- identifications: "choosing a line" here is "choosing a cusp" in SM-C23's joint covariance (frame C only); the
  Higgs's twist here is e(3a), the Higgs's 6Y = 3 paired with the line's a, read in SU(5)'s centre (B1934 § 3)
- definitions: a line is a point v = (a, b) of (Q/Z)^2 taken up to sign, of order lcm of the denominators; a is the
  coordinate the cusp i∞ sees; K = {(2/5, b): b = 1/10, 3/10, 1/2, 7/10, 9/10}; the carriers are (2/5, 1/10) and
  (2/5, 1/2) (B1753); the p-part of v is e·v with e ≡ 1 mod the p-power of the order and ≡ 0 mod the rest; a rule is
  unit-invariant when its selected set is closed under v -> u·v for every unit u of Z/N, N the order of v; a cusp is
  an orbit of <T, −I>; the act's line is {k(1, 2)/5} (B1943); the unit twist is 3a ≡ ±1/5 mod 1; the least level is
  the least multiple of 5 at which (L, e) is not (Q, d) transposed mod N with 6Y = (Q 1, u −4, d 2, L −3, e 6);
  Π = order equal to the least level and the unit twist; Π_inv the same with 3a any non-zero element of (1/5)Z/Z
- imports: none (B1934's charges and Legendre table, B1943's act's line, both imported unchanged from main; numpy
  enters only through B1934's module)
- premises on main: B1934, B1943, B1733 (row convention), B1753, B1755, B1786; the SM seat's SM-C23 and SM-C24
  (frame C's joint covariance; the cusps that see the 5-part); the sealed card and run at relays/sm_r384/
- decisive script: relays/claims/sm_refile/r384_decisive.py, SHA-256 34577bcb3df465e7, depends on the standard library
  and numpy, run as python3 relays/claims/sm_refile/r384_decisive.py, output SHA-256 e5d72a6aacd26824
- decisive lines: 16 lines marked "DECISIVE:", SHA-256 e5d72a6aacd26824
- failing control: python3 relays/claims/sm_refile/r384_control.py
- second computation: none
- already on main?: `grep -il "unit-invariant\|Galois bit\|one cusp" frontier/*/FINDINGS.md` on be8c83d4f: 35 arcs,
  none on the class (2/5, odd/10) as a cusp or a bit; closest arcs B1753 (the referee's "mostly a pick") and B1934.
  Correction to the old page: its "all 11" unit-invariant rules (E5) is a miscount; the run has 12, none exactly K;
  E5 and the verdict stand
- what would make it fail: a unit-invariant rule that selects exactly the five lines of K (none of the 12 tested
  does), K's unit closure equal to K, K not a single cusp, or Π not selecting exactly K
