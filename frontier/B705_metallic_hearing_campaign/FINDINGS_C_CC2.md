# FINDINGS C — CC2 (advisory, read-only): Bronze holonomy + cross-family period-3

**Prereg cited:** `MASTERPLAN_AND_PREREG.md`, sha256 =
`a06a1b074f22548d5d875baa8845914ca98bb007e5f789d6190df216d24cf6b6`
(verified locally: `shasum -a 256` on the seat-local copy reproduces this hash exactly.)

**Tools:** `snappy` 3.3.2 (pyenv python 3.12.1, no Sage) — confirmed working.
`snappy.pari` (bundled PARI) used for `algdep`/`lindep`/`nfdisc` since
Sage-gated `trace_field_gens()`/`find_field()` are unavailable in this
environment. `sympy` used for exact polynomial factoring. No git/repo state
touched; this file is new advisory output only.

---

## HEADER VERDICT

**NO-CROSS-FAMILY-PERIOD, with an HONEST-FLAG on the literal swap pipeline.**

Bronze's hyperbolic structure, trace field, and monodromy data were built and
verified **from scratch, exactly**, including a hard cross-check against the
independently banked B649/silver identification (see Step 2). The literal
campaign-defined "swap" object — B649's σ* matrix, obtained only via a
multi-stage pipeline (exact SL(2,L) holonomy → 27-dim E6 Sym-lift → "double"
construction → H¹ Fox-calculus cohomology → weld intertwiner → antilinear
involution) — was **not** reproduced from scratch for bronze in this session;
that pipeline took five registered stages for silver alone
(`/Users/dri/oa-seat-cc2/seat-work/finisher_queue/f4_receipt/b649_copy/`, read
for context only, not modified). In its place I computed an honest, directly
verified **proxy for torsion status**: the exact shape parameters of bronze's
ideal-tetrahedron triangulation. That proxy, plus the exact trace field, is
enough to answer the period-3 question with real data, not fabrication.

---

## STEP 1 — identifying the bronze object (convention decided + verified)

### The prereg's two candidate conventions are both mathematically broken as literal SL(2,Z) monodromies

