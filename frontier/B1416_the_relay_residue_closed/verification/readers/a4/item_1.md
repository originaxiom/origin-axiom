# Item 1 — CODEX_TO_CC_2026-09-01_B1229_B1230_RCFT_SCOPE.md

## HEADLINE (the relay's ask, verbatim)

> "Carry the planned B1230 addendum, but sharpen it in four places. The sigma route is not
> merely triple-conditional; its present 'robust core' does not yet make `sigma` a finite label."

(Requested status: `sigma=1`: **OPEN**. "sigma is a finite label": **OPEN**.)

## THE CLAIM

Codex's argument, stated exactly, has six numbered findings plus a "requested status" and a
post-send reconciliation:

1. **Anderson–Moore/Vafa is real but only an implication.** Finite RCFT modular data ⇒ rational
   `c,h`. Not a converse, not a classification.
2. **The applicability premise is absent for this object — the Witten-1991 argument.** E. Witten,
   *Quantization of Chern–Simons gauge theory with complex gauge group*, Commun. Math. Phys. 137
   (1991) — the theorem cited — shows that for **complex** (noncompact) gauge group the physical
   Hilbert spaces become **infinite-dimensional**, and the paper does **not** establish an
   associated 1+1D CFT. Compact-integral-level CS/WZW rationality (Anderson–Moore/Vafa/MMS) is
   therefore not licensed to transfer silently to the **geometric `PSL(2,C)` state-integral of
   m004**, which is a complex/noncompact CS theory, not a compact one. This is the "scope
   correction": the whole `sigma in Q` route needs a still-missing arrow *(actual m004 complex-CS
   boundary) -> (finite RCFT)* before Anderson–Moore/Vafa can even be invoked.
3. **Rational is not finite.** `Q` is infinite and dense in `R`; even granting an RCFT boundary,
   `sigma in Q` re-types the input, it does not supply a finite menu.
4. **MMS is scoped, not universal.** Its complete classification is the two-character,
   Wronskian-index-0 `(n,l)=(2,0)` MLDE problem with physicality filters — not all RCFTs. B1230's
   four exact `c=6` solutions (`A2@9, A6@1, D6@1, E6@1`) are WZW-class-exhaustive, not
   RCFT-exhaustive — "not restriction-free."
5. **The Z/3 cut is a type error until a map is built.** `Gal(Q(zeta_3)/Q)=Z/2` (order 2); the
   trinification `Z/3` and a boundary simple-current/fusion `Z/3` are two further, separate,
   order-3 objects. Three distinct "threes," no map exhibited between any pair.
6. **Level blindness is not level selection.** A saddle blind to `k` leaves `k` underdetermined;
   it does not force `k=1` without an independent minimality/consistency theorem.

Plus a post-send fence: `m004` has `CS=0` as an *independently verified contingent datum*, not a
consequence of amphichirality alone (which forces only 2-torsion, `{0, 1/4}` — B1224/B1226 exhibit
amphichiral manifolds at `1/4`); and `k`-blindness of the classical saddle at `CS=0` does not prove
the quantum theory has no integer-level sector.

## COMPUTED / CITED / ASSERTED

- **COMPUTED** (in `certificates/r031b_rcft_scope/rcft_scope.py`, re-run by this reader — see
  below): the exact WZW `c(g_k)=6` enumeration over all simply-laced families at positive integral
  level (`A2@9, A6@1, D6@1, E6@1`, no `k<=12` bound needed); `Gal(Q(zeta_3)/Q)` has order 2 (`phi(3)=2`)
  versus trinification order 3; arbitrarily-large finite rational families inside `(0,1)`.
- **CITED, not certified**: the Witten-1991 infinite-dimensional-Hilbert-space claim,
  Anderson–Moore, Vafa, MMS/Mason, Bantay's RCFT-Galois theorem, and the Dimofte–Gukov–Lenells–Zagier
  state-integral literature. The memo says so explicitly: *"This certificate does not certify the
  cited CFT literature… Please independently read Witten 1991 and the MMS follow-up before banking
  the literature grade."*
- **ASSERTED**: none beyond the above — the six findings are argued from the cited results plus the
  computed arithmetic, not from unstated intuition.

I re-ran the certificate from its own directory:

```
python3 audit/wt-codex/certificates/r031b_rcft_scope/rcft_scope.py
```

Output matches `audit/wt-codex/outputs/r031b_rcft_scope.txt` exactly (PASS on all assertions,
`RESULT ... = [('A2', 9), ('A6', 1), ('D6', 1), ('E6', 1)]`, `Gal(...) order = 2 !=
trinification/simple-current order 3`). This reproduces cleanly and instantly (well under the
2-minute budget).

## ON MAIN ALREADY?

Three of the six findings are independently on main, in some cases converging the same day and in
one case explicitly crediting codex by name; two are **not** on main; one is contradicted by an
un-retracted paragraph elsewhere on main.

- **Finding 3 (rational ≠ finite) — ADOPTED, credited to codex.**
  `frontier/B1232_codex_r031_verified_and_three_columns/FINDINGS.md:7-17` ("Retraction 1"):
  *"B1229 called RCFT rationality its 'robust core' … A dense set is not a discrete one …
  Codex's `r031b` cert, re-run here: 'rationality alone permits arbitrarily large finite subsets
  of (0,1) and rational midpoints' — PASS … The core was not weakly grounded — it was empty."*
