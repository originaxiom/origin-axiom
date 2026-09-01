# H1 — B267 grade re-read (Ring R3, HELD item #23a)

**Cell type:** reader cell (no recomputation; R13/R14 own the E₆ numerics). **Verdict: GRADE-OVERSTATED.**
The `PROVED` grade is correct for what the arc actually proves; the registry row's *wording* ("are the same
Lie object") and the arc's tagline ("The two E₆'s are one E₆") state an identification the evidence does not
and cannot earn under the B1231 rule. The arc's own 2026-06-28 correction (B272) already downgraded it to a
"consistency check"; the generated registry surfaces never absorbed that correction because it lives only
in `FINDINGS.md`, not in `arc_verdict.json`'s `claim_one_line`.

Read in full: `frontier/B267_e6_coherence/FINDINGS.md`, `frontier/B267_e6_coherence/e6_coherence.py`,
`frontier/B267_e6_coherence/arc_verdict.json`, `tests/test_b267_e6_coherence.py`,
`WORKING_RULES.md` §"THE IDENTIFICATION RULE" (l.233–255), `docs/IDENTIFICATION_LEDGER.md`,
`docs/THEOREM_REGISTRY.md` l.272 (T-IDENTIFICATION-IS-AN-INPUT), B272 §correction item 2, B1228 §retraction,
and the sweep's flag (`internalization/S9_bare_identifications.md` l.64–69, 205–207; `SEAT_ADJUDICATION.md` l.64).
`docs/OPEN_LEADS.md` and `docs/THEOREM_REGISTRY.md` contain **no** B267 row (grep empty); B267 surfaces only in
the generated views (`VERDICT_LEDGER.md` l.165, `THE_SPINE.md` l.330, `CLOSED_DOORS.md` l.313) and
`HINT_LEDGER.md` H64.

---

## (1) What B267 actually proves — as a theorem with hypotheses

**Hypotheses (all imported, none derived in the arc):**
- H-a. `2T = SL(2,𝔽₃)` has McKay graph = affine E₆ with marks `(1,1,1,2,2,2,3)` — **B266** (Sage/GAP; the script
  hard-codes `MARKS_2T`).
- H-b. The faithful 2-dim character of `2T` is `(2,1,1,−2,−1,−1,0)` on classes of sizes `(1,4,4,1,4,4,6)` — GAP
  via B266, hard-coded (`CHI_2T`, `CLASS_SIZES_2T`).
- H-c. The E₆ Dynkin diagram (arms 2,2,1) — **hard-coded** in `e6_dynkin_adjacency()`; the script does *not*
  remove a node from a computed McKay graph, despite the docstring "E6 Dynkin = affine-E6 McKay graph of 2T
  minus one affine node".
- H-d. B264's grading exponents `{1,4,5,7,8,11}` — hard-coded `EXPONENTS`; B264 *chose* the principal
  `sl(2)→e₆` and decomposed `e₆` by E₆ exponents, so the geometric side is E₆ **by construction**.

**Statement proved (and locked by `test_b267_e6_coherence.py`):**

> Let `D` be the E₆ Dynkin diagram and `h = 12`. Then (i) the adjacency eigenvalues of `D` are exactly
> `2cos(πm/12)` for `m ∈ {1,4,5,7,8,11}`, i.e. the exponents of E₆; (ii) `Σ marks(2T) = 12 = h`;
> (iii) `Σ exponents = 36 = ℓh/2` and `ℓ(h+1) = 78`; (iv) the Molien series of `2T` in its faithful 2-dim
> representation is `(1+q¹²)/((1−q⁶)(1−q⁸))`.

Every clause is a textbook invariant of the single Lie type E₆ / the E₆ Kleinian singularity (Kostant 1959/1984,
McKay 1980, Springer). Combined with H-a (B266) and H-d (B264), the corollary the arc is *entitled* to is:

> **Corollary (type coincidence).** The Dynkin type attached to `4₁` arithmetically (trace field → ramified 3 →
> `2T` → McKay, B266) and the Dynkin type of the target Lie algebra in B264/B265's flat-connection construction
> are the **same Cartan type, E₆**; consequently they share exponents, Coxeter number, root count, dimension,
> and the exponent set grading B264's tangent space is the McKay/Coxeter exponent set.

Nothing in the arc constructs a map from one E₆ to the other, and there is no object on the arithmetic side
for such a map to have a domain: McKay produces a **diagram** (a type label), not a group acting on the
flat connections or on `π₁(4₁)`. The arc's own guardrail concedes the live identification is elsewhere:
FINDINGS "Honest guardrail": *"Coherence of Lie invariants is **not** a proof that the 3d-3d **input** type
must be this E₆"*.

## (2) Identification or coherence check?

