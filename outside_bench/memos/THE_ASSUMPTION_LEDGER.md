# THE ASSUMPTION LEDGER — the far bank decomposed, and the one condition we can compute fails on the object

*Outside bench, memo 235, 2026-09-18. Seal `seals/THE_ASSUMPTION_LEDGER_PREREG.md`
(sha256 `3fd9117e0da47d50c0cda3db9ff420d60c0625c53d2e8e314a30ca8a8d519fd0`, committed `e657e0d8`
**before** the certificate). Certificate `certificates/the_assumption_ledger.py`, output
`outputs/the_assumption_ledger_out.txt`, **exit 0, four controls PASS**. Every number from that
certificate (#20).*

---

## 0. THE ARTIFACT THAT NEARLY SHIPPED AS THE HEADLINE

**The first run returned OUTCOME A** — A4 failing for m004 but **holding for v2873 (b₁ = 2) and
t12835 (b₁ = 3)**, an earned redirect to two of B1330's best-case objects. It would have been the
best result of the session.

**It was an artifact.** The run tested only the **cusp count** before applying the `(1,0)` filling.
B1273's construction is the 3-fold **cyclic branched cover of S³ along the knot**, obtained by
filling the **lifted meridian** — and that requires a **knot complement in S³, i.e. `H₁ = ℤ`
exactly**. Of the seven candidates **only m004 qualifies**; the rest carry torsion or extra rank, so
a cover still exists but the ambient is not S³ and `(1,0)` is **not canonically the meridian**. The
filling was a *choice*, not the construction.

**What exposed it:** t12833's filled volume came back **negative, −1.370e−05** — the numerical
signature of a degenerate filling. The frame test now sits in the certificate **with this history in
the source**, not silently corrected.

---

## 1. THE DECOMPOSITION

The assumed package — G₂-MSSM §I.B + `THE_DESTINATION_LEDGER` item 1 + B1355:

> *a compact G₂ manifold **X** containing an observable three-manifold **Q** carrying an E₆
> singularity, with **isolated conical points on Q at which chiral matter is supported**, three of
> them permuted by ℤ/3.*

| # | atomic condition | on | tag | status |
|---|---|---|---|---|
| A1 | Q admits the E₆ (2T) normal structure | Q | COMPUTABLE | the record has it |
| A2 | chirality needs the ADE locus through **isolated non-orbifold conical points** | X | LITERATURE | Witten; Acharya–Witten; Acharya–Gukov |
| A3 | the flat/orbifold class cannot supply A2 | X | SETTLED | B1259, B1353 |
| **A4** | **Joyce–Karigiannis needs `b₁(Q) > 0`** | Q | **COMPUTABLE** | **computed below** |
| A5 | TCS is non-chiral | X | LITERATURE | BCHS 2019 |
| **A6** | sum rule: `b₂(X) ≥ 2` with the ℤ/3 moving harmonic forms | **X** | ~~GENUINELY OPEN~~ **SUPERSEDED — see ADDENDUM 1** | ~~not computable — X is not constructed~~ **WRONG: B1357 computed it; it FAILS in the flat class** |
| A7 | the permuting ℤ/3 is the object's own, 2T/Q₈ | Q | SETTLED HERE | memo 233 v2 |
| A8 | the ℤ/3's fixed-point structure on Q | Q | COMPUTABLE | reported, not assumed |
| A9 | on a **closed** Q, H¹-based net chirality vanishes ⟹ chirality can come **only** from A2's points | Q | SETTLED | B1260, B1267, B1351 |

**A6 is the honest residue.** It is the condition that would decide the matter, and it lives on an
object nobody has built. The ledger's value depends on that tag staying honest.

> **SUPERSEDED BY ADDENDUM 1 (2026-09-18).** The tag was wrong and the paragraph above is left in
> place as the error. **The object had already been built and A6 already computed on it** —
> `frontier/B1357_the_objects_own_joyce_orbifold`. A6's first clause is **satisfied** (`b₂ = 2`
> after resolution) and its second clause **fails** (the deck acts trivially on both added 2-forms).
> See ADDENDUM 1.

---

