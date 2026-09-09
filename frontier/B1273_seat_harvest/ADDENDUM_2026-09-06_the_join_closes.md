# Addendum (2026-09-06) — THE JOIN CLOSES: the extendable class IS the geometric class

**The arc left one open question:** *"is the geometric class the extendable one?"* — the join of the
owner's arithmetic separator (Round 11 / B1272) and codex's topological one (R037). **It closes, and
the mechanism is forced.**

## The computation

SnapPy 3.3.2 confirms **m000's orientation cover is m004** (`identify()` → `m004(0,0)`, `4_1(0,0)`;
cyclic, degree 2; vol 1.0149 → 2.0299). With π₁(m000) = ⟨a,b | aabbAB⟩:

```
pi_1(m000) -> 2T :  72 homomorphisms,  48 SURJECTIVE
    -- exactly codex R037's independently reported count for m000
ord(rho(a))    census over the 48:  {6: 24,  3: 24}
ord(rho(a^2))  census over the 48:  {3: 48}
```

**Why a²:** H₁(m000) = ℤ (from `aabbAB`: 2a+2b−a−b = a+b = 0), so the orientation character
w: π₁(m000) → ℤ/2 is nontrivial on **both** generators. **m000's meridian a is
orientation-REVERSING**, hence not in π₁(m004); **m004's meridian is a².**

## The mechanism — it is forced, not incidental

**2T's element orders are {1,2,3,4,6}, so ord(x²) ∈ {1,2,3} for every x: squaring can NEVER produce
order 6.** Since m004's meridian is a **square** in π₁(m000), any 2T-quotient of m004 that **extends**
over m000 must have **meridian order 3**.

> **Order 6 — the non-geometric class — is unreachable by extension, by parity.**

## The join

| separator | seat | picks |
|---|---|---|
| geometric: holonomy reduced mod (1−ω) | owner, Round 11 (verified B1272) | **meridian order 3** |
| extends over m000 | codex R037 | **meridian order 3** (this addendum) |

> **Two independent selectors — one arithmetic, one topological — pick THE SAME class.**
> And codex's is revealed as an **orientation** selector in a precise sense: extension over the
> non-orientable base forces the meridian to be a square, and squaring kills order 6.

## What it does to I-6

B1263 called the choice *"a genuine binary with no symmetry reason to prefer either."* It is now
**doubly determined**: the geometric class is the extendable class, and the other is its central H¹
twist (reproduced 48/48 in the parent arc). **"The 2T" is canonical.** I-6's **multiplicity objection
is fully paid** — no residue. **The row remains UNEARNED**: it still needs the map to the transverse
ALE Γ, which is a *different* debt from *which* 2T.

**And for the H5 census:** this is the first of its eight measured multiplicities to be **collapsed to
a point by two concordant selectors**, not merely counted. That is a genuine dent in the pattern, not
a rephrasing of it.

## Controls

- The m000 surjection count (**48**) reproduces codex's independently reported value.
- **ord(ρ(a)) takes BOTH values 3 and 6** over the 48 — so the collapse to `{3}` under squaring is a
  real consequence of squaring, not an artifact of a degenerate sample.
- The parity argument is checked against 2T's actual order spectrum **{1,2,3,4,6}**, computed.
