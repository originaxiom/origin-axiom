# B974 — PHASE A SYNTHESIS (MASTERPLAN v3)

*Written for the banking seat. Four leads scouted and worked: L134 (B970), L132 (B971),
L137 (B972), L135 (B973). Three of the four were expected to close negative or vacuous;
all three did. That is the intended outcome, not a shortfall.*

**Firewall status:** structure only. No measured value is claimed. Gate 5 untouched.
Nothing here promotes to `CLAIMS.md`.

---

## 0. WHAT THIS CELL COMPUTED FOR ITSELF

A synthesis seat that only forwards other cells' numbers is citing, not computing. Five
load-bearing facts — one per lead plus one new — were re-derived here from the E₆ Cartan
matrix alone, independently of the four cells' code. Scripts and outputs are in this
directory (`verify1_anomaly_vacuity.py`, `verify2_psi_grading.py`, `verify3_pencil_gauge.py`,
`verify*_out.txt`), all re-runnable in seconds.

| # | fact | result |
|---|---|---|
| V1 | over the **27** (Weyl orbit of ω₁), `Σ λ(H)` and `Σ λ(H)³` as forms in the six Cartan coordinates | **identically 0** — L132's vacuity identity, confirmed |
| V2 | MB12 **failure controls** for V1 | su(3) **3**: `Σλ³ = 3g₁g₂(g₁−g₂) ≠ 0`; su(5) **5** and **10**: equal nonzero cubics (so **10 ⊕ 5̄** cancels — the textbook SU(5) cancellation, reproduced). **The test can fail.** |
| V3 | ψ-grading of the 27 (H dual to α₁, centralizing the D₅) | `{−2/3: 10, 1/3: 16, 4/3: 1}` — the **1 + 16 + 10** split with ψ in ratio **4 : 1 : −2**; **exotics = 11** against a 16, **12** against a 15 |
| V4 | the exotic-mass selection rule | `ψ(10)+ψ(10) = −4/3`; the **unique** state in the 27 with the compensating `+4/3` is **the singlet S**. L134's central claim, confirmed with no fitting |
| V5 | **new here**: every weight of the 27 lies in the class **1/3 mod ℤ** of the ℤ/3 centre grading (all three levels ≡ 1/3) | ⟹ **27 ⊗ 27 carries centre-charge 2/3 ≠ 0, and the adjoint carries 0** ⟹ **the 78 does not occur in 27 ⊗ 27** (see §2.4 — this is the mechanism behind the whole verdict) |

Additionally computed (V6, `verify3`): under the pencil's own ℚ\*-gauge freedom `t → t/c`
applied to the object's canonical cubic `s³ − 12s − 5`, the coefficient supports move —
`P_lead ∈ {{}, {3}, {5}, {13}}`, `P_const ∈ {{5}, {3}, {2,5}, {5,7}, {5,13}}` — while the
**discriminant squarefree kernel stays {7, 11} at every c**, and the field is invariant
because `ℚ(cα) = ℚ(α)` for `c ∈ ℚ*`. This decides a question §3 raises and §2.5 answers.

---

## 1. PER LEAD

### 1.1 L134 — the twelve exotics → **CLOSED, and it is not an independent gap**

