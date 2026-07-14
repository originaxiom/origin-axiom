# Chirality from the Figure-Eight Knot: the θ-Odd Sector of the E₆ Character Variety and Its Listeners

**Author:** originaxiom

**Status:** draft v1 (PC26). Target: *Communications in Mathematical Physics*;
alternative: *Quantum Topology*. Companion: PC25 (the amphichiral fold), PC23,
PC24.

---

## Abstract

(As in ABSTRACT.md; final text to be synchronized at v2.)

---

## 1. Introduction

The companion letter [PC25] proves that the figure-eight knot's own
hyperelliptic involution, acting on the deformation complex of the principal
E₆(ℂ)-character variety at the geometric representation, *is* the diagram
involution θ, so the E₆ → F₄ fold is forced by the knot; and that the forcing
stops there (five further-selector routes closed; the holonomy lies in no real
form). This paper asks and answers the next question:

> *What are the θ-odd directions — physically speaking, are they a chirality —
> and who can hear them?*

The answers, in the order proved:

**The θ-odd sector exists as honest moduli** (§3). The obstruction theory at
the principal representation vanishes through third order: the quadratic form
H¹ × H¹ → H² is identically zero — all 21 components, exactly, over ℚ(√−3) —
and the Massey triple products vanish exactly. Two disjoint computational
pipelines (a dps-100 numerical one and an exact minuscule-model one built five
months apart) agree on every component.

**The θ-grading is a chirality grading** (§4). Every sl₂-stable subalgebra of
e₆ is a sum of isotypic blocks; the θ-even block-sums close inside f₄; and
activating any θ-odd block forces the full e₆. The twisted mirror-double
representation built along a θ-odd direction has Zariski closure all of
E₆(ℂ), so its 27-dimensional constituent is genuinely complex: the θ-odd
motion carries chiral matter in the precise, group-theoretic sense, while the
θ-even stratum is chirality-blind.

**No single-object probe hears it** (§5). Three unhearability theorems. (i)
The vacuum is fixed by the charge conjugation C, and C is central in the
modular representation, so vacuum expectation values never see the θ-odd
sector at any level. (ii) The Dehn-filling covectors span exactly the θ-even
subspace (proved at level 1 by an overdetermined slope sweep; the level-2
extension is a structural corollary of (i)). (iii) For every color V of every
stage, a bare knot state satisfies J_V = J_{V̄} — the figure-eight is
invertible and dual color is orientation reversal — so single-object states
are θ-even identically, at every level of every theater.

**The listener is the antiphase mirror channel** (§6). The θ-odd states are
u_λ = (e_λ − e_λ̄)/√2, and the operational identity
tr_odd ρ = ½(Z − Z_C) holds: the chiral amplitude is half the difference
between the plain play of the object's mapping torus and the play with the
charge-conjugation twist inserted. The twist has a name: since S² is the
central element, the C-twisted mapping torus is the torus bundle of the
*other* SL(2,ℤ) lift −A of the object's PSL(2,ℤ) monodromy — a genuinely
different Sol manifold — so **chirality is what the two lifts agree on**.
Moreover the chiral and achiral channels never interfere linearly: the six
twisted torsions obey the sign law sign(τ_m) = (−1)^m, which makes the
one-loop factors of the θ-odd blocks real and of the θ-even blocks imaginary,
whence |total|² = |chiral|² + |achiral|² exactly.

**The amplitude laws are exact arithmetic** (§7). On the SU(3)_k tower the
figure-eight's chiral amplitude obeys the two-tone law
tr_odd = [4|κ] − [5|κ]·φ⁻¹ (κ = k+3), verified blind on twelve levels and on
five held-out levels including the additive collision at κ = 20 (value φ⁻²).
The mechanism is a Weyl-twisted finite Weil factorization — the stage trace
splits into twelve Gauss sums indexed by ±W(A₂), with conductors
det(A ⊗ (±w) − I₄) — from which the law, the golden closed form
−φ⁻¹ = (1/12)[(1+5) − 6√5], the heavier words' interference (silver's tones
{4,5,7}; bronze's exact cancellation at κ = 10), and the *absence* of any
divisibility law for the achiral channel are all derived. On the golden stage
(κ = 5) and on E₆ level 2 the even channel vanishes identically — the entire
invariant is the chiral amplitude — and the three E₆₂ per-pair amplitudes are
exactly (2/√7)·sin(2πj/7)·ζ₁₄^k, the ℤ/7 sine kernel times 14th roots.
Finally, the sector-exchange theorem: the same √5 Gauss data is θ-even on
SU(2)₃ and θ-odd on SU(3)₂ because −1 belongs to W(A₁) and not to W(A₂) —
parity of content is a property of the theater's symmetry group.

