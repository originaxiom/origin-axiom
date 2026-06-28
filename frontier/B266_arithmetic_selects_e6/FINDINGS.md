# B266 — wall #2: the figure-eight's arithmetic canonically selects E₆ (via the ramified prime)

**Status: banked observation (frontier). FIREWALLED — arithmetic / rep theory, NOT physics. Nothing to
`CLAIMS.md`.** Attacks wall #2 of the five-wall map (B259). `arithmetic_selects_e6.py` (pyenv, pure python + sympy)
+ `mckay_selection_sage.py` (sage-python, the GAP McKay graphs).

## The question
We kept *choosing* E₆ as the 3d-3d "type." Is E₆ actually **selected** by the figure-eight, or imposed by hand?
There were two E₆'s: the **input-E₆** (the 6d (2,0) type we picked) and the **output-McKay-E₆** (E₆ attached to the
trace field `ℚ(√−3)` through McKay). This probe shows the output-E₆ is **not arbitrary** — it is forced by the
unique ramified prime of the trace field, by a chain of theorems, and the figure-eight group itself surjects onto
the relevant McKay group.

## The selection chain (each link a theorem; all verified)
1. **Trace field = `ℚ(√−3)`** — SnapPy: min. poly `x²−2x+4`, disc `−3` (classical, Maclachlan–Reid: the
   figure-eight is `H³/PSL₂(O₃)`, `O₃=ℤ[ω]`). The Riley rep is manifestly over `ℤ[ω]` (`t = 1+ω`, `t²−t+1=0`).
2. **Unique ramified prime = 3**; the residue field at `𝔭=(√−3)` is `𝔽₃`.
3. **Reduction mod `𝔭`: the figure-eight group ↠ `SL(2,𝔽₃)`** — verified: `ω≡1`, `t≡2`, so `a=[[1,1],[0,1]]`,
   `b=[[1,0],[2,1]]` are two parabolics that **generate all of `SL(2,𝔽₃)`** (image order 24).
4. **`SL(2,𝔽₃) = 2T`** (binary tetrahedral, order 24) — classical.
5. **McKay(2T) = affine E₆** — GAP: 7 nodes, marks `{1,1,1,2,2,2,3}`.

> So **E₆ is canonically attached to the figure-eight's arithmetic** — and the figure-eight group itself surjects
> onto `2T = `McKay-E₆.

## Why E₆ and not another type — and the two-ended structure, from one mechanism
- `SL(2,𝔽_q)` is a McKay/ADE (binary-polyhedral) group **only for `q∈{3,5}`** → `2T/E₆` and `2I/E₈`. (`q=2` gives
  `S₃`; `q≥7` gives groups far too large.)
- For `ℚ(√−3)` only `3` ramifies (`5` is inert → `𝔽₂₅`, huge), so the **unique** McKay-reduction is mod 3 → `2T` → **E₆**.
- The **other arithmetic end** `ℚ(√5)` (the spherical / `det=5` end, B247–B261) ramifies at `5` → `SL(2,𝔽₅)=2I` → **E₈**.
  ⟹ the two-ended **E₆/E₈** structure = the two **ramified-prime reductions** of the two end-fields.
- **E₇ is homeless:** `E₇ = `McKay(`2O`, binary octahedral, order 48), and `48` is never an `SL(2,q)` order `q(q²−1)`,
  so `2O` is no prime reduction of such an arithmetic group. This reproduces **B256** ("E₇ geometrically homeless")
  from the *same* mechanism. (GAP confirms `2O ≇ SL(2,q)` and McKay(2O) = affine E₇, marks `{1,1,2,2,2,3,3,4}`.)

## What this does to wall #2 — and the honest guardrail
**Reframed, half-closed.** From *"input-E₆ (chosen) vs output-E₆ (McKay), link unknown/arbitrary"* to *"the
output-E₆ is **canonically selected** by the trace field's ramified prime, and the figure-eight group surjects onto
`2T=`McKay-E₆."*

