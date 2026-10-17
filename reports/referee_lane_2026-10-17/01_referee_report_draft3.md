# Referee report — What a grammar of records fixes (Draft 3)

An outside referee's report, 2026-10-16/17, on the Draft 3 PDF (sha256 398141118cf6…, byte-identical to the PDF then
committed at `papers/P9_what_a_grammar_fixes/`). The checking scripts are in `checks/` beside this file. The report was
applied by main as S142 (Draft 5, P-189); it is kept here as the record of what was checked and how.

## Summary and recommendation

Recommendation: major revision. Not acceptable as a research article in its present form, for reasons of content and
calibration rather than correctness; every claim I could check is correct, and the paper's own accounting (0 of 19) is
accurate.

The submission reads a one-sentence principle ("existence is what remains when cancelling to nothing cannot complete")
as SL(2,ℤ) acting on ℤ² by the two unit shears L and R, calls the hyperbolic conjugacy classes threads and the whole
action the weave, and then proves: (i) the mod-2 reduction permutes the three non-zero parities as S₃ and the quaternion
point of the Fricke surface carries 2T (Thm 6); (ii) a lift of that action to the three parity lines is the Γ(4)
weight-one theta multiplier twisted by χ_η²¹ (Thm 9); (iii) in a fibre frame the theta triplet is isotropic by Jacobi,
so every single-point coupling has a null vector (Thm 12); (iv) an exact determinant/adjugate identity for a bilinear
coupling on M₂(ℂ)×M₂(ℂ) (Thm 20); (v) an index n(|Λ⁺|−3) that equals ±3 on two of four invariant domains (Thm 24); and
a weight −1 automorphy law for a defect D whose period phase on a closed geodesic is i^{#L−#R} (Lemma 21, Thm 22). It
then reports that none of this fixes a flavour number (N1–N7).

What the paper gets right: the mathematics is correct wherever it can be checked (ledger below), the inputs are priced in
one table, the provenance of the seed is disclosed, failures are kept, and the record is public with passing locks. That
is rarer than it should be.

What it does not have: a result a reader outside the program needs. The flavour triplet is the classical action of the
modular group on the three even theta characteristics; the twist by a power of χ_η is the only thing a genuine lift
could differ by (Major point 1); the "structural zero" is Jacobi's identity; the ±3 is the dimension of a postulated
triplet read through a chosen domain; the negatives refute the program's own ansätze (one Higgs, τ = ω, eighteen flat
lines) rather than bound anything outside them. The paper says all of this itself, in the scope notes — but the abstract
and the section titles say more than the scope notes allow, and the text carries roughly forty pages of program
apparatus (arcs, seals, locks, seats, tribunals, scoreboards, Reading boxes) that a journal reader cannot use.

The honest shapes this material can take are two: a short mathematical note (Theorem 20, Lemma 21 with Theorem 22, the
constant-mode check, and the exponent 21 with its convention) or a program report on the arXiv as it stands, with the
fixes below. As a physics submission it would be rejected for having no physical result, which the authors already know.

## Verification ledger

Every hand-checkable claim was re-derived independently of the record; the exact identities all hold. The checks below
were run in a fresh environment (sympy 1.14, mpmath 1.3, 30-digit precision where numeric), with no access to the
repository's scripts.

### Exact identities (Sections 2, 5, Appendix A)

