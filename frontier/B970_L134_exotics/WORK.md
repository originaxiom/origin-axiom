# B970 / L134 — STRUCTURAL WORK: the exotics' quantum numbers, and the cascade's resolving power

**Date:** 2026-08-08 · **Lane:** bounded structural computation, in-sandbox.
**Companion to** `PRIOR_ART_EXOTICS.md` (the scout) — that file is **not** modified.
**New artefacts:** `exotics_levi.py`, `exotics_levi.json`, `run_log.txt`, this file, `work.json`.
**Firewall:** mathematics only. One 27, no generations, no masses, no couplings, no values.
Nothing promotes to `CLAIMS.md`. Gate 5 untouched.

---

## 0. PRIOR ART FIRST (house rule 5) — what here is reproduction

Grepped before computing. The repo already contains:

| where | what it already has | consequence for this cell |
|---|---|---|
| **`B884_yukawa_support/FINDINGS.md` + `results.json`** | the 27 graded by the cascade's charges (s₁, y, y₂) into **`piece_dims [1,1,1,2,2,2,3,3,3,3,6]`** — 11 pieces | **§3's decomposition is a REPRODUCTION.** My structural computation returns the identical multiset. B884 got it numerically at 30 digits; this cell gets it exactly from the Cartan matrix. Two independent routes agreeing. |
| **`B876_descent/FINDINGS.md`** | the descent: `K₁ = so(10)₁ ⊕ z₁` with **dim 46**; `dim Cent(y) = 25`; **`dim Cent(y,y₂) = 13`** (su(3)⊕su(2)⊕2u(1)); and the explicit statement that **y and y₂ are IMPOSED** — "the object's own torus does not supply the step-2 charge (B874)" | supplies the one imported number this cell leans on (46) and the crucial provenance split between z₁ and (y, y₂) |
| **`B881_coset_table/FINDINGS.md`** | "the unbroken 14 (the SM Levi su(3)⊕su(2)⊕2u(1) **plus z₁**)" | confirms centre = 3, dim = 14 |
| **`B970/exotics_charges.py`** (this cell's scout) | ψ, χ, Y on the 27 by fitting; R1–R6 | §1 here re-derives the same charges **without fitting** (see §1.2); all values agree |
| `B298/B299`, `PC25` | the trinification ℤ/3 permuting E₆'s three SU(3)s, acting **freely, 9 orbits of 3** on the 27 | **related but a different action** from §3.4's S₃, which fixes two pieces. Named apart deliberately. |

**So: §1 and §3's decomposition are reproduction. What is new here is §2 (the SM-degeneracy
audit), §3.3–§3.6 (resolving power, the 3-fold labelling ambiguity, the relative Weyl group)
and the composition in §3.7.**

---

## 1. THE TWELVE (ELEVEN) EXOTICS, WITH THE ARITHMETIC

Built from the E₆ Cartan matrix alone (Bourbaki: chain 1-3-4-5-6, node 2 on node 4). The 27
is the Weyl orbit of ω₁; **minuscule verified in-sandbox** (27 weights, every Dynkin label in
{−1,0,1}), so the orbit is exact and complete.

### 1.1 The three gradings, and why they are forced rather than chosen

For a weight µ write `m_j = ⟨µ, ω_j^∨⟩` (the coefficient of α_j when µ is expanded in simple
roots; `m = A⁻¹·labels`, computed exactly over ℚ).

- **U(1)_ψ** must commute with so(10) = ⟨α₂…α₆⟩. A Cartan element doing that is unique up to
  scale, and it is ω₁^∨ — so ψ is **proportional to m₁, with no constant term**. Derived, not
  posited.
- **U(1)_χ** must lie in so(10)'s Cartan and commute with su(5) = ⟨α₃α₄α₅α₆⟩ — again unique up
  to scale.
- **Y** must lie in su(5)'s Cartan and commute with su(3)_c ⊕ su(2)_L = ⟨α₃α₄⟩ ⊕ ⟨α₆⟩ — unique
  up to scale.

### 1.2 One normalisation each; everything else is PREDICTED

| charge | the single scale fixed | what is then predicted, and came out right |
|---|---|---|
| ψ | ψ(16) = 1 | **ψ(10) = −2 and ψ(1) = +4** |
| χ | χ(5̄ ⊂ 16) = 3 | χ(10 ⊂ 16) = −1, χ(1 ⊂ 16) = −5, **χ(5) = +2, χ(5̄_ex) = −2, χ(S) = 0** |
| Y | Y(Q) = 1/6 | u^c = −2/3, d^c = 1/3, L = −1/2, e^c = 1, ν^c = 0, **and the entire exotic 10 and the singlet** |