**Established.** The exotic sector is `D(3,1)₋₁/₃ ×3`, `H_u(1,2)₊₁/₂ ×2` (ψ = −2, χ = +2),
`D̄(3̄,1)₊₁/₃ ×3`, `H_d(1,2)₋₁/₂ ×2` (ψ = −2, χ = −2), `S(1,1)₀` (ψ = +4, χ = 0) — **eleven**
states against the 16, twelve only when counted against a 15-fermion generation (the twelfth
being ν^c, which sits **inside** the 16). Independently confirmed here at V3. No bare mass
exists inside a single 27; any mass operator for the exotics must carry `(ψ, χ) = (4, 0)`;
**exactly one direction in the 27 has it — S, the highest-weight/rank-1 element of J₃(𝕆)
with reductive stabiliser Spin(10)** (V4, computed, no fitting). The mechanism in the
literature is one line everywhere — `W ⊃ κ S D D̄`, `M_D = κ⟨S⟩`, i.e. `M_D/M_Z′` is a
**coupling** ratio, not a scale ratio (Kang–Langacker–Nelson 0708.2701, King–Moretti–Nevzorov
2002.02788, Halverson–Langacker 1801.03503 — *read by the scout, not re-derived here*). Under
SM quantum numbers alone the exotics are **not new**: `D̄ ≡ d^c`, `H_d ≡ L`, `S ≡ ν^c`, and
`D`, `H_u` are their conjugates — **the set of exotics with SM quantum numbers found nowhere
in the 16 is empty**; what makes them findable is multiplicity and vector-likeness, not a
charge. MB12 certificate for that test: run on the **78** it *fails* (X/Y bosons at (3,2)₋₅/₆).
Second computed result: the A₂+A₁ Levi resolves a **split, not a label** — exactly three
so(10)s sit above it, they disagree, **9/27 states are unambiguous and 18/27 change side**,
and the residual relative Weyl group `N_W(W_L)/W_L` = **S₃** (built from all 51840 elements of
W(E₆)); but the cascade's **first** step already fixes one so(10), because `Cent(ψ)` has
dim 46 and an exhaustive scan of all 2⁷−1 subsets of the extended diagram shows every dim-46
centralizer is so(10) ⊕ u(1).

**Not established.** Nothing here makes the exotics heavy. The three-so(10)/S₃ result was
obtained with **no literature read** and should be carried as **very likely a reproduction**
of standard E₆ su(3)³ lore until scouted. Collider numbers quoted in the record (250/190 GeV)
are stale 2008 figures; the modern ≈1.3–1.5 TeV bound was **not** re-derived. Nevzorov
1205.5967's requirement of *extra* TeV vector-like matter beyond complete 27s is carried from
the scout, unverified — and it matters (§2.3).

**Disposition: CLOSED.** Verdict: *L134 is a corollary of the 27-VEV row, not a second input.*
⟨S⟩ ≠ 0 **is** E₆ → SO(10), rank 6 → 5 — the same input at the same step as L133/L138.
Carrying it as a separate ledger row double-counts. Three ledger corrections are owed (§3.1).

### 1.2 L132 — anomaly non-vacuity → **CLOSED, VACUOUS, and triply so**

**Established.** On complete 27s every anomaly condition vanishes identically — confirmed
here at V1 in all six Cartan coordinates, so every cubic, mixed and gravitational condition
is a coefficient of an identically-zero form. The vacuity is **layered**: at **SU(5)**
granularity there is a real cancellation (`10: +5/36` against `5̄: −5/36`, and V2 confirms
`Σλ³(10) = Σλ³(5)` so `10 ⊕ 5̄` cancels — a live failure mode); at **SO(10)** granularity
**each piece vanishes separately**, with no 16 ↔ (10+1) cross-talk; and third, the exotics
being a real (vector-like) SM rep, giving them **free** hypercharges `y₁, y₂` leaves all four
coefficients identically zero in `y₁, y₂` — **the anomaly check carries zero information about
L134's exotic sector at any charge assignment**. MB12 discharged both ways: lone 10, lone 5̄,
`27 − e^c`, `27 − exotic-5` (Witten odd) all fail; su(3)'s 3 and su(5)'s 5/10 have nonzero
cubics through the same code path; of 2047 non-empty sub-multiplet sets exactly **one** has a
3-dimensional anomaly-free abelian sector — the complete 27. Does Y fall out? **No, twice**:
over the 27 the solution space is 3-dimensional (no selection); over the complete 16 it is
2-dimensional (`ψ` dies, `Y` is not distinguished from `χ`); only over the chiral **15** is
`Y` forced — and the step conferring the selective power is deleting **ν_R**, a total SM
singlet contributing 0 to every coefficient, i.e. **a deletion the hypercharge conditions
cannot themselves detect**. The precise non-vacuity condition, stated: *L132 acquires content
iff something deletes states from inside an SO(10) multiplet in a non-vector-like way.*

