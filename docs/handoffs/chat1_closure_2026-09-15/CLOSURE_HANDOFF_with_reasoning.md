# chat1 → cc : CLOSURE HANDOFF, 2026-09-15
## Written as reasoning, not as results. The worries are the payload.

**Seat status unchanged: no branch, no write access, zero arc numbers, E71 exposure nil,
does not persist.** This supersedes nothing in the earlier handoff; it continues it.

**Read this one for the doubts.** Every section below records what we believed, what we
computed, and what killed it. Several of the killings are of my own claims, and the last
section kills most of the document. That is the point — if you only take the surviving
results you will inherit the confidence without the corrections that earned it.

--------------------------------------------------------------------------------
# 0. WHERE THE LAST HANDOFF LEFT IT, AND WHY IT WAS WRONG

I closed with: **"chirality or forcedness — that trade is now stated with both sides
proved."** m004 is forced (Jørgensen) but amphichiral; m202/s959 are chiral but named by no
uniqueness theorem. Pick one.

**The owner dissolved it in one message,** and the correction is a *level* error, not a
detail:

> Parity sorts the requirements. Cohomology dimensions are homeomorphism invariants and
> `Mbar ~= M`, so **counts are mirror-EVEN** — they survive anywhere. B1297 T1 banks
> `I(V*) = -I(V)`, so the **index is mirror-ODD** — on a self-mirror object it equals its
> own negative, hence **zero, FORCED**.
>
> **On m004, chirality is a THEOREM-ZERO; the count is merely ABSENT.**
> In a frontier list those look identical. They are different in kind.

Then: all three of m004, m202, s959 have trace field `Q(sqrt-3)`; a cusped manifold with
imaginary-quadratic invariant trace field is arithmetic; same field ⇒ **commensurable**.
**The forcing selects the CLASS. The physics lives on a member.** No trade.

**Worry to carry:** I stated that trade twice, with confidence, in a document you have
already intaken. The failure mode is attaching a theorem about one object to the wrong
level of the structure. It is the same shape as the m004-face collapse the owner has been
naming for months, and I reproduced it while writing the correction to other people's
instances of it.

--------------------------------------------------------------------------------
# 1. THE CLASS IS THE OBJECT  [VERIFIED]

Humbert's formula: `vol(H^3/PSL(2,O_3)) = 0.169156934`. Then, to six decimals:

| | index in `PSL(2,O_3)` | Sym | order-3 elements |
|---|---|---|---|
| `m004` | **12** | `D_4` = orders {1,2,4} | **0** |
| `m202` | **24** | `D_6` | 2 |
| `s959` | **36** | `D_6` | 2 |

`PSL(2,O_3)` carries torsion of orders 2 **and** 3. **m004 at index 12 cannot see the
3-torsion; m202/s959 can.** The order-3 was never absent from the object — it is
**invisible at that depth**. The Bianchi orbifold is itself forced (Meyerhoff 1985:
minimal-volume cusped orientable hyperbolic orbifold), so the class has its own uniqueness
theorem, independent of Jørgensen's on m004.

--------------------------------------------------------------------------------
# 2. A LAW I PROPOSED AND KILLED IN ONE STEP  [WITHDRAWN]

Under pressure to be brave I proposed: **"everything forced is mirror-even; every sign is
chosen"** — i.e. *a derivation cannot output a hand*. It held on six objects with no
counterexample, and I stated it as a consequence about the limits of derivation itself.

**Refuted by the first honest falsifier test.** The **Weeks manifold** `m003(-3,1)` —
unique minimal-volume closed orientable hyperbolic 3-manifold (Gabai–Meyerhoff–Milley
2009) — is **forced and CHIRAL**. So are `m129` and `m125`.

**Worry:** six data points became a principle about mathematics in general, one message
after I told the owner my failure mode is over-reading positives. The falsifier was obvious
and I only ran it because the owner asked for the next step.

--------------------------------------------------------------------------------
# 3. FOUR PROPERTIES, NOTHING HAS ALL FOUR  [VERIFIED]

| | forced | chiral | 2T door | order-3 |
|---|---|---|---|---|
| `m004` | yes | **no** | 48 | **0** |
| Weeks `m003(-3,1)` | yes | yes | **0** | 2 |
| `m129` / `m125` | yes | yes | 192 | **0** |
| `m202` / `s959` | **no**\* | yes | 96 / 576 | 2 |

\*forced at class level (§1). Weeks has `H_1 = Z/5 + Z/5` — the prime 5 twice — and **still
zero** surjections to `2I = SL(2,F_5)`: **having the prime in homology does not open the
door.** Its invariant trace field is cubic, a different commensurability class.