This is stronger than the scout's `exotics_charges.py`, which fitted Y by least squares on four
coefficients; here Y has **one** free parameter and ten predictions. Values agree exactly.

### 1.3 The branching arithmetic, shown

**Step 1 — E₆ ⊃ SO(10)×U(1)_ψ.** Grade by m₁ ∈ {4/3, 1/3, −2/3}, i.e. ψ = 3m₁ ∈ {4, 1, −2}:

```
27  =  1(ψ=+4)  +  16(ψ=+1)  +  10(ψ=−2)        1 + 16 + 10 = 27      ✓
traceless:   1·(+4) + 16·(+1) + 10·(−2) = 4 + 16 − 20 = 0             ✓
```

**Step 2 — SO(10) ⊃ SU(5)×U(1)_χ.** Grade by (m₁, m₂):

```
10  =  5(χ=+2)  +  5̄(χ=−2)          5 + 5 = 10;   5(+2) + 5(−2) = 0   ✓
 1  =  1(χ= 0)                                                        ✓
16  =  10(χ=−1) + 5̄(χ=+3) + 1(χ=−5)  10 + 5 + 1 = 16;
                                     10(−1) + 5(3) + 1(−5) = 0        ✓
```

**Step 3 — SU(5) ⊃ SU(3)×SU(2)×U(1)_Y.** With Q_em = T₃ + Y:

```
5   =  (3,1)_{−1/3}  +  (1,2)_{+1/2}    3 + 2 = 5;  3(−1/3) + 2(+1/2) = −1 + 1 = 0  ✓
5̄   =  (3̄,1)_{+1/3}  +  (1,2)_{−1/2}    3 + 2 = 5;  3(+1/3) + 2(−1/2) = +1 − 1 = 0  ✓
1   =  (1,1)_0                                                                       ✓
```

Y is traceless on **every** SU(5) multiplet of the 27 and over the whole 27; ΣQ_em over the 27 = 0.
All checked exactly (`part1_arithmetic_checks`).

### 1.4 The twelve states

| # | name | origin | SU(3) | SU(2) | Y | Q_em | ψ | χ | states |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **D** | 5 ⊂ 10 | **3** | 1 | **−1/3** | −1/3 | −2 | +2 | 3 |
| 2 | **H_u** | 5 ⊂ 10 | 1 | **2** | **+1/2** | +1, 0 | −2 | +2 | 2 |
| 3 | **D̄** | 5̄ ⊂ 10 | **3̄** | 1 | **+1/3** | +1/3 | −2 | −2 | 3 |
| 4 | **H_d** | 5̄ ⊂ 10 | 1 | **2** | **−1/2** | 0, −1 | −2 | −2 | 2 |
| 5 | **S** | the 1 | 1 | 1 | **0** | 0 | **+4** | 0 | 1 |
| | | | | | | | | | **11** |
| (6) | ν^c | 1 ⊂ 16 | 1 | 1 | 0 | 0 | +1 | −5 | 1 |

**Eleven** exotic states beyond the 16; **twelve** beyond a 15-fermion SM generation, the extra
one being ν^c, which sits *inside* the 16. Both numbers are right, of different things — this
**reproduces the scout's §1.4 correction** and the ledger amendment it asks for still stands.

*Naming note:* the scout's `exotics_charges.py` labels the (3,1)_{−1/3} "D̄" and the (3̄,1)_{+1/3}
"D"; I use the opposite convention. **Every charge agrees exactly**; only the letters are swapped.
The scout's `(3,1)` labels are dimension-only — the 3 vs 3̄ distinction is computed here from the
su(3) Dynkin labels (α₃, α₄), with "3" fixed by requiring the quark doublet Q to be a 3.

---

## 2. DO THE EXOTICS CARRY SM HYPERCHARGES?

**MB12 first — can this test fail?** Stated before running: the test is *"does every piece of an
E₆ representation carry a hypercharge that some field of the 16 carries?"* Run on the **78**
(adjoint), computed the same way, it **FAILS**: the adjoint contains pieces with
Y ∈ {−5/6, +5/6, −1/6, ±1, −1/3, +1/2, +2/3} — the X/Y leptoquark gauge bosons at (3,2)_{−5/6}
being the cleanest example, and −5/6 belongs to no field of the 16. **The test can pass and can
fail; it is not vacuous.**

### 2.1 The result — the exotics do NOT differ