**What is not claimed** (§8). The five walls — values, selection-
disjointness, chiral index, compactness, reachability — are restated as
theorems of absence, updated where this paper's results sharpen them.

### 1.1 Status conventions

- **[PROVED]** — exact/symbolic computation or complete argument (integer,
  rational, algebraic-number, or finite-group arithmetic; computer-assisted
  exact computation included).
- **[COMPUTED]** — numerical with stated precision and residuals; not a proof.
- **[CITED]** — literature, not re-derived.
- **[CONJECTURE]** — open, flagged.

Every theorem below is backed by a repository lock (a pytest test executing
the discriminating computation); the lock names appear with each statement.

---

## 2. The object, the stage, the fold

**The object.** The figure-eight knot complement M = S³ ∖ 4₁: the simplest
hyperbolic knot; amphichiral, invertible (symmetry group D₄ **[PROVED**,
`test_b279`**]**); fibered with once-punctured-torus fiber and monodromy
A₁ = [[2,1],[1,1]] ∈ SL(2,ℤ) (trace 3, golden eigenvalues φ^{±2}); trace
field ℚ(√−3). The 2-generator presentation ⟨a, b | a W b⁻¹W⁻¹⟩,
W = ba⁻¹b⁻¹a, carries the geometric representation ρ₀ with
tr ρ₀(ab) = (5 ± √−3)/2.

**The stage(s).** Three families of theaters appear. (i) The *classical*
deformation stage: the E₆(ℂ)-character variety at ρ = φ_prin ∘ ρ₀, whose
tangent decomposes into six lines indexed by the E₆ exponents
m ∈ {1,4,5,7,8,11} **[CITED** Menal-Ferrer–Porti, Falbel–Guilloux; PC25**]**.
(ii) The *quantum* stages: the modular representations H_k(T²) of the WZW
theories (SU(2)_k, SU(3)_k, (E₆)_k), where the closed mapping torus of a word
in R, L has invariant Z = tr ρ_k(word) **[CITED** standard; Jeffrey**]**.
(iii) The finite Weil representations on ℂ[P/κQ], through which (ii) factors
(§7).

**The fold.** θ = the E₆ diagram involution = Out(E₆): fixes f₄, exchanges
27 ↔ 27̄, acts on the six tangent lines by exponent parity — the θ-even
(F₄) exponents are {1,5,7,11}, the θ-odd pair is {4,8}. The identification of
θ with the knot's hyperelliptic involution on the deformation complex is
PC25's Theorem 1 **[CITED here]**. The amphichiral involution is the
*antilinear* conj∘θ; the ℂ-linear involution on the complex is θ itself
**[PROVED**, `test_b570_c1`, `test_b353`**]**.

---

## 3. The θ-odd moduli exist: unobstructedness to third order

**Theorem 3.1 (the quadratic obstruction vanishes). [PROVED]**
Let (H¹, H²) be the twisted cohomology of the deformation complex at ρ, with
dim H¹ = dim H² = 6 (one line per exponent). The cup-product quadratic form
Q: H¹ × H¹ → H² vanishes identically: all 21 components Q(u_i, u_j) = 0,
i ≤ j ∈ {1,4,5,7,8,11}, exactly, over ℚ(√−3).
*Locks:* `test_b575_bridge_obstruction` (the exact minuscule-model pipeline:
e₆ realized in gl(27) with GF(2)-solved structure signs, Fox calculus on the
relator, per-block cup products); agreement with the independent dps-100
pipeline of the {4,8}-integrability program **[PROVED**, reconciliation
banked**]**.

**Theorem 3.2 (Massey vanishing). [PROVED]**
The triple Massey products on H¹ vanish exactly; with 3.1, the deformation
theory is unobstructed through third order, and each θ-odd line integrates to
a formal arc that is honestly chiral at second order.
*Locks:* `test_b578_massey` (OA_SLOW-gated).

*Remarks.* (a) The two-pipeline agreement (numerical 2026-02; exact 2026-07)
is the paper's reproducibility anchor. (b) We do not claim analytic
integrability beyond third order; the statement proved is exactly the order
computed. **[CONJECTURE**: full formal integrability.**]**

---

## 4. The θ-grading is a chirality grading

**Theorem 4.1 (block-sum rigidity). [PROVED]**
Every sl₂-stable subalgebra of e₆ containing the principal sl₂ is a direct
sum of the six isotypic blocks. The θ-even sums close inside f₄. Every subset
containing a θ-odd block generates the full e₆: all six forcing channels are
nonzero. *Locks:* `test_b576_deformed_closure` (OA_SLOW-gated).

