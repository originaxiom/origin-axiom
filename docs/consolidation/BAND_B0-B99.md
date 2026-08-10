# Consolidation Refresh — Band B0–B99 (the base mathematics)

**Status:** READ COMPLETE (B1–B99). Dispositions proposed, none applied.
**Executes:** `docs/THE_CAMPAIGN.md` § *THE CONSOLIDATION REFRESH*, band 1 —
the owner's own instruction that B0–B100 goes first.
**Discipline:** the campaign's steps 1–6. Every row below cites the arc and quotes the
missing statement verbatim. Nothing here is banked; this is a working note on a feature
branch, not a ledger entry.

**Method note.** Read `FINDINGS.md` **bodies**, not claim lines (`COMPUTE_THE_PROGRAM.md`
P3 step 5). Every "absent" below was checked by repo-wide grep over `--include=*.md
--include=*.py`, not by memory — per `WORKING_RULES.md` §0.

---

## 1. What this band actually contains

B1–B5 and B68, B73 have **zero-byte `FINDINGS.md`** — they are among the 45 never-ingested
arcs that ladder rung **X17** names (*"`scripts/forcing/build.py` ingests only files named
exactly `FINDINGS.md` — 45 arcs never ingested, including B1–B5"*). X17 is marked **DONE
(B985)** for the glob fix; the *content* of B1–B5 is still empty here, so the rung's repair
fixed the ingester, not the missing findings.

The band splits into three self-contained investigations:

| arcs | subject | outcome |
|---|---|---|
| B6–B9 | the field-theoretic lift of P15/P16 (wave eqn, Fisher–KPP, spectrum, fusion) | all **STALLED** — the potential is derived, every dynamics is inserted |
| B13–B47 | the half-step, the trace map, and the `I=1/4` selector | ends at **C5**: `T1 → S1 → I=1/4 → λ/h=1`, conditional |
| B48–B99 | the SL(3)/SL(4)/SL(n) metallic trace-map tower | the `degree=rank` programme; P21–P32 promoted from here |

The verdict vocabulary in this band is **`STALLED` / `PRODUCES-PROOF-MODULE` /
`NEEDS_VALIDATION` / `CONDITIONAL`** — an *earlier enum* than the current
`PROVED / NEGATIVE / OPEN / RETRACTED` in `arc_verdict.json`. Worth noting: the
`arc_verdict.json` layer was back-filled, so a `PROVED` verdict on a B13-era arc is a later
seat's re-reading of a body whose own word was `STALLED`.

---

## 2. THE HEADLINE DEBT ROW — the exchange symmetry is an uncounted axiom

**Confidence: high. Verified by four independent greps and by reading every arc in the chain.**

### The statement, verbatim from the arcs

**B16 (`B16_record_swap_status/FINDINGS.md`), under "What Is Not Forced":**

> *"A1-A6 in the current conditional uniqueness theorem do not require the
> orientation-reversing swap. … Therefore `P` is not currently a theorem of the substrate.
> It becomes forced only after adding an exchange-symmetry axiom such as: 'The two record
> labels carry no intrinsic identity before dynamics, so the substrate admits the involution
> exchanging them.' **That axiom is plausible, but it is still an axiom.**"*

**B14** — `F = LP`, `F² = A`, and `F` is unique up to sign in `GL(2,ℤ)`. Also the exact
classification: *"`B(a,b)` has an integer orientation-reversing square root **iff a=b**."*

**B18** — the trace map `T(x,y,z) = (z, x, 2xz − y)` is *"the functorial trace lift of the
half-step"* `F`, **not of `A`**.

**B13, under "Controls"** — the sharpest form:

> *"the safe statement is not 'the trace map contains itself' in an unrestricted sense; it is
> 'the trace-coordinate lift of the primitive orientation-reversing half-step contains the
> `A` sector.'"* — because for direct `A` the symmetric-square lift gives `(t−1)(t²−7t+1)`,
> i.e. **the rank-2 sector is the `A²` sector, not the `A` sector.**

**B19/B32** — the weakest sufficient condition is the operational `(LX)² = A`, and B32's
dependency audit states the chain explicitly:

> *"A1-A6 → A / exchange/half-step → F=LP, F²=A / trace functoriality → T / central-sign
> quotient → projective period-3 return"*

### Why it matters

The trace map is not a side tool. `COMPUTE_THE_PROGRAM.md` §1 lists it as **the twelfth
face** — *"the character-variety / trace-map substrate (Fricke–Vogt, the **L/R shears**, the
I=1/4 selector)"* — and `WORKING_RULES.md` records the atlas's measurement that *"the trace
map recurs in **45 %** of probes."* The entire SL(n) tower (B27–B105, P21–P32), the
Fricke–Vogt invariant line, and C5's selector sit on `F`, and `F` needs `P`.

