# Memo 206 — L78 ANSWERED, AND THE ROUTE COULD NEVER HAVE FAILED: who can hear chirality at level 2

**Seal:** `outside_bench/seals/L78_ROUTE_A_PREREG.md`, sha256
`bff5ed36d85880c5a667c54086aa28f88d0fd182f8ef2a9e517c59a2bf355edf`, committed and
pushed before any computation.
**Certificate:** `outside_bench/certificates/l78_route_a.py` ·
**Output:** `outside_bench/outputs/l78_route_a.txt`
**Outcomes: CELL 1 = A · CELL 2 = A · CELL 3 = A.** Controls C1–C4 all pass.

---

## 0. Why this was run, and what was already there

`docs/OPEN_LEADS.md` carries **L78 — the level-2 filling span (Route A)** as
**"OPEN — Round 2 first," ★★★★**, with the two outcomes *"rank > θ-even dim ⇒ the
θ-odd state amplitude (Q3's missing fact) becomes computable; rank pinned ⇒ a SECOND
structural-unhearability theorem. Either banks."*

**It is not open.** `frontier/B583_chiral_content/FINDINGS.md` §X3, dated 2026-07-14 —
the same day L78 was registered — states: *"Level 2: rank exactly 6 = dim(θ-even) over
719 slopes (θ-odd projection 4e-13); the level-1 control reproduced Q1's rank 2 exactly.
… **L78 resolves:** the θ-odd amplitude is NOT reachable by Route A."*

What was missing is the reason this memo exists: **that level-2 number has no lock and
no code.** The arc directory `frontier/B583_chiral_content/` contains `FINDINGS.md`,
`READING_RAW.md`, `arc_verdict.json` and `x2r_recompute.py` — nothing that computes X3 —
and the arc's lock `tests/test_b583_content.py` tests the mechanism **at level 1 only**,
in a 3×3 theater. The nine-primary claim has stood in prose for two months.

This memo reproduces it from the Cartan matrix, and then computes the thing X3's own
conclusion names and does not perform.

---

## 1. The stage, rebuilt here

W(E₆) by BFS over the six simple reflections: **51840 elements, exact**. The level-k
integrable weights by enumerating the marks (1,2,2,3,2,1): **3 at level 1, 9 at level 2.**
Kac–Peterson `S` by the Weyl sum at k+h^∨ = 14, computed in **integer arithmetic mod
9·(k+h^∨)** and read off a root-of-unity table — no floating-point exponent is ever
formed from a large argument. `T` from h(λ) = (λ,λ+2ρ)/28 with c = 78/7.

**The stage's own gates, all before any cell (control C2):**

| gate | level 1 | level 2 |
|---|---|---|
| \|W(E₆)\| | 51840 exact | 51840 exact |
| `S` symmetric | 1.3e−14 | 6.9e−15 |
| `S` unitary | 2.1e−14 | 5.7e−15 |
| `S²` a 0/1 permutation | 2.2e−14, **True** | 4.2e−15, **True** |
| `(ST)³ = S²` | 2.7e−14 | 7.2e−15 |
| Verlinde coefficients integral | 3.1e−14 | 2.0e−14 |
| Verlinde coefficients ≥ 0 | yes | yes |
| min quantum dimension | 1.000000 | 1.000000 |

Two independent corroborations the seal did not ask for and that the stage passes anyway:

- **h(27) at level 1 = 0.666667 = 2/3**, the value B569 *proved* from the root system
  when it corrected the incoming handoff's inconsistent data; **h(78) at level 2 =
  0.857143 = 6/7 = h^∨/(k+h^∨)**, the adjoint's forced value.
- **`C := S²` IS the E₆ diagram flip.** The nine primaries' classical dimensions by
  Weyl's formula over the 36 positive roots (also computed here) are
  1, 27, 351, 351, 78, 27, 351, 650, 351; `C` as a permutation is
  `[0,5,3,2,4,1,8,7,6]`, and the diagram flip (1↔6, 3↔5) on the Dynkin labels is
  **the same permutation, asserted as a gate**. So 27↔27̄, 351↔3̄5̄1̄, 351′↔3̄5̄1̄′, with
  **1, 78 and 650 self-conjugate**.

The `C`-eigenspace split, computed: **level 1 → θ-even 2, θ-odd 1; level 2 → θ-even 6,
θ-odd 3.**

---

## 2. CELL 1 — the number reproduces. OUTCOME A.

Vacuum-seeded filling covectors `e₀ · ρ(g_{p,q})`, `g_{p,q} ∈ SL(2,ℤ)` built by
continued fraction with the 2×2 first column asserted equal to (p,q) for every slope.

| level | Q | slopes | rank | dim(θ-even) | max \|θ-odd projection\| |
|---|---|---|---|---|---|
| 1 | 5 | 39 | **2** | 2 | 3.18e−14 |
| 1 | 15 | 287 | **2** | 2 | 9.93e−14 |
| 1 | 30 | 1111 | **2** | 2 | 2.10e−13 |
| 2 | 5 | 39 | **6** | 6 | 2.26e−15 |
| 2 | 15 | 287 | **6** | 6 | 1.08e−14 |
| 2 | 30 | **1111** | **6** | 6 | **2.14e−14** |

**B583 X3's level-2 rank 6 reproduces**, on a different and larger slope set (1111 vs
its 719), with the θ-odd projection an order of magnitude tighter than its 4e−13. The
**level-1 control (C1) returns rank 2**, B580 Q1's banked number. **Control C4** — the
rank is identical at 39, 287 and 1111 slopes, so it is not a sampling artifact.

