# CELL S′ — THE SCALE-TORSOR NO-GO THEOREM (wall 10 → standalone theorem)

**B666 leads campaign, Addendum 2, cell S′.** Outcome per sealed
addendum (82d5cd62): **PROVEN** — wall 10 (the dimensionful no-go,
B660/S3, LAW_MAP row 10) upgrades from theorem-by-assembly to a
standalone one-page theorem with a group-cohomological mechanism, its
rigidity step verified EXACTLY on every banked symmetry structure.
Decisive script `verify_rigidity.py`; full transcript
`cellS_output.txt` (25 s; int/Fraction/sympy only, no floats in any
decisive step).

---

## 1. The two formalizations

**Definition 1 (framework output).** A *framework output* is an
element of a fixed number field F, carried by a representation of (or
fixed by / equivariant under) one of the banked finite or profinite
symmetry structures. The banked instances, each with its provenance:

| structure | G | where banked |
|---|---|---|
| the silver chord-data Galois frame | Gal(L/ℚ(i)) = Klein four (σ, τ, στ) | B662 cellD (exact 8×8 rational maps; Fix(σ,τ) = ℚ(i) = k(Γ)) |
| the hearing image, ker(det) | 2I = SL(2,5), class equation [1,1,12,12,12,12,20,20,30] | B640 (hearing group), B644 (congruence-shadow theorem, elementwise) |
| the full level-15 hearing image | im ρ ≅ 2I × ℤ/3 | B640 |
| the mod-conductor shadow group | SL(2,ℤ/15) ≅ SL(2,3) × SL(2,5) (CRT) | B640; the shadow-functor mechanism B644/B650-W2 |
| the κ=14 stage shadow core | PSL(2,7) = GL(3,2), order 168 | B646 (A₁ mod 7: order 8 in SL(2,7), order 4 in PSL), B666 cell3 |
| the stage Weyl group | W(E6), order 51840 | B570/B578 (BFS-enumerated; the level-2 stage machinery) |
| the shadow tower (profinite limit) | lim← SL(2,ℤ/m) along conductors | the "measurement is passage through the finite" principle (LAW_MAP; B640/B644) |

Every banked output — tones, cubic components, portal entries, ladder
integers, Y-tensors, σ*-matrices — is an exact algebraic number in
such an F, stabilized by such a G (B660/S3 row 2).

**Definition 2 (dimensionful quantity).** Fix the multiplicative group
ℝ₊ of unit rescalings. A *dimensionful quantity of weight w ≠ 0* is a
coordinate on the ℝ₊-torsor of unit choices: an element of a
1-dimensional real representation ℝ_w of ℝ₊ on which λ ∈ ℝ₊ acts as
multiplication by λ^w. Equivalently: a quantity with no canonical
value, only a value-per-unit-section, transforming by λ^w under unit
change. (Allowing an auxiliary finite factor, the scaling group is
ℝ₊ × Φ with Φ finite; nothing below changes.) "Nontrivial scale
representation" means w ≠ 0.

The point of the definitions: a *prediction* of a dimensionful
quantity by the framework would be a map from the framework's output
algebra to ℝ_w that respects the symmetry structure the outputs carry
— a G-equivariant map, where G acts on ℝ_w through some homomorphism
G → ℝ₊ (the only way a group can act on a 1-dimensional real
representation of the scaling type while commuting with the ℝ₊-action;
an action through negative scalars factors as {±1} × ℝ₊, and the {±1}
part is torsion, handled identically).

---

## 2. The lemma (the rigidity step)

**Lemma.** Hom(G, ℝ₊) = 0 for every finite group G, and
Hom_cont(G, ℝ₊) = 0 for every profinite group G.

*Proof.* (i) *Finite case: ℝ₊ is torsion-free.* Let φ: G → ℝ₊ and
g ∈ G with gⁿ = 1, n = ord(g). Then φ(g)ⁿ = φ(gⁿ) = 1 in ℝ₊. The map
x ↦ xⁿ is strictly increasing on ℝ₊ (n ≥ 1), so x = 1 is its only
fixed preimage of 1: φ(g) = 1. Every element of a finite G is torsion,
so φ ≡ 1. Equivalently: φ factors through the abelianization G^ab
(ℝ₊ abelian); G^ab is a finite abelian group, hence pure torsion,
hence has no nontrivial torsion-free quotient; every subgroup of ℝ₊
other than {1} is torsion-free of infinite order; so the image is {1}.

