# B384 (D4/PD3.1) — T1 BANKED: the Kashaev ladder carries ℚ(√5) content at every 5|N level

**Status: T1 banked; T2/T3 pending (registered). Pre-registration: PREREGISTRATION.md
(committed first). Firewalled: statements about ⟨4₁⟩_N as an algebraic number.**

## The finding that reframed T1

⟨4₁⟩_N = Σ_k Π_{j≤k}(2 − qʲ − q⁻ʲ) is **not a rational integer at general N** (the famous
integer sequence lives at a different normalization/limit): the exact value is an algebraic
integer in ℚ(ζ_N)⁺. First exact values (trace-projected Galois components, all exact):

    ⟨4₁⟩_5 = 46 + 2√5 = 4(11+φ)+…  — ℤ[√5] exactly (numeric 50.4721…)
    N=15:  rational part 8377/4,   √5-part 2023/4      (value ≈ 5855.43)
    N=25:  35142,                  13100                (≈ 312 972)
    N=45:  159911217/4,            71150671/4           (≈ 4.784e8)
    N=135: 290399598603800503336,  129870648314553074968 (≈ 1.045e22)
    (N=7, 9, 27, 81: no √5 subfield — rational parts 113, 258, 79576, 4784926648467)

**Registered bet (b) PASSES: the √5-component is nonzero at EVERY 5|N level tested** — the
golden field is present in the Kashaev ladder exactly at the levels where our tower lives.
Sanity gate (a): 2π·log⟨4₁⟩_N/N decreases 4.93 → 2.36 (N=5→135) toward Vol(4₁) = 2.0299 —
consistent with the volume conjecture's slow convergence (KNOWN — gate only, no claim).
Bet (c) (valuation ladder) — the components at 15/45/135 carry denominator 4 at 15 and 45 but
not 135; no clean Pisano-tied valuation pattern surfaced on three levels: **bet (c) KILLED as
registered** (no relation visible; banked as the negative).

NEEDS-SPECIALIST (novelty): whether the exact ℚ(√5)-content of ⟨4₁⟩ at 5|N is in the
literature (Habiro-ring/Garoufalidis–Zagier neighborhood expected to know it).

**Provenance.** kashaev_smalls.py (exact ℤ[x]/(xᴺ−1) arithmetic + Ramanujan-sum traces;
~2 min) → kashaev.json; locks tests/test_b384_kashaev.py.
