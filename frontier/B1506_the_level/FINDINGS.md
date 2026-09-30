# B1506 — THE LEVEL: one background has one count on every level. B1378's M₆ triplet is the orbit of the root's whole deck: it lives on s961, the root's only 3-fold cover, as the deck orbit of one generation-shaped background that does not lift to SL(2)_β × ℂ*², and it is one object on the root. s961 carries 48 such backgrounds in 16 orbits of three, and on M₆ these are the only root-deck orbits of three among 2 160 generation-shaped backgrounds (the rest come in sixes). One versus three is the root versus its unique 3-fold cover.

**Date:** 2026-09-30 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's "lets do 1 first" (sL-5, the number
question: is a count taken on a cover or on its quotient?) · **Status:**
- PROVED: T1–T7 (§2), proved at seal. Every design-time decision (D1–D8) came out as proved (§3).
- SEALED AND RUN: the complete Standard-Model-frame census of M₁…M₆ (§3–§4). Seal `PREREGISTRATION.md` (sha256 `664f8192…`,
  SEAL_LEDGER), committed at 58e3f28f before the instrument existed. One result was seen before the seal, the seed's orbit of three.
  It is disclosed there and in §1. Predictions: **P1–P8 all YES.**
- One defect in the instrument's own checking code, found in the first run's log before any prediction was read and fixed; the whole
  instrument was rerun (§8, ERROR_LEDGER E52 instance).

**Fence:** main's B1297 class index on B1374's reducible non-split doublet modules, as in B1374–B1378; index ≠ generation count; the
backgrounds are non-semisimple (Corlette–Donaldson), and the end law is sL-8's. · **Price:** unchanged, 0 of 19 · **Numbering:** B1506.

## 0. Seen from above

sL-5 asks whether the M₆ deck is gauged (one index −1 object on M₂) or a global symmetry (three on M₆), and B1384 S3 said the
mathematics does not decide it. The genesis's tower has one base: every level Mₙ covers the root m004, and the root's deck ℤ/n acts on
every level. This arc asks what that fixes.

- **One background, one count.** Shapiro keeps a background's index when it is induced down (B1384 S3), and a pullback keeps it on
  the way up (T2). So a single background has the same count on every level. "One or three" is never about one background.
- **The triplet is the orbit of the root's whole deck.** τ³ changes the seed's SL(2)_β × U(1)² data only by the ℤ/2 that E₆ ⊃
  (SU(2) × SU(6))/ℤ₂ quotients out (T4). So the seed's orbit under ℤ/6 has three members, and they are the triplet: it is fixed by the
  whole deck of M₆ over the root, not only by the part over M₂.
- **It lives on s961.** The triplet descends to s961, the root's only connected 3-fold cover, as the deck orbit of one background
  D₀. Among the four descents exactly one has every sector's meridian value trivial, and Shapiro forces its six counts to be (−1)⁶
  (T6). D₀ does not lift to SL(2)_β × ℂ*²: its extension character is not a square.
- **So one versus three is the root versus s961.** The root object Ind D₀ has count −gcd(n, 3) on Mₙ: one on m004, M₂, M₄, M₅, and
  three on s961 and M₆ (T7). The genesis fixes both levels, since s961 is m004's only 3-fold cover. What remains of sL-5 is one bit:
  is the root's deck gauged (one) or kept (three)?
- **s961's complete census.** In the Standard-Model frame s961 carries:
  - 72 firing doublet modules, all on its 12 non-square loci;
  - 48 generation-shaped backgrounds, none of which lift;
  - 16 orbits of three under the root's deck, split 24/24 in sign;
  - in each background, ν^c with the same sign as the rest: whole generations.

  B1375 saw none because it counted lifted backgrounds only (§6).
