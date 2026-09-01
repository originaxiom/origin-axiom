# R01 — B1225 recomputation: the no-canonical-selector theorem

**Verdict: PARTIAL (core MATCH; one clause out of reach).** The theorem's computation —
the action of G = Stab_Aut(D)|_T on every menu value is trivial — is independently
recomputed here from committed inputs and **reproduces exactly**: 0 values moved, every
orbit a fixed point, so invariance selects nothing. The menu-cardinality clause
(W1 = 11,720) is **not reconstructable from any committed file** (the enumerator is
cloud-side; the arc's own ADDENDUM and the relay ledger say so; my closure counts
confirm no natural rule over the committed atoms yields 11,720). The vacuity
assessment — the load-bearing deliverable — is below: **the theorem is a
definitionally-forced consequence with exactly ONE failable empirical premise**, and
the arc's own committed verification script checks neither.

## Blind log (binding discipline 1)

Read BEFORE computing (claim + committed inputs of OTHER arcs only):
- frontier/B1225_no_canonical_selector/FINDINGS.md (the claim)
- frontier/B1225_no_canonical_selector/ADDENDUM_2026-08-31_the_atom_list_is_not_in_main.md
- frontier/B1203_two_probes/FINDINGS.md, verification/reproduce.sh,
  verification/probes.txt, b1203_results.json (the 17-atom list + ops + W1)
- frontier/B1168_c5_investigation/FINDINGS.md, verification/c5_parity.txt (the law)
- frontier/B1191_close_loop_batch3/FINDINGS.md, verification/batch3_cells.json
  GC-15 entry (the definition of G)
- ledger excerpts: docs/GRAND_COMPUTATION_LEDGER.md, docs/CAMPAIGN_STATUS.md,
  docs/RELAY_LEDGER.md (SEND_THE_SEVENTEEN_ATOMS row), papers/P3_THE_PAPER/CLAIM_CANDIDATES.md

Read AFTER recompute_action.py + recompute_output.txt were on disk:
- frontier/B1225_no_canonical_selector/verification/reproduce.sh
- frontier/B1225_no_canonical_selector/arc_verdict.json
- frontier/B1227_one_theorem_two_regimes/two_regimes.py
- tests/test_b1231_identification.py (B1225 mention: a WORKING_RULES string check only)

No B1225-dedicated test lock exists in tests/.

## What was recomputed (my code: recompute_action.py, output: recompute_output.txt)

1. **Aut(D), independently**: snappy gives symmetry_group(m004) = D4, order 8,
   amphichiral — 4 orientation-preserving + 4 orientation-reversing elements.
   Matches the banked Isom(m004) = D4 (B1104) without citing it.
2. **The action, from first principles**: an isometry invariant is by definition
   unchanged by every orientation-preserving self-isometry; an orientation-reversing
   one acts through the mirror, which acts on complex-valued archimedean data by
   conjugation c (B1168's own-verified rows: complex volume conjugates, CS -> -CS).
   So the Aut(D)-action on values factors through eps: D4 -> {1, c}. All 8 elements
   implemented individually.
3. **The atoms**: the only enumerated 17-atom list anywhere on the bench —
   {1, 2, 3, 11, 12, 27, 64, 72, 78, 112, 953, 2304, 151/64, 553/64, 3/8, phi, 2+sqrt3}
   from B1203's committed reproduce.sh — verified exactly real in sympy; **all 17
   fixed by all 8 group elements, exactly** (0 moved).
4. **Ops equivariance, symbolically**: c commutes with {+, -, *, /} identically;
   with sqrt **only on nonnegative arguments** — c(sqrt(-2)) - sqrt(-2) = -2*sqrt(2)*i != 0,
   exhibited exactly. B1225's step 5 ("{+,-,*,/,sqrt} are G-equivariant") is literally
   false without the domain restriction; the conclusion survives because every menu
   VALUE is real (B1203) and c fixes every real regardless of construction route.
   A benign but real gap in the banked statement.
5. **The menu**: closures of the atoms under the ops — |depth 1| = 761 distinct
   values, |depth 2| > 300,000 (cap). **No committed rule yields 11,720**; the tier
   rule lives only in cloud's enumerator (consistent with the ADDENDUM and relay
   CC_TO_CLOUD_2026-08-31_SEND_THE_SEVENTEEN_ATOMS.md). Triviality was checked on
   the **complete single-op stratum (1,173 exact symbolic values: all a op b plus
   sqrt a)** — 0 moved by any group element — and all 761 depth-1 closure values are
   real, hence c-fixed. Since triviality on real values is construction-independent,
   the banked conclusion follows for ANY menu inside the real closure of these atoms,
   whatever cloud's tier rule is: **the recomputation covers the 11,720 without
   needing to enumerate them.**
6. **Control (binding discipline 3)**: planted a mirror-odd atom (i*sqrt(2), a
   stand-in for a beta-odd datum). The reality assert catches it; the same orbit
   machinery finds **69 of 648** planted-menu values MOVED by the mirror; an
   invariance filter now cuts a nonzero, correctly-identified subset. **The
   instrument can find a nontrivial action when one exists** — the zero cut on the
   real menu is a finding, not blindness.

