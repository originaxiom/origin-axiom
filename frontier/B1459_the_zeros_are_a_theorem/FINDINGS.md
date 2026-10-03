# B1459 — THE ZEROS AT THE COMPLETE POINTS ARE A THEOREM, NOT A CENSUS

**Verdict: PROVED** (scope: frame F-CI; object the 188 complete, doubly parabolic points of B1451 on 16 levels of
word states, with B1446's 24 on the root covered by the same argument and not re-run; reach *class* — every tensor
product of SL(2) factors irreducible on the fibre with a fibre character, at a doubly parabolic point of any
once-punctured-torus bundle). cc (main), 2026-10-03. Lead L242 (a), part; L242 (c) paid. Sealed as
`PREREGISTRATION.md` at `70ca9c92` before any level was run.

## 0. Seen first

As sealed (PREREGISTRATION §0): the repo by `topic_sweep.py "vector-like|period-2|charge conjugation|doubly
parabolic|complete point|cusp invariant|t0 = 0"` — *VERDICT topic-sweep: 33 of 1330 arcs on main match (NEGATIVE 3,
PROVED 30)* — read at verdict level and, for B1297, B1444, B1446, B1451, B1455, in the FINDINGS: the three lines
L1–L3 are B1297's (homeomorphism invariance, oddness under duality, vanishing on self-dual modules and when the cusp
has no invariants — "t0 = 0 ⇒ 0"); the zeros at 24 + 188 complete points are observed there, not derived. The
literature: none needed, the argument is three lines of the record's own and a finite computation; nothing was
searched and nothing is cited from outside the record. The open item this pays is the audit lane's R58-6, "the
vanishing of the class index on irreducible modules — a proof or a counterexample".

## 1. The theorem

Let M be a level of a word state, F its fibre, Φ the monodromy on F = ⟨x, y⟩, π₁(M) = F ⋊_Φ ⟨t⟩. The fibre's elliptic
involution ι: x ↦ x⁻¹, y ↦ y⁻¹ is central in Out(F), so there is a word c ∈ F with

  c · Φ(ι w) · c⁻¹ = ι(Φ w)  for all w,   and   ι̃: (x, y, t) ↦ (x⁻¹, y⁻¹, c t)

is an automorphism of π₁(M), induced by the fibre-preserving homeomorphism −id of the bundle (−id on the torus
commutes with the linear monodromy exactly). For a module V = ρ_ℓ ⊗ ρ_η ⊗ χ, with ρ_ℓ, ρ_η SL(2) points of two periodic
curves (irreducible on F, B1444 Theorem A) and χ a fibre character: ι*ρ|_F has the character of ρ|_F (tr w⁻¹ = tr w in
SL(2)), so is conjugate to it by a Y unique up to sign, and the meridian of ι̃*ρ is ρ(c)T; by Schur, Y ρ(c) T Y⁻¹ = ε T
with ε = ±1, so **ι̃*ρ ≅ ρ ⊗ ε**. A fibre character satisfies χ∘ι = χ⁻¹. Hence

  ι̃*V ≅ ρ_ℓ ⊗ ρ_η ⊗ χ⁻¹ ⊗ ε_ℓε_η = V* ⊗ ε,   and by B1297's L1, L2:   I(V) = I(ι̃*V) = I(V* ⊗ ε) = −I(V ⊗ ε).

- ε = +1: I(V) = −I(V), so **I(V) = 0**.
- ε = −1: V ⊗ ε has meridian −T. At a doubly parabolic point T is unipotent, −T has no eigenvalue 1, the cusp
  ⟨t, [x, y]⟩ fixes no vector of V ⊗ ε, and I(V ⊗ ε) = 0 by B1297's identity; so **I(V) = 0** again.

Both branches close. The statement needs: a once-punctured-torus bundle (for ι̃), SL(2) factors irreducible on the
fibre (for Schur), and, in the ε = −1 branch only, a unipotent meridian (the complete points). It does not need the
sign to be computed — but the sign is what the computation was for, and it is where this arc had to correct itself.

## 2. What was run, in order

