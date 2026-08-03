# W0d — THE QUANTUM SCOUT (seat cc3, 2026-07-17)

Structure-of-the-field scout for the SELECTION & QUANTUM-COCHAIN CAMPAIGN's D-A program
("the quantum cochain design"). Repo `/Users/dri/oa-seat-cc3/origin-axiom`
read-only throughout; nothing here touches it. One exploratory numeric
probe was run (`quantum_probe.py`, float64, same precision class as the
banked `su32_wrt.py` gate script) to attach concrete numbers to the
candidates — clearly marked SCOUT-GRADE, not a sealed wave-2 computation.
Every UNSURE tag below is load-bearing: this cell would rather under-claim
than hand wave 1 a wrong confident target.

---

## 0. Scope note: what "the classical 5" is being compared to

Per `PREREG_SCC.md` and the B662 record (`frontier/B662_successor_campaign/
cellH/FINDINGS_CELL.md`): H¹(D;27) = 5 on the golden (unbent) double D of
the figure-eight knot complement, with H⁰(D;27)=1, Z¹ dim 31. The classical
program's cochain machinery is honest group cohomology of π₁(D) (an
amalgam of two once-punctured-torus-bundle groups glued along the cusp
torus, 4 generators, one relator "LONG(a,b)LONG(c,d)" — cellH's basis
control) with coefficients in the 27 (an E6 module via the holonomy). The
cup product H¹×H¹→H²(D;27̄) fills the 5-dim H² (rank 5); scalar Massey
products are zero-with-full-indeterminacy or undefined (cellH: **the
Massey wall**, the fourth wall on `docs/LAW_MAP.md`'s list). "The stage" is
SU(3)₂ (κ=5, "the golden stage", `TERMINOLOGY.md`), 6 simple objects; "the
weld operator" W = ρ(RL), R=T, L=S⁻¹T⁻¹S in the modular representation of
S,T on the stage's 6-dim state space — this exact R,L convention is banked
verbatim in `papers/drafts/PC26_full_chain/PAPER.md` (Theorem 8.1's
closure theorem) and `frontier/B664_metallic_landscape/
METALLIC_LANDSCAPE_HANDOFF.md` ("the weld operator W(n) = R^{n−2}L on the
SU(3)₂ space"; the figure-eight case is n=3, W=RL). The hearing group is
2I×ℤ/3 (`frontier/B640_hearing_group/FINDINGS.md`); the Γ₅′-doublet
identification is `frontier/B662_successor_campaign/cellI/FINDINGS_CELL.md`
("the ear's hearing representation IS the Γ₅′-doublet 2̂′", exact character
equality on all 9 conjugacy classes of SL(2,5) = 2I).

---

## 1. THE RIGIDITY WALL, stated precisely

**Claim as sealed in the prereg:** Ocneanu rigidity — fusion/modular
categories admit no deformations; Davydov–Yetter H² and H³ vanish.

**What I can state with CONFIDENCE (general theory, not from the repo —
the repo has no prior discussion of Davydov–Yetter cohomology; a search
for "Ocneanu", "Davydov", "rigidity" across the repo found the phrase only
in an unrelated cell (`B429_bosonic_rigidity`, a different use of the word
"rigidity") and one direct citation of **Ocneanu's actual body of work**
in `frontier/B312_face_iv_houses_the_form/FINDINGS.md` line 63: "Ocneanu
(quantum subgroups / module categories over SU(2)ₖ)" — confirming Ocneanu's
relevant contribution in this repo's own citation trail is precisely
*module categories*, i.e. candidate (a) below, not the deformation theorem
per se):**

- For a fusion category C over an algebraically closed field of
  characteristic 0 (finite, semisimple, rigid monoidal, simple unit —
  SU(3)₂ qualifies, and being modular/ribbon only adds structure), there
  is a deformation cochain complex (Davydov–Yetter / Yetter's original
  braided-deformation complex, later developed by A. Davydov) governing
  infinitesimal deformations of the associativity constraint (the pentagon
  F-symbols) with the category's own tensor-square structure as
  coefficients ("trivial"/regular coefficients). **H²_DY classifies
  infinitesimal deformations of the associator; H³_DY is the obstruction
  space to integrating a deformation order by order.** Ocneanu's rigidity
  theorem (originally a subfactor/planar-algebra finiteness result: only
  finitely many finite-depth subfactors — equivalently fusion categories —
  share a given fusion ring; the categorified statement, e.g. in
  Etingof–Nikshych–Ostrik "On Fusion Categories" Ann. Math. 2005 and their
  later "Fusion categories and homotopy theory" 2010) says **H²_DY(C,C) =
  H³_DY(C,C) = 0** for such C. Consequence: **no continuous one-parameter
  family of fusion/modular categories exists through SU(3)₂** — its
  F-symbols, S, T are rigid up to gauge; there is no "nearby" modular
  category to deform into, and no infinitesimal obstruction theory to
  build a moduli space from. This is the standard content and I am
  CONFIDENT in the overall conclusion (no deformation-type quantum-side
  moduli). I am **UNSURE** of the precise original-paper attribution and
  exact degree-shift convention (some sources index the same complex
  starting at H⁰ or H¹ rather than H²/H³ for the two roles above) — the
  conclusion is robust to that indexing ambiguity, so it doesn't affect
  what follows.
- **A sharper, and in my view under-stated, corollary that finishes off
  the naive design even more directly:** the ONE Davydov–Yetter degree
  that is generically *nonzero* — H¹_DY(C,C) ≅ Aut⊗(id_C), the group of
  monoidal natural automorphisms of the identity functor, the
  "gauge"/gerbe symmetry of the associator — is not even the *right type*
  of object to host a "quantum H¹ = 5-dimensional vector space" comparison:
  it is always a **finite discrete group** (concretely, Aut⊗(id_C) embeds
  in the character group of C's universal grading group). **I verified
  this concretely for SU(3)₂** (`quantum_probe.py` PART 1, SCOUT-GRADE
  float computation from the banked S-matrix via the Verlinde formula):
  the fusion ring is multiplicity-free (45 nonzero (a,b,c) structure
  constants out of 216, all equal to 1), and its three invertible
  (quantum-dimension-1) objects {(0,0),(0,2),(2,0)} close under fusion
  into an exact **ℤ/3** — so even the one DY-degree that survives
  rigidity for SU(3)₂ is a 3-element group, not a 5 (or any-)dimensional
  ℂ-vector space. **CONFIDENT** on the SU(3)₂ computation (cross-checked:
  gate passes, integrality exact to 1e-15); **CONFIDENT** on the general
  shape of the argument (Aut⊗(id) is discrete for any fusion category);
  UNSURE only on whether "the universal grading group's dual" is the
  textbook-exact description of H¹_DY in every convention, vs. a closely
  related but not-identical discrete invariant.
- **What this kills, precisely:** any design that treats "quantum H¹" as
  (i) a tangent space to a deformation of the SU(3)₂ category itself
  (H²_DY, killed dead: 0), or (ii) the obstruction space to such a
  deformation (H³_DY, killed dead: 0, vacuously since there's nothing to
  obstruct), or (iii) the "gauge/automorphism" cohomology H¹_DY (survives,
  but is the wrong *kind* of object — discrete, order-3, not a
  5-dimensional space, so it can never be compared to the classical H¹
  on equal footing even though it's nonzero).

**A second, independent, and equally fatal trap for the "obvious" reading
of the given banked data (2I×ℤ/3, the Γ₅′-doublet) — NOT Ocneanu rigidity,
but standard Maschke/semisimplicity, and worth flagging with EQUAL
force because the prereg's own bait ("the hearing group 2I×ℤ/3", "the
Γ₅′-doublet ear") points straight at it:** ordinary group cohomology
H^n(G;V) of a **finite** group G with coefficients in a genuine (hence
completely reducible, char 0) representation V vanishes for all n>0 —
this is Maschke's theorem, via the standard averaging/transfer argument
(order-|G| torsion kills every positive-degree class). So **H¹(2I×ℤ/3;
V) = 0 and H¹(SL(2,5); 2̂′) = 0**, identically, for the same underlying
reason (semisimplicity of ℂ[G] for finite G in characteristic 0) that
Ocneanu rigidity uses for the categorical case — but this is a DIFFERENT,
more elementary theorem, worth stating separately because a naive reading
of candidate (e) below ("use the Γ₅′-doublet directly") would reach for
exactly this dead construction. CONFIDENT (Maschke's theorem is completely
standard).

**A third wall, already banked in this repo and directly relevant to HOW
any surviving candidate may be compared to the classical 5** — not a
cohomology-vanishing theorem but a **no-map theorem**, so it constrains
the *shape* of the comparison rather than killing a candidate outright:
`frontier/B650_typed_functor/FINDINGS.md` ("THE EQUIVARIANCE WALL", also
`docs/LAW_MAP.md` row 9) proves **no nonzero ℂ-linear monodromy-equivariant
map exists from the classical (infinite-order, hyperbolic-spectrum) A₁
representation to the finite-stage hearing representation** (Sylvester
solve T·A₁ = ρ_hear(RL)·T returns T=0, exactly; disjoint spectra —
hyperbolic φ^{±2} vs. the finite congruence shadow — kill every
intertwiner). The banked, surviving form of the classical↔quantum
correspondence is **group-functorial** (reduction mod the conductor,
composed with the stage's character — B644's congruence-shadow theorem)
and **number/invariant-level**, never module-linear. **Design consequence
for wave 1, stated as a recommendation, not a new theorem:** whatever
"quantum H¹" is chosen, its comparison to the classical 5 must be posed
as *"does this independently-computed quantum dimension equal 5"* (a
number-level falsifier, exactly the form the prereg already asks for),
never as *"here is an equivariant map between the classical H¹(D;27)-module
and a quantum-stage representation carrying the same information"* — the
latter is provably impossible by B650, regardless of which cohomology
theory is chosen for the quantum side. CONFIDENT (this is a proved, banked
theorem, correctly read across from its original hearing-plane setting to
the general shape of the problem — the specific application to "quantum
cochains" is MY inference, UNSURE-flagged, though the underlying
theorem is not in doubt).

---

## 2. THE SURVIVING CANDIDATES (enumerated)

Not killed by §1's three obstructions:

- **(a) Module-functor / bimodule cohomology with coefficients in the weld
  W** (Hochschild-type, nontrivial bimodule coefficients).
- **(b) Tube algebra of C, Hochschild cohomology with W-twisted
  coefficients.**
- **(c) The annular/affine category and its trace theories.**
- **(d) "Categorified Fox calculus"**: cohomology of the mapping torus of
  the weld acting on the stage's state space (the direct analogue of
  H¹(ℤ;M) for the monodromy) — extended to the double's amalgam structure
  (Mayer–Vietoris) to actually mirror H¹(D;27) rather than just H¹ of one
  side.
- **(e) Constructions using the Γ₅′-doublet directly** — reframed (the
  literal reading is dead by Maschke, §1): the surviving version is
  **Eichler–Shimura / parabolic cohomology of the infinite Fuchsian group
  Γ(5)** (not the finite quotient SL(2,5)) with coefficients in Sym^k of
  the doublet — this escapes both Maschke (Γ(5) is infinite) and Ocneanu
  rigidity (it isn't fusion-category cohomology at all).
- No further candidate found beyond (a)–(e); I looked for "Brauer–Picard
  group" / "G-crossed extension" framings (my own standard-theory
  addition, folded into (a) below) and did not find anything in the repo
  under those names (expected — this is genuinely new scouting territory;
  a repo-wide search for "quantum cochain", "tube algebra", "Hochschild",
  "categorified Fox" turned up nothing prior to this cell).

**An honest cross-cutting caveat that affects (a)–(c) specifically,**
found while trying to make them concrete (§3): the "weld operator"
ρ(RL) as banked is a **linear operator on the stage's 6-dimensional state
space** (the S,T/mapping-class-group representation of the modular
functor) — it is NOT manifestly a **monoidal autoequivalence of the
fusion category SU(3)₂ itself**. Candidates (a)–(c) as literally stated
need W to BE a bimodule/autoequivalence (an object of the Brauer–Picard
groupoid), which is a strictly stronger structure than "a matrix that acts
on the fusion-ring vector space." Whether ρ(RL) genuinely upgrades to such
a categorical autoequivalence (as opposed to living only in the "annular"/
defect layer, which is actually the NATURAL home for S,T-type data and
is exactly what tube-algebra/annular-category language (b)/(c) is built
for) is, as far as I can tell, an **open design question**, not something
banked or something I can resolve here. **UNSURE, flagged prominently:**
this affects whether (a)/(b)/(c) are well-posed out of the box or need a
prior (nontrivial) categorification step. Candidate (d), by contrast, only
ever needs W as a bare linear operator, so it has no such gap.

---

## 3. Per-candidate assessment

### (a) Module-functor / bimodule cohomology, coefficients = the weld W

**Banked data consumed:** S, T (⇒ fusion rules N^c_{ab} via Verlinde,
computed exactly in `quantum_probe.py` PART 1); the weld word RL; NOT
consumed: F-symbols/6j-symbols for SU(3)₂ (not banked anywhere in the
repo — confirmed by the search in §0/§2).

**Is rigidity really escaped when coefficients are nontrivial? Assessed:
TRUE, with MEDIUM-HIGH confidence, not certainty.** Ocneanu rigidity
(§1) is specifically a statement about the REGULAR bimodule (deforming
the associator with the category's own tensor square as coefficients).
The analogous deformation theory for **G-crossed extensions** /
Brauer–Picard-group cohomology (Etingof–Nikshych–Ostrik's "Fusion
categories and homotopy theory," and the subsequent literature on
Brauer–Picard groups of fusion categories) uses H², H³ valued in
INVERTIBLE BIMODULE coefficients precisely to classify honestly
nontrivial extensions (e.g. Tambara–Yamagami-type categories exist and
are classified by nonzero such classes) — so nontrivial-coefficient
cohomology is demonstrably NOT forced to vanish by the same argument.
This is standard theory I am recalling, not deriving from the repo, and
I have not personally re-derived the vanishing/non-vanishing distinction
from first principles here — hence MEDIUM-HIGH, not CONFIDENT.

**The finite linear-algebra problem, concretely:** if W is granted to be
a genuine invertible C-bimodule (the honest open step, §2), the relevant
cochains in low degree are natural transformations built from Hom-spaces
Hom(a⊗b, W(a)⊗W(b)) etc. for simple a,b (n=6 ⇒ at most 36 such Hom-spaces
per degree, each of dimension bounded by the already-computed fusion
numbers N^c_{ab} — all ≤1 since the ring is multiplicity-free, §1); the
actual differentials need the F-symbols.

**Computability grade: PRICED.** Needs either (i) a full derivation of
SU(3)₂'s 6j-symbols from Uq(sl3) representation theory at the relevant
root of unity (known in principle in the literature, not banked), or (ii)
importing a literature table. Not buildable from what's in the repo alone.

**Falsifier:** the dimension of the degree-2 twisted Hochschild group
HH²_W(C,C) (or its Euler characteristic across the low-degree complex) —
"does it equal 5, or the number of nontrivial W-crossed extension classes
match some multiple of 5" — cannot be stated more concretely without
first doing the F-symbol work.

### (b) Tube algebra of C, Hochschild cohomology with W-twisted coefficients

**Banked data consumed:** same as (a): S,T ⇒ fusion rules exactly; NOT
consumed: F-symbols (needed for the tube algebra's associative
multiplication, Ocneanu's precise definition).

**The finite linear-algebra problem:** Ocneanu's tube algebra Tube(C) is,
as an ungraded vector space, a sum over triples of simple objects of
Hom-spaces controlled by the fusion rules; its irreducible-representation
category is (by the standard theorem relating the tube algebra to the
Drinfeld center) equivalent to the representation category of Z(C), and
for a MODULAR C, Z(C) ≅ C ⊠ C^rev (Müger's theorem — CONFIDENT this is
the standard statement, though I have not re-verified it here), giving
**n² = 36 simple objects** in the center — a concrete, exact-now count.
I attempted a cheap proxy for "the tube algebra's size": Σ_{a,b,c}
N^c_{ab}·N^c_{ba} over the 6 simple objects = **45** exactly
(`quantum_probe.py` PART 1 — this reproduces the same 45 as the count of
nonzero fusion triples, since the ring is multiplicity-free and
essentially fusion-commutative here). **I flag this 45 as a related
structure-constant count, NOT a verified claim that it equals Ocneanu's
actual tube-algebra dimension** — I have not implemented his precise
definition (which involves an extra sum/basis over "tube" generators, not
just this bilinear pairing) and do not want to overstate a number I
haven't derived from a primary source. UNSURE on the exact integer; more
confident (CONFIDENT) on the n²=36-center-simples fact and on 45 being
*a* genuine, exactly computed invariant of the fusion ring even if not
literally "the" tube algebra dimension.

**Computability grade: FEASIBLE for the fusion-theoretic skeleton (sizes,
center simple count); PRICED for the actual Hochschild cohomology**
(needs the tube algebra's multiplication, hence F-symbols, same gap as (a)).

**Falsifier:** dimension of a W-twisted trace/character space on Tube(C)
(the "twisted sectors" count) vs. 5 — same shape of question as (a),
same missing ingredient.

### (c) The annular/affine category and its trace theories

Essentially the same mathematics as (b) viewed diagrammatically (annular
category ≅ idempotent-completion-adjacent presentation of the same data
that builds the tube algebra); same banked-data profile, same missing
F-symbols, same PRICED grade. I did not find independent content here
beyond what (b) already covers, so I am folding it into (b) for ranking
purposes rather than inflating the candidate count. **Falsifier:** same
as (b)'s.

### (d) Categorified Fox calculus (mapping-torus cohomology of the weld)

**Banked data consumed:** S, T exactly (`su32_wrt.py`, gate-verified,
test-locked by `tests/test_b238_su32_levelrank.py`); the weld word RL in
the banked R=T, L=S⁻¹T⁻¹S convention. This is the most literal
categorification of the classical machinery: H¹(D;27) is honest group
cohomology of an infinite-cyclic-extension-flavored presentation (Fox
calculus on the amalgam); the natural single-generator translation is
H⁰(ℤ;V) = ker(W−I), H¹(ℤ;V) = coker(W−I) for V = the stage's state space
and W = ρ(word) — the standard fact that for ℤ acting on a f.d. module M
via a single automorphism T, H⁰(ℤ;M)=ker(T−1), H¹(ℤ;M)=coker(T−1) (from
the free resolution 0→ℤ[ℤ]→ℤ[ℤ]→ℤ→0). CONFIDENT this reduction is
correct as stated (elementary homological algebra); UNSURE whether "the
right" translation of the classical DOUBLE's structure (an amalgam, not
a single HNN extension) is this simplest single-operator model or the
richer Mayer–Vietoris version below.

**Two concrete sub-versions, both EXACT-NOW-to-FEASIBLE from banked data
alone (no F-symbols needed — this is the candidate's chief structural
advantage over (a)/(b)/(c)):**

1. **Simplest form — SCOUT-GRADE COMPUTED, EXACT-NOW (up to redoing in
   exact/cyclotomic arithmetic — done here in float64 only):** V = the
   bare 6-dim SU(3)₂ state space, single operator W=ρ(RL).
   `quantum_probe.py` PART 2: **rank(W−I) = 6 exactly, nullity = 0** — all
   six eigenvalues of W lie strictly off 1 (angles at ±1/20, ±9/20, ±3/20
   of a full turn; four of order 20, two of order 10, lcm 20 — this
   exactly reproduces the banked B640 fact "ord(W(RL)) on the FULL 6-dim
   stage = 20", a clean internal cross-check that the computation is
   using the correctly-banked convention). **So H⁰(ℤ;V_stage) =
   H¹(ℤ;V_stage) = 0 for the bare single-operator model — an exact,
   already-computed MISMATCH with the classical 5** (0 ≠ 5). This is
   informative, not fatal: it tells wave 1 the naive single-vector-space
   reading is dead on arrival, and motivates the richer version below.
2. **Richer form, mirroring the double's actual amalgam presentation —
   FEASIBLE, not yet built:** the classical D is M ∪_cusp M̄ (two
   once-punctured-torus bundles glued along the boundary torus); the
   natural quantum translation is a Mayer–Vietoris sequence relating
   H*(ℤ;V) for M's monodromy word, H*(ℤ;V) for M̄'s (mirror/inverse)
   monodromy word, and H*(ℤ²;V) for the cusp torus's peripheral action —
   the last piece needs "how does the peripheral (boundary Dehn twist)
   subgroup act on the stage," which is plausibly already banked
   implicitly: the boundary twist acts diagonally by the conformal-weight
   phases on T's diagonal (the ribbon twist), so this is likely
   EXACT-NOW-adjacent rather than needing new external input, but nobody
   has assembled the actual Mayer–Vietoris sequence and chased dimensions
   yet — hence graded FEASIBLE, one genuine (if modest) construction step
   away from EXACT-NOW.

**Computability grade: EXACT-NOW** (sub-version 1, done above) /
**FEASIBLE** (sub-version 2, the one that actually mirrors H¹(D;27)).

**Falsifier:** dim coker(W_double − 1) for the full amalgam construction,
compared to 5. (Sub-version 1's falsifier, dim coker(ρ(RL)−1) on the bare
stage = 0, is already computed and already a clean mismatch — reported
above as a completed, if preliminary, negative result.)

### (e) The Γ₅′-doublet, reframed (Eichler–Shimura on Γ(5))

**Banked data consumed:** cellI's exact statement (`frontier/B662_
successor_campaign/cellI/FINDINGS_CELL.md`) that the ear's hearing
representation IS the Γ₅′-doublet 2̂′ (character equality on all 9
conjugacy classes of SL(2,5), exact in ℚ(ζ₂₀)), and that weight-5
modular-type forms on Γ(5) are FORCED (H129, the E₈-exponent mechanism);
open lead L108 (`docs/OPEN_LEADS.md`) — "produce the weight-5 doublet
forms Y^(5)(τ) from the framework's own tower" — is exactly the
missing leg this candidate would supply if built.

**The literal reading is dead (Maschke, §1): H¹(SL(2,5); 2̂′) = 0
identically** — SL(2,5) is finite and 2̂′ is an honest ℂ-representation.
**The surviving reframing (MY OWN standard-theory addition, not banked —
UNSURE how cleanly it matches YLD's actual fractional-weight/metaplectic
setting, flagged prominently):** ordinary Eichler–Shimura theory relates
H¹_parabolic(Γ; Sym^k(std)) for an INFINITE Fuchsian group Γ (here Γ(5),
torsion-free, genus 0 — X(5) is the classical Klein quintic curve,
generically cited as genus 0 with icosahedral automorphism group A₅ ≅
PSL(2,5)) to spaces of weight-(k+2) cusp+Eisenstein forms on Γ. This
escapes Maschke (Γ(5) is infinite) and is not fusion-category cohomology
at all, so Ocneanu rigidity is simply not applicable. **However**: the
forms cellI/H129 actually work with (YLD's F₁,F₂) are honestly of
FRACTIONAL weight 1/5, requiring a metaplectic double cover / nontrivial
multiplier system — a genuinely different (harder) variant of
Eichler–Shimura than the textbook integer-weight case, and I am **UNSURE**
whether the clean H¹_parabolic ≅ modular-forms statement carries over
without modification. What IS banked and solid (cellI, in-sandbox
verified) is the REPRESENTATION-THEORETIC skeleton — Sym^{5k}(2̂)
decompositions, no cohomology invoked — which is a different (simpler,
already-computed) kind of fact than a cohomology dimension count.

**Computability grade: FEASIBLE** for the representation-theoretic
skeleton (already mostly done, cellI); **PRICED** for a literal
Eichler–Shimura-type cohomology dimension count against the fractional-
weight setting specifically (needs new machinery: the metaplectic
generalization, not standard textbook material I can cite with
confidence).

**Falsifier:** dim of the weight-5 doublet-isotypic piece of the relevant
parabolic cohomology (or, more conservatively, of M₅(Γ(5)) itself: YLD's
formula dim M_k(Γ(5)) = 5k+1 gives dim M₅(Γ(5)) = 26 — a very different
scale from 5, so if this were literally the comparison target it would
already read as a strong mismatch order-of-magnitude; but I flag this
specific number as a weak, UNSURE falsifier since it is not clear this
"M_k" is even the right cohomological object to compare, only that it is
the object cellI/YLD actually compute).

---

## 4. RANKING for the wave-1 design decision

1. **(d) Categorified Fox calculus / mapping-torus cohomology of the
   weld — TOP RECOMMENDATION.** It is the most literal, least-assumption
   categorification of exactly the machinery the classical side already
   uses (Fox calculus on a presentation ⇒ ker/coker of a monodromy
   action), it needs ONLY banked S,T data (no F-symbols, no unresolved
   "is W really a bimodule" gap — §2's cross-cutting caveat does not
   apply to it), its simplest form is EXACT-NOW and has *already been
   computed* in this scout (h⁰=h¹=0, an honest, informative, internally
   cross-checked-against-B640 mismatch), and its natural next step (the
   Mayer–Vietoris amalgam version, sub-version 2) is FEASIBLE with a
   clearly named, modest, all-banked-ingredients construction task —
   exactly the shape of thing a wave-2 cell can be preregistered against.
   It also automatically respects the equivariance-wall design constraint
   from §1 (it never claims a map between the classical 27-module and the
   quantum stage; it computes a quantum-side number to compare
   independently).

2. **(a)/(b)/(c) module-functor / tube-algebra / annular Hochschild
   cohomology with W-twisted coefficients — SECOND, more ambitious, tier.**
   These are the mathematically "right" richer answer if the goal is a
   genuinely categorical (not just "operator on a vector space")
   cohomology theory, and (a)'s TRUE-with-medium-confidence escape from
   Ocneanu rigidity is real and interesting — but they are blocked behind
   an honest, currently-unresolved gap (is the weld literally a bimodule/
   autoequivalence, or only a state-space operator — §2) and a genuine
   PRICED cost (SU(3)₂'s F-symbols are not in the repo and would need
   either fresh derivation or literature import). Worth pre-registering
   as a wave-2 target ONLY after (d)'s cheaper version is exhausted and
   if (d) alone can't be made to hit 5 — these are the natural escalation,
   not the first move.

3. **(e) the Γ₅′/Eichler–Shimura reframing — THIRD, a genuinely exciting
   but ORTHOGONAL lead, not a direct competitor for "the H¹(D;27)
   target."** Its natural comparison object (weight-5 forms on Γ(5)) is a
   different classical structure than H¹ of the double D; it is better
   understood as the concrete content behind open lead L108 (the γ₅′
   functor's "last leg") than as a rival design for "quantum H¹." I
   recommend keeping it OUT of the D-A synthesis's primary target choice
   and instead cross-referencing it explicitly as feeding L108, so wave 1
   doesn't conflate two different questions (the H¹(D;27)-comparison
   design vs. the already-open γ₅′-functor completion).

**Explicitly DEAD, to close off before wave 1 spends any cell on them:**
naive H¹_DY(SU(3)₂, SU(3)₂) (Ocneanu rigidity, H²=H³=0 in the relevant
degrees, and H¹ is discrete order-3, not a vector space — computed
exactly, §1); naive H¹(2I×ℤ/3-or-SL(2,5); any genuine representation,
including the Γ₅′-doublet) (Maschke, §1); any design that requires an
equivariant LINEAR MAP between the classical H¹(D;27)-module and a
quantum-stage representation (the equivariance wall, B650, §1) — the
comparison must be number-level, not map-level.

---

## Files produced in this cell

- `SCOUT.md` (this file)
- `reading_log.md`
- `quantum_probe.py` — SCOUT-GRADE (float64) exploratory script, reads only
  the banked, read-only `frontier/B238_su32_levelrank/su32_wrt.py`
- `quantum_probe_output.txt` — its verbatim run output
