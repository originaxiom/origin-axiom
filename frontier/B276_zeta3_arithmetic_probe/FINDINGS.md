# B276 — the ζ₃ ramified-prime probe: Z's arithmetic at the E₆ end is ℚ(√−3) (the 2T field)

**Status: banked observation (frontier). FIREWALLED — quantum topology / arithmetic, NOT physics. Nothing to
`CLAIMS.md`.** The one computable test of wall #2. `b276_zeta3_probe.py` (pyenv; reuses B261's `colored_jones`).

## The question (wall #2, computable form)
Does the figure-eight's quantum invariant `Z[T[4₁]]` "know about" the arithmetic that selects E₆ (B266: trace field
`ℚ(√−3)` → ramified prime 3 → residue `𝔽₃` → `SL(2,𝔽₃)=2T=`McKay-E₆)? This is the **E₆-end companion** to B261,
which found the E₈-end signature at `ζ₅` (→ `ℚ(√5)` → `2I=E₈`, period 5 = det).

## What is computed
Evaluate `J_N(4₁;q)` (B261's verified Habiro colored Jones) at the roots generating the figure-eight's **own** trace
field `ℚ(√−3)` — `ζ₃` and `ζ₆=e^{iπ/3}` (the Riley `t` / regular-ideal-tetrahedron shape, B264/B269). The recursion
**degenerates** (q-holonomic → finite/periodic), exactly as B261 found at `ζ₅`:

| `q` | period | `J_N(4₁)`, first period | ring |
|---|---|---|---|
| `ζ₃` | **3** | `1, 1, 13` | `ℤ[ζ₃] = O_{ℚ(√−3)}` |
| `ζ₆` | **6** | `1, −1, 1, −1, 1, 89` | `ℤ[ζ₃]` |

All values are algebraic integers in the trace-field ring of integers (period = order of the root — the E₆-end
analog of B261's `ζ₅` period-5). The trace field is `ℚ(√−3)` (SnapPy: `4₁` trace field `= x²−2x+4`, root `1+i√3`);
its **unique ramified prime is 3**, with the explicit ramification `(1−ζ₃)(1−ζ₃²) = 3` (so `(3)=(1−ζ₃)²` up to a
unit). The residue field is `𝔽₃`, and `SL(2,𝔽₃)=2T→`McKay-E₆ (B266). The state-integral **saddle** sits at
`z=e^{iπ/3}∈ℚ(√−3)` (B269) — Z's geometric data lives in the same field.

## The two ends, side by side (B258's two-field structure, now from the quantum invariant)
```
E6 end:  q ∈ {ζ₃, ζ₆}  →  trace field ℚ(√−3)  →  ramified prime 3  →  𝔽₃  →  2T  →  E6
E8 end:  q = ζ₅ (B261)  →  ℚ(√5)               →  det = 5            →  𝔽₅  →  2I  →  E8
```

## Honest scope — PARTIAL by design
This is a **coherence**: Z's degeneration locus and saddle field are exactly the field whose ramified prime yields
`2T=`McKay-E₆. It does **not** exhibit `SL(2,𝔽₃)=2T` *acting on* any structure inside Z, so it does **not** settle
the `input-E₆ = output-E₆` conjecture (wall #2) — it **sharpens** it (matches B266's guardrail, B269's residual).
The CRUX (does the 3d-3d *input* type equal the manifold's arithmetic type) remains the stop-gate.

Anchors: B261 (`ζ₅`/E₈ end, the verified `colored_jones`), B266 (arithmetic selects E₆: `ℚ(√−3)`→3→2T), B269
(saddle `z=e^{iπ/3}`), B258 (two-field structure). Lit: Habiro (cyclotomic expansion); Garoufalidis (AJ for `4₁`);
Coste–Gannon (Galois action on WRT).
