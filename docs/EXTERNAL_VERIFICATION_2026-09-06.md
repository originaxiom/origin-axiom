# EXTERNAL VERIFICATION — 2026-09-06: the record re-derived by a fresh seat, the assembly against the Standard Model, and the deciding computation B1260 named

*A fresh seat, no shared session state, working from a clean clone with the full history fetched
(2864 commits, 2026-05-22 → 2026-09-06). Brief from the owner: clone, analyse, verify the claims;
the goal being a parameter-free derivation of the Standard Model from the object; and the standing
rule that nothing may be called missing until the repository has been swept for it. Everything below
was recomputed with code written for this document (`scripts/external_verification/`), or is cited
to the arc that establishes it. Register: structure statements only; no measured value is asserted
anywhere; Gate 5 untouched.*

---

## 0. The verdict in one paragraph

The mathematics the record calls proved is correct wherever this seat re-derived it (18 of 18 spine
checks, the twisted-cohomology dimension law, the anomaly and global-form computations). The record's
own account of its physics reach is also correct, and it is the same account from June to today: the
object hands over the algebra E₆ through the McKay correspondence, and from E₆ the textbook
grand-unified descent reproduces the Standard-Model-shaped algebra, the ℤ₆ global form, the
hypercharge direction and `sin²θ_W = 3/8` — none of which discriminates E₆ from SU(5) or SO(10), and
none of which uses the object past its trace field. What a parameter-free Standard Model needs beyond
that — three chiral generations, a Higgs sector with a potential, the Yukawa and gauge values, a
four-dimensional action — is not present anywhere in the corpus as a derivation. This is not a claim
made from memory: the repository's own absence-sweep and already-banked instruments were run on every
one of those items (§6), and every hit is a ledger row recording the absence, a literature scout, or
a possibility-space exhibit. The one live computation the owner's main goal named this week
(`docs/MAIN_GOAL.md` JOIN 1, question 1; `frontier/B1260_where_chirality_can_live/FINDINGS.md`) was
run here to completion and lands on the closing branch: the cusped object carries **no net chirality**
on any representation tested, including the non-self-dual ones B1260 pointed at (§3). **The
programme's ingredients assemble into exactly what the record says they assemble into — the form of
the Standard Model's gauge sector — and not into its contents.** What separates the two is not
unassembled material; it is a short list of constructions the record itself marks UNEARNED or absent,
restated in §5.

---

## 1. What this seat did

| step | instrument | outcome |
|---|---|---|
| read the whole history | `git log --reverse`, all 2864 commits, plus every governing document and ~45 load-bearing arcs | the arc of the programme is consistent: physics probes negative (June), the E₆ bridge and seam (late June), the measurement cascade (August), seven then ten value negatives, the generation-count line opened and closed this week |
| governance gates | `python3 scripts/gates/gates.py` at `86576d2c` | **30 of 30 PASS** |
| the test suite, fast lane | `pytest tests/ -m "not slow"` | see §7 |
| independent recomputation | `scripts/external_verification/spine_recompute.py` — own code, no repository imports | **18 of 18 PASS** (§2) |
| twisted cohomology of m004 | `scripts/external_verification/fox_symn_and_lemma.py`, exact over two primes | the Menal-Ferrer–Porti law reproduced; the net-chirality lemma verified (§3) |
| the deciding computation of B1260 | `scripts/external_verification/nonselfdual_w1w2.py`, `nonselfdual_psl27_extension.py` | **h¹(V) = h¹(V\*) on every non-self-dual representation tested** (§3) |
| the absence rule | `scripts/checks/absence_sweep.py` on eight terms across all ten heads; `scripts/checks/already_banked.py` on six questions | every term PRESENT; every hit read and classified (§6) |

---

## 2. The spine, recomputed

All of the following were computed from scratch (sympy/mpmath/numpy), not by running the repository's
scripts. Each agrees with the banked statement.