| Claim | Where | Method | Result |
| --- | --- | --- | --- |
| [LR,RL] = (−7 6; −6 5), trace −2, −U with U unipotent | Prop. 1, A.2 | exact integer arithmetic | holds |
| (LR⁻¹L)² = −I, (L⁻¹R)³ = −I, fixed points i and ω | Prop. 1, A.2 | exact | holds |
| Fricke: x²+y²+z²−xyz−2 = tr[LR,RL] = −2 | §2 | exact | holds |
| Mirror diag(1,−1) sends L→L⁻¹, R→R⁻¹ | §2 | exact | holds |
| det(B−I) = 2−tr B; torsion ab; one torsion-free closure on the 12×12 grid; SNF of LR−I trivial | Thm 2, Fig. 2 | exact | holds |
| L fixes parity (0,1) and swaps the other two; R fixes (1,0); LR cycles | Lemma 4 | exact mod 2 | holds (with the row-vector, right-action convention of A.0) |
| ρ·ρ = 0 at every τ (Jacobi) | Lemma 11, A.1 | mpmath, 30 digits, 4 points incl. i and ω | holds to 10⁻³² |
| det Y(a) = (ρ·ρ)(a·a)(ρ·a); Y(a)ρ = (ρ·ρ)a | Thm 12(1) | polynomial identity in 6 variables | holds exactly |
| s₁s₂ = ‖ρ‖²‖a‖², s₁²+s₂² = 2‖ρ‖²‖a‖²+|a·ρ|², m² = ξ₋/ξ₊ with ξ²−(4+κ)ξ+4 = 0, m ∈ [½,1] for real a | Thm 12(2) | random isotropic ρ, real a, 5 draws | holds to 10⁻⁶ |
| det Y(S,M) = 4 det S det M tr(ϵSMᵀ) | Thm 20 | polynomial identity in 8 variables | holds exactly |
| adj Y = det S A(M) + det M P A(S), with A as displayed | Thm 20 | polynomial identity | holds exactly as printed (the transposed variant fails, so the matrix A is printed correctly) |
| Y(S,Nϵ⁻¹) = Y(N,Sϵ⁻¹); det Y = −4 det S det N polar(S,N); tr(ϵSMᵀ) = −polar | Thm 20 | polynomial identities | hold exactly |
| A(pqᵀ) rank one, ‖A‖ = 2‖M‖²; Gram spectrum {1,2,2,4}‖M‖² | Prop. 19 | numeric | holds |
| m₁m₃ = m₂² at N = S; squared masses are the roots of x³−e₁x²+e₂x−e₃ | Thm 20(2),(3) | numeric | holds to 10⁻¹⁵ |
| Σ_r ρ_r² ℘(z_r) = 0 for the stated unit↔half-period assignment; fails for the other assignments at generic τ | Prop. 13 | ℘ from −(log θ₁)″ with its constant fixed by the Laurent pole; 3 values of τ | holds to 10⁻³¹; swapped assignments give O(1) |

The identity behind Prop. 13 also has a two-line proof the paper should give: with e(1/2)−e((1+τ)/2) = π²θ₄⁴ and
e((1+τ)/2)−e(τ/2) = π²θ₂⁴, the sum is θ₂⁴(e₁−e₃) + θ₄⁴(e₂−e₃) = π²(θ₂⁴θ₄⁴ − θ₄⁴θ₂⁴) = 0 once Jacobi is used to split
θ₃⁴.

### The representation ρ (Theorem 9, Remark 10, Theorems 27–28)

The paper's stated formula ρ = χ_η²¹ ⊗ ρ_u, taken literally in the basis (θ₂², θ₃², θ₄²) with the classical
transformation laws of the theta constants and of η, reproduces every structural claim the paper makes about ρ. This is
the strongest check in the report: it was built from the formula alone, with no access to the record's lifts.

| Claim | Where | Result from the reconstruction |
| --- | --- | --- |
| ρ is a genuine representation of Mp₂(ℤ): s² = (st)³, s⁸ = 1, s⁴ = −1 | Thm 9(1) | holds |
| ∆⁴ ↦ −1 on T | Thm 9(1) | holds (s⁴ = −I) |
| exponents of t on T are (1/8, 3/8, 7/8) turns | Thm 9(2) | holds: {1/8, 3/8, 7/8} |
| image has order 96; the untwisted ρ_u has order 48 | Thm 9, §4 intro | holds: 96 and 48 |
| ρ irreducible and not equivalent to its conjugate | Thm 9 scope, B1640 | holds: commutant dimension 1, ⟨χ, χ̄⟩ = 0 |
| weight 3/2 allowed, the dual not (central element) | Thm 9(3) | holds: ρ(s²) = i·1, so i^(−2k) = i forces k ≡ 3/2 (mod 2); the dual needs k ≡ 1/2 |
| dim M_k(ρ) = 0,0,1,1,2,2,3,3 at k = −1/2, 3/2, …, 27/2; dim M₃(ρ_u) = 1 (the Serre derivative only) | Thm 9(3) | holds exactly (computed as η³f ∈ M_{k+3/2}(ρ_u) with the cusp condition on the θ₃²+θ₄² component) |
| residual at generic τ = four scalars; at i cyclic of order 8 with a plane containing the clock line and (θ₂²+θ₄²); at ω cyclic of order 12 with three eigenlines of squared overlap 1/3 with every parity line | Rem. 10 | holds: centre of order 4; ρ(s) has eigenvalue e^{iπ/4} on span(θ₃², θ₂²+θ₄²); ρ(st) eigenvectors have |components|² = (1/3,1/3,1/3) |
| 68 subgroups in 26 conjugacy classes; 57 abelian; T restricted to H a sum of three characters exactly for the abelian ones | Thm 27(1) | holds: 68, 26, 57 (orders 1:1, 2:7, 3:4, 4:11, 6:4, 8:19, 12:5, 16:7, 24:5, 32:3, 48:1, 96:1) |
| ρ(LR) has eigenvalues {1, ω, ω²}, is monomial with a 3-cycle, and its operator mean is the rank-one democratic matrix | Thm 28(2) | holds |

