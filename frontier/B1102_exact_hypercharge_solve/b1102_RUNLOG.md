# B1102 RUNLOG — THE EXACT HYPERCHARGE SOLVE AT THE LANDING

Compute bench run. Preregistration: `B1102_PREREGISTRATION_draft.md`. All work in
`b1102_staging/`; the certification-frozen repo tree was read-only throughout.

## 0. Setup and provenance chase (before any computation)

The prereg and task brief both name `b1098_sl2_strata.py` as the place to learn the e6
basis/bracket conventions. Reading it showed it does not construct the bracket itself —
it `exec`s a CERT file (`(scratchpad)/cloud_handoff/certificates/twisted_double.py`,
overridable via `B1098_CERT_PATH`) and pulls `br, evec, hvec, ROOTS, IDX, N, DIM` from
its globals. That CERT file turned out to already be staged in this session's scratchpad
(`scratchpad/cloud_handoff/certificates/twisted_double.py`) — but reading it showed
**it in turn** imports the actual e6 construction from a fixed absolute path outside the
repo: the paper-lineage branch's verify module `check_charge_bracket.py` ("Appendix B —
verification of the ONE certificate the structure theory consumes"), via
`importlib.util.spec_from_file_location`. [Bank-time note: that module was VENDORED into
this arc dir as `e6_bracket_vendored.py`, provenance header carrying the original's
sha256, so the arc is self-contained.] It is a clean, single-purpose module (72 roots, Frenkel–Kac
cocycle, antisymmetry+Jacobi verified in its own `main()`) — confirmed to be the actual
root of the bracket convention B1098's and B1100's stored numbers live in, by re-deriving
the stored A2 triple's structure directly from it:

- `X = e_{α0} + e_{α2}`, `H = 2h_0 + 2h_2`, `Y = -2e_{-α0} - 2e_{-α2}` exactly — i.e. the
  triple is **literally the "Levi(0,2)-regular" nilpotent** from B1098's own enumeration
  (simple roots at 0-indexed positions 0 and 2). `[H,X]=2X`, `[H,Y]=-2Y`, `[X,Y]=H` all
  verified exact.

This module (`ccb`) was used directly (via `importlib`, same mechanism `twisted_double.py`
itself used) as the foundation in `b1102_common.py`, rather than re-executing
`twisted_double.py`'s own heavy stages (Fox calculus / longitude search / Mayer–Vietoris —
none of which this arc needs; only its stage-0/stage-1 e6+27 construction is relevant, and
that stage-1 crystal-of-ω₁ construction is reproduced fresh, own code, in
`b1102_common.build_27`, independently re-verified against the full Chevalley bracket
below). This provenance chase, and the choice it justifies, is recorded here in full
rather than silently assumed.

**The 27, own certification.** `build_27` (crystal of ω₁, shift-cocycle module action)
was checked against `rho27([u,v]) = [rho27(u), rho27(v)]` on **all C(78,2) = 3003**
Chevalley basis pairs, exact: **PASS, 0 failures.** (Re-run independently a second time
inside `b1102_solve.py` before use there too — see §4.)

## 1. Op1 — the adapted re-basis (`b1102_adapted_basis.py`)

**Centralizer.** `c = ker(ad X) ∩ ker(ad H) ∩ ker(ad Y)`, exact sympy nullspace of the
stacked 234×78 matrix: **dim 16**, matching B1098's banked number. Cross-checked via an
independent modular-rank computation (own Gauss elimination over GF(p)) at two primes
(1000003, 1000033): `78 - rank(S mod p) = 16` at both — consistent.

**Ideal split — validated before touching real data.** `split_ideals`
(`b1102_ideal_split.py`) is fresh code: intrinsic structure constants of `c`, primary
decomposition of `ad(generic x)` (squarefree-certificate to catch eigenvalue collisions
between the two would-be ideals), union-find merge of the resulting PURE blocks by
bracket-connectivity (justified by the standard fact that a simple Lie algebra's root
graph is connected, so same-ideal blocks always eventually connect, while cross-ideal
brackets are identically zero so different-ideal blocks never do), then bracket-closure
to recover each full ideal, then **exhaustive** certification (every cross-ideal bracket,
not a sample).

