# The parabolic locus of the metallic family: Cohn's stage, principal breathers, and the commutators of quantized cat maps

**Draft v3 — 2026-07-08. v2 + literature-gate round 1 (`LIT_GATE.md`): the quantum-half
principles now CITED (Kurlberg–Rudnick, Mezzadri, Beyl/Nobs–Wolfart, Howe/Thomas) with
our contributions scoped; TWO gate-gifted upgrades incorporated — the Howe magnitude law
(verified 25/25) and the Serre ℚ-class mechanism for the master factorization. Hunts
(a)–(d) of the gate still in progress; §5's classical-half items remain gate-incomplete.
Narrative beats ⟡ are the owner's.**

---

## Abstract

For integers m ≥ 1 let A_m = R^m L^m = [[m²+1, m],[m, 1]] ∈ SL(2,ℤ) — the *metallic
matrices*, a family of once-punctured-torus bundle monodromies each admitting an
orientation-reversing square root; A₁ is the monodromy of the figure-eight knot
complement, and A₁ is Cohn's matrix g₁. We observe that for ANY pair of symmetric
matrices in SL(2,ℝ) the commutator trace is 2 − (M₁₂ − M₂₁)² with M = AB, and for the
metallic family M₁₂ − M₂₁ = mn(n−m): hence tr[A_m, A_n] = 2 − (mn(n−m))², and exactly
one pair — (1,2), golden and silver — has parabolic commutator. That pair generates the
commutator subgroup of PSL(2,ℤ): the family's parabolic locus is precisely Cohn's
modular torus, the classical stage of Markov's theory. The Fibonacci substitution
applied to the pair walks the Markov spine with the cusp intact at every stage. We
characterize the matrices of SL(2,ℤ) admitting integer square roots of determinant −1
(trace defect a perfect square, plus a divisibility), show that the breathable *traces*
are exactly the metallic traces m² + 2 with A_m the *principal* breather at its trace —
the family exhausts the locus precisely when the narrow class number h⁺(m²+4) is 1 —
and prove a two-level hierarchy of word and manifold symmetries with exact witnesses.
Finally, for the unique parabolic pair we study the commutators of the associated
quantized cat maps (Weil operators) at level 15 = tr(A₁A₂): the commutator trace is a
product of two characters — a quaternionic parity (the pair's mod-3 image is Q₈) and a
mod-5 closure bit (the mod-5 image is SL(2,5)) — the closure set is characterized by
congruence ([W₁ʲ, W₂ˡ] = I iff [A₁ʲ, A₂ˡ] ≡ I mod 15, with (2,3) the minimal address
with both exponents nontrivial), and both the commutator traces and the vanishing tiers
of the pair's interaction form factor through the divisor lattice of the two operator
orders — a pair of functions on 36 cells, printed in full.

---

## 1. Introduction

⟡ *[The owner's opening. The mathematical beats it must carry:]*

In 1955 Harvey Cohn identified the geometric home of Markov's 1879–80 theory of
badly-approximable numbers: the commutator subgroup of the modular group — the
fundamental group of a once-punctured torus, which we will call, as terminology, *the
stage* — with the Markov numbers appearing as one third of the traces of its simple
elements. Seventy years of literature stand on that identification (Aigner 2013;
Reutenauer 2018; Cusick–Flahive 1989).

Cohn's generator g₁ = [[2,1],[1,1]] is the first member of a natural family: the
metallic matrices A_m = R^m L^m, the monodromies of the once-punctured-torus bundles
attached to the metallic means λ_m = (m + √(m²+4))/2. This paper asks the family
question the classical literature does not: *for which pairs (m,n) does the two-generator
group ⟨A_m, A_n⟩ form a stage?* Here the relevant condition on a generating pair is the
cusp condition for a discrete, faithful, type-preserving representation of the
once-punctured-torus group: the commutator must be parabolic with tr[A,B] = −2 (trace
+2 forces reducibility; parabolicity alone means trace ±2).

The answer (§2) has an unreasonably simple mechanism. The metallic matrices are
symmetric, and for ANY symmetric pair in SL(2,ℝ) the commutator trace is
2 − (M₁₂ − M₂₁)², M = AB — a two-line consequence of BA = (AB)ᵀ. The family's entire
contribution is the integer mn(n−m): the deviation from parabolicity is the square of
that integer, so the failures are quantized ⟡, and mn(n−m) = 2 has exactly one solution
in positive integers m < n. The unique pair is (1,2), and Theorem B identifies its group
with Cohn's — generator for generator. The substitution a → ab, iterated on the pair
itself, walks the Markov spine with every renormalized pair again parabolic (Theorem C):
an infinite tower of stages.

Section 3 studies the family's defining symmetry — the orientation-reversing square
root, which we call, as terminology, the *breath* ⟡ — and proves the square-root
criterion for SL(2,ℤ) (Theorem D). Here the panel of this paper's own referee process
forced a sharpening we are glad to report: the family does NOT exhaust the breathable
locus. Odd powers of metallic matrices are breathable composites, and — more
interestingly — when the ring ℤ[λ_m] has nontrivial narrow class group there exist
*non-principal breathers* at the same trace, not conjugate to A_m (Theorem D′): the
breathable traces are exactly the metallic traces, the metallic matrix is the principal
breather, and the family equals the locus precisely when h⁺(m²+4) = 1. The class group
of the scale enters the geometry of the family. Theorem E then organizes the word-level
and manifold-level symmetries of words in {R, L} into two hierarchies with exact
witnesses, including an amphichiral pair with homology torsion (ℤ/12)² whose words fail
the word-level mirror criterion — the two levels genuinely differ.

Section 4 turns to the unique pair's quantization — with its provenance stated plainly:
the operators W_m are the Weil / Hannay–Berry quantized cat maps of A_m at level
N = 15 = tr(A₁A₂) (Hannay–Berry 1980; Degli Esposti; Kurlberg–Rudnick; the level is a
chosen case study — it is the pair's own product trace, but no selection principle is
claimed, and open problem 4 records what fails at other pairs). By Theorem F everything
in §4 reduces to finite group theory of the pair's residue images — the content is
WHICH finite structure the unique parabolic pair selects: the mod-3 image is the
quaternion group Q₈, the mod-5 image is SL(2,5); the commutator of the quantized maps
is governed by two characters (Theorem F); its closure set is exactly the mod-15
commutation locus, with (2,3) the minimal nontrivial address; and both the commutator
trace and the interaction form's vanishing tiers factor through the divisor lattice of
the operator orders — the master table of 36 cells, printed in §4.3 (Theorem G).

**Reading guide and honesty protocol.** Classical material is cited and never
re-claimed. §5 lists what we could not locate — with the quantum-half items explicitly
SUSPENDED until the search extends over the quantized-cat-map corpus. Every numerical
claim carries an exact certificate with a public reproducer (Appendix A); several
results were reached through refutations of their own first forms — including by this
paper's internal referee panel — and Appendix B records that path, because the method
is part of the result. ⟡

---

## 2. The parabolic locus of the family

### 2.1 Metallic matrices, halves, and the norm

R = [[1,1],[0,1]], L = [[1,0],[1,1]]; A_m := R^m L^m = [[m²+1, m],[m,1]], tr A_m = m²+2.
The *half-matrix* X_m = [[m,1],[1,0]] satisfies X_m² = A_m and det X_m = −1; it is the
companion matrix of x² − mx − 1, so det X_m = N(λ_m) = −1: the orientation character of
the half and the field norm of the scale coincide, for every m, and persist through the
same-field degeneracies (m = 1, 4, 11, 29, … are φ, φ³, φ⁵, φ⁷ — odd powers, norm −1
throughout). No imaginary quadratic field carries a unit of norm −1. (One-line proofs;
`br_n_norm.py`.) Geometrically, M(A_m) is a hyperbolic once-punctured-torus bundle and
X_m generates a non-orientable bundle double-covered by it — for m = 1, the Gieseking
manifold (census-verified: vol(m004)/vol(m000) = 2 exactly).

### 2.2 Theorem A: the symmetric-pair identity and the unique parabolic pair

**Lemma 2.2 (the transpose mechanism).** Let A, B ∈ SL(2,ℝ) be symmetric and M = AB.
Then BA = (AB)ᵀ, hence [A,B] = M·(Mᵀ)⁻¹ and

  tr[A,B] = tr(M (Mᵀ)⁻¹) = 2 − (M₁₂ − M₂₁)².

*Proof.* For M = [[p,q],[r,s]] with det M = 1, (Mᵀ)⁻¹ = [[s,−r],[−q,p]], so
tr(M(Mᵀ)⁻¹) = ps − qr − qr + ps − (q² + r²) + 2qr = 2 − (q − r)² after using ps − qr = 1.
∎

**Theorem A.** tr[A_m, A_n] = 2 − (mn(n−m))², and the commutator is parabolic with
trace −2 iff mn(n−m) = 2, whose unique solution in positive integers m < n is (1,2).

*Proof.* A_m, A_n are symmetric; M = A_mA_n has M₁₂ − M₂₁ = mn(m−n) by direct
computation (M₁₂ = (m²+1)n + m, M₂₁ = mn² + m... displayed in full in the text). Apply
Lemma 2.2. For the uniqueness, mn(n−m) = 2 with 0 < m < n forces mn ≤ 2, so m = 1,
n = 2. ∎

Remarks. (i) The square is not a family miracle: EVERY symmetric pair tears by a
perfect square — the mechanism is the transpose involution, which on the character
variety of the once-punctured torus is induced by the elliptic involution. What is the
family's own is the integer mn(n−m) and everything §2.3–2.4 builds on the unique pair.
(ii) The failure is quantized and shared: pairs with equal mn(n−m) tear equally —
(1,3) and (2,3) both give −34. ⟡ (iii) At (1,2), the trace triple (3, 6, 15) satisfies
Markov's equation x²+y²+z² = xyz — the triple 3·(1,2,5) — and the *product trace*
tr(A₁A₂) = 15 returns as the level of §4. We refer to 15 as the pair's *seam trace*
(terminology, used only in that sense below).

### 2.3 Theorem B: the parabolic locus is Cohn's stage

With g₁ = [[2,1],[1,1]], g₂ = [[1,1],[1,2]] (Cohn 1955): A₁ = g₁; A₁A₂⁻¹A₁ = g₂;
A₂ = g₁g₂⁻¹g₁. Hence ⟨A₁,A₂⟩ = ⟨g₁,g₂⟩, which by Cohn's theorem is the commutator
subgroup of PSL(2,ℤ) — free of rank two, the fundamental group of the modular
once-punctured torus, on which the Markov correspondence lives (traces of simple closed
geodesics = 3 × Markov numbers; cited, not re-derived). Moreover every balanced word in
R, L lies in this subgroup (L = ST⁻¹S⁻¹ in PSL(2,ℤ), so the abelianization ℤ/6 reads
t^{#R−#L}). ∎ ⟡

### 2.4 Theorem C: the chain walks the spine

s₀ = A₂, s₁ = A₁, s_{k+1} = s_k s_{k−1}. (i) The traces obey u_{k+1} = u_k u_{k−1} −
u_{k−2} and every consecutive triple satisfies Markov's equation (the Vieta move
(x,y,z) ↦ (y,z,yz−x) preserves x²+y²+z²−xyz; the seed (6,3,15) lies on it).
(ii) u_k/3 walks the spine 1, 2, 5, 13, 194, 7561, …
(iii) Every renormalized pair (s_k, s_{k+1}) has tr[s_k, s_{k+1}] = −2.

*Proof of (iii).* Each step is a Nielsen transformation of the generating pair of
⟨A₁,A₂⟩, free of rank two by Theorem B. The conjugacy class of the commutator of a
generating pair of a rank-two free group is invariant under Nielsen transformations up
to inversion (the well-definedness of the boundary of the once-punctured torus). In
SL(2), tr(M⁻¹) = tr((tr M)I − M) = tr M, and trace is a class function; hence
tr([s_k, s_{k+1}]) = tr([A₁,A₂]^{±1}) = −2. ∎

The cusp survives every application of a → ab: the substitution acts on stages and
never tears one. ⟡

---

## 3. Breathability: the criterion, the principal breather, and the two hierarchies

### 3.1 Theorem D: the square-root criterion

**Theorem D.** B ∈ SL(2,ℤ) with tr B > 2 admits X ∈ GL(2,ℤ) with det X = −1, X² = B,
iff t := √(tr B − 2) ∈ ℤ_{>0} and t divides B − I entrywise; then X = (B − I)/t, unique
up to sign.

*Proof.* (⟹) det X = −1 and Cayley–Hamilton give X² = (tr X)X + I, so B = tX + I,
t = tr X, tr B = t² + 2, and X = (B − I)/t. (⟸) Set X = (B − I)/t. Then
det(B − I) = 1 − tr B + det B = −t², so det X = −t²/t² = −1; and by B's own
Cayley–Hamilton, B² = (t²+2)B − I, whence X² = (B² − 2B + I)/t² = t²B/t² = B.
Uniqueness: any root Y satisfies Y = (B − I)/tr Y with (tr Y)² = t². ∎

Every metallic matrix is breathable, with X_m = (A_m − I)/m.

### 3.2 Theorem D′: traces, principal breathers, and the class group

**Theorem D′.** (i) The breathable traces are exactly the metallic traces:
{tr B : B breathable} = {t² + 2 : t ≥ 1}. (ii) The family does not exhaust the
breathable locus: A₁³ is breathable ((A₁³ − I)/4 = X₁³), as is every odd power of a
metallic matrix; and at the metallic trace itself there exist breathers not conjugate
to A_m whenever the narrow class number h⁺(m²+4) exceeds 1 — for m = 6 (ℤ[√10],
h⁺ = 2), B′ = [[19,30],[12,19]] of trace 38 passes the criterion with root
X′ = [[3,5],[2,3]], and B′ is not GL(2,ℤ)-conjugate to A₆ (the associated binary forms
lie in different genera; a conjugator search is exhausted as a check). (iii) Under the
Latimer–MacDuffee correspondence, the GL(2,ℤ)-classes of roots of trace t = m biject
with the ideal classes of ℤ[λ_m]; A_m is the breather of the principal class. **The
family equals the breathable locus at its traces iff h⁺(m²+4) = 1.**

*Proof sketch and certificates.* (i): both inclusions are Theorem D plus X_m. (ii): the
displayed matrices verify in one line each (reproducers cited); non-conjugacy by the
genus of the forms (the character (·|5) separates (1,−9,−1)-type from the non-principal
form) — details in the text. (iii) is Latimer–MacDuffee applied to x² − mx − 1. ∎

⟡ *[The panel of our own referees forced this theorem: the first draft claimed
"family = locus" and was wrong; the correction is more mathematics, not less — the
class group of the scale is part of the breath's story.]*

For the chain of §2.4: no composite chain word is breathable for 2 ≤ k ≤ 200 (mod-p
quadratic-non-residue certificates; the traces exceed astronomical size long before
k = 200, so modular certificates are the honest method). Beyond rung 200, and for
composite metallic words in general, we state it as a conjecture — noting A₁A₃ (trace
27, defect 25 = 5²) passes the square test and fails only the divisibility, so the
conjecture genuinely requires Theorem D's second condition.

### 3.3 Theorem E: the two hierarchies, with exact witnesses

For words w in {R, L}: rev·swap(w) := the reversal with R ↔ L; *word-mirror* :=
rev·swap(w) is a cyclic rotation of w; *balanced* := #R = #L. For bundles:
*amphichiral* := M(w) admits an orientation-reversing self-isometry; *rooted* := the
monodromy satisfies Theorem D's criterion.

**Lemma 3.3 (the bridge).** rev·swap(w) is the word of the transposed monodromy read
backwards; a cyclic rotation changes the monodromy by conjugation. Hence if w is
word-mirror, M(w) admits an orientation-reversing self-homeomorphism: word-mirror ⟹
amphichiral. (Standard-shaped; stated with proof in the text, cited where available.)

**Theorem E (word level).** word-mirror ⟹ balanced (rev·swap exchanges the letter
counts; rotations preserve them). Strict: RRRLLRLL is balanced, not word-mirror — and
its bundle is genuinely chiral (CS = −0.0012159…, its rev·swap partner +0.0012159…: a
chiral mirror pair of balanced words).

**Theorem E″ (manifold level).** rooted ⟹ amphichiral (the deck involution of the
orientation double cover reverses orientation). Strict, and the two levels differ:
the two cyclic classes LLLRLLRRRLRR, LLLRRLRRRLLL′ (trace 146, t = 12) are rooted —
hence amphichiral (and verified: CS = 0, an isometric pair) — but NOT word-mirror; their
homology torsion is (ℤ/12)², the root's square trace surfacing as square homology.
Amphichiral-without-root: the chain word aba (M(RLRRLLRL), vol 7.6417106…, torsion 37,
CS = 0).

**Proposition E‴ (frozen residue).** Define the residue of a word as
det(Par·W(w)) at level 15 (§4.0 for Par, W). Then residue(w) = −ω^{#L−#R} with
ω = e^{2πi/3}: balanced words have residue −1 ("frozen"), and the Fibonacci letter
tower (a → R, b → L), whose imbalance at rung k is ±F_{k−2}, has residue cycling with
the Fibonacci sequence mod 3 — period 8, the Pisano period π(3). (Verified exactly;
the proof is the determinant computation det W_R = ω̄, det W_L = ω, det Par = −1.)

**Scope notes (exact).** Two-block products of metallic letters are word-mirror
(rev·swap(uv) = vu, a rotation of uv); the chain words s_k are word-mirror for all
k ≤ 8 (verified; the general case reduces to the standard-word near-palindrome lemma,
left open); the general product of ≥ 3 metallic letters need NOT be word-mirror
(A₁A₂A₃ fails — first found by this paper's referee panel). Consequently: the chain's
bundles are amphichiral through rung 8 by Lemma 3.3 + verification (CS = 0 exactly at
every computed rung), conjecturally for all rungs; the letter tower is chiral at rungs
3–8 (CS ≠ 0, verified) and conjecturally beyond — its imbalance defeats only the word
criterion, so chirality beyond rung 8 is open.

---

## 4. The commutators of the quantized pair

### 4.0 The operators, defined (and their provenance)

Let N = 15, ζ = e^{2πi/N}. On ℂ[ℤ/15]: the twist D = diag(ζ^{j(j−1)/2}); the unitary
DFT F; W_R := (F D F*)*, W_L := D; for a word w in {R, L}, W(w) is the corresponding
product, and W_m := W(R^m L^m) — **the Weil / Hannay–Berry quantized cat map of A_m at
level 15** (Hannay–Berry 1980; the metaplectic/Weil representation of SL(2, ℤ/N) at odd
N: Kloosterman 1946, Nobs–Wolfart 1976, Gérardin; the arithmetic of quantized cat maps:
Degli Esposti, Kurlberg–Rudnick Duke 2000). Par is the parity operator
(Par ψ)(x) = ψ(−x) — the Weil image of −I. **Proposition 4.0**: under the level-15 Weil
representation R ↦ W_R and L ↦ W_L up to projective scalars; at odd level the projective
representation linearizes (the Schur multiplier of SL(2, ℤ/m) is trivial for m ≢ 0 mod 4
— Schur, Beyl Math. Z. 191 (1986); a concrete genuine choice of phases is
Kurlberg–Rudnick Thm 5), and commutators [W(u), W(v)] are independent of all phase
choices (Mezzadri, Nonlinearity 15 (2002), §3) — the commutator table below is therefore
convention-free by citation as well as by our three-lift verification. ord(W₁) = 20, ord(W₂) = 12 (computed exactly; these orders define the
torus below). The *interaction form* of the pair is (a,b) ↦ tr(Par·P_a·Q_b), where
P_a (a ∈ ℤ/20) and Q_b (b ∈ ℤ/12) are the spectral projectors of W₁ and W₂; its values
lie in ℚ(√5, √−3), and the four *Galois channels* of a value are its coordinates in
the basis {1, √5, √−3, √−15} (the four isotypic pieces under Gal(ℚ(√5,√−3)/ℚ) — the
Klein four-group). The *tier* of a point (a,b) is the vanishing pattern of its four
channels; exactly five patterns occur — none, {√−3,√−15}, {√5,√−15}, {√5,√−3,√−15},
all — realizing the subfield lattice, with counts 120/20/20/10/70. A point with all
four channels zero is *dark*; with none, *fully active*. (These five sentences are the
complete dictionary for Theorem G.)

The level is the pair's seam trace, chosen as a case study; no selection functor is
claimed (open problem 4 records that the analogous choice at (1,3) behaves differently).

### 4.1 The commutator table

tr[W₁ʲ, W₂ˡ], 1 ≤ j, l ≤ 5 (exact in ℚ(ζ₆₀); verified in three independent lifts —
the commutators are lift-independent by Proposition 4.0):

|      | l=1 | l=2 | l=3 | l=4 | l=5 |
|------|-----|-----|-----|-----|-----|
| j=1  | −1  | 3   | −5  | 3   | −1  |
| j=2  | 3   | 3   | 15  | 3   | 3   |
| j=3  | −1  | 3   | −5  | 3   | −1  |
| j=4  | 3   | 3   | 15  | 3   | 3   |
| j=5  | −5  | 15  | −5  | 15  | −5  |

κ_q := tr[W₁,W₂] = −1, while tr[A₁,A₂] = −2: the quantization of the parabolic pair is
not parabolic at the generators.

**The magnitude law (Howe's formula, verified 25/25):** |κ_q(j,l)|² =
#Fix([A₁ʲ, A₂ˡ] acting on (ℤ/15)²) — the table's magnitudes are the square roots of the
classical commutators' fixed-point counts (Howe; exact character values with signs:
Thomas, J. London Math. Soc. 77 (2008)). The divisors of 15 appearing in the table are
Howe's formula evaluated at level 15.

### 4.2 Theorem F: closure, and the residue groups

**Theorem F.** (i) The mod-3 image of (A₁, A₂) is Q₈ (a² = b² = [a,b] = −I); the mod-5
image is SL(2,5), order 120. (ii) [W₁ʲ, W₂ˡ] = I ⟺ [A₁ʲ, A₂ˡ] ≡ I (mod 15). The ⟸
direction follows from Proposition 4.0 (genuine representation; the commutator depends
only on the mod-15 residue); the ⟹ direction is verified exactly on all 240 points of
the order torus (equivalently: the Weil representation sends no non-identity commutator
arising here to a scalar — checked, not claimed abstractly). (iii) In particular
[W₁², W₂³] = I exactly: A₁² is central mod 3 and A₂³ is central mod 5, so the
commutator dies at the CRT-central address — and (2,3) is the minimal address with both
exponents nontrivial (visible in the table: no entry 15 occurs with j ≤ 1 or (j,l)
lexicographically below (2,3)). The full closure set is the mod-15 commutation locus.

Two exact curiosities, recorded without weight: tr(Par·W₁W₂) = ζ₆₀⁸ and
tr(Par·W₂W₁) = ζ₆₀⁴ — the two orderings differ by ζ₁₅, the level's own phase; and
|Q₈/±| · |PSL(2,5)| = 4 · 60 = 240, the number of points of the order torus.

### 4.3 Theorem G: the master theorem — the divisor lattice

**Theorem G.** (i) κ_q(j,l) := tr[W₁ʲ, W₂ˡ] = ε(jl) · χ₅(j,l), where ε = 3 for jl even
and −1 for jl odd (exactly: [A₁ʲ, A₂ˡ] ≡ (−I)^{jl} mod 3, since Q₈ is class-2 nilpotent
with central commutator), and χ₅ = 5 or 1 according as [A₁ʲ, A₂ˡ] ≡ I (mod 5) or not.
(ii) Both maps on the order torus ℤ/20 × ℤ/12 — the commutator trace κ_q and the tier
of the interaction form — factor through the divisor pair (gcd(x,20), gcd(y,12)):
each is single-valued on the 36 divisor cells. The master table:

| gx\gy | 1 | 2 | 3 | 4 | 6 | 12 |
|---|---|---|---|---|---|---|
| **1** | −1 free | 3 free | −5 qs | 3 free | 15 dark | 15 dark |
| **2** | 3 free | 3 free | 15 dark | 3 dark | 15 qrs | 15 dark |
| **4** | 3 free | 3 dark | 15 dark | 3 free | 15 dark | 15 qrs |
| **5** | −5 free | 15 rs | −5 qs | 15 rs | 15 dark | 15 dark |
| **10** | 15 rs | 15 rs | 15 dark | 15 dark | 15 qrs | 15 dark |
| **20** | 15 rs | 15 dark | 15 dark | 15 rs | 15 dark | 15 qrs |

(each cell: κ_q value, tier; cell sizes are φ(20/gx)·φ(12/gy)). **The mechanism is
classical**: factorization-through-gcd is Cohen's class of "even functions (mod r)"
(PNAS 41 (1955): f(n) = f(gcd(n,r)), the span of Ramanujan sums), and for
rational-valued class functions of powers of finite-order operators it follows from the
ℚ-class principle (Serre, Linear Representations, §12.4/§13.1: rational class functions
are constant on elements generating the same cyclic subgroup). κ_q is rational-valued
and, by the magnitude law, determined by the fixed-point count and sign data of the
classical commutator — both computed exactly per divisor cell; the tier map's
factorization is verified exactly on all 240 points, with the per-channel
Galois-isotypic argument (the same mechanism applied channel-wise) recorded as the
remaining written step. Consequences read off the table: a fully
active cell never sits at quantum closure (no "free" in the κ_q = 15 cells — full
activity requires non-commutation); the partial tiers are commutator-pure (rs and qrs
only at closure; qs only at κ_q = −5); darkness concentrates at closure (54 of the 70
dark points). Conceptually: a point's divisor cell fixes both the CRT-centrality data
governing κ_q and the cyclotomic support governing which quadratic channels can vanish;
the remaining step — deriving each cell's tier from its cyclotomic support — is stated
as the opening problem of the companion paper on the interaction form. ∎ (for (i) and
the displayed verification of (ii))

### 4.4 A scoped remark

κ = tr[A,B] stratifies the family's pairs, with (1,2) alone parabolic. The richness of
the interaction structure at other pairs tracks the prime factorization of the pair's
product trace, not κ itself (the (1,3) pair at level 27 = 3³ collapses to two values;
(2,3) at level 63 = 9·7 is rich again despite equal κ = −34): the architecture of §4.3
is level arithmetic. Any finer role of κ is open work, outside this paper.

---

## 5. What is classical, and what we could not locate

**Classical, cited.** The transpose/elliptic involution on the punctured-torus character
variety; Fricke trace identities; Cohn's theorem and the Markov correspondence; the
tree and spine; Latimer–MacDuffee; the Weil representation at odd level and its CRT
factorization; quantized cat maps (Hannay–Berry; Degli Esposti; Kurlberg–Rudnick);
Gieseking's manifold; Q₈ and SL(2,5).

**We could not locate** (searched against the three Markov monographs and standard
databases; references welcome): (a) the metallic parametrization tr[A_m,A_n] =
2 − (mn(n−m))² as a statement about this family, with the symmetric-pair mechanism —
NOTE: since the mechanism is generic for symmetric pairs, the identity may well appear
in the symmetric/palindromic corner of Markov theory, and our gate there is not yet
line-by-line complete; (b) the uniqueness of (1,2) as the family's parabolic pair;
(c) Theorem D with the divisibility condition and Theorem D′'s principal-breather /
class-number statement; (d) the two-level hierarchy with the (ℤ/12)² witnesses.
**The quantized-cat-map gate, run (LIT_GATE.md):** the commutation principle's ⟸
direction, the genuine representation at odd level, the CRT factorization, and the
character-magnitude machinery are all in print and cited above (Kurlberg–Rudnick;
Mezzadri; Schur/Beyl/Nobs–Wolfart; Howe/Thomas). What our search of that corpus did not
find: the ⟹ direction of Theorem F(ii); the explicit commutator table at any composite
level; the Q₈ × SL(2,5) commutator-image assembly at N = 15; the closure-address
statement; and the joint (κ_q, tier) divisor-lattice factorization. These are stated as
this paper's contributions in the scoped sense above.

## 6. Open problems

1. The family quantum column (κ_q at each pair's product trace; does closure track CRT
   centrality uniformly?). 2. The cyclotomic-support step of Theorem G. 3. The two tower
   constants: c = 0.934102018057787980264187790656… (tower volumes are Fibonacci-additive
   to < 10⁻²⁷ by rung 13; PSLQ excludes small relations against a golden-sector
   Lobachevsky basis at stated height bounds) and λ_chain = 1.57705744122666946… (PSLQ
   excludes integer relations of degree ≤ 8 at height ≤ 10⁴): both pinned, neither
   identified — height-bounded exclusions, not non-algebraicity certificates. 4. Why 15
   twice (the seam trace equals the conductor-type level of ℚ(√−15); the naive family
   law fails at (1,3)). 5. The standard-word lemma (chain words word-mirror for all k).
   6. The chain-breathability conjecture beyond rung 200. 7. The heredity of the chain's
   torsion primes.

## Appendix A: reproducibility
[Per-theorem script/lock map as in v1, updated: Lemma 2.2 symbolic check; Theorem D′
counterexample verifications; the master table generator; 17 + 4 locks at v2.]

## Appendix B: the corrections ledger ⟡
[As v1, extended by one chapter: this paper's own referee panel found the two-block gap
in the first amphichirality theorem, the class-group counterexamples to "family =
locus", the generic-symmetric-pair mechanism behind Theorem A, and the missing
Hannay–Berry shelf — each verified and incorporated. The panel is part of the method;
the method is part of the result.]

---
*MSC 11J06, 11E16, 57K10, 20H10, 81Q50. Repository URL at packaging.*
