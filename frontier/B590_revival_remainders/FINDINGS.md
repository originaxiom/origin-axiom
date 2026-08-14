# B590 — R2/V3 delivered; R1's sealing verdict was VACUOUS and is now genuinely blocked

cc banking seat, closed 2026-08-01 under B840 at the owner's direction (the arc was paused
2026-07-14 with "bank pending"). Prereg in `PREREGISTRATION.md`. Gate 5; nothing to `CLAIMS.md`.

## R2 / V3 — delivered, read blind

`v3_three_16s.py` runs (`v3_output.txt`). The three D₅ frames' decompositions of the **27**, and the
Φ-orbit structure:

- **Φ-orbits on the 27 weights: nine orbits of size 3.** Charge node index 0; split **1 / 10 / 16**,
  gate **PASS**.
- `|16ᵢ ∩ 16ⱼ|` = **16** on the diagonal, **10** off it; `|16ᵢ ∩ 10ⱼ|` = **0** / **5**;
  `|10ᵢ ∩ 10ⱼ|` = **10** / **5**. **Triple intersection `16∩16∩16` = 6.**
- The three singlets are **distinct**.
- Orbit profiles across frame-0's (16, 10, 1): `(16,16,16)×2`, `(10,16,16)×3`, `(10,10,16)×2`,
  `(10,10,10)×1`, `(1,16,16)×1` — nine orbits, 27 weights.

**The singlet's own orbit is `(1,16,16)`:** the frame-0 singlet is Φ-related to two weights that
frame-0 places in the 16. Read blind, as the prereg required; **no interpretation is attached.**

## R1 — the sealing verdict was VACUOUS, and that is the finding

`s031_m3_sealing.py` as written **printed `SEALED` at m=3 on both seeds with 0 escapes.** **That verdict was empty — nothing was ever tested:**

> **`polish_mp` built 9 complex trace equations — 18 real — for 22 real unknowns, and `mdnewton`
> requires a square system. It raised `cannot solve underdetermined system` on EVERY input, at every
> m.** The loop counts the exception and `continue`s **before** the field-membership test, so
> `escapes == 0` held because **no point was ever tested.**

**The m=1 "pipeline validation" shared the defect** — 12 irreducible, 12 polish failures — so the
guard designed to catch exactly this could not fire either. **Both the verdict and its validation
were vacuous** (MB12 class).

### Three bugs found and fixed

1. **`polish_mp` underdetermined.** Fixed with an **exact torus gauge** `B[0,1] = B[0,2] = 1` — the
   residual SL(3) diagonal-torus conjugation is exactly 2 complex dof, and traces are
   conjugation-invariant so the gauge changes the representative, never the answer. *(A first
   attempt pinned the entries to their unpolished least-squares values, which capped the polish at
   ~1e-9; the m=1 validation caught that and it was replaced.)*
2. **`in_field` truncated the test element to 50 digits** while its basis `POWERS` was built at 70.
   `pari.lindep` fitted the 20-digit gap with a spurious relation of height ~10¹⁸ — residual 8.5e-59
   (passing the 1e-30 gate) but blowing the 10⁶ height gate — so **every** member was rejected.
3. **The positive control built its values in double precision** (`complex(GAMMA…)`, ~16 digits) and
   asked for a residual below 1e-30. **Bugs 2 and 3 are independent; fixing either alone left the
   control failing**, which is why the prereg's STOP fired at all.

Controls now pass with the correct minimal heights (1, 3, 7), and polish succeeds 10/10.

### With the pipeline working, m=1 does not seal

`{'m': 1, 'irreducible': 13, 'escapes': 13, 'polish_failures': 0}`. The polished traces are **not**
in ℚ(√−3): `lindep` heights come back at **~10⁵⁰** against a 10⁶ gate, with residuals only ~1e-26 —
no genuine relation, just noise-fitting.

> **R1 is BLOCKED on a real, diagnosed failure instead of passing vacuously.** Whether the m=1
> escapes are a genuine property of these off-sublocus fixed points or a further pipeline defect is
> **not determined here**, and the m=3 question the cell was written to answer **remains open.**

**Also recorded:** the script computes the bronze `b++RRRLLL` trace field as **degree 8**
(`x⁸−59x⁷+2335x⁶−59176x⁵+1164604x⁴−15470917x³+148990805x²−865754218x+3047203448`), while the
prereg's framing quotes B578-D6 for **degree 6**. **That discrepancy is unresolved.**

## Disposition

**R2/V3 delivered. R1 blocked with its defect diagnosed and three bugs fixed.** The arc is closed as
reported rather than left paused; **the m=3 sealing question is returned to the open queue**, now
with a working polish and a named next obstacle.

`r1_output.txt` · `v3_output.txt`
