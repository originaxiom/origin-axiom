# Referee report, B1817 (strand A's A1; hostile, read-only)

*Saved by main from the referee's hand-back; the referee could not write the file. Its drivers are `drv.py` and `drv2.py`,
with outputs `out0.txt`, `out1.txt`, `o_b.txt` and `o_c.txt`. Main's regeneration is in `main_rerun/`.*

**VERDICT: PASS WITH CORRECTIONS.**
- The 4, ¼ and 1 results and the N_c control reproduce.
- The phrase "line-specific non-integer constant" is wrong for several slopes.
- "Never the colour count" is too strong for the exploratory scope.

## 1. Independent regeneration: OK for the integer limits
R₂ is read on L_max, with b = 0.137 unless stated.

| N_c | α | result |
|---|---|---|
| 3 | 1/10 | S 3.9986 (Im 12) → 3.9996 (Im 14); S̃ 0.2501 → 0.2500; identical at Re τ ⅓, 0.1 and 0.6 |
| 3 | 1/9 | S 4.0075 → 4.0037; S̃ ¼ |
| 3 | 2/5 | 1.0000 at every Re τ, Im τ and b |
| 2 | 1/6 | S 4.0000, S̃ 0.2500, independent of Re τ |
| 4 | 1/14 | S 3.985 → 3.994; S̃ 0.2509 → 0.2504 |
| 5 | 5/12 | S ¼, S̃ 3.9996 → 4.0000 |
| 3 | 1/8 | S 3.4299 at Re τ ⅓, 0.1 and 0.6 and at both b; S̃ 0.2916: a true line constant |

## 2. The charge patch: OK, with one wording point
- compute() reads SIXY only through sector_twists (census.py line 67), so only the six sector twists q·w change.
- H is never read. The Higgs reading S, line_w, cA and the residues carry no hidden N_c dependence.
- The patched charges are hypercharge-consistent:
  - Q + u = −N_c;
  - Q + d = N_c;
  - L + e = N_c = H.
- **So the control tests only whether integer multiples of the twist produce N_c. It does not test whether some other
  colour-dependent structure could. § 3 should say so.**

## 3. The equal-exponent selection: OK
- nn and e2 implement B1788 correctly.
- **The unequal-slope spot-check** (N_c = 3, α = 1/7): the exponents are 1/7 (down) and 2/7 (leptons). R₂ falls 1.8e-3,
  2.0e-4, 2.6e-5, 3.8e-6 at Im τ 8, 10, 12, 14, so it has no finite limit.
- Equal exponents are a necessary condition only. Several selected slopes are torsion-degenerate, or have vanishing
  theta constants, where the closed form is not claimed: 0, ½, ¼, 1/12, 5/12.

## 4. The "line-specific constants": CONFIRMED-PROBLEM
**Several are not line constants.**
- **At 1/12** (N_c = 3, S, Im τ 12):
  - 2.5577 at b = 0.137 but 1.697 at b = 0.311;
  - 1.59 at Re τ 0.1 and 17.36 at Re τ 0.6.
  - The b-scan gives 1.39, 2.56, 1.28, 1.70, 1.05, 3.77 at b = 0.05, 0.137, 0.2, 0.311, 0.4, 0.6, and 0 at b = 0, 0.5,
    0.75.
- **At 5/12:** S̃ gives 3.03 at b = 0.05, so 3 is reached on a continuum of b.
- **At 1/4:** S = S̃, swinging 0.51–1.14 with b.

**The draft's own jsonl shows the same.** At Im τ 12 the two offsets give:
- 1/12: 2.5577 against 1.697;
- 1/4: 0.7714 against 0.506;
- 5/12: 0.600 against 0.4999;
- N_c = 2, 1/8: 1.09 against 1.37;
- N_c = 2, 3/8: 0.16 against 1.20.

The census's b-filter excludes these, so the integer table is fair. But § 2's bullet presenting them as constants
contradicts that filter.

**The slowly converging 2/23 depends on Re τ.**
- At Im τ 12 it gives 2.88 at Re ⅓, 2.95 at Re 0.1 and 2.28 at Re 0.6.
- Along Im τ (Re ⅓) it gives 2.59, 2.88, 3.12, 3.31, 3.47, 3.50 at Im 10, 12, 14, 16, 18, 20. It passes through 3.
- It breaks down at Im 24 (0.15), the double-precision floor. The limit is unresolved; 4 is plausible but not shown.

**So "nothing tracks N_c" is not established on b-dependent or unconverged slopes.** It holds only where the limit is
independent of b and Re τ and has converged. Re τ-independence was not part of the census filter.

## 5. The clamped L: MINOR, supporting the draft
- The 4 and ¼ limits (1/10, 1/9, 1/6) are identical at Re τ 0.1 and 0.6 and at Im τ 12 and 14. They are not artefacts
  of the clamp.
- But L is a fixed model input, extrapolated from B1667's column. These are limits of the instrument, not of the
  physical cusp. State this.
- R₁ carries no cusp limit: it is erratic (0.018 to 4940).

## 6. Overclaims
- **The title:** "NOTHING TRACKS N_c" should read "no b- and Re τ-independent converged limit equals N_c or 1/N_c".
- **"A property of the theta structure":** the 4/¼ swap is observed, not derived. Say "consistent with".
- **"Closes the remaining frame-internal formulation":** say "closes the twist-charge route on the equal-exponent
  slopes tested".
- **"NEGATIVE as scoped"** is acceptable after these rewordings.
