# Addendum (2026-09-06) — the obstruction is not RANK, it is GENERIC RIGIDITY: a dichotomy at every rank 2–6

**Run immediately after the arc, because the arc named "a non-rigid non-self-dual system" as its
revival path and rank 3 was where rigidity bit.** So: go up in rank.

## The search

Irreducible SL(n,ℂ) representations of π₁(m004) solved directly from the mapping-torus relations
(t A t⁻¹ = φ(A), t B t⁻¹ = φ(B), det = 1), irreducibility enforced by requiring the algebra generated
by A and B to be all of Mₙ:

| n | reps found | non-self-dual | h¹ ≠ 0 | (h¹(V), h¹(V\*)) | INDEX |
|---|---|---|---|---|---|
| 2 | 10 | **0** | 0 | (0,0) | 0 |
| 3 | 10 | 6 | 0 | (0,0) | 0 |
| 4 | 10 | 9 | 0 | (0,0) | 0 |
| 5 | 10 | 9 | 0 | (0,0) | 0 |
| 6 | 10 | **10** | 0 | (0,0) | 0 |

**A control passes on the way:** **n = 2 returns ZERO non-self-dual reps** — exactly right, since every
SL(2) representation is self-dual. The self-duality test is therefore not vacuous and not broken.

**34 non-self-dual representations found across ranks 3–6. Every one of them RIGID (h¹ = 0).**

## The finding: it is not rank, it is genericity

Going up in rank **does not help**, because **rigidity is generic at every rank** and a random solver
only ever lands on generic points. What the search exposes is a **dichotomy**:

> **the non-rigid systems we know** (Sym^n of the geometric holonomy, h¹ = 1 by Menal-Ferrer–Porti,
> reproduced 5/5 in the parent arc) **are SELF-DUAL** → index 0 **by duality**;
> **the non-self-dual systems we find are RIGID** → index 0 **for lack of modes**.

**Either way the index vanishes, but for two different reasons, and neither is a cancellation.**

## What this does to the revival path

The parent arc's hatch said *"a non-rigid non-self-dual system would reopen it"*. That stands — but
this addendum **corrects where to look**: **not at higher rank, at SPECIAL LOCI.** The modes live at
measure-zero points (the geometric rep and its symmetric powers are exactly such points), and **no
random search will ever reach them.** A revival must **construct** a non-self-dual system at a special
locus, not sample for one.

**Honest scope:** this is a **search** result over 50 representations, not a theorem. It does not prove
that no non-rigid non-self-dual system exists — it shows that none occurs generically at ranks 2–6,
and that the two known ways to get index 0 are structurally different.

## Verification

`verification/higher_rank_search.py` — standalone; reprints the table above.
