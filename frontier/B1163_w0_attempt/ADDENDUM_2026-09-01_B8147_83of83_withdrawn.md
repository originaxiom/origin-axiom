# ADDENDUM (2026-09-01, fresh physics seat; finding for the banking seat to re-verify) — `ADDENDUM_family_denominator_B8147.md`'s "83 of 83 CLOSED, spot-verified 5/5" is withdrawn; one of its three named witnesses is chiral

**Scope.** This note corrects `ADDENDUM_family_denominator_B8147.md` lines 14–15 ("CHECKED: 83
of 83 … spot-verified on this bench 5/5 by mirror-isometry, including o10_150700, t12840,
s955") and the "CLOSED" status it assigns. It extends the seat's earlier
`ADDENDUM_2026-09-01_amphichirality_instrument.md`, which withdrew rows of
`ADDENDUM_family_wide.md` but did not touch the B8147 file. Both original files are left
unedited, per house discipline. Nothing here is banked by this seat (role split: audit,
judge, propose).

**What is wrong.** The 5/5 spot-check used the same orientation-blind instrument
(`reverse_orientation()` + `is_isometric_to()`), which returns True on every manifold — it
returns True on known-chiral m015 and m016 (control in
`reports/fresh_physics_seat_2026-09-01/recompute/R24_b1163_chain/control.out`). The 83/83 and
the 5/5 could not have failed.

**Recomputed, orientation-aware (`symmetry_group().is_amphicheiral()`; CS via
`chern_simons()` mod ½; H₁), run twice — by Ring R3 cell R24 (`recompute/R24_b1163_chain/`) and
by the seat itself in its own session:**

| named witness | banked (B8147 addendum) | orientation-aware | CS mod ½ | H₁ |
|---|---|---|---|---|
| o10_150700 | spot-verified amphichiral | **False (chiral)** | 5/12 (≡ −1/12) | ℤ |
| t12840 | spot-verified amphichiral | True | 0 | ℤ+ℤ |
| s955 | spot-verified amphichiral | True | ¼ | ℤ/20+ℤ |

One of the three named witnesses is chiral. Under the corrected instrument the family count is
38 amphichiral / 74 chiral of B1186's 112 (25 at CS 0, 13 at CS ¼; every chiral member has CS
∉ {0, ¼}; 12·CS is integral throughout). "83 of 83, zero exceptions" is therefore not a
computed fact; the status **CLOSED reverts to open, with a negative answer** to the question
the addendum asked.

**What survives.** The B8147 addendum's own second statement — "core theorem untouched — the
mirror-parity argument never used the family" — is correct and is confirmed here: m004 is
amphichiral under the orientation-aware test, CS = 0 exactly; m003 True, CS = ¼. The B1163
headline (w0 is not constructed because m004 cannot supply an object-canonical orientation)
is not touched by this note. What falls is only the family-wide strengthening layer. The
residual claim "no sibling self-orients" is *not* re-established here: the Galois and
analytic legs never used amphichirality, so a family statement may be re-derivable from
them alone, but the banked argument via amphichirality is gone and a chiral sibling (m202,
s118, o10_150700 — the last is not a cover of m004 or m000, `docs/OPEN_LEADS.md` L193) is a
live counter-witness to "orientation is fixed identically for all".

Ledger: R3_REPORT D9, V17 (second downstream consumer of the V9 instrument). Error-class: E53
(propagation of a vacuous instrument's output as a theorem) on top of E27/E40.
