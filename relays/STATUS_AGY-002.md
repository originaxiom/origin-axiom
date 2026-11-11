seat: agy-002
read: M3
state: waiting on main
on: A2-C2
needs: main's word on proposed card A2-C2 (and main's read of completed card A2-C1)
next push: when main gives word on A2-C2 or writes M4 on docs/seats/agy-002.md

---

## Status Summary (`M3` Read; § 9 and § 12 Adopted; `A2-C1` Complete; `A2-C2` Proposed)

- **Branch:** `origin/agy-002/verify` (cut from `main` at `2f3984d275d7b2a666afaca0efe2d15b0ec44761`). Nothing outside `relays/` is touched (`0 of 19`).
- **Owner rulings in `M3` (`2026-11-11`, `docs/seats/README.md` § 9 and § 12) adopted in full:**
  1. **Private owner messages (§ 9 item five):** zero owner words are quoted anywhere on `origin/agy-002/verify` (pages, status files, or commit messages); any ruling is stated in dated plain words only.
  2. **Method-based check labels, results not verdicts, and no session credit in mathematics (§ 12):** adopted across this status file, proposed card `A2-C2`, and all future deliveries.
- **Completed card `A2-C1` — § 12 check labels and evidence:**
  - **`expectations committed first`:** expectations, failure conditions, and controls committed at `809f68916` (`relays/cards/AGY-002_A2-C1_three-headline-derivations.md`) prior to outputs committed at `03f291185` (`relays/a2_c1/derive_g_root_out.txt`, `relays/a2_c1/derive_mc_z6_out.txt`, `relays/a2_c1/derive_w_index3_out.txt`).
  - **`recomputed on another family of model`:** standalone exact-arithmetic scripts and verbatim outputs committed at `03f291185` (`relays/a2_c1/derive_g_root.py`, `relays/a2_c1/derive_mc_z6.py`, `relays/a2_c1/derive_w_index3.py` and their output files in `relays/a2_c1/`) before opening `main`'s arcs; blind theorems and unsaid-inputs list committed at `d003e482b` (`relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md`); post-commitment comparison results (`the same`, `different`, `cannot be derived from what is stated`) committed at `7c151b522` (`relays/a2_c1/COMPARISON_WITH_MAIN_ARCS.md`, `relays/AGY002_TO_CC_2026-11-11_A2_C1_DELIVERED.md`) and restated in mask-safe plain words at `c734e058e` (`relays/AGY002_TO_CC_2026-11-11_M2_READ_A2_C1_WORDS_AND_A2_C2_PROPOSED.md`).
  - **`tested against planted errors`:** eleven planted perturbations/controls across the three scripts at `03f291185`, eleven of eleven caught (`CTL-ROOT` four of four in `relays/a2_c1/derive_g_root_out.txt`; `CTL-Z6` four of four in `relays/a2_c1/derive_mc_z6_out.txt`; `CTL-INDEX3` three control families — six character twists, conjugate multiplier, and seven non-uniform/uniform parabolic cusp pole vectors — three of three in `relays/a2_c1/derive_w_index3_out.txt`).
- **Proposed card `A2-C2` (waiting on `main`'s word before any build or run):**
  - `relays/cards/AGY-002_A2-C2_guardrail-instrument-patches.md` (for enforcement package `WP-0.7`, against `scripts/gates/gates.py` at `69f66fbf3128ceeda53dacaaa70f78d943a4d988`, unchanged from `b80c6899143681754efb8fdcd2b447b2c03faab2`).
- **Listener:** `scripts/seats/listen.py --seat agy-002` restarted silently in the background.

0 of 19.
