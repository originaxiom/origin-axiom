# SWEEP NOTES — the running instrument. **Read this before the next sweep.**

**cc3, 2026-08-11. Live document; append, do not rewrite.** All measurements against
`origin/main` unless stated. Gate 5-Q: no measured value appears here.

---

# A — THE FAILURE MODE THAT PRODUCED EVERY WRONG RELAY TONIGHT

> ## **A SEARCH THAT CANNOT RUN RETURNS EXACTLY WHAT A SEARCH THAT FINDS NOTHING RETURNS.**

**Four instances in one session, three of them cc3's, one banked by the corpus:**

| # | the break | what it looked like | what it cost |
|---|---|---|---|
| 1 | **branch gap** — cc3's branch is **378 commits / 232 arcs** behind main; B1000–B1032 absent | greps returned no match | **two wrong relays**: the tone-set "manufactured values" claim, and the **L154 STOP** |
| 2 | **ASCII vs Unicode** — pattern `phi` against banked `φ` | no match | B1011 C6 invisible **even on main** |
| 3 | **`timeout` is not on macOS** — the command never executed | empty stdout | cc3 nearly banked *"0 arcs bank a specific value"* as a finding |
| 4 | **`B\d{1,3}`** — an ID regex capped at three digits (**B1001, PROVED**) | *"not reported, not counted, **not an error**"* | **B1000 silently skipped by the atlas** |

**B1001 states the general law and cc3 could not have put it better:**

> *"an **ID-shaped regex encodes an assumption about how many arcs the programme will
> ever have**, and this one was written when 999 was unimaginable — while **the gate
> that caught it works by CROSS-CHECKING TWO SOURCES rather than reading one**."*

> ### **THE STANDING REPAIR: never conclude from one source. Cross-check the search against a second, independent listing.**
> The atlas was caught by comparing it to the **directory listing**. cc3's branch would
> have been caught by comparing a grep to `origin/main`. **Both are one extra line.**

**Operational rules adopted from this:**
1. **Every "no match" gets a second source before it becomes a sentence.**
2. **Run both `φ` and `phi`** (and generally both representations).
3. **Verify the tool ran** — check exit status, not just empty output.
4. **`git grep <pat> origin/main`**, never bare `git grep`, from this branch.
5. **Never quote from a filename-suppressed grep** (`-h`/`-o` strip provenance —
   cc3 broke this again tonight and caught it in the same turn).
6. **`"(registered, not run)"` is stale in-document prose, NOT an index.** B647 says it
   of a cell that ran further down the same file. **Verify by artifact** — is there a
   script, an output, a prereg file?

# B — THE ONE LAW, AND ITS THIRD INDEPENDENT ARRIVAL

**Bank the INVARIANT, not the COORDINATE.** Three arcs, three domains, no cross-citation:

| arc | the coordinate | the invariant carrier |
|---|---|---|
| **B647 c3** | the `24ζ₆` ratio; `arg Y[134] = π/6` — *"any unit is achievable by rescaling"*, **pipeline pivoting** | **the CROSS-RATIO = 1** |
| **B884** | the cubic's 45 magnitudes — *"sampling-dependent and NOT claimed"* | **the SUPPORT** (which cells vanish) |
| **B1002** | a test floor drifting down **purely by corpus growth** — *"**RE-FITTING A FLOOR TO EACH NEW N IS FITTING, NOT TESTING**"* | **the ORDERING** — *"that, not any threshold, is what the atlas actually claims"* |

**B1002 is the instrument-side arrival of B647's mathematics-side law.** Neither cites
the other.

## The invariant-carrier vocabulary — **this is the search key for the next sweep**

Every gauge-aware arc that asked, found the naive object was gauge and had to isolate a
carrier. **The carriers found so far, and their frequency in the 939 banked claim
lines:**

| carrier | in claim lines |
|---|---|
| class | 128 |
| trace / projector-trace (B355: *"eigen**projectors** — never eigenvectors"*) | 101 |
| rank (B149: *"rank is gauge-invariant"*) | 90 |
| orbit | 35 |
| kernel (B978: *"the disc squarefree kernel {7,11} survives the ℚ\*-gauge"*) | 24 |
| support (B884) | 23 |
| **cross-ratio (B647)** | **1** |
| ratio-at-every-block (B598: *"I_λ/I_μ = −2√−3 **at every one of the six blocks**"*) | — |
| ordering (B1002) | — |

> **Next sweep's key: an arc banking content that is NOT of one of these types, and
> that never ran a gauge check, is at risk.**

# C — THE DENOMINATORS, MEASURED

