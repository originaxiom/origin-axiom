# The parabolic locus of the metallic family: Cohn's stage, principal breathers, and the commutators of quantized cat maps

**Draft v7 — 2026-07-08. v6 completed for the owner's voice pass: the two appendices are
now written in full (reproducibility map + corrections ledger), the two towers (the chain
and the Fibonacci letter tower) are disambiguated and their constants defined as limits of
named sequences, Lemma 3.3's proof and provenance are separated, and the verified Alexander
family law (Δ_m = char poly of A_m) is folded into §2.1. Marks ⟡ remain the owner's to voice.
v6 baseline: panel round 2 COMPLETE (all five seats; see PANEL_v2_FINAL.md). No mathematical claim was broken; every computation reproduced. The
revision (a) reframes §4 as the *level-15 Weil shadow* of the pair and discloses the
mod-15 collision (A₁₆,A₁₇) ≡ (A₁,A₂) that makes §4 blind to parabolicity; (b) repairs the
Theorem F(ii) ⟹ argument (genuine-rep faithfulness on the order-4 center, not projective
injectivity alone); (c) corrects the two §4.2 "curiosities" (the image is Q₈ × SL(2,5) of
order 960; the ζ₆₀ phases are lift artifacts, only the ratio invariant); (d) demotes the
h⁺-equivalence to the class-number-one specialization of the Sarnak/Latimer–MacDuffee
count (N(λ_m)=−1 ⟹ h⁺=h, so the narrow refinement is inert); (e) retitles Theorem G from
"master theorem" to a worked N=15 instance of the Cohen/Serre factorization; (f) fixes the
§4.3 channel legend, the abstract sign, the genus forms, and the constants' precision. The
literature gate is COMPLETE (both rounds; `LIT_GATE.md`). What survives as ours: the
family question, the two-parameter failure integer and its uniqueness scan, the
principal-breather assembly, the hierarchy witnesses, and the explicit N=15 quantum tables
(the commutator table, the Q₈×SL(2,5) image assembly, the closure address). Narrative
beats ⟡ are the owner's.**

---

## Abstract

