# B1435 PREREGISTRATION — THE INTERACTION CENSUS: which of E₆'s cubic couplings survive as actual relative triple products on the generation-shaped backgrounds of the generated state space?

**Sealed 2026-10-01, before the instrument is run on any generation-shaped background. Seat: cc (main). Occasion: the
owner's direction of 2026-09-30 — "we must account for the whole allowed architecture, its relations and
interactions" — and the one calculation two seats named as next and neither ran: the web seat's corrective audit
(its ledger item K23, "the repaired relative interaction calculation: NOT RUN") and the SM lane's fence that no
coupling of the index's zero modes has been computed.**

## 0. The quantifier (P0)

For every generation-shaped background of B1434's census — 30 levels of 19 signed word states, 8 800 backgrounds —
and every unordered pair A, B of its firing doublet sectors (the six of B1374: Q, u^c, e^c, d^c, L, ν^c): the value
of the relative triple product of the two matter classes with the class of the spin-0 sector the pair couples to.
The scope sentence names no manifold.

## 1. What is computed

- **Modules.** A background has extension character ℓ and sector modules V_s = R ⊗ β_s, R = [[ℓ, c], [0, 1]]
  (B1432's conventions, `cover_census.module`). If its count is +1 the zero mode of sector s is the one interior
  class of H¹(M; V_s); if −1, of H¹(M; V_s*).
- **The functional.** E₆'s invariant tensors (the bracket on the 78, the action 78 × 27 → 27, the cubic on the 27)
  restricted to two SL(2)_β-doublet sectors and one spin-0 sector are a Clebsch–Gordan constant times the unique
  SL(2)-invariant, T(a, b, w) = (a₁b₂ − a₂b₁)·w. Invariance forces the spin-0 character:
  η = (α_A β_B)^(−sign). Its mode is the class of H¹(M; η).
- **Allowed.** A pair is *allowed* when minus its charge (6Y, 3γ) is the charge of a spin-0 sector of 78 ⊕ 27 ⊕ 27̄
  (the table `SPIN0` in the instrument). Fifteen of the 21 pairs are: Q·u^c (78's H_u), Q·Q and u^c·e^c (78's D),
  Q·d^c and e^c·L (27̄'s H_d), u^c·d^c and Q·L (27̄'s D̄), d^c·d^c, d^c·L, L·L (the 27's 10), Q·ν^c, u^c·ν^c, e^c·ν^c
  (the 27̄'s 10̄), d^c·ν^c (27's D), L·ν^c (27's H_u). That the Clebsch–Gordan constant of each is non-zero is **not**
  verified here; "allowed" means charge-allowed.
- **The number.** Y(A, B) = ⟨(a, e) ∪ b ∪ h, [M, ∂M]⟩ through T, on an explicit relative fundamental chain (C, z)
  of the normalised bar complex: z = [t|λ] − [λ|t], C = prism(σ) + filling(Φ_*σ − σ), σ the fibre's relative 2-chain
  [x|y] + [xy|x⁻¹] + [xyx⁻¹|y⁻¹] − [x|x⁻¹] − [y|y⁻¹]. The identity ∂C = z is asserted as an identity of integer
  chains on every level before any module is evaluated. Docstring of `verification/relcup.py` (sha-256 below).
- **What is invariant.** Each class is a line. A single Y is defined up to a non-zero scale, so **its vanishing is
  an invariant and its value is not.** The census records, per background and pair: h¹(η), whether η is trivial on
  the fibre, whether Y ≠ 0, whether the Higgs class has h(t) ≠ 0 — each at three primes ≡ 1 mod N above 3 000,
  the same primes as B1434.
- **Asserted in the run (not predictions):** every firing class is interior (a relative lift exists);
  Y(A, B) = Y(B, A) at every prime; the three primes agree. A level where the primes disagree is reported as
  discarded and re-run at further primes.

## 2. What has been seen before the seal (disclosed)

- **Controls on objects outside the population** (records `controls_run.txt`, `control_pullback_run.txt`,
  `control_plumbing_run.txt`):
  - ∂C = z on ten monodromies and on the identity;
  - the product F × S¹ with trivial coefficients: x*∪y*∪t* = +1, y*∪x*∪t* = −1, x*∪x*∪t* = 0, x*∪y*∪x* = 0;
  - the bundle with monodromy −I and sign coefficients: ±1, antisymmetric;
  - a unipotent rank-two module over the product: the value is independent of the relative lift and of coboundaries
    in all three slots on 40 of 40 interior pairs (all non-zero), and **depends** on the lift on 20 of 20 pairs
    whose second class is not interior (the bite: the invariance is not vacuous);
  - the two-term chain [x|y] − [y|x] has boundary [yx] − [xy] ≠ −[λ] (the web seat's correction C02, reproduced).
- **M₂ = m206, the root's double cover: its eight firing modules, which are not generation-shaped backgrounds (M₂
  has none).** Self-pair couplings at Higgs characters non-trivial on the fibre: all eight non-zero; pulled back to
  M₄ the value doubles exactly (8 of 8); coboundary-invariant (8 of 8). A synthetic six-fold copy of one module:
  21 pairs non-zero at three primes, symmetric. **So a non-zero secondary product at a fibre-non-trivial Higgs
  character has been seen once, off the population.**
- **Read, not computed here:** the web seat's withdrawn probe (its P08: up non-zero, down and lepton zero, on its
  M₆ triplet in its own frame, computed on the chain its own audit rejected); the SM lane's B1362/B1367 (deck
  symmetric textures; the doublet–triplet pincer for point-localised matter).
- **No coupling has been computed on any generation-shaped background. The characters of the backgrounds have not
  been inspected for which Higgs characters are trivial.**

## 3. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| P1 | The up-type coupling Y(Q, u^c) is non-zero on **every** background of the population. | 40% |
| P2 | On every background, Y(Q, d^c) and Y(e^c, L) vanish together or not at all (they share one Higgs line). | 60% |
| P3 | **Some** background has Y(Q, u^c) ≠ 0 with Y(Q, d^c) = 0 = Y(e^c, L) — the pattern the web seat withdrew. | 35% |
| P4 | On every level, all backgrounds of the level have the same zero pattern on the allowed pairs. | 45% |
| P5 | For allowed pairs whose Higgs character is non-trivial on the fibre, Y ≠ 0 exactly when the Higgs class has h(t) ≠ 0, on every background. (The Higgs class alone decides.) | 35% |
| P6 | Some background has Y(Q, u^c) ≠ 0 with all four triplet-mediated couplings Q·Q, u^c·e^c, u^c·d^c, Q·L zero. | 15% |
| P7 | On the 24 own-level backgrounds (the two states that fire at k = 1), Y(Q, u^c) ≠ 0 on all. | 40% |
| P8 | Every background has at least one non-zero allowed coupling. | 80% |

## 4. What each outcome would mean (written before the data)

- **P1 YES with P3 YES on all** would be a structural hierarchy: the up-type coupling exists at the level of the
  topological cubic and the down and lepton couplings do not. **P1 NO** would name the backgrounds on which no
  up-type coupling exists; those cannot carry a Standard-Model spectrum with masses from this cubic.
- **P4 NO** would make the zero pattern a datum that separates backgrounds the index does not separate.
- **P5 YES** would reduce the interaction census to one number per Higgs character; **P5 NO** makes the matter
  classes matter.
- **P6 YES** would be a doublet–triplet split at the level of couplings, where B1367 found none for point matter.
- **P8 NO** would exhibit backgrounds whose zero modes do not interact through E₆'s cubics at all.
- None of the outcomes is a Yukawa value, a mass or a mixing. The fence is B1432's and B1434's, plus this arc's:
  main's class index on reducible non-split modules; non-semisimple backgrounds; index is not a generation count;
  the frame is carried to every state as an instrument; a coupling's vanishing is computed, its value is a
  normalisation; the Clebsch–Gordan constants are not checked; which spin-0 sector is a physical Higgs is not
  asked.

## 5. Not in this arc

Couplings across the members of a deck orbit (they are not E₆ tensors of one background); the scale-invariant
monomials of the non-zero couplings; exact arithmetic; fillings; non-cyclic covers.

## 6. Hashes at seal

See `ARTIFACT_HASHES.txt`.
