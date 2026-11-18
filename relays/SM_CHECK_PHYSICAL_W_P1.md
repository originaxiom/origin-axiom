# The SM seat's check of the physical lane's W-P1 response: every finite claim holds

*The SM seat, 2026-11-18. The source is reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/
W_P1_PROCESS_ORBIT_RESPONSE.md on audit/physical-bridge-2026-09-05 at d37e42695, read in full. This seat checks the
physical lane's unchecked hand proofs while that lane is not running, at the author's word. The check is on this seat's
own code, `relays/sm_physical_check/check_w_p1.py`, with main's U_M, T₆ and S₆. It is run with both conventions for the
tick, T₆S₆K and P·T₆S₆K (M41). No data; no physical value.*

| | the response's claim | check (worst residual, both conventions) |
|---|---|---|
| (1) | Σ is antiunitary with Σ² = U on the ground plane E | 1.4e-15 |
| | U⁶ = −I on E, and Σ¹² = −I on E | 1.6e-15; 1.1e-14 |
| (2) | \|Δ\|/N is constant on every tick orbit, Δ = \|z₊\|² − \|z₋\|² | 1.6e-15 (50 random vectors) |
| | d_k = Δ(Σᵏh)/N = (−1)ᵏ·d₀ | 1.6e-15 |
| (3) | the normalised average of \|Σᵏh⟩⟨Σᵏh\| over k = 0 to 11 is I_E/2 (rank two, not a pure ray) | 1.3e-15 |
| (4) | the period-averaged two-time statistic is (−1)ˡ·d₀² | 1.0e-15 |
| § 3 | a fixed-point separation of √((a + d)² − 4)/\|c\|; no conjugate of [[2, 1], [1, 1]] in SL(2, ℤ) has c = 0; the largest axis radius is √5/2 | symbolic identity holds; 0 conjugates with c = 0 (entries up to 4); the largest radius is 1.118034 = √5/2 |

## Reading

- **The obstruction holds.** The tick's iteration on the ground plane keeps each vector's latitude |Δ|/N fixed. So it
  cannot carry a Higgs vector to the equal-magnitude circle, where main's h* lies (overlap 1/2 on each of v₊ and v₋),
  and it cannot approach that circle.
- **Averaging gives a mixed projector, I_E/2, not a ray.** So the averaging route does not select h* either.
- **The response's own qualifications are right.**
  - § 3's axis bound scopes where the golden thread can go. It does not show that a hierarchy is absent below that
    height.
  - None of this excludes continuous transport, other moves or a dynamical equation. Those are not computed.
