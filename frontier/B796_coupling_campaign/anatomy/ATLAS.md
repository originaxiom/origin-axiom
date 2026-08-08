# THE ANATOMY ATLAS

**m004 — the figure-eight knot complement.**
Nine plates, rendered from computed data. A reading and shooting document.

---

## THE OBJECT

Take an ordinary knot — the figure-eight, the second-simplest knot there is, the one
you tie by accident in a cable. Now throw the knot away and keep the space around it.
What is left is a three-dimensional space with a hole where the string used to be, and
that space is the object in these plates. It is not a picture of a knot. It is a
picture of a knot's **absence**.

The remarkable thing is what happens next. That leftover space cannot be shaped
freely. It admits exactly one hyperbolic geometry — one set of distances, one volume,
one everything — and there is nothing to tune. Mostow rigidity makes the geometry a
consequence of the topology, so every number on every plate here is *forced*: the
volume is 2.0298832128 and could not have been otherwise; the space is glued from
exactly two identical ideal tetrahedra, each perfectly regular, all their dihedral
angles 60°. **Zero free parameters.** Nobody chose anything.

Two more facts set this particular object apart. First, it has **one open end** — a
single cusp, an infinitely long funnel where the removed knot went off to infinity.
Cross-section that funnel and you get a torus, and the torus has a definite shape:
the lattice Λ = ℤ + ℤ·2√−3. That single mouth is where almost everything audible
about the object comes out. Second, m004 is the **unique arithmetic knot** — the only
knot in the 3-sphere whose complement is arithmetic. Its symmetries are made of
Eisenstein integers, ℤ[ω], and it sits as an index-12 cover over a small parent
orbifold. That uniqueness is a genuine theorem (Reid), and it is the reason this
object has been stared at for years.

What follows is what it looks like.

---

## 1. THE BODY

**`plate_E_body.png`**

**What you are looking at.** Three panels. Left: the packing of horoballs at the
object's single cusp — a plane tiled with mutually tangent spheres, seen from
infinity looking down the throat of the removed knot. Big spheres sit nearer the
viewer and legitimately hide small ones; the occlusion is real, not stylistic.
Centre: a magnified strip of the packing, redrawn as outlines so the hidden cascade
of ever-smaller spheres is visible down to radius 0.004. Right: the two ideal
tetrahedra the whole space is cut from, drawn as their shape-parameter triangles.

**The one thing to notice.** The sphere sizes are not free. Every radius that occurs
is exactly 1/(2N) where N = a² − ab + b² is a norm of an Eisenstein integer — checked
for every one of the 36 distinct radii found, up to N = 100. The packing is not a
picture of geometry decorated with arithmetic; the arithmetic *is* the geometry. And
the two tetrahedra are identical and perfectly regular: this space is built from one
crystal, twice.

**Status: computed data, cross-checked two independent ways.** SnapPy's horoball
centres and the group Γ₄₁'s own cusp points were compared and found *literally equal*
— same radii, same centres, no fitted offset. The two routes had appeared to disagree;
the render agent traced that to a torus-seam rounding convention (a point on the
seam counted once as x = 0 and once as x = 1) and the disagreement dissolved. The
volume identity vol = 2Λ(π/3) = 2.0298832128 is exact and proved.

---

## 2. THE MOUTH — THE MODES

**`plate_A_modes.png`**

**What you are looking at.** Four standing waves of the object, drawn on the torus
that closes off its single open end. Warm is positive, cool is negative, pale is the
**nodal set** — the curves along which the object is exactly silent. These are
solutions of Δf = λf on the knot complement: the shapes the space would ring in if
you could strike it.

**The one thing to notice.** Three of the four panels are lopsided, particular, with
no symmetry you can name. The fourth — the one labelled INHERITED, λ = 51.013243 —
has visible **triangular** symmetry. That is not an artistic difference. That mode
does not belong to m004 at all; it belongs to the parent orbifold underneath, and it
is carrying the parent's hexagonal lattice up through the cover. You are looking at
the difference between a voice and an echo.

