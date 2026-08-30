# MEMO 156 — GATE D: THE FIRST NUMERICS AT THE OBJECT'S OWN κ

**Banked 2026-08-30.** Seal `seals/GATE_D_FIRST_NUMERICS_PREREG.md`, pushed before computing.
Certificate `certificates/gate_d_numerics.py`; output vendored.

**Nobody had looked at this.** `already_banked.py` on the gate's terms returns **0 settled arcs at
threshold**, from the instrument that discriminates correctly on the corpus's own controls.

---

## 0. OUTCOME

**`D-0 PASS | D1-REPRODUCES | D2-STRUCTURED | D3-GENERIC`** — exactly the prior recorded in the seal
before running, which is stated so the agreement is not read as confirmation of anything.

---

## 1. THE COUPLING IS FORCED, AND IT IS A SIXTH ROOT OF UNITY

The trace map's invariant **is** the programme's κ. Verified in-cell:

- **`κ = 1 + ω = √3·e^{iπ/6}`** to 1e-13 — exactly the value `OPEN_PROBLEMS.md` Gate D names;
- `I` is invariant under `(x,y,z) ↦ (xy−z, x, y)` to **8.6e-15** on 200 random complex points;
- and with the full-trace initial point `(E−λ, E, 2)`, **`I ≡ λ² + 2`** identically, so
  **`λ² = κ − 2 = ω²`** — the record's own banked identity — giving

> **`λ = ω`, a primitive sixth root of unity, `|λ| = 1`.**

The coupling is **not chosen**. It falls out of the object's own invariant, and it lands exactly on
the unit circle — the boundary between the regimes, which is itself worth a specialist's attention.

## 2. THE CONTROL, AND WHY IT IS NOT VACUOUS

At real λ the approximant spectra must be unions of **Fibonacci-many bands** with measure → 0:

| n | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| **bands** | **5** | **8** | **13** | **21** | **34** | **55** | **89** |
| measure | 1.427 | 1.075 | 0.789 | 0.587 | 0.434 | 0.321 | 0.238 |

**Every count is a Fibonacci number**, and the measure falls monotonically. That is the
Damanik–Gorodetski structure reproduced from scratch, and it is a control an empty instrument
**cannot** pass — which matters, because an earlier version of this cell passed exactly that way
(§4).

## 3. THE OBJECT

At `λ = ω`, over `[−6,6]²` in ℂ:

| n | area fraction | box-dim |
|---|---|---|
| 6 | 0.00285 | 1.247 |
| 8 | 0.00104 | 0.951 |
| 10 | 0.00037 | **0.794** |

**Zero interior cells.** So the object's set is a genuine fractal — empty interior, area → 0, and a
box-counting dimension **strictly between 0 and 2**. **D2-STRUCTURED:** the object's cocycle *does*
have the shape a Damanik–Gorodetski result describes. That is the first thing a specialist would
ask, and it now has a measured answer instead of a shrug.

**And it is not the object's alone.** Across same-modulus controls `κ = √3·e^{iθ}`:

| θ | 0 | π/12 | **π/6 (object)** | π/4 | π/3 | π/2 | 2π/3 |
|---|---|---|---|---|---|---|---|
| box-dim | 0.962 | 0.876 | **0.669** | 0.702 | 0.758 | 0.834 | 1.205 |

Every θ gives a fractal of comparable dimension. **D3-GENERIC.** The object's value *is the minimum
of the seven* — recorded because it is true, and **not claimed**, because the spread is 0.536 and one
point at the bottom of seven is not a discriminator. This is the B996 lesson applied before the fact
rather than after.

## 4. THE HONEST HEADLINE: THE CONTROL FIRED THREE TIMES BEFORE THE INSTRUMENT WAS FIT

The seal made the positive control **binding** — *"if it fails, no object result may be reported."*
It failed three times, and each failure was mine:

1. **Wrong convergence parameter.** I tested measure-shrinkage against *grid resolution*. A
   zero-measure set converges in **iteration count**; refining the grid at fixed N measures the same
   fattened set more finely and cannot shrink. Control fired.
2. **Mixed trace conventions.** I fed Sütő's *half-trace* initial point `((E−λ)/2, E/2, 1)` into the
   *full-trace* Fricke map. Control fired again. Fixing it produced the identity `κ = λ² + 2` and
   with it the `λ = ω` result — **the correction was worth more than the cell's own headline.**
3. **A vacuous pass — the dangerous one.** With the convention fixed, every fraction read `0.00000`
   and the control *passed*: "monotone and small" is satisfied by an instrument that finds
   **nothing**. A measure-zero Cantor set is invisible to grid sampling at any resolution. This is
   the MB12 failure the corpus names and `check_test_vacuity.py` exists to catch — **a criterion
   that can pass for the wrong reason.** Caught by noticing the real-λ spectrum, which is certainly
   non-empty, read as empty. The detector was rebuilt on the band method and the control was
   strengthened to require **non-emptiness and Fibonacci band counts**, which nothing degenerate can
   fake.
4. A fourth, smaller: a sign error made every box-dimension negative, which had D-2 reading
   DEGENERATE.

**Four instrument corrections, three of them caught by a control I had bound in advance and one by
reading.** The cell's real yield is that the seal's binding clause worked: at three separate points
I had a runnable instrument producing confident output, and each time the control refused it.

## 5. WHAT THIS BUYS, STATED NARROWLY

It does **not** answer Gate D, and a numerical picture is not a theorem. What it does:

- **reduces the specialist's unknown** from *"is there anything there?"* to *"there is a fractal of
  box-dimension ≈ 0.8 with empty interior, at a coupling forced to be a sixth root of unity, and the
  structure is shared by every same-modulus invariant"*;
- **supplies the `λ = ω` identity**, which is exact, derived, and not previously stated in this
  form on the record;
- **and pre-empts the question a specialist would otherwise ask first**, which is whether the
  complexity is object-specific. It is not, and we say so before being asked.

**Q10's queue row should carry all three**, and is updated accordingly.

## 6. FENCES

- Nothing from memos 137/143–147 was reused; the record warns that Hermitian machinery does not
  transfer and the cocycle was rebuilt from the trace map.
- Box-counting on a 600×600 grid at n = 10 is a coarse dimension estimate; the *ordering* of the
  seven controls should not be over-read, only the fact that all seven are comparable.
- Gate 5 clean: κ is the object's own invariant, computed from ω.
