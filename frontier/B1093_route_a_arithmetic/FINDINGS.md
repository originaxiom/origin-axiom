# B1093 — ROUTE A'S ARITHMETIC, MAIN-BENCH PROVED (L169): every obstruction candidate trivial, with the class number now PROVED not cited

**Date:** 2026-08-20 · **Verdict: PROVED (own-code re-derivation, exact; one rigor upgrade beyond both prior benches; the counter identification remains the OWED residual)**

## What was proved from scratch (no PARI; sympy + hand-rolled algorithms)

K = ℚ[x]/(x³ − 12x − 5), the field classifying B990's rational orbit.

1. **disc = 6237 = 3⁴·7·11 and ℤ[θ] = O_K** — Dedekind's criterion at the sole
   candidate p = 3 passes (and passes again under an alternate lift: the robustness
   check the source never ran).
2. **h(K) = 1 PROVED** (the audit seat cited it banked; this bench proved it):
   Minkowski bound (2/9)√6237 ≈ 17.55; Kummer–Dedekind factorization of every p ≤ 17;
   all EIGHT prime ideals of norm ≤ bound exhibited PRINCIPAL with explicit generators
   (e.g. (2, θ+1) = (−1 − 2θ + θ²), (11, θ+2) = (−2 − θ)), each generator
   cross-validated numerically at 40 digits and ideal-membership-tested against its
   specific factor (resolving the two same-norm primes at 7 and 11 correctly).
3. **The units**: N(θ² + 2θ − 4) = +1 and N(3θ² + 6θ + 2) = −1 exact by three
   independent routes each; multiplicatively independent (log-determinant ≠ 0).
   Fundamentality ASSUMED-FROM-SOURCE and labeled — see 4 for why it no longer matters.
4. **The signature map is surjective, and the proof needs less than anyone claimed**:
   sign vectors sgn(−1) = (−,−,−), sgn(u₁) = (−,−,+), sgn(u₂) = (+,−,+) row-reduce to
   the 𝔽₂ identity — rank 3. **The rigor upgrade: surjectivity uses only that these
   are genuine units** (their signs already fill {±1}³, and the full unit group's sign
   image cannot exceed the codomain) — **h⁺ = h = 1 conditional ONLY on h = 1, which
   item 2 now proves.** |Cl/Cl²| = |Cl/Cl³| = 1 trivially.

## What this means for THE RANK WALL's Route A

B990's Route A ("shrink the group": count G(ℤ)-orbits inside the object's G(ℚ)-orbit —
if 1, the integral orbit is a canonical point up to G(ℤ), exactly what a VEV direction
needs) carried an UNFAVOURABLE prior. **Every class-group quantity that could obstruct
the count is now trivial at proof grade on this bench.** The obstruction is absent.

## The residual, unchanged and honestly owed

Trivial candidates make the count LIKELY, not proved: **identifying WHICH
Kato–Yukie/Bhargava-type quantity actually counts integral orbits in this
correspondence is the owed step** (L169's second half; literature lane — in the
owner-routed package's orbit). Until it lands, Route A reads: OPEN, UNOBSTRUCTED,
counter-unidentified.

**Locks:** the discriminant/Dedekind facts, the eight generators' norms and
memberships, the sign-vector rank — all fast exact assertions.
