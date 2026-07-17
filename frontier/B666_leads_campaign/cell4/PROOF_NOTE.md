# R21-9 — The pair-evenness lemma: abstract proof (theorem grade)

**Cell:** B666 campaign, cell 4. **Target:** the one exhaustively-verified
step of the sign-hears-the-discriminant theorem (B656/G1; dossier C2).
**Outcome: PROVEN.** The lemma is in fact *unconditional* (no hypothesis
on p at all), and the proof needs no local analysis: the feared
ramified-prime subtlety dissolves globally. As corollaries, both
directions of the C2 biconditional *and* the exactly-half law land at
theorem grade. Verification of every step: `cell4_verify.py` /
`cell4_output.txt` (this directory); all decisive arithmetic exact.

---

## 1. Setting and statements

Throughout: `w ∈ GL_n(ℤ)` of finite order ("integral, eigenvalues roots
of unity"; every Weyl-group element on a rank-n lattice qualifies),
`t ∈ ℤ`, `f(x) = x² − t x + 1`, and

    B_w = t·I − w − w⁻¹ .

For `m ≥ 1` write `Φ_m` for the m-th cyclotomic polynomial and `ψ_m ∈
ℤ[x]` for the (monic) minimal polynomial of `2cos(2π/m)`; `deg ψ_m =
φ(m)/2` for `m ≥ 3`, and `ψ_1 = x − 2`, `ψ_2 = x + 2`.

**Nondegeneracy.** Call `t` *nondegenerate for w* if `det B_w ≠ 0`.
Since the eigenvalues of `w + w⁻¹` are `2cos θ ∈ [−2, 2]`, every `t`
with `|t| ≥ 3` is nondegenerate for every finite-order `w`; the only
integer degeneracies are `t ∈ {−2,−1,0,1,2}` meeting eigenvalue orders
`m ∈ {1,2,3,4,6}` (the integral values of `2cos`). All banked batteries
have `t ≥ 3`.

**Lemma (pair-evenness, unconditional form).** Let `w ∈ GL_n(ℤ)` have
finite order and let `t` be nondegenerate for `w`. Then the contribution
of all non-real eigenvalues of `w` to `det B_w` is the square of a
rational integer. Consequently, for **every** prime `p` (ramified or
not, `p | m` or not), the total p-adic valuation of the product of
`f` over the complex-conjugate eigenvalue pairs of `w` is even.

**Theorem (sign hears the discriminant).** Let `n` be even, `w ∈
GL_n(ℤ)` of finite order, `t` nondegenerate. Let `a_2 = a_2(w)` be the
multiplicity of the eigenvalue `−1`. Then for every prime `p`:

    v_p(det B_w) ≡ a_2(w) · v_p(t² − 4)   (mod 2),        (master congruence)

and `det(w) = (−1)^{a_2(w)}`. Hence:

- **(odd case)** if `v_p(t²−4)` is odd, `det(w) = (−1)^{v_p(det B_w)}`
  for *all* such `w`;
- **(even case)** if `v_p(t²−4)` is even, `(−1)^{v_p(det B_w)} = +1`
  for all `w`, so in any group `W ⊆ GL_n(ℤ)` containing an element of
  determinant `−1` (any reflection group), the agreement set is exactly
  `ker(det)` — **exactly half** of `W`.

The biconditional of B656/G1 and the exactly-half law are the two
bullets read together.

---

## 2. Proof of the Lemma

**Step 1 (Galois orbits are forced).** `w` has finite order, so its
minimal polynomial divides some `x^N − 1`, which is squarefree over ℚ;
hence `w` is diagonalizable and its characteristic polynomial — which
lies in `ℤ[x]` because `w` is an integer matrix — factors as

    char_w(x) = ∏_m Φ_m(x)^{a_m},   ∑_m a_m φ(m) = n .

So the eigenvalue multiset of `w` is a union of *full* sets of primitive
m-th roots of unity. This is the crux: no partial conjugate-pair
bookkeeping can occur; every pair sits inside a full rational orbit.

**Step 2 (the half-trace identity).** For `m ≥ 3`,

    Φ_m(x) = x^{φ(m)/2} · ψ_m(x + 1/x).                     (†)

Standard (the real cyclotomic polynomial); verified symbolically for
`m = 3..50` in Step A of `cell4_verify.py`. Proof: the map `ζ ↦ ζ+ζ⁻¹`
is exactly 2-to-1 from the `φ(m)` primitive m-th roots onto the
`φ(m)/2` distinct numbers `2cos(2πk/m)`, `k ∈ (ℤ/m)^×/{±1}` (distinct
because `cos` is injective on `(0,π)`; 2-to-1 because `ζ ≠ ζ⁻¹` when
`ζ² ≠ 1`), and these are precisely the Galois conjugates of
`2cos(2π/m)`, i.e. the roots of `ψ_m`, each once. Both sides of (†) are
monic of degree `φ(m)` after clearing, with the same roots.

**Step 3 (the orbit product is a rational square).** Fix `m ≥ 3`. The
product of `f` over the full orbit is the resultant
`Res(Φ_m(x), x² − tx + 1) = ∏_{Φ_m(ζ)=0} f(ζ)`. Two equivalent
evaluations:

*(a) pairwise.* For a conjugate pair `ζ, ζ̄ = ζ⁻¹` with `c = ζ + ζ⁻¹`:

    f(ζ) f(ζ⁻¹) = ζ(c − t) · ζ⁻¹(c − t) = (t − c)²,

using `f(ζ) = ζ² − tζ + 1 = ζ(ζ + ζ⁻¹ − t)`. By Step 2 the multiset
`{c}` over the `φ(m)/2` pairs is the full root set of `ψ_m`, each once,
so the orbit product is `∏_c (t − c)² = ψ_m(t)²`.

*(b) via (†).* Let `α, α⁻¹` be the roots of `f` (so `α + α⁻¹ = t`; `α`
may be real, complex, or a double root — no case split needed). Then

    Res(Φ_m, f) = ∏_ζ (ζ − α)(ζ − α⁻¹) = Φ_m(α) Φ_m(α⁻¹)
                = α^{φ(m)/2} ψ_m(t) · α^{−φ(m)/2} ψ_m(t) = ψ_m(t)².

Either way:

    ∏_{ζ prim. m-th} f(ζ) = ψ_m(t)²  ∈ ℤ,  identically in t.       (‡)

Verified symbolically (polynomial identity in `t`) for `m = 3..50`,
covering every ramified shape `m = p, p², 2p, 4p, pq, …` — Step B.

**Step 4 (conclusion).** The non-real-eigenvalue contribution to
`∏_λ f(λ)` is `∏_{m≥3} ψ_m(t)^{2 a_m}`, the square of the rational
integer `∏_{m≥3} ψ_m(t)^{a_m}`, nonzero by nondegeneracy. Its p-adic
valuation is even for every prime `p`. ∎

**Why the ramification worry dissolves.** The banked heuristic said
"`v_p(f(ζ))` and `v_p(f(ζ̄))` live in `ℚ(ζ_m)`, where `p` may ramify
(`p | m`) and complex conjugation need not fix the primes above `p`" —
so pairwise *local* evenness looked delicate. The proof never enters
the local picture: (i) at the level of a single pair, `f(ζ)f(ζ̄) =
(t−c)²` is the square of an algebraic integer, so *every* valuation of
every number field takes an even value on it — conjugation-stability of
primes is irrelevant; (ii) at the level of the rational valuation
`v_p`, integrality of `w` forces full Galois orbits, and the full-orbit
product is the rational square (‡) — splitting/ramification data of `p`
in `ℚ(ζ_m)` is never consulted. Stickelberger/Swan-type discriminant
arguments (route (b) of the task) are not needed; the resultant is a
perfect square *identically*, not merely of even valuation.

---

## 3. Proof of the Theorem

By Step 1 and nondegeneracy, with `a_1, a_2` the multiplicities of
`+1, −1`:

    det B_w = ∏_λ (t − λ − λ⁻¹)
            = (t−2)^{a_1} (t+2)^{a_2} ∏_{m≥3} ψ_m(t)^{2 a_m}.       (★)

(For `λ = ±1`: `t ∓ 2`; each conjugate value `c` appears twice per
Step 2.) Verified exactly, element-by-element, against direct
`det(tI − w − w⁻¹)` computed by exact adjugate inversion — Step C
cross-checks on W(D4) and W(E6).

*Even-rank bookkeeping.* `n = a_1 + a_2 + ∑_{m≥3} a_m φ(m)` with every
`φ(m)` even for `m ≥ 3`, so `n` even forces `a_1 ≡ a_2 (mod 2)`.

*Determinant.* The primitive m-th roots (`m ≥ 3`) multiply to `1` in
conjugate pairs, so `det(w) = (−1)^{a_2}`.

*Master congruence.* Taking `v_p` of (★):

    v_p(det B_w) = a_1 v_p(t−2) + a_2 v_p(t+2) + 2(…)
                 ≡ a_2 (v_p(t−2) + v_p(t+2))            [a_1 ≡ a_2]
                 = a_2 · v_p(t²−4)   (mod 2).

*Odd case.* `v_p(t²−4)` odd gives `v_p(det B_w) ≡ a_2`, so
`(−1)^{v_p(det B_w)} = (−1)^{a_2} = det(w)`.

*Even case.* `v_p(t²−4)` even gives `v_p(det B_w)` even, so
`(−1)^{v_p(det B_w)} = +1`; agreement holds exactly on `{det w = +1} =
ker(det)`, of index 2 whenever `W` contains any determinant-`−1`
element. ∎

*Odd-rank note (as banked).* Without `a_1 ≡ a_2`, the congruence stays
`v_p(det B_w) ≡ a_1 v_p(t−2) + a_2 v_p(t+2) (mod 2)`: the law
bifurcates into separate `det(A∓I)`-parities, as recorded in B656.

---

## 4. Verification ladder (all exact; full log in `cell4_output.txt`)

| step | check | scope | result |
|---|---|---|---|
| A | (†) half-trace identity | m = 3..50, symbolic | PASS |
| B | (‡) `Res(Φ_m, f) = ψ_m(t)²` | m = 3..50, symbolic in t | PASS |
| C | `a_1 ≡ a_2`, `det w = (−1)^{a_2}` | every element, W(D4) 192 + W(E6) 51840 | PASS |
| C | (★) vs exact adjugate `det B_w` | 48 D4-elts × 7 t; 24 E6-elts × 2 t | PASS |
| D | odd case, all w | W(D4)+W(E6) × t ∈ {3,4,5,6,7,9,10}, all p \| t²−4 with odd v_p (incl. p=2 at t=6,10) | all `|W|/|W|` PASS |
| D | even case exactly-half | t=4 p=2, t=7 p=3, both groups | 96/192 and 25920/51840 PASS |
| — | banked battery reproduction | test_b656_digest G1 numbers (t=5: 192/192 at p=3,7; t=7: 96 at p=3, 192 at p=5) | reproduced |

Distinct characteristic polynomials: 9 on W(D4), 25 on W(E6) (= the
conjugacy-class count of W(E6); det B_w and det w are class functions,
so the per-type exact computation covers every element).

---

## 5. Status deltas

- **R21-9 CLOSED — PROVEN.** The last asterisk of the
  sign-hears-the-discriminant theorem falls: "pair-evenness at ramified
  primes (exhaustively verified)" upgrades to *proved, unconditionally
  in p*, with the two-line mechanism `f(ζ)f(ζ̄) = (t − c)²` +
  full-orbit integrality `⇒ Res(Φ_m, f) = ψ_m(t)²`.
- The hypothesis actually needed is weaker than banked: any
  finite-order element of `GL_n(ℤ)`, n even, t nondegenerate — the
  Weyl-group structure is irrelevant to the congruence; `W` enters only
  in the even-case half-law (need one determinant-`−1` element).
- **Free upgrade:** the exactly-half law (dossier C2's "genuinely
  unprecedented component") is now also proved, not just observed: the
  even case forces sign `+1` identically, and half-ness is exactly
  `[W : ker det] = 2`.
- Degeneracy boundary stated exactly: `det B_w = 0` only at
  `t ∈ {−2,…,2}` against eigenvalue orders `m ∈ {1,2,3,4,6}`; all
  banked stages (`t ≥ 3`) are safe.
