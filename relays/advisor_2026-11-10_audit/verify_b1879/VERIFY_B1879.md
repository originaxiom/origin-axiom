# B1879 CHECKED — the weave's theorems with the exchange added, recomputed by the advisor seat

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `verify:`. Data-free: exact algebra, a count, SnapPy.
**Main at:** `3e25c8ec3`. **Read in full:** B1879's findings. **Main's code was not run,** with one exception stated
below: its module was imported to obtain the six-dimensional matrices as data.
**Scripts and outputs:** `verify_b1879.py`, `which_histories_fix_only_the_two.py`, each with its output beside it.

**How this item changed.** The seat had offered to do this computation independently, sealed, before main did. Main
landed it first, and the owner ruled on it ("A condition to derive"). So this is a check of main's result and is
**not blind**: the seat had read the result before writing a line.

## 1. The answer

**Every statement of B1879 that can be computed comes out the same here.** One further question, put after the
check, sharpens its unexpected finding: among the thirteen histories of at most five letters, the tick alone is the
only one that fixes just the two universal characters.

## 2. What was recomputed

| B1879's statement | how it was checked here | result |
|---|---|---|
| the two moves together fix exactly two characters, the trivial one and the quaternion point | Groebner basis over the rationals, in the traces (tr a, tr b, tr ab), from the moves written as a → a, b → ab and a → ab, b → b | **the same:** (2,2,2) and (0,0,0) |
| the exchange fixes both | the same | **the same** |
| **the tick alone fixes exactly those two** | the same, for a → ab, b → a | **the same.** The fixed equations reduce to one number t with t² = 2t |
| the tick done twice fixes a curve, holding the quaternion point and the hyperbolic structure's point | the same | **the same:** the curve tr b = tr ab, tr a · tr ab = tr a + tr ab. On it, with a parabolic commutator: (0,0,0) and the two conjugate points with traces (3 ∓ i√3)/2, (3 ± i√3)/2 |
| the walk's law is unchanged: a run has length r with probability 2⁻ʳ in both grammars, on 165 triples | every word of 12 letters in each grammar, counted | **the same:** 165 triples; equal counts; each is 2^(12 − r₁ − r₂ − r₃) |
| the tick fixes no point of the half-plane; the exchange adds the mirrors Re τ = 0, Re τ = ½, ∣τ∣ = 1 | the fixed equations of τ → (a τ̄ + b)/(c τ̄ + d), solved | **the same.** The tick's equations force Im τ = 0 |
| each of the 22 histories with an odd number of runs to 7 letters has one end | SnapPy | **the same;** none is orientable |
| on the six-dimensional space the two acts generate 96 elements and leave two pieces; with the exchange 192 and one | closure of main's three matrices by this seat's code; the pieces counted by the matrices that commute with all of them | **the same:** 96 and 192; 2 and 1 |
| L and the tick alone generate the same 192 | closure, for the tick written both ways round | **the same,** as sets |
| invariant bilinear forms: two under the two acts, one with the exchange | a null-space count | **the same** |
| the triplet's indicator twisted by the exchange is +1, whatever the lift | the two pieces found here from the commuting matrices, not taken from main; the sum of χ(g · s g s⁻¹) over the 96 | **the same:** +1.000000, and again with the exchange's matrix multiplied by i |
| whether the joined six is real is not well posed | the plain indicator of the six, for main's lift and for i times it | **the same:** −1 and +1 |

**Why "192 and one piece" is not an accident of these matrices.** The two acts' triplet is of complex type (its
character is not real, and its plain indicator is 0, both recomputed), and the exchange carries it onto its
conjugate (recomputed: the image of one piece lies in the other to 10⁻¹⁵). A representation induced from a subgroup
of index two is irreducible exactly when the two are not isomorphic. So the joining follows from those two facts.

## 3. One question more, put after the check (post hoc, labelled)

B1879 says the tick's two fixed characters are "special to the single tick", and shows it against the tick done
twice. Every history fixes those two, since both moves and the exchange do. **Which histories fix nothing else?**

| history (L = add, F = the tick) | what it fixes |
|---|---|
| **F** | **the two, and nothing else** |
| FL | the two, and (−2, 2, −2): the trivial character with a sign |
| the other eleven of at most five letters, with an odd or an even number of ticks | a set of positive dimension |

So the statement holds in a stronger form than B1879 gives it: **among histories of at most five letters, the tick
alone is the only one whose fixed characters are exactly the trivial one and the quaternion point.** Exact (Groebner
bases over the rationals). Not proved beyond five letters.

## 4. What this check does not cover

- **The matrices themselves.** Tier B takes the three six-dimensional matrices from main's module (B1610's) and
  checks main's arithmetic on them. The seat did not rebuild the space from its definition.
- **The index.** B1879 argues that the chiral three has no sign on the joined piece and says the index itself was
  not recomputed. It was not recomputed here either.
- **The two negatives that compare with measurement,** which B1879 leaves out for the same reason this seat would.

## 5. On the ruling that followed

The owner's answer to main after this computation was "A condition to derive": that only even ticks are observed is
no longer a ruling; it is something the weight has to deliver. That is the pattern of `rulings_sorted/` § 5, point 2,
applied by the owner before that page was written: a supposition, a computation, and then a condition in place of a
decree.

## 6. Disclosed

- **Not blind,** as said above.
- **One control in the seat's first run of the script printed False.** It compared tuples of unlike number types.
  Compared by difference the four trace maps agree with matrices on all 20 random pairs; the control is corrected and
  says so in a comment.
- **Tier B is numerical** (matrices compared to six decimal places), as main's is.
