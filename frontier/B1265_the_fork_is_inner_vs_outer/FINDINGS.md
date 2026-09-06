# B1265 — THE REAL FORM IS DERIVED, AND THE FORK IS A RANK OBSTRUCTION: D₂'s signature is −14, and E₆(−26) is OUTER

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact, from the object's own 78; four MB12 controls) · **Price: unchanged at 14**

## The question — `docs/MAIN_GOAL.md` JOIN 3

**B1140** banked the fork as a brute fact: *"the fork's two real forms split the world with **nothing
shared** — E₆(−14) took the charges, E₆(−26) took the geometry (Lorentz, compact colour, the
graviton)."* **No arc crosses it**, and **B1263/B1264** localised **I-10** and **I-11** to it, pricing
it at **2 units**. Is the fork **forced**, or an artifact of a **choice**? **Neither — it is a rank
obstruction.**

## 1. The real form is DERIVED, not chosen

Real forms of a complex simple Lie algebra correspond (**Cartan**) to involutions up to conjugacy,
labelled by the **signature** dim 𝔭 − dim 𝔨. **D₂ — the object's own twist** (B916's 11-flip, decoded
by B1250 as the SO(10) grading) — **is an involution**, and computed here on the adjoint by
conjugation, entry (i,j) ↦ sgn_i·sgn_j·(i,j):

```
dim k = 46  ( = so(10) + u(1) = 45 + 1 )     dim p = 32     46 + 32 = 78
SIGNATURE  =  32 - 46  =  -14
```

> **E₆(−14) is *by definition* the real form of signature −14.**
> **The object's own D₂ selects it uniquely among the five. The charge branch is DERIVED.**

This matters beyond bookkeeping: it is a place where the object supplies **a point, not a family** —
one real form out of five — which is worth noting against the H5 census of B1264 (though H5 permits
it, the real form being a fact *about the object itself*).

## 2. And the fork is a RANK obstruction

D₂ is conjugation by a **torus element** (a sign character on the weights), hence **INNER** — and
inner involutions reach only the **equal-rank** real forms (rank 𝔨 = rank e₆ = 6):

| real form | 𝔨 | dim 𝔨 | signature | rank 𝔨 | |
|---|---|---|---|---|---|
| E₆(−78) compact | e₆ | 78 | −78 | 6 | INNER |
| **E₆(−14)** | **so(10)+u(1)** | **46** | **−14** | **6** | **INNER ← where D₂ lands** |
| E₆(2) | su(6)+su(2) | 38 | 2 | 6 | INNER |
| **E₆(−26)** | **f₄** | 52 | −26 | **4** | **OUTER** |
| E₆(6) split | sp(4) | 36 | 6 | 4 | OUTER |

> **E₆(−26) — the branch that took Lorentz, compact colour and the graviton — has 𝔨 = f₄ of RANK 4.
> No torus element of E₆ can reach it.**

**So B1140's *"nothing shared"* is not a coincidence of two campaigns.** One branch is **inner**, the
other **outer**, and no inner map reaches an outer form. That is *why* the two halves never meet.

## 3. What would cross it — named exactly

Only an **outer** involution, i.e. one using E₆'s **diagram automorphism** — which is precisely **θ**,
the **27 ↔ 27̄** swap the corpus banks as the object's own symmetry.

**So JOIN 3's blocker is no longer "find a bridge". It is: does the object's θ act as an outer
involution here, and with which fixed subalgebra?**

## The fence — where this arc stops

That **θ is E₆'s outer automorphism** is standard (the diagram's ℤ/2 exchanges the two 27s). That the
**object's** θ *is* that automorphism, and can serve as the required Cartan involution, is **not
established here** — and the corpus's own θ facts **cut both ways**: the object is θ-symmetric, but
**θ is trivial on the character variety** (it fixes every SL(2) trace), which is a reason to doubt it
carries the geometric content the E₆(−26) branch needs.

**Nothing here earns I-10 or I-11. The price stays at 14.** What changed is that JOIN 3's blocker is
now a **named rank obstruction with a named unique candidate crossing**, rather than a brute fact.

## Controls (MB12, both directions)

- The eigenspace split is **computed from the object's 78 generators**, not read off B1250 — and
  **every generator is asserted D₂-homogeneous**, which would fail loudly if D₂ did not act
  diagonally on the root spaces.
- dim 𝔨 + dim 𝔭 = 78 is checked.
- **The signature test can come out otherwise:** all five real forms are tabulated with their
  signatures, and **−14 selects exactly one row**.
- The inner/outer split is decided by **rank(𝔨) vs rank(e₆) = 6**, tabulated for all five.

## Verification

`verification/fork_inner_outer.py` — standalone.

- **Feeds on:** B1140 (the fork), B916/B1250 (D₂), B883 (the 27 and 78), B1263/B1264 (the
  localisation and pricing), B1261 (the scoreboard).
- **Registers:** no change; **sharpens I-10 and I-11's shared price**.
