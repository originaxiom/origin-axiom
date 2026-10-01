# B1512 PREREGISTRATION — THE SELF-COINCIDENT ORBITS: Ballas' family under m004's symmetries. The fibre's hyperelliptic involution fixes it, the dual family is the family at 1/q, and the amphichiral map sends q to 1/q. So the twisted polynomials of M₅'s and M₆'s self-coincident orbits are rational and rigidly paired. Where are their real exceptional points, and does case (b) fire there?

**Sealed 2026-10-01, before any twisted polynomial of the twelve self-coincident orbits of M₅ and M₆ is computed (exactly or over
GF(p)). Seat: cc (the SM-derivation branch). Occasion: the owner's "go" on the recommendation after main's S31, which named B1511's
lead 1 (the 32 self-coincident pairs) and lead 3 (the reality symmetry).**

## 0. The question

B1511 carried B1509's rank-five extension W₁ = [[V, c·L], [0, L]] (V = ν ⊗ ρ_q, L = ν⁻⁴) to m004's cyclic covers M₁–M₆. Its case (b)
(L non-trivial on the fibre, trivial on the cusp) counts I(W₁) = 1 − r1 ∈ {0, +1}. It needs h¹(ν ⊗ ρ_q) ≥ 1 and h¹(ν⁵ ⊗ ρ_q) ≥ 1 at
the same q.
- On M₄'s two 3-torsion orbits the coincidence is automatic: ν⁵ lies in ν's deck orbit. Case (b) fired there at q = φ^{±4}, λ = 1,
  every member +1.
- On M₅'s four eigenline orbits (every λ ∈ μ₄) and M₆'s eight order-8 orbits (λ = ±1) the coincidence is automatic too. B1511's GF(p)
  gcd test could not separate them: 32 pairs UNRESOLVED.
- B1511 found, post-run, that every twisted polynomial is real (P_ν = P_{ν⁻¹} over GF(p)). Its lead 3 asked for the reason.

This arc asks:
- **Q1 (the symmetries).** Why is P_ν = P_{ν⁻¹}, and what else do m004's symmetries force on the twisted polynomials? *(Decided at
  design time: Lemmas I, G, D, E and A, §3.)*
- **Q2 (the 32 pairs).** On M₅ and M₆, where are the positive real exceptional points q ≠ 1 of the self-coincident orbits, what is
  the fibre there, and does case (b) count there? *(Open: §6.2.)*

## 1. Setting and notation

As in B1511 §1, whose library is reused by import (`frontier/B1511_the_projective_tower/verification/tower_lib.py`,
`tower_census.py`).
- π = ⟨m, n | R = mnMNmNMnmN⟩, with fibre F = ⟨x = nm⁻¹, y = mnm⁻²⟩ = [π, π] and φ(g) = mgm⁻¹, Φ = [[0, −1], [1, 3]].
- π_n = F ⋊ ⟨z = mⁿ⟩, Tₙ = coker(Φⁿ − 1). Characters are ν = (ν_F, λ) with ν_F = (a, b) mod N. The deck acts by (a, b) ↦ (b, 3b − a).
- P_ν(q, s) is the characteristic polynomial of the level-n fibre monodromy on H¹(F; ν_F ⊗ ρ_q). It is monic of degree 4 in s and
  depends on ν_F only.
- Main's index I = n(V) − n(V*) on the Reidemeister–Schreier presentation of Mₙ, over GF(p) through B1374's index_lib.
- **The twelve orbits** (B1511 C10, recomputed in K3):
  - M₅ (T₅ = 𝔽₁₁²): orbits 12, 15, 18 and 19, the characters on the two Φ-eigenlines.
  - M₆ (T₆ = ℤ/8 × ℤ/40): orbits 1, 3, 31, 32, 33, 34, 47 and 53, of characters of order 8.
  - **The 32 pairs:** M₅'s four orbits × λ ∈ {1, i, −1, −i}, and M₆'s eight orbits × λ = ±1. B1511 resolved M₆'s λ = ±i pairs: no
    common root.

## 2. Computed before the seal (disclosed)

