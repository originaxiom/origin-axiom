# THE ASSEMBLED PICTURE --- origin-axiom, chat1 seat, 2026-09-13
## From a two-letter rule to an anomaly-free rank-4 Standard Model, with four named inputs.

**Status of every line below: DERIVED (follows), VERIFIED (computed here, controls passed),
CITED (published theorem, not ours), or INPUT (a choice, named as such).**

--------------------------------------------------------------------------------
# 1. THE CHAIN

| | step | basis |
|---|---|---|
| **DERIVED** | `a -> ab, b -> a` abelianises to `M = [[1,1],[1,0]]`, `det = -1` | `M = R·S` = twist × swap; the swap is the `a<->b` exchange and carries the determinant |
| **DERIVED** | `M^2 = RL`; its mapping torus is `m004` | squaring buys orientability and costs the mirror: `M^2 = X·swap(X)`, so the word **is its own mirror by construction** — 30/30 double ticks amphichiral, 86/100 chiral off the locus |
| **CITED** | `RL` is not a presentation — it is **the canonical decomposition** | Lackenby, *Comment. Math. Helv.* 78 (2003): the Epstein–Penner decomposition of a once-punctured-torus bundle **is** its monodromy triangulation |
| **CITED** | `m004` is **forced** | Callahan, *Conform. Geom. Dyn.* 13 (2009) Cor 2.4, via Adams (2002): **the only orientable hyperbolic 3-manifold with Jørgensen number 1.** Saturates the universal discreteness bound. Verified: J = 1 to 15 dp |
| **CITED** | `phi` is what classifies it | Minsky, *Ann. Math.* 149 (1999): punctured-torus groups are determined by end invariants. `m004`'s are the fixed points of `RL` on the circle: **1.618033988750 and −0.618033988750** |
| **VERIFIED** | trace field `Q(sqrt-3)` | shape min poly `x^2 - x + 1`, disc `-3`; fixes the `PSL(2,O_3)` commensurability class |
| **VERIFIED** | **the physics lives on a chiral member of the same class** | `m202` (vol ×2) and `s959` (vol ×3): same trace field, **chiral**, `D_6`, two order-3 isometries with cusp trace −1 on every cusp |
| **INPUT** | ramified prime 3 → `SL(2,F_3) = 2T` | B727: this face is **generic, not evidence** |
| **INPUT** | McKay(`2T`) = affine `E_6` | one ADE classification seen from four sides |
| **DERIVED** | `Z/3` grading of `E_6` → `A_2^3` = **trinification** | Kac label on the mark-3 node; affine diagram minus `alpha_4` = three `A_2`'s |
| **VERIFIED** | `E_6 = 24 + 27 + 27bar` | `78 - 24 = 54 = 27 + 27`. **`27` and `27bar` sit in SEPARATE grades — this is the chirality.** Order 2 gives `F_4`, all reps self-dual, vector-like; **order 3 is inner, escapes it** |
| **INPUT** | which `A_2^3` of the 40 | fc: exactly one is stable under the founding ratio from both sides |
| **VERIFIED** | `det(A-I) = 2 - tr A = 3` for order 3 | on `m202` and `s959`: cusp traces `[-1,-1]`, dets `[1,1]` → **three fixed lines on every cusp** |
| **INPUT** | three fixed lines = three `27`s | the identification. R15's three-arc hypothesis in another language |
| **VERIFIED** | `3 x 27` is anomaly-free | `sum Y = 0`, `sum Y^3 = 0`, `SU(2)^2 U(1) = 0`, `SU(3)^2 U(1) = 0`, Witten: 18 doublets (even). The non-abelian anomalies cancel **by the cyclic grading**, not by tuning |
| **VERIFIED** | rank 6 → **4** | `SU(2)_R` breaks and one `U(1)` is eaten. **Not stuck at rank 5** like B1283's `SO(10)` chain, where no VEV is charged under the `Z'` |
| **VERIFIED** | `sin^2 theta_W = 3/8` | one-loop SM running from measured inputs reaches **0.37480 at 1e13 GeV**; `a1^-1 = 42.43` vs `a2^-1 = 42.40`. Stech–Tavartkiladze quote `1.3e13`. Nothing fitted |

**Spectrum:** 15 chiral states per `27` (`q, u^c, d^c, l, e^c`) + vector-like exotics.
**× 3 = 45 chiral states.** Standard Model content, exactly.

--------------------------------------------------------------------------------
# 2. THE FOUR INPUTS, AND THEY REDUCE TO THREE QUESTIONS
1. ramified prime 3 → `2T`  ·  2. McKay → `E_6`   — **these two are one question**
3. which `A_2^3` of the 40
4. three fixed lines = three `27`s

--------------------------------------------------------------------------------
# 3. THE CORRECTION THAT MADE THIS ASSEMBLABLE  (owner's, verified here)

**Parity sorts the requirements, and the sorting was measured, not asserted.**
- Cohomology dimensions are homeomorphism invariants and `Mbar ≅ M`, so **counts are
  mirror-EVEN** — they survive on any object.
- B1297 T1 banks `I(V*) = -I(V)`, so the **index is mirror-ODD** — on a self-mirror
  object it equals its own negative, hence **zero, forced**.

> **On `m004`, chirality is a THEOREM-ZERO and the count is merely ABSENT.**
> In a frontier list those look identical. They are different in kind: one can never be
> fixed there, the other was only ever a matter of looking at the right object.

**And the object was in the record.** Measured:

| | chiral | `2T` door | order-3 | vol/vol(m004) |
|---|---|---|---|---|
| `m004` | **no** | 48 | **0** | 1 |
| `m202` | **yes** | 96 | **2** | 2 |
| `s958` | yes | 96 | **0** | 3 |
| **`s959`** | **yes** | **576** | **2** | **3** |
| `m009` | yes | **0** | 0 | — |

`m009` is chiral but its trace field is `Q(sqrt-7)`; `SL(2,F_q)` is binary polyhedral only
for `q ∈ {3,5}`, so **no `2T`, no `E_6`.** The door is not automatic.

**`s958` vs `s959`:** same volume, both chiral. `s958` has `Sym = Z/2` and **no** order-3.
`s959` has `D_6` and **two**. B1330/B1331 — the 952 sectors, the `L_V` computation — ran
on **`s958`.** The neighbour.

**And this dissolves the trade I had stated twice.** `m004`, `m202`, `s959` all have trace
field `Q(sqrt-3)`; a cusped manifold with imaginary-quadratic invariant trace field is
arithmetic; same field ⇒ **commensurable**. **The forcing selects the CLASS. The physics
lives on a member of it.** Nothing downstream of the trace field distinguishes them.

--------------------------------------------------------------------------------
# 4. FALSIFIABLE OUTPUT
- `sin^2 theta_W = 3/8` ⇒ intermediate scale `M_I ~ 1.3e13 GeV`, **no fitting**
- trinification `SU(3)_C x SU(3)_L x SU(3)_R` at `M_I`
- vector-like exotics `D (3,1)_{-1/3}`, `L (1,2)` at the breaking scale
- **a family-non-universal `Z'`** — B1283's fork: `10^2–10^3 TeV` (light family) or
  **a few TeV (third family)**, which is LHC/FCC-testable

