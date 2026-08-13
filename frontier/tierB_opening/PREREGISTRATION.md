# PREREGISTRATION — B518 Tier B, the gap-OPENING table, tested properly

**cc3, 2026-08-13. Owner-commissioned. SEALED BEFORE ANY COMPUTE.**
**Gate 5-Q: no measured physical value enters CLAIMS.md; this is a spectral computation.**

**⚠ ARC ID: NONE CLAIMED.** Per the renumber batch (`8e926df7`), **B1045–B1059 are
RESERVED-NEVER-ASSIGNED on main and main continues at B1060.** cc3's original plan named
`B1045` and **would have collided on its first commit** — caught by reading the reservation
before writing. This work lives at `frontier/tierB_opening/`, deliberately **without a
B-number**, so the atlas's `B\d{1,4}` matcher correctly ignores unbanked work. **cc assigns
an ID if and when it banks.**

---

# §0 — WHAT IS BEING TESTED, AND WHY IT IS THE ONLY ONE OF ITS KIND

**B518 Tier B** is the corpus's **only live, lab-buildable, external prediction**:

| chain | dyadic ½-gap | golden 1/φ-gap |
|---|---|---|
| pure Fibonacci (`a→ab, b→a`) | **absent** | present |
| pure Thue–Morse (`a→ab, b→ba`) | present | **absent** |
| **MIXED (Fib+TM directive)** | **present** | **present** |

**B519 refuted it 3–0. B525 RETRACTED that refutation** — it had conflated Bellissard
gap-**LABELLING** (necessary; about *where* gaps may sit) with gap-**OPENING** (which gaps
physically open; labelling is silent on this, and **Thue–Morse is the textbook case where
labelled gaps fail to open** — Bellissard–Bovier–Ghez). **The cell has been live and
untouched since 2026-07-12.**

# §1 — ⚠ PRIOR-CONTACT REGISTER. cc3 IS NOT BLIND AND WILL NOT PRETEND TO BE.

**Read-only reconnaissance ran during planning and saw partial answers. Designing the
decision rule afterwards risks fitting it to what was seen. Everything below is declared
NOW so it cannot later be laundered as a product of this cell.**

**KNOWN AT SEAL TIME:**

- **K1 — the `thr=0.03` threshold may manufacture the Fibonacci ABSENT cell.** The Fibonacci
  label at order 17 sits at IDS `0.5065778`, **0.0066 from ½ — inside the existing test's own
  0.01 tolerance** — and its gap appeared **open**, width ≈`0.0096`, converging. The cell
  passes only because `0.0096 < 0.03`.
- **K2 — the mixed row's golden gap may be an IMPOSTOR** at IDS `= 8/13` (a Fibonacci
  convergent, and the chain's own letter frequency one step earlier).
  `|8/13 − 1/φ| = 0.00265`.
- **K3 — a rank-1 mechanism predicts failure.** `M_tm = [[1,1],[1,1]]` has rank 1: each tm
  step resets letter frequencies to (½,½). So `freq → 1/φ` needs **finitely many** tm steps
  while `freq = ½` exactly needs the **last** step to be tm — **mutually exclusive.**
- **K4 — the TM module may be `(1/3)ℤ[1/2]`, not the banked `ℤ[1/2]`.**
- **K5 — the three chains are currently compared at different N, two mid-substitution.**

> **RULING: K1–K5 carry the weight of their mathematics and NONE of the weight of their
> discovery.** They are **reconnaissance at one λ, one boundary condition, one seed** — not
> results. **This cell re-derives every one of them under the protocol below or reports them
> as not reproduced.**
>
> **AND THE HAZARD THIS CREATES, NAMED: the decision rule below was written knowing K1–K5.**
> **Anyone auditing this cell should check whether the rule is tuned to produce them.**
> cc3's defence is that the rule is **threshold-free by construction** (§4) — the two
> hypotheses sit a full unit apart in an exponent — **but cc3 is not the seat that gets to
> judge that.**

