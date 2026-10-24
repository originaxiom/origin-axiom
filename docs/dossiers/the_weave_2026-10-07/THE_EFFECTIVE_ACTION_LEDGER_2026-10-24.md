# The effective action's ledger: what the joint action forces for a joint (τ, h) effective potential, and what it leaves free

The SM-derivation seat, 2026-10-24, at the owner's word ("yes please lets do it", to "a ledger first: what the joint
action forces as field content and couplings, and what it leaves free").

**A READING: nothing here is computed, and it adds no claim.** Where it and an arc disagree, the arc wins. It was built
from four sweeps of the record, read-only, and every load-bearing line below was checked at its file and line:
- the variables and the field content;
- the couplings and their constants;
- the effective-action pieces already computed;
- GENESIS and main's register on what is forced.

Sources: NOTE = `docs/dossiers/the_weave_2026-10-07/NOTE.md`; GENESIS = main's GENESIS.md (v1.54, read with git show).

## 1. The question

The rule adopted today (`docs/THE_WEAVE.md`, "Spontaneous breaking is not a hand-pick") makes a selected state a weave
result only if it minimizes the joint action's own effective action. That needs a forced content, coefficients forced
or computed in the same frame, and a truncation that is the unique invariant of its order. The target object is the
one-loop effective potential on the joint space of τ, the fibre's line w and the Higgs direction h. Can it be computed
without a choice?

## 2. The ledger

Statuses: **FORCED** (the joint action produces it), **COMPUTED** (on record, no free coefficient), **CHOSEN** (a
dictionary datum, a reading or a hand choice), **FREE** (a free number), **OPEN** (not settled).

**A. The variables**

| item | status | source |
| --- | --- | --- |
| τ, the fibre's modulus | its space FORCED (M₁,₂ over M₁,₁); its value a state the moves do not fix | NOTE:1280, 4404 |
| the flat line w ∈ U(1)² on the fibre | allowed, not forced; the moves jointly fix only the trivial line | NOTE:4405–4407, 8678–8681 |
| a flavour Wilson line in Aut(𝕎) = U(3) | allowed, not forced; up to six real numbers | NOTE:4744–4745 |
| the Higgs direction h ∈ M = ℂ³ | OPEN; the fork (A) a covariant form, (B) a vev minimized with τ | the breaking chain, section 5 |
| the doublets H_u, H_d | CHOSEN (the Standard Model's H̃ was an identification made by hand) | main's P-365 |

**B. The structure the joint action forces**

| item | status | source |
| --- | --- | --- |
| E₈, the lattice | COMPUTED from the moves given the prime 5: ⟨R, L⟩ mod 5 = SL(2, 𝔽₅) ≅ 2I, whose icosians give E₈'s 240 roots (W135's K0, rebuilding B1270). The prime 5 is CHOSEN: B1270 takes it from the golden face and says which face's group is used is not forced, and nothing on record forces it (W31) | NOTE, W135 and W31; PROGRESS_LOG, B1270 |
| E₆ × SU(3) inside E₈, the frame | unique up to the moves, the same for every thread (W135's K0) | NOTE, W135 |
| the Lie type, on main | one of THE_CLAIM's five typed data, narrowed to "accept-the-nomination" (B1025, with B1123's flag). GENESIS's "the frame (E₆, SO(10), SU(5)) is a choice" (its FK11 row) concerns the chiral reading's GUT frame, not E₈ | main's THE_CLAIM §1; GENESIS FK11 row |
| the joint family group Γ₄ = PSL(2, ℤ/4); matter in ρ′ | FORCED (W136) | NOTE:8932–8935 |
| the matter T = ℓ ⊗ M, one holomorphic zero mode per parity | FORCED (W21) | NOTE:3639–3640 |
| couplings as modular forms in 1′, ρ′ (twice), ρ′ ⊗ sgn; no constant Yukawa | FORCED (W135) | NOTE:9058–9065 |
| the base factor Im τ·\|η\|⁴ | FORCED (W120); any holomorphic τ(z) solves, so nothing selects | NOTE:10185, 10211 |
| Φ, the fibre's uniformizing field | FORCED, \|Φ\| = ½ with no τ in it; silent toward the three | NOTE:9406 |
| the qubit dictionary (R = Sym² of the theta qubit; I = 2r/(1 + r²)) | COMPUTED (W152) | NOTE, W152 |

**C. The loop's content**

| item | status | source |
| --- | --- | --- |
| which fields, how many, bosons or fermions | **CHOSEN: "a dictionary datum (GENESIS FK11) that the weave does not fix"** | NOTE:4770–4771 |
| the content's signs, the mass term's reading, the hand | CHOSEN (FK11) | NOTE:5124 |
| a content that holds τ in the fits' band | needs 89 to 95 extra complex scalars (B1704); "Nothing on record selects such a content" | NOTE:5261–5264 |
| FK11 itself | UNEARNED; UNEARNABLE within F-HE and F-CI on any thread or cover (v1.27) | GENESIS FK11 row |