Census scan (1400): exactly **four** manifolds have chiral + door + order-3 —
`m202`, `s776`, `s784`, `s959` — splitting by field:
`m202`,`s959` → `Q(sqrt-3)`, cusp traces `[-1,-1]`, **det(A-I) = 3** (the count);
`s776`,`s784` → `Q(sqrt-7)`, cusp traces `[2,..]`, **det(A-I) = 0** (no count).
**Correction to my earlier claim:** the 2T door is NOT determined by the trace field —
`s776` has `Q(sqrt-7)` and 1152 surjections while `m009` has the same field and 0.

--------------------------------------------------------------------------------
# 4. THE TWO Z/3's — THREE LINKS VERIFIED, THE FOURTH REFUTED
### *(this is the most important section; it kills the SM assembly's last joint)*

**VERIFIED.** `(sqrt-3)` is the ramified prime, `O_3/(sqrt-3) = F_3`, `omega -> 1`. An
order-3 element of `SL(2,O_3)` (trace −1) reduces to `[[0,2],[1,2]]`: det 1, **order
exactly 3**, **unipotent** (`(A-I)^2 = 0`). All **8** order-3 elements of `2T` have trace
2 ≡ −1 and **none lies in `Q_8`**, so each generates `Z/3 = 2T/Q_8`.
`det(Cartan E_6) = 3 = |Z(E_6)| = |2T/Q_8|`.

**REFUTED.** `Z/3 = 2T/Q_8` acts on irreps by **tensoring with a character**, which
preserves dimension: it cycles the three 1-dims, cycles the three 2-dims, and **fixes the
unique 3-dim**. That is the **arm rotation** of affine `E_6`, acting on finite `E_6` as the
**CENTRE**. The centre acts by **scalars** (`27 -> omega*27`, `27bar -> omega^2*27bar`) and
**does not grade the algebra**. The Kac grading with `g_0 = A_2^3` (trinification) is a
**different, non-central** order-3 automorphism.

> **The Z/3 the arithmetic supplies is the centre. The Z/3 the SM assembly needs is not.**

**This is the joint the whole trinification chain rested on.** I had it marked as the last
remaining input; it is not open, it is **false along this route**.

**Worry:** I nearly reported the three verified links as "the chain closes." The fourth
link is the only one that mattered and it is the one that fails.

--------------------------------------------------------------------------------
# 5. LEFSCHETZ: L(g) = 3, AND omega/omega^2 ON H^1  [VERIFIED, FORCED]

`|det(A-I)| = 3` is the number of fixed points of `A` on the cusp torus. **Three fixed
points per cusp ⇒ the Z/3 is NOT free**; the quotient is an orbifold with singular locus.
Two cusps → 6 ends → **3 arcs** (+ possible circles, `chi = 0`) → `chi(Fix) = 3`, so by
Lefschetz **L(g) = 3** on both `m202` and `s959`.

Then, and this is **forced not assumed**: a 1-dimensional **rational** rep of `Z/3` must be
trivial (`omega` is irrational), and `b_2 = 1`, so `tr_2 = 1`. With `b_1 = 2` and
`L(g) = 1 - tr_1 + tr_2` this gives **`tr_1 = -1`**, which over `Q` is uniquely the
2-dimensional irreducible: **eigenvalues `omega, omega^2`, no invariants.**

**H^0 → 1 · H^1 → omega, omega^2 · H^2 → 1.** The base carries exactly the three
cube-root sectors.

**Worry, and I raised it myself:** `det(A-I) = 3` is `trace = -1` is "order 3". Three fixed
points, six ends, three arcs, `L = 3`, `omega/omega^2` — **one fact in five vocabularies,
not five pieces of evidence.** B727's lesson, committed by me, one message after verifying
its most important instance.

--------------------------------------------------------------------------------
# 6. THE MATCHING, COMPUTED — AND THE OBSTRUCTION IT EXPOSES  [VERIFIED]

Diagonal `Z/3` on base × fibre; invariants are eigenvalue products equal to 1:

| H^1 piece | rep | product | invariant |
|---|---|---|---|
| `omega` | `27` | `omega^2` | no |
| `omega` | `27bar` | **1** | **yes** |
| `omega^2` | `27` | **1** | **yes** |
| `omega^2` | `27bar` | `omega` | no |

**27 → 1, 27bar → 1. Difference 0. VECTOR-LIKE.**

And the reason is general: `H^*(X;Q)` is a **rational** rep of `Z/3`; every rational
`Z/3`-rep is `(trivial)^a + (2-dim irreducible)^b`; the 2-dim irreducible carries **one
`omega` and one `omega^2`**. So **`omega` and `omega^2` multiplicities are ALWAYS EQUAL —
any space, any `Z/3` action, any `b_1`.**

> **Any diagonal `Z/3` twisting against a central charge gives equal 27 / 27bar counts.
> Vector-like, always. A fact about rational cohomology, not about m004 or its class.**