For integers m ≥ 1 let A_m = R^m L^m = [[m²+1, m],[m, 1]] ∈ SL(2,ℤ) — the *metallic
matrices*, a family of once-punctured-torus bundle monodromies each admitting an
orientation-reversing square root; A₁ is the monodromy of the figure-eight knot
complement, and A₁ is Cohn's matrix g₁. For ANY pair of symmetric
matrices in SL(2,ℝ) the commutator trace is 2 − (M₁₂ − M₂₁)² with M = AB — the
coordinate form of classical facts (Sarnak's reciprocal-geodesic mechanism; the axes-
through-i slice of Gehring–Martin's commutator calculus) — and for the metallic family
M₁₂ − M₂₁ = mn(m−n): hence tr[A_m, A_n] = 2 − (mn(n−m))², and exactly one pair — (1,2),
golden and silver — has parabolic commutator. That pair is Reutenauer's Markoff
morphism, generator for generator: the family's parabolic locus is precisely Cohn's
modular torus, the classical stage of Markov's theory. The Fibonacci substitution
applied to the pair walks the Markov spine with the cusp intact at every stage. Assembling
the classical square-root criterion (Northshield 2010) with the Latimer–MacDuffee
correspondence, we show that the breathable *traces*
are exactly the metallic traces m² + 2 with A_m the *principal* breather at its trace —
the family exhausts the locus at its traces exactly in the class-number-one case
h(m²+4) = 1 — the class-number-one specialization of the Latimer–MacDuffee/Sarnak count
(since N(λ_m) = −1 forces narrow = wide class number) — and prove a two-level hierarchy of
word and manifold symmetries with exact witnesses.
Finally, for the unique pair we study the commutators of the associated quantized cat
maps (Weil operators) at level 15 = tr(A₁A₂) — a construction that sees only the pair's
image mod 15, so it is a shadow of the arithmetic 15 = 3·5 rather than of parabolicity
(we exhibit a non-parabolic pair with the identical tables): the commutator trace is a
product of two characters — a quaternionic parity (the pair's mod-3 image is Q₈) and a
mod-5 closure bit (the mod-5 image is SL(2,5)) — the closure set is characterized by
congruence ([W₁ʲ, W₂ˡ] = I iff [A₁ʲ, A₂ˡ] ≡ I mod 15, with (2,3) the minimal address
with both exponents non-central mod 15), and both the commutator traces and the vanishing tiers
of the pair's interaction form factor through the divisor lattice of the two operator
orders — a pair of functions on 36 cells, printed in full.

---

## 1. Introduction

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

The answer (§2) has an elementary mechanism. The metallic matrices are
symmetric, and for ANY symmetric pair in SL(2,ℝ) the commutator trace is
2 − (M₁₂ − M₂₁)², M = AB — a two-line consequence of BA = (AB)ᵀ. The family's entire
contribution is the integer mn(n−m): the deviation from parabolicity is the square of
that integer, so the failures take perfect-square values, and mn(n−m) = 2 has exactly
one solution in positive integers m < n. The unique pair is (1,2), and Theorem B identifies its group
with Cohn's — generator for generator. The substitution a → ab, iterated on the pair
itself, walks the Fibonacci-word branch of the Markov spine — the traces/3 =
1, 2, 5, 13, 194, 7561, … (the branch generated by the Fibonacci word, distinct from the
conventional 1, 2, 5, 13, 34, … branch) — with every renormalized pair again parabolic
(Theorem C): an infinite tower of stages.

Section 3 studies the family's defining symmetry — the orientation-reversing square
root, which we call, as terminology, the *breath* — and re-proves, for completeness,
Northshield's square-root criterion for SL(2,ℤ) (Theorem D). Here the panel of this paper's own referee process
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

Section 4 turns to the pair's quantization — the *level-15 Weil shadow* — with its
provenance and its limits stated plainly: the operators W_m are the Weil / Hannay–Berry
quantized cat maps of A_m at level N = 15 = tr(A₁A₂) (Hannay–Berry 1980; Degli Esposti;
Kurlberg–Rudnick). The construction sees only the image mod 15: since A₁₆ ≡ A₁ and
A₁₇ ≡ A₂ (mod 15), the wildly non-parabolic pair (A₁₆, A₁₇) (tr[·] = −73982) yields every
table of §4 identically. So §4 is a study not of parabolicity but of the finite arithmetic
of 15 = 3·5 — which is the honest content. By Theorem F everything in §4 reduces to finite
group theory of the pair's residue images — the content is
WHICH finite structure the unique parabolic pair selects: the mod-3 image is the
quaternion group Q₈, the mod-5 image is SL(2,5); the commutator of the quantized maps
is governed by two characters (Theorem F); its closure set is exactly the mod-15
commutation locus, with (2,3) the minimal address whose both powers are non-central mod 15; and both the commutator
trace and the interaction form's vanishing tiers factor through the divisor lattice of
the operator orders — the master table of 36 cells, printed in §4.3 (Theorem G).

**Reading guide and honesty protocol.** Classical material is cited and never
re-claimed. §5 carries the per-claim verdicts of the two-round literature gate,
including its downgrades of this paper's own earlier claims. Every numerical
claim carries an exact certificate with a public reproducer (Appendix A); several
results were reached through refutations of their own first forms — including by this
paper's internal referee panel — and Appendix B records that path as a methodological
note.

---

## 2. The parabolic locus of the family

### 2.1 Metallic matrices, halves, and the norm

R = [[1,1],[0,1]], L = [[1,0],[1,1]]; A_m := R^m L^m = [[m²+1, m],[m,1]], tr A_m = m²+2.
The bundle M(A_m) is fibered, so its Alexander polynomial is the characteristic polynomial
of the monodromy: **Δ_m(a) = a² − (m²+2)a + 1** (verified m = 1…5 in SnapPy: a²−3a+1,
a²−6a+1, a²−11a+1, a²−18a+1, a²−27a+1) — the family's Alexander invariant is exactly its
metallic trace m²+2.
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

*Provenance.* The identity is the coordinate form of classical facts, in three
clothings. Symmetric elements of SL(2,ℝ) are exactly those inverted by conjugation with
S₀ = [[0,−1],[1,0]] (equivalently: hyperbolics whose axes pass through i — Sarnak,
Reciprocal geodesics, Clay Proc. 7 (2007)); hence [A,B] = M(Mᵀ)⁻¹ = −(MS₀)² and
tr[A,B] = 2 − tr(MS₀)² = 2 − (M₁₂ − M₂₁)². The same statement is the axes-through-i
slice of Gehring–Martin's commutator-parameter calculus (J. Anal. Math. 63 (1994):
tr[A,B] − 2 = −4 sinh²(ℓ_A/2) sinh²(ℓ_B/2) sin²θ; for the metallic family
sin²θ = 4(n−m)²/((m²+4)(n²+4)) and the product is (mn(n−m))² — verified). And it is a
direct substitution into Fricke's κ (Goldman, Handbook of Teichmüller theory II). We
found the coordinate form written out nowhere and use it as an elementary lemma — not a
new result.

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
(terminology, used only in that sense below). (iv) The unique pair is not new AS a
pair: (A₁, A₂) = (μ(x), μ(y)) for Reutenauer's Markoff morphism μ(x) = [[2,1],[1,1]],
μ(y) = [[5,2],[2,1]], whose parabolic commutator he computes via Fricke's identity
(Integers 9 (2009); From Christoffel Words to Markoff Numbers, OUP 2019, Thm 3.1.1).
New here is the FAMILY reading: the two-parameter formula and the uniqueness scan.
Uniqueness statements at the matrix level should be compared with Schmutz Schaller
(Russian Math. 66 (2022)) and with Nielsen's classical theorem (the commutator of any
basis of F₂ is conjugate to [a,b]^{±1}), which Theorem C uses.

