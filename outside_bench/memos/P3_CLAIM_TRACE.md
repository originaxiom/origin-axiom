# MEMO 149 — THE CLAIM TRACE: P3's DRAFT AGAINST ITS OWN ARCS

**Banked 2026-08-29.** Seal: `seals/P3_CLAIM_TRACE_PREREG.md`, pushed **before** any retrieval.
Certificate: `certificates/p3_claim_trace.py`, pinned to **`89affd5b`** — the paper's own commit,
not this lane's default pin, because the draft was written against that corpus state.
**1119 arc records.** Follows memo 148, which could not run this check because §§5–6 carry no
arc references.

---

## 0. VERDICT

**One load-bearing drift, one confirmed upgrade to memo 148, three of the spec's own headline
results dropped, and zero arc citations — against a draft whose claims otherwise trace accurately.**

| cell | outcome | one line |
|---|---|---|
| **D1** | **D1-NOISY** | mechanical retrieval's top hit was wrong or materially incomplete on **18 of 50** claims — **36%** |
| **D2** | **D2-DRIFT** | 2 drifts in 50; the rest trace accurately, several of them exactly |
| **D3** | **D3-STALE** | the drift's arc is superseded twice over by arcs the draft does not carry |
| **D4** | **D4-GAPS** | zero arc citations; three of the spec's own headline results absent from the draft |

**The draft's claims are, with two exceptions, honestly sourced.** That is the majority finding and
it should be said first. §6 in particular — the section withdrawing its own supports — is the most
accurately cited passage in the paper.

---

## 1. D1 — THE RETRIEVAL WOULD HAVE LIED, AND BY HOW MUCH

The seal put this cell first because B1210's sweep found clause-scoped matching cut its own flag
count from 15/24 to 5/24 (*"mostly noise"*), and because this bench has produced three keyword
false positives of its own this session. **Measured: on 18 of 50 claims (36%) the top mechanical
hit was wrong or materially incomplete.** Over the 25% threshold, so **D1-NOISY**.

The instructive failures:

- **C02** — *"E₆ is the only exceptional label an imaginary quadratic field can reach."* Mechanical
  top hit: `B1174`, unrelated. The **correct arc is `B239`**, which never entered the top four:
  *"For unimodular elements disc = t²−4det, so the only imaginary quadratic trace fields are ℚ(i)
  and ℚ(√−3) …, and E₇'s ℚ(√2) is parity-excluded."* An old, low-numbered, exactly-on-point arc,
  invisible to token overlap because it shares almost no vocabulary with the claim it proves.
- **C30** — the rank-reduction claim retrieved `B1210` (a sweep *about* citations) over `B953`
  (the arc that computes U(1)_ψ and U(1)_χ). Sweeps outrank sources, because sweeps talk about
  everything.
- **C40**, **C50**, **C07**, **C15** — all mis-topped.

**The transferable point:** the failure mode is not false positives on nonsense, it is *plausible
arcs that discuss the right area without asserting the claim*, plus **true sources that share no
vocabulary with the sentence they support**. A citation pass run mechanically would have produced a
bibliography that looks right and is wrong in a third of its rows.

---

## 2. D2 — THE DRIFT THAT MATTERS: AN ARC TITLED "NOT CLOSED" USED AS A CLOSURE

The paper leans three times on one lemma:

- §6: *"an invariant selector provably cannot pick a point of its own orbit."*
- §7, the *family, VEV, filling* row: *"**Closed, in the only available form.** An invariant
  selector cannot pick a point of its own orbit, so **a finite menu is terminal, not a
  deficiency**."*
- §8, under *What is permanent*: *"The finite labels **will not reduce further** either … a finite
  menu is **the terminal state and not a deficiency**."*

The lemma is true and is exactly `B990`'s theorem. **The closure the paper draws from it is not.**
`B990` is titled **"X10 SHARPENED, NOT CLOSED"** and says, in the same breath as the lemma:

> *"**Exactly two routes exist**: SHRINK THE GROUP (ℚ → ℤ …) or ADD NON-INVARIANT STRUCTURE. The
> concrete next computation is the count of G(ℤ)-orbits inside the object's G(ℚ)-orbit … **IF IT IS
> 1 the integral orbit IS a canonical point up to G(ℤ), which is exactly what a VEV direction
> needs.**"*