**Not established.** No live literature search was reachable from either seat — the scout's
§4 null is **uncertified**. The 2047-subset map was run once (scout) and not re-run. The
cohomological reading was closed by computation (the centralizer of the principal sl(2) in
e₆ is 0-dimensional, so H¹(M; 27) matter has no continuous commutant and no anomaly conditions
exist to write) — that closes a route, it does not open one.

**Disposition: CLOSED — VACUOUS.** With a **prior-art correction inside our own corpus**: B864
(`frontier/B864_anomaly_ledger/FINDINGS.md`) had already banked both the vacuity sentence and
the hypercharge-uniqueness result on 2026-08-03, and B951's literature panel did not surface
it. Both Phase A seats reproduced B864's arithmetic exactly. **This is a reproduction, not a
discovery.** A scope-note, not a retraction, is owed on B864 (§3.2).

### 1.3 L137 — the value/pencil split → **CLOSED, REFUTED (strong half) and UNSEALABLE (weak half)**

**Established.** A pre-statable criterion exists — *intrinsically-normalised element of K*
(canonical minimal polynomial, no ℚ\*-action) versus *root-locus in a pencil `A + t·B`* (free
coordinate scale acting as `(a₃, a₂c, a₁c², a₀c³)`) — and it does **not** separate. Three
computed reasons. (i) **Counterexample on the value side:** T, B914's colorless coupling
invariant, registered at `docs/LAW_MAP.md:197` in §F "the value layer" as *normalization-free*,
fails both extreme clauses (`|P_lead| ≥ 5`, `|P_const| = 5`) and fails **invariantly**
(`F(T) ≥ 7` forced primes against a ceiling of 4). Gate run first: T's banked 50-digit value
is a root of its banked cubic to rel. residual 1.34e-54, content 1. (ii) **The pencil-side
verdicts are not properties of the objects:** B888's two cubics **flip to holding** inside
their own gauge orbit, and μ's diagnosis flips too (`P_const = {13}` at B941/B947's `ρ = 13t`,
`{}` at B866's own `t` — same locus). Confirmed here independently at V6 on the object's own
`s³ − 12s − 5`: the lead and constant supports take four and five different values across the
gauge orbit. (iii) **The statistic is not taxonomic** and, by-product, **not effectively
computable** (T's 53-digit cofactor is unfactored), and **its own vacuity exclusion is not
gauge-invariant** — K's canonical generator both *holds* and is *excluded*, so one field
reaches holds, fails and excluded by renormalisation. All seven B941 families generate the
**same** field K (138 primes, zero splitting-type mismatches), corroborating B910's One-Field
theorem: seven elements of one field in seven normalisations, with no arithmetic class
distinction available to seal.

**Not established.** Field identity is Chebotarev evidence, not proof (sympy
`field_isomorphism` → None, `maximal_order` → flint `CoercionFailed`, the same failure B937
documents). `|P_lead(T)|` and `F(T)` are lower bounds — sufficient to decide, not exact. The
classification of T as a value family is argued (it shares every pre-statable property of the
holders; the only excluders are "was in B941's list" or a post-hoc size cutoff), not assumed —
but it is an argument, and the refutation rests on it.

**Disposition: CLOSED — REFUTED, no successor.** The enlarged census (found 11 further banked
cubics; score moves 5/2 → **8 of 9 value holding, 0 of 4 pencils holding**, and B947's own
decision rule returns OUTCOME SPECIAL **again**) is the trap, not the evidence: it is more
tempting and equally post-hoc. **Never seal the coefficient-support form again.** One
method-level addition to MB12 is earned: *is the criterion invariant under the object's own
gauge freedom?*

### 1.4 L135 — the presence side / frame rebuild → **DISCHARGED for the rebuild, BLOCKED on tier**

**Established.** The frame is fully defined in-repo (`CMT_DRAFT.md` §2 + `B854`'s
`e6_centralizer.py:232-252`) and was rebuilt from B854's build alone at **two primes never
used on this bench** (41131, 41201; scout added 40883): **51/51 mandated and cross-checks
PASS, 90/90 combined**, nothing tuned. Floor dim **12** (exact ℚ), M12 dim **12, 12**,
`M12 ∩ core = 0`, frame Gram diagonal with signature (2,2) and the four ledger norms
digit-identical, core 30, `derived(floor)` = 8 with centre 0 (⟹ A₂), κ coefficient-identical
with const −19³ and disc kernel {7,11}, wall dims [30,30,30] with pairwise **and** triple
intersections all equal to the floor, closing `3·30 − 3·12 + 12 = 66`. **One import removed:**
the μ-walls are now derived from M12 itself (`det₁₂ = c·cubic⁴`) and then *agree* with the
cited μ — so the two-normalization hazard L137 identifies cannot bite here. All seven of
B958's presence-side legs are now computable on this bench (previously zero): legs 5–7 had
never been run and give **12 one-dimensional common eigenlines with 12 distinct weight
4-tuples**, closed under **exactly** the B939 W_frame Klein group and not under any of four
non-W_frame sign patterns, in **3 free orbits of size 4**. **Reduction worth banking:** the
orbit ↔ generation bijection is *forced* by legs 5+6 plus ratio-distinctness — a corollary,
so the presence side should stop counting it as an eighth independent fact. **New structural
fact, born from a recorded failure rather than tuned away:** the noncompact charges g₈, g₁₆
have M12 weights in F_p at **24/24** κ-split primes; the compact charges g₁₄, g₂₂ at **16/24**,
failing *totally* (residual 12, six irreducible quadratics). So "in F_p" means **"in the wall
field K"**: the noncompact weights live in K, the compact weights need a **proper extension**
of K. The frame's compact/noncompact split is mirrored in the arithmetic of the M12 weights.

**Not established.** Char-0 exactification over K — this cell added **primes, not tier**, and
four independent primes is not a certificate. The identity of the compact-weight extension is
open (16/24 is consistent with density ½, two-sided p ≈ 0.15; 24 primes cannot identify it;
ℚ(√77) was **not** tested and **cannot** be tested this way — every scanned prime splits κ and
therefore already forces 77 to be a QR, an MB12 vacuity the seat caught and reported rather
than passing). Conjugacy of `derived(floor)` with the standard A₂ Levi is consistent with
(equal centralizer dim 16), not proven. Import I-4 outstanding. And the seat records honestly
that its own mandated check `M12 ∩ core = 0` is **dimension-generic** (12 + 30 < 78) —
non-vacuous but weak; the discriminating content is `span = 66` via the wall dims and the
triple-intersection numbers.

**Disposition: BLOCKED — on char-0 exactification over K** (restriction of scalars, the B877
FMT recipe). Precise blocker: everything above is mod-p at four primes; the certificate tier
requires exact arithmetic over K, and that same step settles the compact-weight extension as
a side effect. **Not blocked on definitions** — that debt is discharged. **This unblocks
L142** ("three sites, one field: one theorem or three facts?"), which was explicitly waiting
on L135's definitions.

---

## 2. WHAT CHANGED ABOUT THE SM VERDICT

The banked sentence: *"the object supplies the adjoint half of a grand-unified symmetry
breaking and not the 27 half, and the 27 half is an input in every theory anyone has."*

**Verdict: unchanged in substance. Sharpened in three ways, weakened in one, and given a
mechanism it did not have.** Adversarially, below.

### 2.1 The sharpening that matters most — three leads collapse into one input

L133 (rank reduction), L134 (exotic mass) and L132 (anomaly content) were scouted as three
independent gaps. They are one.

- **L133** needs rank 6 → 4 with the 27 kept complex: two rank-1 **27 VEVs**.
- **L134** needs `(ψ, χ) = (4, 0)`, and the unique carrier in the 27 is **S** — the rank-1
  direction, i.e. **the first of those same two 27 VEVs** (V4, computed here).
- **L132** acquires content **iff** something deletes states from inside an SO(10) multiplet
  non-vector-likely — which is exactly what **the second** 27 VEV (SO(10) → SU(5), splitting
  the 16 into 10 + 5̄ + 1) does, and nothing else in the object's kit does.

**The missing piece is not three gaps but one operation used three times.** This *strengthens*
the verdict — the shortfall is more economical than the ledger records — and it costs the
`GUT_REQUIREMENTS_LEDGER` a row (§4.2). It also means the verdict's single input is doing more
work than previously recorded: it is the unique source of rank reduction, exotic mass,
anomaly content, **and** the matter/exotic labelling.

### 2.2 The weakening — "the adjoint half" must be scoped to the PATH, not the landing site

L134's second finding is the one thing in Phase A that bites the *positive* half of the verdict.
The A₂+A₁ Levi — the cascade's landing site, the thing the verdict points at — **does not label
matter versus exotic**. Three so(10)s sit above it, they disagree on **18 of 27 states**, and
the residual relative Weyl group is S₃; the Levi alone cannot even tell the lepton doublet from
the two Higgs doublets. What rescues it is that the **first** cascade step already fixes one
so(10) (`Cent(ψ)` = dim 46, and every dim-46 centralizer in e₆ is so(10) ⊕ u(1)), so the
*ordered chain* carries information its *endpoint* has lost.

> **Scope repair owed:** the object supplies the adjoint half **as a path — an ordered chain of
> centralizers — not as its landing site.** Any statement of the verdict that points only at
> `su(3) ⊕ su(2) ⊕ u(1)³` is claiming more resolving power than that algebra has.

This does not threaten the verdict; it corrects how the verdict is stated. It is nonetheless
the single most consequential correction Phase A produced, because the landing site is what
every summary row cites.

### 2.3 The one genuine threat found, and it is to a comfort, not to the verdict

L132's vacuity rests on the spectrum being a union of complete 27s. L134's literature scouting
surfaces Nevzorov 1205.5967: realistic E₆ models must add **extra TeV vector-like matter beyond
complete 27s** for the lightest exotic to decay. If that is right — *carried from the scout,
not re-derived, and it should be verified before it is used* — then any viable phenomenology
built on this object is **not** a union of complete 27s, which is precisely L132's non-vacuity
condition. So:

> **"Complete 27s ⟹ anomaly-free ⟹ nothing to check" is a statement about the OBJECT's
> spectrum, not about any physics built on it. The anomaly layer must not be reported as
> settled — it is vacuous exactly where the object is, and becomes live exactly where physics
> would have to go.**

That is a live successor question, and it is the only one Phase A generated on the SM side.

### 2.4 The mechanism the verdict did not have (V5, computed here)

All 27 weights lie in a single non-trivial class (1/3 mod ℤ) of the ℤ/3 centre grading —
computed at V3/V5, and consistent with B960's banked `ω₁ ∉ root lattice`. Therefore
**27 ⊗ 27 carries centre-charge 2/3 ≠ 0 while the adjoint carries 0, so the 78 does not occur
in 27 ⊗ 27.** Consequences, stated carefully:

- A fermion bilinear inside a single 27 lives in 27 ⊗ 27. **No adjoint VEV can give any 27
  fermion a mass** — mass operators must be cubic (27³, where the centre charges sum to 0),
  which is exactly where L134's `κ S D D̄` was found to live. It had no choice.
- The object's entire operational kit is adjoint-sector (banked: centralizers, rank-preserving).
  **So the kit can give mass to gauge bosons and never to matter** — and it fails to do so
  *because the 27 is complex*, the same fact (27 complex ⟺ τ ≠ id, B963) that blocks rank
  reduction.
- The complementarity is exact: the SM chain needs **27 VEVs** for E₆ → SU(5) (rank 6 → 4) and
  an **adjoint** VEV for SU(5) → SM (rank 4 → 4, no **24** in any 27 branching, B962). The
  object supplies the second kind and not the first. It performs the analogue of the 24-step,
  but starting from rank 6, which is exactly why it ends with three u(1)s instead of one — and
  L134 shows the two extra u(1)s are **ψ and χ**, precisely the charges that distinguish the
  eleven exotics from a generation.

> **One sentence, with mechanism:** *the object's adjoint operations break symmetry without
> ever touching matter mass or matter chirality, because the 27's centre charge excludes the
> adjoint from every fermion bilinear — so the half it cannot supply is not a missing step but
> a missing representation.*

The verdict's second clause ("an input in every theory anyone has") is untouched: nothing in
Phase A derives a 27 VEV, and the literature scouting that supports the clause remains
scouted-not-re-derived, with the live-search null uncertified.

### 2.5 Adversarial check on L138 — does L137's refutation undermine the firing?

It would be a serious problem if L137's "the pencil statistic is gauge-dependent" also
dissolved L138/B969's identification of K. **It does not, and this was computed rather than
argued** (V6): across the pencil's ℚ\* gauge orbit on `s³ − 12s − 5`, coefficient supports take
four/five distinct values while the **discriminant squarefree kernel is {7, 11} at every c**,
and `ℚ(cα) = ℚ(α)`. B969's invariants — the field, the [1,2] splitting type, the √77 kernel —
are exactly the gauge-invariant ones; B947's statistic is not. **L137 retroactively certifies
B969's choice of invariant.** L138's own scope stands unchanged and unweakened: a canonical
*orbit* is not a canonical *VEV*.

---

## 3. CONTRADICTIONS — named, not smoothed

**3.1 The ledger's L134 wording is false as written, in four places.** *"The record has never
addressed them"* / *"not addressed anywhere in the record"* is wrong: `B951`'s
`PRIOR_ART_HYPERCHARGE.md` treats the exotic sector at literature scale (names D/D̄, H_u/H_d, S;
quotes Langacker RMP 81 (2009) 1199 on the diquark/leptoquark → proton-decay constraint), and
`B962`'s `PRIOR_ART_VEV.md` §Q5c does the SU(5)×U(1)_N branching with the D/D̄ pair. Correct
wording: *literature-scouted in B951 + B962; no computed cell until B970.* Affected:
`docs/GUT_REQUIREMENTS_LEDGER.md` §C row 3′, `docs/THE_SM_VERDICT.md` §5 row 2,
`docs/OPEN_LEADS.md` L134, `PROGRESS_LOG.md`.

**3.2 "Twelve exotics" is an arithmetic error in the ledger — and the two Phase A cells then
disagreed with each other.** 10 + 1 = **11**, not 12 (V3, computed). Twelve is right only
against a **15**-fermion generation, i.e. only if ν^c is counted as exotic — which contradicts
the repo's own *"the 16 is one SM generation with a right-handed neutrino."* Both numbers are
correct about different things and the record uses them interchangeably. **And L132's own WORK
then says "the twelve exotics are a real (vector-like) SM rep"** while L134 says eleven. The
substance is unaffected (S is a total singlet contributing 0 to every anomaly coefficient
regardless), but the count must be fixed in both directions.

**3.3 "The exotics are vector-like" is true only at SM granularity, and L134 says the
opposite one level up.** L132: vector-like under SU(3)×SU(2)×U(1)_Y, hence anomaly-invisible.
L134: **ψ-chiral** — `D` and `D̄` both carry ψ = −2, which is *why* a mass needs ψ = +4 and why
`exotic mass ≠ 0 ⟹ U(1)_ψ broken`, rep-independently. Not a contradiction, but a bare
"the exotics are vector-like" in a ledger row would be a scope violation of exactly the kind
the `lawmap-scope` gate was built for. Required phrasing: *vector-like under
SU(3)×SU(2)×U(1)_Y; chiral under U(1)_ψ.*

**3.4 B864 was missed by B951, and B864's headline is narrower than its wording.** L132 found
that `frontier/B864_anomaly_ledger/FINDINGS.md` (2026-08-03) already banked both the vacuity
sentence and *"hypercharge is the unique gaugeable U(1) in the chain's abelian sector"* — a
prior-art miss inside our own corpus, by a cell whose job was prior art. And the uniqueness is
uniqueness **over an imported chiral truncation** (the 15): over the complete 27 the solution
space is 3-dimensional, over the complete 16 it is 2-dimensional and does not separate Y from
χ. The scout further found **156** truncations of the 27 each admitting a unique anomaly-free
u(1). **Scope-note, not retraction:** the selective power lives in the truncation, not in the
anomaly conditions.

**3.5 Three banked statements about the frame are incorrect or stale as written.**
(i) B958's *"the repo contains no independent construction of M12"* — **incorrect**: it
inspected B909 only; B911 had already built it. (ii) B961's *"need solo's definitions stated
precisely enough to rebuild"* — **they were**, in `CMT_DRAFT.md` §2. (iii)
`CMT_DRAFT.md:190`'s W_frame "PENDING" row is **stale** (W_frame is realized in Aut(e₆) at
`B939/assembly.py:349-357`). **And one live code/definition mismatch:**
`frame.py:162-168`'s `su(3)_colour` is **the standard A₂ Levi, not `derived(floor)`**. Both
give dim Z = 16, so B958's dimension-only condition survives — but any finer test must use the
floor's, and conjugacy of the two is *consistent with*, not *proved by*, the equal dimension.

