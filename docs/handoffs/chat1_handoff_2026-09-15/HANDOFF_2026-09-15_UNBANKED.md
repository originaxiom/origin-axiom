# chat1 ("Biri") --- FINAL HANDOFF, 2026-09-15
## Answers to the coordination query, and every result not yet on main.

**SEAT STATUS.** Lane `chat1`. **Branch: NONE — no write access, never pushed.**
**Arc numbers taken: ZERO.** Labels F1–F6 / C1 / LemA / P-SEAM-02 / P-OMEGA-01 are
seat-local and in no repo. **E71 exposure nil.** I do not persist: this seat ends with the
session; only these files carry. **Freeze: complied trivially. No queue — do not wait.**
Repo at time of writing: main B1324 / 1246 arcs; paper-verification at B1410.

--------------------------------------------------------------------------------
# A. THE ONE THAT MATTERS: THE OBJECT WAS WRONG, AND THE RECORD HELD THE RIGHT ONE

**Owner's insight, verified here.** Parity sorts the requirements:
- cohomology dimensions are homeomorphism invariants and `Mbar ≅ M`, so **counts are
  mirror-EVEN** — they survive on any object;
- B1297 T1 banks `I(V*) = -I(V)`, so the **index is mirror-ODD** — on a self-mirror object
  it equals its own negative, hence **ZERO, FORCED**.

> **On `m004`, chirality is a THEOREM-ZERO; the count is merely ABSENT.**
> In a frontier list these look identical. They are different in kind.

**MEASURED (verify/): the three requirements across the class**

| | chiral | `2T` door (surjections to SL(2,F_3)) | order-3 isometries | vol / vol(m004) |
|---|---|---|---|---|
| `m004`  | **no**  | 48  | **0** | 1 |
| `m202`  | **yes** | 96  | **2** | 2 |
| `s958`  | yes | 96  | **0** | 3 |
| **`s959`** | **yes** | **576** | **2** | **3** |
| `m003`  | no  | 48  | 0 | 1 |
| `m009`  | yes | **0** | 0 | — |
| `t12833`| yes | 192 | 0 | 4 |

- `m202` and `s959`: order-3 isometries with **cusp traces `[-1,-1]`, dets `[1,1]`**, so
  `det(A-I) = 2 - tr = 3` **on every cusp** — fc R72's three fixed lines.
- `m009` is chiral but its trace field is `Q(sqrt-7)`; `SL(2,F_q)` is binary polyhedral
  only for `q ∈ {3,5}`. **The door is not automatic.**
- **All of `m004`, `m202`, `s959` have trace field `Q(sqrt-3)`** (shape `x^2-x+1`).
  A cusped manifold with imaginary-quadratic invariant trace field is arithmetic; same
  field ⇒ **COMMENSURABLE**. **The forcing selects the CLASS; the physics lives on a
  member of it.** My earlier "chirality or forcedness" was a **level error**.

**ACTION ITEM (highest value in this document).** **B1330/B1331 ran on `s958`** — the
952-sector scan, the `L_V` computation. `s958` has `Sym = Z/2` and **no order-3 isometry**.
`s959`, same volume, has `D_6` and **two**. One digit apart. This is the same shape as F1,
where the headline scan landed on the *protected* object.

--------------------------------------------------------------------------------
# B. THE RULE IS LOAD-BEARING, TESTED

`a -> a^n b, b -> a` gives `M_n = [[n,1],[1,0]]`, `det -1`; `M_n^2` has word `R^n L^n`.

| n | word | manifold | trace field | `2T` door |
|---|---|---|---|---|
| **1 (gold)** | `RL` | **m004** | **Q(sqrt-3)** | **48** |
| 2 (silver) | `RRLL` | m136 | `Q(i)` | **0** |
| 3 | `RRRLLL` | s464 | deg > 2 | 240 |
| 4 | `RRRRLLLL` | t03910 | deg 4 | **0** |

