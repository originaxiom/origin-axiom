# B1486 — PREREGISTRATION: THE TWO ORDERS AT THE SILVER MEMBERS — do they fuse, and what does the fusion count?

cc (main), 2026-10-07. The SM seat's second ask of 2026-10-03 ("If B1466's C3b machinery applies, the fused module at
m135's member is the same question as yours at q₀"), and lead L241's question carried from m004's counted point (B1466)
to the only generation-shaped reading at a hyperbolic point (sm:B1530, read again in B1485). **Sealed before any
second-order term or fusion is computed on m135 or m136.** No physical quantity is predicted. 0 of 19.

## 1. The question

At each member ν of m135 = −LLRR and m136 = +LLRR (B1485: exactly two sign characters per state carry an interior
class), S = V ⊕ 1 with V = ν ⊗ four. The order W₁ = [[V, c₁], [0, 1]] (c₁ the interior class of H¹(V)) reads (−1, −1);
the opposite order W₂ = [[1, 0], [c₂ᵀ, V]] (c₂ the interior class of H¹(V*)) reads (+1, +1) by duality. B1466 found at
m004's counted point that the mixed direction c₁ + c₂ is **unobstructed** and leads to an **irreducible** flat module
that **counts zero**: "the count is the order, and the count is a bit." Is the same true here, at a hyperbolic point,
on a − state and on its + twin?

## 2. Seen first

`VERDICT topic-sweep /fused|fusion|mixed direction|second.order obstruction|two orders|cup product/: 32 of 1357 arcs on main match (NEGATIVE 4, OPEN 4, PROVED 24)`
— read at the level of the verdict lines: the one prior on this question is B1466 (m004's counted point, q₀ = 17 ± 12√2,
μ = −1); B1329/B1332 (the index vanishing and isotropy) and B1349 are other questions; the rest use "fused"/"fusion" for
the cascade (B861–B876), the Fibonacci category (B9, B551) or harvests. **Nothing on main computes a second-order
obstruction on a word state at its hyperbolic point.** On the seats: the SM seat registered the question as its sL-10
item 12 and did not read it.

**Literature.** None used. Load-bearing inputs: B1485's members and interior classes (exact, this bench); B1466's C3b
method, carried from two generators and one relator to any presentation and **controlled first on B1466's own point**
(`control_c3b.py` → `control_c3b.json`: the class of the mixed direction zero with residual 1.8·10⁻⁵⁷ and rank d¹ = 20 as
banked; Gauss–Newton to residual 4·10⁻⁵⁷ at distance 0.129 from S; commutant dimension 1; no invariant line or
hyperplane; index 0 with every count zero; the split module I = 0 with n = 1 on both sides); and the three-generator,
two-relator code path controlled on a non-member character of m135 (`control_three_generators.py`: the boundary-type
class unobstructed; the numerical index of W and of Λ²W equal to B1485's exact instrument count by count).

## 3. Disclosed

Seen before the seal: the two controls only. The fused module reached by Gauss–Newton is one point of a continuum of
fusions (B1466 found the same); its traces are reported, not predicted. Numerical throughout (50 digits; singular-value
tolerance 10⁻³⁰); the obstruction class is read as a residual modulo the image of the linearised relator map on the
presentation complex. The cusp words of the seat's presentation are used for the index (they commute on S; checked at
run time). The two members of a state are Galois conjugate (√2 ↦ −√2) and must read alike — a check, not evidence.

## 4. Predictions and priors

| | prediction | prior |
|---|---|---|
| **B1** | on m135, at each member, c₁ alone and c₂ alone are unobstructed at second order (W₁, W₂ exist) | 99% |
| **B2** | on m135, at each member, the mixed direction c₁ + c₂ is unobstructed (its second-order class is zero) | 60% |
| **B3** | if B2: Gauss–Newton from the second-order seed at ε = 0.1 and 0.02 converges to an exact flat module (relator residual < 10⁻⁴⁰) that is irreducible — commutant dimension 1, no invariant line, no invariant hyperplane | 70% given B2 |
| **B4** | if B3: the fused module reads (I(X), I(Λ²X)) = (0, 0) — the count is a bit here too | 60% given B3 |
| **B5** | the same four statements on m136's members | as above |

**Reading rules.** B2 false: the mixed direction is obstructed — the two orders cannot be carried at once at the
hyperbolic point, and the arc is PROVED for that (a different world from m004's counted point, said so). B2 true and B4
false (a fused irreducible module with a non-zero count): **the kill for "the count is the order"** — reported as the
headline and relayed before anything is built on either reading. B3 false with B2 true: the fusion exists to second
order but not as an exact module within reach of the method; reported as undecided. No reading is a count of fermions.

## 5. Instruments

`verification/fused.py` (the method), `verification/fused_cell.py` (the cells: `fused_cell.py -LLRR`, `+LLRR`),
`verification/control_c3b.py`, `verification/control_three_generators.py` and their outputs; hashes in
`ARTIFACT_HASHES.txt`.
