# T3 and T4: the walk theorems and door A, read at source (audit room; data-free; 2026-10-29)

*For main, the final verifier. The tracked tree was read only. One result is new: § 1.5, the walk's exit law in closed
form. It is labelled as derived here, and it was checked three ways numerically. Main should verify it before any row
moves.*

*Seen first: `VERDICT topic-sweep /horocycl|shear|unipotent|translation of Re|Re tau|parabolic/ (full text): 185 of
1561 arcs on main match (NEGATIVE 47, OPEN 6, PROVED 131, RETRACTED 1); 23 register rows match (DECLINED 1, DONE 12,
LEAD 1, QUEUED 9)`. P-472 (door A) and P-473 (door B) are the register's rows for this work.*

## 0. The answers

### T4: the walk theorems

- **The claim is a theorem for the record's walk, and a stronger one than the record states.**
- **The closed form (derived here, § 1.5).** At every pull-back strength p ∈ [0, 1], the exit law is exactly
  - **ν_p = (1 − p)·M + p·F₊M**,
  - where M is Minkowski's measure on [0, ∞] and F(x) = −x is B1662's mirror.
- **What follows from it:**
  - The walk realises the move clock exactly, at every p.
  - Its exit law is singular to Lebesgue at every p.
  - The pull-back strength sets only the side, P(ξ > 0) = 1 − p exactly, and the speed. It does not set the shape.
  - At p = 0 the exit law is Minkowski's measure itself.
- **The published theorems give the singularity independently,** each under its own hypotheses (§ 1.2):
  - Gadre–Maher–Tiozzo (2015, 2017) for p ∈ (0, 1]. They need the support to generate the group as a semigroup, which
    fails at p = 0.
  - Deroin–Kleptsyn–Navas (2009) and Bénard (2022/2024) for every p.
  - Blachère–Haïssinsky–Mathieu (2011) at p = ½ only.
- **Scope:** i.i.d. letters with a finite first moment in the word metric. Walks with an infinite first word moment are
  not covered, and they can have exactly Lebesgue exit law (Furstenberg).
- **The row:** given GM5b's walk as B1662–B1663 model it, area is EXCLUDED and the move clock is FORCED. It is
  conditional on the owner's ruling that the walk is the programme's dynamics (P-473).

### T3: door A

- **Dani's classification, read at source.** On SL(2, ℝ)/SL(2, ℤ), every finite horocycle-invariant ergodic measure is
  either Haar or the uniform measure on a closed horocycle.
- **Nothing on record generates the continuous action τ → τ + t.** The record has only discrete steps:
  - T and S, as the frame's SL(2, ℤ) covariance: relabellings, not motions (B1724, B1733).
  - The unit shears L and R: GM2, and the records W34 keeps (B1675).
  - The geodesic flow, whose closed orbits are the threads (GENESIS § 4's arena reading; both of B1813's clocks).
- **The Re τ = ¼ column is an interpolation, not a symmetry.**
  - B1814's preregistration labels it CHOSEN by inheritance.
  - It is accurate because L's dependence on Re τ falls like e^(−2π Im τ) (measured here, § 2.3).
  - The frame's other outputs depend on Re τ.
- **So door A cannot fire on the present record.**
- **An added continuous shear would be the horocycle flow.** Together with the geodesic flow, it forces area by Dani's
  theorem. Alone, it does not.

## 1. T4: the walk theorems

### 1.1 What was read (accessed 2026-10-29; PDFs fetched to an isolated scratch folder)

