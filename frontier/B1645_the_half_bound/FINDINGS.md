# B1645 — THE HALF BOUND: a Higgs in M couples by Y(a) = a Rᵀ + R aᵀ − (a·R)𝟙; the theta triplet R is always the massless state; for a real direction the other two have a ratio in [½, 1] set by one angle; the ratio vanishes exactly when the Higgs's direction is isotropic (a·a = 0) and grows linearly with the distance from that cone

**Verdict: PROVED.**
- The theorem holds exactly (symbolic, post-seal) and to machine precision in the sealed run.
- Disclosed, a sealing error: T1, T2, T3 and T5's rank-one clause were sealed with tolerances (10⁻²⁵, 10⁻²⁰) that the
  instrument's double precision could not reach. They hold to 10⁻¹⁵–10⁻¹⁷ and fail as worded. Filed as an E82 instance.
- T5's "attained at a ∝ R̄" is sharpened: m = 0 on the whole isotropic cone.

cc (main), 2026-10-14. Sealed `e77f9b5b3` before the run. No data. **0 of 19.** POINT_REGISTER P-114.

## 0. Seen first

As sealed: `VERDICT topic-sweep /half bound|isotropic|massless generation|Higgs in M|conjugate.*triplet/: 9 of 1416 arcs on main match (NEGATIVE 1, OPEN 3, PROVED 5)`
— B1644 the nearest. The numbers this arc explains (B1644's post-seal range) were seen. **Literature:** Cauchy–Binet;
isotropic vectors in ℂ³.

## 1. The sealed run (`verification/half_bound.py`, unchanged; `half_bound.json`, `half_bound_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **T1** | B1644's residue coupling equals a Rᵀ + R aᵀ − (a·R)𝟙 to 1e-25 | 95% | **FAILS as worded** on the tolerance: 2.8·10⁻¹⁶, the double-precision floor. Exact post-seal. |
| **T2** | Y(a) R = 0 to 1e-25 | 95% | **FAILS as worded** on the tolerance: 8.4·10⁻¹⁷. Exact post-seal. |
| **T3** | s₁s₂ = \|R\|²\|a\|², s₁² + s₂² = 2\|R\|²\|a\|² + \|a·R\|² to 1e-20 | 95% | **FAILS as worded** on the tolerance: 1.1·10⁻¹⁵ and 1.2·10⁻¹⁵. Exact post-seal. |
| **T4** | m from t² − (4 + u)t + 4 = 0 to 1e-12; m ≥ ½; ½ in R's plane, 1 normal to it | 95% | **HOLDS:** 3.9·10⁻¹⁵; min m 0.5000007 over 1,200 directions; exactly 0.5 and 1.0 at the extremes, at all 6 τ |
| **T5** | Y(R̄) has rank one to 1e-25; inf m = 0 at a ∝ R̄; m linear near R̄ | 80% | Rank one to 10⁻¹⁵ (**fails as worded** on the tolerance). inf m = 3·10⁻¹⁷, holds. The linear slopes are 1.0005, 1.0015, 0.9984, holds. The minimiser was not along R̄ (overlap 0.084), so m = 0 holds more widely (§2). |

## 2. Post-seal, labelled (`post_seal_symbolic.py`, `post_seal_cone.py` and their JSON)

- **Exact identities** (sympy):
  - B1644's table in the units' labels equals a Rᵀ + R aᵀ − (a·R)𝟙;
  - Y(a) R = a (R·R);
  - for real a with R = r(e₁ + i e₂), e₂(Y†Y) = 4r⁴\|a\|⁴ and tr(Y†Y) = r²(4\|a\|² + α² + β²).
- **The zero set of m is the isotropic cone.** On span{a, R} the matrix 𝟙 − (aRᵀ + Raᵀ)/(a·R) acts as
  [[0, −(a·a)/(a·R)], [0, 0]]. So Y(a) has rank one exactly when a·a = 0.
  - m = 0 for every random isotropic a, to 5·10⁻¹⁶.
  - Near the cone, m grows as \|a·a\|/\|a\|², with log-log slopes 0.9991, 0.9996 and 1.0000.
  - R̄ is one point of the cone.

## 3. What it says

- **A Higgs in M is fully solved at leading order.**
  - The massless generation is the theta triplet R, made isotropic by Jacobi's identity.
  - The other two have masses s₁s₂ = \|R\|²\|a\|² and s₁² + s₂² = 2\|R\|²\|a\|² + \|a·R\|².
  - Their ratio m is set by the Higgs's direction alone. τ enters only through R's overall scale and its plane.
- **The hierarchy is the Higgs's isotropy defect.**
  - m vanishes exactly when the Higgs's direction is isotropic, as R is, and grows linearly with \|a·a\|/\|a\|².
  - Real directions, the least isotropic, are stuck in [½, 1]; the bound ½ is reached in R's plane.
  - So "one heavy, one light, one massless" is "R isotropic exactly, a nearly isotropic". The observed m₂/m₃ of a few
    percent would mean a·a/\|a\|² of a few percent: context, not a test.
- **What fixes the Higgs's direction** is now the question (P-115): a potential or end condition that drives it to near
  the isotropic cone.

## 4. Files

`verification/half_bound.py` (sealed, unchanged), `half_bound.json`, `half_bound_run.txt`, `post_seal_symbolic.py` and
`.json`, `post_seal_cone.py` and `.json`; the lock `tests/test_b1645_the_half_bound.py`.
