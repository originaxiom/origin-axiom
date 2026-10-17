# The ladder — a pattern analysis of the origin-axiom record

An outside referee's reading of the record at fe25f7e (16–17 Oct 2026): every arc's verdict file and the first 6,000
characters of every FINDINGS.md mined for the objects that recur, the dependencies between arcs, and the identification
ledger. The mining regexes and the Markov check are in `checks/check9_ladder_mining.py`.

## The finding

Every object the record calls forced is a shadow of one classical structure: SL(2,ℤ) acting on ℤ², seen through its
canonical quotients and its first hyperbolic element. The ladder is the subgroup–quotient lattice of that one group,
and it has been climbed before — by Dedekind, Klein, Fricke, Markov, Rademacher, Atiyah and Ghys. The record's 1,397
arcs re-climb it under new names: the golden ratio, the figure-eight, 2T and E₆, the parities, the theta triplet, the
η-twist, the period phase, the constant mode are rungs E, E, D, D, C, C, B, B, F of a seven-rung tower whose top is the
abelianisation SL(2,ℤ) → ℤ/12 and whose spectrum is the Selberg trace formula. Physics never enters the ladder. It
enters only through the identification ledger, and the ledger's own statuses say what the mathematics cannot: of 34
identifications, every one that is EARNED identifies a structure with a structure; every one that identifies a
structure with a physical value is UNEARNED or REFUTED, 0 of 12. The record has already named this law — the Quiddity
No-Go — as a conjecture; its own ledger is the evidence.

## The census of the record

The record (14,075 files at fe25f7e) holds 1,439 arc folders, 1,397 with a verdict: 946 PROVED, 346 NEGATIVE, 93 OPEN,
12 RETRACTED. The negative share is 26% and flat across every subject (21–26% on every rung below), so the verdicts do
not separate mathematics from physics; the identification ledger does. 2,382 stated dependencies connect the arcs; 939
arcs state none. 46 arcs are superseded, 117 create a law.

The backbone — the arcs most often depended on — is the E₆ era: B1297 (the spectral-cover index, 36 dependants), B854
(the centraliser of 2T in e₆, 24), B892 (the gauge algebra z = su(3)⊕su(2)⊕u(1)³, 22), B883 (the 27 on the Chevalley
frame, 21), B1291 (the parity theorem: 3 excluded on a one-cusped manifold, 21). The weave era's hubs are B1600 (13),
B1620 (11), B1642 and B1644 (11 each).

What the record pays attention to, by the number of arcs that mention an object:

| Object | Arcs | First | Last | Peak block |
| --- | --- | --- | --- | --- |
| spin structure / the hand / chirality | 520 | — | — | B1400s |
| the golden ratio, φ, Fibonacci | 505 | B−1 | B1655 | B400s |
| E₆, E₈, the 27 | 503 | B−1 | B1666 | B1100s |
| the figure-eight (m004, 4₁) | 492 | B2 | B1614 | B200s |
| the cusp / the puncture | 428 | — | — | — |
| masses, Yukawa, Higgs, generations | 337 | B55 | B1667 | B1200s |
| the SL(n) towers | 323 | B−1 | B1490 | B100s |
| the metallic family | 226 | — | — | — |
| theta functions | 200 | B61 | B1658 | B1100s |
| the Dedekind η function | 55 | B144 | B1667 | B1400s |
| the trefoil | 16 | — | — | — |
| the Selberg trace formula | 10 | B382 | B1666 | B1600s |
| the η-invariant / signature defect | 6 | B1325 | B1650 | B1600s |
| the Rademacher function / Dedekind sums | 2 | B728 | B1623 | — |

Two patterns. First, the order of attention runs up the ladder from its most special rung: the golden ratio and the
figure-eight (rung E) peak in B200–B400, E₆ and the 27 (rung D) in B1100, the index and the hand (rung F) in B1400,
theta and η (rungs C and B) in B1600. The record climbed from the particular toward the general, which is why each rung
was met without its classical name. Second, the names that unify the climb are the rarest words in the record:
Rademacher 2 arcs, the η-invariant 6, Selberg 10, the trefoil 16, out of 1,395. The objects that explain the
recurrences are the ones the record has not yet called by name.

## The ladder

One group, SL(2,ℤ) on ℤ², and the structures canonically attached to it. Each rung lists the classical object, the
record's words for it, the number of arcs that live there (an arc can sit on several rungs), what is fixed on that rung,
and what is not. Reading down the table is reading the record's history backwards: it entered at rung E and has been
climbing toward A and B.

