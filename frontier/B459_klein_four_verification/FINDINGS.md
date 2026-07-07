# B459 — the "Klein-four selection rule" addendum: arithmetic VERIFIED, mechanism identified, dictionary HELD

**Status: banked (frontier). Firewalled. Verifies the 2026-07-07 addendum bit-for-bit and
corrects its interpretive layer. No H1; the physics dictionary is HELD per the standing rules.**

## Verified exactly (`verify_patterns.py`, exact ℚ(ζ₆₀))

FT-ing each of the four genus-channel coordinates (1, √5, √−3, √−15) of the banked pair seam
(B358/B367 machinery) to the dual boundary torus ℤ/20×ℤ/12:

| pattern (channels zero) | count | claimed | ✓ |
|---|---|---|---|
| {} | 120 | 120 | ✓ |
| {√−3, √−15} | 20 | 20 | ✓ |
| {√5, √−15} | 20 | 20 | ✓ |
| {√5, √−3, √−15} | 10 | 10 | ✓ |
| all four | 70 | 70 | ✓ |

**5 of 16 patterns occur** ✓. **Law 1** (no single vanishing): PASS. **Law 2** (√−15 dies in
every nontrivial pattern): PASS. The √−15-dead total = 120 = exactly B431's banked dark count
(the addendum is a refinement of banked structure) ✓.

## The mechanism, identified (the correction that matters)

**The five patterns are exactly the SUBFIELD LATTICE of ℚ(√5,√−3)** (verified: set equality):
{} = generic value · {√−3,√−15}=0 ⟺ value ∈ ℚ(√5) · {√5,√−15}=0 ⟺ value ∈ ℚ(√−3) ·
{√5,√−3,√−15}=0 ⟺ value ∈ ℚ · all ⟺ 0. A biquadratic field has exactly five subfields —
that is where "5 of 16" comes from.

- **The addendum's "Law 3 is a consequence of the algebra" is FALSE as stated**: component-wise
  vanishing is not multiplicative (√−15 itself has q=r=0, s≠0). The honest statement: *every
  dual-torus value lies in a subfield*, and the subfield lattice automatically carries the
  Galois group's structure — the "group law closure" is equivariance, not a miracle. "You
  cannot accidentally reproduce a group's multiplication table" inverts the truth: an
  equivariant construction reproduces it automatically. The Klein four here is the banked
  genus-Galois group — the program's central laundering mechanism (K020) — re-derived.
- **The genuinely NEW empirical facts** (not lattice-forced, banked here): (i) every value lies
  in a subfield or is generic — no partial-vanishing configurations exist; (ii) **the
  ℚ(√−15)-valued pattern is ABSENT** (verified: no point has q,r dead with s alive) — no point
  of the dual torus is purely seam-valued; (iii) the tier counts (120, 20, 20, 10, 70). These
  are exact selection-rule refinements of B431 — S053-lens material (kernel structure), real
  and bankable as arithmetic.

## Dispositions (per the standing rules)

- **HELD(value-matching)**: "17:6:1 ↔ CKM:PMNS:strong-CP", and any C/P assignment of the Galois
  elements (the addendum itself admits the assignment is unknown). ℤ/2×ℤ/2 ≅ C×P is a
  structural predicate that cannot fire alone (B452's frozen rule); it is also the automorphism
  group of every biquadratic field — the weakest possible structural match.
- **Prior for the unshared computation** ("24 pairs quantized at √3, √5, √(5/3)"; "53 forbidden";
  "88→24"): the claimed quantized ratios are |√−3|, |√5|, |√5/√−3| — the basis elements'
  absolute values, i.e. channel-occupancy-forced. Unverifiable until that computation is shared;
  the burden-inversion rule will apply to it on arrival.
- **Naming**: "the Spirit" (for the parity operator Par) stays in the speculation room; FINDINGS
  keep the operator's name. The observer/measurement Concept-Atlas card already covers the
  Par-insertion fact.
- **The enhanced-Probe-2 request** (Galois-decompose CS(V₁/V₂); ℤ/2³ = "C×P×T"): folded into
  E5 (B458, running) — the ℚ(√−7) flip on the V₁/V₂ pair is E5's prereg'd pairing gate; a
  direct product of Galois groups exists tautologically, so "extends to C×P×T" is a naming until
  a coupling observable is named — HELD.

## Reproduce
```
python3 verify_patterns.py     # exact; prints the table + all checks
pytest ../../tests/test_b459.py
```
