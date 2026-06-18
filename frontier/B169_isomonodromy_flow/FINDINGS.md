# B169 — the isomonodromy (Painlevé-VI) flow + the firewall-relocation verdict (P1/PR2, completes P1)

**Date:** 2026-06-18. **Status:** completes the Betti→Hitchin direction (P1 of Masterplan II, `OPEN_LEADS` H5-c).
B164 (PR1) built the static (0,4) cubic; this PR2 builds the **deformation** — a working Schlesinger /
Painlevé-VI **flow** — and reaches the verdict. **Result:** the isomonodromy flow exists and is genuinely
**monodromy-preserving** (the one place a continuous "flow/time" enters from within); the metallic monodromy
realizes on it with dynamical degree `λ_m²` (homological method, correcting B164); **but** the flow's "time" is a
dimensionless modulus and the system is scale-free, so **the scale stays external — the Hitchin/dynamical side
RELOCATES the firewall, it does not cross it**, exactly as `../philosophy/P010` / `../docs/STRATEGIC_SYNTHESIS.md`
§8c predicted. Standalone isomonodromy / character-variety math; **no Origin-core claim, no physics, no scale**;
P1–P16 frozen; nothing to `../../CLAIMS.md`. Ledger V161. Reproducer `isomonodromy.py`.

## Results

- **P1 [exact] — the cover dictionary, done right.** The metallic `M_m=[[m,1],[1,0]] ∈ SL(2,ℤ) ⊂ MCG(S_{0,4})`
  acts on the cubic with **dynamical degree `λ_m² = (eigenvalue of M_m)²`** (the homological / Picard-lattice
  degree, Cantat–Loray). m=1,2,3: `λ_m² = (3+√5)/2, 3+2√2, (11+3√13)/2`. **This corrects B164's C4**, which used a
  point-orbit-norm proxy that tracked the *naive* (cancellation-free) degree, not the dynamical degree.
- **P2 [num] — the Schlesinger flow is isomonodromic.** Integrating the Schlesinger system
  `dA_i/ds = [A_3,A_i]/(s−t_i)` (RK4, 4 Fuchsian residues on ℙ¹, one pole `s` moving) **preserves every local
  conjugacy class** — `det A_i` for i=1,2,3 and `tr/det` of `A_∞=−ΣA_i` — to **drift 4.25×10⁻¹⁰** over `s: 2→3`,
  while the residues genuinely move. So the monodromy is conserved along the flow: a real, continuous,
  monodromy-preserving deformation. **Control (non-vacuity):** a non-Schlesinger ODE drifts by **16** (does *not*
  preserve the conjugacy classes) — the preservation is a real property of the Schlesinger system, not an artifact.
- **P3 [structural / POSTULATED] — the firewall-relocation verdict.** The flow's "time" `s` is the **dimensionless
  cross-ratio modulus** (a coupling-space coordinate — the same type-mismatch with physical time as `P006`), and
  the Schlesinger system is **scale-free** (no dimensionful parameter; the flow equation is homogeneous). A
  physical scale would be the **Higgs field's** — i.e. the gauge theory's, **external** (B151). So crossing to the
  Hitchin/dynamical side **relocates** the firewall (to "where does the Higgs scale come from"), it does **not**
  dissolve it.

## What P1 settles (and what stays open)

- **Settled:** the seed's dynamical partner (the Painlevé-VI flow on the (0,4) cubic) is built, verified
  monodromy-preserving, and carries the metallic dynamics (degree `λ_m²`). The category-root prediction is
  **confirmed**: the dynamical side exists, but its scale is external — the firewall relocates, not crosses.
  This grounds the deferred door-4/door-5 sharpening of B167 (the scale enters externally, on the Hitchin side).
- **Open (NEEDS-SPECIALIST, not this sandbox):** the full Hitchin/Higgs-bundle construction (the hyperkähler
  metric, the spectral curve) where the Higgs field's scale lives explicitly; and whether *any* relational
  ("Machian") reading makes that scale internal — expected no, per the relocation verdict.

## Firewall
Standalone isomonodromy / character-variety mathematics. No scale, no Λ, no crossing — the verdict is precisely
that the scale is **external**. Nothing to `CLAIMS.md`; P1–P16 untouched.

## Anchors
B164 (P1/PR1, the static (0,4) cubic + the orbit-norm proxy this corrects), B150 (Cantat–Loray dynamical degree),
B151 (the scale is external), B167 (the conserved⟹no-scale lemma this grounds — door 4/5), P010 + §8c (the
Betti↔Hitchin relocation hypothesis, now confirmed), `speculations/S024` (the Hitchin side), `OPEN_LEADS` H5-c
(→ CHARACTERIZED). Ledger V161. External: Schlesinger equations; Painlevé VI as isomonodromy (Jimbo–Miwa,
Boalch); non-abelian Hodge (Hitchin, Simpson) — the Higgs side where the external scale lives.

## Reproduction
`python frontier/B169_isomonodromy_flow/isomonodromy.py` — P1 (dynamical degree λ_m² via homology), P2 (the
Schlesinger flow preserves monodromy to 1e-10 + the wrong-ODE control), P3 (the relocation verdict). Prints
`ALL CHECKS PASS`.
