# Referee report, round 2 — the revision

**Manuscript:** revised `main.tex` + `anc/`, dated 2026-09-17, against my report of the same date
(`REFEREE_REPORT_2026-09-17.md`). Repository state reviewed: `origin/main` at `21c47a51` (S19).
**Recommendation: minor revision.** The substantive fix — the one that mattered — is done and
verified. Three defects survive, two of them recurrences of items I raised, and all three are in the
verification machinery rather than in the mathematics. None is more than a few lines' work.

I re-checked the fixes rather than taking the changelog's word for them, and I checked the revision
for anything newly broken. The paper's mathematics is untouched by this round: the only claim-bearing
edits are the census-drift paragraph, two percentages, and one added hypothesis, all verified below.

---

## 1. Status of the six changes I asked for

| # | request | status |
|---|---|---|
| 1 | fix `.gitignore` so the B1419 census ships; runner names failing tests | **done** |
| 2 | regenerate or drop `anc/REPORT.md` | **half done** — regenerated with correct counts, but certifies PASS on a seals-only run, discarding a green the locks would have given (§2.1) |
| 3 | rebuild the manifest so `git_head` matches its contents | **not done** — the recorded commit still does not resolve (§2.2) |
| 4 | fix the census-drift population | **done, well** |
| 5 | Figure 1 caption; sin²θ_W; MFP hypothesis; manifest wording | **3 of 4** — one of three sin²θ_W sites survives (§2.3); manifest wording unchanged |
| 6 | framing: title, abstract, the 53/57 ratio, the index wording | **not adopted** (§4) |

### What is properly fixed

- **`.gitignore`.** Negation rules now exist for both
  `frontier/B1419_the_arithmetic_fillings_corrected/verification/*.jsonl` and
  `frontier/B1137_regulator_probe/results/*.jsonl`, the census file is tracked, and
  **`tests/test_b1419_arithmetic_fillings.py` now passes — 5 tests, 10 s**, on a fresh worktree of
  `origin/main`. This was the worst defect and it is gone. The sweep for other locks reading
  untracked data, which I did not ask for, is the right generalisation — **and it holds**: I scanned
  all 147 manifest locks for literal data filenames, resolved them under `frontier/`, and found
  **zero** files that a lock reads, that exist on disk, and that are untracked. (Method's limit: a
  lock building a path dynamically would escape this scan.)
- **The new regression lock checks trackedness directly.** `test_b1424_referee_defects.py` carries a
  `_tracked()` helper that shells out to `git ls-files --error-unmatch`, so the class of defect — not
  just the instance — is guarded on the data-file front. That is the right shape, and it makes the
  gap in its percentage test (§2.4) the more conspicuous.
- **`run_package.py`** now passes `-rf --durations=5 --color=no` and strips ANSI before parsing, so a
  failing run names its failures. Exactly the fix needed.
- **The lock suite now passes end to end**, which is better than the revision claims for itself. On a
  fresh worktree of `21c47a51` I ran `run_package.py --seals --locks` to completion:

  ```
  seals: PASS 21/21
  locks: PASS 147 lock files: 727 passed, 14 skipped in 847.93s (0:14:07)
  ```

  **Zero failures.** The changelog's "the package's remaining failures are named rather than
  mysterious" undersells the state: the harvest lock's six rows were evidently rowed, and the flaky
  subprocess lock passed here. Against round 1 (10, then 9, then 5 failures) this is a clean green,
  and it is the first run of this package I have seen pass.
- **The census-drift paragraph** is rewritten to carry both triples, name which population each is
  taken over, and say that an earlier version had it wrong. The numbers are right: I had measured
  33.00 → 33.88 → 31.38 on the one-cusped census and 34.25 → 29.38 → 21.12 on the full one, and both
  are quoted correctly. The new conclusion — that the door is *not* an artefact of the census's small
  end, so the genericity argument is stronger — follows from the corrected figures.
- **Figure 1** now reads "Fifty-three links are forced" and its tick loop draws 57 ticks under a
  57-link axis. The chain table is intact: 57 rows, tally 36/8/6/4/2/1, axioms at 3, 4, 5, 18, none
  in 6–17. The appendix still has 67 rows.
