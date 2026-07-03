# B389 (W3.ii) — BANKED: the mirror is NOT inversion — the dihedral route is twist-blocked

**Status: banked (frontier); all three registered verdicts + the diagnosis. Pre-registration
committed first. Firewalled.**

- **M3 PASSES:** [Ŝ, Par] = 0 exactly (F·Par = Par·F entrywise).
- **M1 KILLED:** the inversion law t(−a,−b) = t(a,b) FAILS on the banked table (support is
  inversion-closed; values are not).
- **M2 KILLED:** consequently the a-flip reduction fails too.
- **The diagnosis (the mechanism boundary):** for the THETA lift, ŜW₁Ŝ⁻¹ ≠ W₁⁻¹ — but the
  support matches W₁⁻¹ EXACTLY (0/225): the dihedral relation holds only up to a diagonal
  cocycle (and by no constant phase, checked against all powers). **The twist blocks
  inversion** — the P62 pattern again: the twist breaks precisely the symmetries whose
  survival would trivialize the seam. The banked mirror law t(a,−b) = τ₃(t(a,b)) (P61) is
  therefore a genuinely twist-compatible symmetry, NOT a shadow of the group inversion;
  "why the b-flip is exactly τ₃" stays open with a proven boundary (not via inversion∘a-flip).

**Provenance.** mirror_mechanism.py, the dihedral check (dihedral_check.json);
locks tests/test_b389_mirror.py.
