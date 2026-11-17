# Card `AGY-002_FOUND-G9-ERRATUM` — Dictionary Key Typo `PF9_5_caught` (`0 of 19`)

In `465eead1e` (`relays/agy002_found_g9/verify_found_g9.py`), `run_section_3_p864_repair_and_sweep()` returned key `"PF9_5_above_ymax_flag_caught"` while `main()` looked up `"PF9_5_caught"`, raising `KeyError` before writing output. Preserving `465eead1e` untouched under `artifact-hashes`, `relays/agy002_found_g9_fixed/verify_found_g9_fixed.py` aligns that dictionary key, updates `prior_mfs` count from `6` to `7`, and seals expectations before execution (`0 of 19`).