**3.6 B947's SPECIAL verdict stands but its statistic does not survive the object's own gauge
freedom.** The canonical generator of K both **holds** and is **excluded as vacuous** by
B947's own rule, depending on normalisation (confirmed here at V6 for the support statistic).
This does not retract B947 — it scopes it: *B947's pass/fail is a property of a chosen
normalisation of a cubic, not of the locus it describes.*

**3.7 Minor, recorded so it does not become a phantom disagreement.** L134's scout and work
seats swap the `D`/`D̄` letter assignment (all charges agree); L137's scout and work seats give
`|P_lead(T)| ≥ 4, F ≥ 6` and `≥ 5, ≥ 7` respectively (the work refined the bound — both are
lower bounds, and either already decides). **Near-collision to avoid conflating:** L134's
"S = ω₁, the rank-1 element" (a *weight of the 27*) and B960's "ω₁ ∉ E₆'s root lattice"
(a *lattice membership*) are different statements about the same symbol, and V5 shows they are
not merely compatible but the same fact seen twice.

---

## 4. WHAT THE BANKING SEAT MUST DO NEXT — priority order

1. **Repair the verdict's scope (§2.2).** In `docs/THE_SM_VERDICT.md` and every row that
   cites the landing site: the object supplies the adjoint half **as an ordered chain of
   centralizers, not as the algebra it lands on** — the A₂+A₁ Levi alone does not label matter
   versus exotic (18/27 states change side across the three so(10)s above it), while the
   cascade's first step does fix the so(10). Highest priority because the landing site is what
   every summary row points at.
