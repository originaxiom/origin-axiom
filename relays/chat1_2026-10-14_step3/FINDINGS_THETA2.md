# THETA2 — the other parameter-free completion: the (3/2, 7/2) cell keeps its nearly degenerate light pair; only E4·F gives it rank two

chat1, 2026-10-15, morning.
- **Sealed** at `4f7db6631` (`PREREGISTRATION_THETA2.md`, sha256 f5b2d017…).
- **The script** `theta2_completion.py` was committed at `f7fb61f8f`, after the seal and before its one run (969 s).
- **Output** `theta2_completion_run.txt` and `theta2_completion.json` (`933748a69`), committed before this read-out.
  - An interim copy of the log, its first three lines and no number, was swept into `d1e4ebe94` by a broad `git add`
    while the run was going. Disclosed there.
- **0 of 19.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q | the controls hold | 85% | **HOLDS.**<br>(a) The identities hold in value to 10⁻³⁸.<br>(b) α = (−221, −4, −112) and β = (−224, −4, −112), exactly the referee's.<br>(c) H-ORTH reproduces the sealed run to 1.2·10⁻⁸ on admitted threads.<br>(d) H-E4 reproduces the post hoc exactly.<br>(e) Invariance to 2.9·10⁻¹³ |
| T1 | under ϑ², the (3/2, 7/2) cell has rank 3 on every admitted thread | 95% | **HOLDS:** 59 of 59 |
| **T2** | under ϑ², no admitted (3/2, 7/2) thread in the band splits the light pair (m₁/m₂ ≤ 0.005) | 85% | **HOLDS:** 18 threads in the band, no hit |
| T3 | under ϑ², the least m₁/m₂ in the band is ≥ 0.3 | 70% | **HOLDS:** 0.770 (LLLRRR) |
| T4 | under ϑ², the (−½, 7/2) cell has rank 2 on every admitted thread | 98% | **HOLDS:** 59 of 59 |
| T5 | under ϑ², the (−½, 7/2) root has m₂/m₃ in [0.002, 0.07] | 55% | **HOLDS:** 0.0333 |

## The root under each completion

| completion | (3/2, 7/2): masses (m₃ = 1) | (−½, 7/2): masses | the (−½, 7/2) root's place among the 59 |
|---|---|---|---|
| H-ORTH (thread-dependent) | 1 : 0.809 : 0.618 | 1 : 0.0215 : 0 | 36th |
| E4·F (c = 0) | 1 : 0.485 : 0 | 1 : 0.0184 : 0 | smallest |
| step 3a's particular sections, uncompleted | 1 : 0.683 : 0.544 | 1 : 0.0332 : 0 | 28th |
| ϑ²F | 1 : 0.683 : 0.544 | 1 : 0.0333 : 0 | 28th |

## What it shows

1. **In the (3/2, 7/2) cell only E4·F gives rank two.** **[SEALED, T1–T3]**
   - Every other completion computed leaves the light pair nearly degenerate, at m₁/m₂ ≥ 0.77 in the band: H-ORTH,
     ϑ², and the particular sections.
   - E4·F (c₊ = 0) is the knife-edge.
   - So no parameter-free or norm-based completion splits the light pair at rank 3. Whether the cell has a massless
     first generation is decided by the completion.
2. **The (−½, 7/2) root moves with the completion,** from 0.0184 (E4·F) to 0.0215 (H-ORTH) and 0.0333 (ϑ²). It stays
   in the band throughout.
   - So the earlier proximity of the E4·F value to the down quarks' m_s/m_b (0.0187 ± 0.0016, 0.2σ) belongs to one
     completion. Under ϑ² the same root sits 9σ away.
   - Recorded without weight; this weakens the coincidence further.
3. **The tower is exact** (in value, to 10⁻³⁸).
   - The 3/2 sections are the Serre derivative of the −½ sections.
   - Every one-unit 7/2 section is E4·F + c f.
   - Step 3a's particular sections are E4·F + α f, and on the ± lines they are ϑ²F.
   - So every matter mode in this framework descends from the three −½ sections, one of which is R itself.

## Fence

- **Which completion is physical** is not decided. E4·F (the ring) and ϑ²F (the derivative) are both parameter-free and
  the same on every thread.
- **The object:** W72's framework, B1644's coupling at the puncture, and Lyndon words to length 8 with y ≤ 3.
- **Not tested:** the (7/2, 7/2) cell; sectors; the lift; CP.
- No value. **0 of 19.**
