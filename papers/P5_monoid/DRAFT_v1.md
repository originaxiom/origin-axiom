# The four verbs of F₂ — a classification of End(F₂) by its action on the character variety

**Draft v1 (table-first), 2026-08-01.** Written under the outline's discipline: **one claim per row
with its reproducer and its LEVEL; no synthesis sentence without a computation behind it.** Phase 1's
lit-gate is binding on every row (`PHASE1_LITGATE.md`).

**Levels used throughout** — the distinction the gate proved load-bearing:
**`End(F₂)`** (the free group itself) · **`trace-map`** (the induced polynomial map on X(F₂)) ·
**`toral`** (the abelianization, M₂(ℤ) on a torus).

---

## §1 The classification — four strata of End(F₂)

**Hopf dichotomy** — im(φ) has rank 2 ⟺ φ injective; rank ≤ 1 ⟺ ker φ ≠ 1.
**CITED**: Nielsen–Schreier + F₂ Hopfian via Mal'cev (Lyndon–Schupp §I.4). Crossed with
det(abelianization):

| stratum | citizen | trace map | κ-law (exact) | level | status |
|---|---|---|---|---|---|
| **1** inj, det ±1 (Aut) | metallic `a→aᵐb, b→a` | `(z, x, xz−y)` at m=1 | **κ′ = κ** | trace-map | computed |
| **2** inj, \|det\| ≥ 2 | `A→A², B→B²` (det 4) | `(x²−2, y²−2, xyz−x²−y²+2)` | **κ′−2 = (κ−2)·x²y²** | trace-map | computed |
| **2′** det −2 | period-doubling `a→ab, b→aa` | `(z, x²−2, (x²−1)z−xy)` | stratum-2 family | trace-map | computed |
| **3** inj, det 0 | Thue–Morse `a→AB, b→BA` | `(z, z, xyz−x²−y²+2)` | **κ′−2 = (κ−2)(x²+y²−xyz)** | trace-map | computed |
| **4** non-inj | `a→ab, b→ab` | factors through one variable | **image ⊂ {κ=2}** | trace-map | computed |

**Witnesses, all in the free group** (`End(F₂)` level, not trace-map): stratum 3 injective because
`(AB)(BA) = AB²A ≠ BA²B = (BA)(AB)`, so ⟨AB,BA⟩ is free of rank 2 and Hopficity forces injectivity
(**I1**); stratum 2 by `A²B² ≠ B²A²`; stratum 4 by the exact kernel element `φ(AB⁻¹) = 1`.

**Reproducer:** `frontier/B497_endomorphism_monoid/verify_monoid.py` — Cayley–Hamilton per trace map,
random exact SL(2,ℚ), F_p guards, free-group witnesses. **Lock:** `tests/test_b497_monoid.py`.
**Current output:** `stratum-2 trace maps … True`, `exact kappa multipliers … True`,
`witnesses … True`, `F_p guard … True`.

> **§1.1 What is NOT claimed here (Phase 1, Gate C).** Cantat–Dujardin and Cantat–Dupont–
> Martin-Baillon have developed the dynamics of **automorphism** groups acting on precisely this
> object — the relative character variety of the once-punctured torus, where the commutator is the
> loop around the puncture. **Stratum 1 is their territory.** The claim of this section is the
> classification **across strata 2, 3 and 4 — the non-invertible sector**, which the automorphism
> literature does not address.

---

## §2 The two universal laws

**U1 — the reducible locus {κ = 2} is invariant under EVERY endomorphism of F₂.**
Proof: reducible ⟺ simultaneously triangularizable; words in triangular matrices are triangular.
**The lemma is KNOWN-FOLKLORE; the banked contribution is its USE** — the per-verb multiplier table,
i.e. that `(κ−2)` divides `(κ′−2)` for every substitution, with the multiplier read off §1.
*Level:* trace-map. *Verified on 20 random endomorphisms.*

**U2 — the classical floor is toral.** On {κ = 2}, parametrized by eigenvalue characters (α, β),
every endomorphism acts **through its abelianization matrix** on the character torus. Verified
exactly for representatives of all four strata. The classical shadow of the whole monoid is
**M₂(ℤ) acting on a torus**: cat maps (1), expanding toral endomorphisms (2), projections (3),
constants (4). *Level:* **toral**.

> **§2.1 The toral floor is CITED, not claimed (Phase 1, Gate E — the sharpest gate).**
> **The monoid SL₂(ℕ) is generated FREELY by L and R.** This is classical Stern–Brocot/Farey
> material (Reutenauer, *On the Stern–Brocot expansion of real numbers*; Northshield on Stern's
> diatomic sequence), together with the L/R-word ↔ continued-fraction encoding.
>
> **Everything the Stern–Brocot literature owns lives downstairs.** U2 is *called* the toral floor for
> exactly this reason. **What survives above it is the Hopf coordinate — injective vs non-injective —
> which abelianization forgets**, and that is where §1's classification lives.
>
> **This gate could have pre-empted the paper, and the paper's own methods discipline is what
> answered it** (see §6).

---

## §3 The drift ledger

| verb | multiplier | `E[log mult]` | how |
|---|---|---|---|
| units (stratum 1) | 1 | **0** | trivially |
| decimation (stratum 2) | `x²y²` | **−2** | Fourier |
| Thue–Morse (stratum 3) | `x²+y²−xyz` | **0** | convex combination |