- **M₆'s complete census.** 2 160 generation-shaped backgrounds, all with count ±1: 336 lift (B1375's 67 200 lift data, exactly) and
  1 824 do not. Under the root's deck:
  - 16 orbits of three, which are s961's 48 pulled back (they lift on M₆);
  - 352 orbits of six;
  - none of size one or two.

  The triplet type is exactly s961's, and so is B1375's "ν^c with the generation's own sign": its 9 600 are those 48. The root object
  of an orbit of six counts gcd(n, 6) on Mₙ: one on m004, two on M₂, three on s961, six on M₆.
- **The fence.** The three blocks of an orbit are three distinct vacua: their extension characters differ by characters of order 4.
  One E₆ vacuum carries one generation, so reading an orbit as three generations needs the whole orbit in one physical configuration
  (§5).

## 1. The seal, and the one result seen before it

The arc began as a proof that nothing the root's whole deck fixes can have count three. Its check, the seed's orbit under ℤ/6, was
expected to be six and came back three. The argument had relied on B1375's "s961 fires nowhere", which holds only for backgrounds
that lift to SL(2)_β × ℂ*². That outcome was not sealed. The seal (58e3f28f):
- lists everything seen before it;
- proves T1–T7 from that one fact;
- decides D1–D8 at design time;
- seals P1–P8.

Two of the design-time items were moved to predictions before the seal (P7, P8), because their proofs used the seed's non-trivial
unipotent meridian, which a general background need not have. The draft's case analysis, built on the withdrawn premise, was removed
before the seal.

## 2. The theorems (proved at seal; full proofs in `PREREGISTRATION.md` §2)

- **T1 (the loci lemma, every level).** A finite-order character λ of π₁(Mₙ) has h¹(λ) ≥ 1 iff one of:
  - λ = 1;
  - λ is non-trivial on the fibre and λ(tₙ) = 1.

  Otherwise only tₙ ↦ φ^{±2n}, which is not a root of unity. The reason: φ fixes the fibre's boundary, and restriction H¹(F; σ) →
  H¹(∂F; ℂ) is an isomorphism, so φⁿ acts trivially. So every finite-order locus is trivial on the cusp. Main's B1427 computed the
  loci over the whole character group for n = 2…7, the two golden ones included; T1 is the statement for every n.
- **T2 (a pullback keeps the index).** A doublet module that satisfies T5 keeps its index under pullback. Every twist by a deck
  character moves the meridian value off 1, and so fails T5.
- **T3 (lifts).** A Standard-Model-frame background lifts to SL(2)_β × U(1)² iff its extension character is a square, because
  H²(Mₙ; ℂ*) = 0. Non-square loci exist exactly when the fibre torsion has even order: M₃ and M₆ for n ≤ 6.
- **T4 (the kernel).** (−1_{SL(2)}, 1, e^{iπQ_γ}) is trivial in E₆ ⊃ (SU(2) × SU(6))/ℤ₂: Q_γ is odd on the 6, so e^{iπQ_γ} = −1_{SU(6)}.
- **T5 (the root's census).** m004's only finite-order locus is λ = 1. Its only candidate module is the unipotent U, which is
  self-dual, so I(U) = 0. Hence no firing background is fixed by the whole deck of its level.
- **T6 (the triplet descends to s961).** τ³ acts on the seed by T4's kernel, so the triplet is the seed's root-deck orbit.
  - The seed extends to s961 in four ways (flips by −1_{SL(2)} and by e^{iπQ_Y}).
  - D(t₃)² = S(t₆) is a non-trivial unipotent, and −N has no square root in SL(2, ℂ). Hence each descent's meridian values form the
    pattern σ·(y, 1, 1, 1, y, 1) over (Q, u^c, e^c, d^c, L, ν^c), and exactly one descent D₀ has all six equal to 1.
  - Shapiro and T5 then force I(D₀,s) = I(S_s) = −1 in every sector.
  - D₀'s orbit on s961 has three members, by T5.
  - D₀ does not lift, since the lifted census of s961 is silent.
- **T7 (counts by level).** Ind D₀ on m004 has count −gcd(n, 3) on Mₙ.

**T7's proof for any background (a remark, checked after the run).** Let B be a T5-candidate module on M_k (every firing sector is
one). The subgroups are normal, so Mackey writes the restriction of Ind B to Mₙ as gcd(n, k) blocks Ind_{M_l}^{Mₙ} of the translates
τʲB restricted to M_l, l = lcm(n, k). Each block counts I(B), by Shapiro, T2 and the deck-invariance of the index. So Ind B counts
gcd(n, k) · I(B) on Mₙ, and I(B) on the root. The proof uses nothing about the stabiliser. The root object of an orbit is Ind of one
member from the level where the orbit is free.