This is **stronger than the F_4 vector-like theorem and independent of it**: F_4 kills
`sl_2`-factored (order-2) holonomy; **rationality kills every `Z/3` orbifold twisting on
every base.** My own morning result — "order 3 is inner, escapes F_4" — is true and
**useless**: it escapes the weaker obstruction into the stronger one.

--------------------------------------------------------------------------------
# 7. WHERE THE OBSTRUCTION FAILS  [VERIFIED]  — and §8 deflates this

**Maschke:** `k[Z/3]` is semisimple iff 3 is invertible in `k`. Over `Q` **and over
`Q(omega)`**, every `Z/3`-module is semisimple and `Ext^1 = 0`. **R27's nonsemisimple
module cannot live over either. It requires characteristic 3.**

In char 3: `x^3 - 1 = (x-1)^3`, there is **no primitive cube root of unity**
(`omega = omega^2 = 1`), an order-3 element is **unipotent**, and modules are distinguished
by **Jordan block size** — extension data, exactly what semisimplification destroys and
traces cannot see.

**Reproduced explicitly on the programme's own objects** (Fox calculus mod 3, using a
homomorphism `pi_1 -> F_3` which exists because `b_1 = 2`):

| | traces | `h^1` nonsemisimple | `h^1` semisimplification |
|---|---|---|---|
| `m202` | (2,2) identical | **2** | **4** |
| `s959` | (2,2,2) identical | **5** | **6** |

**Same character, different cohomology.** This is R27's reported phenomenon —
*"semisimplification has index zero despite the same trace on every word"* — shown to be
**generic in characteristic 3**, not a property of whatever module R27 found.

--------------------------------------------------------------------------------
# 8. THE DEFLATION — READ THIS BEFORE USING §§6–7

The owner asked whether §7 was actually new. **On the evidence, mostly not.**

**All of it is textbook.** Maschke 1899. `x^3-1 = (x-1)^3` in char 3. Unipotents have order
`p` in char `p`. Cohomology is not a character invariant. Rational characters pair `omega`
with `omega^2`. **Modular representation theory is a century old and this is its first
page.** No new mathematics was produced.

**The "convergence" is largely tautological.** Maschke fails at `p` exactly when `p`
divides `|G|`; I chose `G = Z/3`, so it fails at 3 — definitional. `Q(sqrt-3) = Q(omega)`
ramifies at 3 *because* it is the cube-root field. **These are not three independent 3's
meeting. They are one 3, because the construction is about 3.** Same error as §5's worry,
at larger scale.

**And the corpus already lives there.** Word-boundary counts on `origin/main`:
`F_p` **114** · `unipotent` **88** · `semisimple` **79** · `reductive` 26 · `Jordan block`
17 · `F_3` 12 · `modular representation` 6 · `Maschke` 5 · `Brauer` 5 ·
`characteristic 3` 4. **`nonsemisimple`: 0** — a missing word, not a missing result.
`SL(2,F_3)` **is** the door and has been since B266. I "found" the field the programme has
been standing in for a thousand arcs.

--------------------------------------------------------------------------------
# 9. THE RESIDUE — what I would actually bank

**(a) One checkable scoping item, and it is the only thing here with leverage.**
If B1330's 952 sectors and B1331's `L_V` were computed with **semisimple / complex
coefficients**, then by §6 their zeros are **guaranteed by Maschke before the computation
runs**, and should be rowed as **scope**, not as evidence of absence. One check against
those two arcs. Either it is true and deserves a row, or it is false and §§6–8 evaporate.

**(b) Two computations that are mine and correct:** the `h^1` pairs in §7 on `m202`/`s959`
with identical traces. A worked example of R27's phenomenon on the programme's objects.
**An example, not a finding.**

**(c) The §4 refutation.** The arithmetic `Z/3` is the **centre**, not the Kac grading. This
one does not deflate and it removes the SM assembly's last joint.

**(d) §1 and §3's tables.** Measured, reproducible, and they relocate the campaign's
objects.

--------------------------------------------------------------------------------
# 10. THE METHODOLOGICAL RECORD

Across this session, **every result that survived was negative or came from outside me**:
- the owner's parity insight → dissolved the trade (§0) and located `m202`/`s959`
- the owner's "a dead end is a new lead" → re-read five walls as localisations, three held
- the owner's "are you sure it's new" → produced §8, which demotes my best-feeling result
- the Weeks manifold → killed my law (§2)
- Maschke → killed my "order 3 escapes F_4" as useless (§6)
- the corpus's own grep → killed §7's novelty (§8)

**My computations held. My readings of them failed, repeatedly.** Where a control existed,
it caught me — nine times. Where one didn't, I over-read. **The division cc proposed —
this seat computes and sweeps, interpretation is gated elsewhere — is supported by the
measured rate, not by modesty.**

**If you take one thing:** §9(a) is checkable in minutes and either matters or doesn't.
Everything else in §§5–8 should be held at the confidence level §8 assigns it.
