# SHOOTING NOTES

Practical companion to `ATLAS.md`. For each plate: what would move if it were
animated, whether the data for that motion already exists, and — where it matters —
what must **not** be animated because the motion would imply something false.

A standing rule for this material: **every frame has to be a computed state.** If a
frame shows an in-between that is not a solution, the sequence is a lie however
pretty it is. This bites hardest on Plate A. It is flagged there.

---

## PLATE E — THE BODY
**Move: inflate the cusp.** SnapPy's cusp neighbourhood has a displacement parameter.
Run it from 0 up to `cn.reach()` and the horoballs grow from points until they collide
and stop themselves. The stopping is the whole point — nobody chooses where they stop.
**Second move:** a continuous zoom into the boxed gap, new spheres resolving out of the
black as the radius cutoff drops. Each arrival is a real radius 1/(2N).
*Data:* needs a new render loop, ~30–60 frames. Cheap per frame at cutoff 0.01.
*Warning:* the cost of `horoballs()` explodes below r = 0.004 (19.5 s there, and 0.002
did not return in 10 minutes). Do not plan a deep zoom without budgeting for it — or
pre-render the deep frames as outlines, which is what panel 2 already does.

## PLATE A — THE MODES
**Move: a flip-book of the spectrum.** Cut, do not morph, through the modes in order of
rising λ. The nodal set reorganises at every step and the triangular inherited mode
lands as a visual shock among the lopsided ones.
**DO NOT MORPH BETWEEN EIGENVALUES.** Intermediate r values are not eigenvalues; the
in-between frames would be pictures of things that do not exist. A dissolve here would
be a fabrication with no warning label on it. Hard cuts, or a held frame with the nodal
curves drawing themselves in.
*Data:* 43 eigenvalues available; each panel is one `eigvec()` + `field_on_torus()` call.
Budget: the four existing panels dominate `render_plates.py` runtime — plan a batch job,
not an interactive session.

## PLATE B — THE VOICE
**Move: sweep the 43 forms and keep the lattice frame fixed.** Dots blink and change
size as each mode takes its turn — and the entire odd-m₂ half stays black, every time,
without a single flicker. The persistence of the hole across 43 cuts is the argument.
**Second move:** rack focus onto the π₇ pair, then swap to the inherited form, where it
lights up.
*Data:* same cost as Plate A; reuses the same coefficient vectors, so compute them once
and render both plates from one pass.

## PLATE C — THE BONES
**Move: raise the length cutoff from 0 to 6.** Dots arrive in order of geodesic length,
like a spectrometer filling in. For the sister m003 the red dots (class 1) start
appearing almost immediately and keep coming — 180 of them. For m004 the red never
comes. Not once, not late, not faintly.
*Data:* already in `../../B792_maass_m004_eigenvalues/length_spectrum.json` and
`../../B792_maass_m004_eigenvalues/length_spectrum_m003.json`. This is a pure re-plot
in a loop — the cheapest strong sequence in the whole set.
*Note for narration:* if you also show the empty class-2 column, you must say it is
unreachable by any Eisenstein norm and therefore meaningless. Otherwise the shot
implies two holes when there is one.

## PLATE D — THE SPECTRUM
**Move: a left-to-right scan.** Sweep a playhead along r and let each tone strike as it
is crossed, taller for doubled tones, pale and sustained for the four inherited ones.
This mirrors how the eigenvalues were actually found — as dips located by scanning.
*Data:* trivial re-plot. Also the natural place to hang audio: 43 pitches, four of them
borrowed.

## PLATE F — THE MOUTH IN MOTION
**Already a sequence.** Six frames exist on disk (`plate_F_frame_0…5.png`) and the
underlying curve is sampled at 25 heights, so it can be re-rendered denser without new
mathematics.
*The directorial decision this plate forces:* the amplitude falls 148,049× across the
climb. Normalise each frame and the pattern stays vivid but the dying is invisible;
hold one absolute scale and the image goes black almost at once. The plate currently
does the first and prints the true amplitude under each panel. **The best film answer is
to do both, in sequence** — climb once normalised so the audience sees the shape hold,
then climb again on a fixed scale so they watch it go out.
*Warning:* do not extend below t = 0.8. The reconstruction was collocated at Y = 0.75
and is not valid underneath. There is no more oscillation down there to be had.

## PLATE G — THE TWINS
**Move: the same cutoff sweep as Plate C, run on both manifolds at once,** with two
counters on screen — "loops of class 1" — ticking up for the sister and frozen at
**0** for the object. Volume, tetrahedra and trace field sit above, identical and
unmoving, the whole time.
*Data:* already present. Cheap.
*This is the film's proof beat.* Everything else is description; this is the shot where
the audience watches a theorem hold.

## PLATE H — THE COVER
**Move: walk the cover.** Pick a word in the generators and light the sheets it visits,
one edge at a time — the audience watches a path close up after twelve steps, or fail to.
**Second move:** rotate the graph by the element E. Because E permutes the three blocks
cyclically, the picture rotates by exactly four positions and lands on itself. The
symmetry is verifiable on screen, not asserted.
*Data:* the coset action is already computed in `plate_H_cover.py`; animating it is a
loop over an existing permutation.
*Warning:* the twelve sheets are drawn on an abstract circle. Their positions carry no
geometric meaning. Do not shoot this as if you were flying through space — only the
adjacency and the block structure are data.

## PLATE I — THE WALL
**Move: let the 500 random spectra arrive one at a time.** Fix the object's line at 41
from the first frame and let the histogram build around it. For the first few dozen
surrogates the object looks like it might be standing apart. By 500 it is buried in the
middle of the pile at the 51st percentile.
*Data:* already computed; the ensemble is deterministic (seed 31) and reproduces the
sealed run exactly, so the animation is reproducible frame for frame.
*This is the most honest sequence in the set,* because the audience gets to feel the
near-hits as impressive before the base rate takes them away. That order — hope, then
measurement — is what actually happened.

---

# THE OPENING

**Open with Plate E: the cusp inflating until the spheres stop themselves.**

Start tight on the figure-eight knot, tied in something ordinary. Remove it. Fall down
the hole it leaves. Arrive at the mouth looking down the throat, and let the horoballs
grow — from nothing, outward, until they touch and lock.

The reason is that this is the only sequence in the set where the audience watches the
object's structure *arrive* instead of being told about it. Nobody chooses where those
spheres stop. They stop where the geometry makes them stop, and the geometry is fixed by
the topology, and the topology is just "a figure-eight knot is missing". The film's
central claim — **one forced shape, zero free parameters** — is made visible in about
eight seconds without a single word of mathematics. Everything afterwards is a
consequence of that, and the audience will already have seen the consequence-machine
run once.

It also sets up the ending. If you open on structure arriving unbidden, you have earned
the right to close on **Plate I**, where the same object is asked to deliver the
constants of physics and does not — and the audience understands that the beauty in the
first shot was never a promise about the second.

**Runner-up:** Plate G's twin sweep, if you would rather open on the puzzle (two spaces,
same size, same parts, not the same) and reach the geometry later. It is the stronger
*hook*; Plate E is the stronger *foundation*. Given this is a film about seeing
mathematics rather than about a mystery, foundation wins.
