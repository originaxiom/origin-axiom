# B183 — the open/driven collective arrow door: opening the metallic collective gives a *thresholdless* arrow

**Date:** 2026-06-22. **Status:** the third hunt of the search specification (`../speculations/S036`) — the
**OPEN / DRIVEN collective** door, the last untested arrow/scale door that `B181` flagged as open ("an *open /
driven / dissipative* large-N collective"). We **computed** it (per the standing directive: we calculate; we mark
NEEDS-SPECIALIST only when the computation is genuinely exhausted — it was *not*; this is decisive). **Result: the
same INVERSION `B181` found for the scale-door.** Opening the metallic collective (a non-Hermitian / driven coupling)
*does* yield a genuine irreversible (non-unitary) spectrum — but at **zero threshold**, *because* the object is
permanently critical (`B181`). Criticality = **maximal fragility** to the open-system arrow, not robustness. And the
threshold is **dimensionless** and the arrow's **source is external** (you must open the system) — so **SCALE stays
external and the arrow is not self-generated: the firewall holds.** **Firewall-side**: emergent non-Hermitian /
localization math (`K010` boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V177.
Reproducer `open_collective.py` (`ALL CHECKS PASS`).

## Two naive probes fail first (recorded so the real one isn't bypassed)

The "open system" instinct is a PT-symmetric (balanced gain/loss) chain. Two natural PT probes are **artifacts**:
- a **halves-split** chain (+iγ left / −iγ right) gives `max|Im(E)| = γ` *exactly* for all γ — a gain-localized
  edge state picks up the full `+iγ`; no threshold, an artifact of the split (not a real PT transition).
- a **staggered** chain (±iγ on alternating sites) gives `γ_c → 0` for **any** onsite `V≠0`: the first-order
  imaginary shift `⟨ψ|W|ψ⟩ = Σ|ψ(n)|²(−1)ⁿ ≠ 0` breaks chiral symmetry, so the metallic **and** the extended-AA
  chain both give `0` — **only `V=0`** is protected, and even that `γ_c→0` with `N`. A **chiral-symmetry** artifact,
  **not** a localization probe (recorded as **C0**).

## The discriminating, theorem-backed probe — Hatano–Nelson

The **imaginary gauge field** `g` (asymmetric hopping `e^{+g}/e^{−g}`) under **periodic** boundaries. The real
spectrum (reversible / unitary-like) develops complex eigenvalues — a non-Hermitian **point gap** = non-unitary,
irreversible evolution `e^{−iHt}` = **an arrow** — at the threshold

> **`g_c = min over the spectrum of the Lyapunov exponent γ(E)` = the inverse localization length** [Hatano–Nelson
> PRL 1996; non-Hermitian skin effect / point-gap topology].

(PBC is essential: under *open* boundaries the gauge field is a similarity transform, the spectrum stays real for all
`g`. The loop obstructs the gauge.)

| model | `g_c` (N=320) | `min Lyapunov` | exact | localization |
|---|---|---|---|---|
| **metallic** (golden Sturmian) | **0.0010 ≈ 0** | ≈ 0 | — (critical) | critical (`B181`) — **thresholdless** |
| periodic (free) | 0.0000 | 0 | 0 | extended — thresholdless |
| **AA-localized** (`V=8cos`) | **1.367** | 1.294 | **ln 4 = 1.386** | localized — **protected** |
| random (uniform) | 0.109 | 0.033 | — | localized — protected |

- **C1 — the metallic collective is THRESHOLDLESS.** Permanently critical (`B181`: `γ≈0` on the spectrum) ⟹
  `min Lyapunov ≈ 0` ⟹ `g_c ≈ 0`: the open metallic chain gains an irreversible (complex) spectrum under the
  *slightest* drive — **no protective threshold.** Criticality = **maximal fragility** to the arrow (the inversion).
- **C2 — a localized control IS protected, exactly.** The Aubry–André localized chain (`V=8cos`, *off* the metallic
  class) keeps a **real** spectrum up to a **finite** `g_c = ln 4 = 1.386` — the *exact* inverse localization length
  (`γ=ln(λ/2)` with `λ=8` → `ln 4`), `~1300×` the metallic. Openness → irreversibility only above a finite drive.
- **C3 — the threshold IS the inverse localization length (the HN theorem).** `g_c` tracks `min`-Lyapunov: `≈0` for
  critical/extended (metallic, periodic), finite for localized (AA, random); AA matches exact `ln 4` to ~5%. The
  openness→irreversibility threshold *is* the localization length — and the metallic object's is **zero**.
- **C4 — FIREWALL: a real arrow, but dimensionless and externally sourced.** The complex spectrum is a *genuine*
  non-unitary / irreversible arrow — qualitatively unlike the **combinatorial** Ω-arrow (`B168`) and the **reversible**
  trace map (`B177`). **But** (a) `g_c` is **dimensionless** (a Lyapunov exponent, lattice units) — **no emergent
  dimensionful scale**; (b) the arrow's **source** is the externally-imposed openness (the imaginary gauge field is
  *input*) — it is **not self-generated**. What *is* intrinsic and new is the **zero threshold** (criticality ⟹ `g_c=0`).