Mirroring B1098's own stated practice ("pre-validated on synthetic sl₃⊕sl₃ data with
known ground truth, catching its own first-version bug before touching the real
algebra"), the same discipline was followed here: `test_ideal_split_synthetic.py` builds
two independent copies of sl₃ as explicit 3×3 matrices, embeds them block-diagonally in
gl₆, then applies a **fully random invertible 16×16 rational mix** (the hard case — *no*
starting basis vector is pure) before running `split_ideals` on the result. First attempt
hit a real bug: `sp.nsimplify()` applied to already-exact `sp.Rational` values (rather
than `sp.Rational()` directly) sent PSLQ hunting for closed forms and produced enormous
nested-radical garbage, hanging the run (caught by a timeout, diagnosed via a profiling
script, fixed by removing the stray `nsimplify` calls). After the fix: **PASS** — `dims
[8,8]`, `cross_brackets_zero=True`, and each recovered ideal verified **pure** against
the synthetic ground truth (lies entirely in one of the two known blocks). Only then was
the method applied to the real 78-dim centralizer data: **same result, `dims=[8,8]`,
`cross_brackets_zero=True`, `dims_match=True`** (2.2s).

**Building the adapted Cartan — standard method, not the generic-element fallback.** The
original (sympy-nullspace) 16-vector basis of `c` turned out to be almost entirely single
root/Cartan vectors (only one of the sixteen, a combination of `h0,h2,h3`, is a genuine
mix of both ideals — checked directly, not assumed). Reclassifying those clean vectors by
ideal membership (a rank test against each recovered ideal's span) found, per ideal, six
pure root-space members. `find_cartan_generators` then builds each ideal's own 2-dim
Cartan from two independent root-derived coroots `[e_r, e_{-r}]` — **certifying** each
before accepting it (must actually commute with X, H, Y). Both ideals succeeded via this
"standard method" (the prereg's named alternative to a generic-element Cartan); the
generic-element **fallback path was implemented but not needed** this run.

*A confusion caught and resolved along the way:* an early hand-exploration used
`H14 = [e_{root14}, e_{-root14}]` (root14 = the E6 root `(1,1,2,3,2,1)`) as one of the
adapted generators and worried it might carry a leftover component in the *other* ideal
(since its raw Cartan coordinates touch `h4,h5` too). Checked directly by solving
`H14 = (ideal-A part) + (ideal-B part)`: the ideal-A part is **exactly zero** — `H14` is
purely ideal-B despite its raw coordinates, because "purely in one ideal" is a
basis-independent subspace fact, not a "zero coefficients in some raw index set" fact.
No bug; a reminder that ideal-purity has to be checked as a subspace-membership question,
not eyeballed from sparsity patterns.

**Certification (all four, exact):**

| check | result |
|---|---|
| pairwise commute (all 6 pairs) | **True** |
| lie in `c` (commute with X,H,Y) | **True** |
| rank (linear independence) | **4** |
| diagonal on the 27 (⟹ semisimple) | **True, True, True, True** |

The generators produced this run: `H[(0,0,0,0,-1,-1)], H[(0,0,0,0,-1,0)]` (ideal A) and
`H[(-1,-2,-2,-3,-2,-1)], H[(-1,-1,-2,-3,-2,-1)]` (ideal B) — a *different* (but equally
valid) choice of root pair than the hand-exploration's `h1,h4,h5,H14`; both are bases for
the same abstract rank-4 Cartan of `c`, and both come out diagonal with small integer
eigenvalues on the 27 (checked with both; reported here is the script's own deterministic
choice, which depends only on the order sympy's `nullspace()` happens to return — re-run
twice, byte-identical both times).

**This is the headline structural win of Op1**: because the adapted generators are
genuine root-derived coroots (living inside the ambient Cartan span{h₀,...,h₅}), they act
**diagonally, with small integer eigenvalues (all in {-1,0,1})** on the 27 — unlike
B1100's fully generic random-combination Cartan, whose coordinates were cubic `CRootOf`
irrationalities. The prereg's named non-triviality ("if the ℚ-form's non-splitness lives
inside each factor, the coordinates stay in extensions") **did not occur** for this A2
landing: the ℚ-form splits cleanly.

## 2. Op2 — the joint weight table

Because all four generators are diagonal in the crystal (weight) basis, the joint
eigenspaces can be read off directly — but the **stacked-kernel method was still run in
full** as the certifying check (not skipped just because the diagonal case makes it
trivial): for every candidate 4-tuple, `stack = vstack(M_k - t_k I)` and
`d = 27 - rank(stack)`, exact.

Result: **15 distinct classes, sizes `[3,3,3,3,3,3,1,1,1,1,1,1,1,1,1]`, sum 27** — an
**exact match to B1100's banked pattern** (their `3⁶·1⁹`), now with **small-integer
coordinate tuples** instead of cubic irrationalities. Total Op1+Op2 runtime: **7.8s.**

## 3. Op3 — the collapse solve

**The banked target.** `frontier/B1100_landing_content/b1100_hypercharge.py`'s `target`
list — `[1/6]×6, [-2/3]×3, [1/3]×3, [-1/2]×2, [1]×1, [0]×1, [-1/3]×3, [1/3]×3, [1/2]×2,
[-1/2]×2, [0]×1` (27 entries; degeneracy pattern `(6,6,4,3,3,2,2,1)` as pre-registered).
Cross-checked against `docs/SM_SPECIFICATION_LEDGER.md`'s per-state hypercharge rows
(Q₍₁/₆₎×6, u꜀₍₋₂/₃₎×3, d꜀₍₁/₃₎×3, L₍₋₁/₂₎×2, e꜀₍₁₎×1, ν꜀₍₀₎×1 — one generation's 16 —
plus a second `(-1/3,1/3,-1/2,0)`-shaped block matching the standard E6-GUT `27=16+10+1`
branching's "10" piece): both sources agree exactly. No measured physics value entered
anywhere — this is the program's own banked integer/rational assignment (B950's ledger),
used per the prereg's license, unchanged from B1100.

**"Trial-0", read honestly.** B1100's literal `t_float =
[0.19087301,-0.20768005,-0.09401027,0.47783176]` (`b1100_hypercharge.json`) lives in
*their* fully-generic Cartan and does not type-check against this run's different
(root-adapted) basis — replacing that basis is the entire point of Op1. The
methodologically faithful reading of "trial-0's collapse assignment as the first
candidate" is to run the *same* random-direction method fresh, here. Done:
**20,000 random-direction trials, ZERO pattern-hits.** This is itself an interesting,
honestly-reported sub-finding — in B1100's basis the compatible cone was "open/generic,
hit at trial 0"; in *this* basis (small-integer weight coordinates rather than algebraic
irrationalities) the same naive search found nothing in 20,000 tries. That is consistent
with what Op4 finds below: the solution set here is a small **finite, isolated** set
rather than an open cone, so a uniform float search has a low chance of landing near one
by luck. `trial0_assignment_solves = False`, reported plainly rather than smoothed over.

**The exact, exhaustive path (not a sample).** Four of the fifteen classes turned out to
be exact ±standard-basis vectors (multiplicity 3 each) — i.e. literally `±e_k` for
`k=0,1,2,3`. Because these four are linearly independent, **a solving direction `t` is
completely determined by which target value gets assigned to each of them** — and
because each has multiplicity exactly 3, that assigned value **must** be one of the five
target values with multiplicity ≥ 3 (`{1/6, -2/3, 1/3, -1/2, -1/3}`; sizes `6,3,6,4,3`).
Trying **all `5⁴ = 625`** combinations is therefore a *complete* search over every
possible solving direction — not a heuristic, and provably unable to miss a solution.
(A general fallback path — pick any 4 linearly-independent classes, enumerate
multiplicity-respecting value assignments to them, solve, verify — is implemented and
would run if fewer than 4 pure classes existed; not exercised this run since the fast
path applied.)

**Result: 18 exact solving directions**, all denominators dividing 6, e.g.
`(1/6, 1/6, 2/3, -1/3)`, `(1/6, 1/6, -1/3, 2/3)`, ... (full list in `b1102_results.json`).
**C1 MATCH-EXACT: PASS.**

## 4. Op4 — exact verification and uniqueness

Every one of the 18 was independently re-verified (a second, separate pass) against the
full 27-state target multiset — all 18 pass. Before any of this, `b1102_solve.py`
re-derives the 27 from scratch (its own `load_ccb` + `build_27` + full 3003-pair
Chevalley re-certification) and re-checks that the loaded generators still commute with
`X,H,Y`, rather than trusting `b1102_intermediate.json` blindly — this is the closest a
single-session run can come to the prereg's "independent own-code verifier... before
banking" without a second, genuinely separate agent; recorded honestly as a partial,
not full, discharge of that method constraint.

**Uniqueness: NOT unique (18 solutions), and NOT a continuous family.** Each of the 18 is
an isolated point (a discrete linear system, solved exactly, not an underdetermined one)
— **dimension 0**. An attempt was made, in exploratory work on an earlier by-hand choice
of adapted basis (`h1,h4,h5,H14` — a different, though equally valid, root-coroot pair
than the one the finished script deterministically settles on), to explain the 18 as a
single orbit under the rank-4 Cartan's residual Weyl-type symmetry (S₃×S₃, order 36, from
the two ideals' reflection groups; the four individual reflections were explicitly built
and verified to correctly permute the 27's weight set exactly). The orbit of one solution
under this group had size 18 too, matching the count, but was **not set-equal** to the
found list under the direct coordinate pairing tried — a subtlety (Weyl's action on `t`
as a dual-space functional vs. on weights as vectors need not coincide with the naive
coordinate dot product used) that was not chased to ground within budget, and was **not
re-attempted on the final script's own basis** — so this paragraph is reported as a
suggestive, unconfirmed lead, not a checked fact, and should not be read as more than
that. What **is** fully certified, independent of this loose end, is completeness: the
exhaustive-search argument above (§3) proves 18 is the *exact*, *complete* count for the
actual, final basis, not a sample and not basis-dependent luck. Reported as: **a finite,
explicit, zero-dimensional set of size 18**, plausibly (but not proven here) a single
orbit of some residual discrete symmetry.

## 5. Op5 — the su(2) beside it

**Identifying color vs. the su(2) factor.** The prereg's suggested discriminant ("color =
the ideal under which the 27 decomposes as 9 copies of 3 or 3̄") turned out **not** to
cleanly separate the two ideals: both show the *same* symmetric weight pattern under
their own 2-dim Cartan (`0×9` plus all six roots ×3 each) — a direct consequence of the
trinification structure `27 = (3,3̄,1)⊕(3̄,1,3)⊕(1,3,3̄)`, in which every surviving factor
plays the "3", "3̄", and "1" role once each across the three blocks. So the two ideals are
structurally interchangeable at this level; which one hosts the su(2) was decided
constructively instead, as below.

**Y-neutral roots.** For the representative solution `t = (1/6, 1/6, 2/3, -1/3)`, both
ideals' three positive roots were tested for `t·(root's own weight coordinates) = 0`
(the condition for that root's raising/lowering operators to preserve Y). Result:
**exactly one Y-neutral root per ideal** (2 total). Checked across **all 18** solutions,
not just the representative: **every single one has exactly 2 Y-neutral roots** (one per
ideal) — a clean, universal, exactly-verified structural fact, not a fluke of the chosen
representative.

**The su(2), built and certified.** An `sl₂`-triple `{e,h,f}` from one Y-neutral root
(this run: ideal A's root `(0,0,0,0,0,-1)`), verified:

- Chevalley relations `[h,e]=2e, [h,f]=-2f, [e,f]=h` — **exact**.
- Commutes with the **entire other ideal** (all six roots + both its own Cartan
  generators, not just its Cartan) — **exact, True**.
- Commutes with the solved `Y` — **exact, True**.
- `[H,E]=2E, [E,F]=H` re-verified on the **full 27×27** representation matrices (sympy
  exact rational matrix multiplication) — **exact, True**.

**Decomposition.** Under this su(2): **6 doublets (12 states) + 15 singlets — exactly 27,
with ZERO triplets or higher** (only eigenvalues `-1,0,1` occur on the 27 under `h`,
confirmed by construction, not assumed). Of the six doublets: **three carry distinct
nonzero "color"-Cartan weight** (Y = 1/2, -1/2, -1/2 respectively) and **three carry zero
color weight, all at the SAME Y = 1/6** — the latter is a clean, single, well-defined
`(1,2)_{1/6}`-type triple (three copies of one color-singlet doublet, structurally
"3 L-doublets"-shaped). The former three do *not* share one Y value, so they do **not**
organize into a single clean `(3,2)_Y` irreducible block under a genuine unbroken color
SU(3) — which brings us to:

**The honest, precisely-located caveat (a sharper finding than C3's literal text asks
for).** Checked directly, not assumed: **does the full color ideal — its raising/lowering
root generators, not just its own 2-dim Cartan — actually commute with the solved Y?**
**No.** For the representative: `[e_{color-root}, Y] ≠ 0` for at least one color root.
Checked across **all 18** solutions and **both** ideals (36 checks total, each an exact
bracket computation): **for NO solution does either full ideal commute with Y as a
whole.** Only each ideal's own 2-dim Cartan (trivially, since Cartan is always abelian)
and the exhibited su(2) commute with Y. So the clean product picture "SU(3)_color ×
SU(2) × U(1)_Y, all three mutually commuting" does **not** emerge from any of the 18
exact solutions — only "U(1)×U(1) (color's Cartan) × SU(2) × U(1)_Y" does. This is a
genuine, robust, solution-independent structural fact about this A2 landing, reported in
full rather than smoothed into the su(2)-only criterion C3 literally asks about (which
does pass — see below).

**Structure-level only.** Per the prereg: **chirality-at-count is NOT claimed.** The
doublet/singlet split, the color-weight labels, and the Y values are all structural
(representation-content) facts; nothing here asserts a left/right chirality assignment or
a fermion-count claim beyond the multiplet shapes computed.

## 6. Verdict, against the pre-sealed outcome grammar

**C1 MATCH-EXACT: PASS.** An admissible assignment (in fact 18) reproduces the banked
6Y-derived multiset exactly — proven by a complete, not sampled, enumeration.

**C2 UNIQUENESS/PRICE: characterized, not unique.** 18 isolated exact solutions,
zero-dimensional (not a continuous family); a residual discrete freedom, priced at
`log₂(18) ≈ 4.17` bits if a bit-count is wanted, though the prereg only asks
unique-vs-family and the honest answer is "neither — a finite explicit set, fully listed."

**C3 SU(2)-COMPATIBILITY: PASSES on its literal text** (the exhibited su(2) does not
misalign with Y; the doublet structure lands as doublets/singlets only, with a clean
three-copies-one-value color-singlet doublet triple) **— carrying one honest, sharper,
solution-independent caveat**: the full color SU(3) (beyond its own Cartan) never
commutes with the solved Y, for any of the 18 exact solutions, so the clean
SU(3)×SU(2)×U(1) *product* structure is not achieved even though the *numbers* match
exactly.

**Overall reading, stated plainly and without softening either side**: the landing's
u(1) cone, shown pattern-compatible by B1100, is now shown **value-compatible** too — an
exact match exists, exhaustively verified, closing B1100's named residual on the positive
side. The A2 landing **carries the banked hypercharge exactly**, at a priced 18-fold
discrete freedom. But the fuller gauge-structure question this makes newly askable — does
a clean unbroken SU(3)×SU(2)×U(1)_Y product emerge, not just the right numbers — gets a
**no**, checked directly rather than assumed away. Neither fact should be read through
the other: the hypercharge VALUES match exactly (a real, hard-won positive); the
PRODUCT-GROUP structure a physicist would want alongside those values does not (a real,
precisely-located complication). "Standard-Model-shaped" is fair at the value level;
"SM-contained at the A2 stratum" as a full gauge structure is not yet earned by this
computation and should not be claimed from it.

**negative_type: None** (this is not a NO-EXACT-MATCH run — C1 passed).

## 7. What smelled interesting / worth a second look

- The naive float search failing completely (0/20000) in this basis while the exact
  search succeeds completely (18/625, a 2.9% hit rate over the *relevant* combinatorial
  space) is a nice, self-consistent picture: this basis's compatible set is finite and
  isolated (measure zero in the continuum), unlike B1100's open/generic cone. Worth
  remembering as a general lesson: "pattern-hit at trial 0" is a property of the *basis
  chosen*, not of the underlying question, and a harder-to-float-hit basis can still be
  exactly, exhaustively solvable.
- The Weyl-orbit characterization of the 18 solutions (§4) is the one loose end not fully
  closed — the *count* and *completeness* are proven regardless, but a clean
  group-theoretic "why 18" was not reached. Named as a residual, not hidden.
- The color/Y non-commutation (§5) is the most important substantive finding beyond the
  prereg's literal asks. It is exact and solution-independent (36 checks, all negative),
  not a numerical coincidence of the one representative direction.

## 8. Resources

Total wall time: **Op1+Op2 ≈ 7.8s, Op3+Op4+Op5 ≈ 5.2s (after a matmul optimization —
sympy exact matrix multiplication instead of a hand-rolled Python triple loop over
Fractions, which had taken ~93s for one step; same exact result, ~20x faster). Combined
≈ 13 seconds**, far inside the ~3 hour budget; no step stalled, so the named fallback
(cubic-CRootOf path) was not invoked for runtime reasons — it also was not invoked
because the "standard method" (root-derived coroots) succeeded directly (see §1). All
arithmetic exact throughout (Python `Fraction` / sympy `Rational`); no floats entered any
banked number — floats were used only for the trial-0 search (§3, explicitly reported as
a negative/non-hit) and are absent from every accepted result. No network. No measured
physics value anywhere.

## 9. Files

- `b1102_common.py` — shared engine: `load_ccb`, `build_27` (own crystal-of-ω₁
  construction), `verify_27_is_a_rep`, ad-matrix helper, modular-rank cross-check.
- `b1102_ideal_split.py` — the general ideal-splitting algorithm (primary decomposition +
  bracket-connectivity merge + closure), own code.
- `test_ideal_split_synthetic.py` — the pre-flight synthetic sl₃⊕sl₃ (fully mixed basis)
  validation of `split_ideals`, run and passing before the real-data run.
- `b1102_adapted_basis.py` — Op1 (adapted re-basis) + Op2 (joint weight table); writes
  `b1102_intermediate.json`.
- `b1102_solve.py` — Op3 (collapse solve) + Op4 (exact verification/uniqueness) + Op5
  (the su(2) beside it); reads `b1102_intermediate.json`, writes `b1102_results.json`.
