# B269 — T[4₁] Rungs 2 (flavor / cusp Weyl) + 3 (partition-function saddle)

**Status: banked observation (frontier). FIREWALLED — 3d-3d / quantum topology, NOT physics. Nothing to
`CLAIMS.md`.** Completes the deferred T[4₁] rungs (B262 audit; B268 Phase 2). `t41_rungs_2_3.py` (pyenv,
sympy + mpmath).

## Rung 2 — the flavor symmetry and the cusp Weyl ℤ/2
The figure-eight has **one** cusp, so it cannot host a cusp-*swap* (the multi-cusp Weyl→nonabelian test needs ≥2
cusps — e.g. the Whitehead link, S033). The single-cusp symmetry is the **meridian Weyl ℤ/2** `(M,L)↦(1/M,1/L)`
(the hyperelliptic involution of the boundary torus). Verified: it is an **exact symmetry of the A-polynomial**
(the Coulomb branch, B260), and `A(1,L) = (L+1)²` (the complete / amphichiral structure, double root `L=−1`).

> **Verdict:** flavor `= U(1)_m ⋊ ℤ/2 = O(2)` — the Cartan plus its Weyl reflection, **not** an enhanced `SU(2)`.
> The single-cusp peripheral data is abelian (Mostow); there are no W-boson monopole operators, so no `SU(2)`
> enhancement. This is the **abelian wall** (S029/S033) holding — an honest **negative**.

The clarifying point: the nonabelian **E₆** of the arc (B264–B267) is the 3d-3d **type** (the character variety),
**not** a flavor enhancement of the abelian `T[4₁]`. Rung 2 cleanly separates the two layers and rules out the
"multiplicity manufactures `SU(2)`" hope for a single cusp.

## Rung 3 — the partition-function saddle reproduces the complex volume, and centers on `e^{iπ/3}`
`T[4₁]` is 2 chirals + 1 gauged `U(1)` (B262) = **2 quantum dilogarithms + 1 integral** = the figure-eight **state
integral**. Its classical (`b→0`) saddle is the gluing/critical-point equation; the geometric solution is the
**regular ideal tetrahedron** shape `z = e^{iπ/3}`, with critical value

> `Vol(4₁) = 2·Im Li₂(e^{iπ/3}) = 2.0298832…` `= ` B250's complex volume (CS `= 0` at the amphichiral point).

**Coherence (the payoff).** The saddle shape `e^{iπ/3}` is the *same* `e^{iπ/3} ∈ ℚ(√−3)` as the Riley parameter
`t` (B264) and the center of the ramified-prime reduction (B266). So the partition function's geometric saddle
lands on exactly the `ℚ(√−3)` point whose reduction mod `(√−3)` produces `2T = `McKay-E₆. At the golden root
`q=ζ₅`, the colored-Jones limit is the antiperiod-5 sequence (B261). This closes the loop
**B250** (complex vol) / **B260** (A-poly saddle) / **B261** (golden-root colored Jones).

## "Does `Z` know about `2T`?" — honest verdict (the wall-#2 probe)
The geometric saddle **does** sit at the `ℚ(√−3)` ramified-prime center `e^{iπ/3}` — a genuine coherence between
the partition function and the arithmetic that selects E₆. But the full statement (the WRT invariant at the
relevant root of unity *reflecting* `SL(2,𝔽₃)=2T`) is the **remaining wall-#2 conjecture** — not closed here. The
honest status: the analytic object (`Z`, its saddle) and the arithmetic object (`2T`, the ramified prime) meet at
`e^{iπ/3}`; whether the *quantum* invariant carries `2T` structure is the open physics-adjacent question.

Anchors: B262/B263 (`T[4₁]` definition), B260 (A-poly / Coulomb branch), B250 (complex volume), B261 (golden-root
colored Jones), B264 (Riley `t=e^{iπ/3}`), B266 (ramified-prime → `2T`), S033/S029 (the abelian wall). Lit:
Dimofte–Gaiotto–Gukov; Andersen–Kashaev (state integral); Hikami; Neumann–Zagier.
