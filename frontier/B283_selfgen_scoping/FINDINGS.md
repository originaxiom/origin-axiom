# B283 — scoping the "arithmetic self-generation" vein: it collapses too

**Status: banked scoping (frontier). FIREWALLED. Nothing to `CLAIMS.md`.** The proper scope of the
arithmetic-self-generation thread (path-a / the metallic WRT tower), done the same way as the CRUX (B281): state the
claims, decompose, **adversarially test genericity**, verdict. Prompted by "scope the arithmetic vein — properly."

## The claims (path-a / the metallic WRT tower)
The metallic monodromies `R^m L^m` (`m=1` = figure-eight) give WRT invariants `Z_k(m) = tr(ρ_k(R^m L^m))` whose
**level-period encodes the arithmetic** — "the object self-generates arithmetic." Path-a's exploratory claims:
period `= rational·(m²+4)`; **absent when `m²+4` is prime**; conjecturally **`= order of the fundamental unit`** of
`ℚ(√(m²+4))`; `Z` outputs `1/λ_m` (the metallic unit).

## Decomposition — where each claim stands
| level | status | basis |
|---|---|---|
| WRT period reflects the trace-field arithmetic (the core "self-generation") | **PROVEN + GENERIC + KNOWN** | see below |
| period = order of the fundamental unit | **SUPERSEDED** | replaced by the exact `P(m)=m(m²+4)/gcd(m²+4,4)` (B204) |
| period absent when `m²+4` prime | **FALSIFIED** | a search-bound artifact (B204): `m=1` (disc 5, prime) has the *smallest* period |
| trace map / Fibonacci self-generation (`κ=2+λ²`) | **KNOWN** | = the Fibonacci-Hamiltonian trace map (banked K007/K010/B107/B148) |
| metallic family generates `ℚ(√(m²+4))` | **ELEMENTARY** | `tr(R^m L^m)=m²+2` ⟹ trace field `ℚ(√(m²+4))`; immediate |

### The core level — PROVEN, GENERIC, KNOWN
- **PROVEN** (B204): `per|Z(a,b)| = lcm(a,b)(4+ab)/gcd(4+ab,4)`, via Landsberg–Schaar + 2D Gauss reciprocity; the
  metallic diagonal is `a=b=m`. (Lemma closed, exact integer arithmetic.)
- **GENERIC** — the law is for **all** once-punctured-torus bundles `R^a L^b`; the metallic family is just the
  diagonal. **Verified independently here** (`selfgen_genericity_probe.py`): the period is governed by `det(φ+I)`
  for metallic (`RL`→5, `RRLL`→4, `RRRLLL`→39), **non-metallic** (`RRL`→6, `RRRL`→21), **and irregular words**
  (`RLRL`→15, `RRLRL`→24). The metallic family carries **no** distinguishing signal.
- **KNOWN** (B204 novelty audit V199, 99-agent): `Z_k = tr(ρ_k(A))` of a torus-bundle mapping torus = a quadratic
  Gauss sum via reciprocity is **exactly Jeffrey 1992**; the proof re-derives her method. (Also: this `Z_k` is the
  invariant of the *closed*-torus mapping torus, a Sol manifold — **not** the cusped figure-eight complement.)

## Verdict — the vein collapses, like E₆
There is **no object-specific novel arithmetic signal** in the self-generation vein. The WRT period is generic
(Jeffrey, all torus bundles), the trace map is the Fibonacci Hamiltonian (known), and the metallic fields are
elementary. The metallic family / figure-eight is the diagonal of a general law, not a distinguished object.

## The meta-conclusion (both veins now scoped)
**Both the E₆-physics vein (B282) and the arithmetic-self-generation vein (B283) collapse to the same place:**
generic structure + known prior art + the **same two NEEDS-SPECIALIST kernels** (the arithmetic-McKay selection; the
τ = E₆ outer-automorphism) + **Reid's unique-arithmetic-knot theorem**. The two veins we had left both reduce to the
one specialist gate already isolated by the R6 audit and the CRUX scope (B281).

**The in-sandbox program is exhausted of new object-specific signal.** Not for lack of computation — *because* the
structure is generic, and the one genuinely object-specific fact (4₁ is the unique arithmetic knot, trace field
ℚ(√−3), ↠ 2T) is small, banked, and its promotion to physics is the single specialist question. The honest next
move is **consolidation + a specialist packet**, not more in-sandbox mining.

`selfgen_genericity_probe.py` · `verdict.py` · `tests/test_b283_selfgen_scoping.py`.
