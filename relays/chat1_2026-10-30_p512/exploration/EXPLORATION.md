# P-512, the exploration that informed the rule (labelled; below the gate; data-free)

These scripts were run in a scratch directory before `../P512_RULE.md` was written, and their printed outputs were read
then. They are committed unchanged except for the path to main's checkout, which is now read from the environment variable
OA_MAIN (a checkout of main at 5e5e75ac4). Each is rerun once after the rule's commit, and its output is kept as `run_*.txt`
for the record.

- `sym_y.py`, `sym2.py`: the coupling Y(S; M) and its 2×2 minors, symbolic (sympy).
- `explore1.py`: R₂ on 1/8 and 3/8 at b = 0, 0.137 and 0.311 (Re τ = ⅓, Im τ = 10).
- `explore2.py`: D3's three reductions at b = 0, at Im τ 2.5 and 6.
- `explore3.py`: the leading formula 2|det M|/Q₀₁(M) at Im τ 10, for b = 0, 0.137 and 0.311.
- `explore4.py`: |r₀₁/r₀₀|, x's closed form, and |det M₀| against b_x + b_y.

Nothing here is graded. The cells are in the rule and in the sealed check script.
