# B8120 — scrutiny triage

**Arc dated:** 2026-08-21 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

THE P1 SCRUTINY TRIAGED AGAINST OUR PAPER: 12 OF 13 CLOSED, ONE FIXED HERE, ONE LEFT OPEN AND
NAMED. The scrutiny audited an ANCESTOR -- 'THE GOLDEN GRAMMAR', 35pp, 2026-08-15, at
papers/scrutiny_golden_grammar/v6_source/main.tex -- not our 50pp 2026-08-21 arXiv paper, though
they share labels and are the same lineage. BOTH FATALS ARE DISCHARGED: F1's requested repair
(make Q(sqrt-3)=>2T a numbered theorem with hypotheses) is already Proposition prop:mod3 with
the parabolic generators exhibited, and rem:consumes states F1's own observation as a design
feature; F2's six undefined objects appear zero times in our text. NINE MAJORS ARE DISCHARGED by
the two referee rounds our paper has been through since. ONE WAS LIVE AND IS NOW FIXED: M5 --
our verify/ had no entrance check and App B had no row for prop:mod3. The scrutiny seat wrote
check_entrance.py; it was REPRODUCED AND RUN IN-SANDBOX BEFORE ADOPTION rather than cited, it
exercises exactly our generators, and its 2T control is 'exactly one involution' -- the same
instrument this seat used independently in B8111 and B8118. Adopted with provenance, App B row
added, suite now 20/20 from the extracted tarball. ONE IS NOT CLEARLY DISCHARGED AND IS FLAGGED
RATHER THAN PAPERED OVER: M4 -- our text still concludes 'exactly those conjugate to a power of
one of the three words', and the argument given supports only that powers of arithmetic
monodromies are arithmetic; the converse rests on reading BMR's classification of cyclic
commensurability classes as power-closed and exhaustive, which needs BMR's theorem statement to
settle. ALSO CORRECTED: my own first read told the owner the scrutiny targeted
papers/flagship/main.tex. It did not. Corrected the same turn. Triages 13 findings (2 fatal, 11
major) against papers/structure_paper/arxiv/main.tex by reading our text, not by trusting the
scrutiny's page references, which are to a different document. Does NOT triage the MINOR
findings, the five CONSTRUCTIVE items (E1-E5), or Round 2's R1-R4 -- those remain untriaged and
are named as such. Gate 5 untouched.

## What the arc recorded

### `verdict`

THE P1 SCRUTINY TRIAGED AGAINST OUR PAPER: 12 OF 13 CLOSED, ONE FIXED HERE, ONE LEFT OPEN AND
NAMED. The scrutiny audited an ANCESTOR -- 'THE GOLDEN GRAMMAR', 35pp, 2026-08-15, at
papers/scrutiny_golden_grammar/v6_source/main.tex -- not our 50pp 2026-08-21 arXiv paper, though
they share labels and are the same lineage. BOTH FATALS ARE DISCHARGED: F1's requested repair
(make Q(sqrt-3)=>2T a numbered theorem with hypotheses) is already Proposition prop:mod3 with
the parabolic generators exhibited, and rem:consumes states F1's own observation as a design
feature; F2's six undefined objects appear zero times in our text. NINE MAJORS ARE DISCHARGED by
the two referee rounds our paper has been through since. ONE WAS LIVE AND IS NOW FIXED: M5 --
our verify/ had no entrance check and App B had no row for prop:mod3. The scrutiny seat wrote
check_entrance.py; it was REPRODUCED AND RUN IN-SANDBOX BEFORE ADOPTION rather than cited, it
exercises exactly our generators, and its 2T control is 'exactly one involution' -- the same
instrument this seat used independently in B8111 and B8118. Adopted with provenance, App B row
added, suite now 20/20 from the extracted tarball. ONE IS NOT CLEARLY DISCHARGED AND IS FLAGGED
RATHER THAN PAPERED OVER: M4 -- our text still concludes 'exactly those conjugate to a power of
one of the three words', and the argument given supports only that powers of arithmetic
monodromies are arithmetic; the converse rests on reading BMR's classification of cyclic
commensurability classes as power-closed and exhaustive, which needs BMR's theorem statement to
settle. ALSO CORRECTED: my own first read told the owner the scrutiny targeted
papers/flagship/main.tex. It did not. Corrected the same turn.

### `scope`

Triages 13 findings (2 fatal, 11 major) against papers/structure_paper/arxiv/main.tex by reading
our text, not by trusting the scrutiny's page references, which are to a different document.
Does NOT triage the MINOR findings, the five CONSTRUCTIVE items (E1-E5), or Round 2's R1-R4 --
those remain untriaged and are named as such. Gate 5 untouched.

### `correction_of_my_own_first_read`

I first told the owner the scrutiny targeted papers/flagship/main.tex. WRONG. It targeted
papers/scrutiny_golden_grammar/v6_source/main.tex, a third copy. Corrected the same turn, before
it propagated.

## Depends on

`B8111`, `B8118`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