| claim | where banked | this seat's computation | result |
|---|---|---|---|
| `A = LR = [[2,1],[1,1]]`, trace 3, eigenvalues φ^{±2}, `A = F²`, Möbius fixed points φ, −1/φ | P1, P2, P15 (`CLAIMS.md`) | exact sympy | agrees |
| the Riley representation of 4₁ has `u² − u + 1 = 0`, u = 1+ω; trace field ℚ(√−3) | `frontier/B266_arithmetic_selects_e6/FINDINGS.md` | solved the two-bridge relation `a·w = w·b`, `w = b a⁻¹ b⁻¹ a`, symbolically | agrees (the polynomial is `u²−u+1`, as B266 states; a first draft of this check wrote `u²+u+1` and was corrected) |
| the longitude commutes with the meridian and translates by 2√3·i (cusp shape 2√−3); its SL(2) lift has trace −2 | B1086, B1112 | word search over the centraliser of the meridian; λ = `bABaaBAb` | agrees |
| reduction mod (1−ω): the image of π₁(4₁) is SL(2,F₃) = 2T, order 24 | B266 | group closure over F₃ | agrees |
| McKay graph of 2T = affine E₆ (marks 1,1,1,2,2,2,3; Perron eigenvalue 2) | B266, B727 | 2T built as the 24 Hurwitz units, character table computed, McKay matrix from characters | agrees |
| Vol(m004) = (3√3/2)·L(χ₋₃,2) = 9√3·ζ_K(2)/π² | I-3 (`docs/IDENTIFICATION_LEDGER.md`), B680 | volume from the Clausen function (two regular ideal tetrahedra) against the L-value from trigamma | agree to 30 digits; both equal 2.0298832128193072 |
| `sin²θ_W = 3/8` | B919 and its addendum | `Tr T₃² / Tr Y²` on 5̄, 10, 16, 5̄+10, 27 | 3/8 on every one — **non-discriminating**, exactly as the B919 addendum says |
| the global form kernel is ℤ₆ | B862 | direct count of the centre elements acting trivially on one generation | ℤ₆ |
| hypercharge is the unique gaugeable U(1) | B864 | linear anomaly conditions on `aY + bχ + cψ` | **with 15 Weyl fermions**: b = c = 0 forced. **With the 16 (ν^c present)**: χ is anomaly-free too and the gaugeable space is two-dimensional. B864's uniqueness is a statement about the 15-fermion generation; B1096's "every channel vanishes on the derived 16" is the same fact from the other side. Both are textbook anomaly theory, as B1160 itself states |
| every Sym^n of SL(2) is self-dual (E65) | `docs/ERROR_LEDGER.md` E65; B1260 §3 | the space of invariant bilinear forms is one-dimensional for n = 1..8 | agrees |
| E₈ ⊃ E₆ × SU(3): 248 = 78 + 8 + 27·3 + 27·3 | B1138 | dimension bookkeeping only | agrees |

**Two things this table does not say.** It does not say that these results are novel — the record's
own novelty ledger (`docs/NOVELTY_SWEEP_LEDGER.md`) and the paper draft (`papers/P3_THE_PAPER/main.tex`)
already classify them as reproductions of standard mathematics with one class-level entry point. And it
does not say the heavy structural computations were re-derived here: the Chevalley e₆ build, the
20-orbit census of B1098, the fork ladder of B1138 and the crossing data of B915 were read for internal
consistency and found consistent with standard Lie theory, not recomputed.

---

## 3. The one computation this seat ran that the record had not: net chirality on the cusped object

### 3.1 The question

`docs/MAIN_GOAL.md` JOIN 1, question 1 asks whether the generation count should be read on the closed
double D_t, where B1086 finds `h¹(27) = h¹(27̄)`, or on the cusped manifold, where Poincaré duality does
not obviously force pairing. B1260 (banked on `main` today) proved the closed wall general, walled the
abelian sector by Alexander reciprocity, reduced the question to rank ≥ 3 representations not factoring
through SL(2), located the only such branches the corpus has realised — B71's non-self-dual SL(3)
components W1 and W2 — and **named the deciding computation without running it**: compute `h¹(V)`
and `h¹(V*)` there and compare.

### 3.2 A lemma that says where net chirality can come from at all

Let M be the knot complement (compact, orientable, one torus boundary ∂M) and V any finite-dimensional
representation of π₁(M) with `H⁰(M;V) = H⁰(M;V*) = 0`. Write `res_V : H¹(M;V) → H¹(∂M;V)` for
restriction to the cusp. Then

> **N(V) := h¹(M;V) − h¹(M;V\*) = rank(res_V) − h⁰(∂M;V).**

*Proof.* χ(M;V) = 0 and H³(M;V) = 0 give h¹(V) = h²(V); Lefschetz duality gives h²(M;V) = h¹(M,∂M;V\*).
The long exact sequence of the pair with coefficients V\* gives h¹(M,∂M;V\*) = h⁰(∂M;V\*) + h¹(M;V\*) −
rank(res_{V\*}), hence N(V) = h⁰(∂M;V\*) − rank(res_{V\*}); exchanging V and V\* gives the displayed form.
∎ (Elementary; recorded because it converts the JOIN-1 question into a statement about the cusp.)