### The diff — where it is missing

| document | occurrences of "exchange symmetry" / "record swap" / "half-step" | B16 cited? |
|---|---|---|
| `docs/LAW_MAP.md` | **0** | no |
| `docs/THE_FRAMEWORK.md` | **0** | no |
| `docs/THE_CLAIM.md` | **0** | no |
| `docs/THE_LADDER.md` | **0** | no |
| `docs/INPUT_COMPLETENESS_LEDGER.md` | **0** | no |
| `docs/COMPUTE_THE_PROGRAM.md` | **0** | no |
| `CLAIMS.md` | 1 (in C5's prose, not as an axiom) | no |
| `docs/UNIQUENESS_THEOREM.md` | 1 — **but only in the A7 role** (see below) | no |

**Exactly one arc in the whole corpus cites B16.**

`THE_CLAIM.md`'s counted input list reads: *"The six axioms A1–A6 and one bit A7 … plus
five typed external data."* **The exchange-symmetry axiom is not in it.**

### The distinction the record collapses (a terminology collision, B1013-class)

`P` carries **two different roles**, and no document separates them:

1. **Class-level (the A7 role).** `P` is merely the *conjugating element* witnessing
   `LR ~ RL`. `UNIQUENESS_THEOREM.md` §5 and **B979** use it only this way — B979's whole
   argument is that A7 is *based*-level while the swap observation is *class*-level.
   Here `P` is **not** an axiom; it is the reason A7 exists.
2. **Substrate-level (the B16 role).** `P` admitted as an *operation on the substrate*, which
   is what produces `F = LP` and hence the trace map. **This is an added axiom** and B16 says so.

Because only role 1 reached the consolidations, role 2 vanished. A reader of
`THE_FRAMEWORK.md` Layer 0 — which presents A1–A6 + A7 as the complete axiom cost — cannot
recover the fact that the trace-map substrate costs one more.

### Honest scope — what this does NOT touch

**It does not disturb `THE_CLAIM.md`'s derivation theorem.** That chain runs
`A → m004 → ℚ(√−3) → 2T → E₆ → cascade` (B892/B862/B864/B863/B994/B978/B884/B897/B303) and
does not pass through `F` or the trace map. The uncounted axiom is load-bearing for the
**trace-map substrate** — the twelfth face, the SL(n) tower, the Fricke–Vogt/`I=1/4` line,
C5 — and for B13's "the object's trace map contains its own sector" reading.

**Disposition:** RESTORE — as a `THE_LADDER.md` rung (a HOLE inside Layer 0) and one line in
`THE_FRAMEWORK.md` Layer 0. Recommended wording, scoped: *"A1–A6 + A7 force the object. The
trace-map substrate (the twelfth face) additionally requires the exchange-symmetry axiom
(B16): P is not forced by A1–A6."*

---

## 3. SECOND DEBT ROW — B54's involution and the two-ended split were never joined

**Already found once, by the repo itself, and never actioned.**

`frontier/B571_day0_internalization/REPORT.md` item **A3** (confidence: medium):

> *"**B54's twin quadratics {disc −3, disc +5} at c=1 — the earliest sighting of the
> two-ended split, never cross-referenced.** … the P-exchange symmetric/antisymmetric sectors
> of the SL(3) trace-map Jacobian at c=1, m=1 give exactly t²−t+1 (Eisenstein, −3) and
> t²−t−1 (golden, +5) — the same field pair that later became the load-bearing B247–B261
> two-ended structural theorem (ℚ(√−3)/E₆ vs ℚ(√5)/E₈). **Grep confirms zero cross-references
> between the two literatures anywhere in the repo.**"*

Verified here: B54 is cited by B55, B58, B63, B64, B65, B108, B112, B742, B746,
`CAMPAIGN_STATUS.md` and `THEOREM_LEDGER.md` — **all inside the SL(n)-tower literature. No
arc in B247–B261 cites B54.** The cross-reference is still zero.

B55 then extends the c=1 row to **all m**, and the structure is **mod 4**, not odd/even:

> *"m = 1, 3 (mod 4): (t−1)(t+1)(t²−t+1) Φ₆ (Eisenstein, disc −3) / m = 2 (mod 4):
> (t−1)(t+1)(t²+1) Φ₄ (Gaussian) / m = 0 (mod 4): (t−1)³(t+1) degenerate"*
> and the antisymmetric sector is universal: *"(t−1)(t+1)(t²−mt−1)"*.

**Note the collision with the two rows.** `COMPUTE_THE_PROGRAM.md` says the family has two
rows — *"golden in PSL(2,𝒪₋₃), silver in PSL(2,𝒪₋₁)"* — i.e. ℚ(√−3) and ℚ(i). B55's mod-4
symmetric sector produces **exactly those two fields**: Φ₆ (Eisenstein) at m ≡ 1,3 and Φ₄
(Gaussian) at m ≡ 2. This is the row structure appearing in the trace-map Jacobian, one era
early, and it is stated nowhere in the two-ended literature.

**Disposition:** RESTORE as an `OPEN_LEADS` row, carrying B571's own sharpened revival
question verbatim: *"is the B54 involution P … the same Galois/group-theoretic element that
splits the two-ended object into its hyperbolic-ℚ(√−3) and spherical-ℚ(√5) halves —
mechanism identity, or two independent apparitions of the same discriminants?"*
**Note that this question is `P` again** — the same uncounted involution as §2. The two debt
rows are one object.

---

## 4. Smaller law-shaped results checked against LAW_MAP

| arc | law-shaped statement (verbatim or exact) | LAW_MAP | disposition |
|---|---|---|---|
| B14 | `B(a,b)` has an integer orientation-reversing square root **iff `a=b`**; `X² = A ⟹ X = ±F` | cited once, for `M² = RL` / Gieseking only | **fragmentary** — the *classification* is not carried |
| B13/B22 | `t²−3t+1` appears in a symmetric-square lift **exactly when `det(M) = −1` and `tr(M) = ±1`** — "minimal-discriminant orientation-reversing structure" | absent | **absent** — a genuine selection law |
| B22 | `det(M) = −1 ⟹ charpoly contains `(t+1)`" — so the parity eigenvalue is **generic** and cannot carry special content | absent | **absent** — a negative control worth keeping |
| B26/B29/B45 | the Lucas hierarchy: `char(Fⁿ) = t² − Lₙt + 1`, `I = (Lₙ−2)/4`, `(λ/h)² = Lₙ − 2 = 1, 5, 16, 45, 121, …` | absent | **absent** |
| B30 | the central-sign quotient descends polynomially: `(u,v,w,r) → (w, u, 4uw−4r+v, 2uw−r)` with `r² = uvw` | absent | **absent** |
| B35 | the half-step acts on central signs with **order 3 over 𝔽₂**: `(sa,sb) → (sa·sb, sa)` — the mechanism behind the projective period-3 | absent | **absent** |
| B49 | the quartic splitting criterion: `t⁴−At³+Ct²+At+1` splits over ℤ iff `D = A²−4(C+2)` is a square and `A+√D` is even; plus the square-gap propagation lemma | absent | **absent** — a reusable proof module |
| B51 | the symbolic-`m` `c=3` block factorization: symmetric `(t−1)(t+1)(t²−(m²+2)t+1)`, antisymmetric `(t²+mt−1)(t²−(m³+3m)t−1)` | via P22 (B65) at SL(4) only | **fragmentary** at SL(3) |
| B48 | algebraic entropy of the metallic SL(3) trace map: `h_alg(T_m) = log((m+√(m²+4))/2)` | absent | **absent** |
| B54 | the `m=1` cyclotomic sweep `c = −1, 0, 1, 2, 3 → Φ₃, Φ₄, Φ₆, parabolic, char(A)` — elliptic → parabolic boundary → **first hyperbolic factorization** | absent | **absent** |

---

## 5. Cross-cutting observations about the record itself

1. **The band's own verdicts are systematically more modest than the ledger built on them.**
   Every B13–B47 arc says `STALLED`; the chain they establish is C5, correctly labelled
   `conditional`. The discipline held here.
2. **B8 records a near-miss under explicit disclaimer** — `m/g = √(5/(4 log φ)) ≈ 1.6117` vs
   `φ ≈ 1.6180`, *"NOT exact and should NOT be inflated."* This is the falsification
   discipline working at the earliest date in the corpus, and it is the template the later
   Koide handling (B686/B703/B743) follows.
3. **B6 and B7 give two incompatible lifts of the same exact potential** (conservative wave
   equation vs dissipative gradient flow), and B7's own words name the tell: *"the two
   coexisting lifts … is itself the tell: the potential is forced, the dynamics is not."*
   This is Layer 5's "form, not contents" firewall, discovered empirically at B6–B9 long
   before it was named as a Galois theorem in K020.

---

## 6. THE BAND'S UNIFYING FINDING — `P` is one object wearing six names

**This is the strongest thing in the band, and the record states it nowhere in one place.**

Reading B14 → B16 → B18 → B51 → B54 → B62 → B64 → B74 in order, the same involution appears
under six different names, each introduced independently:

| # | name | where | what it does |
|---|---|---|---|
| 1 | **the record swap `P = [[0,1],[1,0]]`** | B16 | exchanges the two records; **an added axiom, not in A1–A6** |
| 2 | **the half-step** `F = LP`, `F² = A` | B14 | the square root of the object, unique up to sign |
| 3 | **the trace map's generator** | B18 | `T` is the trace lift of `F`, *not* of `A` |
| 4 | **the exchange involution** | B51, B54 | commutes with the fixed-line Jacobian `J(m,c)` for **all** `c`; block-diagonalizes it |
| 5 | **the opposition involution `θ = −w₀`** | **B62**, verbatim: *"the exchange involution `P` (`tr W ↔ tr W⁻¹`) **is** the opposition involution `θ = −w₀` on the `sl(n)` root system"* | supplies the θ-split sector dimensions for all `n` |
| 6 | **the contragredient / Dickson parity** | B64 | `P` sends `m → −m`; `L_k(−m) = (−1)^k L_k(m)`, hence even-\|k\| symmetric / odd-\|k\| antisymmetric |
| (7) | **W_N charge conjugation** | B74 | *"the W_N charge-conjugation grading … and the Dickson P-grading **ARE THE SAME involution** — −w₀"* |

**Verified absence.** `docs/LAW_MAP.md` and `docs/THE_FRAMEWORK.md` contain **zero**
occurrences of "opposition", "exchange symmetry", "record swap", or "half-step".
`knowledge/K005` explains `θ = −w₀` as standard Lie theory and **never connects it to the
record swap**; `CLAIMS.md` P33 states the height lemma without the identification. So the
identification exists **only inside B62's body** — precisely the surface
`COMPUTE_THE_PROGRAM.md` P3 step 5 says gets missed.

**Why this matters beyond bookkeeping.** The chain means the object's *substrate* symmetry and
the *root-system* symmetry that organizes the entire SL(n) tower are the same map. That is a
genuine unification the programme owns, sitting unstated — and its first link (#1) is an
axiom nobody counts. Stated together, the honest sentence is:

> *One involution runs from the two-record substrate to the sl(n) opposition involution. It is
> what makes the half-step exist, what makes the trace map the object's own, and what grades
> the Dickson tower. It is **not** implied by A1–A6.*

**Disposition:** RESTORE as a single `LAW_MAP` row plus a `THE_FRAMEWORK` Layer 0 line;
re-verify B62's identification before restoring (campaign step 5) — B62 grades itself *"a
live structural result, not a theorem."* **The restored row must carry that grade**, not
upgrade it.

---

## 7. Further law-shaped results from B61–B99

| arc | statement | LAW_MAP | disposition |
|---|---|---|---|
| B61 | **B60's "SL(5) conditioning wall" was a rank-deficient coordinate set, not a precision limit** — *"The barrier was a coordinate-system defect"*; inverse-word coordinates give genuine rank 24 | absent | **absent** — an instrument lesson identical in shape to B1007's |
| B62 | completed SL(5) fixed-line factorization, degree 24, powers `{−1,1,1,2,2,3,4,5}`, sign sectors `{−2,−3}`, parity degree 4 | absent | **absent** |
| B66 | **`max(n−d,1)` multiplicity law REFUTED** at SL(6): the \|k\|=3 multiplicity is **2, not 3** — it does not grow with `n` | absent | **absent** — a killed law, first-class |
| B70 | the two-block obstruction is **RANK-1**: the only non-separable term is `a·b·tr(X²)`, and `tr(X²) = −2·(Hessian of e₂)` — the single two-index generator is pinned exactly to `e₂` | absent | **absent** — the sharpest statement of the tower's open core |
| B77 | degree=rank refined to the **signed** law `[A,B] = (−1)^{n−1} μⁿ`; and **the A↔D unification is REFUTED** — degree=rank and the Dickson tower are *genuinely different objects*, the mechanism living in the peripheral/cusp structure, not the trace ring | absent | **absent** — a load-bearing negative |
| B84 | the SL(5) barrier is **non-convergence, not gauge**: gauge-*invariant* power sums `tr(DT₀^k)` scatter across seeds, so the ε→0 limit yields genuinely different operators | absent | **absent** |
| B85 | **Λ² functoriality of the figure-eight substitution** — `Λ²(A²B) = (Λ²A)²(Λ²B)`, `Λ²(AB) = (Λ²A)(Λ²B)`; the arc's own words: *"a clean new structural fact (not previously recorded)"* — **but Λ²V does not remove the `char(M²)²` degeneracy** (a root-system fact) | absent | **absent** |
| B69 | the **cusp–torsion law**: cusps at `x = 2cos(π/k)`, `k ∈ {3,…,m+2}`, `k ≡ m (mod 2)` | absent | **absent** |
| B76 | `2cos(π/k) = [2]_q` at `q = e^{iπ/k}` — the cusp value **is** the SU(2)_{k−2} WZW quantum integer; the golden point sits at `k=5 → SU(2)₃`, and appears **not at m=1** but at odd `m ≥ 3` | absent | **absent** — and note it complicates "golden = m=1" readings |
| B87 | m=3 trace-relation curve is **genus 1, not ≥2** — refining V33/Gate1, whose *"irrational ⟹ genus ≥2"* argument *"was too loose"*; the golden factor `x²−x−1` is **shared with m=1's branch locus** | absent | **absent** — a self-correction of a banked bound |

---

## Band status

- [x] B1–B9, B13–B99 read in full (bodies, not claim lines)
- [x] law-shaped results extracted and diffed against `LAW_MAP.md` / `THE_FRAMEWORK.md`
- [x] debt rows written with verbatim quotes and arc citations
- [ ] dispositions applied — **deliberately not applied**; per the owner's instruction this
      band is read-first, bank-later. Nothing here has touched `main`, `CLAIMS.md`,
      `LAW_MAP.md` or `PROGRESS_LOG.md`.
- [ ] B62's identification re-verified in-sandbox before any restoration (campaign step 5)

## Infrastructure defect found while running the locks (not a band-content finding)

`python3 -m pytest -q` **aborts at collection** on a fresh clone that follows
`requirements.txt`, running **zero** tests: `Interrupted: 3 errors during collection`. Cause —
three unguarded top-level `import snappy` statements, where `REPRODUCIBILITY.md` declares
snappy optional (*"The verified figure-eight constants are hard-coded and tested without it"*):

- `tests/test_b461.py:2`
- `tests/test_b719_scale.py:2`
- `frontier/B849_order_parameter/order_parameter.py:22` (loaded by `tests/test_b849_order_parameter.py`)

Nine other test modules import snappy **correctly** (indented, or via `pytest.importorskip`) —
so the safe pattern is established in the repo and these three deviate. The proven core
P1–P16 locks pass in isolation (**76 passed, 8 skipped**), and all **26 governance gates pass**.

