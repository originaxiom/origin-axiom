# The pre-seal review's own code (read-only reviewing agent, three passes on designs v1, v2 and v3)

Written by main's read-only reviewing agent in a scratch directory, independently of the instrument (direct theta
series, `rv_core.py`), and copied here unchanged so that the numbers the preregistration discloses (§0b, items 2, 4 and
6) stay reproducible. Their printed outputs were not saved; the numbers are quoted from the agent's reports. Run from
this folder (`python3 -B rv_check5.py` and so on; `rv_check6.py`, `rv2_check2.py`, `rv2_check3.py` and
`rv3_check1.py` load their neighbours by relative path). The first-pass scripts (`rv_*`) read design v1, the second
(`rv2_*`) design v2 on the instrument's seeded draws, and the third (`rv3_*`) design v3.
