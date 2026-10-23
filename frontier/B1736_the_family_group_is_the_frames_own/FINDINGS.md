# B1736 — THE FAMILY GROUP IS THE FRAME'S OWN (P-302): W135'S E₈ FROM 2I AND ITS Γ′ REBUILT ON MAIN; THE OBJECT'S ORDER-3 ELEMENT ACTS AS THE FAMILY ROTATION (B1275'S OPEN STEP, CANONICAL NOT SELECTIVE); B1656'S COUPLING IS Y = u hᵀ + h uᵀ − (u·h)1 + u₁[h]_× + h₀(u₁1 + [u]_×), AND ITS CHANNEL WEIGHTS ARE 1 ⊕ ρ′ — THE SAME CUBE ROTATIONS AS THE HIGGS

**Verdict: PROVED** (exact algebra and machine-precision numerics; no data). cc (main), 2026-10-23. **0 of 19.**

## 0. Why

P-302 (the SM seat's W134 and W135, row 1314): E₈ and E₆ × SU(3) built from the moves are one weave object; the joint
family group is the cube's rotations; Sym³ρ′ has no invariant, so no constant Yukawa and every family mass is a modular
form of τ. The parked-items sweep (L237 (b), QUEUE item 1) asked main to verify it and then read B1656's four channels
against it: does the joint frame forbid any channel the frame uses, and which representation do the Higgs and the
channels carry? B1275 (2026-09-06) verified E₈ ⊃ E₆ × SU(3) as standard Lie theory and left one step open: that the
object's own order-3 element is the A₂ rotation.

## Seen first

`VERDICT topic-sweep /family group|Sym.?3|cube.?s rotation|icosian|E8 from 2I|order.3 element|quaternion product|channel weights? (as|form|transform)|1 ⊕ ρ|singlet ⊕ triplet/ (full text): 38 of 1507 arcs on main match (NEGATIVE 8, PROVED 30)`.

Bearing on it: B1275 (the E₈ family mechanism, its open step), B1724 (S and S̃ covariant under SL(2, ℤ), by numerics on
the ratios), B1727 (S = 1 gives c·1 + [a]_×), B1716 (Y_ab = Σ m_s [C_a⁻¹ S C_b]_s), B1659 (the determinant law and the
symmetric form), B1730 (main's ρ). None writes the coupling in vector form or the channel weights' transformation.
**Literature:** the icosian construction of E₈ (Conway and Sloane, *Sphere Packings, Lattices and Groups*, ch. 8);
character theory of finite groups; standard.

## Disclosed

- W135's script (a6bfe19c0 on the SM seat's branch) and the reader's scratch checks (audit/drafts/leads_reeval/L237.md)
  were read before this arc. Nothing is imported from the seat: the icosians, the form, the simple roots, the group
  closure and the tensors are main's own code; the frame's functions are B1723's `b1656_funcs` and B1691's components,
  as every census since.
- Two slips were caught and fixed before the run recorded here: the identity was counted twice in part C (orders 73
  and 25), and part D first carried the wrong sign on u₁[h]_× (relative error 1.77). Both runs are in the audit room;
  the recorded run reproduces the corrected audit run exactly.
- W135's K2 (the anomaly of the full 27, m ≡ 5 − r mod 8) is not re-derived here.

## 1. E₈ from 2I (part A, exact over ℚ(√5))

The 120 unit icosians (2I) and φ⁻¹·2I under B(p, q) = 2 EN(Re(p q̄)), EN(a + b√5) = a + b:
- **240 roots, all of norm 2**; a generic functional gives **8 simple roots whose Cartan matrix is E₈'s** (entries
  2, −1, 0; determinant 1; branch degrees 1, 1, 1, 2, 2, 2, 2, 3).
- 2I's **20 elements of order 3 form one conjugacy class** in **10 subgroups**; each subgroup ⟨w⟩ gives the A₂
  {±1, ±w, ±w²}, **72 roots orthogonal to 1 and w (E₆)** and **162 in six classes of 27**; the 10 frames are distinct
  and **conjugation by 2I permutes them transitively**. W135's K0 holds.

## 2. The object's order-3 element (part B)

- ⟨R, L⟩ mod 5 = SL(2, 5) → 2I, with R and L sent to order-5 units and extended along words (a bijection of 120).
- **g = −RL⁻¹ mod 5 = [[0, 4], [1, 4]]** goes to g_q = (−½, −¼ − ¼√5, 0, −¼ + ¼√5), **of order 3**.
- **Left multiplication by g_q is an isometry of E₈** that preserves g_q's frame (A₂ and E₆ as sets), rotates its A₂,
  and **permutes the six classes of 27 in two 3-cycles** — the same permutation as B1275's A₂ Weyl rotation s_a s_b
  (a = 1, b = g_q). It is not that rotation: s_a s_b fixes E₆ pointwise, left multiplication does not. B1275's sum rule
  1 holds on this frame (no two roots of one class sum to a root).