| Rung | Classical object | The record's words | Arcs | Fixed there | Not fixed there |
| --- | --- | --- | --- | --- | --- |
| A. The group | ℤ² with the two unit shears L, R generating SL(2,ℤ); Stern–Brocot and continued fractions; the Bernoulli walk on L, R and Minkowski's ?-function; the Fricke–Vogt invariant κ = tr[a,b] | records, moves, pull-back, non-cancellation, the weave, the escape, states, words | 497 | the combinatorics: words ↔ classes, the Lyapunov exponent 0.396, the singular end law | anything carrying a scale |
| B. The abelianisation | SL(2,ℤ) → ℤ/12 (Mp₂ → ℤ/24): the η multiplier, the Rademacher function Ψ, Dedekind sums; Ψ = linking with the trefoil (Ghys) = η-invariant and signature defect of the torus bundle (Atiyah, Hirzebruch) | the η-twist (21 ≡ −3), the period phase i^{#L−#R}, the coherent quarter, the 1/8-turn exponents, allowed weights 3/2 mod 2 | 58 | every phase and every allowed weight; the ℤ₄ monodromy of the amplitude | anything with a magnitude |
| C. The mod-2 quotient | SL(2,𝔽₂) ≅ S₃ on the three even spin structures = three even theta characteristics; Γ(2) and its Hauptmodul λ = θ₂⁴/θ₃⁴; Γ(4) and the weight-1 triplet (θ₂², θ₃², θ₄²); Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴; the half-period values of ℘ | the three parities, the clock, the triplet T, the isotropic triplet ρ, the defect D, the structural zero, Prop. 13 | 551 | the three, the triplet's multiplier, isotropy, the zero-diagonal texture | which parity is which field (the dictionary) |
| D. The order-3 point | ω and its stabiliser ℤ/6 (the trefoil's ℤ/2 ∗ ℤ/3); SL(2,𝔽₃) = 2T, A₄; McKay: 2T ↔ affine E₆ (2O ↔ E₇, 2I ↔ E₈); ℤ[ω]; the hexagonal modular torus H/Γ′; λ(ω) = e^{iπ/3} | the common point, 2T at the common point, the E₆ era, the 27, trinification ℤ/3, τ = ω, the order-12 residual, D(ω) = 0 | 797 | the group, its McKay dual, the symmetric point | any mass: the symmetric point degenerates them (N5, Prop. 18) |
| E. The first hyperbolic class | trace 3, discriminant 5, class number 1, the unit φ²; the Cohn matrix LR; the figure-eight m004 and its sibling m000; Markov's equation (the weave's trace triples (3,3,3), (3,3,6), (3,6,15), (6,15,87) are the Markov tree ×3 — verified); Hurwitz's √5 and the Lagrange spectrum; period-one continued fractions [m; m, m, …]; the Fibonacci substitution; Fibonacci anyons with quantum dimension φ; ℤ[φ] and icosahedral quasicrystals; Vol(4₁) = (3√3/2)L(χ₋₃,2); the A-polynomial's Mahler measure | the seed, the root, the tick, the metallic family, the escalator towers, the golden quasicrystal (B517), the Jones/anyon era, I-3, I-12, I-20, I-21 | 927 | uniqueness of the trace-3 class, φ as the first Lagrange constant, the Markov tree | why this class: SE1 is tailored to it (disclosed) |
| F. Geometry and spectrum | closed geodesics (Series) = modular knots in SL(2,ℝ)/SL(2,ℤ) = the trefoil complement (Quillen–Milnor); the Selberg trace formula and Maass forms; Duke's equidistribution; the once-punctured torus and its cusp; twisted Euler characteristics (zero on cusped 3-manifolds); χ(M₁,₁) = −1/12, χ(M₁,₂) = 1/12 | threads, the arena, the layers, the constant mode 0.31500491, the class index, N1, the three ends, the end radius | 591 | equidistribution, the vanishing of χ, the orbifold Euler characteristics | any index without a chosen domain; any end without a chosen horocycle |

The physics words — masses, mixing, gauge group, Higgs, neutrinos, Λ, anyons — occur in 663 arcs, and in only 17 of
them without a ladder object alongside. Physics is never a rung; it is always an identification of a rung with
something outside the ladder.

## One object, many names

The concordance below is the practical output of the pattern analysis: each row is a recurrence the record met under
its own name. "Verified" means checked by computation in the referee's session; the rest are classical and cited.

| The record's name | The classical name | Where it lives | Status |
| --- | --- | --- | --- |
| non-cancellation, κ ≠ 2 | the Fricke–Vogt invariant κ = tr[a,b]; κ = −2 is the parabolic commutator, the puncture | rung A | classical (Fricke, Goldman); I-20 earned |
| the weave | the modular group on the upper half-plane; the ruled weave ⟨L,R⟩ is the braid group B₃, Mp₂(ℤ)'s cover | A | classical |
| threads | closed geodesics of the modular surface = modular knots (Series 1985, Ghys 2006) | F | classical |
| the arena | SL(2,ℝ)/SL(2,ℤ) = the trefoil complement (Quillen, in Milnor's K-theory book) | F | classical |
| the seed LR, the root | the Cohn matrix of the golden ratio; the monodromy of the figure-eight; the first Markov number | E | classical |
| the common point and its surface x²+y²+z² = xyz | the Fricke surface at κ = −2 = Markov's surface x²+y²+z² = 3xyz after dividing by 3; (0,0,0) is the quaternion representation; the weave's generator pairs (LR, RL⁻¹), (LR, RL), (LR, LRRL), (LRRL, LRLRRL) have trace triples (3,3,3), (3,3,6), (3,6,15), (6,15,87) = 3 × the Markov triples (1,1,1), (1,1,2), (1,2,5), (2,5,29) | E | verified |
| the three parities, the clock | SL(2,𝔽₂) ≅ S₃ permuting the three even spin structures / theta characteristics | C | classical |
| the triplet T and its multiplier | the Γ(4) weight-1 triplet (θ₂², θ₃², θ₄²) twisted by χ_η²¹; and (θ₃², θ₂², θ₄²) = (p² + q², 2pq, p² − q²) for the weight-½ doublet (p, q) = (θ₃(2τ), θ₂(2τ)) — the flux-2 zero-mode doublet of a magnetized torus: T is the symmetric square of two generations, not three elementary ones | C | verified (the representation reconstructed from the formula; the Sym² identity is classical) |
| the hand | the choice of sheet of the orientation double cover (m004 over m000); ρ against ρ̄ | B/C | classical |
| 2T at the common point | SL(2,𝔽₃); McKay graph = affine E₆ (the whole E₆ era is this rung's McKay shadow, I-1 earned) | D | classical |
| the tick σ² = LR; the rule a → ab, b → a | the Fibonacci substitution; the golden matrix LP of determinant −1, (LP)² = LR; the Gieseking manifold m000 | E | classical |
| the isotropic triplet ρ·ρ = 0, the structural zero | Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴ | C | verified |
| Prop. 13, Σρ_r²℘(z_r) = 0 | the three half-period values of ℘ for the Legendre form; a two-line identity | C | verified, with proof |
| the defect D | (2/π)(θ₂²θ₄²/θ₃⁶)·L′(λ) on the imaginary axis, L the Rogers dilogarithm, λ the Γ(2) Hauptmodul; D(ω) = 0 because λ(ω) = e^{iπ/3} is the figure-eight's tetrahedral shape; D is not a Maass form | C/E | verified |
| the period phase i^{#L−#R} | #L − #R = Ψ(γ), the Rademacher function (checked on nine words); e^{iπΨ/2} is the multiplier of η⁶; Ψ = the linking number with the trefoil (Ghys) = the η-invariant / signature defect of the thread's torus bundle (Atiyah 1987) | B | verified + classical |
| the constant mode 0.31500491 | the identity term of the Selberg trace formula; Duke's equidistribution of closed geodesics | F | verified to eight digits |
| the escape rate 0.396 | the top Lyapunov exponent of the Bernoulli product of L and R; the p = 0 end law is Minkowski's ?(x) | A | verified |
| the weight-1 Yukawa (unique) | the Zee texture: zero-diagonal Majorana matrix, bimaximal mixing, inverted ordering; (φ⁻², φ⁻¹, 1) at τ = i | C/E | verified |
| the Higgs S ∈ M₂(ℂ) with S̃ = ϵS̄ϵᵀ; V = 1 ⊕ U(2) | the bidoublet of left–right symmetric models and its conjugate; the one-bidoublet degeneracy | identification | classical (physics) |
| the down–lepton miss, 3.14 | the Georgi–Jarlskog colour Clebsch 3 (a Higgs with a colour-charged component) | identification | classical (physics) |
| the metallic family L^mR^m, L^mP | period-one continued fractions [m; m, m, …], discriminants m² + 4 | E | classical |
| the E₆ 27 and trinification ℤ/3 | McKay + the stabiliser of ω | D | classical |
| the golden quasicrystal (B517), the Fibonacci anyon (Jones era) | ℤ[φ] in its icosahedral and TQFT dresses: the same rung-E unit | E | classical |

## The identification ledger is the whole physics

`docs/IDENTIFICATION_LEDGER.md` keeps 34 rows, I-1 to I-34, each an identification of an object of the ladder with
something else, with a status. Sorting them by what the right-hand side is gives the only clean separation in the
record:

| Right-hand side of the identification | Rows | EARNED | UNEARNED | REFUTED |
| --- | --- | --- | --- | --- |
| another mathematical structure (McKay E₆; Vol(m004) = an L-value; the character variety = the modular curve 40a3; the Fricke invariant; the Maclachlan–Reid quaternion algebra; the SO(10) grading of E₆; D₄ triality; the genus V₄; the Eisenstein unit; the three ADE hats) | 10 | 6 | 1 | 3 |
| a physical *structure* (the trace map = N = 2* S-duality; 3d gravity inside E₆ Chern–Simons; the ALE group of a 6d type; SU(4)₁; the Lorentz spin lift; the spin class; the principal sl₂ embedding; the chiral vacuum; the gauge-algebra lift; the charge locus; the CFT module group) | 12 | 2 | 8 | 2 |
| a physical *value or count* (θ_QCD; θ̄; the observer's ℤ/2; the listener map, twice; hypercharge Y; the generation index; a cohomology dimension as the generation count; the chiral index as the generation count; the triplet as the left-handed multiplet; the hypercharge dictionary; the read-out of masses and the CKM) | 12 | 0 | 10 | 2 |

Structure-to-structure identifications get decided: six earned, three refuted, one open, because each is a theorem or
its negation. Structure-to-value identifications never get earned: zero of twelve, in 1,397 arcs. The record conjectured
this as the Quiddity No-Go (S067: a parameter-free self-generating structure supplies the form, never the selection of
an element); the ledger is its empirical proof on the record's own history. The two earned physical-structure rows
(I-2, I-19) identify a symmetry with a symmetry — the modular group with the modular group — and yield no number either.

The current paper's inputs table is the same pattern seen from the other side: all of its rows are postulates,
readings, choices or identifications, and the only lines it can mark derived are those that stay inside the ladder.

## The principle, and three predictions

Let G = SL(2,ℤ) act on ℤ². Everything the record has proved is a statement about G: its canonical quotients (G → ℤ/12,
the η character; G → SL(2,𝔽₂) ≅ S₃, the parities; G → SL(2,𝔽₃) = 2T, the common point; G → SL(2,ℤ/4) of order 48 and
the weave's image of order 96), its commutator subgroup (the punctured torus, the Markov tree), its first hyperbolic
class (φ, the figure-eight), its homogeneous spaces (the upper half-plane, the trefoil complement) and their spectra (η,
θ, Maass forms, the trace formula). The unifying principle that gives rise to all of them is G. "Non-cancellation" is
not an axiom that produces G; it is the sentence κ ≠ 2 read inside G's character variety, as the paper itself says.
Three predictions follow, each falsifiable on the next hundred arcs:

1. Every future arc graded PROVED whose statement carries no identification will be a theorem about G already in the
   literature, or a corollary of one, under a new name. A counterexample is a PROVED, identification-free arc with no
   classical counterpart; the concordance above found none among the paper's results.
2. No arc will earn a structure-to-value identification until an axiom is added that is not a reading of G — a
   dynamics, a flux, a potential, an end mechanism. The ledger's EARNED column in its value rows stays at 0 until
   GENESIS gains such a line.
3. The climb ends at rung B. The forced results now being found (B1623, B1650, B1666: the period phase, the
   η-invariant, the layers) are the abelianisation and the trace formula; above them G has no further canonical
   structure, so every later "forced" step will be a choice of quotient, class or domain — a selection, which the record
   already knows how to price.

If prediction 2 is wrong, the program has physics; if it is right for another hundred arcs, the program's result is the
Quiddity No-Go itself, with 1,400 arcs as its evidence.

## What is left to do on the ladder

1. Rename. Adopt the classical names beside the record's (a glossary from the concordance above). It costs a day and
   ends the rediscoveries: the Markov surface, the Rademacher function, the Zee texture and the bidoublet each cost arcs
   that a name would have saved.
2. The one famous open problem that lives on the record's own object is Markov's uniqueness conjecture (Frobenius 1913;
   Aigner, *Markov's Theorem and 100 Years of the Uniqueness Conjecture*, 2013): every Markov number is the largest
   member of exactly one triple. The weave's generator pairs are the Markov tree, the common point is Markov's surface,
   and the record's "selection" question — which thread, which class — is uniqueness in Markov's own language. No new
   leverage is claimed; it is where a mathematician would point the machinery.
3. The only route to a derived number is an identification that comes with its own dynamics: a magnetized torus whose
   zero modes carry ρ with its twist, where the Yukawas are computed overlaps and the free data are integers (fluxes)
   plus τ. The record's triplet is the symmetric square of the flux-2 doublet, so the search begins with two flux-2
   sectors and a flux-4 Higgs. If no assignment reproduces the twist, that is a negative worth sealing.
4. Or publish the law. Prediction 2 as a result — a 1,397-arc experiment in which every structure-to-structure
   identification was decided and no structure-to-value identification was earned — is a case study in the
   structure–value gap that the philosophy of physics argues about abstractly (Newman's 1928 objection, which the
   record already answers with its Galois firewall). It is the one thing in the record nobody else has.