Three consequences, each checked below:

- **Self-dual V** (every representation factoring through SL(2), so every Sym^n and every 27 restricted
  along the principal or any other sl₂): N = 0 trivially. This is E65 in cohomological form.
- **Conjugate-self-dual V** (V\* ≅ V̄, i.e. an invariant Hermitian form of any signature): N = 0,
  because h¹(V̄) = h¹(V). Any holonomy landing in a real form of E₆ whose 27 carries a Hermitian form —
  E₆(2), E₆(−14), E₆(−78) — therefore has N = 0 outright. Only the real forms with a *real* 27, E₆(6)
  and **E₆(−26)**, and genuinely complex images escape this argument; and even there **N ≠ 0 requires the
  cusp holonomy to have fixed vectors** (else h¹(∂M;V) = 0 and both terms vanish).
- **Where a difference could live:** a non-self-dual V with cusp-fixed vectors and an *unbalanced*
  restriction rank. The computations below probe exactly that locus.

### 3.3 Instances computed

Presentation and conventions: the two-bridge presentation `⟨a,b | a w = w b⟩`, `w = b a⁻¹ b⁻¹ a`, meridian
a, longitude `bABaaBAb`; for the SL(3) components the mapping-torus presentation `⟨a,b,t | t a t⁻¹ =
a²b, t b t⁻¹ = ab⟩` with meridian `a⁻¹t` and longitude `[a,b]` (B71's conventions). Fox calculus, left
module, `d¹∘d⁰ = 0` checked to machine precision in every instance; ranks exact over F_p for the Sym^n
table, by singular-value gap otherwise. In **every row** the lemma held as an identity between
independently computed quantities.

| representation | non-self-dual? | cusp-fixed vectors? | h¹(V) | h¹(V\*) | N |
|---|---|---|---|---|---|
| Sym^n of the geometric rep, n = 0..16, two primes | no | n even: yes | 1 (n even), 0 (n odd) | same | 0 |
| 27 along the principal sl₂ (Sym¹⁶⊕Sym⁸⊕Sym⁰) and along the subregular (Sym¹²⊕Sym⁸⊕Sym⁴) | no | yes | 3 and 3 | 3 and 3 | 0 |
| PSL(2,7), 3-dim irreducibles, all 12 homomorphism classes (6 surjective) | **yes** (the two 3's are dual) | yes when the meridian has order 4 (eigenvalue 1); no when order 7 | 1 / 0 | 1 / 0 | 0 |
| non-semisimple extension `0 → ρ_geom → V → χ_t → 0` at both twisted-Alexander roots `t = 2 ∓ √3` | **yes** | no (the lift has tr λ = −2) | 0 | 0 | 0 |
| B71's W1, W2 at nine generic points | **yes** | no | 0 | 0 | 0 |
| **W1 and W2 on the locus where the cusp holonomy has a fixed vector** (six points, three central twists ζ of the monodromy each) | **yes** | **yes**, at exactly one twist per point | **1** at that twist, 0 otherwise | **same** | **0** |

The mapping-torus pipeline was validated first on the geometric fibre holonomy (the Anosov fixed
character (z̄, z, z), z = (3+√−3)/2): Sym² gives h¹ = 1 with h⁰(∂M) = 1 and restriction rank 1; Sym¹ gives
0; the ζ-twisted extension gives 0 — the Menal-Ferrer–Porti values.

### 3.4 What this settles and what it does not

**B1260's deciding computation lands on its second branch.** On the only rank-3, non-SL(2) components the
corpus has realised, and on the locus where a difference could have appeared, the cusped manifold pairs
27 with 27̄ exactly as the closed double does. The wall extends past closedness and past the abelian
sector; the generation count cannot be a net-chirality count on this manifold on any representation
tested. Not settled: a theorem that N vanishes for *every* representation of the knot group (the
instances suggest `rank(res_V) = h⁰(∂M;V)` holds generally — a "half lives, half dies" statement beyond
the self-dual case — but this seat has not proved it and does not claim it).

**And even a nonzero N would not have delivered generations.** `docs/IDENTIFICATION_LEDGER.md` row I-26
(registered today) says the reading "a twisted-cohomology dimension of a real 3-manifold = the number of
4d chiral generations" has never been exhibited: the index theorems that count generations live on a
Calabi–Yau 3-fold or a G₂ 7-manifold. Nothing in §3 pays I-26; it only shows that the quantity I-26 would
have read is identically balanced.

---

## 4. The assembly, laid against the Standard Model's specification

`docs/SM_SPECIFICATION_LEDGER.md` §A lists what a complete picture must supply. Here is each row against
what the corpus holds, with the mechanism and this seat's check. Grades: **REPRODUCED** (follows from
the E₆ input by standard group theory, discriminates nothing about the object), **CLASS-FORCED** (forced
by the trace field ℚ(√−3), a commensurability-class invariant), **EXHIBITED** (present as a possibility,
not forced), **ABSENT** (no construction in the corpus; established by sweep, §6), **CLOSED-NEGATIVE**
(tested and failed under seal).

| SM requirement | what the corpus holds | grade | anchor arcs | this seat |
|---|---|---|---|---|
| the gauge algebra su(3)⊕su(2)⊕u(1) | the cascade lands on su(3)⊕su(2)⊕u(1)³ (rank 6); the SM's is rank 4; the extra u(1)'s are the GUT's ψ and χ ≅ B−L | REPRODUCED; **rank obstruction is a theorem** | B892, B952, B992 | centraliser-of-semisimple argument is standard; agrees |
| the global form [SU(3)×SU(2)×U(1)]/ℤ₆ | inherited from embedding in a simply-connected GUT group; B1221: path-independent "and that is exactly why it is not new" | REPRODUCED | B862, B1221 | ℤ₆ kernel recomputed |
| hypercharge direction | anomaly cancellation on a 15-fermion generation | REPRODUCED (textbook; B1160 says so) | B864, B1160, B991 | recomputed; with ν^c the direction is not unique |
| hypercharge normalisation | homogeneous equations fix a direction, never a scale | **not derivable in principle** | B991 | agrees |
| `sin²θ_W = 3/8` | GUT normalisation, identical for every SU(5)-compatible content | REPRODUCED; the run to M_Z misses at 16σ (α_s-dominated) | B919, B915 | 3/8 recomputed on five reps |
| **three generations** | one 27 holds one 16 (multiplicity one; three copies need dim ≥ 48); no hyperbolic knot has a C₃ trace field; the h¹ = 3 is three inequivalent sl₂-blocks; the E₈ (27,3) is a possibility-space exhibit; every three-ness tested this week died (I-24 REFUTED, E64, E65, I-26 UNEARNED) | **ABSENT as a derivation**; EXHIBITED in E₈ only | B307, B685, B1033, B1138, B1253, B1255, B1256, B1257, B1259, B1260 | §3 adds: net chirality is zero on the cusped object too |
| chirality | constructible by a θ-odd twist of the double (closure full E₆(ℂ)) but **vector-like in count** on every closed assembly; observer-supplied by the record's own reading | CLOSED-NEGATIVE at count level | B582, B576, B1086, B1087, B1259 | §3 |
| the Higgs doublet and its potential | the doublet's *slot* (10 ⊂ 27) is identified; no adjoint VEV can mass a 27 fermion; the VEV direction is "an input in every framework and canonical nowhere"; the ℙ³ Higgs line is "one condition short" | slot EXHIBITED; **potential and VEV ABSENT** | B884, B978, B962, B1206 | sweep §6: no potential anywhere |
| the 19 (26/28) parameters | ten sealed value negatives; no object period, natural form, coupling, coincidence or regulator is an SM ratio; the type law: outputs are a finite algebraic menu | **CLOSED-NEGATIVE** | B915, B925, B929, B1027, B1066, B1075, B1126, B1128–B1137, B1032 | sweep §6 |
| Yukawa couplings | the *support pattern* of the cubic is computed (11 coupled cells); a three-family texture exists in the E₈ possibility space; no value | pattern EXHIBITED; **values ABSENT** | B884, B1150, B1185 | sweep §6 |
| neutrino masses | GUT ledger row 8: "mechanism available" in SO(10)/E₆, **not addressed** | ABSENT | `docs/GUT_REQUIREMENTS_LEDGER.md` | sweep §6 |
| a 4d action / dynamics | the object's own 2+1 gravity action `S = −Vol·σ` is a fact about its hyperbolic geometry; the B6 field equation's kinetic term is declared a choice; B1157: no parameter-free dynamical law at the archimedean place; no Dirac operator, no propagator, no Ward identity | **ABSENT** | B6, B1088, B1157, B944 | sweep §6 |
| scale | Mostow rigidity fixes shape not size; CS = 0 deletes the quantised half of the action | **external by theorem** | B1012, B1226 | agrees |
| the physics identification itself | "structural analogue ≡ physical quantity", the listener map | **UNEARNED** (I-13) | `docs/IDENTIFICATION_LEDGER.md` | this is the row every physics reading rests on |

Two rows deserve emphasis because they are where an outside reader would look for the programme's
object-specific content. **E₆ itself** is forced only through the trace field ℚ(√−3): the surjection
onto 2T is shared by about one census manifold in three (B993), the sister m003 carries the same field
(B727), and B727's own verdict is that the E₆ recurrence is the ADE classification refracted through one
arithmetic fact. **The SM endpoint of the cascade** is forced by "registerability", which B994 identifies
with chirality and B713/B760 show the object does not supply; the record grades it REPRODUCED, and the
paper says "the content is forced by the anomaly conditions alone, in a computation containing no token
of the object".

---

## 5. Why the assembly stops where it does — the theorems, not the mood

Each line names a proved obstruction and where it is proved. None of them is "not yet tried".

1. **Rank.** Centralisers of semisimple elements contain a maximal torus; the measurement cascade
   cannot reduce rank 6 to rank 4 (B952). The non-abelian hatch reaches rank 4 (B1098) but its
   exact-hypercharge landing is not colour-commuting (B1102), and the class choice is a priced input.
2. **Self-duality.** Every representation factoring through SL(2) is self-dual, so 27 ≅ 27̄ along any
   sl₂ (E65; recomputed §2), and h¹(27) = h¹(27̄) on every closed 3-manifold (B1086, B1260 §1).
3. **The cusp does not escape.** N(V) = rank(res_V) − h⁰(∂M;V); zero on every representation tested,
   including the non-self-dual SL(3) components on their fixed-vector locus (§3).
4. **Multiplicity.** One 27 carries the 16 with multiplicity one (B1255); no hyperbolic knot has a
   cyclic-cubic trace field (B307); the E₈ triplet is not object-paid (B1138, B1150).
5. **Values.** Scale-torsor no-go (B666), value-invisibility (B936), the anomaly layer identically zero
   on the derived 16 (B1096), the type law (B1032), and ten sealed negatives: the object emits finite
   labels and relations, never a generic real. The paper's own Non-claims box states this.
6. **Normalisation.** Anomaly equations are homogeneous (B991); no additional structure of the kind the
   corpus has removes this.
7. **Dynamics.** Modular flow trivial (B721); no parameter-free law at the ∞-place (B1157); the kinetic
   term is a choice (B6).
8. **Identification.** The object cannot select within its own canonical class (B1225); the listener map
   (I-13) and the generation-count reading (I-26) are UNEARNED — observer inputs, not derivations.

**What would have to change for a parameter-free Standard Model.** Not assembly. Each of the following
is a construction the corpus does not contain, confirmed by sweep: (i) a compactification or index
theorem on a 6- or 7-dimensional carrier in which a cohomology of this object counts 4d chiral
generations (I-26); (ii) a mechanism producing three copies of the 16 rather than three sl₂-blocks of one
27; (iii) a scalar potential with a rank-reducing vacuum (B962's "input in every framework"); (iv) a
four-dimensional action with a Dirac operator; (v) an earned map from structural analogues to measured
quantities (I-13), which the type law says cannot land on a generic real. Items (iii)–(v) are the same
inputs every grand-unified construction imports; the corpus's honest distinction is that it prices them
rather than deriving them.

---

## 6. The absence rule, discharged

`WORKING_RULES.md` forbids writing "we do not have X" without a sweep. Sweeps run (all ten heads,
filenames and contents, deleted-in-history, working tree):

| term | verdict of `absence_sweep.py` | what the hits are |
|---|---|---|
| "Higgs potential" | PRESENT (3 files) | B962's prior-art scout of the VEV literature and a speculation file — a survey of what *other* frameworks input; no potential derived |
| "quartic coupling" | PRESENT (1 file) | a literature-panel report inside B927 |
| "Yukawa matrix" | PRESENT (3 heads, off-main) | the cloud seat's E₈ possibility-space texture (harvested as B1150) and a physics-seat evaluation digest; kinematic, "no bundle, no Dirac operator, no field, no value" |
| "seesaw" | PRESENT (5 files) | `docs/GUT_REQUIREMENTS_LEDGER.md` row 8 ("not addressed"), a novelty sweep, a literature gate |
| "proton decay" | PRESENT (16 files) | the GUT ledger row 5 ("not addressed"), logs, the hydrogen audit |
| "compactification" | PRESENT (24 files) | I-26's own row, `docs/MAIN_GOAL.md`, B1025's input audit — the word appears where its absence as a construction is recorded |

`already_banked.py` on the six questions ("three generations derived forced", "Higgs potential quartic",
"Yukawa value mass ratio derived", "neutrino mass seesaw", "Dirac operator action 4d", "coupling constant
value alpha derived") returns the arcs already cited in §4: B1138 (exhibited, fenced), B1252 (one
generation), B1253 (refuted), B968, B962, B1028, B1162 ("withholds the values"), B1076 (NEGATIVE), B1150
(possibility space), B950/B952 (ledger rows), B1141/B1145 ("thesis-level, not a theorem"), B1128 (null),
B1131 (no bridge). **Every item in §5's list is therefore present in the corpus as a recorded absence,
a fence, or an exhibit — and in no case as a derivation.**

---

## 7. Suite, gates, and one observation about the certification envelope

- Gates: 30 of 30 PASS at `86576d2c` before any change by this seat.
- Fast lane: `pytest tests/ -m "not slow"` on a fresh clone (Python 3.11.15, numpy 2.4.6, scipy 1.17.1, sympy 1.14.0, mpmath 1.3.0, SnapPy 3.3.2 — not the pinned pyenv 3.12.1 / numpy 2.4.0 bench): **6074 passed, 8 failed, 53 skipped, 9 deselected in 1 h 02 min**, at `86576d2c`. The eight, triaged from their tracebacks:
  - five are fresh-clone artefacts of the class B1240 named — a lock reading a bench-local, untracked file (`tests/test_b1062_bridge.py`, `tests/test_b1063_refresh.py`, `tests/test_b1137_regulator_probe.py`, `tests/test_b646_wave2.py`) or a relay file on another seat's branch (`tests/test_b1035_receipts.py`);
  - two look like environment drift and deserve a look on the pinned bench: `tests/test_b565_realform.py` (the SL(2,ℂ) lift SnapPy returns for the meridian has the opposite sign, trace `1+√3·i` where the lock expects `−1−√3·i` — the E5 class in `REPRODUCIBILITY.md`), and `tests/test_b616_heldout.py` (a pinned results string not reproduced);
  - one is numerical and unexplained here: `tests/test_b511_d5.py` (`assert 0.0 > 0.8`, preceded by a divide-by-zero warning in `frontier/B511_physics_verdict/d3_wild_access.py`).
  None of the eight touches a claim this document leans on.
- **Observation (E46 species).** During the fast-lane run the working tree acquired one modification:
  `frontier/B1242_l199_two_earning_computations/verification/l199.json` was rewritten with
  floating-point-noise differences in its cusp-shape fields, because
  `tests/test_b1242_l199_two_earning_computations.py` executes the arc's verification script, which
  writes its own JSON back into the tree. The file was restored, not committed. This is the class
  `WORKING_RULES.md` §CE already names (a certifying run mutating the tree it certifies); a lock that
  regenerates a tracked artefact should write to a temporary location and compare.
- This seat's additions are confined to `docs/EXTERNAL_VERIFICATION_2026-09-06.md` and
  `scripts/external_verification/`; no ledger, log or arc was edited, and banking (an arc number, the
  kill graph, `PROGRESS_LOG.md`/`CHANGELOG.md`) is left to the owner's seat under its own protocol.

---

## 8. Limits of this verification

Read in full: the governing documents, the identification, SM, GUT, input and theorem ledgers, the paper
draft, and the FINDINGS of the arcs cited above. Recomputed: §2 and §3. Read for consistency only: the
Chevalley-basis constructions (B854/B883/B1102), the fork ladder (B1138), the 64-decomposition (B1140),
the sl₂-orbit census (B1098), the sealed value crossings (B915 and successors). Not run: the slow lane
(`OA_SLOW=1`), anything needing Sage. This seat found no error in a banked mathematical statement it
checked; it found the record's summaries occasionally stronger in tone than their arcs (the same species
the record's own E53 class tracks), never in substance.
