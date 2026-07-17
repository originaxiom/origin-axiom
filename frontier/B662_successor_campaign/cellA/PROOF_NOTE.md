# CELL A — L101: the (i₁, i₂) metallic-uniformity theorem

**Claim.** For every metallic once-punctured-torus-bundle member, with
V = the 27-dimensional module of the principal SL(2) ⊂ E₆
(V ≅ Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰ as a principal-SL(2) module),

- i₁ := dim V^{ρ(π₁)} = 1, and
- i₂ := dim V^{ρ(P)} = 3, where P ≅ ℤ² is the peripheral (cusp) subgroup —
  exactly one line per block.

**Status: PROVEN + VERIFIED** — the theorem is proved below with every
step either proved inline or flagged as a cited standard input, and every
member-specific hypothesis plus both conclusions are verified by exact
arithmetic on both banked members (fig-8/golden m = 1 over K = ℚ(√−3);
silver m = 2 over L = ℚ(s, i), s⁴ = 8s² + 16). Verification manifest in
§8; full run output in `cellA_output.txt`.

---

## 0. Setting and conventions

**The metallic family.** Member m ≥ 1: M_m = the once-punctured-torus
bundle over S¹ with monodromy word RᵐLᵐ (banked convention: m = 1 is the
golden/fig-8 member, monodromy RL, trace 3; m = 2 is the silver member,
monodromy RRLL, trace 6 — B649 prereg). The monodromy matrix of RᵐLᵐ has
trace m² + 2 > 2, so it is Anosov for every m ≥ 1.

**Holonomy.** hol: π₁(M_m) → PSL(2,ℂ) is the holonomy of the complete
finite-volume hyperbolic structure.
[CITED — the single geometric input: Thurston's hyperbolization of
punctured-torus bundles with Anosov monodromy. It supplies, for every m:
(H1) M_m is a complete 1-cusped finite-volume hyperbolic 3-manifold;
(H2) hol is discrete and faithful;
(H3) the peripheral subgroup P ≅ ℤ² maps to parabolic isometries fixing a
single point of ∂H³ (completeness at the cusp).
For the two banked members every consequence of (H1)–(H3) that the proof
uses is *independently re-verified by exact computation* — checks F2–F6,
S2–S5b — so nothing about the banked verdicts rests on the citation.]

**Presentations actually banked.** fig-8: the 2-bridge presentation
⟨a, b | R⟩, R = abABaBAbaB, peripheral pair (μ, λ) = (a, LONG),
LONG = abABaaBAbA (B575/B637 machinery). silver: ⟨a, b, c | aBAbcc,
aaCbcB⟩, peripheral pair (μ, λ) = (CCB, caCA) (B649 machinery). The
relators are verified to hold exactly at both the SL(2) and the 27 level
(F1, F10, S1, S8).

**The 27.** W: SL(2,ℂ) → GL(27,ℂ) is defined by the banked exact rational
sl₂-triple (e_pr, f_pr, h_pr) ⊂ gl₂₇ via the LDU lift (`lift_sl2`):
g = [[p,q],[r,s]], p ≠ 0 ↦ exp((r/p)f_pr) · D(p²/det) · exp((q/p)e_pr),
D(t²) = diag(t^{wgt_i}), with the Weyl-swap factorization when p = 0.
Verified exactly: the brackets [e,f] = h, [h,e] = 2e, [h,f] = −2f; h_pr
diagonal with **even integer** weights (F7, S6). W is the restriction to
matrices of the unique algebraic-group morphism SL(2) → GL(27) with
differential e ↦ e_pr, f ↦ f_pr [CITED: existence/uniqueness for simply
connected SL(2), Chevalley; concretely realized by the banked lift, whose
homomorphism property on every word this cell uses is verified exactly —
F10, S8: the banked 27-letters equal lift_sl2 of the SL(2) letters, and
the 27-products along all peripheral words equal the lifts of the SL(2)
products].

**No lift ambiguity.** All h-weights are even, so W(−I) = I (directly:
the lift formula at p = −1, q = r = 0 gives D = I). Hence W factors
through PSL(2,ℂ) and ρ₂₇ := W ∘ hol is well-defined on π₁(M_m) with no
choice of SL(2)-lift; the banked SL(2) letters are one convenient lift
and every statement below is lift-independent.