**Guardrail (verify-don't-trust — this is exactly where over-claiming lurks):** nothing in the 3d-3d framework forces
the 6d **input** type to equal `McKay(reduction mod the ramified prime)`. That identification stays a **conjecture** —
but now a sharp, motivated one (the arithmetic produces *exactly* E₆, with E₈ at the other end and E₇ provably
homeless), not an arbitrary imposition. Wall #2 is not eliminated; the remaining gap is precisely "input type =
arithmetically-selected type?"

Anchors: B247–B261 (the two-ended E₆/E₈ structure), **B256** (E₇ homeless — now explained), B258 (the two fields
co-appear), B259/B260 (the wall map / wall #2), B264/B265 (E₆-irreducible flat connections exist — *what* the
selected type is *about*). Lit: McKay 1980 (binary polyhedral ↔ affine ADE); Maclachlan–Reid (arithmetic of
hyperbolic 3-manifolds, figure-eight = `PSL₂(O₃)`); the classical `SL(2,𝔽₃)≅2T`, `SL(2,𝔽₅)≅2I`.

## Correction (2026-06-28 adversarial audit / B272)
The canonicity argument "`SL(2,𝔽_q)` is binary-polyhedral only for `q∈{3,5}`" is **correct**, but the stated
reason ("`q=2` gives `S₃`; `q≥7` too large") **skipped `q=4`** — the dangerous near-miss, since `SL(2,𝔽₄)≅A₅`
(order 60) is the *icosahedral* group, easily confused with the *binary* icosahedral `2I=SL(2,𝔽₅)`. Correct
exclusions: `q=2→S₃` (center trivial), `q=4→A₅` (center trivial — not in `SU(2)`), `q≥7` (order `q(q²−1)` too large
/ wrong composition factors). The **decisive criterion** is *the existence of a faithful 2-dim quaternionic
(Frobenius–Schur `−1`) irrep* — present only for `q∈{3,5}` (`2T`, `2I`); the center-`ℤ/2` test alone is necessary
but **not** sufficient (it passes for all odd `q`, e.g. `q=7,9`). Conclusion unchanged; justification corrected.

## Novelty (R6, 2026-06-28)
**PARTIALLY-KNOWN.** Reduction `knot group → SL(2, residue field of a trace-field prime)` is standard (Long–Reid
1998; Chinburg–Reid–Stover 2011 for *ramified* primes; Şengün; Riley for `4₁↠SL(2,𝔽₃)`); McKay `2T↔E₆/2I↔E₈`
textbook (Dechant). The **arithmetic-selection overlay** (ramified prime → binary-polyhedral → McKay-ADE as a
*selection rule*, E₇ homeless because `2O≠SL(2,q)`) was not found in prior art — APPEARS-NOVEL, modest,
NEEDS-SPECIALIST. See `frontier/B264_e6_character_variety/NOVELTY.md`, `docs/NOVELTY_AUDIT.md` R6.

## Correction (R6 addendum, 2026-06-28) — the two ends are GROUP-asymmetric
The deep-research audit (R6) surfaced Stuebner 2025 (arXiv:2502.06488): **`pi_1(4_1)` does NOT surject onto `A_5`**,
hence not onto `2I=SL(2,F_5)`. **Verified in-sandbox** (GAP `GQuotients` on the SnapPy presentation,
`verify_surjections.py`): `2T=SL(2,F_3)` → **2** surjections (the E₆ leg is genuine), but `A_5` → **0** and
`2I=SL(2,F_5)` → **0**. So the line-30 framing "the two-ended E₆/E₈ structure = the two ramified-prime reductions of
the two end-fields" is correct **only at the FIELD level**: the E₆ end is a genuine *group* surjection of the
figure-eight (its own trace field `ℚ(√−3)`, ramified prime 3); the E₈ end is `ℚ(√5)`'s ramified prime 5 — the
*spherical companion's* field, **not** a surjection of `pi_1(4_1)`. The ends are arithmetically **asymmetric at the
group level**. (b266_surjection_verdict.py + test; NOVELTY_AUDIT R6 addendum.)