- **The Menal-Ferrer–Porti hypothesis** is now carried, and **the translation is correct** — I
  checked it at the source rather than against the paraphrase. MFP §1 states: *"for every positive
  integer n there exists only one complex irreducible representation Vₙ of SL(2,ℂ) **of dimension
  n**. Moreover, Vₙ is **(n−1)-th symmetric power** of the standard representation."* So the source's
  n ≥ 2 is exactly m ≥ 1, and the paper's "m ≥ 1 (the source's n ≥ 2)" is right, as is its added
  remark that the theorem says nothing about the untwisted case.

---

## 2. What is still wrong

### 2.1 `anc/REPORT.md` still certifies PASS without having run the locks

The report was regenerated — fresh timestamp, and the counts now match the manifest (67 claims,
95 pairs, 21 seals, 147 locks) instead of the stale 54/75/111/18. But it is **29 lines long**: a
header, the manifest line, a `## Seals — PASS (21/21 match)` section, and

> **Overall: PASS.**

There is **no `## Test locks` section at all.** It was produced by `run_package.py --seals`, not
`--seals --locks`. So the shipped certificate is green on a run that never executed the thing the
package exists to execute.

This is the same defect as my §4.2 in a new form, and it is now sharper rather than softer, because
the changelog for this very revision says in its own words that locks still fail:

> *The package's remaining failures are named rather than mysterious: the harvest lock fires
> correctly on six genuinely unrowed audit-seat pre-execution documents … and one subprocess lock
> whose timeout was tuned to an idle machine.*

A reader opening `anc/` sees "Overall: PASS" beside a manifest of 147 locks, with nothing indicating
which steps produced that verdict.

The mechanism is visible in `run_package.py`: `all_ok` is initialised to `True` and is only `&=`-ed
against steps that actually ran, so any subset of steps that passes yields `Overall: PASS`. A run
with `--seals` alone therefore cannot fail.

**The sting here is not that the verdict is wrong — it is that you gave up a green you had earned.**
As §1 records, I ran the full package on this revision and it passes: 147 lock files, 727 passed,
14 skipped, **zero failures**. A `--seals --locks` run would have produced a genuine "Overall: PASS"
backed by a `## Test locks — PASS` section. Instead the shipped certificate asserts the same verdict
on evidence that does not reach it, in the one artefact whose entire purpose is that a reader need
not take an assertion on trust. This is the paper's own standard applied to the paper's own report.

Two fixes, and I would take both: run the locks before shipping, and have the runner qualify its
verdict by what it ran — "Overall: PASS (seals only; locks not run)". The second is three lines and,
unlike remembering a command at submission time, cannot be skipped.

### 2.2 The manifest's `git_head` still does not resolve

`MANIFEST.json` records `environment.git_head = ddff9c63`, in both the shipped bundle and the
repository's own copy at `origin/main`. **That object does not exist in the repository** —
`git cat-file -t ddff9c63` and `git rev-parse ddff9c63` both fail after fetching every ref. The
manifest was again built before the commit that contains it existed; S19 landed as `21c47a51`.

The changelog says "the rule is now in the submission recipe", which is a procedure, not a check.
The shipped artefact still violates it, so the recipe did not hold on the first run after being
written. `build_manifest.py` should refuse to record a `git_head` that is dirty or that does not
contain the files it just catalogued — again a few lines, and unlike a recipe it cannot be forgotten.

### 2.3 The chain table ships one stale row, and its drift gate samples 9 of 57

This is the most interesting of the three, because it explains the near-miss in §1's item 5 and
because it touches a guarantee the paper makes in its own text.

The changelog says the 0.9 % figure was "stated in three places" and corrected. Two were: the
summary and the non-claim both now read 0.8 %. The third was not. **Link 43 of the chain table still
reads `$\sin^2\theta_W$ by 0.9\%`** — in the repository's `main.tex`, in the shipped bundle, and in
the submitted PDF, where it renders as *"(α_s by 35%, sin²θ_W by 0.9%); the desert is dead as a
mechanism"*.

That row is *generated*. Running `scripts/checks/paper_chain_table.py --tex` on the current tree
emits link 43 with **0.8 %**. So the shipped paper disagrees with its own generator:

```
link 43  generator: ... known to ($\alpha_s$ by 35\%, $\sin^2\theta_W$ by 0.8\%); the desert is dead ...
         paper    : ... known to ($\alpha_s$ by 35\%, $\sin^2\theta_W$ by 0.9\%); the desert is dead ...
```

Comparing every generated row against both files: **exactly 1 of 57 rows is stale**, and it is
link 43. (`referee_2026-09-17/scripts/r2_chain_table_drift.py` does this comparison and prints the
pair above.)

The paper says of this table (§3):

> *the table itself is generated from the ledger rather than typed --- which is how two mis-parses
> were caught while preparing it*

and the gate `tests/test_paper_chain_table.py` is meant to enforce that. Its last test ends:

```python
rows = [l for l in gen.splitlines() if re.match(r"^\d+ & ", l)]
assert len(rows) >= 46, len(rows)
for row in rows[:6] + rows[-3:]:
    assert row in tex, f"chain table is stale, regenerate: {row[:60]}"
```

It compares **the first six and last three rows** — 9 of 57. Rows 7 through 54 are never checked, and
the one stale row sits there. The gate passes. The fix is to drop the slice and iterate over `rows`;
I ran that comparison and it finds the stale row immediately.

So the guarantee as the paper states it — generated, not typed, gated against drift — currently holds
for 9 of 57 rows. Either widen the gate or soften the sentence; widening is one line and is clearly
what was intended.

### 2.4 Two smaller things

- **The new regression lock guards the instance, not the class.**
  `tests/test_b1424_referee_defects.py` is good practice and its five tests cover the tracked census
  file, the `.gitignore` negation, both drift triples and a second method. But its percentage test
  asserts the literal strings `"0.9\\%$, about fifty experimental" not in t` and
  `"$0.8\\%$, about fifty experimental" in t` — it pins the one prose site and says nothing about any
  other occurrence, which is why the generated row sailed past it. `"0.9\\%" not in t` would have
  caught it. This is worth fixing not for its own sake but because the project's own `ERROR_LEDGER`
  opens with the rule that entries are per error *class*, not per incident; the lock is written the
  other way round. Note also that the lock covers the three defects that were fixed and none of the
  two that recurred (§2.1, §2.2) — its shape is the shape of what got done.
- **`MANIFEST.md`'s header** still reads "95 establishing records" where 95 is the number of
  claim–record *pairs* and the number of distinct records is 80. Unchanged from round 1.

---

## 3. Nothing new is broken

I diffed the revision in full. Beyond the fixes, the only changes are typesetting: an `array`
package, the freedom ledger's three explicit ragged-right columns, and the chain figure's labels
rewritten as two-line centred nodes. The abstract is byte-identical. The chain table and the
appendix table are structurally unchanged and I re-verified both tallies. No new claim was
introduced, so nothing in this round needed fresh mathematical verification beyond the three edits
checked in §1.

---

## 4. The framing recommendation, restated once and then dropped

My §3 asked for three things that are judgement rather than defect: bring the title and abstract to
the standard the §4 scope note already meets; demote the 53-of-57 ratio; and say in the abstract, as
§7 already says in its scope note, that the index is a count of twisted classes rather than a
four-dimensional index. None was adopted, and the author is entitled to decline a referee's taste.
I record the recommendation as standing and will not press it again: it does not bear on whether the
paper's claims are true, only on how a reader will first read them.

---

## 5. Recommendation

**Minor revision.** Items §2.1, §2.2 and §2.3 are each a few lines and each is a check rather than a
prose change, which is the right kind of fix for a paper whose thesis is auditability. Once the
package refuses to print PASS for a step it did not run, the manifest refuses a `git_head` it cannot
justify, and the chain-table gate reads all 57 rows, the verification story will be as strong as the
paper says it is.

I will say plainly what this round showed, in both directions. The one defect that could have
invalidated a claim — the census evidence excluded from every clone — was fixed properly,
generalised to a sweep for other instances, and locked; and the package now passes end to end on a
clean checkout, 727 tests and no failures, which is the first time I have seen it do so. What remains
is a gap between what the machinery **asserts** and what it **evidences**: twice it states a verdict
broader than the run behind it, and once it ships a table row its own generator contradicts. None of
the three changes a mathematical claim, and the first of them is now understating a real result
rather than overstating an unreal one — but for a paper whose thesis is that a reader need not take
an assertion on trust, closing that gap is worth more than the three-line diffs suggest.