| source | what I read |
|---|---|
| Gadre, Maher, Tiozzo, *Word length statistics for Teichmüller geodesics and singularity of harmonic measure*, Comment. Math. Helv. 92 (2017) 1–36; arXiv:1212.1481v3 | §1 in full (Theorem 1.1, Corollary 1.2, Theorems 1.4–1.5, §1.3 the SL(2, ℤ) case), §4.1, §5 opening and §5.4 |
| Gadre, Maher, Tiozzo, *Word length statistics and Lyapunov exponents for Fuchsian groups with cusps*, New York J. Math. 21 (2015) 511–531 (nyjm.albany.edu/j/2015/21-23) | §1 (Theorems 1.1–1.3 and the history paragraph), §4 opening (the hypotheses), references |
| Guivarc'h, Le Jan, *Asymptotic winding of the geodesic flow on modular surfaces and continuous fractions*, Ann. Sci. ÉNS 26 (1993) 23–50 (Numdam, asens.1666) | full text from the OCR layer: Theorems 2.1 and 2.3, §§3–4 and the references. I searched for any random-walk or harmonic-measure statement and found none |
| Guivarc'h, Le Jan, *Note rectificative*, Ann. Sci. ÉNS 29 (1996) 811–814 (Numdam, asens.1755) | full text |
| Guivarc'h, Le Jan, *Sur l'enroulement du flot géodésique*, C. R. Acad. Sci. Paris 311 (1990) 645–648 | **NOT READ.** Gallica blocks automated access. Known only through secondary accounts (§ 1.7) |
| Blachère, Haïssinsky, Mathieu, *Harmonic measures versus quasiconformal measures for hyperbolic groups*, Ann. Sci. ÉNS 44 (2011) 683–721 (Numdam, asens.2153) | §§1.6–1.7: Theorem 1.10 and its attribution |
| Deroin, Kleptsyn, Navas, *On the question of ergodicity for minimal group actions on the circle*, Mosc. Math. J. 9 (2009) 263–303; arXiv:0806.1974 | §1 (Theorems C and G, Conjecture 1.21, Corollary 1.22, Remark 1.23, the moment remark), §3 Question 3.3, §5.2 opening |
| Kaimanovich, Le Prince, *Matrix random products with singular harmonic measure*, Geom. Dedicata 150 (2011) 257–279; arXiv:0807.1015 | the introduction |
| Bénard, *Winding of geodesic rays chosen by a harmonic measure*, arXiv:2211.15232v3 (2024) | §1.1 (Corollary 1.3 and its history), the definitions of §1.2, §5.2 (the proof of Corollary 1.3) |
| Forghani, Kaimanovich, *Singularity of compound stationary measures*, arXiv:2503.09770v1 (2025) | introduction §7; §1.F, Remarks 1.20–1.22 (the Minkowski and Denjoy measures on ∂PSL(2, ℤ)) |
| Randecker, Tiozzo, *Cusp excursion in hyperbolic manifolds and singularity of harmonic measure*, J. Mod. Dyn. 17 (2021) 183–211; arXiv:1904.11581 | the introduction and Theorems 1–2 |
| Kosenko, IMRN 2021 (arXiv:1911.00801); Kosenko, Tiozzo, arXiv:2012.07417 | abstracts and introductions. **Both treat cocompact groups only and do not apply to SL(2, ℤ).** No later finitely-supported result specific to SL(2, ℤ) was found beyond Bénard's and Forghani–Kaimanovich's |

### 1.2 The theorems, exactly

