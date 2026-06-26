# B226 / L43 — the two-SUSY bridge resolved: two faces, separated by the hyperbolic / non-hyperbolic divide

**Date:** 2026-06-26. **Status:** the deepest open question (L43), scouted to a literature-grounded resolution.
The same golden/figure-eight object carries supersymmetry twice — are they one structure or two faces? **Two
faces**, and the literature makes the separation sharp. Firewall: dimensionless CFT/CS bookkeeping + **cited**
literature facts; the physics reading is firewalled in `speculations/S040`. **Nothing to `CLAIMS.md`; P1–P16
untouched.** Ledger **V229**.

## The two sides (grounded)

| | Side A — emergent chain SUSY (B221/B222) | Side B — licensed 3d-3d SUSY (K006) |
|---|---|---|
| object | golden = Fibonacci = **SU(2)₃** anyon chain | figure-eight `4₁` (= the golden `m=1` bundle) |
| theory | tricritical Ising `M(4,5)` | `T[4₁]`, a 3d N=2 theory |
| Chern–Simons | **unitary SU(2)₃** (coset) | **complex SL(2,ℂ)** = 3d gravity |
| SUSY | **N=1** superconformal (2d) | **N=2** (3d); `M_SUSY = M_flat` = char variety (40a1) |
| invariant | `c = 7/10` (`SU(2)₃` WZW `c=9/5`) | `Vol = 2.0299`, `CS = 0` |

## The resolution (literature)

The two SUSYs are **two faces**, separated precisely by the **hyperbolic / non-hyperbolic** divide:

- **2D Virasoro minimal models — including the supersymmetric ones (the tricritical Ising) — are realized as 3d
  bulk theories from NON-hyperbolic (Seifert / torus-knot) 3-manifolds**, via `T[SU(2)]` with `SU(2)_k`
  Dehn-filling:
  - Gang–Kang–Kim et al., *Non-hyperbolic 3-manifolds and 3D field theories for 2D Virasoro minimal models*
    (arXiv:**2405.16377**): `M(P,Q) ↔` Seifert `S²((P,P−R),(Q,S),(3,1))`; **TCI `M(4,5)` via
    `S²((5,−1),(4,5),(3,1))`**.
  - *…bulk field theories for **supersymmetric** / `W_N` minimal models* (arXiv:**2511.04524** = JHEP 03(2026)066).
  - *Torus Knots and Minimal Models Revisited: Rational VOA characters from **non-hyperbolic** knots*
    (arXiv:**2512.23122**).
- **The figure-eight is hyperbolic**, so its 3d-3d theory `T[4₁]` is the **complex-SL(2,ℂ) / 3d-gravity** object
  (`Vol=2.0299`), **not** a minimal model (e.g. arXiv:**2401.13900**, *3d gravity from Virasoro TQFT*, analyzes
  `4₁` explicitly).
- The Fibonacci-state tricritical SUSY can even be **fractional** (coset-CFT) supersymmetry (arXiv:**1905.09960**),
  distinct again from the standard golden chain's N=1 superconformal.

**So the genuine shared ingredient is `SU(2)₃` (through `T[SU(2)]` / `SU(2)_k` Chern–Simons), NOT the
figure-eight's hyperbolic geometry.** The golden-chain CFT (TCI) lives on the **non-hyperbolic / minimal-model**
side; the figure-eight knot (the golden `m=1` bundle) lives on the **hyperbolic / 3d-gravity** side. They are two
distinct 3-manifolds / theories in the **same Class-R / 3d-3d framework** — two faces, not one structure.

## What it rhymes with (firewall-clean)
This mirrors the repo's banked **closed-Sol vs cusped-hyperbolic duality** (B217/V200): golden sits on *both*
sides of a hyperbolicity split, as **different manifolds** — there the period (algebraic, closed) vs the volume
(geometric, cusped); here the minimal-model CFT (non-hyperbolic) vs the 3d-gravity theory (hyperbolic).

## Verification (verify-don't-trust the literature scout)
The load-bearing papers were checked against their **actual arXiv abstracts** (not just the summarizer): 2405.16377
(Gang–Kang–Kim, minimal models ↔ Seifert), 2512.23122 (Gang–Park–Sohn, torus-knot minimal models), JHEP 03(2026)066
and JHEP 01(2025)027 (SUSY / non-unitary N=1 minimal models from 3-manifolds) — all **real and as cited**. One
correction: an earlier full-text summary suggested a "hyperbolic-link alternative" construction; the **abstract is
Seifert-only**, and "Choi–Gang–Kim 2022" is *Infrared phases of 3D class R theories* (not a hyperbolic-link →
minimal-model recipe). So "two faces" is verified and slightly stronger: there is **no established construction
giving the figure-eight a minimal model**. (Residual, registered as a thread: a *non-canonical* class-R/hyperbolic
construction could conceivably engineer one — unestablished, not a counterexample.)

**New lead surfaced (L45):** B224's metallic chains → `M(m²+3, m²+4)`, and Gang–Kang–Kim realize `M(P,Q)` via the
Seifert space `S²((P,P−R),(Q,S),(3,1))` — so each metallic SUSY chain has an **explicit Seifert-3-manifold dual**.
Computing that family (and whether the metallic Seifert data is special) ties B224 to the active 3d-3d program.

## Honest status / tiers
- the central charges / level bookkeeping (`SU(2)₃` WZW `9/5`; coset `7/10`): **`[exact]`** (firewall-clean).
- the resolution "two faces, separated by hyperbolicity": **`[literature-grounded]`** — the minimal-model ↔
  non-hyperbolic / figure-eight ↔ hyperbolic split is established (Gang et al.; cited), not derived in-sandbox.
- the **exact** figure-eight `3d-3d → 2d` reduction: **NEEDS-SPECIALIST** (the qualitative answer is settled; the
  explicit boundary computation is not in-sandbox).
- novelty of the *framing* (golden splitting across the hyperbolicity divide) UNCHECKED.

## Reproduction
- `python l43_grounding.py` (pyenv) — the two-side bookkeeping + the verdict + references.
- `tests/test_b226_two_susy_bridge_L43.py` — the central charges + the verdict structure + the references.

## Net
L43 resolved: the object's two supersymmetries are **two faces**, separated by the hyperbolic / non-hyperbolic
divide. The TCI (golden chain) comes from a non-hyperbolic Seifert space via `T[SU(2)]`; the figure-eight is
hyperbolic (3d gravity). The bridge is `SU(2)₃`/`T[SU(2)]`, not the figure-eight's geometry. (`B221/B222 → B226`;
firewalled reading `S040`; rhymes with `B217`.)
