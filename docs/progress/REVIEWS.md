# The decadal repo reviews — ledger (GOVERNANCE §11)

Every ~10 merges on `main`, a whole-repo review fires: full suite + all gates +
atlas regeneration + a claims-vs-frontier promotion-candidacy sweep + a framing sweep +
a stale-leads check, ending in a dated report appended here. The gates surface DUE
status automatically (`python3 scripts/gates/gates.py review-due`).

Protocol per review: (1) suite green; (2) gates green; (3) atlas regenerated and fresh;
(4) sweep `frontier/` FINDINGS for entries that meet the GOVERNANCE §5 promotion bars
and list the candidates (promotion itself happens only through the §5 gates, logged);
(5) sweep for framing drift and stale `OPEN_LEADS` rows; (6) append the report below
with a new anchor-commit.

---

## Review 0 — 2026-07-03 (baseline; the reform itself)

anchor-commit: 7d8786d0dcf7e0e332a53e26815f55a954208447

The instituting review. Gates implemented and green (7/7); suite lock added; the
promotion-audit lane registered (see `docs/OPEN_LEADS.md`); ledger sections extended
with **Certified data**. Next review due after 10 merges from this anchor.

---

## Review 1 — 2026-07-03 (the first scheduled decadal review; merges 1–10 from Review 0)

anchor-commit: ffc94bc5ef8b594bff881d8883fd5d49007c8a18

1. **Suite:** green at the gating run for this review's PR (recorded in the PR body).
2. **Gates:** 7/7 green, including the append-only gate on its new roll-up path (amended this
   review to recognize the GOVERNANCE §9 quarterly roll-up; removed prefix verified verbatim in
   `docs/progress/PROGRESS_2026-Q2.md`).
3. **Atlas:** fresh at 353 probes (regenerated with B372).
4. **Promotion-candidacy sweep:** trivially current — the §5.1 audit executed inside this review
   window (61 entries: P17–P55, C6–C12, E1–E15; 6 holds), and the two post-audit probes promoted
   at banking (B371 → P56/P57; B372 → E16). No unadjudicated candidates outstanding. The named
   future pass: exact-core extraction for the held dps-100 quartet (B352/B353/B357/B370).
5. **Framing/stale-leads:** framing gate green repo-wide; OPEN_LEADS rows current (W2.7 closed by
   B372 with the null-refutation recorded; W2.10 executed; W2.11 and the conductor-structure lead
   registered; L51 DORMANT per owner directive).
6. **Window highlights (merges 1–10):** B370 both legs (order-3 integrability; the τ-defect
   θ-grading); the promotion audit executed; the document map + toolbox; B371 (the minimal
   two-state sector, P56/P57); B372 (the seam persists at level 45 — the home grows; E16).
   Ledger now: 57 proven · 12 conditional · 16 certified-data · 9 open · 10 dead.

Next review due ~10 merges from this anchor.

---

## Review 2 — 2026-07-04 (merges 11–25 from Review 1; the counter hit 15 during the overnight arc)

anchor-commit: 4cc43e448616a0c134b82d6154ae8c5b299ef76a

1. **Suite:** green at this review's gating run (recorded in the PR body).
2. **Gates:** 7/7 green.
3. **Atlas:** fresh at 360 probes.
4. **Promotion-candidacy sweep:** the steady state is working — every post-audit probe promoted
   at banking (P56–P61, E16–E17) or correctly held: **B377's v2 existence law is promotion-GATED
   on the in-flight acceptance duel** (375 passed; 405/675 pending) — the gate is the discipline,
   not a backlog. The dps-quartet's exact-core extraction pass remains the named future item.
5. **Framing/stale-leads:** framing gate green repo-wide. OPEN_LEADS current (W2.11 carries the
   P60/P61 progress; the priced-doors and Recognition campaign rows current; L51 DORMANT).
6. **Window highlights (merges 11–25):** the priced-doors campaign registered and run (the
   tower arc B372–B374: five rungs, two phase laws killed by registered kills); the recognition
   hit (P59 — the quantized golden cat map); the Derivation Campaign opened (D0 confirmed, the
   v2 law derived from the complete local table); the selection-rule reduction (P60 — a table
   became one number); the Galois covariance laws (P61). Ledger now: **61 proven · 12
   conditional · 17 certified-data**. Three-seat verification ran in both directions, with
   wrong-object errors caught on BOTH sides (the verifier's row/column error included — recorded).

Next review due ~10 merges from this anchor.

---

# Review 3 — 2026-07-04 (merges #472–#482, the autonomous-mode window)

anchor-commit: `a4c0c06f40ba94df5564a19d55d314dd06e2ecc7`

**Scope.** PRs #475–#482: P62 (twist isolation), B382 legs 1–4 (the why-1/12 program), B383
(row-16 theorem), the acceptance-duel banking wave (P63–P65 promotions in flight this PR).

**Claims hygiene.** Three promotions this window (P63/P64/P65) — each carries prereg-first
provenance, exact verification, and locks; the CLAIMS header's stale "fifteen proven" line
fixed; append-only respected (corrections in place with markers, none needed this window).

**Verification depth.** B382's canonical cross-check was REGISTERED before running (the
strongest pattern of the window — prediction: linear part (0,0); passed on all five words).
The duel's 405 stall was diagnosed to a real engineering trap (primes ≡ 1 mod 13500 lack ζ₈₁;
silent floor-division corruption) — fixed, and the fix is itself documented in FINDINGS. The
Kashaev T1 integrality assumption was WRONG (values are not rational at general N) — caught by
the exact machinery's own assert, corrected to Galois-component extraction; the correction is
the finding.

**Debt.** (i) B384 T2/T3 pending (registered); (ii) the CRT closed form of the −1/16 phase sum
(named residue of P64); (iii) D3(a) bright/dark criterion still open; (iv) the mirror's
non-Galois mechanism and the (2,3) stabilizer — both named in OPEN_LEADS; (v) suite flake
policy unchanged (one rerun, then targeted-gate documentation).

**Verdict.** Discipline held under autonomous mode: every bank prereg'd, two kills banked as
findings, one trap documented. The promotion cadence (3 in one window) reflects the campaign
reaching its derivation targets, not bar drift — each promotion's evidence is a registered
prediction that passed.
