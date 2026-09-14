# B1405 — THE WORD ANCHOR RE-PRICED: BRANCH A'S ANCHOR IS NOT
# MIS-SIZED, IT IS MIS-TYPED (2026-09-14)

## 0. THE ONE-SENTENCE RESULT

B1349's ledger prices the word anchor as **a label** — `log₂7 ≈ 2.81` bits to
name a non-unit residue — and branch A's one surviving reading then closes by
**+1.19 bits**. B1404's two outside theorems say the word is not a label:
**Lackenby** makes it the manifold's own canonical decomposition, and
**Jørgensen/Callahan** make `m = 1` the *output of a principle* rather than a
choice from a menu. Re-priced as what it actually is — a **departure from the
selected object** — the same reading comes to **−13.70 bits**.

**The arithmetic of B1349 is untouched. What changes is what the arithmetic is
about.** 20/20 checks, `b1405_pricing.py`.

## 1. THE CRUX: TWO m's, AND THE LEDGER BILLS THE WRONG ONE

`ord(R) = ord(L) = 15` in SU(3)₂, so the readout is a function of **m mod 15**.
The manifold is not. Verified exactly:

    weld(1) = weld(16)   and   weld(3) = weld(18)      EXACTLY
    vol(b++ R¹L¹)  = 2.02988321281930725      (= m004, identified)
    vol(b++ R¹⁶L¹⁶) = 7.1768908458832718224

**Same reading, different manifolds, a volume apart.** So *naming a residue* and
*naming a manifold* are different acts — and every selection principle the
programme has is about the **manifold**. E72's class, one level up: not one
symbol carrying two values, but one **anchor** pricing two different choices.

## 2. EVERY SELECTION PRINCIPLE OUTPUTS m = 1, AND 1 IS A UNIT

| m | volume | `λ_m` | `m²+4` | `gcd(m,15)` | branch |
|---|---|---|---|---|---|
| **1** | **2.0298832128** | `(1+√5)/2` | 5 | 1 | **B** |
| 2 | 3.6638623767 | `1+√2` | 8 | 1 | B |
| 3 | 4.8138191861 | `(3+√13)/2` | 13 | 3 | A |
| 4 | 5.5736091128 | `2+√5` | 20 | 1 | B |
| 5 | 6.0669922401 | `(5+√29)/2` | 29 | 5 | A |
| 6 | 6.3913914548 | `3+√10` | 40 | 3 | A |
| 7 | 6.6106012368 | `(7+√53)/2` | 53 | 1 | B |
| 8 | 6.7634987585 | `4+√17` | 68 | 1 | B |
| 9 | 6.8734717904 | `(9+√85)/2` | 85 | 3 | A |
| 10 | 6.9548036915 | `5+√26` | 104 | 5 | A |

Five principles, all landing on `m = 1`:

| principle | selects | `gcd(m,15)` | source |
|---|---|---|---|
| minimal volume in the family | m = 1 | 1 | verified here, strictly increasing |
| minimal systole `2 log λ_m` | m = 1 | 1 | verified here, `λ_m` strictly increasing |
| Jørgensen extremality `J = 1` | m = 1 | 1 | B1345/B1401; Callahan's uniqueness cited |
| McKay-unique shadow | m = 1 | 1 | B997, cited |
| a cusp-order conductor exists | m ∈ {1,2} | 1 | B675/B1403 |

**Every one outputs a UNIT of ℤ/15 — every one lands on branch B, the dead
branch.** Not a single principle in the corpus selects a branch-A word.

## 3. AND BRANCH A'S OWN RESIDUES ARE THE ONES THE CORPUS ALREADY DISQUALIFIED

Branch A = `{0, 3, 5, 6, 9, 10, 12}`, branch B = the 8 units.