2. **Merge L134 into the 27-VEV row and delete the duplicate gap.**
   `docs/GUT_REQUIREMENTS_LEDGER.md` §C row 3′ and `docs/THE_SM_VERDICT.md` §5 row 2 currently
   count the exotics as an independent requirement. They are the *same* input at the *same*
   step (⟨S⟩ ≠ 0 **is** E₆ → SO(10)). Record the gain: the shortfall is one operation used
   three times, not three gaps.
3. **Fix the four false/incorrect wordings before anything else is written on top of them**
   (§3.1, §3.2, §3.5): "never addressed" → "literature-scouted in B951 + B962, no computed
   cell"; "twelve" → "eleven against the 16, twelve only against a 15"; B958's and B961's
   frame statements; the stale W_frame PENDING row. This is exactly the `retraction-sweep` /
   `lawmap-scope` workflow L139 and L140 installed — use them rather than hand-editing.
4. **Bank L132 as CLOSED-VACUOUS with the B864 prior-art correction on its face** (§3.4), and
   record the non-vacuity condition verbatim as the successor: *L132 acquires content iff
   something deletes states from inside an SO(10) multiplet in a non-vector-like way.* Add the
   B864 scope-note (uniqueness over an imported chiral 15, and the deletion of ν_R is
   undetectable by the very conditions it enables).
