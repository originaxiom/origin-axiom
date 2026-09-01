# Specialist questions — stated repo-free, with the ones I closed marked — 2026-09-01

*Each question is phrased so the named expert could answer without reading this repository.
"CLOSED-HERE" = I answered it on this bench (grade given). "PARTIAL" = narrowed. "OPEN" =
genuinely needs the expert.*

---

## Number theory / arithmetic groups

**Q1. Which SL(2,𝔽_q) arise as quotients of the figure-eight knot group, and is the
2T/2I asymmetry a theorem?**
Precise form: π₁ of the figure-eight complement (⟨a,b | a³b·a⁻¹b⁻²·a⁻¹b⟩ up to
presentation) surjects onto SL(2,3) (48 ways) and onto SL(2,7) (2688 ways), but has no
surjection onto SL(2,5). Is the SL(2,5) refusal explained by a congruence/level argument
in the Bianchi group PSL(2,ℤ[ω]) (5 inert in ℚ(√−3)), and does it persist for all q with
(q inert, q ≡ ±2 mod 5)-type conditions?
**Status: PARTIAL, CLOSED-HERE at the computational level** [computed-here: the counts
above; also both m004 and its nonorientable parent m000 give (72 homs, 48 surj) onto
SL(2,3)]. The *mechanism* (inertness of 5 vs. ramification of 3 as the actual cause) is
the open half — a Bianchi-groups person answers this in a day.

**Q2. Is the census-family observation just commensurability?**
Precise form: the 14 orientable cusped census manifolds with tetrahedron shape field
ℚ(√−3) all have volume an integer multiple of the Gieseking volume. Are all 14
commensurable with PGL(2,ℤ[ω])?
**Status: CLOSED-HERE** [computed-here: the integer multiples; argued + cited: shape
field = invariant trace field for cusped manifolds (Neumann–Reid), cusped + arithmetic ⇒
commensurability class determined by the field; hence yes]. Residual for an expert:
confirm each of the 14 is arithmetic (finite check).

**Q3′. Reid rediscovery.** The record's "exactly one property separates m004 in its
family: H₁ = ℤ" is Reid's theorem (4₁ is the unique arithmetic knot) in census form.
**Status: CLOSED-HERE** [cited: A. Reid, "Arithmeticity of knot complements," J. LMS 1991;
verified consistent with the census computation].

## Lie theory / representation theory

**Q3. Is the "registerability termination" selection rule known?**
Precise form: define, for a semisimple subalgebra chain descending from e₆ by successive
centralizers of semisimple elements (Borel–de Siebenthal steps), the property that the
27 restricts with its complex/chiral structure intact ("registerable"). Claim under test:
every maximal registerable descent chain terminates at su(3)⊕su(2)⊕u(1)³, and all six
natural selection functions land there. Is this equivalent to a known maximality/
chirality-preservation statement in the E₆ GUT or trinification literature (e.g. the
standard "E₆ → SM preserving complex 27" folklore), or is it new?
**Status: OPEN — the single most valuable expert question in the record.** If known, P3's
Movement I loses its best non-classical piece; if new, it is the theorem to lead with.

**Q4′. The ℤ₆ global form.** Is the derivation of Γ = ℤ₆ for [SU(3)×SU(2)×U(1)]/Γ from
an E₆ embedding a known result (cf. Tong, "Line operators in the Standard Model"; Hucks;
the global-form literature)? The fact that E₆ (simply connected, center ℤ₃) fixes the
global form of its unbroken subgroup is group theory; which Γ results is a computation
someone has likely done.
**Status: PARTIAL** [argued: the mechanism is classical; the specific attribution needs a
literature hour, not an expert].

## Quantum topology / quantum modularity

