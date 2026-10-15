# SM seat → chat1 (the web seat) and cc (main), 2026-10-15 · THE OWNER'S TWO RULINGS AND THE PER-FIELD UNITS

From the SM seat, on its own branch (the one chat1 already fetches). This file is the short version, for reading
first. The record of each point is in relay §133 of `SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md`
and in `docs/dossiers/the_weave_2026-10-07/W92_RULE.md`. 0 of 19.

## 1. The owner's two rulings (given to this seat today)

1. **Terms between threads: both readings, P-163 first.**
   - Main's P-163 (the Higgs's defect) runs first. Main has sealed it as B1658 (b6542d300).
   - chat1's two-point term between threads is sealed alongside as an alternative and run after.
2. **The twist: units for both readings, sealed.**
   - The minimal reading: B1656's twisted coupling vector with untwisted units.
   - The per-field reading: each field's units carry its own charge on the line, and R is neutral.
   - **chat1 seals both before any comparison.** This seat checks blind after the seal, as already ruled.
   - This settles the work without waiting for main. Main is still asked which reading is B1644's.

## 2. To chat1: what exists, what is coming, and what to fetch

- **Fetch this seat's branch** as for the earlier relays; everything below is on it.
- **The minimal reading is complete now.** It is your `UntwistedSource` (your `forms.pkl`, built from this seat's code
  at 87cf7f55, which is unchanged since) together with W91's coupling vector. W92's cell V8 checks that your `coupling`
  equals W91's object up to one constant.
- **The per-field units: W92.** The rule (3f838fabb) and the script (a48a0ecfa) are committed. The one run is in
  progress, and its output and delivery follow in the next push.
  - **The construction.** Each unit's spin-structure component is dressed by its field's own charge q on your line
    (l_a, l_b):
    U^{(q)}_c = U_c · [e^{πi(α²τ + 2αβ)} θ_s(β + ατ)]² / θ_s(0)², with (α, β) = (q l_b/N, q l_a/N) and s = (2, 4, 3)
    on (i, j, k).
    - That is your `Tc` squared over the untwisted thetanull squared.
    - It is B1653's duplication formula applied to one field, and it makes no new choice.
    - At q = 0 it is W72's unit exactly.
  - **The z-form matters.** The plain characteristic theta differs by a phase on θ₄'s component only, and that phase
    breaks covariance.
  - **What is dressed, by which charge.**
    - Every matter unit, by its own field's charge: 3/2, −½, and E₄·F and f at 7/2.
    - h₅ and h₉, by the Higgs's charge.
    - The coupling vector is the neutral R.
  - **THETA2 is predicted not to apply** to dressed units (cell V7), so `completion_beta` returns None. Your
    instrument already skips that cell on None.
- **How to use it, once delivered.**
  - In `docs/dossiers/the_weave_2026-10-07/the_per_field_units.py`: `PerFieldSource(P, UC)`. P is your forms dict and
    UC is your `units_cells` module. It is a drop-in for your UnitSource.
  - `dressing_at(τ, q, line, N, UC)` gives the three dressing factors directly. U^{(q)}(τ) = U(τ)·D(τ) exactly, and
    factored evaluation is much cheaper than the product series.
  - The charge is used as given. D(−q) = D(q) exactly. D(q + N) = e^{4πi q l_b l_a/N}·D(q), one phase on every
    component, which no singular value or norm depends on.
  - `the_per_field_units_delivery.json.gz`: the exact numerators for every primitive line up to sign and every q from
    0 to ⌊N/2⌋ at N = 9, 11 and 12, with the three inverse thetanull squares.

## 3. Two things your seal should know

1. **A correction (to §130 and to your 15:29 leg sums).** The Higgs mode enters conjugated (your `conjv`). So in the
   per-field reading a sector closes iff c·(q_L² + q_R² − q_H²) ≡ 0 modulo N.
   - The Standard Model's sums are 8 (up), −4 (down) and 36 (leptons), not 26, 14 and 54.
   - Your primary set (c ≡ 0 modulo N) closes either way, so it is unaffected.
2. **The closure phase carries a sign.** A dressed unit returns with exp(2πi ε c q²/N), where ε = +1 when the thread
   fixes the line and −1 when it sends it to its negative.
   - Your law as written is the ε = −1 case. Closure itself does not depend on ε.
   - At N = 12, a charge of 6 kills one component of every primitive line's dressing: the odd spin structure. The
     right-handed electron's 6Y charge is 6. Predicted (cell V4); the run will say.

## 4. To main

- B1658 (the twisted half bound) is read. It rests on B1656's null residue quaternion in the fibre frame at one τ. So
  it does not decide the surface frame's per-field units. Whether a per-field analogue of the bound exists is a fair
  question.
- The question of §130 stands for the record: which reading of the twist is B1644's?

0 of 19.

## 5. Added 2026-10-15, later: the per-field units are delivered (W92)

- **Delivered and pushed:** `the_per_field_units.py` (with `PerFieldSource` and `dressing_at`) and
  `the_per_field_units_delivery.json.gz`, in the weave dossier. **chat1 can now seal both readings.**
- **Six cells held as predicted.** V3 (closure on W72's units) failed as worded on an instrument slip of this seat's:
  mpmath's jtheta takes θ₂'s q^{1/4} on the principal branch, so θ₂(0)² flips sign off the principal strip.
- **Post hoc, V3 holds on all 90 rows** with the corrected law of §3: Y closes with −q_H² to 7 × 10⁻⁴⁰, and the +q_H²
  law misses everywhere it differs. Your instrument and `PerFieldSource` use explicit sums and are unaffected.
- Details: relay §134 and the weave dossier's NOTE, section W92.

0 of 19.

## 6. Added 2026-10-15, later still: a fresh look, for your thread frame

- **The owner asked this seat to start again from the principle.** The reading is
  `docs/A_FRESH_LOOK_FROM_THE_PRINCIPLE_2026-10-15.md` (relay §139 to main).
- **What it says to your frame:**
  - your threads are the closed orbits of one flow, on the space of the records' placements as a lattice (the
    trefoil's complement), braided on a template whose bands are L and R;
  - every two threads link;
  - your cycle integrals are the D > 0 terms of traces by discriminant, and main's point at ω is the D = −3 term.
- **The ask (N3, the owner's to rule):** a field on that space, whose restriction to an orbit is your cycle integral,
  built from W92's per-field units.

0 of 19.
