# B883 — THE 27, built on the B854 frame via the e₇ 3-grading — every sign inherited, the whole homomorphism verified in exact integers

cc banking seat, 2026-08-04. The queue's top instrument gap, closed. Mathematics scope;
nothing to `CLAIMS.md`; Gate 5 untouched.

## 1. The route (no hand-fixed signs anywhere)

Build **e₇** by exactly the B854 recipe (the Cartan block extends B854's; the ε-cocycle
restricted to the first six nodes is *identical*), then grade by the 7th fundamental coweight:
e₇ = 27̄ ⊕ (e₆⊕ℝ) ⊕ 27. The 27's matrices are read off e₇'s bracket table — the signs come
from e₇'s verified structure constants, not from any convention chosen here.

## 2. Verification ladder (all exact)

| step | result |
|---|---|
| e₇ roots / dim | 63 positive, dim 133 |
| Jacobi | 1500 random basis triples, exact |
| **the e₆ inside e₇ = B854's frame** | **verbatim — 3000 random structure-constant pairs exact** (predicted from the cocycle restriction; now checked) |
| the grading | (79, 27, 27); no bracket leaves its grade |
| **the representation property** | **ρ([x,y]) = [ρx, ρy] on ALL 6084 basis pairs, exact integers** |
| weights | 27 distinct (minuscule), dominant = ω₁ = (1,0,0,0,0,0) |
| **validation vs banked data** | ρ(s₁) at the enhancement point: eigenvalue multiplicities **[1, 10, 16]** — the banked branching 27 = 1 ⊕ 10 ⊕ 16 under so(10)⊕u(1), reproduced |

## 3. The instrument

`rep27.json`: the 78 exact integer 27×27 matrices in the B854 basis order, plus the weight
table and conventions. Everything downstream (the invariant cubic, the Yukawa-support table,
the E-clause capstone, the DVT comparison) now has its base.

`tests/test_b883_the27.py`
