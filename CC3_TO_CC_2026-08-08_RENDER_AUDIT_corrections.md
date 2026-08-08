# CC3 → CC — HANDOFF: what the render audit found that needs correcting

cc3 audit seat, 2026-08-08. The owner (filmmaker seat) asked for a visual
anatomy of the object. Rendering it turned into an audit: three defects
surfaced that weeks of *computing* had not surfaced, two of them in code
whose outputs are already banked on main. All three verified on this seat
independently of the render agents that reported them (I did not take
their word; the checks are reproduced below and committed).

Artifacts: frontier/B796_coupling_campaign/anatomy/ (plates A–I,
ATLAS.md, SHOOTING_NOTES.md, all scripts). Branch pushed.

---

## C1 — DOCSTRING OVERCLAIM in hejhal_m004.build_moves()
**Severity: low (no result affected). Action: fix the docstring.**

`build_moves(maxlen=5, cmax=2.2)` documents itself as returning the
group elements with |c| ≤ 2.2. It does not — it returns those reachable
by words of length ≤ 5, which is a proper subset:

    words ≤ 5 :  91 moves      (by |c|²: {1: 35, 3: 24, 4: 32})
    words ≤ 6 : 143 moves      ({1: 47, 3: 42, 4: 54})
    words ≤ 7 : 207 moves      ({1: 61, 3: 66, 4: 80})

The render agent found it while cross-checking snappy's horoball centres
against the group's cusp points (it recovers 8 of the 12 norm-4 cusp
points at |w| ≤ 5, all 12 at |w| ≤ 6).

**Bounded on this seat — no downstream impact.** The moves are used for
exactly one thing: steepest-ascent pullback. I re-ran the pullback with
the ≤5 and ≤7 sets over 120 sample points at Y = 0.75:

    points whose reduced height differs : 0
    max |t*(≤5) − t*(≤7)|               : 0.00e+00   (bit-identical)

Geometric reason: ascent only needs *a* height-raising element; the extra
116 are alternative routes to the same maximum. **Every banked eigenvalue
(B792/B797/B878, and my λ₂ 25-digit value) is unaffected.** The fix is one
docstring line — "words of length ≤ maxlen with 0 < |c| ≤ cmax; NOT a
complete list of such elements" — plus, if you want it, a note in B878's
harvest that the solver's move set is truncation-bounded by design.

---

## C2 — GLOBAL-PHASE CONTAMINATION in every reconstructed eigenfunction
**Severity: medium for anything that USES eigenfunctions pointwise.
Action: pin the phase in the shared helper; re-check two banked results.**

The collocation eigenvector comes out of an SVD, which fixes it only up to
an arbitrary global phase e^{iθ}. Nothing in the pipeline pins θ. Measured
(the phase that would make a₋μ = conj(aμ), i.e. the object's own real
form):

    λ₁ = 16.5151 :  θ = +40.20°     Re-contamination ≈ 34%
    λ₂ = 25.0108 :  θ = +148.92°    Re-contamination ≈ 96%
    parent 51.01 :  θ = −26.55°     Re-contamination ≈ 23%

So `Re f` as computed is an arbitrary rotation inside the eigenspace, not
the canonical real eigenfunction. Mathematically both Re f and Im f solve
Δf = λf, so nothing is *false* — but the quantity is **not reproducible**
(a re-run gives a different rotation) and any pointwise use of Re/Im
separately is meaningless without the pin.

Fix (one line, verified): compute θ from the conjugate-pair ratios and
multiply by e^{−iθ/2}. After pinning, residual |a₋μ/conj(aμ) − 1| falls to
5.8e−06 … 7.2e−05 and |Im f|/|Re f| ≤ 2.9e−06 across all four modes.

**What to re-check on main, and what is safe:**
- SAFE — everything phase-invariant, which is most of what is banked:
  σ_min dips and refinements (the eigenvalues themselves), |a|-based
  quantities, the S-invariance old/new test (a ratio of the same function
  at two points), the sector-projection test (a generalized eigenproblem
  in the eigenspace), the mode-count certification, the SM/PSLQ work.
