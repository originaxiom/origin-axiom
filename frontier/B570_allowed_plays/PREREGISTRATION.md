# B570 — THE ALLOWED PLAYS: the stage's selection rules, proved wholesale

**Preregistered:** 2026-07-14. **Status:** queued (launches when the day-0 internalization
campaign completes). **Owner directive:** *"a deeper investigation campaign on what exact
plays are allowed on the stage, or what exact plays are forbidden, so we understand what's
allowed to pass."*

## The inversion

Sixteen σ→SM chains were killed retail — each incoming play triggered its own
investigation. This campaign proves the selection rules **wholesale**: characterize the
full set of plays the stage admits, as a decidable membership test. Any future play
(the SM included) is then checked against a theorem, clause by clause, in minutes.

It extends B568-SQ (the *minimal* play → **all** plays) and B569 (one selector killed →
**all** selectors classified).

## Definition (play)

A play is an assignment to the five slots the program has already established:

| Slot | Content | Known constraint (banked) |
|------|---------|---------------------------|
| M — matter | species/cast with 2d anomaly conditions | 3 casts at total 7 (B568-SQ); Σχ, Σχ³ conditions mod 11 (B565) |
| T — theater | the modular/anyon data hosting the monodromy | DFib at rung 0 only; E₆,₁ hosts ρ(A₁) with Z=+1 (B569) |
| S — selector | the rep-theoretic channel through the algebra face | F₄ route vector-like, ALL subgroups (B569); no real form (B565-H1) |
| D — dynamics | the clock/Hamiltonian compatible with the monodromy | order arguments kill SM-like spectra at level 15 (B567) |
| Λ — scale | absolute units | ABSENT (banked; the one structurally missing slot) |

## The cells

**AP1 — the cast lattice (matter).** [sonnet] The full solution set of the banked 2d
anomaly conditions mod 11 — all casts, all totals, not just the minimal stratum. Is the
solution set a monoid/lattice? Present generators. Verify first, from the bank, the exact
constraint form (B565: Σχ ≡ 6, Σχ³ ≡ 4 mod 11); recompute in-sandbox. Deliverable: the
cast monoid, presented; the 3 minimal casts recovered as its bottom stratum.
*Falsifier: the solution set has no finite presentation → report the growth function instead.*

**AP2 — the allowed-theater table (quantum).** [sonnet compute, opus verify] For every
small consistent modular datum — abelian (ℤ/N, q) for N ≤ 24 (all quadratic forms,
Gauss–Milgram-consistent pairings only) plus the standard low-rank nonabelian theories
(Fib, DFib, Ising, SU(2)ₖ small k) — evaluate the monodromy: ρ(A₁), Z = Tr ρ(A₁), order,
θ-structure. B569's row (E₆,₁ ≅ ℤ/3, q = 2a²/3: Z = +1, θ-split {±i | +1}) is the seed.
Pattern questions (preregistered, falsifiable): Is Z always real? Always in {0, ±1, ±√N…}?
Which theaters are *blind* to the object (Z = rank or factorizes) vs *sighted*?
*Consistency gate first, always — the B569 lesson: an inconsistent (S,T) makes every
downstream number word-dependent noise.*

**AP3 — the clock arithmetic (allowed frequencies).** [sonnet] ord(A₁ mod N) for all
N ≤ 1000 — pure arithmetic of A₁ = F², i.e. Pisano-period arithmetic. Preregistered
conjecture: the order of ρ(A₁) in any level-N theater is determined by (divides a fixed
function of) the Pisano period π(N) and the c mod 24 phase. If it holds on the AP2 table:
*the stage's allowed plays tick at Fibonacci–Pisano frequencies* — prove it; if not, bank
the counterexample.

**AP4 — the chiral-selector table (the complex side).** [opus; the deepest cell] Classify
the maximal (and second-layer) connected subgroups H ⊂ E₆ by whether 27|_H is complex
(chirality-capable) or self-conjugate: Spin(10)×U(1), SU(3)³, SU(6)×SU(2), F₄, Sp(8),
G₂×SU(3)… — a finite branching table, computable from weight systems (B569's method:
exact root/weight arithmetic; the F₄ row is already proved self-dual). THEN the
object-side question: the Zariski closure of the object's holonomy inside E₆(ℂ) (from the
B565 explicit construction) — is the 27 irreducible under it? Which rows of the table are
*reachable*? This operationalizes the two-sides reframe (B569 discussion): the compactness
failure and the chirality wall may be one fact — chirality lives on the complex side,
where the object already lives.
*Falsifier for the reframe: the closure lands inside a θ-stable subgroup → the chirality
wall holds even complexified; bank that as the fifth wall.*

**AP5 — the order obstruction (dynamics).** [sonnet] Generalize B567: for a play at level
N, the projective order of A₁ in SL(2,ℤ/N) constrains every Hamiltonian's spectrum
(H = −i log ρ(A₁) has frequencies in (2π/ord)·ℤ). Table over the program's levels
(3, 5, 11, 15, 30, 165, 1155…). Deliverable: the order-obstruction criterion as a
one-line test any dynamical play must pass.

