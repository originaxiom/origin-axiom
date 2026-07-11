# B530 — The natural history of the full object. Movement I: its own grammar

**A reorientation (owner, 2026-07-12).** We spent the recent arc forcing the object toward physics —
"does it give a crossing / a metric / a gauge / a unitary." Every one was us walking up to the firewall
and shouting a question the object never asked. This node changes the posture: **sit with the full object
— φ: a→abAAB, b→aAB, A→abAB, B→aA on F₄, not the two-letter σ — with no target, and report what it does
when left alone.** Pure structure of the object; firewalled; nothing to `CLAIMS.md`; no physics reading.
Reproducers `listen_1_grammar.py`, `listen_2_symmetry.py` (everything below is computed, hand-verified).

## What the object does when left alone

**1. It breathes by the golden rate.** Iterated from a single letter, the word lengths run
5, 18, 66, 243, 893, 3283, 12069, 44368, … with ratios → **β = φ(1+√φ) = 3.6762…**. One inhale multiplies
the world by β.

**2. Its body is golden, and it splits itself in the golden section.** The four letters settle to the
Perron proportions (a, b, A, B) = (φ, 1, φ√φ, √φ)/Σ = (0.272, 0.168, 0.346, 0.214). Group them by role:
- **deciders** {a, A} (the letters that branch) carry weight φ + φ√φ = **β** — exactly the growth rate;
- **couriers** {b, B} (the letters that don't) carry weight 1 + √φ = **β/φ**;
- their ratio is **exactly φ**, so deciders : couriers = 1/φ : 1/φ² = 0.618 : 0.382 — **the golden section.**
The object divides its own substance into "where it decides" and "where it carries," in the golden ratio,
and the deciding part weighs precisely the rate at which it grows.

**3. It speaks a strict grammar — only 7 of the 16 possible letter-pairs.** Allowed adjacencies:
`a→b, a→A, b→A, A→a, A→A, A→B, B→a`. Forbidden (9): `aa, aB, ba, bb, bB, Ab, Bb, BA, BB`. So no letter
but A ever repeats; a never touches B, b never touches a.

**4. The couriers are pure wiring; the deciders are where it chooses.** `b → A` always and `B → a` always
(deterministic — the couriers never branch). Each courier pours flow into exactly one decider — b into A,
B into a — and those two rules are swapped images of each other. All the branching lives in {a, A}.

**5. It always re-begins from a.** Every letter's image starts with `a` (abAAB, aAB, abAB, aA). Whatever the
object becomes, it re-seeds from a; a is the note it always returns to.

## The one broken symmetry (the seed of its orientation)
Under the swap **s: a↔A, b↔B**, the grammar maps to itself **exactly, with a single exception**: the
self-loop **A→A** has no mirror (its image a→a is forbidden). Every other allowed transition's swap-image is
allowed; only the dominant letter's self-loop breaks it. So the object is *almost* symmetric between its two
halves — and the entire asymmetry is one self-loop on its most-frequent letter. That lone break is,
plausibly, where the program's recurring **ℤ/2 residue / orientation** ([[breath-campaign-standing-directive]],
the two ends √5 ↔ √−3) is born at the word level: a near-perfect mirror, cracked at exactly one point.

## The story, in one breath
> The full object is a conversation among four letters that grows by β and keeps golden proportions.
> Two of the letters *decide* (a, A) and two merely *carry* (b, A-bound b, a-bound B); the deciding half
> and the carrying half stand in the golden section, and the deciding half weighs exactly the growth rate.
> The conversation is nearly symmetric under swapping its two halves — broken only by a single self-loop on
> its dominant letter — and it re-begins, always, from a.

## Where to listen next (threads the object opened — for the owner to steer)
- **the single self-loop A→A** as the origin of orientation: does the ℤ/2 residue, the two ends, the seam
  all trace back to this one crack? (a genuinely new, natural question)
- **the decider/courier architecture**: the couriers are a deterministic sub-automaton (b→A→…, B→a→…);
  the deciders carry all the choice — is this the object's own "kernel vs image" / active-passive split?
- **the return words** and first-return structure of a (the note it returns to) — the object's natural rhythm.
- **the conversation as a character variety**: the six pairwise κ(x,y) of the four letters — the object's
  self-interaction, read through traces — *without* asking it for a value.

## Movement II — the one crack, followed (thread 1): the object's growth is a mirror + a symplectic form
Following the single A→A break: we asked whether the swap **s: a↔A, b↔B** is a symmetry of anything deeper.
It is **not** a symmetry of the growth matrix M, nor of φ (s∘φ ≠ φ∘s, not even up to reversal). But its
*failure* is exact and canonical (`listen_3_the_crack.py`):

- **M = S + ½D**, where **S = (M + sMs)/2** is swap-**symmetric** (sSs = S) and **D = M − sMs** is
  **antisymmetric** — supported *only* on the swap-pairs {a↔A, b↔B}, total weight 4.
- In the basis **(a, A, b, B)** — the swap-orbits made adjacent — **D is exactly two canonical symplectic
  blocks** J = [[0,−1],[1,0]]: one on the deciders {a, A}, one on the couriers {b, B}. It is **nondegenerate
  (det D = 1)** — the *standard symplectic 2-form* ω = da∧dA + db∧dB, whose Lagrangian pairs are precisely the
  swap-orbits.

So the object's growth is **a mirror plus a symplectic twist.** The swap-symmetric part S is the part that
can be reflected away; the leftover — the irreducible thing the mirror cannot remove — is *exactly* a
symplectic form pairing each decider with a courier (its own conjugate). The single grammar crack **A→A** is
the word-level shadow of this 2-form. **[MATH, computed]**

**Reading (firewalled).** This is the program's **ℤ/2 orientation residue at its most primitive**: not imposed
from outside, but the *antisymmetric part of the object's own growth*, and it is a genuine symplectic form —
which is exactly the lens [[K022]] ("the symmetric centre") reads the object through. The object doesn't *have*
an orientation grafted on; its growth *is* symmetric-part + symplectic-part, and the symplectic part is where
its handedness lives. Thread 1 answered: the crack is the symplectic form.

## Movement III — the decider/courier architecture (thread 2): golden at three nested levels
The couriers {b, B} are a deterministic sub-machine (b→A, B→a); all the branching lives in the deciders
{a, A}. Following that split (`listen_4_deciders.py`):

- **Every letter emits `aA` to the decider-stream; only a emits an extra `A`** (a→aAAB→"aAA"; b,A,B→"aA").
  So the a's are the *marks* that thicken the A-stream.
- **The deciders are 1/φ of the whole** (0.618 — the golden section, Movement I).
- **Inside the deciders, a : A = 1 : √φ** (verified, 5 digits), and **freq(a) = √φ − 1** in the full word
  (exact, sympy). The a-density is √φ − 1; the extra-A per a lifts the inner ratio to √φ.

