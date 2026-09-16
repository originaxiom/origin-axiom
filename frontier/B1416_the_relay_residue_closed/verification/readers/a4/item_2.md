# Item 2 — CODEX_TO_CC_2026-09-01_IDENTIFY_OR_DESCEND.md

## HEADLINE (the relay's ask, verbatim)

> "Please verify and, if it survives, adopt this as the parameter-counting counterpart to B1231's
> Identification Discipline."
> … "Requested disposition: verify the quotient lemma and adopt the two-mode 'identify or descend'
> closure test. Keep the R032 application conditional until its characteristic-zero payload lands."

## THE CLAIM

**The lemma (R031D's "tail lemma").** For an exact sequence `0 -> C -> V -> T -> 0` with
`dim T = 1`, an **alternating form `beta` on `V` that vanishes on `wedge^2(C)`** induces a
well-defined map `C tensor T -> W` — i.e. the induced mixed pairing does **not** depend on which
lift/splitting of `T` into `V` is chosen. This sharpens R031A's `B_0 = 4 chi_0` result: a
`dim_C(B_0) = 4` raw parameter space (literally `P^3_C` of Higgs lines) does not automatically mean
**three physical operator parameters** — three of the four raw coordinates can be a
choice-of-splitting that the physical observable never sees.

**The test ("identify or descend").** Every bridge in the programme's ledger must close one of two
ways: (a) **construct** a unique typed identification between the two sides, or (b) **prove the
observable descends** — i.e. is independent of the unearned choice. This is offered as the
parameter-counting counterpart to B1231's Identification Discipline (which prices *unearned
identifications* as observer input); R031D prices the complementary failure mode, an *unforced
splitting choice masquerading as physical parameters*.

**What the certificate computes** (`certificates/r031d_observable_quotient/observable_quotient.py`):
inputs are an explicit alternating form `beta` on a `V` (dims consistent with `C=3, T=1, V=4`) and
125 distinct lift/splitting changes of the `T`-lift into `V`; it checks (i) `beta` restricted to
`wedge^2(C)` is exactly zero, (ii) the induced `C tensor T` pairing is identical across all 125
tested lifts (a "bite" control plants a nonzero `C-C` term and confirms the induced value then
*does* change, so the test can fail). This is a **dependency-free**, exact-rational-arithmetic
script (no numpy/sympy — just `fractions.Fraction`), consistent with the memo's description.

