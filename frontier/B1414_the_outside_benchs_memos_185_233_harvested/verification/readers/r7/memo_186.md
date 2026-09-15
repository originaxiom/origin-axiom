# Reader r7 — Memo 186 (`memos/THE_TAILS_OF_A_FAMILY.md`)

## 1. HEADLINE

"**THE FENCE GOES FROM 7 COEFFICIENTS TO 52, ON FOUR KNOTS**, five tails identified in closed
form, and the false/genuine theta split turns up inside a single one-parameter family."
Date: 2026-09-09.

## 2. CLAIMS

1. Data-integrity: five determinant/filename mismatches identified — two `CJTwist.<p>` files
   have a "lost minus sign" (`CJTwist.1` is actually `K_{-1}=4_1`, `CJTwist.2` is actually
   `K_{-2}=6_1`); `5_2` (det 7) is **not** in the delivered set. Grade: measured fact (T1–T3
   controls PASSED).
2. Controls T1, T2, T3, T5, T6 all PASSED (T5 vs GM eq (24) for `3_1`, T6 vs GM eq (166) for
   `4_1`, n=1..12 exact). Grade: PASSED.
3. Tail fence extended from 7 (memo 184) to **52** certified coefficients (step-2 window), on
   **four** knots (unknot, `3_1`, `4_1`, `6_1`, `9_2` — five series total counting both ends).
   Grade: measured, matched not fitted.
4. Five distinct tail series identified in closed form: `1`, `±(q;q)_∞` (×2 ends), a genuine
   theta at `6_1`'s high end (Rogers–Ramanujan modulus, `= Σ(−1)^n q^{n(5n+3)/2}`), a false
   theta at `9_2`'s low end (modulus 16). Grade: PROVED/matched exactly.
5. **CELL 1 (is the stable end always `(q;q)_∞`?) → OUTCOME B** (no — `6_1` high end and `9_2`
   low end are not). Grade: OUTCOME B, measured (memo 184 had only argued this from
   Armond–Dasbach).
6. **CELL 2 (genuine vs false theta, by two independent signatures) → OUTCOME B** (both kinds
   occur): `6_1` high = genuine theta (periodic `a_n`, period 5); `9_2` low = false theta
   (aperiodic, `|a_n|` reaching 19 by n=45). Grade: OUTCOME B, two signatures agree.
7. Armond–Dasbach's "Andrews–Gordon-type series" prediction for `6_1` confirmed by name
   (Rogers–Ramanujan product). Grade: confirmed.
