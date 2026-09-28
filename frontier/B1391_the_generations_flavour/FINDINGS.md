# B1391 — THE GENERATIONS' FLAVOUR (test 4, in structural form): the frame's two generations on cube~3.24 are the doublet of its isometry group D₃ ≅ S₃. The order-3 isometry gives them the charges ω and ω², and the swaps exchange them. So with one Higgs doublet of each type they are exactly degenerate in every sector at the symmetric point, and any hierarchy between them is D₃ breaking. The pullback three of B1390 carries ℤ/3's regular representation: at the symmetric point B1362's circulant degeneracy (a degenerate up-type pair for a Higgs of any definite charge), or S₃'s "2 + 1" when a symmetry inverts the deck. The symmetric geometry supplies a flavour group, not the Yukawa ratios.

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** test 4 of the kill tests on the chirality mechanism
(the Yukawas), after test 3 was decided by B1390. · **Status:**
- PROVED: the equivariant index; the representation, exact from banked data and B1390's fixed sets; the textures, symbolic.
- NEGATIVE: for Yukawa ratios as an output of the symmetric geometry.

**Not sealed:** its outcome follows from banked theorems once the fixed sets are known, and sealing such a test would be theatre
(the B1371 lesson). · **Fence:** the seat's frame, spin-0 half, the 27-frame of B1389; tree level; the Higgs doublets' representations
are an input (they carry index 0, B1372) · **Price:** unchanged, 0 of 19 · **Numbering:** B1391.

## 0. Seen from above

The plan's fourth test was the Yukawas. Before any overlap integral, symmetry fixes what a Yukawa coupling can be.
- **The action.** The isometries that fix the Higgs class act on the zero modes.
- **The character.** The frame's count is the Euler characteristic of the pair (M_T, ∂⁺M_T) at an invariant cut, so the character of
  that action is a Lefschetz number: χ(Fix g, Fix g ∩ ∂⁺).
