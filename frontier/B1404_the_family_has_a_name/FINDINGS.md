# B1404 — THE FAMILY HAS A NAME: MINSKY'S CLASSIFICATION, VERIFIED ON
# RECEIPT (2026-09-14)

## 0. WHAT ARRIVED, AND WHAT SURVIVED

A relay: that the object's family is **Minsky's punctured-torus groups**,
that the family's defining condition is `κ = −2`, that the family is
**classified by its end invariants**, and that m004's end invariants are
`φ` and `φ′` — so *"the golden ratio determines the object"* is a published
theorem applied to its own object rather than a resonance.

Verified on receipt, 40/40 exact checks (`b1404_the_family.py`) plus a
corpus audit (`b1404_absence_audit.py`). **The mathematics survives. Three
statements around it do not, and the corrections are the arc's real
content.**

- **STANDS** — the citation. Minsky, *The classification of punctured-torus
  groups*, Annals of Math. (2) **149** (1999) no. 2, 559–626
  (arXiv math/9807001). Its abstract defines the family as *"free
  two-generator Kleinian groups with parabolic commutator"* and proves
  Thurston's ending lamination conjecture for them. Confirmed against the
  arXiv record, not taken on relay.
- **STANDS** — `φ` and `φ′` are the fixed points of `RL` on the circle at
  infinity, **exactly**, with `φ` attracting and `φ′` repelling, and `φ′`
  is `φ`'s Galois conjugate. Proved, not measured (§2).
- **STANDS, AND IS THE BEST PART** — `κ = −2` is the family's **definition**,
  and E72's fibre triple is on the Markov surface **exactly** (§4).
- **EXTENDED IN READING, NOT IN ARITHMETIC** — the relay speaks about
  `m = 1`; the statement holds for the whole metallic ladder. But **every
  number in that extension is already banked** (K002, B148/V137,
  T-GIES-FAM); what is new is only that `λ_m` **is an end invariant** (§5).
- **CORRECTED** — the classified object is the **fibre group**, not m004.
  m004's own knot group is *not* in the family, and this is decidable rather
  than a matter of emphasis: its commutator is not parabolic (§3).
- **CORRECTED** — `1.618033988750` and `−0.618033988750` are **coordinates in
  a marking**, not invariants. A change of marking moves them while fixing
  the manifold. What is marking-free is their `SL(2,ℤ)` orbit — equivalently
  the conjugacy class of `RL`, equivalently the dilatation `φ²` (§3).
- **CORRECTED** — the absence audit. Minsky is absent; so are Marden, Maskit,
  Bromberg, ending laminations and Epstein–Penner. But Guéritaud, Futer,
  Floyd–Hatcher, Lackenby and Jørgensen are all **in** the record, several in
  `THEOREM_REGISTRY.md` itself, and `κ = −2` has been banked for hundreds of
  arcs (§5).

## 1. THE ONE-SENTENCE RESULT

**The corpus has been computing inside a named, classified family for its
whole life, and had every ingredient of the classification except the
classification.** It banked the defining equation (`κ = −2`, the Markov
surface), the canonical triangulation (Floyd–Hatcher, via Lackenby and
Guéritaud), and the invariant itself (`φ`) — and never had the theorem that
says those three are one statement. Minsky supplies it. The programme's
oldest sentence, *the golden ratio determines the object*, is true of the
**fibre group**, as a corollary of a 1999 classification, once the object
and the marking are named.

## 2. THE END INVARIANTS, EXACTLY

`RL = [[2,1],[1,1]]`, trace 3, hyperbolic. As a Möbius map its fixed-point
equation is `z² − z − 1 = 0` — proved by expansion, not quoted — so the
fixed points are exactly

    φ  = (1+√5)/2 =  1.61803398874989…      (ATTRACTING, M′ = 1/φ⁴)
    φ′ = (1−√5)/2 = −0.61803398874989…      (REPELLING,  M′ = φ⁴)

with `φ′` the image of `φ` under `√5 ↦ −√5` and `φ′ = −1/φ`. Attracting vs
repelling is settled by the derivative `1/(cz+d)²`, which is the only way it
is *settled* rather than named. The monodromy's dilatation is `φ² = (3+√5)/2`.