**cc3 DECLARES NO PREDICTION on the outcome and WILL NOT ADJUDICATE IT.** The verdict is
cc's bench.

# §2 — CONVENTIONS, PINNED. **None of these exist in any document today.**

1. `H = tridiag(1, V, 1)` with `V_i = +λ` for letter `a`, `−λ` for `b`. **Stated because the
   a↔b choice makes Fibonacci a different chain** (TM is symmetric under it).
2. **`λ` is a variable, never a constant.** The existing test implies `λ=1`; **no document
   states it.** §5 sweeps it.
3. `±λ` convention (not `±λ/2`, not `{0,λ}`) — B505 records the resulting factor-of-4
   ambiguity in `κ−2 = 4λ²` vs `λ²`. **At λ=1: `κ=6` under B505/B518's convention, `κ=3`
   under B161/B162's. Both are in the record.**
4. Finite `N×N` matrix = **Dirichlet BC**. Tested for sensitivity in C8.
5. **COMPLETE SUBSTITUTION WORDS ONLY. NEVER TRUNCATED.** A truncated word is not a
   controlled object: its boundary defect is O(1) states — the size of the effect measured.
6. The directive is an **infinite sequence with a stated generating rule**, never a
   hardcoded list.

# §3 — THE LADDERS AND THE REGISTRATION TEST

**Ladders (complete words, consecutive depths so both parities are sampled):**
Fibonacci `F_n`; TM `2^n`; mixed `|σ₁…σₙ(a)|` for the stated directive.

**Equal-N comparison is NOT required**: every reported quantity is an `N→∞` limit, and limits
need no N-matching. Report both N and depth axes.

**Registration**, per chain word of length `N`: `c = round(v·N)`;
`k = argmax` spacing over `[c−M, c+M]` with **`M = 8` fixed**; `W = E_{k+1} − E_k`;
`s = median` of the other spacings in the window.

> ## **THE REGISTRATION TEST — the cheapest guard and the whole game:**
> ### **`N·|IDS_N − v| ≲ 2`, non-increasing, across a ≥100× range of N.**
>
> **A DIVERGENCE test, not a proximity test.** Any impostor `v' ≠ v` has
> `N·|IDS_N − v| → N·|v'−v| → ∞` **linearly**, however small `|v'−v|` is. A true label stays
> `O(1)` forever. **No tolerance is introduced. It costs nothing beyond rungs already run.**

# §4 — OPENNESS WITHOUT A MAGIC THRESHOLD

Within one parity class (depth step 2):
`β = −ln(W_{n+2}/W_n) / ln(N_{n+2}/N_n)` · `ρ = W/s`

| | β | ρ |
|---|---|---|
| real gap, positive limiting width | **→ 0** | **∝ N** |
| 1/N finite-size level spacing | **→ 1** | **O(1)** |

**OPEN** iff `|β| ≤ 0.10` **and** `d log ρ / d log N = 1 ± 0.15` **and** registration passes —
**in BOTH parity classes.** **CLOSED** iff `β ≥ 0.70` or `ρ` shows no growth. Otherwise
**AMBIGUOUS — reported as such, never forced.**

**Parity is not optional:** reconnaissance saw a tail whose ½ gap alternates between width
`0.9165` and `0.0000` by depth parity. **Fit within a class; the verdict is the WORSE class.**
If the directive is eventually periodic with period `p`, use `p` residue classes, not 2.

**Reported:** `W̃_∞ = W_∞/(4+2λ)` (dimensionless, chain-comparable) via Richardson limit per
parity, ± half the parity amplitude.

# §5 — λ, AND WHY A POINT-CHECK IS UNSAFE IN BOTH DIRECTIONS

`λ ∈ {0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2}`. **At λ=0 every cell is CLOSED; at large λ nearly
everything opens — a large-λ confirmation is close to vacuous.** Report per cell the
**opening law** `W̃_∞ ~ c·λ^p`, or a threshold `λ_c` — **not a boolean.**