- **What it needs.** Only the fixed sets (B1390's instrument) and where their ends fall in the partition (B1387).

On cube~3.24, the one member where the frame's index is computed:
- R, the order-3 isometry, fixes 3 arcs between the Eisenstein cusps. Each ∂⁻ there is a disc holding exactly one of R's three fixed
  points, so 4 ends lie in ∂⁺ and **L(R) = 3 − 4 = −1**.
- Each swap fixes 4 arcs between the annular cusps 1 and 2. An involution of an annulus has at most two fixed points, so the ends split
  2 / 2 and **L(swap) = 4 − 4 = 0**.
- With L(e) = N = 2, the character is (2, −1, 0), which is **E, D₃'s two-dimensional irreducible representation**.
- B1388's zeros agree: R fixes the three zeros at its axes' midpoints, with Hopf indices +1, −1, +1, so tr R = −1.

Schur then decides the Yukawas at the symmetric point:
- **One Higgs doublet of each type** (necessarily in a one-dimensional representation). The only covariant forms on E ⊗ E are
  [[0, y], [y, 0]] (Higgs in A₁) and [[0, −y], [y, 0]] (Higgs in A₂). Each has one singular value twice, so **the two generations have
  equal masses in every sector.** The symmetric 10·10·5_H coupling needs A₁ and vanishes for A₂.
- **A Higgs in E** (a doublet of doublets). The masses are |a h₊| and |a h₋|. A vacuum that keeps any swap has |h₊| = |h₋|, and one that
  keeps R has h = 0. **They split only if the Higgs vacuum breaks D₃ entirely.**

The pullback three (B1390's only non-cancellation route) is the free ℤ/3's regular representation, one generation per charge.
- **A Higgs of definite charge q.** The symmetric coupling has support i + j + q ≡ 0 (mod 3) and always a degenerate pair. For q = 0
  this is B1362's circulant circ(x, y, y), with masses x + 2y and x − y twice. The 10·5̄ coupling is a permutation texture and is not
  constrained.
- **If a further isometry inverts the deck** (σRσ⁻¹ = R⁻¹), the three generations are S₃'s "2 + 1": a singlet and the doublet E. That
  is the classic starting point of S₃ flavour models (Pakvasa–Sugawara, Phys. Lett. B 73 (1978) 61; the democratic texture, Harari–Haut–Weyers, Phys. Lett. B 78 (1978) 459). Its
  democratic limit x = y gives one massive and two massless generations.

**The verdict for test 4, as posed.** The symmetric geometry fixes a flavour group and its representation on the generations. It does
not fix the ratios: every hierarchy between symmetry partners is a symmetry-breaking effect of a size the geometry does not supply.
This is B1362's lesson for the deck, recovered here for the Eisenstein mechanism's own member and for its only route to three.

## 1. The equivariant index

**Lemma 1 (the character is a Lefschetz number).** Let g be an isometry fixing the Higgs class v. Take the cut M_T invariant: equal
heights on the cusps g permutes. Then g preserves ∂⁺M_T and acts on H*(M_T, ∂⁺M_T), whose Euler characteristic is the frame's count
N. By the Lefschetz fixed-point theorem for pairs, Σ(−1)ⁱ tr(g | Hⁱ) = χ(Fix g ∩ M_T) − χ(Fix g ∩ ∂⁺M_T). So the generations, the
index as a virtual representation, have character χ_V(g) = L(g). ∎

**Lemma 2 (where the fixed points fall).** Let g act on a cusp torus T_c with isolated fixed points and preserve the partition.
- (a) If ∂⁻_c is a single closed disc, g's restriction to it is a periodic map of a disc. By Kerékjártó it is conjugate to a rotation, so
  it has exactly one fixed point there.
- (b) If ∂⁺_c and ∂⁻_c are single annuli and g is an orientation-preserving involution, each annulus holds 0 or 2 of its fixed points:
  the Lefschetz number on an annulus is 1 − (±1), and each isolated fixed point has index +1. So a four-point involution splits 2 / 2,
  provided no fixed point lies on the zero curve. ∎

At the leading modes the proviso holds with room:
- **Cusp 1.** The mode is a single primitive cosine, which is ±a at the involution's fixed points.
- **Cusp 2.** The √3-shell is dominated by one primitive direction: 2.209 against 0.335 + 0.335, B1387.
- **Cusps 0 and 3.** R's three fixed points carry 3|c| cos(φ + 2πm/3) with cos 3φ = 0.370 (B1386, B1387), none of them zero.

## 2. Computed (`verification/flavour.py`, seconds; record `flavour_run.txt`)

**The fixed sets** (B1390's instrument on cube~3.24; |Aut| = |Isom| = 6; the ends match SnapPy's |det(A − I)|):

| element | fixed set | ends on the cusp tori | in ∂⁺ (Lemma 2) | L(g) |
|---|---|---|---|---|
| e | M_T | — | χ(∂⁺) = −1 − 1 + 0 + 0 | **+2** |
| R, R² | 3 arcs, no closed curve | 3 on cusp 0, 3 on cusp 3 | 2 + 2 (∂⁻ is one disc at each) | **−1** |
| each of the three swaps | 4 arcs, no closed curve | 4 on cusp 1, 4 on cusp 2 | 2 + 2 (annular at each) | **0** |

The character is (2, −1, 0) on the classes (e, R, swap), and its decomposition is 0·A₁ + 0·A₂ + **1·E**. A twist of the isometries'
lift to the bundle by a character of D₃ leaves this unchanged (E ⊗ A₂ ≅ E).

**The textures** (sympy, exact):

| representation of the generations | Higgs | covariant Yukawa | singular values |
|---|---|---|---|
| E (cube~3.24) | A₁ | [[0, y], [y, 0]] (symmetric) | \|y\|, \|y\| |
| E | A₂ | [[0, −y], [y, 0]] (antisymmetric: no 10·10·5_H) | \|y\|, \|y\| |
| E | E, vacuum (h₊, h₋) | diag(a h₊, a h₋) in the basis (e₊, e₋) | \|a h₊\|, \|a h₋\|; equal on any swap-invariant vacuum |
| ℤ/3 regular (pullback three) | charge 0 | [[y₀, 0, 0], [0, 0, y₅], [0, y₅, 0]] = circ(x, y, y) in the permutation basis | \|y₀\|, \|y₅\|, \|y₅\| |
| ℤ/3 regular | charge 1 | [[0, 0, y₂], [0, y₄, 0], [y₂, 0, 0]] | \|y₄\|, \|y₂\|, \|y₂\| |
| ℤ/3 regular | charge 2 | [[0, y₁, 0], [y₁, 0, 0], [0, 0, y₈]] | \|y₈\|, \|y₁\|, \|y₁\| |

The last three rows hold for the symmetric (up-type) coupling. The non-symmetric 10·5̄ coupling is a permutation texture with three
independent entries.

**How common the 2 + 1 structure is** (`flavour.py deck`, about a minute). Of B1386's 184 members (ocube06_08812 and its covers of
degree 2 and 3):
- 142 have an order-3 isometry that rotates no cusp, so it acts freely (B1390);
- 115 have one that another isometry inverts, for instance ocube06_08812 itself (|Isom| 18) and all seven degree-2 covers.

The symmetry a "2 + 1" needs is therefore common. The binding condition for a pullback three is |N| = 1 on the quotient.

## 3. What this settles, and what it does not

**Settled (test 4 at the symmetric point).**
- **Neither member of the record gives a hierarchy by itself.** The frame's generations carry an isometry representation (a flavour
  group), and the representation leaves degenerate masses on every member the record has.
  - cube~3.24: complete degeneracy of its two generations.
  - The pullback three: a degenerate up-type pair.