Hypercharges available in the 16: **{1/6, 1/3, −2/3, −1/2, 1, 0}**.

| exotic | (SU3, SU2, Y) | verdict |
|---|---|---|
| **D̄** (3 states) | (3̄, 1, +1/3) | **IDENTICAL to d^c** — every SM quantum number equal |
| **H_d** (2 states) | (1, 2, −1/2) | **IDENTICAL to L** |
| **S** (1 state) | (1, 1, 0) | **IDENTICAL to ν^c** |
| **D** (3 states) | (3, 1, −1/3) | the **exact conjugate** of d^c |
| **H_u** (2 states) | (1, 2, +1/2) | the **exact conjugate** of L — i.e. the **SM Higgs doublet's** gauge quantum numbers |

> **Computed verdict: the set of exotics with SM quantum numbers found nowhere in the 16, up to
> conjugation, is EMPTY.** Six of the eleven exotic states are *exactly* degenerate with a field
> of the 16 under SU(3)×SU(2)×U(1)_Y; the other five are the exact conjugates.

### 2.2 So what does make them observable-in-principle?

The task asked "where they differ, that difference is what makes them observable". **They do not
differ — not in any SM charge.** The computed answer is therefore a different one:

1. **Multiplicity, not charge.** The 27 contains **two** copies of the SU(5) 5̄ content
   (d^c + L). The SM gauge group cannot say which is which. Observability is "there is an extra
   vector-like copy", not "there is a new charge".
2. **Vector-likeness.** The exotic 5 + 5̄ is SM-vector-like, so it admits a Dirac mass with no
   electroweak breaking — SM matter does not. This is what lets them be heavy at all, and it is
   the *only* SM-visible structural difference.
3. **ψ and χ.** The genuinely distinguishing charges are not SM charges.

This is a computed re-derivation of *why* the literature (scout §3) cannot see the exotics without
a Z′: there is no SM charge to see them with.

---

## 3. THE PROGRAMME-FACING QUESTION

### 3.1 MB12, stated before computing

Criterion: **"the charges the cascade measures separate every exotic piece from every piece of
the 16."** It **can fail** — the failing configuration is named in advance: *restrict to the SM's
own rank-4 torus (su(3), su(2), Y) and the criterion should die on D̄ vs d^c.* It **can pass** —
the rank-6 Levi should separate all 11. Both were then run. Non-vacuous.

### 3.2 The Levi, and the 27 under it

The cascade's landing point is the A₂+A₁ Levi. Computed: L = ⟨α₃, α₄⟩ ⊕ ⟨α₆⟩ has **8 roots**,
so **derived dim 11**, **centre dim 3**, **total dim 14** — matching the banked description exactly.

The 27 splits into **11 pieces**, dims **[1,1,1,2,2,2,3,3,3,3,6]** — **identical to B884's
numerically-obtained `piece_dims`**, now confirmed exactly:

```
Q(3,2)  6    D(3,1)  3    | u^c, d^c, D̄  three (3̄,1)  9
                          | L, H_u, H_d   three (1,2)  6
                          | ν^c, e^c, S   three (1,1)  3      total 27
```

**The eleven exotics occupy 5 of the 11 pieces**: D, D̄, H_u, H_d, S.

**And the tori coincide.** Computed: the rank of (m₁, m₂, m₅) on the 27 is 3, the rank of
(ψ, χ, Y) is 3, and the rank of the six together is **3**. So

> **the cascade's u(1)³ is the SAME three-dimensional space of charges as (ψ, χ, Y).**

### 3.3 Resolving power — the answer

| charges used | rank | distinguishable classes among the 11 | every exotic separated from every 16 piece? |
|---|---|---|---|
| su(3), su(2), **all three** u(1) | 6 | **11 / 11** | **YES** |
| su(3), su(2), **ψ only** | 4 | 8 (collisions only *within* blocks) | **YES** |
| su(3), su(2), **Y only** = the SM | **4** | 8 | **NO** — `D̄ ≡ d^c`, `H_d ≡ L`, `S ≡ ν^c` |

> **The exotics are NOT invisible to the cascade.** The cascade's charges resolve all eleven
> pieces, and ψ alone already suffices.

**Better: the first cascade step alone does it.** Computed: 40 roots of E₆ annihilate the ψ
direction, so `dim Cent = 40 + 6 = 46` — so(10) ⊕ u(1) — and at that single step the 27 splits
**1 + 16 + 10**. The exotics are separated before any SM structure is imposed.