---

*Both rounds' reproductions are in `referee_2026-09-17/scripts/`. Round 2 additionally: a fresh
worktree at `21c47a51` with the package run end to end; `git cat-file`/`rev-parse` on the recorded
manifest commit; a row-by-row comparison of the generator's 57 rows against both `main.tex` copies;
and the Menal-Ferrer–Porti convention read from the source PDF.*


---

## 6. Addendum — §7's witness, now verified independently

Both rounds listed the index computations of §7 among the things I had **not** checked. One of them
I have now checked, from the definitions, over exact ℚ(u) with u² − u + 1 = 0 — my own field
arithmetic, Fox calculus, cohomology and restriction map, reading nothing from the project's scripts
(`referee_2026-09-17/scripts/r3_m010_index.py`).

Base data all confirms: det A = det B = 1; the relator `aabaBaaBab` evaluates to the identity;
(1, u) is a common eigenvector with eigenvalues u and −1, so ρ really is reducible and non-split;
and χ(a) = u, χ(b) = −1 is trivial on the relator and on both peripheral words `AbAA`, `babA`.

| | a₀ | a₁ | t₀ | t₁ | r₁ | n | claimed |
|---|---|---|---|---|---|---|---|
| V = Sym³(ρ)⊗χ | 0 | 1 | 1 | 2 | 0 | 1 | matches |
| V* | 0 | 2 | 1 | 2 | 2 | 0 | matches |
| ss = Sym³(ρ_ss)⊗χ | 1 | 4 | 4 | 8 | 4 | 0 | matches |
| ss* | 1 | 4 | 4 | 8 | 4 | 0 | matches |

**I(V) = n(V) − n(V*) = +1**, and the paper's stated form t₀ − r₁ gives +1 as well.
**I(ss) = 0.** And ρ and ρ_ss have the **same trace on all 400 random words tested** — as they must,
the invariant flag making the trace blind to the extension.

So §7's escape from the vanishing theorem is real and exact: a characteristic-zero, non-semisimple
local system carrying a non-zero index, invisible to every trace. That also explains why a
same-eigenvalue "irreducibility filter" is the wrong instrument here — an invariant line with
*different* eigenvalues passes it — which is the correction the audit lane's R27(c) hands back to the
main record.

**Provenance, which the paper does not state.** This witness is the audit lane's **R27**
(`audit/physical-bridge-2026-09-05`), harvested onto main as `B1413` on 2026-09-15 and verified
there before the paper's 09-17 draft. §1 lists it under "what is new"; §1 also describes the work as
"a single author with AI-assisted verification passes". That is not false — the lane is an AI seat —
but "verification" understates a lane that *originated* the result. I would name the lane.

One further thing the lane holds that the paper does not carry: on its own physical route the same
count runs the other way. Its R15/R19 obtain a net **three** on a *prescribed singular source*
ansatz — declared modelling data, explicitly "NOT an identification with the principal Riley local
system" — and its **R30 finds no zero modes at finite width** once those cores are resolved, on
m202. A stronger negative than §7 states, and it is on the branch rather than in the paper.

### 6.1 The lane's held correction is right, and it is unmerged

`CODEX_TO_CC_2026-09-16_..._HELD.md` reports that main's I-26 decision table conflates the undrilled
core with the drilled exterior. I checked the Euler arithmetic
(`referee_2026-09-17/scripts/r3_i26_euler.py`); every row of the lane's table reproduces for
k = 1, 2, 3, 5, 7:

| | χ |
|---|---:|
| Q (compact core, torus boundary) | 0 |
| N (k contractible solid arc tubes) | k |
| T (k lateral annuli) | 0 |
| C = Q \ N (drilled exterior) | −k |
| E (exterior tori minus 2k endpoint discs) | −2k |
| (C, E) | **+k** |
| (Q, E) | **+2k** |

