> **CORRECTION 2026-09-17 (xB020).** §6's named mechanism — *"a non-orientable manifold's holonomy
> lands in `PGL(2,ℂ)`, outside the `SL(2,ℂ)` theory"* — is **WRONG and is withdrawn.**
> **`PGL(2,ℂ) ≅ PSL(2,ℂ)`** (over an algebraically closed field every element has a square root), a
> fact **this same session banked two arcs earlier in xB012's V2** — so this arc contradicted xB012
> within the session. **The real mechanism is COMPLEX CONJUGATION:** `Isom(H³) = PSL(2,ℂ) ⋊ ℤ/2`,
> the extra factor anti-holomorphic and in no `PGL`. **Everything else here is unaffected** — the
> tool audit, the two bits splitting across the squaring, and the ill-posedness of the escape route
> never used that sentence, which was explicitly labelled *"not computed here."*

# xB019 — THE ONE-TICK OBJECT: B1234's live question answered, and the two bits split across the squaring

**Seat `xb`, `sep16-branch`, 2026-09-17. PREREGISTRATION sealed `e20e39f9…` and PUSHED at `55b984d`
before `verification/` existed, with its **configuration axes declared**. Verdict: PROVED.**

Gate 5 absolute: no value, no generation count, no physics reading, nothing to `CLAIMS.md`.

---

## 0. The question was already on the board, left open on purpose

xB018 named `GL(2,ℤ)` as the axis it held fixed. **The sweep found an arc already on that axis with a
question deliberately left open** — B1234:

> *"**Does not establish:** that dropping A6 makes values derivable. A non-orientable object may not
> support the machinery at all — **Chern–Simons, the complex volume and the SL(2,ℂ) representation
> theory all use orientation** — so dropping A6 may **break the tools** rather than open a door.
> **That is now the live, sharp question.**"*

**And one guess of mine died before the seal was written.** I expected A7's bit to be "GL-conjugacy
only" — that `LR` and `RL` might be conjugate in `GL(2,ℤ)` but not in `SL(2,ℤ)`. **They are conjugate
in `SL(2,ℤ)`**, conjugator `(−5,−8,−3,−5)`, `det = 1`. B979's "same conjugacy class" is an SL
statement and correct. *(The Breath pulse is exhibited in the same check: `M = [[1,1],[1,0]]`,
`det = −1`, `M² = RL` — the Fibonacci matrix, whose eigenvalue is φ itself.)*

## 1. G1 — B1234 reproduces exactly

`m000`'s orientation cover **is isometric to m004**, volume ratio **2.0000000000**. And an
independent surjection count — iterating all `24²` pairs in `SL(2,𝔽₃)` against each relator —
returns **48 for Gieseking and 48 for m004**. **B1234's cells 2 and 3 confirmed.**

**B1234's own unclaimed clause is carried, not dropped:** surjecting onto 2T is **generic (~⅓,
B993/B996)**, so the equal counts are **not** evidence of distinction. The point is only that **A6
was not needed for the arithmetic.**

## 2. G2 — the tool audit, which answers the question

| tool | m000 (one tick, non-orientable) | m004 |
|---|---|---|
| volume | **exists** — 1.01494160641 | exists |
| `H₁` | **exists** — `ℤ` | exists |
| `π₁` | **exists** — `⟨a,b \| aabbAB⟩` | exists |
| symmetry group | **exists** — `ℤ/2` | exists (order 8) |
| surjections ↠ 2T | **exists** — 48 (G1) | 48 |
| **Chern–Simons** | **BREAKS** — `ValueError: Manifold is not oriented` | exists |
| **complex volume** | **BREAKS** — `ValueError: Manifold is not oriented` | exists |

> **Exactly the two orientation-dependent tools break — and they break BY DEFINITION, not by
> difficulty.** There is no harder computation to attempt: Chern–Simons and the complex volume are
> *defined* for oriented manifolds.

## 3. G3 — the blind cell: the two bits split across the squaring

