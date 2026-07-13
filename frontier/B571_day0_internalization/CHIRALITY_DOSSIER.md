---

# CHIRALITY DOSSIER — "Are you sure the object has no chirality?"

**Scope:** the complete, precise inventory of every sense in which chirality/orientation appears in the origin-axiom program, with proof-tier labels, and the adjudication of whether the object's own chirality can feed the SM's complex-fermion slot. All source files are absolute-pathed at the end.

---

## Executive answer (the one-sentence verdict)

**The object is richly chiral in one Z/2 and provably symmetric in a *different* Z/2 — and the SM needs the one where it is symmetric.** There are **two distinct orientation involutions** on the geometric data, and the whole confusion in the question dissolves once they are separated:

- **c = complex conjugation** (τ ↔ τ̄, √−3 ↔ −√−3, orientation reversal, σ ↔ σ̄, the arrow of time). **The object BREAKS this** — items 2–5 are all instances. This is a genuine, computed chirality.
- **θ = Out(E₆) = the E₆→F₄ fold = the 27 ↔ 27̄ swap** (the representation-theoretic duality the SM's complex fermions require). **The object is SYMMETRIC under this** — it is amphichiral, it folds to F₄, its matter is vector-like. Items 6–7 are this wall.

**COMPUTED (this session, `sympy`):** on the geometric holonomy, **c ≠ θ**. The adjoint rep is always self-dual, so θ *fixes* the adjoint trace, while c *moves* it (the trace 37437270 + 38799960√3·i is non-real; its conjugate is the Galois image √−3↦−√−3). So the two involutions act differently on the same rep. The object's abundant chirality lives entirely in the c-column; the SM slot is the θ-column, and there it is flat.

---

## Part I — The inventory (every chirality, by proof tier)

### 1. The body is amphichiral (θ-symmetric) — THEOREM
The knot 4₁ is the canonical amphichiral knot: it equals its own mirror. In the program this is realized as **CS = 0 exactly** (real Chern–Simons action) and, at the algebra level, as the E₆→F₄ fold θ = Out(E₆) = ℤ/2 (T-θTANGENT in THEOREM_REGISTRY; B353/B521). **The amphichiral involution IS θ, canonically:** the sl₂-commutant of Aut(𝔢₆) is {1, θ}, θ = the E₆→F₄ diagram folding. This is the *body's* symmetry, and it is exactly the wall (see items 6–7).

### 2. B470 "chiral limbs on an amphichiral body" — COMPUTED (banked, firewalled)
`frontier/B470_reflection_campaign/FINDINGS.md`. The **limbs are the two towers** built from the object's word:
- **LETTER tower** (a→R, b→L, the Fibonacci word): **chiral from n=3 onward, CS ≠ 0** — a genuine chirality of the growth process.
- **BODY chain** (a→RL, b→RRLL, metallic letters): **mirror-breath at every rung, CS = 0** — amphichiral, because metallic letters are revswap-palindromes and any word in a palindromic alphabet is word-mirror (uv ∼cyc vu).
So the same object has an amphichiral *body* (item 1) carrying *chiral limbs* (the letter tower). The chirality is real but lives in the **word/orientation register (c)**, not the representation register. RF3 sharpens it quantum-mechanically: det(Par·W) = −ω^{#L−#R} runs a **Pisano-8 residue rhythm** on the letter tower, frozen at −1 on the body.

### 3. B356 — the chirality-window = Eisenstein ω — COMPUTED (banked, W1.2)
`frontier/B356_sigma_stability_scan/FINDINGS.md`. Enumerating all faithful 27-dim assemblies with an invariant cubic (necessary condition for a **chiral** G ↪ E₆): **complex (chiral-candidate) assemblies exist ONLY for A₄ and 2T** — exactly the two groups with nontrivial ℤ/3 abelianization (the ω-characters). S₄, 2O, A₅, 2I are closed by a **reality theorem** (every character real ⇒ every assembly self-dual/vector-like). So the *only* door to representation-level chirality is the Eisenstein ω = ℤ/3 twist — and even that is only character-level *necessary*, not *sufficient* (actual E₆ embedding with nondegenerate cubic = the still-open H103). **Determinant lemma (exact):** every SL(2,ℂ)-factoring route forces a quaternionic self-dual 2 — the "complex escape" is closed before branching.

### 4. The Breath campaign (B469) — the orientation ℤ/2 residue — COMPUTED (banked)
`frontier/B469_breath_campaign/FINDINGS.md`. The campaign object *is* the residue: the **orientation character**, the one ℤ/2 that survived every register.
- **BR1:** quantum residue det(Par@N) and classical residue sign(σ) both equal **(−1)^((N−1)/2)** — two registers breathe together.
- **BR2:** the residue's geometric carrier = the **orientation double cover** of the non-orientable half-monodromy bundle (family-uniform, verified in SnapPy).
- **The mechanism (banked):** the residue **IS the norm of the scale** — X_m companion matrix has det = −1, so BR2's orientation bit and the field-norm of the scaling unit are literally the same −1. **This residue is c, not θ**: it is carried by orientation reversal / complex conjugation (BR-note: "complex conjugation is orientation-reversing, and Vol is odd under it"). It sits squarely in the c-column.

### 5. B568 time-arrow — σ̄ not conjugate to σ — COMPUTED (banked)
`PROGRESS_LOG.md:3254`, `frontier/B568_own_questions/RESULTS.md` (Q2 arrow). **Dynamical chirality:** σ̄ is not conjugate to σ (exhaustive over all 24 permutations); **D_KL(ω‖ω̄) ≈ 12 bits**; **4 forbidden bigrams per direction, zero overlap**; arrow bidirectional (R=9 recognizable) but asymmetric. Complementary Q2 result: each self-coupling rung adds **exactly one bit** (H_n = n + H₀, deficit D = 0.14951… conserved). This is the strongest *positive* chirality the object carries — a genuine arrow — but again it is **orientation/time (c)**, tied via B303 to the sign of the CS-clock (CS(1,n) definite sign, CS(1,−n) = −CS(1,n)); it does not touch the 27↔27̄ representation slot.

### 6. B565-T3 — chiral index ≡ 0 (the fourth wall) — COMPUTED (banked, locked)
`frontier/B565_gauge_behavior_campaign/RESULTS.md`. On the anyon/species chain the **chiral index is identically 0** (exact chiral symmetry ~1e-14 up to N=8000, 2 word-sets + random controls; sublattice imbalance 0; amphichiral label pairing σ + (1−σ) = 1 exact for all 6 B546 labels; the one nonzero-looking winding was a closed-gap cond-1e16 artifact, honestly discarded). **The object is gauge-vector-like; SM matter is chiral (Nielsen–Ninomiya-rigid).** This is θ-symmetry read at the mechanism (index) level — the fourth, mechanism-level wall.

### 7. B569 — the 26 of F₄ is self-dual ⇒ vector-like for EVERY subgroup — THEOREM
`frontier/B569_complete_chain/FINDINGS.md`. A cross-seat handoff claimed the full σ→SM chain with a chiral 16 from 27 → 16 ⊕ 10 ⊕ 1. **Refuted by one line of Lie theory:** that is the Spin(10)×U(1) ⊂ **E₆** branching, and **Spin(10) ⊄ F₄**. Inside F₄, **27 = 1 ⊕ 26, and the 26 is self-dual** (its 24 nonzero weights are exactly the short roots of F₄, negation-closed; character real; 26 ≅ 26*). A self-dual rep restricts to a self-dual rep of *every* subgroup ⇒ **zero chiral theories on the F₄ stage** (not one). This is item 6 re-derived from pure Lie theory, independent of the object: *the stage itself refuses chirality*. (Also killed in B569: the handoff's "chirality bit" Z = −1 was a word artifact — the consistent E₆,₁ value is Z = +1, θ commutes-not-inverts.)

### 8. B565-H1 — the holonomy lands in F₄(ℂ)/E₆(ℂ) in NO real form — COMPUTED (banked, locked)
`frontier/B565_gauge_behavior_campaign/RESULTS.md`, `realform_adjoint_traces.py`. **THE REAL-FORM THEOREM:** the geometric holonomy is in **no real form** of F₄(ℂ)/E₆(ℂ):
  (i) **non-real adjoint traces** tr Ad_𝔢₆ ρ(a) = **37437270 + 38799960√3·i**, exact in ℚ(√−3), two witnesses / two code paths — kills all real forms;
  (ii) the regular-unipotent meridian (Jordan {3,9,11,15,17,23}) independently kills the compact forms.
TDV transfers only as the **complexified** statement (H₁ℂ ∩ H₂ℂ = 𝔰𝔩(3,ℂ) ⊕ 𝔰𝔩(2,ℂ) ⊕ ℂ). **The compact slice — what makes it a gauge group — is extra structure the hyperbolic geometry does not provide.** Non-reality = complex-conjugation (c) asymmetry: the object is *not* fixed by c.

**The two-faces theorem (PC25, locked, `test_two_faces_compactness_split`):**
- **ALGEBRA face** (character variety, E₆(ℂ)): provably **non-compact in every real form** (H1). Values-free, Galois-graded.
- **MEASUREMENT face** (Weil rep on ℂ¹⁵ = ℂ³⊗ℂ⁵, WRT/modular data): **unitary, finite image — compact, always.**
Compactness is a *measurement-face* feature; the algebra face never supplies it. The banked bridge is the volume-conjecture instance (B258 Kashaev ⟨4₁⟩_N → Vol).

---

## Part II — The adjudication: can the object's own chirality feed the SM slot?

### The two-sides reframe, stated precisely
The reframe (owner) is: Boyle's chirality construction needs the **complexified** Jordan algebra / **E₆(ℂ)** (not a compact real form), and B565-H1 says the object's holonomy is **exactly** non-real E₆(ℂ) — so the compactness-failure (H1) and the vector-like wall (T3/B569) might be **two views of one fact**: the object lives on the complex side, where chirality is possible.

### What is THEOREM here
1. **The object is θ-symmetric (amphichiral).** 4₁ = its mirror; CS = 0; θ = Out(E₆) = the E₆→F₄ fold is a genuine symmetry of the geometric object. (item 1, T-θTANGENT.)
2. **Through F₄ the matter is exactly vector-like.** 27|_{F₄} = 1 ⊕ 26, 26 self-dual ⇒ self-dual under *every* F₄ subgroup including G_SM = H₁∩H₂. Zero chiral theories on the F₄ stage. (items 6, 7.)
3. **The holonomy is complex-conjugation-asymmetric** (non-real adjoint traces; no real form). (item 8.)
4. **(COMPUTED this session) c ≠ θ on the geometric rep.** The adjoint is always self-dual ⇒ **θ fixes tr Ad**, while **c moves it** (non-real, its conjugate = the Galois image √−3↦−√−3). The two ℤ/2's act differently on the same representation.

### What the reframe gets RIGHT
The reframe's premise is sound and matches the repo: **the object does live on the complex side** (E₆(ℂ), no real form — H1), and **that is exactly where a complex 27 could exist** (Boyle's complexified J₃(𝕆)). Compactness-failure and complex-domain-ness *are* two views of one fact. This is correct and is the genuine "positive."

### Where the reframe BREAKS (the honest wall)
Being on the complex side is **necessary but not sufficient**. The SM's chirality is a *θ-fact* (27 ≠ 27̄ as reps of the SM subgroup), and the object's structure realizes θ as a **symmetry** (the amphichiral fold to F₄), not as a broken direction:
- **The E₆→F₄ fold = θ = the 27↔27̄ identification.** Folding to F₄ is *literally* passing to the θ-fixed locus, where 27 and 27̄ merge into 1⊕26. The object's amphichirality (why 4₁ = its mirror) is the *same* ℤ/2 as the vector-like wall. **Amphichiral ⟺ θ-symmetric ⟺ vector-like** is one identity, not a coincidence.
- The chirality the object **does** break is **c** (orientation/time/√−3-conjugation), a *different* ℤ/2, sitting on the algebra face's Galois grading. Items 2–5 are all c. My computed c ≠ θ shows breaking c does **not** break θ.
- So the two-sides reframe conflates two complexifications: E₆(**ℂ**) being non-real (a **c**-statement, true of the object) is not the same as the 27 being a **complex representation** in the θ-sense (a rep-duality statement, where the object is symmetric). Boyle needs the latter; the object supplies the former.

### The precise disposition
**The object HAS chirality — abundantly — but it is the wrong ℤ/2.** Its chirality is orientation/arithmetic/dynamical (c: the residue, the arrow, the chiral limbs, the √−7 chiral field, σ≠σ̄). The SM's chirality slot is representation-theoretic (θ: 27↔27̄), and the object is provably θ-symmetric (amphichiral → F₄ → self-dual 26). **No route currently in the repo carries a c-breaking into a θ-breaking.** The reframe correctly locates the object on the complex side but does not cross the gap: it identifies *where* chirality would have to live, not a mechanism that puts it there.

---

## Part III — The 2–3 sharpest COMPUTABLE next questions

These are exactly the questions that would confirm or refute the reframe by testing whether **c can be made to equal θ** on the geometric component.

**Q-A (the crux — reduce to SL(2,ℂ), cheap in SnapPy/sympy). Does complex conjugation c fix or MOVE the geometric component of the E₆ character variety?**
Concretely at the figure-eight level: is the entrywise-conjugate holonomy ρ̄ conjugate *within E₆(ℂ)* to ρ itself (c inner, fixes the component), or to θ∘ρ (c = θ, the reframe's dream), or to a genuinely distinct mirror component (c independent)? The cusp shape gives the handle: τ = −2√−3, c(τ) = +2√−3, and **4₁ is amphichiral** so there is an orientation-reversing isometry φ with ρ̄ ≅ ρ∘φ. Compute whether φ, pushed up to E₆, is inner, equals θ, or is a third thing. **If ρ̄ ≅ θ∘ρ → the reframe is vindicated (c = θ, the object's orientation-chirality IS the 27↔27̄ chirality — a major positive). If ρ̄ ≅ ρ → c and θ are independent and the wall is confirmed.** (My adjoint computation is preliminary evidence for the second: θ fixes tr Ad, c does not.)

**Q-B. Does θ (the E₆→F₄ fold / Out E₆) exchange the conjugate pair {ρ, ρ̄}, or fix each?**
Compute θ∘ρ and compare traces to ρ and ρ̄ on a generating set (meridian, longitude, the element a with tr Ad = 37437270+38799960√3·i). Because the *adjoint* is self-dual, θ fixes tr Ad(a) while c conjugates it — already computed this session ⇒ on the adjoint, **θ ≠ c**. The open piece is the **27** (not the adjoint): does θ on the 27-rep of the geometric holonomy equal c on the 27? This needs the 27-dim rep of the E₆ holonomy, buildable from the B347/B565 data. **This is the direct test of "does the object factor through the θ-fixed (F₄) locus,"** i.e. whether the vector-like wall is intrinsic or an artifact of the fold choice.

**Q-C. Does the σ/σ̄ ℤ/2 residue (B469 orientation character, B568 arrow) map to the 27↔27̄ swap or to the √−3↔−√−3 cusp conjugation?**
Trace the dynamical residue (−1)^((N−1)/2) — carried by the orientation double cover (BR2) — up through the holonomy to see whether it acts on the E₆ rep as **c** (cusp-shape conjugation, orientation reversal) or as **θ** (27↔27̄). The BR2 mechanism (residue = norm of the scale = orientation reversal) strongly predicts **c**, which would *confirm* items 2–5 all live in the c-column and are disjoint from the SM's θ-slot — closing the reframe honestly. A surprise (residue ↦ θ) would be the single most important positive the program could produce. **Cheapest of the three:** it is a map-tracking computation on already-banked residue and cover data, no new heavy machinery.

---

## Source files (all absolute)
- `/Users/dri/origin-axiom/frontier/B470_reflection_campaign/FINDINGS.md` — chiral limbs / amphichiral body, CS towers, RF3 residue rhythm
- `/Users/dri/origin-axiom/frontier/B356_sigma_stability_scan/FINDINGS.md` — chirality-window = Eisenstein ω, reality theorem, det-lemma
- `/Users/dri/origin-axiom/frontier/B469_breath_campaign/FINDINGS.md` — orientation ℤ/2 residue = norm of the scale, orientation double cover
- `/Users/dri/origin-axiom/frontier/B568_own_questions/RESULTS.md` — Q2 arrow (each rung +1 bit); + `PROGRESS_LOG.md:3254` σ̄≠σ, D_KL≈12 bits, 4 forbidden bigrams
- `/Users/dri/origin-axiom/frontier/B565_gauge_behavior_campaign/RESULTS.md` — T3 chiral index ≡ 0, H1 real-form theorem, two-faces split
- `/Users/dri/origin-axiom/frontier/B565_gauge_behavior_campaign/realform_adjoint_traces.py` — the non-real adjoint trace + Jordan-type reproducer
- `/Users/dri/origin-axiom/frontier/B569_complete_chain/FINDINGS.md` — 26 of F₄ self-dual ⇒ vector-like for every subgroup; Z=+1 correction
- `/Users/dri/origin-axiom/docs/THEOREM_REGISTRY.md` — T-θTANGENT (amphichiral involution = θ = Out E₆), T-MIRROR
- `/Users/dri/origin-axiom/PROGRESS_LOG.md` — PC25 (real-form theorem), B303 (CP sign = CS-clock sign = arrow), Door-2 amphichirality-allows-not-forces

**Tier legend used:** THEOREM = proven/standard Lie theory; COMPUTED = in-sandbox verified + locked; OPEN = the Q-A/Q-B/Q-C next steps; SPECULATIVE = none banked here (the reframe is treated as a *hypothesis to test*, correctly placed, not crossed).