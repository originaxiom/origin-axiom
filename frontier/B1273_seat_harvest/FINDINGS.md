# B1273 — THE SEAT HARVEST: three independent routes separate the same binary, and codex's central twist is reproduced on main's data

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (what is verified here) + a scoped harvest register · **Harvested, NOT merged**

## The convergence on I-6's binary

| seat | route | status here |
|---|---|---|
| **main** (B1263) | π₁(m004) has **48** surjections onto 2T in exactly **2** Aut(2T)-orbits | computed |
| **owner** (Round 11) | separated by **meridian order**: mod (1−ω) → **3**; the (0,0,0) quaternionic character → **6**; triples **(3,6,4)** / **(6,6,4)** | **VERIFIED at B1272**, incl. that the banked holonomy reduced mod (1−ω) is surjective and lands in the order-3 class |
| **codex** (R037) | *"m000 and m004 each have 48 surjections = two Aut(2T) orbits"*; *"exactly one of m004's two 2T quotient classes extends over m000"*; *"the nonextendable class is the unique central H¹ twist of the extendable class"* | **count matches independently; the twist REPRODUCED here** |

**Verified of codex R037 on main's own enumeration:** |Z(2T)| = **2**; H¹(m004; ℤ/2) = ℤ/2 (H₁ = ℤ,
both generators meridians), so the unique nontrivial central twist **negates both**; under it **all 48
surjections move to the other orbit** (48 moved, 0 fixed, **0 invalid**), carrying **(3,6,4) →
(6,6,4)**.

> **So codex's "central H¹ twist" is the SAME pairing the owner's meridian-order separator sees** —
> negating by −I is exactly what turns order 3 into order 6. **Three routes, three seats, one binary.**

**A failed first attempt is kept:** twisting **one** generator yields **0 valid quotients**, because
the character must be a homomorphism and both meridians generate H₁. **The seat printed a conclusion
the data did not support and withdrew it**; the control now asserts `invalid == 0` **before** orbit
counts are read.

## Harvested but NOT verified here — recorded with scope, not adopted

- **codex R037** — the **m000 extension** half needs the covering inclusion π₁(m004) < π₁(m000).
  **m000 is the Gieseking manifold, NON-orientable** (SnapPy 3.3.2: ⟨a,b | aabbAB⟩, vol 1.0149), and
  **m004 is its orientation double cover** (vol 2.0299). **So codex's selector is an ORIENTATION
  selector.** *Whether the geometric class is the extendable one is the open join of the two
  separators* — and it is the natural next computation.
- **codex R039** — each m004 A4-map has two 2T lifts, **exactly one extending over m000**.
- **codex R038** — 27 → 10₂ + 5₋₄ + 5̄₋₆ + 5̄₄ + 1₀ + 1₁₀ under an SU(6)→SU(5) VEV, carrying its own
  **NEGATIVE**: one decomposable VEV is **not D-flat**.
- **codex R040** — all **1260** cusped non-orientable census orientation covers are **CS-zero**.
- **SM-derivation seat** — **h¹(M;27) = 3 = h¹(M;27̄) exactly over ℚ(ω)**, *independently confirming
  B1267's numerically-obtained index 0*; plus a three-generation mechanism from **E₈ ⊃ E₆ × SU(3)**.
  The **branching is verified here** (248 = 78+8+(27,3)+(27̄,3̄); 240−72−6 = **162 = 6×27**) and is
  **standard**; the **object-specific** claim — that the object's *own* order-3 element realises the
  family SU(3) — is **not** verified here, and that seat reports **the Yukawa forces ZERO on the
  triplet**.
- **physics-seat** — 138 commits, Rounds 1–12; **Round 12 already folded main @ `0ecd9557`**.

**Every codex output carries its own scope line** (e.g. R037: *"abstract finite quotient only; no ALE,
physical E6, spin or chirality identification"*), and those fences are **carried across intact** — none
is relaxed by being harvested.

## Controls (MB12, both directions)

- The **centre is computed**, not assumed.
- The twist is checked to produce **valid quotients** (`invalid == 0`) before orbits are counted — the
  check that caught the one-generator error.
- The twist must move **every** surjection (**48/48**); a partial move would mean it is not the
  class-swapping H¹ character.

## Verification

`verification/harvest.py` — standalone; imports B1263's enumeration directly.

- **Feeds on:** B1263, B1272, B1267, and the codex/SM-derivation/physics seats.
- **Registers:** no status change; **I-6's binary now has three concordant separators**.
