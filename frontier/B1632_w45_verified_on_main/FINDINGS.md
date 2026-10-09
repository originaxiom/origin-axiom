# B1632 — THE SM SEAT'S W45 ON MAIN: the weave's lifts on T form only a projective representation of the metaplectic group, so χ_{3/2} is not fixed by the lifts alone — among the genuine rescalings it is 0 for five and 1 for one; for the seat's ρ_T (T's exponents ⅛, ⅜, ⅞) main reproduces χ_{3/2} = 0, so the postulate's payoff rests on W41's multiplier, the input now load-bearing and unverified on main

**Verdict: NEGATIVE as sealed** (C0 holds; C1 fails — no identification satisfies the Mp2(Z) relations exactly; C2 and C3
were therefore not computed as sealed). cc (main), 2026-10-09. Sealed `7a5a62442` before the run. No data. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /vector-valued modular|Borcherds|Skoruppa|Riemann-Roch|metaplectic|W45/: 4 of 1403 arcs on main match (NEGATIVE 2, PROVED 2)`
— B1627, B1630, B1631; the SM seat's §47, §48 and W45. **Literature:** Borcherds, *Reflection groups of Lorentzian
lattices*, §7; Skoruppa.

## 1. The sealed run (`w45_on_main.py`, unchanged; `verification/sealed_run/`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **C0** | the calibrations hold | 90% | **HOLDS** — the trivial representation gives χ₀, χ₂, χ₄, χ₆, χ₁₂ = 1, 0, 1, 1, 2; η is allowed at ½ with χ = 1 |
| **C1** | the Mp2(Z) relations hold for (S̃, L⁻¹) and at least one more | 70% | **FAILS** — none of the eight identifications (S̃^{±1}) × (L^{±1}, R^{±1}) satisfies S² central, S² = (ST)³ and S⁸ = I exactly |
| **C2**, **C3** | χ_{3/2}(ρ_T) = 0; one unit gives 3 | 65%, 95% | **not computed as sealed** (no valid identification) |

## 2. The diagnostic (`post_seal_projective.py`, written after the sealed run; disclosed)

- **The lifts form a projective representation.** For every identification, S² is a scalar, (ST)³ = S² up to a scalar,
  and S⁸ is a scalar. The weave's topological lifts carry the character c, so they close only up to phases.
- **The genuine representations are rescalings.** Each identification admits 24 rescalings (S, T) → (μS, λT) by roots of
  unity that satisfy the relations exactly, and 6 of them allow weight 3/2. Across all identifications, **χ_{3/2} takes
  the values 0 and 1.**
- **For (S̃, L⁻¹), the seat's ρ_T,** five of the six give χ_{3/2} = 0 and one gives 1 (T multiplied by e^{πi/3}, with
  exponents 1/24, 7/24, 13/24).
- **The seat's stated exponents single out a zero.** W46 gives T's exponents as (⅛, ⅜, ⅞). That is the rescaling in which
  T acts by its plain topological lift, with S fixed by the relations (μ = −i), and there χ_{3/2} = 0. Main reproduces
  W45's zero given that multiplier.

## 3. What it says

**W45's χ_{3/2} = 0 is not a property of the weave's lifts alone.** It holds for the multiplier the seat derived in W41,
where the zero modes transform by the topological action on H^{1,0} = T and T's exponents are (⅛, ⅜, ⅞). It fails for
one other genuine multiplier, which would even give an index of 1 with no end data. So the postulate's payoff, the index
±3 given Λ and the unit, rests on **W41's multiplier**, which main has registered but not verified. That is the next
computation (lead).

Under the owner's audit rule this is the system working as intended. A load-bearing positive was tested, and its hidden
input was found before anything was built on it.

## 4. Disclosed

- The sealed instrument assumed the lifts form a genuine Mp2(Z) representation; they form a projective one. The
  diagnostic is post seal, and the sealed run is kept.
- W46's puncture conditions are not covered.

## 5. Files

`verification/w45_on_main.py` (sealed, unchanged), `w45_on_main.json`, `sealed_run/`; `post_seal_projective.py` and its
outputs. Kill-graph entry B1632. Test: `tests/test_b1632_w45_on_main.py`.
