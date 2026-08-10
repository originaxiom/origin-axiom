# B1009 — the verification pass: 4 of 5 confirmed, 1 scope overreach withdrawn, 1 cc3 claim killed

**Date:** 2026-08-10 · **Seat:** cc (verification, post-model-switch) · Gate 5 untouched.

**Verdict: PROVED** (an adjudication with computed checks). **The seat that banked B1007/B1008 and
Review 42 was audited by a fresh seat under verify-don't-trust. Four items confirmed clean. One
headline inference — in five reader-facing documents — is withdrawn. One incoming cc3 claim is
refused.**

---

## CONFIRMED (4 of 5)

| # | item | result |
|---|---|---|
| 2 | **B1008's re-derivation** | **CONFIRMED.** `epoch.py` reproduces independently (0.8497 vs 0.8496 — differing only by B1008's own added probe, as expected). The epoch table reproduces exactly. **It is NOT a rationalized threshold:** the old lock was `cov > 0.85`; the replacements test a *different and stronger* proposition (the epoch gap and the density collapse) and the aggregate is recorded in a wide band that only catches gross regression. **Mutation-tested: the density lock fails if B801–900 density rises from 2.98 to 3.97** — i.e. it bites exactly when the lexicon is widened |
| 3 | **B1007's flip to NEGATIVE** | **CONFIRMED.** `branch_cell9_rung1_v2.py` carries seal hash `169e9042` (3×), matching B922's stated prereg; `import flint`, `ctx.prec`, `acb.bessel_k`, `acb_mat` all present. **B798's text does contain `"arb/mpmath Bessel"`** — it named arb, so B798 stands in full |
| 4 | **X1 / X2 re-grades** | **CONFIRMED.** Both attributed closings appear **verbatim**: B725's *"FORM forced (+ the quadratic explained), CONTENT open"*, B559's *"black-hole area-law signature is ABSENT"* |
| 5 | **kill-graph routing** | **CONFIRMED.** B995 → `ill-posed-conjunction` matches its verdict (rarity implies separation); B996 → `genericity` matches (access is generic). Both `fact_computed: true` are earned — B995 computed (1−r)⁵ and the 19.3 % uniqueness rate, B996 computed \|SL(2,ℤ/N)\| and the shadows |

## KILLED — item 1, the headline inference, in five reader-facing documents

Review 42's synthesis concluded: *"**therefore matching the Standard Model could never have
confirmed the axioms — even if it had worked**."* **Withdrawn.**

**What the cited arcs actually support is about the E₆ WAYPOINT, not the SM ENDPOINT.** B996's own
sentence: *"reaching E6 is not evidence C1–C5 were right **if a third of entry points reach E6
too**."* B993 says the same at the manifold level (~1 in 3).

> **Neither arc computes what a NON-GOLDEN grammar produces DOWNSTREAM of E₆** — the ℤ₆ form, the
> hypercharge direction, the generation count, the matter reps. **A repo-wide search over all
> `arc_verdict.json` finds no arc running the cascade on any m ≥ 2 grammar.** So the SM-match's
> discriminating power beyond E₆ is **UNCOMPUTED, not zero.**

**And B997 cuts the other way:** at each word's *own* conductor the golden **is** unique, so the
family members are **demonstrably not equivalent** — evidence against assuming their cascades
coincide. **Registered L149**, with two outcomes and neither assumed.

## KILLED — an incoming cc3 claim, and it is a known conflation recurring

cc3's `STEPPING_BACK` relay (2026-08-09) lists among *delivered* results: **"θ_QCD = 0,
parameter-free, which is a solved naturalness problem sitting in the ledger without emphasis."**

**Not banked, and the repo says the opposite in two places:** `THE_SM_VERDICT.md` row 6 lists strong
CP as **"never addressed"**, and `THE_LADDER.md` **X6 is BLIND** with *"no registered obligation
set"*. No `arc_verdict.json` carries the claim.