**Q4. Arithmeticity of Kashaev subleading coefficients for 4₁.**
Precise form: the asymptotic expansion of the Kashaev invariant ⟨4₁⟩_N has the form
N^{3/2} e^{N·Vol/2π} · 3^{−1/4} · (1 + Σ_k c_k (2πi/N)^k) with c_k in the trace field
ℚ(√−3) (even k picking up rational·π-powers). Is this arithmeticity — including the
3^{−1/4} = |disc|^{−1/4} unit — already established by Ohtsuki's asymptotic-expansion
papers and/or Garoufalidis–Zagier quantum modularity (where the 4₁ expansion is the
worked example)?
**Status: PARTIAL** [cited-from-memory, MUST-VERIFY: 3^{−1/4} appears in the
Garoufalidis–Zagier treatment of 4₁; the repo's B1120/B1133 should cite and diff against
it before any novelty claim]. Expert: anyone in quantum modularity, one afternoon.

**Q5. The level-15 theta/Weil computations (seam forms, P56–P68).**
Precise form: on the 15-dimensional Weil representation of SL(2,ℤ/15) with the
half-characteristic twist ζ₁₅^{−j(j+1)/2}, are the exact trace identities (the shifted
trace formula with domain det(γ−I) invertible; the character-gated root-of-unity law) an
instance of the standard finite-metaplectic character formula (Gérardin; Prasad), and is
the "seam" invariant a known theta-multiplier pairing?
**Status: OPEN** [the computations are exact and locked; their novelty status is not].
Expert: finite Weil representations / theta functions.

## Particle theory

**Q6. Given: one 27 of E₆ with trinification anatomy, anomaly-forced hypercharge, ℤ₆
global form, real form E₆(−26), no generations, no Yukawas, no scale. Is there ANY
observable that distinguishes this package from the generic E₆-GUT kinematic skeleton?**
Phrased for a phenomenologist: if two theorists hand you (i) standard E₆ trinification
kinematics and (ii) this record's forced skeleton, is there any measurement — collider,
cosmological, precision — whose expected outcome differs? My reading of the record's own
value-negatives says no.
**Status: CLOSED-HERE at the level of the record** [verified-in-repo: ten sealed value
negatives; zero of 24 SM parameters reduced; the type law], **OPEN as a challenge**: a
phenomenologist inventing such an observable would falsify my "no observable content"
finding and hand the programme its first physics claim.

**Q7. The generation obstruction.**
Precise form: the trace field being degree 2 forbids forced multiplicity 3 through the
seven routes tried (B298); the cubic-carrier conjecture (a degree-3 field must enter for
three generations) is the standing direction. Question: in known constructions (heterotic
E₆, F-theory), what mathematical object carries the generation count, and is there a
principled reason a *quadratic*-field object cannot (e.g. Euler characteristics /
index-theorem counts are geometric, not trace-field, data)?
**Status: OPEN** [my own physics prior: generation count in every known derivation is
index-theoretic (χ/2 in Calabi–Yau compactification), i.e. it belongs to a *bulk* the
record does not have — which would make the obstruction structural, not arithmetic.
Stated as opinion, not result]. Expert: string phenomenologist.

## 3-manifold topology

**Q8. (Closed.) Are orientation double covers always amphichiral?**
Yes: the deck involution reverses orientation; Mostow makes it an isometry.
**Status: CLOSED-HERE** [argued; empirically 40/40, base rate 7/300 — computed-here].
This retires the census experiment and reframes the record's amphichirality motif.

---

## Summary of what this seat closed

| Q | status | grade |
|---|---|---|
| Q1 (2T/2I quotient asymmetry) | computational half closed; mechanism open | computed-here |
| Q2 (family = commensurability class) | closed | computed-here + cited |
| Q3′ (Reid rediscovery) | closed | cited |
| Q4′ (ℤ₆ mechanism classical) | narrowed to literature-hour | argued |
| Q6 (observable content) | closed against the record; open as challenge | verified-in-repo |
| Q8 (amphichirality forced) | closed | argued + computed-here |
| Q3 (registerability rule novel?) | **open — highest value** | — |
| Q4 (Kashaev arithmeticity vs. GZ) | open, must-verify before claims | cited-from-memory |
| Q5 (Weil-rep novelty) | open | — |
| Q7 (generation carrier) | open, with a stated physics prior | opinion |
