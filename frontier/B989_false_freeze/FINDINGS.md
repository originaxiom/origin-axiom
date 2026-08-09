# B989 — the document that explained the opt-out had opted itself out

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** repository governance. Gate 5 untouched.
**Found by:** Review 41, step **7a** — the first run of the document-currency reading, on the day it
was written.

---

## The bug

`doc-currency` (B984) lets a document opt out of currency checking with an in-file marker,
`<!-- doc-currency: frozen -->`, on the stated condition that the opt-out is **visible** — frozen
files are printed on every run.

`docs/PRACTICES.md` reported as **frozen**. It was not. It **documents the marker**, inside a code
span, in the practice entry that describes `doc-currency` itself:

> *"**`frozen`** — an in-file marker `<!-- doc-currency: frozen -->` for records, dated snapshots…"*

The regex matched the documentation.

> **A document explaining how to opt out had opted itself out — and `PRACTICES.md` is a *living
> methods* document, exactly the kind the gate exists to keep current.**

**Fix:** the marker counts only when it *is* a marker — detection tightened to **line-initial**
(`^\s*<!--`). The documentation line begins `- **\`frozen\`**` and no longer matches. PRACTICES is
back under checking, and current.

## Why it matters more than one file

**This is the second time in one day that mention-was-read-as-use, in a second, independent gate.**
Hours earlier `retraction-sweep` fired on **B983's own error table** — a *record* of what was
wrongly claimed, sitting beside its refutation — because the mention cue was implicit.

> **Mention-vs-use is a failure mode of text-matching gates as a class, not a bug in either one.**

Both gates were written the same week, by the same seat, each with an explicit mention/use
distinction in its docstring — and both got it wrong in practice. The distinction is easy to state
and hard to implement, because the *safe* direction differs: a retraction sweep must be **strict**
(a missed live use is the harm), while a freeze marker must be **narrow** (a false freeze silently
disables the check, and silence is the harm).

**Standing note for any future text-matching gate:** decide, in the docstring, **which direction of
error is the harm**, and set the pattern's strictness to match. A gate whose false positives are
loud is safe; a gate whose false *negatives* are silent is not.

## A third instance, recorded because it is the same shape at the data layer

Review 41's step 7c found the coverage count for **Markov blanket** had risen from **0 to 2** — and
both hits are **B984 and B988, the arcs that record its absence**. **Registering a gap creates hits
for the gap.** No gate was involved; the measure inflates itself. Annotated in `THE_LADDER.md` so a
later review does not read the rung as covered.

## Scope

Governance, not mathematics. One-line regex fix plus two annotations. What it changes is that
**`PRACTICES.md` is checked again** and that the class — *mention read as use* — is now named in
three places (this arc, the retraction sweep's record, and the ladder's X31 caveat) rather than
being rediscovered a fourth time.
