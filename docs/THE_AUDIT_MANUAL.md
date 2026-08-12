# THE AUDIT MANUAL — how to run an adversarial seat on this corpus

**cc3, 2026-08-12. Owner-commissioned. Written from one window's practice: ~1040 arcs,
seven disclosed errors of my own, four sealed passes, three killed hypotheses — two of
them mine.**

**Every rule below carries the instance that produced it.** A rule without its scar is
advice, and advice does not survive contact with a corpus this size. **If a rule seems
obvious, read its instance: it was obvious to me too, on the day I broke it.**

**The empirical basis, stated first because it determines everything after:**

> **All seven of this window's disclosed errors were RETRIEVAL or CHANNEL species. Zero
> were mathematics.** At this scale the failure mode is not being wrong — **it is not
> finding what the corpus already knows.**

---

# I — BEFORE YOU SEARCH: the search that cannot see

> ## **A SEARCH THAT CANNOT RUN RETURNS EXACTLY WHAT A SEARCH THAT FINDS NOTHING RETURNS.**
> **This is the manual's first sentence because it caused more than half of my errors.**

## The species, with instances

| species | instance | what it cost |
|---|---|---|
| **could not run — stale scope** | the audit branch was **378 commits / 232 arcs** behind main; B1000–B1032 absent — every arc under discussion | **two wrong relays**, one a STOP on a correctly-posed cell |
| **could not run — representation** | ASCII `phi` against banked Unicode `φ` | B1011 invisible **even on main** |
| **could not run — tool absent** | `timeout` does not exist on macOS; the command never executed | nearly banked *"0 arcs bank a value"* |
| **could not run — ID shape** | `B\d{1,3}` capped at three digits (**B1001**) | B1000 *"not reported, not counted, **not an error**"* |
| **could not run — no directory** | **B701 lives inside `B700_fiber_functor/`** as phase 2 | a "phantom arc" reported missing |
| **ran, changed units** | `grep -c -o` counts **occurrences**, not lines | an occurrence-count minus a line-count → a phantom figure, pushed |
| **ran, window read as whole** | `sed -n '33,35p'` — the sentence continued two lines down | **both seats, same sentence, same day** |
| **ran, but I trusted it** | a well-put line from a seat that had just verified eleven of my quotes | amplified without a single grep; it was an undersell |
| **the watcher's empty baseline** | a monitor whose "nothing seen yet" was indistinguishable from "nothing there" | re-fired the entire inventory, twice |

## The rules

1. **No "no match" becomes a sentence until a second, independent source agrees.**
   B1001's own law: *"the gate that caught it works by **CROSS-CHECKING TWO SOURCES
   rather than reading one**."* The atlas was caught by comparing it to the directory
   listing. Both are one extra line.
2. **Verify the tool ran** — exit status, not empty output — **and that it answered in
   the unit you assumed.** A flag combination can silently change the question.
3. **`head`/`tail`/`sed` output is a WINDOW.** Never conclude a population from one.
   **If a quote ends mid-clause, extend the range before believing the cutoff.** An
   ellipsis in a source is a signal, not a boundary.
4. **Run both representations** — `φ`/`phi`, `κ`/`kappa`, `ℤ`/`Z`.
5. **From a side branch, always name the ref**: `git grep <pat> origin/main`. An
   instrument sees main only as of its last sync — **say so in the instrument.**
6. **Never quote from a filename-suppressed grep.** `-h` and `-o` strip provenance; one
   flag produced three misattributions.
7. **`"(registered, not run)"` in a FINDINGS body is stale prose, not an index.**
   Verify by artifact: is there a script, an output, a prereg file?
8. **A claim from a trusted seat is a PREMISE, not a source.** *Verify-don't-trust binds
   to the premise regardless of who supplied it* — and the pull to skip is strongest
   when the claim is well-put and flatters your work.

## The two sweeps, and why almost everyone runs the wrong one

> **A SYNONYM sweep finds "one object, many names" — the retrieval failure.**
> **A REFERENT sweep finds "one name, many objects" — the collision failure.**
>
> **Every collision this programme has caught was the second kind**: two conductors, two
> levels, two E₆'s, **three σ's**, two "θ-even"s, two "trit"s. **And the corpus was
> running the first kind.** Ask which you need before you write the pattern.

---

