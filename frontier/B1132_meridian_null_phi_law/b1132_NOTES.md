# R_meridian — B1128's two remainders: (B) the non-degenerate meridian, (C) the φ-law

**Scope.** Closes the two items B1128 (`frontier/B1128_instrument_null/`) left open: its own
named fenced gap ("a DIFFERENT meridian would see the invisible wy-component and report
different numbers, and this was not searched") and its flagged, un-banked side-finding
(`h(R²L², θ) = −φ·h(RL, θ)`). Charter: `VALUE_PROBE_WAVE_CHARTER.md`. All work is on this
bench, in this scratchpad directory; the repo was read-only throughout. Gate 5 checked
mechanically (grep, reported below): no SM number appears before the explicit Part C
section of `meridian.py`.

**Deliverables in this directory.**
- `meridian.py` — standalone (no repo imports, no machine paths), the whole computation.
- `results.json` — its machine-readable output (verdict + every number below).
- `full_run.log` — the full stdout of the run this NOTES.md reports.
- `reference_b1128_instrument.py` + `reference_run.log` — B1128's own script, copied
  verbatim and re-run on this bench as an independent reproduction control (its output
  diffed byte-identical against the banked `frontier/B1128_instrument_null/b1128_results.json`,
  confirmed before any new code was written).

---

## 0. Controls first (both reproduction routes agree with B1128, exactly)

Two independent reproductions of B1128, both exact:

1. **B1128's own script, re-run verbatim** on this bench: `diff` against the banked
   `b1128_results.json` after JSON-normalizing both sides — **byte-identical, exit 0**.
2. **`meridian.py`'s own independent re-implementation** (Part A — same logic, written
   fresh, not imported): Kac-Peterson gates PASS (errors ~1e-50); B593's value reproduced
   to 7.4e-51; both curves' real-circle ranges match B1128's banked `[0.309017, 0.587785]`
   and `[0.500000, 0.951057]`; the original degeneracy `h(R²L²,θ)=−φ·h(RL,θ)` reproduced
   with worst residual 1.15e-50 (B1128 reported 1.1e-50).

New control specific to this extension: **`M_odd(g)` has `det = 1` exactly** (err ~1e-51)
for both `g = RL` and `g = R²L²`, for the whole tested run — i.e. the welded 2×2 matrix is
genuinely in SU(2), not merely unitary up to an unaccounted phase `χ(g)`. This licenses the
Pauli decomposition `M = w0·I + i(wx·σx+wy·σy+wz·σz)` with **all four components exactly
real** (checked: max imaginary residue 3.7e-51) — the load-bearing fact that makes reading
off `wy` below a legitimate move rather than a discarded phase.

---

## 1. TASK (B) — the full sphere, and whether the degeneracy survives leaving the circle

### 1.1 The extension

B1128's real great circle `u(θ) = cosθ·u3 + sinθ·u6` is the `ψ ∈ {0,π}` slice of the
standard qubit/coherent-state parametrization of the **whole** of ℂP¹_odd:

```
u(θ,ψ) = cos(θ)·u3 + e^{iψ}·sin(θ)·u6,   θ ∈ [0, π/2],  ψ ∈ [0, 2π)
```

