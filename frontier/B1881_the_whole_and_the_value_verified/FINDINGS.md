# B1881 — The web seat's two relays of 2026-11-11, verified on main: what symmetry allows a state of the whole, and what a history reads

*Main, 2026-11-11 (S306p). The web seat sent two relays overnight, both on the object the record says is missing: a
read-out on the whole (B1872 § 3, B1875 § 7; P-776). Each asks main to verify with its own code. This arc does that.
Data-free: integers, exact algebra, numerics at 50 digits on classical objects, and the record's flat-fibre
instrument on run sequences. No value of τ on record is read or compared, and no frame is evaluated at any point
named here. None of the seat's code is run. 0 of 19.*

## 1. The answer first

- **Every exact fact of both relays is recomputed by main's own code:** 65 checks, none failing. [CORRECTED
  2026-11-12, found by a second reading of Review 79's mends: this read "is reproduced". The record keeps that word
  for the same code run again on a clean checkout (`docs/seats/README.md` § 12). None of the seat's code was run.]
- **The first relay's statement holds, and it is elementary:** a function unchanged by a group of symmetries is
  greatest on a set the group carries to itself. So it is greatest at one point only where every symmetry fixes
  that point. Symmetry says where a single place can be. It does not put one there.
- **Its three cases, at level 5, are as the seat says:**

| the grammar and the mark | points fixed by every symmetry | what an intrinsic read-out can do |
|---|---|---|
| two acts, one twin | none | every place comes at least as a pair; exactly three pairs exist |
| two acts, the line | two | one place only at one of those two |
| the tick an act | an arc, with those two points as its ends | one place anywhere on the arc |

- **The second relay's statement holds in the instrument it names:** as the golden gaps lengthen, a history reads
  the own value of its deepest departure. The allowed readings have a least and no greatest.