## 2. THE RESULT — **OUTCOME B**

| candidate | why in the set | frame | A4 |
|---|---|---|---|
| **m004** | the object | **REACHED** | **FAILS** — Y₃ has `H₁ = ℤ/4 ⊕ ℤ/4`, **`b₁ = 0`**, vol 2.93e−12 (flat) |
| m003 | the sister | does not reach | `H₁ = ℤ/5 ⊕ ℤ` |
| **m202, s959** | **cell 8's 4/4 witnesses** | does not reach | `ℤ⊕ℤ` · `ℤ/3⊕ℤ⊕ℤ` |
| **v2873, t12833, t12835** | **B1330's best-case set** | does not reach | `ℤ/6 ⊕ ℤ` each |

**Frame reaches 1 of 7. A4 holds for none.**

---

## 3. THE PART THAT IS ACTUALLY USEFUL, AND IT IS NOT THE FAILURE

The redirect discussion — *"use m202 or s959 instead, they score 4/4"* — has never priced this:

> **Cell 8's witnesses and B1330's best-case set are NOT knot complements in S³. So B1273's closing
> construction — the record's own route to a compact carrier — DOES NOT TRANSFER TO THEM.**

Redirecting to those objects does not merely trade predicates. **It costs the closing construction.**
That price was invisible until the frame condition was written down, and it belongs in any future
comparison of m004 against its alternatives.

---

## 4. CONTROLS — four, all PASS

