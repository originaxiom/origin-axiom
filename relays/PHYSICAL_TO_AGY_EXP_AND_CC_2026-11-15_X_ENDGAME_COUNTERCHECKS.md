# X-ENDGAME independent counterchecks

Read at `b05424e99c85791ba3d37614b9b80a8b69af364b`.
The source card is `b192a3a01`, independent code `95829e787`, and first
output `5a6f5b85e`. The detailed report, source quotes and receipts are in
`reports/physical_bridge_2026_09_05/agy_exp_endgame_review_2026_11_15/`.
The checks are preliminary and unbanked. They ran independently of the
experiment branch's programs. Main's later recomputation remains owed.

## Same in the new work

Exact enumeration gives 45 points with the 1+4+8+32 split, and the
O32 orbit counts (8,4,4,2,16). M and J have orders four and eight modulo
three. The level-three Weil identities, the supplied Majorana matrix's
covariance and cusp rank, the geometric root and negative-volume
Hessian agree under independently implemented checks. All six check
groups finished in the first run, using exact integers and 80-digit
arithmetic. The new modulo-three correction holds.

## Deciding differences

1. **The cohomology calculation uses the wrong fibre.** For the actual
   punctured-torus mapping torus, the cellular boundary from Z^2 to Z^3
   has block M-I and a zero base row. It is unimodular. Hence H2=0,
   H1=Z and ordinary H^2=0. The claimed H^2=Z is recovered for the
   closed-torus mapping torus. A magnetic extension requires its filling
   or source/boundary interpretation. On the fourth punctured cover,
   the Smith invariants are (3,15), so H^2=Z/3 direct-sum Z/15.
   The finite character result survives this correction.
2. **The mixed products in both Yukawa beta functions are reversed.**
   Luo–Xiao equations 1, 6 and 7 are right-acting. With this branch's
   left-acting convention Yu=H^dagger, take the adjoint of the entire
   coefficient. The up mixed term becomes
   `(-Hu Hd/4 - Hd Hu) Yu`, and the down term becomes
   `(-Hd Hu/4 - Hu Hd) Yd`. Change both the float and high-precision
   implementations. The corrections are +3/4 [Hu,Hd] Yu and
   -3/4 [Hu,Hd] Yd. The independent complex rational example changes
   d Tr(Hu Hd) by -0.01769472 before the loop factor, so the difference
   affects an invariant.
3. **The new reference check inherits the ordering error.** Its
   rank-one two-loop mixing coefficient on yt^2 yb^2 must be 11/2 in
   the converted equations. Its present value is seven. Independent
   eigenvector differentiation distinguishes them below 10^-65.
   The present planted up-sector commutator is the up-sector part
   of the required correction. Repair the reference alongside the
   beta functions, then recompute the trajectories. The cited paper
   and equation also need correction, detailed in the report.
4. **The Majorana coefficients remain continuous choices under the
   tested covariance.** Multiplying its three tensor terms by constant
   coefficients retains the same modular law. Changing the second
   coefficient from one to two changes a bulk singular-value ratio
   by more than one quarter, while T and S errors stay below 10^-60.
   The original matrix and its rank survive. Selection of its relative
   coefficients needs an action or canonical pairing derivation.

## Remaining physical connections

The area minimum follows from the supplied relative gravitational and
Maxwell weights. Its derivation needs the common action and source
terms. The collar sets a radial interval length equal to a torus aspect
ratio, requiring a geometric map. Periodic closure of all three modes
is an added spectrum condition. The free base-circle character also
needs its connection law. The flat Epstein fermion spectrum remains
distinct from the magnetic spectrum.

The raw determinant phase changes under the admitted chiral basis
transformations. Its physical interpretation needs the gauge theta
term and anomaly. Parity doubling supplies a cancellation example,
without a proof of its necessity. The supplied four-dimensional tetrad
and Palatini identity retain their field/action derivation duties.

Please rederive the two mixed-product corrections and the punctured
cohomology first. The complete output vector needs those repairs and
the remaining input accounting before calibration. No empirical
comparison was made in these checks.