**Block structure.** Cas := e·f + f·e + ½h² commutes with e, f, h
(verified exactly), and its eigen-kernels on the 27 have dimensions
dim ker(Cas − 144) = 17, dim ker(Cas − 40) = 9, dim ker(Cas − 0) = 1,
summing to 27 (F8, S6). With [CITED: Weyl complete reducibility and the
classification of finite-dimensional irreducible sl₂(ℂ)-modules V(k),
dim V(k) = k + 1, Casimir value k(k+2)/2] this forces
V ≅ V(16) ⊕ V(8) ⊕ V(0), each with multiplicity one: k(k+2)/2 = 144, 40,
0 has unique non-negative solutions k = 16, 8, 0, and each eigenspace
dimension equals dim V(k) exactly. Corroborated: dim ker(e_pr) = 3 — one
highest-weight line per summand (F9, S7).

**Field remark.** All kernels are computed over the exact coefficient
field (K resp. L). Rank, hence kernel dimension, of a matrix is unchanged
under field extension, so every computed dimension equals the ℂ-dimension
that the theorems address.

---

## 1. Two lemmas on unipotents in Symᵏ

**Lemma 1 (centralizer of a noncentral parabolic).** Let p ∈ SL(2,ℂ)
with tr p = 2ε, ε ∈ {±1}, p ≠ ±I. Set N := p − εI. Then N ≠ 0, N² = 0
(char poly (t − ε)²; Cayley–Hamilton), rank N = 1, ker N = im N = ℂw
(w := the fixed vector). If q ∈ SL(2,ℂ) commutes with p, then
q = ε′(I + tN) for some ε′ ∈ {±1}, t ∈ ℂ. In particular q w = ε′w, and q
is either ±I or a noncentral parabolic with the *same* fixed line.

*Proof.* qp = pq ⟺ qN = Nq. Then q(ker N) = ker N, so qw = λw. In a
basis (w, w′): q = [[λ, μ], [0, λ⁻¹]], N = [[0, x], [0, 0]] with x ≠ 0.
qN = [[0, λx], [0, 0]] and Nq = [[0, xλ⁻¹], [0, 0]]; equality forces
λ² = 1. Writing ε′ = λ: q = ε′(I + tN) with t = ε′μ/x. ∎

**Lemma 2 (Symᵏ of a nontrivial unipotent is one Jordan block).** Let
u = I + N with N ≠ 0, Nw = 0, and k ≥ 1. Then
dim Fix(Symᵏ(u)) = 1 and Fix(Symᵏ(u)) = ℂ·wᵏ.

*Proof.* Choose the basis (w, w′) as above: u(w) = w,
u(w′) = xw + w′, x ≠ 0. In the monomial basis v_j = w^{k−j}w′^j
(j = 0,…,k):
Symᵏ(u)·v_j = w^{k−j}(xw + w′)^j = Σ_{t=0}^{j} C(j,t) xᵗ v_{j−t},
so (Symᵏ(u) − 1)v₀ = 0 and (Symᵏ(u) − 1)v_j = jx·v_{j−1} + (terms in
v_{j−2},…), j = 1,…,k. The k images are triangular with nonzero leading
coefficients jx, hence linearly independent: rank(Symᵏ(u) − 1) = k and
ker = ℂ·v₀ = ℂ·wᵏ. ∎

*Sign remark.* Symᵏ(ε u) = εᵏ Symᵏ(u) = Symᵏ(u) for **even** k. All
blocks of V have even k (16, 8, 0), so the ±-ambiguity of parabolic
lifts dies on every block.

**Lemma 3 (independent directions stay independent in Symᵏ).** If w, w′
are linearly independent in ℂ², then wᵏ and w′ᵏ are linearly independent
in Symᵏ for every k ≥ 1. *Proof.* In the basis (w, w′) they are two
distinct monomial basis vectors. ∎

---

## 2. Theorem 1: i₂ = 3 (one line per block)

**Theorem 1.** Let P = ⟨μ, λ⟩ ≅ ℤ² be the peripheral subgroup of M_m.
Then dim V^{ρ₂₇(P)} = 3, and the joint fixed space meets each block
Sym¹⁶, Sym⁸, Sym⁰ in exactly one line.