## 3. Computed (`verification/the_level.py`; record `the_level_run.txt`, `the_level.json`; 29 minutes)

**A. Covers (SnapPy).** m004's connected covers of degree 2 to 6 number 1, 1, 2, 4, 11. The only ones of degree 2 and 3 are cyclic:
m206 and s961. Every non-cyclic cover up to degree 6 is irregular. det(4₁) = 5, so there is no S₃ quotient. The cyclic covers are
m206, s961, t12839, o10_150696 and otet12_00013, with H₁ as in B1375.

**B. Presentations and the deck.**
- On B1381's mapping torus (M₁…M₆), τ = (φ, φ, t) is an automorphism: the formal identity, and up to 12 genuine representations
  per level. τⁿ is conjugation by t, and φ fixes abAB.
- On B1384's Reidemeister–Schreier covers (M₂…M₆), τ = conjugation by a has the closed form z ↦ z, y_k ↦ y_{k+1},
  y_{n−2} ↦ y_{n−1}z⁻¹, y_{n−1} ↦ zy₀. It is a homomorphism on the holonomy-type representation, and so is its square.
- B1378's TAU and TAU2 are not homomorphisms on that representation.

**C. The loci lemma.** The gcds of the Fox minors, exact over ℚ(ζ_e):

| level | σ = 1 | σ ≠ 1 |
|---|---|---|
| M₁ | s² − 3s + 1 | — |
| M₂ | s² − 7s + 1 | s − 1 (4) |
| M₃ | s² − 18s + 1 | s − 1 (15) |
| M₄ | s² − 47s + 1 | s − 1 (44) |

M₅ (N = 660, 79 860 characters) and M₆ (N = 120, 38 400 characters) were scanned at three primes. They have 120 and 319 non-trivial
loci, every one with t ↦ 1 and a non-trivial fibre part, and no exception. The census's own loci (below) had no exception on any level
or presentation either. The first run scanned M₅ and M₆ at one prime and reported two exceptions on M₅ (§8).

**D. The complete census**, three primes, every non-zero index re-checked (none differed). The table covers every locus, square or
not; "gen." counts generation-shaped backgrounds.

| level | pres. | loci (non-square) | candidates | firing (non-sq.) | modules by orbit size | gen. (lifted) | gen. by orbit size | lift data |
|---|---|---|---|---|---|---|---|---|
| M₁ | RS, MT | 1 (0) | 1 | 0 | — | 0 | — | — |
| M₂ | RS, MT | 5 (0) | 25 | 8 (0) | 2: 8 | 0 | — | — |
| s961 | RS, MT | 16 (12) | 256 | 72 (72) | 3: 72 | 48 (0) | 3: 48 | — |
| M₄ | RS, MT | 45 (0) | 2 025 | 488 (0) | 2: 8, 4: 480 | 256 (256) | 4: 256 | 12 800 |
| M₅ | RS | 121 (0) | 14 641 | 2 200 (0) | 5: 2 200 | 400 (400) | 5: 400 | 800 |
| M₆ | RS | 320 (240) | 102 400 | 12 536 (11 184) | 2: 8, 3: 72, 6: 12 456 | 2 160 (336) | 3: 48, 6: 2 112 | 67 200 |

