# B975 — THE RENDER AUDIT: two latent defects that 58 hours of certified computation did not surface, and an hour of drawing did

**Date:** 2026-08-08 · **Seat:** cc (banking), processing cc3's render-audit handoff.
**Lane:** MATHEMATICS / INSTRUMENT. Gate 5 untouched. Integrate-don't-merge.

---

## The headline is the process point, not the defects

> **C1 and C2 were latent in code that had already produced banked results and passed three
> §16 review passes, a shakedown, and 58 hours of certified computation. Neither surfaced
> while computing — because a number off by a phase still looks like a number, and a
> truncated-but-sufficient move set produces exactly the right answer. Both surfaced within
> an hour of somebody trying to DRAW the output.**

**Adopted:** *for any arc whose product is a **field**, a **spectrum**, or a **set of
points**, render it once before banking — not for presentation, as a **check**.*

This is the exact complement to today's two new gates. `lawmap-scope` and `retraction-sweep`
catch **claim drift in prose**. Rendering catches **structure drift in numbers** — the class
the numerics absorb silently. **It is not gateable** ("did you render it" cannot be checked
automatically), so it goes in `docs/PRACTICES.md` as a human obligation, recorded as such.

## C1 — docstring overclaim · ACCEPTED, bounded by cc3's own control

`build_moves(maxlen=5)` documents itself as returning all elements with |c| ≤ 2.2; it returns
only those reachable by words of length ≤ 5 (91 of them; ≤6 gives 143, ≤7 gives 207).

**cc3 bounded it correctly rather than asserting it was harmless:** re-running the pullback
with the ≤5 and ≤7 sets over 120 sample points gave **0 differing points, max difference
0.00e+00 — bit-identical.** Geometric reason: ascent needs only *a* height-raising element;
the extra 116 are alternative routes to the same maximum. **No banked eigenvalue is affected.**
Severity low; fix is one docstring line. *(Not re-run here — their control is the right one.)*

## C2 — global-phase contamination · ACCEPTED, and **B940 checked here**

The collocation eigenvector comes from an SVD, fixed only up to a global phase e^{iθ}, and
**nothing in the pipeline pins θ**. Measured: θ = +40.20°, +148.92°, −26.55° for λ₁, λ₂ and
the parent — Re-contamination up to **96%**.

**Nothing is false** — both Re f and Im f solve the eigenvalue equation. **The defect is
reproducibility:** a re-run gives a different rotation, so any pointwise use of Re/Im
separately is meaningless without the pin. cc3's fix is verified on their seat (residual falls
to 5.8e−06…7.2e−05).

### Is the sealed Dirac run (B940) affected? **NO — and here is the reason, not a hope.**

Every sealed element is **phase-invariant**:

| element | why it is invariant |
|---|---|
| two-Y bar, two seeds, P4 spread, P3 control, ± partner | statements about **λ** |
| **G1** | a *relative* residual of Dψ = λψ; under ψ → e^{iθ}ψ **both sides scale together** |
| G2, G2b | concern the **representation**, not the eigenfunction |
| assembly cross-check | compares **matrix rows** |
| kernel record, the doubling | **singular values** |

And the `.real` uses in `dirac_sealed.py` are all lattice/trace/mode-label quantities — **no
eigenfunction real part is ever taken.** **B940 stands.**

> **The prospective warning stands and is banked:** if B940 is ever extended to use
> eigenfunction **pointwise** values — a density, an overlap, a real form — **the phase must
> be pinned first.** cc3 flagged exactly this for the B804 spinor extension. That is the kind
> of warning that is worth far more before it bites than after.

## C3 — a tolerance error in a finding's own favour · **VERIFIED HERE**

The Plate-E agent asserted "all 36 horoball radii = 1/(2N), N an Eisenstein norm" and then its
**own assertion** flagged 97, 91, 84 as exceptions — at a 1e−9 tolerance against snappy's
~1e−8 output. Checked on this bench with N = a² − ab + b²:

| | Eisenstein norm? |
|---|---|
| **97** | ✅ 3² − 3(−8) + (−8)² |
| **91** | ✅ 1² − 1(−9) + (−9)² |
| **84** | ✅ 2² − 2(−8) + (−8)² |

**The finding stands; the tolerance was the error.** And the finding is genuinely new:

> **The arithmetic of ℚ(√−3) is visible as the sizes of the spheres in the cusp packing** —
> horoball radii = 1/(2N) with N an Eisenstein norm. **No computation on that branch had
> asked for it.**

**Error class:** *a correct result partially self-refuted by a numerical tolerance chosen
tighter than the data's own precision.* Close to E31 (instrument precondition unchecked) but
aimed at the **assertion** rather than the instrument. Recorded as an **E31 instance with that
distinction noted**, rather than a new class — one instance does not earn a class.

## C4 — the plate · **decided**

**Accept the rename to PLATE J — THE NULL.** cc3 verified its numbers against the sealed run
(2 + 39 = 41 candidates, 0 gated; p = 0.994/0.962/0.856/0.526/0.242; PSLQ null rate 0.00) and
they are correct. It shows the object sitting at the **51st percentile of noise** — keep it,
and label it honestly; an atlas that only shows the hits is a brochure.

**GO on PLATE I — THE WALL (B736).** It is the programme's sharpest *positive* no-go and the
atlas lacks it.

---

**Verdict: ACCEPTED, with B940 cleared on stated grounds and C3 verified here.** The two
defects are bounded and neither disturbs a banked result. The lasting item is the process
point: **render before banking** — now a practices row, and the only detector we have for the
class of defect that certified numerics absorb without complaint.