---

## 3. CELL 2 — Route A's positive outcome was never available. OUTCOME A.

| identity | level 1 | level 2 |
|---|---|---|
| `e₀C = e₀` (the vacuum is C-fixed) | 2.24e−14 | 3.04e−15 |
| `[C,S] = 0` | 1.24e−16 | 1.68e−16 |
| `[C,T] = 0` | 2.96e−14 | 6.63e−15 |
| worst `\|vC − v\|` over the sweep | 8.33e−14 | 8.27e−15 |

`C` is central in the image of SL(2,ℤ) and fixes the vacuum covector. Therefore for
**every** word `g`, `(e₀ρ(g))C = e₀Cρ(g) = e₀ρ(g)` — every vacuum-seeded filling
covector is C-fixed, hence θ-even, **whatever the slope set is.**

> **INTERPRETIVE.** L78's outcomes were *"rank > θ-even dim"* versus *"rank pinned."*
> The first is excluded by three lines of algebra that hold in any modular tensor
> category, since `C = S²` is always central and always fixes the vacuum. **A lead
> graded ★★★★ and carried as OPEN for eight weeks had only one available outcome the
> whole time** — MB12's requirement that a preregistered test be able to both pass and
> fail was not met by L78 as written. The genuine two-outcome question inside it is the
> one CELL 1 answers: whether the rank *saturates* the θ-even subspace (6) or falls
> short of it. It saturates.

---

## 4. CELL 3 — who *can* hear it. OUTCOME A. (New.)

B583 X3's conclusion is *"the state's chiral content requires **non-vacuum observer
states**."* It did not say which, or how much. Computed here at level 2 over 1111
slopes, with the θ-odd reach = the rank of the projection of span{seed·ρ(g_{p,q})} onto
the θ-odd 3-space:

| seed | self-conjugate? | span rank | **θ-odd reach** | max \|θ-odd proj\| |
|---|---|---|---|---|
| `1` [000000] | **yes** | 6 | **0** | 2.14e−14 |
| `78` [010000] | **yes** | 6 | **0** | 1.85e−14 |
| `650` [100001] | **yes** | 6 | **0** | 2.17e−14 |
| `27` [000001] | no | **9** | **3** | 0.6870 |
| `27` [100000] | no | **9** | **3** | 0.6870 |
| `351` [000010] | no | **9** | **3** | 0.6870 |
| `351` [001000] | no | **9** | **3** | 0.6870 |
| `351` [000002] | no | **9** | **3** | 0.6870 |
| `351` [200000] | no | **9** | **3** | 0.6870 |

> **THE REACH LAW (computed, not cited): a primary observer hears chirality if and only
> if it is not self-conjugate — and every one that hears it hears ALL of it.**
> Reach 0 for exactly the three `C`-fixed primaries {1, 78, 650}; reach 3 of 3, the
> whole θ-odd space, for each of the six that sit in a `C`-pair. There is no partial
> hearing anywhere in the theater.

And the pure chiral seeds, `(e_i − e_{C(i)})/√2`, one per pair:

| seed | span rank | θ-odd reach | max \|proj\| |
|---|---|---|---|
| `27` − `27̄` | **3** | **3** | 0.9716 |
| `351` − `3̄5̄1̄` | **3** | **3** | 0.9716 |
| `351′` − `3̄5̄1̄′` | **3** | **3** | 0.9716 |

Span rank **3**, not 9: a `C`-antisymmetric seed's filling span is **entirely inside the
θ-odd 3-space**, and this is exact, not approximate. Over all three pairs jointly:
joint reach **3 of 3**, three equal singular values **47.138095**, and

> Frobenius² of the full span = **6666.000000** · captured by θ-odd = **6666.000000** ·
> predicted if the span were entirely θ-odd = 2 × 3 pairs × 1111 slopes = **6666.000000**
> · **leakage into θ-even = −9.1e−13.**

This is the exact mirror of CELL 2: `e_i − e_{C(i)}` is C-*anti*fixed, `C` is central, so
every covector it generates is C-antifixed — θ-odd, with nothing left over.

**Control C3 (MB12 transversality, run before any cell was read).** Seeds placed inside
the θ-odd 3-space return span rank 3 and θ-odd reach 3 with max\|proj\| = 1.000 — the
instrument **can** report a non-zero, so a reported zero is a fact about the seed and
not about the instrument (memo 164: control passing is not instrument working; this
control tests working).

---

## 5. What this settles, and what it does not

**Settled.**

- L78 is **RESOLVED**, and was resolved on the day it was registered. Its row in
  `docs/OPEN_LEADS.md` is **stale**. Its level-2 number now has an independent
  reproduction and a certificate; it previously had neither.
- The second structural-unhearability theorem is **confirmed at level 2 and explained**:
  not a coincidence of ranks but the centrality of `C = S²` plus the vacuum being
  `C`-fixed.
- The theater is **not** the obstruction. The θ-odd sector is fully reachable — by
  anything not self-conjugate. **The vacuum is the obstruction, and only the vacuum.**

**Not settled, and not claimed.** This memo computes **reachability**, not a value.
Knowing that a `27`-seeded observer reaches the whole θ-odd 3-space does not compute the
object's θ-odd amplitude — B580's Q3 asked for the amplitude of a **specific state**,
and this bench has not computed that state. What CELL 3 removes is the belief that no
observer could carry the information; what it does not supply is the number.

> **INTERPRETIVE.** `WHAT_WOULD_COUNT.md` §4A.1's one open item is *"chirality without an
> inserted closing."* Nothing here closes it. What this does is locate the wall
> precisely: the corpus's chirality-at-count results (B1086's h¹ equality, B1087's charge
> complementarity) are statements about **vacuum-based** observation, and the reach law
> says a non-self-conjugate observer is not subject to that constraint. Whether an
> observer in a `27` is a **legitimate** object of the theory — rather than an extra
> datum inserted by hand — is exactly the "inserted closing" question, and this memo
> does not answer it. It says only that if such an observer is legitimate, it hears
> everything.

---

## 6. Corrections filed at the point of occurrence

**BENCH ERROR #25.** In the previous turn's status answer I named L78 as *"the highest-graded
still-open lead"* and the first rung to climb. It was resolved in `B583/FINDINGS.md`
eight weeks earlier, in a file that says *"L78 resolves"* in those words. I read the
lead register and did not read the arcs it pointed into. The rule that would have caught
it is already standing — *exhaust the repo BEFORE ranking a gap* — and I applied it to
the building step, not to the ranking step. **The rule now reads: before a lead is named
as open in a status answer, its own arcs are read, not just its row.**

The work above is not thereby wasted — CELL 1 supplied the missing reproduction and
CELL 3 is new — but the ranking that sent me here was wrong, and register R113's item 1
is superseded by this memo.

**Defect caught in-run, before banking.** The certificate's first run printed the nine
primaries under names copied from another arc's ordering; the labels were wrong while
every number was right. Replaced with labels **computed** here — Weyl's dimension formula
over the 36 positive roots — and the `C =` diagram-flip identification promoted from a
printed remark to an asserted gate.

**A pairing bug that crashed rather than lied.** The Weyl dimension formula was first
written with `(μ, α)` as `μ·Cα` instead of `μ·α` (the correct pairing for simply-laced
`ω_i` against root coordinates). It raised `ZeroDivisionError` on the first product
instead of returning plausible wrong dimensions.
