# Reader r6 — memo 190 (outside_bench/memos/THE_BLOCKER_IS_BROKEN.md)

## 1. HEADLINE
"MEMO 183 ADDENDUM 4's BLOCKER IS BROKEN: f₆, f₇, f₈, … for m(5₂), by Park's inverted Habiro
route, with every step checked against something this bench already owned." Dated 2026-09-09.
ADDENDUM 1 (same date): "the route now runs on the whole twist family" (GS06's C-polynomial
implemented for every twist p).

## 2. CLAIMS
1. Memo 183 addendum 4's single-index-fit blocker past f_5 is real (context, not re-asserted here).
2. Park's recursion (Conjecture 2, arXiv:2106.03942) derived from his Ĉ and controlled 4 ways
   (C1–C4 all PASSED) — grade: CONTROLLED, not independently proved (Conjecture 2 is explicitly
   a conjecture).
3. CELL → OUTCOME A: all six Verma-trace blocks f_0..f_5 (224 coefficients total) reproduced
   exactly by the route — grade: OUTCOME A (verified reproduction).
4. f_6, f_7, f_8 computed and printed, banked in `data/f52_blocks_beyond.json` — grade: COMPUTED,
   explicitly labelled NOT A THEOREM ("blocks past f_5 rest on [Conjecture 2] … are not theorems").
5. ADDENDUM 1: GS06 Definition 1.3 operator implemented for every integer p; C1–C4 controls
   (p=+2, p=+1, p=−1, and 51-check annihilation test on 5 knots/2 sources) all PASSED — grade:
   VERIFIED (operator level), with explicit non-claim that the per-knot boundary ansatz fixing
   a_{-1} is untested.
6. R83's fence on the c_eff route is explicitly stated as UNCHANGED by having more blocks.

## 3. CERTIFICATE
- `certificates/f52_beyond_f5.py` exists; `certificates/gs06_twist_family.py` exists (both in
  `outside_bench/certificates/`).
- Outputs exist: `outputs/f52_beyond_f5_out.txt`, and `outputs/gs06_twist_family_out.txt` is
  referenced by the memo (not independently re-verified for existence beyond the primary file,
  which was confirmed).
- Output's final block matches the memo's headline verbatim: the tail of
  `f52_beyond_f5_out.txt` reads "CELL -> A : the route reproduces every block the Verma trace
  could reach PASSED" and restates the "not a theorem" caveat almost word for word — AGREES.
- No seal for this memo (Gate 5 exact-arithmetic memo; no seal file is named or required).

## 4. ON MAIN ALREADY?
- (c) NOT ON MAIN. Grepped `frontier/`, `docs/`, `papers/` for `f52_beyond_f5`, `F190-1`,
  `memo 190`, `GS06`, `Park's inverted`, `gs06_twist_family` — zero hits anywhere outside
  `outside_bench/`. This is pure exploratory colored-Jones/Habiro-series computation that has not
  been harvested into any frontier/B-arc, docs claim, or paper citation. It sits entirely inside
  the outside-bench lane (`outside_bench/memos`, `outside_bench/certificates`,
  `outside_bench/data/f52_blocks_beyond.json`).
- The referenced predecessor memos (183, 185) and successor use (memo 177's ceiling question,
  memos 184/186) are themselves outside-bench memo numbers, not B-arcs — no independent check
  possible against `frontier/`.

## 5. NEEDS COMPUTATION HERE
- Claim 3 (f_0..f_5 reproduction): DISCRIMINATING FACT — re-run
  `outside_bench/certificates/f52_beyond_f5.py` fresh (self-contained, `__file__`-relative,
  python3 + sympy per the outside-bench convention) and diff its printed f_0..f_5 series against
  the 224 coefficients quoted in the memo table (§4). Expected: byte-identical MATCH on all six
  blocks, since this is claimed as OUTCOME A (a computation, not a judgement call).
- Claim 5 (GS06 operator controls): re-run `gs06_twist_family.py`'s C4 (the 51-check annihilation
  test) — recompute the Habiro coefficients for 3₁, 4₁, 6₁, 9₂ (from Garoufalidis–Sun tables) and
  5₂ (from the bench's own R-matrix state sum) independently and confirm the GS06 recursion
  annihilates all 51. Expected: 51/51 PASS, per the memo.
- Claim 4 (f_6..f_8): DOCUMENTARY relative to theorem status (explicitly non-theorem), but the
  arithmetic itself is a discriminating fact — recompute f_6 from the recursion and diff against
  the printed series in §5 of the memo.

## 6. SUPERSESSION
No later outside-bench memo (191–233 scanned via INDEX.md and full-text grep for "memo 190",
"f52_beyond_f5", "F190-1") revisits or withdraws this memo. Not superseded by anything on main
either, since it never landed on main. Stands as written, with its own explicit "not closed"
label on Conjecture 2 intact.

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK** (partial) — the OUTCOME-A reproduction of f_0..f_5 (224 coefficients,
zero disagreement) is a clean, cheap, discriminating computation worth a frontier arc row citing
Park (arXiv:2106.03942) and Garoufalidis–Sun (math/0504305) as sources; the f_6..f_8 extension and
Conjecture-2 dependence should be banked explicitly as CONJECTURE-DEPENDENT, not upgraded, since
the memo itself refuses to call it a theorem and no downstream frontier arc exists yet to inherit
the caveat.