### 2.3 Theorem B: the parabolic locus is Cohn's stage

With g₁ = [[2,1],[1,1]], g₂ = [[1,1],[1,2]] (Cohn 1955): A₁ = g₁; A₁A₂⁻¹A₁ = g₂;
A₂ = g₁g₂⁻¹g₁. Hence ⟨A₁,A₂⟩ = ⟨g₁,g₂⟩, which by Cohn's theorem is the commutator
subgroup of PSL(2,ℤ) — free of rank two, the fundamental group of the modular
once-punctured torus, on which the Markov correspondence lives (traces of simple closed
geodesics = 3 × Markov numbers; cited, not re-derived). The identification is implicit
in Reutenauer's morphism — the pair IS (μ(x), μ(y)) — and we record the
generator-for-generator dictionary for the family reading. Moreover every balanced word in
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

**Definition (breathable, breather, rooted).** B ∈ SL(2,ℤ) with tr B > 2 is *breathable*
if it has an orientation-reversing integer square root: some X ∈ GL(2,ℤ) with det X = −1
and X² = B; such an X is a *breather* (the root, not B). A word w ∈ {R,L}* is *rooted* if
its monodromy matrix is breathable. (These are the same notion; "rooted" is the word-level
name used in §3.3.)

### 3.1 Theorem D: the square-root criterion (classical)

**Theorem D (Northshield).** B ∈ SL(2,ℤ) with tr B > 2 admits X ∈ GL(2,ℤ) with det X = −1, X² = B,
iff t := √(tr B − 2) ∈ ℤ_{>0} and t divides B − I entrywise; then X = (B − I)/t, unique
up to sign.

*Proof.* (⟹) det X = −1 and Cayley–Hamilton give X² = (tr X)X + I, so B = tX + I,
t = tr X, tr B = t² + 2, and X = (B − I)/t. (⟸) Set X = (B − I)/t. Then
det(B − I) = 1 − tr B + det B = −t², so det X = −t²/t² = −1; and by B's own
Cayley–Hamilton, B² = (t²+2)B − I, whence X² = (B² − 2B + I)/t² = t²B/t² = B.
Uniqueness: any root Y satisfies Y = (B − I)/tr Y with (tr Y)² = t². ∎

The criterion with the formula X = (B − I)/t is Northshield's (Square roots of 2×2
matrices, Contemp. Math. 517 (2010), eq. (7)); O'Sullivan (arXiv:2408.14405, §8.3)
exhibits the determinant-−1 root of the R^tL^t word explicitly. We state the proof for
completeness and cite rather than claim. Every metallic matrix is breathable, with
X_m = (A_m − I)/m.

### 3.2 Theorem D′: traces, principal breathers, and the class group

