# Run integrity log

1. Wrote and locally hashed PLAN.md before running verify.py. This was a verification plan after analytic reasoning, not an externally sealed blind prediction.
2. Initial run produced the expected outcomes. Two trivial Frobenius-Schur entries were represented as Float(1.0) because Python evaluated integer twist division before SymPy conversion. The nontrivial -sqrt(2) obstruction was already symbolic and unchanged.
3. Corrected the checker to sympify twists before division. Added a test rejecting floating-point atoms in the symbolic modular/fusion/indicator data. Reran all tests: exact indicators are now [1,1,-sqrt(2)]. No verdict changed. Initial output is retained in attempts/.
4. Added an independent D2 lattice coefficient calculation, agreeing with free-fermion oscillator products through relative q^16. This cross-check was an explicit post-plan verification extension.
5. Added COVER_ADDENDUM_PLAN.md and verify_cover.py after the main run: 10 exact groups passed; compactification genus three and invariance under L and R verified.
6. Reran the main script at 100 decimal digits. Symbolic results unchanged; numerical residuals decreased with precision.
7. Added PARITY_ADDENDUM_PLAN.md and verify_parity_conjugacy.py after the cover run: eight exact groups passed. The differential-operator consequence is an analytic theorem only under the stated identical gauge-covariant-domain assumptions.
