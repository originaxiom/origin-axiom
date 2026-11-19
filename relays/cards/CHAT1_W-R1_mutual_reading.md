# Card W-R1: mutual reading. Can two records read each other, and does the reading carry a magnitude?

**Seat:** the web seat (chat1). **Opened:** 2026-11-19, at the author's word that day, after a conversation on the
programme's wall. Written and committed before any of its numbers is computed. **Kind:** `result:` data-free. Nothing is
set beside a measured number.

**The idea, as this seat states it** (a reading; the idea is the author's). The programme has records and no reader:
the read-out (I-33) is chosen, not derived. One answer from outside physics is that existence is a shared awareness. In
this programme's terms that would mean records that read each other, where what exists is what their readings agree
on. A non-cancellation principle forces structure and prefers no size. A reading is a positive act, and a pairing can
carry a number. So the question is whether a reading the records make of each other supplies a magnitude.

---

## 1. What the record already decides (the sweep, at main 24a478df2)

**Records.**
- **B1675** (PROVED): a record that its own motion keeps fixed exists only at an end. A shear (L or R) or the mirror
  keeps a private class. No thread does, and neither does the weave's joint action. Its last clause left a relational
  record open: whether the moves admit a non-zero equivariant map Hom_G(W, V).
- **B1717** (PROVED; P-278 DONE): **the plan's first test is done.**
  - On B1675's private modules V₂ (dimension 4) and V₃ (dimension 2), the moves act irreducibly (Burnside). The
    commutants are the scalars, Hom_G(V₂, V₃) = 0, and the coefficient module maps into neither.
  - Its scope: k ≤ 3, linear maps only. Higher k, tensor products and other coefficients are not computed, and
    bilinear pairings are not computed at all (its script solves only A X = X B).
- **This seat's W-C3** reproduced B1675 exactly with its own code (`relays/chat1_2026-11-11_wc3/`):
  - L and R each keep one private class at k = 2, none at k = 3;
  - the mirror P keeps two at k = 2 and one at k = 3.

**Selection.**
- **The group-wall theorem** (B1327's no-go, B1881 (A), this seat's walls note of 2026-11-11): a condition the moves
  respect has a solution set the moves carry to itself. So it cannot single out a point of its own orbit.
- **B1327** (OPEN) names the way around it: not an observer but a second relatum. An invariant of a pair needs a
  partner, not an act. This is its type R.
- **The plan's second test is decided by these.** B1687 (PROVED) shows the moves generate the whole one-qubit Clifford
  group modulo phases (Aut(Q₈) = S₄). So no condition two Pauli frames satisfy together, and the moves respect, picks
  out an axis. It can fix only the frames' relative position, which is type R. Nothing is computed for it here.

**Earlier readings of the observer.**
- **B1614** (the earlier "awareness arc"): the weave names itself but cannot sign itself.
- **B1169 and B1184:** the object cannot close itself; its boundary sees everything and chooses nothing.
- **B1750:** the observer re-typed as closer (retired), signer (unit and orientation, conventions) and identifier (the
  identification ledger).
- **P-204:** the author's argument that existence belongs to the whole system of acts and their relations. Main adopted
  its distinction test.
- **P-177:** the author's "the interaction is the reality"; item 5 is still open.
- **This seat's door-C relay (2026-11-06, § 6):** the author's teller and listener. There the listener only conditions
  which lifts pass, a selection and not a back-action.

**What is untested.** A pairing between two records. Each record evaluates the other, and the moves keep the value. The
two records can be of one module or of two, and they can be the two ends' own records. B1717 asked whether one record
maps into another; it never asked whether two records read each other.

## 2. The principle as mathematics

- **Records:** B1675's private classes, V_k = the kernel of H¹(F₂; Sym^{2k} ρ_Q) → H¹(⟨c⟩; Sym^{2k} ρ_Q), at the common
  point ρ_Q (a ↦ i, b ↦ j), with the moves acting as in W-C3.
- **A reading of V_k' by V_k:** a bilinear form B: V_k × V_k' → ℂ.
- **A mutual reading that the weave keeps:** B(gx, gy) = B(x, y) for every move g. The space of these is
  Hom_G(V_k, V_k'^*).
- **What exists, on this reading:** the invariants of pairs. That is B1327's type R, now with a definite number per pair.
- **The two records of the ends:** x_L, the private class L keeps, and x_R, the one R keeps. Their mutual reading is
  B(x_L, x_R).

## 3. The derivation, written before computing

At the common point ρ_Q has finite image Q₈. So Sym^{2k} ρ_Q splits into Q₈'s characters.
- The trivial part, M_k = (Sym^{2k} ℂ²)^{Q₈}, has dimension m₀(k) = ((2k + 1) + 3(−1)^k)/4: that is 0, 2, 1, 3, 2, 4 for
  k = 1 to 6.
- A non-trivial character χ has H¹(F₂; χ) of dimension 1, restricting injectively to the puncture (χ([a, b]) = 1). So it
  adds nothing private.
- The trivial part contributes H¹(F₂; ℂ) ⊗ M_k, and all of it is private, since a cocycle with trivial coefficients
  vanishes on a commutator.

**So V_k ≅ St ⊗ M_k,** with dimension 2m₀, matching B1675's "private = 2m₀". Here St = H¹(F₂; ℂ) = ℂ².
- A move acts on St by its own matrix: the action on the torus's first cohomology. L is [[1, 0], [1, 1]] in the basis
  (z(a), z(b)).
- It acts on M_k through Out(Q₈) = S₃, by its normalised lift. Inner automorphisms, −I among them, act trivially on M_k.

This is B1675's "why" ("a thread acts on the private states as its hyperbolic matrix tensored with a map of finite
order"), made exact. It reproduces every number in § 1:
- L is unipotent on St and an involution on M_k, so it fixes e ⊗ M_k^{L}: 1 at k = 2 and 0 at k = 3 (M₃ is S₃'s sign).
- P swaps the cohomology basis and is an involution on M_k, so it fixes a space of dimension dim M_k: 2 and 1.
- B1717's commutants follow: M₂ is S₃'s irreducible 2, and M₃ its sign.

**Predictions.**
- **P0.** For every k ≤ 6 there is an invertible G-equivariant map St ⊗ M_k → V_k, for G = ⟨L, R, P, −I⟩. St and M_k are
  computed by their own routes, the first from the moves on Hom(F₂, ℂ), the second from the lifts on Sym^{2k} restricted
  to Q₈'s fixed vectors.
- **P1.** dim End_G(V_k) = dim End_{S₃}(M_k), and dim Hom_G(V_k, V_k') = dim Hom_{S₃}(M_k, M_k'), for every k, k' ≤ 6.
  - M_k's characters, from the octahedral group on the spin-k representation, give M₁ = 0, M₂ = σ, M₃ = ε, M₄ = 1 ⊕ σ,
    M₅ = σ and M₆ = 1 ⊕ ε ⊕ σ. Here 1, ε and σ are S₃'s trivial, sign and two-dimensional representations.
  - So dim End_G(V_k) is 1, 1, 2, 1, 3 for k = 2 to 6.
  - Hom_G(V_k, V_k') is 1 between any two of V₂, V₄, V₅ and V₆; 1 between V₃ and V₆; 2 between V₄ and V₆; and 0
    otherwise.
  - These are linear relational records between different k, beyond B1717's range.
- **P2.** The ⟨L, R⟩-invariant bilinear forms between V_k and V_k' are exactly ω_St ⊗ (the S₃-invariant bilinear forms
  between M_k and M_k'), with ω_St the symplectic form of St.
  - Their dimension is dim Hom_{S₃}(M_k, M_k').
  - On V_k with itself they are alternating (S₃'s representations are real) and, where M_k is irreducible,
    non-degenerate. This is the intersection pairing of the punctured torus.
  - P reverses orientation, so each such form is P-anti-invariant. Under ⟨L, R, P, −I⟩ none is invariant.
- **P3, the ends read each other.**
  - L and R each act on M_k as a transposition, two different ones. So L keeps a space of dimension
    dim M_k^{L}: 0, 1, 0, 2, 1, 2 for k = 1 to 6, and R the same.
  - Where that space is a line (V₂ and V₅), B(x_L, x_R) ≠ 0 for the invariant form: the two ends' records read each
    other.
  - Its scale-free values are fixed by S₃ and SL(2, ℤ). The run computes two, predicted now:
    - R₁ = B(x_L, R²x_L)/B(x_L, R x_L) = −4;
    - R₂ = B(x_L, x_R)²/(B(x_L, P x_L)·B(x_R, P x_R)) = −1.
  - The derivation of these: on St the forms give −2/−1; on σ the fixed lines of two reflections meet at 60°, so the
    reflected line makes 120°; and P carries x_L to a multiple of x_R.

## 4. The test (one sealed script, exact)

On the weave's private modules, k = 1 to 6, computed by extending W-C3's code (`w34_private_states_amendment_1.py`,
imported unchanged):
- **T1.** For G = ⟨L, R⟩ and G = ⟨L, R, P, −I⟩: the dimensions of End_G(V_k), Hom_G(V_k, V_k') and the invariant bilinear
  forms, with each form's symmetric and alternating parts and its rank; P's sign on each; Burnside's dimension of the
  algebra the moves generate on V_k.
- **T0, P0's check.** St and M_k by their own routes; the dimension of Hom_G(St ⊗ M_k, V_k), and whether it contains an
  invertible map. M_k's decomposition under S₃ is computed from characters.
- **T2.** In each V_k: L's and R's fixed spaces, B(x_L, x_R) for each invariant form, and the fixed list of scale-free
  ratios, exact.

**Controls.**
- **C1:** W-C3's numbers come out again for k ≤ 3: dimensions (0, 4, 2); L, R, P keeping (0, 0, 0), (1, 1, 2),
  (0, 0, 1).
- **C2:** B1717's: End_G(V₂) = End_G(V₃) = 1, Hom_G(V₂, V₃) = 0.
- **C3, a positive control:** End_G(V₂ ⊕ V₂) = 4.
- **C4:** at a random irreducible pair (W-C3's K1), where Sym^{2k} has no finite image, the invariant forms on the
  private module are computed and reported. That is the generic case, outside the derivation.

**Expected [J].** P0, P1, P2 and P3 hold, and every control holds.

## 5. What each outcome means

- **If P0 to P3 hold.**
  - Two records can read each other. The ends' records do, and records of different k are tied by linear maps (V₂ to V₄
    and V₅).
  - But every relation the weave keeps between its private records is the one symplectic form of the torus times
    finite-group data of S₃.
  - So every number a mutual reading of them makes is algebraic and fixed by the group: a constant, not a magnitude
    that could set τ or a mass.
  - On the weave's own records, the silence on magnitudes is the group's, not a missing reader. The idea is not
    retired, but this, its first and cheapest setting, is.
- **If P0 fails** (V_k is not St ⊗ M_k for some k), the private records carry structure the derivation missed. That
  structure is what the next sealed test would read.
- **If any scale-free reading is not a finite-group constant**, the hint has paid. The next step is a sealed test of
  whether that number removes a counted choice.

## 6. Not in scope, and next

- Readers in other modules: the matter triplet T, the coefficient module ρ_Q's odd blocks, the frame's couplings.
- A reader of the frame: the read-out I-33 itself, and two frames reading each other, such as the two vacua S and S̃
  (P-177's open item).
- Data, of any kind.

0 of 19.