**Theorem D′.** (i) The breathable traces are exactly the metallic traces:
{tr B : B breathable} = {t² + 2 : t ≥ 1}. (ii) The family does not exhaust the
breathable locus: A₁³ is breathable ((A₁³ − I)/4 = X₁³), as is every odd power of a
metallic matrix; and at the metallic trace itself there exist breathers not conjugate
to A_m whenever the class number h(m²+4) exceeds 1 — for m = 6 (ℤ[√10],
h = 2), B′ = [[19,30],[12,19]] of trace 38 passes the criterion with root
X′ = [[3,5],[2,3]], and B′ is not GL(2,ℤ)-conjugate to A₆ (the associated binary forms
lie in different genera; a conjugator search is exhausted as a check). (iii) Under the
Latimer–MacDuffee correspondence, the GL(2,ℤ)-classes of roots of trace t = m biject
with the ideal classes of ℤ[λ_m]; A_m is the breather of the principal class. **The
family equals the breathable locus at its traces iff h(m²+4) = 1** — the
class-number-one specialization of the Latimer–MacDuffee/Sarnak count.

*Proof sketch and certificates.* (i): both inclusions are Theorem D plus X_m. (ii): the
displayed matrices verify in one line each (reproducers cited); non-conjugacy by the
genus of the associated disc-40 binary quadratic forms — principal (1,−6,−1) vs.
non-principal (2,0,−5); equivalently the disc-40 form t² + 6st − s² does not represent ±2
(checked, |s,t| ≤ 400 and by residues), so no GL(2,ℤ) conjugator exists. (iii) is the Latimer–MacDuffee correspondence applied verbatim to x² − mx − 1
(Latimer–MacDuffee 1933; Taussky); Sarnak's reciprocal-geodesic count is the same
correspondence in negative-Pell/class-number form; his det-−1 reciprocators ARE our
breathers (X, det −1, X² = A). Which t give h(t²+4) = 1 is the Yokoi problem
(Yokoi 1986–88). We do not claim novelty for the equivalence: it is the =1 case of
Sarnak's count — "the number of root classes is one ⟺ the class number is one" — and
since N(λ_m) = −1 makes the order's narrow and wide class numbers coincide (h⁺ = h for
every metallic order), even the narrow refinement is inert. What we contribute is only the
placement of A_m as the principal breather and the resulting reading of the family. ∎

*Remark (provenance of the correction).* An earlier draft claimed "family = locus" and was
wrong; this paper's own referee panel produced the counterexamples. The correction is more
mathematics, not less — the class group of the scale is part of the breath's story.

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

**Lemma 3.3 (the bridge: word-mirror ⟹ amphichiral).** Let A(w) ∈ SL(2,ℤ) be the monodromy
of the word w. Reading w backwards with R ↔ L gives the transpose: A(rev·swap(w)) = A(w)ᵀ.
Now A(w)ᵀ = J⁻¹A(w)⁻¹J with J = [[0,1],[−1,0]] (since for any M ∈ SL(2), Mᵀ = J⁻¹M⁻¹J).
So if w is word-mirror — rev·swap(w) a cyclic rotation of w, i.e. A(rev·swap(w)) conjugate
to A(w) — then A(w) is conjugate to A(w)⁻¹ by an element of GL(2,ℤ) of determinant −1 (the
composite of the rotation-conjugator with J, det J = 1 but the transpose flips orientation).
A determinant−(−1) conjugacy of the monodromy to its inverse induces an orientation-REVERSING
self-homeomorphism of the mapping torus M(w) (it reverses both the fiber, via transpose, and
the base ℤ-direction, via inverse). Hence M(w) is amphichiral. ∎

*Provenance.* The criterion is known in substance: the full statement (both mechanisms, with
sufficiency-not-necessity) is proved for closed Sol torus bundles by Tian–Wang–Wang
(arXiv:2406.13241, Lemma 3.1, Thm 3.5) and transplants to the punctured case; the algebra
"rev·swap = conjugate-to-inverse" is Baake–Roberts (J. Phys. A 30 (1997), Props. 3–5); the
symmetry group of a punctured-torus bundle is the monodromy's GL(2,ℤ)-normalizer
(Floyd–Hatcher 1982, p. 268). Morimoto's unoriented classification marks the trap avoided
above: plain conjugacy to A^{±1} ignores orientation — the determinant −1 of the conjugator
is what makes the self-homeomorphism orientation-reversing. Ours are the punctured word-form
statement, the witnesses, and the tables.