8. The false/genuine theta split (the one "memo 173 got backwards and memo 177 §1 now turns
   on") occurs **inside one one-parameter family** (`K_{-2}=6_1` genuine, `K_4=9_2` false),
   not between unrelated knots. Grade: new finding, not previously claimed elsewhere.
9. Explicitly does **not** reopen the `c_eff` route (Register R83 stands: `c_eff(1/(q;q)_∞^m)
   = m` is available to order). Grade: negative/scope statement.
10. Named follow-ups F186-1 (get `5_2`/`8_1`/`7_2`), F186-2 (measure the full family
    p=−14…15). Grade: not executed, named only.

## 3. CERTIFICATE

- `certificates/cj_table_ingest.py` — EXISTS.
- `certificates/tail_tables.py` — EXISTS.
- `outputs/cj_table_ingest_out.txt` — EXISTS; tail confirms "ALL DATA CHECKS: PASSED" and lists
  the exact filename/determinant mismatch table quoted in the memo verbatim.
- `outputs/tail_tables_out.txt` — EXISTS; tail matches the memo's §5 language almost verbatim
  ("Memo 184's fence was SEVEN stabilised coefficients. It is now FIFTY-TWO, on four knots…",
  and the false/genuine-inside-one-family finding, and the `c_eff` non-reopening statement).
  Both outputs agree with the memo's headline.
- **No seal** for this memo (not a preregistered A/B-cell memo; it is a data-ingest +
  measurement memo). No sha256 claim is made, so nothing to check here.

## 4. ON MAIN ALREADY?

- No `frontier/`, `docs/`, or `papers/` file (outside `outside_bench/`) mentions `CJTwist`,
  "colored jones tail", or `tail_tables` — grep across `frontier/ docs/ papers/` (excluding
  `outside_bench/`) returns **zero hits**. → **(c) NOT on main.** This is a pure outside-bench
  measurement that has not been harvested into a `frontier/B*` arc or cited in `docs/`.
- The memo's own "already-banked" check (its §0, run against `colored jones tail`, `twist
  knots`, `Rogers-Ramanujan product`, `false theta`, `genuine theta`, `Andrews-Gordon`) found
  only lexical collisions on unrelated arcs (`B944_dynamics_chirality_sweep`,
  `B1127_antilinear_completion`, `B1139_symmetry_point_table`, `B1093_route_a_arithmetic`) —
  consistent with my own finding of (c).
- Register R83 (the `c_eff` de-funding) is cited but not independently re-checked here since it
  is out of scope (claim 9 is a "does not reopen" statement, not a new claim).

## 5. NEEDS COMPUTATION HERE

- Claim 1/2 (data integrity, determinant identification): DOCUMENTARY in the sense that it is a
  one-time check against Garoufalidis–Sun's own tables, but is independently recomputable:
  a verifier should re-run `certificates/cj_table_ingest.py` (self-contained, python3+sympy) on
  the same vendored `data/cj_tails.json` prefixes and confirm `det(K_p)=4p−1`/`4p+1` recovers
  the filename→knot map. Cheap (<1 min).
- Claim 3/4 (52-coefficient fence, five closed forms): recompute `certificates/tail_tables.py`
  and confirm the two-signature theta/false-theta test (periodic vs aperiodic exponents in
  `Φ = Π(1−q^n)^{a_n}`) independently — this is the single discriminating fact. Expected: exact
  reproduction of the printed series and their supports (e.g. `6_1` support
  `0,1,4,7,13,18,27,34,46,55`).
- Claim 8 (false/genuine split inside one family): NEEDS COMPUTATION — this is exactly memo
  186's own named follow-up F186-2 ("measure the whole family p=−14…15... `tail_tables.py
  --from-tables <files>` already does it"). A verifier should run that flag over the fuller
  family once the additional `CJTwist` files (F186-1) are fetched, and check whether the
  false/genuine split is a clean function of `sign(p)` or something more granular.
- Claim 9 (c_eff non-reopening): DOCUMENTARY (a scope disclaimer, not a computation).

## 6. SUPERSESSION

- Not superseded by any later INDEX.md row I found (no later memo number references "memo 186"
  as withdrawn). Memo 187 (`THE_ERRATUM_LOCALISED`, INDEX row 284) explicitly builds on memo 186
  ("the same lost minus sign as memo 186's tables") without contradicting it — it is a
  continuation, not a retraction.
- Memo 185's addenda (INDEX row 282, `THE_CYCLOTOMIC_ROUTE_IS_CLOSED`) reference memo 186's four
  tables directly ("Habiro's C_m solved triangularly out of memo 186's four tables (round-trip
  verified...)") — this is a downstream *use* of memo 186's data, further corroborating rather
  than superseding it.
- No arc on main contradicts or supersedes it (there is no arc on main addressing this subject
  at all — see §4).

## 7. GRADE PROPOSAL

**REPRODUCE-AND-BANK.** This is a clean, exact (matched-not-fitted), controlled measurement
with no seal-cell apparatus needed because the claims are enumerable facts (determinant
identification, closed-form coefficient matches) rather than preregistered binary outcomes; it
sits entirely outside the frontier/ arc system and its central discriminating facts (the
five-tail identification, the false/genuine split inside one family) are cheap and worth an
independent verifier's arc row — plus its own named follow-up F186-2 is a ready-made next
computation.
