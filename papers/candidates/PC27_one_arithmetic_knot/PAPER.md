# One Arithmetic Knot: a self-policed program, its forced arithmetic core, and a computed account of where it stops

**Origin Axiom Program.** Internal working paper (candidate). 2026-07-21.

> **Status.** Paper candidate — `METHODS_PAPER / NEGATIVE_RESULT / SURVEY_MAP`. All verification here
> is internal (owner + AI seats; see `PROVENANCE.md §0`). No result in this document is promoted to
> `CLAIMS.md`; no Standard-Model quantity is claimed. This is a coherent evidence cluster worth
> auditing, not a publication-ready or externally-reviewed result.

---

## Abstract

The Origin Axiom program studies a single mathematical object — the figure-eight knot complement
`m004` (equivalently the once-punctured-torus bundle with monodromy the cat map, and its metallic
trace-map tower) — together with the structure of an *observer* coupled to it. We report the honest
state of the program at the point where its physics-facing ambitions have been closed by its own
methods. Three things are established. **(1) A forced arithmetic core.** The invariant trace field
of `m004` is `ℚ(√−3)`, and `m004` is the unique arithmetic knot; the program's measurement structure
is a genuinely-forced Klein-four `V₄` seam with a bounded, discrete menu of observers; and the Born
rule's *form* is forced while its *quantum content* lives in field extensions the object does not
force. **(2) A methodology.** The program's transferable contribution is a base-rate / look-elsewhere
discipline that it turned inward on its own flagship structural claim, computing that claim down to
genericity and closing the bridge to physics by computation rather than defending it. **(3) Two
closing negatives.** The *object-level observer* — a single-level non-abelian Bianchi analogue of a
Bost–Connes symmetry-breaking system — is obstructed for two independent reasons; and *zero* of the
Standard Model's parameters are reduced by the framework, for three independent reasons. We state
each result at its true strength with its honest bound. The deliverable is a self-policed body of
mathematics about one arithmetic knot and a rigorous, computed account of where — and why — it stops.

**Keywords.** figure-eight knot complement; arithmetic hyperbolic 3-manifold; `ℚ(√−3)`; Bianchi
group; congruence subgroup; Bost–Connes system; Born rule; base-rate methodology; negative results.

---

## 1. Introduction

### 1.1 The object and the coupling frame

The object of study is `m004`, the complement of the figure-eight knot `4₁` in `S³`. It is a
once-cusped hyperbolic 3-manifold of minimal volume `2.0298832…`, a once-punctured-torus bundle whose
monodromy is (conjugate to) the cat map `[[2,1],[1,1]]`, and — by Reid's theorem — the *unique*
arithmetic knot complement. Its invariant trace field is `ℚ(√−3)`; its fundamental group is a
subgroup of the Bianchi group `PSL(2, 𝒪₃)`, `𝒪₃ = ℤ[ω]` the Eisenstein integers.

The program's organizing thesis — the *observer-coupling* frame — is that the object supplies
*structure* (relations, symmetries, arithmetic) but never a *value*; every value, orientation,
choice, or "closing" belongs to an observer coupled to the object, and is provably a non-canonical
free choice. This paper does not argue that thesis afresh; it reports what the object forces under
it, and where the coupling to physics is closed.

### 1.2 The discipline

The methodological spine is a **base-rate / look-elsewhere firewall**. A near-hit between an
object-invariant and a target number is treated as worthless unless it beats the look-elsewhere
rate: a rich object's spectrum near-hits *any* dimensionless ratio, so a match is evidence only when
the search width and height ceiling forbid a trivial self-rational from masquerading. Symmetrically,
an unearned "no match" is treated as as bad as numerology: negatives must be *computed*, not
asserted. This firewall is the paper's real contribution (§4); it is what makes the negative results
(§5) credible.

### 1.3 Contribution and structure

We establish a forced arithmetic core (§3), state the methodology as a transferable discipline (§4),
and prove two closing negatives (§5): the object-level observer is obstructed, and the framework
reduces zero Standard-Model parameters. §6 states the disposition. Throughout, each claim is tagged
at its true strength, with its honest bound, and cross-referenced to the internal computational
record (the `B###` banked-result numbers) which serves as the reproducibility ledger (Appendix A).

---

## 2. The forced arithmetic core

We record the results that survive the firewall.

### 2.1 The atom