| theorem | group | the step law μ | conclusion |
|---|---|---|---|
| **GMT 2017, Corollary 1.2** (= GMT 2015, Theorems 1.2 + 1.3) | a Fuchsian group of cofinite volume, not cocompact (a nonuniform lattice in SL(2, ℝ)) | finite first moment in the word metric, "whose support generates G as a semigroup" | ν ⊥ Lebesgue. The mechanism: the word-to-relative length ratio ρ is a finite constant ν-a.s. and infinite for Lebesgue-a.e. ray |
| **GMT 2017, Theorem 1.5** | the mapping class group | finite first word moment; the semigroup generated by the support is a non-elementary subgroup | ν ⊥ Lebesgue on PMF |
| **DKN 2009, Theorem C + Corollary 1.22** (Remark 1.23: applies to PSL(2, ℤ)) | PSL(2, ℤ) acting on ℝP¹ | finite first word moment; no measure invariant under all of supp μ; "either the support supp(m) generates G, or the semigroup generated by this support acts minimally" | the unique stationary measure is singular. Theorem C: the Lyapunov expansion exponent of PSL(2, ℤ) is 0 |
| **BHM 2011, Theorem 1.10** (attributed to Guivarc'h–Le Jan, "the last corollary of [the 1990 note]") | discrete Γ < PSL(2, ℝ) with non-compact, finite-volume quotient | "a symmetric law µ with finite support on Γ" | ν₁ ⊥ Lebesgue. BHM's own proof is for symmetric, finite support |
| **Bénard 2024, Corollary 1.3** | any finitely generated discrete Γ ⊆ PSL(2, ℝ) containing a parabolic | non-elementary ("the semigroup generated by its support contains two hyperbolic isometries" with disjoint fixed points); finite first word moment | ν is singular to the Patterson–Sullivan class, which is Lebesgue for a lattice. It removes GMT's semigroup assumption and the superexponential moment assumption of Gekhtman–Tiozzo |
| **Randecker–Tiozzo 2021, Theorems 1–2** | non-uniform lattices in Isom(ℍᴺ), N ≥ 2 (N = 2 is GMT 2015) | generating; finite k-th word moment, k > N − 1; finite exponential moment in the relative metric | ν ⊥ Lebesgue |
| **Guivarc'h–Le Jan 1993 + 1996** | finite-index normal subgroups Γ of PSL(2, ℤ) (torsion-free apart from three cases) | **no random walk.** Theorem 2.1 is about the geodesic flow under Liouville | the normalised winding (1/t)∫ω converges in law to a Cauchy law; cusp forms give a Gaussian. The 1996 note completes the proof of Theorem 2.1, saying "Lemma 4.2 is incorrect" and treating coding time against flow time |
| **The moment condition is sharp** (GMT 2015 §1; DKN §1; KLP; Randecker–Tiozzo) | any lattice in SL(2, ℝ) | Furstenberg's discretisation of Brownian motion: infinite support, finite first moment in the Riemannian metric, infinite first word moment | the exit law IS Lebesgue. GMT 2015: "the assumption of finite first moment is essential" |
| **Khinchin's theorem** (GMT 2017, eq. (2)) | — | — | for Lebesgue-a.e. x, (a₁ + ⋯ + aₙ)/n → ∞. Any law whose continued-fraction digits have an a.s. finite long-run mean is singular |

### 1.3 The record's walk, read from the code

- **B1662** (`frontier/B1662_…/verification/the_pull_back_acts.py`, `walk_A`, line 57):
  - X ← X·s with s uniform on {L, R, L⁻¹, R⁻¹}, i.i.d., multiplied on the right.
  - This is the case p = ½.
- **B1663** (`frontier/B1663_…/verification/the_pull_backs_strength.py`, `walk`, lines 75–82):
  - L and R each with probability (1 − p)/2; L⁻¹ and R⁻¹ each with probability p/2; i.i.d., right-multiplied;
    p ∈ {0, 0.1, …, 0.5}.
  - The limit is ξ = lim Xₙ(∞).
- **What the record adopts:** GENESIS GM5b adopts only the legality of inverse moves. It fixes no walk and no weights.
  The walk is B1662/B1663's model of the motion. B1663 § 3 says it is the picture's reading, firewalled.

### 1.4 The hypotheses checked, for every p

| hypothesis | p = 0 | 0 < p < 1 | p = ½ |
|---|---|---|---|
| finite support (so every moment is finite) | ✓ | ✓ | ✓ |
| i.i.d. (memoryless) | ✓ | ✓ | ✓ |
| the support generates SL(2, ℤ) as a group | ✓ (⟨L, R⟩ = SL(2, ℤ)) | ✓ | ✓ |
| the support generates SL(2, ℤ) as a semigroup (GMT) | **✗**: only the positive monoid | ✓ (closed under inverses) | ✓ |
| symmetric (BHM) | ✗ | ✗ | ✓ |
| non-elementary in Bénard's sense | ✓ (LR and L²R are hyperbolic with disjoint fixed points: φ, −1/φ and 1 ± √3) | ✓ | ✓ |
| no common invariant measure (DKN) | ✓ (L fixes only ∞, R only 0) | ✓ | ✓ |
| **which theorems apply** | DKN, Bénard, § 1.5; not GMT | GMT, DKN, Bénard, § 1.5 | all |

### 1.5 New: the exit law in closed form (derived here; main to verify)

**The claim.** For the step law μ_p = (1−p)/2·(δ_L + δ_R) + p/2·(δ_{L⁻¹} + δ_{R⁻¹}), at every p ∈ [0, 1]:

> **ν_p = (1 − p)·M + p·F₊M.**

- **M is the exit law of the positive walk.**
  - The infinite word L^{a₀}R^{a₁}L^{a₂}⋯ converges to [a₀; a₁, a₂, …], since L(x) = x + 1 and R(x) = x/(x + 1).
  - Uniform i.i.d. letters give a₀ + 1 and the later aᵢ i.i.d. Geometric(½) on {1, 2, …}.
  - On (0, 1), the normalised M is d?: the cylinder [0; a₁, …, aₙ] has mass 2^(−(a₁+⋯+aₙ)).
- **The cited identification.** Forghani–Kaimanovich, Remark 1.21: Minkowski's "Fragefunktion ? is the cumulative
  distribution function" of this law. GMT 2017 §1.3 describes the same digits for the dual-tree walk "neglecting
  backtracking".
- **F(x) = −x** is B1662's mirror (F4: F L F = L⁻¹ and F R F = R⁻¹).

**Proof 1: direct stationarity (elementary).**

1. **One step of the positive walk:** M = ½L₊M + ½R₊M. By the mirror, F₊M = ½L⁻¹₊F₊M + ½R⁻¹₊F₊M.
2. **Reduction to one identity.** With q = 1 − p,
   - μ_p ∗ ν_p − ν_p = qp·[½(L₊ + R₊)F₊M + ½(L⁻¹₊ + R⁻¹₊)M − M − F₊M].
   - So the claim at any one p ∈ (0, 1) is equivalent to the claim at all of them.
   - It is equivalent to the identity M + F₊M = ½(L₊ + R₊)F₊M + ½(L⁻¹₊ + R⁻¹₊)M.
3. **Splitting at 1.** From step 1, M|[1, ∞] = ½L₊M and M|[0, 1] = ½R₊M. So
   - ½(L⁻¹₊ + R⁻¹₊)M = ½M + ½[L⁻¹₊(M|[0,1]) + R⁻¹₊(M|[1,∞])].
   - The bracket lives on (−∞, 0]. The mirror image handles the positive half.
   - The identity reduces to F₊M = L⁻¹₊(M|[0,1]) + R⁻¹₊(M|[1,∞]).
4. **Applying F** turns it into two symmetries of Minkowski's measure:
   - **On [0, 1]:** FL⁻¹(x) = 1 − x, and 1 − R(y) = R(1/y). This is ?(1 − x) = 1 − ?(x).
   - **On [1, ∞]:** FR⁻¹(x) = x/(x − 1). With x = 1 + y it is y ↦ 1/y.
   - Both are the swap P (L ↔ R, P(y) = 1/y) acting on a uniform i.i.d. word, so both hold.
5. **Uniqueness.** supp μ_p generates SL(2, ℤ), which is non-compact and strongly irreducible. So the μ_p-stationary
   probability on ℝP¹ is unique and is the exit law (Furstenberg; the uniqueness clause as DKN §1 state it). ∎

**Proof 2: from the free product (independent).**

1. **The letters in PSL(2, ℤ) = ⟨a⟩ ∗ ⟨b⟩,** with a = S and b = ST:
   - L = ab, R = ab², L⁻¹ = b²a, R⁻¹ = ba (checked by matrix multiplication).
2. **The step law needs no labels.** On the Cayley graph it is "an a-edge, then a triangle-edge to either other vertex"
   with probability q, and "a triangle-edge, then an a-edge" with probability p.
   - So every automorphism of the unlabelled Cayley graph fixing e preserves the walk.
   - Hence the exit law is invariant under Forghani–Kaimanovich's group ℛ of "rotations".
3. **Their Remark 1.22:** the ℛ-invariant probabilities are exactly κ^{½, p′}, with i.i.d. uniform b/b² letters.
4. **The side weight.** Let p′ be the probability that the limit word begins with a.
   - The one-step equation is p′ = q(1 + p′)/2 + p·p′/2, so p′ = 1 − p.
   - Words beginning with a are the positive words W₁W₂⋯ (Wᵢ ∈ {L, R}), so ξ > 0.
   - Words beginning with b or b² land on ξ < 0, with law F₊M.

**Checks (numerical; scripts in the scratchpad, § 4).**

- **The digits.** I read 1 500 walks per p, at p ∈ {0, 0.25, 0.5}, with three seeds.
  - From each walk I took exactly 100 settled digits after the first two.
  - The frequencies of 1, 2, 3, 4 and ≥ 5 match 2^(−k).
  - χ² for single digits: 0.6–4.7 on 4 df. χ² for disjoint pairs: 3.0–14.9 on 8 df.
- **The side.** P(ξ > 0) = 0.753–0.771 at p = 0.25 (1 − p = 0.75) and 0.504–0.515 at p = ½.
- **The stationarity.** I drew 2 × 10⁵ samples from the claimed ν_p and computed
  E[φ(ξ) − Σ μ(s)φ(sξ)] for φ = cos kθ and sin kθ (θ = 2 arctan x, k = 1, 2, 3).
  - |z| ≤ 1.8 in all 18 cells.
  - **The control fails as it must:** with the side weight moved by 0.1, |z| reaches 123.
- **B1663's sealed T2** fits 1 − p:
  - P(ξ > 0) = 1.000, 0.900, 0.753, 0.713, 0.622, 0.531 at p = 0, 0.1, …, 0.5.
  - The largest deviation is 2.1 SE, at p = 0.2.
- **A method note (a length bias).**
  - Pooling all digits of walks stopped at a size cap over-weights small digits.
  - My first runs pooled this way. They gave a digit-1 frequency near 0.502 at every p, including p = 0, where the law is
    exactly Minkowski's.
  - A fixed number of digits per walk removes the bias.
  - B1663's post-seal frequencies (0.502 and 0.504 for digit 1) carry this small bias. No verdict changes.

**What it gives.**

1. **Singular at every p ∈ [0, 1].**
   - Minkowski's measure is singular: under M the digit mean tends to 2 a.s., while under Lebesgue it tends to ∞ a.e.
     (Khinchin).
   - Denjoy 1938 and Salem 1943 are the originals, as cited by Forghani–Kaimanovich; not read here.
   - This proof of door B uses none of Guivarc'h–Le Jan.
2. **The walk's measure is the move clock at every p, not merely "not area".**
   - The ray to ξ has i.i.d. Geometric(½) tail digits, so its long-time averages are those of the lifted Minkowski
     measure:
     - B1813's height law, P(Im τ > 3) ≈ 0.0346;
     - B1663's averaged defect, 0.517.
   - So B1663's T4(b) failure is exact in the limit. The averaged defect's a.s. limit is the same constant for every p;
     finite-length averages can differ only through the first digits.
   - B1813's referee check 5 is explained: the walk with inverses has the move clock's height marginal.
3. **B1663's empirical sentence becomes a theorem** for the side and the shape. "p sets which end and how fast, not the
   shape" now reads: P(ξ > 0) = 1 − p exactly, and the tail law does not depend on p. The speed was not examined here.
4. **The scope of the closed form:** i.i.d. letters with equal weights within each pair (L against R, and L⁻¹ against
   R⁻¹), B1663's own scope.
   - With unequal weights within a pair, the closed form fails: at p = 0 the law is a Denjoy measure (Forghani–
     Kaimanovich §1.F).
   - Singularity still holds by the theorems of § 1.2.

### 1.6 The conclusion, with its scope (the EXCLUDED row as the mathematics gives it)

- **THEOREM, for the record's walk** (B1662/B1663's step law, every p ∈ [0, 1]):
  - The exit law is (1 − p)·M + p·F₊M.
  - It is singular to Lebesgue.
  - For ν_p-a.e. endpoint, the geodesic ray's time averages are the move clock's, not hyperbolic area's.
  - In GMT's terms, the ray's word-length ratio is finite, where a Lebesgue-typical ray's is infinite.