**Status: computed data, first rendering.** These eigenfunctions had never been drawn
before; the eigenvalues are numerically certified (mode-count certification, relative
error ~1e-9), not proved to exist in the sense of a theorem. Treat them as
high-quality measurement, not as arithmetic fact.

---

## 3. THE VOICE

**`plate_B_voice.png`**

**What you are looking at.** Not the wave itself but its **recipe** — which pure
harmonics of the cusp torus each mode actually uses, plotted on the lattice of
harmonics (m₁, m₂). Dot size is how loudly that harmonic is used. A cross is exact
silence.

**The one thing to notice.** Half the lattice is dead. Every harmonic with odd m₂ is
unused, in every form, without exception — the object only ever speaks in even
harmonics of its cusp. That is a hidden half-period symmetry, visible here as a
missing comb. Then there is the circled pair: **π₇**, a specific harmonic that every
one of the object's *own* modes refuses to use, while the inherited mode uses it
freely. A note the child cannot sing and the parent can.

**Status: computed data with one contested reading.** The odd-m₂ vanishing is
overwhelming in the data and is the fingerprint of a genuine symmetry, but it is
presented here as an observed regularity across the computed forms, not as a theorem
with a written proof in this branch. The π₇ zero is a recent observation on a finite
set of modes. Do not narrate either as "proved" — narrate them as *seen*.

---

## 4. THE BONES

**`plate_C_bones.png`**

**What you are looking at.** Every closed geodesic in the object, and in its sister
m003, out to length 6. A closed geodesic is a way of walking in the space and arriving
back where you started, facing the way you set off — a loop the space allows. Each dot
is one such loop: horizontal is how long the walk is, vertical is how much it twists
on the way round. 370 for the object, 411 for the sister.

**The one thing to notice.** There is no red in m004. Colour encodes an arithmetic
class — the norm of the loop's trace, modulo 4 — and the object uses only classes 0
and 3. Class 1 is empty. The sister uses it 180 times. This is not a shortage of data
and not an artefact of the cutoff: **it is a proved theorem** and it holds at every
length, forever.

**Status: proved theorem.** `../../B792_maass_m004_eigenvalues/mod4_trace_law_proof.txt`,
Theorem 2: for every γ ∈ Γ₄₁,
N(tr γ) mod 4 ∈ {0, 3}. One honesty note that belongs on screen if you use this
plate: class 2 is *also* empty, for both manifolds, and that is **not** a
discriminator — no Eisenstein norm is ever ≡ 2 mod 4, so the column is unreachable by
arithmetic and means nothing. The only real hole is class 1.

---

## 5. THE SPECTRUM

**`plate_D_spectrum.png`**

**What you are looking at.** The object's whole voice as a barcode: 43 tones, every
eigenvalue up to r = 13.5. Amber lines are the object's own. Tall pale lines are the
four it inherited from its parent. Raised lines are doubled tones — two independent
modes ringing at exactly the same pitch.

**The one thing to notice.** Four of forty-three are not its own. And the doubling is
not rare: 29 of the 43 come in pairs. A space this rigid is not producing a random
smear of pitches; it is producing a structured chord with a small number of borrowed
notes in it.

**Status: computed data, where the literature had none.** These 43 were computed in
this campaign. They are numerically certified and stable under refinement; they are
not analytically proved, and the list is complete only *up to r = 13.5*, which is
where the computation stopped — not where the spectrum stops.

---

## 6. THE MOUTH IN MOTION

**`plate_F_motion.png`**  (+ `plate_F_frame_0.png` … `plate_F_frame_5.png`,
data in `plate_F_data.json`)

**What you are looking at.** One mode — the inherited one, λ = 51.013243 — photographed
six times as you climb *out* of the cusp, at heights t = 0.85 up to 2.10. Below, the
measured loudness of the mode at 25 heights, on a log scale, with the exact predicted
decay curve drawn through the measurements.

**The one thing to notice.** Two things, and they are opposite. The sound dies
astonishingly fast: over the plotted climb the amplitude falls by a factor of
**148,049**. But the *pattern does not change at all* — the shape correlation against
the first frame stays within 1.6e-05 across the whole climb. The mode is dominated by
a single harmonic shell almost immediately, so what changes going up the throat is
loudness alone, never geometry. The curve it falls on was not fitted; it is the exact
Bessel prediction, drawn on top of the data.

