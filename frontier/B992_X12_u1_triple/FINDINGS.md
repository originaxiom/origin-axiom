# B992 — X12 SETTLED: the second measurement's u(1)³ *is* span(Y, χ, ψ)

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** MATHEMATICS (algebra). Gate 5 untouched.
**Campaign order 10.**

**P0 — the quantifier:** computes over the **algebra e₆** — its Cartan, Levi and centralizer
structure. **Not a manifold.** Nothing here concerns m004, its class, its rows or its child.

---

## The debt B953 left, in its own words

> *"the object's u(1)³ is almost certainly u(1)_Y + u(1)_χ + u(1)_ψ (**INFERRED from the
> bookkeeping, testable, NOT established here**)"*

An arc flagging its own inference. **Now computed.**

## The first attempt, which failed — recorded because the failure is the content

The obvious argument: Y, χ, ψ all centralize su(3)_C ⊕ su(2)_L, so if that centralizer is
3-dimensional they must fill it. Computed on the B961 frame:

    dim Levi                  = 14   (matches B892)
    dim derived = su(3)+su(2) = 11   (matches B892)
    dim z_e6(su(3)+su(2))     = 9    <-- NOT 3

**Nine.** The naive dimension argument does **not** close it: a 3-dimensional span sitting inside a
9-dimensional centralizer proves nothing about equality.

## What the failure showed

The 9-dimensional centralizer carries **six directions that are root vectors, not Cartan elements**
— and **Y, χ and ψ cannot live there.** They are the u(1) generators of a chain of **regular**
subalgebras sharing the Cartan:

> **E₆ ⊃ SO(10) × U(1)_ψ ⊃ SU(5) × U(1)_χ ⊃ SM**

so all three **are Cartan elements by construction**. The Levi likewise **contains the Cartan**
(`a2_a1_levi` returns root vectors *plus* `cartan_basis`), so its centre is exactly the part of the
Cartan annihilated by the Levi's roots.

**Restricting to the Cartan is not a convenience. It is where the objects live.**

## The computation that settles it

    dim z_e6(su(3)+su(2))              = 9
    dim Cartan                          = 6
    dim (centralizer + Cartan)          = 12
    => dim (centralizer ∩ Cartan)       = 9 + 6 − 12 = 3

**Exactly three — and that intersection *is* the Levi's centre, the u(1)³ of B892's second
measurement.**

Now the containments, each for its own reason:

| | why it centralizes su(3)_C ⊕ su(2)_L |
|---|---|
| **Y** | by construction — it is the SM's own u(1) |
| **χ** | su(3)⊕su(2) ⊂ **su(5)**, and χ centralizes su(5) in SU(5)×U(1)_χ ⊂ SO(10) |
| **ψ** | su(3)⊕su(2) ⊂ **so(10)**, and ψ centralizes so(10) in SO(10)×U(1)_ψ ⊂ E₆ |

They are linearly independent — the three distinct abelian factors of the chain.

> **A 3-dimensional subspace of a 3-dimensional space is the whole space.**
> **span(Y, χ, ψ) = z_e₆(su(3)⊕su(2)) ∩ Cartan = the second measurement's u(1)³.**

**No basis choice, no explicit coordinates for Y, χ or ψ** — a dimension count plus three
containments.

---

**Verdict: X12 SETTLED AFFIRMATIVELY. B953's inference is now established.** The rung moves from
HOLE to a computed fact, and one more "inferred, not computed" flag in the corpus is discharged.

**Why the failed first attempt is banked alongside:** the 9-dimensional answer is the *natural* thing
to compute and it is *misleading* — a later seat running the same obvious check would conclude the
question is harder than it is, or worse, would take the 9 as evidence against. **The distinction
between the centralizer and its Cartan part is the whole content, and it is invisible until the
naive count is run and fails.**