**AP6 — THE SELECTION-RULES THEOREM (synthesis).** [fable] Assemble: *a play passes iff
M ∈ cast-lattice ∧ T ∈ sighted-theaters ∧ S ∈ reachable-chiral-selectors ∧ D passes the
order obstruction ∧ Λ is relational (no absolute scale).* Then run through the rules ONCE,
clause by clause: (i) the SM — the definitive gap-spec, sharper than all sixteen
adjudications combined; (ii) two controls (a random anomaly-free toy; the Ising world) to
show the rules discriminate; (iii) the minimal play (B568-SQ) recovered as the theorem's
ground state.

## LANE C — the seventeenth question (the object's chirality vs the play's chirality)

**Added 2026-07-14** after the incoming five-sources/θ-odd handoff, processed
verify-don't-trust. **Its structural spine verifies exactly** (locks:
`tests/test_b570_theta_odd_spine.py`): E₆ exponents {1,4,5,7,8,11}, F₄ exponents
{1,5,7,11}, θ-odd = {4,8} (H¹ split 4+2); the **ω-connection** — the θ-odd Coxeter
eigenvalues e^{2πi·4/12}, e^{2πi·8/12} are exactly ω, ω² (the Eisenstein chirality
window B356 and the θ-odd sector are the same structure); E₆ level 2 has exactly 9
integrable reps, θ-split 3 fixed + 3 pairs (θ-odd dim 3); the banked non-real trace
lies in ℚ(√−3)∖ℝ.

**Adjudication of the assembly:** the five banked sources are real (B470 limbs,
B356 window, B469 residue, the σ̄≢σ arrow, B565-H1 non-real traces). The claimed
*convergence* of all five on the θ-odd sector is proved only for sources 2 and 5 —
which are literally the same fact (the holonomy fixes one embedding of ℚ(√−3)).
Sources 1, 3, 4's θ-odd links are conjectures — they ARE cells C4/C5 below. The
B470 table row ("the 5-fold cover lives in the θ-odd exponents") is unestablished
(exponent 5 is θ-EVEN; the handoff's own Task 4 concedes this). The T3/SQ
"reinterpretations" are labeled interpretations: the T3 theorem (chiral index ≡ 0)
is untouched; whether it "only tested the θ-even face" is exactly what C1–C3
decide. The gap⟺chirality duality converges with the B569 two-sides reframe —
independently reached by both seats — and is cell C2's theorem to prove or break.

- **C1 — cusp-sign propagation.** [sonnet] Does the cusp orientation (the sign of
  √−3 fixed by the holonomy) propagate to a preferred sign in the exponent-4
  deformation direction of H¹? Compute the θ-odd deformation pairing explicitly.
- **C2 — the gap-chirality duality theorem.** [opus] State and prove (or break):
  traces real ⟺ ρ̄ ≅ ρ ⟺ holonomy conjugates into a real form (with the Galois-
  descent obstruction as the fine print). If true: the compactness gap and the
  chirality are formally dual — you cannot close one without losing the other.
- **C3 — the level-2 monodromy on the θ-odd 3-space.** [opus; the sharpest cell]
  Build the E₆ level-2 modular data (9 primaries, Kac–Peterson S, T with c =
  2·78/14 = 78/7; consistency gate FIRST — the B569 lesson), evaluate ρ(A₁), and
  restrict to the 3-dim θ-odd subspace. Level 1 was trivial there (+1, B569); if
  level 2 acts nontrivially — distinguishing 27-type from 27̄-type — chirality is
  DYNAMICAL, not just structural. Falsifier: trivial again → the θ-odd sector is
  monodromy-blind at low level; bank the null.
- **C4 — the cover-chirality census.** [sonnet] Which cyclic covers of 4₁ are
  chiral (B470's limbs), and does chirality correlate with the θ-odd exponents
  {4,8} (i.e. covers of degree ≡ 4, 8 mod 12?) or with the interaction of sectors?
  In-sandbox via cover invariants (Alexander/torsion asymmetry under mirroring).
- **C5 — the arrow → level-sign transport.** [sonnet] Reversing orientation maps
  CS level k → −k and ω ↔ ω̄. Does the σ/σ̄ dynamical arrow (D_KL ≈ 12 bits)
  transport to the sign choice (k > 0, +√−3) the holonomy fixes? Make the
  transport explicit or bank the disconnect.

Lane C sharpens AP4: if C2 holds, the AP4 reachability question becomes *the*
question — the object's chirality exists (five sources); whether any play can
carry it is decided by which chiral selectors its E₆(ℂ) holonomy reaches.

## Discipline

Adversarial verification per cell (kills need in-sandbox discriminating facts; JEWEL
verdicts get maximum scrutiny). Every table row that banks gets a lock. Consistency gates
before evaluation everywhere (the B569 lesson). Firewall: the theorem classifies the
stage's admissible structures; the SM appears only as a clause-by-clause audit subject;
nothing to CLAIMS.md. Fold in the day-0 internalization campaign's chirality dossier and
buried-treasure list before launch (they may add cells or sharpen AP4).
