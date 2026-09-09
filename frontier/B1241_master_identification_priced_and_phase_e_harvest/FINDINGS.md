# B1241 — THE MASTER IDENTIFICATION PRICED: the listener map u gets its register row (I-13) — and the fc R51/R52/Phase E harvest

**Date:** 2026-09-02 · **Seat:** cc (main) · **Source:** the physics-seat evaluation branch (fc) @ 37bcfed7 — R51, R52,
Phase E part 1 (71 seat judgments on the reader flags); every number recomputed here, every judgment re-read against
main · **Lead:** the identification discipline (B1231; Phase C of its plan, queued there and never run) · **Wall:** none
touched · **Verdict:** OPEN — the record/harvest class (as B1167/B1171/B1213/B1240): five register rows, one law-row
correction, three verdict-file overstatements repaired, two recomputations reproduced; no theorem claimed; Gate 5 untouched

## THE PRIZE FIRST

B1231 wrote it as a sentence and never as a row: **the listener map u — "this dimensionless structural analogue in
the object IS this physical quantity" — is an identification, the programme's master identification, and it has been
performed implicitly and for free since the first physics-flavoured cell.** The register opened on 2026-09-01 with
twelve rows and the master identification was not one of them. B532 (`i6_phase3_synthesis.py`, lines 51/74/100/105)
names "Born rule", "Gravity" and "TIME ARROW" for structural analogues; the arc's FINDINGS carry no fence; the fence
that exists is the owner's, in `docs/CLOSURE_2026-07-11.md:55–60` ("dimensionless structural analogues … the B398 gate
stays shut on any physics reading"). fc's Phase E flagged B532 as UNCAUGHT and cited the wrong fence
(B1017/B1164's price list) — the flag was right, the citation was not, and the correct disposition is stronger than a
fence: **a register row.**

**I-13 — structural analogue ≡ physical quantity (the listener map u) — UNEARNED.** What earns it is not a
computation inside the object; it is the crossing cell — u constructed from field data, never fitted, then a sealed
prediction compared (W5/W6, `main-goal-bridge-to-sm`). This row is the price of the programme's main goal stated in
the register's own currency, and it is the reason the input ledger's parameter count is a lower bound (B1231): every
physics reading of any cell in the corpus draws on I-13 until the crossing cell earns it.

Four more legacy identifications surfaced by fc's Phase E, each re-read on main: **I-14** (B305: the trinification
ℤ/3 ≡ the Eisenstein-unit ℤ/3 — B323 says the two are *distinct* and the crux "does L3 connect to L4?" is open;
UNEARNED, not "refuted downstream" as fc wrote), **I-15** (B715: the E₆(ℂ) Chern–Simons promotion ≡ 3d Euclidean
quantum gravity — a principal-sl₂ embedding with no dynamics exhibited; UNEARNED), **I-16** (B675: SU(4)₁ ≡ the
silver's stage — a conductor-8 / level-8 number match with uniqueness unshown; UNEARNED), **I-17** (B312: "one E₆,
three ADE hats" — B727 already proved the recurrence is FORCED by the ADE classification and only the atom ℚ(√−3) is
object-specific; REFUTED by the B1223 template). **The ratchet is raised by hand 5 → 9**, logged in
`docs/IDENTIFICATION_BASELINE.json` as the third dated raise; nothing was absorbed.

## 1. fc R51 — family amphichirality: independent convergence with B1235, and one row of ours that was wrong

fc's R51 recomputed the 112-family's chirality from scratch and reached B1235's split exactly — **38 amphichiral /
74 chiral**, B1181's 83/83 vacuous by the orientation-blind isometry call — without reading B1235 (their branch head
predates it). Two independent benches, one detector each, one answer. R51's residuals, all recomputed here
(`verification/r51_all_regular_subfamily.py`, `r51_all_regular_subfamily_output.txt`, REPRODUCE):

- the **all-regular subfamily** (every tetrahedron shape = ω = e^{iπ/3}): |A| = **77** of 112; **34 amphichiral / 43
  chiral** — so B1163's W0 leg ("the all-regular members are amphichiral") holds for 34, not 77; the non-regular 35
  split 4/31;