**Result 2.1 (the atom).** The invariant trace field of `m004` is `ℚ(√−3)`, and `m004` is the unique
arithmetic knot complement (Reid 1991). This double distinction — arithmetic and a knot — forces the
seam field `ℚ(√−3)`.

*Support.* Reid's uniqueness is cited external mathematics; the trace-field identity is verified
in-repo via Neumann–Reid (shape field = invariant trace field; the ideal tetrahedron shape is
`e^{iπ/3}`). *(Record: B266.)*

**Honest bound.** The much-remarked resonance of `ℚ(√−3)` with `E₆`-type structure is a property of
the *field*, not of the knot's homotopy type: the sister manifold `m003` shares `ℚ(√−3)` (and the
minimal volume) but is not a knot (`H₁ = ℤ/5 ⊕ ℤ`). Thus the atom is "a field distinguished by a
knot," and it is (per §4.2) the *only* object-specific content that survives the flagship self-audit.

### 2.2 The measurement torsor

**Result 2.2 (the `V₄` seam).** The object's own intrinsic arithmetic (trace field, Alexander
polynomial, `A`-polynomial branch locus) forces exactly three quadratic fields, the three involutions
of one biquadratic field: *being* `ℚ(√−3)`, *hearing* `ℚ(√5)`, and *meeting* `ℚ(√−15) = ℚ(√−3·√5)`.
Their Galois group is `V₄ = C₂×C₂`. No fourth face is forced: adjoining the "stage" field `ℚ(√−7)`
does not refine `V₄` but explodes it to `(ℤ/2)³`, so `ℚ(√−7)` is a fiber-functor stage, not a face.
*(Record: B701/B704/B730.)*

**Result 2.3 (the bounded observer menu).** The menu of observers — the torsor of arithmetic-Galois
symmetry-breakings of the object's conjugation on its congruence quotients `PSL(2, 𝒪₃/n)` — is a
bounded, depth-independent, discrete `𝔽₂`-vector space of rank ≤ 3: a dimension-zero set of at most
eight points. `Aut(𝒪₃) = Gal(ℚ(√−3)/ℚ) = ℤ/2` is a single global involution that reduces to the
Frobenius at *every* inert prime simultaneously, so the observer bit does not grow with the number of
primes. Consequently, observers are *constructible* (specify finitely many bits) but *not
cherry-pickable* to encode continuous data. *(Record: B733; two-seat consensus.)*

**Honest bound.** The full automorphism group of `PSL(2, 𝒪₃/n)` does grow with depth (e.g.
`Out(PSL(2,𝒪₃/4)) = S₄`), but it decomposes as the conjugation bit lifted, plus a diagonal
`𝔽₂`-rank that *saturates* (the 2-adic sequence is `0,2,3,3,3,…`), plus an odd `ℤ/3` module
multiplicity. Even the full structure is bounded; it never approaches a continuum. The choice among
the ≤ 8 observers is provably free: no canonical torsor-isomorphism exists (the two golden irreps of
the relevant finite group are unitarity-unpointed while the modular-tensor-category torsor is
unitarity-pointed, obstructing a canonical identification). *(Record: B701 phase 2.)*

### 2.3 The congruence realization

**Result 2.4 (congruence at level `(8)`).** `Γ = π₁(m004) ⊂ PSL(2,𝒪₃)` has geometric index 12 and is
a *congruence* subgroup of level `(2)³ = (8)`: the `PSL`-image index (with the correct `SL`/`PSL`
center bookkeeping) is 6 at level `(2)`, 6 at level `(4)`, and reaches the geometric index 12 first
at level `(8)` (and stably thereafter). The single-level observer image in `G₈ = PSL(2,𝒪₃/(8))`
(order 30720, index 12) has order 2560. The conjugation bit `ω ↦ ω²` reduces mod `(2)` to the
`𝔽₄`-Frobenius, which swaps the two 5-cycle classes of `A₅ = PSL(2,𝔽₄)` — i.e. it induces the
*outer* automorphism `Out(A₅)` at the sister's level-`(2)` quotient. Hence the observer's `ℤ/2` swap
is realized concretely on both the abelian tower (as CM-inversion) and the non-abelian tower (as
`Out(A₅)`). *(Record: B734 (correcting B731); B732; B721.)*