**Theorem 4.2 (the chiral play). [PROVED]**
The θ-odd-twisted mirror-double representation — the object coupled to its
mirror along a θ-odd dial direction — has Lie closure e₆ and Zariski closure
E₆(ℂ); its 27 is a complex (chiral) representation, and no real form
intervenes: the coupled character is non-real (witness the exact value
tr₂₇ = (1295415 + 1011915√−3)/2). Consequently there is no forced branching
to any real form's subalgebra chain. *Locks:* `test_b582_chiral_play`,
`test_b583_content`.

Together: *the chirality of the object is exactly the θ-odd motion* — the
θ-even stratum cannot tell left from right (it closes in the fold), and every
θ-odd deformation can.

---

## 5. Three unhearability theorems

**Theorem 5.1 (vacuum deafness). [PROVED]**
On every stage, C is central in the modular representation ([C,S] = [C,T] = 0)
and the vacuum is C-fixed; hence every vacuum amplitude is θ-even at every
level. *Locks:* `test_b583_content` (X3), re-verified per-stage in
`test_b584`/`test_b586`.

**Theorem 5.2 (filling deafness). [PROVED at level 1; structural at all levels]**
The Dehn-filling covectors span exactly the θ-even subspace: at level 1, an
overdetermined coprime-slope sweep gives span rank exactly 2 with θ-odd
projection < 10⁻¹⁰, with the lens-space control gate passed.
*Locks:* `test_b580_q1`.

**Theorem 5.3 (bare states are deaf sources — every color, every stage). [PROVED]**
For any stage and any color V: J_V(4₁) = J_{V̄}(4₁). (4₁ is invertible
**[PROVED**, D₄ symmetry group, `test_b279`**]**, and coloring by the dual is
orientation reversal **[CITED** Reshetikhin–Turaev functoriality**]**;
verified computationally for su(3) fundamental vs anti-fundamental at eight
generic points, `test_b584`.) Hence every bare knot state has zero θ-odd
component: the object alone — and its mirror alone — is mute in the chiral
channel.

---

## 6. The listener

**Theorem 6.1 (the antiphase channel and the operational identity). [PROVED]**
The θ-odd states are u_λ = (e_λ − e_λ̄)/√2, and
> tr_odd ρ = ½ ( Z − Z_C ),
where Z_C is the amplitude with the C-twist inserted. Chirality is heard only
by an observer holding the object and its mirror in coherent antiphase.
*Locks:* `test_b584_theta_listener`.