**Coherence check, not an identification in the rule's sense — provided it is read as (1).**

The rule (`WORKING_RULES.md` l.235–236): *"For any claim of the form 'X here IS Y there': exhibit the MAP, then
show it ACTS FAITHFULLY. Matching orders, names, dimensions or numbers are **not** a connection."*

- As a **type-agreement** statement, matching exponents is the *correct and sufficient* evidence: the exponent
  multiset determines the Dynkin type, and any two complex simple Lie algebras of type E₆ are isomorphic. The
  evidence is not "of a kind the rule bars" for *this* claim; the rule bars it as evidence for a claim of
  the form "X IS Y" between two specific objects playing two roles.
- As the arc's **tagline** — FINDINGS: *"> **The two E₆'s are one E₆.**"*, script: *"They are ONE E6"*, H64:
  *"YES — one E₆ on five invariants"*, registry: *"are the same Lie object"* — it reads as exactly such an
  "X here IS Y there" claim (the flat-connection E₆ ≡ the McKay-nominated E₆), and for *that* reading the
  evidence is the barred kind: no map, no action. This is the same species as ledger row **I-6** (`π₁(m004)↠2T
  ≡ the 6d type's ALE Γ`, UNEARNED) one floor down; B267's "one E₆" is I-6 read at the Lie-algebra level.
- B272 (2026-06-28) already made this distinction and appended it to FINDINGS: *"That is a **consistency
  check** (the two constructions are not in conflict; both are E₆), not five independent measurements."*
  The registry never received it: `arc_verdict.json` was authored (`W1-wave1-fanout`) from the pre-correction
  headline.

**One sweep claim does not hold up.** S9 l.67–68 cites *"B1228's σ = 1 retraction already showed the two
E₆-sources (McKay-on-2T vs geometric CS boundary, which is A₁) can come apart"*. B1228's pair is **McKay E₆ vs
the geometric `PSL(2,ℂ)` connection's boundary WZW (A₁)** — a different pair from B267's (McKay E₆ vs B264's
`e₆`-valued flat connections). B1228 does not contradict B267's type coincidence; it contradicts nothing B267
says. That part of the flag should be dropped; the phrasing objection stands on its own.

## (3) Is PROVED correct, and does the row overstate?

- **PROVED — stands** for the statement in (1). The four clauses are exact sympy checks against known closed
  forms; the lock test reproduces them. The `test_mckay_graph_recovers_b264_exponents` name is generous (the
  graph is hard-coded; the genuine `McKay(2T)=Ẽ₆` derivation is B266's `mckay_selection_sage.py`), but the
  dependency is explicit in FINDINGS' correction and B266 is itself PROVED and ledger row I-1 EARNED.
- **The registry row overstates.** `arc_verdict.json` `claim_one_line` (propagated verbatim to
  `VERDICT_LEDGER.md` l.165, `THE_SPINE.md` l.330):
  > `"Coherence check passes: the arithmetically-selected E6 and the character-variety E6 are the same Lie object, the McKay exponent set matching the tangent-space grading."`

  "the same Lie object" asserts identity of two objects in two roles; the arc proves identity of **type**.
  Under T-IDENTIFICATION-IS-AN-INPUT (`THEOREM_REGISTRY.md` l.272), the unstated reading is an unpriced input.

**Proposed re-wording (one field, `arc_verdict.json` `claim_one_line`; the generated views follow):**

> `"Coherence check passes: the arithmetically-selected Dynkin type (B266, McKay on 2T) and the type of B264/B265's flat-connection target coincide as E6 — same exponents {1,4,5,7,8,11}, h=12, dim 78, Molien (1+q^12)/((1-q^6)(1-q^8)). Type agreement only: no map between the two E6 roles is exhibited (see B272 correction; the identification is I-6's species and remains open)."`

Companion edits the owner may want (not made here): `HINT_LEDGER.md` H64's *"YES — one E₆ on five invariants"*
→ *"YES on type; consistency check (B272)"*; and a **ledger row** for the Lie-level identification
"flat-connection E₆ ≡ McKay-nominated E₆" — status UNEARNED, source B267/B268, earned by *"a construction in
which one E₆ acts both as the structure group of the flat connections and as the 6d type of the ALE ℂ²/2T"*.
Adding that row raises UNEARNED from 2 to 3 and would trip `gate_identification_register`'s ratchet; since
the debt dates from 2026-06-28 and predates the census, it is a baseline correction (sweep item #24's
"undercounts by construction"), not a new debt — the owner should re-baseline rather than suppress the row.

## Verdict

**GRADE-OVERSTATED.** Keep `PROVED`; replace `claim_one_line` as above; do not re-grade the arc's mathematics.
Nothing in this cell was recomputed; nothing outside this file was modified.
