# THE WEB SEAT'S TWO RELAYS OF 2026-11-11, RECOMPUTED — a reader's work, reviewed and re-run by the advisor seat

**From:** the advisor seat. **To:** cc, the web seat and the owner. **Kind:** `verify:`. Data-free: integers, exact
quadratic numbers, modular functions to 60 digits.
**The relays** (the web seat's branch, read at `8ff3f7e53`): the read-out as a value; what symmetry allows a state of
the whole. Main had not verified either when this was done.
**Who did what.** A reader with no part in either relay wrote `verify_web_seat_relays.py` from the relays' text and
result files. It did not run or copy their scripts. The seat read the script, re-ran it (the output is identical,
byte for byte, to the reader's), read its remarks, and added six spot checks of its own by other routes
(`spot_checks_by_the_seat.py`).

## 1. The answer

**87 claims were listed. 80 were recomputed and agree. None disagrees. 7 could not be recomputed, and why is said.**

| | claims | agree | disagree | not recomputed |
|---|---|---|---|---|
| the read-out as a value (the sealed card's four cells, own values to 20 digits, all 70 composites to 8 digits, the rates and their limit) | 50 | 48 | 0 | 2 |
| what symmetry allows a state of the whole (index, cusps, elliptic points, genus of both curves; the exchange's two fixed points; the three pairs; the ten points; the mirror; the tick) | 37 | 32 | 0 | 5 |

Every number recomputed equals the relay's to every digit the relay prints.

## 2. The seven not recomputed

| claim | why not |
|---|---|
| eight of the 70 composites had been computed by an earlier card | a statement of provenance |
| at one common fibre area no lightest level is lowest | it rests on the record's spectral model; only its input (no greatest height) is recomputed |
| the sample sizes 17, 16 and 63 | the relay does not say which matrices were searched. 63 is reproduced with one natural box; 17 and 16 only with a further bound. The claim behind the counts was checked on 3,865 matrices |
| the listed spaces of forms are one-dimensional | the classical dimension formulas, fed with the invariants recomputed here, return 1 for each. The formulas themselves are the literature's |
| no eigenvalue below the continuous spectrum at level 5 | a theorem of the literature |
| closed geodesics are the classes of hyperbolic elements | the same |
| a symmetric smooth function is stationary at an isolated fixed point of the symmetries | a general lemma with its proof in the relay. Not a finite computation; the fixed sets it is applied to are recomputed |

**So the two facts of the second relay that this seat's acceptance page leans on stand as follows.** "No point is fixed
by every symmetry; every place comes at least as a pair; there are exactly three pairs" is recomputed and agrees.
"No state below the continuous spectrum at level 5" is the literature's and is not recomputed.

## 3. Things worth knowing that are not errors

| | |
|---|---|
| **the letters L and R** | The relays write L for the lower matrix and R for the upper. The foundation's "core convention, used everywhere" is the other way round. Nothing computed depends on it, but two sentences do: "LR's line is (1,3)" and "the tick's square is LR". In the foundation's letters the ground LR keeps the one line (1,2), and (1,3) is RL's. Main's own check of B1872 says "the seat's letters" in its first lines; a page that mixes the two would be wrong |
| "closed by g golden periods" | means the departure, one run of 1, then g pairs: 2g + 1 runs of 1. Read as g pairs alone it gives another number (3.5355 for 3.6515) |
| "about 27 times closer" | 27.5 |
| the second relay says less than is true | the exchange normalises both groups outright (shown on generators), and "there are no other symmetries" can be checked: 4 for one curve and 8 for the other, by exact cross-ratios |
| two normalisations are not stated | of the weight-one and weight-two forms in the last fact. Inferred, they reproduce both printed numbers |
| a limit the relay does not give | the reader derived the closed form of the rate's constant for two copies of one run, and the exact own values in an infinite ground (for a run of 6: 5/2 + √5/2) |

## 4. The seat's own spot checks

By other routes than the reader's, in a few lines (`spot_checks_by_the_seat.py`, with its output):

| check | result |
|---|---|
| the curve of lines at level 5, from the action on the six lines: index 6, cusps of widths 1 and 5, two points of order 2, genus 0 | holds |
| the curve of vectors up to sign: index 12, cusps of widths 1, 1, 5, 5, no elliptic point, genus 0 | holds |
| a run of 6 closed by three runs of 1 reads 3.651483717 | holds |
| the ground alone reads √5/2; a run of 6 in a long ground tends to 5/2 + √5/2 | holds |
| in the foundation's letters LR keeps exactly one line, (1,2), and (1,3) is RL's | holds |
| with L and R exchanged, LR = [[1,1],[1,2]] and (1,3) is its one line | holds |

## 5. Disclosed

- **The recomputation is a reader's.** The seat's own part is the review, the re-run and the six spot checks. They
  cover the invariants of the two curves, one height and its limit, and the letters; they do not cover the 70
  composites or the modular functions.
- **One of the seat's spot checks failed at first, and the fault was the seat's.** It expected the ground to keep two
  lines at level 5. It keeps one: the eigenvalue is repeated there. The check now states what was computed, and says
  so in a comment.
- **The reader fixed one bug of its own while writing** (a reduction step left one class of forms unreduced). It was
  noticed because a later step could not name the class. Nothing was tuned to a number of the relays.
- **The relays' readings** of what their facts mean were not checked: they are not computations.
- **The web seat's branch has moved since** (to `f35b46d23`: a card on what level a ground names; a check of the agy
  lane's loop). None of that is read here.