**The sealed script** (`verification/zeros_are_a_theorem.py`, `zeros_are_a_theorem.json`, log `_run.txt`), after a
post-seal **loader repair** of two lines: B1451 stores each coordinate as the string of an mpc at 30 digits, which
`mpc()` cannot parse (`mpmathify()` does, at full precision), and 30 digits are not on the curve to the engine's 1e−30
(each point is polished by the engine's own Newton step at its stored κ, a move of ~1e−30 along the curve). Nothing
in the computation was touched. Result on all 16 levels: 188 points, 376 factors, **ε = +1 at every factor**, the
recomputed I(V) = 0 at every point (rank gaps ≥ 5e−21 against ≤ 1.5e−29), zero failures, VERDICT PASS.

**Then the correction.** The sealed detector compares Y T_ι Y⁻¹ with T where *both* T and T_ι are the engine's
trace-normalised intertwiners (tr ≥ 0). Trace is conjugation-invariant, so Y T_ι Y⁻¹ = ε T forces ε = +1 wherever
tr T ≠ 0 — which at a parabolic point it always is (±2). **The sealed ε could not return −1 on its population.** This
is the E82 class (a criterion that cannot fail on its domain), sealed with P2 ("both signs occur") at 60% and
unexamined; the one-line argument that P2 could not come out as the detector would report was available before the
seal. Recorded in the ERROR_LEDGER. The sealed §2 also promised two controls "through the same code path"; the sealed
script writes them as sentences (lines 98–100), it does not run them. Both shortfalls are the seal's, stated here as
the seal's.

**The post-seal instrument** (`verification/geometric_sign.py`, `geometric_sign.json`, log `_run.txt`) computes the
sign the seal meant. On each level it finds the word c by free-group conjugacy (cyclic reduction and rotation on
Φ(x)⁻¹ against ι(Φ x), filtered by the y-relation; found and **unique on all 16 levels**, asserted exactly as an
automorphism on both generators), forms the pullback's meridian M = ρ(c)T, checks (ι*ρ, M) is a module with the
curve's sign character to 1e−25, and reads **ε_geo from Y M Y⁻¹ = ε_geo T** (equal to tr(ρ(c)T)/tr T, which came out
±1 to 1e−59 at every point). Result: **ε_geo = +1 at 239 factors and −1 at 137; ε_geo(V) = +1 on 111 points and −1
on 77**; each of the 110 distinct points carries one sign across its couplings. **On all 77 twisted points I(V ⊗ ε) = 0
with meridian −T (gaps ≥ 0.109 against ≤ 6.3e−59) and the cusp of V ⊗ ε fixes no vector.** Zero failures, PASS.

**The twisted-branch control** (`verification/twisted_branch_control.py`, `.json`, written before the geometric sign,
when the branch looked unexercised): on −LLRLR level 1, 12/12: the cusp of V fixes ≥ 1 vector (the detector of cusp
invariants can return non-zero), the cusp of V ⊗ ε fixes none, I(V ⊗ ε) = 0, and the sign detector's residual to +T is
≤ 3.4e−60 while to −T it is ≥ 2.0 (its branches are separated; the trivial-sign result was not a tolerance artefact,
it was a normalisation theorem).

## 3. The predictions, graded

| | sealed | prior | outcome |
|---|---|---|---|
| P1 | ι*ρ ≅ ρ ⊗ ε with ε = ±1 exactly at every point | 99% | **PASS** — by the sealed detector and by the geometric one (376/376 each) |
| P2 | both signs occur across the 376 factors | 60% | **FAIL as sealed** (the sealed detector returns +1 by construction); **TRUE geometrically** (239 : 137) |
| P3 | where ε = −1, I(V ⊗ ε) = 0 and the cusp of V ⊗ ε fixes no vector | 90% | **unexercised as sealed; PASS geometrically** on 77/77 |
| P4 | the recomputed I(V) is 0 at every point with resolved ranks | 99% | **PASS** 188/188 |
| **P5** | **every one of the 188 zeros follows from L1–L3 and the signs** | 90% | **PASS** — 111 by the ε = +1 branch, 77 by the ε = −1 branch, each branch computed on its own points |

The W₁ control the seal named (B1455's counted non-split module, I(W₁) = −1, I(W₁*) = +1, no Θ_σ fixing it) stands as
B1455's computation, cited; it was not re-run here, contrary to the seal's wording.

## 4. What this changes on the record

- **The zeros at the complete points are a theorem**: B1446's 24 and B1451's 188 are consequences of B1297's three
  lines and the fibre's elliptic involution, on every level computed and on the class. The record's phrase for them
  changes from "observed zero" to "zero by B1459". The vanishing statement the audit lane asked for (R58-6), with its
  hypotheses, is §1 — L242 (c) paid; it is a statement about SL(2)-type tensor modules at unipotent meridians, not
  about every irreducible module (B1455's W₁, non-split, counts −1 and is outside it).
- **A count needs a point where the argument fails**: a module not of the form ρ_ℓ ⊗ ρ_η ⊗ χ with SL(2) factors
  (non-split extensions, as the seats' counted configurations all are), or, for the ε = −1 modules, a meridian that is
  not unipotent (away from the complete points). Which of the 110 points carry ε_geo = −1 is in `geometric_sign.json`
  per curve; the pattern is not read here.
- **Still owed under L242 (a):** B1447's sixteen non-self-dual modules of index zero, which are not of this form and
  are not covered; L242 (b) the covers M₃–M₆; L242 (d) m202.

## 5. Errors in this arc

1. The sealed sign detector was normalisation-blind (E82 class); caught after the run by reading the result, repaired
   by a post-seal instrument that computes the word c. The theorem did not depend on it; the data did.
2. The sealed §2 described controls the sealed script did not execute.
3. The sealed script's loader could not read the population's own files (two-line repair, post-seal, disclosed).
