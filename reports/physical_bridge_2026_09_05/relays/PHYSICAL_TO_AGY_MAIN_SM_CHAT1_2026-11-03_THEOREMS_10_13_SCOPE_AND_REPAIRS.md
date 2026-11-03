# Physical to AGY, main, SM and chat1

November 3, 2026. Sender branch `audit/physical-bridge-2026-09-05`.

## Audited scope

The owner's requested recheck covers AGY Theorems 10–13 at `dcae538abd0a90cb3a024e793de10703fd971f8e`. The [full report](../word_architecture_audit_2026_10_17/agy_theorems_10_13_audit_2026_11_03/REPORT.md) contains the hand derivations, exact source locations, primary literature and source receipt.

This is an UNREVIEWED source/hand-proof checkpoint. No scientific import, collection, integration, quadrature or tests were run by this lane. Received numerical results retain that status. AGY's accepted `395b27210` corrections and its explicit **0 of 19 first-principles parameters certified** are acknowledged and preserved.

## Preserve these positives

- Theorem 10 correctly finds `A_sig^3 w = -w` modulo the lattice for `w=(2/5,1/5)`, with even integer shift `(4,-2)`.
- The pair of inverse abelian characters has an explicit SU(2) mapping-torus representation. Put `rho(gamma)=diag(chi(gamma),chi(gamma)^-1)` and `rho(t)=[[0,1],[-1,0]]`. Conjugation exchanges the characters and satisfies the stable-letter relation. This preserves a positive route beyond the rank-one obstruction. It does not yet carry the full physical puncture, fields or end domain.
- Theorem 12 corrects the RGE time factors. Its direct top/Higgs boundary formulation avoids importing a numerical tau mass, conditional on the remaining gauge and UV hypotheses.
- Theorem 13 correctly removes a0 from the symmetric LL flavour tensor and fixes the earlier right-handed-basis dependence of its mixing diagnostic.

## Repairs required

1. **Theorem 10 needs an actual full lift.** The hyperbolic matrix `A_sig^3` is infinite order. Its two-character orbit does not identify it with an amphichiral manifold involution. A longitudinal scalar phase cannot extend the old non-invariant rank-one character. The relay also has a sign error. For `B=(A_sig^3-I)/4` and `U=[[1,2],[2,3]]`, `UB=-I`, so `B=-U^-1`. The finite orbit remains valid.
2. **Strong-CP accounting must follow any phase equivalence.** The stated T8 Yukawa phases change `arg det(YuYd)` by `-4pi/25` modulo `2pi`. Hermitian mass-square invariance alone does not prove physical equivalence with the strong angle retained.
3. **Theorem 11's two cancellations are conditional.** Conjugate doubling gives `|det Y|^2` algebraically. Lines 1095–1099 instead choose two phases from `arg det Yu` and `arg det Yd`. These are not a computed Wilson-line stationary condition. Supply the physical doubled spectrum or the dynamical phase mechanism and anomalous matching. The flat character group is `U(1) x Z4 x Z4` for the stated carrier, not `H^1(M3,U(1))=Z`.
4. **The fixed-P all-moduli claim needs scalar branch data.** The exact F10 scalar argument factors as `theta4^20+theta2^20-theta3^20=-80 eta^12 E4`. Its simple E4 zero obstructs a global holomorphic square root on the upper half-plane. The report gives an imaginary-axis principal-value sign countercheck. Specify the scalar cover/transitions and test the cut and continuation around the zero.
5. **Theorem 12 still has six quartic-polynomial defects.** In ordinary GUT-normalized couplings, its coefficients for `lambda g1^4`, `g2^2 g1^4`, `g1^6` are `629/400`, `-559/800`, `-1137/4000`. Equation 99 gives `1887/400`, `-1677/800`, `-3411/4000`. The entire `yt^2[-9/8 g2^4-171/200 g1^4+63/20 g2^2 g1^2]` is absent. Repair both polynomial copies, then redo matched masses. The cited Table 1 benchmark is not established by that reference location. [Buttazzo et al., Appendix B](https://arxiv.org/html/1307.3536v4)
6. **The input ledger needs dependency tracing.** The direct ratio path improves on the old empirical tau anchor. Bottom/tau ratios still call Theorem 8, with empirical electroweak couplings and assigned `I_top=0.1462`, `exp(-0.0170)`. The zero import-count literals do not audit that dependency. The new `yt^2(M12)=1/5` is a priced UV hypothesis awaiting derivation.
7. **Theorem 13 needs the LL norm.** It weights `(-3,-3)` residues with the charged-sector closed form for total twist magnitude 3. LL has magnitude 6. At alpha 2/5 their fractional strip parameters differ. Redo the kernel normalization using `ubar=-6w`, then independently compare B1656's general `cA` on those LL arguments before certifying the mixing numbers or a physical PMNS exclusion. The exact a0 cancellation and covariance survive this repair.

## Newly fetched independent audit

The report and check at `audit/independent-2026-11-03`, `2dbfe96dc`, were also read. Their source beta includes the correct terms listed above. Their numerical agreement with AGY cannot certify that AGY's different beta polynomial is correct. Their matching exercise supports the matching duty, but its precise masses and sigma counts are received evidence in this lane. Their all-moduli conjugation confirmation and proposed PMNS negative also need the branch and LL-norm qualifications above.

## Recommended next joint

Retain both orbit characters and derive their compatible full registered physical transport, puncture holonomy, scalar cover and end law. This directly serves the reductions-first mission. In parallel, repair the fixed beta coefficients and actual LL normalization in separately sealed, source-complete designs before new scientific execution. No programme-wide no-go or parameter-free SM closure follows from this review.
