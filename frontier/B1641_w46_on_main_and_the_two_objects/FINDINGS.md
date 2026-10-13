# B1641 — W46 ON MAIN, AND THE TWO OBJECTS: the fibre loops of M₁,₂ act on the matter by the parity signs under the only lifts that agree with the ruled moves (the geometric lift, trivial on cohomology, differs from them by the central sign at Δ⁴); so couplings obey a parity selection rule — diagonal for a parity-blind Higgs, the golden pattern for a Higgs carrying parity; the SM seat's W46 index table is verified on main; the hand is not tied to the puncture condition at the representation level

**Verdict: PROVED.** Every predicted cell holds (O1, O2, O3, W1, W2, W3). The read-out cell H came out "neither", which by
its sealed rule refutes the reading that the hand is the puncture condition's orientation at the representation level.
cc (main), 2026-10-13. Sealed `99975fb63` before the run. No data. **0 of 19.** POINT_REGISTER slot Q2.

## 0. Seen first

As sealed: `VERDICT topic-sweep /W46|point-push|fibre loop|fiber loop|Birman|central extension|inner automorphism|puncture condition/: 10 of 1412 arcs on main match (NEGATIVE 2, PROVED 8)`.
Also read before the seal:
- B1634, B1617 and B1630;
- the SM seat's W46 rule and NOTE section, and its W56 rule;
- the Banking Seat's Gates 11 and 12;
- the frame audit's referee reports.

A smoke run of the imports and matrix shapes, with no read-out, preceded the seal (disclosed there).

**Literature:** the Birman exact sequence (point-pushing as the kernel of the forgetful map on mapping class groups);
Borcherds and Skoruppa's dimension formula for vector-valued modular forms, as used in B1632; the cohomology of a group
with a module on which inner automorphisms act through the module itself (standard).

## 1. The sealed run (`verification/w46_on_main.py`, unchanged; `w46_on_main.json`, `w46_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **O1** | conj(a), conj(b), conj(c) on V: the record's uniform lift gives ±(the parity signs); the block-wise geometric lift M_p(c) = χ_p(c)ρ_Q(c) gives the identity | 90% | **HOLDS.** The record's lift gives +parity for a and b (signs (−1, 1, −1) and (1, −1, −1) on the three blocks) and −I for c = a b⁻¹ a⁻¹ b. The geometric lift gives the identity on V and on T, all three times. |
| **O2** | Δ⁴ by the moves is −I on T; conj(c) by the geometric lift is +I; they differ by −1 | 85% | **HOLDS.** Δ⁴ = (L R⁻¹ L)⁴ is the inner automorphism by a b⁻¹ a⁻¹ b, the only reduced word to length 6. The moves' product on T is −1.000000000000001·I. The geometric conj(c) on T is +I. ρ_Q(c) = −1. |
| **O3** | the parity selection rule; c a one-dimensional piece of ρ_θ^{⊗3} with η⁶'s character; c(u, u, u) = 24η⁶ | 85% | **HOLDS.** The invariants of T ⊗ T are 3-dimensional (the diagonal) and those of T ⊗ T ⊗ T are 6-dimensional (distinct triples only); c's character is S ↦ i, T ↦ i; c(u, u, u) = 24η⁶ to 2.4·10⁻³⁰ at 5 random τ. The identity of form c(·, ·, u) = the golden coupling holds, as it must. |
| **W1** | main's L₆: braid; exponents (⅛, ⅛, ⅜, ⅝, ⅞, ⅞); pieces of dimension 2 and 4 | 80% | **HOLDS.** Braid relation; two valid identifications (S = S̃, T = L and their inverses); exponents (1, 1, 3, 5, 7, 7)/8; commutant of dimension 2, pieces of dimension 2 and 4. |
| **W2** | χ₁ = 0 on the pieces and L₆; χ_{3/2}(ρ_T) = 0 = χ_{1/2}(ρ̄_T); η² calibrates to 1 | 85% | **HOLDS** in both identifications; weight 1 allowed in both. |
| **W3** | index(Λ₊, n) = n(\|Λ₊\| − 3) | 80% | **HOLDS.** The table is +3, 0, −3 for Λ₊ = 0; +1, 0, −1 for V2; −1, 0, +1 for V4; −3, 0, +3 for L₆ (n = −1, 0, 1), in both identifications. |
| **H** | read-out: ρ_T or ρ̄_T (up to a character) as a sub or quotient of ρ₆ | — | **Neither**, in both identifications. The commutant has dimension 2, so ρ₆ is the sum of two non-isomorphic irreducibles of dimension 2 and 4, and no 3-dimensional constituent exists. |

