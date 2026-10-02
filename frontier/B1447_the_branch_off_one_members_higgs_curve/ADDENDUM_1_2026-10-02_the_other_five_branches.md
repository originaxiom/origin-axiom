# B1447 — ADDENDUM 1 (2026-10-02): the other five branches exist and are irreducible; no parabolic point was reached on them

The arc constructed representations only on the branch at the real branch point on the arc of real representations.
`verification/other_branches.py` runs the same construction at the other five roots of B1446's sextic, with the
sector and the sign of the meridian found there (records `other_branch_NN.json`, `other_branch_run_N.txt`; the run
was stopped after 11 of the 40 planned starts and the records are partial).

| branch point u | starts run | irreducible (the matrices span M₃) | \|log\| of the three eigenvalues of the trivial-twist triplet at s = 0.1 |
|---|---|---|---|
| −3.39224 (real, κ = 14.69) | 3 | 3 | 5.011, 0.0013, 5.010 |
| 0.24471 − 0.66638 i | 2 | 2 | 2.574, 0.0010, 2.573 |
| 0.24471 + 0.66638 i | 2 | 2 | 2.575, 0.0014, 2.574 |
| 1.76177 − 0.81604 i | 2 | 2 | 3.270, 0.0015, 3.267 |
| 1.76177 + 0.81604 i | 2 | 2 | 3.299, 0.0026, 3.301 |

**So all six branches exist**, each an irreducible family of rank-three flat connections, and each shows the
pattern of the arc's §5: one light eigenvalue that vanishes at the branch point and a pair that splits. The scale
of the pair differs by branch — 1.42 at the real point of the arc, 5.01 at the other real one, 2.57 and 3.27 to
3.30 at the two complex pairs.

**No boundary-parabolic point was reached on any of the five**: every homotopy stalled short of the target, most at
a residual near 4·10⁻¹¹. That is the behaviour of a target at which the equations are singular — a reducible
point with the meridian's eigenvalue tripled but not regular would be one — and it is the same stall ten of the 32
starts of the real branch showed. It is not evidence that these branches have no parabolic point; the method did
not decide it.

Nothing in the arc is changed.