## Diff against the banked claim

| clause | banked | recomputed | diff |
|---|---|---|---|
| G fixes every atom | asserted (via B1168 law) | 17/17 fixed, exact, all 8 elements | **MATCH** |
| action on menu trivial | "all 11,720 fixed points" | 0 moved on complete single-op stratum + full real closure argument | **MATCH** (for any menu inside the real closure) |
| hence no invariant selection | trivial action => every subset invariant | same, immediate | **MATCH** |
| W1 = 11,720 | cited from B1203/cloud | **not reconstructable from committed files** | out of reach (hence PARTIAL) |
| step 5 "sqrt is G-equivariant" | stated unconditionally | true only on nonnegatives; exact counterexample exhibited | note: statement needs the domain restriction |

## The banked verification is not a computation (found post-blind)

B1225/verification/reproduce.sh computes nothing about the action: it greps string
fragments ("11720", "c-equivariance", "0 of 11720", "GC-15") out of OTHER arcs'
claim_one_line fields and prints REPRODUCES. As a check of the theorem it could only
fail by citation drift. The arc is open about being structural ("its inputs are
banked arcs"), but the mathematics itself was never machine-checked on this bench
before this cell — B1203 checked reality under c only; B1227 later argued
(correctly) that real + amphichiral => mirror-even for free, which my step 2
reproduces independently.

## VACUITY assessment (the load-bearing deliverable)

**Verdict on the theorem: NOT a vacuity, but conditionally-forced — one failable
premise, then tautology. And the arc's OWN check is vacuous as a computation.**

Decompose "G fixes every menu value":

- **Failable part (empirical, could have come out otherwise)**: the 17 atoms are
  real (equivalently, given amphichirality and R torsion-free per B1227,
  mirror-even). Cloud's enumerator could have emitted a complex atom — the
  omega-tier actually does, per B1203's own note. My control shows the check bites
  when this premise fails: a planted non-real atom produces a nontrivial action and
  a nonzero cut. **This is the theorem's entire empirical content, and it is one bit.**
- **Forced part (definitional, could NOT have come out otherwise)**: given real
  atoms and reality-preserving ops, triviality is analytic. "Canonical" is DEFINED
  as beta-even = mirror-fixed; Aut(D) acts on numerical invariants only through the
  mirror (orientation-preserving isometries fix invariants by the definition of
  invariant); so "the stabilizer fixes everything canonical" is the definition of
  canonical read twice. B1225's headline — *invariance cannot distinguish among
  invariants* — is, as stated, a tautology, and the arc half-admits it ("one line
  from the programme's own law").

So: **could this theorem have come out any other way given its definitions? No** —
once (menu inside beta-even AND dimensionless) and (G inside Aut(D)) are both fixed
by prior definitions, "G acts trivially" is the only possible outcome, and "trivial
action selects nothing" is immediate (every subset invariant). The honest reading,
which the record itself converges to via the ADDENDUM and B1227: the PROVED content
is the **conditional** "IF the menu is built from real (beta-even), dimensionless
atoms THEN no G readable off D can select in it" — where the IF is the single
failable input, verified on-bench (B1203's reality assert, reproduced exactly here).
The theorem's value is diagnostic, not computational: it reclassifies the "missing
forcing theorem" as a category error (asking invariance to break a tie among
invariants). That is a legitimate no-go, of the same epistemic type as "a symmetry
cannot distinguish elements of its own fixed-point set" — true, useful as an
organizing law, and never at risk.

**One discrepancy of record, flagged (not mine to resolve)**: the 2026-08-31
ADDENDUM and the relay row state the 17-atom list "is enumerated on NO branch" —
but B1203's committed verification/reproduce.sh (in main since 2026-08-30, commit
89affd5) hard-codes an explicit 17-atom dict. Either the addendum's search missed a
committed list, or that dict is an unprovenanced stand-in — in which case B1203's
"all 17 atoms real" bench verification rests on numbers whose provenance is not
committed either. My triviality result is indifferent to WHICH reals the atoms are;
the reality premise's provenance is not.

> **Resolved 2026-09-01 (banking seat's correction, adopted).** The dict in B1203's `reproduce.sh` IS the real
> MENU-1 list: it agrees atom for atom with the provenanced `ATOMS` array in
> `origin/claude/outside-bench:outside_bench/certificates/menu_width.py` (a1d99957, 2026-08-28). So the list is
> **present on main in B1203's cert; the search that missed it looked at branches instead of the arc's own
> verification directory.** Step 2 is thereby verified directly (all 17 real, dimensionless, nonzero ⇒ mirror-even).
> What is single-homed to outside-bench is only the *tier rule* (the enumerator), not the atoms.
> Finding filed as `frontier/B1225_no_canonical_selector/ADDENDUM_2026-09-01_the_atom_list_is_on_main.md`.

## Gate 5

No measured Standard Model value used anywhere (atoms are the committed integers/
surds; the control atom is i*sqrt(2); snappy data is geometric).

## Files (this cell only)

- recompute_action.py — the blind recomputation (written before opening B1225/verification)
- recompute_output.txt — its output, verbatim
- FINDINGS.md — this file