**Status: computed data, with an explicit scale caveat.** The decay law and the
turning height t\* = 0.9748 are exact. The *absolute* amplitude is not: no L² norm for
this form exists in the artifacts, so the normalisation ‖a‖₂ = 1 is stated on the
plate and every printed amplitude is relative to it. Also note: Maass forms are
stationary. There is no time here. "Motion" means motion up the cusp.

---

## 7. THE TWINS

**`plate_G_twins.png`**

**What you are looking at.** m004 beside m003, its sister. Three panels: a ledger of
what is identical and what is not; a paired histogram of the arithmetic classes of
their loops; and both length spectra face to face, m004 above the axis, m003 below.

**The one thing to notice.** These two manifolds have the **same volume** —
2.0298832128, to every digit — are built from the **same two regular ideal
tetrahedra**, and have the **same trace field** ℚ(√−3) and the same parent. Almost
everything a physicist would reach for is shared. And they are not the same space:
H₁(m004) = ℤ, H₁(m003) = ℤ/5 ⊕ ℤ. The sister is not even a knot complement in S³.
This plate is the control experiment for the whole programme, and it is why the field
ℚ(√−3) cannot be what makes m004 special — the sister has it too.

**Status: proved theorem plus exact computation.** The class-1 hole is the theorem
above. `is_isometric_to` returns False. Homology, Chern–Simons (0 vs 0.25) and
symmetry groups (D4 vs ℤ/2 + ℤ/4) are exact. Non-isospectrality is demonstrated on
the ℓ ≤ 6 window, which is all the data covers — but that window already settles it:
119 lengths shared, 72 unique to m004, 90 unique to m003, and 16 of the shared ones
occur a different number of times.

---

## 8. THE COVER

**`plate_H_cover.png`**

**What you are looking at.** The object seen as a stack. Panel 1 is a true Schreier
coset graph: twelve sheets, computed by enumerating the cosets of Γ₄₁ in the parent
group, with each generator's action drawn as coloured edges. Panel 2 shows the
spectral consequence — the parent's tones above, the object's 43 below, with lines
joining the four that are the same. Panel 3 shows why the level is 4 and not 2.

**The one thing to notice.** The three-fold symmetry in panel 1 is not a layout
choice. The ⟨T,U⟩-orbits fall into three blocks of four, and the element E permutes
those blocks cyclically, so E acts as rotation by exactly four positions. The picture
looks symmetric because the group is. The second thing, if you have room: the cusp
subgroup is transitive on all twelve sheets — which is the group-theoretic reason
m004 has exactly **one** cusp rather than twelve.

**Status: proved theorem.** Γ₄₁ is a congruence subgroup of level exactly (4) —
Theorem 1 of the same proof file — and the index is exactly 12. The script asserts
|G| = 3840, |H| = 320, 12 cosets, blocks [4,4,4], mod-2 index 6, and fails the render
if any of these breaks. An independent check via Humbert's volume formula gives
2.0298832128 / 0.1691569344 = 12.0000000. Caveat for narration: the top row of panel 2
is the four *inherited* eigenvalues, not the parent's complete spectrum, which this
repository does not hold.

---

## 9. THE NULL

**`plate_J_null.png`**

**What you are looking at.** The negative result, drawn instead of asserted. The
programme's long-running question was whether this object's spectrum encodes the
constants of physics. That question was run as a **sealed, pre-registered experiment**:
17 certified eigenvalues, 18 banked PDG target values, direct matches and all 544
pairwise ratios, plus a PSLQ search for algebraic relations over six candidate fields.
Panel 1 puts the object against 500 random spectra of the same size and shape. Panel 2
shows the five targets that produced a near-hit. Panel 3 is the ledger.

**The one thing to notice.** The object produced **41 near-hits on physics constants.**
Five hundred spectra drawn at random produced a median of **40**. The object sits at
the **51st percentile** — dead centre of chance. That is the whole story in one number.
Forty-one coincidences sounds like a discovery until you learn that noise gives you
forty. Not one candidate passed the pre-registered gate; the PSLQ search returned zero
relations over all six fields, including ℚ(√5).