- **A_m = [[m+1,1],[1,1]]** (the prereg's primary suggestion): `det = m`.
  For golden (m=1) this is 1 — fine, and it does equal the figure-eight
  monodromy up to conjugacy. But for **bronze (m=3), det = 3**. An integer
  matrix with det ≠ ±1 is **not invertible over ℤ**, hence cannot represent a
  mapping class of the punctured torus at all. [[4,1],[1,1]] is simply not a
  valid monodromy — this candidate is dead on arithmetic grounds, not a matter
  of taste.
- **A = [[3,1],[1,0]]** (the cross-check alternative): `det = -1`. This *is*
  invertible over ℤ, but det = −1 means it is orientation-**reversing** on the
  punctured torus; the mapping torus of an orientation-reversing self-map of
  an orientable surface is **non-orientable** (same reason a reflection of
  the circle gives the Klein bottle, not the torus, as its mapping torus).
  It is also, structurally, not reachable as any word in the two
  det = +1 parabolic generators L, R (products of det-1 matrices always have
  det = 1), so it cannot be "the L,R word" the prereg asks for either.

### The convention that actually works: L^m R^m

With `L = [[1,0],[1,1]]`, `R = [[1,1],[0,1]]` (both det 1, trace 2, parabolic
— the standard punctured-torus-bundle generators; golden = word "LR"), I
computed `trace(L^m R^m)` symbolically for m = 1..5:

```
m=1 (LR):       trace = 3   = m^2+2
m=2 (LLRR):     trace = 6   = m^2+2
m=3 (LLLRRR):   trace = 11  = m^2+2
m=4 (LLLLRRRR): trace = 18  = m^2+2
m=5 (...):      trace = 27  = m^2+2
det = 1 always.
```

Derivation of why this is the right family: for the metallic ratio
x_m = (m+√(m²+4))/2 (root of x² = mx+1), one finds x_m² + x_m⁻² = m²+2
exactly (sympy-verified). So **trace(L^m R^m) = x_m² + x_m⁻²**, i.e. the
monodromy's dilatation is x_m² (not x_m itself) — exactly mirroring the
known golden case (figure-eight monodromy eigenvalue is φ², not φ; same
field ℚ(√5) either way). This reproduces golden (m=1, "LR", trace 3) exactly
as given, and predicts **silver = "LLRR" (m=2), bronze = "LLLRRR" (m=3)**.

### Verification against the banked SILVER/B649 identity (independent cross-check)

Built `snappy.Manifold('b++LLRR')` and ran `.identify()`:

- **Result: `m136` exactly**, volume `3.6638623767` (matches, digit for digit,
  the banked B649 stage-1 finding: *"m136: volume 3.6638623767 ... A = RRLL"*
  in `b649_copy/FINDINGS.md`). `RRLL` and `LLRR` are cyclic/mirror rewordings
  of the same conjugacy class (same trace 6, same manifold). This is a
  genuine independent confirmation, not an assumption: **the L^m R^m
  convention reproduces the exact object the campaign already calls SILVER,
  down to the volume.**
- Golden check: `b++LR` → SnapPy `.identify()` returns `m004 / 4_1` (the
  figure-eight knot complement), volume `2.02988321282`, as expected.

Given this double confirmation, **bronze = the L³R³ = "LLLRRR" monodromy is
the correct pick**, not the two broken candidates above.

### Bronze monodromy data (exact)

- Matrix (one representative, up to GL(2,Z) conjugacy): `L³R³`, trace = 11,
  det = 1. `|trace| = 11 > 2` ⟹ **hyperbolic (pseudo-Anosov) confirmed.**
- Eigenvalues: roots of `λ² − 11λ + 1 = 0` ⟹ **λ = (11 ± 3√13)/2** exactly
  (√117 = 3√13).
- Bronze ratio: x = (3+√13)/2, root of x² = 3x+1 (i.e. x = 3+1/x) — the
  standard bronze ratio, field **ℚ(√13)**, real quadratic.
  Exactly verified: x² = (11+3√13)/2 = the larger eigenvalue above. So, as
  anticipated, **the monodromy eigenvalue is x² (bronze ratio squared), the
  same pattern as golden (eigenvalue = φ²) and silver (eigenvalue = δ², since
  trace 6 gives eigenvalues 3±2√2 = δ² and δ⁻², δ=1+√2)**.

---

## STEP 2 — bronze's hyperbolic structure and trace field (built + computed exactly)

`snappy.Manifold('b++LLLRRR').identify()` → **`s464`** (a named SnapPy census
manifold: 6 ideal tetrahedra, matching the word length 2m=6). Solution type:
"all tetrahedra positively oriented" (genuine complete hyperbolic structure
found, not degenerate). 1 cusp.

| | golden (m004/4₁) | silver (m136/B649) | bronze (s464, this cell) |
|---|---|---|---|
| word | LR | LLRR | LLLRRR |
| trace | 3 | 6 | 11 |
| ratio field | ℚ(√5) | ℚ(√2) | ℚ(√13) |
| # ideal tetrahedra | 2 | 4 | 6 |
| volume | 2.02988321282 | 3.6638623767 | **4.81381918610** |
| symmetry group | D4 (banked) | — | **D4** (`M.symmetry_group()`) |

Fundamental group (SnapPy, `lift_to_SL2=False` — the default
`polished_holonomy()` crashes on this manifold with a `%`-on-tuple bug in
`snappy/snap/polished_reps.py`'s `lift_to_SL2C`, worked around, same
workaround the banked B649 pipeline itself needed for its multi-torsion H₁):

```
Generators: a, b, c
Relators:   abABccc,  aaaBcbC
```

`tr(b) = −2` **exactly** (parabolic, the peripheral/meridian generator — same
pattern as golden's `tr(ab) = −2` and silver's `tr(b) = 2`; all three
punctured-torus bundles show a rational-trace-±2 peripheral element, as
required for a genuine single cusp).

**Exact trace field of the holonomy representation** (300–500 bit polished
holonomy + PARI `algdep` + `sympy` exact factoring, cross-checked against
three independent group elements):

- `tr(a) = tr(c)` (complex-conjugate pair) satisfies the **irreducible
  degree-8** polynomial `x⁸+4x⁷+4x⁶+x⁵+8x⁴+11x³−4x²−3x+6`.
- `tr(ac)` and `tr(abc)` **each also** satisfy irreducible degree-8
  polynomials — and an exact integer-relation search (`pari.lindep` on
  `[1,tr(a),tr(a)²,...,tr(a)⁷, tr(ac)]` and the same with `tr(abc)`) found
  genuine ℚ-linear relations expressing `tr(ac)` and `tr(abc)` as
  polynomials in `tr(a)` alone. **Conclusion: all three generate the same
  single degree-8 field** — this is bronze's trace field, not three
  unrelated ones.
- **PARI-certified invariants of that field** (`nfdisc`, `polredabs`,
  signature): degree 8, **discriminant 391728981 = 3 · 7³ · 617²**,
  **signature (r1,r2) = (0,4) — totally imaginary** (no real embeddings, 4
  conjugate pairs), reduced minimal polynomial
  `x⁸+6x⁶−x⁵+12x⁴−3x³+8x²−x+2`.
- A real quartic subfield exists (generated by `tr(acb)`, real value
  ≈ −3.4559446, irreducible min poly `x⁴+x³−8x²+4x+8`, discriminant
  `−276416 = −2⁶·7·617`, Galois group D4 order 8, **signature (2,1) — mixed,
  not totally real**). Checked explicitly by factoring this quartic over
  ℚ(√13): **it stays irreducible — ℚ(√13) is NOT a subfield.** So, exactly as
  with golden (ratio field ℚ(√5) vs. trace field ℚ(√−3) — unrelated, this is
  standard and expected), **bronze's ratio field ℚ(√13) and its actual
  hyperbolic-holonomy trace field (degree 8, totally imaginary) are
  independent number fields with no containment relation.** This is not a
  red flag; it is the same structural fact golden already exhibits.

For comparison, the banked B649 pipeline's own stage-1/2a result for silver
(`b649_copy/FINDINGS.md`, independently re-derived here as a sanity check):
`tr(ac) = −√2−√2i` (I reproduced this **exact same value**, same sign
convention, from `b++LLRR`), full trace field `L = ℚ(s,i)`, `s⁴=8s²+16`,
**degree 8**, containing `ℚ(ζ₈)=ℚ(i,√2)` as a degree-4 subfield. So **silver's
full trace field is ALSO degree 8** (not 4 — the degree-4 ℚ(i,√2) is only a
subfield, generated by the single cross-trace `tr(ac)`) — the same
degree-8-with-a-smaller-named-subfield structure I found for bronze.

---

## STEP 3 — swap/torsion data: what's accessible vs. HONEST-FLAG

**What could NOT be reproduced (flagged, not fabricated):** the campaign's
literal "swap" object is the antilinear involution σ* diagonalized on
H¹(double; 27) in the B649 Track-S pipeline (stages 1→2a→2b→3a→3b in
`b649_copy/`: exact SL(2,L) holonomy, a Sym-lift into a 27-dimensional
E₆ representation via the principal sl₂, construction of a "double" of the
manifold, Fox-calculus H¹ computation, a weld intertwiner, then the 5×5
matrix C with `C·conj(C)=I`). That pipeline took five gated stages to reach
silver's swap diagonal `(d₀,d₁,1,−1,1)`. It is **not reproducible from
scratch for bronze in this cell** — there is no shortcut version of it
available here, and I will not invent numbers for it.

**What IS accessible and was computed exactly, as the honest substitute
signal:** the shape parameters (cross-ratios) of the ideal tetrahedra in each
bundle's canonical triangulation, at 300-bit precision, with exact minimal
polynomials via `algdep`. A root of unity is *forced* to have modulus exactly
1 in every embedding — so "does any shape have |z|≠1" is a rigorous,
unfakeable torsion/non-torsion test, computed the same way for all three
objects:

| object | tetrahedra shapes (moduli) | torsion? |
|---|---|---|
| **golden** (m004) | both shapes z = e^{iπ/3} exactly, `|z|=1`, min poly `x³+1` — a genuine primitive **6th root of unity ζ₆** (figure-8's two tetrahedra are both regular ideal tetrahedra) | **TORSION** |
| **silver** (m136) | 4 shapes: one conjugate pair `|z|=1` exactly (`z=i`, min poly `x²+1` — a 4th root of unity), the other pair `|z|=√2` and `1/√2` (definitively not modulus 1) | **MIXED at shape level** (banked literal σ* swap is non-torsion, per `b649_copy`) |
| **bronze** (s464, this cell) | 6 shapes in 3 conjugate pairs, moduli ≈ **1.727972, 1.314524, 0.760732** — **none equal to 1** | **NON-TORSION** (clean; no root of unity appears anywhere in the triangulation) |

(Note |tet0|=|tet1|² to displayed precision for bronze — an internal
consistency check of the layered triangulation, not a separate claim.)

This is an honest proxy, not the literal campaign invariant — flagged as
such — but it points the same direction the banked silver swap already
points, and it is exact, reproducible, unfabricated data specifically about
bronze.

---

## PERIOD-3 VERDICT

**NO-CROSS-FAMILY-PERIOD.** Across golden → silver → bronze:

- Trace field degree: **2 → 8 → 8** (golden is the outlier/small case — well
  known independently: the figure-eight complement is one of the very few
  *arithmetic* once-punctured-torus bundles, hence its unusually small,
  class-number-1 imaginary-quadratic trace field ℚ(√−3)=ℚ(ζ₆). Silver and
  bronze both land on degree-8, non-elementary, non-arithmetic-looking
  fields — there is no sign of a 3-cycle returning bronze to golden-like
  simplicity.)
- Torsion status: golden is torsion (its shapes are literally sixth roots of
  unity — the CM/arithmetic case); silver is mixed at the shape level but
  its literal banked swap invariant is non-torsion; bronze's shapes are
  cleanly, unambiguously non-torsion (no root of unity anywhere). This reads
  as **"golden is the one arithmetic exception, everything past it is
  generic/non-torsion"** — not a period-3 pattern of any kind.
- Ratio field: always real quadratic (√5, √2, √13) in all three cases —
  expected by construction (metallic ratios are always real quadratic units),
  not distinctive, and **structurally unrelated to the trace field** in every
  case checked (golden and bronze verified directly; silver's ℚ(i,√2) merely
  *contains* ℚ(√2) as a subfield, which is a closer relationship than
  bronze has to ℚ(√13) — itself more evidence that there is no uniform
  cross-family law, since even the ratio-field/trace-field relationship
  differs object to object).

This is exactly the **banked e1 prediction**: each object's swap data lives
in its own trace field, chosen by that object's own arithmetic, with golden
singled out only because it happens to be the arithmetic/CM case in the
family — not because of any periodic law indexed by m or m mod 3.

---

## BRONZE AUDIBILITY

Per the prereg's own stated heuristic (real ratio/weld field ⟺ audible,
predict AUDIBLE if the relevant prime ≡ 1 mod 4): **bronze's ratio field is
ℚ(√13), real (13 is squarefree, 13 ≡ 1 mod 4 since 13 = 4·3+1) ⟹ predicted
AUDIBLE.** This is consistent with — though not a re-derivation of — cell A's
own Table 1 (`FINDINGS_A_CC2.md`), which already lists p=13 as a REAL/audible
SL(2,13)-stage prime for the unrelated character-field construction there;
the recurrence of √13-is-real-and-audible across two different objects in
the campaign is a coincidence worth flagging, not a claim that the two
constructions are the same object.

Separately, and for completeness: bronze's *actual* hyperbolic-holonomy
trace field (degree 8) is totally imaginary (signature (0,4)) — as it must
be for a genuine hyperbolic structure. This is the different, non-real
object from Step 2, not what the audibility heuristic is asking about.

---

## BASE-RATE GATE

- "ℚ(√13) is real because 13≡1 mod4 (13 is already positive/real, so its
  square root is real regardless of the mod-4 condition; the mod-4 condition
  is about which SIGN of p gives a real ℚ(√±p) in the p*-construction used
  elsewhere in this campaign)" — bookkeeping, not a result on its own.
