# P-268 — a prediction for B1713's stored output, written before that output is read (2026-10-22)

cc (main). Committed and pushed before B1713's stored model output (the JSON its sealed instrument writes) is read. B1713's run was in progress at this commit. Its outputs are unread, and no model value on a line of order 1–7
was computed by main for this note.

## The candidate law (from B1712's order-12 zero, read after B1712's run)

**Where it comes from.**
- By B1659's determinant law, det Y = 4 det S det M tr(εSMᵀ). In B1656's four-channel matter M = Σ u_s E_s*, with
  u_s = √(2πL + c_s) R_s, one has det M = ¼ (2πL Σ R_s² + Σ c_s R_s²).
- The first sum vanishes for every twist, because the residue matrix has rank one.
- The first generation is therefore massless for every Higgs exactly when D = Σ c_s R_s² = 0.

**The mechanism read from order 12.**
- **The left field.** A field's two theta components carry the characteristics a and a + ½. When the left twist has
  exact order 4 (a ≡ ±¼, or the same in the second slot), the involution u ↦ −u exchanges them.
- **The right field.** When the right twist is 2-torsion, the involution fixes each of its components up to sign.
- **The result.** P_{s·q}(u) ∝ P_s(−u) for a fixed quaternion q. The channels pair with equal regularised norms and
  residues in the ratio ±i, so D cancels.

**The law (conjectured).** In B1656's four-channel frame at B1667's canonical end, a sector's first generation is
exactly massless, for every Higgs, at every τ and on both horocycles, when its left twist q_L·w has exact order 4 and
its right twist q_R·w has order at most 2.

This fits all of B1712's stored output:
- the leptons (q_L, q_R) = (−3, 6) on every order-12 line, 48 of 48, where 3w has order 4 and 6w order 2;
- no zero in any sector on orders 8–11, nor in the quarks at order 12.

## The prediction for orders 1–7 (B1713's stored output)

1. **On every order-4 line (6 lines up to sign), all three sectors have an exactly massless first generation.**
   - Up quarks (1, −4): w has order 4 and −4w = 0.
   - Down quarks (1, 2): w has order 4 and 2w order 2.
   - Leptons (−3, 6): 3w has order 4 and 6w order 2.
   - "Exactly massless": the stored m₁/m₃ ≤ 10⁻¹² at every grid point, on both horocycles, and in every up reading.
2. **This mechanism gives no zero on any line of order 1, 2, 3, 5, 6 or 7.**
   - No prediction is made about other mechanisms: B1703's R₁ rule at leading order; the isotropy of the untwisted theta
     triplet at w = 0 (B1644). A zero found there will be reported as outside this law, not as a failure of it.
   - A zero on a line of order 2, 5, 6 or 7 that neither of those mechanisms names would count against the law's
     completeness.

**What would refute the law:** any order-4 line on which some sector's first generation is lifted (m₁/m₃ > 10⁻¹² at
some grid point).
