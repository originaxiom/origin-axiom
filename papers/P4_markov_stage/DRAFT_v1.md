# The unique parabolic pair of the metallic family: Markov's stage, breathability, and a quantum commutator

**Draft v1 — 2026-07-08. Every displayed claim is lock-backed (17/17 re-verified at draft
time; Appendix A maps claims to reproducers). Narrative beats marked ⟡ are the owner's to
retell. Lit-status per the honesty protocol of §5: "we could not locate" is the strongest
novelty language this paper uses.**

---

## Abstract

For integers m ≥ 1 let A_m = [[m²+1, m],[m, 1]] ∈ SL(2,ℤ) — the *metallic matrices*, the
monodromies of the once-punctured-torus bundles with orientation-reversing square roots;
A₁ is the monodromy of the figure-eight knot complement. We prove the trace identity

  tr[A_m, A_n] = 2 − (mn(n−m))²,

so the commutator's deviation from parabolicity is a perfect square, and exactly one pair
— (m,n) = (1,2), the golden and silver matrices — closes the cusp. This pair generates
the commutator subgroup of PSL(2,ℤ), Cohn's modular torus group: the classical stage of
Markov's theory of badly approximable numbers. The Fibonacci substitution applied at the
level of the pair walks the Markov spine with the cusp intact at every stage. We
characterize the metallic family as the *breathability locus* — the matrices in SL(2,ℤ)
of trace t admitting an integer square root of determinant −1 are governed by t − 2
being a perfect square together with an integral divisibility, and tr(A_m) − 2 = m² —
and we prove a stratified hierarchy of symmetries (root, mirror, balance, residue) for
words in the metallic alphabet, with exact witnesses separating every stratum. Finally
we quantize: at level 15 = tr(A₁A₂), the Weil-representation commutators [W₁ʲ, W₂ˡ] are
governed by two characters — a quaternionic parity (the mod-3 image of the pair is Q₈)
and a mod-5 closure bit (the mod-5 image is SL(2,5)) — the quantum cusp closes exactly at
the CRT-central address [W₁², W₂³] = I, and both the commutator traces and the vanishing
tiers of the pair's interaction form factor through the divisor lattice of the two clock
orders. Throughout, the classical core (Fricke, Cohn, Markov) is credited as such; §5
states precisely which statements we could not locate in the literature.

---

## 1. Introduction

