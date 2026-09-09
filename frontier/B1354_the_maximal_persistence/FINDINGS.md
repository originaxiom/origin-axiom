# B1354 — THE MAXIMAL PERSISTENCE: formal branches tangent to the V₁₀ direction that keep all three cusp-fixed vectors of ρ₀ exist — the second-order class must drop V₄, V₈, V₁₆ and carry a definite V₆ component tied to V₁₄, after which every higher order is affine and free — exactly modulo two primes, through order 8 (Toeplitz kernel dimensions 3m); B1352's registered residue answered in the affirmative — and the answer closes the window rather than opening it: along every such branch the traces move at first order but the self-duality defects vanish through order 8. The fixed-vector branch is formally self-dual: on the object, cusp-fixed weights and self-duality come together along V₁₀ at the formal level exactly as at B1352's Sp(8) points. No carrier of a net count; 0 of 19.

**Verdict: PROVED** (exact statements modulo p = 67108819 and 67108837: the obstruction-class tower and its Gröbner bases, the climb, the trace series; no numerics). Depends on B1350 (the exact block classes, the formal integration), B1352 (the fixed-vector locus, the first-order table, the loss orders on the constructed branches; §6 registered this question), B1268 (the augmented Newton and the bound). Verification: `verification/` (records `persistence_tower_run.txt`, `continuation_run_p1.txt`, `continuation_run_p2.txt`, `trace_series_run_p1.txt`, `trace_series_run_p2.txt`). Lock: `tests/test_b1354_the_maximal_persistence.py`.

## 0. The question

B1352 found that along every formal V₁₀ branch it constructed (greedy, random within the keeping classes, random) the three
cusp-fixed vectors of ρ₀ are lost at order 4 (order 2 generically), and registered the residue: the freedom at each order is
the eight classes of H¹(M; e₆), and a *tuned* branch might keep a vector longer. This arc decides it.

## 1. The obstruction-class tower (`persistence_tower.py`)

