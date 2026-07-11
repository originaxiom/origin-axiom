# B500 — the child hunt, depth 4: NO AIRLOCK; the wild ladder (S₅, S₉, S₁₀)
**Prereg'd target x⁴−x−1 (d_K=−283) NOT FOUND at depth 4** — all 36 three-verb words solved clean
(exact resultant eliminants + saturation; 0 timeouts; hunt_results.txt). The airlock never fired.
Depth 5 = the remaining zone before "the child is not a short word" banks as the negative.
**Discovery (W1 answered beyond its asking):** the wild register ESCALATES — depth 3 gave S₄; depth 4
births **S₅ quintics** (ord 120; ≥8 words), **S₉ at degree 9** (FFMD, FMDF), **S₁₀ at degree 10**
(FDDM, MFDD) — full symmetric groups of growing degree. The grammar writes arbitrarily wild
sentences; the value-lattice is a LADDER, not a bound. The live question is now SELECTION (why any
particular field): B501 (stationary measure = which fields a typical history births) and B502 (the
parity constraint) are the prereg'd answers. Firewalled; no value-matching performed.

## Depth 5 — the KILL is PROVISIONAL: no hit in 115/150 words (2026-07-11; CORRECTED 2026-07-12)

> **CORRECTION (B525 'Are You Sure' audit — a census-completeness / necessary-not-sufficient error).**
> An earlier version claimed "**completed 141 of 150**, 0/141, only 9 unfinished." That was wrong. Of the
> 141 logged lines, **26 are bare `TIMEOUT`** — `hunt_d5.py` arms `signal.alarm(300)` *before* the
> resultant/elimination and on timeout only logs the word (no `factor()`, no `polgalois`, no d_K=−283
> check). So only **115 of 150 words were actually analyzed** (0 hits), and **35 of 150 (23%) are
> UNCHECKED** — 26 timeouts + 9 never-reached (the run was killed mid-stream; there is no `HUNT COMPLETE`
> line). A 77%-analyzed census does **not** license the universal "child is not a short word." Downgraded.

The depth-5 sweep (`hunt_d5.py` → `hunt_results_d5.txt`, ~18h streamed) **analyzed 115 of the 150**
all-three-verb words with **ZERO hits** (no d_K = −283, no field isomorphism to ℚ[x]/(x⁴−x−1); the B398
airlock never fired, grep-verified over the whole file). **35 words remain UNCHECKED** (26 timeouts + 9
never-reached — the D/M-heavy tail whose resultant eliminants blow up to degree ~3000–9280, beyond
in-sandbox `gp`). The KILL is therefore **PROVISIONAL**: strongly suggestive (0/115, all analyzed words
give generic wild Sₙ) but **not the complete depth-5 exhaustion** the prereg's KILL requires.

- **What the analyzed words produce:** generic large symmetric Galois groups — S₇ ×15, S₁₁ ×10, S₆ ×5,
  S₈ ×5, S₅ ×5, S₉ ×4, D₄ ×3. Consistent with the B499 wild census; but this is 0/115, **not** 0/141.
- **REOPEN (audit action):** re-run the 35 unchecked words with a longer/removed timeout or a tractable
  method (Gröbner/eliminant over 𝔽_p, or a targeted d_K=−283 factor test) before the KILL can be banked as
  complete. Until then, "the child is not a short word" is a *provisional* negative, not a theorem.
- **Bearing on the project:** still a suggestive line toward "the object produces generic wild arithmetic,
  not the special −283 child" — but it is now explicitly incomplete, and must NOT be cited as a completed
  KILL alongside Gate C / B519. Firewalled; no value-matching. Lock: `tests/test_b500_kill.py` (updated to
  pin 115 analyzed / 35 unchecked).