- the **metallic bundles** b++RᵐLᵐ, m = 1…6: all six amphicheiral, symmetry order 8, CS = 0 (to 10⁻¹⁶), H₁ = ℤ (m=1),
  ℤ/m ⊕ ℤ/m ⊕ ℤ (m ≥ 2); m = 1 is the figure-eight (Vol 2.029883…) — fc's R43 correction of the bundle rows confirmed;
- o10_150700 chiral with CS = −1/12 (B1235's table already carried it); sweep #1212 stands.

**The row of ours that was wrong.** B1235 wrote "its family-test law at LAW_MAP:263 stands". fc read the row and
said the amphichirality clause "should be withdrawn or re-derived". fc is right and B1235 was a miss — **mine**: the
second clause of THE ONE-WAY FAMILY TEST ("only HELP family-level claims … exactly how amphichirality strengthened to
83/83") is (a) illustrated by the very computation B1235 retracted as vacuous and (b) logically wrong for UNIVERSAL
family claims — enlarging 14 → 112 *hurt* "the family is amphichiral" (it went from 14/14 to 38/112). The one-way
asymmetry holds for existential claims ("some member has it") and for object-level claims; for universal claims
enlargement is one-way in the OTHER direction. Corrected in place at `docs/LAW_MAP.md:263` with a dated bracket, an
addendum on B1235, and an **E53 row of my own** (the correction reached B1181's verdict and B1235's FINDINGS on
2026-09-02 and did not reach the law that quoted the retracted number as its example).

## 2. fc R52 — B8070's anomaly cubic reproduced; the committed script prints the refuted computation

One generation Q, uᶜ, eᶜ, dᶜ, L with multiplicities 6, 3, 1, 3, 2; the three linear anomaly conditions cut the
hypercharge 5-space to the plane {yQ = −yL/3, ye = −2yL, yu = 2yL/3 − yd}; the cubic on it factors as
**−2·yL·(2yL+3yd)·(4yL−3yd)/3** — fc's R52 and B8070 l.84 agree, and so does this bench
(`verification/r52_anomaly_cubic.py`, sympy, REPRODUCES). The three anomaly-free lines: hypercharge (1,−4,6,2,−3),
the u↔d swap (1,2,6,−4,−3), the vector-like line yL = 0. fc's further finding stands as reported: **B8070's committed
script prints the computation its FINDINGS refute** (the commutator norms 2.83 / 12.73 / 86.27 that carry the
refutation are unscripted). B8070 lives only on cc3's `origin/paper/structure-genesis-first` (main cites it once, in
`docs/CLOUD_ALIAS_TABLE.md`) — a record point for cc3, relayed; nothing on main changes.

## 3. fc Phase E part 1 — 71 seat judgments read against main

fc's Phase E reads 2494 reader flags into four types (IDENTIFICATION_BY_TYPE 161, SELF_REFERENTIAL_LOCK 128,
CLAIM_EXCEEDS_COMPUTATION 65, FITTED_VALUE 36 — 390 flags over 369 arcs, 62 packets) and part 1 judges the first 71.
This is, from a different net, the Phase C sweep B1231's plan queued ("52 BARE candidates needing judgment") and
never ran. Every §A spine row and every §B record row was re-read on main (`verification/fc_phase_e_rows_verified.tsv`,
18 rows, one line each: fc's flag, fc's judgment, the status on main, the evidence by file:line, the earning path).