**And D3: the route was pursued, and it is partly succeeding.**

- **`B1093` (PROVED)** — *"**EVERY obstruction candidate for Route A's integral-orbit count is
  trivial at proof grade — the obstruction is ABSENT**; the OWED residual unchanged: identifying
  WHICH Kato-Yukie/Bhargava quantity counts integral orbits."*
- **`B1099` (OPEN)** — *"ONE STRATUM DECIDED FREE: Krutelevich Cor 16 … the FULL norm-preserving
  group's integral orbit at the object's invariant is **UNIQUE** (the coarse half of Route A,
  **closed positive**)."*

So the corpus's state is: a live programme, one stratum closed positive, every obstruction proved
absent, one literature-lane residual owed — aimed at exactly the reduction the paper calls
**permanent**. The draft declares terminal a row the programme is actively and successfully
reducing, and mentions none of it.

**Direction of the drift: in the paper's favour.** It converts an open, advancing row into a closed
one, in the freedom ledger the paper calls its spine and in the section titled *the wall*.

**REPAIR** — the honest form is available and costs the paper nothing, because it is a *better*
sentence: *the finite menus are terminal against any invariant selector; whether they reduce under
the arithmetic route (integral orbits) is open, one stratum is already unique, and that is where a
reduction would come from.* A named live route reads stronger than an asserted permanence.

> **Note on my own adjudication.** My first reading stopped at `B990` and had the finding as "an arc
> that says NOT CLOSED is cited as closed." Following the route forward changed it: the point is not
> that the arc hedges, it is that **two later arcs advance past it**. The finding got sharper by
> being checked, not weaker — and I would have banked the shallower version had I stopped at the
> first arc, which is the D1 lesson landing on me rather than on the draft.

### The second drift: the conductor, upgraded from memo 148

Memo 148 found Theorem 2.1 turning on the undefined word *conductor*, and showed that under the
standard reading three further metallic grammars (m = 11, 14, 39) acquire a McKay-type modulus.
**The corpus is ahead of both the paper and me.** `B1002` is titled *"THE CONDUCTOR IDENTIFICATION
IS RIGHT, AND **CONDUCTOR NAMES TWO THINGS**"*:

> *"TWO DISTINCT QUANTITIES BOTH CALLED CONDUCTOR IN ADJACENT LAWS, a live terminology collision …
> B675's cusp order's conductor is golden 4 and silver 2, while B666's word's own conductor (the
> shadow modulus) is golden 5 and silver 8 … **so any future arc using the word must say which**."*

The paper uses the word without saying which. **It re-opens an ambiguity the corpus closed and
violates a rule that corpus explicitly banked.** `B1002` also supplies a mechanism the paper drops:
the golden's shadow is the McKay group because *both* conditions hold — 120 = |2I| with N ∈ {3,4,5}
complete, **and** gcd(4,5) = 1 makes the reduction unramified, while the silver fails both.

**And `B997`'s own scope limit, absent from the draft:** *"THE END REACHED IS **E8, NOT E6** … this
does **NOT** rescue the E6 chain's object-specificity."* The draft presents this theorem in §3 as
one of exactly two surviving facts, under the sentence *"Everything this paper claims is built on
them and on nothing else"* — while §4's arena is E₆ data (the 72 roots, the 27) reached by the 2T
step §2 declared generic. The draft names E₈ **once**, inside the theorem's proof, and never says
its unique survivor m = 1 lands there. A referee must compute m² + 4 = 5 ⟹ |SL(2,ℤ/5)| = 120 = |2I|
to discover that the surviving uniqueness and the argument it is supporting sit at opposite ends of
the exceptional series.

---

## 3. D4 — ZERO ARC CITATIONS, AND THREE HEADLINES DROPPED

**The draft cites no arc anywhere.** A mechanical scan for B-numbers returns nothing. This is a
known fact about the draft's stage — the spec lists per-claim citations as outstanding — and it is
reported as a measurement, not a charge.

What is not on the spec's outstanding list: **three of its own headline results are absent from the
draft entirely**, verified by keyword scan over the full source.

