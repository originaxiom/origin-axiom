# B1231 — THE IDENTIFICATION DISCIPLINE

cc banking seat, 2026-09-01. Owner-approved plan. **Gate 5 absolute.**
Applied **first** to this bench's own two failures, before any instrument was built to find others'.

## The diagnosis

**This programme succeeds when it TYPES and fails when it IDENTIFIES.**

Every identification failure in the record has one shape — two structures whose labels match, in
**different places**, joined without a map:

| arc | the glue | why it died |
|---|---|---|
| **B813** | CS(m004) = θ_QCD | dead **on type**: a functional *value* cannot fill a *coefficient* slot |
| **B1223** | V₄ ⋊ S₃ = D₄ triality | **the template**: the map existed, the **action** was trivial — *"Direct is not semidirect"* |
| **B1228** | π₁(m004)'s 2T ≡ the transverse ALE Γ | two different 2T's, two different places |
| **B1230 C-5b** | the object's ℤ/3 ≡ the boundary's module group | same species, **one cell later**, inside the computation presented as the stronger recovery |

Against that, every success was a **typing** move — B1226 (parity × dimension), B1227 (one statement,
two value groups), B1230/C-1 (*over what field?*).

## Why it is not merely hygiene

By **B1225 the object provably cannot identify** — naming requires an outside. So an unearned
identification is not a reasoning slip:

> it is an **observer input the ledger never counted**, and
> **the input ledger's parameter count is a LOWER BOUND** until every one is earned or priced.

And the programme's own goal sharpens: **the listener map `u` IS an identification map**, performed
implicitly and for free for two years. Pricing it *is* the crossing cell.

## Delivered

1. **The rule** (`WORKING_RULES.md`, binding): *exhibit the map, then show it acts faithfully.*
2. **The register** (`docs/IDENTIFICATION_LEDGER.md`), 7 audited rows — **EARNED 3** (McKay 2T↔E₆;
   trace-map ↔ N=2\* S-duality; Vol = (3√3/2)·L(χ₋₃,2)), **REFUTED 2**, **UNEARNED 2**.
   *The three earned rows are the chain's real spine.*
3. **The instrument** (`scripts/checks/identification_audit.py`) — `--extract` / `--triage` / `--selftest`.
4. **The declaration** — `identifications` in `arc_verdict.json`, schema-locked, **required from B1231 on**.
5. **The gate** — `gate_identification_register`, a **ratchet**: every declared identification has a
   row, and the UNEARNED count may not **increase**. **Verified to bite** (a synthetic new UNEARNED
   row reds it; removing it greens it). Not a hard block, deliberately: a hard block makes the
   fastest path to green *marking things EARNED*, pressuring the very judgment it protects.

## The instrument's measured limit — asserted, not hidden

A first draft's wide net returned **272 candidates, overwhelmingly false** (this repo's caps-heavy
prose triggers "IS the" constantly). The narrowed net returns **61 with good precision** — but
**misses the bare-assertion form**, which is exactly how C-5b's error was phrased.

> **The instrument built to catch my error would not have caught my error.**

So **detection is a lossy safety net; declaration is the mechanism.** A selftest control asserts the
blind spot *as a fact*, so no later seat mistakes `--extract` for coverage.

## The sweep (phases A+B, full corpus)

61 candidates across all 1,179 arcs: **3** with map language, **6** with typing language, **52 BARE**
and needing judgment. Phase C is scoped by this result rather than by a guess — **queued, not run**.

## The citation debt — discharged, and it deflated the headline

The one approved fan-out: two bounded verification agents, one paper each.

**MMS holds and sharpens.** The two-character ℓ = 0 classification is genuinely **proved** — Mason
(2018) completed MMS's own *mathematically incomplete* 1988 argument. Every central charge confirmed
exactly. E₆'s two-character status confirmed with a **better** reason than banked: 27 and 27̄ are
exchanged by the outer automorphism and have **identical full characters**, not merely equal h. E₈
excluded *structurally* as a one-character theory. **But the seven-value list is ℓ = 0 only** —
nonzero-Wronskian two-character theories are separate classifications, so **the menu of 7 is not the
whole menu.**

**Anderson–Moore/Vafa deflates.** Neither 1988 paper could be read (paywalled, pre-arXiv) and the
check says so. Real hypotheses: modular invariance **and finitely many primaries**. Grade:
**PHYSICS-ARGUMENT, not theorem** (the rigorous version is Dong–Li–Mason 2000 under *inequivalent*
hypotheses, per Gaberdiel–Kausch). And explicitly: **a general Chern–Simons-boundary chiral algebra
is not automatically covered — finiteness of primaries must be independently established, not
assumed.**

**B1229 assumed it and called it the robust core. It is not robust.** σ ∈ ℚ is **conditional** on an
unestablished finiteness, at physics-argument grade even when granted. B1229 is fenced in place.

## Net

σ's headline now carries **three conditionals, none stated when banked** — the finiteness, the ℓ = 0
restriction, and identification **I-7**. Nothing deleted, nothing exhibited, **σ = 1 remains
retracted**, B1034's L154 remains NO-EXHIBIT / UNDECIDED.

## Reproduce

`python3 scripts/checks/identification_audit.py --selftest` · lock `tests/test_b1231_identification.py`