5. **Bank L137 as CLOSED-REFUTED, name T, and register no successor.** Add to MB12: *is the
   criterion invariant under the object's own gauge freedom?* Add one sentence to
   `docs/LAW_MAP.md` row 211. Add the B947 scope-note (§3.6). Record the by-product that the
   statistic is not effectively computable on banked cubics.
6. **Bank the L138 shielding result (§2.5, V6)** — the disc squarefree kernel and the field are
   gauge-invariant where coefficient support is not, so L137's refutation does not touch B969.
   This is cheap, it is computed, and without it a reader will assume the opposite.
7. **Bank the L135 rebuild (51/51, two fresh primes) and the new arithmetic fact** — noncompact
   M12 weights in K, compact weights in a proper extension (16/24, scoped to density ½ with
   the extension unidentified) — and record the MB12 catch that ℚ(√77) **cannot** be tested by
   κ-split primes. Downgrade the orbit↔generation bijection from an independent leg to a
   corollary of legs 5+6.
8. **Open the successor cell: char-0 exactification over K** (restriction of scalars, B877 FMT
   recipe). It is the only thing between this bench and a certificate-grade frame, and it
   settles the compact-weight extension as a side effect.
9. **Mark L142 unblocked.** Its stated prerequisite was L135's frame definitions; those are now
   discharged and the instrument is validated at four independent primes. Its discriminating
   test is already named — *exhibit a morphism carrying one pencil to another, or show the
   agreement is only of outputs* — and L137's One-Field corroboration (seven families, 138
   primes, zero mismatches, plus T) makes it sharper, not softer.
