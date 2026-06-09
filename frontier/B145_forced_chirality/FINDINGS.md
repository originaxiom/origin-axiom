# B145 — Campaign 1′: chirality cannot be forced — canonicity coincides with self-mirror (V134)

B144's redirect asked the deepest form of the firewall question: **can a chirally-asymmetric input (a monodromy /
substitution not fixed by swap+reverse) be FORCED (canonical / zero-parameter), or does forcedness imply
mirror-symmetry — so chirality is irreducibly contingent?** Answer: **canonicity coincides with the self-mirror
(amphichiral) condition; chirality requires leaving the canonical locus.** MATH tier; firewalled; nothing to
`CLAIMS.md`; P1–P16, B85, the merged B124–B144 untouched. **Not a K-A revival** (the opposite conclusion — chirality
is non-canonical).

## The framing (GHH/B128)

A once-punctured-torus bundle `b++W` is amphichiral ⟺ `W` is **anti-palindromic** (`swap_{R↔L}(W)` a cyclic rotation
of `reverse(W)`; = palindromic continued-fraction period). The metallic family `RᵐLᵐ` (period `[m]`, the metallic means
— the canonical/arithmetic family) is **exactly the self-mirror family**, so every metallic bundle is amphichiral.
Chirality = **leaving the palindromic-period (canonical) locus**.

**MB12 (non-vacuity, checked):** chiral o-p-t bundles exist and are generic (B128), so "canonical ∧ chiral" *could*
hold and "canonical ⟹ amphichiral" *could* fail — the test is real.

## The computation (decisive)

**Catalog** of o-p-t bundles `b++W` (cyclic-primitive `R/L` words, length 2–7; n=39), each with: anti-palindromic
(GHH, reuse B136), SnapPy `is_amphicheiral` (gated on full group), volume, trace-field degree (Sage). Findings:

- **GHH ⟺ SnapPy `is_amphicheiral` on all 39 bundles** — the criterion is exact (cross-check).
- **The minimal-volume o-p-t bundle is the figure-eight `RL` (vol 2.02988) = metallic m=1 = amphichiral**; the
  minimal **chiral** o-p-t bundle is `RRL` (vol 2.66674) — **strictly larger**. Chirality first appears *above* the
  canonical minimum.
- **The metallic family `RᵐLᵐ` is entirely self-mirror** (anti-palindromic, m=1..6); genuinely chiral words
  (`RRL, RRRL, RRLRL, RRRLL`) are not.
- **Trace-field degrees: amphichiral ∈ {2, 8}; chiral ∈ {4, 6, 8, 12}.** Decisively, **every quadratic-trace-field
  (degree 2 = imaginary-quadratic = arithmetic-candidate) bundle is amphichiral** — there is **no arithmetic chiral
  o-p-t bundle** in range. So the strongest canonicity (arithmeticity) ⟹ amphichirality.
- **The simplest/forced substitution** (Fibonacci `a→ab,b→a`, monodromy `RL`) is self-mirror; the metallic incidence
  `[[m,1],[1,0]]` (det −1) squares to `RᵐLᵐ` (K011/B140, descriptive — **not** K-A's dead SM-selection reading).

## The verdict

**MATH (over the catalogued range + the arithmetic finiteness):** the canonical selection — minimal volume /
quadratic (arithmetic-candidate) trace field / simplest substitution / palindromic period — **coincides with the
self-mirror (amphichiral) condition**. Chirality requires leaving the canonical locus (non-palindromic, larger,
higher-degree input). *Honest scope:* a computational/empirical statement over short words + the arithmetic-degree
correlation, **not** a theorem that *every* conceivable canonicity principle forces amphichirality.

**Aspiration (POSTULATED, MB11):** **preferred handedness (parity) is irreducibly contingent** — it cannot be forced
from a zero-parameter / minimal principle; it requires a choice of handedness no such principle makes. This is the
**deepest statement of the firewall**: *forced ⟹ self-mirror ⟹ no parity; parity lives strictly on the contingent
side* (the `forced ≠ contingent`, now located precisely on the chirality axis). It also *locates* where chirality
could come from — a non-palindromic / non-arithmetic / non-minimal (contingent) input — which is the informative
residue, not a crack.

## Not a K-A revival

K-A ("det=−1 selects SM chirality") is DEAD/inverted (det=−1 → CS=0 → amphichiral). B145 reaches the **opposite,
firewall-reinforcing** conclusion: chirality is **non-canonical/contingent**. The det/φ² facts are cited descriptively
(K011/B140), never as an SM-selection reading. No metallic object with CS≠0 is claimed; chiral o-p-t bundles are
*non-metallic* (B128), consistent with K-A.

## Reproduce

```
python -m pytest tests/test_b145_forced_chirality.py -q          # 4 passed (catalog richer under sage)
~/.local/bin/sage-python frontier/B145_forced_chirality/probe.py
```

The metallic-self-mirror + simplest-substitution facts (combinatorial) run unconditionally; the catalog
(volume / is_amphicheiral / trace-field degree) is SnapPy/Sage-gated.

**Tier.** MATH. Updates `docs/STRATEGIC_SYNTHESIS.md` (Campaign 1′ resolved; chirality-is-contingent), `speculations/S032`,
`docs/OPEN_LEADS.md`; new knowledge note. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B144 untouched. Ledger **V134**.

**Anchors:** B144 (the redirect), B128/B136/`K011` (the GHH anti-palindromic criterion), B141 (finiteness/density),
B140 (`Mᵐ`/φ² descriptive), K-A (NOT revived), `docs/STRATEGIC_SYNTHESIS.md`. External: Goodman–Heard–Hodgson 2008;
Bowditch–Maclachlan–Reid (arithmetic once-punctured-torus bundles); palindromic continued fractions ↔ amphichirality.