**Fourier–Bohr `|V̂(v)|` is triage only, ONE-DIRECTIONAL** (`|V̂|>0 ⇒ opens at first order`).
**Never a decision rule:** `|V̂(½)| = 0` for pure TM while its ½ gap is `0.828` wide.

# §6 — THE ABSENT CELLS: SYMBOLIC, PLUS AN EXCLUSION PROFILE

**Exact module non-membership in sympy** — no floats, no tolerance: `½ ∉ ℤ+φℤ`;
`1/φ ∉ (1/3)ℤ[1/2]`. **Machinery self-test: reproduce `(1/3)ℤ[1/2]` for pure TM** — the naive
letter-frequency tower gives `ℤ[1/2]` and is **wrong**, which is the built-in unit test.

**But symbolic non-membership alone licenses nothing measurable, because both modules are
DENSE** — at any tolerance an allowed label lies within it, and by Dry Ten Martini
(Band–Beckus–Loewy 2024) every Sturmian label opens for every `λ≠0`. **So "absent at
tolerance δ" is FALSE for every δ.** The measurable content is the **exclusion profile**
`W*(δ) → 0` with fitted exponent `q`, on a geometric δ ladder (`2⁻² … 2⁻¹²`, subject to
`δN ≥ 20`).

# §7 — CONTROLS. C1 AND C3 MAY NOT BE SKIPPED.

| id | control | required |
|---|---|---|
| **C1** | i.i.d. Bernoulli at matched letter frequency | **all CLOSED. If any cell reads OPEN the openness criterion is broken and NOTHING else in the run means anything.** |
| **C3** | 200 random shifted targets through the identical pipeline | **pipeline-level false-positive rate < 5%** |
| C2 | periodic `q = 5, 13` | ground truth `(1/q)ℤ` |
| C4 | doubling decoy `a→aa, b→bb` on Fibonacci | even denominators, **zero TM content** — tests whether "½ ⇒ TM ancestry" |
| C5 | tail-swap (`fib`, `tm`, `(fib,tm)`, permuted) | **the answer may depend on the tail** |
| C6 | λ = 0 | all CLOSED |
| C7 | Sturm-vs-dense; windowed-vs-full | exact agreement |
| C8 | seed / word-offset / BC | `W̃_∞` unchanged |
| C9 | rank margin | **> 3** to claim an identification |

# §8 — THE DECISION RULE. FROZEN HERE.

**CONFIRMED** iff: `½, 1/φ ∈ G_mixed` exactly · the six cells read
`Fib(CLOSED, OPEN) · TM(OPEN, CLOSED) · mixed(OPEN, OPEN)` · every OPEN passes registration in
**both** parity classes · every CLOSED shows `W*(δ)→0, q>0` · **C3 < 5% and C1 all-CLOSED**.

**REFUTED** on any of:
- **R1** — `1/φ ∉ G_mixed` or `½ ∉ G_mixed` (Bellissard necessity forbids the gap; **zero CPU**)
- **R2** — a mixed cell CLOSED at every λ in the grid
- **R3** — registration diverges while another module element stays bounded
- **R4** — a cell OPEN in one parity class and CLOSED in the other
- **R5** — C1 returns OPEN for any cell (**pipeline invalid; specifically NOT a confirmation**)
- **R6** — C3 > 20% (**INCONCLUSIVE, never support**)

**SURVIVES-WEAKENED** if the row holds only above some `λ_c`, or only for an
eventually-Fibonacci tail. **The restriction becomes part of the claim and B518 must be
re-worded.**

**AMBIGUOUS** is a real outcome and gets published as one.

# §9 — WHAT THIS CELL DOES NOT DO

Approach a lab · write the photonic/polariton spec sheet (PC23's `4δ + 2Γ < g_min`, and only
if the numerics survive) · **adjudicate its own outcome (cc's bench)** · touch `CLAIMS.md` ·
claim an arc ID.

**And a name collision to respect:** B530's "mixed chain" is a **different 4-letter object**.
**A verification of one must never be reported as the other.**

---

**Seal: SHA-256 over this file as committed. cc3 cannot amend it after the hash is handed
over; an amended file is a different cell.**