For the doubly degenerate fibre group these two points **are** the ending
laminations — the stable and unstable foliations of the pseudo-Anosov
monodromy, read as slopes on `∂ℍ² = ℝ̂`. That identification is the standard
one and is **cited, not re-derived here**; what is re-derived here is that
the two numbers are what the relay says they are.

## 3. TWO CORRECTIONS THAT CHANGE WHAT MAY BE SAID

### (a) The classified object is the FIBRE group

Minsky's family is free, two-generator, discrete, **parabolic commutator**.
m004's knot group has none of the last property:

    κ_meridian = tr[a,b] = 3/2 + (√3/2)i,   κ_meridian − 2 = a primitive
    cube root of unity,   |κ_meridian + 2| = 3.6055…  ≠ 0

computed from SnapPy's holonomy at 60 digits (§6 on why that precision is
load-bearing). A parabolic commutator needs `κ = −2`; m004's meridian pair
misses it by a wide margin. **So Minsky classifies the once-punctured-torus
fibre group of m004 — the infinite cyclic cover — and m004 is recovered from
it by the ℤ-action, not by the classification alone.** The relay's sentence
*"m004's end invariants are φ and φ′"* is true of the cover and false of
m004 as stated.

### (b) The two NUMBERS are a marking; the ORBIT is the invariant

Conjugating the monodromy by `P ∈ SL(2,ℤ)` re-marks the fibre and leaves the
mapping torus alone. The trace is unchanged — same mapping class, same
manifold — and the fixed-point pair moves:

| marking `P` | the pair |
|---|---|
| `[[1,1],[0,1]]` | `(φ², 2−φ)` = `(+2.618034, +0.381966)` |
| `[[1,0],[1,1]]` | `(φ−1, −φ)` = `(+0.618034, −1.618034)` |
| `[[2,1],[1,1]]` | `(φ, φ′)` = `(+1.618034, −0.618034)` |
| `[[0,−1],[1,0]]` | `(φ′, φ)` — the pair swaps |

So *"the end invariant is exactly 1.618033988750"* prices a choice that was
never billed — **E76's shape, on a quantity the programme cares about more
than any other.** What is invariant is the `SL(2,ℤ)`-orbit of the ordered
pair, and the orbit has an exact certificate: every member is a **noble**
number, its continued fraction periodic part exactly `[1]`.

    CF(φ) = [[1]]        CF(φ²) = [2,[1]]        CF(φ−1) = [0,[1]]

The marking-free readings of the same fact, in ascending strength:
`the end invariant is noble` → `the pair is the fixed-point pair of RL up to
SL(2,ℤ)` → `the monodromy is conjugate to RL` → `the dilatation is φ²`.
**Each is a statement about the object; `1.618033988750` is a statement about
a basis.** The programme's sentence survives at the orbit level and does not
survive at the digit level.

## 4. THE BEST PART: THE RECORD ALREADY HELD THE DEFINITION

E72 (banked 2026-09-12, B1344) diagnosed `κ` as **one symbol, two
quantities**: the meridian `κ − 2 = ω²` of the knot group, and the fibre
`κ = −2` of the punctured-torus pair — both correct, neither wrong, the
error being to read a statement about one as a statement about the other.
B1344 derived the fibre point independently as the monodromy fixed point
`(2+ω, 1−ω, 1−ω)`, minimal polynomial `x² − 3x + 3`.

**Minsky turns the diagnosis into an explanation.** `κ = −2` is not a
computed property of that pair — it is **the condition that puts the pair in
the family at all**. Verified exactly here, in the corpus's own banked
numbers:

- the Fricke identity `tr[A,B] = x²+y²+z²−xyz−2` — **proved symbolically in
  SL(2)** rather than recalled (E58);
- `κ(2+ω, 1−ω, 1−ω) = −2` exactly, hence `|κ − 2| = 4`;
- equivalently `x²+y²+z² = xyz` — **the banked triple is on the MARKOV
  surface**, which is precisely the `κ = −2` locus;
- `x + x̄ = 3 = tr(RL)`;
- the triple is a fixed point of a **non-trivial** length-2 Vieta composite
  (42 of 324 composites fix it; trivial ones filtered by testing against a
  generic point of the surface, and the fixers verified to move that generic
  point).

