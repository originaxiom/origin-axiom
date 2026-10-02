# B1450 — THE FILLED INDEX ON THE GRID: the Gang–Yonekura formula on the 87 slopes of m004 reproduces every published entry and is defined on all 78 hyperbolic fillings; it does not see arithmeticity; and the triangulations behind the two index arcs are 1-efficient by a theorem whose hypothesis is checked here

cc, 2026-10-02. Lead L225 (registered 2026-09-18) asked three things about the 3D index. Question 2 was answered at
B1431. This arc answers 1 and 3. Preregistration sealed at `2f75736d` on both remotes before the grid was run.
**Verdict: NEGATIVE** for the lead's question 1 (the filled index does not separate the six arithmetic fillings by
any simple feature); the other predictions came out as sealed.

## 1. What the source proves, and a correction to the lead

Celoria–Hodgson–Rubinstein, *The 3D index and Dehn filling* (arXiv:2509.09886), read from the PDF on this bench.
Their Theorem 6.2 proves the Gang–Yonekura formula **for a manifold with at least two cusps**, the filled manifold
still cusped, both triangulations 1-efficient. For a one-cusped manifold the filled manifold is closed, and in
their words "a rigorous definition of the 3D index of closed manifolds does not currently exist"; applying the
formula there is "improper", supported by computation, and stated as their Conjecture 14.1.

**Lead L225 said this programme has "a proven transformation law for the 3D index under exactly that
operation". For this grid — every filling closed — the source proves no such thing.** The lead was written from
the abstract. Everything below is the formula used as a definition, on the footing of the source's own §13.

## 2. The instrument and its control

I_{M(α)} = Σ_{k∈ℤ} (−1)^k [ q^{k/2}·I^{kα} − I^{2α\*+kα} ], i(α, α\*) = 1, with the boundary classes of m004 from
B1428's verified instrument; exact integers, in q^{1/2}; a sum with unboundedly many terms of bounded degree is
returned as undefined (`verification/filled_index.py`).

**Control, before the seal: 16 of 16 published figure-eight entries reproduced to q¹⁰** (`control_run.txt`): 0 on
(1,0); 1 on (0,1), (1,1), (2,1), (3,1); undefined on (4,1); the series of (5,1) … (10,1), (1,2), (1,3), (1,4); and
(40,1) against the published limit n → ∞. One symbol of the printed (6,1) row, "t", is read as q^{1/2}.

## 3. The sealed run (87 slopes, |p| ≤ 8, 1 ≤ q ≤ 8; `grid_index.json`, `grid_read.txt`)

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | defined and 1 + P(q), P ≠ 0, on all 78 hyperbolic slopes | 85% | **YES, 78 of 78** |
| P2 | 1 on (0,1), (±1,1), (±2,1), (±3,1); undefined on (±4,1) | 90% | **YES** |
| P3 | all 43 mirror pairs identical | 95% | **YES, 43 of 43** |
| P4 | (decided on the control) no feature separates the six arithmetic slopes | — | **none of six does** |
| P5a | to q¹⁰ the series does not distinguish all 39 slopes with p > 0 | 70% | **YES: 26 distinct, four classes** |
| P5b | no arithmetic slope shares its series with a slope other than its mirror | 90% | **YES** |

The leading term of I − 1 over the 39 slopes with p > 0:

| leading term | slopes |
|---|---|
| −q^{1/2} | (6,1) — arithmetic |
| −q | (5,1) — arithmetic (the Meyerhoff manifold) |
| −q² | (7,1), **(8,1) — arithmetic** |
| −2q | 31 slopes |
| −3q | (4,3), (7,2), (8,3), (8,5) |

So **(8,1), arithmetic, and (7,1), not, begin alike (1 − q² + …), and that alone refutes separation by the leading
term**; the other five features of the reader (the coefficient, half-integer exponents, the coefficients of q and
of q²) fail the same way. What the table does show is that the three arithmetic pairs are among the four integer
slopes of the grid — which is a statement about B1419's census (the arithmetic fillings are (±5,1), (±6,1), (±8,1)),
not about the index. The coincidence classes to q¹⁰ are (1,4)…(1,8); seven slopes with |p − q| = 1 or 2 and q ≥ 4;
(3,5), (3,7); and (3,8), (5,7), (5,8): the series stabilise as the slope grows, as the source notes for 1/n.

## 4. 1-efficiency without Regina (question 3)

Garoufalidis–Hodgson–Rubinstein–Segerman (arXiv:1303.5278), read from the PDF: Theorem 1.2, a triangulation admits
an index structure if and only if it is 1-efficient; **Theorem 1.5, an ideal triangulation of an oriented atoroidal
manifold with a cusp that admits a semi-angle structure is 1-efficient**; a strict angle structure is one. The
arguments of the shapes of a triangulation with every tetrahedron positively oriented are a strict angle structure.
`verification/one_efficiency.py`: on the twelve census triangulations B1428 and B1431 used (m003, m004, m006, m007,
m009, m015, m016, m017, m019, m022, m023, m026) every tetrahedron is positively oriented, the least imaginary part of
a shape between 0.33 and 0.87. **12 of 12 are 1-efficient by the theorem.** This is a cited theorem with its
hypothesis checked here at high precision, not an interval certificate (the bench's plain Python has no interval
arithmetic for SnapPy) and not an independent proof. It does not cover the randomised retriangulations of those
arcs, which were agreement controls and remain that.

## 5. The fence

- The closed index is not a defined invariant; these are values of a formula (§1).
- Ten coefficients; two slopes can agree to q¹⁰ and differ later, as (1,3) and (1,4) differ only at q¹⁰.
- "Does not separate" is for six stated features. A lookup table separates any finite set of distinct series; no
  feature that is natural and blind to the answer was found, and none was sought beyond the six.
- As the lead's own fence says, the 3d–3d theory is supersymmetric and the object's carrier admits no supercharge:
  this is an invariant on the same manifolds, not a bridge. **0 of 19.**

## 6. Lead

L225 is closed by this arc: question 1 NEGATIVE, question 2 at B1431, question 3 by §4.