| dropped | spec's billing | draft |
|---|---|---|
| **the quine** (`B1184`) — the object names itself in mirror-even letters and provably cannot sign itself | movement III's closing claim | `quine`, `sign itself`, `self-nam` — **0 occurrences** |
| **the Φ₃ three-face figure** (`B1195`/`B1200`) — one invariant as saddle equation, founding obstruction and boundary structure | *"**The closing figure**"*, and **F3** in the figure list | `saddle`, `partition function`, `three faces` — **0** |
| **E₆ boundary ≅ M(𝕆,ℂ)** (`B882`/`B904`, restated in `B968`) | movement I's opening evidence | `Jordan`, `Albert`, `octonion`, `M(𝕆` — **0** |

`B1195` is banked PROVED and carries the saddle equation *"the SADDLE EQUATION IS THE FOUNDING
QUADRATIC u²+u+1 = 0 exactly"* — the spec's own closing image, and the draft does not use it.
Whether to restore them is an editorial call and not this bench's; **that they are gone appears to
be unrecorded**, which is the reportable part.

---

## 4. WHAT TRACED CLEANLY — the majority, and it deserves saying

Verified against the arc text, not against a keyword hit:

- **C13/C14** (252 / 222 / 2, zero object tokens) → `B1170`, exact.
- **C16, C18** (the rank-3 sector; the linear conditions and the cubic) → `B1160`, exact.
- **C19** (the ℤ₆ global form, six Weyl realizations) → `B1080`, exact.
- **C21** (termination, with a positive control) → `B863`, exact.
- **C22** (the adjoint gives no 27 fermion mass) → `B978`, which supplies a *mechanism* the draft
  omits: class(27) has order 3, so 2·class(27) ≠ 0 and the 78 cannot occur in 27⊗27.
- **C26** (216-cell grid, 18 sealed targets, zero) → `B1137`, exact.
- **C29** (the 64's invariant content is zero) → `B1140`, exact.
- **C32/C34/C35/C36/C38** (one class, the equivariance, the det = −1 pair, selector-freedom, κ) →
  `B1183`, `B1192`, `B1196`, `B1195`, exact.
- **C41/C42** (the two withdrawn supports) → `B1216`, **accurately, including the reason**: the
  clause has *no failing branch*, and the partner is non-canonical at both the field level (30 of 37
  fields) and the embedding level. **This is the best-cited passage in the paper.**
- **C44/C45** (c((E₆)₁) = 78/13 = 6; the six-clause condition list and the empty candidate set) →
  `B1023` and `B1216`, and the draft matches the **newest** arc. I looked for staleness here and did
  not find it.
- **C46/C47** (λ: unit rank 0 ⟹ regulator identically 1; the exhaustion withdrawn) → `B1216`, exact.
- **C48** (ℙ(B₀): 3 → 2 → 1, points require 0) → `B1206`, exact, including which condition is linear
  and which nonlinear.
- **C50** (no unique 4d theory; unrestricted uniqueness refuted) → `B1215`, exact.

---

## 5. WHAT THIS CELL DID NOT DO, AND ONE THING IT OWES

Bound by the seal: it did not fill the 467-row disposition (an editorial call, cc's and the
owner's); it did not rank severity; and no claim is called false for being hard to trace.

**Two rows I could not settle, reported as audit limits rather than defects:** **C01** (the
canonical-linkage argument giving probability 1) traces to context in `B993`/`B996` but to no arc
that banks the argument itself; **C07** (the programme's own base-rate lag) has no arc and should
not — it is a claim about the programme's history, and my extraction rule over-collected in
admitting it.

**And one debt, filed against this bench and not the draft.** Tracing **C27** — §5's sharpest
sentence, that extending the regulator basis with the object's own complex volume leaves the count
at zero — surfaced `B1217`'s evidence-contract charge:

> *"cloud's EXTENDED run — the V-NEG headline itself — is **NOT REPRODUCIBLE AS COMMITTED**. The
> file at `outside_bench/certificates/vol_basis_extended.py` contains the BASIS BUILDER, not the
> extended probe; **no committed certificate carries the involves_regulator gate**."*

**Checked, and the charge is correct.** That is memo 143's headline, and it is **bench error #15**
— the same class flagged twice before in this lane, recurring on the very next cell after the fix.
The paper's §5 therefore states, as its sharpest form, a result that at the pin no committed
certificate reproduces. `certificates/vol_basis_probe.py` is written and banked and the full grid
is running; **memo 143 stands or is corrected on what it returns, and that outcome is not assumed
here.**