xB018 characterised each bit by the datum it acts on. Applying that here:

| bit | its datum | at tick one |
|---|---|---|
| **A5(c)** — knot-ness | `H₁` torsion-free | **`H₁(m000) = ℤ` — exists, torsion-free. POSABLE, AND ALREADY ON.** |
| **A7** — the LR/RL order | acts by **`CS` negation** (xB018 C5) | **`CS` does not exist. CANNOT BE POSED.** |

> **A5's datum survives the drop and is already satisfied. A7's datum is CREATED by the squaring.
> A7 is not a free choice the construction makes at tick one — it does not exist until tick two.**

This **matches B1083 exactly** — *"on the one-tick object chirality cannot be posed; the second tick
buys orientability and pays amphichirality"* — **reached from a different direction (the tool audit)
and agreeing.** Symmetry groups track it too: `ℤ/2` at tick one, order 8 at tick two.

## 4. G4 — the answer, and it is sharper than "hard"

**Dropping A6 does both:** the arithmetic side is **intact** (volume, `H₁`, `π₁`, symmetry group, the
trace field and the 2T route), and exactly the two orientation-dependent tools **break**.

**And then the consequence.** **Seven of B1234's eight walls are statements about `CS` or about the
mirror** — `CS = 0`; blind to `k`; amphichirality; the CP sign even in `CS`; mirror-even canonicity;
mirror-odd bits; the mirror-pair `θ`. **On the one-tick object there is no `CS` and no orientation to
mirror.**

> **So those walls do not become FALSE there — they become UNSTATEABLE. "Drop A6 to escape the walls"
> is ILL-POSED, not merely hard. There is no `CS` on the one-tick object that could be non-zero.**

**Per the seal's own reporting rule:** this is a **negative for the escape route and a clarification
of the question**. It is **not** a new wall, and it is **not** evidence *for* A6.

## 5. G5 — what the squaring buys, itemised

**Buys:** orientability · the `CS` and complex-volume **tools** · **amphichirality** (100 %-forced for
an orientation double cover, B1234 cell 1, against a 3.0 % base rate) · **and the A7 bit itself**.

**Does not buy:** the invariant trace field, the 2T route, McKay–E₆ (**48 either way**) · and **not
the A5 bit**, which is already posable and already *on* at tick one.

> **The squaring's purchase is exactly ORIENTATION and everything downstream of it — the `CS` tool,
> the mirror, amphichirality, the eight walls, and A7. It buys nothing arithmetic.**

That sharpens B1234's headline (*"the squaring buys orientability and costs every value"*) by saying
**which side each item falls on**, and by **adding A7 to the bought column** — which B1234 could not
have, because xB018 had not yet characterised the bit.

---

## 6. G6 — verdict, with every axis held fixed named

**B1234's live question is answered.** And the new structural fact: **the two bits split across the
squaring.**

**AXES HELD FIXED:** **`m000` only** — the wider non-orientable census is **not** swept, and B1234's
40-of-40 amphichirality rate is **cited, not re-derived** · the two-bit characterisation is
**xB018's**, whose own fixed axes (`SL(2,ℤ)`, `b++`/`b+-`, word length ≤ 8, A5 reading (c)) are
**inherited and not re-opened** · **`PGL(2,ℂ)` vs `PSL(2,ℂ)`** is named as the **mechanism** — a
non-orientable manifold's holonomy lands in `PGL(2,ℂ)`, outside the `SL(2,ℂ)` theory — **but is not
computed here.**

## 7. What this arc does NOT claim

Not that Gieseking is distinguished (2T surjection is generic ~⅓ — B1234's own clause) · not that
dropping A6 makes any value derivable · **not that the tools' breaking is evidence FOR A6** · no
identification (E82/I-10) · no physics reading · nothing to `CLAIMS.md`.

**Locks / artifacts:** `verification/one_tick.py` (G1–G6), `verification/one_tick.json`,
`verification/one_tick.out`.