(ii) *Profinite case: ℝ₊ is connected with no small subgroups.* Let G
be profinite (compact, totally disconnected, G = lim← G/N over open
normal N of finite index) and φ: G → ℝ₊ continuous. Two independent
kills:

- *Compactness.* φ(G) is a compact subgroup of ℝ₊. Under the
  topological isomorphism log: (ℝ₊, ×) → (ℝ, +), a compact — hence
  bounded — subgroup B of (ℝ, +) containing some t ≠ 0 contains all
  nt, n ∈ ℤ, which is unbounded (the archimedean property). So
  B = {0} and φ ≡ 1.
- *No small subgroups / total disconnectedness.* ℝ₊ has an
  identity neighborhood (e.g. (1/2, 2)) containing no nontrivial
  subgroup; a profinite G has a neighborhood basis of the identity by
  open subgroups; the image of each lands in every identity
  neighborhood of ℝ₊ eventually, hence is a subgroup inside
  (1/2, 2), hence trivial — φ is trivial on an open subgroup U, so φ
  factors through the finite group G/∩ₓ xUx⁻¹, and case (i) finishes.
  (Equivalently: φ(G) is totally disconnected in the connected group
  ℝ₊... — the compactness kill above is already complete; this
  second route shows the result does not even need compactness of the
  image, only the profinite topology.) ∎

**Computational verification (exact, per banked group)** — the brief's
required instantiation, all in `verify_rigidity.py`, transcript
`cellS_output.txt`:

| G | built from scratch | fingerprint verified | [G,G] | G^ab | exp(G^ab) | Hom(G,ℝ₊) |
|---|---|---|---|---|---|---|
| Gal(L/ℚ(i)) | (ℤ/2)² realization of the banked {1,σ,τ,στ} | order 4, element orders [1,2,2,2] (noncyclic ⇒ Klein four) | 1 | (ℤ/2)², order 4 | 2 | 0 |
| 2I = SL(2,5) | BFS over T, L mod 5 | order 120; class equation [1,1,12,12,12,12,20,20,30] = the banked B640 profile | whole group (PERFECT) | trivial | 1 | 0 |
| PSL(2,7) | BFS over T, L mod 7, ±I identified | order 168; class equation [1,21,24,24,42,56] | whole group (PERFECT) | trivial | 1 | 0 |
| 2I × ℤ/3 | direct product | order 360 = 120·3 | 2I × 1, order 120 | ℤ/3 | 3 | 0 |
| SL(2,ℤ/15) | BFS over T, L mod 15 | order 2880 = 24·120 (CRT) | order 960 | ℤ/3 (the SL(2,3)^ab factor; SL(2,5) perfect) | 3 | 0 |
| W(E6) | BFS over the 6 simple reflections (integer 6×6, root basis, the B570/B578 pattern) | order 51840; det character surjective onto {±1} (25920/25920) | order 25920 (normal-closure BFS; index 2) | ℤ/2 | 2 | 0 |

The W(E6) case was closed two independent ways: (a) *structurally* —
det: W ↠ {±1} gives |W^ab| ≥ 2, and the exact matrix identity
(sᵢsⱼ)sᵢ(sᵢsⱼ)⁻¹ = sⱼ, verified on all 5 Cartan edges (all bonds
m = 3, odd; diagram connected), makes all six generators conjugate, so
W^ab is cyclic generated by one involution image, |W^ab| ≤ 2; (b) *by
brute enumeration* — the subgroup generated by the commutators
(sᵢsⱼ)² has order exactly 25920, index 2 (hence normal, hence = [W,W]
since the quotient is abelian). Both give W^ab = ℤ/2.

For each group the final step is the sympy-exact statement that the
only positive real solving x^e = 1 (e = exp(G^ab)) is x = 1. The
profinite tower's archimedean step is also witnessed exactly
(Fraction arithmetic).

---

## 3. The theorem

**Theorem (scale-torsor no-go).** Let A be the framework's output
algebra — any F-vector space of outputs carrying an action of a banked
symmetry structure G (finite or profinite as in Definition 1) — and
let ℝ_w be a nontrivial scale representation (Definition 2, w ≠ 0), on
which G acts through some continuous ρ: G → ℝ₊ (or G → {±1} × ℝ₊).
Then:

**(a)** ρ is trivial on the ℝ₊-factor (the Lemma; the {±1}-factor is
torsion, killed the same way inside any torsion-free target — and if
retained, it acts by signs, carrying no scale).

