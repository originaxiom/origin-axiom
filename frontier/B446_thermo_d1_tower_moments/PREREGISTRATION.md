# B446 — PREREGISTRATION: the tower moment law + the twisted SFF (Thermodynamic Campaign, D1)

**Committed BEFORE computation. Firewalled; nothing to `CLAIMS.md`. Campaign: docs/OPEN_LEADS.md
§"The thermodynamic campaign"; frame: speculations/S054.**

## The question (blind)

The program's value theory (B358/B367/B402) banked only FROZEN slices of the quantized golden cat
map at level 15: exact values, number fields, support counts. The missing layer is statistical: the
**distribution of Hecke-eigenstate matrix elements and its moments as a function of the level N** —
the object's quantum-variance structure. Three sub-questions:

- **Q-a (the tower law).** Along the fixed-cofactor tower `N = 15·3^k` (the seam tower, B372/B376),
  what law do the desymmetrized second and fourth moments obey? Pilot evidence (2026-07-06 review,
  to be RE-DERIVED here, not trusted): `N·Var = C₃·S₅` exactly (a CRT fixed-cofactor product law),
  with kurtosis DRIFTING away from the prime-N Kurlberg–Rudnick value 2 — i.e. the tower's limiting
  law is NOT the KR SU(2) law. Derive the law symbolically (CRT factorization of eigenstates +
  the fixed 5-dim ramified factor), verify numerically at ≥4 tower levels, state it as a lemma.
- **Q-b (the joint stratum).** Higher JOINT moments across Hecke orbits at composite N — the stratum
  where only conjecture-level support exists (KR's SU(2)-trace limiting law is conjectural beyond
  the 4th moment). Numerics can support, never decide; framed as certified-instrument data.
- **Q-c (the twisted SFF).** The spectral form factor of `U_N(A)`, untwisted vs parity-resolved
  (Par is a Hecke operator; eigenstates are parity-definite). The untwisted SFF's non-RMT structure
  is PREDICTED to be the banked Pisano law P59 (`ord(A mod N) = π(N)/2` forces massive eigenphase
  degeneracies) — a pre-registered launder-control. The parity-resolved/twisted SFF along the tower
  is the uncomputed piece.

## Registered outcome split (three bins, fixed now)

1. **LAUNDERS** — every measured law is exhibited as an explicit closed-form
   `F(whitelist ∪ class-data)` under the campaign's burden-inversion rule (F complexity-capped,
   reproduces to working precision, predicts out-of-sample at a second m AND a second level).
2. **NEW-MATH** — a law (expected candidate: the Q-a fixed-cofactor product law) that is genuine,
   derivable, previously unwritten (lit-gate below), but carries no independent physical content →
   bank as mathematics, firewalled.
3. **H1-candidate** — an un-launderable structure surviving BOTH controls → escalate under the B398
   discipline (independent adversarial recompute, p<0.01 null, owner present) BEFORE voicing.

**Prediction (stated for honesty):** Q-a lands in NEW-MATH (a derivable CRT lemma); Q-c untwisted
lands in LAUNDERS (= P59); Q-b and Q-c twisted are open with LAUNDERS the strong prior (the atlas:
`units_scale` 45/45 firewall, `observable` 7/7).

## The emergence bar (four-part, binding)

A result is H1 only if (i) forced, (ii) unsought/blind, (iii) an exact match to a *specific*
physical structure (not a generic mod-d or RMT-deviation fact), (iv) survives BOTH controls.
Anything short = a named negative or a NEW-MATH bank.

## Controls (fixed now, computed alongside — never after)

- **Simpler-system:** prime-N KR reproduction (the gate, doubling as the generic-arithmetic
  control) + a NON-Hecke (arbitrary-basis-in-degenerate-space) run showing basis-dependence — the
  desymmetrization-necessity exhibit.
- **Same-class:** the silver cat map `A₂ = R²L²` (trace 6) run through the identical pipeline at the
  same N values (prime gates + a 3-power tower) — is the law's FORM shared with silver (class-generic;
  only constants differ, as functions of m) or golden-specific?
- **m-scan hook:** constants exported per-m for D2's classifier.

## Reproduce-gates (known numbers, must pass before any object claim)

- Prime N: Hecke-desymmetrized `N·Var(f) → Σ_{ν≠0}|f#(ν)|²` (Kurlberg–Rudnick 2005, Annals 161;
  arXiv:math/0302277); for `f = cos 2πx` in the parity-coherent normalization the pilot target is
  `N·Var → 1.000`, `m₄/m₂² → 2.00` (Sato–Tate/SU(2) 4th moment).
- Unitarity + exact Egorov of the Weil-formula quantization at odd N (residuals ≤ 1e-12).
- Hecke commutant order = (8/3)·N at tower levels; commutators ‖[U,H]‖ at machine zero.

## Lit-gate (the campaign's mandatory line)

Nearest published computations: KR 2005 (prime N, variance theorem + SU(2) conjecture);
Gurevich–Hadani 2011 (QUE rate); **Olofsson 2008/2009 (prime-power levels)**; KR math/0701685
(short windows at general composite N). **Our delta: the FIXED-COFACTOR tower `N = 5·3^{k+1}`
product law and its moment drift — believed unwritten.** A focused literature search for
"fixed-cofactor / CRT product law for quantized cat map matrix elements" runs BEFORE the lemma is
claimed as new; if found published, Q-a rebins from NEW-MATH to a citation-confirm.

## Machinery + discipline

- Weil-formula quantization `U(B)_{jk} = N^{-1/2} e_N(inv(2b)(ak² − 2jk + dj²))` for odd N,
  `gcd(b,N)=1`; Hecke operators from norm-one units `a + bA` of `ℤ[A]/N`; joint diagonalization
  (Schur + block rotation). **Documented trap (pilot):** LAPACK splits exact degeneracies at ~3e-8 —
  clustering tolerance 1e-6 (distinct true phases are ≥ 2π/ord separated); naive 1e-8 silently
  yields parity-violating "eigenstates."
- Precision: float64 pipeline cross-checked at one tower level with mpmath (the B445 dps-cliff
  lesson); any rank/degeneracy decision re-verified at high precision.
- Sizes: tower N = 45, 135, 405, 1215 (+3645 if needed); prime gates N = 1201, 2003.
- Everything scripted in this directory; FINDINGS.md + test lock + V-number on bank.

## MB-guards

MB12 (vacuity): each sub-question's split can fire AND fail — Q-a's lemma can fail (pilot could be
a pipeline artifact), Q-c untwisted is the pre-registered launder (its "success" is H0a evidence,
not a discovery). MB7/MB8 (numerology/level-conflation): no value-matching against physical
constants anywhere in D1; the seam/level-15 banked tables are whitelist, not targets.
