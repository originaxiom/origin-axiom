# B1992: hashes fixed before the run (2026-11-25 14:14)

| file | sha256 |
|---|---|
| `frontier/B1992_what_the_whole_can_select_is_algebraic/CARD.md` | `6e4d366ea3a9d9d1459d8d1fe12de50a37f8fd02eece2b90d5f65650ea9f5d1d` |
| `select.py` (the check's first name; renamed `select_check.py` below, so it no longer exists under this name) | `8588a6e8ffdb81bb6e8a7eade090eef40c65efecaf96b17b4b007a8d283d8113` |

*Disclosed (2026-11-25 14:15):* `verification/select.py` crashed at import before computing anything, because its name shadows Python's
standard module `select`. It was renamed `select_check.py`; only its usage line changed. Rehashed before the run:

| file | sha256 |
|---|---|
| `frontier/B1992_what_the_whole_can_select_is_algebraic/verification/select_check.py` | `f70ca8f76753c696a7a7c57d447a800e37cbdd3716a32a23c78b970163b228f4` |

*Disclosed (2026-11-25 14:51):* the run above was stopped after 34 minutes with no output: sympy's `solve` on the large Gröbner bases was
the slow step. The script now tests zero-dimensionality only (grevlex). Over ℚ that implies algebraic solutions, by T1, so the
points are not solved for. Rehashed before the rerun:

| file | sha256 |
|---|---|
| `frontier/B1992_what_the_whole_can_select_is_algebraic/verification/select_check.py` | `feec63c72c3c815855631ee36944d8d74cc4a0cf8fddaa555fcefc1f53b4a3fb` |