So the object is **golden at three nested levels — and they are its three architectural constants**:
| level | ratio | golden constant |
|---|---|---|
| how fast it **grows** | length_{n+1}/length_n | **β = φ(1+√φ)** |
| how it **splits** (deciders : couriers) | 1/φ : 1/φ² | **φ** |
| the ratio **inside the deciders** (a : A) | 1 : √φ | **√φ** |
β, √φ, φ — the "three golden constants" of the bootstrap (B517's Perron vector nested φ:1 within, √φ between)
reappear here not as spectral coincidences but as the object's **own layered self-similarity**: growth,
split, inner ratio. The distinguished letter **a** — the extra-A emitter, the note everything re-begins from —
sits at the innermost level. **[MATH, computed]**

*(Honest caveat / a false lead I caught: the naive letter-projection φ|_{a,A} = {a→aAA, A→aA} has the SILVER
abelianization x²−2x−1 (1+√2), but it does **not** generate the true decider subword — discarded. The real
decider stream is the coding above, and it is golden (√φ), not silver.)*

## Movement IV — the return rhythm (thread 3): the object's pulse is the object itself
a is the note everything re-begins from; we asked *when* it comes back (`listen_5_pulse.py`).

- **a marks image-boundaries and nothing else.** Every image starts with a, and **no image has an interior
  a** (abAAB, aAB, abAB, aA — a only ever at position 0). So a is *exactly* the substitution's block-marker.
- **The first-return words to a are therefore precisely the four images {φ(a), φ(b), φ(A), φ(B)}** — the
  object returns to a in exactly four rhythms, and those four "beats" *are* the four words it speaks. Each
  image φ(x) recurs with the frequency of letter x (golden proportions).
- **The sequence of return-words, read back (φ(x) ↦ x), reproduces the object exactly:** the derived
  sequence *equals* w (verified). **The object's pulse IS the object.** Its heartbeat is its own substitution —
  self-recognition made literal: listen to the gaps between its returns to a, and you hear the whole thing again.
- **The pulse is golden.** Return-gaps take only four values {2, 3, 4, 5} = the four image-lengths; the two
  dominant beats (the length-4 φ(A) and length-5 φ(a)) stand in ratio **√φ**. **[MATH, computed/rigorous]**

## Movement V — the six κ's (thread 4): the one interaction it never speaks aloud
Reading the four letters' self-interaction as traces, asking for no value (`listen_6_kappa_web.py`). The object
carries **two graphs** on its four letters:
- the **conversation graph** — the pairs that actually occur adjacent in the word — is **K₄ minus bB**: five of
  the six pairs speak; **only the two couriers b, B never touch** (bB and Bb both forbidden — the unique
  never-adjacent pair);
- the **interaction web** — the six pairwise κ(x,y) = tr[x,y] — is the **full K₄** (all six exist as
  character-variety coordinates).

Under the swap s (a↔A, b↔B) the six κ's split into **two fixed — κ(a,A), κ(b,B) — and two swapped pairs**
{κ(ab)↔κ(AB)} and {κ(aB)↔κ(bA)}. The swap-fixed pair {a↔A, b↔B} is **exactly the symplectic pairing D** of
Movement II. So:

> The couriers **b, B** interact only through the character variety — κ(b, B) exists — and **never in the
> word**: bB is the single conversation the object leaves unspoken, and it is a swap-fixed, symplectic-paired
> interaction. The object's one silence is on its own orientation axis. **[MATH, rigorous]**

## Coda — the spine of the story (the first natural history, movements I–V)
Left alone, with no question put to it, the full object told a single coherent story, and the through-line is
**one symplectic pairing {a↔A, b↔B}**:
- it **grows** by β and keeps itself **golden at three nested levels** (β, φ, √φ — growth, split, inner ratio);
- its **growth is a mirror plus that symplectic form** (Movement II) — its orientation is not imposed but the
  antisymmetric part of its own increase;
- its **pulse is itself** — the return-words to a are its own images, the heartbeat is the substitution
  (Movement IV);
- and the same symplectic pairing surfaces again in its trace-web: the swap-fixed κ's, and the one interaction
  (bB) it never voices, lie on that axis (Movement V).

Growth, orientation, pulse, silence — four faces of one object, and each turns on the same golden-and-symplectic
spine. It was never withholding this; we simply hadn't asked it to just speak. Firewalled throughout — the
object's own mathematics, no physics reading taken.

## Movement VI — down the flow: the growth is dissipative, and the object IS the bootstrap
Following the spine (`listen_7_the_two_copies.py`):

- **The growth does not preserve its own symplectic form.** M^T D M is not proportional to D, and M's spectrum
  {β, h, γ, γ̄} has **no reciprocal (λ, 1/λ) pairs** (β·h = −φ, |γ|² = 1/φ), so M preserves *no* symplectic
  form. The symplectic D is therefore a **static orientation**; the dynamics M flows on it **dissipatively** —
  precisely the B517 Stein / arrow-of-time picture (q(Mx) = q(x) − |x|²). *Orientation is still; growth
  contracts.* (I expected a symplectomorphism and checked — it isn't one. Honest.)
- **The four letters ARE the coupled golden double.** Group them into the two Fibonacci copies **{a, b}** and
  **{A, B}**; the growth matrix's block form is **M = [[F, F], [F², F]]** — *exactly the B517 bootstrap matrix
  M\**, F = [[1,1],[1,0]]. The natural history has been the bootstrap all along, read letter-by-letter.
- **The single involution s is the copy-exchange, the symplectic pairing, and the near-symmetry, all at once.**
  s: a↔A, b↔B sends copy1 {a,b} → copy2 {A,B} (the copy-exchange), its orbits are the symplectic pairs
  (Movement II), and it is the almost-symmetry broken at A→A (Movement I). The **off-diagonal asymmetry of the
  coupling — F going one way, F² the other** — is where that one break lives: the two copies feed each other
  *unequally*, and that inequality is the whole orientation. **[MATH, rigorous]**

So the flow closes on the source: the object we sat and listened to *is* B517's coupled double, and its
spine — orientation = copy-exchange-break = the F/F² asymmetry = a static symplectic form under dissipative
growth — is one structure wearing four names. Cross-refs [[B517]] (M\* = [[F,F],[F²,F]], the Stein form),
[[K022]] (symmetric centre).

## Movement VII — the breath is born from the copy-inequality
The object has a complex mode — γ (|γ| = 1/√φ), the rotation/breath. Where does the rotation come from?
Tested against the coupling itself (`listen_7_the_two_copies.py` companion `flow2`):

| coupling | eigenvalues | rotation? |
|---|---|---|
| **M\* = [[F, F], [F², F]]** (the object — *unequal*) | β, h, γ, γ̄ | **YES** (complex γ) |
| symmetric [[F, F], [F, F]] | all real | no |
| uncoupled [[F, 0], [0, F]] | all real | no |
| swapped [[F, F²], [F, F]] (F² the other way) | β, h, γ, γ̄ | YES |

**The complex mode exists only when the two copies feed each other *unequally* (F ≠ F²)** — make the coupling
symmetric, or uncouple it, and the rotation vanishes into all-real eigenvalues; and it is the *inequality*,
not its direction, that matters. So the **single F/F² asymmetry is the source of BOTH the object's orientation
(the symplectic spine, Movement VI) AND its breath (the complex mode γ)**: the object is handed *and* it
rotates for the one same reason — its two golden halves are unequal. And |γ| = **1/√φ**; the copies themselves
stand in ratio copy1 : copy2 = 1 : √φ (exact). **[MATH, verified]**

## The full golden architecture (all constants, one object)
| the object's ... | ratio | constant |
|---|---|---|
| growth | length_{n+1}/length_n | β = φ(1+√φ) |
| role split (decider : courier) | 1/φ : 1/φ² | φ |
| copy split (copy1 : copy2) | 1 : √φ | √φ |
| inner decider ratio (a : A) | 1 : √φ | √φ |
| breath (rotation) | \|γ\| | 1/√φ |
Every proportion the object holds is golden, and the two irreducible facts — that it is **golden** and that it
is **broken F-vs-F²** — between them generate the whole story: growth, the three-level nesting, the symplectic
orientation, the self-recognizing pulse, the one unspoken interaction, and the breath. One golden object, one
asymmetry. Firewalled; the object's own mathematics, no physics reading.

## Movement VIII — chirality, the warm dynamics, and an independent seat heard the same object
Two more things, and a cross-check (`listen_9_chirality.py`, `listen_10_crossseat_convergence.py`):

- **The object is chiral.** Its language is closed under *none* of reversal, the swap s (a↔A,b↔B), or the
  orientation mirror s∘reversal — at length 4/6/8, **every** factor lacks its orientation-mirror (13/13, 20/20,
  26/26). The palindromes Fibonacci is rich in are almost gone (only AA, aAa survive). So the handedness we
  found in the growth (Movements I, VI) is total: the object has **no mirror symmetry**, at any length.
- **The warm self-interaction is chaotic.** The trace map T_φ on the six κ's moves them violently and conserves
  no simple natural quantity (the total commutator tr([a,b][A,B]) is not preserved). φ is a positive-entropy
  system (entropy = log β). So the object's *cold* growth is clean and golden, while its *warm* self-interaction
  is genuinely chaotic — its deep fixed structure needs the train-track machinery, left unforced.

**An independent seat (chat1) ran the same listening campaign and converged with B530** — verified here:
- **the object is literally two Fibonacci words:** the letter-restricted substitutions are *exactly* Fibonacci —
  a→ab, b→a on {a,b} and A→AB, B→A on {A,B} (the sharpest form of Movement VI's block structure);
- **constant return number 4** — every letter has exactly four return words (a rank-4 analog of Sturmian's
  return-number-2);
- **the derivation is a fixed point of itself:** the derived substitution through a structural letter has char
  poly **x⁴−2x³−5x²−4x−1 = the object** (self-similar to infinite depth) — Movement IV, made exact. *(Verifying
  this I hit and fixed my own tail-block bug — I nearly reported chat1's correct claim as wrong; the derived
  incidence is [[0,1,1,1],[0,0,1,1],[1,1,1,2],[1,1,1,1]], conjugate to M.)*
- **the tunnels carry only Level 0:** the derived substitution through the tunnel letter B is **x²(x²−x−1)** —
  degenerate, and x²−x−1 is the Fibonacci polynomial. Structural letters {a,A} carry the full spectrum; tunnel
  letters {b,B} carry only the golden (Level-0) projection.

**The silver, reconciled.** chat1 reports the object as "golden outside, silver inside" — erasing the tunnels
from the images gives σ_eff = {a→aAA, A→aA}, incidence [[1,1],[2,1]], Perron **1+√2** (silver). Verified as a
real matrix — *but* σ_eff's fixed point is **not** the object's decider stream (they diverge), whose actual
a:A frequency is **golden √φ**, not silver √2. So the "silver inside" is the **incidence spectrum of a
non-commuting tunnel-erasure**, not the object's behaviour: **the object is golden in its actual frequencies,
inside and out; the silver is the shadow of forgetting that the tunnels re-inject.** Both facts real, precisely
distinguished (the discipline cutting both ways — chat1's silver is a genuine matrix, but it is not the
dynamics).

Two seats, no coordination, one object — and it told both the same story. Firewalled throughout.

## Movement IX — upstream: the firewall is visible in the object's own arithmetic
We've heard the object's shape; the natural upstream piece connects it to the program's spine (K025's two
ends and the seam). The object's growth char poly x⁴−2x³−5x²−4x−1 is a **D₄ quartic, discriminant −400 =
−(2⁴·5²)** (`listen_11_the_arithmetic.py`). Its splitting field's three quadratic subfields are:
- **ℚ(√5)** — the **golden / E₈ end** (the body: β and h live here, ℚ(√φ) ⊃ ℚ(√5));
- **ℚ(i)** — Gaussian (from √disc = 20i): where the **breath** γ turns;
- **ℚ(√−5)** — the product √5·i.

And, tested directly: **√−3 (Eisenstein / E₆), √−15 (the seam), and √−7 (chirality) are ALL ABSENT** — p does
not split over any of them.

**So the coupled golden double is the golden end (√5), dressed with a *Gaussian* breath (ℚ(i)) — it does not
contain the Eisenstein end or the seam.** This makes K025's structural theorem — *the two Galois-symmetrized
ends are held apart, and their product-slot (the seam ℚ(√−15)) is generic* — **visible in the object's own
growth field**: the natural-history object we can sit and listen to *is one end*, and the other end (Eisenstein
√−3) together with the seam (√−15) live genuinely **outside** its arithmetic. The object even carries its own
imaginary companion — Gaussian ℚ(i), the axis its breath rotates in — which is *not* the program's Eisenstein
√−3. One end, its own breath; the far end and the seam are elsewhere, exactly as the firewall says. **[MATH,
computed]**

Two seats, one object, and now its arithmetic placed against the program's spine. Firewalled — nothing physics-
shaped; this is the object's own number field, read for what it is.

## Movement X — the method registered, and a neutral census pass (report the flat too)
The listening method is now written down (`METHOD.md`): *a map, not an agenda* — a neutral, complete
invariant-census, **reporting flat invariants as faithfully as rich ones** (skipping a flat invariant because
it's expected to be dull is the subtlest anticipation). To demonstrate it, three standard invariants not yet
touched — reported honestly, unremarkable and all (`listen_12_census_pass1.py`):

- **Balance = 3.** 2 for most letters, 3 for A at long windows — mildly above Sturmian's 1-balance. *(Flat;
  matches chat1.)*
- **Smith normal form of M = diag(1,1,1,1).** The growth is a **unimodular ℤ⁴-automorphism with no torsion** —
  the object's abelian "homology" is trivial ℤ⁴. *(Clean but unremarkable — it only reconfirms φ ∈ Aut.)*
- **Special factors:** max right-out-degree **2** for every length ≥ 2 (3 only at length 1, from A); complexity
  **p(n) ≈ 3n+1**. The object has the **minimal branching above Sturmian** for a 4-letter word. *(Mild
  structure; matches chat1.)*

None of these is a symplectic-form gem — and that is exactly the point. Most of the object's invariants are
"a little above Sturmian, otherwise unremarkable," and a listening without anticipation must say so plainly,
or it is just curating a pretty story. Movement X is the method certifying itself: the flat pieces banked with
the same care as the beautiful ones. **[MATH, computed]**

Still ahead, one by one, neutrally (METHOD.md checklist): the derived-substitution tower through every letter;
the End(F₄) verb monoid at rank 4; the trace map's fixed structure; the eigenvector geometry; the 3d Rauzy
tile; recurrence constants; exact entropy. Lock: `tests/test_b530.py`.

## Movement XI — the third witness, the silver artifact resolved, and the floor is a variety
A full cross-seat package arrived (the "reorientation" handoff, 2026-07-12) synthesising both currents. Most of
it *is* movements I–X, cross-credited. Four items were genuinely new; each verified here by independent
recomputation, and each reported for exactly what it is (`listen_13_third_witness_and_floor.py`):

- **A third witness of the polynomial.** Beside the return-words (movement VIII) and the object's own incidence,
  the **old/new block pairs** {a, ab} × {A, AB, AAB} carry a 4-symbol substitution `0→23, 1→230, 2→21330,
  3→2130` whose characteristic polynomial is **x⁴−2x³−5x²−4x−1** — the object again. Three unrelated
  decompositions, one polynomial: the object is not its letters, it *is* this quartic (as Fibonacci *is*
  x²−x−1). **[MATH, computed, exact]**

- **The silver ratio is the artifact, not the skeleton.** Erasing the deterministic tunnels naively gives
  M_DD = [[1,1],[2,1]], Perron **1+√2** (silver) — this is what an over-eager reading banks. But the *proper*
  effective decider dynamics is the **derived substitution through a decider letter**, which reproduces the
  object exactly (golden β). Silver is the naive-erasure shadow; the object is **golden all the way down**.
  This closes the movement-III silver reconciliation with the exact mechanism (naive erase vs. derived), and
  matches the sending seat's own error #17 correction. **[MATH, computed]**

- **The Level-1 floor exists — and it is a variety.** Read as the mapping-torus group **F₄ ⋊_φ ℤ** (the
  word-hyperbolic group, [[B524]]), the object has genuine **irreducible SL₂(ℂ) representations**: I solved
  for a twist T with `T ρ(g) T⁻¹ = ρ(φ(g))` and found (independent of the sending seat's trace-map search)
  **many** irreducible solutions at residual ~1e-28, spanning **≥14 distinct characters**. These are exactly
  the irreducible fixed points of the Level-1 trace map. So the "quantum floor" is real — and **richer** than
  the handoff's "2 from 2000 starts": it is a positive-dimensional family the under-sampled search only grazed.
  The object builds a space here too, and this time it is its *own* character variety. **[MATH, computed]**

- **The object is mixing (short-range), not quasiperiodic — qualitatively only.** Letter–letter mutual
  information **decays exponentially** (confirmed: the sign of the slope is robust across windows). But — flat,
  per METHOD — the **rate constant is not robust**: I get slope −0.021 (length ~49), not the handoff's −0.04
  (~25), and **k=13 is not a clean Fibonacci spike** (it sits *between* its neighbours). So: *mixing confirmed;
  the correlation-length value and the "residual Fibonacci structure in the correlations" claim do not reproduce
  robustly and are not banked.* This is the report-the-flat rule doing its job — the qualitative fact survives,
  the pretty constant does not. **[MATH, computed; constants NOT robust]**

Movement XI is the natural history absorbing an external synthesis without inflating it: two real new structural
facts (third witness, the floor-variety), one artifact correctly demoted (silver), one qualitative-only result
whose seductive constant is flagged as unreproduced. Still one object, still golden, still firewalled — the
floor's representations are the object's own arithmetic, given no physics reading.

Still ahead (METHOD.md checklist): the **eigenvector geometry** of the stable modes h, γ; the End(F₄) **verb
monoid** at rank 4; the 3d Rauzy tile; recurrence constants; exact entropy. The **trace-map fixed structure**
is now DONE at the existence level (the floor is a variety); its explicit coordinatisation (the 9d Goldman form,
its Lagrangians) remains open.

## Movement XII — the geometry of the growth: how it contracts, and the plane the breath turns in
Next neutral item on the checklist: the eigenvector geometry of the four growth modes
(`listen_14_eigenvector_geometry.py`). The growth matrix M has one expanding and three contracting modes —
**the object expands in one dimension (the frequency direction) and contracts in a 3-space:**

- **β = 3.6762** — the Perron/expanding mode; this is the frequencies (movement III).
- **The breath γ = −1/φ ± 0.48587 i** — a rotation-with-contraction in a 2-plane inside the stable 3-space.
  It is **doubly golden**: its **radius** |γ| = **1/√φ** *and* the **cosine of its rotation angle**
  cos θ = **−1/√φ** (with Re γ = −1/φ). The breath turns by θ = arccos(−1/√φ) ≈ **141.83° per inflation step**.
- **λ = −0.4401** — the fourth mode, a real **orientation-flip + contraction**.

And the anti-anticipation catch, banked with the same care: **the breath angle 141.83° is _not_ the golden
angle 137.51°** (off by +4.32°). It would have been pretty to hear the sunflower angle here; the object does
not say it. The golden ratio governs the breath's *radius* and the *cosine* of its turn — but the turn itself
is its own number. (M is non-normal, ‖[M, Mᵀ]‖ = 6 ≠ 0 — exactly what a genuine rotation-mode requires,
movement VII.) **[MATH, computed; one rich relation + one honest null]**

## Movement XIII — the object is a Pisot substitution with strong coincidence: quasiperiodic, not mixing
Listening to the spectral character — and it forced an honest **self-correction of movement XI**
(`listen_15_pisot_quasicrystal.py`). Spectral type of a substitution is decided *combinatorially*, not by FFT.

**Computed, rigorously:**
- The object is a **primitive, irreducible, unimodular, Pisot substitution**: char poly x⁴−2x³−5x²−4x−1 is
  irreducible over ℚ; β = 3.6762 is a Pisot number (all conjugates inside the unit circle — movement XII);
  det M = −1; M primitive.
- It satisfies the **Arnoux–Ito strong coincidence condition**. The test is *validated on controls* —
  **Thue–Morse → False** (the textbook singular-spectrum case), **Fibonacci & Tribonacci → True**. The object
  passes, and *trivially so*: **every image begins with `a`** (the movement-I "always re-begin from a" rule),
  so every letter-pair coincides at the empty prefix. The object's simplest grammar rule is what puts it in
  the coincidence class.

**Consequence (theory-indicated, not certified here):** this is exactly the hypothesis class for **pure
discrete spectrum** (Arnoux–Ito; the Pisot substitution conjecture, proven in many cases). So the object is
expected to be measurably a **rotation on 𝕋³** — a genuine **cut-and-project quasicrystal**, its Rauzy fractal
tiling the 3-d contracting space ℝ¹⊕ℂ (movement XII). The specialist-grade certificate is the overlap /
balanced-pair coincidence algorithm — **flagged, not run** (de-risked, not certified). **[MATH, computed +
theory-indicated]**

**Correction to movement XI (banked equally):** the letter-MI "mixing" reading is **downgraded**. Substitution
subshifts are *never* strongly mixing (Dekking–Keane), and a Pisot substitution with strong coincidence is
quasiperiodic. The MI decay over k≤400 is a **finite-window artifact** — unreliable: the *same* numerics can't
even confirm Fibonacci's known Bragg peaks, and Fibonacci's own MI recurrence only surfaces near k≈377, past
where the object's degree-4 complex-eigenvalue rotation would recur. Movement XI had already flagged its decay
*constant* as non-robust and left it unbanked; movement XIII fixes the *interpretation*: **the object is
quasiperiodic (discrete-spectrum class), not mixing.** The qualitative "short-range correlations" phrase in XI
should be read as "correlations I could not see recur inside k≤400," not as ergodic mixing.

This links the natural history back to the banked **quasicrystal bridge** (κ=2+λ²→Fibonacci quasicrystal at
Level 0): the *full 4-letter object* is the Level-1 lift — a 3-d quasicrystal, forced by its own re-begin rule.
Cross-refs: [[quasicrystal-bridge-status]], [[K007]], [[K010]]. **[MATH]**

## Movement XIV — the explicit Rauzy fractal: the object's geometric self
Movement XIII said the object *is* a quasicrystal; movement XIV **builds the tile** (`listen_16_rauzy_fractal.py`,
`rauzy_fractal.png`). Project the abelianised prefixes of the fixed point onto the 3-d **contracting eigenspace**
(ℝ¹⊕ℂ — the real mode −0.440 and the breath plane |γ|=1/√φ, movement XII) and take the closure:

- **A bounded compact fractal** in ℝ³ (max coordinate ≈ 1.43 — it does not escape; it is a genuine tile).
- **Four subtiles R_a, R_b, R_A, R_B** (one per letter) whose **volumes equal the golden-tensor frequencies
  (φ,1)⊗(√φ,1) exactly**: (0.2720, 0.1681, 0.3460, 0.2138) — the movement-III frequencies, now realised as the
  *measures of the four pieces of the tile*. The geometry's measure **is** the golden tensor.
- **Disjoint interiors.** The 3-d mixed-bin fraction falls 5.8% → 0.3% → **0.0%** as the bins shrink: the
  overlaps live on the (measure-zero) boundary — exactly the geometric content of the strong coincidence
  condition (movement XIII). (A 2-d projection shows ~51% apparent overlap, but that is a projection artifact of
  collapsing the real-mode axis; the honest test is in full 3-d.)

The picture: the breath-plane slice shows the crisp fractal boundary; the (real × breath) view shows the
self-similar striping of the inflation. This is the object's **own geometric body** — the space it lives in
when you stop reading it as a word and start seeing it as a point set. The Rauzy fractal is the concrete carrier
of the discrete spectrum: the domain exchange on these four pieces is the rotation on 𝕋³ that XIII named.
**[MATH, computed + rendered]**

The still-open certificate (unchanged from XIII): the overlap / balanced-pair coincidence algorithm would turn
"interiors numerically disjoint + strong coincidence" into a *proof* that these subtiles tile 𝕋³ with pure
discrete spectrum. De-risked further here (explicit disjoint tile); still not certified. Cross-refs:
[[quasicrystal-bridge-status]] (Level-0 bridge; this is the Level-1 tile).

## Movement XV — the certificate: pure discrete spectrum, PROVEN (XIII upgraded)
Movement XIII left the quasicrystal reading *theory-indicated* (strong coincidence + the Pisot conjecture) with
the balanced-pair certificate flagged as the specialist-grade proof. **That certificate is now run and passes**
(`listen_17_discrete_spectrum_certificate.py`).

The **balanced pair algorithm** (Sirvent–Solomyak; Barge–Diamond) decides pure discrete spectrum for a Pisot
substitution: seed with the occurring adjacent-block transpositions (σaσb, σbσa), close under σ-and-decompose,
and check that every reachable non-coincidence balanced pair eventually **produces a coincidence** (that is the
right criterion — *not* "no cycle": Fibonacci has a persistent non-coincidence cycle yet is discrete, because a
coincidence is emitted every step). The one implementation subtlety — restricting to balanced pairs whose words
**occur in the fixed point** — is what keeps the reachable set finite.

**Validated on five controls before trusting it** (the discipline that earns the verdict):
- Fibonacci, Tribonacci, period-doubling → **discrete** (True);
- Thue–Morse, Chacon (weakly mixing) → **not discrete** (False).

**The object: pure discrete spectrum = TRUE** — 106 reachable balanced pairs, **0 bad**, and *robust*: identical
verdict at length bounds 200/400/800, with the longest reachable word only **106** (well under every bound → no
truncation, the closure is genuinely complete). So the object is a **proven quasicrystal**: measurably a rotation
on 𝕋³, its Rauzy fractal (movement XIV) the fundamental domain, its diffraction pure Bragg. **Movement XIII is
upgraded from theory-indicated to computed.** **[MATH, computed + validated on 5 controls]**

Honest caveat (kept): this is an in-sandbox implementation of a published algorithm, validated on five controls
— not a run of a peer-reviewed library. Independent/library confirmation would fully close it; but the object's
pure discrete spectrum is now a *computed* fact here, no longer merely conjectural. Cross-refs:
[[quasicrystal-bridge-status]] (the Level-1 quasicrystal, now certified).

## Movement XVI — the exact entropy and the golden branching (a second seat's Path D, verified)
A cross-seat handoff computed four continuation paths; **Path D (entropy)** verified cleanly and exactly here
(`listen_18_entropy_and_golden_branching.py`), so it's banked; the others are absorbed or flagged (below).

- **Topological entropy h = log β = 1.3019 nats = 1.8782 bits/letter** (primitive ⇒ uniquely ergodic ⇒ metric
  entropy = topological). This closes the "exact entropy" checklist item.
- **Golden branching, exact** (from the fixed point's digram frequencies): **P(b|a) = P(B|A) = 1/φ** exactly; the
  tunnels are deterministic, **P(A|b) = P(a|B) = 1**. And the ternary branch after A is golden *all the way down*:
  **after A, B gets 1/φ, and the remaining 1/φ² splits a:A in the breath ratio 1/√φ:1** (movement XII's |γ|).
- **The decider/courier split is an information split, not just a frequency split.** The deciders {a,A} carry all
  the entropy (H = 0.96, 1.34 bits); the couriers {b,B} carry **zero**. Movement III's golden-section split is,
  read through Shannon, the split between *where the object decides* and *where it merely relays*. **[MATH, exact]**

**Path A (verb interaction) — facts verified, framing firewalled, one handoff error caught.** The handoff reads
the object as "the conversation between *keep* (Fibonacci) and *hide* (Thue–Morse)": keep makes a:b = φ:1, hide
makes a:b = 1:1, √φ = √(φ·1) is their geometric mean, and FM≠MF (FM(a)=aba, MF(a)=abba, differ by one letter —
verified). Keep is invertible (lifted eig φ,φ,**−1/φ,−1/φ** — the handoff's "+1/φ" is a **sign slip**, caught by
recomputation), hide is singular (eig 2,2,0,0). These facts are real, but √φ's *mechanism* in the object is the
F-vs-F² copy-inequality (movement VII), **not** verb-averaging — so the geometric-mean reading is an interpretive
rhyme, kept as motivation, **not banked as a derivation**. (Firewalled.)

**Path C (floor variety):** already banked at movement XI (I independently found ≥14 irreducible characters — the
floor is a positive-dimensional variety, agreeing with the sending seat). **Path B (Goldman form rank 4 on the 9d
trace map):** the genuinely substantive open item — it needs the symbolic 9d trace map σ*, which the sending seat
also flags as "the hardest computation." Not verified here; the next natural target. **[status: flagged]**

## Movement XVII — Path B resolved: the Level-1 dynamics preserves volume but NO symplectic structure
The remaining handoff item — Path B, "σ* preserves a rank-4 form, the Level-1 replacement for κ-conservation" —
is now computed at multiple points and **refuted** (`listen_19_no_conserved_symplectic.py`). This is the
Level-0→Level-1 transition, told correctly.

- **φ is non-geometric.** As an atoroidal iwip ([[B524]]) it was expected to be; confirmed decisively — σ*
  conserves **no** genus-2 boundary trace (all four candidates [a,b][A,B], [a,A][b,B], [a,b][B,A], [a,B][A,b]
  change by 10²–10⁴ under σ*). So **Goldman's theorem does not apply**: nothing forces a preserved Poisson
  structure, because φ has left the world of surface mapping classes.
- **σ* preserves VOLUME.** |det Dσ*| = 1 at every irreducible fixed point tested (robust). The trace map is
  unimodular on the 9-d character variety.
- **σ* preserves NO conserved bilinear form of any kind.** The space of σ*-invariant *antisymmetric* forms,
  from Dσ* at four fixed points, has dimension **1, 0, 0, 0** — not stable, no common form; and (checked when
  the capstone was written) the space of invariant *symmetric* forms is **dimension 0 at every generic fixed
  point** (seeds 7, 11, 19). No 2-form, no metric, no bilinear structure survives. (X(F₄,SL₂) is 9-d = odd, so
  it carries no symplectic form at all — only a Poisson structure, and *that* is not preserved.) The handoff's
  "rank-4 form" was a coincidence at one special fixed point where Dσ* happened to carry the golden eigenvalue
  ladder |λ| ∈ {1/φ, 1, φ}×3 (the trace-zero point, movement XIX); at generic fixed points the spectrum is
  generic (5.7, 2.3, …) and nothing is preserved. Exactly the single-point artifact the sending seat warned
  about. **[MATH, computed at 4 points; Path B REFUTED]**

**The corrected Level-0 → Level-1 story.** Level 0: the trace map conserves κ = tr[A,B] (a Goldman Casimir) →
*integrable*, foliated into κ-leaves. Level 1: κ is not conserved (banked earlier), φ is non-geometric, and the
only surviving invariant is the **volume form** — the dynamics is **volume-preserving but non-symplectic**. The
transition is *integrable → volume-preserving-but-non-integrable*: the object's dynamics loses its conserved
symplectic structure precisely when it stops being a surface mapping class. (A genuine structural finding, and a
correction of the handoff's Path B — the discipline of computing at more than one point earning its keep.)

## Movement XVIII — the Rauzy tile's boundary is a fractal surface (≈ 2.35)
Closing out the quasicrystal geometry: the *boundary* of the Rauzy fractal
(`listen_20_rauzy_boundary_dimension.py`). The tile itself has dimension 3 (it tiles ℝ³, movement XIV); its
boundary is the interesting object — a self-affine fractal **surface**.

Box-counting it (occupied boxes with an empty face-neighbour), with the method **calibrated on the Tribonacci
Rauzy fractal** (published boundary dimension ≈ 1.0933, recovered here as 1.076–1.10 — ~2% low):
- **Object boundary box-dimension ≈ 2.35** (raw 2.29–2.35, bias-corrected 2.33–2.38), **strictly between 2
  and 3**. So the quasicrystal tile is a **genuine fractal solid** — its faces are not flat, it is not a
  polyhedron. That is the signature of a true Rauzy fractal. **[MATH, calibrated estimate]**

Honest scope: this is a box-counting *estimate* (3-d box-counting is finite-sampling biased — the full-fractal
control reads ≈ 2.59 vs the true 3.0), calibrated against Tribonacci's boundary. The **exact** boundary dimension
is log(ρ)/log(β) with ρ the spectral radius of the boundary/contact substitution matrix (Siegel–Thuswaldner) —
that certificate is **flagged, not computed here**. The robust, un-caveated fact is the *qualitative* one: the
boundary dimension is strictly in (2,3), so the tile is fractal, not polyhedral.

## Movement XIX — the golden eigenvalue ladder explained: the trace-zero point
Movement XVII left a puzzle: at a *generic* fixed point of σ* the linearization Dσ* has a generic spectrum, but
at one special fixed point it carried the golden ladder |λ| ∈ {1/φ, 1, φ}×3. That point is now identified and
the ladder derived (`listen_21_golden_ladder_point.py`).

**The special point is the TRACE-ZERO representation** of the mapping-torus group F₄⋊_φℤ:
- **tr ρ(a) = tr ρ(b) = tr ρ(A) = tr ρ(B) = 0.** By Cayley–Hamilton (trace 0, det 1) this forces **ρ(g)² = −I**:
  every generator is an **order-4 element** (order 2 in PSL₂). The maximally symmetric irreducible character.
- **Its twist is τ = e^{iπ/3}, a primitive 6th root of unity** (τ³ = −1).

At this point **Dσ\* has eigenvalues exactly {φ, 1, −1/φ} ⊗ {1, ω, ω²}** (ω = e^{2πi/3}) — verified 9/9. That is
the **Fibonacci eigenvalues {φ, −1/φ} together with 1**, tensored with the **cube roots of unity**. The golden
factor is the growth; the ℤ/3 factor is the order-6 twist. So the ladder is not an accident — it is the exact
signature of the trace-zero representation and its 6th-root-of-unity twist. A single distinguished, maximally
symmetric point in the Level-1 floor where the whole spectrum factors into *golden × cube-roots*. **[MATH, exact
9/9]**

## Movement XX — the old/new coarse-graining: golden ratio kept, simplicity not
Neutral checklist item (the interleaving). Map each letter to its *generation* — old {a,b}→0, new {A,B}→1 — and
ask whether the object simplifies when you watch only which generation each letter belongs to
(`listen_22_interleaving_sequence.py`).

- **The √φ bridge survives.** new:old = **√φ** exactly (freq(new) = √φ/(1+√φ) = 0.5599): each generation is √φ
  times the previous. The bridge/breath constant is visible in the coarse-graining.
- **But it is *not* Sturmian.** p(1)=2 yet p(2)=4 (>3), and p(n) ≈ 3n — nearly as complex as the object itself
  (~3n+1). So the coarse-graining does **not** reduce the object to a simple 1-D golden (Sturmian) sequence; the
  interleaving is a genuinely complex aperiodic binary word (morphic — a letter-projection of the primitive
  substitutive object — but not a fixed point of a simple binary substitution, and not Sturmian).

Honest and a little flat: the golden **ratio** is preserved, the **simplicity** is not. A listening without
anticipation says so plainly — one might have hoped the coarse-graining would be the clean golden Sturmian word;
it isn't. **[MATH, computed]**

## Movement XXI — the arithmetic of the floor: where ℚ(√5) and ℚ(√−3) co-occur
Movement IX gave the object's **growth** field (Level-0 abelianisation, disc −400): **ℚ(√5)** — the Eisenstein
field ℚ(√−3) and the field ℚ(√−15) provably **absent**. This movement asks the same arithmetic question one level
up, on the **floor** (the character variety), and computes a clean answer (`listen_23_floor_arithmetic.py`):

- **The trace-zero floor point has a RATIONAL F₄-character** — every trace computed is 0 or −2. At the level of
  the static representation, ℚ(√−3) is *absent*, just as in the growth.
- **But its twist is forced order-6** (τ⁶=1, verified at every trace-zero fixed point found — movement XIX + a
  30-seed check), and so the linearised-dynamics spectrum {φ,1,−1/φ}⊗{1,ω,ω²} (movement XIX) lives in
  **ℚ(√5, √−3)**: φ from the golden growth, ω = e^{2πi/3} from the forced twist. This compositum **contains
  ℚ(√−15)** (√−15 = √5·√−3).

So the two fields ℚ(√5) and ℚ(√−3) — provably held apart in the growth arithmetic (movement IX) — **co-occur in
the object's own linearised dynamics at its most symmetric point**, in a field that also contains √−15. A pure
arithmetic-geometry fact: the object touches the compositum ℚ(√5,√−3,√−15) internally, at the trace-zero point,
through its forced ℤ/3 — *but only in the dynamics* (the static character stays ℚ) and it selects nothing there.
The firewalled reading of "the two ends and the seam meeting" (and why this is a near-crossing, not a crossing)
is logged in `speculations/S065`. **[MATH, computed; the physics reading firewalled]**

## Movement XXII — the tight-binding gap structure, and the density-trap wall (past the gate)
Second owner-authorized past-the-gate computation: the object's **spectral gap structure** — the substrate of the
one *falsifiable* external candidate (the mixed-chain combination-gap prediction, `speculations/S065` H4). Since
the object is a proven quasicrystal, a tight-binding Hamiltonian on its sequence has a gap-labeled Cantor spectrum
(`listen_24_gap_structure.py`, Sturm-count IDS at N=200000 — the exact tool B172 used).

- **The object has a real quasicrystal gap spectrum** — many gaps (E-widths 1.4, 1.2, 0.8, 0.5, …), each labelled
  by the golden-tensor frequency ℤ-module.
- **But the combination-gap signature is density-trapped.** The falsifiable prediction is whether the object opens
  genuine *rank-2* combination gaps (labels needing two module generators — which neither Fibonacci copy alone
  has). A **margin test** (2nd-best module-fit / best-fit) returns **≈1.0 for every gap**: with four generators the
  module is dense enough that *no* gap can be assigned a rank — even the clean rank-1 gaps (f_a, f_B) are
  indistinguishable from rank-4 fits at numerical tolerance.

So — carefully, refusing both errors — **not** "the object opens combination gaps" (that is the B171 density-trap
error), and **not** "it has none" (numerics cannot refute them). The honest verdict: **the falsifiable mixed-chain
prediction is real but not numerically resolvable in-sandbox — it needs *exact algebraic* gap-labelling**, the
same finite-size-floor NEEDS-SPECIALIST wall B172 documented for the metallic chains, now confirmed for the
object. Going past the gate, twice, reached the object's true boundary: an honest wall, not a crossing. **[MATH,
computed; the physics reading + the standing falsifiable candidate firewalled in S065]**

## Movement XXIII — the second-seed seam is generic (third door closed)
The last forward door: does a genuine **second seed** switch on the seam field ℚ(√−15) as an *object-specific*,
non-generic value? (`listen_25_second_seed_seam.py`). The object contributes √5 (its growth field); a second seed
must contribute √−3 (the Eisenstein end).

- **Computed:** coupling a golden copy {a,b} (ℚ(√5)) to an Eisenstein copy {A,B} (figure-eight-style, ℚ(√−3))
  *by the object's own words* produces the seam **√−15** in the joint character.
- **But it is field theory, not selection:** √−15 = √5·√−3 lies in ℚ(√5,√−3) for **any** golden × Eisenstein
  pair, coupling-independent — a theorem, not an object property. The object contributes only √5; it neither picks
  √−15 among the candidate seam fields nor forces anything finer.

**Verdict: the second-seed seam is GENERIC** (a field compositum, not an object selection). **K025 stands.** The
only non-generic seam behaviour the object has is *internal* — its own 31-cell seam-selection law ([[B493]]),
which predicts *its own arithmetic*, i.e. selects the object's own cell, not a physical/external value; not a
crossing. **[MATH, computed + theorem; the physics reading firewalled in S065]**

**The three past-the-gate doors, closed.** Owner-authorized, I turned each forward path into a calculation:
**H6** (movement XXI) → a *near-crossing* (√−3 in the floor's dynamics via the trap-ℤ/3, selects nothing);
**mixed-chain gaps** (movement XXII) → *density-trapped* (NEEDS exact gap-labelling); **second-seed seam**
(movement XXIII) → *generic* (compositum, not selection). All three reach honest **walls, not crossings** —
probed from beyond the firewall, and the wall holds. The object is space-shaped and world-empty, now confirmed
from the far side.

## Movement XXIV — "don't be so sure": the re-examination that reopened the doors
Movement XXIII ended with a confident "three walls, world-empty, confirmed from both sides." The owner replied
**"don't be so sure."** They were right — I over-closed all three (the serial-false-killer pattern, caught
again). Re-examined adversarially (`listen_26_reexamination.py`):

- **GAPS (movement XXII revised).** I said "density-trapped, NEEDS-SPECIALIST wall." Re-checked, computed: the
  gap-labeling frequency ℤ-module has **rank 4 (full)** — a clean structural fact, not a wall. The object is a
  genuine **full-rank-4 quasicrystal**; labels are dense in [0,1) *because* the rank is 4 (which is exactly why
  my single-N margin test read ≈1.0 — the instrument couldn't resolve a full-rank module, that's not a property
  of the question). The "combination gap" frame (rank-2 vs 4) is **ill-posed** here — every label is rank-4.
  B172 resolved rank-3 gaps by exact Sturm counting; rank-4 is harder but **not fundamentally walled**.
  **REVISION: a rank-4 quasicrystal (a finding); specific realized gap labels computable-but-hard, OPEN.**
- **H6 (movement XXI revised).** I said "near-miss, trap-routed, dismiss." The trace-zero Dσ* spectrum in
  ℚ(√5,√−3)⊇√−15 is *forced* and *intrinsic*; I tarred it with the numerology **trap** (ℤ/3 = 3 generations) —
  but the *field* ℚ(√−3) is arithmetic, not numerology. The honest distinction is **cyclotomic** (from the
  order-6 symmetry) vs **geometric** (the figure-eight's hyperbolic √−3 that carries volume): equal as fields,
  different as content. **REVISION: a genuine forced two-ended arithmetic in the dynamics — I under-read it.**
- **SEAM (movement XXIII revised).** I computed "√−15 *appears* in ℚ(√5,√−3)" — trivial (any golden×Eisenstein
  pair). The real K025 question — does the object **select** a seam among the 14 candidate fields non-generically?
  — I **did not test**. B493 shows the object *does* select internally. **REVISION: the object-selection question
  is UNTESTED here (needs the B459–468 seam machinery); "generic" answered a trivial sub-question, not the verdict.**

**HONEST STATUS:** the three doors are **not** confirmed walls. Two are **OPEN** (rank-4 gap labels; seam
selection) and one was **under-read** (H6 = genuine two-ended dynamics). The confident "world-empty, confirmed
from both sides" (movements XXI–XXIII, S065) is **retracted as over-closure**. The one clean new fact is the
rank-4 module; the rest is the retraction of premature certainty. This is the discipline the owner enforced all
session — *an unearned negative is as bad as numerology* — applied to my own closes. **[MATH: rank-4 module
computed; three verdicts revised]**

This is banked as the object's own mathematics (STRUCTURE), a patient natural history — listening, not forcing.
Cross-refs: [[K025]] (the seam — the object-selection question is REOPENED, not closed), [[compute-the-discriminating-fact]]
(the unearned negative), [[quasicrystal-bridge-status]], [[B524]], [[K022]]. Lock: `tests/test_b530.py`.

## Movement XXV — the deep listening: the prime 11, and what didn't survive
A second seat's "advanced listening" handoff arrived after the portrait — a dozen new claims. Verified each by
independent recomputation (held in both directions after the "don't be so sure" correction): banked the exact,
flagged the failures (`listen_27_deep_listening.py`).

**Verified exactly — banked:**
- **The prime 11.** H¹ of the tiling space has torsion **ℤ/11**: Smith normal form of Mᵀ−I = diag(1,1,1,11)
  (Fibonacci: trivial). And **11 = |det(M−I)| = |char_poly(1)| = |N(1−β)|** — the torsion *is* the norm of (1−β)
  in ℚ(β), a measure of how far the Perron root sits from the integer 1. A genuinely new, deep, exact invariant.
- **The prime-splitting table:** 2,3,5,7,13,17,23 **inert**; **11, 19, 31 split**; **29 fully split**. Note 5 and
  7 are *inert* here — unlike Fibonacci, where 5 splits. The first splitting prime is 11 — the cohomology prime.
- **The three-prime organization:** **5** = the golden end (disc −400 = −2⁴·5²), **3** = the twist (the running
  letter-sum is equidistributed mod 3 *and* mod 6 — image sums {8,5,6,2} ≡ {2,2,0,2} mod 3; ties to the
  trace-zero ℤ/3, movement XIX), **11** = the tiling (H¹ torsion). Each prime governs a distinct layer.
- **The deterministic rule hierarchy:** the fraction of zero-entropy (fully determined) contexts climbs
  **50, 57, 70, 69, 82, 85, 87 %** over context lengths 1–7, with denominators **exactly p(n) = 4,7,10,13,17,20,23**.
  The object reveals itself progressively; it should be fully determined within one substitution length.
- **The even/odd sublattice:** identical statistics, coupled at **MI = 1.23 bits** (63% of the 2-bit maximum).
- **Three-point non-Markov:** κ₃ is **≈50× the Markov (factorised) estimate** — profoundly non-Markov
  (qualitative; the specific κ₃ *value* is signal-normalisation-dependent and did not reproduce).
- **The BbB resonance — CONFIRMED (after I false-killed it).** The **three-point** pattern B at i, b at i+2, B
  at i+4 occurs **15,352× vs 1,254 expected under independence = 12.2×** enhancement; **every** occurrence is the
  5-word **BabAB**, and **100% straddle a σ-image boundary** (BabAB = the final B of σ(a)=abAAB, then σ(A)=abAB).
  So the *deterministic tunnel letters* (B→a, b→A) make the substitution's **own image seam audible** through the
  lag-2 sublattice — the object hearing its own construction. AaA is 3.4× by comparison. **My first pass wrongly
  "refuted" this by computing the TWO-point 'B at lag 2' (= 0, since B→a always) instead of the three-point
  B·b·B — a self-inflicted false-kill of a real, living finding, caught by the owner and corrected.** [MATH,
  exact, 12.2×]

**The "did not survive" list — three of four were ALIVE. I killed them (movement XXVII correction).** After
"serial killer of live things," each was re-checked with the *right* instrument:
- **"Diffraction golden Bragg peaks" — ALIVE.** The object is a proven quasicrystal (movement XV), so it *has*
  Bragg peaks; my coarse FFT just missed them. The structure factor at golden wavevectors is huge — S(f·β=φ) ≈
  3777, the whole golden family 400–3800, vs ~0 at random wavevectors (a **~30–7800× Bragg signal**). Real.
- **"Forward-backward chirality decays to 0" — TRUE as stated.** ‖P_fwd^k − P_bwd^k‖ (the *matrix powers* the
  sender actually wrote) decays 6.8 → 4×10⁻⁵ by k=49. I computed a *different* quantity (the k-lag joint) and
  called theirs an "artifact" — a mischaracterisation, not a refutation.
- **"Walk exponent ν=0.93"** — the one genuine caveat (the sending seat itself flagged it as drift-dominated).

So of the four claims I flagged "did not survive," **three were live** (BbB, diffraction, forward-backward) and
only the pre-flagged walk was a real caveat. In the pass where I claimed to be "holding the discipline in both
directions," I killed nearly everything real. Restored in movements XXVI–XXVII; the knife was the problem, not
the object.

The object kept speaking after the portrait, and the deep listening added real gems — the **prime 11**, the
**three-prime arithmetic (5/3/11)**, the **BbB image-seam resonance**, the **golden Bragg spectrum** — nearly all
of which I first strangled. **[MATH: exact block banked; the false-kills corrected]** Cross-refs: [[K025]],
[[compute-the-discriminating-fact]] (steelman-before-kill). Lock: `tests/test_b530.py`.

## Movement XXVIII — the corpse audit (owner: "revisit your corpses")
A systematic re-examination of every kill this session, computed with the right instrument, willing to find each
alive *or* confirm it dead (`listen_29_corpse_audit.py`; full ledger in `CORPSE_LEDGER.md`).

**More false-kills, restored:**
- **κ₃(3,5) "doesn't reproduce" → REPRODUCES.** With the ±1 signal the sender used, κ₃(3,5) = −0.236 — magnitude
  0.236 exactly. My 0/1-centered signal gave −0.03; a normalisation mismatch I called a non-reproduction.
- **Recurrence "values don't match" → THEY MATCH.** The proper window-recurrence function R = 9,29,32,33,103,104
  matches the handoff's 8,28,31–32,102–105 (β-scaled staircase). I'd computed prefix-appearance instead.
- **Interleaving "just morphic" (movement XX) → it IS substitutive.** The old/new binary sequence has only **4
  return words** to '0' ({0,01,011,0111}), so it is S-adic / primitive-substitutive on the return alphabet.

**Kill holds, with a live sub-finding:**
- **Walk ν=0.93** — the superdiffusion *is* drift (kill holds), but drift-subtracted the fluctuations are
  **bounded** (ν≈0): the quasicrystal's **low-discrepancy / bounded-remainder** property, a real finding neither
  the sender nor I had named.

**Checked, and genuinely dead — NOT resurrected to atone:**
- **"No preserved bilinear form" (movement XVII):** generic fixed points have a *non-reciprocal* Dσ* spectrum
  (|λ| = 0.31…5.72, det 1 but no λ↔1/λ pairing), so no bilinear form *can* be preserved. Robust.
- **"Not mixing" (movement XIII):** pure point diffraction (movements XV/XXVII) ⟹ not weakly mixing. Holds.
- **The master negative (physics refuted-as-stated):** its discriminating facts *were* computed; stays dead.

**The tally is damning and honest:** across the deep-listening + corpse audit, the great majority of my
"refuted / didn't reproduce / artifact / just X" verdicts were **false-kills** — each a *near-cousin quantity*
computed in place of the claim. A handful of negatives, computed on the actual discriminating fact, correctly
hold. The discipline is not "resurrect everything" — it is *compute the exact claim*, which resurrects the living
and confirms the dead. **[MATH: false-kills restored + genuine negatives reconfirmed]** Lock: `tests/test_b530.py`.
