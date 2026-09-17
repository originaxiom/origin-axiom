# xB023 — L194's SELECTION HALF: the selection is explained, the mechanism I proposed for it is not

**Date:** 2026-09-17 · **Seat:** `xb` · **Branch:** `sep16-branch` · **Verdict: PROVED**
(ESTABLISHED / UNSETTLED, per the mixed-arc rule)

**PREREGISTRATION sealed `277542e74fa92bb4…`, committed and pushed at `cbfeec0` BEFORE
`verification/` existed**, with two binding kill conditions — **one of which fired.**

---

## THE RESULT FIRST

xB020 forced `CS` into the 2-torsion `{0, ¼}` but did **not** derive which value the object takes.

**ESTABLISHED — the selection at the object, on the full census.** Over **all 203 123 one-cusped
orientable census manifolds** (0 errors), 181 are amphichiral:

| | `CS = 0` | `CS = ¼` |
|---|---|---|
| **is an orientation double cover** | **78** | **0** |
| **is not** | 28 | 75 |

**Base rate for `CS = 0` among amphichiral non-covers: 27.2 %. Among covers: 100 %, 78 of 78.**
The kill condition — *one* quarter-class orientation double cover — **did not fire.** B1239's
bucket B had 6 zero / 5 quarter on a 3000-window; this is the entire census.

**And on the 1260 cusped orientation double covers: 1260 at class zero, 0 at ¼, 0 other.**

> **m004 sits at `0` because it carries a free orientation-reversing involution — it is the
> orientation double cover of the Gieseking manifold m000. m003 does not, and sits at `¼`.**

**UNSETTLED — and my own sealed explanation is dead.** I predicted that `|Tor H₁|` being a perfect
square is what forces this. **REFUTED: 670 of 1260 — 590 counterexamples.** The seal's instruction
was explicit (*"one counterexample kills the law and the arc must drop it entirely rather than
weaken it"*), so **it is dropped**, and W3's chain through it is **withdrawn**. xB022's `+4` torsion
law and W5's correlation (50 % square among zero-class against 16 % among quarter-class, 34 points
apart) remain **true and unexplanatory**.

---

## THE CELLS

**W0 — every banked input re-derived, none cited.** `cs(m004)` class **zero**, `cs(m003)` class
**quarter**; `H₁(m004) = ℤ`, `H₁(m003) = ℤ/5 ⊕ ℤ`; **positive control** `m000.orientation_cover()`
has isometry signature `cPcbbbiht` = m004's; `m003` is **not** an orientation double cover of any of
the 1260 census non-orientable manifolds (1117 distinct cover signatures). **Every sealed prediction
on the banked inputs reproduced.**

**W1 — the instrument gap PROVED, not relayed.** SnapPy's `Isometry` exposes exactly
`cusp_images, cusp_maps, extends_to_link, num_cusps` — **no translation**. And the reason is given
algebraically rather than asserted: for `A ∈ GL(2,ℤ)`, `A² = I`, `det A = −1`, the eigenbasis gives
`(x,y) ↦ (x + b₁, −y + b₂)`; the `y`-equation is **always** solvable, so a fixed point exists **iff
`b₁ ≡ 0`**. Freeness depends **only on the translation**, never on `A`. **Exhibited:** two
involutions with *identical* linear part, one with 24 fixed points, one free. **`cusp_maps()`
provably cannot decide L194's question.**

**W2 — the torsion prediction refuted; the CS half stands.** 1260 covers: **670 square (REFUTED)**;
**1260 of 1260 at CS class zero (0 quarter, 0 other)**. Graded a **measured result**, not a theorem.

**W3 — the selection, with the dead chain reported before its remains.** `m003` is not a cover — a
**computed fact** from W0's search, *not* a consequence of its torsion. `m004` is one. Being one
forces class zero. **The selection is explained by the free involution, not by `H₁`.**

**W4/W5 —** above. **W6 — L194 is NOT closed**, declared in the seal before any cell ran.

---

## ADDENDUM — KAWAUCHI READ, AND THIS SEAT'S OWN CRITIQUE WITHDRAWN

