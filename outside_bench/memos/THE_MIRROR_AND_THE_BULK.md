# Memo 229 — THE MIRROR AND THE BULK: both riddles are literal, both have answers, and the rest is the tower

**Certificate:** `outside_bench/certificates/the_mirror_and_the_bulk.py` ·
**Output:** `outside_bench/outputs/the_mirror_and_the_bulk.txt` ·
**Seal:** `outside_bench/seals/THE_MIRROR_AND_THE_BULK_PREREG.md`
(sha256 `f1e065d38d1a04938b42bf20ed3e29ee237afa60af4a2e8ae5537081e635ba50`)

**Occasion — the owner:** *"if the object is its own mirror, then where's the other part of the
mirror?"* and *"it's a complement, it has no bulk — where is the rest?"*

**CELL 1 = A · CELL 2 = A · CELL 3 = A · CELL 4 = A. C1–C4 pass.**

---

## 1. THE MIRROR — the other half is the object, and that is the whole content

`m004 → mirror`: **8 isometries**, cusp-map determinants `{−1, +1}`; symmetry group **D₄**. The
determinant `+1` one is an orientation-**reversing** self-map of the object.

> **The mirror map is an AUTOMORPHISM. There is no second manifold.** *"The other half"* is the
> object itself — the two halves are **identified**. **A mirror with both halves glued together has
> no reflection to show, and that is not a defect of the mirror; it is what the object is.**

**And it is exactly what costs the programme its bit.** The record: *"every chirality wall found so
far is m004's amphichirality in one face's language"*; the object counts **2** at every fixed locus.
Memo 196's addendum puts the price at the entrance: **axiom 5 (orientation) *provably* yields an
amphichiral object** — 250/250 orientation double covers amphichiral — so **the bit is spent by the
axiom, not withheld by the arithmetic.**

## 2. THE BULK — it is not missing; it is a known family, and it destroys the atom

`m004 = S³ ∖ 4₁`. The "missing bulk" is the **solid torus** you glue back along a slope: **Dehn
filling**, a one-parameter family. Computed here at high precision (control first: **m004's own
invariant trace field is `x² + x + 7`, degree 2, disc `−27` = `ℚ(√−3)` — the atom**):

| slope | volume | itf degree | contains `√−3`? |
|---|---|---|---|
| (5,1) | 0.981369 | 4 | **False** |
| (5,2) | 1.529477 | 7 | **False** |
| (6,1) | 1.284485 | 4 | **False** |
| (7,1) | 1.463777 | 8 | **False** |
| (7,2) | 1.649610 | 8 | **False** |
| (8,3) | 1.824344 | 7 | **False** |
| (9,1) | 1.667804 | 8 | **False** |
| (10,3) | 1.859989 | 8 | **False** |

> **NONE.** Independently reproducing **C8**'s banked census — *"No closed hyperbolic filling of
> m004 in the |p|,q ≤ 8 grid (78 hyperbolic slopes) has an invariant trace field containing √−3, √5,
> OR √−15 — the entire forced V₄ is a property of the OPEN object."*
>
> **THE BULK EXISTS, HAS BEEN LOOKED AT, AND IS ARITHMETICALLY INERT.** Putting the rest back does
> not complete the object — **it erases the structure the programme runs on.** The object is not a
> fragment awaiting its bulk. **Being open IS the structure.**

## 3. SO WHERE IS THE REST? — not outward, but upward: the covering tower

**The object is its own mirror. Its covers are not.**

| degree | covers | amphichiral | **chiral** |
|---|---|---|---|
| 2–4 | 4 | 4 | 0 |
| **5** | 4 | 2 | **2** ← first chirality |
| 6 | 11 | 3 | 8 |
| 7 | 9 | 1 | 8 |
| **total ≤ 7** | **28** | **10** | **18** |