`verification/controls.py --record` → `verification/controls_run.txt` (K1–K10, 70 s), and `verification/census.py --dry --record` →
`verification/census_dry_run_level4.txt`. **No control computes any twisted polynomial, root or count of the twelve orbits.**
- **K1 — the involution ι** (Lemma I):
  - words in the free group: ι², ι(R), ι(x), ι(y), ι(m), ι(longitude);
  - the exact intertwiner C(q), unique up to scale, with det C = 16q² and C² = 4q.
- **K2 — ν∘ι = (ν_F⁻¹, λ)** on every character, levels 1–6.
- **K3 — the classes.**
  - The self-coincident orbits of levels 4–6, with their Galois classes: each is closed under ν ↦ ν^k (k a unit) within the deck orbit
    and its inverse.
  - M₅ has two classes, {12, 19} and {15, 18}. M₆ has four, {1, 3}, {31, 53}, {32, 34} and {33, 47}.
  - The 32 pairs match B1511's record one for one.
- **K4 — the reconstruction reproduces banked polynomials exactly:**
  - the untwisted levels 1–6, against Res_r(Q(q, r), s − rⁿ);
  - s961's O₂ (= Q(q³, s)), O_A and O_B (B1511 Part A);
  - M₄'s two 3-torsion classes (B1511 Part C1).
  Each needs 3–4 primes near 2³¹ and agrees at 2 fresh primes, in 2–5 s.
- **K5 — the root-and-count driver on B1511's banked case-(b) point.** M₄, both 3-torsion orbits, λ = 1, q² − 7q + 1. At every member,
  every root and three primes (6 prime–root pairs per orbit): I(W₁) = +1, I(W₂) = −1, I(Λ²W₁) = 0, data (0, 1, 1, 0), fibre
  (1, 1, 1, 1), rank B = 4. This is B1511's row.
- **K6 — the numeric fibre data at the real root itself** (60 digits, singular values):
  - (1, 1, 1, 1) at q = φ^{±4} for three M₄ members;
  - B1509's Jordan block (1, 2, 2, 2) at q² − 34q + 1, λ = −1.
  The zero singular values are below 10⁻⁵⁰ and the others above 0.07.
- **K7 — B1511's banked GF(p) degrees for the 32 pairs, read back.**
  - Every M₅ pair has deg(q⁸⁰P(q, λ)) = 85 and q-multiplicity 75. That is Laurent range [−5, 5]. The (q − 1)-multiplicity is 2 at
    λ = 1 and 0 otherwise.
  - Every M₆ pair has 102 and 90, that is [−6, 6]. The (q − 1)-multiplicity at λ = 1 is 2 for classes {1, 3} and {31, 53}, and 4 for
    {32, 34} and {33, 47}.
  - At λ = ±i, B1511 resolved all 16 of M₆'s self-coincident pairs (no common root besides 0 and 1).
  - For M₅ at λ = ±i, gcd(P(q, i), P(q, −i)) was the whole polynomial at all three primes.
- **K8 — the duality and the strong inversion** (Lemmas D and E):
  - the exact intertwiners D (ρ_q^{−T} → ρ_{1/q}, det −16q(q² + q + 1)) and E (ρ_q → ρ_{1/q}∘ε, det 16q⁴), each unique up to scale;
  - ε is an involutive automorphism;
  - Lemma D's identity holds on all 13 banked polynomials.
- **K9 — Lemma E on characters.**
  - P_{(b,a)} = P_{(a,b)} over GF(p) at all 32n + 1 interpolation points, for every character of T₂, T₃ and T₄ (2, 6 and 21 pairs,
    none differing).
  - The swap (a, b) ↦ (b, a) exchanges M₅'s two classes and fixes each of M₆'s four.
