# B1641 — PREREGISTRATION: W46 ON MAIN, AND THE TWO OBJECTS — do the fibre loops of M₁,₂ act on the matter, and what selection rule do they leave?

cc (main), 2026-10-13. **Sealed before `w46_on_main.py` runs.** No data. 0 of 19. POINT_REGISTER slot Q2 (P-017, P-018,
P-019, P-079, P-080; P-074 and P-083 in part).

**Why it matters.**
- The record puts the chiral ±3 on M₁,₂ (W45, W46; GENESIS v1.37–v1.41, "given Λ and the unit"). M₁,₂'s fibre loops are
  point-pushes, which are the inner automorphisms of F₂.
- B1634 excluded those inner automorphisms from the moves on the ruled branch, where the couplings live (B1635–B1639).
  The frame audit (B1640) named this two objects for one chain.
- Two outcomes are possible. If the fibre loops act on the matter T by the parity signs, a parity-blind Higgs allows only
  diagonal couplings. If they act trivially, M₁,₂ and the ruled branch agree on T, and W46's index needs recomputing only
  in its own terms.
- W46 itself (the index table n(|Λ₊| − 3)) is the most-relied-on result main has never recomputed (census §2, item 1).

**The derivation, by hand, written before the run.**
1. **V and its fibre.** V = ⊕_p H¹(F₂; χ_p ⊗ ρ_Q), where ρ_Q is the quaternion representation (a ↦ i, b ↦ j) and χ_p
   runs over the three non-trivial characters of H₁(F₂; ℤ/2). An automorphism m acts by z ↦ g⁻¹(z ∘ m), given an
   intertwiner g with ρ ∘ m = Ad(g) ρ. The record (B1600's `move_matrix`, B1617's `lift_of`) uses one 2O element g for
   all three parity blocks.
2. **The geometric lift of a fibre loop.** For m = conj(c), the module's own action M_p(c) = χ_p(c) ρ_Q(c) is an
   intertwiner on block p. For a cocycle z,
   M_p(c)⁻¹ z(c x c⁻¹) = z(x) + (1 − M_p(x)) M_p(c)⁻¹ z(c),
   which differs from z by a coboundary. **So with the block-wise geometric lift every inner automorphism acts on V as the
   identity.** With the record's uniform lift g = ρ_Q(c), it acts on block p as χ_p(c): the parity signs.
3. **The central sign at Δ⁴.** Δ⁴ = conj(c) with c = a b⁻¹ a⁻¹ b (B1634). Then χ_p(c) = 1 and ρ_Q(c) = i(−j)(−i)j = −1.
   - Geometric lift: the identity on V.
   - Product of the move lifts: −I on T (B1634).
   So the geometric fibre loops and the ruled moves' lifts do not form one representation of Aut⁺(F₂) on T. They differ
   by the central element −1 at Δ⁴. This is the Banking Seat's Gate 11 obstruction (Δ⁴ = −I₃), computed directly.
4. **The selection rule.** If the fibre loops act by the parity signs:
   - The invariants of T ⊗ T are the diagonal e_p ⊗ e_p.
   - The invariants of T ⊗ T ⊗ T are e_p ⊗ e_q ⊗ e_r with χ_p χ_q χ_r = 1, i.e. p, q, r distinct. The symmetric one is
     c_pqr = 1 on distinct triples.
   - c(·, ·, u(τ)), with u = (θ₂², θ₃², θ₄²), is exactly B1636's golden coupling [[0, θ₄², θ₃²], [θ₄², 0, θ₂²],
     [θ₃², θ₂², 0]]. This needs the right order of u's entries on the parity lines (θ₃² on the clock's line, B1634).
   - In ρ_θ's own coordinates c spans a one-dimensional subrepresentation of ρ_θ^{⊗3} with η⁶'s character (S ↦ i,
     T ↦ i), and c(u, u, u) = 6 θ₂²θ₃²θ₄² = 24 η⁶ by Jacobi's θ₂θ₃θ₄ = 2η³. **So a parity-blind Higgs gives diagonal
     couplings only, and a Higgs in T gives exactly the golden coupling's pattern.** (That c(·, ·, u) is the golden
     coupling is an identity of form, not a finding.)