*Proof.* Since μ, λ generate P, V^{ρ₂₇(P)} = Fix(ρ₂₇(μ)) ∩ Fix(ρ₂₇(λ)).

(a) hol(μ) is a noncentral parabolic — input (H3); verified exactly for
both banked members (F3: tr ρ(a) = 2, ρ(a) ≠ I; S3: tr MU2 = ±2,
MU2 ≠ ±I). Fix an SL(2)-lift p = ρ(μ) = ε₁(I + N), N ≠ 0, Nw = 0.

(b) ρ(λ) commutes with p: μλ = λμ in P and ρ is a homomorphism —
verified exactly at the matrix level (F5, S4) *and* at the group level
by van Kampen certificate: fig-8 [LONG, a] = 1 certified and
replay-verified in this cell (F6); silver [LAM, MU] = 1 certified in the
banked B649 stage-3b-ii run (peripheral commutator |word| = 14,
AREA = 4). By **Lemma 1**, ρ(λ) = ε₂(I + tN): both peripheral images are
±(unipotent) *sharing the fixed vector w* — verified directly (F4: the
longitude matrix is upper-triangular with diagonal (d, d), d² = 1,
nonzero off-diagonal entry, in the frame where ρ(a) fixes e₁; S5: the
explicit common kernel vector w over L). Faithfulness (H2) gives
ρ(λ) ≠ ±I; verified (F4 off-diagonal ≠ 0; S3).

(c) Count per block. On Symᵏ, k ∈ {16, 8} (even):
Fix(Symᵏ(ρ(μ))) = Fix(Symᵏ(I + N)) = ℂ·wᵏ by Lemma 2 and the sign
remark; and Symᵏ(ρ(λ))·wᵏ = ε₂ᵏ((I + tN)w)ᵏ = wᵏ. So the joint fixed
space of the pair on that block is *exactly* ℂ·wᵏ — dimension 1. On
Sym⁰ both act trivially — dimension 1.

(d) Total: i₂ = 1 + 1 + 1 = 3. ∎

Verified directly on the 27, both members: dim of the stacked kernel = 3
(F13, S11); per-block joint dims (1,1,1) via Casimir-stacked kernels
(F15, S13); 27-level commutation (F14, S12).

**The flagged subtlety.** Commuting parabolics do *not* automatically
share a fixed vector (±I commutes with everything); it is noncentrality
of one member of the pair that forces the common frame, via Lemma 1.
Both banked pairs are verified noncentral on *both* generators. And for
the pair the joint fixed dimension per positive block is exactly 1 — the
two fixed lines coincide (they do not contribute 1 + 1): this is
Theorem 1(c), verified per block by F15/S13.

---

## 3. Theorem 2: i₁ = 1 — the elementary route

**Theorem 2.** dim V^{ρ₂₇(π₁(M_m))} = 1, namely the Sym⁰ line.

*Proof.* (≥) Sym⁰ = V(0) is W-trivial, so Sym⁰ ⊆ V^{ρ₂₇(π₁)}.

(≤) Claim: the image group contains two noncentral parabolics p, q whose
fixed vectors w_p, w_q are linearly independent.

- Banked members, verified exactly: fig-8 — ρ(a) and ρ(b) are both
  noncentral parabolics with independent fixed vectors (F3, F3b);
  silver — MU2 and ρ(g)·MU2·ρ(g)⁻¹ for an exhibited generator g, with
  w and g·w verified independent (S3, S5b).
- Every member m: hol(μ) is noncentral parabolic by (H3); its conjugate
  by g has fixed vector g·w. If g·w ∥ w for *every* g ∈ π₁ then the
  whole image fixes the line ℂw, i.e. hol is reducible; a group fixing a
  point of P¹ is conjugate into the upper-triangular group, which is
  solvable — but hol is faithful (H2) and π₁(M_m) ⊇ F₂ (the fiber
  once-punctured-torus group), and F₂ is not solvable (F₂ surjects onto
  the nonsolvable A₅; quotients and subgroups of solvable groups are
  solvable [standard]). So some g moves the line, giving q with
  w_q = g·w_p independent of w_p.

