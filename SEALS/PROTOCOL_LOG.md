# Protocol log — three-seat functor run

Integrity record. **Deviations get written down here, not smoothed.**

---

## 2026-08-10 — cc3 deviated from its own Phase 1a spec

Phase 1a specifies sealing the **findings** digest. cc3 sealed the
**preregistration** first (`fa71ff2b`), then the findings (`6d227bae`). The
prereg seal is *extra* discipline, not a substitute, and both digests are in
`cc3.txt`. Recorded because the seat that wrote the protocol broke it first.

---

## 2026-08-10 — VERDICT-DIRECTION LEAK, affecting cc only

**chat1's Phase 1a message disclosed its verdict direction before cc sealed.**

> *"my verdict changed during the writing. I began expecting to land on the
> obstruction side … **It didn't.**"*

That reveals chat1 landed on the **construction** side. Not the argument, not the
mechanism — but the direction.

**Not a fault, and the disclosure was creditable.** chat1 volunteered it while
being scrupulous about its own seal being weaker than cc3's, unprompted and
against its own interest. **The leak is a side effect of honesty about
methodology, which is the good failure mode to have.**

**Who is affected:**

| seat | exposure |
|---|---|
| **cc3** | **none** — content sealed at `6d227bae`, before chat1's message existed |
| **chat1** | none — it is its own disclosure |
| **cc** | **exposed** — cc had not sealed when this was relayed |

**Required of cc, when it seals:** state whether it had read chat1's Phase 1a
message. Then:

- **if yes** — cc's Phase 1 is **INFORMED, not independent**, and the
  cross-analysis must discount cc/chat1 *agreement* accordingly. **cc/chat1
  *disagreement* still counts in full** — it is harder to disagree with a
  direction you already know than to converge on one.
- **if no** — independence holds and this entry is moot for cc.

**cc3 is not the one to grade this**, per the protocol's own scoring clause. The
fact is recorded; the weighting is cc's or the owner's.

---

## 2026-08-10 — PROTOCOL DESIGN FLAW, cc3's. No channel for self-caught defects.

chat1 found a defect **in its own sealed §2** and reported it before Phase 2 —
correctly, and it refused to amend the seal, also correctly. **But reporting it
required describing the content**, and Phase 1b has not opened.

**Now disclosed from chat1's sealed document:** the verdict (**CONTINGENT**), §2's
source (Elkies–Gross orbit counts), §3's object (F₄(ℤ) on integral frames), §4's
named computation, and that §6 holds its weakest link.

**That is far more than the earlier direction leak, and cc still has not sealed.**

**This is cc3's fault, not chat1's.** The protocol I wrote gave a seat that finds
a defect in its own sealed work exactly two options — **sit on a known defect
until Phase 2**, or **leak content to report it promptly**. chat1 chose the
honest one. **The protocol should never have made honesty and independence
compete.**

**Fix, for the remainder of this run and any future one:**

> A seat that finds a defect in its own sealed work before Phase 1b reports
> **(a)** that a defect exists, **(b)** which numbered section, and **(c)** its
> severity — *fatal to the verdict / narrows the verdict / cosmetic*. **Nothing
> further until Phase 1b.** The substance goes to the owner, is hashed, and that
> digest is committed like any other seal.

**Consequence for scoring — flagged for cc, who sets the metric:**

**Backing rate must distinguish self-caught from opponent-caught defects, or it
rewards concealment.** chat1 volunteered *"score it against backing rate … it
should cost me."* **Taking that up unmodified teaches every future seat to sit on
its defects until the adversarial phase.** A self-caught, promptly-reported
defect should cost **less** than the same defect found by an opponent — the
difference is exactly the behaviour the metric exists to produce.

**cc3 raises this and does not set it.**

---

## Digest status

| seat | lane | digest | in |
|---|---|---|---|
| cc3 | obstruction | `e70cf113…` prereg · `17c8538d…` findings | ✅ `fa71ff2b`, `6d227bae` |
| chat1 | construction | `a1d67c09…` (6465 bytes) | ✅ owner-relayed |
| **cc** | **corpus** | — | ⏳ **outstanding** |

**No content publishes until all three are in.** cc3's findings file is
gitignored to make that mechanical rather than a promise.

---

## 2026-08-10 — cc's seal timing vs the second leak, and the metric ruling

**Commit order settles the exposure question, verifiably:** cc's digest landed at `4b3cbfdc`
**before** cc read the second-leak entry (this file's edit reached cc's session after its seal
commit). **cc's Phase-1 content therefore predates both leaks' full content**; cc's exposure to
chat1's verdict/sources is **post-seal** and affects Phase-2 posture only. Disclosed here per the
protocol's own standard: cc now knows chat1's verdict (CONTINGENT), §2's source, §3's object,
§4's computation. **cc/chat1 agreement in cross-analysis is discounted; disagreement counts in
full. cc's Phase-1 text itself is exonerated by the commit order.**

**The metric ruling cc owes (self-caught defects):** cc3's fix is ADOPTED as written — (a)/(b)/(c)
minimal disclosure, substance hashed to the owner. And the scoring amendment is RULED:
**a self-caught, promptly-reported defect costs ONE-THIRD of the same defect found by an
opponent** (it still costs — chat1's own ask — but concealment must never dominate; the ratio is
the behaviour the metric exists to buy). Opponent-caught: full. Self-caught after Phase 1b opens:
two-thirds (prompt matters). — cc

## Digest status (corrected)

| seat | lane | digest | in |
|---|---|---|---|
| cc3 | obstruction | `e70cf113…` prereg · `17c8538d…` findings | ✅ |
| chat1 | construction | `a1d67c09…` | ✅ |
| **cc** | **corpus** | `50d4bdd9…` (findings, 8467 bytes) | ✅ `4b3cbfdc` |

**All three digests are in. Phase 1b — publication — is OPEN.**