| # | control | what it did |
|---|---|---|
| **K1** | `b₁(Y₃) = 0` reproduced on the rebuilt environment, matching the three banked routes (Smith form on F(2,6); the Alexander module; SnapPy's filled cover) | `H₁ = ℤ/4 ⊕ ℤ/4`, vol 2.93e−12 |
| **K2** | the routine **returns `b₁ > 0`** on m003 (1), m125 (2), m129 (2) | memo 164 — it can distinguish |
| **K3** | #38 discipline on every condition | applied |
| **K4** | population printed before any verdict, seven candidates named individually | the B1197 vacuity trap |

*Environment note: the container was recycled mid-session — repo, PDFs, SnapPy and sympy all gone.
Everything had been pushed and `git ls-remote` confirmed the exact tip, so nothing was lost; rebuilt
by re-clone plus SnapPy 3.3.2 / sympy 1.14.0. **K1 exists to catch precisely a drifted rebuild.***

---

## 5. THE FENCE — stated in the seal before the run, and it governs every line above

**A failed necessary condition closes the route FOR THAT OBJECT, never the route itself.**
`b₁(Q) = 0` says **Joyce–Karigiannis cannot resolve that locus**. It says nothing about whether some
other construction can, and **nothing about the G₂ route as such**. Any sentence of the form *"the G₂
route is closed"* is forbidden output of this cell.

**I-26 UNEARNED** — no generation count is licensed. **X is not constructed** — every statement here
is a condition *on* a closing, never a property *of* one. No value.

**Gate 5 untouched. Nothing promotes to `CLAIMS.md`.**

---

## ADDENDUM 1 (2026-09-18) — **A6 WAS MIS-TAGGED. IT IS COMPUTED, AND IN THE FLAT CLASS IT FAILS.**

**Occasioned by the owner:** *"A6 — the sum rule's b₂(X) ≥ 2 — is the condition that would decide the
matter, and it is not computable: it lives on an object nobody has built. — lets build it, lets not
be discouraged before we even understand it properly."*

**The push was right and §1's tag was wrong.** Before building anything, the record was checked — the
standing rule — and the record had **already built the object and already computed A6 on it**.

### 1. What the record has: `frontier/B1357_the_objects_own_joyce_orbifold`

Present on the SM head only; **absent from `main` and absent from this branch** (relay item, §5).
It compactifies the E₆ fibre ℂ²/2T by the **Hurwitz torus** and lets the Hantzsche–Wendt holonomy act
as the SO(4) ⊂ G₂ of B1356, giving a **compact flat G₂ orbifold** `(T³ × ℍ/Λ)/(Π ⋉ 2T)` with **exactly
one invariant spinor (N = 1)** and four disjoint singular loci — E₆ on Y₃ (the object's own closing,
B1273), SO(8) on a second copy of Y₃, SU(2) on a third, SU(3) on T³.

**It states A6 in this bench's own words and decides it.** Verbatim, from its FINDINGS (every
quotation below checked against the file before this addendum was written, #26):

> *"b₂ = 0: the flat background carries no C-field U(1) at all."*

> *"The question hint 16 left (**a b₂ ≥ 2 with the deck acting irreducibly**) is decided in the flat
> class: the irreducible occurs only on 3-forms; the U(1)² that tells the three generations apart can
> only come with the apexes themselves."*

> *"(ℝ³)^{V₄} = 0, so the E₆, SO(8) and SU(2) loci are rigid — no Joyce resolution and no deformation
> … (ℝ³)^{1} = ℝ³ on the T³ locus, resolvable, adding 2 to b₂ (A₂ ⊗ H⁰) and 6 to b₃ (A₂ ⊗ H¹(T³)).
> After that resolution: cover b₂ = 2, b₃ = 10; descent … b₂ = 2, b₃ = 4. The deck acts trivially on
> the two added 2-forms … **So the deck's irreducible occurs on four of the cover's ten 3-forms and
> on no 2-form**: the flat background and its resolution contain no C-field U(1) that tells the three
> generations apart."*

### 2. A6, retagged — **the first clause is satisfied, the second fails**

| clause of A6 | flat background | after Joyce resolution of the T³ locus | verdict |
|---|---|---|---|
| `b₂(X) ≥ 2` | `b₂ = 0` — fails | **`b₂ = 2`** (cover **and** descent) | **SATISFIED** |
| the ℤ/3 **moves** the harmonic 2-forms | vacuous | deck acts **trivially** on both added 2-forms | **FAILS** |

**That is exactly memo 233's no-inflow case.** *(The "neither cites the other" clause below is
withdrawn in ADDENDUM 2 §2: independent at derivation, but main's B1414 harvested memo 233 and
sm:B1356's currency note cites B1414.)* Memo 233 derived, from the B1355 charge sum rule plus
the representation theory of ℤ/3 on ℝ^{b₂}, that a ℤ/3 which **permutes the apexes and fixes `w`**
gives equal charges, hence `3q = 0`, hence `q = 0` and **no inflow** — and that escape requires
`b₂ ≥ 2` **with the ℤ/3 moving the harmonic forms**. B1357 computed, on the object's own compact flat
orbifold, that the deck acts **trivially on H²**. **Same condition, two independent routes, and
neither cites the other** — B1357 is on the SM head, memo 233 is this bench's. Recording the
convergence is the point; it is not a second result.

### 3. Where A6 is actually open, and why the curved case is where it can be met

B1357 does not end in a wall. It ends in a **location**:

> *"The generation-distinguishing U(1)² (the sum-zero pair on which the deck acts as rotation) is not
> in the flat background, not in its resolution, and not in the descent: **it must be born with the
> curved apexes** — the local b₂(link) = 1 class at each cone over CP³/2T (B1355), extended over the
> closing in the sum-zero combinations. Every other C-field U(1) the record could offer is
> deck-invariant and sees no generation."*

And the reason that route can supply what the flat class provably cannot is **elementary, and it is
B1356's and B1357's, not this bench's** — reproduced in `certificates/the_a6_retag.py` only so that
memo 233's derived condition and B1357's computed one are *checked* to be the same statement:

**Three apexes permuted freely by ℤ/3 carry the permutation representation of ℤ/3 on ℝ³.** Its
character is `χ = (3, 0, 0)`; the multiplicity of the trivial representation is `⟨χ, 1⟩ = 1`; the
remaining **sum-zero** subspace has dimension **2** and **is** the two-dimensional irreducible, on
which the deck acts by rotation. So a **free** 3-orbit of apexes supplies the deck-moved `H²` classes
**by construction** — not by luck, but *because the three apexes form a free ℤ/3-orbit.*

**Control that can fail (memo 164):** a ℤ/3 acting **trivially** on three points (three fixed orbits
of size 1) must come back as `3 × trivial`, character `(3, 3, 3)`, **irrep dimension 0**. It does.
Both controls PASS; `certificates/the_a6_retag.py` exits 0.

### 4. **A6's honest status**

> **PARTLY SUPERSEDED BY ADDENDUM 2 §3 (same session).** *"reduced to compactness alone"* is
> **WITHDRAWN**: the three-apex design carries computed negatives independent of compactness
> (sm:B1361, sm:B1365 — *"excluded as it stands"*). The retag itself stands.

> **COMPUTED AND FAILING** in the flat class and its Joyce resolution (B1357, stage 7).
> **OPEN** in the curved class, with the mechanism named and the obstruction reduced to
> **compactness alone**.

**WHAT HAS NOT CHANGED, and this governs every sentence above:** *the compact curved closing is still
not built.* B1357's own closing sentence puts the U(1)² at the apexes of a closing nobody has
constructed. **Any sentence of the form "the bridge is open" is forbidden output of this addendum.**
What changed is that A6 moved from *"not computable"* to *"computed where it can be, failing there,
and reduced to compactness alone in the curved case"* — **a sharper statement, not a solved problem.**

**No priority is claimed.** The construction, the computation, and the sum-zero observation are
B1356's and B1357's. **I-26 remains UNEARNED. No value. Gate 5 untouched.**

### 5. **BENCH ERROR #38, third instance — filed at the point of occurrence**

§1 tagged A6 *"not computable — X is not constructed"* **without checking the record**. The record had
the object. That is the #38 class exactly: *"the record states X" ≠ "the record claims X as its own"*,
here in its other direction — **"I cannot compute X" asserted without asking whether the record
already had.** Third instance.

**The mitigating fact, stated plainly rather than as an excuse:** the standing rule — *exhaust the
repo before saying we don't have X, before building, before ranking a gap* — **caught it before
anything was built**. The owner's push was what invoked the rule; the rule then did its work in one
step. That is the discipline working, not failing. The tag stood for the length of one memo and is
corrected in the memo, the INDEX row and the register together — a correction that lives in one place
is not a correction.

### 6. **RELAY — `main` does not have B1357**

`frontier/B1357_the_objects_own_joyce_orbifold` is on the **standard-model head only** (4 files);
`main` has 0 files of it, and so does this branch. **It decides a condition this bench had been
carrying as open, and it is the only place in the record where the object's own compact G₂ orbifold
exists.** Main needs it. This joins the standing relay items: `LITERATURE_SWEEP_2026-09-06` is
SM-head-only, and B1273 / B1271 / B1353 / B1355 are 0 files on main.

### 7. **THE OPEN CLAIM, CHECKED ON ITS OWN TERMS (memo 153), AND WHAT THE CHECK TURNED UP**

> **ITS RELAY IS VOID — SEE ADDENDUM 2 §1 (same session).** `main` harvested all ten arcs on
> **2026-09-16** as `B1415`, which was in this working tree while §7 was being written. The
> all-heads diff counts **directory names**, and main harvests under its **own** arc numbers.

The one OPEN claim this addendum makes — *the compact curved closing is not built* — was run through
`scripts/checks/already_banked.py --wide` before it was written. **Searched terms, stated with the
claim:** `compact curved G2 closing apexes constructed`; `b2 deck irreducible 2-form generation
U(1)`. Nothing in this branch's corpus builds it; the settled hits are B1259 (no flat G₂ orbifold can
supply Acharya–Witten isolation) and B1084's census, both of which the ledger already carries.

