# B771 FINDINGS — WAVE 4 (13 cells: 6 wave-3 carries + 7 fresh pool, 3 Gate-5-Q-sensitive)

*2026-07-23. Workflow wf_b231f420-cc8 (interrupted once, resumed clean via cache).
26 agents, 13/13 reported. Gate: **10 banked, 3 carry**. cc hand-verified 15a1
(PARI: rank 0, torsion 8), the 2O order-48 structural fact, C_5=121=11². Machine
table wave4_results.json.*

## Banked (10)

| cell | verdict | one line |
|---|---|---|
| W4-270r | **RESOLVED-B → CLOSED** | the gap-slope carry (3rd attempt) finally lands: the ratio is FIT-PROTOCOL DEPENDENT (1.148 curvature-removed vs 1.256 banked, 9.4% apart); the candidate √(1/φ²+1)=1.176 lies between and is refuted in BOTH readings; honest depth cap 9, results.json now emitted incrementally. |
| W4-150r | **RESOLVED-A → CLOSED** | carry-fix: in-code verdict block added (gated on S4's 3 N-selection checks, allow-lists the 2 known S2 diagnostics with a reason) — the B178/B171 gap-power law now closes with earned verdict logic. |
| W4-067r | **RESOLVED-B → CLOSED** | carry-fix: reframed as 6 distinct composite words under one method (not statistical seeds); the K016-expected negative (classical fields don't fuse) stands. *[B773 re-tests at chord level — see below]* |
| W4-078r | **RESOLVED-A → CLOSED** | carry-fix: honest verdict logic; the KMS ladder βₙ=log λ_PF closed form (λₙ=λ_{n−1}(1+√λ_{n−1}), 3/2 growth) earned, not self-fulfilling. |
| W4-084r | **RESOLVED-A → CLOSED** | carry-fix: **border IS forced at collar depth d\*=1** for σ₄ — the decisive K-theory gate the wave-3 cell skipped; the AP complex (b₁=4, Ȟ¹=ℤ⁴) now certified. |
| W4-183 | **RESOLVED-A → CLOSED** | BSD for 15a1 fully computed, rank 0, internally consistent — hand-confirmed by PARI (rank 0, torsion order 8). |
| W4-124 | **RESOLVED-B → CLOSED (Gate-5-Q negative)** | the silver hearing group does NOT and CANNOT show 2O structure (conductor-8 shadow distinct from order-48 2O) — the 2O/E7 conjecture killed structurally. |
| W4-192 | **RESOLVED-B → CLOSED (Gate-5-Q negative)** | the Baez–Schwahn fifth F₄ door is real (Stab=12=dim su3+su2+...) but the object canonically selects NO nested pair — expected negative, E20 held. |
| W4-115 | **RESOLVED-B → banked (trace-level); chord under B773** | no law relates cover-torsion to charge tower e_n at trace level (n=5 hit isolated). *B772 flagged trace-blind; B773 W4-115c re-tests at the chord level — the durable verdict awaits that.* |
| W4-304 | **RESOLVED-B → banked (trace-level); chord under B773** | level-45 pair-sector rows identically zero at trace level. *B772 flagged trace-blind; B773 W4-304c re-tests the θ-odd analog + base-rate correction.* |

## Carry (3) — verdict sound, narrative/sub-check defect

| cell | the catch |
|---|---|
| W4-017r | **the substantive win is real** — W3-017's false-empty census class 10 IS corrected: it carries the degree-4 quartic t⁴−9t³−12t²+27t+9 (SVD-verified, all census degrees {2,4,8} reproduced, Ruelle gap ≥0.19 recertified). But the cell's compute.py narrates a *fabricated* "verified in-cell" scope claim about a class-3 degree-10 point that the code never solves. Carry: strip the fabricated comment; the class-10 correction stands. |
| W4-139 | the m=3 eliminant does NOT wall — A₃(M,L) computed exactly (irreducible). But the "genus ≥ 1" lower bound is asserted in prose, never computed (needs the birational Fxz→G step). Stays UNRESOLVED → EXTERNAL, correctly not a negative (B772's mislabel finding confirmed). |
| W4-194 | the RESOLVED-B (H121 dissolves under hardening) is NOT overturned — the firewall negative stands. But a supporting check (B3 open-closed differential) is vacuous by construction. Carry: remove the vacuous check; the negative holds on B1. |

## Cross-references (honesty)
- W4-115, W4-304: banked here as TRACE-LEVEL negatives; **B772 flagged both trace-blind
  and B773 is re-computing them at the chord level right now.** Their durable status is
  whatever B773 returns; the Wave-4 verdict is the trace-projection result only.
- W4-067r: also a B773 target (W3-067c) at chord level.

Census deltas: CLOSED +8, EXTERNAL +1 (W4-139), 3 carry. Gate 5/5-Q clean on the
banked ten (3 firewall negatives held correctly). Nothing to CLAIMS.
