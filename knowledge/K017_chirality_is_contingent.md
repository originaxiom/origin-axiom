# K017 — Chirality is contingent: the canonical once-punctured-torus family is the self-mirror family

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. The
> bankable MATH of Campaign 1′ (B145/V134) — the deepest form of the firewall, on the chirality axis.

## The question

The firewall's one *proven* obstruction to SM-like physics is **chirality** (parity violation). B144 showed
seed-heterogeneity (gluing distinct metallic bundles) injects *contingency* (a discrete `κ`-fork, B131) but **not**
chirality-breaking — the composite family is mirror-closed. Its redirect: preferred handedness needs **breaking the
construction's `R↔L` mirror symmetry** — a **chirally-asymmetric input** (a monodromy / substitution not fixed by
swap+reverse). Campaign 1′ (B145) asks the decisive question: **can such an input be *forced* (canonical /
zero-parameter), or does forcedness imply mirror-symmetry?**

## The criterion (GHH 2008, B128/B136)

A once-punctured-torus bundle `b++W` is **amphichiral ⟺ its `R/L` monodromy word `W` is anti-palindromic**
(`swap_{R↔L}(W)` is a cyclic rotation of `reverse(W)`) — equivalently its continued-fraction period is **palindromic**.
The metallic family `RᵐLᵐ` (period `[m]`, the metallic means — the canonical/arithmetic family) is **exactly the
self-mirror family**, so every metallic bundle is amphichiral. **Chirality = leaving the palindromic-period locus.**

## The result (B145, computational)

A catalog of o-p-t bundles (cyclic-primitive `R/L` words, length ≤ 7; n = 39), each classified by the GHH criterion
(cross-checked against SnapPy `is_amphicheiral` — **agreement on all 39**) with volume and trace-field degree:

- **The minimal-volume o-p-t bundle is the figure-eight `RL` (vol 2.02988) = metallic m=1 = amphichiral**; the minimal
  **chiral** bundle is `RRL` (vol 2.66674), **strictly larger** — chirality first appears *above* the canonical minimum.
- **Trace-field degrees: amphichiral ∈ {2, 8}; chiral ∈ {4, 6, 8, 12}.** Every **quadratic** (imaginary-quadratic =
  arithmetic-candidate) bundle is **amphichiral** — there is **no arithmetic chiral o-p-t bundle** in range. The
  strongest canonicity (arithmeticity) ⟹ amphichirality.
- The **simplest/forced substitution** (Fibonacci `a→ab, b→a`, monodromy `RL`) is self-mirror.

**Verdict (MATH, over the catalogued range + the arithmetic-degree correlation):** the canonical selection — minimal
volume / quadratic (arithmetic) trace field / simplest substitution / palindromic period — **coincides with the
self-mirror (amphichiral) condition**; chirality requires leaving the canonical locus (non-palindromic, larger,
higher-degree input). *Honest scope:* a computational/empirical statement, **not** a theorem that every conceivable
canonicity principle forces amphichirality.

## The reading (POSTULATED — firewalled)

**Preferred handedness (parity) is irreducibly contingent** — it cannot be forced from a zero-parameter / minimal
principle; it requires a choice of handedness no such principle makes. This is the **deepest statement of the
firewall**: *forced ⟹ self-mirror ⟹ no parity; parity lives strictly on the contingent side* (the chirality-axis
instance of `forced ≠ contingent`). It also *locates* where chirality could come from — a non-palindromic /
non-arithmetic / non-minimal (contingent) input — which is the informative residue, not a crack.

## What this is, and is not

It is **MATH** (which o-p-t bundles are amphichiral, and how that correlates with canonicity) plus a firewalled reading.
It is **not** a K-A revival: K-A ("det=−1 selects SM chirality") is DEAD/inverted (det=−1 → CS=0 → amphichiral); B145
reaches the **opposite, firewall-reinforcing** conclusion (chirality is non-canonical). No metallic object with CS≠0 is
claimed — chiral o-p-t bundles are *non-metallic* (B128), consistent with K-A. The `det`/φ² facts (`K011`/B140) are
descriptive only.

**Anchors:** B145/V134 (the catalog + verdict), B144 (the redirect — chirality needs an asymmetric input), B128/B136/
`K011` (the GHH anti-palindromic criterion; the chirality recursion), B141 (finiteness/density), `../speculations/S032`
(the interaction program), `../docs/STRATEGIC_SYNTHESIS.md`, `../speculations/TOMBSTONES.md` (`K-A`, not revived).
External: Goodman–Heard–Hodgson 2008 (arXiv:0801.4815); Bowditch–Maclachlan–Reid (arithmetic punctured-torus bundles);
palindromic continued fractions ↔ amphichirality.
