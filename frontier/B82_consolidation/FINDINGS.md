# B82 (Phase 3) — consolidation, novelty positioning, and the physics-chapter close

**Date:** 2026-06-05. **Status:** synthesis / positioning (no new theorem; backed by the V53–V64
locking tests). Standalone low-dim topology / invariant theory; **no Origin-core claim**; proven core
P1–P16 untouched. Script: `probe.py` (prints the synthesis tables). Test: `tests/test_b82_consolidation.py`.

This consolidates the two governed exploration runs (V53–V64) into the coherent picture they actually
support, positions the results against the literature (internally — no external contact), and formally
closes the physics-probing chapter.

## 1. The three real threads (synthesis)

The repository's genuine mathematical content is **low-dimensional topology + invariant theory of
`sl(n)`**, organized into three threads:

1. **The SL(n) metallic tower factorization** (B48–B66, B80). The `(n²−1)`-dim fixed-line Jacobian
   `J(m)` of the metallic trace map factors over the Dickson catalog `char(±Mᵏ)`, `L_k=tr([[m,1],[1,0]]^k)`,
   with a **proven parity grading** (B64: even-`|k|` P-symmetric, odd-`|k|` P-antisymmetric) and the
   **opposition-involution `θ=−w0` sector structure** (B62). **NEW (B80/V62):** the SL(4) tower is now
   established **from first principles** (CRT/F_p symbolic-m Jacobian), upgrading B65's float-numerics;
   **(B81/V63):** SL(5) hits the doubly-degenerate even-k gauge-corruption barrier (the residual
   `e₂=tr(Λ²A)` two-block obstruction, B58).
2. **The figure-eight A-polynomial connection** (B67, B71). The trace-map fixed locus reproduces the
   **Cooper–Long figure-eight A-polynomial exactly** at SL(2) (B67), and the **Falbel SL(3)
   Dehn-filling A-variety** (`W1=D2: M³=L`, `W2=D3: M³L=1`; B71, arXiv:1412.4711). Meridian and
   longitude come from the bundle monodromy `t`.
3. **degree=rank** (B73, B75, B77). On the rank-`n` figure-eight bundle's **principal** Dehn-filling
   component `{tr A=tr A⁻¹=1}`, the longitude is the **signed `n`-th power** of the meridian:
   **`[A,B] = (−1)ⁿ⁻¹ μⁿ`** (B77/V60). Confirmed at `n=3,4` and across the odd metallic `m`-axis
   (`m=1,3` at `n=3`) — a two-parameter `(m,n)` rank invariant on **every computable cell** (B79/V64).

These three threads are **one object**: the SL(n) figure-eight / metallic character variety. Thread 1 is
its trace-map dynamics (Jacobian spectrum); threads 2–3 are its peripheral (cusp) geometry. **B77 showed
they are *not* unified through the eigenvalue spectrum** — degree=rank is peripheral, the tower is the
Jacobian — a distinction worth keeping.

## 2. Novelty positioning (internal; no external contact)

- **Tower factorization:** the trace-map machinery is largely `STANDARD_REPACKAGE` (Lawton;
  Baake–Grimm–Roberts; B53), but the **SL(n) fixed-line factorization over the Dickson catalog** with
  the parity/opposition structure (B62/B64) was flagged `APPARENTLY_NEW` (PC12 Thm 4). The **CRT/F_p
  first-principles derivation** (B80) is a clean computer-assisted method; the SL(4) result confirms B65.
- **degree=rank:** the **SL(3)** case **is Falbel's Dehn-filling A-variety** (B71 = Falbel et al.,
  arXiv:1412.4711) — *known*. The **general `degree=rank` pattern** (`[A,B]=(−1)ⁿ⁻¹μⁿ` on the principal
  component, all `n`) and the SL(4) `M⁴=L` are a **natural conjecture in the Bergeron–Falbel–Guilloux
  framework** for SL(n) figure-eight character varieties; I am not aware of it being stated explicitly,
  so label **`APPARENTLY_NEW` (pending an external literature check)**. The honest signals: it is an
  `n≥3` phenomenon (A0: SL(2) is degenerate), it is **not** `Sym^{n−1}` of an SL(2) filling, and the
  `n` is almost certainly the **Falbel filling slope** of the principal component (the likely mechanism,
  B77 having localized it to the peripheral structure). **This is the one result most worth a real
  literature check before any external claim.**

## 3. The physics chapter — formally closed

Every attempt to cross from this mathematics into 3+1D physics has returned **negative or
"same-structure-coincidence,"** across two campaigns:

| probe | verdict |
|---|---|
| metallic anyons / TQC (V28) | categorifies only at `m=1` (Ostrik) — no family |
| SL(n) quasicrystal spectra (V29) | symplectic obstruction (`SL(n)=Sp` only at `n=2`) |
| j=1728 / Seiberg–Witten (V34/V37/V53) | forced CM coincidence, no Coulomb family |
| higher-spin / W_N (V56) | parity grading = `−w0` of `A_{n−1}` — same Lie algebra, no bridge |
| cusp-torsion / quantum group (V58) | `2cos(π/k)` — just roots of unity, no MTC family |

**Verdict: there is no physics here.** The recurring kernel of every "bridge" is the *invariant theory
of `sl(n)`* (2+1D / representation-theoretic), never a 3+1D / gravity / dynamical crossing. The
physics-probing chapter is **closed**; future runs should not re-litigate these kills without genuinely
new evidence (a computation that changes the picture), per the standing discipline.

## 4. Phase-3a note (symbolic-exact M⁴=L)

degree=rank at SL(4) is `high-precision-numerical` (V54, `M⁴=L` to ~1e-39 — already certain). A
symbolic-exact upgrade over `ℚ(ω)` was **attempted and is intractable**: the symbolic 4×4 inverse
(needed for the inverse-word trace conditions) + the nonlinear solve over `ℚ(ω)` stalls (sympy did not
return on 8 equations / 8 unknowns in >2.5 min), confirming the SL(3)-only nature of B71's adjugate
trick. Per the plan, the **high-precision `~1e-39` result (V54) stands**; the marginal value of a
symbolic upgrade over an already-certain `1e-39` is low.

## Reproduce

```bash
python frontier/B82_consolidation/probe.py
python -m pytest tests/test_b82_consolidation.py -q
```
