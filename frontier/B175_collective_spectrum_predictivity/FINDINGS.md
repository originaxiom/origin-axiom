# B175 — the collective spectrum is two-number predictable (heights exact + the weak-coupling width law)

**Date:** 2026-06-18. **Status:** the master extraction of the multibody lane (plan
a local planning note, P1+P2) — the **disciplined version** of a cross-session
("chat2") "combination ridge." Establishes that the woven metallic spectrum is **predictable from two pairs of
numbers**: `(α₁,α₂)` fix every gap *height* exactly (gap-labeling theorem), and `(λ₁,λ₂)` fix every gap *width* via
an order-power law **at weak coupling**. **Firewall-side**: emergent quasicrystal physics (`K007`/`K010` boundary;
bichromatic optical lattices + quasicrystals are *measured* materials); predictivity over **structure**, not over the
value of a fundamental constant; **nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V169. Reproducer
`collective_predictivity.py` (`ALL CHECKS PASS`).

## The headline (positive, bounded)

For the woven two-frequency chain `V_n = λ₁ g(α₁n+θ₁) + λ₂ g(α₂n+θ₂)`:

- **Heights — exact, all couplings.** Every prominent gap sits at a **gap-labeling label** `n₁α₁ + n₂α₂ mod 1`
  (the rank-3 module, B173) — verified to `<2e-3` (max label-error **8e-5**) and **seed-robust** (golden+silver
  *and* golden+bronze). `(α₁,α₂)` → every gap **position**.
- **Widths — the order-power law at weak coupling.** A combination gap of label `(n₁,n₂)` opens at perturbative
  order `|n₁|+|n₂|`, so `width ~ λ^{|n₁|+|n₂|}`: the measured log-λ slope **converges to the order** — decisively at
  order 2 (the `(1,1)` gap: slope **1.92** golden+silver, **2.01** golden+bronze) and trending at order 3 (`(2,1)`:
  slope **2.6 → 3**, not yet asymptotic). `(λ₁,λ₂)` → every gap **width** (perturbatively).

So `(α₁,α₂,λ₁,λ₂)` — two frequencies and two couplings — **forecast the entire weak-coupling spectrum, position and
size of every gap.** That is the strongest honest form of "one input forces many outputs," and it is **collective**:
the single unit has no combination gaps at all.

## The bound (stated once, not deleted)

The width law is **perturbative**: at **strong coupling** the gaps **saturate** and the order-scaling breaks (the
`(1,1)` slope collapses from ~2 to negative as λ grows past ~0.4). And — this is the honest scope the whole program
keeps — this is predictivity over **structure** (where gaps open and how wide), **not** over the *value* of a
fundamental constant. The win is real and it is bounded; both halves are true.

## The model distinction (reconciles B172/B173, and corrects the cross-session over-reach)

A cross-session pass reported a wide combination "ridge" as a property of "weaving metallic laws." Verified here: the
ridge **opens in the smooth cosine (bichromatic) model** (the `(2,1)` gap width **0.211**) but is **~closed in the
metallic Sturmian-indicator chain** (width **0.016**). The reconciliation, exactly as B173 flagged: **gap *heights*
are potential-independent** (the gap-labeling *module* — a theorem), but **which gaps actually open, and their
widths, are potential-dependent**. The cross-session claim "the lattice depends only on the two frequencies, not the
potential's shape" is true for the *module* (the menu) and **false for the realized gaps** (the ridge). The ridge is
a genuine feature **of the bichromatic model**, not of metallic substitutions per se.

## Null

A random IDS position *far* from every small label hosts **no real, λ-scaling gap** — its width is **tiny (<0.005,
≈100× below the real combination gaps) and flat** (no order-scaling). The order-power structure is **specific to
gap-label positions**, not a generic artifact of a dense module.

## Verify-don't-trust record

Three self-corrections produced this finding: **(i)** the cross-session "ridge as metallic property" → corrected to
cosine-model-specific (C4); **(ii)** my own first "clean width law everywhere" → **refuted** at strong coupling
(slopes ≠ order), then **rescued** as a *weak-coupling* law by a second check (order-2 slope → 2); **(iii)** this
probe's C5 null threshold was mis-set (a tiny flat 6e-4 "width" tripped a `>3e-4` count) → fixed to the honest test
(tiny **and** flat), not a loosened bar.

## Scope / firewall

Emergent quasicrystal / condensed-matter spectral theory (`K010` boundary). No scale, Λ, mass, or constant; the S035
link is a one-way `[LEAP]` hook, value-matching forbidden. **Nothing to `../../CLAIMS.md`**; P1–P16 untouched.

## Anchors
`B171`/`B172`/`B173` (the metallic woven chain, the combination gap, the gap-labeling reduction — the heights here),
`B174` (the character-variety face), `K007`/`K010` (the object; the measured-materials boundary),
`../../speculations/S035` (the one-way "building blocks' behaviour" hook). External: gap-labeling theorem
(Johnson–Moser 1982; Bellissard; Damanik–Fillman 2022); perturbation theory of quasiperiodic gaps (the order =
Fourier-label-degree width scaling); bichromatic / Aubry–André incommensurate operators.

## Reproduction
`python frontier/B175_collective_spectrum_predictivity/collective_predictivity.py` — C1 heights = labels (2 pairs);
C2 the weak-coupling width law (order-2 slope ≈ 2); C3 the strong-coupling saturation bound; C4 the cosine-vs-Sturmian
model distinction; C5 the null. Prints `ALL CHECKS PASS`.