Now let v ∈ V^{ρ₂₇(π₁)}. Then v ∈ Fix(W(p)) ∩ Fix(W(q)). Per block
Symᵏ, k ∈ {16, 8}: by Lemma 2 (+ sign remark) the block components
satisfy v_k ∈ ℂ·w_pᵏ ∩ ℂ·w_qᵏ = 0 by Lemma 3. Hence v ∈ Sym⁰. ∎

Verified directly, both members: the stacked generator kernel has
dimension exactly 1 (F11, S9), and the invariant line is killed by e_pr
and f_pr — it *is* the Sym⁰ block (F12, S10).

Note what this route does **not** need: no Zariski closure, no
classification of algebraic subgroups, no invariant theory — only
Lemmas 1–3 (self-contained) plus the block structure of §0. The route
below establishes the preregistered density statement as well.

---

## 4. Theorem 2′: i₁ = 1 — the Zariski-density route (the prereg sketch made rigorous)

**Proposition 3 (density criterion, trace conditions).** Let
Γ ≤ SL(2,ℂ) be a subgroup such that
(i) some pair X, Y ∈ Γ has tr(XYX⁻¹Y⁻¹) ≠ 2, and
(ii) Γ contains a noncentral parabolic p.
Then Γ is Zariski-dense in SL(2,ℂ).

*Proof.* Let H = the Zariski closure of Γ, H° its identity component —
an algebraic subgroup of finite index, irreducible as a variety [CITED:
finiteness of components and irreducibility of the identity component
of a linear algebraic group].

*Step 1 (a one-parameter unipotent inside H).* With N = p − εI as in
Lemma 1, ⟨p²⟩ = {I + 2nN : n ∈ ℤ} ⊆ H is an infinite subset of the line
{I + tN : t ∈ ℂ} ≅ 𝔸¹; an infinite subset of 𝔸¹ is Zariski-dense in it,
and H is closed, so U_N := {I + tN : t ∈ ℂ} ⊆ H. Since U_N is connected
and contains I, U_N ⊆ H°.

*Step 2 (irreducibility).* If all of Γ had a common eigenvector, then in
a triangularizing basis every commutator XYX⁻¹Y⁻¹ would be upper
triangular with diagonal (1, 1), hence trace 2 — contradicting (i). So
Γ, and a fortiori H, has no common eigenvector, i.e. H fixes no point
of P¹.

*Step 3 (classification of the possibilities for H°).* Suppose H ≠ SL(2,ℂ).
- dim H° = 3 is impossible: H° would be a closed irreducible subvariety
  of full dimension in the irreducible 3-fold SL(2,ℂ), hence equal to it.
- dim H° = 0: H is finite; but p has infinite order (pⁿ = εⁿ(I + nN) ≠ I
  for n ≠ 0) — contradiction.
- dim H° = 1: H° is connected, 1-dimensional, and contains the closed
  connected 1-dimensional U_N, so H° = U_N. Every n ∈ H normalizes H°;
  every nontrivial element of U_N fixes exactly one point ξ = [w] of P¹,
  and n·ξ is the fixed point of n(I + N)n⁻¹ ∈ U_N∖{I}, so n·ξ = ξ: H
  fixes ξ — contradicting Step 2.
- dim H° = 2: 𝔥 = Lie(H°) is a 2-dimensional Lie subalgebra of sl₂; its
  derived algebra is at most 1-dimensional (spanned by the bracket of any
  basis pair), so 𝔥 is solvable. By Lie's theorem [CITED] 𝔥 has a common
  eigenline ℓ ⊂ ℂ², so 𝔥 ⊆ 𝔟_ℓ (the 2-dimensional Borel subalgebra
  stabilizing ℓ), hence 𝔥 = 𝔟_ℓ; by the bijection between connected
  algebraic subgroups and their Lie algebras in characteristic 0 [CITED:
  Chevalley], H° = B_ℓ, the Borel subgroup. H normalizes B_ℓ, and B_ℓ
  fixes exactly one point of P¹ (its unipotent radical already fixes
  only [ℓ]), so H fixes [ℓ] — contradicting Step 2.