- **The wider statement, from the literature:** every i.i.d. walk on SL(2, ℤ) with finite first word moment has an exit
  law singular to Lebesgue. The sources are:
  - GMT 2015/2017 if its support generates the group as a semigroup;
  - DKN 2009;
  - Bénard 2024 for every non-elementary law;
  - elementary laws, which have atomic exit laws or Lebesgue-null limit sets.
  The same holds on any nonuniform lattice (GMT) and on any finitely generated discrete group with a parabolic (Bénard).
- **What is NOT excluded:**
  - Walks with an infinite first word moment. Furstenberg's construction gives exactly Lebesgue, so "no walk can sample
    area" is false without the moment condition.
  - Letter processes that are not walks, unless their digit mean is a.s. finite (Khinchin). That does exclude every
    stationary ergodic letter process with a finite mean run length.
  - That the programme's dynamics is a walk at all. This is the owner's ruling (P-473); B1663 § 3 firewalled the walk as
    a reading.
- **The row's wording:** "Given GM5b's walk as B1662–B1663 model it, the move clock is FORCED (the exit law is
  Minkowski's at every pull-back strength) and hyperbolic area is EXCLUDED; the exclusion extends to every i.i.d. walk
  with finite first word moment; conditional on the walk being the dynamics."
- **At p = 0 the harmonic measure equals Minkowski's measure:** yes, exactly. Sources:
  - § 1.5's first bullet;
  - Forghani–Kaimanovich, Remark 1.21;
  - GMT 2017 §1.3;
  - Kaimanovich–Le Prince's history paragraph: continued fractions with independent digits as harmonic measures of
    walks on SL(2, ℤ), via Chatterji 1966 and Furstenberg 1963 (not read).

### 1.7 Corrections the reading found

- **(a) The Guivarc'h–Le Jan citation.** B1663 § 0 cites Guivarc'h–Le Jan (1990, 1993, with its 1996 erratum) for the
  exit law's singularity.
  - The 1993 paper and the 1996 note contain no random-walk statement. The 1993 introduction says "These results were
    announced in a note [GL], together with other results".
  - The random-walk corollary is in the 1990 note, which was not read.
  - Secondary accounts of its scope differ:
    - Γ(2): GMT 2015 and 2017, Bénard;
    - SL(2, ℤ) with finite support: Randecker–Tiozzo;
    - non-cocompact lattices under a moment condition: KLP, DKN;
    - symmetric, finitely supported laws: BHM's Theorem 1.10.
  - The row should rest on GMT, DKN, BHM, Bénard and § 1.5, all read.
- **(b) The GMT citation.** B1663's "Gadre, Maher and Tiozzo (2015)" is the New York J. Math. paper. The CMH paper (2017;
  arXiv 2012) states the same Fuchsian result as Corollary 1.2.
  - Both need the support to generate the group as a semigroup.
  - That holds at p > 0 and fails at p = 0, where DKN, Bénard or § 1.5 cover it.