A formal branch ρ_t = exp(X(t))ρ₀, X = tY + t²X₂ + t³X₃ + …, is determined order by order by the relator up to Z¹ at each
order: X_k = part(−R_k^{low}) + Σᵢ λ^{(k)}ᵢ Zᵢ, with the coboundaries dropped (gauge) and λ^{(k)} ∈ F⁸ the class added at
order k; the relator at order k + 1 constrains λ^{(k)} affinely through the polarisation B(Y, Zᵢ) — **2 of the 8 directions
at every order** (the rank of the polarisation columns modulo im d¹), 6 free, the direction Y itself (reparametrisation)
among them. A cusp-fixed vector v₀ persists through order m iff the obstruction classes o₁, …, o_m vanish,
o_m = Q_T(Σ_{j=1}^m T_j v_{m−j}) ∈ coker T₀ (30-dimensional), T(t) = [μ(t) − I; λ(t) − I]. The newest class enters o_m only
through T_m v₀ ∋ Σᵢ λ^{(m)}ᵢ z(Zᵢ)v₀, whose class vanishes exactly for the classes that keep v₀ to first order (B1352 stage C:
V₂, V₆, V₁₀, V₁₀#2, V₁₄ keep every vector; V₈ keeps e₁, e₂; V₄ keeps e₂; V₁₆ none). So the question is a polynomial
system: o₂ affine in λ⁽²⁾; o₃ affine in (λ⁽²⁾, λ⁽³⁾); o₄ quadratic in λ⁽²⁾ and affine in λ⁽³⁾, λ⁽⁴⁾; the relator defects
affine in the newest λ. The system (1408 equations in the 24 unknowns λ⁽²⁾, λ⁽³⁾, λ⁽⁴⁾) is built exactly by polynomial
interpolation of the pipeline (quadratic model, verified at random points), the affine unknowns are eliminated, and the
remaining equations in λ⁽²⁾ are decided by a Gröbner basis over GF(p).

**Result (both primes, all four directions of the V₁₀ plane, targets e₀, e₁, e₂ and a random vector):** the Gröbner basis is
never {1}; it is **linear**, with four elements:
λ⁽²⁾_{V₄} = 0, λ⁽²⁾_{V₈} = 0, λ⁽²⁾_{V₁₆} = 0, λ⁽²⁾_{V₆} = c·λ⁽²⁾_{V₁₄} + d
(c, d specific constants; V₂, V₁₀, V₁₀#2, V₁₄ free) — the same family for every target and every direction. The κ-terms
(the freedom of adding lower fixed vectors to the series when another vector is lost earlier: needed for e₁, e₂ since V₈,
V₄ are allowed for them) only enlarge the family (Pass C: seven-element linear bases). So: **there are formal branches
tangent to V₁₀ along which all three cusp-fixed vectors persist through order 4** — the greedy branch is not one of them
because its second-order V₆ component is wrong.

## 2. The climb (`continuation.py`)

Order by order: at order k the unknowns are the free parameters of λ^{(k−2)}'s family (symbolic), λ^{(k−1)} and λ^{(k)}
(affine); the equations are the relator defects and the obstruction classes of all three vectors at orders k − 1 and k; the
quadratic model is exact; the affine unknowns are eliminated; the rest is decided by Gröbner. **From order 5 on there are no
quadratic terms at all and the systems are consistent with three free pure directions carried at each order**: the climb
continues through order 8 modulo both primes, and the branch found has Toeplitz kernel dimensions
kd(1..9) = [3, 6, 9, 12, 15, 18, 21, 24, 27] — all three cusp-fixed vectors persist through order 8 (B1352 stage D's
instrument). Its second-order class has V₄ = V₈ = V₁₆ = 0 and non-zero V₆, V₁₄ (prime 1: V₆ = 50723718, V₁₄ = 56733388; prime
2: V₆ = 3584654, V₁₄ = 56733388, in F_p).

## 3. What kind of branch it is (`trace_series.py`)

Along a formal branch the traces tr ρ_t(w) are power series in t. For eight words (a, b, ab, a²b, [a, b], ba², the longitude,
ab⁻¹), modulo both primes, through order 8:

| branch | Toeplitz kd(1..9) | traces move first at order | self-duality defects tr ρ_t(w) − tr ρ_t(w⁻¹) non-zero at orders |
|---|---|---|---|
| greedy (`obstruction_higher.py`; the Newton curve's model) | 3, 6, 9, 12, 12, 12, 12, 12, 12 | 1 | **4, 5, 6, 7, 8** (none for the palindromic words [a,b], ab⁻¹) |
| tuned (all three cusp-fixed vectors kept) | 3, 6, 9, 12, 15, 18, 21, 24, 27 | 1 | **none through order 8** |

Both are genuine curves of characters (the traces move at first order; B1350's first-order trace-flatness was of the
*defects*, not of the traces). The greedy branch leaves the self-dual locus at order 4 — the exact form of B1352's t⁴ law
for the trace defects — and loses the fixed vectors at the same order. The tuned branch keeps the fixed vectors and stays
self-dual: it is a formal branch of the self-dual locus with three cusp-fixed weights — the formal version of B1352's Sp(8)
points, with the θ-odd tangent V₁₀ realised at the representation level by the tuned second-order term (at the reducible
point ρ₀ a θ-odd class and a θ-even class can differ by a direction the character map does not see).

## 4. What it means

B1352 §6 asked whether a tuned formal branch tangent to V₁₀ keeps a cusp-fixed vector beyond order 4. It does — and every
such branch is formally self-dual. So the two conditions a net count needs on the cusped object (a cusp-fixed weight and a
non-self-dual representation) exclude each other along V₁₀ at every order reached: where the fixed vectors persist the
character stays self-dual (27 ≅ 27̄, N = 0), and where the character leaves the self-dual locus (order 4) the fixed vectors
are lost (order 4). L204's last formal residue is closed with the same mechanism as its numerical half: **fixed vectors and
self-duality are one condition along V₁₀.** The θ-odd frame on the object carries no count, formally or numerically.

## 5. Caveats

1. "Formal branch through order 8" is exact modulo two primes; the reduction from ℚ(ω) is the repository's two-prime rule
   (a rank modulo p is at most the exact rank; a consistent system over ℚ(ω) reduces to a consistent one modulo p for all but
   finitely many p; the converse, that a solution modulo p lifts, is what the numerical realisation supplies).
2. The climb fixes the lower orders at random points of their families and keeps only the newest two orders symbolic; it
   exhibits one branch (and a large family), it does not classify all of them.
3. A numerical realisation of the tuned branch (a 600-bit climb over ℂ and the augmented Newton) was begun and abandoned: the pseudo-inverse of the cusp-fixed matrix at ρ₀ is precision-hostile at 600 bits (its 25th singular direction sits at 10⁻⁷⁰ of the scale, resolved as zero only at 2000 bits — B1350's lesson again), and after the exact answer of §3 the realisation adds nothing the physics needs.
4. "Formally self-dual through order 8" is the statement; it is not a proof that the tuned branches lie in the Sp(8) family to all orders.

## 6. Files

`verification/persistence_tower.py` (the tower; Pass A, the completeness check, Pass C), `continuation.py` (the climb),
`trace_series.py` (the traces and self-duality defects along both branches), records `*_run*.txt`.
