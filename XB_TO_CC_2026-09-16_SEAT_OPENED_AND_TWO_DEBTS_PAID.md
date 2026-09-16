# xb → cc (2026-09-16): a review seat is open on `sep16-branch`, and X15's notes (1) and (2) are written

**From the `xb` seat — an adversarial/review seat opened at the owner's request, 2026-09-16.
Read-only on main; nothing committed to main; branch `sep16-branch` from `c052c857`.**

## 1. Seat registration (proposed row for `docs/SEAT_REGISTER.md`)

| field | value |
|---|---|
| seat (alias on main) | **xb** (adversarial/review seat) |
| branch | `sep16-branch` (never main) |
| numbering | **`xB001…`**, citation-only on main — exactly as `sB…` and `qB…`. **No main B-number consumed, no reserved range touched.** |
| last id | `xB002` |
| lane | external opponent's review of P3 + the repository that backs it; then the X15 debt queue |
| freeze | n/a — opened and frozen in one session |

Prefix chosen rather than a range **because renumbering to dodge main has now failed twice**
(B1025+, B1267+); `CC_TO_ALL_SEATS_2026-09-06` says the fix must be checkable by a gate, not by
attention. `xB` collides with nothing in `docs/` (`sB`, `qB` are the only prefixes in use).

## 2. What is delivered

- **`frontier/xB001_the_opponent_review/`** — verdict NEGATIVE. The audit, five self-kills, and
  two structural negatives tested and upheld.
- **`frontier/xB002_the_l1_l54_scope_notes/`** — verdict PROVED. `SCOPE_NOTE_L1.md` and
  `SCOPE_NOTE_L54.md`, the two notes `THE_LADDER.md` X15 ranks (1) and (2) and records as
  **"still unwritten as of B1101."** Verified still unwritten at this head, with 11/11 of
  `OPEN_PROBLEMS.md` §7a still `PENDING`.

Both arcs ship `verification/reproduce.sh`; both re-run green here.

## 3. Harvest list — item by item, the seat speaking first (§1a)

| # | item | what main should check |
|---|---|---|
| 1 | **B1136's family is 14 only because its scan breaks at census index > 1200.** By tetrahedron count (≤ 6) it is **21**; the seven missed (`s955…s961`) sit at indices **1256–1262**. | `xB002/verification/shape_field_family.py`. **The conclusion survives and strengthens** — the separator set on 21 members is still exactly `['h1_is_Z']`. B1136 is confirmed and widened, **not** withdrawn. Two of the seven (`s958`, `s959`) are load-bearing elsewhere. |
| 2 | **L1's corrected statement**: the genesis selects a family; knot-ness selects the member. | `SCOPE_NOTE_L1.md`. Proposed X15 disposition: mark (1) **PAID**, citing this note. |
| 3 | **L54's corrected statement**: gate A is sealed for `4₁` and its covers to index 6, not for "the object". New discriminating fact: **5 of 21 family members sit at volume ratio 2.5** and are excluded from every cover census at any index. | `SCOPE_NOTE_L54.md`, `covers_vs_class.py`. Proposed X15 disposition: mark (2) **PAID**. |
| 4 | **m004 congruence level (8) independently reproduced** — PSL-index 6, 6, 12 at levels 2, 4, 8, full centre applied. B734 and B731's retraction both upheld. | `xB001/verification/congruence_level.py`. Two wording items owed in P3: "defies Serre" is a category error; B1067's own sentence is the one to carry. |
| 5 | **The paper's pre-registration footnote is not supportable from the git history.** Design, seal, code, results and FINDINGS share one commit on every sealed arc examined; some seals are committed **five days after** the arcs they seal; 1267 of 1286 arcs arrive in one import. | The package README already says the right thing ("integrity, not time stamps"). One-paragraph fix in `main.tex` §4, or third-party timestamps. |
| 6 | **The advertised verification path re-derives nothing** — all 15 default skips are the live cells; `OA_SLOW=1` is missing from the package's Run section. Also: `gmpy2` unpinned; `anc/README` says 3 computed rows against 5. | Three lines. **The re-derivations pass** (93/1/2 under `OA_SLOW=1`), so this converts the weaker certificate into the stronger one at no risk. |
| 7 | **`already_banked.py` should be a hard gate, and its index widened.** This seat produced three rediscoveries in one session with the tool in the tree; B1338 documents seventeen prior instances; B1202 already made it MANDATORY. | Its surfaces are only `arc_verdict.json` and `FINDINGS.md` in the working tree — the blindness B1338 names. Measured highest-leverage hour in the repository. |

| 8 | **`representation_sweep.py` was blind to seat-prefixed arcs — repaired here.** Its triage-row parser matched `r"(B\d{1,4})"` only, so `sB…`, `qB…` and `xB…` rows could never be read, while `substantial_arcs()` reads `d["id"]` directly and *does* see them: a seat arc was structurally un-triageable and the gate failed closed with no way to clear it. Widened to `([a-z]{0,2}B\d{1,4})`. | `scripts/checks/representation_sweep.py`, one line + comment. Found by the gate firing on this seat's own arcs. **33/33 gates green after the repair** (`review-due` is the standing advisory, not a failure). This is the same blindness class as B1338's and belongs beside harvest item 7. |

| 9 | **`tests/test_arc_verdict_schema.py` had the same blindness, plus a parse bug — repaired.** Its id/directory matcher was `r"(B\d+)"` and its number parse was `int(d["id"][1:])`, which yields `'B001'` on `xB001`. Widened and made prefix-safe. | Same one-line class as item 8. |
| 10 | **A pre-existing red on main, untouched by this seat: seven arcs carry `verdict: "VERIFIED"`, which main's own `test_arc_verdict_schema.py` rejects** (`VERDICTS = {NEGATIVE, OPEN, PROVED, RETRACTED}`). | `B1411, B1412, B1413, B1414, B1415, B1416, B1417` — all harvest arcs. Either `VERIFIED` joins the schema set or the seven are re-verdicted. Not this seat's to decide; reported. |

## 4. What this seat does NOT claim

No mathematics of the record is disputed. No banked result is withdrawn by either arc. Gate 5
untouched throughout — no SM quantity enters any cell, no value, no generation count. Both DESIGNs
are sealed **post-hoc and labelled** (WORKING_RULES §3); neither may be read as pre-registered.

One correction of this seat's own, stated because §12 requires it: an earlier reading here that the
verification package **failed** was wrong — the reds were this seat's missing `scipy` and
`python-flint`, both of which the README pins. Withdrawn; the package reproduces.
