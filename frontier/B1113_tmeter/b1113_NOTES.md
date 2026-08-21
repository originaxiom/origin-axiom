# B1113 verification notes — THE JORDAN t-METER (JORDAN_MEMO.md §B)

Status placeholder — filled in after `b1113_verify.py` finishes running.
This file records the operator reconstruction and its justification in full,
independent of the run's numeric outcome, so the reasoning is auditable even
if the run turns out DISCREPANT or the numbers don't match the memo's.

## 1. What was being verified

JORDAN_MEMO.md §B claims, on the twisted double of the figure-eight complement
(B1086 machinery, `frontier/B1086_spectrum_law/`), with theta-odd dial
parameter t ∈ {0, 1, 2, ω}:

1. `tr(A·B_R)` is t-INDEPENDENT (memo's number: `141750+1011915q` at every t).
2. `tr(B_L·B_R)` and `tr([B_L,B_R])` SEPARATE every dial value.

Nowhere in `frontier/B1086_spectrum_law/FINDINGS.md`, its `arc_verdict.json`,
or the certificate `twisted_double.py` are operators literally named `A`,
`B_L`, `B_R` defined. The memo's own probe output
(`breakthrough_memos/jordan_probe_out.txt`) shows only stage-0..stage-3 print
lines (e6 load, principal sl2 + dial slots, the 27, the relator check) and
then jumps directly to the trace table — it does NOT run the certificate's
stage 4 (Fox calculus H¹), stage 5 (longitude search), or stage 6
(Mayer–Vietoris double). That is the strongest single clue to what the memo's
operators are: they are built from stage-0..stage-3 objects only (the e6
load, the 27, the principal sl2, the dial slots hv8/hv16, and the Riley-type
generator matrices A27, B27) — no cohomology, no longitude, no doubled space
required.

## 2. The reconstruction

- **A := A27 = ρ(a)** — the meridian / peripheral generator (in the
  certificate's own naming: `A27 = nilexp(E27p, ONE)`, "Riley A=[[1,1],[0,1]]
  = exp(e)"). Chosen because:
  - the memo writes it unsubscripted ("A", not "A_L"/"A_R"), matching that
    the meridian is literally the curve IDENTIFIED across the gluing torus
    (both copies share it) — it is "the seam" in the most literal sense;
  - the certificate's own stage-6 code asserts `Dt` (the dial) commutes with
    both the meridian and the longitude on the SAME copy — "dial must
    centralize the cusp" (needed for the twisted-double construction to be a
    well-defined gluing at all). That is exactly the property needed to make
    "A" dial-blind irrespective of which copy it is evaluated in, so there is
    no need for an "A_L"/"A_R" distinction.

- **B_L := B27 = ρ(b)** — the certificate's OTHER Riley generator
  (`B27 = nilexp(F27p, QQ)`, "B=[[1,0],[q,1]] = exp(qf)"), untwisted (left
  copy, no dial applied). Chosen because "b" is explicitly NOT part of the
  peripheral subgroup: the certificate's stage 5 has to go SEARCH for the
  longitude as a nontrivial word in a and b (`lam_word = 'bABaaBAb'`), which
  means <a, b> ⊋ the peripheral subgroup <a, λ>. So b is a genuinely
  "single-hand" (non-boundary) generator — the natural reading of the memo's
  "single-hand words" as opposed to A's "seam-crossing" status.

- **B_R(t) := D(t)·B27·D(t)⁻¹**, D(t) = exp(t·ρ(x_slot)) — the SAME
  generator, evaluated in the right copy's dial-twisted coefficient system.
  This is CONJUGATION, not a bare product `D(t)·B27`. Two independent reasons:
  1. *It is what the certificate's own Mayer–Vietoris code actually does.*
     `mv_h1()` twists right-copy cocycle VALUES by left-multiplying with
     `Dm` (`u=[_dot(Dm[i],u) ...]`). For a cocycle z of a representation ρ,
     the map z ↦ D·z is exactly the cocycle transformation induced by
     replacing ρ with ρ'(g) = D·ρ(g)·D⁻¹ (direct check:
     z'(gh) = D·z(gh) = D·(z(g)+ρ(g)z(h)) = z'(g) + (Dρ(g)D⁻¹)·z'(h)).
     So "the right copy, dial-twisted" means precisely "the representation
     conjugated by D(t)", and B_R(t) is the b-generator's matrix in that
     conjugated representation.
  2. *It is the unique simple convention that reproduces the memo's claimed
     algebra, GIVEN control #5 below.* If A commutes with D(t) for all t
     (verified directly, not assumed — see §3), then for B_R = D·B27·D⁻¹:
     ```
     tr(A·B_R) = tr(A·D·B27·D⁻¹) = tr(D·A·D⁻¹·D·B27·D⁻¹)  [A=DAD⁻¹, A central to D]
               = tr(D·A·B27·D⁻¹) = tr(A·B27)         [trace is conjugation-invariant]
     ```
     — CONSTANT in t, for *any* B27, by a two-line argument that only uses
     "A commutes with D(t)". A bare-product convention `B_R = D·B27` gives
     `tr(A·B_R) = tr(D·A·B27)`, which does NOT telescope away and is
     generically t-dependent — contradicting the memo's central claim. So
     dial-blindness of tr(A·B_R) essentially FORCES the conjugation reading.

- **`[B_L,B_R]`** — checked under BOTH readings, reported explicitly:
  - *Lie/matrix commutator* `B_L·B_R − B_R·B_L`: its trace is IDENTICALLY
    ZERO for ANY two square matrices whatsoever (`tr(XY)=tr(YX)` always, for
    all X,Y — this is why "trace" and "traceless = sl_n" are synonymous).
    Computed as an internal sanity check; it cannot be the memo's reported
    nonzero, t-varying numbers, and the script asserts it is exactly zero at
    every cell as confirmation the arithmetic is sane.
  - *Group commutator* `B_L·B_R·B_L⁻¹·B_R⁻¹`: generically nonzero and
    t-dependent — the natural "commutator" in a discrete representation /
    Wilson-line setting (which this whole construction is: A27, B27 are
    GROUP elements, not Lie-algebra elements). Reported as "the" answer.
  - **A falsifiable prediction made BEFORE running the numbers**: at t=0,
    D(0)=exp(0)=I, so B_R(0)=B_L exactly, so the group commutator is the
    identity matrix and `tr([B_L,B_R])=27=dim`, and separately
    `tr(B_L·B_R)|_{t=0} = tr(B27²)`, which is also exactly 27 because B27 is
    UNIPOTENT (all eigenvalues 1, being exp of a nilpotent matrix), and any
    power of a unipotent matrix is again unipotent, so its trace is the
    dimension. **Both predictions were written down before inspecting
    jordan_probe_out.txt's t=0 row — which reads exactly `27` for both
    quantities.** This is filled in as a match/mismatch check in the results.

- **Dial slot**: the memo does not say which theta-odd slot (hv8 or hv16) it
  used. This bench computes BOTH and reports hv8 as primary (it is the slot
  used first/by default throughout the certificate's stage-6 sweep), with
  hv16 as a robustness cross-check.

## 2b. Fences on this reconstruction

- This is a RECONSTRUCTION, not a citation. No file in the banked record
  spells out "A = ...", "B_L = ...", "B_R = ...". The argument above is a
  best-effort, auditable inference from (i) the certificate's own variable
  names (A27/B27 literally named A/B), (ii) the structural centralization
  facts the certificate asserts and this bench independently re-verifies,
  (iii) what makes the memo's own claimed algebra true by a clean two-line
  argument rather than by numerical accident, and (iv) a sharp t=0 prediction
  checked against the memo's own printed numbers. If a different, differently
  named construction was actually used upstream, this bench's numbers may not
  match the memo's even though the qualitative law (dial-blind vs separating)
  could still hold for a structurally analogous reason.
- The group-commutator reading of `[B_L,B_R]` is a choice, not a derivation;
  the Lie-bracket reading is ruled out by a hard fact (always-zero trace),
  but among remaining options (group commutator in either order,
  B_R·B_L·B_R⁻¹·B_L⁻¹, etc.) this bench picked the standard order and
  reports it plainly so it can be checked against the alternative if needed.

## 3. Controls (run BEFORE trusting the new traces)

Filled in from the actual run — see the "positive_controls" block of
`b1113_results.json` and the terminal log for pass/fail and exact values.

1. **rho27 respects all C(78,2)=3003 Chevalley brackets** (exhaustive,
   reproduces the certificate's own "stage 1 VERIFY ... PASS").
2. **Principal string content = [16, 8, 0]** (reproduces the certificate's
   "stage 2: principal strings: [16, 8, 0]").
3. **Relator `a·w·b⁻¹·w⁻¹` (w=bABa) acts as the identity on the 27**
   (reproduces the certificate's "stage 3: relator ... PASS"; independently
   cross-checked by `tests/test_b1086_spectrum_law.py::test_relator_and_riley`,
   the SAME relator in the SL(2) 2×2 case).
4. **h¹(M;27) = 3** via Fox calculus on the SAME presentation/generators —
   the explicit banked NUMBER in `FINDINGS.md` ("h¹(M;27) = 3 = 1+1+1
   solo"). This is the primary "reproduce a banked B1086 number" control the
   task requires, closing the gap that `jordan_probe_out.txt` itself never
   ran this stage.
5. **D(t) centralizes A27** (the meridian), independently verified at every
   t for both theta-odd slots — the one structural fact the whole
   t-independence argument in §2 rests on. NOT assumed from the certificate's
   own (unverified-by-this-bench) assertion; recomputed from scratch here.

Controls 1–3 and 5 validate every piece of machinery the NEW trace
computation touches (e6 load, principal sl2, dial slots, the 27, A27, B27,
D(t), and the one commutation fact). Control 4 is the FINDINGS.md-explicit
"banked number" the task's CONTROLS clause asks for; it exercises
Fox-calculus machinery that the main computation does not otherwise need, but
is cheap given the same A27/B27 are reused, and it is a genuine independent
check on the representation's correctness (a wrong sign or wrong crystal
convention would very likely perturb this rank computation even if it
happened to leave the relator satisfied).

**Scope decision, stated honestly**: this bench did NOT reproduce the
doubled/twisted numbers h¹(D_t;27) = 5/2/5 (FINDINGS.md's headline spectrum
law), because that requires the longitude search + torus cohomology +
Mayer–Vietoris machinery (certificate stages 5–6), which the memo's OWN new
claim does not use (its traces are plain 27×27 matrix products, not
cohomology classes — confirmed by jordan_probe_out.txt stopping after stage
3). Reproducing h¹(D_t;27) as well would have been a strictly stronger
control but was judged not to touch anything the new claim depends on beyond
what controls 1/2/3/5 already cover, and was traded against the time budget.

## 4. Results

Run completed in **14.8s** (wall clock, single-threaded, `python3`, exact
`Fraction`/`sympy.Rational` arithmetic throughout, no floats).

### 4.1 Positive controls — ALL FIVE PASS

| # | check | result |
|---|---|---|
| 1 | ρ27 respects all C(78,2)=3003 Chevalley brackets (exhaustive) | PASS |
| 2 | principal string content = [16, 8, 0] | PASS |
| 3 | relator `a·w·b⁻¹·w⁻¹` (w=bABa) = identity on the 27 | PASS |
| 4 | **h¹(M;27) = 3** (Fox calculus; the explicit banked FINDINGS.md number) | **PASS (computed 3)** |
| 5 | D(t) centralizes A27, both theta-odd slots, all t | PASS |
| — | sanity: tr(matrix/Lie commutator) ≡ 0 at every cell | True, as required |
| — | t=0 sharp prediction (tr(B_L B_R) = tr([B_L,B_R])_group = 27 = dim) | CONFIRMED |

Every control that could have caught a wrong sign, wrong crystal convention,
wrong nilpotent-exponential recipe, or wrong operator identification passed.
Nothing stopped the run; the new traces below are trusted on that basis.

### 4.2 The three traces, slot hv8 (primary), exact

```
t       tr(A.B_R)              tr(B_L.B_R)                                              tr([B_L,B_R]) [group commutator]
0       141750+1011915q        27                                                       27
1       141750+1011915q        -4268791455703081896933+4496860756304889154560q          -1012494675441866094969680468476925337415653-19181399207157472539697602748942049339166720q
2       141750+1011915q        -1136640792617359937187813+1151247446406074247229440q    -16755160684243541173825124529943231919652126693-1308432850647916106766787473050401389584509255680q
omega   141750+1011915q        4725568716294111759387                                   21245539863128390787066847414681242215854107
```

- **tr(A·B_R): dial-blind — CONFIRMED.** Exactly `141750+1011915q` at all
  four t (bit-for-bit identical Fraction pairs, not just "close").
- **tr(B_L·B_R): separates all four t — CONFIRMED.** Six pairwise
  comparisons (0/1, 0/2, 0/ω, 1/2, 1/ω, 2/ω), all distinct.
- **tr([B_L,B_R]) (group commutator): separates all four t — CONFIRMED.**
  Same six-way distinctness.
- **tr([B_L,B_R]) (Lie/matrix commutator, sanity channel): identically 0 at
  every cell**, exactly as forced by linear algebra alone (tr(XY)=tr(YX)
  always) — confirms this reading is NOT what the memo's nonzero numbers
  can mean, and that the arithmetic pipeline is internally consistent.

### 4.3 Cross-check against the memo's own printed numbers

The memo's `jordan_probe_out.txt` numbers were NOT used as an input to this
script's construction (the operator reconstruction in §2 was fixed by
structural argument first); the comparison below is informational, done
after the fact.

- **Slot hv8 (primary): matches on 12/12 cells** — every single digit of
  every reported Fraction pair, across all three quantities and all four t,
  including 40+ digit integers. This is not the kind of agreement that
  happens by accidental convention choice; it means the outside bench's
  unstated A/B_L/B_R construction and dial slot were reconstructed exactly.
- Slot hv16: matches on 6/12 cells — precisely the 6 cells that are
  slot-independent by construction (tr(A.B_R) at all 4 t, since A commutes
  with the dial regardless of slot per control #5; plus the two t=0 values,
  which are forced to 27 regardless of slot since D(0)=I for any slot). The
  other 6 (t=1,2,ω values of tr(B_L.B_R) and the group commutator, which
  genuinely depend on which nilpotent generator drives the dial) do NOT
  match hv16 — confirming the memo's numbers were built from hv8
  specifically, not hv16, and that hv16 is a genuinely different (not
  accidentally identical) operator.

## 5. Verdict

**CONFIRMED.** Both parts of the memo's §B claim hold, exactly, on this
bench's independent construction:
1. tr(A·B_R) is t-independent (dial-blind) — the seam operator A, which the
   dial is required to centralize for the twisted double to be a
   well-defined gluing at all, produces a trace that cannot see t, by a
   clean two-line conjugation-invariance argument (§2), confirmed exactly.
2. tr(B_L·B_R) and tr([B_L,B_R]) (group commutator) separate all four dial
   values exactly — a mixed (seam-crossing, in the sense of pairing the
   untwisted left generator against the dial-twisted right one) word sees
   the dial where a single-copy word cannot.

The sharp law as stated in the memo — "free data of one object (the dial) =
forced/character-level data of the coupled pair" — is exactly what happens
here: t is unmeasurable via any operator that must commute with it in a
single copy (B1087's own finding), but becomes a class-function-level
invariant (a trace) of the two-copy pair the moment a genuinely
non-centralizing generator is used to couple them.

Operator-identification confidence: **HIGH**, upgraded from "best-effort
reconstruction" to "exact reproduction" by the unforced 12/12 digit-for-digit
match in §4.3, which was not targeted or curve-fit (the construction in §2
was fixed before the comparison was run).

Nothing smelled wrong. Runtime, control coverage, and the independent
digit-exact reproduction all came in cleaner than expected for a same-day
reconstruction of an unstated operator convention.

## 5. Portability caveat

`twisted_double.py` (the outside-bench certificate this arc's construction is
read from) has its OWN internal hardcoded absolute import:
```
spec_from_file_location("ccb", "<paper-branch>/verify/check_charge_bracket.py")
```
which points outside `origin-axiom` entirely, to a separate parallel-audit-seat
checkout that happens to exist on this machine but is not part of the
read-only repo this task specifies. `b1113_verify.py` therefore does NOT
dynamically load `twisted_double.py` at runtime; it reads it as a design
reference only, and independently rebuilds the needed pieces against the
repo's own vendored, sha256-provenanced copy of the SAME e6 module
(`frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py`, whose
header records the original's sha256 as
`4f10df9f55bd58bfb814f8b4428ff55bc710d4e49713876797b5c35f5990455f` — confirmed
by this bench to match the outside file byte-for-byte). This makes
`b1113_verify.py` runnable on any checkout of this repo without depending on
a second, machine-specific worktree.