Notes on the table:
- **B1375 comes back from the lift data.** Its firing pairs are 16 = 8 · 2, 976 = 488 · 2, 4 400 = 2 200 · 2 and
  10 816 = 1 352 · 8 (M₆'s firing modules on square loci). Its backgrounds are 12 800, 800 and 67 200 exactly. Its loci are the
  square loci times their square roots, less the trivial root: 9, 31, 89, 241, 639.
- **Signs and sizes.** Every generation-shaped background on every level has count ±1 in each charged sector, and the signs split
  equally on every level (24/24, 128/128, 200/200, 1 080/1 080). The index is deck-invariant on every level.
- **s961.** Each non-square locus carries 6 firing modules and 4 backgrounds, and every sector of a background has one sign.
- **Pulled-back modules.** The 8 modules with orbit size 2 on M₄ and on M₆ are M₂'s 8 pulled back, and the 72 with orbit size 3 on M₆
  are s961's (E, T2). A pullback's orbit has the size it had below, and no orbit has size 1.
- **ν^c.** On M₄ and M₅ no background carries ν^c. On M₆, 240 do (120 of each sign) and 1 920 do not.

**E. Pullbacks keep the index (T2)**, on the mapping torus, every candidate:

| base → cover | 1 → 2, 3, 4, 5, 6 | 2 → 4 | 2 → 6 | 3 → 6 |
|---|---|---|---|---|
| candidates, index kept, = Shapiro's twist sum | 1 each | 25 | 25 | 256 |
| firing pullbacks | 0 | 8 | 8 | 72 |

**F. The triplet, its descents, the root object**, three primes.
- The seed's six translates are three classes. τ³ fixes the seed, and τ² multiplies λ by a character of order 4.
- The four E₆ descents to s961 have meridian patterns and indices:
  - (0,0,0,0,0,0): (−1)⁶;
  - (0,1,1,1,0,1)·½: Q and L fire;
  - (1,0,0,0,1,0)·½: u^c, e^c, d^c, ν^c fire;
  - all ½: nothing fires.
- λ on s961 is not a square. D₀'s orbit has three members and pulls back to the triplet.
- The members are (−1)⁶, the triplet sum is (−3)⁶, and Ind D₀ gives (−1, −1, −3, −1, −1, −3) on M₁…M₆ in every sector.

**H. The s961 / M₆ correspondence.**
- All 48 of s961's backgrounds pull back to generation-shaped backgrounds of M₆ with the same six counts, fixed by τ³.
- On M₆ all 48 lift: an extension character that is not a square on s961 becomes one on its double cover.
- M₆'s τ³-fixed generation-shaped backgrounds are exactly these 48.

**Checked after the run** (`verification/post_run_checks.py`, record `post_run_checks_run.txt`, `post_run_checks.json`; not
predictions):
- **The fence.** On s961 every orbit's three extension characters are distinct and differ pairwise by characters of order 4. The
  reason is that φ − 1 is invertible on H₁ (det(φ − 1) = −1). On M₆ the 48 in orbits of three behave the same way, and every orbit
  of six carries six distinct characters. On M₄ the ratios have orders (15, 3, 15), and on M₅ all have order 11.
- **The singlet against the orbits.** On M₆ B1375's singlet split is the orbit split. Its 9 600 lift data with ν^c of the
  generation's sign are the 48 backgrounds in orbits of three (s961's, 200 lift data each). Its 57 600 without ν^c are the 288 lifted
  backgrounds in orbits of six. Of the 1 824 that do not lift, 1 632 carry no ν^c, 96 carry it with the generation's sign and 96 with
  the opposite sign.
- **The level law.** Two backgrounds of each orbit size on s961, M₄, M₅ and M₆ were checked in every sector at three primes. Ind from
  M_k to the root counts gcd(n, k) · I on Mₙ, times the sign, with ν^c zero where the background has none:
  - (1, 1, 3, 1, 1, 3) from s961;
  - (1, 2, 1, 4, 1, 2) from M₄;
  - (1, 1, 1, 1, 5, 1) from M₅;
  - (1, 2, 3, 2, 1, 6) from M₆, for its orbits of three and of six alike.

  For an orbit of three on M₆, Ind from M₆ is Ind D ⊕ Ind(D ⊗ ε), where D is its descent to s961 and ε is M₆'s deck character over
  s961. So the orbit's root object is Ind D, from s961, which counts gcd(n, 3).

