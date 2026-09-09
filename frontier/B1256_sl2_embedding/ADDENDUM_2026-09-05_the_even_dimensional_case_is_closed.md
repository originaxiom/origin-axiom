# Addendum (2026-09-05) — the even-dimensional case is CLOSED, computed not cited: h¹(Sym^odd) = 0

**This arc left exactly one thing open and named it:** *what H¹(M; Sym^odd) contributes under the
spin-lifted holonomy* — because three of the four candidate embeddings carry even-dimensional
summands, and the banked form of Menal-Ferrer–Porti covers only the nontrivial **odd**-dimensional
case. The owner's standing rule is **compute before deferring to a specialist**. It was computable.

## The computation

m004's group is 2-generator / 1-relator, so Fox calculus gives H¹ exactly:

    C⁰ = V --d0--> C¹ = V⊕V --d1--> C² = V
    d0(v) = ((ρ(a)−1)v, (ρ(b)−1)v)     d1(u₁,u₂) = ρ(∂r/∂a)u₁ + ρ(∂r/∂b)u₂
    dim H¹ = dim ker d1 − dim im d0

with the banked holonomy (B598 `peripheral_certificate_exact.py`): `⟨a,b | abABaBAbaB⟩`,
ρ(a) = [[1,1],[0,1]], ρ(b) = [[1,0],[c,1]], c² − c + 1 = 0. **The relator maps to +I**, so ρ is an
honest SL(2,ℂ) rep and Sym^n is defined for *every* n. Ranks taken over 𝔽_p for two independent
primes p ≡ 1 mod 3 (1000003, 1000609), which **agree on every row**.

| n | dim V | rep type | h⁰ | h¹ |
|---|---|---|---|---|
| 0 | 1 | odd-dim (trivial) | 1 | **1** |
| even ≥ 2 | odd | **Sym^even** | 0 | **1** |
| odd | even | **Sym^odd** | 0 | **0** |

Checked n = 0…16. **Menal-Ferrer–Porti is reproduced on this bench for the object specifically**
(h¹ = 1 per nontrivial odd-dimensional power), and the open half is answered:

> **Even-dimensional summands (Sym^odd) contribute EXACTLY ZERO to h¹.**

## What it does to this arc — both directions, stated plainly

**The assumption was correct**, so the arc's arithmetic stands. But the assumption was doing work in
*distinguishing* the candidates, and that work is now redistributed:

- **Under the spin lift**, even-dimensional summands are harmless free riders, so **all four**
  candidates type h¹ = 3 as three chiral and are **equally valid**. The subregular is merely the
  tidiest, **not** the necessary one. *The arc's "only one needs no assumption" framing is retired:
  the assumption is verified, so it privileges nobody.*
- **Under the canonical PSL(2,ℂ) holonomy** — which is what **B1112** actually banks, the SL(2,ℂ)
  lift being *extra* structure and a **choice** — even-dimensional summands are **not
  representations at all**, so only all-odd decompositions are admissible and the **subregular
  E₆(a₁) (27 = 13+9+5) is genuinely unique**.

**So the uniqueness survives, but it is now conditioned on a stated hypothesis** (take the canonical
holonomy, not the lift) rather than on an unverified gap. That is a strictly better epistemic
position, and a weaker headline than the arc first carried.

**I-25 is unchanged and still UNEARNED** — this addendum settles a *sub*-question, not the
embedding choice itself.

## Verification

`verification/h1_symmetric_powers.py` — standalone, two primes, prints the full table.
