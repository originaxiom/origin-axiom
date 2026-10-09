# B1490 — ADDENDUM (2026-10-09, Review 62's R62-4): the files changed after the seal, named

The seal (`080189f89`) and the bank (`4e617453e`, S70) differ in five of the seven hashed files. FINDINGS §3 records the
reason, the E21 guard catching the sealed text calling the order-1920 group PSL(2, ℤ[ω]/4), but it does not name the
files. They are named here so the record's seal tool can see the disclosure:
- `verification/common_cover_main.py`: the docstrings name the group SL(2, ℤ[ω]/4)/{±I} (order 1920), not
  PSL(2, ℤ[ω]/4) (order 960). `orbit_perms` was added for the stabiliser of K's coset.
- `verification/congruence_level.py` and `verification/congruence_level.json`: the same naming correction, and the
  level-4 count re-run under it.
- `verification/level_recount.py` and `verification/level_recount.json`: the recount re-run after the correction.

The sealed run's outputs are kept in `verification/sealed_run/`. The sealed instruments are in git at the seal commit.
No number of the arc changed.