- **K10 — the amphichiral map α** (Lemma A):
  - α is an automorphism (the semidirect check in the free group, ψ invertible). Its fibre action M = [[2, 1], [−1, −1]] commutes
    with Φ and has M² = Φ⁻¹ and det −1, so α reverses orientation.
  - The exact intertwiner A (ρ_q → ρ_{1/q}∘α) has det −16q³.
  - The table of the four symmetries (ι, ε, α and the audit lane's θ), with θ = ιφ⁻²ε on H₁(F).
  - Lemma A's consequence holds on all six banked relations: s961's O_A → Ō_B, Ō_A → O_B and O₂ → O₂, and M₄'s class 1 → class 10.
  - α fixes each of M₅'s two classes. On M₆ it exchanges {1, 3} ↔ {31, 53} and {32, 34} ↔ {33, 47}.
- **The dry run.** The census code at level 4 (M₄'s banked classes) reproduces B1511 Part C1 in 46 s:
  - the polynomials and the banked degrees;
  - λ = 1: q − 1, q² − 7q + 1 and q² + q + 1; λ = −1: an octic with no positive root; λ = ±i: nothing;
  - the counts above, at 6 prime–root pairs × 4 members per class;
  - Lemma D's identity and the closure of the roots under q ↦ 1/q;
  - D8, D9 and D10.

**Disclosures.**
- **How the symmetries were found.**
  - ι's intertwiner was found by solving Cρ_q(g) = ρ_q(ιg)C over ℚ(q).
  - D and ε came from solving the four candidate intertwiner systems (targets ρ_q, ρ_{1/q} and their duals) at q = 3/7 and 5/2, then
    exactly (K8).
  - A short-word search for automorphisms of π (images of length ≤ 7) found only orientation-preserving ones: fibre det +1 with the
    fibration kept, or det −1 with it reversed.
  - α was then built from the fibre: Out(F₂) = GL₂(ℤ), and the centralizer of Φ contains M (det −1).
- **A design slip, caught before the seal.** A draft of this document called ε "the amphichiral map". ε acts by det −1 on H₁(F) and
  also reverses the fibration, so it **preserves** orientation: it is a strong inversion, of the audit lane's θ type (θ = ιφ⁻²ε on
  H₁(F)). The orientation-reversing symmetry is α. The draft was corrected before sealing. It will be logged in ERROR_LEDGER at
  banking.
- **The banked degrees (K7) were read before the seal.** They fix the Laurent ranges ([−5, 5] and [−6, 6]).
- **One instrument repair before the seal:** a JSON key-type error in the controls' record (integer and string keys mixed), fixed by
  naming the keys `level_n`.

## 3. Proved now (design time)

The four symmetries used:

| map | images of m, n | on H₁(F) | on π/F | orientation | family |
|---|---|---|---|---|---|
| ι (hyperelliptic) | mnm⁻¹, mn⁻¹mnm⁻¹ | −1 | + | kept | ρ_q∘ι ≅ ρ_q |
| ε (strong inversion) | mn⁻¹m⁻¹, mnm⁻¹n⁻¹m⁻¹ | swap, det −1 | − | kept | ρ_q ≅ ρ_{1/q}∘ε |
| α (amphichiral) | mnm⁻¹, nmn⁻¹m⁻¹n²m⁻¹ | [[2, 1], [−1, −1]], det −1 | + | reversed | ρ_q ≅ ρ_{1/q}∘α |
| duality | — | — | — | — | ρ_q^{−T} ≅ ρ_{1/q} |

**Lemma I (the hyperelliptic involution fixes Ballas' family).** Let ι: m ↦ mnm⁻¹, n ↦ mn⁻¹mnm⁻¹.
- (i) ι(R) is a cyclic conjugate of R⁻¹ in the free group, and ι² = id on m and n. So ι is an involutive automorphism of π (K1).
- (ii) In the free group, ι(x) = x⁻¹, ι(y) = y⁻¹ and ι(m) = ym. So ι preserves F and each π_n: ι(mⁿ) = (ym)ⁿ = y·φ(y)⋯φⁿ⁻¹(y)·mⁿ.
- (iii) ν∘ι = (ν_F⁻¹, λ). The fibre part of ι(z) has class (1 + Φ + ⋯ + Φⁿ⁻¹)e_y. That lies in im(Φⁿ − 1) =
  (1 + ⋯ + Φⁿ⁻¹)(Φ − 1)ℤ², because Φ − 1 ∈ GL₂(ℤ). Checked on every character for n ≤ 6 (K2).
- (iv) Let C(q) = [[q, q, −2q, 3q], [q + 4, q, −2q, q], [q + 6, q, −2q − 6, 2q + 9], [4, 0, −4, 6]]. Then Cρ_q(g)C⁻¹ = ρ_q(ιg) for
  g = m, n, hence for all g. det C = 16q² and C² = 4q.

*The transport principle* (used for every lemma below). Let β be an automorphism of π, with β(F) = F and β(z) ∈ F·z^σ (σ = ±1).
Let M be a π_n-module. Pulling back by β identifies H¹(F; M) with H¹(F; M∘β). The action of z on the second matches that of β(z) on
the first, which acts as z^σ does, since F acts trivially on its own cohomology. So **the polynomial of M∘β is that of M, with
s ↦ 1/s when σ = −1.**

*Consequence (reality).* (ν ⊗ ρ_q)∘ι ≅ (ν∘ι) ⊗ ρ_q, with σ = +1, so **P_{ν_F⁻¹}(q, s) = P_{ν_F}(q, s)** on every level, with the same
h^i. ρ_q is real, so every twisted polynomial has real coefficients. This proves B1511's post-run (c) and answers its lead 3.

**Lemma G (Galois).** For a unit k mod N, σ_k: ζ_N ↦ ζ_N^k sends S_ν to S_{ν^k} entrywise, since ρ_q is defined over ℚ(q). So
σ_k(P_ν) = P_{ν^k}.
- If every ν^k lies in the deck orbit of ν or of ν⁻¹, then deck invariance (B1511 Theorem B) and Lemma I make P_ν ∈ ℚ[q^{±1}, s].
- This holds for all twelve orbits (K3): one rational polynomial per class, 2 classes on M₅ and 4 on M₆.

**Lemma D (the dual family is the family at 1/q).** Let D(q) = [[0, 0, 2, 2], [0, −4(q + 1), −2(q − 1), 2], [2q, 2(q − 1), −(q + 1), 0],
[2q, 2q, 0, 0]]. Then Dρ_q(g)^{−T}D⁻¹ = ρ_{1/q}(g) for g = m, n, and det D = −16q(q² + q + 1) ≠ 0 for q > 0 (K8).
- *P_ν(q, 0) = 1.* The one-step determinant is det S_ν = (ν(y)/ν(x))⁴, since det A₁ = det A₂ = 1. Around a level the product is
  ν((1 + ⋯ + Φⁿ⁻¹)(e_y − e_x))⁴ = 1, by (iii) above.
- *Consequence 1.* **P_ν(1/q, s) = s⁴P_ν(q, 1/s).**
  - The fibre is a once-punctured torus Σ whose boundary is ℓ. V = ν ⊗ ρ_q has no invariant vector on ℓ: its eigenvalues are q, q, q,
    q⁻³, ν(ℓ) = 1 and q ≠ 1. So H*(∂Σ; V) = H*(∂Σ; V*) = 0, and H¹(Σ, ∂Σ; V*) = H¹(Σ; V*).
  - Poincaré–Lefschetz duality pairs H¹(Σ; V) with H¹(Σ, ∂Σ; V*), invariantly under the monodromy. So the polynomial of V* is the
    reciprocal of that of V.
  - V* = ν⁻¹ ⊗ ρ_q* ≅ ν⁻¹ ⊗ ρ_{1/q}. With Lemma I this gives the identity for q ≠ 1, and it is polynomial in q.
  - This is the reciprocity of twisted Alexander polynomials for self-dual representations (§5.2), with the dual sitting at 1/q.
- *Consequence 2.* If P_ν(q₀, λ) = 0 at a real q₀ > 0, then P_ν(1/q₀, λ) = 0, by Consequence 1 at s = λ and reality. **The positive
  real exceptional set at each λ is closed under q ↦ 1/q.**
- *Consequence 3 (on counts).* For the background (ν⁻¹, 1/q) and the dual class, the module read for W₂ through its dual,
  [[V′*, c′L′⁻¹], [0, L′⁻¹]], is W₁(ν, q, c) itself. Here V′* = ν ⊗ ρ_{1/q}* ≅ V and L′⁻¹ = ν⁻⁴ = L. **So I(W₂)(ν⁻¹, 1/q₀) =
  −I(W₁)(ν, q₀)**, class by class (D8).
- *Consequence 4.* P_ν is palindromic in s iff P_ν(1/q, s) = P_ν(q, s).

**Lemma E (the strong inversion).** Let ε: m ↦ mn⁻¹m⁻¹, n ↦ mnm⁻¹n⁻¹m⁻¹.
- ε(R) is a cyclic conjugate of R and ε² = id. In the free group ε(x) = y, ε(y) = x and ε(m) = x⁻¹m⁻¹, so σ = −1. ε sends the longitude
  to a conjugate of its inverse. On H₁(F) it has det −1 and it reverses the fibration, so it preserves orientation (K8, K10).
- The audit lane's generator inversion θ: m ↦ m⁻¹, n ↦ n⁻¹ satisfies θ = ιφ⁻²ε on H₁(F) (K10). Since Out(F₂) = GL₂(ℤ), ε is θ up to
  ι, the deck and an inner automorphism.
- An explicit E(q) with det E = 16q⁴ gives Eρ_q(g)E⁻¹ = ρ_{1/q}(εg). This is the audit lane's F14 (ρ_q∘θ ≅ ρ_q^{−T}) read through
  Lemma D.
- *Consequence.* **P_{(b,a)} = P_{(a,b)}** for every character of every Tₙ.
  - By transport with σ = −1, the polynomial of (ν∘ε) ⊗ ρ_q ≅ (ν ⊗ ρ_{1/q})∘ε is the reciprocal of P_ν(1/q, ·). By Lemma D that is
    P_ν(q, ·). And ν_F∘ε = (b, a).
  - Checked on levels 2–4 (K9).
  - On M₅ the swap exchanges the classes {12, 19} and {15, 18}. So **M₅'s four self-coincident orbits share one polynomial.**

**Lemma A (amphichirality).** Let ψ: x ↦ xy⁻¹x, y ↦ xy⁻¹, with inverse x ↦ y⁻¹x, y ↦ y⁻²x. In the free group ψφ(g) = y·φψ(g)·y⁻¹ for
g = x, y. So α(g) = ψ(g) on F and α(m) = ym define an automorphism of π = F ⋊_φ ⟨m⟩. In the letters m and n, α(m) = mnm⁻¹ and
α(n) = nmn⁻¹m⁻¹n²m⁻¹.
- Its fibre action M = [[2, 1], [−1, −1]] commutes with Φ, with M² = Φ⁻¹ and det −1, and σ = +1. So α reverses orientation: it is
  the figure-eight's amphichirality, a square root of the inverse monodromy.
- An explicit A(q) with det A = −16q³ gives Aρ_q(g)A⁻¹ = ρ_{1/q}(αg) (K10).
- *Consequence 1.* **P_{ν∘α}(q, s) = P_ν(1/q, s)**, by transport with σ = +1. Here ν_F∘α = (2a − b, a − b).
- *Consequence 2.* α fixes each of M₅'s two classes (K10). So **M₅'s polynomial is invariant under q ↦ 1/q, hence palindromic in s**
  (Lemma D, Consequence 4).
- *Consequence 3.* On M₆, α exchanges {1, 3} ↔ {31, 53} and {32, 34} ↔ {33, 47}. So P_{31,53}(q, s) = P_{1,3}(1/q, s) and
  P_{33,47}(q, s) = P_{32,34}(1/q, s). With Lemma D, α-paired classes have the same positive real exceptional sets.
- *Consequence 4 (on counts).* Main's index is invariant under any automorphism carrying the peripheral subgroup to a conjugate. By
  Mostow–Prasad, α is induced by an isometry, which preserves the one cusp. So **the count of ν∘α at q equals the count of ν at 1/q**,
  for W₁ and W₂ alike (D10).
- The same lemma explains B1511's pairings, at banked data (K10):
  - s961's O_A ↔ Ō_B ("as O_A") and O₂ fixed, so O₂ is palindromic;
  - M₄'s class 10, which is class 1 at 1/q.

**What the lemmas leave open.**
- Whether M₅'s single polynomial, and M₆'s two pairs, have positive real roots q ≠ 1 at the sealed λ's.
- At those roots: whether the fibre root is simple, and whether x ∪ c ≠ 0 (B1511 Theorem A(v)).

The run computes these.

## 4. BANKED IDENTITY:

Before any new number is read, the sealed run reproduces B1511's banked case-(b) row:
- the (0, 5) class of M₄ reconstructed equals B1511 Part C1's exact P(q, s);
- at the first prime–root pair of q² − 7q + 1 (p = 1021, q ≡ 355), I(W₁) = +1, I(W₂) = −1 and I(Λ²W₁) = 0.

The run stops if either fails.

The controls (§2) have already reproduced the following through this arc's instrument:
- B1509's Q at every level 1–6;
- B1511's five s961 polynomials and M₄'s two classes;
- B1511's case-(b) counts at all 12 prime–root–orbit points;
- B1509's Jordan block numerically.

Every index reading asserts the annihilator identity and the B1297 identity (B1511's counter).

## 5. PRIOR ART:

### 5.1 The repository

A read-only sweep covered main (d88c220e), this branch (7f03e853) and the audit lane (audit/physical-bridge-2026-09-05 at 472a9595).
- **The fibre's −I as a symmetry, with ρ_geo:**
  - main's B1297 (FINDINGS.md:136–146): "P: a ↦ a⁻¹, b ↦ a³b … P = −1 on the Alexander module, and on the torsion of every cyclic cover
    C_n". There ρ_geo∘P ≅ ±ρ_geo by Mostow, and ψ∘P = ψ⁻¹, for main's index on Sym²ρ_geo ⊗ ψ;
  - main's B1298 naming caveat (FINDINGS.md:31–33; HINT_LEDGER.md:719): B347/B353's "hyperelliptic" map is the strong inversion;
  - main's B1299 (V ≅ τ*V* on covers, SL(3));
  - main's B1434/B1438 (ι as a monodromy letter);
  - this branch's B1280 (τ: a ↦ a⁻¹, b ↦ b⁻¹ pairs V with τ*V*, SL(3)), B1381 (−I as an alternative monodromy) and B1279 (rank one
    on Y₉).
  **None uses Ballas' ρ_q.**
- **ρ_q under a symmetry: the audit lane's F14** (received_r47/F14_FINDINGS.txt:33–51). θ: m ↦ m⁻¹, n ↦ n⁻¹ with ρ(g)^{−T}J = Jρ(θg)
  and det J = −q(q² + q + 1)³/[16(q + 1)⁴], on m004 only. Its scope: "No claim about all finite covers or all their characters is
  made" (:161–163). Also R47/R48 (CANONICAL_DUALITY: "NOT … an all-representation/all-cover theorem").
  - **Lemma E is F14's θ**, up to ι and the deck (θ = ιφ⁻²ε on H₁(F)), read through Lemma D. It is credited to F14.
  - **Not stated on any ref:** ρ_q∘ι ≅ ρ_q (Lemma I), ρ_q* ≅ ρ_{1/q} (Lemma D), the amphichiral α with ρ_q∘α ≅ ρ_{1/q} (Lemma A), and
    their consequences for the twisted polynomials and counts on covers.
- **Reality of the twisted polynomials:**
  - B1511's post-run (c), observed and not proved (its lead 3);
  - analogues for other objects: main's B1297 (Galois self-duality), B1438 (a rank-one slope is real), B425/B581 (integer
    coefficients for Sym^{2m}ρ_geo).
- **Multi-modular reconstruction:** B425's geometric_torsion.py (CRT and rational reconstruction for Sym^{2m}ρ_geo) and B666 cell 9.
  Never for ρ_q or P_ν.
- **M₅'s eigenline and M₆'s order-8 characters:**
  - rank one on the closed covers (B1301, B1278, B1303);
  - the rank-two Standard-Model census (B1506, B1375; main's B1432/B1434/B1438; the audit lane's R69);
  - in the ν ⊗ ρ_q case-(b) setting, only B1511.
- **The 32 pairs:** resolved on no ref (B1511 §8 lead 1).

*Novelty, as far as this sweep reaches:*
- Lemmas I, D and A with their intertwiners, and their consequences for the tower;
- Lemma E's identification of M₅'s classes;
- every computation in §6.

### 5.2 The literature

- **The family itself.** S. Ballas, "Finite volume properly convex deformations of the figure-eight knot", arXiv:1403.3314.
- **Projective duality.** The dual of a properly convex projective structure is properly convex, with holonomy ρ^{−T} (Vinberg's
  duality). That the dual of Ballas' structure at q is Ballas' structure at 1/q is therefore expected. I found it stated nowhere;
  Lemma D proves it by an explicit intertwiner.
- **Symmetries of the figure-eight.** Its isometry group is the dihedral group of order 8, with orientation-reversing elements
  (amphichirality). ι, ε and α are such isometries read on π (Mostow–Prasad). That Ballas' family is carried to itself, with
  q ↦ 1/q for the fibration-reversing or orientation-reversing ones, is what Lemmas I, E and A prove.
- **Reciprocity of twisted Alexander polynomials** for representations conjugate to their duals:
  - P. Kirk and C. Livingston, "Twisted Alexander invariants, Reidemeister torsion, and Casson–Gordon invariants", Topology 38 (1999);
  - J. Hillman, D. Silver and S. Williams, "On reciprocality of twisted Alexander invariants", AGT 10 (2010) 1017, arXiv:0905.2574.
  Lemma D's Consequence 1 is this reciprocity, with the dual at 1/q.
- **The fibre formula.** For a fibred manifold, the twisted Alexander polynomial is the characteristic polynomial of the monodromy on
  the fibre's twisted cohomology (B1511 §5.2).

## 6. What the sealed run reads

### 6.1 Decided at design time (computed as checks; a failure refutes a step above)

- **D1 (Lemmas I, G).** For each class:
  - the reconstruction stabilises and agrees at two fresh primes;
  - every member of both of the class's orbits has the same polynomial mod p at a further prime;
  - the polynomial mod p does not depend on the choice of the root of unity.
- **D2 (Lemma D).** P(q, 0) = 1 and P(1/q, s) = s⁴P(q, 1/s) for every class. Every positive real exceptional set is closed under
  q ↦ 1/q.
- **D3 (Lemma E).** M₅'s two classes have one polynomial.
- **D4.** B1511's banked GF(p) degrees (K7) are reproduced exactly for every pair.
- **D5.** M₆ at λ = ±i: no positive real root other than 1, B1511's resolution reproduced exactly.
- **D6.** At every point read:
  - rank B = 4, so H⁰(F) = 0;
  - the numeric fibre dimensions at the real root equal the GF(p) ones;
  - h¹(L) = 1 and h¹(V_ν) = h¹(V_{ν⁵}) ≥ 1;
  - every count lies in Theorem A(v)'s range, W₁ ∈ {0, +1} and W₂ ∈ {0, −1}, with both identities;
  - I(Λ²W) = 0.
- **D7.** At each point, every member of the class (both orbits) gives the same counts at every prime–root pair.
  - Reason: dimensions are Galois-invariant. Every pair of a root mod p and a character of the class is a Galois conjugate of the pair
    of the real root and some member. Lemma I and Mostow–Prasad make the counts ι-invariant.
  - The exception is a GF(p) rank drop.
- **D8 (Lemma D, Consequence 3).** The W₂ values at the reciprocal factor with λ⁻¹ are the negatives of the W₁ values at the factor
  with λ.
- **D9 (Lemma A).** M₅'s polynomial is palindromic in s and invariant under q ↦ 1/q. On M₆, P_{α(C)}(q, s) = P_C(1/q, s) for each
  class C.
- **D10 (Lemma A, Consequence 4).** The W₁ and W₂ values of class α(C) at the reciprocal factor equal those of C at the factor, at the
  same λ.

### 6.2 Sealed predictions (open)

Priors are mine at the seal.
- **P1 — M₅'s polynomial is B1509's Q at q⁵: P = Q(q⁵, s)** (~25%). This is the pattern of s961's O₂, where P = Q(q³, s). It is
  consistent with K7 and D9. No mechanism is known (B1511 lead 2).
- **P2 — M₅ has a positive real exceptional point q ≠ 1 at some λ ∈ μ₄** (~90%).
- **P3 — M₆ has one at λ = ±1 for some class** (~85%).
- **P4 — case (b) fires on M₅** (~65%): at some real exceptional point every member counts I(W₁) = +1. That is orbits of five, five
  10̄′ per orbit (N(10′) = −I).
- **P5 — case (b) fires on M₆** (~65%), in orbits of six.
- **P6 — every real exceptional point among the 32 pairs is a simple fibre root**, kernel dimensions (1, 1, 1, 1) (~55%).
- **P7 — at every simple real exceptional point, every member counts I(W₁) = +1** (~70%). Read as not applicable if there is none.

## 7. The instrument (after the seal)

`verification/census.py --record` → `verification/census_run.txt` and `census_log.txt`. The library is `verification/selfco_lib.py`,
which imports B1511's.
- **Part 0.** The banked identity (§4).
- **Part A.** The lemmas re-checked inside the run (K1, K2, K8, K10), the classes (K3), and the class maps under α.
- **Part B.** For each class:
  - P(q, s) over ℚ, reconstructed from the first member of its first orbit. It uses primes p ≡ 1 mod lcm(N, 4) above 2³¹,
    Chinese remaindering and rational reconstruction. It is accepted after two consecutive unchanged reconstructions and checked at
    two fresh primes.
  - D1's member and root-of-unity checks at a further prime.
  - Its symmetries, equality with Q(qⁿ, s), D2's identity, the relations between the classes of the level (D3), D9 and D4.
- **Part C.** For each class and λ ∈ μ₄:
  - the real exceptional polynomial: P(q, λ) for λ = ±1, and gcd(Re, Im) for λ = ±i;
  - its factors over ℚ, and their positive real roots other than 1 (exact isolation by sympy, real-root count cross-checked with
    arb);
  - the closure under q ↦ 1/q.
- **Part D.** At each factor with such roots:
  - the numeric fibre data at every positive root for every member of the class (60 digits);
  - over GF(p) at the three smallest primes p > 1000 with p ≡ 1 mod lcm(N, 4) at which the factor is squarefree of full degree with a
    root, at every root, for every member of both orbits: the fibre data (rank B, dim ker(S − λ)ʲ on H¹) and B1511's case-(b) counts
    (h¹ of L, V_ν, V_η and V_η*; I(W₁), I(Λ²W₁), I(W₂) and I(Λ²W₂) for every basis class and c1 + c2).
- **Part E.** The 32 pairs' table, D8, D10, and the M₆ λ = ±i check (D5).

## 8. Reading rules, and what this arc will and will not claim

- **Reading rules.**
  - A count at a real exceptional point is read when every prime–root pair at the three primes and every member of the class agree.
    By D7 that common value is the count at the real point for every member.
  - A disagreement at one prime is reported as a GF(p) rank drop. A disagreement at all three primes is reported as a genuine
    difference, with the values (B1374's convention). The numeric fibre data then decide the fibre side.
  - "Fires" means I(W₁) ≠ 0 for some class at some positive real q ≠ 1.
  - P7 reads only simple points (numeric kernel dimensions (1, 1, 1, 1)).
- **Will claim:**
  - Lemmas I, G, D, E and A as proved, with their consequences;
  - the polynomials of the six classes, exactly;
  - the real exceptional points and the counts, with their precision stated: exact roots, numeric fibre data, GF(p) counts;
  - the completed per-level table of B1511 Part D.
- **Will not claim:**
  - a selection of q, of the level or of an orbit;
  - a 5̄′ (B1511 Theorem A(vi) is unchanged: Λ²W counts 0 everywhere);
  - three: orbits of five and six give gcd(n, k) = 5 and 6 per orbit, and Theorem E is unchanged;
  - that an orbit is several generations of one vacuum (B1506's fence);
  - an end condition beyond main's interior index;
  - any physics beyond the SU(5)′ dictionary's count.
  - **I-26 stays UNEARNED; 0 of 19** unless a result here earns otherwise, which none of P1–P7 can.