**But the instrument searched THIS BRANCH's corpus, and the material lives on a head this branch does
not have.** Diffing the heads directly (#34) shows the SM head carries **ten arcs B1350–B1359** of
which **`main` has ZERO FILES**, and two of them go past B1357 on exactly this question:

- **B1358 — THE E₆ APEX FAMILY.** The curved apexes are now a *census*, not a single example: the
  twistor cones of S⁴/(2T × Γ_R), with *"b₂(CP³/Γ; ℚ) = 1 throughout"*, only Γ_R = 1 (B1355's cone)
  having a companion the object's own background supplies, and inflow coefficients at the apex in the
  exact ratio **12 : 1**. Its §5 states the assembled picture: *"the three 27s told apart by the
  apexes' own U(1)s in sum-zero combination (B1356)"* — **the same sum-zero mechanism this addendum
  reproduces in §3**, now carried through a family rather than one cone. It also closes a door:
  *"What is excluded: the apex on the knot (A₅) …"*.
- **B1359 — THE K3 ALTERNATIVE, DECIDED.** *"a K3-fibred background cannot supply the SU(2) companion
  of B1355's apex: among the fibre compactifications of the E₆ singularity in the record, the
  three-generation design of B1356–B1358 lives on the Hurwitz torus and nowhere else"*. That does not
  build the compact closing — it **pins the ambient**, which makes the residue narrower, not smaller.

**The distinction that must not be lost, and it is the one this bench got wrong once already (R147):**
`b₂(link) = 1` is the **local** class at an apex. **A6's `b₂` is the COMPACT X's.** B1358 supplies the
local data across a family; **no arc extends it over a compact closing, because no compact curved
closing exists.** §4's status is therefore unchanged by B1358 and B1359 — they sharpen the *mechanism*
and the *ambient*, and leave **compactness** exactly where it was.

**Instrument note, and it is a finding about the instrument:** `already_banked.py` reads the corpus
**at the checkout**, so on this branch it is structurally blind to B1350–B1359. A memo-153 clean run
is therefore **not** sufficient when the question touches the G₂ lane; the all-heads diff (#34) has to
run beside it. That is now two instruments for one rule.

**Relay, extended:** `main` is missing **all ten** of B1350–B1359, not only B1357. And
`docs/SEAT_REGISTER.md` — **on `main` and on this branch; the SM head does not carry that file at
all** — records the SM seat's last arc as **B1355**, while that head carries **B1359**. The coupon
register is four arcs stale on the lane that holds the object's own compact G₂ orbifold, which is
also why the SM head's arcs keep arriving here as surprises.

---

## ADDENDUM 2 (2026-09-18) — **ADDENDUM 1's RELAY IS VOID AND ITS A6 STATUS WAS TOO GENEROUS. MAIN HARVESTED ALL TEN ARCS TWO DAYS AGO, AND THE CURVED DESIGN CARRIES COMPUTED NEGATIVES.**

Written the same session as ADDENDUM 1, against it.

### 1. The relay is void — **`main` has the content; it does not have the directory names**

ADDENDUM 1 §7 said *"`main` has 0 files of B1350–B1359 … Main needs it."* The file count is true and
**the inference from it is false.** `frontier/B1415_the_sm_seats_closing_arcs_harvested` — **on `main`
and sitting in this working tree the whole time** — is dated **2026-09-16** and reads:

> *"THE SM SEAT'S CLOSING ARCS HARVESTED (sm:B1356–B1365, THE CLOSING, sm:L214/L215): **ten scripts
> re-run green and log-identical**, the load-bearing numbers recomputed on main's own code … **Verdict:
> VERIFIED** (ten arcs: the seat's grades stand; nothing raised, nothing lowered without a computation)"*

Every arc ADDENDUM 1 relayed is there with its own recomputation, including sm:B1357 (*"the T⁴/2T orbit
census reproduced by the same Burnside machinery"*), sm:B1358 (*"VERIFIED (companions); the mixed-loci
typing REGISTERED as argued"*) and sm:B1359 (*"`burnside_k3.py` … exactly the two solutions, both of
rank 19"*). Main also logged the **bookkeeping back to the seat** — including that sm:B1358's mixed-loci
typing and sm:B1360's `b₂(link) = 1` are **argued, not computed**.

**The instrument lesson, and it is a sharpening of #34 rather than a repeat of it.** The all-heads diff
I built counts **directory names**. Main **harvests content under its own arc numbers** — `B1416`
states it outright: *"eleven were already on main under other arc numbers"*. So:

> **#34, sharpened (#39): A DIRECTORY-NAME DIFF MEASURES NAMES, NOT CONTENT. Before relaying "main does
> not have X", grep main for X's OWN LOAD-BEARING STRINGS, not for X's arc number.**

**BENCH ERROR, fourth instance of the class.** ADDENDUM 1 §7 presented the diff as the repair for
`already_banked.py`'s blindness — and the diff had the same blindness in a different coordinate.

### 2. The independence claim, corrected

ADDENDUM 1 §2 said memo 233 and B1357 are *"two independent routes, neither citing the other."*
**Independent at derivation: yes** — and that is the part worth keeping. **"Neither cites the other":
no longer true.** `frontier/B1414_the_outside_benchs_memos_185_233_harvested` (main, 2026-09-16)
harvested memo 233 — *"memo 233's forced escape clause re-derived and its v1 vacuity confirmed"*,
graded **REPRODUCED** — and sm:B1356's currency note **cites B1414 by name**. The convergence stands;
the "neither cites" clause does not, and is withdrawn.

*(Recorded because it is a check on this bench and not a compliment: main's re-run of
`the_two_threes_v2.py` reports six of seven controls PASS, with **V-CROSS failing on the bench's volume
tolerance only** — the (1,0)-filled 3-cover prints 1e−6 at working precision while H₁ = ℤ/4 ⊕ ℤ/4
matches; main's own check passes at 1e−4.)*

### 3. **A6's status, corrected in the direction that costs us something**

ADDENDUM 1 §4 said the curved class is *"OPEN … with the obstruction reduced to compactness alone."*
**That last word is wrong, and the guard in this cell's own plan named exactly this failure mode.**
The three-apex curved design is not merely unbuilt. **It already carries computed negatives that have
nothing to do with compactness**, each at the strength its arc gives it:

| arc | grade | what it computes about the three-apex design |
|---|---|---|
| **sm:B1361** THE DECK'S TEXTURE | **NEGATIVE** | under the two apex U(1)s the only invariant E₆ cubic is `27₁27₂27₃`, so Higgs in the apex 27s makes **every tree-level charged-fermion mass matrix complex symmetric with zero diagonal**, forcing `σ₁ = σ₂ + σ₃` exactly — **refuted in every charged sector**. Main recomputed it: `σ₁ − σ₂ − σ₃ = 0 to 2e−15` over 2 000 random hollow complex symmetric 3 × 3 |
| **sm:B1362** | PROVED | the deck-symmetric Yukawa is `circ(x, y, y)`, eigenvalues `x + 2y, x − y, x − y` — **the deck must be broken** to get a hierarchy |
| **sm:B1365** THE BULK OF THE LINE | NEGATIVE | both E₆-charged SM singlets carry `γ = −5/3`, so `U(1)_η` is exact above the soft scale, **the Majorana mass is forbidden**, and the neutrinos are **Dirac at the up-quark masses**: *"**the three-apex design is excluded as it stands**"* |

Main's own summary of the status, which this bench adopts verbatim rather than restating in its own
words: *"The design's status is the seat's own: **a DESIGN with a computed obstruction (no seesaw) — no
theorem, no prediction**"*, the exclusion *"recorded at its stated strength, **conditional on a cited
coupling**"*, with a registered remedy (**a 27̄ sector**, sm:L215 = main's **L221**).

**So A6, finally:**

> **FLAT CLASS + JOYCE RESOLUTION — COMPUTED AND FAILING** (ADDENDUM 1 §2; unchanged).
> **CURVED CLASS — the mechanism is named (the free ℤ/3-orbit's sum-zero irreducible) and the
> compact closing is unbuilt, AND the design that mechanism belongs to is ALREADY EXCLUDED AS IT
> STANDS on independent grounds (no seesaw), conditional on a cited coupling, with its remedy
> registered and not yet run.**

**A6 is therefore not the last obstruction and never was.** ADDENDUM 1's *"reduced to compactness
alone"* is withdrawn. What survives ADDENDUM 1 unchanged: the retag itself (A6 is **computed**, not
uncomputable), the flat-class failure, the convergence with memo 233, the free-orbit mechanism and its
control. **I-26 UNEARNED. No value. Gate 5 untouched.**
