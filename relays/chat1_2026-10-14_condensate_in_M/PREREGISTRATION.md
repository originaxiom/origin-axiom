# The cusp condensate's direction in M: the owed test (chat1, 2026-10-14). Sealed before any code that computes it.

**Why.**
- The owner's ruling of 2026-10-14 (09:01) chose the audit lane's cusp condensate as the field's origin and owed two
  tests, rule first: its mirror image, and **the direction it picks in M**.
- The SM seat's W70 and W71 ran other tests: the condensate's charges, and the field-free end. This one is still owed.
- The owner asked chat1 for it: "continue with the decisive test".
- chat1's relay of the same day (`CHAT1_TO_CC_2026-10-14_THE_FIELD.md`, §4.3) predicted, with prior 50%: if the
  condensate's quaternion-SU(2) part is a tame residue at an unfiltered genuine cusp, it is null, and W64's leading order
  follows with no potential.

**Seen first** (read before this seal; repo first).
- The audit lane's `weave_field_map_2026_10_14/PROOF.md`:
  - the quaternion embedding is a conjugate of I₃ ⊗ ρ_Q in SU(6), with puncture commutator −I₆;
  - Ad(puncture) = Ad(weak centre) on all of E₈;
  - weak singlets are puncture-even and weak doublets odd;
  - "Nor does the C_p matrix alone exhibit a weak-doublet gauge Higgs".
- The audit lane's `weave_cusp_condensate_2026_10_08`: the condensate is one per p-odd root (112), as the root sl₂ with
  A_x = −H/(4y) and q = E/(2√y).
- The SM seat's W70 and its rule:
  - 6 = ρ_Q ⊗ 3 in blocks (b, a, ab);
  - the six admissible hypercharges are block-scalar;
  - four neutral Higgs-like condensates per Y;
  - the lane's α = e₃ + e₅ has SU(6) weight ws₀ + ws₁ + ws₄.
- The SM seat's W71 and P024.
- B1644: a quaternion-doublet Higgs cannot couple, while one in the adjoint, M, can.
- W63 and W64: M, with the moves acting through O, and the isotropic lines.
- P-108: a parent map is owed, because this embedding's weak doublets have odd quaternion centre.

**Instrument.**
- W70's own script, copied verbatim as `w70_lib.py` from the SM seat at `d73c539b0` (sha256 d0954826…). The roots,
  chain, weights, h_Q, colour, weak and admissible hypercharges are all used from it unchanged.
- New code (`condensate_in_M.py`) does only the projections and the classification below. It is exact, in rationals.

**The two readings of "M"**, both fixed now so the test cannot be dodged by definition:
- **Reading A, B1644's M:** the adjoint of the quaternion structure. In the lane's embedding that is su(2)_Q = I₃ ⊗ ρ_Q
  inside su(6): Cartan h_Q, raising roots ws₂ᵣ − ws₂ᵣ₊₁ (r = 0, 1, 2), taken diagonally.
- **Reading B, W70's "three quaternion units":** the block space 3_B of 6 = ρ_Q ⊗ 3_B, the blocks (b, a, ab), with
  SU(3)_B acting on it.

| | prediction | prior |
|---|---|---|
| Q0 (control) | W70's N1 and N4 reproduce through `w70_lib`: 240 roots; 112 p-odd = weak doublets; 40 colour-singlet doublets; for each of the six admissible Y, four neutral colour-singlet doublets with \|Y\| = ½ | 97% |
| A1a | su(2)_Q is a complete Standard Model singlet in this embedding: its roots and h_Q are orthogonal to the colour roots and to the weak axis, and Y vanishes on it for all six admissible Y. **So B1644's Higgs in M is no weak doublet here** | 95% |
| A1b | **The first cell.** No condensate has an M-part: none of the 112 p-odd roots is a root of su(2)_Q, so E_α ⊥ su(2)_Q for all 112 | 99% |
| A1c | The backreaction H_α = α (the sl₂ Cartan in A_x = −H_α/(4y)) has a non-zero M-component, along h_Q, for all 112 (α·h_Q is odd). It is real, so never isotropic | 97% |
| B1 | Under SU(2)_Q × SU(3)_B every p-odd root carries an integer (real) block weight: ±e_r for the 6-type roots, e_r − e_s (r ≠ s) or 0 for the 20-type | 95% |
| B2 | For each admissible Y, the four neutral Higgs-like condensates have block roots ±(e_r − e_s), with {r, s} the two blocks whose Y is not −5/6 | 85% |
| V (verdict) | Under neither reading does any single root condensate supply a non-zero complex null vector in M. **The condensate picks no isotropic line in M**, and relay §4.3's hope (W64's leading order from the condensate with no potential) fails at the first cell | 90% |

**Read-outs (no prior).**
- The table of α·h_Q over the 112, and for the 24 ever-Higgs-like roots.
- The block roots of the neutral Higgs-like condensates under each Y.
- If Reading B's axis (the third block t) were read as B1644's a = e_t (units b ↔ j, a ↔ i, ab ↔ k): m₂/m₃ at τ = iy
  from B1645's closed form, at y = 1, 2, 4.

**What a result means, fenced.**
- V holding means the owner's chosen field (the electroweak-type condensate, p-odd) and the record's flavour Higgs in M
  (B1644 to B1649, and the field of chat1's passage under H-RES, both p-even) are **two different fields** in this
  embedding.
- Joining them needs a coupling or a parent map the record does not yet have (P-108). It does not kill either one.
- No value, no count. **0 of 19.**