**(b)** Consequently a G-equivariant map T: A → ℝ_w intertwines the
G-action on A with the TRIVIAL scale action on ℝ_w; but ℝ_w is, as a
scale representation, characterized by its nontrivial ℝ₊-weight w,
which no element of the image can carry canonically: the value T(a)
would have to be simultaneously unit-independent (it is constructed
from G-structured algebraic data alone, with no unit section in
sight — A contains no ℝ₊-torsor coordinate, B660/S3 rows 2–3: no
continuous parameter anywhere post-GATE B, no dial in the sealed
grammar) and of weight w ≠ 0 under unit change. The only element of
ℝ_w fixed under the weight-w rescaling action is 0. Hence **T = 0**.

**(c)** Sharper form of (b), Sylvester-style (the exact analogue of
the banked equivariance wall's T = 0, B650 W2-G1): consider the full
scaling-equivariance demand — T(λ·a) = λ^w T(a) for the unit-rescaling
action λ ∈ ℝ₊. The framework's outputs are exact algebraic numbers:
the ℝ₊-action on A is TRIVIAL (rescaling units does not move an
algebraic integer, a trace, a ladder integer — B660/S3 row 2). So
T(a) = T(λ·a) = λ^w T(a) for all λ ∈ ℝ₊, and (λ^w − 1) T(a) = 0 with
λ^w ≠ 1 for any λ ≠ 1 (w ≠ 0): **T(a) = 0 for every a**. The
disjointness that kills the intertwiner is exactly the one the banked
wall saw between infinite-order hyperbolic spectrum and the finite
congruence shadow — here between the trivial and the weight-w
ℝ₊-spectrum. ∎

**Corollary (no dimensionful prediction).** No nonzero assignment from
the framework's output algebra into any nontrivial scale
representation exists; every dimensionful quantity (mass, VEV, Λ,
cross-section, any running coupling) is permanently outside the
framework's reach AS A VALUE — now not as a typing rule (B650 R5) or
an assembled wall (B660/S3) but as a two-line rigidity theorem:
*finite/profinite symmetry cannot act nontrivially on a scale, and
scale-free data cannot map equivariantly onto a scale except by zero.*
The B615-era nulls on dimensionful comparisons remain retro-explained
(a typing violation is now a vanishing theorem).

---

## 4. Scope and honesty

- This is a theorem about THIS framework's output type — outputs =
  algebraic numbers structured by the banked finite/profinite groups —
  **not a statement about nature**. It does not say dimensionful
  quantities are unpredictable in general; it says *this kind of
  structure* cannot emit one. A framework with a genuine ℝ₊-torsor
  coordinate among its outputs (a modulus, a running scale, a
  continuous dial) escapes the theorem at Definition 1; this
  framework provably has none (B660/S3 rows 2–3, the B652 no-scale
  grammar wall — those remain inputs for the "no dial" premise, the
  one assembly ingredient this note consumes rather than reproves).
- What upgraded: the MECHANISM. Wall 10's row 4 ("finite shadows
  cannot carry a noncompact direction") is now the Lemma with a proof
  and six exact per-group instantiations, and the wall's conclusion is
  the Sylvester-style T = 0 of §3(c) rather than an assembly of typing
  rows.
- Falsifier (inherited and sharpened): exhibit a banked output NOT
  stabilized by a finite/profinite structure — i.e. a genuinely
  continuous ℝ₊-parameter in the output algebra — and the theorem's
  hypothesis fails; one example suffices.
- Dimensionless ratios, phases, mixing parameters, counting: untouched
  by this theorem (weight w = 0 is outside its hypothesis). That is
  the licensed observable class of B660/S3, unchanged.
- Gate 5: nothing here is SM-facing; no value, no comparison. The
  companion note (cell S″, `SILENCE_NOTE.md`) carries the one labeled
  physical hypothesis; this note carries none.

## 5. Files

- `verify_rigidity.py` — the decisive script (all six groups built
  from scratch; exact arithmetic throughout)
- `cellS_output.txt` — full verbatim transcript, all gates
- companion: `SILENCE_NOTE.md` (cell S″, the gluing statement)

Banked inputs cited (read-only): B662 cellD `PROOF_NOTE.md` (the
Galois frame), B640/B644 FINDINGS (2I, the class equation, the shadow
functor), B646 FINDINGS (PSL(2,7)), B650 FINDINGS W2-G1 (the
equivariance wall T = 0), B660 `packet/s3_nogo/NOGO_NOTE.md` (wall
10), B570 `c3_e6_level2_monodromy.py` (the W(E6) builder pattern —
re-implemented here in pure integer arithmetic, not imported).