- **So B1275's open step closes, canonically but not selectively:** the founding ratio's order-3 element induces
  exactly the family rotation on the six classes of its own frame — but every order-3 element of 2I does (one class),
  so the object picks which of 10 conjugate frames, not whether there is one.

## 3. W135's Γ′ with main's ρ (part C)

ρ′ = ρ ⊗ χ_η^k with B1730's ρ(T) = e^{iπ/4}L⁻¹, ρ(S) = e^{iπ/4}P; det ρ′ = 1 exactly for k ≡ 5 mod 8:

| k | order of Γ′ | real | dim (Sym³ρ′)^Γ′ | dim (Λ³ρ′)^Γ′ |
|---|---|---|---|---|
| 5 | 72 | no | **0** | **1** |
| 13 | 72 | no | **0** | **1** |
| 21 | **24** (the cube's rotations: orders 1, 2⁹, 3⁸, 4⁶) | yes | **0** | **1** |

At k = 21, **Sym³ρ′ = 1′ ⊕ ρ′ ⊕ ρ′ ⊕ ρ′⊗sgn** (multiplicities 1, 2, 1; ⟨Sym³, Sym³⟩ = 6). W135's K3 and K4 hold.

## 4. B1656's coupling in vector form (part D)

With S = h₀·1 + h_i i + h_j j + h_k k and M = Σ u_s E^s (the dual basis of B1656), in the unit order (i, j, k):

  **Y = u hᵀ + h uᵀ − (u·h)·1 + u₁[h]_× + h₀(u₁·1 + [u]_×)**

exact to 4 × 10⁻¹⁶ against `coupling()` on 50 random complex inputs (B1659's determinant law holds alongside,
3 × 10⁻¹⁵). Read as tensors on family ⊗ family ⊗ Higgs:
- **the channel 1 is −ε_abc** — the one invariant of Λ³ρ′, E₈'s family coupling;
- **the channels i, j, k together are −δ_ab δ_cs + δ_ac δ_bs + δ_as δ_bc**, invariant only with u = (u_i, u_j, u_k)
  carried as a triplet; each alone has Sym³ and mixed parts and no invariant part;
- with u = 0, Y = u₁[h]_× is rank 2 for every complex h (third singular value ≤ 5 × 10⁻¹⁶).

## 5. The channel weights are 1 ⊕ ρ′ (part E)

At three points and lines (0.3 + 1.4i on (2/5, 1/10); −0.2 + 1.7i on (1/3, 1/5); 0.15 + 1.25i on (3/7, 2/7)), all three
sectors, the weights u_s = √(2πL + c_s) R_s at τ and at the image (B1724's laws):
- **under T:** the Higgs moves by e^{iπ/4}(1 ⊕ R₋₉₀°) (residual ≤ 10⁻¹⁶); **u moves by the same R₋₉₀° and u₁ by the
  same scalar** (∣scalar∣ = 1, phase common to u₁ and u in each sector; residual ≤ 2.6 × 10⁻¹³);
- **under S:** the Higgs moves by a scalar times P (residual ≤ 2 × 10⁻¹⁶); **u moves by −P, a proper rotation, with the
  scalar of u₁** (∣scalar∣ the same in every sector at a given τ; residual ≤ 2.3 × 10⁻¹³).

So (u₁, u) carries 1 ⊕ ρ′ with ρ′ the cube's rotations, the Higgs carries ρ′, and by §4, **Y(γτ) = scalar · R_γ Y(τ) R_γᵀ**
for both generators: B1724's covariance, which was numerical on the ratios, follows from the structure.

## 6. What it means

- **The joint frame forbids nothing the frame uses.** Its only constant coupling is ε (Λ³), which enters as u₁[h]_×;
  the Sym³ "constant Yukawa" W135 excludes is not in B1656's coupling. The symmetric part — the part that can split
  the three masses — is u hᵀ + h uᵀ − (u·h)1, built from the channel triplet, which is a modular triplet like the Higgs.
- **So the hierarchy is the relative geometry of two triplets:** with the Higgs pure (h₀ = 0, as every census since
  B1700), the masses in each sector are the singular values of u hᵀ + h uᵀ − (u·h)1 + u₁[h]_×, functions of the
  invariants of (h, u, u₁) alone. The Higgs triplet h(τ) is common to the sectors; each sector has its own (u₁, u) from
  its twists. With the channel triplet off (u = 0), the third mass vanishes for every Higgs.
- **For P-294 and P-295:** a hand-put lepton factor or reading rule must act on this structure; the structure fixes the
  family group, not the factor.
- W135's K2 (the 27's anomaly) stays the seat's (cited).

## Files

- `verification/the_family_group.py` → `the_family_group.json`, `the_family_group_run.txt` (parts A–E).
- The lock: `tests/test_b1736_the_family_group_is_the_frames_own.py`.