At k = 3 both numbers are correct arithmetic — **for different pairs**. χ(C,E) = 3 is R24's model;
χ(Q,E) = 6 uses the *undrilled* Q. The table took the second where the model requires the first. And
the lane's second point is elementary and also right: n Dirac pairs carry 2n Weyl components with net
index 0 for every n, so a six-state count is not an index of six — a state sum is not an index
difference.

**So the largest chirality count anywhere in this programme is a bookkeeping conflation, the
correction has been computed, and it is sitting unsent on a branch.** It should be merged.

### 6.2 What the accumulated negatives now look like

Set the lane beside the paper and every route to a non-zero chirality count in this construction has
been closed or reduced to zero:

| route | outcome |
|---|---|
| geometric finite twists | zero **by theorem** (Menal-Ferrer–Porti + transfer) |
| the cyclic tower | zero, by two conjugations |
| the object's own reducible locus | zero on all 235 modules computed |
| non-semisimple modules on the class | **+1 — verified exactly here** — but a count of twisted classes, provably not a 4-D index, admissibility open with a prior against |
| prescribed *singular* source (lane R15/R19) | three — on declared modelling data, not the object's own representation |
| the same source *resolved* to finite width (R30) | **zero** |
| the I-26 "six" | a conflation of two pairs; and three Dirac pairs are net zero anyway |

That is a strikingly consistent body of negative evidence, obtained by independent routes, and it is
the programme's real result. It also sharpens my §3 framing point rather than softening it: a
document whose accumulated content is *this object does not deliver chiral matter, and here are
seven independent ways of seeing it* is not well titled "Standard-Model structure from the
figure-eight knot complement".

### 6.3 R30's finite-width vanishing — checked, and it holds

This was the load-bearing analytic step in the strongest negative anywhere in the programme, and I
said it needed reading rather than running. Having read it, most of it *is* checkable
(`referee_2026-09-17/scripts/r4_r30_check.py`), and all four pillars hold.

**(A) The conjugation.** The argument turns on `d_q = exp(−qF) d_A exp(qF)` for `d_q = d_A + q dF∧`.
This is right: `d(exp(qF)) = q exp(qF) dF` and A is central, so the multiplier is bounded and
invertible and gives a **chain isomorphism** — hence H*(d_q) is ordinary flat cohomology at every
fixed finite width. The document's own caveat is also right and important: the multiplier is *not*
unitary on the unchanged L², so this transports **cohomology, not the operator's spectrum**.

**(B) The complex.** For the frozen m202 core, `f · v = 0` — so it is a complex.

**(C) The Betti table**, all three rows, recomputed from the ranks:

| character | (H⁰,H¹,H²,H³) |
|---|---|
| trivial | (1,2,1,0) |
| nontrivial, P = 0 | (0,1,1,0) |
| nontrivial, P ≠ 0 | (0,0,0,0) |

**And the decisive part: P ≠ 0 at all eight nontrivial order-3 characters** (values −2 and
−½ ± i√3⁄2). "Source-C3" lives exactly there, so every nontrivial order-3 character lands in the
bottom row: **no zero modes at finite width.** R30's headline is verified, not merely reported.

**(D) The §3 chain homotopy.** Verified in every degree: `p∘i = id`, and `id − i∘p = dH + Hd` with
the document's explicit `i`, `p`, `H`. So for non-zero attachment `t` the resolved complex retracts
onto the **base** complex, not the relative one — at k = 3 that is the three relative odd classes
cancelling against three even core partners, six states gone.

**The gap, which the lane states itself and I confirm is real.** The conjugation is at *fixed* finite
width. As width → 0 the multiplier `exp(−qF)` need not stay bounded, and there is no uniform-domain
argument — so the singular three of R19 is not contradicted, it simply lives on a different domain
that the resolved theory does not converge to. §4's "light partners in shrinking wells" is explicitly
conditional on uniform bounds *not yet proved for the actual global Poisson solution*.

**What that adds up to.** The three is not the limit of anything physical that has been constructed.
It exists in a singular prescribed-source model; the resolved model that was built to make it
physical has zero; and the two are not connected by a limit anyone has established. That is a
cleaner and stronger statement of the programme's central negative than the paper's §7 makes, and
it belongs in the paper.

---

## 7. Correction: I reviewed a projection of the project, not the project

