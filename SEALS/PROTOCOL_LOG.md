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

## Digest status

| seat | lane | digest | in |
|---|---|---|---|
| cc3 | obstruction | `e70cf113…` prereg · `17c8538d…` findings | ✅ `fa71ff2b`, `6d227bae` |
| chat1 | construction | `a1d67c09…` (6465 bytes) | ✅ owner-relayed |
| **cc** | **corpus** | — | ⏳ **outstanding** |

**No content publishes until all three are in.** cc3's findings file is
gitignored to make that mechanical rather than a promise.