**Honest bound.** Result 2.4 is *Serre-defying*: the congruence subgroup property fails for Bianchi
groups, so a congruence knot subgroup is non-generic. It was computed independently three times
in-sandbox but is flagged **pending external literature cross-check** before being treated as
textbook-settled. This result corrected an earlier internal conclusion of "non-congruence" that had
stopped the level-check one 2-adic power too shallow (logged as error class E22) — an instance of the
discipline correcting itself.

### 2.4 The Born-content ledger

**Result 2.5 (Born form and why-quadratic).** In the operator-algebra construction of the observer
(the object's tracial type-`II₁` factor + an external weight → type-`III` factor; measurement as
cooling through a `β = 1` symmetry breaking), the Born *form* `ω(P) = Tr(ρP)` is forced by Gleason's
theorem on the frame's own factors, and the *quadratic degree* of the probability is forced by the
order of the conjugation: `|ψ|² = ψ·c(ψ) = N_{ℂ/ℝ}(ψ)`, so `degree = |Gal(ℂ/ℝ)| = 2`. An order-3
swap would give a cubic norm — a live falsifier, not a fit. *(Record: B723/B725.)*

**Result 2.6 (the content ledger).** The Born data stratifies by arithmetic. The object supplies its
two *quadratic* fields as the classical probability content — *form* `ℚ(√−3)` (being) and non-uniform
*weights* `1 : φ²` native to `ℚ(√5)` (hearing). The *quantum* content is a set of *quartic*
extensions the object does not force: the interference phase `ζ₅ ∈ ℚ(ζ₅)` is imported, provably not
in the compositum of the two bare faces since `Gal(ℚ(ζ₅)/ℚ) = C₄ ≠ C₂×C₂ = Gal(ℚ(√−3,√5)/ℚ)`; the
amplitude field `ℚ(√(2+φ))` and associator field `ℚ(√φ)` are further distinct quartic types. A
PSLQ search over 33 Dehn-filling trace fields did not find `√(2+φ)` natively, and the coincidence
`D₄ = Isom(4₁)` was base-rate-killed. *(Record: B725–B729.)*

**Honest bound.** Result 2.6 is a *pattern*, not a derivation of quantum mechanics: the object
supplies classical probability content (its quadratics), while interference and phase live in
quartics it does not force (a golden-modular-tensor-category overlay). It is a structure of *what an
observer imports*, delimited exactly.

---

## 3. The methodology (the transferable contribution)

### 3.1 The base-rate firewall

The firewall (§1.2) is formalized as a two-sided gate. **Positive side:** a candidate identity between
an object-invariant `x` and a target `t` counts only if `x` is *algebraic of low height over a
predicted object field* and survives more digits than were used to find it (membership, base-rate
immune) — not merely `x ≈ t` (proximity, base-rate dead). **Negative side:** a "no match" counts only
if the *discriminating fact* is computed in-sandbox, never cited or asserted. The look-elsewhere rate
is quantified: the object's torsion/trace spectrum yields a factor-≈3 near-hit to *any* dimensionless
target at a rate of order a few per decade, so unforced near-hits carry ≈ zero information.

### 3.2 The flagship self-audit

The discipline was then turned on the program's own most-celebrated *structural* claim — that `E₆`
recurs, as if by design, across three faces (the McKay correspondence from the binary tetrahedral
group, the Lie/character-variety face, and the Cappelli–Itzykson–Zuber modular face). Applied
honestly, all three probes returned **generic**:

- The three faces are one canonically-linked ADE classification (a forced graph identity;
  `P(recurrence | one label) = 1` — there is no coincidence to price).
- `{E₆}` is the *only* exceptional label reachable over an imaginary-quadratic field (`2O` needs
  `√2`, `2I` needs `√5`, both real) — no birthday problem to overcome.
- Even the underlying surjection `π₁ ↠ 2T` is not knot-unique: several non-arithmetic knots surject
  as well; and the sister `m003` ties the field without being a knot.

After the audit, the only object-specific content standing is the atom (Result 2.1). *(Record: B727;
cross-verified independently.)* We regard this — *a program computing its own flagship down to
genericity and banking the deflation* — as the paper's central methodological result.

### 3.3 The honestly-closed bridge