**Stratum 2.** Per factor, `E[log(4cos²t)]` under the Haar angle density `(2/π)sin²t`. With
`log|2cos t| = Σ_{k≥1}(−1)^{k+1}cos(2kt)/k` and `sin²t = (1−cos2t)/2`, the k ≥ 1 terms integrate away.
`mult_D = x²y²` has two independent factors ⟹ **`E[log mult_D] = −2`. QED.** (mpmath 15-digit check.)

**Stratum 3.** `mult_M` is the convex combination `4sin²(a+b)·(1+u)/2 + 4sin²(a−b)·(1−u)/2`; the
u-integral reduces to a hand proof and gives **`E[log mult_M] = −4.5×10⁻²⁷`, zero to 26 digits.**

**Reproducer:** `frontier/B498_mixed_monoid_dynamics/c3_orbits.py`. **Lock:** `tests/test_b498_mixed.py`.
**Current output** (two seeds): units `+0.15 / +0.07`; F80/M20 `−2.12 / −2.13`; F80/D20 `−5.26 / −4.66`;
F80/M10/D10 `−3.68 / −4.87`.

> **§3.1 The METHOD is classical (Phase 1, Gate D).** `E[log|2cos t|]` by that Fourier series is the
> textbook Mahler-measure computation, and Lyapunov exponents of random matrix products are a deep
> developed field (Furstenberg; Viswanath on random Fibonacci sequences; the CLT literature).
> **The claim of this section is the LEDGER — `−2` and `0` as invariants separating the verbs — not
> the technique that evaluates them.** This is the paper's highest residual novelty risk and is
> flagged as such.

---

## §4 The geometry of the singular verbs — a dichotomy

**Q3 (exact).** The decimation mapping torus `G_dec = ⟨A,B,t | tAt⁻¹=A², tBt⁻¹=B²⟩` contains
**BS(1,2) = ⟨A,t⟩ exactly** — the edge subgroup embeds, by Britton's lemma for ascending HNN, and the
relation is the witness. Hyperbolic groups contain no Baumslag–Solitar subgroups ⟹ **`G_dec` is NOT
word-hyperbolic**, and not a hyperbolic-3-manifold group. *Level:* `End(F₂)`. **Exact.**

**Q2 — and this row is deliberately two cells.**

| | |
|---|---|
| **EVIDENCE** | no periodic conjugacy class found: **all 117 cyclic classes of length ≤ 6, k ≤ 6, powers ≤ 4**. Bounded search. |
| **HYPOTHESIS VERIFIED** | **NO.** Mutanguha's theorem requires **no BS(1,m) subgroup for any m ≥ 1**, plus irreducibility. **Neither is checked here.** The search is evidence for *atoroidality* — a related but different condition. |

> **A single-cell row reading "φ_TM is atoroidal, hence word-hyperbolic by Mutanguha" would be
> false.** The theorem is not being applied; bounded evidence is being reported next to it.

**What Mutanguha does give us (Phase 1, Gate A):** the theorem is an **iff** and **applies to all
injective endomorphisms of F₂** — exactly this setting. **That makes Q3 exact in the direction it is
used**, since exhibiting BS(1,2) is precisely the theorem's own obstruction.

**To read before v2:** *Hyperbolicity of Multiple Ascending HNN Extensions of Free Groups*
(arXiv 2604.19154, 2026) — directly adjacent and post-dating the outline.

**Also cite:** *ascending HNN extensions of f.g. free groups are Hopfian*
(Geoghegan–Mihalik–Sapir–Wise) — it bears on §1's Hopf coordinate.

**Reproducer:** `frontier/B497_endomorphism_monoid/phase23_run.py`.

---

## §5 The classical-floor torsion factory, the monopoly death, and Q1b

The `det(N ± I)` construction on the classical floor; the wild S₄ birth; and the Q1b reduction lemma.
**Reproducer:** `frontier/B498_mixed_monoid_dynamics/q2_depth3.py`. **Lock:** `tests/test_b498_mixed.py`.
*Level:* toral (factory) / `End(F₂)` (Q1b). **[v2: expand to one row per sub-claim.]**

---

## §6 Methods — the failure mode this paper was written against

The campaign's six caught errors share one shape: **a named mathematical term used with the wrong
technical content** — "quadratic twist" for Jacobian-of-cover; "cyclic" for odd permutations; wrong
a-invariants; sign slips. **Reaching for the impressive word instead of computing the boring check**
(do the j-invariants match? what is the permutation's parity? which model does the repo bank?). The
same failure killed three earlier drafts, whose prose sat one categorical level too strong.

**The protocol that caught all six:** every named term banked **with its defining invariant computed
in the same script**; every identity **with its level** (`End(F₂)` / `trace-map` / `toral`) and
`φ(a), φ(b)` spelled out.

> **This is not a methodological aside. It is why §2.1 exists.** The Stern–Brocot literature owns
> the free generation of SL₂(ℕ) by L and R — a fact that would pre-empt a careless version of this
> paper. **It does not pre-empt this one only because the classification is stated at `End(F₂)` and
> that fact lives at `toral`.** The lit-gate found the collision; **the level discipline had already
> answered it.**

---

## Provenance

Every row above resolves to **B497** or **B498** with a running reproducer and a passing lock —
**18 locks green** (`test_b497_monoid.py`, `test_b498_mixed.py`); claim resolution table in
`PHASE0_CLAIMS.md`; lit-gate in `PHASE1_LITGATE.md`. **Anchor: P4.**

**Firewalled:** the verb names (evolution / renormalization / decoherence / erasure) live in
`speculations/S063` only and appear nowhere in this draft as physics.

**Next:** Phase 3 — adversarial pass, **pointed first at §4's Q2 row**, then the voice pass.
