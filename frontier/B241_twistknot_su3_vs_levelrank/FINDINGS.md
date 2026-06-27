# B241 — the twist-knot SU(3) (Gang–Yonekura) vs our level-rank SU(3)₂ (B238): two different SU(3)'s

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Resolves the §6 horizon question of the PC19 paper. Run: `python twist_su3.py` (pyenv).

## The question (§6 horizon)
Is the **Gang–Yonekura twist-knot SU(3)** the same as our **level-rank SU(3)₂** (B238)? The figure-eight sits in
both the metallic and twist-knot families, so the two SU(3)'s meet at `4₁` — are they one object?

## The two SU(3)'s (verify-don't-trust, incl. verifying the negative)
- **(A) Gang–Yonekura** [arXiv:1803.04009, JHEP 07(2018)145]: a global **flavor** symmetry of the 3d `N=2` theory
  `T[K]`, enhanced from `U(1)`, present for **all hyperbolic twist knots**, built from the `A₁` (=SU(2)) 6d `(2,0)`
  theory. → **universal** across the twist family; a *surprise* (not predicted from CS level structure).
- **(B) ours** [B238]: a Chern–Simons **gauge** group `SU(3)₂`, the level-rank dual of `SU(2)₃` (shared
  `κ=k+N=5`), whose figure-eight WRT coincides at `−1/φ`. → **figure-eight-specific** (fails for silver/bronze),
  golden.

## Verdict: distinct — different *type* and different *specificity*
1. **Type:** (A) is a *flavor* symmetry of an SCFT; (B) is a *gauge* group of a CS/WRT theory. Categorically
   different roles.
2. **Specificity:** (A) is **universal** across all hyperbolic twist knots; (B)'s `−1/φ` coincidence is
   **golden/figure-eight-specific**. If they were the same SU(3), the level-rank coincidence would be
   twist-knot-universal — it is not.
3. **Level:** (A) is independent of any CS level; (B) *is* the specific level-rank pair `SU(2)₃↔SU(3)₂` (`κ=5`).

A self-check of the negative (this session's lesson): could (A) secretly be (B)? No — (A) holds for *all*
hyperbolic twist knots and is explicitly a *surprise not predicted from CS level structure*, whereas (B) is a
level-specific (`κ=5`) duality; a flavor symmetry is not a gauge group. The conflation is exactly the kind of
same-letter glue the program guards against.

## Computational corroboration (this file + reused)
- **Within GY's own family**, only `4₁` is amphicheiral, so only `4₁` gives a **real (golden, `∈ℚ(√5)`)** `SU(2)₃`
  colored Jones at the golden root (in fact pure-`ℤ`, B240); `5₂, 6₁` are chiral → **complex** (`∈ℚ(ζ₅)`). The
  golden/level-rank structure is `4₁`-specific *within the twist family* — orthogonal to GY's universal SU(3).
  (SnapPy confirms `4₁` is the unique Jones-palindromic = amphicheiral twist knot; `5₂,6₁,7₂,8₁,9₂` are chiral.)
- **(reused B238)** the level-rank `SU(2)₃↔SU(3)₂` WRT coincidence is figure-eight-specific in the metallic family.

## Firewall note
This further deflates the `H37` SM-emergence rhyme: even the *two SU(3)'s* the program touches (the flavor
enhancement and the level-rank gauge dual) do **not** unify — they are different objects. The physics framing
(SU(3) = the strong force) stays firewalled. A clean *distinction*, not a bridge.

Anchors: B238 (level-rank SU(3)₂), B240 (golden colored Jones / the R-matrix tool), B71/B129 (the SL(3,C)
figure-eight — a *third*, again distinct, "SU(3)": the higher-rank character variety). Literature: Gang–Yonekura
arXiv:1803.04009; Naik–Ramadevi et al. arXiv:2106.15012 (level-rank duality of knot invariants).