- **(c) P-473's sentence.** "No finitely supported random walk on SL(2, ℤ) has an absolutely continuous exit law" is true.
  Its support is (a) and (b), not Guivarc'h–Le Jan alone. The same applies to the briefing's § 3.2 sentence.
- **(d) B1663's post-seal digit frequencies** carry the small length bias of § 1.5's method note. No verdict changes.
- **(e) The Minkowski identification.** B1663 § 0's "the Minkowski question-mark measure as the exit law of the walk with
  L and R alone" is correct. B1813's "B1663 found it as the walk's" is correct at every p, by § 1.5.

## 2. T3: door A, horocycle invariance

### 2.1 Dani's classification, read at source

**Where I read it.** Dani, *Invariant measures of horospherical flows on noncompact homogeneous spaces*, Invent. Math. 47
(1978) 101–138. I read the scanned original (GDZ, PPN356556735_0047, LOG_0013): the introduction and Theorem A
(pp. 101–102), and the end of §10 (pp. 136–137).

**Theorem A, in my words.**
- **Hypotheses:**
  - T is a reductive Lie group whose non-compact simple factors have ℝ-rank 1;
  - U is a maximal horospherical subgroup;
  - Γ is a lattice in T;
  - π is a finite U-invariant ergodic measure on T/Γ.
