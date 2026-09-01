# R35 — ten census-type rows recomputed with SnapPy + PARI (no Sage)

**Targets** (`load_bearing_unrecomputed.tsv` rows marked ASSERTED / IMPORTED / reproducible-unknown): B3 (figure-eight
triangulation counts), B127 (CS(RᵐLᵐ) ≡ 0, m = 1..6), B129 (silver degree-2 covers reach (cusps, rank) = (2,2)),
B147 (volume = integer × Bianchi covolume: 12, 12, 3), B197 C4 (b++RRL/b++RLL: equal volume, CS = ±1/48), B212
(silver square-traces ≡ 0 mod (1+i), no order-3 element), B258 (trace-field degrees 2 / 8 / 8; "silver non-arithmetic"),
B321 (cusp shape 2√3 i, |shape|² = 12), B322 (the 79 hard-coded filling invariants), B326 (H₁ of the 3-fold cyclic
cover = ℤ ⊕ (ℤ/4)²). Script `r35.py`, ~3 min.

| row | claim | R35 | verdict |
|---|---|---|---|
| B3 / B262 | m004: 2 ideal tetrahedra, 2 edge classes, 4 faces, 1 cusp | 2 / 2 / 4 / 1 (SnapPy; #edges = #tets for an ideal triangulation) | MATCH |
| B321 | cusp shape 2√3·i, |shape|² = 12 | −1.1e−15 + 3.4641016151 i, 12.000000000000 | MATCH |
| B127 | CS(b++RᵐLᵐ) = 0 for m = 1..6 | all six ≤ 1.6e−16 | MATCH. Recorded, not claimed by the bank: the b+− sign family (m003-type) has CS = 1/4 for every m = 1..6 |
| B197 C4 | b++RRL, b++RLL: equal volume 2.6667, CS = ±1/48 | 2.6667447834 both; CS +0.020833333333 / −0.020833333333 = ±1/48; isometric (orientation-reversing) | MATCH |
| B147 | vol / Bianchi covolume: RL 12, RRLL 12, RRL/RLL 3 (bank: run under Sage, recorded) | covolumes from \|D\|^{3/2}ζ_K(2)/4π² (PARI `lfun`): O₃ 0.1691569344, O₁ 0.3053218647, O₇ 0.8889149278; ratios 12.000000000, 12.000000000, 3.000000000, 3.000000000 | MATCH |
| B129 | silver b++RRLL (= m136) has degree-2 covers with (cusps, free rank) = (2,2) | 7 covers: three are (2,2), four are (1,1) | MATCH |
| B326 | H₁(3-fold cyclic cover of the figure-eight complement) = ℤ ⊕ ℤ/4 ⊕ ℤ/4 | ℤ/4 + ℤ/4 + ℤ | MATCH |
| B212 | silver holonomy: tr(a²) = +2i, tr(b²) = 2, tr(c²) = −2i, all ≡ 0 mod (1+i); no order-3 element mod (1+i); invariant field ℚ(i), full trace field bigger | polished holonomy (1600 bits): tr(a²) = 2i, tr(b²) = 2, tr(c²) = −2i exactly (Gaussian integers); squares of all words of length ≤ 3 also ≡ 0 mod (1+i); invariant trace field ℚ(i); trace field degree 8, x⁸−4x⁷+12x⁶−20x⁵+24x⁴−20x³+12x²−4x+1 | MATCH |
| B258 | trace-field degrees: 4₁ → 2, silver → 8, bronze → 8, "(non-arithmetic)" | 4₁: 2 (ℚ(√−3)); m136: **trace field degree 8, invariant trace field ℚ(i)**; s464: 8 and 8 (the same octic) | numbers MATCH; **inference wrong for silver** — see below |
| B322 | 79 hard-coded volumes + core-geodesic lengths of m004(p,q), \|p\|,\|q\| ≤ 8 | 41 distinct volumes + 39 core lengths recomputed; 78 of the 79 bank numbers reproduced to 5 decimals; 0.57808 not reproduced by this cell's core-length method (fillings with non-positively-oriented solutions skipped) | MATCH (78/79; the miss is this cell's, not evidently the bank's) |

## The B258 finding

B258 (`two_ended_unification.py` l.13: "SnapPy gives the silver (m=2) and bronze (m=3) trace fields DEGREE 8 --
non-arithmetic"; FINDINGS l.15–21: "only the figure-eight has a quadratic trace field … the figure-eight is the
unique object that is simultaneously metallic and arithmetic"; verdict PROVED) draws arithmeticity from the degree of
the *trace* field. Arithmeticity of a cusped Kleinian group is decided by the **invariant** trace field being imaginary
quadratic with integral traces (Maclachlan–Reid; B147 states the criterion correctly at its l.10). The silver bundle's
invariant trace field is ℚ(i) (B210, B212, R33, this cell), its traces are algebraic integers (tr(a²) = 2i etc.), and
its volume is exactly 12 × covol(PSL(2,ℤ[i])) (B147, reproduced here). **Silver is arithmetic; B258's "non-arithmetic"
and "figure-eight-specific quadratic field" statements are wrong for m = 2**, and the "only the figure-eight" clause
misapplies Reid's theorem (about knot complements) to bundles, which is the very error B125 corrected in B123.
Bronze (s464, invariant field the octic above) is genuinely non-arithmetic, so B258's m = 3 statement stands.
B147 and B258 sit in the bank with contradictory arithmeticity claims for the same manifold and neither points at the
other. Relay item for cc.

**Physics content:** none in any row. "No observable content."