I treated `main` plus the paper as the work, then added one lane. That was wrong, and it made my
summary in §6.2 wrong. `main` is **101 commits** — a curated line. The work lives in four lanes of
~3000 commits each, two of which do not share history with `main` at all. Two results I never saw
change the picture.

### 7.1 There IS a Standard-Model-shaped chiral generation — on the tower

`claude/standard-model-derivation-0qt6ao`, **B1374/B1375, 2026-09-16** — the day before this draft.
Not "the index is non-zero": **all five charged sectors (Q, u^c, e^c, d^c, L) firing together at
±1**, a complete SM-shaped chiral generation, on the object's own cyclic covers:

| level | | generation-shaped backgrounds | count |
|---|---|---|---|
| Y₂ = m206 | | 0 | — |
| Y₃ = s961 | nothing fires | 0 | — |
| Y₄ = t12839 | | **12 800** | exactly one, ±1 |
| Y₅ = o10_150696 | | **800** | exactly one, ±1 |
| Y₆ | | **67 200** | exactly one, ±1 |

**80 800 backgrounds, every one carrying exactly one net generation — never two, never three**, with
one background per level re-derived exactly over ℚ(ζ₆₀) and ℚ(ζ₁₃₂).

**What I checked myself:** every row of the scaffolding — Y₂ ≅ m206, Y₃ ≅ s961, Y₄ ≅ t12839,
Y₅ ≅ o10_150696 confirmed by isometry, and all five H₁ groups exact against SnapPy. And the firing
signature B1375 reports on all 80 800 backgrounds, **(a₀,a₁,t₀,r₁) = (0,1,1,0) against (0,2,1,2)**,
is *exactly* the signature I independently computed on the m010 witness in §6. The instrument I
verified is the instrument this runs on.

**What I have not checked:** the 80 800 count, the one-per-background law, the exact ℚ(ζ)
re-derivations.

**What the paper does with this.** It reduces it to seven words — "on the object's own degree-four
cyclic cover t12839" — inside a list of ±1 values. `12 800`, `80 800`, "one generation",
"generation-shaped" appear **nowhere in the manuscript**.

### 7.2 And there is a computed reason why the object itself returns zero

`sep16-branch`, **xB021, 2026-09-17** — this draft's own date. The three bits act on CS ∈ ℝ/½ℤ:
A5 (knot-ness) `x ↦ x + ¼`; A6 (orientation/the squaring) and A7 (the LR/RL order) both `x ↦ −x`.
Then |⟨A5,A6,A7⟩| = 4, the orbit of the object's value 0 is {0, ¼}, and **the stabiliser of 0 is
exactly {A6, A7}** — orbit–stabiliser, 4 = 2 × 2.

So the two bits the paper calls *withheld* and *relational* are precisely **the object's own
stabiliser**, and a fixed point cannot report on its own stabiliser. 9 of 12 banked negatives are
instances of this; the 3 misses are named and are all arithmetic. Preregistered with a binding kill
condition that did not fire.

That is a structural account of §7's central negative, and the manuscript does not contain it.

### 7.3 What this does to my verdicts

- **§6.2's "seven routes, all negative" was wrong.** The tower route is *positive*. I listed
  "non-semisimple class modules: +1" without knowing it was a complete generation on 80 800
  backgrounds.
- **"Nothing new about the Standard Model"** — true of the *paper*, and it stays true, because the
  paper does not carry these. False of the *project*.
- **"The three is not the limit of anything built"** — still true, and now better: the mechanism that
  *does* produce chirality produces **one**, never three. The count of three is not merely unreached;
  it is answered in the negative by a mechanism that works.

What does **not** change: these fire on **non-semisimple** backgrounds, exactly the admissibility
question the paper itself flags and grades with a prior against, and B1375 fences itself the same way
("no physics reading, no value, no three"). xB021 says of itself "a diagnosis, not a door." So this
is not derived physics. It is an exactly-computed Standard-Model-shaped chiral structure with a clean
law, plus a computed explanation of the object's silence — and **the paper is a lossy projection that
drops both.**

The strongest recommendation of this whole review is therefore not any of §2's fixes. It is: **the
paper is not reporting the project's two best results.** One is a parenthetical, the other is absent.
