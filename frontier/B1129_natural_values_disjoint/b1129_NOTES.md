# P-NATURALVALUES — NOTES: the object's own invariants against the SM's numbers

**Probe cell of THE VALUE-PROBING WAVE, the "all around" leg.** Executed against the sealed
`PRECOMMIT.md` in this directory; comparison code `naturalvalues.py`; full machine output
`results.json` (23 invariants × 22 targets = 506 pairs, every pair scored).

## Headline verdict

> **NATURAL-VALUES-DISJOINT** (menu-wide), **+ one flagged, UNCLAIMED NAMED-CANDIDATE**
> (`|det φ| = 2/3` vs the Koide relation), relayed to cc3 per the owner's standing 3rd-opinion
> rule for any positive-looking artefact.

22 of 23 object-invariants show **zero** pairing above 2 significant figures against any of the
22 SM targets, across the full 506-pair grid — the object's own natural forms (a knot volume, a
Beilinson regulator, a genus residue, five tones, an E₆ structure-constant menu, a Kashaev
constant) are, like its tower periods (V-3/B1126), **disjoint from the Standard Model's
dimensionless numbers.** This is the sharper terminal negative the task anticipated: not just
"no period of the tower is an SM ratio" (V-3), but "no *natural, already-published, single-level*
invariant is one either" — closing the value question from a second, independent direction.

## The one exception, examined in full

`abs_det_phi` (=|det φ|=2/3, the magnitude of the exact determinant of B904's explicit E₆
isomorphism, computed over ℚ, "0 mismatches" on 3,003 basis pairs) lands **exactly** on
`Koide Q (=2/3 target)` (rel_diff = 0.0, to all 30 computed digits) and within **5 significant
figures** (9.23×10⁻⁶ relative, "0.9σ" in the loose sense — though see below on why that σ number
is not meaningful here) of `Koide Q_emp`, the ACTUAL empirical combination built from PDG
2024 electron/muon/tau masses (0.66666051...).

**Why this is named, not claimed — four independent grounds, all checked:**

1. **Fails strict pre-commitment, structurally.** Per the charter's rule 1 ("no scan-and-pick-
   closest") and this probe's own PRECOMMIT.md Part D: this pair was found by exhaustively
   comparing a frozen 23-row menu against a frozen 22-row target list, not named in advance.
   *Every* survivor of this scan is capped at NAMED-CANDIDATE by construction — this is true
   regardless of how striking the number looks, and it is the single most decisive reason this
   cannot be promoted on this run.
2. **No principled instrument exists.** A repo-wide search for co-occurrence of magic-square /
   Barton–Sudbery / E₆-structure-constant vocabulary with Koide / lepton-mass vocabulary returns
   nothing beyond this probe's own construction. There is no conceptual bridge between "the
   determinant of a 78×78 change-of-basis matrix between two presentations of the same Lie
   algebra" and "a combination of three measured charged-lepton masses" — no map, no shared
   physical or mathematical mechanism, nothing upstream connecting the two domains. This is
   exactly the "kind wall" the repo's own Gate 5 doctrine names (B811/B813): a value comparison
   without a typed object→SM functor is not evidence.
3. **Look-elsewhere is small in-grid but the TRUE reference class is much larger.** The in-grid
   look-elsewhere p-value (≈0.93%: the chance of a hit at least this close occurring somewhere
   in this specific 506-pair grid by pure chance) is smaller than V-3's own flagged near-miss
   (16.4%) — mechanically this pair reads as "more notable." **But the honest reference class is
   not this one grid.** The Koide relation is itself a 40+-year-old *unexplained* empirical
   near-coincidence in the Standard Model's own lepton sector (Q_emp ≈ 2/3 to 5-6 significant
   figures, with no accepted first-principles derivation) — meaning "something equals ≈2/3" is
   already a well-populated attractor that many unrelated constructions in physics and math have
   been compared against over decades, almost always coincidentally. The true look-elsewhere
   denominator is closer to "everything anyone has ever compared to 2/3," which is vastly larger
   than 506 — so even this pair's already-small in-grid p-value substantially *overstates* its
   significance.
4. **Structural 2,3-smoothness on BOTH sides, for unrelated reasons.** 16 of the 23 candidates
   in this menu are exact rationals (not irrational closed forms), and the ones with any
   denominator at all are all {2,3}-smooth (μ=−24=−2³·3, ν=−12=−2²·3, det φ=−2/3) — a direct,
   understood consequence of the object's own arithmetic (disc ℚ(√−3) = −3, and the small
   integer Cartan data of E₆'s Chevalley basis). Koide's 2/3 was independently chosen by
   Koide (1981) *because* it is an attractively simple fraction bounded in the relation's
   natural range [1/3, 1]. Two independent "simple-fraction attractors" colliding on the
   simplest nontrivial fraction with denominator 3 is a specific, nameable alternative
   explanation — not proof of coincidence, but a concrete competing hypothesis that has not
   been ruled out, and by Occam should be preferred absent an instrument.