- **Conclusion:** there are a closed subgroup L and t ∈ T such that
  - (i) LtΓ is closed and π(T/Γ − LtΓ/Γ) = 0;
  - (ii) L ⊇ U, tΓt⁻¹ ∩ L is a lattice in L, and π is "the finite L-invariant measure on LtΓ/Γ".
- **SL(2, ℤ) in Dani's own words.** His introduction names SL(2, ℤ) in SL(2, ℝ): it "constitutes the simplest example of
  the above phenomenon", namely that the horospherical flow is not uniquely ergodic.

**The modular case (my specialisation; standard).** Take T = SL(2, ℝ), U = N = {u_s} and Γ = SL(2, ℤ).
- **Which L can occur.** A closed L ⊇ N that contains a lattice is unimodular. The closed subgroups containing N are:
  - N (up to ±I);
  - the Borel subgroup AN, which is not unimodular and so contains no lattice;
  - SL(2, ℝ).
- **So π is one of two kinds:**
  - Haar;
  - or the N-invariant probability on a closed N-orbit, a periodic horocycle.
- **The same statement for every cofinite Fuchsian group with a cusp:** Strömbergsson, Duke Math. J. 123 (2004) 507–547,
  §3. Either the normalised volume, or "the support of ω is a closed orbit h of the flow".
- **Invariant measures that are not ergodic** are c·Haar plus a mixture of closed-horocycle measures. A measure that gives
  the closed horocycles zero mass is Haar (Strömbergsson, Proposition 3.1).
- **On the modular surface** the closed horocycles are the images of the lines Im τ = y with upward vectors, one for each
  y > 0, of length 1/y.

**Not read.** Dani–Smillie, Duke Math. J. 51 (1984) 185–194, was not reachable as full text or abstract. Nothing below
uses it. Sarnak 1981 (CPAM 34) is known only through Strömbergsson §1: closed horocycles equidistribute to area as
y → 0.

**Two consequences used below.**
1. **Geodesic and horocycle invariance together force Haar.** The geodesic flow carries the closed horocycle at height y
   to the one at height e^(±t)·y, and no probability on heights is invariant under that. Both of B1813's clocks are
   geodesic-flow-invariant. The move clock is not Haar, so by this consequence it is not horocycle-invariant.
2. **Horocycle invariance alone does not force Haar.** It admits any law of heights spread over closed horocycles.

### 2.2 What "τ → τ + t" is on the modular surface

- **On ℍ, τ ↦ τ + t is the left action of u_t.**
  - It does not normalise SL(2, ℤ).
  - On the modular surface it is defined only for t ∈ ℤ, where it is the identity: T is a relabelling.
- **The horocycle flow acts on the other side:** g ↦ g·u_t on T¹(Γ\ℍ) = Γ\SL(2, ℝ).
  - On the upward vector at τ = x + iy it reads τ ↦ τ + t·Im τ: a translation of Re τ at fixed Im τ, at unit hyperbolic
    speed.
  - It closes after t = 1/Im τ, where it meets T.
  - On flat tori (unimodular lattices) it is the continuous shear (x, y) ↦ (x + ty, y) of the fibre's flat structure,
    with the marking held fixed.
- **The record's unit shears and the horocycle flow therefore act on opposite sides.**
  - L, R and T ∈ SL(2, ℤ) relabel the marking and fix every point of the moduli space. The flow moves the fibre.
  - The parabolic elements of Γ are exactly the periods of the closed horocycles: Γ·g·u_{1/y} = Γ·T·g for g = a_y.
  - In the same way, the threads are the periods of the closed geodesics.
  - The record reads the threads as closed geodesics (GENESIS § 4). It never reads the shears as closed horocycles.
- **A continuous version of GM2's shear is illegal on the records.** [[1, t], [0, 1]] does not preserve GM1's ℤ² when
  t ∉ ℤ.