**Theorem E (word level).** word-mirror ⟹ balanced (rev·swap exchanges the letter
counts; rotations preserve them). Strict: RRRLLRLL is balanced, not word-mirror — and
its bundle is genuinely chiral (CS = −0.0012159…, its rev·swap partner +0.0012159…: a
chiral mirror pair of balanced words).

**Theorem E″ (manifold level).** rooted ⟹ amphichiral (the deck involution of the
orientation double cover reverses orientation — the Gieseking-classical mechanism;
closed-case statement in Sakuma 1985, Case II). Strict, and the two levels differ:
the two cyclic classes LLLRLLRRRLRR and LLLRRLRRRLLR (trace 146, t = 12) are rooted —
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

## 4. The level-15 Weil shadow of the pair

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

**The shadow is mod-15.** Every operator in §4 is a function of the pair's residue in
SL(2,ℤ/15): W(A) depends only on A mod 15. Consequently the whole chapter — the commutator
table, the closure set, the tiers, the master table — is an invariant of the mod-15 image,
not of the integers (1,2) or of parabolicity. Concretely A₁₆ ≡ A₁ and A₁₇ ≡ A₂ (mod 15),
and the pair (A₁₆, A₁₇), whose commutator trace is 2 − (16·17)² = −73982 (as far from
parabolic as one likes), produces §4 verbatim. We therefore read §4 as the arithmetic of
the level 15 = 3·5 that the pair happens to point to (its product trace), and claim nothing
about parabolicity here; open problem 4 records that the analogous construction at other
product traces behaves differently.

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

κ_q := tr[W₁,W₂] = −1, while tr[A₁,A₂] = −2: the level-15 shadow of the commutator is not
the shadow of a parabolic — consistent with §4.0, the operators do not see parabolicity.

**The magnitude law (Howe's formula, verified 25/25):** |κ_q(j,l)|² =
#Fix([A₁ʲ, A₂ˡ] acting on (ℤ/15)²) — the table's magnitudes are the square roots of the
classical commutators' fixed-point counts (Howe; exact character values with signs:
Thomas, J. London Math. Soc. 77 (2008)). The divisors of 15 appearing in the table are
Howe's formula evaluated at level 15.

### 4.2 Theorem F: closure, and the residue groups (the iff assembled from published
halves)

