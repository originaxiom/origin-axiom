# B1306 — THE OLDER DEBT, SLICE B: the first payment on R56-1 — the SM-derivation seat's three commits past main's pin (the tower law's positive half proved; the presentation identity proved; sm:B1350's exact obstruction calculus; the prior-art correction of main's own Entry 5; two of main's locks that fail on a fresh clone) and the cloud's memos 182–184 (a printed quantum A-polynomial that does not annihilate its own series; the colored-Jones tail of m(5₂) a false theta): DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1306 (slice B), §1a rules 1–4; Review 56's R56-1 payment order (a):
"newest first" = exactly the six NEW items the harvest gate reported on its first run. · **Seats pinned for this slice:** the SM-derivation branch @
`ca850d6b` (three commits past `0dffacd4`: `19f6feef`, `258aeeb5`, `ca850d6b`), the cloud branch @ `02a885ca` (three commits past `792918b7`:
`05da3f2d`, `b059c072`, `02a885ca`). · **Read in full before this seal:** the seat's `ADDENDUM_2026-09-08_the_positive_half_proved.md` (its proof,
steps (1)–(5), and `law_positive_half_run.txt`), `ADDENDUM_2026-09-08_the_presentation_identity_proved.md` (+ run), sm:B1350 FINDINGS §4(a)–(d) and
the two obstruction run records, the relay's third note (2026-09-08, later), B1281's addendum "the seats verified II", `docs/PRIOR_ART_ASSELMEYER_MALUGA_2026-09-08.md`
§1–§4, the added lines of THE_ASSEMBLY / THE_DESTINATION_LEDGER / THE_VIEW_FROM_ABOVE; the cloud's memo 183 with both addenda, memo 184, memo 182 §3
as corrected by 184 §5, and the three certificate outputs. **Fetched at inform time and NOT yet read past their tables of contents:** Park,
arXiv:2004.02087v2 (the PDF and the arXiv LaTeX source, under the gitignored `audit/literature/park/`) — the coefficients of its eq (32) are
unread at this seal; only the line numbers at which `f_0^{m(5_2)}` and `\hat{A}_{m(5_2)}` occur in the source were located by grep.

## 0. The rule lines

`already_banked.py`: "colored Jones tail false theta 5_2" → no settled arc (B1127 matched 3 generic terms); "quantum A-polynomial erratum m(5_2)"
→ no settled arc; "second-order obstruction V10 subregular" → no settled arc; the tower-law terms → B979 (L131/A7, unrelated). `absence_sweep.py
"figure 8 knot"` → PRESENT on one head (this correction is not "we don't have X"; it is "we said X was absent and it is present"). Receipt:
`verification/sliceB/already_banked_at_seal.txt`.

## 1. The view from above

Six items are NEW because two seats kept working after main's pins: that is the harvest gate doing its job on its first day. Three of the six are
theorems or exact computations that bear on main's own live leads — the tower law (L203's finite menu now has a proved half), the presentation
identity (the foundation of B1306 A's verification), and the V₁₀ obstruction calculus (L204, the one direction where a chirality bit could still
live in the flat frame). One is a correction of main by the seat: **B1306 A said the figure-eight is named in none of sixteen papers; the seat
found it on page 29 of the 2019 paper, spelled "figure 8 knot"** — main's own search pattern was too narrow, and the correction must reach every
surface that carries the wrong sentence (five, listed in §2 Q3). One is a defect in main found by the seat (two locks read gitignored run records).
The cloud's two are instrument findings on a borrowed input (Park's paper) that decide whether the c_eff line can reach a second hyperbolic knot,
and one of them (memo 183) is the kind of claim — a published formula is wrong — that must not be repeated on main without an independent check;
main can do what the cloud could not: **fetch the arXiv source and read the equation as typed**. The one thing it means if the slice fails: if
the positive-half proof does not reproduce on main's own Fox calculus, the tower's law loses its theorem and L203's menu is back to a conjecture.

## 2. The questions, pre-registered (priors; PASS and FAIL both reachable)

**Q1 — T-TOWER-LAW-POSITIVE-HALF (sm:B1304 addendum @ ca850d6b), re-derived with main's own code.** The seat says: *"If ord_m(u) is odd, or
ord_m(−u) is odd, then h¹(Y_n; ψ) = 1 at every level n at which ψ lives."* Main's check (`verification/sliceB/b1306_positive_half.py`, its own Fox
calculus of the half-deck h: a ↦ ab, b ↦ a, built from B1306 A's machinery, exact modulo two primes ≡ 1 mod m): (a) at every Ψ-eigencharacter
class (m, u) of every level n ≤ 13: the one-period product N₀ has tr N₀ = 1 + (−1)^e and N₀ fixes the coboundary vector; for e odd N₀² = I and
P_n = N₀^{2n/e} = I; (b) the conductor form ⇔ the odd-order form over all (m, u) with m ≤ 4000 (own enumeration of the roots of x² − x − 1 mod m);
(c) the converse's content at n ≤ 13: no class with both orders even carries. **PASS** = (a), (b), (c) all hold — the theorem enters main's
THEOREM_REGISTRY as VERIFIED with credit by pin; **FAIL** = any class where the theorem's prediction and h¹ disagree (the finding). Prior 0.90.
Also re-run the seat's `law_positive_half.py` and `presentations_h1_all_characters.py` in the pinned worktree (receipts).