5. **W46 on main.**
   - The six local solutions are L₆ = ⊕_u ℂ²_u, the stalk of 𝕎 (the seat's W24 `blocks_action`). A move m with lift g sends
     block (u ∘ m) to block u by g. Main rebuilds this from its own lifts.
   - The checks: the exponents of ρ₆(T) (W46: ⅛, ⅛, ⅜, ⅝, ⅞, ⅞ with the record's lifts); invariant subspaces of dimension
     2 and 4; χ₁ = 0 on each; χ_{3/2}(ρ_T) = χ_{1/2}(ρ̄_T) = 0 by main's Borcherds–Skoruppa formula (B1632). The index
     table: index(Λ₊, n) = −χ_{3/2+12n}(ρ_T) + Σ_{pieces ⊆ Λ₊} χ_{1+12n}(ρ_piece) = n(|Λ₊| − 3).

## Seen first

`VERDICT topic-sweep /W46|point-push|fibre loop|fiber loop|Birman|central extension|inner automorphism|puncture condition/: 10 of 1412 arcs on main match (NEGATIVE 2, PROVED 8)`
— B1634 (⟨L, R⟩ ∩ Inn(F₂) = ⟨Δ⁴⟩; Δ⁴ = −1 on T), B1617 and B1630 (the inner automorphisms as parity signs), B1640.
Also read before this seal:
- the SM seat's W46 rule and its NOTE section (the table, the exponents, V2 and V4, "T is a pullback, so its monodromy
  is the inverse");
- the Banking Seat's Gate 11 headline ("Δ⁴ = −I₃ obstructs the sign's extension") and its Gate 12 proposal;
- the frame audit's referee reports (the two objects).
- **the SM seat's W56 rule** (d8599653d, before its run): a Higgs exactly like a generation (conj ρ_T at 3/2) has no
  coupling form at the geometry's weight 9/2, the dual triplet is allowed, and in the E₆ frame no Higgs in 27s splits d
  from e. This arc does not test the Higgs's weight; that is W56's, and main verifies it separately (POINT_REGISTER
  P-083).

**Literature:** the Birman exact sequence (point-pushing); Borcherds and Skoruppa's dimension formula for vector-valued
modular forms (as in B1632).

## Disclosed

- **A smoke run before the seal** loaded the imported modules and checked matrix shapes only (no cell read-out).

- **W46's numbers are seen.** The W cells check them on main's own construction; they are not blind.
- **The blind cells are O1–O3 and H.** O1–O3 have predictions derived above by hand. H is a read-out with its reading
  rules stated in advance.
- **The order of u's entries on the parity lines is B1634's** (θ₃² on the clock's line). O3 uses it.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **O1** | conj(a), conj(b), conj(c) act on V: (i) with the record's uniform lift as ±(the parity signs χ_p) block by block; (ii) with the block-wise geometric lift M_p(·) as the identity, to 1e-12 | 90% |
| **O2** | Δ⁴ as the product of the move lifts is −I on T (B1634 reproduced); conj(c), c = a b⁻¹ a⁻¹ b, with the geometric lift is +I on T. So the moves' lifts and the geometric fibre-loop lifts differ by −1 at Δ⁴: they do not form one representation of Aut⁺(F₂) on T | 85% |
| **O3** | (a) under the parity action (diag χ_p on the parity lines, modulo the central sign of O1–O2): the semi-invariants of T ⊗ T are the 3-dim diagonal; of T ⊗ T ⊗ T the 6-dim span of distinct triples, whose symmetric part is 1-dim = c. (b) In ρ_θ's own coordinates (the pure θ² multiplier ρ(S) = −i P₁₃, ρ(T) = diag(i, 1, 1) P₂₃ on (θ₂², θ₃², θ₄²)), c spans a one-dimensional subrepresentation of ρ_θ^{⊗3} with character S ↦ i, T ↦ i (η⁶'s), and c(u, u, u) = 24 η⁶ at 5 random τ to 1e-12 (Jacobi). (c) A consistency check, an identity of form: c(·, ·, u(τ)) is B1636's golden coupling | 85% |
| **W1** | main's L₆ from its own lifts: the braid relation holds; ρ₆(T) has exponents (⅛, ⅛, ⅜, ⅝, ⅞, ⅞); invariant subspaces of dimensions 2 and 4 exist | 80% |
| **W2** | for every valid identification (S, T) of the six at which weight 1 is allowed (ρ₆(S)² = −I): χ₁ = 0 on the 2-dim piece, the 4-dim piece and L₆; χ_{3/2}(ρ_T) = 0 = χ_{1/2}(ρ̄_T) (B1634's ρ_T); calibration η² gives χ₁ = 1 | 85% |
| **W3** | the table index(Λ₊, n) = n(|Λ₊| − 3) for Λ₊ ∈ {0, V2, V4, L₆}, n ∈ {−1, 0, 1} | 80% |
| **H** | READ-OUT: whether ρ_T and ρ̄_T, each up to a scalar character, occur as a subrepresentation or a quotient of ρ₆. Rule: if exactly one of them occurs as a sub, it is the puncture condition the hand belongs to; if both or neither occur, the hand is not tied to the puncture condition at the representation level | — |

**The reading, written before the run (the cells can only lower it).**
- **If O1–O3 hold.** M₁,₂'s fibre loops act on T trivially as geometry and by the parity signs as the record lifts them,
  and the two differ by the central sign at Δ⁴. The ruled branch's lifts are the ones with the sign (B1634).
  - Read physically: the matter is "spinorial" around the commutator loop.
  - The selection rule the parity action leaves: diagonal couplings for a parity-blind Higgs, the golden pattern for a
    Higgs in T, as a pattern only. Whether a Higgs in T is allowed at the geometry's weight is W56's question (P-083),
    not this arc's.
  - So the two objects are one, with the Higgs's parity content as the free datum. That is W55's "the Higgs sector's
    flavour structure".
- **If O1(ii) fails** (the geometric lift does not act trivially), the cocycle algebra in step 2 is wrong as applied, and
  this arc names where.
- **If W1–W3 hold,** W46 is verified on main and leaves the census's verification debt.

## Instruments

`verification/w46_on_main.py`, importing B1600's `w10_check.py` (`move_matrix`, `rep`, the bases), B1617's `lift_of`,
B1632's `chi`, and B1635's forms for O3; hashes in `ARTIFACT_HASHES.txt`.