- WORTH A LOOK — anything that took a real part or compared two
  eigenfunctions' pointwise values: I could not find such a use on main,
  but B878's harvested `branch_cell9_rung1_v2.py` and any future
  spinor/Dirac extension (B804) would hit it immediately. Flagging before
  it bites.
- MY OWN DELIVERABLE was affected: the first Plate A rendered λ₂ as ~96%
  its imaginary part. Corrected and re-rendered as
  `plate_A_modes_canonical.png`; the original is retained in-arc as the
  record of the defect, labelled.

---

## C3 — A TOLERANCE ERROR IN A FINDING (in the finding's own favour)
**Severity: nil for the repo, but it is an E-class instance worth a row.**

The Plate-E agent reported "36 distinct horoball radii, all exactly
1/(2N) with N an Eisenstein norm" and asserted it in code — then its own
assertion flagged three exceptions (97, 91, 84). The exceptions were its
1e−9 tolerance against snappy's ~1e−8 float output: 97.000000005 *is* 97,
and 97 = 11² − 11·3 + 3² is an Eisenstein norm. At 1e−6:

    all 36 distinct radii = 1/(2N), N an Eisenstein norm : TRUE, 0 exceptions

The finding stands and is, I think, genuinely pretty: **the arithmetic of
ℚ(√−3) is visible as the sizes of the spheres in the cusp packing.** The
instance worth recording is the shape — *a correct result partially
self-refuted by a numerical tolerance chosen tighter than the data's own
precision* — which is close to E31 (instrument precondition unchecked)
but pointed at the assertion rather than the instrument. Your call whether
it is an E31 instance or its own class.

---

## C4 — SCOPE DEVIATION IN A DELIVERED PLATE (mine to own)
**Action: rename, and one plate still owed.**

The campaign's fifth agent stalled mid-stream and returned a plate that is
not the one I briefed. I asked for the **being/hearing wall** (the B736
Sylvester no-go: disjoint spectra ⇒ T = 0). It delivered instead a
rendering of the **SM null** — the 41 near-hits against 500 surrogate
spectra (median 40; the object at the 51st percentile), the per-target
surrogate probabilities, the three-test ledger, the sealed prereg hash,
and B727's structural wall.

I verified its numbers against our own sealed run: 2 + 39 = 41 candidates,
0 gated; p = 0.994 / 0.962 / 0.856 / 0.526 / 0.242 on the five near-hit
targets; PSLQ null rate 0.00. **All correct.** It is, in my view, the most
honest image in the atlas — it shows the object sitting at the 51st
percentile of noise. But it is mislabelled: it is currently `plate_I_wall`
and its title says THE WALL.

Ask: accept it as **PLATE J — THE NULL** (renamed), and treat **PLATE I —
THE WALL (B736)** as still owed. I can render the real one on a GO; it is
cheap (two lattices plus the unit-circle separation of the being and
hearing spectra) and it is the programme's sharpest *positive* no-go,
which the atlas currently lacks.

---

## THE PROCESS POINT

Two of these (C1, C2) were latent in code that had already produced banked
results and had passed three §16 review passes, a shakedown, and 58 hours
of certified computation. Neither surfaced while we were computing,
because a number that is off by a phase still looks like a number, and a
truncated-but-sufficient move set produces exactly the right answer. Both
surfaced within an hour of somebody trying to *draw* the output.

Proposal, one line, cheap to adopt: **for any arc whose product is a field,
a spectrum, or a set of points, render it once before banking.** Not for
presentation — as a check. It is the only instrument we have that fails
loudly on defects the numerics absorb silently. (It also produced the one
new observation of the day, C3's horoball–Eisenstein relation, which no
computation on this branch had asked for.)

## STATE

λ₂ delivered and banked (25 certified digits; PSLQ clean). The parent run
is in P3, ~a day out; its mode joins Plate A as a fifth panel on landing.
The D2/D5 relays and the loss-audit report are with you. My queue after
the parent: the combined PSLQ, and Plate I proper on your GO.

— cc3
