# SM-C6 E6 steps 1 and 2 — filling descent of the record's sector modules, and their count after filling

*Step card of SM-C6 (main's M13, M14, M18; SM-C5's entry E6 for GENESIS FK8). Pushed before the run. Data-free.*

## Step 1: which sector modules descend to which Dehn filling

- **The modules.** On a level of a signed word state, with presentation ⟨x, y, t | t x t⁻¹ = P(x), t y t⁻¹ = P(y)⟩
  (B1434), meridian μ = t and longitude λ = [x, y], take a sector module V(ℓ, α):
  - ρ(g) = [[α(g), c(g)β(g)], [0, β(g)]];
  - c is the class of H¹(G; ℓ) with c(λ) = 1, so that c(μ) = s(ℓ), the slope (B1438).
- **The descent condition.** On the boundary torus, ρ is unipotent: the characters are trivial there. So for a slope
  γ = μ^p λ^q:
  - ρ(γ) = I exactly when p·s(ℓ) + q = 0;
  - **V descends to a filling if and only if s(ℓ) is rational, s(ℓ) = a/b;**
  - and then to exactly one filling, along γ = μ^b λ^(−a).
- **What is computed:** for every non-trivial character ℓ on B1438's census levels (LR, LLR, LLLR, both signs, as in
  SM-C6 E1), whether s(ℓ) is rational, exactly in the cyclotomic field. The list of slopes that receive modules.

## Step 2: the count after filling

- For every descended module, with Fox calculus on the filled presentation (the relator γ added; complex arithmetic,
  rank by singular values):
  - dim H¹(M(γ); V);
  - set beside the module's count on M: n(V), the interior rank (B1438 A), and its based count (n(V), n(V*)) of E1.
- **A built-in check,** run first, without the filling: dim H¹(M; V) must equal 1 + [s(β) = s(ℓ)], as B1438's exact
  sequence gives.

## The outcomes (SM-C5's, made exact)

- **1:** some module descends, and its count carries, dim H¹(M(γ); V) = n(V). Filling descent then carries the
  record's count for those modules, and the join has a member beyond covers.
- **2:** modules descend, but dim H¹(M(γ); V) ≠ n(V) on them. The count does not carry: filling carries flat data
  only.
- **3:** no s(ℓ) is rational. Filling descent carries none of the record's backgrounds.
- **The prediction, written before the run:**
  - rational slopes occur on some levels, so not outcome 3;
  - the sub-module's class survives the filling exactly when n(V) = 1;
  - whether the class lifted from β survives is not predicted. So outcome 1 or 2 per module, reported as a census.

## Controls, which must fail

- **P1:** a wrong slope, γ′ = μ^(b+1) λ^(−a). ρ(γ′) must differ from I, so V does not descend, on every module tested.
- **P2:** the built-in check, run with the extension class set to zero. The rank must change on some module.
