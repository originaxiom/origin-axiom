# B8085 — Route A run: the arithmetic obstruction B990 predicted is **ABSENT**

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Owner-directed:** *"do route 1 properly."*
**Verdict: PROVED**, two independent engines. Reproducer `integral_orbits.py`.
**Preregistered** — `PREREGISTRATION.md` sealed before the narrow class number was computed.

## The question B990 posed, and its own prior

B990 proved the orbit-to-point gap **structural**: an orbit invariant is constant on the orbit, so
*no refinement of it can ever pick a point*. Exactly two routes cross it. **Route A: shrink the
group** — count the `G(ℤ)`-orbits inside the object's `G(ℚ)`-orbit, because *"if it is 1, the
integral orbit is a canonical point up to `G(ℤ)` — which is exactly what a VEV direction needs."*

B990 attached an explicit prior: **UNFAVOURABLE** — *"class numbers of this kind are generically
> 1, and the programme's history is a record of homogeneity winning."* **Adopted here unchanged.**

## The result

The rational orbit is classified by the cubic étale algebra `K = ℚ[x]/(x³−12x−5)`. Integral orbits
inside one rational orbit are, in every correspondence of this Kato–Yukie / Bhargava type, counted
by a **class-group-type quantity of `K`**. Rather than assume which, **all candidates were computed**:

| counter | value |
|---|---|
| `h(K)` | **1** *(already banked — not this arc's finding)* |
| **`h⁺(K)` — narrow class number** | **1** *(new)* |
| `\|Cl/Cl²\|` | **1** |
| `\|Cl/Cl³\|` | **1** |

**The mechanism for `h⁺ = 1`:** the unit signature map is **surjective** onto `{±1}³`. The
fundamental units `x²+2x−4` (norm +1) and `3x²+6x+2` (norm −1) have sign vectors `[1,1,0]` and
`[0,1,0]`; with `−1`'s `[1,1,1]` they span `𝔽₂³` — rank **3 of 3**, image **8 of 8**. So
`h⁺ = h·2³/8 = 1`.

**B990's prior did not hold.**

## What this means, at exactly its strength

> **The arithmetic obstruction Route A was expected to meet is absent.** Whichever class-group
> quantity governs the integral orbit count, it is **trivial** — which is why all four were
> computed: the conclusion does not depend on resolving which one applies.

## What it does **not** mean

**It does not say the integral orbit count is 1.** Identifying *which* quantity counts the integral
orbits is Kato–Yukie/Bhargava integral theory, and is **registered as owed, not asserted.** This arc
removes the obstruction B990 predicted; it does not by itself deliver the canonical point.

It also does **not** claim `h = 1` as a finding — that is banked, and was independently
reconfirmed by an external referee this week.

## Controls

- **Two independent engines**: PARI/GP (`bnfinit`, `bnfnarrow`) and an independent route in sympy —
  units verified by **resultant norm ±1**, signs by exact evaluation at the three real roots, the
  `𝔽₂` rank by hand elimination. Both give `h⁺ = 1`.
- **The field is verified before any class datum is read**: `disc = poldisc = 6237 = 3⁴·7·11`, so
  `ℤ[x]/(f)` is the maximal order; irreducible; signature `[3,0]`, totally real.
- No headline is a printed constant (E43).

## SCOPE

**P0, from B990, restated:** the **algebra and its arithmetic** — rational and integral orbits of
pairs of 27s, and the class arithmetic of `K`. **Not a manifold**; nothing about m004, its class,
its sisters, its rows or its child. **Gate 5:** a VEV *direction* is a direction in an algebra; no
value, scale or measured quantity enters.