- **Main adds three things.** The rate is derived, not only observed (§ 4). The seat's convention and main's name
  one allowed set (§ 5). And the owner's ruling on the tick, given after both relays were written, picks the third
  row of the table and gives a test the weight must pass (§ 6).
  [NOTED 2026-11-12 (Review 80; a reader's finding, made again on this page and not checked by main): the second of
  the three is not an addition. § 5's second correction says what it is: the two tests are one test, so the
  agreement is an instance of an identity, and it could have failed only by an error of coding. B1895 § 6 counts
  reporting it as a finding among main's errors. This bullet was left as written when § 5 was corrected, and it
  stays as written.]
- **Nothing is selected.** No point named here is compared with anything.

## 2. The first relay, fact by fact

Conventions are the seat's, which are the record's (B1733): a line of order 5 is a row (α, b) mod 5, a move γ sends
it to (α, b)γ⁻¹, and the mark is v = (1, 3).

| the seat's fact | what main computed | result |
|---|---|---|
| Q1: the two quotients | the action of S and T on the 12 rows up to sign and on the 6 lines | one twin: index 12, cusp widths 1, 1, 5, 5, no elliptic point, genus 0. The line: index 6, widths 1, 5, two elliptic points of order 2, genus 0 |
| Q2, Q3: the elliptic points | the lines that S keeps | exactly two: the mark's and that of v T⁻¹. The points are i and −1 + i. The elliptic element sends v to 2v: it keeps the line and exchanges the twins |
| Q4, R1, R2: the dual involution W | W = g₀⁻¹ [[0, −1], [5, 0]] g₀; 97 matrices of trace 0 and determinant 5 in its coset, each reduced as a form | W = [[−3, −14], [1, 3]], W² = −5. The fixed points are of discriminant −20, in the two form classes (1, 0, 5) and (2, 2, 3). Any two with one form are related by the group: **exactly two fixed points** |
| Q4: the kernel | by hand, and in integers at all 97 | the fixing matrix has square −5, and its kernel on the points of order 5 is the mark |
| Q5: the mirror | on the fixed and the elliptic points | it fixes each of W's two fixed points and exchanges the two elliptic points |
| Q7, R6: the coordinate t = (η(τ)/η(5τ))⁶ | at 50 digits | t(τ) t(−1/(5τ)) = 125. t = +5√5 and −5√5 at the two fixed points. The elliptic points are t = −11 ± 2i. The mirror is t ↦ t̄. So W with the mirror fixes the circle ∣t∣² = 125, and all four points lie on it |
| R3: the coordinate s | the Rogers–Ramanujan fraction's fifth power, at 50 digits; W's lift, exactly | t = 1/s − 11 − s. The twin exchange is s ↦ −1/s. W lifts to s ↦ (βs + 1)/(s − β), β = (−11 − 5√5)/2, an involution |
| R4, Q6: the three pairs | the three holomorphic involutions' fixed points, exactly; the group they generate with the mirror | six fixed points, none common to two involutions. The group has order 8. The six points fall into **exactly three pairs**, each point with a stabiliser of order 4. No point is fixed by the whole group |
| R5: the ten points | j(τ) − j(5τ) as a polynomial in t, factored | −(t² − 125)(t² + 22t + 125)(t² + 4t + 125)(t² + 18t + 125)(t² − 14t + 125). All ten roots lie on ∣t∣² = 125 |
| R7, R8: the tick | in integers | F = [[0, 1], [1, 1]] has F² the ground, determinant −1 and vF = 3v. F = S⁻¹m, with m the mark's mirror; S keeps the line and m keeps ±v. So if the tick is an act, the mark's mirror is a move of the group that keeps the line |
| R9: weight 1 and weight 2 | the Eisenstein series, at 30 digits | each odd character's weight-1 series vanishes at one elliptic point and not at the other. E₂(τ) − 5E₂(5τ) vanishes at both, and is −40 times the product of the two |

**One thing main computed that the seat left open.** At the ten points the tori are those with an endomorphism of
norm 5. Main predicted the discriminants −4, −11, −16, −19 and −20 before the run, and so the values of j: 1728,
−32768, 287496, −884736, and the two conjugates of discriminant −20. The run gives which factor carries which:

| factor in t | j at its roots | discriminant |
|---|---|---|
| t² + 22t + 125 | 1728 | −4 (the pair over i) |
| t² + 18t + 125 | −32768 | −11 |
| t² + 4t + 125 | 287496 | −16 |
| t² − 14t + 125 | −884736 | −19 |
| t² − 125 | 632000 ± 282880√5 | −20 (W's two fixed points) |

These are values of j at classical points of complex multiplication. They are compared with nothing.

## 3. The second relay, cell by cell

The instrument is the record's (B1857's flat-fibre model, on a clock the record counts as chosen). The height of run
i of a cyclic run sequence is H_i = (r_i + x_i + y_i)/2, with x_i and y_i the continued fractions read forward and
backward. Main computed it from exact integer matrices, and checked it against the form B1875 used.

| the seat's cell | main's result |
|---|---|
| V0: the own values | (6): 3.618034. (11): 6.118034. (2,1,2,1,2): 1.723607 |
| V3: the single runs | a run of n keeps the line exactly when n ≡ 1 mod 5 (checked to n = 40). The runs 6, 11, 16, 21, 26 have own value (n − 1)/2 + √5/2, to 10⁻⁴⁰. The control, 7, does not keep the line |
| V1: copies of one departure | (6): the distance from the own value is 0.019, 0.0028, 5.9·10⁻⁵, 2.7·10⁻⁸, 5.4·10⁻¹⁵ at k = 1, 2, 4, 8, 16, the same for two, three and four copies. (11): 0.023 at k = 1. (2,1,2,1,2): 0.00069. Two copies tie exactly |
| V1: the rate | 1.924847 per golden period in all nine cases; 4 ln φ = 1.924847 |
| V2: different departures | in all five mixtures the apex is unique, at a run of the deepest departure, and the distance from its own value falls below 6·10⁻¹⁵ at k = 16 |
| after the review: short gaps | (6) with one period on both sides reads 3.6515, 0.92 percent above its own value; (11) is 0.65 percent off. (6)₁(6)₂ reads 3.6371, below (6)₁ alone |
| after the review: the pair A, B | A = (2,1,1,4,4) and B = (2,1,2,4,4) keep the line, with own values 2.418183 and 2.423508. In A₁B₂ the apex is in A, at 2.425956. For every gap from 2 to 12 it is in B |

- **A least, and no greatest.** Over all 16,275 run sequences of even length to 6 with runs to 5 [CORRECTED
  2026-11-12 (Review 79): this read "cyclic run sequences". 16,275 = 5² + 5⁴ + 5⁶ counts sequences; up to rotation
  they are 2,815. The least is the same either way. ADDED the same day, found by a second reading of this mend: the
  script's label for this check kept the old words, and so did the run and its file. The label is corrected and
  the script computes the counts: 16,275 as written, 2,815 up to rotation, and 5,575 up to the rotations that keep
  which letter a run is], the least
  apex is the ground's own, √5/2. The own values of the allowed single runs are 5m/2 + √5/2 for the run of 5m + 1,
  and grow without bound.
- **So if the whole is read by its greatest, there is no outcome in this instrument.** That is the record's own
  statement that nothing places the height (T:NO-PLACE), seen in one more instrument.

## 4. The rate, derived

The seat observed the factor tending to φ⁴ and did not prove it. It follows in one line.

- One golden period of ground takes the tail x of a continued fraction to 1/(1 + 1/(1 + x)).
- That map fixes 1/φ, and its derivative there is φ⁻⁴ (exactly; checked symbolically).
- A change in what lies beyond g periods of ground therefore reaches a run's height reduced by φ⁻⁴ᵍ.
- Main's step ratios for two copies of (6), from k to k + 1: 6.9351, 6.8658, 6.8558, 6.8543, 6.8541, 6.8541.
  φ⁴ = 6.854102.

This is the flat-fibre counterpart of the factor (5 + √21)/2 that the hyperbolic invariants show (P-775), which is
observed and not proved. The two are different numbers.

## 5. One allowed set, in the two conventions

The seat writes rows, the mark (1, 3) and the ground [[1, 1], [1, 2]]. B1872 writes columns, the mark (1, 2) and the
ground [[2, 1], [1, 1]]. [CORRECTED 2026-11-12 (Review 79): that is not B1872's convention. B1872's own run prints the
seat's: rows, the line ±(1, 3) with its twin ±(2, 1), and the ground ((1, 1), (1, 2)). The second convention tested
here, columns with the mark (1, 2) and the ground [[2, 1], [1, 1]], is its transpose and is this arc's own; the
script's docstring carries the same wrong name. The conclusion, one allowed set in both, is not touched.] Main did not know beforehand whether "keeps the line" names the same run sequences in both.

> **CORRECTED 2026-11-12, a second time,** found by a second reading of the note above by a session that did not
> write it. The note calls the second convention the transpose of the seat's. It is not the transpose.
>
> - **What it is.** The seat's convention with every matrix conjugated by the swap of the two coordinates, the order
>   of the letters kept, and read on columns. The seat's ground is symmetric, so its transpose is itself. The second
>   ground, [[2, 1], [1, 1]], is the seat's conjugated by the swap.
> - **Its mark.** The row (1, 3) annihilates the column (2, 1) modulo 5, and (2, 1) lies on the mark's own line. The
>   second mark, the column (1, 2), is the swap of (2, 1).
> - **So the two tests are one test.** A row is kept by a matrix exactly when the column it annihilates is kept. The
>   lock computes this on all 120 matrices of determinant 1 modulo 5, for each of the six lines. With a mark that
>   does not annihilate its own line the same recipe gives another test: for (1, 1) the two agree on 88 of the 120.
> - **What that changes.** The agreement on 47,988 sequences is an instance of an identity. It could have failed only
>   by an error of coding, and it shows nothing more than that the two functions are coded as described. Main did
>   not see this when it asked the question, and the sentence before this note stays as it was written.
> - **The agreement on the reversed sequence** is where a transpose does enter. A row is kept by a matrix exactly
>   when the same vector, as a column, is kept by its transpose, for any mark. The second convention's word on the
>   reversed sequence is the transpose of the seat's word, conjugated by the swap.
> - **Corrected with it:** the docstring of the script's second function, which still named B1872, and the script's
>   header.

- On all 47,988 run sequences of length 2, 4 and 6 with runs to 6, the two agree, with no exception.
- They also agree when one is read on the reversed sequence. So the allowed set is closed under reversal.
- They do not agree when one sequence is rotated by a run (8,366 differ). That is expected: "keeps the line" is said
  of a word as written, started in the ground. It is a property of an element of the group, not of a cycle.

## 6. What it means for the read-out on the whole (main's reading; a criterion, not a result)

The owner ruled, after both relays were written, that the tick is an act, that every tick is in the ledger, and that
"only even ticks are observed" is a condition the weight has to deliver (B1879 § 7). Beside the owner's ruling on
what closing means the record holds main's safeguard, which is main's wording and not the owner's: one outcome is
one orbit of the whole (P-774).

**That picks the table's third row.** With the tick an act the mark's mirror is a move (§ 2, R7). The group is
larger, and a point of the larger quotient is a point of the two-act quotient together with its mirror image.

**So an outcome of the whole is of one of two kinds:**

| the outcome, seen in the two-act quotient | what an observer at it sees | the hand |
|---|---|---|
| one point that the mirror fixes | every tick as a symmetry | none |
| a pair of points that the mirror exchanges | at either member, the even ticks only | the two members are the two hands; naming one is a convention |

- **This gives the owner's condition a form that can be tested.** "Only even ticks are observed" is delivered exactly
  when the outcome is a pair that the mirror exchanges. It is not delivered if the outcome is fixed by the mirror.
  A set larger than one orbit leaves a free number.
- **It also answers the first of the seat's three forks from what is already on record, as main reads it.** "Does a
  mirror pair count as one place?" With the tick an act the mirror is a move, and the pair is one orbit. If one orbit
  is one outcome, the pair is one outcome. The first half is the owner's ruling; the second is main's safeguard. So
  main reads the fork as settled, says on whose words each half rests, and tells the owner.
- **Where the relay's arc stands in this.** On the arc ∣t∣² = 125 the mirror is t ↦ t̄. Its two ends, t = ±5√5, are
  real: outcomes without a hand. Every other point of the arc is one member of a mirror pair, the point over i among
  them. So for an intrinsic read-out with one outcome, the owner's condition asks for an interior point of the arc
  and excludes its two ends.
- **And it says what symmetry cannot do.** Symmetry confines a single outcome to the arc. The instrument's greatest
  has no outcome (§ 3). Neither places a value. What is left to do so is the weight, as the record already says
  (P-774), and this section is the first clause of its design (P-776).

**What this section is not.** It computes no weight and no state. It assumes level 5, which is put in. It covers
only a read-out built from the quotient alone; one that uses the tori and a content is outside it. It is main's
formulation, a day old and unread by any other seat.

## 7. What is not shown

- **Nothing is selected, and nothing is compared.** The two fixed points, the ten points, the arc and the three
  pairs are compared with no value of τ on record, and no frame is evaluated at them.
- **Level 5 is put in.** By the ladder's rule every level counts at once, and neither of the seat's two rules chooses
  a level.
- **The instrument is one, on a chosen clock.** Nothing in § 3 is shown on the hyperbolic metric.
- **Taken from the literature and not checked here:** Selberg's bound at level 5; the dimensions of the spaces of
  forms beyond what the weight-1 and weight-2 checks test; that the symmetries listed are all of them. Main checked
  the group of order 8 on the sphere and did not prove that no further symmetry exists.
- **The seat's two remaining forks are open:** whether a state built from the quotient alone is what "the whole"
  means, and a sealed card on where the forced objects are greatest on the arc, which is at the owner's word only.

## Seen first

- **The repo sweep,** `VERDICT topic-sweep`: for the dual involution, the two level-5 quotients and their special
  points, the seat's own sweep of main at `b28dceea8` stands in its relay (17, 18, 16 and 35 arcs under four
  patterns) and main re-read its two headline findings: the record names the dual involution only at level 15
  (B689, B692, B694, B695, B698), and B1809's lemma has the three kinds of fixed set. For the own value and its
  rate: P-717's row holds the one-departure case; B1857 the instrument; B1875 the composition; P-775 the hyperbolic
  factor.
- **The literature.** Everything in § 2 is classical: the Atkin–Lehner involution of level 5, its fixed points of
  discriminant −20, the Hauptmodul and its relation to the Rogers–Ramanujan fraction, the modular equation of level
  5. Main cites none of it as its own.

## Disclosed

- **Three of main's own checks failed on the first run, and none of the seat's facts.** Two used a constant computed
  in double precision inside a 30-digit series. One asked for "0.93 percent", a figure main had typed and the relay
  does not print; the offset is 0.9245. The checks are mended in place and say so. No expectation was changed.
- **The expectations were written before the run,** in the script's header. [CORRECTED 2026-11-12 (Review 79):
  nothing on file shows that. Script, run and findings entered the record in one commit, with no earlier commit of
  the header. By the protocol's labels this arc is computed once.] Eleven held. The twelfth, on the two
  conventions, was not predicted.
- **§ 6 was written with the owner's ruling in hand.** It is a reading of facts verified here, not a prediction made
  before them.
- **Main read both relays about ten hours after the first was pushed** (B1880 § 6). [CORRECTED 2026-11-12
  (Review 79): the section cited is about a re-audit that sat unread for eight hours, not about these relays. The ten
  hours are main's reckoning and no file is cited for them.]
- **Three checks did not check what they said** (added 2026-11-12, Review 79, found by a reading of this arc by a
  session that did not build it). Two were passed the literal value true and counted among the 65: that the mirror
  normalises the group, and that the single runs' own values increase without bound. Both are computed now. A third,
  mended earlier and said to ask what the relay says, asked for main's own figure; it now asks for both. And the
  lock said it recomputed the index, the cusp widths and the elliptic points, and recomputed the index alone; it
  recomputes all three now.
- **Those mends were read on 2026-11-12 by a session that did not write them, and four things were found.** The
  word transpose (§ 5). "Reproduced" for what was recomputed, in § 1 and in the verdict line. The script's label
  for the least apex, which the mend of the page had not reached (§ 3). And that the lock held two of the nine mends
  and nothing held the other seven. All four are corrected, and the lock holds each.
- **Main found two more while mending those.** The check on the two conventions passed if any one of three readings
  agreed; it asks now for the two that § 5 states. And one line of the run printed a set, in an order that changed
  from run to run; it is sorted, and the run is the same file at every run.

## Reproduce

```
python3 -B frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py
python3 -m pytest -q frontier/B1881_the_whole_and_the_value_verified/verification/
```