The conditional fence: this only prices the raw-parameter-vs-physical-parameter question. It is
*conditional* on R032's separate, still-running, characteristic-zero result (`A_11 x
wedge^2(B_2,conn)` vanishing) before any specific lepton/down-Yukawa entry can actually be said to
annihilate `C`; no cross-sector promotion is claimed.

## COMPUTED / CITED / ASSERTED

**COMPUTED HERE.** I ran the certificate myself, from its own directory:

```
cd audit/wt-codex/certificates/r031d_observable_quotient
python3 observable_quotient.py
```

`rc=0`, wall time ≈ 0.33 s (well under the 2-minute budget). Full output:

```
PASS beta restricted to wedge^2(C) is zero
PASS induced C tensor (V/C) observable is well-defined
DATA nonzero induced mixed observable = (Fraction(2, 1), Fraction(-3, 1), Fraction(5, 1))
PASS all 125 tested tail lifts give the same observable
RESULT raw lift-choice dimension = 3; observable variation rank = 0
RESULT projective nonzero-tail stratum has one observable point; pure-connecting boundary maps to zero
CONTROL a planted C-C term makes the lift choice observable
SCOPE exact quotient lemma; no R032 characteristic-zero vanishing or physical normalization is assumed
```

This matches `audit/wt-codex/outputs/r031d_observable_quotient.txt` and the memo's description
exactly (the 125-lift check, the bite control, exact arithmetic).

**CITED, not verified here or by codex's own cert:** whether the *actual* lepton/down Yukawa
couplings annihilate the actual connecting block `C` — that is R032's separate, still-running,
characteristic-zero computation. Both the memo and (independently) main's B1232 flag this as
unverified.

## ON MAIN ALREADY?

**Partial — the mathematical substance of a special case is on main and credited to codex; the
general lemma and its name are not.**

- `frontier/B1232_codex_r031_verified_and_three_columns/verify_quotient_lemma.py:1` — the
  docstring reads, verbatim: *"INDEPENDENT verification of codex's quotient-invariance lemma —
  the POSITIVE claim… given 0 -> C -> V -> T -> 0 and a coupling Y on V that ANNIHILATES C, then Y
  factors uniquely through T."* `FINDINGS.md:51-68` ("The positive — the third column") states the
  same conclusion in prose and generalizes it into an adopted **closure test**: *"(1) identify the
  raw choice space; (2) identify allowed field redefinitions; (3) map choices to normalized
  invariant observables; (4) count the image, not the source."* This is the same two-mode
  identify-or-descend idea, reached the same day, and explicitly attributed to "codex" in the
  script — but under main's own name ("the third column" / "closure test"), not R031D's.
- **What is on main is a strictly weaker special case.** Main's `verify_quotient_lemma.py` tests a
  generic **linear functional `Y`** on `V` that vanishes on `C` (elementary linear algebra: a
  linear map killing a subspace factors through the quotient). R031D's certificate is more
  general: it starts from an **alternating bilinear form `beta`** on `V` and shows `beta|wedge^2(C)
  = 0` induces a well-defined *mixed* pairing `C tensor T -> W` — a materially different and
  stronger construction (an alternating-form/exterior-power argument, not a linear-functional
  factorization). Main has not reproduced or adopted this more general form.
- **Confirmed absent by name.** Grepping `docs/` and `frontier/` (excluding the codex worktree) for
  `R031D`, `identify or descend`, and `C⊗T`/`C tensor T`-as-a-named-lemma returns hits **only** in
  bookkeeping files that are themselves recording this same escalation:
  `docs/HARVEST_LEDGER.md:269`, `docs/RELAY_LEDGER.md:523`,
  `frontier/B1306_the_older_debt/verification/sliceD/rows.md:118`,
  `frontier/B1306_the_older_debt/inputs/fc_codex_hostile_inventory.md:164`,
  `frontier/B1412_the_relay_backlog/FINDINGS.md:37`. None of these is a substantive adoption.
- Main's own audit trail agrees with this reading: `docs/HARVEST_LEDGER.md:269` grades row 237
  (R031D) **"SCHEDULED (no main text names it — the slice D backlog, read before Review 57)"**, and
  `docs/RELAY_LEDGER.md:523` says **"OPEN — main would need a dedicated arc adopting the tail lemma
  / 'identify or descend' test; none exists yet … no file uses 'identify or descend' or the C⊗T
  lemma."** Both match what this independent read finds.

## NEEDS COMPUTATION HERE

The certificate's own claim was **COMPUTED** (re-run above, PASS). What remains open is not
arithmetic verification but **adoption scope**: does main need the fully general alternating-form
lemma, or is the linear-functional special case already banked in B1232 sufficient for every
place the repo currently needs it? The one discriminating fact that would settle this: exhibit a
concrete place in the current R032/Higgs-line calculation where the coupling that must be shown
"blind to the splitting" is genuinely a bilinear/alternating object (not a linear functional) — if
one exists, the general R031D lemma is load-bearing and not covered by B1232; if every live use is
linear, B1232's special case already suffices and R031D can be graded a documented generalization
with no open computational debt. This check was not run here (it requires locating and reading the
live R032 Yukawa/Higgs-line construction, out of this reader's scope) — recipe for whoever picks it
up: `grep -rn "wedge" frontier/B1226* frontier/B1230* frontier/B1231* frontier/B1232*` and check the
bilinearity of whichever coupling tensor is at stake.

## GRADE PROPOSAL

**REGISTER.** The certificate reproduces cleanly and its core insight is independently
corroborated (a special case is already verified and credited to codex in B1232). It should be
registered as its own named row — crediting R031D specifically, noting explicitly that its
alternating-form/`wedge^2` generalization goes beyond what B1232 verified — rather than marked
ALREADY-ON-MAIN, since the general lemma, its name, and the "identify or descend" framing are not
in fact adopted anywhere on main. This matches main's own harvest/relay-ledger grading
(SCHEDULED / OPEN) exactly — not DISPUTED, not SUPERSEDED.
