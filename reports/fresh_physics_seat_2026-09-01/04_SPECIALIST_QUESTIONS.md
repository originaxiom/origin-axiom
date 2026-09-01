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
**Status: CLOSED — by the record itself, after this list was first written.** B1221
(2026-08-31) ran the decisive computation the prior-art dossier isolated: the ℤ₆ kernel is
a property of the (algebra, representation) pair — computed from the 27's content alone,
SU(5) appearing nowhere, MB12 controls discriminating (72 and 18 on other content) — so it
is obtained identically on the chains that never enter SU(5). **Verdict KNOWN** (the
dossier's Entry 4 is marked so): path-independence *explains* the 1980 result. My PARTIAL
was the right lean; the record finished it.

## Quantum topology / quantum modularity

**Q4. Arithmeticity of Kashaev subleading coefficients for 4₁.**
Precise form: the asymptotic expansion of the Kashaev invariant ⟨4₁⟩_N has the form
N^{3/2} e^{N·Vol/2π} · 3^{−1/4} · (1 + Σ_k c_k (2πi/N)^k) with c_k in the trace field
ℚ(√−3) (even k picking up rational·π-powers). Is this arithmeticity — including the
3^{−1/4} = |disc|^{−1/4} unit — already established by Ohtsuki's asymptotic-expansion
papers and/or Garoufalidis–Zagier quantum modularity (where the 4₁ expansion is the
worked example)?
**Status: CLOSED-AS-KNOWN-ADJACENT — verified on this bench by reading the source.**
I obtained and read Garoufalidis–Zagier ("Knots, perturbative series and quantum
modularity") directly. It contains, explicitly for 4₁: **A(0) = 3^{−1/4}** as the leading
unit, and the full perturbative series **Φ(4₁)(h) with coefficients in
ζ₈·δ^{−1/2}·ℚ(√−3)[[h]]** — i.e. trace-field arithmeticity of the subleading coefficients,
including the |disc|^{−1/4} unit, is in the published literature. The repo's B1120/B1133
"make-or-break POSITIVE" is therefore a **rediscovery/extension** (their specific
C₁, C₂, C₃, C₄ rational values and the parity law are finer data than GZ print, but the
arithmeticity *claim* is GZ's). Notably, THE_FRAMEWORK's adelic section cites GZ, but
B1120/B1133's own FINDINGS do not diff against it locally — an E37-shaped citation gap
worth one addendum before any external use. [computed-here: text extraction; grade —
read-directly, not from memory.]

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
| Q4′ (ℤ₆ mechanism classical) | **closed — KNOWN, by the record's own B1221** | verified-in-repo |
| Q4 (Kashaev arithmeticity vs. GZ) | **closed — KNOWN-adjacent, GZ read directly** | read-directly |
| Q6 (observable content) | closed against the record; open as challenge | verified-in-repo |
| Q8 (amphichirality forced) | closed | argued + computed-here |
| Q3 (registerability rule novel?) | **open — highest value** (dossier entries 2–3 unsearched) | — |
| Q5 (Weil-rep novelty) | open | — |
| Q7 (generation carrier) | open, with a stated physics prior | opinion |

## Cross-reference: the record's own specialist queue (found on the second pass)

`docs/SPECIALIST_SEND_QUEUE.md` (B1179) holds six bounded outward questions, all on owner
HOLD. Overlaps with mine: their **Q1 (SEAM-A Gate 2 — Andersen–Hansen cusped extension /
arithmetic-CS finite-phase→Vol)** is the record's ★★★★ and does not appear on my list
because it is genuinely NEEDS-SPECIALIST and already sharply posed (B1156: the a-priori
MISMATCH refuted, the Arakelov row carries Vol as the Borel regulator — I read and endorse
the framing). Their Q3 (the B491 seam form) neighbors my Q5. One question the queue no
longer needs: the Lee tangential-base-point question was closed *internally* by B1209
(the torsor is trivial for m004 — |a₁| = 1 at all four ideal points), which is exactly the
kind of self-specialization the seed asked me to attempt and the record performed on its
own. My net addition to their queue after closures: **Q3 (registerability termination —
prior-art entries 2–3), Q5 (finite Weil/theta novelty), Q7 (generation carrier as
index-theoretic data)** — three questions, none duplicating theirs.
