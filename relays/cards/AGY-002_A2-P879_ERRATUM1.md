# `AGY-002` Card `A2-P879` Erratum `1` — Sealed Pre-Run `Fraction` Fix in `L_2` Check (`v2`, `0 of 19`)

- **Date:** `2026-11-20`
- **Immutable Record (`v1` untouched):** `relays/a2_p879/verify_a2_p879.py` and `relays/a2_p879/SCRIPT_SHA256.txt` (`commit de80a1eab`) passed the zero-float AST check cleanly and remain unmodified. On its first execution, line `265` raised `TypeError: cannot create mpf from Fraction(3, 2)` when checking `L_2` monotonicity inside `check_ast_and_custody` (`mp.mpf(y)` received `Fraction(3, 2)` rather than `mp_rat(y.numerator, y.denominator)`).
- **Superseded Producer (`v2`):** `relays/a2_p879_v2/verify_a2_p879_v2.py` fixes that single rational conversion (`mp_rat(y.numerator, y.denominator)` for `Fraction` inputs in `check_ast_and_custody`) without altering any pre-registered theorem, bound, or bar of Card `A2-P879` (`a4a342d2c`), and uses `max_levels = 16` in `run_T5_global_certifier_and_controls`.

0 of 19.