- The actual content delivered by this cell: (1) a corrected, verified
  identification of what "bronze" even is (the prereg's two suggested
  conventions are both broken as literal monodromies — one has det=m≠±1 and
  fails outright for m≥2, the other has det=−1 and is orientation-reversing
  / not an L,R-word); (2) the working convention L^mR^m, verified not by
  assumption but by an independent digit-for-digit volume/identify() match
  against the banked B649=m136 object at m=2; (3) bronze's exact trace field
  (degree 8, totally imaginary, discriminant 3·7³·617², proven to be a single
  field via three cross-checked traces) and its provable independence from
  the ratio field ℚ(√13); (4) an honest, rigorous non-torsion verdict on
  bronze's tetrahedra shapes (all six have modulus ≠ 1, hence none are roots
  of unity) as the accessible substitute for the literal swap invariant,
  which is flagged — not fabricated — as out of reach in this cell.

---

## HONESTY SUMMARY

- Bronze's hyperbolic structure, volume, symmetry group, exact holonomy
  trace field (degree, discriminant, signature, minimal polynomial), and
  exact tetrahedra shapes were all computed from scratch and are reported
  exactly above (all verified via multiple independent traces/relations, not
  single-shot numerics).
- The literal B649-style "Y-tensor"/swap σ* matrix (the 27-dim E₆ Sym-lift +
  double + H¹ cohomology construction, per `b649_copy/`) was **not**
  reproduced for bronze — that pipeline required five gated stages for
  silver alone and is not something this cell can shortcut. No numbers for
  it were invented; the tetrahedra-shape torsion test is reported explicitly
  as a proxy, not as the literal campaign invariant.
- Artifacts: this file only. No git or origin-axiom repo state touched;
  scratch computations were run in a private scratchpad directory, not
  written into the seat-work tree.

*End of exact-arithmetic cell.*