--------------------------------------------------------------------------------
# 5. PROVEN NEGATIVES --- stop spending effort here
- values are **moduli**: every input downstream of the object is one
- the sign is **not object-derivable** (B289 finding 4); Lemma A makes it field-theoretic:
  no automorphism of `Q(zeta_12)` inverts `chi` while fixing `Q(sqrt-3)`, because
  `Q(zeta_3) = Q(sqrt-3)`
- `m004`'s contribution to any index theorem is **exactly zero**: `eta = 0` by
  amphichirality, `cs = 1.35e-16`, verified three ways
- **`eta` does not carry the index**: `s958` at `-1/12`, `v2873` at `+1/6` — chiral, live
  boundary term, **index still zero**
- `chi = 0` for **every mapping torus in every dimension**; `M x S^1` inherits it
- chirality cannot come from `m004`: `Sym(m004) = D_4`, orders `{1,2,4}`, **no order 3**

--------------------------------------------------------------------------------
# 6. WITHDRAWN TONIGHT (mine, all of it)
- `kappa - 2 = omega` as a finding — it is Riley's parameter, i.e. the trace field restated;
  and the point used was a **knot-group** character, while the strata are **fibre-side**
  maps. Category error, withdrawn in full
- amphichirality ⟺ Jørgensen saturation — **refuted** (chiral `5_2` below amphichiral `6_3`)
- "the index vanishes because `chi = 0`" — **contradicts my own algebra**, which says the
  identities leave `I` free
- the `V_1/V_2` chirality story — **h¹(3) = h¹(3bar) = 0** at a verified point on `V_2`,
  off the `V_0` intersection, trivial-coefficient control passing
- "chirality or forcedness" — a **level error**; the forcing selects the class
- the "slack table" as Jørgensen numbers — one generating pair, word-length 0 searched

--------------------------------------------------------------------------------
# 7. WHAT REMAINS
1. the three questions of §2
2. the spectrum is two measured properties (chirality, count), **not yet a derivation**
   that they assemble
3. `E_6` remains generic (B727 stands)
4. mark the frontier: **open** vs **proven-negative**. §5 is currently filed as §7.
