# 199 — THE BIT SECTION 8 BANKS IS NOT THE SIGN THE OBJECT WEARS

**Date** 2026-09-11 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/section8_bit_is_not_the_mirror.py` · **Output**
`outputs/section8_bit_is_not_the_mirror_out.txt`
**Seal** `seals/SECTION8_BIT_ADJUDICATION_PREREG.md`, sha256
`a0f898ac70dc9bdaa27778e98d73692f94e8abb443aba3922962c07ca4094dbb` — **sealed before the
certificate was written**
**Gate 5 untouched**

**Occasion — an open question another seat named, owned by nobody, and explicitly handed off.**
`frontier/B1327_relation_not_observer/FINDINGS.md` (verdict **OPEN**, on `<seat>/paper-verification-ufp0zn`
at `e829c02c`):

> *"A relation among three bits spanning two tables is exactly where a double count would hide.
> **This is not a claim.** §8's chirality bit is a Fricke-`kappa` torsor class of a pair, and may not
> be the same object as the manifold's mirror sign. Whether they are the same bit is for the seat
> that owns §8 to adjudicate. If they are, one of the three rows is not an independent input."*

---

## 1. The answer: **NO. They are not the same bit.**

Two separations, either sufficient on its own, both computed.

**(i) DOMAIN — one moves when the object does not.**
Hold the object relatum fixed at B1248's `A_OBJ` and move **only the partner**. The §8 class takes
**eight distinct values across all four branches** — `{−181, −29, −19, −1, 0, +1, 5, 11}` — with the
object relatum never changing once. The manifold's mirror sign is read off the object's **own
symmetry group** with no partner named anywhere, and splits its eight isometries **4 + 4**.

A function of a pair that moves when only the partner moves is not a function of the object. The
paper says this about its own bit in as many words — *"an invariant of neither relatum separately"* —
and that sentence is the refutation of the identity, not a gloss on it.

**(ii) PRESENCE — on the object itself they disagree about existing.**
The mirror sign is **present and non-trivial**: m004 is amphichiral, four of its eight isometries
reverse orientation. The §8 bit is **absent**: the object's canonical pair sits at `kappa = −2`, so
`2 − kappa = 4 = 2²`, `D = +1` — the branch where the mirror is realised **inside** `SL₂(ℤ)`, i.e.
**no bit at all**. B1248 supplies the mechanism: *the cusp pins `kappa` below the wall `kappa = 2`.*

**A quantity that is there and a quantity that is not there are not the same quantity.**

## 2. What that does to the over-count

`mirror = arrow × swap` is a relation among **three functions on the object's own isometry group**.
It does not reach §8's bit. So it **does not span the two tables**, and no ledger row is a
restatement of another *through this relation*. **B1327's over-count resolves NO**, and B1327's own
framing — *"this is not a claim"* — was the right call.

## 3. This bench found the answer already banked, and that is the finding

The standing rule is *exhaust the repo before ranking a gap*. Terms run through
`scripts/checks/already_banked.py`: *"chirality bit same as mirror sign"*, *"Fricke kappa torsor pair
double count"*, *"arrow swap mirror three bits one relation"*, *"freedom ledger independent input
over-count"*. The first two return **B1248 — PROVED** — which contains **both** halves of the answer
already:

> *"over ℚ(√−3) a survey of 91 short-word pairs in π₁(m004) found the class taking many values"* …
> *"THE OBJECT'S OWN VALUE — and why **the object alone has no bit**"*

**The question B1327 raised as open was answered by a **PROVED** arc banked 2026-09-05, six days before B1327 was written, and
neither arc cites the other.** This is the citation gap this bench has now measured four times
(memo 195's five uncited arcs, memo 196's chain, memo 198's gate). It is not a new kind of defect;
it is the same one, and it cost a seat a question mark on a settled fact.

## 4. One observation about B1327's own computation, offered to its seat

B1327's verified computation is *"the object's eight isometries realise 4 of the 8 a priori sign
triples … with zero violations of `mirror = arrow × swap`."* Reproduced here exactly. But **all eight
cusp maps are diagonal** (verified: zero off-diagonal entries), and for a diagonal matrix
`det diag(a,d) = a·d` **identically**. So on this presentation the product law is not a discovered
relation — it is the determinant of a diagonal matrix. **The empirical content of the check is the
diagonality, not the product.**

This does not weaken B1327's typing proposal, which does not rest on the product. It does mean the
relation cannot be cited as independent evidence that three named bits are one relation, because
given diagonality it could not have come out otherwise.

## 5. A convention error of this bench's own, filed at the point of occurrence

An earlier pass computed `kappa` in the **character-variety** normalisation `tr[A,B] − 4` and
compared it to B1200's statement, printing a mismatch — i.e. this bench momentarily read a **PROVED**
arc as contradicted. B1200 and §8 both use `tr[A,B] − 2`. On m004's holonomy, verified in control C2:

    tr[A,B] - 2 = -0.500000000000 + 0.866025403784j = omega
    |tr[A,B] - 2| = 1.000000000000            <- B1200's UNIT OBSTRUCTION
    Phi_3(tr[A,B] - 2) = 1.79e-15             <- B1200: identically 0

**B1200 reproduces. The contradiction was the convention, and the convention was mine.** The control
is kept in the certificate permanently, printing **both** forms, so the next reader cannot make it
silently. **BENCH ERROR #19.**

## 6. What this does NOT settle, and this bench does not own it

* **Whether `arrow` and `swap` are independent of each other.** That relation is internal to
  B1327's triple, it is real, and it is untouched here. On m004 the mirror sign is determined by the
  other two — but all three are **object-internal**, so if a row moves on that account it is not §8's.
* **Which freedom-ledger row, if any, moves.** That is the §8/§9 owner's call. This bench reports
  only that **the identity the over-count needed does not hold.**
* **Nothing here makes the §8 bit derivable.** *"Which pair is used remains supplied"* is the
  paper's own withdrawn support and this memo recovers none of it. Indeed §1(i) sharpens the cost:
  the bit depends on the partner across all four branches, so *which partner* is load-bearing.

*Gate 5 untouched — no measured value is used or named. Nothing promotes to `CLAIMS.md`. No arc is
retracted; one OPEN question of another seat's is answered, and one convention error of this
bench's is filed.*
