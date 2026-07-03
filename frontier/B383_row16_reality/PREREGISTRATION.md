# B383 (D3 residue) — PRE-REGISTRATION: the row-16 reality theorem

**Committed before the computation. Target: PROVE t(16,b) ∈ ℚ(√5) for all b — the sharpest
named residue of the selection-rule arc (P60's row-16 darkness, so far data not theorem).**

## The route (the formula angle, new since B382)

Row 16's DFT window is 5-torsion only: ζ₂₀^{−16j} = ζ₅^{−4j} (16 ≡ 0 mod 4). Define the
τ₃-anti part of the Par-table: for each cell, Canti[j,l] := the (√−3, √−15)-component pair of
C[j,l] (exact, via the H-decomposition applied cell-wise — cells live in ℚ(ζ₆₀), so "anti part"
means (C − τ₃C)/2 with τ₃ the √−3-flip on the FULL field, computed as the appropriate
Galois-average difference).

**T1 (the finite proof).** Σ_j ζ₅^{−4j} ζ₁₂^{−lb} · Canti[j,l] = 0 for ALL b — equivalently
the row-16 line of the anti-table's DFT vanishes identically. If this holds cell-exactly it IS
the theorem at level 15 (finite exact verification). KILL: any b with a nonzero anti-component.

**T2 (the mechanism).** Exhibit the symmetry of Canti forcing the kill: candidate — the
j-support/period structure of Canti under j → j+5 (the ζ₅-window sees only j mod 5 classes;
a cancellation pattern inside each class forces T1). Report the exact pattern found, or
NO-PATTERN if T1 holds without a visible one-line mechanism.

**T3 (the scope check).** The same window argument applies to rows 0 and 4 (also ≡ 0 mod 4) —
but rows 0 and 4 are NOT dark (they carry z,s in the 3-block... row 4's bright cells are in
b ∈ {4,8}). So the window alone cannot be the mechanism; T2's pattern must be row-16-specific
(e.g. the ζ₅^{−4j} vs ζ₅^{−j} exponent class distinguishing 16 from 4). This asymmetry is the
registered acceptance test for any claimed mechanism: it must explain 16 dark AND 4 bright.

## Outcomes (two-outcome discipline)

- T1 passes ⇒ the row-16 reality theorem is PROVED (finite exact verification) — bank + lock;
  T2/T3 sharpen it to a mechanism or leave it as verified-finite.
- T1 fails ⇒ the banked row-16 darkness is support-specific (only the stored cells are real) —
  itself a sharper statement; bank the failing b's exactly.

Machinery: the B382 table code (par_trace, DFT) + seam_certification's Galois tools. Exact
throughout; locks from the output JSON. Firewall: a statement about the level-15 theta model.
