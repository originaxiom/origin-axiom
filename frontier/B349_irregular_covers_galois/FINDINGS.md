# B349 — gate A extension: irregular covers through index 6 — canonical multisets, no forced choice (conditional)

**Status: banked (frontier) as a CONDITIONAL structural result. Attacks gate A (S032-A) in-sandbox,
extending B330/B350/B348 to another named untested class. Firewalled; nothing to `CLAIMS.md`.**

B350 sealed the **cyclic** cover tower; the untested residual still named **irregular** (non-normal)
covers. This probe enumerates **all** covers of the figure-eight through index 6 (SnapPy subgroup
enumeration) and runs the gate-A question at each index.

## Verified (SnapPy 3.3.2; census banked as exact integers)
- **(i) Cross-validation of B350.** The cyclic covers' `H₁` torsion from SnapPy's group
  enumeration equals B350's `coker(Aⁿ−I)` Smith normal forms **exactly** (`n=2..6`: `[5]`,
  `[4,4]`, `[3,15]`, `[11,11]`, `[8,40]`) — two independent routes (subgroup enumeration vs.
  monodromy algebra), one answer.
- **(ii) The cover census is a canonical multiset.** Per index: `4` → 1 cyclic + 1 irregular
  (`H₁ = ℤ²`, torsion-free); `5` → 1 cyclic + 3 irregular (`ℤ³`; two copies of `ℤ/2⊕ℤ²`);
  `6` → 1 cyclic + 10 irregular (4× `ℤ/3⊕ℤ²`, 2× `ℤ/12⊕ℤ`, 2× `ℤ/5⊕ℤ²`, 1× `ℤ/2⊕ℤ/4⊕ℤ²`,
  1× `ℤ/4⊕ℤ/8⊕ℤ`). The multiset is what the object determines; no member carries a mark.
- **(iii) Every within-index invariant multiplicity is resolved by isometry.** The two index-5
  `ℤ/2⊕ℤ²` covers are **isometric** (4 isometries); each index-6 multiplicity group (4×, 2×, 2×)
  collapses to a **single isometry class**. The "distinct" members are one geometric object seen
  through non-conjugate subgroups — a distinction invisible to every manifold invariant, and the
  identification is realized by the object's own symmetries (the covering isometries live in the
  commensurator; the same self-identification pattern as B348's amphichiral sign-kill; cf. B323's
  commensurator level).

## MB-guard note
`is_isometric_to()` is orientation-**blind** (REPRODUCIBILITY MB/B128). That is *sufficient
here, honestly*: gate A asks whether the object **distinguishes** a member; identification by
*any* self-isometry already defeats a forced choice. (No chirality claim is being made — that
would need the amphichirality protocol.)

## Honest scope (C-guardrail)
Index ≤ 6 is a **computational horizon, not a theorem**. The class "all irregular covers" stays
formally open beyond it; so do the other named residual classes (nonabelian Ptolemy/adjoint
torsion, CS/`η` beyond `CS=0`, `SL(n≥3)` gluing invariants, extended-Bloch/`K₃` torsion).

## The firewall (held)
A structural (no-value) statement: the only outputs are homology types and isometry counts of
covers, all canonical/multiset-level. Nothing to `CLAIMS.md`.

## The fence
SnapPy subgroup/cover enumeration + homology + `is_isometric_to` (with the MB note above);
banked census asserted as exact integers. `irregular_covers.py` ·
`tests/test_b349_irregular_covers_galois.py` (importorskip-gated on SnapPy, like the other
SnapPy locks). Related: **B330** (mechanism), **B350** (cyclic tower; SNF cross-validated here),
**B348** (self-symmetrization), **B326** (the `n=3` cover), **B323** (commensurator level),
**OPEN_PROBLEMS.md** gate A. Lit: standard low-index subgroup enumeration; SnapPy census
methods (Culler–Dunfield–Goerner–Weeks).