| residue | what it is |
|---|---|
| **0** | the **empty word**: `R⁰L⁰ = I`, so `weld = C` and `λ = 1` — ear-independent for a trivial reason. Reachable by a real manifold (`m = 15`), whose SU(3)₂ reading is nevertheless the bare charge conjugation. |
| **3** | the **BRONZE** — B675's certified **DEAF** object: cusp shape's Galois group `S₄`, non-abelian, `[ℚ(τ):ℚ] = 8`, heard by no stage family at any rank. |
| 5, 6, 9, 10, 12 | cusp field **non-quadratic** (B1403, verified there for m = 3..8). |

So branch A's cheapest live entry point is the one member of the family the
corpus has *proved* no stage can hear.

## 4. WHAT THE PRINCIPLE IS WORTH, AND THE RE-PRICED LEDGER

If `m = 1` is the output of Jørgensen extremality, it costs **0 bits** — you
name a condition, not a manifold. Abandon the principle and you must name a
manifold explicitly. A floor on that:

    |OrientableCuspedCensus| = 212 641   →   log₂ = 17.70 bits

and this is only a **floor**: Callahan's uniqueness is over *all* orientable
hyperbolic 3-manifolds, so the true pool is unbounded.

| word anchor, branch A's surviving reading | bits | outputs | total | |
|---|---|---|---|---|
| **B1349 as banked** — name a non-unit residue | 2.81 | 4 | **+1.19** | closes |
| m = 0 excluded as degenerate (6 live residues) | 2.58 | 4 | **+1.42** | closes |
| **name the MANIFOLD, principle forfeited** | **17.70** | 4 | **−13.70** | **FAILS** |

**The second row is reported because it cuts against this arc.** Dropping the
degenerate residue makes branch A *cheaper*, and the banked reading closes by a
little more, not less. It changes nothing about the third row.

## 5. THE VERDICT IS A FORK, AND BOTH HORNS FAIL THE ROW'S PURPOSE

The re-pricing does not say B1349 computed the wrong number. It says the number
answers a question that has to be chosen first:

- **If the row is a claim about THE OBJECT** — which is the only reading under
  which it can serve as *"the object predicts X"* — then the word must be the
  object's own word. Lackenby says that word is not a free label; Jørgensen and
  four other principles say it is `m = 1`; `gcd(1,15) = 1`, so it is on
  **branch B**, which is dead on two independent gates. **The row is dead.**
- **If the row is a claim about a RESIDUE CLASS in SU(3)₂ modular data**, then
  branch A closes at `+1.19` exactly as banked — **but the row is then not about
  m004**, and cannot be cited as the object predicting anything. The residue
  class `m ≡ 3` contains no manifold any principle selects, and its smallest
  member is deaf.

**Either way the row cannot do the job it was licensed for.** This is the
**third independent** ground for *do not spend it*: addendum 1's arithmetic,
addenda 2–4's kind, and now the anchor's type.

**What this does to L209** (*is the θ-even mirror row the right observable?*):
it does not make the owner's decision, but it makes it **decidable**. The
question is no longer "is this the right observable" in the abstract — it is
*"is the row about the object or about a residue?"*, and both answers are now
priced.

## 6. FENCES

- **B1349's mathematics is untouched**: the `gcd(m,15)` law, the exact spectra,
  the field statement, the C6 containment, the 4/4 split, and the `+1.19` of its
  own accounting all stand as computed. Only the **type** of the word anchor is
  in question here.
- The `17.70` bits is **a floor under one reading of the accounting**, and the
  census is a modelling choice, stated rather than hidden. The load-bearing claim
  is the *type* argument of §1 and §5; the bit figure quantifies it and is not
  needed for the verdict — `2.81` versus a departure from a five-fold selection
  is a mismatch of kind, not of magnitude.
- Jørgensen/Callahan uniqueness, B997's McKay uniqueness, B675's bronze
  deafness and Lackenby's canonicity are **cited**, not re-derived.
- Nothing here reaches `CLAIMS.md`, F2 or Gate 5, and no value is compared to
  any measurement.

Artifacts: `b1405_pricing.py` (20/20). Locks: `tests/test_b1405_word_anchor.py`.
