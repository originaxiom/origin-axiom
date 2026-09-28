# xB033 — THE HEADLINE IS THIS ARC'S OWN PROCESS FAILURE: the main claim was banked 26 days earlier, in the very lead this arc was reading, one line below where it stopped reading

**Seat `xb`, `sep16-branch`, 2026-09-28. PREREGISTRATION sealed at `0721f678`.**

---

## 0. WHAT WENT WRONG, FIRST

The seal derived, and set out to test: *for a closed amphichiral hyperbolic 3-manifold `cs ≡ 0 (mod ½)`;
the quarter class cannot occur.*

**`B1239` banked exactly that on 2026-09-02.** Its verdict row, verbatim:

> *"the observable statement (1/4 excluded) needs neither Kawauchi nor freeness: APS `3eta = 2cs +
> tau (mod 2)` with `eta = 0` under ANY orientation-reversing isometry and `tau` an integer gives `cs`
> in `{0,1/2}` mod 1 for every closed amphichiral manifold — **verified on the ENTIRE closed census,
> 37 amphichiral / 37 zero (7.8e-16)**"*

**And it is written into `L194` itself** — the lead this arc opened — as the *"Refined 2026-09-02
(B1239)"* paragraph. **This seat read `L194` with a fixed 15-line window that ended one line before
that paragraph began.** The answer was two lines past the edge of the window.

> **A fixed-line window is not reading a lead.** `already_banked.py` exists on this bench; the seal
> did not run it. **This is the second process failure of this kind in the session** — xB029 leaned on
> Friedmann–Witten while filing them CITED-UNREAD in the same commit — and both have the same shape:
> **the information needed was present and not looked at.**

---

## WHAT SURVIVES, AND IT IS MODEST

### 1. Independent reproduction 26 days later — and 48 orders tighter

| | B1239 (2026-09-02) | **xB033 (2026-09-28)** |
|---|---|---|
| closed census scanned | entire | **11 031, 0 errors** |
| amphichiral (`is_amphicheiral()`) | **37** | **37** |
| of those at class **zero** | **37** | **37** |
| max `\|folded cs\|` | `7.8 × 10⁻¹⁶` | **`3.8 × 10⁻⁶⁴`** |

The tightening is not a new idea — it is `ManifoldHP` where B1239 used double precision. **The result
is B1239's; the precision is this arc's.**

### 2. A predicate correction, in B1239's favour and against this arc's

Y1 required `is_full_group() AND is_amphicheiral()` and got **36**. B1239 required only
`is_amphicheiral()` and got **37**. **B1239 was right and this arc was over-strict.**
`is_full_group() == False` means SnapPy has not certified the symmetry group is the full one, so
`is_amphicheiral()` can give a **false negative** there but not a false positive — **requiring it can
EXCLUDE a genuinely amphichiral manifold, which for a claim of the form "EVERY amphichiral manifold is
at zero" tests a strictly WEAKER statement.** The one manifold at issue is **`v2678(2,1)`**, and it is
at class zero. Y1's 36 is a subset of the 37.

### 3. Two more inputs stripped from the derivation

B1239 established the statement *"needs neither Kawauchi nor freeness"* and reached it through
**APS** (`3η ≡ 2cs + τ (mod 2)`) with **`η = 0`**. It needs neither of those either:

> **(i)** for closed `M`, `cs` is well defined **mod 1** — CGHN §5A, READ-AT-SOURCE ·
> **(iii)** `cs(M*) = −cs(M)`
> ⟹ amphichiral gives `cs ≡ −cs (mod 1)` ⟹ `2cs ≡ 0 (mod 1)` ⟹ **`cs ∈ {0, ½} (mod 1)`** ⟹
> **`cs ≡ 0 (mod ½)`.**
>
> **No `η`. No APS. No `τ`. No Kawauchi. No freeness.**

**THE WEAKEST LINK, NAMED AND NOT VERIFIED:** `cs(M*) = −cs(M)` is **USED-NOT-READ** in this record —
xB021 (A6/A7) and xB023 (W0) rely on it and **no arc quotes a source for it.** The whole derivation
rests on it, and so, differently, does B1239's (`η(M*) = −η(M)`). **Neither is read at source.**

### 4. The contrast, quantified — and it is the modulus that does the work

| | modulus of `cs` | amphichirality forces | quarter class |
|---|---|---|---|
| **closed** | **mod 1** (CGHN §5A) | `cs ∈ {0, ½}` | **EMPTY — 0 of 37 measured** |
| **cusped** | **mod ½** (Neumann; CGHN §5A) | `cs ∈ {0, ¼}` | **NON-EMPTY — 75 of 181 measured** |

**Y2 reproduces xB023 exactly:** amphichiral one-cusped `{zero: 106, quarter: 75, other: 0}`, 0 errors.

> **So the `0`-vs-`¼` dichotomy the record has circled since 2026-09-02 is a fact about the MODULUS of
> `CS`, not about the manifolds — and B1239 already called it "cusp-local". This arc adds the reason
> the locality is there: `π²` versus `2π²`.**

### 5. The negative control, which is what makes the closed number mean anything

Of **400** non-amphichiral closed manifolds (a **declared** bounded sample), **395 are at class
"other"** and only **5 at zero** — a base rate of **1.25 %**. Against that, 37 of 37 amphichiral at
zero is not a coincidence the census could produce. **The constraint is real and the instrument
discriminates.**

---

## THE VERDICT

**xB033 banks no new mathematics.** It reproduces B1239 at higher precision, corrects its own
predicate in B1239's favour, strips two inputs from the derivation, and quantifies the closed/cusped
contrast with a clean negative control.

**L194 is unchanged and still open.** It asks about **cusped** manifolds with a **free
orientation-reversing deck**, where amphichirality alone permits `¼` — and B1239 already localised it
to *"an orientation-reversing isometry acting freely on every cusp it preserves."* **Nothing here
touches that.**

**Gate 5 absolute. No value. Nothing to `CLAIMS.md`.**

## SCORING THE SEAT'S PRIOR

Y1 holds with a clean negative control **(correct, and irrelevant — it was already known)** · Y2
reproduces **(correct)** · Y3's *"a relocation, not an answer"* **(correct, and the relocation was
B1239's)** · **and the prior missed the only thing that mattered: whether the arc was necessary at
all.** **The seal's prior said the best outcome was "that the record stops treating the ¼ class as a
phenomenon about manifolds when it is a fact about a modulus." The record had stopped 26 days ago.**
