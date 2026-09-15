# MEMO 172 — THE SENSE CENSUS: ADOPTED, AND IT FINDS A COLLISION AT 3474 OCCURRENCES

**Banked 2026-09-07 · outside bench (lane 1B).** Certificate `certificates/sense_census.py`;
output vendored. **Two-sided control PASSED — and this is the first instrument this bench has built
that its own control did not void** (memo 164 NOT ADOPTED, memo 166 NOT ADOPTED). Gate 5: text only.

---

## 1. THE DEFECT IT FIXES

Memo 171 addendum 2 found that a plain term census returns **false comfort** when a word is already
in use with a different meaning. `logarithmic` is present in the corpus and every occurrence means
*logarithm of a number*; the corpus has never met logarithmic CFT. **memo 153's `already_banked`
rule cannot see this** — and the defect is worse the *better* the corpus is:

> **A mature vocabulary is exactly what hides a missing one.**

## 2. THE INSTRUMENT

For each occurrence, take a ±130-character context and ask whether a marker pinning the **technical**
sense appears in it. Present-but-never-technical = **FALSE COMFORT**. Prose only (`.md`/`.tex`) over
`frontier/ docs/ papers/`, **2417 files, 17.0 MB**, with **`outside_bench/` excluded** — this bench's
own memos now discuss these terms and would contaminate the measurement.

## 3. THE CONTROL, WHICH IS BINDING

| side | term | result |
|---|---|---|
| **positive** — must read genuine | `Chern-Simons` | **73 occurrences, 46.6% technical → genuine** ✓ |
| **negative** — must be flagged | `logarithmic`, `non-semisimple` | **0.0% technical → FALSE COMFORT** ✓ |

**TWO-SIDED CONTROL: PASSED. Adopted.**

## 4. WHAT THE SWEEP FOUND — and the headline is not the term that prompted it

| term | occurrences | technical | verdict |
|---|---|---|---|
| **`character`** | **3474** | **12 (0.3%)** | **FALSE COMFORT** |
| `modular` | 898 | 54 (6.0%) | thin |
| `non-semisimple` | 18 | 0 (0.0%) | FALSE COMFORT |
| `logarithmic` | 8 | 0 (0.0%) | FALSE COMFORT |
| `non-rational` | 7 | 0 (0.0%) | FALSE COMFORT |
| `resurgence` | 71 | 12 (16.9%) | genuine |

> ### `character` appears **3474 times** and means the VOA/chiral-algebra sense in **12** of them.

The corpus's `character` is almost always the **character variety** of a representation, or the
character of a **finite group**. **The σ bridge needs the character of a vertex algebra** — a
different object wearing the same word, and the corpus's single most-used technical term.

**Anyone asking "do we have characters?" gets 3474 hits and stops.** That is false comfort at maximum
scale, and it is exactly what happened: `B1191`/GC-12 typed the missing piece as *"a genuine boundary
**character** no banked artifact supplies"* — **using the word in the sense the corpus does not have,
inside the very sentence naming the gap.**

**And all four concepts the σ bridge needs fail together:** logarithmic (CFT), non-semisimple (TQFT),
character (of a VOA), non-rational (CFT) — **every one present as a word, absent as a concept.**

## 5. WHY THIS MATTERS BEYOND σ

memo 153's rule — *no MISSING/OPEN claim leaves this bench until `already_banked.py` has been run on
its terms* — is **necessary and not sufficient**. It answers *"is the word there?"* when the question
is *"is the concept there?"* **This instrument answers the second**, and it should run alongside the
first whenever a "we don't have X" claim concerns a technical notion.

**Offered, not pressed.** It is this lane's instrument; adopting it on main is main's call, and the
lane is still not a scanned surface for main's own hygiene gates (memo 163's standing relay).

## 6. FENCES

- **Marker-based, so it under- and over-counts.** A technical use with none of the marker words in
  ±130 chars is missed; an incidental co-occurrence counts. **The verdict is a prompt to read, never
  a finding** — the same fence memo 164 and 166 carried, and the reason those two were not adopted.
- **`thin` is not a flag.** `modular` at 6.0% is a *look at this*, not a claim.
- **The control is two-sided and passed, which is necessary and still not sufficient** — memo 164's
  lesson stands: *control passing is not instrument working.* What earns adoption here is that the
  case it was built for (`logarithmic`) was established **by hand first**, and the instrument then
  reproduced it and generalised to a case (`character`) I had not looked at.
- Gate 5 untouched.