- **A continuous version of the frame's T-covariance breaks the lines.** It would carry a line (α, b) to (α, b − tα)
  (B1733's convention). That leaves (ℚ/ℤ)², the torsion lines, for t ∉ ℤ, so it destroys the frame's discrete line data.

### 2.3 The sweep: what the record has

| item | what it has | continuous τ → τ + t? |
|---|---|---|
| GENESIS GM1–GM5 | integer records ℤ² (GM1); GM2 "Unit shears: elementary updates are L and R"; inverse moves (GM5b); the arena reading SL(2, ℝ)/SL(2, ℤ), whose geodesic flow's closed orbits are the threads (§ 4: "a reading recorded … nothing derived from it"); physical time NOT DERIVED (§ 3) | **no.** The updates are discrete. The only flow named is the geodesic flow, as a reading |
| W34 / B1675 | "a shear is unipotent and fixes one line": L or R acting on H¹(F₂) at the quaternion point; the measurer's record sits at an end | **no:** integer unipotents |
| B1630 | S = RL⁻¹R fixes i, order 8 on T | **no** |
| B1676 | the ticks (threads) on the parity lines | **no** |
| B1667 | the **fibre's** horocycles (the maximal embedded one; the one of length 2) fix L(τ). Re τ = 0.25 is a read-out column | **no:** fibre geometry, and a discrete choice between two horocycles (P-402) |
| B1712–B1740 (and B1741, B1814) | L read at Im τ from B1667's Re τ = ¼ column; grids at discrete Re τ; T-covariance checked numerically | **no.** B1814's preregistration calls the interpolation "CHOSEN by inheritance". **Measured here from B1667's `the_canonical_cusp.json`:** at fixed Im τ, L_max varies over Re τ by 0.49 % (Im τ = 1), 0.10 % (1.25), 0.022 % (1.5) and ≤ 10⁻⁵ from Im τ = 2. That is the e^(−2π Im τ) size of the non-constant Fourier modes: the column keeps L's constant term, its average over the closed horocycle. It approximates a read-out; it is not a symmetry of the measure |
| B1724, B1733, B1736 | S and S̃ are SL(2, ℤ)-covariant, S* only under Γ⁰(2); T acts on lines by (α, b) ↦ (α, b − α) | **no:** discrete relabelling |
| the frame's outputs | the Re τ = 0 zero family (P-292; B1716); the CP lines Re τ ∈ {0, ½}; J generic (B1713); THE_WEAVE: the strong-CP phase 12 arg η(τ) → π Re τ at large Im τ | **the frame is not Re τ-invariant;** Re τ carries an observable |
| THE_WEAVE.md, "shear" | only W34's | **no** |
| the SM seat's dossier (its NOTE.md for the weave dossier of 2026-10-07, on its branch at 3889806ad; 34 matching lines) | "shear" is L or R (W2, W6; the measurer "at the cusp of the modulus, where the shear L is parabolic"); "horocycle" is the fibre's (W75, W100, W145–W170: L_max against L₂ as a discrete choice); W75's w ↦ w + 1 is the fibre puncture's parabolic generator | **no** |
| B1813, B1814 | both clocks are geodesic-flow-invariant measures (the threads' arclength; Minkowski lifted); height marginals only | **no** |
| the other sweep hits from B1600 on (56 arcs) | "parabolic" as puncture holonomy or character-variety level; Nielsen shears (B1672); "parabolic T gives no point" (B1804) | **no** |

### 2.4 The verdict

- **NOT GENERATED.** Nothing on record generates the continuous action τ → τ + t, as a dynamics or as a symmetry the
  measure must respect.
- **What the record has instead:**
  - its discrete steps: T and S as relabellings, L and R as updates and kept records;
  - the geodesic flow, through its threads.
- **Door A cannot fire on the present record.**
- **Its premise is not met** ("the frame's τ-independence along Re τ … is such an action"):
  1. The column is an approximation of one read-out, CHOSEN.
  2. Invariance of a read-out is not invariance of a measure. Dani's theorem needs the measure invariant, and a read-out
     that is constant along Re τ leaves the Re τ-law unobserved rather than fixing it.
  3. The frame's CP outputs depend on Re τ.

### 2.5 What an added continuous shear would be, and whether anything would justify it

- **What it would be.** The horocycle flow on T¹ of the modular surface.
  - Where a line of order N is carried, it is the flow on Γ₁(N)\SL(2, ℝ).
  - Concretely, it is the continuous shear of the fibre's flat structure. On upward vectors, τ ↦ τ + t·Im τ.
- **What it would force.**
  - **With the geodesic flow,** which both of B1813's clocks already respect: Haar (§ 2.1, consequence 1). That is
    hyperbolic area: the geometric clock FORCED and the move clock EXCLUDED.
  - **Without the geodesic flow:** only "Haar plus mixtures of closed horocycles". Area follows only if the closed
    horocycles carry no mass.
- **What could justify it.** None of the candidates is on record.
  - **(a) Teichmüller dynamics.**
    - The record's geodesic flow is the diagonal part of SL(2, ℝ) acting on flat fibres. Taking the whole action, or its
      Borel part AN, as the motion would bring the horocycle flow in.
    - Choosing the whole group rather than its diagonal part is an added rule, CHOSEN.
    - It would decide the clock by fiat: the only SL(2, ℝ)-invariant probability is Haar.
  - **(b) Interpolating GM2's unit shears.** That is illegal on the integer records (GM1). It is legal only as a motion of
    the fibre's geometry, and GENESIS does not generate that motion: τ is a modulus, not a record.
  - **(c) "No preference in Re τ."** A uniform Re τ at each height gives the closed-horocycle measures, not area. It
    reaches area only with geodesic invariance added, or in the limit of long horocycles (Sarnak).
  - **(d) Physics: Re τ as an axion.**
    - THE_WEAVE's strong-CP phase tends to π Re τ. An axion has a perturbative continuous shift symmetry, broken to ℤ by
      effects of order e^(−2π Im τ).
    - That shift is the left action, not a flow on the moduli space. Near the cusp it agrees with the horocycle flow on
      upward vectors, and the record's column interpolation is exactly its approximation.
    - It is not on record as a symmetry of the measure, and the frame's CP outputs break it.
- **So door A is a CHOSEN door.** If chosen, it gives the geometric clock at once, as P-472 says, because B1813's clocks
  already respect the geodesic flow. The record supplies no reason to choose it.

### 2.6 Doors A and B at the boundary (a reading)

- **The horocycle flow moves endpoints by translation.** The flow based at the cusp translates the other endpoint: on
  upward vectors at height y, x ↦ x + t·y.
- **Lebesgue is the only translation-invariant class.**
- **T2 computed door A at the boundary.** Minkowski's measure is quasi-invariant under T but singular under the
  non-integer translation x ↦ x + 1/3. So the move clock's boundary law is not even quasi-invariant under one non-integer
  horocycle step.
- **Door B says the walk's exit law is exactly that law (§ 1.5).**
- **One fact, read from two sides:** area is the horocycle-invariant measure, and the walk is not horocycle-invariant.

## 3. Rows main may file (proposals; main decides)

- **P-473 → an EXCLUDED/FORCED row** with § 1.6's wording and scope. It is conditional on the owner's ruling that the
  walk is the dynamics.
- **The exit-law identity, ν_p = (1 − p)M + pF₊M,** is law-grade. Once verified on main it needs its own LAW_MAP row
  (WORKING_RULES §10).
- **P-472 → NOT GENERATED.** Door A is CHOSEN. If added together with the geodesic flow, it FORCES area (Dani). The
  record's column is an approximation, CHOSEN, not a symmetry.
- **Corrections (a)–(d) of § 1.7.** The briefing's § 3.2 attribution to Guivarc'h–Le Jan should be replaced as in (a).
- **TERMINOLOGY.**
  - "Shear" names two things: the discrete unit shear (GM2, an element of SL(2, ℤ)) and the continuous horocycle flow.
  - "Horocycle" names the fibre's (B1667) and the moduli space's.

## 4. Reproducibility

The scratch scripts live in the session scratchpad, which a restart can wipe, so the decisive one is reproduced below:
- `(the reader's scratch folder)/digit_iid_fixedK.py`,
  with its outputs `fk_seed{101,202,303}.txt`;
- `…/scratchpad/stationarity_check.py`, with its output `stationarity_check_out.txt`;
- the length-bias runs `digit_iid_seed*.txt` and `d20_seed*.txt`.

The stationarity check (Python, standard library; run as `python3 -I stationarity_check.py 200000`):

```python
import math, random
L=(1,1,0,1); R=(1,0,1,1); Li=(1,-1,0,1); Ri=(1,0,-1,1)
def sample_M(rng, depth=48):             # Minkowski's measure on [0, inf]: [G-1; G, G, ...]
    g=[]
    while len(g)<depth:
        k=1
        while rng.random()<0.5: k+=1
        g.append(k)
    d=[g[0]-1]+g[1:]; x=float(d[-1])
    for a in reversed(d[:-1]): x = a+1.0/x if x!=0 else math.inf
    return x
def mob(m,x):
    a,b,c,d=m
    if math.isinf(x): return a/c if c else math.inf
    den=c*x+d; return (a*x+b)/den if den!=0 else math.inf
th=lambda x: math.pi if math.isinf(x) else 2*math.atan(x)
def run(p, side_pos, n, seed):           # z-scores of E[phi(xi) - sum_s mu(s) phi(s.xi)]
    rng=random.Random(seed); st=[(L,(1-p)/2),(R,(1-p)/2),(Li,p/2),(Ri,p/2)]; acc={}
    for _ in range(n):
        x=sample_M(rng); x = x if rng.random()<side_pos else -x
        t0=th(x); ts=[(th(mob(m,x)),w) for m,w in st]
        for k in (1,2,3):
            for f,fn in (('c',math.cos),('s',math.sin)):
                dd=fn(k*t0)-sum(w*fn(k*t) for t,w in ts); s=acc.setdefault(f+str(k),[0,0]); s[0]+=dd; s[1]+=dd*dd
    return {key:round((s1/n)/math.sqrt(max(s2/n-(s1/n)**2,0)/n),2) for key,(s1,s2) in acc.items()}
for p in (0.0,0.25,0.5):
    print(p, run(p,1-p,200000,11), run(p,min(1,1-p+0.1) if p>0 else 0.9,200000,12))  # claim, then control
```

Output: under the claimed law, |z| ≤ 1.8 in all 18 cells. Under the control, |z| = 123, 113 and 86 on sin θ, and about
15 on sin 3θ.
- The block above, run as printed, reproduces the scratchpad output digit for digit.
- At n = 6 × 10⁴ the same code gives |z| ≤ 2.4 under the claim.
  - The same pattern appears at p = 0, where stationarity is exact by construction.
  - All three p share seed 11, and so the same Minkowski draws, so it is one shared fluctuation.
  - The control still fails at that n, with |z| = 49–68.

0 of 19.