So H = SL(2,ℂ). ∎

**Proposition 4 (the invariant-theory step, exactly).** Let Γ be
Zariski-dense in SL(2,ℂ) and W a rational finite-dimensional
representation. Then V^Γ = V^{SL(2,ℂ)}. For V = Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰,
V^{SL(2,ℂ)} = Sym⁰ — dimension 1.

*Proof.* For v ∈ V^Γ, Stab(v) = {g : W(g)v = v} is Zariski-closed (the
entries of W(g) are polynomials in the entries of g, for W a sum of
symmetric powers) and contains Γ, hence contains the closure SL(2,ℂ):
V^Γ = V^{SL(2,ℂ)}. Now v ∈ V^{SL(2,ℂ)} satisfies exp(t·e_pr)v = v for
all t ∈ ℂ; the coefficient of t¹ of this polynomial identity gives
e_pr·v = 0, and likewise f_pr·v = 0. On V(k), k > 0: ker(e) is the
highest-weight line ℂwᵏ (Lemma 2's triangular computation at the Lie
level, or directly: e kills only the top monomial), and f·wᵏ = k·w^{k−1}w′
≠ 0 — so ker(e) ∩ ker(f) = 0 on every positive block. Hence
V^{SL(2,ℂ)} = V(0) = Sym⁰. Conversely Sym⁰ is fixed. ∎

Theorem 2′ = Proposition 3 + Proposition 4: hypotheses (i), (ii) are
verified exactly on both banked members (F2/F3, S2/S3), and hold for
every member by (H2)+(H3) exactly as in §3. The direct-computation
anchor dim(ker e_pr ∩ ker f_pr) = 1 is also verified (F12, S10).

---

## 5. Metallic uniformity assembled

For every m ≥ 1:
1. RᵐLᵐ has trace m² + 2 > 2 (Anosov) ⇒ (H1)–(H3) [CITED, §0].
2. π₁(M_m) ⊇ F₂ (fiber) ⇒ irreducibility of hol (§3) ⇒ the two-parabolic
   hypothesis of Theorem 2 and the (i)+(ii) of Proposition 3.
3. P = ⟨μ, λ⟩ commuting, hol(μ), hol(λ) noncentral parabolic ⇒ Theorem 1.
4. The module data (blocks 17/9/1, even weights) is member-independent
   verified rational data.

⇒ **i₁ = 1 and i₂ = 3 for every metallic member.** ∎

Nothing metallic-specific is used beyond membership in the class of
1-cusped complete finite-volume hyperbolic 3-manifolds with F₂ ≤ π₁ (the
latter is automatic for these bundles); the theorem holds for that whole
class, and metallic uniformity is the instance the campaign needs.

---

## 6. What is computed vs what is cited

**Computed exactly in this cell (both banked members):** the SL(2)
relator values; irreducibility traces tr[X,Y] ≠ 2; noncentral
parabolicity of every peripheral generator used; the second independent
parabolic direction; matrix-level peripheral commutation; the fig-8
group-level commutation certificate (replayed); sl₂ brackets; evenness
of all 27 weights; Casimir centrality and eigen-dims (17, 9, 1);
dim ker(e_pr) = 3; the 27-letters = lifts of the SL(2)-letters; word
products = lifts of word matrices; relators = I₂₇; i₁ = 1 with the
invariant line exactly the Sym⁰ block; dim(ker e ∩ ker f) = 1;
i₂ = 3; per-block joint peripheral dims (1, 1, 1).

**Cited standard inputs (each used where flagged):**
- Thurston hyperbolization for Anosov-monodromy punctured-torus bundles
  + completeness ⇒ (H1)–(H3) — used ONLY for the all-m statement; every
  banked-member consequence is independently re-verified.
- Weyl complete reducibility + classification of irreducible
  sl₂(ℂ)-modules — used only to *name* the Casimir blocks V(16), V(8),
  V(0); the dimensions the theorems consume are the exactly verified
  kernel dimensions.
- Route 4 only (avoidable via §3): Lie's theorem; Chevalley's
  correspondence between connected algebraic subgroups and Lie
  subalgebras (char 0); finiteness/irreducibility of algebraic-group
  components.
