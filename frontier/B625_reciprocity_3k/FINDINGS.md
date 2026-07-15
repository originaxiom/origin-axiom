# B625 — the reciprocity criterion corrected: 3|κ, not parity (queue item 3 SHARPENED)

**Status: banked (frontier). Campaign round-2 cell H. Reproducer
step4_diagnosis.py.**

The B623 residual was mis-framed as odd-vs-even κ. THE ACTUAL CRITERION:
the Deloup–Turaev evaluation matches EXACTLY iff **3 | κ** (the A₂
lattice discriminant [P:Q] = 3): 48/48 exact at 3|κ (κ = 3..21, worst
deviation 1.8e−9), 0/96 elsewhere with large clean mismatches. Root
cause traced to hypothesis (1) of Deloup–Turaev's Theorem 1 (the form's
values ⟨y, h(y)⟩ land in (2/3)ℤ — the denominator-3 obstruction, an
analytic necessity argument; sufficiency of the hypothesis as the ONLY
obstruction not separately proved). A genuine float-label bug in the
B623 coset enumeration was found and FIXED (it spuriously failed one
term even inside the valid domain at κ = 9, 15). The κ-unconditional
closed form (the general Wu-class machinery or a CRT split at level 3κ)
is set up and remains the scoped residual.