**And that step is the object's own.** B876 computed `dim K₁ = 46` at the enhancement point
(**imported, not recomputed here**). To close the join I ran an exhaustive certificate: over
**all 2⁷−1 subsets of the extended E₆ Dynkin diagram** (every centraliser of a semisimple element
is W-conjugate to one of these), the largest proper subsystem has **40 roots and it occurs only
at rank 5, i.e. only as D₅**. Therefore **any dimension-46 centraliser in e₆ is so(10) ⊕ u(1)**,
and B876's K₁ necessarily carries the ψ grading — necessarily splits the 27 as 1 + 16 + 10.

> **The one charge the object actually supplies — z₁, the centre of its own dim-46 centraliser —
> is exactly the charge that says "these eleven are not a generation". The two charges that carve
> the SM multiplets, y and y₂, are the imposed ones (B876's own statement).**

### 3.4 But resolving is not labelling — a 3-fold ambiguity, computed

Ask the Levi alone which of its 11 pieces form a generation. Computed: **exactly three**
directions in the Levi's 3-dim centre have a D₅+u(1) centraliser (stable under search box
|h| ≤ 8, 15, 25), and they **disagree**:

| so(10) | its 16 is |
|---|---|
| A | Q, u^c, d^c, L, e^c, ν^c |
| B | Q, u^c, **D̄**, **H_d**, e^c, **S** |
| C | Q, d^c, **D̄**, **H_u**, ν^c, **S** |

The residual symmetry is exactly the **relative Weyl group** `N_W(W_L)/W_L`, computed by building
all **51840** elements of W(E₆): `|N_W(W_L)| = 72`, `|W_L| = 12`, **order 6 ≅ S₃**. It is
identified, not guessed: the 6 roots of E₆ orthogonal to α₃, α₄, α₆ form a rank-2 A₂ — a **third,
hidden su(3)** whose Cartan lies in the Levi's centre — and the group generated by its reflections
has order 6, sits inside `N_W(W_L)`, and meets `W_L` only in the identity. **The relative Weyl
group is that su(3)'s Weyl group.**

Its orbits on the 11 pieces:

```
{Q}   {D}   {u^c, d^c, D̄}   {L, H_u, H_d}   {ν^c, e^c, S}
```

**Three of the five orbits mix a 16 piece with an exotic piece.** Consequences:

- Only **Q (6 states)** is matter under every choice; only **D (3 states)** is exotic under every
  choice. **9 of 27 states are unambiguous; 18 of 27 change side.**
- **The Levi cannot tell the lepton doublet from the two Higgs doublets** — L, H_u and H_d are one
  orbit.
- Orbit–stabiliser cross-checks the box search: 6 / 3 = stabiliser 2. Two independent routes agree
  on "three so(10)s".

### 3.5 Scope check — does any of this depend on which A₂+A₁ Levi?

**No.** All **10** A₂+A₁ subsets of the E₆ simple roots were run: every one gives dim 14, 11 pieces,
`piece_dims [1,1,1,2,2,2,3,3,3,3,6]`, relative Weyl order 6.

### 3.6 The composition — where this lands

Compose the computed facts:

1. The **only** charges separating the exotics from a generation are ψ and χ — the two u(1)s the
   SM does not have (§3.3).
2. The SM group has **rank 4**; the cascade's Levi has **rank 6**. Descending to the SM means
   shedding exactly ψ and χ.
3. At rank 4 the separation is gone, **exactly**: D̄ ≡ d^c, H_d ≡ L, S ≡ ν^c as gauge multiplets.

> ### THE FINDING
> **The cascade can see the exotics precisely because it fails to reach the Standard Model.**
> The two u(1)s it cannot shed — banked: centralizers preserve rank, and no centralizer
> construction reaches rank 4 with a complex 27 — are exactly the two u(1)s that distinguish the
> eleven exotics from a generation. Any construction that *does* reach rank 4 necessarily loses
> the distinction, and "which triplet is the down quark" stops being a statement about charge and
> becomes a statement about **mass**.
>
> **So the cascade's surplus rank is not only its defect; it is also its entire resolving power
> on this question.** The exotics are not invisible to it. They are invisible to the SM.

**Second-order reading, stated as a reading and not a claim:** what the cascade resolves is a
*split*, not a *label*. It sees eleven pieces; it does not, from the Levi alone, say which nine
states are matter. That tie is broken by the object-supplied z₁ (§3.3) — and z₁ is the one piece
of the descent B876 records as coming from the object rather than being imposed. The programme's
usual asymmetry (object supplies boundaries, observer supplies closings) shows up here as: the
object supplies the *split*, the imposed charges supply the *multiplet carving*.