The corpus has 930 lines mentioning Markov across 269 files and **442 lines
carrying `κ = −2` across 187** — counted at `d08d1f98`, before this arc wrote
about any of it, and across every spelling (ASCII and Greek `κ`, ASCII hyphen
and Unicode minus). **It has been working on the family's defining
locus, by its defining equation, at scale, without the family's name.** That
is the finding: not a missing computation, a missing *identification*.

## 5. THE LADDER — AND THE ARC'S OWN LESSON, APPLIED TO ITSELF

The relay speaks about `m = 1`. The general form:

    R^m L^m = [[1+m², m], [m, 1]] = X_m²   with   X_m = [[m,1],[1,0]], det −1

so `RᵐLᵐ` and `X_m` have the **same** fixed points, and the fixed-point
equation of the m-th bundle's monodromy is

    z² − m z − 1 = 0     — discriminant  m² + 4

| m | attracting fixed point `μ_m` | CF | `m²+4` |
|---|---|---|---|
| 1 | `(1+√5)/2` | `[[1]]` | 5 |
| 2 | `1+√2` | `[[2]]` | 8 |
| 3 | `(3+√13)/2` | `[[3]]` | 13 |
| 4 | `2+√5` | `[[4]]` | 20 |
| 5 | `(5+√29)/2` | `[[5]]` | 29 |
| 6 | `3+√10` | `[[6]]` | 40 |
| 7 | `(7+√53)/2` | `[[7]]` | 53 |
| 8 | `4+√17` | `[[8]]` | 68 |

Verified exactly for `m = 1..8`: the attracting fixed point is the m-th
**metallic mean** `λ_m`, the repelling one its Galois conjugate `−1/λ_m`
(Vieta: sum `m`, product `−1`), the dilatation `λ_m²`, the continued
fraction purely periodic `[m]`. `z² − mz − 1` is irreducible over ℚ for
every `m ≥ 1`, since `m²+4 = k²` forces `(k−m)(k+m) = 4`, i.e. `m = 0`.

**AND NONE OF THAT ARITHMETIC IS NEW TO THE CORPUS.** Found while checking
this arc's own line counts, in `papers/metallic_one_object/SYNTHESIS.md`:

> `λ_m` is the fundamental unit (norm −1) of `ℚ(√(m²+4))`, with the period-1
> continued fraction `λ_m = [m;m,m,…]` **[banked K002]** … the metallic
> monodromy **is** the `SL(2,ℤ)` MCG action on the Fricke cubic; the Dehn
> twists preserve `κ`; `tr φ_m = m²+2`; the larger eigenvalue is `λ_m²`; the
> **`κ = −2` slice is the Markov surface** **[banked B148/V137]**

Every element of the table above — the mean, the discriminant `m²+4`, the
period-1 continued fraction, the dilatation `λ_m²`, `X_m = [[m,1],[1,0]]`,
and the identification of `κ = −2` with the Markov surface — **is banked,
and has been for hundreds of arcs.** This section adds exactly one thing:
that `λ_m` **is the end invariant** of the m-th bundle's fibre group in
Minsky's sense, so that the corpus's `m²+4` is the **discriminant of the
classification's coordinate**.

**That is this arc's own thesis happening to this arc.** The first draft of
this section was written as an *extension*, and it is not one — it is the
same identification failure the arc is about, committed while diagnosing it,
and caught only because a line count sent me into a file I had no other
reason to open. **Recorded as a fence, not a footnote:** §5's arithmetic is
citation, `T-ENDLADDER` is registered as already-banked, and the new content
of this arc is the **reading**, in §§2–4 and 6, not the numbers here.

## 6. THE ABSENCE AUDIT, CORRECTED — AND WHY IT NEEDED A HOMONYM FILTER

The relay reported broad absence. Run properly (`b1404_absence_audit.py`,
excluding this arc from its own grep), the picture is narrower and more
interesting:

