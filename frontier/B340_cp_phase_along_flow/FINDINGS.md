# B340 / H108 — the CP phase along the flow: `±π/6` is extremal at the amphichiral point

**Status: banked (frontier). Tier-1 (flow interior). New instrument (κ along fillings — none existed). Firewalled;
nothing to `CLAIMS.md`.** The object's CP phase is `κ = tr[a,b] = √3·e^{±iπ/6}` at the cusp (B285). H108 asked whether,
along the `(1,n)` filling flow, the CP phase (`arg κ`) tracks the chirality (`CS`, B338) as chirality turns on. We
instrumented `κ` via SnapPy's holonomy (the `SL(2,ℂ)` rep of `π₁`) at each filling. This is **object-internal** — no
lepton mixing.

## Result
- **Cusp (`n→∞`, amphichiral, `CS=0`):** `κ = √3·e^{iπ/6}` → `arg κ = π/6` (**extremal**), `|κ| = √3`.
- **Filling turns on chirality (`CS ≠ 0`):** `arg κ` **decreases** from `±π/6` (30° → 18.8° at `n=2`); `|κ|` **grows**
  from `√3` (→ 1.82).
- **Scaling:** `(π/6 − arg κ) ≈ 3.8·CS²` — **second order** in the chirality.

## Reading (firewall held)
The CP phase `±π/6` is the value at **zero chirality**; chirality **lowers** it, at `O(CS²)`. Because the deviation is
**even** in `CS` (`arg κ` is a function of `CS²`) while `CS` is **odd** (`CS(1,−n) = −CS(1,n)`, B289), the CP-phase
*magnitude* does not distinguish the CP **sign** at leading order — **the sign lives in the orientation** (external),
consistent with B285 (the CP sign is external; the object supplies both). So chirality and the CP phase **do** co-flow,
but not "both turn on together": the CP phase is **extremal (`±π/6`) at the symmetric amphichiral cusp**, and chirality
deforms it at second order. This makes the object-internal *chirality → CP* relationship concrete; the physical reading
(CP violation vs chirality) is `[LEAP]` and not claimed.

## The fence
SnapPy 3.3.2 holonomy (`SL2C` of `π₁(m004(1,n))`) → `κ = tr(ρ[a,b])`, with recorded values + a live path. No physics
values. Nothing to `CLAIMS.md`.

`cp_phase_along_flow.py` (pyenv/SnapPy) · `tests/test_b340_cp_phase_along_flow.py`. Related: **B285** (`κ = √3 e^{±iπ/6}`,
the CP sign external), **B338** (`CS ~ −1/(2n)`), **B289** (`CS(1,−n)=−CS(1,n)`), **B318** (amphichiral involution =
conjugation), **B339** (the CS sub-leading). Lit: Riley (the parabolic rep); Thurston (Dehn-surgery deformation of the
holonomy).