## What this means for the search (S036)

The last open scale/arrow door — "an *open/driven* large-N collective" — is now **computed, not deferred.** The
honest verdict has the same shape as every prior door, with a genuine new structural fact:
- the **ARROW** ingredient is **upgraded** from "✗ combinatorial only" (`B168`/`B177`) to **"~ emergent in the *open*
  collective: a genuine non-unitary spectrum, *thresholdless* for the critical metallic object, but *dimensionless*
  and *externally sourced*."** A real arrow appears when you open the system; criticality makes the conversion
  thresholdless; it is not self-generated and carries no scale.
- the **SCALE** ingredient **stays external** (the threshold/length is dimensionless, lattice units) — consistent
  with `B181`'s verdict and the relocated wall (`K018`/`B169`, the Hitchin/Higgs side).
- the unifying picture: permanent criticality (`B181`) is a **double-edged** property — it *is* the scale-freeness
  (`ξ→∞`, no length) **and** the maximal fragility to the open-system arrow (`g_c=0`, no protective threshold). One
  property, both inversions.

## Scope / honesty
- Tests the **non-Hermitian / imaginary-gauge** (Hatano–Nelson) channel of "open/driven," decisively, for the single
  metallic chain vs three controls (extended, two localized), with the threshold validated against the **exact**
  HN/AA value `ln 4`. It does **not** test a genuinely interacting *many-body* open system (Lindblad/driven-dissipative
  with interactions) — that remains a distinct, larger object (NEEDS-SPECIALIST *for that channel*), but the most
  natural single-particle open-system door (the one `B181` named) is now answered by computation.
- The arrow is a **response** to an externally-imposed openness, not self-generation; no claim that the closed object
  produces an arrow (it does not — `B177`).
- Emergent non-Hermitian / localization mathematics (`K010` boundary); no physical-magnitude claim; nothing to
  `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`../speculations/S036` (the search register — the ARROW ingredient and the open-collective door this closes), `B181`
(permanent criticality = scale-freeness; the `min`-Lyapunov this re-uses), `B168` (the combinatorial Ω-arrow — what
this is *not*), `B177` (the closed trace map is reversible — what opening changes), `K007`/`K010` (the metallic
cocycle / Cantor spectrum, the `K010` boundary), `K018`/`B169` (the relocated external scale, Hitchin/Higgs side).
External: Hatano–Nelson (PRL 1996, imaginary gauge field, real→complex transition at the inverse localization length);
non-Hermitian skin effect / point-gap topology (Okuma–Kawabata–Shiozaki–Sato; Gong et al.); the non-Hermitian
Aubry–André (Longhi 2019, localization ↔ real-complex spectral transition).

## Reproduction
`python frontier/B183_open_collective_arrow/open_collective.py` — C0 the staggered-PT chiral artifact (null);
C1 metallic thresholdless (`g_c≈0`); C2 the localized control protected at exact `ln 4`; C3 the HN theorem
(`g_c = min` Lyapunov); C4 the firewall verdict. Prints `ALL CHECKS PASS`. Fast locks in
`tests/test_b183_open_collective_arrow.py` (3 tests, ~5s).
