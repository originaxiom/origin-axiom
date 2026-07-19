# FINDINGS A — CC2 (advisory, read-only)

**Prereg cited:** `MASTERPLAN_AND_PREREG.md`, sha256 =
`a06a1b074f22548d5d875baa8845914ca98bb007e5f789d6190df216d24cf6b6`
(verified locally: `shasum -a 256` on the seat-local copy reproduces this hash exactly.)

**Method:** exact symbolic arithmetic (sympy, `Rational`/`sqrt`/`exp(I*pi*...)`, no floats used for any
claim — floats shown below are decimal *display* of exact values only).

---

## HEADER VERDICT

**AUDIBILITY-LAW-HOLDS.**

> A prime stage p hears a real metallic tone ⟺ p ≡ 1 (mod 4) ⟺ ℚ(√p\*) is real (p\* = (−1)^((p−1)/2)·p),
> and the tone itself is α = (−1±√p\*)/2, the Gauss‑sum‑split trace of the two (p−1)/2‑dimensional
> cuspidal ("golden") characters of SL(2,p) on a regular unipotent element.
> **Only p = 5 gives a literally metallic-ratio (unit) tone** — α = 1/φ = φ⁻¹, norm exactly −1, the
> fundamental unit of ℚ(√5) itself. For p = 13, 17, 29 the tone is a genuine, non-unit real quadratic
> integer of ℚ(√p) (norm −(p−1)/4 = −3, −4, −7 respectively) — real, audible, but *not* metallic in the
> strict unit/φ sense. This finer distinction is the actual content of this cell (see base-rate gate below).

---

## PART 1 — Disentanglement: swap ≠ weld (the B702 correction)

### (a) Being-face SWAP — golden case
Eigenvalues (ζ₆, ζ̄₆, ω², ω, 1), all roots of unity:

| eigenvalue | exact value | 2·Re |
|---|---|---|
| ζ₆ = e^{iπ/3} | (1+i√3)/2 | **1** |
| ζ̄₆ = e^{−iπ/3} | (1−i√3)/2 | **1** |
| ω² = e^{−2iπ/3} | (−1−i√3)/2 | **−1** |
| ω = e^{2iπ/3} | (−1+i√3)/2 | **−1** |
| 1 | 1 | **2** |

Tones: {1, 1, −1, −1, 2} ⊂ **ℚ** — all rational.
Trace field: ζ₆ generates ℚ(ζ₆) = **ℚ(√−3)** (since ζ₆ = (1+√−3)/2) — **imaginary quadratic**.
(Silver swap: (d₀,d₁,1,−1,1), non‑torsion norm‑1 elements of ℚ(i); tones are likewise rational, field
**ℚ(i) = ℚ(√−1)**, also imaginary. Verified separately — not the load‑bearing computation of this cell,
included for completeness of the correction statement.)

### (b) Hearing-face WELD — order‑10 monodromy
e^{±i·108°} = ζ₁₀^{±3} (confirmed: arg(ζ₁₀³) = 108° exactly, sympy `arg` = 3π/5 rad).

2·Re(ζ₁₀³) = 1/2 − √5/2 = **−1/φ**, where φ = (1+√5)/2.

Exact check: sympy confirms `simplify(2*re(zeta10**3) - (-1/phi)) == 0` → **True**.
Field: **ℚ(√5)** — **real** quadratic.

### (c) Conclusion — the objects are disjoint
| object | face | trace field | real/imaginary | tones |
|---|---|---|---|---|
| golden SWAP | being | ℚ(√−3) | imaginary | rational {1,1,−1,−1,2} |
| silver SWAP | being | ℚ(√−1) | imaginary | rational |
| WELD (order‑10) | hearing | ℚ(√5) | **real** | **metallic**, −1/φ |

**B702 is corrected:** "metallic hearing ⇔ real‑quadratic SWAP" conflates two unrelated objects. The
SWAP (being‑face, either golden or silver) lives in an imaginary quadratic field with rational trace —
**no metallic tone is present in either swap, full stop**. The metallic tone (−1/φ ∈ ℚ(√5), real) belongs
to the WELD, a hearing‑face object. The real golden‑vs‑silver asymmetry that *does* exist between the two
swaps is **torsion (golden: roots of unity, periodic) vs non‑torsion (silver: infinite order, aperiodic)**
— not a real‑field‑vs‑imaginary‑field distinction, since both swap fields are imaginary quadratic.

---

## PART 2 — The audibility law (prime stages)

Standard fact (B700 cell 5, cited not re-derived): SL(2,p) has two irreducible "golden" characters of
degree (p−1)/2 over the character field ℚ(√p\*), p\* = (−1)^((p−1)/2)·p ≡ 1 (mod 4). On a regular unipotent
element, the two characters take the Gauss‑sum‑split values **α± = (−1 ± √p\*)/2**.

### Table 1 — field / reality

