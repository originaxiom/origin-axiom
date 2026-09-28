# xB033 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-28. Sealed, hashed and pushed before any cell runs.**

## P0

**The debt this seat proposed and never ran.** After xB023 Addendum 2 this seat offered two moves and
said the second was the one to run first: *"attack L194 from the closed side instead of the cusped
one — APS's `3η ≡ 2cs + τ (mod 2)` holds for COMPACT manifolds, and G3b handed us an exact compact
tower."* The owner's direction went elsewhere (the buried four, then the thermodynamic side). **It is
picked up here.**

**And working it out changed what it is.** **APS is not needed.** The closed case is settled by the
MODULUS alone, and that is the arc's content.

**Gate 5 absolute. No value. Nothing to `CLAIMS.md`.**

## THE DERIVATION, WRITTEN OUT BEFORE IT IS TESTED, WITH EVERY INPUT GRADED

| input | grade |
|---|---|
| **(i)** for **closed** M, `cs` is well defined **mod 1** | **READ-AT-SOURCE** — CGHN §5A: *"If M is closed the Chern–Simons invariant is well defined modulo 1, but Snap and SnapPea still only compute modulo 1/2."* |
| **(ii)** for **cusped** M, `cs` is well defined **mod ½** | **READ-AT-SOURCE** — Neumann, *Combinatorics of Triangulations…* §1, via this register: compact mod `2π²`, non-compact mod `π²`, and CGHN §5A's `cs = CS/2π²` |
| **(iii)** `cs(M*) = −cs(M)` under orientation reversal | **the record's own working assumption** (xB021 A6/A7, xB023 W0). **Graded here as USED-NOT-READ**: it is standard and the record has relied on it repeatedly, but no arc quotes a source for it. **Named as the arc's weakest link.** |

**Then, with no further input:**

> **CLOSED, amphichiral:** `cs ≡ −cs (mod 1)` ⟹ `2cs ≡ 0 (mod 1)` ⟹ **`cs ∈ {0, ½} (mod 1)`** ⟹
> **`cs ≡ 0 (mod ½)`. THE QUARTER CLASS CANNOT OCCUR.**
>
> **CUSPED, amphichiral:** `cs ≡ −cs (mod ½)` ⟹ `2cs ≡ 0 (mod ½)` ⟹ **`cs ∈ {0, ¼} (mod ½)`** ⟹
> **THE QUARTER CLASS IS PERMITTED** — and xB023 found **75** of them.

**So the `0`-vs-`¼` dichotomy the record has been circling since 2026-09-02 is a statement about the
MODULUS OF `CS`, not about the manifolds.** No `η`, no APS, no Meyerhoff–Ouyang.

## THE CELLS

**Y1 — THE PREDICTION, TESTED: every closed amphichiral hyperbolic 3-manifold has `cs ≡ 0 (mod ½)`.**
*Instrument (pre-seal fact, declared):* `chern_simons()` **raises `ValueError` on a closed census
manifold** (*"The Chern–Simons invariant isn't currently known"*). The working route, found before this
seal: build the **cusped** parent, call `chern_simons()` so the invariant is known, **then** fill.
Verified pre-seal on `m004(6,1) → cs = 0.067931673480` and `m004(1,2) → −0.24660725265`.
*Prediction:* **0 exceptions.**
*KILL, binding:* one closed amphichiral manifold with `cs ≢ 0 (mod ½)` refutes the derivation, and then
**one of (i), (ii) or (iii) is wrong — most likely (iii), the arc's declared weakest link — and THAT is
the headline.**
***NEGATIVE CONTROL, BINDING AND THE CELL IS WORTHLESS WITHOUT IT:*** the **non**-amphichiral closed
manifolds must show a **spread** of `cs` values mod ½. **If closed `cs` reads ≈ 0 for everything, the
test measures nothing** — and the two pre-seal values above already suggest it will not, which is why
they are recorded here rather than after.
*Vacuity control:* the count of closed amphichiral manifolds found must be **≥ 20**, or the cell is
reported as UNDERPOWERED.

**Y2 — THE CUSPED CONTRAST, re-derived rather than recalled.** Re-measure the amphichiral **cusped**
split (xB023 banked `106` zero / `75` quarter / `0` other).
*Prediction:* reproduces, and **the quarter class is non-empty** — exactly what the weaker modulus
permits and the stronger one forbids.

**Y3 — WHAT THIS DOES TO L194, stated at its true width.** *Required honesty, declared now:* **this
does NOT answer L194.** L194 asks whether a **free orientation-reversing deck** forces `cs ≡ 0 (mod ½)`
for **cusped** manifolds. The derivation above shows amphichirality alone gives only `{0, ¼}` there,
**so the input that selects `0` is genuinely extra and L194's question survives intact.** What changes
is its **shape**: the dichotomy is not a property of the manifolds to be explained, it is the modulus;
**and the thing still to be explained is the SELECTION of `0` within `{0, ¼}`.**

## WHAT THIS ARC WILL NOT CLAIM

Not that L194 is closed · not that `η` or APS were needed (they were not, and the arc must say so
rather than dress the derivation in them) · not that (iii) has been verified — **it is used, unread,
and named** · **no crossing of Gate 5** · nothing to `CLAIMS.md`.

## THE SEAT'S PRIOR

Y1 holds with a clean negative control · Y2 reproduces · **Y3 is the honest payload: a relocation, not
an answer** · and **the best outcome is that the record stops treating the `¼` class as a phenomenon
about manifolds when it is a fact about a modulus.**