⟡ *[The owner's opening. The beats the draft supplies:]*

In 1955, Harvey Cohn observed that Markov's 1879–80 theory of minima of indefinite
quadratic forms — the theory that begins with the golden ratio as the worst-approximable
number and climbs the tree of triples (1,2,5), (1,5,13), … — lives on a single geometric
object: the commutator subgroup of the modular group, the fundamental group of a
once-punctured torus, with Markov's numbers appearing as one third of the traces of its
simple elements. The stage has been studied for seventy years; its literature is a
library (Aigner 2013; Reutenauer 2018; Cusick–Flahive 1989).

This paper asks one question the library does not: Cohn's generators are the first two
members of a natural *family*. The matrices

  A_m = [[m²+1, m],[m, 1]],  m = 1, 2, 3, …

are precisely the monodromies R^m L^m of once-punctured-torus bundles built from the
metallic means λ_m = (m + √(m²+4))/2 — golden, silver, bronze. A₁ = [[2,1],[1,1]] is
Cohn's g₁ matrix-for-matrix, and it is the monodromy of the figure-eight knot complement,
the smallest hyperbolic knot. The family question: *which pairs of metallic matrices
rebuild the stage?* A once-punctured-torus group is characterized among two-generator
groups by its boundary: the commutator of the generating pair must be parabolic —
tr[A, B] = −2, the cusp condition. For which (m, n) does the cusp close?

The answer is Theorem A: the deviation is a perfect square,

  tr[A_m, A_n] = 2 − (mn(n−m))²,

and mn(n−m) = 2 has exactly one solution in positive integers m < n: the pair (1,2).
⟡ *[the failure of every other pair is quantized — equal squares are equal tears; the
owner's line.]* The unique pair generates Cohn's group exactly (Theorem B), the
substitution a → ab iterated on the pair walks the Markov spine with every renormalized
pair again parabolic (Theorem C) — an infinite tower of stages — and the family itself
is cut out by a square condition of its own: breathability (Theorem D).

The second half of the paper quantizes the pair at the level its own arithmetic selects
— 15 = tr(A₁A₂) — and finds the stage's quantum shadow: the commutator of the Weil
operators is governed by two characters; the mod-3 residue of the pair is the quaternion
group, the mod-5 residue the binary icosahedral group; the quantum cusp closes not at
the generators but at the arithmetic's center, [W₁², W₂³] = I (Theorem F); and the
entire selection structure of the pair's interaction — which combinations vanish, which
survive — is a pair of functions on the 36-cell divisor lattice of the two clock orders
(Theorem G, the master theorem).

**Reading guide and honesty protocol.** The Fricke trace identity, Cohn's correspondence,
and the Markov tree are classical; we cite and never re-claim them. The statements we
believe to be new are stated in §5 with the exact language "we could not locate": the
metallic parametrization and its factored square (Theorem A), the breathability
characterization (Theorem D), the stratified symmetry hierarchy with its witnesses
(§3), the closure theorem and the divisor-lattice factorization (§4). Every numerical
claim in this paper is backed by an exact computation with a public reproducer
(Appendix A); several of this paper's results were found by refuting earlier versions
of themselves, and we record that path in Appendix B, because the method is part of
the result. ⟡

---

## 2. The family and the stage

### 2.1 Metallic matrices, halves, and the norm

Let R = [[1,1],[0,1]], L = [[1,0],[1,1]] be the elementary twist matrices, and for m ≥ 1
set A_m = R^m L^m = [[m²+1, m],[m, 1]], with tr A_m = m² + 2. Define the *half-matrix*

  X_m = [[m, 1],[1, 0]],  det X_m = −1,  X_m² = A_m.

X_m is the companion matrix of x² − mx − 1, the minimal polynomial of the metallic mean
λ_m; hence

**Proposition 2.1 (the norm of the scale).** det X_m = N_{ℚ(√(m²+4))/ℚ}(λ_m) = −1 for
every m; the orientation character of the half-matrix and the field norm of the scaling
unit are the same −1. The property persists through the same-field degeneracies: the
ℚ(√5)-members m = 1, 4, 11, 29, … are exactly the odd powers φ, φ³, φ⁵, φ⁷, … of the
fundamental unit, so the norm is (−1)^odd = −1 throughout. No unit of norm −1 exists in
an imaginary quadratic field (the norm form is positive definite): the −1 lives on the
real axis alone. ∎ (One-line proofs; reproducer `br_n_norm.py`.)

Geometrically: the mapping torus M(A_m) is a hyperbolic once-punctured-torus bundle
(m = 1: the figure-eight complement), and X_m generates a non-orientable bundle
double-covered by M(A_m) — for m = 1 this is the Gieseking manifold, and the SnapPy
census confirms the cover exactly (vol ratio 2, m000 → 4₁). The family carries its
orientation-reversing half uniformly.

### 2.2 Theorem A: the uniqueness of the parabolic pair

**Theorem A.** For all integers m, n ≥ 1,

  tr[A_m, A_n] = 2 − (mn(n−m))².

Consequently tr[A_m, A_n] = −2 (the commutator is parabolic) if and only if
mn(n−m) = ±2; for positive integers m < n the unique solution is (m,n) = (1,2).

*Proof.* Write x = tr A_m = m²+2, y = tr A_n = n²+2. A direct computation gives
tr(A_m A_n⁻¹) = (m−n)² + 2, whence by the product-trace identity
z := tr(A_m A_n) = xy − tr(A_m A_n⁻¹) = (mn+1)² + m² + n² + 1.
The Fricke identity for two-generator subgroups of SL(2) (classical; Fricke–Klein, see
also Goldman's survey) states tr[A,B] = x² + y² + z² − xyz − 2. Substituting and
factoring the resulting polynomial in ℤ[m,n]:

  x² + y² + z² − xyz − 2 = 2 − (mn(n−m))²,

an identity verified by expansion (both sides are polynomials of degree ≤ 8; the
identity also follows from exact agreement on any 9×9 integer grid). The equation
mn(n−m) = 2 in positive integers m < n forces m = 1, n = 2 by inspection of the
factorizations of 2. ∎

Three remarks. (i) The failure of every non-parabolic pair is *quantized*: the level
sets of the deviation are the level sets of mn(n−m) — for instance (1,3), (2,3) both
have mn(n−m) = 6, hence both tr[·,·] = −34: equal squares are equal tears. ⟡
(ii) At the unique pair, the trace triple (x, y, z) = (3, 6, 15) satisfies Markov's
equation x² + y² + z² = xyz, i.e. (1, 2, 5) after division by 3 — the third Markov
triple. The seam of the pair, tr(A₁A₂) = 15, will return as the quantization level in
§4. (iii) The commutator itself is [A₁,A₂] = [[11,−24],[6,−13]], a parabolic of trace
−2: the pair (A₁, A₂) is a type-preserving representation of a once-punctured-torus
group — the stage exists.

### 2.3 Theorem B: the stage is Cohn's

Let g₁ = [[2,1],[1,1]], g₂ = [[1,1],[1,2]] be Cohn's generators (Cohn 1955).

**Theorem B.** A₁ = g₁, and the Nielsen identities A₁A₂⁻¹A₁ = g₂, A₂ = g₁g₂⁻¹g₁ hold;
hence ⟨A₁, A₂⟩ = ⟨g₁, g₂⟩, the commutator subgroup of PSL(2,ℤ) — a free group of rank
two whose quotient surface is the modular once-punctured torus. Moreover every *balanced*
word in R, L (equal exponent sums, in particular every metallic matrix and every word of
the chain of §2.4) lies in this subgroup: in PSL(2,ℤ), L = S T⁻¹ S⁻¹ with T = R, so the
abelianization ℤ/6 sends a word to t^{#R − #L}. ∎

Everything Markov-theoretic about ⟨g₁,g₂⟩ is classical and cited, not re-derived: Markov
triples as ⅓-traces, the tree, the correspondence with Christoffel words (Reutenauer
2018). What the theorem adds is the *identification*: the metallic family's unique
parabolic pair does not merely resemble the classical stage; it is the classical stage,
generator for generator. ⟡ *[the program stood on Cohn's stage for a year without
knowing its name — the owner's beat.]*

### 2.4 Theorem C: the chain walks the spine

Define the chain s₀ = A₂ (= b), s₁ = A₁ (= a), s_{k+1} = s_k s_{k−1} — the Fibonacci
substitution a → ab, b → a applied at the level of the pair.

**Theorem C.** (i) The traces u_k = tr(s_k) satisfy the Fricke recursion
u_{k+1} = u_k u_{k−1} − u_{k−2}, and every consecutive triple satisfies Markov's
equation u² + v² + w² = uvw. (ii) u_k/3 walks the Markov spine 1, 2, 5, 13, 194, 7561,…
(iii) Every renormalized pair (s_k, s_{k+1}) again satisfies tr[s_k, s_{k+1}] = −2:
the chain is an infinite tower of once-punctured-torus stages.

*Proof.* (i) is the trace identity tr(PQ) = tr(P)tr(Q) − tr(PQ⁻¹) applied to the chain,
together with the invariance of x² + y² + z² − xyz under the Vieta move
(x, y, z) → (y, z, yz − x) — the seed triple (6, 3, 15) satisfies Markov (§2.2(ii)),
and the move preserves it. (iii) Each step (s_{k−1}, s_k) → (s_k, s_k s_{k−1}) is a
Nielsen transformation of the generating pair; the conjugacy class of the commutator of
a generating pair of a free group of rank two is invariant under Nielsen transformations
up to inversion (this is the well-definedness of the boundary of the once-punctured
torus). Hence tr[s_k, s_{k+1}] = tr[A₁, A₂]^{±1} = −2. ∎

The cusp survives every stage of the substitution: a → ab does not merely act on
letters and matrices — it acts on stages, and it never tears one. ⟡

---

## 3. Breathability: the family as a locus, and the hierarchy of symmetries

### 3.1 Theorem D: which words carry a half

**Theorem D (the root criterion).** B ∈ SL(2,ℤ) with tr B > 2 admits X ∈ GL(2,ℤ) with
det X = −1 and X² = B if and only if t := √(tr B − 2) is a positive integer and t
divides B − I entrywise; in that case X = (B − I)/t, uniquely up to sign.

*Proof.* det X = −1 gives, by Cayley–Hamilton, X² = (tr X)·X + I, so B = tX + I with
t = tr X and tr B = t² + 2; conversely (B − I)/t squares to B whenever it is integral. ∎

For the family, tr A_m − 2 = m² and (A_m − I)/m = X_m: **the metallic matrices are
breathable, uniformly.** For the chain, none of the composite words are: u_k − 2 is a
non-square for all 2 ≤ k ≤ 200 (certified by quadratic-non-residue witnesses mod small
primes; the traces themselves exceed 10¹⁰ digits long before k = 200, so the modular
certificates are the only honest route). The alphabet is exactly the root locus: the
deepest symmetry lives on the letters and never propagates to a composite word. ⟡

### 3.2 The hierarchy with exact witnesses

For a word w in {R, L} write rev·swap(w) for the reversal with R ↔ L exchanged; call w
*word-mirror* if rev·swap(w) is a cyclic rotation of w, *balanced* if #R = #L. Call the
bundle M(w) *mirror* (amphichiral) if it admits an orientation-reversing self-isometry,
and *rooted* if the monodromy satisfies Theorem D's criterion.

**Theorem E (the hierarchy).** rooted ⟹ mirror ⟹ *[for the word criterion]* balanced,
and balanced ⟹ the quantum residue of §4 is frozen. Every implication is strict:

- *mirror without root*: the word aba of the chain — M(RLRRLLRL), vol 7.6417106…,
  H₁-torsion 37 (not a square), CS = 0.
- *rooted without word-mirror*: exactly two cyclic classes of length ≤ 13,
  LLLRLLRRRLRR and LLLRRLRRRLLR (trace 146, t = 12) — both amphichiral (CS = 0, an
  isometric pair), with homology torsion (ℤ/12)²: the root's square trace surfacing as
  square homology. The word criterion is thus sufficient but not necessary for mirror.
- *balanced without mirror*: RRRLLRLL (CS = −0.0012159…; its rev·swap partner carries
  +0.0012159 — a genuine chiral mirror pair of balanced words).

*Proof of the implications.* rooted ⟹ mirror: the orientation double cover of the
non-orientable bundle generated by X has orientation-reversing deck involution.
word-mirror ⟹ balanced: rev·swap exchanges the letter counts, rotation preserves them.
balanced ⟹ frozen residue: §4.1. ∎

**Theorem E′ (palindromic alphabets).** Every word in the metallic alphabet
{R^m L^m : m ≥ 1} is word-mirror — rev·swap fixes each letter, so rev·swap(uv) = vu,
which is a rotation of uv — hence every metallic-word bundle is amphichiral. In
particular the entire chain of §2.4 has CS = 0 at every rung (verified through rung 8),
while the *letter* tower (a → R, b → L) is chiral from its third rung on, with the
imbalance #L − #R = −F_{k−2} driving both the chirality and the residue rhythm of §4. ∎

⟡ *[The two towers — one alphabet breathes at every rung, the other holds its breath
after the seed. The owner's telling; the mathematics above is complete without it.]*

---

## 4. The quantum commutator

### 4.1 The Weil pair at the level the arithmetic selects

Let N = 15 = tr(A₁A₂). On ℂ^N = ℂ[ℤ/15] define the Weil (metaplectic) operators W₁, W₂
attached to A₁, A₂ — explicitly, with ζ = e^{2πi/15}, D = diag(ζ^{j(j−1)/2}) the twist
operator and F the unitary discrete Fourier transform, W_m = ((F D F*)*)^m D^m. All
statements below are verified exactly in three independent lifts (two exact-cyclotomic
constructions and reductions at split primes p ≡ 1 (mod 60)); the commutator table is
lift-independent because the projective scalars cancel in [W₁ʲ, W₂ˡ].

**The table.** tr[W₁ʲ, W₂ˡ] for 1 ≤ j, l ≤ 5:

|      | l=1 | l=2 | l=3 | l=4 | l=5 |
|------|-----|-----|-----|-----|-----|
| j=1  | −1  | 3   | −5  | 3   | −1  |
| j=2  | 3   | 3   | 15  | 3   | 3   |
| j=3  | −1  | 3   | −5  | 3   | −1  |
| j=4  | 3   | 3   | 15  | 3   | 3   |
| j=5  | −5  | 15  | −5  | 15  | −5  |

Every magnitude is a divisor of 15. Note κ_q := tr[W₁, W₂] = −1 while the classical
tr[A₁, A₂] = −2: **the quantization of the critical pair is not critical at the
generators.**

### 4.2 Theorem F: the closure theorem and the residue groups

**Theorem F.** (i) [W₁², W₂³] = I exactly: the quantum cusp closes at (2,3).
(ii) The mod-3 image of the pair (A₁, A₂) is the quaternion group Q₈
(a² = b² = [a,b] = −I), and the mod-5 image is SL(2,5), of order 120.
(iii) A₁² is central mod 3 and A₂³ is central mod 5; hence [A₁², A₂³] ≡ I (mod 15), and
quantum closure occurs exactly where the classical interaction dies modulo the level:
[W₁ʲ, W₂ˡ] = I ⟺ [A₁ʲ, A₂ˡ] ≡ I (mod 15).

*Proof.* (ii) mod 3 is a two-line verification; mod 5 is a closure computation (the
subgroup generated has order exactly 120). (iii) centrality is immediate from (ii)
(in Q₈, a² = −I; in SL(2,5), b³ = −I), and the Weil representation at level 15 factors
as the tensor product of the level-3 and level-5 representations (CRT), through which
the commutator depends only on the classical commutator's residue. (i) is (iii) at
(j,l) = (2,3), verified exactly. ∎

Two exact curiosities we record without weight: the seam's two faces are unit phases,
tr(Par·W₁W₂) = ζ₆₀⁸ and tr(Par·W₂W₁) = ζ₆₀⁴ — their ratio is ζ₁₅, the level's own
phase; and the projective image Q₈/±I × PSL(2,5) has order 4 · 60 = 240, the number of
points of the pair's interaction torus below.

### 4.3 Theorem G: the master theorem — the divisor lattice

The pair's interaction is measured on the torus ℤ/20 × ℤ/12 (the orders of W₁ and W₂):
on one axis by the commutator traces κ_q(j,l) above (extended to all (j,l)), on the
other by the *tiers* — the vanishing patterns of the four Galois channels of the
Par-inserted pair form tr(Par·P_a·Q_b) (the five patterns realize the subfield lattice
of ℚ(√5, √−3); their counts are 120/20/20/10/70).

**Theorem G.** (i) κ_q(j,l) = ε(jl) · χ₅(j,l), where ε = 3 if jl is even and −1 if jl
is odd (the quaternionic parity: [A₁ʲ,A₂ˡ] ≡ (−I)^{jl} mod 3, exactly, since Q₈ is
class-2 nilpotent), and χ₅ = 5 or 1 according as the mod-5 commutator is or is not the
identity. The four values of the table are the four products.
(ii) Both maps — κ_q and the tier — factor through the divisor pair
(gcd(x, 20), gcd(y, 12)): each is a single-valued function on the 36-cell divisor
lattice of the two clock orders. In particular every empirical law relating them (a
fully active cell never sits at quantum closure; the partial tiers are commutator-pure;
darkness concentrates at closure, 54 of 70 dark cells) is a finite check on 36 cells.

*Proof.* (i) is Theorem F(iii) refined by the two residue characters; the mod-3 half is
exact for all (j,l) by centrality of [a,b] in Q₈. (ii) is verified exactly on all 240
points; the master table (Appendix A) lists the 36 cells with their values. The
conceptual reading: a point's cell fixes the orders of its coordinates, hence both the
CRT-centrality data governing κ_q and the cyclotomic support governing which quadratic
channels can vanish. ∎

The one sub-derivation this paper states as a lemma-target rather than proving —
*channel vanishing from cyclotomic support* (that the tier of a cell is forced by which
quadratic subfields the cell's roots of unity span) — opens the companion paper on the
seam form. ⟡

### 4.4 A scoped remark on criticality

κ = tr[A,B] stratifies the family's pairs: the unique parabolic pair sits at κ = −2 and
every other pair is "torn" by a perfect square. We verified that the richness of the
interaction structure at other pairs tracks the prime factorization of the pair's level
(the (1,3) pair at level 27 = 3³ collapses to two values; the (2,3) pair at level
63 = 9·7 is rich again, despite equal κ) — so the architecture of §4.3 is governed by
level arithmetic, and any finer role of κ itself is open work, deliberately outside
this paper.

---

## 5. What is classical, and what we could not locate

**Classical, cited, never re-claimed.** The Fricke trace identities; Cohn's theorem that
⟨g₁,g₂⟩ is the commutator subgroup and its Markov correspondence; the Markov tree and
spine; Hurwitz's bound; the Vieta/tree moves (Aigner 2013, Reutenauer 2018,
Cusick–Flahive 1989); the Weil representation and its CRT factorization; Q₈ and SL(2,5)
as abstract groups; Gieseking's manifold; punctured-torus-bundle volume theory
(Guéritaud); the Bonahon–Wong–Yang asymptotics for the LR bundle (Pandey–Wong).

**We could not locate, after search against the above and the standard databases** —
and we would welcome references: (a) the metallic parametrization
tr[A_m,A_n] = 2 − (mn(n−m))² and its factored-square form; (b) the uniqueness of (1,2)
as the family's parabolic pair; (c) the breathability criterion of Theorem D stated for
SL(2,ℤ) with the divisibility condition, and the identification of the metallic family
as the root locus; (d) the strict hierarchy of §3.2 with its exact witnesses, in
particular the amphichiral pair with (ℤ/12)² torsion; (e) the closure theorem
[W₁²,W₂³] = I and the two-character formula; (f) the divisor-lattice factorization of
Theorem G. Items (a)–(b) sit close to classical Fricke computations and we consider it
plausible they exist in some form; the line-by-line gate against the three monographs
is part of this paper's referee process.

## 6. Open problems

1. The family quantum column: κ_q at the level tr(A_mA_n) for every pair — does closure
   track CRT centrality uniformly? 2. The cyclotomic-support lemma (the companion
   paper's opening). 3. The constants of the letter tower: the volume-per-letter
   c = 0.934102018057787980264187790656… (additivity of tower volumes holds to 10⁻²⁷ by
   rung 13; PSLQ finds no relation against the golden-sector Lobachevsky basis) and the
   chain's growth unit λ_chain = 1.57705744122666946… (certifiably non-algebraic to
   degree 8): both pinned, neither identified. 4. Why 15 twice: tr(A₁A₂) = 15 is also
   the conductor-type level of the pair's seam field ℚ(√−15); the naive family law
   fails at (1,3), and the correct statement, if one exists, is open. 5. The heredity
   of the chain's torsion primes (the observed divisibility table is irregular;
   rank-of-apparition machinery is the named tool).

## Appendix A: reproducibility

Every theorem and table maps to a script and a lock in the public repository:
Theorem A–C `chain_verify.py` (locks test_b471); Prop 2.1 `br_n_norm.py` (test_b469);
Theorem D–E′ `hierarchy_verify.py`, `rf1_towers.py`, `rf3_quantum.py` (test_b469/470);
§4.1–4.2 `kq_verify.py` (test_b472); Theorem G `cross_table.py` + the master table
(test_b474); the faces (test_b472); 17/17 locks re-verified at draft time. Chain-root
certificates: mod-p QNR witnesses, rungs 2–200. The SnapPy verifications (Gieseking
cover; the tower CS values; the witnesses' amphichirality) are quoted with version
pins in the repository logs.

## Appendix B: the corrections ledger ⟡

*[The method as story — the owner's telling; the draft supplies the facts.]* The results
above were reached through their own refutations, which we record because the
discipline is inseparable from the content: the commutator table was first computed
with the wrong values (tr[W₁,W₂] = 1, "the cost of quantization is 3") and corrected by
exact arithmetic within hours, the corrected table then yielding the closure theorem;
the root-witness count of §3.2 was first announced as 52 and is exactly 2 (the trace
test alone is insufficient — the divisibility condition of Theorem D removed fifty
spurious roots, and the surviving pair proved *more*, not less: the word criterion is
strictly weaker than amphichirality); an "accumulating field coincidence" (√−7) died
when the same field appeared in an unrelated control; a claimed correlation between
darkness and closure was refuted and replaced by its exact inverse, which then became
Theorem G's finite check. One orbit of the underlying dynamics, invisible to every
numerical method because its multiplier (914.7) makes its Newton basin and its weight
vanish together, was recovered by algebra auditing numerics — the general lesson, and
the reason every number in this paper carries a certificate.

---
*Acknowledgments, funding, and the repository URL: at packaging. MSC 11J06, 57K10,
20H10, 11F27.*