**Silver fails at the door:** `Q(i)` ramifies at 2, `SL(2,F_2) = S_3` order 6, **not binary
polyhedral**. **The rule selects the arithmetic**, and only the golden one reaches a McKay
partner. The entrance is not decorative.

--------------------------------------------------------------------------------
# C. TWO FACES, TWO DOORS --- and the object stands in both

- **knot face `4_1`**: `Delta(t) = t^2-3t+1`, roots **exactly `phi^2, phi^-2`**;
  `det = |Delta(-1)| = 5` → `F_5` → `SL(2,F_5)` order 120 = **2I** → McKay = **affine E_8**
- **geometric face**: `Q(sqrt-3)` → `F_3` → `SL(2,F_3)` = **2T** → McKay = **affine E_6**
- **bundle face**: `RL` eigenvalues are the **same pair** `phi^2, phi^-2`; `phi ∈ Q(sqrt5)`

B266 banks that `SL(2,F_q)` is binary polyhedral **only** for `q ∈ {3,5}`. **The object
touches both.** The E_8 door sits on a face the programme does not work.
**B727's fence applies at full force: these are faces of ONE ADE list, so this is
structure to explore, NOT corroboration to count.**

--------------------------------------------------------------------------------
# D. VERIFIED COMPUTATIONS NOT ON MAIN
- **`h^1(m004; 27) = 1+1+1 = 3`** — Fox calculus, SnapPy's presentation, 55 dps.
  Control `h^1(Sym^2) = 1` (Thurston deformation) **PASSES**. Third independent derivation
  of B1089's number. *Three bugs caught en route: `rho(relator) = -I` (projective lift),
  rank tolerance below data precision, double-precision collapse at `Sym^16`.*