One convention point should be fixed in the text. With the row-vector, right-action convention of Appendix A, L fixes
the parity vector (0,1) and hence the character (−,+), while Theorem 9(2) places θ₂² — the line ρ(t) fixes — on (+,−).
The two agree under the column-vector (left-action) convention, so nothing is wrong, but the paper should state once
which convention the labels (+,−), (−,+), (−,−) follow, because a reader checking Lemma 4 against Theorem 9(2) with
Appendix A's convention gets the opposite labelling.

### The motion (§5.5, §7.6, §7.7)

The analytic claims about D and f hold; the constant mode is reproduced to all eight printed digits; the period phase
holds on every thread tried; the escape rate at p = 0 is reproduced, the one at p = ½ is 1.6% off and the estimator
should be stated.

| Claim | Where | Method | Result |
| --- | --- | --- | --- |
| D(τ+1) = iD(τ), D(−1/τ) = iτ⁻¹D(τ); χ(R) = −i, χ(L⁻¹R) = −1 | Lemma 21, A.3 | hand derivation (λ ↦ λ/(λ−1), h(λ/(λ−1)) = −h(λ)/(1−λ)) and mpmath at two τ | holds; residuals 10⁻³¹ |
| f = |D|/‖ρ‖² is modular invariant, vanishes at ω, peaks near i | Lemma 21, Fig. 4 | numeric; also f = π|θ₃⁴h(λ)|/(|θ₂|⁴+|θ₃|⁴+|θ₄|⁴) in closed form | holds; f(i) = (π/2) ln 2 = 1.08879, consistent with the colour bar; D(ω) = 0 also follows from Lemma 21 since χ(L⁻¹R)(ω+1)⁻¹ = −e^{−iπ/3} ≠ 1 |
| cusp law D/(q‖ρ‖²) = e^{−iπx/2}(8π²y + 4π(1+e^{−2πix}) − 32π ln 2) | Prop. 16 | hand derivation of the x = 0 form; mpmath at x ∈ {0, 3/10, 1/2, 1}, y ∈ {4, 5} | holds; relative error 2.8·10⁻⁵ at y = 4 and 1.2·10⁻⁶ at y = 5, i.e. O(|q|) as claimed |
| average of f over the modular surface = 0.31500491 | Census 32(1), Fig. 7 | Gauss–Legendre on the fundamental domain, three resolutions | 0.3150049063 at all three resolutions |
| ψ(s+ℓ) = i^{#L−#R} ψ(s), branch sign +1 | Thm 22, Census 23 | geodesic axis mapped to the imaginary axis, phase of dz/ds unwrapped over one period; threads LR, L²R, L³R, L⁵R, L²R², LRL²R, L⁴R²L, LR⁵; three start points each | holds to 10⁻²⁹ on all 24 cases; the continuation of (dz/ds)^{−1/2} returns +(cz+d) |
| escape rate 0.3959 ± 0.0004 at p = 0 and 0.1007 ± 0.0005 at p = ½; P(ξ>0) from 1 to 0.53 | Census 31, Fig. 6 | Monte Carlo of the top Lyapunov exponent of the L^{±1}, R^{±1} walk (60 words of 40 000 letters) | p = 0: 0.3962 ± 0.0001, consistent. p = ½: 0.0991 ± 0.0002, 1.6% (3σ) below the paper's value. P(ξ>0) ≈ 1.00, 0.90, 0.58, 0.53 at p = 0, 0.1, 0.3, 0.5, consistent with Fig. 6(a). The paper's "escape per step" is the Lyapunov exponent, i.e. half the hyperbolic drift of d(i, g·i); it should say so, and state the word length and sample size behind the p = ½ figure |
| 988 signed words to length eight, 448 of odd trace | after Lemma 4 | exhaustive count | holds: 2 × 494 words with both letters, 2 × 224 of odd trace |
| 37 geometries to length eight, 16 odd and 21 even | Census 5 | exhaustive count of primitive cyclic words up to rotation and L↔R | holds: 37 = 16 + 21 |
| "without SE1 every state remains (758 to word length 12)" | Thm 2 scope | exhaustive count | not reproduced: 745 primitive cyclic words up to rotation (379 up to the swap). The paper should define "state" in that sentence |
| Gauss–Kuzmin digits 0.415, 0.170, 0.093, 0.059 | §7.6 | log₂(1 + 1/k(k+2)) | holds |

Not verifiable from the paper (and not attempted): the end radii of Census law 25 (they need the uniformisation of the
punctured torus at each τ), the layer coherence of Census 32(2),(3) (the quantity "phase-one coherence" is not defined
in the paper), the B1660 fit, and anything on L₆ (Theorem 24) or on the zero modes of M₁,₂ (Theorem 6(3)).

### Data, sources and the record

The data claims are right, the classical facts are cited correctly, and the cited record is public and consistent with
the paper; the paper's own checks and the lock tests of Table 2 pass in a fresh clone.

| Claim | Where | Check | Result |
| --- | --- | --- | --- |
| (m_μ/m_τ)/(m_s/m_b) = 3.14 from the running masses at M_Z | §7.5 | Huang & Zhou 2021 (arXiv:2009.04851), Tables 2–3: m_s = 53.16 MeV, m_b = 2.839 GeV, m_μ = 0.101766 GeV, m_τ = 1.72856 GeV | 3.144; the m_s uncertainty alone spans 2.89–3.44, which the paper should quote |
| one Higgs needs 15.9 for the up quarks against the leptons under the half bound | Prop. 19 | (m_c/m_t + m_t/m_c)/(m_μ/m_τ + m_τ/m_μ) with m_c = 0.620, m_t = 168.26 | 15.92 |
| χ² bound 11.07 is the 95% point of χ²₅; the one-sided argument | Census 30 | scipy | 11.070; the argument (min over parameters ≤ value at the true point) is sound |
| Γ(4): genus 0, six regular cusps, dim M_d = 2d+1 for d ≥ 1; the quotient ring ℂ[θ₂²,θ₃²,θ₄²]/(Jacobi) has 2d+1 elements in degree d | §4 | dimension formula and a binomial count | holds (also for odd d, since −I ∉ Γ(4)) |
| Gauss–Kuzmin 0.415, 0.170, 0.093, 0.059; geometric 2^{−k} at p = 0 | §7.6 | arithmetic | holds |
| Bibliography | all | entries [1]–[35] checked against known works | correct as far as checked; [2] carries no URL or DOI |
| The record [2] | all | cloned github.com/originaxiom/origin-axiom at fe25f7e (16 Oct 2026); the built PDF there is byte-identical to the reviewed Draft 3, while its sources already say Draft 4 | every arc the paper cites exists under frontier/ except B1516, which is an SM-seat arc (sm:B1516) that is not in the main tree; cite it with its seat prefix or re-derive it on main |
| Lock tests of Table 2 and of T3–T7 | App. B | pytest on the 12 lock files named in the paper | 30 passed in 14 s (they verify committed hashes and a few live recomputations, e.g. the period phase on five threads and the coherences of LR and L²R²) |
| checks/cusp_law.py, checks/commutator_subgroup.py | App. B | run from the clone | pass; the cusp check computes D through B1654's Szegő-kernel instrument and returns the same 271.269759 that the closed form of Lemma 21 gives here, a useful cross-validation of the two definitions of D that the paper should mention |
| B1663's estimator | Census 31 | read the instrument | the "escape rate" is (1/n) log‖Xₙ‖_F at the first passage of an entry past 10⁶⁰ (or n = 40 000). Emulating that estimator gives 0.1001 ± 0.0004 at p = ½, consistent with 0.1007 ± 0.0005; the fixed-length Lyapunov exponent is 0.0991 ± 0.0002. The 1% gap is the Jensen bias of a first-passage estimator (E[1/τ] > 1/E[τ]); harmless here, but the paper should state the estimator |
| B1666's coherence | Census 32 | read the instrument | coherence = |∫ψ ds| / ∫|ψ| ds over one period, on the threads with #L ≡ #R (mod 4); the paper never defines it |
| B1660's sealed outputs | Census 30 | FINDINGS.md and the JSON | consistent with the paper: 54 cells excluded, best 34.40, run time 6 h 43 min, two labelled post-seal explorations |

## Major points

1. **Theorem 9 is calibrated too high.** Two genuine representations of Mp₂(ℤ) that agree projectively differ by a
   character, and Mp₂(ℤ)^ab = ℤ/24 is generated by χ_η. So once the three parity lines are identified with the three
   even theta characteristics — the classical fact that SL(2,ℤ) permutes the even spin structures of the torus through
   SL(2,𝔽₂) ≅ S₃ — any genuine lift of the moves that agrees with ρ_u projectively is "the theta multiplier up to a
   power of χ_η" automatically. The content of the theorem is therefore the projective agreement (the relative phases
   of the monomial matrices, i on the fixed line against the swap), the exponent 21, and the resulting central
   character (weight 3/2 allowed); and the Scope concedes the twist may be a convention of the homology generators and
   the hand a convention. The abstract ("Its symmetry is the multiplier of the weight-one theta triplet of Γ(4),
   twisted by a character of η") should be rewritten to say what is classical, what is automatic, and what is the
   paper's: a stated lift lands on χ_η²¹ ⊗ ρ_u, with the stated hand. The verification ledger confirms that formula in
   every detail, which is to the paper's credit — but it is a verification, not a derivation of a flavour symmetry.
2. **The chain after Theorem 6(2) is conditional on readings the paper itself grades as unverified.** Theorem 6(3),
   Theorem 24 and the whole fibre frame rest on M₁,₂ "as the weave's surface" (verified only through χ = 1/12), on
   lifts whose coherence over Aut⁺(F₂) is open, on an index formula "taken as stated in B1606 and not re-derived", and
   on three tagged inputs. A statement whose headline number is the dimension of a postulated triplet read through a
   chosen boundary domain should not be announced in the abstract as one of "four things we show". Either derive the
   index formula in the paper (Riemann–Roch on the fibre family, with the exact sequence the authors say is not
   shown), or demote Theorem 24 to a proposition stated as n(|Λ⁺| − 3) and drop "chiral index ±3" from the abstract.
3. **The physics vocabulary outruns the mathematics.** "A structural zero", "the masses factor through two defects",
   "the massless generation" and "the electron's zero" name exact linear algebra at one τ with no dynamics, no kinetic
   terms, no renormalisation, and a dictionary (singular values = masses, flat lines = hypercharges) that is itself an
   input. The scope notes say so; the abstract and the theorem names do not. Rename the objects by what they are (the
   Yukawa matrix of the ansatz, the null vector of the ansatz) and keep "mass", "electron" and "generation" for the
   dictionary paragraph.
4. **The negatives need their comparison class.** Theorem 27(2) (no residual subgroup reducing the mixing count reaches
   the CKM at 3σ) is a general feature of residual flavour symmetries, established by scans over finite groups a decade
   ago: Holthausen and Lim (arXiv:1306.4356) found that the abelian residuals of the groups that fit lepton mixing give
   only the Cabibbo angle, and Yao and Ding (Phys. Rev. D 92, 096010; arXiv:1505.03798) scanned finite groups up to
   order 2000 and found that residual symmetries cannot generate even the order of magnitude of the CKM elements beyond
   Cabibbo mixing. The footnote says "whether the statement for this particular group is already known is open"; the
   paper should position the result against those scans, where the answer for every finite group tried is the same as
   here. Census 30 refutes a model only the program uses (one Higgs, τ = ω, eighteen flat lines, canonical end
   condition), so it locates the boundary of the program, not of the grammar; say so in §7's opening rather than in a
   scope note.
5. **The principle does no work and the paper should stop implying it might.** PF1–PF3 → GM1–GM5 is declared a reading;
   the commutator reading of tr[LR,RL] = −2 is a choice of words about SL(2,ℤ)′; the seed theorem is a reconstruction
   of a sector chosen before the axioms (disclosed). Everything proved is a statement about SL(2,ℤ), B₃ and the theta
   constants. Sections 1–2 (principle), 8 and 10, and the Reading boxes, belong in a separate essay; a journal version
   should begin at the grammar as a definition.
6. **Verifiability is real but incomplete.** The record is public and the locks pass in a fresh clone (ledger). But
   reference [2] has no URL or DOI, `make verify` is "planned and not built", the archival snapshot is promised for
   submission, and sm:B1516 is cited as if it were on main. A referee without the clone can check none of Table 2.
   Build the one-command verification, add the URL and a tagged release, and move the Table 2 scripts into the paper's
   own tree so that the paper is checkable from its archive alone.
7. **State what the "parallel lines" are.** Section 9 says the cross-checks are "internal to the program, not external
   review", which is honest, but the record's commit log describes the reviewing lines as seats and rules that no seat
   or AI is credited in the paper. If the lines are language-model sessions, the methods section must say so: journals
   require an AI-use statement, and a reader weighs "reproduced in independently written code" differently when the
   independent author is an instance of the same model.
8. **Theorem 22's proof should close the sign argument.** The step "the two tangent directions agree, so r tends to a
   positive number" needs one sentence: for s sufficiently negative the argument of dz/ds along [s, s+ℓ] varies by less
   than π, so the continued square root takes the principal branch of a ratio that tends to a positive number. The
   numerics (eight threads, 24 start points, ratio +(cz+d) every time) support the claim; the proof as written does not
   quite deliver it.

## Minor corrections and presentation

All of these are in the Draft 3 PDF; the ones marked ✱ were still in the Draft 4 sources in the repository at fe25f7e.

| Where | Problem | Fix |
| --- | --- | --- |
| §4, first paragraph ✱ | "(Theorem efthm:theta)": in sections/s04_modular.tex line 9 the \r of \ref became a carriage return | restore \ref{thm:theta} |
| Abstract vs Theorem 6 ✱ | abstract says the triplet is "proved to word length six"; Theorem 6 says parts (1)–(2) are theorems for every word, checked exactly to length six | make the abstract match the theorem |
| Prop. 15 ✱ | "at the puncture,, so" | one comma |
| Table 2 | the lock column overflows the right margin and is cut | p-column or \small |
| Table 1 | "τ = ω with the eighteen flat lines" and "the modulus τ = ω and the eighteen flat lines" are two rows for one input; "the end condition at the puncture" and "the canonical end condition … choice of canonical horocycle" overlap | merge; then reconcile the row count with the price "four axioms and nine irreducible identifications" quoted in Figure 1 — Table 1 has twenty rows |
| §2, Theorem 2 scope ✱ | "every state remains (758 to word length 12)" — 758 is the GENESIS census 2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 340, not the 745 primitive cyclic words up to rotation | define "state" or cite the census |
| §2 ✱ | B1516 is cited as an arc of the record, but it lives on the SM seat's branch (sm:B1516), not under frontier/ | cite with the seat prefix, or re-derive the 168-matrix check on main |
| Reference [2] ✱ | no URL, no DOI, snapshot promised "at submission" | add the repository URL and a tagged release before circulation |
| App. B | "checks/cusp law.py" typeset with a space; make verify "planned and not built" | \texttt{} with the underscore; build the target |
| Census 31 | "escape rate" undefined; the record's estimator is (1/n) log‖Xₙ‖ at first passage of 10⁶⁰, which is biased upward by about 1% at p = ½ | define it; say "Lyapunov exponent"; note it is half the hyperbolic drift |
| Census 32(2),(3) | "coherence" and "phase-one coherence" undefined in the paper | define |∫ψ ds|/∫|ψ|ds over one period, on the threads with #L ≡ #R (mod 4) |
| Census 32(2) | "−0.269 ± 0.083 (3.2 standard errors), slower than a random phase would give (−½)": 3.2σ is the distance from 0; the distance from −½ is 2.8σ | state both, and say the error bar is OLS over threads treated as independent |
| Theorem 9(2) vs Appendix A | parity-line labels (+,−), (−,+), (−,−) assume the column-vector convention; Appendix A fixes row vectors, under which L fixes (−,+) | state the convention once (see ledger) |
| Theorem 22 proof | the sign step (Major point 8) | one sentence on the branch |
| Prop. 13 | the identity Σρ_r²℘(z_r) = 0 is proved by a two-line computation with the half-period values (ledger) | give the proof instead of a numerical residual |
| Figure 2 | illustrates the identity torsion = ab | a sentence does the same; the caption's "144 → 1" overstates |
| Prop. 29, Census 30 | a "compiled verdict" and a scoreboard are not a proposition and a law | label them Verdict and Scoreboard, or move to §9 |
| Thm 26 | standard topology (χ of an odd-dimensional manifold with torus boundary) presented as a theorem of the paper | a lemma with a citation |
| §7.5 | the data value 3.14 is quoted without its uncertainty; m_s alone moves it between 2.9 and 3.4 | quote the error |
| §5.3, Prop. 16 and Census 25 | "the first generation's lift" is used with numbers (0.03–0.07, 0.24–0.41) that have no displayed formula | display the formula for the light mass in terms of D and E |
| Vocabulary | threads, weave, clock, tick, hand, defect, arena, side, read-out, dictionary, seats, arcs, locks, scoreboards, tribunal | a glossary, or standard names (hyperbolic class, modular group, …) in a journal version |
| Length | 38 pages, of which Sections 1, 8, 9, 10, the Reading boxes and Appendix C are program narrative | a journal version of ~15 pages with the exact statements; the rest as a supplement |

## Verdict and what would change it

Major revision; as a physics research article, reject. Correctness is not the issue: thirty-odd independent checks,
from polynomial identities to an eight-digit constant, all agree with the paper, and the record behind it is public and
passes its locks. The issue is that the paper has no result outside the program's own frame, and its abstract and
theorem titles say more than its scope notes allow.

What would make it publishable, by venue:

- **A mathematical note (10–12 pages).** Keep Theorem 20 with its symmetric form and the cubic; Lemma 21 and Theorem
  22 with a closed sign argument; the exponent 21 of Theorem 9 stated as a computation of a specific lift, with the
  convention fixed; Prop. 13 with its two-line proof; and Census 32(1) as a numerical check of equidistribution on f.
  Drop the principle, the frames, the index, the negatives and the Readings. Before submitting, check whether Theorem
  20 is a known quaternionic determinant identity.
- **A physics paper.** None exists here yet, and the authors say so. It would need a frame shown to meet the demands of
  Proposition 29 and at least one number fixed by it; the paper's own Table 1 says what would discharge each input.
- **A program report on the arXiv.** The present paper with the minor corrections, the AI-use statement, the URL and a
  tagged snapshot, Table 1 deduplicated and reconciled with the "4 + 9" price, and the abstract rewritten to the scope
  notes' level. It is unusually honest for its genre, and that is worth preserving as is.

Sources: Huang and Zhou 2021, running masses at M_Z (arXiv:2009.04851) · Yao and Ding 2015, lepton and quark mixing
from finite flavour symmetries (arXiv:1505.03798) · Holthausen and Lim 2013, quark and lepton mixing from a common
discrete symmetry (arXiv:1306.4356) · the record at commit fe25f7e · the checking scripts: `checks/check1_identities.py`,
`checks/check2_representation.py`, `checks/check3_motion.py`, `checks/check3b_escape.py`, `checks/check4_dims.py`.

## Addendum — what the structure can and cannot become (fresh eyes, 17 Oct)

No Standard Model number can be derived from this structure, and the reason can now be stated as a theorem-shaped
negative rather than a scoreboard: the grammar's triplet admits exactly two parameter-free Yukawa models, and both are
excluded for every τ.

### The parameter-free models are excluded everywhere

On the ruled branch with the modular-flavour ansatz (fields in T or T̄, Higgs a singlet, couplings vector-valued modular
forms for ρ), the number of free coefficients in a sector is dim M_k of the relevant tensor. Computed with the same
machinery that reproduced Theorem 9(3):

| Coupling | Weights allowed | dim M_k (k ascending) |
| --- | --- | --- |
| L, R both in T: M_k(ρ̄⊗ρ̄) | k odd | k=1: 1 (symmetric) · k=3: 2 (1 sym + 1 antisym) · k=5: 4 (3+1) · k=7: 5 (3+2) |
| L in T, R in T̄: M_k(ρ̄⊗ρ) | k even | k=0: 1 (the identity) · k=2: 2 · k=4: 4 · k=6: 5 |

The weight-0 form is the identity: three degenerate masses. The weight-1 form is unique and has a closed form,

    Y_1(τ) ∝ ( 0     θ₄²   θ₃² )
             ( θ₄²   0     θ₂² )
             ( θ₃²   θ₂²   0   )

— the theta triplet placed on the three off-diagonal pairs, diagonal forced to zero by the η-twist. Its mass ratios are
functions of τ alone: (m₁, m₂, m₃)/m₃ = (½, ½, 1) at ω, (φ⁻², φ⁻¹, 1) at i (the golden ratio), and (≈4e^{−π Im τ/2},
→1, 1) toward the cusp. m₂/m₃ ≥ ½ for every τ, with equality at ω, against 0.0037, 0.019 and 0.059 for the up, down and
lepton sectors. This is a theorem, not a scan: for any complex symmetric 3×3 matrix Y with zero diagonal, s₂ ≥ s₃/2.
Proof: let Y⁺ be the matrix of absolute values; ‖Yx‖ ≤ ‖Y⁺|x|‖, so s₃(Y) ≤ μ, the Perron eigenvalue of Y⁺. Y⁺ is real
symmetric with zero trace and determinant 2|abc| ≥ 0, so its other two eigenvalues are ≤ 0 and sum to −μ, whence μ² ≤
(2/3)·tr(Y⁺²) = (4/3)N with N = |a|²+|b|²+|c|². Then s₂² ≥ (tr(Y†Y) − s₃²)/2 = N − s₃²/2 ≥ N/3 ≥ s₃²/4. Equality needs
|a| = |b| = |c|, which the theta constants satisfy exactly at ω (300,000 random matrices: minimum ratio 0.5011; the
theta matrix at ω: ½). The same ½ is the floor Theorem 12(2) finds for real Higgs directions in the fibre frame (m ∈
[½, 1]), so the bound is a property of the grammar's parameter-free sector in both frames on record, not of one
ansatz. As a Majorana neutrino texture it is bimaximal: θ₂₃ = 45°, θ₁₃ = 0 exactly on Re τ = ½ (there θ₄² = conj θ₃², a
μ–τ reflection) and below 1° elsewhere, θ₁₂ ≈ 45°, inverted ordering with m₁/m₂ → 1 and m₃/m₂ ≈ 10⁻² near Im τ ≈ 3.5.
That texture was studied twenty years ago and dies on θ₁₂ and θ₁₃ unless charged-lepton corrections of Cabibbo size
are added by hand. So N5 (one Higgs at ω) is one point of a negative that holds for every τ: nothing with zero free
numbers survives.

### The first fittable model does not reach the quarks either

At weight 3 each sector has one complex coefficient: M_u = Y_s + r_u Y_a, M_d = Y_s + r_d Y_a with τ shared, six real
parameters against eight quark observables (four mass ratios, |V_us|, |V_cb|, |V_ub|, J). A 400-start Nelder–Mead fit
(`checks/check7_weight3_quarks.py`) bottoms out at χ² ≈ 3.8·10³, with m_u/m_t and m_s/m_b off by factors of 400 and 50.
The forms carry one small parameter, θ₂²/θ₃² ~ |q|^{1/4}, and θ₃ ≈ θ₄ at the cusp, so the spectra are (ε,1,1) or
(ε,ε,1), never 1:ε:ε². The grammar's triplet starts to fit only from weight 5 (four coefficients per sector), which is
ordinary modular-flavour model building with free O(1) numbers. That is the whole content of "0 of 19", now located:
the structure fixes textures; every value is a coefficient.

### Two things the paper proves that are classical, and one that touches physics

- Theorem 22 is the Dedekind–Rademacher formula. For a word γ in L and R, #L − #R = Ψ(γ), the Rademacher function
  (checked on nine words), and the multiplier of η⁶ is e^{iπΨ/2} = i^{#L−#R}. Ghys (2006, the paper's own [13])
  identifies Ψ(γ) with the linking number of the closed geodesic with the trefoil, and Atiyah (Math. Ann. 278, 1987)
  with the η-invariant / Hirzebruch signature defect of the torus bundle of γ — the thread's own mapping torus. So the
  monodromy of the matter amplitude along a thread is the global-anomaly phase of the thread's bundle, ℤ₄-valued, and
  the coherent quarter are the bundles with trivial phase. That is the one place the "motion" meets a physical
  quantity; it should be cited as such.
- D has a closed form in the Rogers dilogarithm L: on the imaginary axis D = (2/π)(θ₂²θ₄²/θ₃⁶)·L′(λ), λ = θ₂⁴/θ₃⁴ (off
  the axis the paper's log|·| version), and D(ω) = 0 because λ(ω) = e^{iπ/3} — the shape parameter of the
  figure-eight's regular ideal tetrahedra, where the Bloch–Wigner dilogarithm is maximal. D is not a Maass form (the
  weight −1 Laplacian ratio varies from 9.4 to 13.8 across five points), so the wave side of Census 32 is a genuine
  spectral expansion, not an eigenvalue.
- The one miss of N5, (m_μ/m_τ)/(m_s/m_b) = 3.14, is the Georgi–Jarlskog Clebsch 3: in every known realisation it
  comes from a Higgs component charged under colour (the 45 of SU(5), the (15,2,2) of Pati–Salam). No flavour symmetry
  supplies it, so the record's "gauge three", graded a selection, has to enter the Yukawa coupling itself; the flavour
  three cannot produce this ratio. Likewise Theorem 12(4), V = 1 ⊕ U(2) with one Higgs, is the one-bidoublet
  degeneracy of left–right symmetric models: S ∈ M₂(ℂ) is a bidoublet and S̃ = ϵS̄ϵᵀ its conjugate, so the three
  readings of the up sector in Census 30 are the standard LR Yukawa structure. Naming the objects imports the known
  results.

### Where physics could still come from, honestly ranked

1. Magnetized tori: the only setting where Yukawas are computed rather than fitted. Find the flux and Wilson-line
   assignment on T² or T²/ℤ₂ whose ℤ₂-even zero modes carry exactly ρ with its η-twist (Kobayashi–Tamba [25]; Kikuchi,
   Kobayashi, Otsuka, Takada, Uchida 2020–21). If one exists, the three-point overlaps are theta functions with no free
   coefficients beyond τ, the fluxes and the Wilson lines, and the question becomes whether any discrete choice fits — a
   finite search, and a real result either way.
2. A new finite modular model: ρ is not the S₄′ triplet of the literature (lowest triplet form at weight 7/2, allowed
   weights 3/2 mod 2, zero diagonal at weight 1, θ₁₃ = 0 on Re τ = ½). Its textures at weights 5–7 are publishable in
   the modular-flavour venue as a new class, with the usual honesty that the O(1) coefficients are fitted.
3. The cusp, not ω: the program's own cusp law D ∝ q·Im τ gives e^{−π Im τ} ≈ m_e/m_τ at Im τ ≈ 2.6 and the weight-1
   ratio m₁/m₃ ≈ 4e^{−π Im τ/2}. If any first-generation number ever comes out of this structure it comes out near the
   cusp. Retiring τ = ω was the right call; the census should be redone at Im τ ∈ [2, 4] before any further negative is
   sealed.

Scripts: `checks/check5_yukawa_dims.py` (the dimension table), `checks/check6_minimal_model.py` (the weight-1 form, its
scan and the closed form), `checks/check7_weight3_quarks.py` (the weight-3 fit).