**Theorem F.** (i) The mod-3 image of (A₁, A₂) is Q₈ (a² = b² = [a,b] = −I); the mod-5
image is SL(2,5), order 120. (ii) [W₁ʲ, W₂ˡ] = I ⟺ [A₁ʲ, A₂ˡ] ≡ I (mod 15). Both directions are corollaries of
published results, though we found the equivalence stated verbatim nowhere: ⟸ is the
classical commutation principle (Kurlberg–Rudnick Cor. 6; in the cleanest form, the
multiplicativity U(A)U(B) = U(AB mod N) at odd N — Kelmer); ⟹ needs the *genuine* (linear) representation, not merely the projective one: projective
injectivity in odd dimension (Appleby, J. Math. Phys. 46 (2005), Bolt–Room–Wall lineage)
forces [A₁ʲ, A₂ˡ] to be a SCALAR mod 15, but the centre of SL(2,ℤ/15) has order four
({I, 4I, 11I, 14I}) and non-identity scalars do occur — e.g. [A₁, A₂³] ≡ 11·I (mod 15), on
28 of the order-torus addresses. What closes the gap is that the genuine Weil rep at odd
level is FAITHFUL on that order-four centre: W(11·I) = Par₃ ⊗ I₅ ≠ I (Kurlberg–Rudnick
Thm 5; Kelmer's genuine multiplicativity), so a scalar image other than I gives [W] ≠ I —
indeed all 28 non-identity-scalar addresses carry κ_q = −5 ≠ 15, i.e. [W] ≠ I. Hence
[W]=I ⟺ [A]≡I mod 15. Our exact check on all 240 points confirms this. (iii) In particular
[W₁², W₂³] = I exactly: A₁² is central mod 3 and A₂³ is central mod 5, so the
commutator dies at the CRT-central address — and (2,3) is the minimal address with both
exponents non-central mod 15 (A₂⁶ ≡ 11·I is central, so e.g. (1,6) also closes — the
minimality is among addresses whose BOTH powers are non-central; verified on the order
torus). The full closure set is the mod-15 commutation locus.

One structural fact and one convention-note, recorded without weight. (a) The image of
the pair in SL(2,ℤ/15) is Q₈ × SL(2,5) of order |Q₈|·|SL(2,5)| = 8·120 = **960**
(CRT; verified by direct enumeration); its projectivization has order 240 = ord(W₁)·ord(W₂)
= 20·12, the size of the order torus. (b) The single products satisfy
tr(Par·W₁W₂)/tr(Par·W₂W₁) = ζ₁₅ in the c = 1 lift; the individual phases are lift-dependent
(a single product is not a commutator, so Prop 4.0 does not protect it — under W₁ ↦ ζ₆₀W₁
the numerator moves), and only the ratio ζ₁₅ is invariant.

### 4.3 Theorem G: a worked instance of the divisor-lattice (even-function) factorization

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

(each cell: κ_q value, tier. Legend — the four Galois channels are the coordinates in the
basis {1, √5, √−3, √−15} of ℚ(√5,√−3); write q = √5, r = √−3, s = √−15, and *rat* = the
rational (basis-1) coordinate. A tier names which channels VANISH: *free* = none vanish
(fully active, count 120), *qs* = {√5,√−15} vanish (20), *rs* = {√−3,√−15} vanish (20),
*qrs* = {√5,√−3,√−15} vanish — only the rational channel survives (10), *dark* = all four
vanish (70). Cell sizes are φ(20/gx)·φ(12/gy).) **The two factorizations are classical, and
independent.** Factorization-through-gcd is Cohen's/McCarthy's class of "even functions
(mod r)" (Cohen, PNAS 41 (1955); McCarthy 1986 for the two-variable (r,s)-even form
f(a,b) = f(gcd(a,r), gcd(b,s))). κ_q factors by Serre's ℚ-class principle (Linear
Representations §12.4/§13.1: rational class functions are constant on ℚ-classes) — it is
rational-valued and, by the magnitude law, determined by the classical commutator's
fixed-point count and sign, computed exactly per cell. The tier factors by the same
even-function mechanism applied to the interaction form's Galois channels
(Coste–Gannon/Bantay equivariance). We emphasize these are two functions obeying the SAME
classical rule on the SAME lattice — not a coupled "joint" theorem; the tier half is here
VERIFIED on all 240 points, not proved, with the per-channel derivation deferred to the
companion paper on the interaction form. Consequences read off the table: a fully
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

**The gate, run in full (two rounds, six hunts; verdicts and references in
LIT_GATE.md).** (a) The symmetric-pair identity: PARTIALLY-KNOWN — classical in three
clothings (Sarnak; Gehring–Martin; Goldman/Fricke), the (1,2) instance verbatim in
Reutenauer; ours is the coordinate lemma as stated, the metallic parametrization, and
the uniqueness scan. (b) Uniqueness of (1,2): the scan is ours; the pair itself is
Reutenauer's, and matrix-level uniqueness claims are positioned against Schmutz
Schaller (2022) and Nielsen. (c) The root criterion is Northshield's exactly; the
classification is Latimer–MacDuffee verbatim; the h⁺-equivalence and the
principal-breather framing were found nowhere stated and are claimed as assembly.
(d) The amphichirality criterion is known in the closed Sol case (Tian–Wang–Wang) over
Baake–Roberts/Floyd–Hatcher; ours are the punctured word-form statement, the strictness
witnesses ((ℤ/12)² pair; the balanced chiral mirror pair), and the tables. RESIDUAL
(stated as the gate found it): no page-level access to the full texts of Aigner 2013
and Reutenauer 2018 was possible — per-item verdicts for the books rest on
chapter-level evidence and the 2019–2026 citing sweep; and Cohn's 1955/1972 papers
could contain the symmetric-commutator identity in entry-level form. References
welcome.
**The quantized-cat-map gate, run (LIT_GATE.md):** the commutation principle's ⟸
direction, the genuine representation at odd level, the CRT factorization, and the
character-magnitude machinery are all in print and cited above (Kurlberg–Rudnick;
Mezzadri; Schur/Beyl/Nobs–Wolfart; Howe/Thomas). The ⟹ direction of Theorem F(ii) is a
folklore corollary (Appleby injectivity + genuine-rep faithfulness on the centre — §4.2),
and the divisor-lattice factorization PATTERN is classical (Cohen/McCarthy even functions;
Serre ℚ-classes) — neither is claimed. What our search of that corpus did not find, and
what we state as this paper's contributions: the explicit N = 15 commutator table; the
Q₈ × SL(2,5) commutator-image assembly at N = 15; and the (2,3)/non-central closure
address. The 36-cell table and its tier readings are ours as a worked instance, not as a
new factorization principle.

