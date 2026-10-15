# The pre-seal review of B1654 (one pass, read-only, 2026-10-15)

A read-only reviewing agent read PREREGISTRATION.md and the instrument as they stood at the first draft (kept as the arc's `design_v1/`; the sealed text is the revision). It ran its own scripts here (pre.py execs
the instrument's functions only, never its cells as a whole). Its findings and what it ran are summarised in the
preregistration's §0b. In brief: no decisive error in the hand mathematics; one MAJOR (N4's control (a) vanished at
τ = i with λ = (1, 2, 4)); minor robustness and text findings; the cutoff-free form of D (s19); the closed-form cusp
constant K = 8π(1 − 4 ln 2) (s25, s28). Main caught one further error in its own revision (the O(1) term of
Σ R_r²|S_r|² near the puncture: bounded, not O(|z|²); ebar_check.py) before the seal.