## 4. The sealed predictions, read

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | every generation-shaped background on s961 has \|count\| = 1 in each charged sector | ~85% | **YES** (all 48) |
| P2 | signs split equally on s961 | ~80% | **YES** (24/24) |
| P3 | all 12 non-square loci of s961 fire | ~60% | **YES** (6 firing modules each) |
| P4 | 336 lifted generation-shaped backgrounds on M₆ | ~85% | **YES** (336, with B1375's 67 200 lift data) |
| P5 | some but not all of those are fixed by τ³ | ~75% | **YES** (48 of 336) |
| P6 | M₆ carries non-lifted generation-shaped backgrounds | ~70% | **YES** (1 824) |
| P7 | every τ³-fixed generation-shaped background on M₆ is a pullback from s961 | ~75% | **YES** (48, = G₃) |
| P8 | no generation-shaped orbit of size 2 on M₄ or M₆ | ~80% | **YES** (M₄ 4: 256; M₆ 3: 48, 6: 2 112) |

All eight came true at priors of 60–85%, where about six were expected, so the priors were conservative. P4 was B1375's count divided
by its redundancy, and P7 and P8 had design-time arguments that fell short of proofs.

## 5. What it means

- **The level question has an answer for one background.** The count does not depend on the level. Shapiro takes the index down,
  and T2 takes it up.
- **Three comes from the root's own deck, on its only 3-fold cover.** The M₆ triplet is not a feature of M₆ over M₂. It is the
  pullback of an orbit of the root's deck on s961, and s961 carries 16 such orbits. On M₆ these are the only root-deck orbits of
  three; every other generation-shaped background there is in an orbit of six. The genesis's tower fixes the two levels that
  matter: the root, where each orbit is one object with count ±1, and s961, where it is three backgrounds with ±1 each. The number
  three is the degree of the root's unique 3-fold cover.
- **An orbit counts gcd(level, size).** An orbit of k backgrounds is one object on the root and counts gcd(n, k) on Mₙ. So the count
  is three exactly when gcd(n, k) = 3: on s961 for orbits of three or six, and on M₆ for orbits of three. As three honest E₆
  backgrounds of one level, it happens only for s961's own orbits. M₆'s orbits of six also restrict to three objects on s961, but
  those are induced from M₆. They are not backgrounds of s961: as E₆ data their structure group is E₆ ≀ ℤ/2.
- **What remains of sL-5 is one bit.** Is the root's deck gauged, so that the physical level is m004 and the count one? Or is it
  kept, so that the level is s961 and the count three? B1384's transition-semantics fence covers exactly this: whether all generated
  states are simultaneously physical is not derived. The audit lane's R58 (finite-cover transport, cited) shows the two readings are
  different theories unless the algebra travels with the cover.
- **The fence, sharpened.**
  - The three backgrounds of an orbit are three distinct E₆ vacua. Their extension characters, the adjoint characters of the
    SL(2)_β holonomy, differ by characters of order 4.
  - A single E₆ vacuum carries one generation.
  - Any frame that makes the family index a tensor factor beside SL(2)_β gives every family the same λ, so it cannot hold an orbit
    as three families of one vacuum. That covers E₆ × SU(3) ⊂ E₈. B1384's item E (the handoff's pairing census, reproduced there,
    not re-derived) reaches the same conclusion for the SL5 commutant: the M₆ orbit is not a mixed-root subbundle of any SL5 flat
    background.
  - So a physical three needs one of two things. One is the whole orbit in one configuration: three copies of the E₆ sector on
    s961, or the induced object on m004 with structure group E₆ ≀ ℤ/3, which counts one. The other is a parent that carries three
    different SL(2)_β holonomies as families. The record has neither.