The bridge from the object to the Standard Model's flavor sector is closed by computation at two
"rungs." At the field-membership rung, the flavor ratios are generic over the object's audible field
`ℚ(√5)` (no low-height algebraicity). At the structural rung, the object's arbitrariness is a
*discrete* `𝔽₂` seam while the Standard Model's is a *continuous* ~19-parameter moduli space — a
mismatch of both cardinality and dimension type, not a gap to be narrowed. *(Record: B685 terminal;
B706 no-match; two-seat.)*

---

## 4. The two closing negatives

Both results below were adversarially verified and independently reproduced across two seats.

### 4.1 The object-level observer is obstructed

**Result 4.1 (obstruction).** `m004`'s own single-level non-abelian Bianchi congruence observer — the
finite order-2560 image of `π₁(m004)` in `G₈` — does not carry a Bost–Connes-type `β = 1`
spontaneous-symmetry-breaking (SSB) with a symmetry-breaking Galois action. Two independent
obstructions:

1. *Finite ⇒ no phase transition.* A single congruence level is a finite group, hence a
   finite-dimensional C\*-dynamical system; the number of extremal `KMS_β` states is independent of
   `β` (Bratteli–Robinson), so there is no phase transition and no SSB. The `β = 1` breaking the
   observer requires *is* the simple pole of the Dedekind zeta `ζ_{ℚ(√−3)}(β)` at `β = 1` (residue
   `2πh/(w√|d|) = 2π/(6√3) ≈ 0.6046 > 0`), an infinite-tower object annihilated by any single-modulus
   truncation (a truncation is an entire Dirichlet polynomial, poleless).
2. *No Shimura route.* The canonical symmetry-breaking Galois action of the Connes–Marcolli /
   Ha–Paugam "fabulous states" is defined only via a Shimura variety's canonical model and CM
   reciprocity, which requires the symmetric space be Hermitian symmetric. The Bianchi symmetric
   space `H³ = SL(2,ℂ)/SU(2)` has odd real dimension 3, hence admits no invariant complex structure
   and is not Hermitian symmetric; `(Res_{K/ℚ}GL₂, H³)` is not a Shimura datum. The route cannot be
   posed.

