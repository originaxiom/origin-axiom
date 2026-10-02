# B1455 — PREREGISTRATION: THE SELECTION RULE, AND THE TEST THAT DECIDES IT ON THE BRIDGE'S VACUA

**Sealed before any computation on the population.** cc (main), 2026-10-02. Source of the question: the web seat's
handoff "The selection rule, and the one test that decides it" (2026-10-02; zip sha256 `655959b2…e69499`, handed over
by the owner, not tracked). The handoff asks that the test be run independently, sealed first, by two routes with no
shared code, and that a negative be banked as a negative.

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "spontaneous|symmetry.breaking|SSB|mirror.{0,30}(pair|orbit|minim|vacu)|selector|
  selects one|invariant selector|plenitude|totalitarian" --refs`: *VERDICT topic-sweep: 62 of 1326 arcs on main match
  (NEGATIVE 11, OPEN 6, PROVED 44, RETRACTED 1); 6 other lanes match*. Read at verdict-line level: B128, B295, B849,
  B853, B1204, B1222, B1225, B1227, B1327. **The rule is on the record already**, as the handoff says of itself: an
  orientation-odd invariant of an amphichiral manifold is zero or 2-torsion (B1227, generalising B1224); no symmetry
  readable off the object selects within its own class (B1225); the earlier claimed symmetry breaking has no order
  parameter at the manifold level (B849); an invariant selector cannot pick a point of its own orbit, which says
  nothing about a relation to a second thing (B1327). **The test is not on main's record:** no arc computes the mirror's
  action on the vacua of an action.
- **The audit lane, read at `64a96ea6`** (its reports, not re-derived): the vacua are its harmonic family on Ballas'
  convex-projective representations ρ_q of the figure-eight group, q > 0, hyperbolic at q = 1. *Its R47 and R54:* an
  exact symmetric matrix S(q) with ρ_q(g)^{−T} S = S ρ_q(θg) for θ inverting both generators, so "the whole q curve is
  fixed by theta plus duality at the character level". *Its open checkbox since 2026-09-25:* "Test base-isometry plus
  duality before claiming unequal mirrors." *Its R54:* the longitude traces 3q + q⁻³ and 3q⁻¹ + q³; "distinct nearby
  q give distinct gauge orbits; the classical minima are non-isolated". *Its R76:* along the non-split extension
  scaled by t the potential is a·t² + c·t⁴ with a ≥ 0, c > 0, lowest at the split limit; a smooth stationary flat
  point of finite energy must be harmonic. *Its R57:* the potential (x² − 1)² as a logical control — no unique
  invariant choice does not mean no asymmetric solution.
- **Literature, read from the source.** Ballas, *Finite volume properly convex deformations of the figure-eight knot*,
  arXiv:1403.3314v3 (sha256 `36f54787…fba40`): pp. 1–2 and 17–19 read as pages; all 21 pages text-searched for "dual"
  and "orientation". It gives the generators 𝓜_t, 𝓝_t used here (p. 17), the hyperbolic structure at t = ½, the
  longitude l = ww^{op} = n m⁻¹ n⁻¹ m² n⁻¹ m⁻¹ n, a parameter s = log(1/(16t⁴)) (so q = 2t and q ↔ 1/q is s ↔ −s), and
  states that the ρ_s are pairwise non-conjugate (p. 2). **It says nothing about duality or about the knot's
  symmetries acting on the family.** Pantev–Wijnholt, arXiv:0905.1968, was read only through a machine summary of its
  HTML: F-terms F − [φ, φ] = 0 and D_A φ = 0, D-term D_A† φ = 0, superpotential the Chern–Simons functional of A + iφ
  (its eqs. 2.16–2.17, 2.25, as summarised). Not read: Ballas–Long (the extension to all s), Cooper–Tillmann, Corlette,
  Donaldson; where they are leaned on below it is as the audit lane cites them.

## 1. The question, made exact

The handoff: *does the bridge's action have a mirror-symmetric potential whose minima are not mirror-symmetric?*

**Which mirror.** For a local system V on M and an automorphism σ of π₁(M) induced by a self-homeomorphism of M,
σ*V is V pulled back. The class index I(V) = n(V) − n(V*) of the record (B1297, B1446) is built from ranks of
restriction maps, so:

- **L1.** I(σ*V) = I(V) for every such σ, orientation-preserving or not. *(A homeomorphism carries the pair (M, ∂M)
  and the local system to themselves.)*
- **L2.** I(V*) = −I(V). *(The definition.)*
- **L3 (the rule, as a statement about the index).** If V* ≅ σ*V for some such σ, then I(V) = 0.
  *(I(V) = I(σ*V) = I(V*) = −I(V).)* With σ the identity this is the vanishing on self-dual modules (B1297 §5.1's
  unitary case is an instance).

So the base mirror alone does not change the count; **the symmetry under which the count is odd is a base symmetry
followed by dualising.** Write Θ_σ(V) = (σ*V)*. These are the "mirrors" of the handoff's rule: its algebraic rows
(real, unitary, rational modules) are Θ with σ the identity, its geometric rows Θ with σ a symmetry of the manifold.