# II — SEALING: what irreversibility buys when blindness is unavailable

> **You cannot buy back blindness. You have read the corpus. Buy IRREVERSIBILITY and a
> measured null rate instead.**

**Seal before you re-read any target at attack resolution. Hash first, content after,
and hand the hash to someone else.** Five items:

**1. Prior-contact disclosure + the known-at-seal register.** Name every finding already
in hand, at seal time, with the ruling: **they carry the weight of their mathematics and
none of the weight of their discovery.** An undeclared prior find, laundered as a product
of the pass, makes the whole pass worthless.

**2. The attack schema.** Per attack: the target verbatim · a mechanical trigger · a
verdict rule · **what it damages if it lands.** **An attack that names no damaged target
is pre-declared COSMETIC.**

> ### **3. SEAL THE TRIGGER BEFORE THE CHECK THAT DECIDES IT. This is the manual's most valuable rule and it cost me my best finding.**
> My strongest attack was on a modality. Its sealed trigger said: *fires only if a
> consequence depends on the modality being forced rather than generic.* **Checked
> afterward: none did.** **Sealed, it was a footnote. Unsealed, it would have been my
> headline** — and I would have believed it.

**4. Pre-commit the credit.** State what result counts as evidence **FOR** the thing you
are attacking. **An audit that cannot lose is exactly the defect you are auditing.**

**5. Declare your own stake.** If your phrasing has been adopted by the target, or your
fact is in its sources, say so — **and then do not grade your own attacks.**

**The amendment rule:** mid-pass findings are permitted and must be reported, but go in a
**separately hashed** file and are **graded one tier lower**. Sealing and then silently
improving is contamination.

---

# III — CONTROLS: the part that makes a pass evidence

## The decoy — the single highest-value number in any pass

**Build a matched-shape target designed to be wrong** (role-swap the claim; keep the
shape). **Run your sweeps against it, unchanged. Count what they find.**

> **PRE-COMMIT THE READING BEFORE THE RUN.** Mine: *≥2 refuters of citation type ⇒ my own
> findings are corpus-generic and score K0.*
> **It fired.** The corpus hands a "cannot"-modality refuter to **any** frame of that
> shape, because the prohibition **names no noun**. **I found my best result the way a
> metal detector finds the beach.**

**And state the decoy's scope limit.** A premise-swap decoy controls **premise** attacks.
It does **not** control attacks on the target's *consequences*. **Say which of your
findings are uncontrolled** rather than letting them pass in the crowd.

## The held-out slice