Every *built* single-modulus SSB system in the literature (Bost–Connes; Connes–Marcolli–Ramachandran
over `ℚ(√−3)`, with `β = 1` breaking over `Gal(K^{ab}/K)`; Bruce's single-modulus systems, breaking
over an abelian ray-class group) is abelian / class-field and sees the *field* `ℚ(√−3)`, not the
non-abelian Bianchi holonomy — the field-vs-object catch, one level up. *(Record: B736 track P2;
converges with the independent group-theoretic angle, which finds the conjugation acts *generically*
on the knot's own observer.)*

**Honest bound.** We do *not* prove a non-existence theorem for an infinite non-abelian Bianchi–Hecke
system with a finite Galois symmetry-breaking; that object is not "single-level" and has no known
construction route (the natural one being provably blocked). The obstruction is stated for the
single-level ask, which is what the observer-as-congruence-structure motivates.

### 4.2 Zero Standard-Model parameters are reduced

**Result 4.2 (no-go).** The framework forces zero reductions of the Standard Model's free-parameter
count. Grading all 24 parameters (9 fermion masses; 3 CKM angles + 1 phase; 3 PMNS angles + 1 phase;
3 gauge couplings; Higgs mass and vev; `θ_QCD`; neutrino masses) against the banked record, each is
"nothing forced": no value is forced, no relation between two parameters is forced, and no discrete
constraint on any continuous parameter is forced. Every candidate reduction dies to one of three
independent, reinforcing obstructions:

1. *The equivariance wall.* The only monodromy-equivariant `ℂ`-linear intertwiner from the being
   sector (cat-map spectrum `{φ², φ⁻²}`, real, hyperbolic, off the unit circle) to the hearing sector
   (an order-10 element, unitary, on the unit circle) is `T = 0`, since the two spectra are disjoint
   (Sylvester). No linear channel transports a continuous quantity across the two faces — the exact
   mechanism a forced relation would require. *(Extends B650.)*
2. *Kind-mismatch.* The object's freedom is a discrete `𝔽₂` set; the flavor freedom is a continuous
   ~19-real moduli space. A finite set cannot impose a dimension-reducing algebraic relation on a
   continuous manifold; a PSLQ search over `ℚ(√5)` (height ≤ 10³) finds no low-height relation among
   the ratios either. *(B706.)*
3. *Bounded ceiling.* The observer space is a bounded rank-≤3 discrete set (Result 2.3); it cannot
   coordinatize a ~19-real moduli space. *(B733.)*

*(Record: B736 track P3; converges with the independent angle, which confirms the forced
being↔hearing lock is real but has no Standard-Model landing site — no gauge-sector alignment for the
finite group's classes/irreps to act on.)*

**Honest bound.** The ledger grades the *banked* record and the natural forced structures; it is not
an exhaustive scan of every conceivable mechanism. The one genuine "crack" — that the being↔hearing
lock is group-functorial rather than merely linear, so it is not *literally* killed by the linear
equivariance wall — was characterized and shown inert (no landing site), not swept aside.

---

## 5. Disposition

The Origin Axiom program is, honestly assessed, a self-policed body of pure mathematics about one
arithmetic knot and the structure of an observer coupled to it — not a road to the Standard Model.
What it forces is narrow, arithmetic, and robust: the atom `ℚ(√−3)` (the trace field of the unique
arithmetic knot); a genuinely-forced measurement torsor — the Klein-four `V₄` seam with its bounded,
discrete, dimension-zero menu of at most eight observers, realized in `m004`'s own congruence
arithmetic at level `(8)` with the conjugation bit `= Out(A₅)`; and a Born-content ledger in which
the object supplies its two classical quadratics while the quantum amplitude and phase are an
imported overlay it does not force. Its real methodological contribution is the base-rate /
look-elsewhere discipline it turned on its own flagship — computing the once-celebrated
`E₆`-across-three-faces structure down to genericity, and honestly closing the bridge to physics by
computation at the doors rather than defending it. The two closing computations seal the disposition:
the object-level observer as a `β = 1` symmetry-breaking system is obstructed (finite level ⇒ no
transition; the Bianchi space is not Hermitian ⇒ no Shimura route), and zero of the 24 Standard-Model
parameters are reduced (equivariance wall; kind-mismatch; bounded ceiling). The deliverable is
therefore exactly what the firewall permits and no more: beautiful, honest mathematics about one
object, and a rigorous, computed account of where — and why — it stops.

---

## Appendix A. Reproducibility ledger (internal record)

Each result is backed by a sealed, prereg'd, adversarially-verified banked arc with an exact lock
test in the canonical repository:

| Result | Banked arc(s) | Lock test |
|---|---|---|
| 2.1 atom | B266 (+ Reid 1991) | trace field `x²−x+1`, disc −3 |
| 2.2 `V₄` seam | B701, B704, B730 | `test_b730_faces_cosmos` |
| 2.3 bounded menu | B733 (two-seat) | `test_b733_observer_space` |
| 2.4 congruence `(8)` | B734 (corr. B731), B732, B721 | `test_b734_m004_congruence`, `test_b732_out_a5` |
| 2.5/2.6 Born ledger | B723, B725–B729 | `test_b725_born` … `test_b729_amplitude` |
| §3 methodology | B724, B727, B685, B706 | `test_b727_baserate` |
| 4.1 observer obstruction | B736 P2 | `test_b736_abc` |
| 4.2 parameter no-go | B736 P3 | `test_b736_abc` |

## Appendix B. External references (fetched / verified in-sandbox)

- A. W. Reid, *Arithmeticity of knot complements*, J. London Math. Soc. (1991) — `m004` the unique
  arithmetic knot.
- W. Neumann, A. Reid, *Arithmetic of hyperbolic manifolds* — invariant trace field = shape field.
- A. M. Gleason, *Measures on the closed subspaces of a Hilbert space* (1957) — the Born form.
- J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions…* (1995) — the
  BC system.
- A. Connes, M. Marcolli, N. Ramachandran, *KMS states and complex multiplication* (Selecta 2005) —
  the `β = 1` SSB over an imaginary-quadratic field; the observer property.
- C. Bruce, *C\*-algebras from actions of congruence monoids* (arXiv:1902.03521, IMRN 2021) —
  single-modulus systems, abelian ray-class breaking.
- P. Deligne, *Travaux de Shimura* / Shimura-datum axioms — Hermitian-symmetric requirement.
- O. Bratteli, D. Robinson, *Operator Algebras and Quantum Statistical Mechanics II* — finite-dim ⇒
  no phase transition.

*Firewall: the negative and the arithmetic only; no Standard-Model value is claimed; nothing here is
promoted to `CLAIMS.md`.*