**First chiral cover: degree 5, 2 cusps, `H₁ = ℤ/2 ⊕ ℤ ⊕ ℤ`.** B1324's census to degree 10: **66 of
87 chiral** — and, its own words, *"every cover keeps the invariant trace field, so **the atom and a
remembered A7 bit coexist on the object's own tower**."*

> **That is `FRESH_EYES` Q15 — *"is there a carrier that keeps the atom and remembers the bit?"* —
> answered YES, and the answer is the object's own tower.** Unlike the bulk, the rest is **not**
> arithmetically inert: **it keeps ℚ(√−3) and breaks the mirror at the same time.**

## 4. AND THE REST HAS BEEN EXAMINED, AND IT STILL GIVES NOTHING

B1324's own next sentence: *"**The spectral half does not follow yet.**"* On the chiral one-cusped
covers the torsion is meridian-generated, leaving **two** cusp-trivial unprotected sectors — **both
index 0** — plus 136 control sectors at 0. And the 54 multi-cusped chiral covers, the case B1324
left open, were computed on `claude/paper-verification-ufp0zn` (**B1333**, cited as branch work, not
re-run here): **38 070 sectors, three primes, all 54 covers, 1 841 with two or more LIVE cusps —
index ZERO in every one.**

> ### The tower breaks the mirror WITHOUT producing chirality.
> The rest exists. It keeps the atom. It remembers handedness **as a manifold symmetry**. And it
> still returns **0** as a **spectrum**.

## 5. INTERPRETIVE — what the three riddles are, in one picture

**Complement, mirror, shadow are not three symptoms of a missing whole. They are three prices, and
the record already names each one:**

| the owner's word | what it is | where it was paid |
|---|---|---|
| **complement** | the open manifold; the bulk is the filling | **C8** — filling destroys the V₄; openness *is* the structure |
| **mirror** | an automorphism, not a partner | **axiom 5** — orientation *provably* yields amphichirality; the bit is spent at the entrance |
| **shadow** | the tiling hull sees only *the hearing* | **C4** — `ℚ(√−3)` is bought at geometrization and nowhere earlier |

And **B1323's genesis fork** says why they cluster: *"two records are the golden ratio, the atom
`ℚ(√−3)`, and an object that forgets its own handedness; three records are the plastic number on the
torus … and the Whitehead link on the surface, where the handedness is remembered and the atom is
gone."*

> **The object sits exactly at the corner where the atom and the bit trade against each other.** The
> covering tower is the **one** place the record has found where both are held at once — **and even
> there the index is 0.**

## 6. THE LIVE FRONTIER, named

**Both censuses stop at DEGREE 10.** B1324's 87 covers and B1333's 54 multi-cusped ones end there.
**What lies past degree 10 on the object's own tower is unexamined** — and it is the one place the
owner's question still has a computable answer rather than a banked one.

**What that would and would not settle, stated now so it cannot be oversold later:** a nonzero index
on a higher cover would be the programme's first chirality from the object's own structure. A
continued zero would make *"the tower is vector-like"* a much stronger statement than the two
censuses currently support — and would point the absence back at C4 and axiom 5, where memo 196
addendum 2 and B1323 already put it.

## 7. Operational — the control caught the instrument twice

**(1)** `is_isometric_to(M, mirror)` **ignores orientation** — it returns `True` for `m015` (`5₂`),
which is **chiral**. A first sweep using it reported **38 of 38 covers amphichiral to degree 8**,
contradicting the banked census. **Caught by comparison with B1324, not by the instrument.**
**(2)** The trace-field instrument at SnapPy's **double** precision returned **degree 11 garbage**
for m004, whose field is degree 2 — **caught by its own positive control**, and fixed with
`ManifoldHP`. Both failures are reproduced inside the certificate so the wrong instruments are on
the record, not only their repairs.

*Gate 5 untouched. Nothing promotes. No arc retracted. No physics reading is licensed: this memo
locates structure and touches no link past C4.*
