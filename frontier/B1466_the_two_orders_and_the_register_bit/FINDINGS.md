# B1466 — THE COUNT IS THE ORDER, AND THE COUNT IS A BIT: at the counted point the two stacking orders count −1 and +1 and are dual up to the inversion; the mixed direction is unobstructed and leads to an irreducible module that counts 0; a source on one line does not choose, and a source on both drives into the count-zero region

**Verdict: PROVED, with one sealed prediction failed and its follow-up computed** (scope: frame F-HE for the vacuum
language and F-CI for the index; object m004's Ballas family at the two counted points q₀ = 17 ± 12√2, μ = −1, level
one, with the ±i and q = 2 controls; reach *single* for the numbers, with C2's theorem general to any point where the two
Ext groups are one-dimensional and A* ≅ ι*A). cc (main), 2026-10-03. The owner's directive of the day ("i aprove, lets do
it when right timing"); lead L241 refinement 2 paid as a sealed arc; GENESIS FK12 (ii)'s "binary or richer" answered at
this point. Sealed at `b3565230` before any point was run.

## 0. Seen first

As sealed (PREREGISTRATION §0): `topic_sweep.py "non-split|extension class|Ext^1|cup product|obstruct|stacking order|the
count is the order|both orders|source term|R76|R77"` — *VERDICT topic-sweep: 115 of 1337 arcs on main match (NEGATIVE 22,
OPEN 6, PROVED 85, RETRACTED 2)*; narrowed to the obstruction vocabulary: B270, B273, B352, B370 (the quadratic cup
product at ρ_prin, zero to third order for the E₆ directions) — C3's method is theirs at the split module; B1453
(`join_own.py`, W₁ = −1), B1455 (L1–L3; ι*W₁, τ*W₁), B1457 (R76's a t² + c t⁴, R77; read), B1459, B1462, B1465, GENESIS GAP3
and FK12, L241's refinement 2. **Literature:** the obstruction theory is textbook; Ballas 1403.3314 as in B1455.

## 1. The two orders (C1, C2)

| point | I(W), 1 on top of A | I(W′), A on top of 1 | I(A ⊕ 1) | W* ≅ ι*W′ | W* ≅ W′ without ι |
|---|---|---|---|---|---|
| q₀ = 17 + 12√2, μ = −1 | **−1** (h¹ 1 / 2, interior 0 / 1; gap 0.34 / 2e−58) | **+1** (h¹ 2 / 1; gap 0.36 / 3e−58) | 0 | yes (dropped 9e−61, kept 0.64; Q invertible) | no (dropped 0.58) |
| q₀′ = 17 − 12√2, μ = −1 | **−1** | **+1** | 0 | yes (8e−60 / 0.21) | no |
| 7 + 4√3, μ = i (control) | 0 | 0 | 0 | yes | no |
| q = 2, μ = −1 (control) | no extension (h¹ = 0) | — | 0 | — | — |

**P1 held, P2 held.** The theorem behind the table: the dual of "1 on top of A" is "A* on top of 1", and A* ≅ ι*A up
to q ↔ 1/q (B1455), so W* ≅ ι*W′; by B1297's L1 and L2, I(W′) = I(ι*W′) = I(W*) = −I(W). **The count is the order, and the
two orders have opposite counts because they are each other's dual seen through the inversion** — not an accident of
the point. L241's refinement 2 (−1, +1, side by side 0) is now sealed and proved.

## 2. Binary or richer: the cup product and the fused module (C3, C3b)

**P3 held, P4 failed.** The second-order obstruction of each order alone vanishes identically (W and W′ exist). The
mixed direction c₁ + c₂ has a second-order cochain of norm 4 390 (q₀) and 11 949 (q₀′) whose **class in H²(Γ; End S) is
zero** (residual 5e−57 and 9e−57 modulo im d¹; rank d¹ = 20, dim H² = 5, gaps clean). The sealed 60% prior for
"obstructed, the register is a bit" was wrong on the geometry: **no obstruction**.

**C3b, the follow-up the seal named.** With ψ solving d¹ψ = −ob, the second-order deformation seeds Gauss–Newton on the
relator (minimal-norm steps on the 50 entries); at ε = 0.1 and ε = 0.02, at both points, it converges to an exact flat
five-dimensional module (relator residual ≤ 2e−52) at distance 0.12 / 0.025 from S. **That module is irreducible**
(commutant dimension 1, gap 0.05 / 3e−60; no invariant line, no dual invariant line — W has (0, 1), W′ (1, 0), S (1, 1)),
its traces leave S's (tr ρ(m) = −2.997, −2.9999 against −3), and **its class index is 0, with h⁰ = h¹ = 0 on both sides** —
acyclic. The two pieces fused into one carry no count.

**So at the counted point:** the flat modules near A ⊕ 1 are richer than a bit — the two stacking lines and a continuum
of irreducible fusions — but **the count is a bit: −1 on one order, +1 on the other, 0 side by side, 0 fused.** "Both
outcomes at once" is a configuration, and it counts nothing; the count exists only where one order is taken. This is
the owner's question (iii) of 2026-10-02 answered at one point by computation: both at once cancels; the choice is where
the count lives.

## 3. The source (C4), and the bar

**P5 held, P6 held.** Along one extension line c₁ ↦ t·c₁ is the same extension for every t ≠ 0 (an isomorphism of
modules), so a source J along one line — the stationary point of a t² + c t⁴ − J t, one real root with the sign of J —
selects a module isomorphic for J and −J: **it does not choose between the orders at all.** A source must have components
on both lines to touch both orders, and C3b says where that leads: into the fused region, where the count is zero. A
count under a source therefore needs the source to lie on one axis exactly, or the potential to drive mixed sources back
to an axis. The latter is a property of the potential's **mixing quartic** — the coefficient d of t₁²t₂² in
V(t₁, t₂) = a(t₁² + t₂²) + c(t₁⁴ + t₂⁴) + d t₁²t₂² + … — which no report derives (R76 gives a and c along one line, read,
not re-derived here). That coefficient is the next computable quantity in the source question, and it belongs to the
harmonic machinery the audit lane holds.

**The bar card (sealed in C4):** population the two orders at the point; rule fixed before computing "the order with the
component of J"; base rate 1/2; p = 1/2 — **UNJUDGED as a selection, FITTED if presented as one**: a source is an input
(THE_BAR; GENESIS GAP3). Computed as predicted.

## 4. What it means

The register at the counted point is a bit in the only sense that matters for the count: two orders, opposite counts,
everything else zero. A relation that fixes the order fixes the count; the object alone offers the orders, the fusion
and the sum, and counts only on the orders. Nothing here is a count on a vacuum (W and W′ are not harmonic, B1455;
the fused module's harmonicity is not examined). **The imported expectation, stated separately:** that a source exists
whose mixing quartic drives it to an axis — not computed. Nothing selects a state. **0 of 19.**

## 5. Errors in this arc

The sealed prior on P4 (60% obstructed) was a guess against the record's own precedent — B270/B273/B352/B370 found every
cup product they computed zero — and should have been 30%. Nothing else; the controls behaved (±i: both orders count 0;
q = 2: no order).
