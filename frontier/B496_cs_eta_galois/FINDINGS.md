# B496 — Gate A class 2b: **SEALED** — the CS/η class is mirror-organized end to end: 2-torsion where amphichiral ({0×13, ¼}), ±pairs with sum 0 where chiral, input labels where generic; η is TOOL-BLOCKED (named)

**Status: banked (frontier), Closure Campaign Phase 2, class 2b (prereg
`docs/CLOSURE_CAMPAIGN_2026-07.md` + local `README.md`; outcome enum SEALED / COUNTEREXAMPLE /
TOOL-BLOCKED). Verdict: SEALED — at the computable horizon; the class beyond these strata
remains open (C-guardrail). Firewalled; nothing to `CLAIMS.md`.**

Gate A (S032-A) asks whether any invariant of the single seed is (1) trace-map-invariant,
(2) discretely multivalued, (3) unsymmetrizable — a forced choice. This probe assembles the
**Chern–Simons / complex-volume value class across every banked stratum computable in-sandbox**
(the seed and its sister; the metallic family; the B489 cyclic-cover tower; the full exceptional
set and the B434 forced ±5 child; the B432 chiral-filling sample) and runs the B330 three-condition
test with the mirror involution σ: cs ↦ −cs in the Galois seat (B318/B348: for this object the
conjugation IS the amphichiral involution). **Tier honesty up front** (the one structural
difference from the all-exact B495): CS is analytic; values are SnapPy **certified-numerical**
(double + quad-double `ManifoldHP` + SnapPea's accuracy estimate), upgraded to **exact** only
where a finite candidate set makes the numeric a pin — the **2-torsion elimination** (orientation
reversal negates cs; an amphichiral manifold therefore has 2·cs ≡ 0, so cs ∈ {0, ¼} mod ½ cusped /
{0, ½} mod 1 closed, and a machine-zero pins the member: the alternative sits at distance ¼) —
and where flat fillings admit **exact rational recognition** (residuals < 1e−12). Conventions
(B151): snappy `cs = CS/2π²` mod ½ (cusped) / mod 1 (closed); `complex_volume` mod iπ²; GTZ
ĉ = i(Vol + i·CS) ∈ ℂ/4π²ℤ (SL₂).

## 0. Controls (prereg: fail ⇒ INVALID; all PASS)

- **CS(4₁) = 0 exactly**: cs = −5.6e−17 (HP −3.1e−65); `complex_volume` = 2.0298832128… + 0·i
  (imag ~1e−15), real part = the independent dilogarithm anchor 2·Im Li₂(e^{iπ/3}) (mpmath 30 dps,
  no SnapPy, no stored constant); GTZ form ĉ = i·2.0298832128 with **CS part 0** (B151);
  symmetry group D4, full, amphicheiral (P9/B318). Exact by elimination: amphichiral ⇒
  cs ∈ {0, ¼}; 0 pinned. ✓
- **The sister m003: cs = ¼ exactly** (P9; HP residual 0.0e+00; cv imag = π²/2), same volume as
  the seed — and m003 is **itself amphichiral** (ℤ/2+ℤ/4, full): ¼ is the OTHER 2-torsion point,
  −¼ ≡ ¼ mod ½, mirror-FIXED. ✓
- **The metallic family cs ≡ 0, m = 1..6** (the B127 K-A computation, reused shape: `b++R^mL^m`
  complex-volume imag machine zero, all ≤ 4e−16) against the census-MIX control (m003 = ¼,
  m004 = 0, m006 = −0.114137 ≠ 0): the family zero is discriminating, not universal. ✓

## 1. The cusped strata: total collapse onto the 2-torsion (mirror-fixed) subgroup — tier: exact

Presentation invariance computed (condition 1): `4_1` = `m004` = `b++RL` isometric, one value;
randomize-stable; reversal FIXES 0 and FIXES ¼. Per-stratum certificates: canonical symmetry
group full + amphicheiral, then 2-torsion elimination:

| stratum | objects | certificate | cs (exact) |
|---|---|---|---|
| the seed | 4₁ = m004 = b++RL | D4, amphichiral | **0** |
| the sister | m003 (same volume, P9) | ℤ/2+ℤ/4, amphichiral | **¼** |
| metallic family m=1..6 | b++R^mL^m (K010/B127 M-2) | D4 each, amphichiral | **0** ×6 |
| cyclic covers n=1..5, 8 | b++(RL)^n (B489 tower) | amphichiral each (orders 8..64) | **0** ×6 |

Cover-tower cross-anchors, exact: n = 2 **is** the unique degree-2 cover (SnapPy `covers(2)`,
isometry-verified); H₁ torsion = |det(Aⁿ−I)| = **|L(2n)−2|** = {1, 5, 16, 45, 121, 2205} (sympy
Lucas arithmetic = SnapPy elementary divisors, all six); vol = n·Vol(4₁) (< 1e−8). **Cusped value
multiset (exact): {0 ×13, ¼}** — every member 2-torsion, i.e. σ-FIXED: the cusped class collapses
onto the fixed subgroup of the mirror involution (the CS-class analog of B495's total Galois
collapse into the fixed field).

## 2. The filling interface: the exceptional rationals, the toroidal wall, the forced child

- **Exceptional set** (B434's non-hyperbolic range, flat solutions): cs(4₁(0,1)) = **0** (the Sol
  point, mirror-fixed); cs(4₁(±1,1)) = **±1/84**, cs(4₁(±2,1)) = **±1/40**, cs(4₁(±3,1)) =
  **±1/24** — Seifert-type **rationals in mirror ±pairs** (recognition residuals ≤ 2.5e−16;
  SnapPea accuracy ≥ 13 digits).
- **The toroidal wall 4₁(±4,1)**: degenerate solution; `chern_simons` RAISES — the hyperbolic
  method's honest boundary. Graph-manifold CS/η there: **TOOL-BLOCKED** (Kirk–Klassen/Ouyang
  Seifert-piece calculus; not in SnapPy, sage/magma excluded by prereg).