**Status: banked negative, computed under a sealed prereg (c6954bfa).** The surrogate
ensemble on this plate is bit-identical to the original sealed run — the script asserts
that its recomputed p-values reproduce the published ones exactly, and that its own
candidate count reproduces the sealed 2 + 39 = 41. What is *not* claimed: this is an
8-digit test over n = 17 eigenvalues with r ≤ 9.84. Deep precision (20+ digits) and
deep algebraicity (50+ digits) remain **open and untested in both directions**. The
honest statement is "no signal found here", not "no signal exists".

---

## 10. THE WALL

**`plate_I_wall.png`**

**What you are looking at.** Two number systems, side by side, and the reason nothing
can be carried between them. Left: **being** — the object's own geometry lives over
ℚ(√−3), a triangular lattice whose units (circled) sit exactly **on** the unit circle.
Right: **hearing** — the object's dynamics live over ℚ(√5), and the relevant eigenvalues
φ² = 2.618… and φ⁻² = 0.382… sit **off** the circle, on the real axis.

**The one thing to notice.** A map transporting a quantity from one face to the other
must solve a **Sylvester equation**, and a Sylvester equation has only the zero solution
when the two spectra are disjoint. One spectrum is on the circle; the other is not.
They share nothing. Therefore the transport map is **exactly 0** — not small, not
approximate. Zero.

**Status: proved negative (B736).** This is the programme's sharpest *positive* no-go:
it does not say "we looked and found nothing", it says "the object's geometry cannot
hand its dynamics a number, by theorem". Note the scope carefully — it forbids
transport **between these two faces**, which is a statement about a relation, not about
the object as a whole. A relational reading (post-B800) treats this as one edge of the
family graph being severed, not the family being mute.

---

## 11. THE CASCADE

**`plate_K_cascade.png`**

**What you are looking at.** The symmetry-breaking chain, drawn from cc's banked
B861/B862 results files — every menu option, dimension, and registerability flag is read
from JSON, not from memory. Three steps: E₆ (dim 78) → SO(10)×U(1) (46) → SU(5)×U(1)
(25) → the Standard Model's gauge group with its **global form**, the ℤ₆ quotient.

**The one thing to notice.** The rule is the same at every step — *among the options
that can carry chiral matter, take the one with the largest leftover symmetry* — and at
every step the choice is **unique**, and it lands on the Standard Model. The ℤ₆ quotient
is **forced, not chosen**.

**Status: conditional on the cascade's own premises.** It says nothing about masses,
couplings, generations, the Higgs, or spacetime. A control run (B869) confirmed the rule
does *not* land on the SM from arbitrary starting groups, so the result is not vacuous —
but "not vacuous" is a long way from "derived". Read this plate next to Plate J: the
cascade is the shape landing, the null is the numbers not landing.

---

## 12. THE THREE ANATOMIES

**`plate_M_faces.png`**

**What you are looking at.** Not the object — the *language* used to describe it. The
programme says "the object has faces". The word is defined three incompatible ways on
`main`, and they were never reconciled: **two** (being ℚ(√−3) / hearing ℚ(√5), "the two
hands"), **three** (B730's forced faces closing at a Klein-four V₄, with *meeting*
ℚ(√−15) = being·hearing), and **eleven** (the operational anatomy actually wired into the
instrument, `B738/kill_graph.json`). Panel 3's bars are counted from that file at render
time — 741 entries, 11 face names — not recalled.

**The one thing to notice.** Two different faces claim the same third slot. `LAW_MAP.md`
line 170 banks emittance as *"a real THIRD FACE"* (B735); B730 says *"beyond being and
hearing there is exactly ONE more forced face — the meeting."* Both are on main, today.
And the anatomy is mostly ornamental: B805 measures that **567 of 733 arcs (77%) attach
to no face at all**, and **6 of the 11 faces carry no proved arc**. Meanwhile *family* is
never defined as a term anywhere in the repo, and no document declares the shift to
reading the object relationally — it is reconstructible only from four arcs over five
days (B803, B805/6, B855, B856).

