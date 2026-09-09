# THE CHAIN — the forced core as an axiom→theorem ledger (B758)

*The P019 discipline (cc3's genesis plan, owner-approved 2026-07-22) applied program-wide:
every link is labeled — **[THEOREM]** (symbolic/exact or computer-assisted-finite proof),
**[CENSUS]** (bounded enumeration, bound in the statement), **[IDENTITY]** (computed exact
equality), **[NO-GO]** (dissolution/obstruction with its discriminating computation banked),
or **[AXIOM]** (a declared choice — PRICED when its forks are computed, UNPRICED-flagged
otherwise), or **[COROLLARY]** (an immediate consequence of an earlier link plus a
definition — carries NO independent computed content and must name the link its content
is inherited from; added 2026-07-24 by the B784 audit, which found C22 had been minted as
a computed [NO-GO] when its computation could not fail). Admission per the sealed prereg fd934b27: exact statement + banked computation
location + green lock. **The going-forward rule: every new banked positive either enters
this chain under one of the five labels or is explicitly a hint/open door — nothing in
between.** This document is a VIEW of the bank; it asserts nothing new. **Every link's lock is cited as a resolvable `tests/...py` path and is gate-checked (`chain-locks`)** — a 2026-07-29 review found four [THEOREM] links citing their locks only in prose ('the B730 locks'), which no gate could verify and no reader could run. Gate 5: no physics
statement appears below; SM-facing content enters only as NO-GO links.*

---

## Part I — the genesis (P019's chain, priced by B749)

> **THE GENESIS HAS A SECOND, STRONGER ROUTE, AND THIS CHAIN DID NOT CITE IT UNTIL B1243
> (2026-09-03).** `docs/UNIQUENESS_THEOREM.md` — banked 2026-05-28, nine days into the repo,
> lock `tests/test_uniqueness_theorem.py` (9 green) — proves **A1–A7 ⟹ A = LR = [[2,1],[1,1]]
> ⟹ P1–P16**: seven individually-motivated axioms of a *minimal record-transfer system*
> (ℤ² substrate; reversible integer transfer; det = +1; a primitive one-channel update forcing
> exactly the shears L and R; torsion-free closure; minimality) **force the monodromy** —
> trace 3, eigenvalues φ², φ⁻² — machine-checked 144 → 1, with **A7 the single irreducible
> bit** (the order convention LR vs RL), which is exactly what selects the golden polynomial.
>
> **Its own §6 limit, kept verbatim in force:** it does **not** derive A1–A7 from anything
> weaker — attempts to derive even L, R from a count-substrate STALLED, and "the substrate,
> positivity, primitivity, and order remained inserted." `paths/PATHS.md`'s 25-path survey of
> mechanisms stands at **4 STALLED, 1 DEAD, 17 UNTOUCHED**, so this is *not*
> selection-by-elimination.
>
> **Not independent of C1–C6:** A1's ℤ² *is* the punctured torus's H₁, so the geometric
> content enters early rather than not at all. State it as **agreement between two
> axiomatizations**, never as two independent derivations.
>
> Pinned by `docs/CHAIN_COVERAGE.json`: dropping this citation reds the suite.

**C1 [THEOREM — Morse–Hedlund].** Every aperiodic sequence has factor complexity
p(n) ≥ n+1; Sturmian words achieve equality. — P019 T3; control fork B749/F7 (with the
quadratic≠metallic erratum sealed in-arc). Lock: `tests/test_b749_genesis_forks.py`.

**C2 [THEOREM — the self-selection, one criterion].** Hurwitz extremality at the golden
slope IS the all-1s continued fraction (the bottom of the Lagrange spectrum): the
minimal-description principle applied to its own parameter has a unique fixed point.
— P019 T4 (v2, the unified form). Lock: `tests/test_b749_genesis_forks.py` — **CORRECTED 2026-08-09 (B998): that file tests F4, F5, F6, F7 only. There is NO F3 test.** The F7 control is present; **F3 is a citation to a test that does not exist.** *(stamp 2026-08-19: still CURRENT as of B1082 — the stale-absence sweep verified this absence/openness against the full corpus.)*

> *Addendum 2026-09-09 (B1323, DESIGN sealed `3e8282a2`).* **(1) The lock sentence above is stale (E53 instance #29):** `tests/test_b1003_f2_f8_locks.py` (B1003, 2026-08-30) asserts all seven fork verdicts including F3's; F3's computation and verdict (ROBUST — silver = m136, arithmetic over ℚ(i), every banked face ABSENT) have been locked since then. **(2) C2 is two links wearing one label, and is now read as such:** *C2a [THEOREM — self-similarity]* a Sturmian word fixed by a substitution has a quadratic slope (B749/F7a; Lagrange); *C2b [CRITERION — minimality]* among the self-similar slopes, minimality selects φ — and C2b is where the price lives: F3's silver is a real arithmetic world that this criterion discards. **(3) The criterion census (`frontier/B1323_the_genesis_upgrades/verification/u2_criterion_census.py`, PASS):** seven formalisations of "the parameter minimally describes itself" agree on φ with a unique minimiser — K1 the Lagrange value (min √5, uniquely at [1;1,…]; the second value 2√2 at the silver), K2 the least constant partial quotient, K3 the first hyperbolic trace 3 with class number h⁺(5) = 1 (one class, [[2,1],[1,1]]), K4 the torsion-free first mixed closure ((1,1) alone on the 12 × 12 grid), K5 the Markov tree's root (1,1,1) ↔ the Fricke triple (3,3,3), K6 the smallest real quadratic discriminant 5, K7 the smallest quadratic Pisot number x² − x − 1 — **and one natural criterion does not: K8, the smallest Pisot number of any degree, is the plastic number ρ = 1.3247… (x³ − x − 1; Siegel 1944), below φ.** So "one criterion, one fixed point" is true of the seven and false of the eighth: C2b's criterion is invariant across the self-application formalisations and is NOT the same as "minimal algebraic growth". Lock: `tests/test_b1323_the_genesis_upgrades.py`.*

**C3 [AXIOM — being is inexhaustible description; PRICED].** The one deep metaphysical
commitment (P019's A0+A2 under the honest recount). Price computed: the periodic sibling
degenerates (B749/F2 ROBUST); the shadow-rule variants degenerate or conjugate away
(B749/F4 ROBUST). — `frontier/B749_genesis_forks/`. Lock: `tests/test_b749_genesis_forks.py`.

**C4 [AXIOM — the geometric carrier; PRICED].** The word is realized on the once-punctured
torus. Price computed (B749/F8, GEOMETRY-NECESSARY): the word's non-geometric canonical
carriers (the tiling hull; the Effros–Shen algebra, K₀ = ℤ[φ]) see ONLY the hearing —
x²+3 stays irreducible over ℚ(√5) (all four redundancy witnesses failed exactly);
**ℚ(√−3) is bought at geometrization and nowhere earlier.** Lock: same file.

> *Addendum 2026-09-09 (B1323): THE DICTIONARY LEMMA between this chain and `docs/UNIQUENESS_THEOREM.md`'s A1–A6 is machine-checked (`verification/u3_dictionary.py`, PASS): the Sturmian morphisms' incidence matrices are exactly the non-negative GL(2,ℤ) matrices = the monoid ⟨L, R, P⟩ (3 280 morphisms of St to length 7 → 87 matrices, every one a product of the two shears and the swap; conversely all 462 non-negative GL(2,ℤ) matrices with entries ≤ 13 are realised by an explicit morphism) — **C1 ↔ A2 + A4**; the Fibonacci morphism has matrix L·P (det −1, A2 without A3), and orientation (C5 ≡ A3) forces the square (LP)² = LR = A while (PL)² = RL — **A7 is the placement of the swap inside the single tick**, the double tick of B1083; the carrier's H₁ = ℤ² and the a·B bundle is m004 — **C4 ↔ A1**, the one non-trivial identification; and from A = LR the cutting sequence of its expanding eigenline (slope 1/φ = [0; 1, 1, 1, …]) is the Fibonacci word letter for letter (600 letters) — A1–A6 return C1–C2's word. The two axiomatisations are one construction in two presentations (registry row T-GENESIS-DICTIONARY). Fork F9 (the substrate count, A1's "not one, not three") is priced in the same arc — see B749's fork table addendum.*

**C5 [AXIOM — orientation; PRICED, the most expensive].** The monodromy is taken
orientation-preserving (golden SQUARED). Price computed (B749/F5 FRAGILE): the discarded
det −1 sibling IS the Gieseking manifold — m004's own orientation double cover parent
(dilatation φ upstairs, φ² down; dual sealed routes + cc's third isometry route).
**Orientation = choosing the child of the parent.** Lock: same file.

**C6 [THEOREM — Thurston/Riley; banked realization].** The mapping torus of the
once-punctured torus under [[2,1],[1,1]] is the figure-eight knot complement: unique
hyperbolic structure, trace field ℚ(√−3), THE arithmetic knot. — B285 (exact Riley rep,
u² + u + 1 = 0); B282. Lock: `tests/test_b285_commutator_phase.py`.

## Part II — the object's forced structure

**C7 [THEOREM — the forced faces].** The object's intrinsic arithmetic forces exactly
three quadratic faces = one Klein-four V₄: being ℚ(√−3) · hearing ℚ(√5) · meeting
ℚ(√−15) (fund. disc −15). — B730 (two-seat). Lock: `tests/test_b730_faces_cosmos.py`.

**C8 [CENSUS — the interface-only V₄].** No closed hyperbolic filling of m004 in the
|p|,q ≤ 8 grid (78 hyperbolic slopes) has an invariant trace field containing √−3, √5,
OR √−15 — the entire forced V₄ is a property of the OPEN object (census fact, not an
all-slopes theorem). — B288/B740 (two-seat, two-method) + B747 + B748 (with the per-slope
√−3 consistency re-derivation 24/24). Lock: `tests/test_b747_b748_sweeps.py`.

**C9 [THEOREM — congruence, conventions named per E23].** m004 IS congruence: standard
SL-kernel level (4); mod-center/PSL filtration realizes the geometric index 12 at (8);
the sisters at (2). — B734 (correcting B731; two-seat). Lock: `tests/test_b734_m004_congruence.py`.

**C10 [THEOREM — character-rigidity + the voice].** The continuous spectrum is ONE
channel — the pullback Eisenstein series, φ(s) = Λ_K(s−1)/Λ_K(s) exactly, with NO
conductor character anywhere in the continuous part; Res φ = 2√3/vol(m004)
(covering-invariant). — B739 + B737. Locks: `tests/test_b737_candidate_zero.py`, `tests/test_b739_rigidity.py`.

**C11 [IDENTITY — the two-column law].** Ten of twelve structural floors carry a FORCED
golden appearance; the emission channel carries none (the voice is pure being-field):
golden is the dynamical/hearing column, Eisenstein the geometric/being column — extended
to the origin by C4/C5 (the gait is combinatorial-dynamical and survives closure; the
name is geometric and does not). — B746 (sealed 12-floor remap) + B749/F6 (the hearing
survives Sol closure) + C8. Locks: `tests/test_b746_golden_ledger.py`.

**C12 [THEOREM — the chord].** The trace map is θ-equivariant; at the fixed line the
Jacobian splits exactly into sum/difference sectors with spectra split by golden-power
parity (the chord carries the ODD powers, dominant φ³ at SL(3); sector assignment proven
across the tower). — B48/B54/B64; recomputed 2026-07-21. Locks: the B64/B48-family locks
+ `tests/test_b745_revivals.py` (the SL(3) anchor).

**C13 [IDENTITY — the mixing structure].** The weld's θ-odd block at g = RL is exactly
unitary with eigenphases ±72°; the overlap matrix between the forced weight basis and the
weld eigenbasis is unistochastic and golden-exact, P = [[φ/√5, 1/(φ√5)], [1/(φ√5), φ/√5]],
with |B₀₀|² = 1 − p = 1/(φ√5) exactly; twist-invariant as a matrix (the B592 sign-flip
swaps eigenphase labels, p ↦ 1−p). — B753 (+ addenda). Lock: `tests/test_b753_mixing.py`.

**C14 [IDENTITY — the pure-3 symmetrized series].** The GSWZ symmetrized product for 4₁,
computed FROM the Kashaev sum (r₁…r₅ PSLQ-recognized under E25; out-of-sample scaling law
verified at 0.2%), reproduces eq (2) exactly and has pure-3 denominators through u⁵ —
while the Φ-level coefficients themselves are NOT pure-3. — B755 cell 3. Lock:
`tests/test_b755_carried.py`.

**C15 [THEOREM — the hearing multiplication law].** For the mod-5 generating function:
a_m·a_n = a_mn (gcd(mn,5)=1) ⟺ χ₂(m)=+1 or χ₂(n)=+1, with exact defect (1−√5)/2 in the
both-nonresidue case; the additive Dirichlet form is final. — B756/DOOR3 (cc2 + cc
independent proof from the banked B666 form). Lock: `tests/test_b756_doors.py`.

## Part III — the no-go chain (the lack, classified)

**C16 [NO-GO — the threefold refusal].** Every banked refusal-to-close falls into exactly
three classes, X empty: NO POINT (×8: the torsor lack — the object provides the group,
never the choice), NO WIDTH (×3: Mostow; one channel; being-only content), NO NAME (×2:
the census triple; the gap as objectivity's edge — the gait transmits, the name does not).
— B750 (sealed enum + can-fail witnesses). Lock: `tests/test_b750_lack_ledger.py`.

**C17 [NO-GO — the SM record].** The no-SM-value wall stands with a four-mechanism
spectral column (B754: 17 KILL-EXTENDS, 0 FACE-OPENS); zero of 24 SM parameters reduced
(banked — the A+B+C campaign, frontier/B736_ABC_campaign/, lock `tests/test_b736_abc.py`); the two live-fire claims adjudicated NOT EARNED / DISSOLVED (B751: the α_s
composite — three insertions + null base-rate; B752: Op-3 — universal collapse, wrong
input, repelling point); the two-ℤ/3 identity DISSOLVED (B757: Sylow-forced coincidence);
the B699 general gloss REFUTED (B756: six counterexamples, reading-dependence stated).
Locks: `tests/test_b754_p2_spectral.py`, `tests/test_b751_adjudication.py`,
`tests/test_b752_receipt.py`, `tests/test_b757_two_z3.py`, `tests/test_b756_doors.py`.
The ONE registered forward item is a HINT, not a chain link (the pin: 0.30902; H-TUROK
wording; owner+L91 gate for any change).

## Part IV — the open frontier (declared, not blurred)

**C18 [AXIOM — the observer's closings; FIRST SUB-STRUCTURE PRICED 2026-07-22].**
Chirality, values, time, and the spatial manifold are the observer's closings of the
object's incompletenesses (B713–B716 as the banked reading; the closings themselves are
the choices). The reflexive sub-axiom A7 (P020: the voice read as self-report — a choice;
the mathematics stands without it) is priced by four computed forks (B759–B762):
- **QP-3 INTEGRATED** — the chord/sum voices couple at SL(3), and the coupling obeys C19;
- **QP-4 NO-HATCH** — no object-native operation signs the chord ({ζ₅, ζ₅⁴} inseparable;
  five operations fail) — the c-into-θ crux tested at its sharpest point yet and HELD;
- **QP-2 FLAT** — zero private states at n = 2, 3, 4 (the boundary description is
  complete: no hidden variables behind the interface);
- **QP-1 QUINE** — the emitted spectral word identifies m004 uniquely among 203,123
  census manifolds (the sister separated by cusp shape).
Composite: the object is a fully transparent, self-naming, integrated speaker that cannot
choose — the observer's contribution reduces to EXACTLY the choice. The remaining unpriced
frontier: the choice-mechanics of the coupling itself (the measurement torsor; the
arithmetic-CS home), plus the c-into-θ crux's remaining routes. Locks:
`tests/test_qp3_integration.py`, `tests/test_qp4_closure.py`, `tests/test_qp2_private.py`,
`tests/test_qp1_self_naming.py`.

**C19 [IDENTITY — the pair-separation law of integration; SCOPE-CORRECTED same-day
(B764)].** The single-trace θ-off-block norm at the geometric representation equals
**|u_geo − ū_geo|** — the geometric Riley pair's separation. For an imaginary-QUADRATIC
Riley field this equals √|disc K| identically (the quadratic-formula identity — m004's √3
is this THEOREM's instance; SL(2) dissociated, SL(3) = Sym² integrated; the commutator
purely chord-directed, 4i√3). B759's original √|disc K| form is NOT general: 5₂ (cubic,
disc −23) gives 2.6143 = the pair separation, not √23 — the discriminant factors as
(u−ū)²·∏[(u−rᵢ)(ū−rᵢ)]², and the off-block is the first factor only (verified to 40
digits). — B759 + B764. Locks: `tests/test_qp3_integration.py`, `tests/test_b764_c19.py`.

**C20 [IDENTITY — the measurement-torsor rank; R29-5, owner-opened].** The discrete
choice-space closing the object has 𝔽₂-rank EXACTLY 3 — the independent generators are
conjugation (c), reversal (θ), and the golden-Galois branch (γ₅); the being-Galois γ₃
acts identically to c on every closing axis. Two exact relations: **time's direction =
the basepoint bit** (both are the γ₅ choice: (1−φ)² = φ⁻² is the Galois action), and
**the chord's sign = c ⊕ θ**. The rank equals the banked observer-menu rank (B733) —
RANK-SATURATED: the menu is the full discrete closing set. The continuous residue
(anchor/values/space) stays Galois-chosen (K020), and the unmoved T1 axis is a named
door. — B766. **[STRENGTHENED 2026-07-25, R31-4 + cc3's convergent b766-scrutiny: the
rank-3 is now COMPUTED from c/θ/γ₅ each moving a distinct probe (was hardcoded flip-vectors);
the chord is corrected to a MATRIX-LEVEL observable (θ is trace-trivial ⇒ the Im tangent is
c-odd, not θ-odd — the chord is Sym²(AB)−Sym²(BA), invisible to tr); and θ=reversal
(trace-trivial at all ranks, matrix-level only) is distinguished from ι=inversion
(trace-active at genuine SL(3), cc3 N7 gated) — on the object's self-dual (Sym²/V0) component
ι~θ so the rank-3 STANDS; the full SL(3) variety may carry ι as a 4th generator. **B786 pins
the character-variety third generator = ι (inversion), with θ (reversal) the matrix-level
chord; object rank 3 unconditional.**]** Locks: `tests/test_b766_torsor.py`,
`tests/test_b786_theta_iota.py`.

**C21 [THEOREM — the T1 structure].** The unmoved axis is DISCRETE: a 3-element torsor
(the V₄-frame choice) under an S₃ of which the banked object-native operations realize
only the identity — T1's fixedness under the closing set is FORCED (abelian inner
triviality), so any instrument moving it must realize an outer V₄-automorphism. There is
no continuous T1 modulus where the object lives (its invariant trace data): the candidate —
the relative position of the c- and θ-eigensplittings — does not exist there, because on the
Sym²(SL(2)) character variety the θ-involution (the 27↔27̄ contragredient g↦g⁻¹) acts
TRIVIALLY. In SL(2) tr(g⁻¹)=tr(g), so every θ-odd trace coordinate and its tangent vanish
IDENTICALLY (not merely at the geometric point): the geometric-point tangent
d/du[tr Sym²(AB)]|_ω = −5 + i√3 has θ-odd (contragredient) part exactly 0, and its imaginary
part is c-odd, not θ-odd. Only the c-eigensplitting exists on this module, so there is nothing
for a θ-frame to be positioned against — the candidate modulus is vacuous. (θ's non-triviality
is a matrix/representation-level fact, gauge from the invariant standpoint; chord = c⊕θ is the
banked torsor relation C20/B766, NOT a tangent-frame alignment derived here.) — B769
[mechanism corrected 2026-07-25: the earlier "tangent frames align → chord = c⊕θ" wording
conflated the c-odd imaginary direction with a θ-odd one — the same class as the B780/B784
c-vs-θ slip; the theorem, discrete T1 with no invariant continuous modulus, is unchanged].
Lock: `tests/test_b769_t1.py`.

**C22 [COROLLARY of C20 — no canonical closing].** Immediate from C20 and the definition
of torsor: the closing set is a (ℤ/2)³-torsor, and a torsor has no canonical point. **The
earned content is C20's rank-3 FAITHFULNESS**, not this restatement — note that the
abstract set {c, θ, γ₅, γ₃} does NOT act freely (γ₃·c is trivial); freeness holds exactly
after C20's quotient. Given that quotient, the action on the 8 closings is free, there is
no G-fixed closing, and no G-equivariant selection exists. **SCOPE (added 2026-09-03, B1244 — a terminology collision, resolved).** "Closing" here means the
**observer's closing set**, the (ℤ/2)³-torsor on {c, θ, γ₅, γ₃}. It does **not** mean a **Dehn filling
of the cusp**, and C22 does not contradict **C46/B287**, where the fiber slope (0,1) **is** a canonical
closing among the ten exceptional fillings. Two different objects carry the same word; neither
statement may be quoted without its object. **The freeness/no-fixed-point
step is DEFINITIONAL — the regular action of any group is free — and is not an independent
computation.** — B782 (corollary cell; its compute verifies a group-theoretic identity only
and cannot fail). Lock: `tests/test_b766_torsor.py` (the failable content);
`tests/test_b782_c22.py` is a tautology check, NOT a regression lock. *[BRIDGE, PRICED to
C18 and NOT asserted here: if every object-internal process is modelled as G-equivariant,
then no internal process selects a closing and the selection is symmetry-breaking rather
than computation. That premise is a modelling assumption, not a result of this arc.]*

**C23 [NO-GO — the T1-mover; closes the door C21 opened].** C21 established that T1's
fixedness is FORCED (abelian inner triviality) and therefore that any instrument moving
it must realize an OUTER V₄-automorphism. **That door is now closed:** the subgroup of
Out(V₄)=S₃ realized by the object's native operations is exactly **{identity}**. The
three closing legs carry DISTINCT conjugation-robust signatures under two invariants —
the orientation homomorphism (holo/antiholo) and the geometric-pair orbit type
(fix/swap {ρ_geo, ρ̄}): c=(antiholo,swap), j₂=c·θ=(holo,swap), τ=θ=(antiholo,fix) —
which leaves only the identity in S₃. **Scope stated honestly (per the arc's own verifier):
the universal spine is the orientation homomorphism I1 (which needs only that the operation
is holo/antiholo) PLUS the explicit fixed-point argument — c(ρ_geo)=ρ̄ is a free orbit
(ρ_geo is non-real, computed) while every object-native operation stabilizes {ρ_geo,ρ̄}.
The pair-orbit invariant I2 and that fixed-point argument SHARE the stabilization premise
and are NOT independent of each other; the enumerated object-native list (D4 via Mostow,
γ₅ field-disjoint, γ₃≡c, V₄ abelian) establishes membership in the holo/antiholo
pair-stabilizing class rather than adding a third argument.** Within that class the wall is
proven: **the T1 3-frame torsor choice is unbroken by any object-native operation; a mover
must lie outside the object's native symmetry group.** — B775 Wave 1 (P2-T1MOVER). Lock:
`tests/test_b783_c23.py`.

---

## Part V — the measurement cascade and the value layer (the B877–B919 window; same-PR catch-up 2026-08-06, B920)

*The window's theorems reached LAW_MAP §F but neither theorem register — the identical gap
the LAW SWEEP had just fixed in LAW_MAP, one register over (cc3 loss audit A5). These are
the catch-up links, brief; each mirrors its LAW_MAP §F row, which carries the full
statement. Gate 5 stands: every row is STRUCTURE (exact algebra on the object's own
charges); no physics value is claimed anywhere below.*

**C24 [THEOREM — the First Measurement].** The object's 2T-charges stratify e₆; three
Galois-conjugate first breakings (μ, constant 13³); z(line) = so(10)⊕u(1); the tiling with
the cyclic law (P69). — B877. Lock: `tests/test_b877_fmt_review.py`.

**C25 [THEOREM — the Second Measurement].** A second measurement of the object's own
charges lands on su(3)⊕su(2)⊕u(1)³ EXACTLY, skipping SU(5); the wall complex in the split
frame, at all three roots. — B892, B893. Locks: `tests/test_b892_smt.py`,
`tests/test_b893_omega.py`.
**SCOPE (B950, carried here 2026-09-03 by B1243 — the citation gate's first catch).** That
algebra is **14-dimensional**; the Standard Model's is **12**. It is the A₂+A₁ Levi — a
**centralizer**, not the SM gauge algebra — and B892's own banner says the phrase "take E₆ to
the Standard Model algebra" **overstates by two abelian factors**. Both extras are named
(B992: the u(1)³ is span(Y, χ, ψ)) and each has a fate: **ψ** is anomalous over any chiral
content, so ungaugeable — free; **χ ≅ B−L** is anomaly-FREE over the object's derived 16
(B1096, C45) and is removed instead by the second VEV ⟨ν^c⟩ (B1017), whose direction is itself
forced (B1092). So **14 → 13 is forced and free; 13 → 12 costs exactly that VEV.**

**C26 [THEOREM — the magic-square isomorphism].** The build IS M(𝕆,ℂ) by explicit
structure constants; 0/3003 mismatches, det φ = −2/3 (P70). — B904. Lock:
`tests/test_b904_bs.py`.

**C27 [THEOREM — the inter-breaking laws].** Vacuum-to-Higgs; the 16/vacuum exclusion —
exact minimal-polynomial theorems on the matter pencil. — B885, B886. Locks:
`tests/test_b885_interbreaking.py`, `tests/test_b886_matter_pencil.py`.

**C28 [THEOREM — the four-column concordance].** Measured ⟺ θ-odd exponents (4,8) ⟺
τ_m > 0 ⟺ split spectrum; unmeasured ⟺ (7,11) ⟺ compact; 7·11 = 77 the resolvent
(disc K = 6237 = 3⁴·7·11, one line from the reduced model x³−12x−5); the golden 5 enters
supp(disc μ) through the model ℤ[t]/μ, **not by ramification in K** — 5 ∤ disc K, 5
unramified in the whole S₃ closure, splitting shape [1,2] (the value primes' shape).
*(Clause corrected 2026-08-18 — audit-seat catch, bench-verified; formerly "5 by
ramification". See B894's addendum; E41.)* — B894, B898. Locks: `tests/test_b894_bridge.py`,
`tests/test_b898_census.py`, `tests/test_c28_ramification.py`.

**C29 [THEOREM — the signature dichotomy].** ad(x₈) ≡ ad(x₁₆): {0³⁰, 48 real};
ad(x₁₄) ≡ ad(x₂₂): {0¹², 66 imag}; zero generic-complex on C. — B898. Lock:
`tests/test_b898_census.py`.

**C30 [THEOREM — the sign-law mechanism].** All six torsion quotients exactly
anti-palindromic; sign(τ_m) = sign(lc)·(−1)^{p_m}; p_m ≡ m (mod 2) in every block. —
B903. Lock: `tests/test_b903_sign.py`.

**C31 [THEOREM — the diagonal cocycle].** All four Π-label cubics have a root in K (each
led by 13³); the Galois S₃ acts on both orbits by ONE root permutation. — B900. Lock:
`tests/test_b900_cocycle.py`.

**C32 [NO-GO — the C-stabilizer].** n(C) = z(C) = 12; no real C-stabilizing symmetry swaps
split/compact or x₈↔x₁₆ — the c-carrier must be complex. — B901. Lock:
`tests/test_b901_stab.py`.

**C33 [THEOREM — the annihilation].** [α_vac] = [α_μ]⁻¹: vacuum ⊕ charge = the split
algebra; certificates on the ζ₆-line. — B902. Lock: `tests/test_b902_kp.py`.

**C34 [THEOREM — the one-class + the numerator law + the observer's place].**
[α_μ] = [α_gen] = [α_κ] = [α_V] = C, vacuum = C⁻¹; each pencil's Kummer element wears its
own prime; den(V) = 𝔭₁(953)⁴ exactly. — B910, B918. Locks: `tests/test_b910_kappa.py`,
`tests/test_b918_v.py`.

**C35 [THEOREM — the sealed generation-shape].** G₂₀'s su(3)′ replicates fixed
color⊗su(2)′ types into flavor triplets; the lepton 3+6 split; Casimirs 4/9, 4/9, 3/8;
mechanism-hood fenced. — B897. Lock: `tests/test_b897_g20.py`.

**C36 [THEOREM — the unified ℤ₂ law + the atoms].** Matter gluing = gauge commutation =
mixed-texture type (8/8, 48/48, two-prime); 15 atoms, bijective tri-partition; the
colorless grid = two pencils of AG(2,3). — B906. Lock: `tests/test_b906_flavor.py`.

**C37 [THEOREM — the e₆(2) selection].** The wall is real exactly in e₆(2), via τ-twisted
alignments only; ε₈ε₁₆ = ε₁₄ε₂₂ = +1 for every C-stabilizing automorphism. — B907. Lock:
`tests/test_b907_selector.py`.

**C38 [THEOREM — the rational atoms + I = −1].** The four charges commute rationally on
the 27; rows = even transversals, cols = odd; P_R = −P_C exact. — B908. Lock:
`tests/test_b908_pin.py`.

**C39 [THEOREM — the signature split of matter].** The canonical H has signature
(15,12) = e₆(2)'s K-split; nine colorless atoms positive-definite with scales; all six
colored atoms Lorentzian. — B912. Lock: `tests/test_b912_norm.py`.

**C40 [THEOREM — the one-number table].** All six normalization-free colorless couplings
EXACTLY equal: T = σ₂(t_K), deg-3; the H-unit gauge = the determinant gauge. — B914.
Lock: `tests/test_b914_table.py`.

**C41 [THEOREM — the unimodularity + the twist-norm law + the product law].** λ = 1
exactly in the charge-equivariant gauge; ∏d_i = −(953/2304)² = N_{K/ℚ}(d);
v₁v₂v₃ = 3^{3/2}λ² exact; structure primes (13,17,19) inert, value primes split [1,2]. —
B916, B917. Locks: `tests/test_b916_bridge.py`, `tests/test_b917_value_arc.py`.

**C42 [IDENTITY — the 3/8 traces].** Tr(T₃²) = 3, Tr(Y²) = 5, Tr(T₃·Y) = 0 exactly
(one-prime tier, rational reconstruction; second prime open-diagnosed) ⟹ the
trace-orthogonality ratio 3/8 — structure, not a physics value (Gate 5). — B919. Lock:
`tests/test_b919_traces.py`. Witness from committed code (B1237, 2026-09-02): B919's runner needs an
uncommitted `cw.py`; the three integers recompute from B1236's committed multiplet content —
`frontier/B1237_physics_seat_r31_r38_harvest/verification/traces_from_b1236.py`, lock
`tests/test_b1237_physics_seat_harvest.py` (a different derivation of the same numbers, not a second prime).

**C43 [NO-GO — the crossing, sealed].** One input (α_em) + the object's boundary + pure
desert MISSES at 16σ, α_s-dominated; the failure triangle banked; the desert is dead as a
mechanism. — B915. Lock: `tests/test_b915_crossing.py`.
**AND THE MISS IS GROUP-INDEPENDENT — BY CONSTRUCTION (added 2026-09-03, B1245).** This is a fact
about the **desert configuration**, not about the object and not about E₆. B915's own
`crossing.py` settles it without a new run: `curve_point(MU)` takes **one physical argument, the
unification scale**. Its inputs are the **SM** one-loop betas (41/10, −19/6, −7), the SM two-loop
matrix, the GUT normalisation 5/3 — shared by SU(5) ⊂ SO(10) ⊂ E₆ under the standard embedding —
and the condition that the three couplings meet. **No group-specific quantity enters the executable
code at all** (the only "E₆" is in the docstring; the only "27" is the coefficient 27/10). So the
desert curve *cannot* depend on which simple group unifies: the control is not "run SU(5) and
SO(10) and compare", it is that **there is no group parameter to vary**. Earned on this bench from
our own sealed computation's dependency structure — **not** cited from the literature, per the
B1244 prereg's E-4. No new measured input: B915's seal already covers α_em(M_Z).

**C44 [NO-GO — the fork].** On e₆ the centralizer ladder is dim z(T1) = 16, z(T1+colour) = 8,
z(T1,T2) = 8, **z(T1,T2+colour) = 0**, slot-independent (two adjacent simple-pair choices
agree). The joint centralizer 0 is **THE FORK — any TWO of {spacetime, colour, hypercharge},
never three**: the closing is forked, E₆(−26) XOR E₆(−14), not one act. — B1138.
Lock: `tests/test_b1138_structural_completion.py`.
**THE OBSTRUCTION IS BORROMEAN, NOT PAIRWISE (added 2026-09-03, B1245).** Read the ladder: every
*pair* has room — z(T1) = 16, z(T1+colour) = 8, z(T1,T2) = 8 — and **only the triple vanishes**. So
this is irreducibly three-way, like Borromean rings: any two link fine, all three do not. That is
what distinguishes it from an uncertainty relation, which is pairwise and conjugate (one pair, one
bound, a continuous trade-off bought with a scale). Here there is **no trade-off** — zero is zero,
not "a little of all three" — and **no scale for one to be measured in** (Gate 5). The resonance
with Heisenberg is a resonance of *non-commutativity in general*, and by the B1223 template a
matching shape is not a connection. *(The programme's genuinely Heisenberg-shaped statement is
elsewhere: **B1087's charge complementarity**, where [H, ρ(μ)] ≠ 0 and [H, ρ(λ)] ≠ 0, so charge and
holonomy admit no common eigenbasis — the same content as [x,p] ≠ 0. Registered as the comparison,
not as an identification.)*

**C45 [NO-GO — the anomaly layer is complete].** Over the object's DERIVED 16 (with ν^c) every
anomaly channel vanishes identically — U(1)³, U(1)-grav, [SU(3)]²U(1), [SU(2)]²U(1),
SU(2)-Witten, and (B−L)³ and (B−L)-grav where the imported 15 gives −1/−1: **ν^c is exactly
what cancels the last non-vanishing invariant**. A layer that vanishes identically cannot
supply a ratio, so **anomaly matching cannot further constrain this matter content** — shut
structurally, not merely unexplored (closes L144). — B1096.
Lock: `tests/test_b1096_anomaly_layer.py`.

**C46 [THEOREM — the seam is selective for structure, a catalogue for values].** The object is a
**complement** — `S³ ∖ K`, defined by what is removed — hence **open**, and closing it (Dehn filling)
**is** the symmetry-breaking: the closure is **constitutive, not external** (B286 corrects P011 — the
wall is at the closure, not in the object). The closing supplies, computed: the forced selection set
(**exactly 10** exceptional fillings), **chirality** (every generic filling is chiral, CS ∉ {0,½}), the
**CP sign** (the mirror slope carries CS = −CS exactly), **scale** (core length along (1,n) ≈ 2π/n → 0),
and the **clock** (H₁(cusp T²) = ℤ², ⟨μ,λ⟩ = 1 — a filling is a polarization). Among the ten the **fiber
slope (0,1) is the UNIQUE torus bundle**, and its monodromy is **exactly A = LR** (B287: Alexander
polynomial t²−3t+1 = charpoly(A), Twister, Regina — three independent confirmations): the object
re-sees its own genesis matrix at a canonical seam. **But the selection is stratified (B294): SELECTIVE
for the object's own structure, a flat CATALOGUE for Standard-Model values.**
**AND THE TWO SIDES DO NOT OVERLAP (B288, NEGATIVE):** of 54 closed hyperbolic fillings, **zero**
re-see ℚ(√−3) and **zero** are arithmetic — *the E₆-selecting arithmetic is an open-object property
destroyed by closing*. So the open object carries ℚ(√−3) → 2T → E₆ and no closing; the closed object
carries a canonical forced closing and no E₆. **The two cannot be held at once** — the same shape as
C44's fork, one level below it. (**No SSB mechanism is available**, B295.)
— B286, B287, B288, B294, B295. Locks: `tests/test_b286_the_seam.py`,
`tests/test_b287_distinguished_closing.py`, `tests/test_b288_arithmetic_filling_census.py`,
`tests/test_b294_selection_verdict.py`, `tests/test_b295_ssb_gauge_status.py`.

**C47 [THEOREM — the parity of the cusp].** For a cusp-fixing isometry g of a one-cusped hyperbolic
3-manifold the cusp-fixed count is |Fix| = |det(A − I)| (translation-independent), finite order in GL(2,ℤ)
gives |Fix| ∈ {0, 1, 2, 3, 4} with **3 from (det 1, tr −1)** — and the geometry forbids it: Fix(g) is closed
geodesics plus geodesic **lines** with two ends each, so with **one cusp** |Fix on the cusp| = 2·(#lines) is
**even**. Verified over 1 200 one-cusped census manifolds ({(0,4): 1 196, (0,): 4}, zero odd violations; m004:
Sym = D₄, |Fix| ∈ {0, 4}); the control fires with ≥ 2 cusps (m202 gives 1 and 3). χ(M) = χ(∂M) = 0 at ANY cusp
count, so |Fix| = 3 and χ(∂⁺M) ≠ 0 are different quantities (B1292). The sibling m202 keeps the arithmetic face
and **loses the golden face** (no fibration carries t² − 3t + 1); its localized count is 3 on both cusps at the
price of one identification (I-30), and none of the six members of the three-line class to nine tetrahedra
keeps the golden face — the count of three costs the face (B1302, B1321). — B1291, B1292, B1302, B1321.
Locks: `tests/test_b1291_parity_of_the_cusp.py`, `tests/test_b1292_hatch_satisfiable_mis_scoped.py`,
`tests/test_b1302_the_sibling_m202.py`, `tests/test_b1321_l205_the_siblings_localized_count.py`.

**C48 [THEOREM — every fixed locus counts two or nothing].** On m004 every isometry has
χ(Fix g) = 1 − s_μ(g) ∈ {0, 2} (arcs χ 2, the axis 0, the glides empty, two isolated interior points for the
order-4 elements) by H₁ = ℤ⟨μ⟩ alone; on a closed rational-homology-sphere closing χ(Fix g) = 1 − deg g ∈ {0, 2}
and **the 2 needs an orientation-reversing isometry** — an amphicheiral closing, CS ∈ {0, ½} — so a closing
chiral in B432's sense has χ(Fix g) = 0 for every symmetry: *on a closed closing you may have the 2 or the
c-breaking, not both* (T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING; 360 symmetries of Y₁…Y₉ all in {2, 0}, the
b₁ = 1 control fires {0, 4}). The caveat coefficient is computed: c₍±2,0₎ = ∓4.260982635(2) i ≠ 0, the (±2,±1)
competitor at 7.6 % of it, every horotorus two annuli, χ(∂⁺M) = 0 by computation. Pantev–Wijnholt's localized
count on the cyclic descent (C₃, C₄) is |det(A − I)| ∈ {0, 4}; across the 87 covers of m004 to degree 10, 968
isometries and 1 376 cusp-fixing pairs give {0: 882, 4: 494} — no order-3 cusp rotation in the tower. Three
appears only through the ℤ/3 descent (3 | n), and the descent is vector-like (C51). — B1294, B1295, B1320.
Locks: `tests/test_b1294_the_chirality_bit.py`, `tests/test_b1295_the_caveat_closed_by_computation.py`,
`tests/test_b1320_phase2_arc0_pw_count.py`.

**C49 [THEOREM — the charge-locus parity lock, and the lift fork].** A charge locus (Morse–Bott zero or
vortex) on Fix(θ) is θ-even, so θ-equivariance forces the Higgs direction into the **F₄ chamber**, whose 15
faces are **vector-like or SU(3)-cubic-anomalous — never chiral and clean** (T-CHARGE-LOCUS-PARITY-LOCK). The
object's own harmonic 1-form is θ-odd, swaps ∂⁺M and ∂⁻M and is **non-zero on the arcs** (ω(∂ₓ) = 1.28 / 0.72):
**the object supplies no charge locus on Fix(θ)**. Dropping equivariance gives the programme's first chiral
spectrum — two 16's of SO(10)×U(1), count 2 — at three closer's choices (locus, sign pair, direction: I-27).
The geometric involution has TWO lifts to E₆, the outer θ_D (fixing F₄) and the inner Ad(exp πiρ^∨) (fixing
A₅ ⊕ A₁, the whole Cartan); **on the geometric germ the lift is outer** (six signs ε_n(ι) = (−1)^{n/2+1} over
two primes, the SM seat's theorem verified), so the inner lift is a closer's choice (I-28). — B1296, B1298.
Locks: `tests/test_b1296_the_charge_locus_parity_lock.py`, `tests/test_b1298_the_lift_fork.py`.

**C50 [THEOREM — the one-cusped index, and the cyclic tower is vector-like].** On a one-cusped 3-manifold
the net chirality of a local system V is I(V) = n(V) − n(V*) = (a₀ − a₀*) + t₀* − r₁, and in domain D
I = t₀ − r₁ (T-ONE-CUSP-INDEX; formula and domain sealed before evaluation). Two theorems make it vanish on
the whole cyclic tower: **T-GALOIS-SELF-DUALITY** — for k = ℚ(√−3) = ℚ(ζ₃) every twist of order prime to 3 is
vector-like by arithmetic alone, on every cover — and **T-PERIOD-2-INVERTS-THE-ALEXANDER-MODULE** — the
period-2 symmetry P: a ↦ a⁻¹, b ↦ a³b acts as −1 on ℤ[t^±]/(t² − 3t + 1), hence on Tors H₁(C_n), so
ψ∘P = ψ⁻¹ and every (2+1)-reducible spectral cover on the cyclic tower is vector-like: 16/16 (C₃), 45/45 (C₄),
61 sectors, and 60 census manifolds with torsion ≥ 3 (12 non-self-dual sectors) all zero. W1/W2 are vector-like
on every cusped cyclic cover (V ≅ τ*V* on the branch locus K; the SM seat's Theorem 1 verified), correcting
"rigid" off K. Reported FORCED, not FAIL: the pre-registered test could not have passed. — B1297, B1299.
Locks: `tests/test_b1297_the_spectral_cover_index.py`, `tests/test_b1299_the_period_2_duality.py`.

**C51 [THEOREM — the tower law and the Standard-Model closings].** π₁(Y_n) = ⟨a, b | φⁿ(a) = a, φⁿ(b) = b⟩
for the golden φ, so **h¹(Y_n; ψ) = 1 exactly when a product of n explicit 2×2 matrices is the identity**
(verified by full Fox calculus at every non-trivial character of Y₃…Y₉ with two primes: supports 3, 0, 20, 27,
56, 0, 147; det = 1 everywhere; the even-level correction at Y₂₀; Y₂₄'s 2-primary support is Y₁₂'s). The tower
law's positive half is a theorem on two benches (T-TOWER-LAW-POSITIVE-HALF: ord_m(u) or ord_m(−u) odd ⇒ a
class at every level). **Y₉ carries the Standard-Model gauge algebra and three complete generations** — 706 464
SM lines in 19 624 inequivalent vacua under the group of order 72, **all in mirror pairs, vector-like**; Y₁₂ is
a second SM closing (34 752 lines; 768 one-triplet vacua, one light generation, SM × U(1)² at tree level).
The tree-level vacuum of Y₉'s closing leaves **SM × U(1)_Z′, rank 5**: a family-non-universal Z′ (E₆ part
(5ψ − 3χ)/2, charges 4, −2, 10, −8, −2, plus a family part under which the VEV'd generation's N, ν^c are
neutral), anomaly-free (the family torus's cubic −20 250 cancelled by the 27̄s), every VEV'd field Z′-neutral;
its first consequence is a **regime fork** (FALSIFIER_REGISTER P9): M_Z′/g₂ ≳ 10²–10³ TeV if a light family is
VEV'd, a few TeV if the third — which family it is, is a value the record does not fix. — B1303, B1306
(the SM-derivation seat's sm:B1278–B1304 and sm:B1350, every number re-run or re-derived on main).
Locks: `tests/test_b1303_the_sm_closings_z_prime.py`, `tests/test_b1306_the_older_debt.py`.

**C52 [NO-GO — the θ-odd frame is closed on every sl₂ germ].** B1280's pairing law pairs every deformation
of the E₆ holonomy at every sl₂ germ except one direction — the V₁₀ of the 42 at the subregular point (L204).
Along it genuine non-self-dual E₆ representations exist (relator residuals 1e−61…1e−68 at 110 digits;
self-duality defect ~1e−10), and at each of the four banked 100-digit points **h¹(27) = h¹(27̄) = 0, no
cusp-fixed vector, N(27) = 0** (a perturbed point fails the relator: control). The one flat-sector direction the
pairing left open carries no net count: **chirality on the object is not in its flat E₆ sector.** — B1322
(the SM seat's sm:B1350 re-read on main with main's own Fox calculus). Lock: `tests/test_b1322_l204_verified.py`.

**C53 [THEOREM — the genesis dictionary, the criterion census, and the substrate fork].** The Sturmian
morphisms abelianise onto exactly the non-negative GL(2,ℤ) matrices = ⟨L, R, P⟩ (3 280 morphisms to length 7 →
87 matrices; all 462 with entries ≤ 13 realised); the Fibonacci morphism is L·P and orientation forces
(LP)² = LR = A while (PL)² = RL — **A7 is the placement of the swap inside the tick**; the a·B bundle is m004
(C4 ↔ A1); the cutting sequence of A's expanding eigenline is the Fibonacci word letter for letter: **C1–C5 and
A1–A6 are one construction in two presentations** (T-GENESIS-DICTIONARY). C2 splits into C2a [THEOREM,
self-similarity ⇒ quadratic slope] and C2b [CRITERION, minimality ⇒ φ]: seven self-application criteria pick φ
uniquely (Lagrange √5 with 2√2 second; the least constant quotient; the first hyperbolic trace 3 with h⁺(5) = 1;
the torsion-free closure (1,1); the Markov root (1,1,1); discriminant 5; the smallest quadratic Pisot), and the
smallest Pisot number of any degree is the plastic number ρ = 1.3247… — the census can fail and is seen to.
**Fork F9 (A1's "not one, not three") ROBUST twice:** one record has no mixed closure; three records on T³ give
E₁₂·E₃₁·E₂₃ with dilatation ρ³ and χ = 0 — no hyperbolic carrier (Gauss–Bonnet–Chern); three records on the
surfaces with H₁ = ℤ³ give the Whitehead link complement m129 (ℚ(i), 4G, chiral), s780 (ℚ(√−7)), t12047
(ℚ(i), 8G, amphichiral) — none keeps ℚ(√−3): the price of a third record is the atom. — B1323.
Lock: `tests/test_b1323_the_genesis_upgrades.py`.

**C54 [THEOREM — the mirror is swap × arrow, and covers do not inherit amphichirality].** On every
one-cusped H₁ = ℤ manifold each isometry's orientation sign is the product of its meridian sign and its
longitude sign, det = s_m · s_l (T-MIRROR-IS-SWAP-TIMES-ARROW); m004's eight isometries realise the four sign
patterns (+,+,+), (−,+,−), (−,−,+), (+,−,−) twice each, kernel {1, P}; in the record's bits the fibre's reflection
is the A7 swap, the flow's reversal is the arrow, the manifold's mirror is their product. Of 2 804 one-cusped H₁ = ℤ census
manifolds to seven tetrahedra, 2 794 are invertible-chiral, 7 symmetry-free, **3 full — m004, s726, s912**.
**Covers do not inherit amphichirality:** of the 87 covers of m004 to degree 10 the 9 cyclic and the 1 regular
are amphichiral and **66 of the 77 irregular covers are chiral**, by two orientation-aware methods; every cover
keeps the invariant trace field, so **the atom and a remembered A7 bit coexist on the object's own tower**
(FRESH_EYES Q15). On the chiral one-cusped covers the torsion is generated by the meridian, so cusp-trivial
twists barely exist: 2 live sectors (order 3), both I = 0; 4 Galois-protected sectors 0; 136 control sectors 0
(a nonzero appears only where the four identities fail). The 54 multi-cusped chiral covers await the multi-cusp
index. — B1324. Lock: `tests/test_b1324_arc_b_and_the_dictionary.py`.

*(B909's remaining debts — the six-cubic √77 law, the Compact Measurement Theorem, the
invisible-12 — enter when their locks land; LAW_MAP §F's pending row governs.)*

---

*Maintenance: additions require the B758 admission criteria (exact statement + location +
green lock + one of the five labels); a link whose lock breaks reverts to the arc trail
until repaired; the chain is regenerable from the bank and never a source of authority
over it (GOVERNANCE: views don't outrank arcs).*

> **LOCK AUDIT, B998 (2026-08-09).** `tests/test_b749_genesis_forks.py` tests **F4, F5, F6, F7**. It contains **no F3 test** (cited above), **no F2 test** — C3's only real price — and **no F8 test** — C4's entire price. **So C1, C2 and C4 carry no in-repo lock, and C3 is locked only by a fork pricing a different axiom. — **SUPERSEDED 2026-08-30 (Cell 5's record read): B1003 subsequently wrote the missing locks. `tests/test_b1003_f2_f8_locks.py` exists and passes (5 tests), asserting all seven fork verdicts, F2's pA-count-0 and falsifiability note, and F8's four failing witnesses including the x²+3 irreducibility and the ℤ[φ] order. C4's price IS locked, and C3's real price (F2) is locked. This audit note asserted a gap its own remedy had closed — the E53 class, inside the ledger that records it.**** The claims are not thereby false: **C1 (Morse–Hedlund) and C2 (Hurwitz/Lagrange extremality) are classical, cited not re-proved.** What was false is this ledger's assertion that they are locked *here*. **CORRECTED 2026-08-09 (B1003): F2 and F8 were COMPUTED all along** — B749 has `compute.py`, `output.txt` and a verdict for all seven forks. **What was missing was the LOCKS**, now written (`tests/test_b1003_f2_f8_locks.py`). **F2 = ROBUST** (pA count 0 for the whole periodic family — A2 selects the destination); **F8 = GEOMETRY-NECESSARY** (four witnesses fail; **x²+3 irreducible over ℚ(√5)** — ℚ(√−3) is bought at geometrization). **The chain's price is exactly two FRAGILE forks: F5 orientation and F6 the puncture.**
