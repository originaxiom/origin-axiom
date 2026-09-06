# B1271 — THE CHAIN TAKEN ALL THE WAY: three generations are the Eisenstein triplet (27,3) of the golden E₈, the 27's own singlets take the rank from 6 to 4, and the Yukawa E₈ forces on the triplet is antisymmetric in the generations — hence zero

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (every structural step exact) + NEGATIVE (the chain forces the triplet's tree-level Yukawa to vanish identically: no hierarchy, no mixing, and the mirror stays; the values stay behind I-13, and the object they need at this step is now named — a *symmetric* family tensor, which the corpus found empty on the object) · **Price: unchanged at 14**

## Why this arc — the owner's third instruction

*"All ingredients for the SM are here; compute the missing all the way to the full SM with three generations."*
B1270 derived E₆ from the two faces and, in doing so, found the **three**: the (27,3) of E₈ ⊃ E₆ × SU(3) — three
full copies of the 27, indexed by the three weights of the Eisenstein 3 and cycled by the founding ratio
g = −RL⁻¹. That is the **multiplicity** mechanism B302/B308/B632 asked for (*"generations, if anywhere, come from
a multiplicity mechanism"*; B308's queued gate: *"can the multiplicity route produce three generations with the
right Yukawa texture?"*). This arc takes that triplet through every remaining Standard-Model step the corpus's
ingredients supply, computes each step exactly, and reports what comes out — including the step that comes out
**zero**.

## 1. Three generations: the triplet (`verification/all_the_way.py` (a), exact on B1270's icosian E₈)

The 162 roots of E₈ outside E₆ ⊕ A₂ fall into six classes of 27 by their Eisenstein pairings. Left multiplication
by g cycles them in two orbits of three — **(27,3) and (27̄,3̄)** — the three pairings of each orbit summing to
zero (the weights of a 3), and quaternion conjugation θ swaps the orbits. **The three generations are the three
weights of the Eisenstein 3: three copies of the whole 27, permuted by the object's own order-3 element**, with
the conjugate triplet as their mirror. This is a count of *things*, not of conjugates in the sense E63 forbids:
the three classes are distinct subsets of the root system, and the SU(3) Weyl group permutes them (the generation
permutation symmetry, as it should be).

As **4d fields** (the E₈ transport of B1270, Acharya–Witten with the golden E₈ along Q): with the Eisenstein 2T as
the holonomy in the 3, the triplet is counted by h¹(Q; 3_ρ) = 1 — **one** 27 and one 27̄, gauge group E₆; with
the holonomy trivial on the 3, the gauge group is E₈ and the matter is **one adjoint chiral multiplet**
(b₁(m004) = 1), whose E₆ × SU(3) content 248 = (78,1) + (1,8) + **(27,3)** + (27̄,3̄) *is* the three 27s and
their mirror. Either way the count on the object is N = 0 (B1268, B1270): the triplet comes with its mirror.

## 2. The chirality bit

The two triplets are exchanged by θ, and θ is the Eisenstein conjugation ω ↔ ω̄ (B1270). Choosing which triplet is
matter is choosing an orientation of the Eisenstein plane: a **mirror-odd ℤ/2**. The object is amphichiral and
cannot supply it (B1184, B713/B760); a closing (B432/B434) or a pair (B1192/B1248: ε = −1) does. **The bit is the
same bit the corpus has carried since B582: not derived, supplied by the closing.** Nothing new here; the bit is
placed exactly — it is the choice between ω and ω̄.

## 3. E₆ → the Standard Model, rank 6 → 4 by the 27's own singlets ((b), exact on B1252's descent)

The adjoint cascade lands on the rank-6 Levi su(3)⊕su(2)⊕u(1)³ and can go no further (B952; B1269's double-
centralizer theorem). The two faces now supply 27s, and the 27 contains **exactly two Standard-Model singlets**
(zero SU(3)×SU(2) charges, Y = 0): weight 12, **ν^c in the 16**, and weight 13, **the SO(10) singlet**. Their charges
under the two extra U(1)s of the Levi form the matrix [[1/3, −1], [1/3, 0]] of **rank 2**: VEVs for both (with their
conjugates in the 27̄ along the D-flat direction) break both extra U(1)s and nothing else, leaving **exactly
su(3) ⊕ su(2) ⊕ u(1)_Y**. Hypercharge (B864/B1252), the ℤ₆ (B862) and sin²θ_W = 3/8 (B919) follow as banked.
**The gauge group of the Standard Model is reached, structurally, from the two faces** — by the 27's singlets,
whose *values* the object does not supply.

## 4. The family tensor E₈ forces ((a), exact)

The bracket of E₈ restricted to (27,3) × (27,3) lands in (27̄,3̄), and on the lattice:

| | |
|---|---|
| two roots of the **same** class (27,3)_i whose sum is a root | **0** of 3 × 27² — 2e_i is not a weight of the 3̄ |
| two roots of classes i ≠ j whose sum is a root | **270 = 6 × 45** per ordered pair, **all** in the class **−e_l of the third index l** (e_i + e_j = −e_l): the support of E₆'s cubic d (45 triples) times the six orderings |

Schur makes this exact: Λ²(27 ⊗ 3) = Λ²27 ⊗ Sym²3 ⊕ Sym²27 ⊗ Λ²3, and 27̄ ⊗ 3̄ sits once, in the second summand
(Λ²27 = 351 irreducible, Sym²27 = 27̄ ⊕ 351′, Λ²3 = 3̄). So the bracket is **d_abc · ε_ijk**: E₆'s symmetric
cubic times the **antisymmetric** family tensor. This is B308's unique cubic (its SO(10) content computed here as
**45 = 40 (10·16·16) + 5 (1·10·10)** — (d)) with the generation index carried by ε.

## 5. The Yukawa on the triplet is zero ((c), exact and symbolic)

A 4d superpotential is a polynomial in *commuting* superfields, and d_abc X^a_i X^b_j X^c_k is symmetric in
(i, j, k) for any symmetric d; so W = Y^{ijk} d_abc 27^a_i 27^b_j 27^c_k sees only the totally symmetric part of
the family tensor Y. E₈ forces Y = ε. Hence

**W_E₈ |_(27,3) ≡ 0** — checked monomial by monomial with generic rational d on the 45-triple support (the
control with a symmetric Y is nonzero: 135 monomials; one generation's own d_abc 27³: 45).

Three independent ways to say the same zero: E₈ has **no cubic invariant** (Casimir degrees 2, 8, 12, 14, 18, 20,
24, 30), so one adjoint chiral has no superpotential; Sym³(27 ⊗ 3) has **no E₆ × SU(3) singlet** because
Sym³(3) = 10; and on m004 itself b₁ = 1, so the Chern–Simons cubic ∫ ω ∧ ω ∧ ω of a single 1-form vanishes. The
consequences, all forced:

- **every tree-level mass of the triplet is zero** — no texture, no hierarchy, no mixing angle, no phase;
- the mirror (27̄,3̄) is equally massless: the vector-like pair is not lifted;
- the neutrino: no Majorana term is even available in d (no 16·16·16, no 1·16·16 — (d)), and the Dirac term is
  part of the same vanishing W.

The corpus met this wall on the object: B632 and B1036 found the cohomological pairing **antisymmetric-only**, its
symmetric part (V3) **empty**, and concluded "no Yukawa". E₈ says the same thing on the lattice — the family tensor
it supplies is ε. The two antisymmetries live on different objects and are recorded as consistent, not identified;
their physical consequence is one and the same zero.

## 6. The Standard Model, item by item, at the end of the chain

| Standard-Model item | what the chain gives, computed | status |
|---|---|---|
| gauge algebra su(3)⊕su(2)⊕u(1)_Y | E₆ from the two faces (B1270) → the rank-6 Levi (B1252) → rank 4 by the 27's two singlets ((b)) | **reached as structure**; the two VEV values not supplied |
| hypercharge, ℤ₆ global form, sin²θ_W = 3/8 | B864/B1252, B862, B919 | reproduced, as banked |
| three generations | the (27,3) of E₈ ⊃ E₆ × SU(3), cycled by the founding ratio ((a)) | **present as structure**; as 4d fields only together with the mirror (27̄,3̄): N = 0 |
| chirality (no mirror) | the Eisenstein orientation ω ↔ ω̄ | supplied by a closing, not by the object |
| Yukawa couplings: 9 masses, 3 angles, 1 phase | E₈'s family tensor is ε → **W ≡ 0** ((c)) | **forced zero** — nothing to compare with the data |
| neutrino masses | no Majorana term in d; the Dirac term is in W | zero at tree level |
| the 19 values | — | 0 of 19 (B1261), unchanged |

**The chain, taken all the way, is a definite parameter-free theory: E₈ (or E₆) on the object's cusped manifold
with one adjoint chiral multiplet, whose E₆ × SU(3) content is three 27s and three 27̄s cycled by the founding
ratio, a Standard-Model gauge group reachable by the 27's own singlets, and a vanishing superpotential. It is not
the Standard Model: it is vector-like and massless.** What the Standard Model needs at the step where this theory
stops is precise: a **symmetric** family tensor Y^{(ijk)} on the triplet, i.e. three 27s that something *outside*
E₈ tells apart (three classes on a closing with a non-zero triple product, or a source of flavour). The corpus's
own search for that on the object found it empty (B1036 V3); its one value-layer candidate, HIER (B918/B923/
B1255), was refuted as a flavour index (I-24). The same closing that supplies the chirality bit is where a
symmetric tensor could come from — it is not in the object.

## 7. Ledger

- **Three generations:** DERIVED as the Eisenstein triplet of the golden E₈ — the multiplicity the corpus asked
  for, with the ℤ/3 that permutes them being the founding ratio; on the object they come with their mirror.
- **Chirality:** the bit is the Eisenstein orientation; supplied by a closing, not by the object (unchanged).
- **Gauge group:** reached exactly by the 27's two singlets (structure), VEV values not supplied.
- **Yukawa:** FORCED ZERO on the triplet — the family tensor E₈ supplies is antisymmetric, and an antisymmetric
  family tensor on E₆'s symmetric cubic is no coupling at all. B308's queued gate ("the multiplicity route with
  the right Yukawa texture?") is answered: the multiplicity route gives three, and gives them **no** texture.
- **Values:** still 0 of 19 (B1261). The named missing object for the values is a symmetric family tensor.

## Controls (MB12, both directions)

- The same-class sums are checked for all 3 × 27² pairs and are **all** non-roots; the cross-class sums are
  checked for all 6 × 27² ordered pairs and land **without exception** in the third index' conjugate class.
- The vanishing of W is checked with *generic* rational values of d on the support (not equal coefficients), so
  it is the antisymmetry of ε and not an accident of d; the symmetric control is nonzero with the expected
  3 × 45 monomials, and a single generation's d_abc 27³ is nonzero with 45.
- The singlet count can fail (the descent's Y is unique; a wrong Y gives a different singlet set) and the charge
  matrix could have been singular; it is rank 2.
- The cubic's content 45 = 40 + 5 reproduces B1253's 40 and adds the 5.

## Verification

`verification/all_the_way.py` (exact; ~3 min; `SELFTEST: PASS`), run record `verification/all_the_way_run.txt`.
Lock: `tests/test_b1271_the_chain_all_the_way.py`.

- **Feeds on:** B1270 (the triplet and the E₈ transport), B1252 (the descent and Y), B1250 (the SO(10) blocks),
  B883 (the weights), B308/B632/B1036 (the cubic and the antisymmetry wall), B952/B1269 (the rank obstruction),
  B1253 (the 40), B1255 (I-24), B1192/B1248 (the bit), B1268 (N = 0), B1261 (0 of 19).
- **Registers:** no identification change; no new unearned input (every step is Lie theory on banked objects, and
  the physics reading is the same I-13 the corpus already prices).