10. **Register one new lead from §2.3:** *does the object's spectrum survive contact with a
    phenomenology that is not a union of complete 27s?* Verify Nevzorov 1205.5967's extra-matter
    requirement first — it is carried, not re-derived, and it is the only Phase A finding that
    points at a live anomaly-layer question.
11. **Scout the three-so(10)/S₃ result before banking it as new.** It was computed with no
    literature read and is very likely standard E₆ su(3)³ lore. Bank it as *reproduced* unless
    the scout says otherwise.

---

## 5. HONEST GAPS — what none of the four leads could settle

- **No literature search was reachable in Phase A.** L132's scout exhausted the session budget
  before its cell began; L134's work and L135 read none. Every literature statement in this
  synthesis is either carried from B951/B962's earlier sweeps or from the L134 scout's reading,
  and **the "no prior art" nulls are uncertified**. The three-so(10)/S₃ result and the modern
  collider bounds are the two places where this is load-bearing.
- **Nothing here produces a 27 VEV, and nothing here found a reason one could be produced.**
  Phase A converged four times on the same missing operation and did not weaken it once. The
  verdict is confirmed, which is the least informative possible outcome and must not be
  dressed up as progress.
- **The frame is at prime tier, not certificate tier.** Four independent primes is evidence,
  not a certificate; char-0 over K is a *tier* gap, not a definitional one. The compact-weight
  extension is unidentified, and the one natural guess (ℚ(√77)) is untestable by the method
  that raised the question.
- **Field identity throughout the value layer is Chebotarev evidence, not proof.** `sympy`'s
  `field_isomorphism` returns None and `maximal_order` fails with `CoercionFailed` — the same
  wall B937 documented. Everything that says "the same field K" means "no splitting-type
  mismatch over 128–138 primes."
- **L137's refutation depends on classifying T as a value family.** The argument is given
  rather than assumed, and the alternative classifications are visibly post-hoc — but it is an
  argument, and a seat that wanted to save the split could contest exactly there. It should
  not, but the record should say that it could.
- **Whether the object has *any* operation that deletes states from inside an SO(10) multiplet
  non-vector-likely was not settled** — L132 stated the condition, L133/L136 closed the
  centralizer class, and what remains outside that class (an orbifold projection, or any
  quotient that is not a commutant) is untouched by all four leads.
- **`|P_lead(T)|` and `F(T)` are lower bounds**, and T's 53-digit cofactor was never factored.
  The verdict does not depend on it; the honesty note does.