## 6. Open problems

1. The family quantum column (κ_q at each pair's product trace; does closure track CRT
   centrality uniformly?). 2. The cyclotomic-support step of Theorem G. 3. **Two constants, from two distinct towers, neither identified in closed form.** The paper
   has two "towers," and the constants must be kept apart. (a) *The chain* is the Markov-spine
   walk s₀ = A₂, s₁ = A₁, s_{k+1} = s_k s_{k−1} (§2.4); write G_k for its number of R/L
   letters (G_k = G_{k−1} + G_{k−2}, Fibonacci). Its per-letter growth is
   **λ_chain := limₖ (tr s_k)^{1/G_k} = 1.57705744122666946…** (the growth of the chain's
   geodesic lengths per letter; recomputed as a genuine limit to 18 digits, n ≤ 55). (b) *The
   Fibonacci letter tower* is the substitution a → R, b → L applied to a seed (§3.3, Prop
   E‴), giving words w_k; **c := limₖ Vol(M(w_k))/|w_k| = 0.934102018057787980264187790656…**,
   the hyperbolic volume per letter, obtained by the Fibonacci-additivity extrapolation
   (the additivity defect is < 10⁻²⁷ by rung 13; a numerical limit, not proved to converge).
   Both are located to the working precision of the reproducer only; at the reproducer's
   precision (≈ 40 digits) PSLQ finds no integer relation of degree ≤ 8 with height ≤ 10⁴ for
   either — but these are HEIGHT-BOUNDED exclusions, NOT non-algebraicity certificates, and
   the truncated digit strings printed here are too short to reproduce them (at 18 digits PSLQ
   returns spurious relations), so the exclusion lives with the reproducer, not the page.
   4. Why 15
   twice (the seam trace equals the conductor-type level of ℚ(√−15); the naive family
   law fails at (1,3)). 5. The standard-word lemma (chain words word-mirror for all k).
   6. The chain-breathability conjecture beyond rung 200. 7. The heredity of the chain's
   torsion primes.

## Appendix A: reproducibility

Every displayed result maps to a public reproducer in the repository (paths under
`frontier/`); each carries a lock (`ALL CHECKS PASS`) re-run at this draft. Symbolic checks
are exact (SymPy over ℚ or a cyclotomic field); the quantum layer is exact in F_p at
p ≡ 1 (mod 60), cross-checked at two primes; SnapPy/sage-python supplies the hyperbolic
geometry.

