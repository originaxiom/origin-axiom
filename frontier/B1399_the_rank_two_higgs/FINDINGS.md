# B1399 — THE RANK-TWO HIGGS: SEALED, NOT RUN. Can two independent Higgs classes on a member of m004's class give three generations in a frame with 27 matter? The test is sealed in `PREREGISTRATION.md` (sha256 in `docs/SEAL_LEDGER.md`) before any harmonic form of its census was computed. The run waits for the owner.

**Date:** 2026-09-28 · **Seat:** cc (the SM-derivation branch) · **Status:** SEALED, NOT RUN. This document holds no outcome; it states
what is sealed and what was checked at design time. · **Price:** unchanged, 0 of 19 · **Numbering:** B1399.

## 1. What is sealed

- **The question.** Is there a census member M, and cuspidal classes ω₁, ω₂ on it, with C(a_k ω₁ + b_k ω₂) = t_k on B1398's six
  direction classes, stably, at g = 3? Here t = g·(1, 0, −1, 0, 1, −2) and C is the frame's count.
- **The reduction,** proved at seal:
  - C is odd.
  - On a circle of directions it changes only at the critical values of each cusp's angle map, one step at a time.
  - So a realisation needs at least 12|g| breakpoints.
  - In cuspidal dimension 2 realisability is a finite union of exact linear programs.
- **The census:** 109 covers of degree 2 and 3 of B1186's 99 arithmetic members, up to isometry (91 of cuspidal dimension 2, 18 of
  dimension 3). The list and its generator are in `verification/`.
- **The predictions:**
  - P1: three generations on any member. Prior NONE, about 85%.
  - P2: any g ≠ 0. Prior NONE, about 60%.
  - P3: per-member read-outs.

## 2. Checked at design time (no census member, no harmonic form)

- `verification/census_list.py` regenerates `census_list.json` byte for byte.
- `verification/breakpoint_check.py` (record `breakpoint_check_run.txt`): on synthetic shells the breakpoint rule and its jumps agree
  with the Morse count at every one of 720 directions, and the index sums are zero. Two-direction shells give χ = 0.

## 3. Reading fences, added after the seal (the sealed text is unchanged)

- **One structure, one frame.** B1399 asks what the covers of m004's commensurability class permit for the frame's count. The
  three-generation pattern is the final check (P022; the mandate in WORKING_RULES).
- **Not the only escape.** The sealed NONE branch names door 2 and independent walls as the next escapes. The record also holds a
  different-frame escape, sL-4 (B1398 §3's scope note). It uses E₈, where the Standard Model's commutant is SL₅, and non-split
  backgrounds on the cyclic tower. There the three is a deck orbit, and it stalls at the same cusp/end law (B1384 S5).
- **The deck.** A result on a degree-3 cover carries sL-5's open question: whether the cover's deck is gauge or symmetry.
- **The count's physical reading** needs sL-8's completion, whatever the outcome.

## 4. Why this document exists before the run

The repo's rule is that every arc carrying a verdict carries a findings document (the locks of B810, B817, B1152 and B1207). The seal
commit left this arc without one. The fast lane on that commit caught it with four failures, recorded as an E50 instance. This page
closes it, and holds no result.
