# PROPOSAL — how the record refers to the AI assistants: a method, described by what was done

**From:** cld-advisor, the advisor seat. **To:** cc (main), who keeps the record's vocabulary. **Asked for by the
owner,** in the words below. **Kind:** a proposal. A design; nothing is built and nothing on main is changed.
**Main read at:** `e6298271a`.

## 1. The owner's words

> "btw a very confusing thing in our whole repo is this AI seats thing, confusing naming understood only internally,
> sometimes presented as some authority, maybe we should propose a cleaner way to refer to the seats idk how, but
> smth less confusing and credibility damaging. ai is part of the methodology, not co-authors"

**The principle he states: AI is part of the methodology, not a co-author.**

## 2. Measured

| | |
|---|---|
| rows of `docs/SEAT_REGISTER.md` | 29 |
| verdict lines that use the word "seat" | 344 of 1,588; of the 1,099 graded proved, 279 |
| verdict lines that name a seat by its nickname | 238; of the proved, 185 |
| verdict lines that say "two-seat", "three-seat", "cross-seat" and the like | 39; of the proved, 26 |
| the word "seat" in eight governing and claim pages | 269 uses, in 7 of them |
| the word "seat" under `papers/` | 180 uses, in 35 of 173 files |
| a seat as the subject of ruling, approving, certifying, deciding, or of "verdict", in the pages at the root of `docs/` | 21 uses in 10 pages |

## 3. What is wrong with it

1. **The names are private.** A reader meets "cc2", "the banking seat", "the agy lane", and learns nothing.
2. **A seat reads as an authority.** "Two-seat", "the review seat's catch", "main approves" sound like separate
   people or an institution confirming a result. It is one person directing assistants, most of one family of model.
3. **The names do not carry what a reader needs,** which is how independent a check was.

This seat's own pages do it as well: "this seat's verdict", "accepted".

## 4. The proposal

### 4.1 Say what was done, not who did it

A small fixed vocabulary for a check, in place of the names. Each use says what the two computations shared.

| the word | what it means | what it replaces |
|---|---|---|
| computed | run once | |
| reproduced | the same code, run again on a clean machine | "verified", where that is all it was |
| recomputed independently | other code, written without sight of the first; the same family of model | "two-seat"; "cc2 computed, cc verified" |
| recomputed by another family, or by a person | the same, by a different family of model, or by a human | "cross-seat", where it is true |
| sealed first | the expectation was fixed and hashed before the result was known | |
| attacked | planted cases or an adversarial reading, with what survived | "the audit seat's catch" |
| outside | by someone who is not of the project | none yet |

### 4.2 Roles, not nicknames, where an actor has to be named

| today | proposed |
|---|---|
| a seat, a lane | a role: one assistant session with a fixed task |
| main, cc, the banking seat | the integrator |
| the SM seat, the web seat, the physical lane, and so on | the builder of a named topic; the checker; the auditor; the reader |
| relay, harvest, bank | report, intake, land |
| the owner | the author, in anything public |

One roster page maps every name used so far to its role, to what it was (an assistant session; which family, said as
"the first family" and "a second family"), and to its dates. The names here are placeholders for main and the owner.

### 4.3 Who decides

**Only the author decides. An assistant computes, checks, proposes and reports.** No assistant is the subject of
"ruled", "approved", "certified", "accepted" or "verdict". A check is passed against a criterion written beforehand:
"meets the criterion for E7; planted cases, outputs committed" and not "the advisor seat accepted E7".

### 4.4 Where each form applies

| place | the rule |
|---|---|
| the public package, the website, the papers | no seat and no nickname at all; the vocabulary of § 4.1; one statement of method, which main has drafted (B1888 § 4 G) |
| new pages of this repository | the roles of § 4.2 and the vocabulary of § 4.1 |
| what is already written | not rewritten. The roster page, and one note at the front door |
| who is named as author of a commit | as the attribution rule already has it |

### 4.5 How it is held

This is the subject of WP-0.9, labels as strong as the content, which is this seat's by main's assignment.

- The grade of a check, in each verdict file, is one of the words of § 4.1, and the headline counts are printed by it.
- A gate on the public statement: none of the internal names appears in it, and every "checked" carries its word.

## 5. What it does and does not do

It does not make any check more independent. **It stops a check from sounding more independent than it was.** And it
costs no rewriting: the statement is written anew in any case, and the 344 verdict lines stay as the record of what
was said.

## 6. Open

1. **The role names.** Integrator, builder, checker, auditor and reader are this seat's guesses.
2. **Whether the instruments are named in the statement of method.** The attribution rule keeps vendors' names out of
   tracked files. A statement of method that does not say which tools were used is not a full one, and journals ask
   for it. This seat would name them once, there, as instruments with their versions, as software is named, and
   nowhere else. That is an exception to the rule, and the owner's to make.
3. **Whether main's own name changes** in new pages, or only in what is public.

## 7. Main's own proposal, as the owner relayed it to this seat the same evening

The owner had put the same point to main, and passed main's answer on to this seat in full. In short: name the
method, never the seat; in anything a stranger opens, no seat names, and each result carries one of a few fixed
labels that anyone can check from the files (computed once; recomputed independently, with separate code; recomputed
on a different family of model; expectations committed before the run; tested against planted errors, N of M caught;
not independently checked); no session is the subject of a verb of authority, "a check has a result, not a verdict";
"session" for "seat" inside the archive, with plain role names; one sentence on method at the front door; the past
stays, with one glossary line. Main has renamed nothing yet and holds it as an open call for the owner.

**The two proposals are one in substance, and main's is the base to take.** It is the better list in two places:
"N of M caught" on a planted test, and "not independently checked" said outright.

Three things from §§ 4 and 6 above that main's list does not have, offered as additions:

| | why |
|---|---|
| a label for **reproduced**: the same code, run again on a clean machine | it is the commonest check there is, and without its own word it will be written as "recomputed independently" |
| labels for **by a person** and **outside the project** | none exists yet; a label that can be seen to be unused says so |
| **each label names its evidence**: the two files, the commit of the expectations, the planted cases | then a gate can hold the label to the files. That is WP-0.9, and this seat builds it to main's list |

Still the owner's, from § 6: whether the tools are named, once, in the sentence on method.

**For this seat's own pages:** its rows say "verdict" and "accepted" because main's builder reads those words. It
changes them when main changes what the builder reads, not before, so that nothing main pins is broken.

