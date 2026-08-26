# Progress bank — Campaign II, Wave 4 checkpoint

**Date:** 2026-08-26

**Source locks:** main `68383e80718e732e7cf5b9e57077a19dff753ad6`; outside-bench
`59680460721a0b9e4f672ad6e997724c226ceb56`; paper
`61a243c65f1a84c700e3c3d9755b11c30a5f0699`

**Status:** active hostile closure campaign; no parameter-free physics closure claimed

## Outcome

The canonical map now contains 120 typed questions:

```text
45 PROVED
40 REFUTED
13 CONDITIONAL
16 EXTERNAL_BLOCKER
 2 EMPIRICAL
 4 OPEN
```

Two former live questions close negatively and acquire correct replacement rows:

- OA-C1083: the constant `3-kappa` formula is not global; it is the parabolic specialization of
  the exact Riley sheet involution OA-C1092.
- OA-C1077: the merged arithmetic zero list is not one-GUE; the narrower two-component
  Wigner-surmise renewal compatibility is OA-C1093 and remains empirical.

## New exact mathematics

1. **Global Riley conjugacy.**  On the full component the deck involution is
   `z -> x^2+1-z` and sends `kappa` to `x^2-1-kappa=tr(ab^-1)`.  The defect of the constant
   cusp formula is exactly `x^2-4`.
2. **Complete fixed scheme.**  The trace-map fixed locus has three support points and scheme
   length four: the simple conjugate pair and the multiplicity-two origin.
3. **Paper-I arithmetic closure.**  The period-one locus is the determinant-minus-one locus;
   `A^2-I=mA` fixes the full mapping-torus Smith factors; the period-two relaxation still has
   a unique torsion-free member.  The old `m=12` class discrepancy is exactly proper versus full
   GL equivalence.
4. **Paper-II characteristic-zero closure.**  Torality and the single E6 A2 Weyl orbit transfer
   the charged fixed algebra to an exact rational arrangement.  The 109-flat, eleven-value rung
   spectrum is therefore exact over Q and Qbar, conditional on the specified principal-2T
   placement.  The distinguished `30 -> 46` plane enhancement is controlled by an irreducible
   cubic field.
5. **Fixed-frame cubic ledger.**  The E6 cubic support is exactly
   `40 (16,16,10) + 5 (10,10,1)` in the selected D5 x U(1)_psi frame.  Its frame parity is not
   beat-stable: 6 of 27 basis columns mix, while the tested lock remains stable.

## New negative controls

- Paper IV's literal cover-indistinguishability inference is false: normalized volume is an
  isometry invariant and scales with cover degree.  The narrower need for a physical conversion
  scale remains valid.
- Paper IV's claimed exhaustive fourteen-member Eisenstein shape-field census is false.  The
  scan stopped at index 1200; `s955` at index 1256 is an exact regular-shape counterexample.
- The claim that `H1=Z` uniquely separates `m004` over the true full family is now a correctly
  typed open computation, not a theorem inferred from a bounded list.
- Paper III's M-character identity is exact only in the direct Euler-product domain, giving the
  integer tail `k>=3`.  It does not construct the `k=2` value or a cusped graviton determinant.

## Four live finite computations

| row | exact obligation |
|---|---|
| OA-C1067 | Apply the complete semilinear Sigma to the banked 64-dimensional basis and compute its square. |
| OA-C1069 | Construct the geometric Pin-minus obstruction/torsor and affine restriction, not only its zero linear shadow. |
| OA-C1074 | Derive the completed zero-count formula and an explicit argument-principle error bound. |
| OA-C1103 | Run an exact full-census shape-field reconstruction and compare the seven declared invariants. |

These four are the remaining registry state `OPEN`; they are not the whole physical critical
path.  Rows already marked `CONDITIONAL` or `EXTERNAL_BLOCKER` still carry the decisive endpoint
debts.

## Revised closure route

The mathematical programme should continue on two lanes that must not be conflated:

1. **Exhaust finite algebra and census questions:** execute OA-C1067, OA-C1069, OA-C1074 and
   OA-C1103; keep branch deltas synchronized; turn every discovered residue into a typed child.
2. **Build the missing physics morphisms:** a four-dimensional realization functor; a selected
   chiral zero-mode/index calculation with three generations and no mirrors; an action and vacuum
   with anomaly cancellation and exotic mass ranks; then normalized couplings, running, masses
   and mixings.

The first lane can make the structure ledger exhaustive.  It cannot substitute for the second.
The current strongest honest thesis is still: the object supplies a rich conditional structure,
while no audited chain derives the full Standard Model or its measured values without additional
inputs.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 documents/program-question-map/render.py \
  --source documents/program-question-map/inventory/backbone.json \
  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \
  --as-of 2026-08-26 --check
```

The detailed source reconciliation is `WAVE4_BRANCH_DELTA_AUDIT.md`.
