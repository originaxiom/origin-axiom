# B1070 — RETRACTED. The rank descent was an artifact of my own script.

**Date:** 2026-08-17. **Verdict: REFUTED, in full.** Nothing banks. The seal's **fourth** declared
outcome is the one that fired: *"rank does not drop; §D survives contact with the anomaly layer;
L144 closes negative."* Recorded here with the mechanism of my error, per the corpus rule that a
true-conclusion-wrong-argument must never be buried.

## The claim I made

That anomaly cancellation carries `su(3)⊕su(2)⊕u(1)³` (Lie rank 6) to `su(3)⊕su(2)⊕u(1)_Y`
(Lie rank 4), escaping the §D rank obstruction, and reaching the SM signature (12, 11).

## Why it is false — four defects, all verified on this bench

1. **The headline was never computed.** The source line reads
   `print(f"  LIE RANK  6 -> 4  : {2+1+3} -> {2+1+1} ...")`. That is literal arithmetic on
   constants. **No Lie rank was calculated anywhere in the script.**
2. **The only quantity actually computed does not move.** Killing rank is **11 with one u(1) and
   11 with three**. The apparent descent `(14,11) → (12,11)` is `len(basis)` — a Python list
   length — i.e. a readout of the argument `n_u1` I passed in.
3. **The algebra was not the algebra.** The three "u(1)" generators do **not** commute with
   `su(3)⊕su(2)`: max ‖[U,X]‖ = **2.83, 12.73, 86.27**. It was never `su(3)⊕su(2)⊕u(1)³`. Its real
   span is **13**, not the printed 14.
4. **The controls were theatre.** C1 checked centralizer *dimension* ≥ 4 inside a rank-4 algebra —
   not rank, and not in `e₆`. C4 tested `anomaly_free()`, which the detector never consumes; the
   prereg required a wrong charge assignment to fail the signature test, and `sm_algebra(1)`
   returns (12,11) unconditionally. **By the seal's own words the detector was measuring nothing.**

## The deeper reason, which the corpus already had

**B971 ran this and closed it VACUOUS** (`frontier/B971_L132_vacuity/PRIOR_ART_ANOMALY.md`). On
the object's *actual* spectrum — the complete **27**, abelian direction left generic across the
whole 3-dimensional centre — every anomaly condition is **identically zero**: U(1)³, U(1)-grav,
[SU(3)]²U(1), [SU(2)]²U(1) all vanish. The solution space is **3-dimensional**. **The abelian
sector goes 3 → 3.** Over all 2047 non-empty sub-multiplet sets, exactly one is fully anomaly-free
and it is the whole 27. B971's controls (su(5)'s 10, su(3)'s 3) give nonzero cubics on the same
code path, so the vacuity is a property of the input, not a defect of the test.

**The 3 → 1 drop exists only over an imported chiral truncation** — the hardcoded `GEN` table.
B864 §4 explicitly declines to derive it. And the object has no operation that could perform it:
*"The object's operations are centralizers, holonomies and gradings. They act on the 27 and
decompose it. Nothing in the kit deletes from it."* B971 further shows **156 of 2047** truncations
each admit a unique anomaly-free direction — so **the selective power lives in the truncation, not
in the anomaly conditions**.

**And the escape was not new.** B992 (`CHANGELOG.md:1424–1427`, 2026-08-09) already identified the
cascade's rank excess as χ and ψ and matched it to B864's anomalous directions — *"the two
directions the cascade cannot shed are the two chiral matter forbids, reached from opposite
directions."* Eight days before this cell.

## The technical objection that would kill it even if the code were right

Anomaly cancellation is a consistency condition on a theory one has **already chosen to gauge**.
Gauge all three u(1)s and two are anomalous ⟹ the theory is inconsistent; it does not *flow* to
the anomaly-free subgroup. Under the corpus's own reading (ψ, χ are observer **dials**, never
gauged) the object still produces the rank-6 Levi and one merely annotates two Cartan directions
"not gauged." That is bookkeeping — and the programme has already ruled on the move at theorem
grade in the opposite direction: **"A global symmetry is not a gauge group"** (B490 T-NOGO-DGG;
B487). Accepting it here would apply the inverse standard to a positive result.

## What stands

- **§D's wording is narrow** — it does cover centralizers only. That observation survives and is
  worth a scope note. But the programme's operative bar is not §D alone; it is the five-way
  closure of `docs/THE_SM_VERDICT.md` plus the input audit (B994, B1000), and B963 proves the
  chirality and rank resources **compete**. Narrow wording, unbroken bar.
- **L144 closes NEGATIVE on this route.** B167's door-map gets the citation it has never had.
- B861/B862/B863 already reach a rank-4 `su(3)⊕su(2)⊕u(1)` with the ℤ₆ global form — **conditional
  on the same missing input**. Graded REPRODUCED, not DERIVED.

## The one thing this cell contributes: a scope note on B864's uniqueness

B864's "hypercharge is the **unique** gaugeable abelian direction" is uniqueness **inside the
chosen 3-plane** `span(Y, χ, ψ)`. Two facts, both re-derived here from scratch:

1. **The coefficient `a` of `Y` drops out identically.** The anomaly functionals are linear in
   `Q`, so `Q = aY + bχ + cψ` gives `a·A(Y) + b·A(χ) + c·A(ψ) = 0`, and `A(Y) = 0` is the textbook
   fact. **The computation therefore says nothing about `Y` at all** — it says `χ` and `ψ` are
   anomalous over the imported 15. `Y` is inserted as a basis vector and reported back.
2. **Drop the 3-plane and uniqueness fails.** Over the full 5-dimensional charge space on
   `(Q, uᶜ, eᶜ, dᶜ, L)`, the linear conditions cut to a 2-plane on which the cubic **factors into
   three lines** (verified with sympy on this bench):
   ```
   cubic = -2·yL·(2·yL + 3·yd)·(4·yL − 3·yd)/3
   ```
   - `2yL + 3yd = 0` — hypercharge
   - `4yL − 3yd = 0` — the u↔d-swapped assignment (Minahan–Ramond–Warner's second solution)
   - `yL = 0` — the vector-like direction

   **Three anomaly-free lines, not one.** B1070's own C4 grid enumerated all three families and
   reported "17 hits" without noticing that two of them are not hypercharge.

This is a **scope note, not a retraction** of B864: its result is correct as uniqueness within
`span(Y, χ, ψ)` over an imported chiral truncation. It should not be quoted as "anomaly
cancellation selects hypercharge."

## The error class, for the ledger

A headline printed rather than computed, wrapped in controls that tested adjacent quantities. This
is the ninth-instance pattern again — *the class error survives even when the class error is the
stated subject* — and it produced a **false positive** this time rather than a false negative.
Both directions are live failure modes; the instrument must be pointed at the claim itself, not
its neighbourhood.
