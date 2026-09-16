# B1369 — THE FAMILY IN THE STANDARD-MODEL FRAME: a chiral generation from bulk matter with the Standard Model unbroken needs a *free cusp* — a cusp whose peripheral image in H₁(M; ℚ) has rank below b₁ — and 77 of the figure-eight family's 112 members have none, the two-cusped siblings m202 and s959 among them; on the 35 members that do, the region-swap parity, run with the isometries' exact action on H₁, kills the partition on 79 of the 83 free cusps; four cusps on four members remain, each with a unique shortest cusp mode — the residual of sL-1

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** NEGATIVE on 108 of 112 members (the free-cusp theorem on 77, parity on 31 more; B1351 (ii) under the whole-torus/annular conventions, the R23 scoping stated) + PROVED (the free-cusp theorem; the region-swap lemma in its general form; the instrument's self-tests) + OPEN on four cusps (o10_150688, o10_150708 cusp 0, o10_150716, o10_150725 cusp 1) · **Price: unchanged** · **Numbering:** B1369 (sL-1 registered by the capstone).

## 0. Seen from above

The owner's question after the verdict of the object: does physics come from the family rather than from m004 alone? In the seat's
frame the question has a precise shape. A bulk sector on a member M is an SL(2)_β-spin times a character χ_w of H₁(M) (B1368), it
carries a chiral index only when it is cusp-fixed on some cusp, non-unitary there (a Higgs field to partition the torus) and its
partition is a disc (B1351 (ii)), and the two halves of a generation never share a spin, so the spin-0 half — a character alone —
must be chiral on its own. A spin-0 sector is cusp-fixed on cusp c exactly when χ_w is trivial on the peripheral subgroup P_c; if the
image of P_c in H₁(M; ℚ) has full rank b₁, χ_w factors through the finite group H₁/P_c, has finite order, is unitary, has no Higgs
field and no index. So a full generation needs a **free cusp**: rank P_c < b₁. This is the one-cusp theorem of B1368 with the
correct multi-cusp hypothesis, and it is decided by homology alone, for every flat connection. The census of B1186's 112 members:
77 have no free cusp — all 54 one-cusped members with b₁ = 1 and 23 multi-cusped members whose every peripheral rank equals b₁, m202
and s959 (ranks [2, 2], b₁ = 2, peripheral subgroups of index 7) among them. The carriers of the count of three are closed by rank.
The 35 members with a free cusp carry 83 of them, and there the isometries decide: an isometry fixing the cusp and acting by −1 on
every free class pulls each Higgs form back to its negative, so its restriction to the torus maps the positive region of the leading
cusp mode onto the negative one, χ(∂⁺) = χ(∂⁻) = 0 — fc R71's region-swap lemma, whose proof never needed the torus action to be
−1. Run with the isometries' exact action on H₁ (the combinatorial automorphisms of the canonical retriangulation, a new instrument
checked against SnapPy on every member), parity closes 79 of the 83 free cusps, four of them only by orientation-reversing
isometries. Four cusps on four members remain — o10_150688, o10_150708 (cusp 0), o10_150716, o10_150725 (cusp 1) — where every
isometry fixing the cusp acts by +1 on a free class; their partitions must be computed, and each cusp lattice has a unique shortest
dual vector, so the partition is annular unless the harmonic form's leading coefficient vanishes. 108 of 112 members closed; the
residual is sL-1's remaining work, named with its instrument.

## 1. The frame on a member with several cusps

1. **Sectors.** A flat E₆(ℂ) connection leaving the Standard Model unbroken has its image in c(SM) = SL(2)_β × ℂ*² (B1366, B1368): a
   representation ρ of π₁(M) into SL(2)_β times a character on the Cartan directions (Y, γ). Every bulk sector is a spin of SL(2)_β
   times a character χ_w of H₁(M); the index of B1351 (ii), N = −χ(∂⁺M; L), is non-zero only on a sector that is cusp-fixed on some
   cusp (a vector fixed by the peripheral holonomy, B1268's h⁰(∂M; V)), non-unitary there (the Higgs field is the real part of log χ_w
   on the weight, B1368 §2) and whose leading cusp mode cuts that torus into discs.