| term | raw grep | after homonym filter | verdict |
|---|---|---|---|
| Minsky | 0 | 0 | **ABSENT** |
| Epstein | 15 | **0** | **ABSENT, MASKED** — every hit is the Epstein *zeta function* |
| Penner | 1 | 1 | present only as Garoufalidis–Kashaev–Lawrence–Penner, not the convex hull |
| Marden / Maskit / Bromberg | 0 | 0 | **ABSENT** |
| ending lamination | 0 | 0 | **ABSENT** |
| end invariant | 5 | **0** | **ABSENT, MASKED** — every hit is *Eisenstein-end* or *E₈-end* |
| Guéritaud | 18 | 18 | **PRESENT** — incl. `THEOREM_REGISTRY.md` |
| Futer | 58 | 58 | **PRESENT**, 32 files |
| Floyd / Hatcher | 25 | 25 | **PRESENT** — incl. `THEOREM_REGISTRY.md` (T-MIRROR) |
| Lackenby | 5 | 5 | **PRESENT** — `NOVELTY_AUDIT.md` cites math/0112221 by number |
| Jørgensen | 93 | 93 | **PRESENT**, 35 files |
| Farey | 47 | 47 | **PRESENT**, 19 files |
| κ = −2 | 442 | 442 | **PRESENT**, 187 files |

So *"not one of them is in the record"* is **wrong for Lackenby,
Floyd–Hatcher, Guéritaud and Jørgensen**, and the claim that Guéritaud–Futer
was *"cited once and set aside"* is wrong by a factor of thirty. The genuine
hole is **Minsky and his half of the literature** — the classification, the
ending laminations, and the Kleinian-group side (Marden, Maskit, Bromberg) —
plus **Epstein–Penner as a name**: the corpus computes with canonical
triangulations routinely and has never cited the theorem that makes them
canonical. Lackenby's result is exactly that bridge (the Floyd–Hatcher
monodromy triangulation **is** the Epstein–Penner decomposition,
Comment. Math. Helv. **78** (2003) 363–384), and the corpus holds one end of
it without the other.

**And the method point, which outlives this arc:** two of the six genuine
absences were **invisible to a bare grep** because this corpus contains an
unrelated Epstein and an unrelated hyphenated *-end*. An absence audit that
counts spellings will report presence where there is none — and, run the
other way, will report absence for a citation carried under a different name.
**An audit by name needs a homonym filter in both directions, and the filter
is only trustworthy if every raw line was read.** All 15 Epstein lines and
all 5 *end invariant* lines were read here.

## 7. THE COST LINE — E75 TWICE MORE, AND A THIRD MECHANISM

The identification of `κ_meridian` against the banked `ω²` **failed on the
first run at a 5.0e−17 residual**, and the measurement was not at fault. The
comparison built its candidate as `complex(sp.N(2 + ω², 50))` — fifty digits
computed, then truncated to sixteen by `complex()` — and compared it at
`1e-25`. One day after E75 was widened from *keys* to *any float standing
where exactness is required, the input included*, the same class reappeared
in the same session, in the **control** rather than the measurement.

**And a second, in the same script, on the ladder of §5: every EVEN `m`
failed a correct statement.** The Galois-conjugacy test substituted
`√(m²+4) ↦ −√(m²+4)` into the root — but `nsimplify` had already turned
`(2+√8)/2` into `1+√2`, so for even `m` the substitution matched nothing and
silently did nothing. **This is E75's disease in symbolic clothing:
identifying an object by its printed representation instead of by a
property.** The fix is E75's own rule applied to symbols — test the
*relation*, not the form: Vieta (`μ + μ̄ = m`, `μ·μ̄ = −1`) plus the minimal
polynomial, both form-independent. Recorded as a **third mechanism** of the
class: rounding keys, float inputs, and now `subs` on a non-canonical
symbolic form.

Two fixes for the first, and the second is the durable one:

1. candidates are now built in mpmath at the ambient precision, and SnapPy's
   high-precision output is carried across by its own decimal **string**
   (`str(x.real())`, spaces stripped) rather than through `complex()` —
   66 digits arrive instead of 16;
2. **the check was replaced by a label-free one.** `κ − 2 = ω²` tests which
   primitive cube root someone chose to call `ω`; `(κ−2)³ = 1` and
   `(κ−2)² + (κ−2) + 1 = 0` test the fact. The label-free version passes at
   `1e-60` and cannot be broken by a convention. **When an exact
   identification needs a named constant, ask whether the name is part of
   the claim** — here it was not, and the check that tested the name is the
   one that broke.

**Two more in the audit script, and one of them is the arc's thesis again.**