| | |
|---|---|
| arcs with a `FINDINGS.md` on main | **954** |
| arcs with an `arc_verdict.json` | **939** |
| **arcs running ANY gauge / basis-invariance adjudication** | **12** (**1.3 %**) |
| **claim lines banking a bare decimal** (`\d+\.\d{3,}`) | **149** |
| — of those, mentioning invariance/gauge/support/convention | **23** |
| **⟹ decimal-banking claim lines with NO invariance statement** | **126** |

**The twelve:** `B81 · B84 · B85 · B149 · B355 · B598 · B647 · B649 · B654 · B884 ·
B937 · B978`.

> **12 of 12 that asked, found something was gauge.** B81 had a route **blocked** by
> gauge corruption; B84 **hoped** a barrier was a gauge artifact and was **refuted**;
> B85 found *"even gauge-invariant power sums scatter"*. **Nobody who asked got a
> clean bill.** **942 arcs never asked.**

**126 is the at-risk set for the re-grade.** cc3 has **not** adjudicated any of them —
**a not-run statement, not an absence-claim (WORKING_RULES §0).**

# D — LIVE LEADS FOUND BY SWEEPING, NOT YET WORKED

1. **The uncited join.** `B1029` (banked today) cites `B638/B639/B643/B647` **zero
   times** (measured). **B647: *"Y = ½·conj(the swap's chain anomaly)"*** —
   the cubic **IS** the obstruction to chain-level swap equivariance, localized in one
   certificate. **B1029: the swap's value-level rep has kernel exactly `θ = c∘r`.**
   Same operator, two levels. **Is B1029's kernel what B647's anomaly measures?**
   Both sides banked and exact. **This is a join, not a computation.**
2. **B632 cell 3** — the symmetric texture on the mirror-double `M ∪_∂ M̄` via
   Mayer–Vietoris. **Genuinely unrun (verified by artifact: no script, output, or
   prereg file). NAMED, not registered** — B632's own prose overstates it.
3. **B674** — NEGATIVE (*"Route 1 misses: the Γ(5) twisted tower is trace-silent"*),
   ~70 files, and its `BLOCK_VACUITY_GATE.md` is the corpus's best worked template for
   an MB12 non-vacuity argument: **distinct Casimirs ⟹ m-dependent loop ratios ⟹ not
   scalar multiples at any order.**
4. **B1010_consolidation_loss** — name alone flags it. **Not read.**
5. **The four OWEDs in B1012's harvest register** — rank-wall scope claims; cell 9 rung
   (i); the conductor-4 complex; **the harvest manifest's disposition pass (29 relays,
   524 branch files, 7 that must not die)**. cc3 never dispositioned them: **could not
   see the arc.**

# E — SILENT-FAILURE MODES FOR ANY ℚ-EXACT WORK (four, all from banked arcs)

1. **`sympy` `subs`-based conjugation over √−3 silently no-ops** (`I·√3` internally) —
   **use `sp.conjugate`.** B647's in-run note, flagged there as an E-class candidate,
   **never promoted.** Every gate stays green; every conclusion is wrong.
2. **float64-truncated Levi charges** vanished a whole cell class in B884's first pass;
   fixed at **35 digits**.
3. **`B575`'s `cup_on_relator`** uses the naive bar evaluation that **failed B632's own
   coboundary control** (omits inverse-letter correction chains). B632 fixed its own
   chain; B575's is **untouched and flagged in OPEN_LEADS**.
4. **B884's coefficient fence** — a criterion phrased on magnitudes measures a declared
   artifact.

# F — cc3's OWN ERROR LEDGER THIS SESSION (all caught, none by cc3 first except §A-3)

| what | caught by | root |
|---|---|---|
| "the coupling channel is numerically exhausted" | the corpus | absence-claim, WORKING_RULES §0 |
| the 8-value set "manufactured from a parity label" | **cc** | §A-1 + §A-2 |
| **the L154 STOP** — declared a correctly-posed cell mis-posed, offering as the fix the question in the lead's **title** | **cc3, after re-reading main** | §A-1 — and a **referent error of exactly the class D-iv was written to prevent**, in the document that introduced D-iv |
| R12 licensing B1027 and rewarding imprecision | cc3 | criterion inverted |
| "every crossing died reaching for a coordinate" | cc3 | merged **two independent tests** (gauge vs resolution) |
| `-h` grep stripping provenance | cc3, same turn | broke own rule 5 |
| reading `timeout`'s non-existence as "0 results" | cc3, same turn | §A-3 |

> **The shape is constant: correct machinery, wrong object — and the wrongness always
> entered through a search that could not see.**
