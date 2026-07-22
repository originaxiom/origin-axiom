# FINDINGS — B764: C19's first out-of-field test — LAW-BREAKS as stated; the corrected law found in the same run

cc banking seat, 2026-07-22. Prereg df0f8e1c sealed with the prediction declared (5₂ must
give √23 if C19's √|disc K| form is a trace-field invariant). Gate 5; nothing to CLAIMS.

## The result

- **Control (m004): the port is faithful** — B759's recipe reproduced exactly (per-mixed-word
  Im = √3; the commutator 4√3; coupling fraction 15/32 to the digit).
- **The prediction FAILS**: 5₂'s per-trace off-block = 2.614283 = 2·Im(u_geo), not
  √23 = 4.795832. **C19 as stated (off-block = √|disc K|) is NOT a general trace-field
  invariant.**
- **The corrected law, found and verified in the same run**: the off-block is
  **|u_geo − ū_geo| — the geometric Riley pair's own separation** — ALWAYS. For an
  imaginary-QUADRATIC Riley field this equals √|disc K| identically (the quadratic-formula
  identity: the pair is the whole root set), which is why m004 and every field-mate shows
  √|disc|. For higher degree the discriminant factors as
  disc = (u−ū)² · ∏ᵢ[(u−rᵢ)(ū−rᵢ)]² and the off-block is only the FIRST factor —
  verified at 5₂ to 40 digits ((z−z̄)²·[(z−r)(z̄−r)]² = −23.000…0 exactly;
  off·m² = √23 to 40 digits).
- Note also: the coupling fraction is NOT universal either (5₂: 0.311037 vs m004's 15/32) —
  it is an object/field quantity, consistent with B759's in-family Galois-invariance claim.

## Consequences applied

- **C19 scope-corrected in the chain**: the √|disc K| form is a THEOREM for
  imaginary-quadratic Riley fields (m004's √3 is real content — the identity is exact,
  and quadratic is the object's own case); the GENERAL law is the pair-separation form.
  The correction strengthens, not weakens: the general statement is cleaner and the
  quadratic case is now proven rather than induced from one family.
- The one-day-old chain link caught and corrected by its own going-forward discipline —
  the first demonstration that chain entries are falsifiable objects, not trophies.

Artifacts: compute.py + output.txt (control + prediction + the 40-digit correction).
Lock: tests/test_b764_c19.py.