**Theorem 6.2 (the naming theorem: the two lifts). [PROVED]**
On the stage S² is the central element; in SL(2,ℤ), S² = −I. Hence
tr(Cρ(W)) = ±tr ρ(S²W) (sign = the stage's S²-vs-C convention), and the
C-twisted mapping torus is the torus bundle of the other SL(2,ℤ) lift −A of
the object's PSL(2,ℤ) monodromy — trace −3, a distinct Sol manifold. The
channel identities give: **the θ-odd amplitude is the lift-symmetrization,
the θ-even amplitude the lift-difference — chirality is what the two lifts
agree on.** *Locks:* `test_b585_listener_law` (N1).

**Theorem 6.3 (quadrature; no linear interference). [PROVED]**
The six Sym^{2m}-twisted torsions of 4₁ obey the sign law
sign(τ_m) = (−1)^m, positive exactly at the θ-odd exponents {4,8}
(*locks:* `test_b581_six_torsions`). Since CS(4₁) = 0, the semiclassical
one-loop factors 1/√τ_m are real for the chiral blocks and imaginary for the
achiral ones; hence for any real weights, |total|² = |chiral|² + |achiral|²
exactly. *Locks:* `test_b583_x2r`.

*Geometric non-realization remark.* The C-twisted torus is Sol, not
hyperbolic; the double of the complement along the cusp is a graph manifold.
No hyperbolic "chord manifold" with new volume/CS/trace-field invariants
exists in this construction **[PROVED/CITED**, B586**]**.

---

## 7. The amplitude laws

**Theorem 7.1 (the two-tone law). [PROVED numerically-exactly across the range; law verified on held-out levels]**
On SU(3)_k (κ = k+3, κ = 4..26):
> tr_odd(4₁-bundle) = [4|κ]·1 − [5|κ]·φ⁻¹, additively
(the κ = 20 collision gives 1 − φ⁻¹ = φ⁻²). At κ = 5 the even channel
vanishes identically and the entire banked invariant −φ⁻¹ is the chiral
amplitude; the θ-odd block is the order-10 golden rotation e^{±3πi/5}, the
θ-even block a silent order-20 clock. *Locks:* `test_b584`, `test_b585`.

**Theorem 7.2 (the Weyl-twisted Weil factorization). [PROVED numerically-exactly; framework CITED]**
For balanced words W,
> Z(W; SU(3)_k) = (1/6) Σ_{w∈W(A₂)} sign(w) · tr(ρ_Weil(W) ∘ P_w)
on ℂ[P/κQ], with the C-twist moving the sum to the −W coset; each of the
twelve terms is a Gauss sum gated by the conductor det(A ⊗ (±w) − I₄) — the
object's eigenvalues twisted by the stage's point group. The identity is
exact at every κ = 4..20 for the golden, silver, and bronze words. From it:
the golden closed form −φ⁻¹ = (1/12)[(1+5) − 6√5]; silver's tone menu
{4,5,7} with 7 = N(α·ω − 1) = 49 (a *registered prediction*, confirmed);
bronze's exact cancellation (4 − 12 + 8)/12 = 0 at κ = 10; and the
*derived absence* of any divisibility law for the achiral channel (its
unit-conductor terms oscillate as quadratic characters). The framework — WRT
invariants of torus bundles as Gauss sums — is Jeffrey's **[CITED**, and the
SU(2) case is the companion program's banked proof**]**; the SU(3)/Weyl-
twisted tone menu is the new content. The per-term reciprocity proof at
SU(3) is **[CONJECTURE**/in progress**]**. *Locks:*
`test_b587_weil_mechanism`.

**Theorem 7.3 (sector exchange). [PROVED]**
The same √5 Gauss data is θ-even on SU(2)₃ and θ-odd on SU(3)₂: on the
rank-1 stage −1 = w₀ ∈ W(A₁) (the parity term sits inside the Weyl sum;
C = 1), on the rank-2 stage −1 ∉ W(A₂) (the parity terms constitute the
C-coset). The ingredient identity ½(1 − √5) = (1/12)[(1+5) − 6√5] = −φ⁻¹
holds exactly. **Whether the object's voice is symmetric or chiral is a
property of the theater's symmetry group.** *Locks:*
`test_b588_sector_exchange`.

**Theorem 7.4 (the E₆₂ amplitudes; the sine kernel). [PROVED numerically-exactly, 40+ digits from exact-basis sums]**
On E₆ level 2 the even channel vanishes identically (Z = +1 all-chiral) and
the three per-pair amplitudes are exactly
> p_j = (2/√7)·sin(2πj′/7) · ζ₁₄^{k_j}, (j′, k) = (1,+3), (3,−2), (2,−1):
the moduli are the ℤ/7 sine kernel — the θ-odd S-block's own row — and the
monodromy adds three 14th-root phases. *Locks:* `test_b586`, `test_b589`.

---

## 8. What is not claimed: the five walls, updated

1. **Values.** No dimensionful or dimensionless SM value is derived. The
   numbers in §7 are stage arithmetic (conductors, Gauss sums, sine kernels).
2. **Selection.** No mechanism selects the SM gauge algebra among the stage's
   options; the one live channel is the θ-odd dynamics itself.
3. **Index.** The chiral index of every single-object construction is 0
   (Theorems 5.1–5.3 are the operational restatement).
4. **Compactness.** The holonomy lies in no real form (PC25 Theorem 3); the
   chiral 27 of Theorem 4.2 is complex over ℂ with no compact-form transfer.
5. **Reachability.** The rank-1 wall (no chiral selector is reachable through
   the θ-stable principal SL(2,ℂ)) stands; the mirror-double of Theorem 4.2
   evades its *hypothesis* (it is not a rank-1 embedding), not the wall.

## 9. Firewalled motivation (one paragraph)

The program's motivating conjecture — that measured values live in the
observer–object coupling rather than in the object — is not a theorem of
this paper. What this paper contributes to it is structural: chirality is
real (§3–4), invisible to every single-object probe (§5), audible precisely
to a mirror-bearing listener (§6), with amplitude laws that are exact
arithmetic of the listening stage (§7), and with the parity of the heard
content decided by the stage's symmetry group (Theorem 7.3). Any future
physics claim would have to pass the five walls of §8, which this paper
leaves standing.

## 10. Reproducibility

Every theorem's lock is a pytest test in the public repository; the heavy
exact pipelines are gated behind OA_SLOW=1. The locks named in this draft
run green as of the draft commit; the full suite (2187 tests) runs green
except one known SnapPy-flaky test unrelated to this material.

## References

[PC25] originaxiom, *The Amphichiral Fold: E₆ → F₄ on the Figure-Eight
Character Variety, and Why It Stops There* (companion draft).
[MFP] Menal-Ferrer, Porti — twisted cohomology of cusped hyperbolic
3-manifolds. [FG] Falbel, Guilloux. [J] L. Jeffrey, *Chern–Simons–Witten
invariants of lens spaces and torus bundles* (CMP 147, 1992). [RT]
Reshetikhin, Turaev. [KP] Kac, Peterson. [TDV] Todorov, Dubois-Violette.
[K] Krasnov. (Full list at v2.)