- **No physics is crossed.** Index ≠ generation count. The backgrounds are non-semisimple. The end law is sL-8's. 0 of 19.

## 6. Corrections of record

- **B1375 ("s961 fires nowhere"; THE_SM_VERDICT's "Y₂, Y₃: no generation-shaped background").**
  - The census parametrised backgrounds by a lift (χ, ψ_Y, ψ_γ), so it saw only square extension characters.
  - On s961 the backgrounds that do not lift fire: 72 modules and 48 generation-shaped backgrounds. On M₆ it counted 336 of 2 160.
  - The absence held for what was enumerated, not for the frame. ERROR_LEDGER, E54 instance (2026-09-30): self-caught when a check
    that relied on it came back three, not six.
  - Its law holds on the complete census: every background has count ±1, on every level. On M₂, M₄ and M₅ its census is complete
    (T3), and this arc reproduces it on two further presentations.
- **B1378 §3 ("instrument limit").** It was a convention slip: the rewriting's last generator is a⁵b. Conjugation by a is
  y₄ ↦ y₅z⁻¹, y₅ ↦ zy₀, and both it and its square are homomorphisms. B1378's index results stand, because `deck()` agrees with the
  correct map on its characters (χ(z) = 0).
- **B1384 S3 ("one versus three is M₂ against M₆").** The triplet is also the pullback of a root-deck orbit on s961. The two levels
  the genesis fixes are the root and s961.
- **Main's B1427 ("Y₃: 0 firing"), relayed, not applied.** Its verification of B1375 used the same lift, so it has the same scope:
  s961 fires on its non-square loci.

## 7. Sweep and prior art

**This branch, main (987c0c8f) and the audit lane were searched** (8c46c279 at the seal, edd753fc at banking; the one new commit is
about cone flux). Terms: deck-invariant or deck-symmetric; descends to m004 or to M₃; one versus three; cover-resolution; non-liftable
or does not lift; (SU(2) × SU(6))/ℤ₂; τ³; word map; quotient/cover.
- **This branch.** B1356 and B1362 have deck-symmetric statements about apexes and Yukawas on the closed Y₃ (charges vanish, or a
  degenerate pair). B1301–B1304 treat the closed tower's half-deck and its conductor ("the level a character is pulled back from").
  B1371 lists m004's degree-2 and degree-3 covers (one each).
- **Main.**
  - B1297 has T6 (the index is invariant under diffeomorphisms) and the deck-invariant free generator on C₃. It notes that the
    non-deck-invariant components of X_SL(3)(C_n) were never enumerated. B1297's frame is (2+1)-reducible SL(3) spectral covers,
    not this one.
  - B1427 solved h¹ ≥ 1 exactly over the whole character group for n = 2…7, by gcds of the Fox minors over ℚ(ζ_e). It found the
    two golden loci per level that a μ_N scan misses. T1 proves for every n what B1427 computed for n ≤ 7, and part C re-derives
    B1427's computation for n ≤ 4. B1427's census used B1375's lift.
- **The audit lane.**
  - R58 (COVER_ACTION, cited in §5) covers finite-cover transport.
  - The received fork note `deck_descent_2026_09_27` covers the M₆ → M₂ deck: a geometric C₃ on the pullback, with D³ = Id.
  - Its PB-HANDOFF-M6 lead (received at 9f9a0751) asks for exactly these checks: the deck word-map discrepancy, Shapiro–Mackey with
    cusp maps, the twisted deck cube, and which quotient or cover is used. It also says a strict C₃ action and three physical
    generations are not given by the deck group's order. This arc settles the first (§6) and agrees with the last (§5). The lead
    also asks for no fresh index census without a changed premise. This census's premise is the backgrounds that do not lift (T3),
    which no earlier census enumerated.
- **Not found anywhere:** the triplet's orbit under the root's whole deck, its descent to s961, the non-lifted census, or the
  gcd level law.

The ingredients are standard: Shapiro–Mackey, the Wang sequence, E₆'s (SU(2) × SU(6))/ℤ₂. What is claimed new is their application
here.

## 8. Caveats

1. **Prime fields.** The indices are computed over prime fields (three primes, every non-zero index re-checked). Exact arithmetic is
   used only for the loci lemma on M₁–M₄.
2. **Character values, and completeness.**
   - The census uses characters with values in μ_N, N = lcm(12, torsion exponent); s961 uses N = 120 on RS and 12 on MT.
   - T1 makes this complete on the finite-order loci, since every one of them has trivial meridian value.
   - The only loci of infinite order are the golden ones, tₙ ↦ φ^{±2n} with trivial fibre part (B1427, two per level, h¹ = 1).
     They carry no T5-candidate in this frame. In every sector α_s β_s is the square of the U(1)_Y × U(1)_γ part, which is
     unitary, so |α_s(tₙ)| = |β_s(tₙ)|⁻¹ = φ^{±n} ≠ 1. Neither diagonal character is trivial on the cusp.
   - Firing needs a trivial meridian value (T5), so the candidates are complete too.
   - The draft of this document gave a weaker reason, "every locus has trivial meridian value". The banking sweep found B1427's
     golden loci, and the argument above replaced it (ERROR_LEDGER, E54 instance of 2026-09-30, item 2).
   - The fifth-root redundancy (the ℤ/5 kernel of D7) is quotiented by identifying backgrounds through their six sector modules.
3. **Scope of the E₆-frame claim.** A background here is determined by its six doublet sectors and λ. The singlet sectors follow
   from (λ, κ, ψ_Y), and T4's kernel acts trivially on them.
4. **P7 and P8** were predictions, because their proofs used the seed's unipotent meridian.
5. **Non-cyclic covers** of m004 are outside the tower. They begin at degree 4 and are all irregular up to degree 6.
6. **The loci check read at one prime (E52 instance, self-caught).** The first run of the sealed instrument scanned M₅ and M₆ for T1
   at the first prime alone. On M₅ (N = 660) the prime 661 reported two exceptions, at meridian exponents 30 and 630. The golden
   locus s² − 123s + 1 has roots 204 and 580 mod 661, both of order 22, and 22 divides 660. So two characters whose meridian value is
   a 22nd root of unity looked like loci mod 661. Over ℂ the roots are φ^{±10}, which are not roots of unity. 1321, 3301 and 4621
   give h¹ = 0 on both characters, and B1375's Y₅ row records the same prime's coincidences ("241 (4 on 661, 0, 0)"). The census
   already required all three primes. The check now does too, and it records what passes at the first prime only (2 on M₅, 0 on
   M₆). The whole instrument was rerun. The first run's log is kept (`the_level_run_first.txt`), and it agrees with the second on
   every other number. T1 was proved at seal and no prediction's reading changed.

## Verification

- `verification/the_level.py`:
  - parts A–F and H;
  - the full run in `the_level_run.txt` and `the_level.json` (29 minutes); the first run's log in `the_level_run_first.txt`;
  - the lock's live tests need about 5 s.
- `verification/post_run_checks.py`: the fence, the singlet against the orbits, and the level law on s961, M₄, M₅ and M₆ (record
  `post_run_checks_run.txt`, `post_run_checks.json`).
- Lock: `tests/test_b1506_the_level.py`:
  - live: the deck and the word map, the loci lemma on M₁ and M₃, s961's complete census on two presentations with the fence, and
    the seed's descent with the level counts;
  - recorded: covers, the loci scans, the census of every level, the pullbacks, the correspondence and the post-run checks.

**Sources:**
- B1374's `index_lib.py`, B1375, B1377, B1378, B1381 (the mapping torus), B1384 (the RS covers, S3, S5, item E), B1371 (the covers),
  B1368 (the E₆ decomposition).
- Main's B1297 (T5, T6).
- The audit lane's R58, PB-HANDOFF-M6 and the received fork note, cited.
- The seal at 58e3f28f.