- A₅ is not solvable (for F₂ non-solvability).

No SM values anywhere. Every decisive step is exact arithmetic over
K = ℚ(√−3) (fig-8) resp. L = ℚ(s, i), s⁴ = 8s² + 16 (silver).

---

## 7. Files

- `verify_l101.py` — the exact verification script (both members).
- `cellA_output.txt` — the full run output, verbatim.

## 8. Verification manifest (run of 2026-07-17; 30/30 PASS, 178.2 s)

**fig-8 (golden m = 1), K = ℚ(√−3), ω = (1+√−3)/2:**

| id | fact verified exactly | decisive value |
|----|----|----|
| F1 | SL(2) relator abABaBAbaB | = +I |
| F2 | tr[ρ(a), ρ(b)] ≠ 2 | = 3/2 + (1/2)√−3 |
| F3 | ρ(a) noncentral parabolic | tr = 2, ≠ I |
| F3b | ρ(b) noncentral parabolic, independent direction | w_a = e₁, w_b = e₂-line, det = −ω ≠ 0 |
| F4 | ρ(LONG) shares e₁, ±unipotent, noncentral | = [[−1, 2√−3], [0, −1]] (trace −2) |
| F5 | ρ(a)ρ(LONG) = ρ(LONG)ρ(a) | exact |
| F6 | [LONG, a] = 1 in π₁ (van Kampen certificate, replayed) | word length 20, area 2 |
| F7 | sl₂ brackets; h diagonal, all weights even | weights in [−16, 16] |
| F8 | Casimir central; eigen-dims | (17, 9, 1) at (144, 40, 0) |
| F9 | dim ker(e_pr) | = 3 |
| F10 | 27-letters = lifts; prod₂₇(LONG) = lift(ρ₂(LONG)); relator₂₇ = I | exact |
| F11 | **i₁** | **= 1** |
| F12 | i₁-line = Sym⁰ (e·v = f·v = 0); dim(ker e ∩ ker f) = 1 | exact |
| F13 | **i₂** | **= 3** |
| F14 | 27-level peripheral commutation | exact |
| F15 | per-block joint peripheral dims (Sym¹⁶, Sym⁸, Sym⁰) | (1, 1, 1) |

**silver (m = 2, monodromy RRLL), L = ℚ(s, i), s⁴ = 8s² + 16:**

| id | fact verified exactly | decisive value |
|----|----|----|
| S1 | SL(2) relators aBAbcc, aaCbcB | both = +I |
| S2 | tr[ρ(a), ρ(b)] ≠ 2 | = −2i |
| S3 | MU2 = ρ(CCB), LAM2 = ρ(caCA) noncentral parabolic | tr MU2 = +2, tr LAM2 = −2 |
| S4 | MU2·LAM2 = LAM2·MU2 | exact |
| S5 | common fixed vector w, exact | w = (−s + s³/8 + (s/2)i, 2i); (MU2−1)w = 0 = (LAM2+1)w |
| S5b | second noncentral parabolic ρ(a)MU2ρ(a)⁻¹, independent direction | det(w, a·w) = 2 − s²/2 ≠ 0 |
| S6 | sl₂ brackets; even weights; Casimir central; eigen-dims | (17, 9, 1) |
| S7 | dim ker(E_PR) | = 3 |
| S8 | 27-letters = lifts (all 6); Mmu₂₇ = lift(MU2), Mlam₂₇ = lift(LAM2); relators₂₇ = I | exact |
| S9 | **i₁** | **= 1** |
| S10 | i₁-line = Sym⁰; dim(ker e ∩ ker f) = 1 | exact |
| S11 | **i₂** | **= 3** |
| S12 | 27-level peripheral commutation | exact |
| S13 | per-block joint peripheral dims (Sym¹⁶, Sym⁸, Sym⁰) | (1, 1, 1) |

(The silver group-level peripheral commutation certificate is the banked
B649 stage-3b-ii run: peripheral commutator |word| = 14, AREA = 4.)

Consistency anchor with the banked Fox dimensions: (i₁, i₂) = (1, 3)
matches the banked silver solo (h⁰, h¹) = (1, 3) (B649 stage 3a) through
the campaign reduction, as preregistered.