**What would upgrade this** (named, not pursued here — out of this probe's scope): a principled
instrument reading Koide's Q from *some* independently-motivated feature of the E₆ magic-square
construction (not the bare determinant, which has no known role in charged-lepton mass
generation in this program), calibrated on independent data, run and reviewed by cc3. Absent
that, this stays exactly what V-3 kept its own near-miss as: a clean, falsifiable, unclaimed
note for the record.

## The full menu's other closest approaches (context, not hits)

The next-closest pairs after the det-φ/Koide pair sit at 1 significant figure or below — e.g.
`dim_27` (=27) vs `m_s/((m_u+m_d)/2)` (=27.33 ± 0.097 PDG) at 1.2% (a bare integer 27 landing
near a quark-mass ratio with a fairly coarse ~0.4% window — unremarkable, one of ~5 expected
2-sig-fig-or-worse hits in a grid this size); `C0_kashaev` (=0.75984) vs `sin(theta23_PMNS)`
(=0.74900 ± 0.009) at 1.4%; `dim_so8` (=28) vs the same quark ratio at 2.5%. None reach the
2-sig-fig floor. The full ranked list (top 30) and the complete 506-row table are in
`results.json`.

## Range check (task step 2)

22 of 23 invariants have |value| inside the SM targets' own magnitude span [0.000288, 137.04]
— a necessary, far-from-sufficient precondition satisfied almost universally here (dims like 78
and structure constants like −24 sit inside this span purely because 1/α_em(0) ≈ 137 sets a
generous upper bound, not because being "in range" carries any significance by itself). Only
`tone_0 = 0` is excluded (by construction: no SM target is exactly zero). Being in-range and
being NOISE simultaneously, for 21 of 23 invariants, is itself part of the disjointness finding:
proximity of *scale* does not translate into proximity of *value*.

## Relationship to V-3/B1126 (no double-counting)

Two of this menu's entries are the SAME real number as entries V-3 already scanned:
`m(A_41)` here is numerically identical to V-3's sealed `Vol/pi` candidate (both = Vol/π); this
probe's independent re-run reproduces V-3's NOISE finding for that value against all 22 targets,
confirming rather than adding new information. `C0_kashaev` (bare 3^(−1/4)) and bare `Vol` were
explicitly typed INELIGIBLE by V-3's own seal (single-level invariants were outside V-3's tower-
periods charter) — THIS probe is precisely the licensed place to test them, and both return
NOISE (closest: C0 vs PMNS θ₂₃ at 1.4%, 1 sig fig; Vol appears nowhere in the top 20 closest
pairs at all). Every other invariant here — L(χ₋₃,2) bare, L'(15a,0), h(ℚ(√−15)), the five
tones, and the entire M(𝕆,ℂ) dimension/structure-constant menu — is new territory V-3 never
touched. So this probe is a genuine extension, not a re-run, with one explicit reproduction
noted for transparency.

## What this closes, and what it does not

**CLOSES:** the question "do the object's own natural, already-published, single-level
invariants (as opposed to tower periods, V-3's territory) contain an SM number" — under the
frozen menu of section A, exhaustively, with one explicitly examined and dismissed-but-named
exception. Combined with V-3, this closes BOTH halves of "does the object's CURRENT arithmetic,
in either its periods or its natural forms, equal a Standard Model number" — the honest answer
to both is no, with the SAME shape of caveat both times (one flagged, unclaimed near-miss,
relayed to cc3, neither claimed as physical).

**DOES NOT CLOSE:** (i) deeper/other natural invariants not named in the charter's menu (this
probe was explicitly barred from "scanning outward" — a genuinely different invariant, e.g. from
a future arc, is untested); (ii) the possibility that `|det φ| = 2/3` reflects a real but
currently-unbuilt mechanism — named, not ruled out, and now on record for cc3 and for anyone
building a future E₆-structure-to-lepton-mass instrument; (iii) the P-INSTRUMENT probe's own
question (a constructed listener map, calibrated on one input, predicting the rest) — this probe
only ever compares raw, undressed values, by design, and a real instrument could in principle
read a coupling from any of these invariants in a way no raw-value scan could detect or rule out.

## Gate 5 / discipline compliance

No SM quantity entered any object-side computation (Part A of `naturalvalues.py` is fully
self-contained, computed before Part B is read, and the assertions at the top of the file check
every object-side number against an independently-banked cross-check before any comparison
runs). No fitted dressing constant was applied anywhere — every Part-A value is exactly the
closed form (or, for `L'(15a,0)`, the highest-precision literal) its source arc already reports.
The one signed/unsigned ambiguity (μ, ν, det φ) was resolved by a uniform, declared-in-advance
rule applied to all three, not selectively to the one that turned out to matter.