— every ray hit exactly once (the two coordinate singularities at θ=0 (`=u3`) and θ=π/2
(`=u6`) are ordinary spherical-coordinate degeneracies, not a construction defect; verified
`ψ=0` reproduces B1128's closed form with **zero** numerical difference). The closed form

```
h(g, u(θ,ψ)) = tone(g) + i·[ wx(g)·sin2θ·cosψ + wy(g)·sin2θ·sinψ + wz(g)·cos2θ ]
```

is the standard SU(2) expectation-value formula (Bloch vector of `u(θ,ψ)` dotted into
`(wx,wy,wz)`); verified against **direct brute-force** evaluation
`u(θ,ψ)† · weld(word) · u(θ,ψ)` at random points with `sinψ ≠ 0` (genuinely off-circle):
worst difference **7.0e-51**.

### 1.2 Does the degeneracy break off-circle? Yes — exactly, everywhere, by a closed form

Reading off all four Pauli components (something B1128's own `curve_axis` already computed
but never used, since its real-circle formula only needed `wx,wz`):

| | tone | wx | wy | wz |
|---|---|---|---|---|
| RL | `+1/(2φ)` | −0.262865556060 | **`−φ/2`** | +0.425325404176 |
| R²L² | `−1/2` | +0.425325404176 | **`(1−φ)/2` = `−1/(2φ)`** | −0.688190960236 |

`(tone, wx, wz)` of R²L² equal exactly `−φ·(tone, wx, wz)` of RL (residuals ~1e-51 — the
part that was already forced, hence the real-circle degeneracy). **`wy` does not**: the
naive residual `wy_B − (−φ·wy_A)` is **exactly `−φ`** (not small — a whole unit of φ),
confirmed two ways:

- **Numerically**, 50 digits: `wy_B − (−φ·wy_A) = −1.6180339887498948482045868...`, matching
  `−φ` to every printed digit.
- **Symbolically** (sympy, not just floating point): `mp.identify()` gives the closed forms
  `wy(RL) = −φ/2`, `wy(R²L²) = (1−φ)/2`; substituting and reducing
  `wy_B + φ·wy_A + φ` modulo φ's own minimal polynomial `φ²−φ−1` gives the zero polynomial
  **identically** — an algebraic proof, not a coincidence at 50 digits.

This gives an exact global identity for the whole Pauli 4-vector (`ŷ = (0,0,1,0)`):

> **`axis(R²L²) = −φ · [ axis(RL) + ŷ ]`**

which implies, at *any* listener `u ∈ ℂP¹_odd` with Bloch vector `(n_x,n_y,n_z)`:

> **`h(R²L², u) = −φ·h(RL, u) − iφ·n_y(u)`**   — **THE GOLDEN MERIDIAN LAW**

Verified at 50 digits at 20 points spanning both poles, four on-circle points, and 16
uniform-random points on the whole sphere: worst residual **1.15e-50** (matches the
precision floor of every other exact identity in this file — i.e. this holds to the limits
of the arithmetic, not approximately). The **naive** relation `h_B = −φ·h_A` was checked at
the same 20 points: residual ~1e-50 wherever `n_y ≈ 0` (poles, on-circle points), and **O(1)**
wherever `n_y` is not small — e.g. residual 1.16 at `n_y=+0.717`, 1.45 at `n_y=−0.896` — in
every case matching `φ·|n_y|` to 3+ significant figures, exactly as the closed form predicts.

**So: yes, the degeneracy breaks off the real circle — completely and provably, not just
"generically."** The exact zero-locus of the breaking term `−iφ·n_y(u)` is `n_y(u)=0`,
which (accounting for the θ=0,π/2 coordinate singularities, themselves already `n_y=0`) is
**precisely** the real great circle through u3, u6 — B1128's own curve, and only that curve.
This is a complete, closed-form answer to the domain question, not a sampled one.

### 1.3 The full-sphere 1-input → N-prediction test (Part C, the only place SM numbers appear)

Because ℂP¹_odd is a genuine 2-real-dof domain and the charter allows exactly ONE
calibration input, fixing `|h_A(u)|=target` leaves a **1-dof residual curve** of solutions,
not a point — so "the prediction" is honestly a **range**, not a number. This is itself the
structural finding `docs/LISTENER_MAP_SPEC.md` anticipated in its own construction notes
("one calibration equation would leave a whole residual circle of u's undetermined, and
'the other predictions' would not be well-defined numbers at all") — confirmed here by
direct computation rather than assumed.

Both the exact closed-form range (elementary spherical geometry: fixing one linear
functional of the Bloch vector to a level set constrains a second linear functional to a
provably-derived interval) and an independent float-precision numeric scan (dense grid +
bisection) were computed; they agree to 5+ significant figures throughout — two independent
methods, as this corpus's standard requires.

| test | calibrate on | achievable range | target box (NO) | overlap? | box as % of range |
|---|---|---|---|---|---|
| Branch-1 analog | \|U_e2\| | \|h_B\| ∈ [0.5, 0.9647] | \|U_e1\| ∈ [0.8092,0.8345] | **yes** | 5.4% |
| Branch-2 analog | \|U_e1\| | \|h_A\| ∈ [0.309, 0.8102] | \|U_e2\| ∈ [0.531,0.5676] | **yes** | 7.3% |
| Ue3 screening | — | both curves' floor ≥ tone ≥ 0.309 | \|U_e3\| ≤ 0.1562 | **excluded a priori**, zero look-elsewhere (survives the widening: still below both curves' minima even at full sphere spread) | — |

Both IO numbers agree with NO to 4 significant figures throughout (not tabulated
separately).

**Coincidence accounting (the charter's rule 4: "a hit must exceed what the unknown can
absorb").** A third, uncalibrated test: what fraction of ℂP¹_odd's own natural (uniform)
measure gives `|h_B|/|h_A|` inside the measured PMNS e-row ratio box, with **no**
calibration at all? Monte Carlo, uniform-on-sphere sampling, 200,000 points, **seed-stability
checked** (5 independent seeds, 500,000 points each: 0.0610, 0.0611, 0.0610, 0.0606, 0.0610
— stable to better than 1%, per this corpus's own exploratory-numerics-rigor standard):

> **≈6.0–6.1% of the whole sphere, with zero calibration, already lands inside the measured
> PMNS ratio box.**

This is the load-bearing number. All three tests land in the same 5–7% ballpark — not a
coincidence of my analysis, but the same fact seen three ways: the freed degree of freedom
(`ψ`, equivalently the achievable-range width) is generically wide enough that a target
sitting near the middle of the SM's own plausible magnitude range has an unremarkable,
one-in-roughly-sixteen chance of falling inside it, **before any object-side structure is
consulted at all**. Framed the way the charter's rule 4 asks — does the hit exceed what
the freed unknown can absorb — the answer is no: a ~6% baseline rate is exactly what "the
unknown absorbed it" looks like, not what "the unknown was forced and still landed
correctly" looks like (contrast the *original* real-circle test, which had **zero** residual
freedom and still missed by ≈5σ — the diagnostic case the charter's language is built for).

**Multiple-testing context (why 6% is not even the right number to compare to 5%).** This
probe alone runs 5–6 near-duplicate sub-tests (2 branches × 2 orderings + the ratio test ×
2 orderings) against the same underlying freedom; at a flat 6% per-test rate,
`P(at least one "hit" among 6) ≈ 31%`. Folding in the coupling channel's own prior recorded
history — 7 sealed value-contact attempts before this one, all null (B1027+B1063, B1066
R-A, B1066 R-B, B1075), this probe's real-circle test being an 8th — pushes the honest
"at least one coincidence this good somewhere in the channel's search history" rate past
50% (`1-(1-0.06)^14 ≈ 58%`) even under a pure-null hypothesis. A ~6% one-off is not a
finding in that context; it is the expected residue of having looked several times.

### 1.4 VERDICT (B): **INSTRUMENT-NULL-FULL-SPHERE**

Precisely, not the same shape as B1128's own null:

- The degeneracy **does break** off the real circle — provably, exactly, everywhere except
  that one curve (§1.2). This is **not** "STILL-DEGENERATE": genuine new dof appears, and
  B1128's own fenced concern ("a different meridian would see the invisible wy-component
  and report different numbers") is **confirmed true** as stated.
- But the newly-freed direction carries **no detectable SM content**: a clean point-valued
  crossing is not even well-posed off the circle (2 dof, 1 input ⇒ a range, not a number,
  §1.3), and graded as generously as possible — does the achievable range bracket the
  target — the answer is yes in both branches, but only by consuming a small, unremarkable
  slice (5–7%) of what the freed freedom can reach, matched independently by a ~6%
  uncalibrated whole-sphere coincidence rate that is itself unremarkable against this
  channel's multi-attempt search history. This is **not** "INSTRUMENT-PREDICTS": nothing
  here exceeds what the unknown can absorb (charter rule 4).
- So the null **extends to the whole of ℂP¹_odd**, closing B1128's fenced gap — but for a
  sharper, more informative reason than "still misses a point": the instrument trades one
  kind of non-informativeness (the real circle's forced, zero-dof identity) for a different
  kind (the full sphere's under-determined, range-only test) — neither configuration
  supports a genuine falsifiable point-crossing. B1128's honest prior (MISS EXPECTED) held
  a second time, on the one direction it had explicitly left unsearched.

**Not numerology, checked directly (same discipline B1128 applied to itself):**
- *Is the extension itself hidden fitting?* No — `(θ,ψ)` is the unique standard,
  no-extra-convention parametrization of the whole projective line (this is what closes
  the "which meridian" question, not another arbitrary pick: the answer is "cover all of
  them," not "choose a second one").
- *Was the 20%/absorbed-threshold or the SM boxes chosen after seeing the numbers?* No —
  the same PMNS boxes B1128 pre-committed (NuFIT 6.1, both orderings) are reused verbatim;
  no new SM number was introduced; the coincidence-accounting machinery (closed-form range
  + Monte Carlo fraction) was designed before the target-box-occupancy numbers were computed
  (the code path is generic in the target, not tuned to this pairing).
- *Could a different word pair have been chosen to make this look better or worse?* Not
  attempted here, deliberately — this probe extends B1128's SAME `RL`/`R²L²` pair to the
  sphere; picking a different pair would conflate two separate questions (which meridian,
  which words) and re-open exactly the scan-and-pick risk the charter forbids. Left as an
  explicitly named open door (below), not silently avoided.

---

## 2. TASK (C) — THE GOLDEN MERIDIAN LAW, formalized

**Statement (banked-ready, one line):**

> For SU(3) at level 2's coupling instrument, with `u3,u6` the derived listener pair
> (B1070/B1071) and `u(θ,ψ)=cosθ·u3+e^{iψ}sinθ·u6` parametrizing all of ℂP¹_odd: the welded
> couplings of `RL` and `R²L²` satisfy, EXACTLY and EVERYWHERE on ℂP¹_odd,
> `h(R²L²,u) = −φ·h(RL,u) − iφ·n_y(u)`, where `n_y(u)=sin2θ·sinψ` is `u`'s Bloch
> y-coordinate; equivalently `axis(R²L²) = −φ·[axis(RL) + ŷ]` as Pauli 4-vectors. The simple
> proportionality `h(R²L²,u) = −φ·h(RL,u)` (B1128's discovery) holds if and only if
> `n_y(u)=0`, i.e. `u` lies on the real great circle through `u3,u6` — nowhere else.

**Domain, exactly characterized (not sampled):** the "if and only if" above is closed-form,
not empirical — it follows directly from `wy(R²L²)+φ·wy(RL)=−φ` being a nonzero constant
(proved symbolically, §1.2), so the breaking term `−iφ·n_y(u)` vanishes exactly on, and
only on, `n_y(u)=0`. That locus is exactly the real great circle (the poles are its two
zero-measure endpoints). This is a complete domain characterization, upgrading B1128's own
"specific curve... not the only choice, and this was not searched" (FINDINGS.md) to a
closed statement: it is not merely "a" choice, it is *the unique locus where the simple
form holds at all*.

**Verification:** 50-digit numeric (mpmath), two independent routes (direct algebraic
substitution into the Pauli decomposition, and brute-force `u†·weld(word)·u` evaluation) —
worst residual 1.15e-50, at 20 points spanning poles/circle/generic; **plus** a symbolic
(sympy) algebraic proof of the load-bearing sub-identity `wy(R²L²)+φ·wy(RL)+φ≡0` modulo
φ's minimal polynomial `φ²−φ−1`, i.e. not merely exact-to-50-digits but exact-as-algebra.

**Is it a known McKay/modular identity, or new?** Not identified as a restatement of an
existing banked law — `docs/LAW_MAP.md` was greped for "golden"/"phi"/"φ" (dozens of hits,
none matching this specific two-word Pauli-vector shift-and-scale form) and B1128's own
`FINDINGS.md`/`NOTES.md` explicitly flag it as "not previously stated as a law in the
corpus... a candidate LAW_MAP row on its own merits." This work does not newly search the
wider McKay-correspondence literature for a match (out of scope for this probe; named as an
open item below) — the honest claim is: new to this corpus, mechanism understood
(the exact Pauli-vector identity above), deeper origin (why `R²L²`'s axis is `RL`'s axis
shifted by exactly one unit of φ along the SAME axis (`ŷ`) that carries the breaking, and
scaled by exactly the ratio already forced on the other two axes) not derived from first
principles — flagged, not hidden.

**Proposed LAW_MAP row** (for the banking seat's judgment, format matching existing rows):

| law | statement | status | witnesses | upgrade path |
|---|---|---|---|---|
| **THE GOLDEN MERIDIAN LAW (SU(3)₂ coupling instrument)** | On the whole of ℂP¹_odd (the listener sphere spanned by the derived pair u3,u6): `h(R²L²,u) = −φ·h(RL,u) − iφ·n_y(u)`, `n_y` the Bloch y-coordinate; equivalently `axis(R²L²)=−φ·[axis(RL)+ŷ]` as Pauli 4-vectors, `ŷ=(0,0,1,0)`. The simple degenerate form `h(R²L²,u)=−φ·h(RL,u)` (B1128) holds IFF `n_y(u)=0` — exactly the real great circle through u3,u6, nowhere else. | **LAW** (exact, 50-digit + symbolic algebraic proof of the load-bearing sub-identity `wy(R²L²)+φ·wy(RL)=−φ`; mechanism understood — the Pauli-vector shift-and-scale identity — deeper group-theoretic origin open) | B1128 (the degenerate case, real circle); this probe, `frontier/.../R_meridian` when banked (the full-sphere extension + symbolic proof) | the group-theoretic reason `R²L²`'s axis is `RL`'s axis shifted by exactly `φ·ŷ`; whether the same shift-and-scale form recurs for other word pairs in the period-5 family (B1128 §2's other 6 words) or is specific to this pair |

---

## 3. Open items registered (not silently dropped — per WORKING_RULES' registration-over-preservation rule)

- **The wider McKay/modular-identity literature search** for the golden-meridian law's
  possible prior appearance elsewhere (outside this corpus) was not performed — flagged in
  §2, not attempted here (this probe's mandate was construct-and-verify on this bench, not
  a literature sweep).
- **The other 6 words** of B1128's period-5 short-word family (`L¹R¹, R³L³, L³R³, R⁴L⁴,
  L⁴R⁴`, all shown by B1128 to share one of the two `|h(θ)|` curves already tested) were
  not individually re-checked for their own shift-and-scale constant off-circle — B1128's
  own real-circle finding (every word matches curve A or curve B's `|h(θ)|` exactly) makes
  this a same-answer-expected but unconfirmed extension; named, not assumed.
- **`wx(g), wz(g)`'s own closed forms** were obtained via `mp.identify()` as nested
  radicals (e.g. `wx(RL) = −√((20−√80)/160)`) but not simplified or symbolically re-verified
  the way `wy` was (since the `−φ` scaling of `wx,wz` was already established at B1128's own
  50-digit standard and re-confirmed here at the same standard — a symbolic proof of that
  part specifically was not additionally sought, since it was not the new content of this
  probe).
- **The CKM bonus** (§ Part C) inherits B1128's own scoping caveat verbatim (PDG values
  carried from training knowledge, not freshly fetched this session) and is reported only
  as descriptive, exploratory context (achievable-range-given-calibration), not graded
  pass/fail — B1128 itself never defined a specific "which CKM entry does curve B predict"
  target, and this probe does not manufacture one post hoc.
- **Whether the ~6% coincidence rate itself is stable under a different SM-side box choice**
  (e.g. a 1σ vs 3σ PMNS box) was not swept — the pre-committed 3σ boxes (matching B1128's
  own convention) were used throughout, once, not re-graded after seeing the result.