| p | p mod 4 | p\* | field ℚ(√p\*) | real? |
|---|---|---|---|---|
| 5 | 1 | 5 | ℚ(√5) | **REAL** |
| 7 | 3 | −7 | ℚ(√−7) | imaginary |
| 11 | 3 | −11 | ℚ(√−11) | imaginary |
| 13 | 1 | 13 | ℚ(√13) | **REAL** |
| 17 | 1 | 17 | ℚ(√17) | **REAL** |
| 29 | 1 | 29 | ℚ(√29) | **REAL** |

### Table 2 — AUDIBLE stages (p ≡ 1 mod 4): exact tones

Minimal polynomial of α: x² + x − (p−1)/4 = 0 (trace −1 always; norm −(p−1)/4).

| p | α+ = (−1+√p)/2 | α− = (−1−√p)/2 | norm N(α) = −(p−1)/4 | is α a **unit** (metallic ratio)? |
|---|---|---|---|---|
| 5 | (−1+√5)/2 = **1/φ** ≈ 0.618034 | (−1−√5)/2 = **−φ** ≈ −1.618034 | **−1** | **YES — α+ = φ⁻¹, the fundamental unit of ℚ(√5) itself (inverse)** |
| 13 | (−1+√13)/2 ≈ 1.302776 | (−1−√13)/2 ≈ −2.302776 | −3 | no — fundamental unit of ℚ(√13) is (3+√13)/2, norm −1; α has norm −3, not a unit |
| 17 | (−1+√17)/2 ≈ 1.561553 | (−1−√17)/2 ≈ −2.561553 | −4 | no — fundamental unit of ℚ(√17) is 4+√17, norm −1; α has norm −4 |
| 29 | (−1+√29)/2 ≈ 2.192582 | (−1−√29)/2 ≈ −3.192582 | −7 | no — fundamental unit of ℚ(√29) is (5+√29)/2, norm −1; α has norm −7 |

**Verified exactly (sympy):** norm(α) = α+·α− = −(p−1)/4 for all four; this equals ±1 (unit condition)
**only** at p = 5, since −(p−1)/4 = −1 ⟺ p = 5. For p = 13, 17, 29 the tone is a bona‑fide real quadratic
*algebraic integer* of ℚ(√p) — audible (real) but **generic**, not a unit / not a power of the field's
fundamental unit, hence not "metallic" in the strict continued‑fraction/unit sense that gives φ its name.

### Table 3 — INAUDIBLE stages (p ≡ 3 mod 4): confirmation

| p | p\* | α± = (−1±√p\*)/2 |
|---|---|---|
| 7 | −7 | (−1±i√7)/2 — complex conjugate pair, **no real part beyond −1/2 shared**, not real-valued as a tone |
| 11 | −11 | (−1±i√11)/2 — complex conjugate pair, non-real |

ℚ(√−7), ℚ(√−11) are imaginary quadratic ⇒ α± ∉ ℝ ⇒ **no real metallic (or even generic real) tone exists
at these stages** — confirmed exactly, not merely by the mod‑4 heuristic.

### Side remark (clearly separated from the Part 1 correction, not a re-conflation)
The p = 5 prime‑stage tone α+ = 1/φ and the weld tone −1/φ (Part 1b) both lie in ℚ(√5) and are literally
± inverse powers of φ (sympy: `simplify(-1/phi + 1/phi) == 0` trivially, i.e. they are negatives of one
another). This is a coincidence *worth flagging*, not a claim that the SL(2,5) cuspidal character and the
order‑10 weld monodromy are "the same object" — they are computed from different structures (a finite
group character table vs. a monodromy eigenvalue). It does independently corroborate that **ℚ(√5) /
metallic‑ratio content is a hearing‑adjacent, real‑quadratic phenomenon**, and that it is emphatically
absent from the being‑face swaps (Part 1a), which are confined to imaginary quadratic fields with purely
rational trace.

---

## BASE-RATE GATE

- "ℚ(√p\*) is real ⟺ p ≡ 1 mod 4" is the **standard Gauss‑sum quadratic‑reciprocity fact** (p\* is defined
  precisely so this holds) — **this alone does not count** as a result; it is bookkeeping.
- The actual content delivered by this cell:
  1. **The correction itself**, stated exactly: swap (imaginary quadratic, rational tones, both golden
     and silver) is disjoint from weld (real quadratic ℚ(√5), metallic tone); the golden/silver asymmetry
     is torsion vs non‑torsion, not real vs imaginary.
  2. **The fine structure inside "audible"**: not all p ≡ 1 mod 4 stages are metallic in the same sense.
     p = 5 is *exactly* singled out among {5,13,17,29} because its cuspidal-character norm −(p−1)/4 hits
     −1, making the tone a genuine unit (φ⁻¹) — the literal fundamental unit of its field. p = 13, 17, 29
     are real and audible but their tones are ordinary (non‑unit) quadratic integers, not metallic ratios.
     **This answers the prompt's question directly: φ (p=5) is special, not generic, among audible stages.**

---

*End of exact-arithmetic cell. No git or repo state was touched; this file is new advisory output only.*