**Q2 — sm:B1350 stages 5a–5c (the exact obstruction calculus).** The seat says: *"No obstruction at second order — exactly … V₁₀, V₁₀#2, V₁₀ ± V₁₀#2
are all integrable through order 6 … the stall of (a) is therefore numerical."* Main re-runs `obstruction.py` and `obstruction_higher.py` in the
pinned worktree (receipts; expected ≈ 3 min each) and checks the arithmetic identity rank d¹ = 156 − dim Z¹ = 156 − (78 + 8) = 70 against its own
h¹(M; e₆) = 8 record (B1265/B1274 lineage). **REGISTERED** on L204 with the seat's limits verbatim (the method is one-sided; stage 4 pending);
main's independent e₆ deformation computation remains the L204 arc, after stage 4 lands. Prior that the re-run reproduces: 0.90. No grade above
REGISTERED is claimed from a re-run.

**Q3 — the prior-art correction (the seat's `docs/PRIOR_ART_ASSELMEYER_MALUGA_2026-09-08.md` §1/§6 and the relay's third note).** The seat says:
*"The complement of the figure 8 knot is one example of an arithmetic hyperbolic 3-manifold" — spelled "figure 8 knot", which a search for
"figure-eight" misses.* Main verified at inform time by its own extraction of the PDF (page 29, with the ﬁ ligature) and by a corrected pattern over
all sixteen text files: three papers contain the digit spelling (1910.09966 p. 29 the knot; 1003.5506 "the ﬁgure-8 knot" among hyperbolic knots;
1107.3458 twice as a figure caption). **VERIFIED-DIFFERS in the seat's favour**; the correction lands on every surface that carries the wrong
sentence — the dossier Entry 5 (two sentences: the adjudication's "does not appear" and the sixteen-paper addendum), `FINDINGS_A.md` §6, B1306's
`arc_verdict.json` claim, HARVEST_LEDGER rows 36 and 82, FRESH_EYES Q14's note, CAMPAIGN_STATUS's B1306 A block — with dated correction notes
(CHANGELOG/PROGRESS_LOG are append-only: a correction entry). Filed in ERROR_LEDGER as an **E54 instance (mine)**: an absence asserted from a
search whose pattern did not cover the source's spelling; the rule gains a clause (digit spellings and ligatures are part of "the whole sweep").
The seat is credited first (its finding, 2026-09-08, before B1306 A landed).

**Q4 — two of main's locks fail on a fresh clone (B1281 addendum II @ 19f6feef).** The seat says: *"`test_b1299…` and `test_b1302…` read
`b1299_w1w2_main.out` and `b1302_signs.out`, which your `.gitignore` (`*.out`, line 21) keeps out of the repository."* Main's sweep at inform time
(every test naming a `.out` file, checked against `git ls-files`): exactly those two, no others. Fix: the two records are renamed to `*_run.txt`
(this repo's own receipt convention elsewhere) and tracked, the two tests updated; `b1299_w1w2_main.py`'s final f-string single-quotes its inner
keys (Python 3.11); both tests re-run. **PASS** = both locks pass from the tracked files; the seat's two asks answered in the held reply. Prior 0.95.

**Q5 — cloud memo 184: the colored-Jones tail of m(5₂) is a false theta (cloud @ 02a885ca).** The cloud says: *"Φ_{m(5₂)} = Σ_{k≥0} (−1)^k q^{k(k+1)/2}
= 1 − q + q³ − q⁶ + q¹⁰ − … read as the stabilising bottom end of J_n(m(5₂)) … at n = 6,7,8,9. Eight stabilised coefficients."* Main's own
calculator (`verification/sliceB/b1306_jones_52.py`): the U_q(sl₂) Ř-matrix on V_N ⊗ V_N in the weight basis from the explicit formula (not the
cloud's decomposition route), exact Laurent arithmetic in q^{1/2}; controls that must all fire — the braid relation and Ř·Ř⁻¹ = 1 (N = 2, 3, 4),
the unknot's quantum trace = [N], the figure-eight's J_N = GM (166) (main's own `J41`, B1305 B) for N = 2, 3, 4, the right trefoil = Habiro (main's
own `J31_habiro`) for N = 2, 3, 4, and J_2 of the 3-braid σ₁³σ₂σ₁⁻¹σ₂ (5₂) equal to the Jones polynomial of 5₂ or its mirror with |V(−1)| = 7 =
det(5₂). Then the two ends of J_n(m(5₂)) at n = 6, 7, 8, 9 with main's own `bottom`/`top`/`stable` (B1305 B). **PASS** = the bottom end's
stabilised coefficients begin [1, −1, 0, 1, 0, 0, −1, 0] (the false theta on eight coefficients) and the top end does not stabilise at n ≤ 9; **FAIL**
= a different stabilised sequence (the finding, both benches then differ on a computable object). Prior 0.80 (the cloud's C1/C2 controls fired and
Park's printed f₀ corroborates; the residual doubt is the end-rule and the framing convention, which main's controls fix independently). Also main's
own check of memo 184 §3: 1/Φ's coefficients grow like 1.2880ⁿ (own series inversion to n = 3000; the false theta's zero inside the disc) — prior 0.90.

**Q6 — cloud memo 183: Park's eq (32) does not annihilate F⁺_{m(5₂)}.** The cloud says: *"[Â F⁺]_{x^{7/2}} = q¹³·f₀(q) ≠ 0 … every single-monomial
repair fails … the erratum is not one dropped term."* It could not fetch the source; main has. Pre-registered fork, decided by the LaTeX: **(i)** the
source's eq (32) is monomial-for-monomial the cloud's transcription (its two PDF extractions agree with the typed equation) — then main recomputes
the x^{1/2}…x^{7/2} equations with its own series code from the source's own printed f₀…f₃ (lines 643–674 of `FKexamples.tex`) under the cloud's
convention A, and PASS = the defect q¹³ f₀ at x^{7/2} reproduced exactly (prior 0.75 given (i)); **(ii)** the source's eq (32) differs from the
cloud's transcription — then the "erratum" is a PDF-extraction artefact, VERIFIED-DIFFERS, and the recursion is re-run from the typed equation
(PASS = it produces Park's printed f₃ exactly). Prior for (i): 0.60 (two independent extractions agreeing is strong; a typesetting-only difference is
the live alternative). Either branch is the finding; neither is a claim about Park's method. The cloud's reading of Park's Table 3 as a false theta
(Ẑ(Σ(2,3,11)) to all orders) is REGISTERED, not re-derived here.

**Q7 — the bookkeeping the gate counts.** HARVEST_LEDGER rows for every item above (the seat's verdict quoted first); the seat's four branch-only
documents dispositioned: `PRIOR_ART_ASSELMEYER_MALUGA` (VERIFIED-DIFFERS, the seat right), `THE_ASSEMBLY` / `THE_DESTINATION_LEDGER` /
`THE_VIEW_FROM_ABOVE` (REGISTERED: their new lines propagate main's B1304/E70 scoping of B1259 and the prior-art frame — no new claim), B1281's
addendum II (REGISTERED + main's fix), the relay's third note (RELAY_LEDGER row updated: BANKED @ ca850d6b, the two asks answered), cloud memos 182
(its §3 correction recorded as SUPERSEDED-BY-SEAT), 183, 184; **pins advance: sm → `ca850d6b`, cloud → `02a885ca`**; `harvest_debt.py` re-run
after the landing must show NEW unrowed 0 for both seats. The held reply to the SM seat (`CC_TO_SM_…`) gains a dated addendum (HELD).

## 3. Not in this slice

The 428 backlog (slices C–D pay it: the never-read physics items first, then the rows for the harvested-earlier items); main's independent e₆
deformation computation for L204 (waits for the seat's stage 4); any c_eff number for 5₂ (the cloud claims none; neither does main); the repair of
eq (32) itself if branch (i) holds (recorded as the open item it is, with the source now in hand — a bounded follow-up if f₄ from the R-matrix
determines it).

## 4. Landing list

`frontier/B1306_the_older_debt/{DESIGN_B.md, DESIGN_B.sha256, FINDINGS_B.md}`, `verification/sliceB/{b1306_positive_half.py (+ .out/.json),
b1306_jones_52.py (+ .out/.json), b1306_park_eq32.py (+ .out), sm_*_rerun.txt, cloud_*_rerun.txt, already_banked_at_seal.txt}`; the five correction
sites of Q3 + ERROR_LEDGER (E54 instance); the two renamed run records + two tests + the f-string (Q4); HARVEST_LEDGER rows + pins; RELAY_LEDGER;
THEOREM_REGISTRY (T-TOWER-LAW-POSITIVE-HALF, VERIFIED here, credit sm:B1304 addendum @ ca850d6b); OPEN_LEADS L203/L204 notes; HINT_LEDGER;
FRESH_EYES Q14; `tests/test_b1306_the_older_debt.py` (slice B tests); CHANGELOG + PROGRESS_LOG + CAMPAIGN_STATUS; `arc_verdict.json` updated.
