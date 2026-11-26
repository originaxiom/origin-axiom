# B2013 — Review 87 entered: three cold readers caught seven of the eight plants and found real faults in eight of the ten arcs read; each is checked by main and mended

**Verdict: PROVED (a process arc).** Main, 2026-11-26. Register rows P-881 and P-882. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 87|plant|reading copy|cold reader/: 54 of 1754 arcs on main match (NEGATIVE 1, OPEN 2, PROVED 50, RETRACTED 1); 67 register rows match (DECLINED 1, DONE 26, QUEUED 40)`.
  These are the earlier reviews' entries and their rows. This arc follows Review 86's method (B1975).
- **The literature:** none applies; this is a review of the record's own window.

## Why now, and what was read

- **When it opened: late.** The review opened at the 40th landing since Review 86's anchor f4a0ab61f, when the push gate
  refused. R84-4 and R85-1 ask that it open by the 34th.
  - The gates printed "review-due: 37" at B2011's landing. Main, in the author's /loop, kept landing (B2012 and a record
    commit).
  - B2012 and the registration of the agy lane's C61 were stranded locally until this entry.
  - The miss is main's (R87-1).
- **The window:** f4a0ab61f to 36f9cc5c2, the anchor of this entry. It holds 40 commits and 38 arcs with a verdict,
  B1975 to B2012 (`verification/review_tools_draft.txt`).
- **The sample.**
  - The tool, seeded by the anchor, drew B1980, B1983, B1993, B1995, B1996 and B2004.
  - Main added B2008, B2009, B2011 and B2012. They are the window's latest arcs and rest most on the seats' claims and on a
    delegated listener.
- **The reading copy and the readers.**
  - The copy was a git archive of the ten arcs at 36f9cc5c2, with eight planted faults in eight arcs. B1980 and B1995 were
    left clean as controls.
  - The plant list is `verification/plants.txt`, sha256 85455f2cc650a0638d9b086119f663d54083e37c2d8a72e50ff9ddfe421c4018.
    The hash was fixed in the scratch room before any reader started.
  - Three readers of main's own model family that wrote none of these arcs:
    - A read B1980, B1983, B1993 and B1995;
    - B read B1996, B2004 and B2009;
    - C read B2008, B2011 and B2012.
  - Each read only its folder of the copy and could run the cheap scripts and tests there.

## The plants

| arc | plant | caught by |
|---|---|---|
| B1983 | E1's count, 13 of 13 primes → 15 of 15 | A |
| B1993 | the mixed orbit's size, 210 → 240 (against 280 = 70 + 210) | A |
| B1996 | the mod-125 slowest decay, 0.8389 → 0.8398 | B |
| B2004 | σ's third component, xy − z → xz − y | B |
| B2009 | the dated note's modulus, mod 135 → mod 153 | **missed.** Reader B quoted the note but could not check its number, because the arc it cites (B2011) was outside its folder. R86-5's plant again; the lesson is R87-4 |
| B2011 | the unpaired count at mod 135, 10 → 12 (against its four factors, degree 10) | C |
| B2011 | a lock that cannot fail, `max(diffs) < 1e-12` → `< 1e12` | C |
| B2008 | the claim line, "not one of the moves (tau not in G_k" → "one of the moves (tau in G_k" | C |

## The readers' own findings, checked by main on the live tree, and the mends

| arc | finding (reader) | checked | mend |
|---|---|---|---|
| B1980 | the verdict line still says frame C fails S; four body passages and the hypotheses field carry the withdrawn result; the lock asserts the withdrawn run's S failure (A16–A18, A20) | **real** | the clause struck from the verdict line; the S-cov rows, "the end is not the breaker", "the next step" and B1978's line marked withdrawn; P-882's Q1 marked retired; hypotheses corrected; the lock's part-B tests labelled as holding the withdrawn runs' text, as run |
| B1980 | the correction's 0.59 to 0.96 for K ≠ 1 unverifiable here (A19) | **answered:** B1982's `fricke_endlaw_run.txt` gives largest distances 5.9e-01 to 9.6e-01 | the claim line cites it |
| B1983 | "at p ≥ 29 more than half the leaves split", false at 47 (23 of 47) (A2) | **real** | 29 ≤ p ≤ 43, and 23 of 47 stated |
| B1983 | κ = −1, 0, 1 "connected at one or two primes at most"; κ = 1 is connected at 5, 7, 43 (A3) | **real** | the counts stated |
| B1983 | the claim line's "the whole singles out the cusp … only at 2 and 3" without the body's hedge (A4) | **real** | scoped as a reading over the primes run |
| B1993 | the claim line frames the result against ω's retirement by a Standard-Model-shaped test; "selects ω" rests on a cited identification (A8) | **real** | the clause removed (history, not a criterion); the identification marked cited; the lifts marked read, not computed |
| B1993 | the lock reads text only (A10) | **real** | `integers.py` (about 25 s) is now rerun against its committed run |
| B1995 | "every mode of W± … ⅓, ⅓, ⅓" is sympy's basis of a 2-dimensional eigenspace (A12) | **real** | the row replaced: only the plane's projector is meaningful, and it gives each member 2/3 |
| B1995 | "2/3 per move" is W₊'s diagonal for a sum of two moves (A13) | **real** | the title and the law map's row corrected |
| B1995 | the claim line has no scope (A14) | **real** | scoped to the linear parts at the common point |
| B1996 | "coefficients near its search limit": they are up to 101 against 200 (B9) | **real** | the numbers stated |
| B1996 | the levels inherit eigenvalues by pull-back; mod 729 by Arnoldi with no committed convergence check; "algebraic, as B1992 requires" is trivial (B10) | **real** | the caveats added |
| B1996 | the lock does not hold the mod-125 value, the control or the gaps (B11) | **real** | now held |
| B2004 | "every word outside Γ′ that fixes a point acts with C's cycle type" is over 217 words, and cycle type is not conjugacy; C has two fixed points at mod 9 (B7) | **real** | scoped; C60's 7,776 non-conjugate elements cited (registered, not checked); the twist sentence marked a reading |
| B2004 | the localisation counts were not locked (B8) | **real** | a test added |
| B2008 | the identification of ℤ₂ × ℤ₂'s factors is a reading; "cannot carry ω's charge" holds at the three levels run; "the chirality bit" (C10, C11) | **real** | scoped and marked as readings in the body and the claim line |
| B2009 | the three exceptions matched to the modes 6, −6, 0 by count only; ρ³ labelled S₄'s sign unchecked (B3) | **real** | a dated bracket says so; the claim line scoped; agy's C61, which claims the assignment, registered for the next arc |
| B2009 | the charge-1 sector and Perm(O) = Ind 1 unstated (B4); "the same six" by rows, not identity (B5); the Seen-first premise uncorrected (B6) | **real** | stated (complex conjugation; transitivity); identity cited to B2010's inflation; the premise marked "not a law" |
| B2011 | the title's "a proof for every rung"; "one law" over five levels (C4, C5) | **real** | "an argument"; "one formula … in the five levels run", M's rule read off them |
| B2012 | "at 7 it is no such reduction" asserted unchecked (C6) | **real** | now argued from the known orbits' leaves (k = 2, 3, (5 ± √5)/2, t², 4; none reduces onto k ≡ 0 mod 7 but the origin), with B1989's list not proved complete |
| B2012 | the 2-adic halves stated for the class k ≡ 5 mod 8 (C7) | **real** | scoped to k = 5, 13, 29 |
| B2012 | the card's Q(x) Q(x − 2) against the run's R(x + 4) R(x + 2) unexplained; the plane computation not machine-checked (C8, C9) | **real** | Q(x) = R(x + 4) stated; `two_subspace.py` checks the plane by sympy |

- **Not mended, with the reason:**
  - B1983's literature cited from memory (A5): already disclosed in its hypotheses.
  - B1993's M4 check is narrower than the cited identification (A9): the identification is marked cited.
  - B1983's lock does not hold its text's counts (A6): it reruns both scripts exactly; the text faults are mended.
  - B2004's Π₂ sector and "to 10⁻¹⁶" are not in its lock (B8): the sector follows by conjugation.
  - B2008's GAP lock reads text (C10): sage runs are not rerun in the suite.
  - B2008's hashed card reads its outcome against the record's split pattern (C11): a hashed card is not edited. This entry
    records it, and B2008's findings now mark the reading as one.

## What the review shows

- **Seven of eight plants caught.** The miss repeats R86-5: a number inside a dated note can be checked only against the
  arc the note cites, and that arc was not in the reader's folder.
- **Every arc read had something.** Three kinds recur:
  - (1) text that outruns its script: B1995's basis-dependent row, B2009's mode assignment, B2012's mod-7 sentence;
  - (2) patterns over the cases run written as laws: B1983, B2004, B2011, B2012. That is the error B2011 itself found in
    B2003 and B2005;
  - (3) withdrawn results left standing in an arc's other parts: B1980.

  All three are known classes in `docs/ERROR_LEDGER.md`:
  - (1) is E11, an overextended record, and, for B1995's basis, E1, undeclared choice drift;
  - (2) is E22, a conclusion from a shallow level check. B2005's "ℤ₆ survives exactly where the halving holds" was also E4,
    a necessary fact read as sufficient;
  - (3) is E13, stale artifact text.

  The pairing law of B2012 is the case E34 warns of, read the right way round: a property of the larger structure (the
  modular group) is named as such, not read as the whole's.
- **No new error class.**

0 of 19.