- **The audit read its own report.** Run against the working tree after the
  arc's prose had reached eight doc surfaces, `GENUINELY ABSENT` came back
  **empty** — Minsky, Marden, Maskit and Bromberg were all "present", in the
  files saying they were absent. Fixed by pinning every grep to `d08d1f98`,
  the commit the arc started from. **A measurement of a corpus that includes
  the measurement is not a measurement**, and the same shape had already been
  caught once in this arc (the first version grepped its own directory).
- **The same regex returned two different counts, by a factor of two,
  depending on the process locale.** `κ = −2` was counted with the bracket
  expression `[-−]2`. Outside a UTF-8 locale a bracket expression is
  **byte-oriented**, and the Unicode minus is three bytes in a one-byte slot,
  so the Greek-kappa branch cannot match at all. Measured: `LC_ALL=C` →
  **215**, `LC_ALL=C.UTF-8` → **442**, same pattern, same corpus, same git;
  the four alternatives written out in full give **442 under every locale**.
  **And it is invisible from where this corpus works** — Python sets
  `LC_CTYPE=C.UTF-8` for its children (PEP 538), so the script was right and
  the identical command in a plain shell was wrong, which is the only reason
  the discrepancy surfaced. Representation a third time in one arc, and the
  worst-behaved of the three: silent, plausible, and off by half.

**And the near-miss that is worth more than either.** §5 was drafted as an
*extension* of the relay. Chasing the line count above put me in
`papers/metallic_one_object/SYNTHESIS.md`, which banks every number in it —
`λ_m = [m;m,m,…]`, `ℚ(√(m²+4))`, `tr φ_m = m²+2`, the dilatation `λ_m²`, and
`κ = −2` as the Markov surface — from **K002** and **B148/V137**. So the arc
whose finding is *"the corpus had the ingredients and not the name"* was
about to bank the corpus's own ingredients as new. Caught by an accident of
bookkeeping, not by a control. **The general rule this earns:** before
writing *extends* or *new*, grep the corpus for the **statement**, not for
the citation — the ingredients hide under the programme's own vocabulary,
which is precisely what makes them invisible.

## 8. FENCES

- Minsky's theorem is **cited**, not re-proved: this arc verifies the
  citation, the definition, and every number the relay attached to it.
- The identification *ending laminations of a doubly degenerate fibre group
  = stable/unstable foliations of the monodromy* is standard and is
  **cited**; not re-derived.
- That the banked triple `(2+ω, 1−ω, 1−ω)` is m004's fibre group is
  **B448/B1344's**, cited; this arc verifies only that it satisfies the
  family's defining equation and is a non-trivial fixed point.
- `tr[A,B] = 2 ⟺ reducible` — the reason the parabolic condition reads `−2`
  rather than `+2` — is classical and **cited**; the Fricke identity itself
  is proved here.
- Nothing here reaches `CLAIMS.md`, F2 or Gate 5. No value is compared to any
  measurement. B675, B1002, B1349, B1402 and B1403 are untouched.

## 9. WHAT THIS OPENS

- **L212** — §5 puts the metallic ladder in Minsky's coordinates. The
  question it makes formulable: B675's bronze is **deaf** on the cusp side
  (`[ℚ(τ):ℚ] = 8`, Galois group `S₄`, non-abelian) while its end invariant
  `(3+√13)/2` is as ordinary as gold's — degree 2, purely periodic `[3]`.
  **Deafness is therefore not visible in the end invariant**, which says the
  cusp field and the classification coordinate carry different information
  about the same manifold. Where the bronze's obstruction lives, in
  Minsky's coordinates, is open and now askable.
- **L213** — Epstein–Penner as a name is absent while its object is used
  everywhere. Auditing which banked results silently assume canonicity
  (rather than merely using SnapPy's triangulation) is a bounded sweep.
- **L214** — the homonym filter is a tool, not an anecdote: the corpus's
  literature audits (`NOVELTY_AUDIT.md`, the registry's NEEDS-LIT rows) were
  all run by name.

Artifacts: `b1404_the_family.py` (40/40), `b1404_absence_audit.py` (pinned at
`d08d1f98`, so it cannot read its own report),
`absence_audit.json`. Locks: `tests/test_b1404_the_family.py`.