| result | statement | reproducer |
|---|---|---|
| Lemma 2.2 | symmetric-pair identity tr[A,B] = 2 − (M₁₂−M₂₁)² | `chain_verify.py` (symbolic, ≡ 0 on the SL(2) locus) |
| Theorem A | tr[A_m,A_n] = 2 − (mn(n−m))²; (1,2) unique | `chain_verify.py` |
| §2.1 Alexander | Δ_m(a) = a² − (m²+2)a + 1, m = 1…5 | `B485_metallic_apoly_family/apoly_sage.py` (SnapPy) |
| Theorem B | ⟨A₁,A₂⟩ = ⟨g₁,g₂⟩ generator-for-generator | `chain_verify.py` |
| Theorem C | spine 1,2,5,13,194,7561; Markov triples; Nielsen | `chain_verify.py` |
| Theorem D / D′ | root criterion; A₁³ and [[19,30],[12,19]] counterexamples; h=1 iff | `hierarchy_verify.py` |
| Prop E‴ | residue = −ω^{#L−#R}; Pisano π(3)=8 | `rf3_quantum.py` |
| Thm E/E″ witnesses | RRRLLRLL chiral (CS ≠ 0); LLLRRLRRRLLR rooted, (ℤ/12)²; aba | `hierarchy_verify.py` |
| §4.1 table | tr[W₁ʲ,W₂ˡ], three-lift exact | `B472_quantum_commutator/kq_verify.py` |
| magnitude law | \|κ_q\|² = #Fix (25/25) | `kq_verify.py` |
| Theorem F | Q₈, SL(2,5); [W₁²,W₂³]=I; (2,3) minimal non-central | `kq_verify.py` |
| Theorem G | ε(jl)·χ₅; 36-cell master table; tiers 120/20/20/10/70 | `B474_tier_commutator_law/cross_table.py` |
| §4.0 collision | (A₁₆,A₁₇) ≡ (A₁,A₂) mod 15 (level-15 shadow) | exact engine `B465_monodromy_intake/exact_engine.py` |
| §6 constants | λ_chain, c as limits + PSLQ height-bounded exclusions | `c_identify.py`, `chain_verify.py` (working precision in-file) |

The two banked errors this draft's own panel caught and fixed (the two-block gap in the
first amphichirality theorem; the "family = locus" over-claim) have regression checks in
`hierarchy_verify.py`.

## Appendix B: the corrections ledger

This paper was built by an internal adversarial-review process — a panel of independent
referees run against each draft, followed by a two-round literature gate — and it corrected
itself repeatedly on the way. We record the path plainly, because a result reached by
surviving its own refutations is more trustworthy than one asserted once, and because the
demotions are as much a part of the mathematics as the promotions.

**Errors the panel found and fixed (banked corrections).**
1. *The first amphichirality theorem was false in generality.* An early draft's
   palindromic-alphabet argument covered two-block products only; rev·swap reverses the block
   *sequence*. Counterexample A₁A₂A₃. The surviving statement is Theorem E/E″ with its exact
   witnesses and Lemma 3.3's bridge.
2. *"Family = breathability locus" was false.* A₁³ is a rooted composite, and [[19,30],[12,19]]
   is a non-principal breather at trace 38 (ℤ[√10], h = 2), not conjugate to A₆. The corrected
   — and stronger — statement is Theorem D′: breathable traces = metallic traces, A_m the
   principal breather, family = locus ⟺ h(m²+4) = 1.
3. *Theorem A is a generic symmetric-pair identity*, not a family miracle (Lemma 2.2); the
   paper's weight moved to the Cohn identification and the metallic integer mn(n−m).

**Literature-gate demotions (accepted in full).**
4. The symmetric-pair identity is the coordinate form of classical facts (Sarnak; Gehring–
   Martin), with the (1,2) pair verbatim Reutenauer's Markoff morphism.
5. The square-root criterion (Theorem D) is Northshield's (2010) — cited, no longer claimed.
6. The amphichirality criterion is Tian–Wang–Wang's closed case (Lemma 3.3), over Baake–
   Roberts and Floyd–Hatcher.
7. The converse of Theorem F(ii) is a folklore corollary of Appleby's odd-dimension
   injectivity — demoted from "ours, verified" to "confirmed"; our 240-point check stands as
   confirmation.

**Round-2 structural corrections.** §4 was reframed as the *level-15 Weil shadow* once the
collision (A₁₆,A₁₇) ≡ (A₁,A₂) mod 15 showed §4 is blind to parabolicity; the "240" and ζ₆₀
"curiosities" were corrected (the image is Q₈ × SL(2,5) of order 960; the single-product
phases are lift-dependent). The "certifiably non-algebraic" claim for the constants became a
height-bounded exclusion.

What survives all of this is stated as ours in §5, scoped exactly: the family question, the
two-parameter failure integer and its uniqueness scan, the principal-breather/class-number
assembly, the hierarchy witnesses, and the explicit N = 15 quantum tables with their
divisor-lattice reading. The method is not the theorem — but it is why the theorems can be
trusted.

---
*MSC 11J06, 11E16, 57K10, 20H10, 81Q50. Repository URL at packaging.*