**D. The couplings and the constants**

| item | status | source |
| --- | --- | --- |
| the Yukawa weight w | FREE: "Nothing here fixes the weight" | NOTE:8987 |
| its C(w) complex constants (6 at w = 6; 26 or 30 at the 27s' weights) | FREE | NOTE:8860–8867 |
| the minimal joint frame's relation M_e = M_d | FORCED, and excluded by data (D ≡ 1 against 10.58) | NOTE:8869–8871 |
| main's channel constants c_s | COMPUTED | NOTE:7414 |
| main's horocycle, line and reading S/S̃ per sector | CHOSEN | main's P-362, P-365; B1744 |
| the lepton factor | FREE (P-294 open) | main's B1726 |
| the Kähler metric | minimal ASSUMED; non-minimal terms add free numbers | NOTE:10298–10300 |
| the gauge couplings | FREE | the breaking chain, section 8 |
| the overall unit | a convention, which GENESIS §7 calls "the observer's" (B1168, OPEN); no theory derives a unit | GENESIS §7 |
| every dimensionless ratio of scales (W150's μ/M̃, the cutoff over the fibre's scale, sm:B1508's ℓ/G) | FREE unless derived, counted against the 19 | NOTE, W150; THE_FRAMEWORK.md, sm:B1508's note |
| the link Λ and the end unit | a tagged working postulate ("given Λ"); FK10 open | GENESIS GM5c row (v1.33), FK10 row |
| the hypercharge charges | put on the sectors by hand (I-32) | main's IDENTIFICATION_LEDGER |

**E. What is already computed, and where it lands**

| piece | canonical? | lands at |
| --- | --- | --- |
| W51's functionals on τ (the parities' determinants, y\|η\|⁴) | each canonical; which one to use is a choice | ω (minimum), i (saddle), or the cusp; the joint determinant is flat |
| W59's one-loop potential on the fibre | each sector's closed form COMPUTED; the total depends on the content (GENESIS FK11) | ω, the cusp or flat, by the content's net sign |
| W62's six-dimensional term | lattice values; its E(τ, 2) part a 1% fit | every content on record runs to a cusp |
| W60, the line at τ = ω | τ fixed by hand, the content chosen | a half-period line |
| main's B1646, B1655; W64; W149 (the h quartic) | coefficients chosen; O has three quartic invariants, so a quartic is not unique | the cone, the real locus or O's special lines; generic only at chosen coefficients |
| W67, the closest to joint | h tied to τ by hypothesis; coefficients on a grid | ω or the cusp |
| W150, the heavy-state holder | a mechanism from the literature; μ/M̃ free | a curve, Re τ flat |
| main's S214, B1699, B1673 | the functional chosen | ω, a saddle, or near-constant |

**F. Never computed**
- Any functional with τ and h as independent variables.
- The fibre's towers with h as a background, that is masses that depend on h.
- The six-dimensional term exactly, over the whole fundamental domain.
- The volume modulus.
- The doublet's potential.
- O's sextic and higher invariants.
- Any content forced by the joint action.

## 3. What the ledger says

- **The joint action forces the space and the representations, not the loop's content.** The variables (τ, w, h) and
  their spaces, the family group, the matter's representation and the couplings' modular form are forced, and so
  is the E₈ branching once the prime 5 is given. Which fields run in the loop, how many and with which statistics is
  GENESIS FK11's dictionary datum, which is unearned. Every content on record was chosen.
- **The couplings' constants and the ratios of scales are free.** The modular forms are forced in kind, but their
  weight and their C(w) constants are not. The overall unit is a convention (GENESIS §7's "the observer's", B1168,
  OPEN), but every dimensionless ratio of scales is a free number unless derived. Λ is a tagged postulate.
- **The truncation test fails already at quartic order for h.** O admits three phase-invariant quartics, so a quartic
  functional of h is not the unique invariant of its order, and the choice among them is a free number.
- **So the joint (τ, h) effective action cannot yet be computed without free inputs.** Under the adopted rule, a
  computation now would carry at least the content as a free datum, plus the constants it uses. The canonical pieces
  on record (W51, W59's sector forms) land at ω, i or the cusp, as Michel's theorem expects.
- **The shape of the gap is now precise.** One unearned item, the content (FK11), stands between the record and a weave
  result by minimization. The constants and the ratios of scales would then be counted against the 19, unless the
  content's own loop fixes them.

## 4. What step 2 can be (for the owner's choice)

1. **A census over contents, rule first.** Take every content in a stated admissible set: signs and multiplicities of
   the forced sectors, under a fixed rule and a trial budget. Ask where the joint (τ, w, h) one-loop minimum can lie,
   and which contents would put it at the target. This needs no answer to FK11. It prices the target in contents, as
   B1704 priced the band at 89 to 95 scalars. Prior, by Michel and the record: symmetric points for every content but
   fine-tuned ones.
2. **The E₈ frame's own content, labelled "given the prime 5 and FK11".** The adjoint 248 under the fibre's
   structure (NOTE:6847) as the loop's bosons. E₈ is computed from the moves once the prime 5 is given (W135), and
   nothing on record forces the prime. Taking the algebra's adjoint as the loop's fields is FK11's dictionary step. So
   it is conditional twice. Whether the prime can be forced is a separate, data-free question (section 6).
3. **Earn the content first (FK11).** That is main's and the owner's question, and GENESIS marks it unearnable within
   F-HE and F-CI.

**This seat's recommendation: 1.** It is the only one that needs no new input, it answers "what would the target cost",
and its negative, if it comes, is clean.

**Option 1, Stage A, done, 2026-10-24 (dated note; NOTE, W154).** At the owner's "GO!!!". At the forced line every
content that treats the parities alike has V = −(A E(τ, 3) + B E(τ, 2)). So at one loop it runs to the cusp, sits at ω
or i, or holds τ on the imaginary axis at y*(t) ≈ 7t/π², with t = B/|A|. The band needs net bosons in ρ_Q outweighing
the rest 42 to 48 times, within a 13% window. Every content on record, and E₈'s 248 (option 2), runs to the cusp.
Stage B, the Higgs direction, waits on the owner.

**Option 1, Stage B, done, 2026-10-24 (dated note; NOTE, W155).** At the owner's "lets do themall". At the forced line
no copy of the Higgs has a zero mode, so a constant vev is not available. Masses never change a cusp's leading term,
so every content that runs still runs, the record's and E₈'s among them. Masses that treat the parities alike only move
the curve; heavy ones send the band's contents to ω. A condensate selects the copy that becomes massless at the cusp,
holds neither Im τ nor Re τ, and moves the band's price by at most 5%, adding two free ratios. Option 1 is closed at
one loop: the band's price stays in the content. What is left is option 3, to earn the content (GENESIS FK11), or a
frame beyond one loop.

## 5. Discrepancies found while sweeping

Corrected on this branch, with dated notes, in the commit that carries this page:
- this branch's THE_WEAVE.md and WORKING_RULES.md still listed GENESIS GM5b as open; main adopted it at v1.48;
- THREE_GENERATIONS_GIVEN_ONE_LINK.md said "the grammar DERIVED", while GENESIS grades GM1–GM4 POSTULATED.

Flagged to main (its files):
- THE_CLAIM's one-sentence claim says "four typed external data", against its §1's five;
- this branch's THE_FRAMEWORK.md carries sm:B1508's note that Λ = −1 fixes the unit, not ℓ/G, leaving one free
  dimensionless constant. Main's copy lacks it, and main's GENESIS GAP list still says "no free dimensionless constant
  (B1088)".

## 6. Corrected before this page was pushed (2026-10-24, at the owner's question)

The owner asked: "are we aure these arw still valid claims especially “observers” and regarding E8 - can we derive
it and make it unconditional, are we at the right moment to probe it once more, clarify it". Two rows of the first
draft, committed but never pushed, were wrong. They are corrected above.
- **The scale.** The draft had it CHOSEN, "the observer's", for every scale. GENESIS §7 says the overall unit is the
  observer's and marks it OPEN (B1168). A unit carries no information, and no theory derives one. The ratios of scales
  are physical, and the draft did not separate them from the unit. They are free numbers unless derived.
- **E₈.** The draft said "GENESIS calls the frame a choice", citing GENESIS's FK14 row. The words are in GENESIS's FK11
  row, and they concern the GUT frame (E₆, SO(10), SU(5)) of the chiral reading. E₈ itself is computed from the moves
  once the prime 5 is given (W135). So the condition is the prime, not the algebra. The step from the algebra to the
  loop's fields is FK11, as for every content.

**The question it leaves (no arc run).** Is the prime 5 forced by the weave? A hand check of classical facts, whose
numbers the page's lock test recomputes: give the move T a finite order N. The moves' group then becomes finite exactly
for N = 2, 3, 4 and 5, with orders 6, 12, 24 and 60 (Klein). By McKay their double covers pair with D₅, E₆, E₇ and E₈,
the diagrams T(2, 3, N), whose Cartan determinants are 6 − N. At N = 6 the diagram is affine. So E₈ is the ladder's last
rung and its only unimodular one. The record's forced structures sit at level 3 (the common point, B1601) and level 4
(Γ₄, W136; the qubit's Clifford group, W152). None sits at level 5. Whether a rule of the joint action takes the whole
ladder is the owner's question. A data-free arc could set it out, rule first; it is offered, not started.

**W153, 2026-10-24 (dated note).** The arc was run at the owner's ruling, every cell as predicted (NOTE, W153). The
prime 5 is the ladder's last finite rung, fixed by the moves' own orders 2 and 3, and E₈ its only unimodular rung. The
record's forced structures use only the primes 2 and 3. So E₈ is forced if the principle takes the whole ladder (R1)
or asks invariance under every move (R2); under R3, the levels in use, the top rung is E₇. The rule is the owner's.
The E₈ row above stands until the owner rules.

0 of 19.