**§A — the SM-spine identifications (15 flagged UNCAUGHT).** Five become register rows (I-13…I-17 above). Three are
not what fc says: **B660 is SELF-CAUGHT** — its verdict reads "CONSISTENT-NOT-SELECTIVE, banked as PLACEMENT", the arc
refuses the identification itself; **B666 is not an identification** — "mode DECIDED by SL(2)-realizability" is
near-definitional once the mod-n shadows are computed in full (2T = SL(2,ℤ/3), 2I = SL(2,ℤ/5), 2O ≠ SL(2,ℤ/n) for
n ≤ 48, and the mod-8 shadow is *all* of SL(2,ℤ/8), order 384 — fc's "three data points" undercounts the mechanism);
**B650** is on the hearing side (the functor "EXISTS one level up" as B644's congruence-shadow theorem) and is left
NEEDS-JUDGMENT for that lane. Seven (B448, B449, B592, B665, B670, B779, B861) are recorded in the TSV as fc reported
them and not re-adjudicated here — they are not on the SM spine and Phase E part 2 is the place.

**§B — three verdict files that overstate their own prose (fc: STALE-VERDICT / LABEL-ONLY), all three confirmed and
repaired at the source arc** (the E53 rule: walk to the arc that minted the claim):
- **B232** `rho_n_plethysm` — verdict PROVED; its FINDINGS:3–4 say "the central *unproved* theorem … an honest
  **reduction** … **not** a proof", :38 "outcome (b) … (not a proof)". Verified exactly to n = 8 and on the real
  Jacobian to n = 5 — that is what stands. Verdict **PROVED → OPEN**, claim rewritten to the reduction + the finite
  check, addendum. (`tests/test_b232_plethysm_recursion.py` pins the recursion, not the verdict string — nothing else moves.)
- **B167** `conserved_no_scale_lemma` — claim reads as a closure ("cannot source an internal scale"); FINDINGS:3–8
  mark the premise POSTULATED and the argument "stated"; firewall-side, nothing promotes. `docs/COSMOLOGY_LEDGER.md:174`
  cites it as forbidding a scale. Claim now carries the qualifier; addendum. Verdict NEGATIVE unchanged.
- **B647** `core_mechanism` — claim_one_line "forces the ratio Y[023] = 24ζ₆·Y[123]"; Cell 1 line 14 of its own
  record: "the core ratio is **NOT forced** — residual ONE ℝ-linear condition" (constrained space real dim 6; the
  spectator law ⟺ arg Y[134] = π/6). Claim corrected to what the cell computed; addendum. Verdict PROVED unchanged (the
  reduction it proves is real; the word "forces" was the overstatement).

No prior addendum or correction existed for any of the three (ERROR_LEDGER, B1237–B1240 silent). These are E53 at
verdict-file grain (the B1237/B1238 shape, #13–#18): the arc's own body knew, the arc's verdict line did not.

## 4. What this arc does NOT do

- It does not earn anything. EARNED stays 4. The five new rows are priced debts (4) and one closed door (1).
- It does not adjudicate the 71 minus 18 rows fc judged outside the spine and record classes; part 2 is theirs.
- It does not touch B8070 (not on main), the hearing-lane B650, or any verdict of record other than B232's word.
- Gate 5: no measured value anywhere in this arc; the anomaly cubic is algebra over indeterminates.

## 5. Corrections of my own recorded here

1. B1235 "LAW_MAP:263 stands" — wrong (§1); E53 instance, mine, corrected at the law row, on B1235, in the ledger.
2. B1231 registered twelve rows and left the master identification as prose; it is now I-13 (§PRIZE).

## 6. Leads

**L199** — two computable earning paths surfaced by pricing: (a) I-16: the silver cusp lattice's discriminant form
against A₃'s (ℤ/4, q = 3/8) — a finite computation that decides whether the level-8 match is unique; (b) I-15: the
Dynkin index of the principal sl₂ ⊂ e₆ embedding, tying the E₆ CS invariant to Vol + i·CS with a computable
coefficient. Neither earns the row alone; each turns a name-match into a map or kills it.

## Files

`verification/r51_all_regular_subfamily.py` (+ `.json`, `_output.txt`) · `verification/r52_anomaly_cubic.py`
(+ `.json`, `_output.txt`) · `verification/fc_phase_e_rows_verified.tsv` · `verification/reproduce.sh` ·
`tests/test_b1241_master_identification_priced.py` · edits: `docs/IDENTIFICATION_LEDGER.md` (I-13…I-17),
`docs/IDENTIFICATION_BASELINE.json` (raise 5 → 9), `docs/LAW_MAP.md:263`, `docs/ERROR_LEDGER.md`,
`docs/OPEN_LEADS.md` (L199), B1235/B232/B167/B647 addenda and verdict files.