**Status: a vocabulary report, not a mathematical claim.** Nothing here is proved or
disproved; the plate asserts only what the files say. It earns its place in the atlas
because it is upstream of everything else in it: 24 of the 32 lead-closures in the
ledger were made before that shift, and 20 of 25 change when re-read relationally. The
rule that emerged is worth keeping on the wall — **a closure survives the relational
re-read exactly when its scope sentence names no manifold.**

---

# WHAT IS REAL AND WHAT IS VOCABULARY

This section exists because the programme that produced these plates has an internal
language, and that language is older and more confident than its results. Keep the
three registers apart on screen.

### (i) The proved mathematics — say these plainly, they are true

- m004 is the **unique arithmetic knot complement** in S³. (Reid.)
- Its geometry is **rigid**: one hyperbolic structure, volume 2.0298832128 = 2Λ(π/3),
  glued from **two regular ideal tetrahedra**. Zero free parameters.
- Its fundamental group Γ₄₁ is a **congruence subgroup of PSL(2, ℤ[ω]) of level exactly
  (4)**, of index **12**. (Theorem 1, this branch.)
- For every loop γ in the object, **N(tr γ) mod 4 ∈ {0, 3}** — the class-1 hole in
  Plate C is a theorem, not a sample. (Theorem 2, this branch.)
- π₁(m004) surjects onto the binary tetrahedral group 2T, with exactly two surjections.
  (B266.) This is the genuine object-specific arithmetic atom, and it stands.

### (ii) The programme's internal names — these are labels, not findings

The campaign uses a private vocabulary. It is evocative and it is *not* results. If any
of it reaches the screen, it must be framed as the programme's own naming.

- **"being" = ℚ(√−3).** The trace field — where the object's symmetries actually live.
  The mathematics here is real, but the word is not a result. And Plate G is the
  correction: the **sister m003 has the same field** and is not even a knot. Whatever
  ℚ(√−3) confers, it does not confer being-this-object.
- **"hearing" = ℚ(√5).** The field the programme hoped the spectrum would speak in.
  It was tested. PSLQ over ℚ(√5) at 8 digits: **zero relations, null rate 0.00.** The
  name outlived the hypothesis.
- **"grammar" = the claimed Standard-Model structural echo** (E₆ recurring across
  McKay / Lie / CIZ faces). **The programme's own audit, B727, took this apart and found
  it largely generic** — and that audit is the honourable thing in this whole story. It
  found that the three "independent" faces are one ADE classification seen three times,
  so P(recurrence | one label) = 1; that ℚ(√−3) can reach **no exceptional label but E₆**
  (E₇ forces √2, E₈ forces √5, both real quadratic), so there was never a draw to win;
  and that 4 of 13 hyperbolic knots surject onto 2T, **including non-arithmetic ones**.
  Its verdict: *the recurrence is forced, not evidence.*

### (iii) What is actually open

- **Deep precision and deep algebraicity.** The Plate I null is an 8-digit result over
  17 eigenvalues below r = 9.84. The 20-digit and 50-digit questions have not been run.
  Open in both directions.
- **The parent's full spectrum**, which would turn Plate H's "four inherited tones" into
  a complete old/new decomposition.
- **Proofs for what Plate B only shows**: the odd-m₂ vanishing and the π₇ zero are
  strong observed regularities awaiting theorems.
- The spectrum above r = 13.5. Nobody has looked.

### The bottom line, stated once, plainly

**This object has produced no Standard Model values. Its value-content tested empty at
every level that has been tested.** That is not the campaign failing; it is the campaign
working. The negative was pre-registered, run, and banked, and Plate I is what it looks
like.

What survives is better told as what it is: a uniquely distinguished mathematical
object, forced into a single shape by its own topology, whose loops obey a proved
arithmetic law, whose spectrum was computed here for the first time, and whose standing
waves had never been drawn until this campaign drew them.

**These plates are about seeing the mathematics. They are not selling a physics claim,
and any cut that implies otherwise is misrepresenting the source.**