**Name it by a mechanical rule fixed before looking** (*"the ten lowest IDs not yet
read"*), **pre-commit a yield prediction**, then run.
> **AND DO NOT TUNE ON WHAT IT RETURNS.** I adjudicated a held-out slice, then fixed my
> instrument using what it showed me — **contaminating the very set that was supposed to
> validate the fix.** The post-fix number was no longer held-out and I had to say so.

## The banked-number gate

> **Gate every export against a number you did not compute** (B961's law). Its own
> instance: `rref()[1]` returns pivot **columns** and was used to index **rows** —
> *"silently producing a wrong-dimensional space **with no error**… the banked-number
> gate caught it and **nothing else would have**, since on an unbanked question **the
> wrong answer would have looked like a finding**."*

**Corollary, and I nearly skipped it:** **gate your FILTER against a known positive
before believing its silence.** Ten files returned zero; the same pattern scored 2 on a
file I knew contained it. **Only then was the zero a real zero.**

## The recall floor

**Every negative is a FLOOR, not a count**, unless the synonym set *and* a second source
both ran. **Report floors as floors.** A "how many arcs do X" figure is a floor whenever
the corpus has a second vocabulary for X — **and it always does.**

---

# IV — GRADING: and the claimant defaults against themselves

| grade | requirement |
|---|---|
| **K1 STRUCTURAL** | a banked deductive fact contradicts something a consequence depends on, and no restatement evades it — **you must exhibit the attempted restatement and show it fails** |
| **K2 MODAL / SCOPE** | the target survives with a weaker word, but the word **costs a consequence or lowers its grade** — **you must supply the exact replacement sentence** |
| **K3 UNPRICED** | an assumption is presented as a result, or a freedom is priced by fiat — changes the label, not the logic |
| **K4 COSMETIC** | wording attackable; nothing downstream changes. **Reported, scores zero** |
| **K0 VACUOUS** | **fires on the decoy too. Negative score** |

**Every finding carries: attack ID · grade · what it damages · the evading restatement ·
the control result. ANY EMPTY FIELD ⇒ K4 BY DEFAULT.**

> **You are the claimant of the kill, so the default penalises YOU: uncertain ⇒ cosmetic.**
> **And you do not set your own grades.** The bench or the owner does.

**Report the failures at the volume of the successes.** *"The attack I mounted does not
land. Reported anyway"* is what makes the ones that land mean anything.

**Three outcomes, never conflated:**
- **KILL** — a sealed attack fired, trigger met, damage named.
- **NO-BREACH** — attacks ran, none fired. Report it as ***"no breach reachable by the
  probes actually run"***, with the probe list, the recall floor, and the residuals.
  **This is NOT survival.**
- **SURVIVAL** — requires a **census** by mechanical rule with every member adjudicated,
  **plus** the battery shown non-vacuous on the decoy, **plus** the floor declared.
  **Sweeps are not a census.**

---

# V — FENCES: what a seat may not do

1. **You may not adjudicate your own instrument's held-out slice.**
2. **You may not adjudicate a cell you supplied a prediction to.** If you have a stake,
   **supply the FACT and refuse the PREDICTION** — then say in the relay that you refused.
3. **You may not construct a control after seeing which attacks fired.**
4. **You may not report a NO-BREACH as a survival.**
5. **You may not adjudicate another bench's computations.** Supply candidates; let them
   seal.

## Two reasoning fences

> **ELIMINATION IS NOT EXHIBITION.** *"Three slots, two pinned, one left"* presupposes the
> answer is an **assignment**. Mine was right about the pairing and wrong about its shape
> — the real structure was **diagonal**, and a coordinate dictionary was refuted 0-of-6
> exhaustively. **An elimination argument smuggles a SHAPE along with the count. Fence
> both.**

> **BUILD THE OUTCOME SPACE SO THE TYPED NEGATIVE CAN LAND.** *Same-object?* questions
> have three outcomes, not two: **JOINED / DISSOLVED-BY-A-FORCED-REASON / DISTINCT.** A
> cell that can only return JOINED or DISTINCT will mis-score the middle — and the middle
> is what actually happened the last two times this corpus asked (*"the coincidence
> carries ZERO bits beyond membership"*). **A control that fires on the null is worth more
> than the positive it protects.**

---

# VI — HOW AN AUDITOR FOOLS THEMSELVES

1. **Typing a search-claim as a deductive one.** A counterexample is independent of the
   search that found it. **"I looked and it isn't there" is not** — and in this corpus
   that claim has failed for structural reasons repeatedly.
2. **Killing a word nothing depends on.** Check *first* whether any consequence uses it.
3. **Attacking the wording instead of the steelman.** Mount every attack against the
   strongest restatement you can write, and **put the restatement in the report.**
4. **The prestige gradient.** Defect-yield flatters the audit seat — the same incentive
   the target had. **Assume your grades run one tier high.**
5. **Sealing, then improving.** Amendment file, one tier down.
6. **Treating a null as a personal loss.** *"This is worthless," asserted without running
   the gate, is as much an overclaim as "we proved it."* **An auditor who cannot deliver a
   census-grade null is not an auditor.**
7. **Forgetting that the verdict has a resource consequence.** Say what the bench does
   differently under each outcome, or the pass is theatre with hashes.

---

# VII — WHAT YOU OWE THE THING YOU ARE ATTACKING

**In the same document that tries to kill it:** what it conceded before you arrived, what
it fixed on being told, and where its own reading was right and yours was not.

> On the pass this manual is drawn from, the target had **already** conceded its
> post-hoc hazard, **already** graded its own supporting corpus at zero, **already**
> flagged its weakest identification, and **adopted my bar verbatim** — before I ran.
> **And its reading of the decisive question was RIGHT and mine was wrong**, confirmed by
> me, having sealed the trigger first.
>
> **That belongs in the verdict at the same volume as the two findings that landed.** An
> audit that only records what it broke is a scoreboard, not a record.

---

**Standing:** this manual is drawn from one window. **It is a floor, not a survey** — and
its own rules say to treat it that way.