> **DIAGNOSIS CORRECTED SAME-DAY (2026-08-10), after reading cc3's `PATH_BEYOND_THE_WALL`, which
> supplies the actual argument:** *amphichirality ⟹ Z_k(M) = Z_{−k}(M) ⟹ θ = 0.* **That is NOT the
> θ/θ_QCD naming conflation this section first guessed** (the B780/B784 class). The object-level
> half is real — m004 is amphichiral and CS = 0 is in the record (X25 carries it). **The failure is
> the last arrow: reading the object's k as the SM's θ_QCD is an object→physics FUNCTOR application,
> and the typed functor is exactly what Gate 5 / L91 say does not exist.** *Shapes are free,
> currencies are not* (`PRICED_DOORS`). What the observation earns is a **firewalled HOOK** — if the
> functor existed, θ_QCD would be the naturally-explained parameter, and it is dimensionless, in the
> one sector the weight ledger lets the object speak to. A reason to want the functor; not a
> delivered result.

**Refused, not merged** — routed back to cc3 (`CC_TO_CC3_2026-08-10_PATH_TRIAGE.md`) for a banked
derivation with the functor step explicit, or withdrawal. *(A CP-adjacent result does exist and is
narrower: B303's sign = sign(CS). That is not θ_QCD = 0 parameter-free.)*

## ADDENDUM (2026-08-10) — the full relay triage, made repo-resident

The rest of cc3's two relays was verified the same day, so the findings live here and not only in
the relay channel (the B999 loss mode):

- **Every other citation checks out verbatim** — B721 (II₁, trivial modular flow), B733/B766/B782
  (the (ℤ/2)³ torsor, rank exactly 3, no equivariant section), B277 (the canonical class-S lift,
  monodromy in the S-duality group, two named blockers), B925 (the desert killed by the chain's own
  algebra). *Minor:* B712's verdict is the imaginary-canonical-point result; the A-polynomial
  reciprocality attribution needs its actual home cited.
- **S3's premise "both factors are known" is NARROWED, not refused.** The II₁ half is solid (B721).
  The **only III₁ on main is B850**, and it is **the foliation algebra, not the observer**;
  **conditional** (its own hatch names the unproven ratio-set reduction for cusped foliations —
  infinite transverse measure, no uniform hyperbolicity); and **generic** (m003 and a non-arithmetic
  control return the same type; the arc is NEGATIVE and *closed* a lead). S3 stays the relay's best
  computation — as *"construct the crossed product and see whether III₁ appears"*, which would be
  the **stronger** result.
- **S2 is the campaign's own X25/X21** (B250's CS vs Gukov's `I_CS`), independently re-derived —
  two seats naming one computation is signal, and it is requirement 4 of `CROSSING_REQUIREMENTS`.
- **S4 (type B1000's five closings by the weight ledger's rule) is cheap and runnable**, and its
  "3 torsor bits vs 5 closings" mismatch is the relay's best open question.

## WHAT CONVERGED — and it is the more valuable half

cc3 reached, independently: **the object is one side of a relation** (≈ Review 42 §4's
observer-coupling crux); **specificity descends three populations and survives at the bottom as a
PROOF** (B997) — the same juxtaposition as Review 42 §3, and **cc3's reading is the correct one**,
which is why the overreach above is the outgoing seat's and not the material's; and **the failure
mode of the day was scope, not arithmetic** — cc3: *"six of my own corrections today had one shape:
a claim whose scope was wider than its evidence. **Not one was an arithmetic error.**"*

> **Both seats' synthesis documents contained exactly the error their synthesis documents diagnose.**
> That is recorded as the finding it is, not as an irony.

**cc3's Level-5 goal statement is sharper than Review 42's and is adopted as the better framing:**
the goal is **not a ToE** but **"a parameter reduction with a counted input list"** — given a small,
named, finite set of external data, the object determines the gauge structure. **Adopted as framing
only**; its *ledger* (the delivered/price columns) is **not** adopted here, because one of its
delivered rows is the θ_QCD claim killed above.

## THE HANDOFF TEST — one real gap found

The mandate asked what could not be reconstructed from the repo alone. **One thing, and it is
load-bearing:** the owner's standing epistemic rule — *"anything you say we don't have is either in
repo, or needs to be figured out"* — **exists only in agent memory, which is machine-local.** A
fresh clone on another bench (cc3, solo, any future seat) would **not** have it. Since it is now
operative and was cited as binding, **it belongs in the repo**: added to `WORKING_RULES.md` §0.

*Everything else in the handoff reconstructed cleanly from `WORKING_RULES §0` → the four grounding
docs → `REVIEWS.md`.*

---

**Verdict: PROVED.** 4 confirmed, 1 withdrawn, 1 incoming claim refused, 1 handoff gap closed.