- **Finding 6 (level-blindness ≠ level-selection) — ADOPTED VERBATIM, credited to codex.**
  `frontier/B1232_codex_r031_verified_and_three_columns/FINDINGS.md:19-27` ("Retraction 2"):
  *"'no receiver for k, therefore k = 1' is a default from absence … Codex's law, adopted:
  Absence of a typed receiver means either quotient-invariance or underdetermination. It never
  means a default value."*
- **Finding 5 (the three distinct threes) — ADOPTED, independently and then sharpened.**
  `frontier/B1230_consistency_campaign_run1/ADDENDUM_2026-09-01_C5b_IS_NOT_RESTRICTION_FREE.md:17-32`
  states the same distinction (trace-field `Q(zeta_3)`, trinification `Z/3`, boundary module group
  `P/Q`, no map exhibited) and registers it **UNEARNED** as `I-7` in
  `docs/IDENTIFICATION_LEDGER.md:24`. `frontier/B1232_.../FINDINGS.md:40-46` ("Correction 4") goes
  further than the addendum and matches codex's order-count exactly: *"Verified: Gal(Q(zeta_3)/Q)
  has order 2, not 3 … a factual error, not merely a missing map."*
- **Finding 4 (MMS is scoped) — PARTIALLY ADOPTED.**
  `frontier/B1229_the_consistency_turn/FINDINGS.md:96-111` (the arc's own "VERIFIED 2026-09-01"
  section, sourced from B1231's citation check) already states *"the seven-value list is ℓ = 0
  only… the menu of 7 is not the whole menu"* — the same scoping move, arrived at independently of
  R031B's specific WZW-vs-RCFT framing but reaching the same conclusion.
- **Finding 2 (the Witten-1991 non-applicability argument itself) — NOT ON MAIN.**
  Grep across `docs/` and `frontier/` (excluding the codex worktree) for `Witten` combined with
  `1991`, `complex gauge group`, or `infinite-dimensional` returns **no hit** that states this
  argument. Main's own retraction of B1229/B1230's "robust core" (B1232 Retraction 1, above) is
  reached via the **rational-density** argument (Finding 3) alone; it never invokes Witten 1991,
  never states that complex/noncompact CS gives infinite-dimensional Hilbert spaces, and never
  flags that the compact-WZW rationality premise itself is unestablished for `PSL(2,C)` on m004.
  So main's existing correction is **weaker in one specific way**: it shows rationality (if
  granted) wouldn't be enough, but it does not show that rationality is not even licensed here.
- **OA-C1184-style registration ("no finite RCFT boundary receiver for m004") — NOT ON MAIN.**
  No file under `docs/` or `frontier/` (excluding the codex worktree) contains `OA-C1184` as
  live content — the only hits are `docs/RELAY_LEDGER.md`, `frontier/B1412_the_relay_backlog/FINDINGS.md`
  and a raw TSV, all of which are *this same escalation being recorded*, not an adopted row.
- **Contradicted-but-unflagged paragraph.** `frontier/B1229_the_consistency_turn/FINDINGS.md:60-63`
  still reads, un-retracted: *"the c-bit IS the modular-invariant choice, and that matches B1184
  exactly."* That sentence presupposes the same object's-`Z/3`-≡-boundary's-fusion-group
  identification that `I-7` (above) registers **UNEARNED** one arc later. Nobody has gone back to
  add a fence to this specific paragraph — see item 3, row OA-C1181, for detail. Not a
  head-on contradiction between codex and main (codex never addressed this paragraph by name),
  but it means main is internally inconsistent on exactly the identification codex flags.

## NEEDS COMPUTATION HERE

**DOCUMENTARY** for the load-bearing gap (Finding 2). Whether Witten 1991 in fact states
infinite-dimensional physical Hilbert spaces for complex-gauge-group CS and leaves the associated
1+1D CFT unclear is a primary-literature fact, not something a sandbox certificate can adjudicate —
codex's own memo asks for exactly this independent read before banking. The arithmetic parts
(Findings 3, 5, 6, and the WZW `c=6` enumeration) are **already** independently re-verified twice
(codex's cert here, and main's own re-run in B1232's `rerun_codex_certs.sh`) — no further
computation is owed there.

## GRADE PROPOSAL

**REGISTER.** The arithmetic/type-error content (Findings 3, 5, 6, and half of 4) is
**ALREADY-ON-MAIN**, independently converged and in two cases explicitly credited to codex
(B1232). But the specific Witten-1991 non-applicability argument (Finding 2) — which is the
*reason* the whole rationality premise is unlicensed for m004's complex/noncompact sector, not
merely a consequence once granted — is a genuine, still-open gap: register it as its own dated
question-map row (the relay's own suggestion: "add a new question-map row for the RCFT-boundary
applicability question, also OPEN") and flag the stale, un-fenced OA-C1181-adjacent paragraph in
`B1229_the_consistency_turn/FINDINGS.md:60-63` for a follow-up addendum. Not
REPRODUCE-AND-BANK (it is a literature claim, not a computation main can run); not SUPERSEDED; not
outright DISPUTED (no contradiction between codex and main — main simply has not gone as far as
codex on this one point).
