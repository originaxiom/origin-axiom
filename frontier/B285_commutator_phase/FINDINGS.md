# B285 — the figure-eight's meridian-commutator phase π/6 (verifying chat-2)

**Status: banked. MATH verified; PHYSICS firewalled. Nothing to `CLAIMS.md`.** chat-2 reported a "forced
CP-violating phase of π/6." Verified the math, firewalled the physics, and found the structural reading that I think
is the actual point.

## The math — VERIFIED
For the figure-eight Riley rep `a=[[1,1],[0,1]]`, `b=[[1,0],[−u,1]]` (Riley poly `u(u²+u+1)²`, geometric root
`u=ω`), the **meridian-commutator trace** is
```
        κ = tr[a,b] = u² + 2 = 3/2 ∓ i·√3/2 = √3 · e^{∓iπ/6}.
```
So `|κ| = √3` and **`|arg κ| = π/6` (30°), exact and forced** by the Eisenstein arithmetic `ℚ(√−3)`. chat-2's
headline (`κ = u²+2`, phase π/6) is **correct**, and its self-catch is right: the **sign** flips between the two
conjugate Riley roots `u ↔ u²` (the `e^{±2πi/3}` ambiguity), which is exactly the conjugation that **amphichirality
(τ, B271) swaps**.

**This is the `ℚ(√−3)` atom again (B282), as a geometric phase** — once the trace field is `ℚ(√−3)`, `κ∈ℚ(√−3)` with
`arg=±π/6` follows. A clean new *face* of the Eisenstein atom (alongside 2T, the saddle `e^{iπ/3}`), not a new
independent object-specific signal.

## The physics — FIREWALLED
Calling `arg κ` a "CP-violating phase" identifies a holonomy-commutator trace with a physical fermion-mixing
(Jarlskog-type) phase — an **unestablished bridge** (the holonomy is not the Yukawa sector). And the baryon number is
**not derived**: chat-2 honestly retracted its "within ~1 order" — `sin(π/6)=1/2` into standard baryogenesis gives
`η_B ~ 10⁻⁴…⁻⁵` vs observed `10⁻⁹·²`, off by 4–5 orders; the smallness is standard cosmology, not the object. **Good
discipline on chat-2's part** (retraction + sign-ambiguity flag + self-caught conjugate-root error).

## The structural reading — the real point
chat-2's result, firewalled, **confirms the structural theorem rather than breaching it.** The object forces the CP
phase **magnitude** (π/6) but **not** its **sign**. Magnitude = structure (forced by the arithmetic); sign = the
matter-over-antimatter direction = the **τ-fork** (wall #3), which needs spontaneous breaking — and the object is
**CP-symmetric** (B252), so it delivers `±π/6` symmetrically and cannot pick a side. So even "CP violation" splits
cleanly along the firewall: **the magnitude is forced (symmetry); the sign is external (dynamics).** Baryon asymmetry
here = a forced π/6 phase + a sign from τ-breaking + a magnitude from freeze-out — **one of three pieces forced, two
external** — which is the structural theorem, not a step through it.

## On chat-2's "chase the sign?" offer
The sign is **not object-derivable in-sandbox**: it is the τ-fork / wall #3, gated by spontaneous breaking, and the
object is CP-symmetric (B252) — so "which sign" is precisely what the object does *not* supply. Chasing it would hit
the firewall, not pass it. The honest statement is the structural one above.

`commutator_phase.py` · `verdict.py` · `tests/test_b285_commutator_phase.py`.
