# Chirality from the Figure-Eight Knot: the θ-Odd Sector of the E₆ Character Variety and Its Listeners

**Author:** originaxiom

**Status:** draft v2 (PC26). Target: *Communications in Mathematical Physics*;
alternative: *Quantum Topology*. Companion: PC25 (the amphichiral fold), PC23,
PC24. v2 absorbs the hearing law, the closure theorem, the semiclassical
correspondence (outcome B) with its negatives, and the provenance statement.

**Provenance.** All verification behind this draft is internal to the
project (the author plus AI-assistant computational seats cross-checking one
another); nothing here has been externally refereed. "Verified" always means
"recomputed by a second internal pipeline". Every theorem is backed by a
repository lock (a pytest test executing the discriminating computation);
the checkable artifacts are the locks and the hashed preregistrations.

---

## Abstract

(Synchronized in ABSTRACT.md at v2-final; the v1 abstract remains accurate
for §§3–7 and is extended by §§8–9: the closure theorem — an amphichiral
object's odd hearing spectrum is conjugation-closed at every level, as an
algebraic identity of modular data — and the golden-stage semiclassical
correspondence, which exists as structure, is level-special, and localizes
every golden value in the listener's matrix elements.)

---

## 1. Introduction

The companion letter [PC25] proves that the figure-eight knot's own
hyperelliptic involution, acting on the deformation complex of the principal
E₆(ℂ)-character variety at the geometric representation, *is* the diagram
involution θ, so the E₆ → F₄ fold is forced by the knot; and that the forcing
stops there. This paper asks and answers the next questions:

> *What are the θ-odd directions — physically speaking, are they a
> chirality — who can hear them, and what exactly does a listener receive?*

The answers, in the order proved: the θ-odd sector exists as honest moduli
(§3); the θ-grading is a chirality grading, with the mirror-double dial map
computed in full (§4); no single-object probe hears it (§5); the listener is
the antiphase mirror channel, and bent listener states are null for the
intertwining form (§6); the amplitude laws are exact arithmetic, now
including the second-order hearing law with its first closed chiral
amplitude (§7); **the pairing structure of the heard spectrum is the
object's amphichirality — a theorem for arbitrary objects and stages**
(§8); and the semiclassical correspondence between the classical dial and
the golden stage exists as structure, is level-special, and fails every
naive value bridge — with the failures themselves exact and informative
(§9). What is not claimed is collected as the updated walls (§10).

### 1.1 Status conventions

- **[PROVED]** — exact/symbolic computation or complete argument (integer,
  rational, algebraic-number, or finite-group arithmetic; computer-assisted
  exact computation included).
- **[COMPUTED]** — numerical with stated precision and residuals; not a proof.
- **[CITED]** — literature, not re-derived.
- **[CONJECTURE]** — open, flagged.

---

## 2. The object, the stage, the fold

**The object.** The figure-eight knot complement M = S³ ∖ 4₁: the simplest
hyperbolic knot; amphichiral, invertible (symmetry group D₄ **[PROVED**,
`test_b279`**]**; the two orientation-reversing involutions act *freely* —
they are Gieseking deck transformations, 4₁ being the unique double cover of
the Gieseking manifold **[PROVED**, `test_b605_door2`**]**); fibered with
once-punctured-torus fiber and monodromy A₁ = [[2,1],[1,1]] ∈ SL(2,ℤ)
(trace 3, golden eigenvalues φ^{±2}); trace field ℚ(√−3). The 2-generator
presentation ⟨a, b | a W b⁻¹W⁻¹⟩, W = ba⁻¹b⁻¹a, carries the geometric
representation ρ₀; the relator forces c² − c + 1 = 0 for the parabolic
parameter, c = ζ₆ a unit, and the certified longitude is
λ = a(bABaaBAb)a⁻¹ with cusp shape −[[1, ±2√−3],[0,1]] **[PROVED**,
`test_b598_step1_exact`**]**.

**The stage(s).** (i) The *classical* deformation stage: the
E₆(ℂ)-character variety at ρ = φ_prin ∘ ρ₀, tangent = six lines indexed by
the E₆ exponents m ∈ {1,4,5,7,8,11} **[CITED** Menal-Ferrer–Porti,
Falbel–Guilloux; PC25**]**. (ii) The *quantum* stages: modular
representations of WZW theories (SU(2)_k, SU(3)_k, (E₆)_k); the mapping
torus of a word in R, L has invariant Z = tr ρ_k(word) **[CITED**
Jeffrey**]**. (iii) The finite Weil representations on ℂ[P/κQ], through
which (ii) factors (§7).

**The fold.** θ = the E₆ diagram involution: fixes f₄, exchanges 27 ↔ 27̄,
acts on the six tangent lines by exponent parity — θ-even {1,5,7,11},
θ-odd {4,8}. The identification of θ with the knot's hyperelliptic
involution is PC25's Theorem 1 **[CITED here]**.

---

## 3. The θ-odd moduli exist: unobstructedness to third order

**Theorem 3.1 (the quadratic obstruction vanishes). [PROVED]**
The cup-product quadratic form Q: H¹ × H¹ → H² vanishes identically: all 21
components exactly, over ℚ(√−3) — the complete polarized set (six pure
directions and fifteen cross-pairs). *Locks:*
`test_b575_bridge_obstruction`; two-pipeline agreement (a dps-100 numerical
pipeline and the exact minuscule-model pipeline built five months apart).

**Theorem 3.2 (Massey vanishing). [PROVED]**
The triple Massey products vanish exactly; the deformation theory is
unobstructed through third order. Beyond order 3 is **[CONJECTURE]**.
*Locks:* `test_b578_massey` (OA_SLOW).

---

## 4. The θ-grading is a chirality grading

**Theorem 4.1 (block-sum rigidity). [PROVED]**
Every sl₂-stable subalgebra of e₆ containing the principal sl₂ is a direct
sum of the six isotypic blocks; θ-even sums close inside f₄; every subset
containing a θ-odd block generates e₆. *Locks:*
`test_b576_deformed_closure` (OA_SLOW).

**Theorem 4.2 (the chiral play; the dial map). [PROVED]**
The mirror-double of the object — the complement glued to its mirror along
the cusp torus, with a twist by a peripherally-fixed dial element v_m at
finite twist parameter — has bracket-closure dimension given by the DIAL
MAP: no twist → 3 (the diagonal sl₂); the m = 1 slot → 3; the θ-even slots
{5,7,11} → 52 = f₄; the θ-odd slots {4,8} → 78 = e₆ — the subset face exact
over ℚ(√−3), the rank face by mod-p certificates at two primes; all six
dial slots verified peripherally fixed under the certified longitude.
The θ-odd-twisted double has Zariski closure E₆(ℂ) and its 27 is complex.
**Even bends stay under the fold; only the odd bends open the whole
stage.** *Locks:* `test_b582_chiral_play`, `test_b598_step7`.

---

## 5. Three unhearability theorems

(As v1: vacuum deafness; filling deafness; bare states are deaf sources at
every color of every stage. *Locks:* `test_b583_content`, `test_b580_q1`,
`test_b584`.) One addition:

**Theorem 5.4 (the unit tone is chirality-deaf). [PROVED]**
At κ = 4 the odd hearing space is one-dimensional and the amplitude is
exactly −1: real, carrying no chirality. *Lock:*
`test_b609_sealed_values`.

---

## 6. The listener

Theorems 6.1–6.3 as v1 (the antiphase channel and tr_odd ρ = ½(Z − Z_C);
the two-lifts naming theorem; quadrature via the torsion sign law
sign(τ_m) = (−1)^m). *Geometric remark updated:* the double of the
complement along the cusp is a Haken manifold whose JSJ decomposition has
two hyperbolic pieces (not a graph manifold). Two additions:

**Theorem 6.4 (the intertwiner and the forced-zero criterion). [PROVED]**
There is a Schur-unique symmetric invertible J with
ρ(X)ᵀJ + Jρ(θX) = 0; no untwisted invariant form exists (solution space
dimension 0); the move-across lemma ⟨Xu, v⟩_J = −ε_X⟨u, Xv⟩_J holds; and
the single-generator contractions ⟨v_m v0, v0⟩_J vanish — even blocks
forced by parity, all blocks forced by weight. *Locks:*
`test_b598_steps35`, `test_b598_lemma`.

**Theorem 6.5 (bent listeners are null). [PROVED]**
The distinguished stage vector v0 is weight-pure at weight 0; hence every
bent state v_m·v0 is weight-homogeneous of nonzero weight and is
J-isotropic: ⟨v_m v0, v_m v0⟩_J = 0 at all six blocks. The listener's
displacement carries no J-scale. *Lock:* `test_b603_isotropy`.

---

## 7. The amplitude laws

**Theorem 7.1 (the two-tone law; the trace form; stage-universality).
[PROVED numerically-exactly across the range; the trace form exact]**
On SU(3)_k (κ = k+3): tr_odd(4₁-bundle) = [4|κ] − [5|κ]·φ⁻¹. Equivalently:
the odd hearing form B_odd = −(the odd compression of ρ(RL)) satisfies
trace B_odd(κ) = [5|κ]·φ⁻¹ − [4|κ] on a fourteen-point grid including the
registered discriminating confirmations κ = 16 → −1 and κ = 40 → −φ⁻².
The same two-indicator law was derived independently in the finite Weil
model (Theorem 7.2's ±-symmetrized assembly): **the odd trace law is
stage-universal across the two quantum models.** *Locks:* `test_b584`,
`test_b585`, `test_b601_pairing_law`.

**Theorem 7.2 (the Weyl-twisted Weil factorization).** As v1, with the
novelty scope CORRECTED (2026-07-15 literature round): Andersen–Jørgensen
(arXiv:1206.2552, Thm 4.1.1 and Props 4.1.2–4.1.3) already compute
SU(3)/SU(N) torus-bundle invariants as Weyl-symmetrized Gauss sums for
TRACE-±2 monodromies — the framework extension to higher rank is theirs
**[CITED]**; this paper's content narrows to: general hyperbolic
monodromies, the conductor menu det(A⊗(±w) − I₄) with its closed forms
in the trace (now DERIVED: the discriminant identity det(h_w) =
sign(w)·det(A⊗w − I₄) is proved exactly, 12/12 — the campaign's cell D),
the C-coset/parity channel structure, and the tone/gating analysis
(§§7.1, 8–9). The reduction of each term to a quadratic Gauss sum on
(P/κQ)² with an explicit self-adjoint h_w is PROVED (96/96 exact); the
final Deloup–Turaev reciprocity step is verified on the even-κ sub-case
and remains **[CONJECTURE]** for odd κ.

**Theorem 7.3 (sector exchange). [PROVED]** As v1: parity of the heard
content is a property of the theater's symmetry group. *Lock:*
`test_b588_sector_exchange`.

**Theorem 7.4 (the E₆₂ amplitudes are symbolic identities). [PROVED]**
On E₆ level 2 the three per-pair amplitudes are exactly
p_j = (2/√7)·sin(2πj′/7)·ζ₁₄^{k_j}, (j′,k) = (1,+3), (3,−2), (2,−1):
proved as identities in ℚ(ζ₈₄) — the squared identity reduced to zero mod
Φ₈₄ over ℚ, the sign branch fixed at full precision (deviations ~10⁻⁴¹).
*Locks:* `test_b589`, `test_b598_step6` (OA_SLOW).

**Theorem 7.5 (the hearing law). [PROVED]**
Deform the listener along a θ-odd dial direction, ψ_ε = ψ + εu. Then
exactly, with no first-order term (parity conservation):
> A_ε(g) = A₀(g) − ε²·(u†W(g)u), and A^tw_ε − A^plain_ε = −2ε²·(u†M_odd u).
At the object's own monodromy weld the first closed chiral amplitude is
> u₃† M_odd u₃ = 1/(2φ) + i·sin(2π/5)/√5 ∈ ℚ(ζ₅), u₆† M_odd u₆ its
> conjugate,
proved symbolically over ℚ(ζ₂₀) (values in ℚ(ζ₅); minimal polynomial
5x⁴ + 5x³ + 1; field norm exactly 1/5). The mechanism is the sign-flip
theorem: P_odd·C = −P_odd, so the twist flips M_odd exactly.
*Locks:* `test_b592_mirror_listener`, `test_b593_round4_hearing` (+ the
exact V1 lock), `test_b606_norm_bridge`.

**Theorem 7.6 (state-independence; the E₆₂ ear). [PROVED]**
The hearing coefficients are independent of the listener's state (only
Cψ = ψ is used); on E₆ level 2 the three diagonal hearing coefficients
equal minus Theorem 7.4's amplitudes: the ℤ/7 sine kernel is the E₆ ear's
coefficient, and the norm-product of the three amplitudes is exactly 1/49.
*Locks:* `test_b594_e6_hearing`, `test_b606_norm_bridge`.

---

## 8. The closure theorem: the heard spectrum's pairing is the object's chirality

*(Novelty note, 2026-07-15: a direct read of Jeffrey 1992 found no
spectral-conjugation statement and no C-twist/(−A)-lift identification —
the boundary for Theorems 6.2 and 8.1 is hardened; Andersen–Jørgensen
state only a one-sentence orientation-reversal remark.)*

**Theorem 8.1 (the closure theorem). [PROVED]**
Let (S, T) be modular data with S symmetric unitary, T diagonal unitary,
S² = ζC for the charge conjugation C and a scalar phase ζ (hence
[S, C] = 0), and [C, T] = 0. Put R = T, L = S⁻¹T⁻¹S. If the weld word w is
GHH-anti-palindromic — equivalently, by the block-palindrome theorem
**[PROVED**, the companion program's B134, mechanism **[CITED**
Goodman–Heard–Hodgson**]]**, the once-punctured-torus bundle is
AMPHICHIRAL — then
> conj(W) = Q⁻¹ Wᵀ Q, Q = P·S·C,
with P the cyclic-rotation prefix; Q commutes with C, so the odd hearing
spectrum is **conjugation-closed at every level**. The three ingredients
(conj(X) = CX⁻¹C; ρ(swap x) = Sρ(x)⁻¹S⁻¹; R, L symmetric, hence
ρ(rev u) = ρ(u)ᵀ) are derived from the axioms and verified exactly at four
levels; the assembled identity holds for four amphichiral welds (16/16)
and fails for three chiral controls (12/12). *Lock:*
`test_b613_closure_theorem`.

**Empirical converse (7 objects × 14 levels). [COMPUTED]**
Every chiral weld scanned fails closure at some level (indeed at almost
all; isolated accidental closures exist — one at a degenerate
one-dimensional level, one at a single non-degenerate level). Level-uniform
closure ⟺ amphichirality on all data; the converse direction is open.
*Locks:* `test_b610_m136_weld`, `test_b611_two_laws`,
`test_b612_pairing_chirality`.

**Corollary 8.2 (the three layers).**
The heard structure separates: the SPECTRUM'S PAIRING carries the object's
chirality (Theorem 8.1); the TRACE carries its arithmetic — the fig-8's
golden two-indicator law (7.1) versus the second object's ζ₆-phased ℚ(√3)
values **[COMPUTED**, `test_b610`**]**; and the MATRIX ELEMENTS carry the
listener's coupling — the hearing spectrum itself is unitary clockwork
(B_odd is unitary by construction; its eigenvalues at the levels computed
are roots of unity: e^{±2πi/5} at κ = 5, the 8th roots minus ±1 at κ = 7,
28th-root angles at κ = 13), while every golden VALUE (Theorem 7.5's
amplitude, its 1/5-norm) lives in the matrix elements of a golden-basis
listener. *Locks:* `test_b609_sealed_values`, `test_b611_two_laws`.

---

## 9. The correspondence, and the honest negatives

**Theorem 9.1 (the spectral bridge). [PROVED]**
det(I − B_odd) = φ² = λ(A₁) at κ = 5: the golden stage's odd hearing form
knows the object's dilatation. *Lock:* `test_b595_dictionary`.

**Null 9.2 (the clock is not the naive period). [PROVED as a null]**
The registered prediction that the stage clock equals the cat-map period
FAILED; level structure does not transport through naive labels. *Lock:*
`test_b596_cat_map`.

**Theorem 9.3 (the correspondence exists as structure; outcome B).
[PROVED at the structural level, under a sealed protocol]**
Under a nine-step audited readiness protocol with a hashed
preregistration, the semiclassical map from the golden stage's θ-odd plane
to the classical dial {u₄, u₈} exists as a structural correspondence:
mirror-equivariant (the copy-exchange mirror maps every classical bending
response to the conjugate phase class with the same integers, 40/40 rows),
width-respecting, and rank-producing at E₆₂ (the odd form's spectrum is
exactly {−1, +i, −i}, giving the canonical conjugation-equivariant 2+1
splitting). It is LEVEL-SPECIAL: the hearing law survives at κ = 10 but
the golden conjugate-pairing of the naive directions does not — the
invariant pairing persists spectrally at every level while the weight-label
basis pairs only at κ = 5. Per-line magnitudes are gauge; no value claim
is made. *Locks:* the `test_b598_*` family; the classical side's exact
content is two integers on conjugate phases, N₄(1+√−3) and N₈(1−√−3),
N₄ = 2⁹·3²·5·7·13, N₈ = 2¹⁵·3⁵·5³·7²·11 (`test_b598_step4b`).

**Negatives 9.4 (no naive value bridge). [PROVED as negatives]**
Two sealed candidate tables were exhausted: (i) no structural
normalization (torsion widths, J-Grams, quantum dimensions) closes the
phase or magnitude gauge — the phase gap is exactly π/15 (the two phase
lattices meet only in ℚ(ζ₃₀)), and the J-Grams vanish identically
(Theorem 6.5); (ii) no torsion-power identity links the hearing integers
to the torsions — their prime supports are disjoint beyond small primes
(97 divides τ₄ only; 31·607·49297 divide τ₈ only). The surviving
field-compatible arithmetic: the golden hearing norm 1/5 and the E₆₂
norm-product 1/49 — each stage's hearing sector carries its defining
prime as a field norm. *Locks:* `test_b606_norm_bridge`; the B602 cell
records.

**Structure 9.5 (the mixing).** The principal blocks admit no G_SM-sector
alignment: the fold welds roots of different charge classes into single
θ-odd directions (9 of 12 pairs class-mixed); the principal strings mix
the pairs; the block lines mix the charges — the only class-pure lines are
the deepest pair (charge class (1,1,2)). Exact mixing fractions are
banked (the top line exactly uniform; the shallowest lines exactly half on
the color roots). **[PROVED**, `test_b604_rosetta`,
`test_b607_charge_table`, `test_b608_rosetta_gsm`,
`test_b609_sealed_values`**]**

---

## 10. What is not claimed: the walls, updated

1. **Values.** No SM value is derived. The exact numbers of §7 and §9 are
   stage arithmetic; the value question was pushed through two sealed
   candidate generations and closed negative both times (9.4).
2. **Selection.** No mechanism selects the SM gauge algebra; moreover the
   blocks do not align with any G_SM sector decomposition (9.5) — a
   would-be selector has nothing sectorally pure to select except the
   double-spinor tips.
3. **Index.** The chiral index of every single-object construction is 0
   (§5); the two amphichiral involutions of the object act freely
   (Gieseking), so no fixed-surface construction is available either.
4. **Compactness.** As v1 (no real form intervenes).
5. **Reachability.** As v1; the mirror-double evades the rank-1 wall's
   hypothesis, not the wall.

### 9.6 Literature context for the golden values (recorded, not claimed)

The flavor-symmetry literature contains named golden-ratio solar-mixing
ansätze: GR1 with sin²θ₁₂ = 1/(1+φ²) = (5−√5)/10 ≈ 0.276
(Kajiyama–Raidal–Strumia 2007; A₅-realized by Everett–Stuart 2009) and
GR2 with sin²θ₁₂ = (3−φ)/4 ≈ 0.345 — **our banked |h₃|² equals GR1's
value exactly**, a shared-5-fold-arithmetic fact (both constructions are
golden arithmetic), not a group identity: the golden stage's clocks have
orders 10/20 and its projective modular image exceeds |A₅| (computed).
The quantity 1/(2φ) ≈ 0.309 is unrecorded in that literature and is
numerically nearest the current fitted solar angle among such algebraic
values — recorded here as literature context under a sealed comparison
protocol whose corrected significance is p ≈ 0.08 (AMBIGUOUS) and whose
angle matches are not robust to the choice of global-fit source; no
claim is made. [CITED: the 2026-07-15 literature synthesis in the
repository.]

## 11. Firewalled motivation (one paragraph)

The program's motivating conjecture — that measured values live in the
observer–object coupling rather than in the object — is not a theorem of
this paper. What this paper contributes is now three-layered (Corollary
8.2): the stage's spectrum is universal clockwork; the spectrum's pairing
is the object's chirality, as a theorem; the trace is the object's
arithmetic; and everything golden that a listener actually receives —
the hearing amplitude, its field norm — lives in the listener's matrix
elements. The correspondence between the classical dial and the golden
stage exists as structure and is level-special (9.3); every naive value
bridge fails exactly (9.4). Any future physics claim must pass the walls
of §10, which this paper leaves standing.

## 12. Reproducibility and provenance

Every theorem's lock is a pytest test in the public repository (heavy
exact pipelines behind OA_SLOW=1); the sealed preregistrations and value
tables are SHA-256-hashed in the repository's hash ledger before their
outcome-bearing computations run. All verification is internal (author +
AI seats); see the repository's PROVENANCE.md §0 and TERMINOLOGY.md.

## References

[PC25] originaxiom, *The Amphichiral Fold* (companion draft). [MFP]
Menal-Ferrer, Porti. [FG] Falbel, Guilloux. [J] L. Jeffrey, CMP 147
(1992). [RT] Reshetikhin, Turaev. [KP] Kac, Peterson. [GHH] Goodman,
Heard, Hodgson, *Commensurators of cusped hyperbolic manifolds* /
the anti-palindromic amphichirality criterion (Exp. Math. 2008).
[G] Gieseking (via standard references on the Gieseking manifold).
(Full list at submission.)