2. **Spin 0.** Cusp-fixed on cusp c ⇔ χ_w trivial on P_c. If the image of P_c in H₁(M; ℚ) has rank b₁, then χ_w factors through the
   finite group H₁(M)/P_c: finite order, unitary, Higgs field zero, ∂⁺ = ∅, N = 0. A non-unitary cusp-fixed spin-0 sector lives on
   cusp c iff **rank P_c < b₁** — a *free cusp* — and then its Higgs class lies in ann(P_c) ⊂ H¹(M; ℝ), the *free classes* of that
   cusp, of dimension b₁ − rank P_c.
3. **Spin ½.** For a representation whose peripheral holonomy is parabolic (the geometric one and its conjugates), the common
   eigenvector of ρ(μ), ρ(λ) has eigenvalues ε_μ, ε_λ ∈ {±1} (the lift's signs; on m004 ε_λ = −1 by Calegari), and ρ ⊗ χ_w has a
   fixed vector on cusp c iff χ_w restricted to P_c is the sign character (ε_μ, ε_λ). Then |χ_w| = 1 on P_c and the Higgs class again
   lies in ann(P_c): the spin-½ half needs a free cusp too, and its partition is that of a free class — the same parity applies. (At
   non-parabolic points of the character variety the peripheral eigenvalues may be non-unitary and the Higgs field has periods on
   the torus; B1368's golden reducible points are of this kind on m004. Those give at most half a generation and do not touch the
   spin-0 half, on which the theorem rests.)
4. **The spin split (B1368).** In the 27 the 10 of SU(5) is spin 0 and the 5̄ spin ½; in the 78 the reverse. Whichever frame, one
   half of every generation is a spin-0 sector, so **a chiral generation from bulk matter with the Standard Model unbroken needs a
   free cusp, and on a free cusp its spin-0 half needs a disc partition of a free class's leading cusp mode.**

## 2. Computed

`verification/siblings_in_the_sm_frame.py` with `verification/family_isometries.py` (SnapPy 3.3.2, sympy; exact over ℚ except the
lifted traces and the cusp moduli, which are floating-point; record `siblings_in_the_sm_frame_run.txt`).

| item | result |
|---|---|
| the family | B1186's 112 members; cusps: 60 one-cusped, 38 two-cusped, 10 three-cusped, 3 four-cusped, 1 five-cusped |
| b₁ and the peripheral ranks | from SnapPy's fundamental group: b₁ = generators − rank of the abelianised relators; rank P_c = the rank added by the abelianised meridian and longitude of cusp c |
| free cusps | **83 on 35 members**; **77 members without one**: all 54 one-cusped members with b₁ = 1, and 23 multi-cusped members with every peripheral rank equal to b₁ |
| one-cusped members with b₁ = 2 (a free cusp) | 6: t06828, o10_150688, o10_150713, o10_150714, o10_150716, o10_150724 |
| m202 | H₁ = ℤ², ⟨a, b \| aabbAbAABBaB⟩; P₀ = ⟨(−2, 3), (1, 2)⟩ and P₁ = ⟨(−1, 3), (−3, 2)⟩ both of index 7, P₀ + P₁ = H₁; lifted traces (+2, +2) on both cusps; 12 isometries (D₆), 6 swap the cusps, 2 are B1321's order-3 rotation (\|det(A − I)\| = 3 on both cusps); spin-0 cusp-fixed on cusp c ⇔ χ_w⁷ = 1; the spin-½ half (a whole 10 in the (2,20) of the 78) cusp-fixed on cusp 0 with all 22 non-SM roots non-trivial: 266 characters on a grid of 1 225, every one of finite order |
| s959 | H₁ = ℤ/3 ⊕ ℤ²; ranks [2, 2]; lifted traces (+2, −2) on cusp 0 and (−2, −2) on cusp 1; 12 isometries (D₆), 6 swap the cusps, 2 are the order-3 rotation |
| the instrument | on every one of the 35 candidates: \|Aut(canonical retriangulation)\| = \|Isom(M)\| (SnapPy), b₁ and the peripheral ranks (link graphs) equal to SnapPy's, ∂∂ = 0, every automorphism a chain map with unimodular action on H₁; on the 73 free cusps of members whose peripheral classes span H₁, the direct action on the free classes and the torus-action types agree with the inference from SnapPy's cusp maps |
| parity | **79 of 83 free cusps closed**: 75 by an isometry fixing the cusp, negating every free class and acting on the torus by ±I (R71's form); 4 (o10_150684 both cusps; o10_150725 cusps 0 and 2) only by the general lemma — the closing isometries reverse orientation (determinant −1 on the torus) |
| the residual | 4 cusps: o10_150688 cusp 0, o10_150708 cusp 0, o10_150716 cusp 0 (one free class each; every fixing isometry acts by +1 on it), o10_150725 cusp 1 (two free classes; the fixers negate one line — the Higgs classes on that line are closed, the rest open). Reduced cusp moduli (5√3/2)i, −½ + (3√3/2)i, (5√3/2)i, −½ + (3√3/2)i (\|τ\| = 4.33, √7, 4.33, √7): a unique shortest dual vector on every one |
| the verdict | **108 of 112 members closed** (77 by rank, 31 by parity); 4 members with an open cusp |
| longitude census (aside) | of the 60 one-cusped members, SnapPy's longitude is rationally null-homologous on 7 and integrally null-homologous (in the commutator subgroup) on 3; on those the lift's trace is −2 (Calegari); elsewhere the trace's sign is the lift's choice on a torsion or non-null class |

## 3. The theorems

**(i) The free-cusp theorem.** On a cusped hyperbolic 3-manifold M, a spin-0 sector cusp-fixed on cusp c with a non-zero Higgs field
exists iff rank P_c < b₁(M). *Proof.* Cusp-fixed means χ_w = 1 on P_c; χ_w descends to H₁(M)/P_c, which is finite iff rank P_c = b₁;
a character of a finite group has finite order, hence |χ_w| = 1 and the Higgs field Re log χ_w vanishes on the weight. Conversely, a
character of infinite order trivial on P_c exists iff H₁/P_c is infinite, and it can be chosen non-unitary (ℂ* is divisible). ∎
With the spin split (B1368: in each matter frame one half of a generation is spin 0), no member without a free cusp gives a chiral
generation from bulk matter with the Standard Model unbroken, for every flat connection — 77 of 112, m202 and s959 among them.

**(ii) The region-swap lemma, general form.** Let g be an isometry of M fixing cusp c and acting by −1 on ann(P_c) ⊂ H¹(M; ℝ). Then
every cusp-fixed spin-0 sector on c has N = 0. *Proof.* The Higgs class [ω] of such a sector lies in ann(P_c); g*ω = −ω as harmonic
forms (g* preserves harmonicity and negates the class). g preserves the cusp's height coordinate and acts on the torus by an isometry
σ, so the leading cusp mode F of ω (the dt-coefficient's lowest Fourier component, whose sign cuts the torus into ∂⁺ and ∂⁻) satisfies
F∘σ = −F. σ is a homeomorphism mapping {F > 0} onto {F < 0}: χ(∂⁺) = χ(∂⁻), and with transverse zeros χ(∂⁺) + χ(∂⁻) = χ(T²) −
χ(zero set) = 0. Both vanish; N = −χ(∂⁺) = 0. ∎ This is fc R71's theorem (B1281 §2D, verified on main in B1417) with the hypothesis
"σ = −1 on the torus" dropped: nothing in the proof used it. It applies to the spin-½ half on the same cusp, whose Higgs class is a
free class too (§1.3).

**(iii) The verdict on 108 members.** On the 35 members with a free cusp, the isometries' action on H₁ is computed exactly from the
canonical retriangulation (§2, the instrument), and an isometry as in (ii) exists on 79 of the 83 free cusps. On those cusps no spin-0
sector — hence no half of a generation — is chiral; the 31 members all of whose free cusps are closed join the 77: **108 of 112.** The
four residual cusps are named; there every isometry fixing the cusp acts by +1 on some free class and the lemma is silent.

## 4. What it means

1. **The siblings are closed by rank.** m202 and s959, the two members that carry the count of three (B1321's order-3 rotation; fc's
   count on m202, B1282), have both peripheral subgroups of full rank: every cusp-fixed spin-0 sector on either cusp is a character of
   order dividing 7 on m202, unitary on both. Whatever those counts are, they are not a chiral generation in this frame — the question
   in the capstone's §6.1 ("can a spin-0 charged sector be cusp-fixed on one cusp while non-trivial through the other?") has the
   answer *only with finite order*. The spin-½ half of m202 can be cusp-fixed with the Standard Model unbroken (266 characters), but
   only unitarily: no Higgs field, no index.
2. **What a free cusp is.** Its free classes are the 1-forms with vanishing periods on that torus — on a one-cusped member the image
   of H¹(M, ∂M) in H¹(M), the duals of the closed surfaces of M (half of H₁(∂M) dies, so rank P = 1 and the free classes number
   b₁ − 1). A one-cusped member has a free cusp iff b₁ ≥ 2 — six of the sixty do. The count-carrying siblings have b₁ = 2 with
   two cusps of full rank: their second Betti number is spent on the cusps.
3. **Parity in its general form matters.** Four cusps are closed only by orientation-reversing isometries (torus action of order 2
   with determinant −1), which R71's statement (σ = −1) did not cover; the proof covers them, and the arc records the general form.
   On o10_150725's rank-1 cusp the fixers negate one of the two free classes: parity closes the sectors whose Higgs class lies on that
   line and is silent on the rest.
4. **The residual, and what decides it.** On the four open cusps the partition of a free class's leading cusp mode must be computed.
   The first fact about it is a lattice fact: each of the four cusps has a unique shortest dual vector (reduced moduli (5√3/2)i and
   −½ + (3√3/2)i), so a harmonic form's leading cusp mode is cos(2πk·x + φ) whenever its coefficient at that vector is non-zero — an
   annular partition, N = 0. Whether the coefficient vanishes (a symmetry can force it: an isometry acting by +1 on the class and by a
   translation on the torus with k·v ∉ ℤ kills the mode) is the harmonic form's cusp expansion, or the isometries' affine action on
   the torus — neither computed here. On the three cusps with one free class, every weight's Higgs field is a multiple of one
   harmonic form, so the spin-0 half of a generation has one partition up to sign, and the sign pattern across the 10 (Y·a + γ₁₀·b on
   Y ∈ {1/6, −2/3, 1}) is uniform only when the γ-component dominates — a constraint for the residual's future computation, not a
   closure.
5. **The three faces.** The free-cusp theorem is homology (the peripheral image and the Betti number); the parity is the isometry
   group acting on the harmonic forms; the index is the quantum theory's. Complementary to main's B1418 (the class census, the
   reducible locus, the sibling and tower relations): B1418's cells ask what the family's members are, this arc asks what they
   can carry in the seat's frame, member by member, and answers for 108 of them.

## 5. Caveats

1. The frame is B1351's (Pantev–Wijnholt on the cusped manifold, abelian Higgs data per sector) with B1368's placement in
   SL(2)_β × ℂ*²; the disc-convention scoping (R23) is as in B1368 §3.2, and the free-cusp theorem's first half — unitary, no Higgs
   field, no partition — holds in every convention.
2. The parity lemma needs transverse zeros of the leading mode (B1281 §2D; B1417's scoping: a non-transverse zero set leaves χ(∂⁺M)
   undefined rather than non-zero, and any allowed perturbation returns 0).
3. The spin-½ discussion (§1.3) assumes parabolic peripheral holonomy; the theorem does not use it.
4. The retriangulation's cusp numbering is matched to the manifold's by the peripheral-rank profiles (equal as lists on every
   member) and by the torus actions against SnapPy's cusp maps (73 cusps, all agree). The 10 free cusps on members whose peripheral
   classes do not span H₁ (o10_150688, o10_150691, o10_150712, o10_150713, o10_150714, o10_150716, o10_150724, t06828) have no
   cusp-map cross-check; their verdicts rest on the direct instrument and its self-tests (∂∂ = 0, the chain-map identity, |Aut| =
   |Isom|, b₁ and the ranks). Of these, 8 are closed by parity and 2 (o10_150688, o10_150716) are open.
5. The leading-mode observation on the residual (§4.4) is not a closure; it names the quantity that would be.
6. The longitude census is an aside: Calegari's −2 is checked only where SnapPy's longitude lies in the commutator subgroup; on a
   torsion or non-null class the lift's sign is a choice and the traces +2 there are not counter-examples.

## 6. Registered

sL-1 stays open on the residual only: four cusps on o10_150688, o10_150708, o10_150716, o10_150725, with the instrument that decides
them named (the harmonic form's cusp expansion at the free cusp, or the isometries' affine action on the torus together with the
leading-mode lemma). Nothing else new; the two-cusped siblings and the one-cusped members are closed in this frame.

## Verification

`verification/siblings_in_the_sm_frame.py` (about a minute; record `siblings_in_the_sm_frame_run.txt`): (A) the family sweep —
cusps, H₁, b₁, peripheral ranks, lifted peripheral traces, the free-cusp census, the longitude census; (B) m202 and s959; (C) m202's
spin-½ half with the Standard Model unbroken; (E) on every member with a free cusp, every isometry fixing it with its torus action and
its action on the free classes, from `verification/family_isometries.py` — the dual 2-complex of SnapPy's canonical retriangulation,
its H₁, the link graphs' cycle spaces (the peripheral subspaces and the cusp tori), t3mlite's combinatorial automorphisms as signed
permutations of cells — with the cusp-map inference kept as a cross-check; (F) the residual cusps' eigenspaces and lattices; (D) the
verdict. Lock: `tests/test_b1369_the_siblings_in_the_sm_frame.py` (the whole script, about a minute, plus the instrument on two members).

**Sources.** B1351 (the index on a cusped manifold), B1368 (sectors, cusp-fixedness, the spin split, the golden reducible points),
B1366 (c(SM)), B1281 §2D (fc R71's region-swap theorem) and main's B1417 (its verification and scoping), B1282 (m202's isometries and
its germ), B1186 (the family census `members_B`), B1352 (the partitions computed on m004's deformations); main's B1321 for the order-3
rotation's count of three on m202 and s959, main's B1418 (DESIGN, the family as the object). Epstein–Penner for the canonical cell
decomposition; SnapPy's `canonical_retriangulation` and t3mlite's `isomorphisms_to`; Calegari, *Real places and torus bundles* (2006).

*(Currency 2026-09-16, B1370: the four residual cusps' tori developed from the tetrahedra shapes and every fixing isometry's affine
action computed (translation parts included); the unique shortest dual vector is an allowed mode for every Higgs class on all four,
so §4.4's conditional is sharpened — annular unless the harmonic form's coefficients at the first 4, 2, 4, 2 allowed single-direction
shells all vanish; no symmetry forces it. The residual is one Fourier coefficient per cusp. `frontier/B1370_the_residuals_leading_mode`.)*