Beyond the seal. B1239 supports the torsion step by citing **Kawauchi, *On 3-manifolds admitting
orientation-reversing involutions*, J. Math. Soc. Japan 33 (1981) 571–589**. **This seat has now
read the paper** (`verification/kawauchi_read.py` quotes it from its own text).

> **THEOREM I.** *"Given a pair (M, α), then the torsion subgroup `T₁(M;ℤ)` … is isomorphic to a
> direct double `A ⊕ A` or a direct sum `A ⊕ A ⊕ ℤ₂` for some A."*
> — where the paper's opening defines a pair as **"M a CLOSED, ORIENTED 3-manifold, α an
> orientation-reversing involution."**
>
> **THEOREM III.** *"(1) σ(M)=0, (2) σ(α,M)=0, (3)…, (4)… are equivalent"*, with **Definition 1.2**
> making `σ(α,M)` the number of **discrete fixed points mod 2**.

**MY FIRST CRITIQUE WAS WRONG AND IS WITHDRAWN HERE.** On Theorem I alone I wrote that the
paraphrase *"invents the freeness hypothesis and drops the `A⊕A⊕ℤ₂` case."* **Both are false.**
Theorem III makes freeness do real work — `Fix = ∅ ⇒ σ(α,M)=0 ⇒ σ(M)=0 ⇒` a **strict** direct
double — so *"free ⇒"* is justified and the `ℤ₂` alternative is correctly excluded in the free case.
**Reading the paper caught this seat's own overclaim, which is the entire point of reading it.**

**The real defect is single, and it is located:** Kawauchi's pairs are **CLOSED**; B1239 applies the
consequence to **CUSPED** manifolds.

**K1 — the theorem tested on manifolds BUILT to satisfy its hypotheses.** The orientation double
cover of a closed non-orientable manifold is closed, orientable, and carries a **free**
orientation-reversing deck involution. Over four closed non-orientable censuses, **46 distinct such
manifolds: 46 of 46 have `|Tor H₁|` a strict perfect square.** 0 errors.
**Negative control from the paper's own text:** `L(p,q)`, `p > 2`, admits no orientation-reversing
involution, so `|Tor| = p` need not be square — the theorem is neither vacuous nor universal.

**K1's FIRST VERSION WAS VOID AND IS RECORDED AS VOID.** It filtered the closed census by
`is_amphicheiral()`, which says only that an orientation-reversing **isometry** exists — possibly of
order 4 or 6 — while Kawauchi's `α` is an **involution**. The hypothesis did not match the theorem's,
so the cell tested nothing, and it duly "refuted" a published theorem on 29 of 36 cases.
**A census check overturning a 1981 theorem is essentially never the right reading.** This is E58's
shape one level up: **not a misquoted theorem, but a mismatched hypothesis.**

**K2 — the closed hypothesis is load-bearing, measured.** The same predicate on the 1260 **cusped**
covers: **670 of 1260 strict doubles (53.2 %)**, 836 (66.3 %) under Theorem I's full form —
**590 failures.** These all carry free deck involutions by construction, so the gap is **not** the
dropped `ℤ₂` alternative: **it is the closed hypothesis.**

**K3 — the damage, stated so it is not inflated.** B1239's **main** closed-manifold conclusion
(`cs ∈ {0,½}` mod 1) rests on **APS with `τ` an integer, not on Kawauchi**. Kawauchi enters only for
the finer `0`-vs-`½` step, which B1239 itself records as **invisible to SnapPy's mod-½ readout**.
**The error is real, located, and contained.**

---

## WHAT THIS DOES NOT DO

**It does not close L194** — declared in the seal before any cell ran. The general cusp-local lemma
still needs the translation part W1 proves SnapPy does not expose. It supplies **no value**. It does
not claim the `0`-vs-`½` distinction SnapPy cannot see.

**Axes held fixed and named:** the census window is stated numerically (203 123 one-cusped
orientable; 1260 non-orientable cusped; 46 constructed closed pairs) and **nothing is generalised
past it** · `CS` read mod ½ · Meyerhoff–Ouyang, L194's other named tool, is **paywalled and remains
UNREAD** — it is cited nowhere in this arc.

**Gate 5 absolute. Nothing to `CLAIMS.md`.**