**The population.** Γ = ⟨m, n | m n m⁻¹ n⁻¹ m n⁻¹ m⁻¹ n m n⁻¹⟩, Ballas' ρ_q with q = 2t; the eight maps
(m, n) ↦ (m^a, n^b) and (m, n) ↦ (n^a, m^b), a, b = ±1; the four targets ρ_q, ρ_q*, ρ_{1/q}, ρ_{1/q}* (ρ* the
contragredient g ↦ ρ(g)^{−T}); and at the exceptional points the modules A = μ ⊗ ρ_q and the non-split extension W₁
of the trivial module by A (B1453's `join_own.py`).

**The computations, fixed now.**

- **C0, controls.** ρ_q is not conjugate to ρ_{1/q} for q ≠ 1 (Ballas: pairwise non-conjugate) and not to ρ_q*; at
  q = 1 all four targets are conjugate. If C0 fails the instrument cannot separate the outcomes and nothing below is
  read.
- **C1.** Which of the eight maps are automorphisms of Γ (the relator goes to the identity under the faithful ρ_q,
  q symbolic or at three rational values). Which preserve orientation: the character of the SL(2,ℂ) holonomy on words
  of zero exponent sum is preserved, or conjugated. What each does to the meridian m and to the longitude l up to
  conjugacy.
- **C2, the test.** For each automorphism σ and each target T: is ρ_q∘σ conjugate to T? **Route 1 (this seat):**
  equality of traces on every positive word of length ≤ 10 in the two generators (enough to separate conjugacy classes
  of pairs of 4 × 4 matrices), in exact rational arithmetic at q = 2, 3, 5/2, 7/3 and 1/5, and symbolically in q on
  words of length ≤ 4. **Route 2 (a separate implementation, written from this file alone, no shared code):** the
  space of intertwiners X with X·ρ_q(σ(g)) = T(g)·X for g = m, n, and whether it contains an invertible matrix.
- **C3, the follow-up.** At q₀ = 17 + 12√2 with the twist μ = −1: I(A), I(W₁), I(Θ_ι W₁) and I(ι*W₁) for ι the
  inversion of both generators, by B1446's index instrument at 60 digits, with the singular-value gap reported.

## 2. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | All eight maps are automorphisms; four preserve orientation and four reverse it. | 70% |
| P2 | (ρ_q∘ι)* ≅ ρ_q for every q, ι the inversion of both generators — the audit lane's R47, by this seat's code. | 95% |
| P3 | ρ_{1/q} ≅ ρ_q*: the dual of the structure at q is the structure at 1/q. Then the eight symmetries split in two kinds: those fixing the longitude fix every vacuum; those inverting it send q to 1/q, and after dualising fix it. | 65% |
| P4 | Among the four orientation-reversing symmetries both kinds occur: one bare mirror fixes every ρ_q, another exchanges ρ_q and ρ_{1/q} with the hyperbolic point q = 1 fixed. | 55% |
| P5 | I(A) = 0, I(W₁) = −1, I(ι*W₁) = −1, I(Θ_ι W₁) = +1. | 95% (L1–L3 and B1453) |
| P6 | **The outcome that matters: A.** Every vacuum of the harmonic family is fixed by a count-odd symmetry Θ_σ, so the index is zero on the whole family by L3; the configurations that count ±1 are the non-split ones, which are not minima. Chirality is not selected by this potential on this family. | 85% |

## 3. Registered outcomes (the handoff's, made exact) and the kill condition

- **A.** For every q some Θ_σ fixes ρ_q. Then by L3 no vacuum of the family carries a count, and the action on this
  family does not select. **This is the kill condition: it is banked NEGATIVE**, with its scope — the frame F-HE, the
  object m004's harmonic family at level one, and the hypothesis that the minima are the reductive points (the audit
  lane's R76 and Corlette's theorem as it cites it; not re-derived here).
- **B.** Some ρ_q (q ≠ 1) is fixed by no Θ_σ. Then the vacua come in pairs under every count-odd symmetry, and the
  follow-up is whether a count is carried by one member: I(V) ≠ 0 for a module V of the frame at a reductive point.
- **C.** The potential is not invariant: some symmetry σ of the manifold takes the family out of itself (ρ_q∘σ is
  conjugate to none of the four targets for any q′ in the family — tested through the longitude trace). Reported with
  where it breaks.

**Reported whatever the outcome:** what the bare mirrors do to the family (P4), because the handoff's protocol asks it
literally (step 4) and the answer may differ from the answer for Θ.

## 4. Disclosed before the run

- Already known to this seat: I(W₁) = −1 at **both** q = 17 ± 12√2 (B1453), and these two points are reciprocal.
  A bare exchange q ↔ 1/q therefore cannot be the symmetry that flips the count, which is what led to L1–L3.
- Already read: the audit lane's statement of P2 and its longitude traces, from which P3's shape was guessed
  (3q + q⁻³ at q is 3q⁻¹ + q³ at 1/q).
- Nothing on the population has been computed by this seat: no ρ_q∘σ, no intertwiner, no orientation character.
- L1–L3 are arguments, not outcomes; if C3 contradicts them the arc reports the contradiction first.
- The handoff's own numbers (its plenitude table, its eight-row table, its corrections) were read before sealing. They
  contain no result of this test: the handoff has not run it.

## 5. What a result would and would not mean

A (the kill) would say: on the one family where the record has an action with a finite-energy vacuum, the vacuum is
fixed by a symmetry under which the count is odd; the counts found by the seats live on configurations that are not
vacua. It would not say that no state, frame or action selects: the scope is one frame on the root. B would open the
follow-up and nothing more. Neither moves the count of derived parameters.