- Every Yukawa log-ratio between symmetry partners is set by the breaking, which the geometry does not supply. **0 of 19.**

**Positive structure, recorded not claimed.**
- The frame *derives* its flavour group from the manifold's isometries: D₃ ≅ S₃ on cube~3.24.
- The pullback three with a deck-inverting symmetry would realise S₃'s "2 + 1", a pattern the phenomenology literature has long used
  as a leading-order start (heavy singlet, light doublet).
- The symmetry is common (115 of B1386's 184 members). Whether any quotient carries |N| = 1 is open, as is the level (sL-5).

**Not settled.**
- The Higgs doublets' representations: they are vector-like, index 0 (B1372), so the index does not fix them.
- The vacuum.
- The overlap integrals that would give the ratios once the symmetry is broken.
- sL-8 (which count, which completion, the anomaly).
- The spin-½ half.

## 4. Fences

- **The frame's.** Spin-0 half; the 27-frame (B1389) for "generation". The theorem is about the relative index at invariant cuts and
  at the leading modes, where the two counts of B1388 agree.
- **Tree-level, symmetric point.** The Yukawa couplings are D₃-covariant tensors because D₃ is a symmetry of the compactification's
  data (the metric, v₊, the bundle). Radiative or non-perturbative effects that break it are outside.
- **The textures.** Schur's lemma and the exact symbolic solutions. The phenomenology references are context, not claims.

## 5. Prior art (swept before banking)

Both branches were swept: this one at 57d2bcdf, origin/main at 987c0c8f. The sweep used git grep for "flavour symmetry", "S₃ flavour",
"D₃ doublet", "equivariant index", "family symmetry" and "Lefschetz number", plus `already_banked.py` on "flavour symmetry doublet
generations isometry".
- **B1362**: a deck-symmetric symmetric Yukawa is circ(x, y, y) with a degenerate pair. It is cited for the pullback three and
  extended here to every Higgs charge.
- **B1361 and B1273**: the deck's hollow texture from three distinct characters.
- **B1255**: over ℚ(√−3) three-ness comes as conjugates or gradings, never copies. B1390's dichotomy is its geometric counterpart:
  rotation or free action.
- **B1033's addendum**: SU(3)_F as a global family symmetry.
- **No arc** computes the isometry representation of the frame's generations, or derives a flavour group from a member's isometries.
