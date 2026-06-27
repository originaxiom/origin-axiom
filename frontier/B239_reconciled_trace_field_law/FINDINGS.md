# B239 — the reconciled unimodular trace-field law (referee-proof; supersedes the "trace-1" framing)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
From chat2's correctness catch on the paper draft. Run: `python reconciled_law.py` (pyenv).

## The problem with the old framing
The B234/B235 statement "**trace-1**, `disc = 1−4·det`" is fragile: the actual bundle monodromy
`RL = [[2,1],[1,1]]` has **trace 3**, not 1, so a referee who computes it would think the law is wrong. "Trace 1"
was only a *representative* (the homological monodromy `M_1=[[1,1],[1,0]]` has trace 1; the bundle monodromy `RL`
has trace 3). Both give `ℚ(√5)`.

## The robust law (verified)
The object's holonomy/monodromy elements are **unimodular** (`det=±1`); for trace `t`, `disc = t²−4·det`.
1. **`√5` is robust:** `RL` (trace 3, det +1 → disc 5) **and** `M_1` (trace 1, det −1 → disc 5) both give `ℚ(√5)`.
2. **The ONLY imaginary quadratic trace fields a unimodular element can have are `ℚ(i)` and `ℚ(√−3)`:** `disc<0`
   forces `det=+1` and `|t|≤1`, so `disc ∈ {−4 (t=0 → ℚ(i)), −3 (t=±1 → ℚ(√−3))}` — **the floor is `disc=−4`.**
   The object sits at `ℚ(√−3)` (prime 3, the figure-eight geometry); the only **other** available imaginary field
   is `ℚ(i)` (prime 2) = the **Whitehead/Borromean parent** (L44/B225, the `40a1` conductor's 2-part). Two possible
   points; the object lands on one. *(Not numerology — a 2-element menu.)*
3. **E₇'s `ℚ(√2)` (disc 8) needs EVEN trace** (`t=±2`, det −1 = silver `M_2`; also `t=±6`,…) → it lives at
   silver/even-`m`. Odd trace ⟹ `disc ≡ 1 (mod 4)`, so E₇ is **parity-excluded** from the odd-trace object.
4. **`ℚ(√−7)` (disc −7) is below the `−4` floor** ⟹ unreachable by *any* unimodular element — cleaner and
   stronger than the earlier "needs `det=2` / non-unimodular."

## Why it matters
This makes the dual-McKay / field-ladder sections of the paper **referee-proof**: `E₆+E₈` (the real `ℚ(√5)` + the
imaginary `ℚ(√−3)`), `E₇` parity-excluded, and the imaginary ladder closed at `{ℚ(i), ℚ(√−3)}` by the `−4` floor —
all from "unimodular + trace parity," no fragile "trace-1." It **reconciles** the unit-determinant closure
(B234/B235) and the trace-parity framing into one stronger statement, and connects the closure to L44 (the `ℚ(i)`
Whitehead/Borromean parent is the *other* point on the 2-element imaginary menu).

## Supersedes / updates
The "trace-1, disc=1−4det" form in **B234** (trace-1 congruence law), **B235** (the √−7 closure), and the **PC19
paper draft** (`papers/metallic_one_object/ARITHMETIC_SELECTION.md` §3, §5) → use this reconciled form. Anchors:
B210 (dual McKay), B225/L44 (the `ℚ(i)` parent / conductor 2-part), B234/B235.
