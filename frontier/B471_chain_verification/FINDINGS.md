# B471 — the Chain Scout verified: the uniqueness is a THEOREM, the pair is Cohn's stage, the chain walks the Markov spine

**Status: banked (frontier). Firewalled. Incoming: Chat-2's CHAIN_SCOUT_FINDINGS
(2026-07-08, properly labeled exploratory; their 7 confirmatory preregs run here). Every
scout claim verified exactly; one upgraded to a closed-form theorem; one downgraded
honestly. Lit-gates recorded — this is the most classical territory in the subject
(Cohn 1955, Markov, Fricke): the novelty is the METALLIC-BODY reading, never the Markov
theory itself. No H1.**

## The theorem (their prereg-1 "attempt proof" — done, closed form)

With x = tr A_m = m²+2, y = tr A_n = n²+2, z = tr(A_mA_n) = (mn+1)²+m²+n²+1 (B467):

**tr[A_m, A_n] = x² + y² + z² − xyz − 2 = 2 − (mn(n−m))²** (symbolic identity).

So the commutator is parabolic (tr = −2, the pair generates a cusped once-punctured-torus
group) ⟺ mn(n−m) = 2 ⟺ **(m,n) = (1,2), for ALL m < n** — not a scan, a theorem. Their
controls reproduce exactly ((1,3) → −34, (1,4) → −142, (2,4) → −254). **The (golden,
silver) pair is the unique metallic pair that closes the cusp — the seam's year-long
address (1,2) now has a one-line mechanism.** Every other pair's commutator is hyperbolic:
the stage tears.

## The Cohn identification (their prereg-2) — certified up to the lit-gate

A₁ = g₁ exactly; A₁A₂⁻¹A₁ = g₂; A₂ = g₁g₂⁻¹g₁ (Nielsen: ⟨A₁,A₂⟩ = ⟨g₁,g₂⟩). And the
membership certification: L = S·T⁻¹·S⁻¹ in PSL(2,ℤ), so every BALANCED R/L word (equal
R- and L-counts — all metallic bodies, all chain words) lies in the kernel of the
abelianization = the commutator subgroup. ⟨g₁,g₂⟩ = [PSL(2,ℤ), PSL(2,ℤ)] = Cohn's modular
once-punctured torus: **lit-gate (Cohn 1955), cited not claimed.** The half-pair [X₁,X₂]
has trace 1 — elliptic of order 6 (the orbifold stage; the Eisenstein 6, plainly noted).

## The chain laws — all verified exact (n ≤ 14)

- **CORRECTION (2026-07-08, from B470-RF2)**: the scout's "trace field ℚ(√(9mₙ²−4))" is
  the monodromy's EIGENVALUE (scale) field — real, hence NOT the 3-manifold trace field
  (which is complex; RF2 finds the actual trace fields exceed degree 12 by body n=3).
  The Markov-form-field statement stands for the SCALE fields; the trace-field tower is
  B470-RF2's open cell.
- Fricke recursion u_{n+1} = u_n u_{n−1} − u_{n−2} on traces 6, 3, 15, 39, 582, …
- The Markov cubic x²+y²+z² = xyz conserved on every consecutive triple; /3 = the spine
  walk 1, 2, 5, 13, 194, 7561, … (the drop-oldest branch).
- **Every renormalized pair (s_n, s_{n+1}) has tr[·,·] = −2**: the chain is an infinite
  tower of punctured-torus stages — "a → ab at every level," cusp conserved, now exact.
- 3 | u_n frozen (as the norm was frozen in BR-N); **mod-60 state period 20 = ord(W₁)**
  — the seam clock reappearing at word level.
- The half-chain: the twisted Fricke law v_{n+1} = v_n v_{n−1} − det(s_{n−1})·v_{n−2}
  (**the breath is the sign in the composition law**) and the field-form selection:
  breathing words (det −1) carry the metallic form v²+4; silent words (det +1) the cover
  form v²−4 — BR-N riding the word tower. Half-chain discs confirm their small-number
  notes (5, 8, 40 → √10, 20160 → √35) — noted, not built upon.

## The constants — confirmed, and the two seats' normalizations reconciled

Torsion temperature: log(torsion)/syllable → **0.6295699…** (their 0.6295727 ✓; my
per-full-letter 1.2591398 = exactly 2× — one full letter = two syllables). λ_chain:
their 2.1775291… and my per-full-letter 3.5223904… satisfy **λ_mine = λ_theirs^φ** —
same constant, two clocks, related by the golden exponent. Non-quadratic-unit flag
stands on both. Lit-gates: Zagier (Markov growth), Guéritaud–Futer (volumes).

## The aba body (their prereg-4) — entered, with a SURPRISE

M(s₃) = b++RLRRLLRL: **vol = 7.6417106, H₁ = ℤ/37 + ℤ (torsion 37 ✓ = u₃ − 2), and
CS = 0 — the aba body is AMPHICHIRAL** (the reverse+swap criterion fixes RLRRLLRL
exactly). This is the decisive contrast with B470's LETTER-tower (chiral from n = 3):
**the body-chain and the letter-tower have different breath behavior** — the chain's
words satisfy the reversal+swap symmetry where the letter words do not. The two towers
are now each other's control; B470's RF1 gains this as a fixed comparison cell.
Temperature data point: log(37)/6 = 0.6018 (early-rung, below the 0.6296 asymptote);
vol/syllable = 1.2736.

## The heredity conjecture (their prereg-6) — honest downgrade

Their specific instances CONFIRM (13 = u₂−2 and 37 = u₃−2 both divide u₅²−4; 17 | disc
n=6), but the general lattice is IRREGULAR (k=2: n ∈ {5,11} on the −2 side, {6,10} on
+2; k ≥ 4 mostly +2-side only). Recorded as the observed table; a clean law needs
rank-of-apparition machinery (Lucas-style) — named follow-up, not a conjecture bank.

## Reproduce
```
python3 chain_verify.py     # ALL CHECKS PASS — theorem, Cohn, chain laws, constants
# aba body: snappy b++RLRRLLRL (session log; vol/CS/H1 as above)
pytest ../../tests/test_b471.py
```