- **The forced child pair 4₁(±5,1) = Meyerhoff ± mirror** (B434): cs = **±0.07703818026377022…**
  (HP; accuracy 11), isometry-identified with m003(−2,3); pair sum ≡ 0 mod 1 (4.4e−16); reversal
  negates. **Chiral by two independent certificates** (cs at distance 0.077 from {0, ½}; symmetry
  group ℤ/2+ℤ/2 NOT amphicheiral). Anti-recognition: no fraction with denominator ≤ 1000 within
  1e−9 — the value **leaves the rational/2-torsion world**, matching its field label x⁴−x−1,
  disc −283, Galois S₄, no quadratic subfield (sympy exact; B434's "new arithmetic") — an
  **external-input** product, not object arithmetic. Cross-path check: `complex_volume` imag =
  2π²·cs mod π² (two SnapPy algorithms agree).
- **η exposure scan (prereg: say so, don't skip)**: SnapPy 3.3.x exposes **no η/ρ API** (dir()
  scan over `Manifold` + `ManifoldHP`: empty) ⇒ the η sub-item is **TOOL-BLOCKED** (named: APS η
  needs Meyerhoff–Ruberman / Ouyang / Kirk–Klassen machinery or sage — excluded by prereg).

## 3. The mirror-pairing law across the generic sample (B432)

All 31 banked chiral slopes recomputed (banked values match 31/31, worst 4.9e−10) and the law
**cs(p,−q) ≡ −cs(p,q) mod 1 holds 31/31** (worst deviation 6.7e−16); volume mirror-even.
Mechanism: mirror(4₁(p,q)) = mirror(4₁)(p,−q) = **4₁(p,−q)** because the seed is amphichiral —
the seed's own symmetry organizes **every** chiral child into a {+c, −c} orbit; selecting a
member = selecting the slope sign = **external input** (the B432 verdict, now value-level).

## 4. The three-condition test (the seal)

1. **Trace-map-invariant** ✓ — CS carries no presentation gauge (topological invariant;
   computed: three seed descriptions one value, randomize-stable, child cross-identified), and
   every stratum is cut intrinsically (the seed; its unique same-volume sister; canonical cyclic
   covers; the K010 metallic monodromy family; the boundary ±5 of the maximal exceptional set).
2. **Discretely multivalued** ✓ — values live in the discrete lattice quotients ℝ/(½)ℤ and ℝ/ℤ
   (B151's "number mod a lattice"); the forced set is finite:
   {0, ¼} ∪ ±{1/84, 1/40, 1/24} (8 values) plus the child pair ±0.0770381802….
3. **Symmetrizable** ✓ — exhaustive three-bin classification under σ: cs ↦ −cs (geometrically
   realized: B318/B348):
   - **bin F, mirror-FIXED (forced)**: all cusped values — {0 ×13, ¼} are exactly the 2-torsion
     points; **amphichirality kills the sign by forcing the value onto the fixed locus** (the
     B348 pattern in its sharpest form: the value IS its own mirror image);
   - **bin P, mirror ±PAIRS (sum ≡ 0, canonical)**: the exceptional rationals and the Meyerhoff
     pair — the {+β, −β} pattern extended; the object forces the **pair** (B434 forces ±5, both
     signs); the member is the orientation/slope-sign = external input; fixed-field datum |cs|;
   - **bin L, input-LABELED**: the generic B432 sample — slope-labeled free input, and even these
     obey the pairing law (31/31), so σ acts coherently on the entire class.
   Full multiset σ-invariant (cusped mod ½, filled mod 1): computed, True.

**No forced choice exists in this class ⇒ SEALED.** The object hands you the σ-symmetric
multiset — fixed points and ±pairs — never a member.

## 5. Honest scope (C-guardrail) — what remains out of reach

- **η / APS ρ (any stratum)**: no SnapPy API (scan negative, §2) — **TOOL-BLOCKED (named)**.
- **Exact number-field CS of the chiral fillings** (extended-Ptolemy/GTZ exact tier for
  ĉ ∈ ℂ/4π²ℤ): needs the Ptolemy database (network) or magma/sage — **TOOL-BLOCKED**. The exact
  tier here covers only what 2-torsion elimination and rational recognition reach.
- **Toroidal ±4 graph-manifold CS/η**: **TOOL-BLOCKED** (Seifert-piece calculus).
- **Verified-interval CS** (`verified_modulo_2_torsion=True`): needs SageMath — named; the
  numeric tier is certified-numerical (HP + SnapPea accuracy), honestly labeled throughout.
- The **universal** all-invariants statement stays **open**: this is "sealed at the computable
  horizon; the class beyond these strata remains open," not victory-by-exhaustion.

## The fence

`probe.py` (runnable, ~3 s, tiers labeled) → `b496_cs_eta.json`;
lock `tests/test_b496_cs_eta_galois.py` (exact backbone without SnapPy: 2-torsion sets, Lucas
torsion law, child quartic, dilogarithm anchor, JSON bins/verdict integrity; SnapPy behind
importorskip: controls, child pair, one exceptional recognition, one mirror-law pair). Reuses
banked method code-shapes: B127 (metallic complex-volume zero), B432 (closed-CS initialization on
the cusp + the 31-slope sample), B434 (quartic lock), B489 (Lucas/cover table), test_snapdata (the
dilogarithm anchor). Cross-refs: **B330** (the mechanism), **B348** ({+β,−β} + conjugation =
amphichiral involution), **B318** (the geometric firewall), **B151** (ĉ ∈ ℂ/4π²ℤ; the lattice),
**B127** (K-A: metallic CS ≡ 0), **B489** (the cover tower), **B432/B434/B443** (filling
chirality, the forced ±5 child, its −283 class), **B495** (the sibling class-2a seal),
`docs/OPEN_PROBLEMS.md` Gate A. Lit: Neumann (extended Bloch, complex volume), Zickert (the
cusped CS algorithm), Meyerhoff–Hodgson–Neumann (closed CS via Dehn surgery), Garoufalidis–
Thurston–Zickert arXiv:1111.2828 (ĉ mod 4π²), Kirk–Klassen / Ouyang (Seifert η/CS — the named
blocked tool), Atiyah–Patodi–Singer (η).

**Nothing to `CLAIMS.md`; firewall untouched.**
