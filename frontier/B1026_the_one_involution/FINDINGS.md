# B1026 — ONE INVOLUTION, SIX NAMES: the substrate record swap IS the sl(n) opposition involution, and its first link is an axiom outside A1–A6

**Date:** 2026-08-10 · **Lane:** MATHEMATICS, exact. Gate 5 untouched — no physics statement,
no measured value, nothing to `CLAIMS.md` from this arc.
**Band:** CONSOLIDATION REFRESH, B0–B99 (`docs/THE_CAMPAIGN.md`), the owner's directive of
2026-08-10: *"read B0→B1010 systematically … refresh all consolidations."*

**On sealing:** no preregistration. The finding surfaced during the mandatory band read, before
any computation, and the computation that follows is a **verification of banked statements**,
not a two-outcome question. Recorded open-and-shut, the B979/B957/B960 pattern.

**Method, per campaign step 5** (*"re-verify the identities before restoring — never restore
from memory"*): `verify.py` recomputes every link from first principles and **imports nothing
from the arcs it verifies** (B14, B16, B54, B62, B64). Second pipeline, not a re-reading.

---

## 1. THE CHAIN

Reading the band in order, the same involution is introduced **six times under six names**, each
time as if new:

| # | name | arc | what it does |
|---|---|---|---|
| 1 | **the record swap** `P = [[0,1],[1,0]]` | **B16** | exchanges the two records — **an added axiom, not in A1–A6** |
| 2 | **the half-step** `F = LP`, `F² = A` | **B14** | the object's square root, unique up to sign in `GL(2,ℤ)` |
| 3 | **the trace map's generator** | **B18** | `T(x,y,z) = (z, x, 2xz−y)` is the trace lift of **`F`**, *not* of `A` |
| 4 | **the exchange involution** | **B51/B54** | commutes with the fixed-line Jacobian `J(m,c)` for **all** `c`; block-diagonalizes it |
| 5 | **the opposition involution** `θ = −w₀` | **B62** | *"the exchange involution `P` (`tr W ↔ tr W⁻¹`) **is** the opposition involution `θ = −w₀` on the `sl(n)` root system"* |
| 6 | **the contragredient** ⟹ Dickson parity | **B64** | `P` sends `m ↦ −m`; `L_k(−m) = (−1)^k L_k(m)`, grading even-\|k\| symmetric / odd-\|k\| antisymmetric |
| (7) | **W_N charge conjugation** | **B74** | *"the W_N charge-conjugation grading … and the Dickson P-grading **ARE THE SAME involution** — −w₀"* |

## 2. WHAT WAS VERIFIED HERE (all six, exact, independent)

```
[OK] link1  B16  {X : X²=I, XLX⁻¹=R} = {±P}; operational {X : (LX)²=A} = {±P};
                 weak control |{det=−1, X²=I}| = 84 > 2, so the criterion selects
[OK] link2  B14  {X : X²=A} = {±F}; B(a,b) has an integer orientation-reversing
                 square root IFF a=b (5×5 grid, no exceptions)
[OK] link3  B13/B22  32 symmetric-square lifts contain t²−3t+1, every one with
                 (det,|tr|) = (−1,1); converse holds; det=−1 ⟹ (t+1) always divides
[OK] link4  B62  θ is an involution, height-preserving, and flips the Dynkin diagram
                 α_i ↦ α_{n−i}; P33's closed form holds over positive roots
[OK] link5  ---  the contragredient acts on weights as −w₀ (ω_k ↦ ω_{n−k},
                 dim Λ^k = dim Λ^{n−k}); trace-trivial at SL(2)
[OK] link6  B64  L_k(−m) = (−1)^k L_k(m), k = 1..8; det(M^k) = (−1)^k
```

**Link 5 is the identification the corpus never states, and it is elementary once written:** the
exchange involution on trace coordinates is `W ↦ W⁻¹`, the contragredient; and on `A_{n−1}` the
contragredient acts on weights as `−w₀`, the opposition involution. **The same map.**

**And link 5 explains why it was missable.** In `SL(2)`, `tr(g) = tr(g⁻¹)` identically — the
contragredient is **trace-trivial at rank 2**, exactly as THE CHAIN's C21 says of `θ`. The map
is *invisible in the object's own rank* and only becomes visible from rank 3 on, which is
precisely where the tower literature (B27 onward) picks it up under a different name.

## 3. THE DIFF — what the consolidations carry, measured

| register | carries | does not |
|---|---|---|
| `docs/THEOREM_LEDGER.md` **C12** | *"the trace map is **θ-equivariant**"*, citing B48/B54/B64 | cite B62; identify θ with `−w₀`; reach B16 |
| `knowledge/K005` | `θ = −w₀` as standard Lie theory, anchored to B62, B74, B112, B118, B121 | connect it to `P`, the half-step, or the substrate |
| `CLAIMS.md` **P33** | the height lemma | the identification |
| `docs/LAW_MAP.md` | — | **zero** occurrences of "opposition", "exchange symmetry", "record swap", "half-step" |
| `docs/THE_FRAMEWORK.md` | — | **zero**, same four terms |

**Exactly one arc in the corpus cites B16.**

## 4. THE CONSEQUENCE FOR THE INPUT COUNT — stated at its honest scope

**B16, verbatim:**

> *"A1-A6 in the current conditional uniqueness theorem do not require the orientation-reversing
> swap. … Therefore `P` is not currently a theorem of the substrate. It becomes forced only
> after adding an exchange-symmetry axiom … **That axiom is plausible, but it is still an
> axiom.**"*

`docs/THE_CLAIM.md`'s counted input list is *"the six axioms A1–A6 and one bit A7 … plus five
typed external data."* **The exchange-symmetry axiom is not in it**, and
`INPUT_COMPLETENESS_LEDGER.md` has no row for it.

**SCOPE — this does NOT disturb the derivation theorem.** `THE_CLAIM`'s chain runs
`A → m004 → ℚ(√−3) → 2T → E₆ → cascade` (B892/B862/B864/B863/B994/B978/B884/B897/B303) and
**never passes through the half-step or the trace map.** What the uncounted axiom is
load-bearing for is the **trace-map substrate**: the twelfth face
(`COMPUTE_THE_PROGRAM.md` §1), the SL(n) tower (B27–B105, P21–P32), the Fricke–Vogt `I=1/4`
line, and C5's selector. `WORKING_RULES` records the atlas measurement that *"the trace map
recurs in **45 %** of probes"* — so the affected surface is large, but it is not the cascade.

**A7 is a different question and is not reopened.** B979 settled it: A7 lives at the **based**
level, and the swap observation is **class**-level. The two roles of `P` — conjugating element
(A7's) and substrate operation (B16's) — are distinct, and no document separates them.

## 5. A SECOND FINDING, produced by the verification failing first

**The first run of `verify.py` FAILED at link 4**, and the failure was the finding.

B62 reports height-2 splits **(2,0), (2,2), (4,2)** at n = 3,4,5 and decides the two unresolved
SL(5) modes with them. `CLAIMS.md` **P33**'s closed form gives **(1,0), (1,1), (2,1)**.
Recomputed here: **P33's numbers are right over POSITIVE roots; B62's are right over the FULL
height-±h space** (each positive root and its negative — the multiplier sector's dimension).
**B62 = 2 × P33, exactly**, and the totals check: `2(n−2)`.

**Both statements are correct. Neither declares its convention.** Two banked statements about
the same object quote different numbers, and a reader diffing them meets a discrepancy rather
than a factor of 2. This is **error class E1 — undeclared choice drift**, which
**`GOVERNANCE.md` §13 and `WORKING_RULES.md` name the programme's *most recurrent* class**
*(source corrected 2026-08-11 by B1033: this line first cited `docs/ERROR_LEDGER.md`, which
registers E1 but never makes that claim)*, and it is now pinned by a lock so the next reader
meets it as a stated fact.

*(Recorded per the campaign's stop rule 3 — propose and refute in the same file. The proposal
here was my own expected number; its refutation is above.)*

## 6. WHAT THIS ARC DOES NOT CLAIM

- **No novelty.** "Contragredient = `−w₀`" is textbook Lie theory (`K005` cites it as such). The
  content is the **identification across the corpus's own six names**, and the **input-count
  consequence** — not the Lie theory.
- **No upgrade of B62.** B62 grades itself *"a live structural result, not a theorem"*; the
  LAW_MAP row added by this arc carries that grade unchanged.
- **No claim that the derivation theorem is weakened.** §4 states the scope.
- **No physics.** Gate 5 untouched.

---

**Verdict: PROVED (mathematics).** Six links independently recomputed; one identification the
corpus holds in fragments across three registers and states in none; one input-count consequence
at a stated scope; and one convention collision found by the verification failing before it
passed.