## 2. What it says

- **The two objects are one, with a parity selection rule.**
  - On M₁,₂ the fibre loops (point-pushes) are the inner automorphisms.
  - The lift of them that agrees with the ruled moves at Δ⁴ is the record's. Under it, conj(a) and conj(b) act on T by the
    parity signs and conj(a b⁻¹ a⁻¹ b) by −1, exactly the moves' Δ⁴.
  - The geometric lift, under which point-pushing acts trivially on the fibre's cohomology, differs from the moves by the
    central sign at Δ⁴. So the matter cannot be fibre-blind and carry the ruled moves at once. It is "spinorial" around
    the commutator loop, and the Banking Seat's Gate 11 obstruction (Δ⁴ = −I₃) is this sign.
  - **The consequence for couplings:**
    - a parity-blind Higgs allows only diagonal couplings;
    - a Higgs carrying parity (in T) allows exactly the off-diagonal pattern, the golden coupling's;
    - c(u, u, u) = 24η⁶ ties that pattern to the θ-triplet itself.
  - Whether a Higgs in T is allowed at the geometry's weight is the SM seat's W56 (P-083), not this arc's.
  - B1635's count on the ruled branch, which ignored the fibre loops, is refined accordingly: on M₁,₂ the coupling
    space is cut by the parity of the Higgs.
- **W46 is verified on main.** On main's own lifts, with main's χ formula:
  - L₆'s structure, every χ₁ = 0 and χ_{3/2}(ρ_T) = 0;
  - the table n(|Λ₊| − 3), so given Λ and n units at the cusp, the four-dimensional index is n times the fibre's index.

  The census's first verification debt is paid; GENESIS v1.37's "with W46" now rests on main.
- **The hand is not the puncture condition's orientation at the representation level.** ρ₆ = V2 ⊕ V4 with both pieces
  irreducible, so neither ρ_T nor ρ̄_T is a sub or a quotient.
  - W46's exact sequence 0 → H⁰ ⊗ λ⁻¹ → L₆ ⊗ λ^{−1/2} → H¹ → 0 is therefore not a sequence of these representations up
    to characters. It holds, if at all, at the level of sheaves on M₁,₁.
  - P-079's shortcut (the hand is the sign of ±3) is refuted at that level; the sheaf-level reading stays the seat's.

## 2b. Post-seal, labelled: the SM seat's W56 parity argument (POINT_REGISTER P-083)

On main's ρ_T (B1634's convention: ρ(S) = lift(S̃)⁻¹), ρ_T(S)² = i·I exactly. A coupling form of weight k in a
representation R needs R(S)² = e^{−iπk}.
- **A Higgs exactly like a generation.** (conj ρ_T)^{⊗3} has (−i)³ = i, so k ≡ 3/2 (mod 2), and the geometry's total
  weight 9/2 is excluded.
- **A Higgs in the dual triplet.** conj ρ_T ⊗ conj ρ_T ⊗ ρ_T has −i, so k ≡ ½ (mod 2), and 9/2 is allowed.

So W56's rule-stage claim holds on main, by arithmetic from one checked scalar, within the record's hand. Under the
conjugate hand (B1640 cell B) the scalar is −i and the matter's allowed weight changes with it, so the statement is
hand-relative. This check is not blind: it was run after W56's rule was read. W56's fits stay the seat's until they
land.

## 3. Disclosed

- W46's numbers were seen before the seal; the W cells check them on main's construction and are not blind.
- O1–O3 are blind and were derived by hand before the seal; H's rule was stated before the run.
- The block-wise geometric lift is defined in this arc; that point-pushing acts trivially on fibre cohomology with it
  is the standard fact the arc confirms. The claim that only the record's lift agrees with the moves rests on the Δ⁴ check
  alone; a full coherence check of lifts for all of Aut⁺(F₂) is the Banking Seat's Gate 12 (P-074).
- c(·, ·, u) = golden coupling is an identity of form.

## 4. Files

`verification/w46_on_main.py` (sealed, unchanged), `w46_on_main.json`, `w46_run.txt`; the lock
`tests/test_b1641_w46_on_main_and_the_two_objects.py`.