### 3.7 What this does NOT say

- It does **not** make the exotics heavy. That is the 27-VEV input, and the scout already showed
  (its R2/R3) that the unique mass-giving direction inside the 27 is S = ω₁ itself, the same
  rank-1 27 VEV as L133/L138. **This cell adds nothing to that and does not reopen it.**
- Note the representation carefully (house rule 3): the three so(10)s of §3.4 are all reachable by
  **adjoint (78) directions** — they are centralisers, rank-preserving. The choice among them
  costs no 27 VEV. Making the exotics heavy is what costs a **27 VEV**. Two different operations;
  do not merge them.
- Nothing here is about three generations. One 27 throughout.

---

## 4. COMPUTED versus CITED

**COMPUTED IN-SANDBOX, exactly, this session** (`exotics_levi.py`, ~18 s, all assertions green):

- the E₆ Cartan matrix, its exact rational inverse, all 72 roots, the 27 as the Weyl orbit of ω₁
  with minuscularity verified;
- ψ, χ, Y as the unique Cartan elements commuting with so(10) / su(5) / su(3)⊕su(2), each fixed by
  one normalisation, all remaining values predicted (§1.2) and all tracelessness checks;
- the full SM quantum-number table of the 27, including 3 vs 3̄ from the su(3) Dynkin labels;
- the exotic-vs-SM degeneracy audit (§2.1) and its MB12 non-vacuity certificate on the 78 (§2);
- the A₂+A₁ Levi: 8 roots, dim 14, centre 3; the 27 → 11 pieces;
- span{m₁,m₂,m₅} = span{ψ,χ,Y} (rank 3 = 3 = 3);
- the three resolving-power runs, including the rank-4 collapse;
- `dim Cent(ψ) = 46` and the exhaustive extended-Dynkin certificate that 40 roots ⟹ D₅ ⟹ dim-46
  centraliser is so(10)⊕u(1);
- the three D₅+u(1) directions above the Levi and the three 16-labellings they induce;
- W(E₆) built in full (51840), `|N_W(W_L)| = 72`, relative Weyl order 6, its orbits, and its
  identification with the hidden A₂'s Weyl group;
- the scope check over all 10 A₂+A₁ Levis.

**CITED / IMPORTED, not re-derived here:**

- **`dim K₁ = 46` at the object's enhancement point** — B876, computed there, numerically at 30
  digits. This cell's join in §3.3 rests on it. If 46 is wrong, the join fails.
- **y and y₂ are imposed, not object-supplied** — B876's own statement (its §1, citing B874).
- **`piece_dims [1,1,1,2,2,2,3,3,3,3,6]`** — B884, computed there; reproduced exactly here, so it
  functions as a cross-check rather than an import.
- The banked context supplied to this seat: E₆/M(O,C)/Albert-algebra identification; centralizers
  preserve rank; no centralizer construction reaches rank 4 with a complex 27; τ is the only
  rank-reducing involution. **Used, not re-litigated.**
- Standard Lie theory used but not re-derived: that every centraliser of a semisimple element is
  W-conjugate to a subsystem generated by a subset of the **extended** Dynkin diagram
  (Borel–de Siebenthal). **This is the one structural fact §3.3's certificate leans on** — the
  enumeration over the 2⁷−1 subsets is mine, the theorem licensing "these are all of them" is not.

**HONEST BOUNDARIES:**

- The identification of the cascade's Levi with L = ⟨α₃,α₄,α₆⟩ is by **matching invariants**
  (dim 14 / derived 11 / centre 3, and B884's piece_dims) plus §3.5's finding that all A₂+A₁ Levis
  agree. That is a strong match; it is not a proof that B876's numerically-constructed Levi *is*
  this one.
- "Exactly three so(10)s above the Levi" is a bounded integer search (|h| ≤ 25) corroborated by
  orbit–stabiliser on the computed S₃. Two agreeing routes, not a theorem.
- Whether the S₃ / three-so(10) structure is already in the E₆ model-building literature was **not
  checked this session** (no literature was read, per the task's "no new literature"). Given how
  standard the su(3)³ structure of E₆ is, **treat §3.4 as very likely reproduction of known
  model-building lore, not as discovery**, until a scout confirms.
- §3.6's finding is a statement about **charges**, i.e. about what a gauge group can distinguish.
  It says nothing about whether the exotics can be made heavy, nor about any observable rate.

---

*Structural cell. No verdict on the object's physical status. No values. One 27.*
