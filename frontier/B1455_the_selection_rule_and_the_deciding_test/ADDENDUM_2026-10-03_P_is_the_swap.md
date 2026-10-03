# B1455 — Addendum 3 (2026-10-03): P is the swap; the symmetry that dualises the family is the strong inversion

The addendum of 2026-10-02 ("its three lines are B1297's") wrote that B1297's period-2 symmetry P acts on Ballas' family
as the inversion ι (m ↦ m⁻¹, n ↦ n⁻¹) does — dualising it. That sentence was wrong, found by the SM seat (sm:B1521 C1)
and re-derived on main (B1462, `verification/p_is_the_swap.py`, SnapPy's holonomy, no code of the seat's): in SnapPy's
presentation the relator lifts to −I and a ↦ −a makes the lift genuine; with m = ab and n = aabA (Ballas' relator holds,
a = MnmN and b = nMNmm give back the generators), P: a ↦ a⁻¹, b ↦ a³b becomes P(m) = MnmNm, P(n) = nmN, which is
conjugation by nM composed with the swap m ↔ n. So **P is the swap's class**; it fixes ρ_q (this arc's own table: ρ_q∘swap ≅
ρ_q), and the dualising symmetry of the family is ι, a strong inversion (meridian-reversing), which B1455's table has as
ρ_q∘ι ≅ ρ_{1/q} ≅ ρ_q*. The two theorems rest on different symmetries: B1297's (P inverts every twist of the tower; on the
tensor modules P carries V to V* ⊗ ε, main's B1459) and this arc's (the inversion dualises Ballas' family). What this arc
computed and banked is untouched; the misattribution is in the addendum's prose only. GENESIS FK12 (ii) carried the same
misreading since v1.3 and is corrected in v1.7 (B1462).