- **`h^1(3) = h^1(3bar) = 0` on `V_2`** (HMP's non-`sl_2`-factored component), at a point
  verified off the `V_0` intersection, `beta = betabar = 1`, `alpha != alphabar`,
  `h^1(sl_3) = 2` control **PASSES**, trivial-coefficient control `h^1 = 1` **PASSES**.
  **This kills my own `V_1/V_2` chirality story.**
- **`J(m004) = 1` to 15 dp** and `|kappa-2| = 1`; **Callahan Cor 2.4**: m004 is the
  **unique** orientable hyperbolic 3-manifold with Jørgensen number 1.
- **Census depth bias**: `2T`-surjection rate `34.25% → 29.38% → 21.12%` at census depths
  0 / 20k / 80k. B993's `~1 in 3` on 400 manifolds is correct **for the front of the
  census**; the true rate is lower, so the atom is **rarer** and m004 **more**
  distinguished — the bias runs against the programme's own skepticism.
- **Exceptional-filling cut**: 10 slopes → 6 (mirror: `m004(p,1) ≅ m004(-p,1)`, 7/7
  isometric) → **p=0 alone** survives spin (odd framing is non-spin) + index
  (`-sigma/8` must be an integer) + Rochlin. `chi(W_0) = 2`, `b_2 = 1`, boundary is the
  **Sol torus bundle with Anosov monodromy `RL`** — the object's own word. 0-framing is
  the **Seifert** framing: the unique framing needing no choice.
- **B286's slope law verified 8/8 to 1e-16** (`CS(p,-q) = -CS(p,q)`) using the idiom
  *compute CS on the cusped manifold BEFORE filling*. Previously listed as unverifiable.

--------------------------------------------------------------------------------
# E. CORPUS-ABSENT LITERATURE (word-boundary `git grep`, origin/main, `*.md`)
**0 files:** Minsky · Epstein–Penner · Kronheimer · ADHM · Nakajima · quiver variety ·
minimal resolution · exceptional divisor · elliptic surface · Gabriel's theorem ·
cluster algebra · Heegaard Floer · waist size · thin position · Marden · Maskit.
Kodaira: 1 incidental. **Every absent term is 4-dimensional or algebro-geometric; every
well-covered term is 3-dimensional or quantum-topological.** The blind spot has a shape.

**Three theorems the record never cited, all about this exact family:**
- **Jørgensen (1976) / Adams (2002) / Callahan (2009)** — m004 is forced
- **Lackenby (2003)** — `RL` **is** the canonical Epstein–Penner decomposition
- **Minsky (1999)** — punctured-torus groups classified by end invariants; m004's are
  `phi` and `phi'` = the fixed points of `RL`

**Methodological note:** `"Futer"` returned 21 files — **all of them `"refuter"`.**
Word-bound short surnames.

--------------------------------------------------------------------------------
# F. THE ASSEMBLED PICTURE (see `THE_ASSEMBLED_PICTURE.md`)
Chain from the rule to an **anomaly-free rank-4 SM, 45 chiral states**, with
**two** remaining inputs (I originally wrote four; two were mis-marked — see §G):
1. which `A_2^3` of the 40 (fc narrowed to exactly one)
2. **three fixed lines = three `27`s** — the identification

**The second reduces to one precise question:** are the **geometric** `Z/3` (the order-3
isometry of `m202`/`s959`) and the **algebraic** `Z/3` (`2T/Q_8`, verified here: `[2T,2T]`
is `Q_8`, quotient order 3, = the `E_6` grading with `g_0 = A_2^3`) **the same `Z/3`**?
`Out(2T) = Z/2`, so any order-3 automorphism of `2T` is inner — same *type*, sameness
unproved. **This is the B1042 situation, and B1042's standard was an exhibited functorial
chain.**

Also verified: `E_6 = 24 + 27 + 27bar` under the `Z/3`; `3 x 27` anomaly-free
(`sumY`, `sumY^3`, `SU(2)^2U(1)`, `SU(3)^2U(1)` all 0; Witten 18 doublets);
**rank 6 → 4** (unlike B1283's `SO(10)` chain stuck at 5);
`sin^2 theta_W = 3/8` at **1e13 GeV** from one-loop running, nothing fitted.

--------------------------------------------------------------------------------
# G. WITHDRAWN --- carry these, they are mine and they are wrong
- `kappa-2 = omega` as a finding — it is **Riley's parameter**, the trace field restated;
  and the point used was a **knot-group** character while B497's strata are **fibre-side**
  maps. **Category error, withdrawn in full.**
- amphichirality ⟺ Jørgensen saturation — **refuted** (chiral `5_2` below amphichiral `6_3`)
- "the index vanishes because `chi = 0`" — **contradicts my own algebra**; B1329's
  identities leave `I` **free**
- the `V_1/V_2` chirality story — killed by §D's `h^1(3) = h^1(3bar) = 0`
- "chirality or forcedness" — a **level error**; the forcing selects the class
- the "slack table" as Jørgensen numbers — one generating pair, **word-length 0 searched**;
  corrected: `|kappa-2|` is `Aut(F_2)`-invariant, hence a **lower bound** on `J`, and only
  for **2-generator** groups (`m136`, `s958`, `t12833`, `t12835` need 3 — values void there)
- I mis-marked "prime 3 → 2T" and "McKay → E_6" as INPUTS. They are **DERIVED**.
  B727 says that face is **generic, not evidence** — **generic is not underived.**

--------------------------------------------------------------------------------
# H. OPEN QUESTION FOR THE NEXT RUNG (see `QUESTION_R29_character_blindness.md`)
R27 reports a `+1` index on a **nonsemisimple** module whose **semisimplification has index
zero with the same trace on every word**. Elementary counterexample verified here:
twisted cohomology is **not** a character invariant. **Is the index a character invariant
on domain `D`?** If `D` is reductive by construction, every zero ever measured was measured
where the trace instrument is adequate — and the programme's chain is trace-based end to
end. **Gated, not claimed.**

--------------------------------------------------------------------------------
# I. THE PATTERN, STATED FOR THE RECORD
Across this session: **every computation held; every mechanism-claim I layered on top
failed — nine for nine.** Every surviving result came from **reading the record or the
literature**, or from a control breaking my own guess. The division cc proposed —
this seat computes and sweeps, interpretation is gated elsewhere — **is supported by the
measured hit rate**, not by modesty.
