# From a minimal self-referential object to a unique superconformal anyon chain

**A draft (motivated, status-labelled).** Dritëro M. (with AI-assisted computation). 2026-06-27.

**Status labels.** **[banked B#]** — established + verified in this repository (tests under `../../tests/`).
**[lit]** — a known result of the cited authors; used, not claimed. **[open / NEEDS-SPECIALIST]** — a genuine
frontier, flagged not claimed. No physical claim is made anywhere; nothing here promotes to `../../CLAIMS.md`.

---

## 1. Motivation

This work began with a philosophical question — *what is the minimal departure from "nothing," the smallest
self-referential structure, and what mathematics does it force?* — and with a small wonder that it kept answering
in the vocabulary of fundamental physics: the exceptional Lie algebras `E₆` and `E₈`, the Fibonacci anyon, and an
emergent `N=1` superconformal symmetry. We keep that motivation in view on purpose. **The theorems below are
purely mathematical and stand entirely independent of it; we state the motivation openly precisely so it can be
held separate from the claims — that separation, not its suppression, is the discipline of this paper.**

The honest form of the starting point: the golden ratio `φ = (1+√5)/2` is *a* canonical minimal self-referential
fixed point — the attracting fixed point of `x ↦ 1 + 1/x`, the "most irrational" number (continued fraction
`[1;1,1,…]`), and the fundamental unit of the simplest real quadratic field `ℚ(√5)`. It is not "the unique simplest
self-referential relation" (the equation `x=1/x` is simpler, if trivial); it is the simplest one carrying a
nontrivial attracting dynamic, and that minimality is what we follow.

The rest of the paper traces the mathematics this object determines, identifies the one place where the golden case
is genuinely selected from its family — *the golden mean is the unique metallic mean whose anyon chain is
superconformal* — and gives a disciplined criterion that separates such object-specific selection from the kind of
generic "the number 5 is everywhere" coincidence that would, rightly, read as numerology. The recurrence of `E₆`,
`E₈`, and `N=1` SCFT is a structural **rhyme** with physics, stated as such; the boundary at which it stops (no
physical scale) is stated precisely in §5.

## 2. The object: metallic once-punctured-torus bundles

For each positive integer `m`, the **metallic mean** `λ_m = (m+√(m²+4))/2` is the larger eigenvalue of
`M_m = RᵐLᵐ ∈ SL(2,ℤ)`, with `R=(¹₀¹₁)`, `L=(¹₁₀¹)`. The mapping torus of the induced automorphism of the
once-punctured torus is a cusped hyperbolic 3-manifold — the **metallic bundle**. At `m=1`: `λ₁=φ`, `M₁=RL`, and
the bundle is the figure-eight knot complement `S³∖4₁` (the simplest hyperbolic knot complement by volume, and the
unique arithmetic knot complement [lit: Reid; Maclachlan–Reid]). The discriminant `n=m²+4` governs the quantum
topology: the `SU(2)` Chern–Simons level is `k=n−2`, the root of unity `q=e^{2πi/n}`.

**Four faces (context).** The figure-eight is studied through four lenses — (I) algebraic geometry: its non-abelian
`SL(2,ℂ)` character variety is the elliptic curve **40a1** (conductor `2³·5`, non-CM, rank 0) **[banked B211]**;
(II) hyperbolic geometry: volume `2.0299…`, invariant trace field `ℚ(√−3)`, two ideal tetrahedra of shape
`e^{iπ/3}` **[lit]**; (III) quantum topology: the Fibonacci `=SU(2)₃/(G₂)₁` modular data, `d_τ=φ` **[lit]**; (IV)
representation theory: the dual McKay `E₆+E₈` (§3). Three of these four are already unified in one reference
(**Cantat 2009** [lit: arXiv:0711.1727], the character-variety trace map = the dynamical degree = the
Fibonacci-Hamiltonian spectral map); the contribution here is not the dictionary but the **selection** result and
its criterion (§3–§4). See the companion `SYNTHESIS.md` for the four-face map in full.

## 3. The selection theorem

### 3.1 The coset coincidence, and why golden is unique

The golden/Fibonacci `SU(2)₃` anyon chain (antiferromagnetic) flows in the infrared to the tricritical Ising model
`M(4,5)`, `c=7/10` **[lit: Feiguin–Trebst–Ludwig–Affleck–Kitaev–Wang–Freedman 2007]** — which is also the first
unitary `N=1` **superconformal** minimal model `SM(3,5)`. So the golden chain has emergent `N=1` superconformal
symmetry (the `h=3/2` supercurrent appears in the finite-size spectrum; the SUSY is emergent, not a lattice
grading) **[banked B221/B222/B223]**.

The mechanism is a coincidence of two coset constructions:
- ordinary **[lit: Goddard–Kent–Olive 1986]**: `M(p,p+1) = (SU(2)_{p−2}×SU(2)_1)/SU(2)_{p−1}`;
- super **[lit: Lashkevich, hep-th/9301093]**: `SM_k = (SU(2)_k×SU(2)_2)/SU(2)_{k+2}`.

At `(p,k)=(4,1)` these are **literally the same coset** `(SU(2)_1×SU(2)_2)/SU(2)_3`, `c=7/10` — verified by central
charges, and unique over a sweep: `(4,1)` is the only pair with matching coset data **[banked B236]**. The
metallic chain at index `m` flows to `M(m²+3, m²+4)` with GKO denominator `SU(2)_{m²+2}`; the coincidence requires
`m²+2 = 3`, whose **unique** positive-integer solution is `m=1`.

> **Theorem (selection).** Among the metallic anyon chains `{RᵐLᵐ}_{m≥1}`, the golden case `m=1` is the unique one
> that is `N=1` superconformal — because `m²+2=3 ⟺ m=1`. **[banked B224/B228/B236]**

The uniqueness *fact* (that the tricritical Ising model is the unique minimal model that is both ordinary-conformal
and superconformal) is standard, traceable to Friedan–Qiu–Shenker [lit: 1985] and Qiu [lit: 1986] — a corollary of
the ordinary series `c=1−6/(q(q+1))` and the super series `c=(3/2)(1−8/(p(p+2)))` overlapping only at `c=7/10`. The
two coset formulas appear **separately** in the literature (ordinary: GKO 1986, Lässig 1991; super: Lashkevich
1993). We offer the observation that the coincidence *is* the two cosets being the **same coset** at `SU(2)₃` as a
**modest organizing proposition** — and we have checked it (a by-hand read, §6): Lashkevich's super-coset paper
makes no reference to the ordinary GKO coset, no comparison, and no tricritical-Ising discussion (its own "unusual"
decomposition is the *different* `SM_k∼(M_k×M_{k+1})/M_1`); we found the same-coset statement nowhere. It is
plausibly unstated, though near-obvious once both cosets are written — so we claim it only as organizing, not as a
theorem.

### 3.2 The arithmetic backbone: a unimodular trace-field law

The figure-eight carries two number fields, and they are one fact with a sign. Its holonomy/monodromy elements are
**unimodular** (`det=±1`); for trace `t` the characteristic polynomial is `x²−tx+det`, discriminant `t²−4·det`.

- **`ℚ(√5)` is robust** (not a "trace-1" accident): the bundle monodromy `RL=(²₁¹₁)` has trace **3**, `det+1`,
  `disc 5`; the homological monodromy `M₁=(¹₁¹₀)` has trace 1, `det−1`, `disc 5` — both give `ℚ(√5)`.
- **The only imaginary quadratic trace fields a unimodular element can have are `ℚ(i)` and `ℚ(√−3)`:** `disc<0`
  forces `det=+1`, `|t|≤1`, so `disc ∈ {−4 (t=0 → ℚ(i)), −3 (t=±1 → ℚ(√−3))}` — a **`disc=−4` floor**. The
  figure-eight's geometry sits at `ℚ(√−3)` (`z=e^{iπ/3}`, `z²−z+1=0`); the *only* other point is `ℚ(i)`, exactly
  the Whitehead/Borromean parent that supplies the prime 2 of the conductor `40=2³·5` **[banked B239/B225]**.

Via the McKay correspondence, `ℚ(√−3)=ℚ(ω₃)` is the character field of `2T=SL(2,F₃)` (`↔E₆`) and `ℚ(√5)=ℚ(φ)` that
of `2I=SL(2,F₅)` (`↔E₈`). So the object carries the **dual McKay `E₆+E₈`** [banked B210]. The octahedral
`2O` (`↔E₇`) is **overdetermined-excluded** (§5.2).

### 3.3 Why "5" — one cascade, not a pile-up

Every appearance of `5` traces to the single discriminant `n=m²+4=5` at `m=1`: the field `ℚ(√5)`, the level
`k=n−2=3`, the root of unity `q=e^{2πi/n}`, the models `M(4,5)=SM(3,5)`, the congruence quotient `SL(2,F₅)=2I=E₈`,
and the conductor's 5-part. The genuinely independent fact is that `n=5` is *simultaneously* the smallest metallic
discriminant, prime, `≡1 (mod 4)` (so `ℚ(√5)` is real), and equal to `4+1` (the ordinary–super overlap index) —
these are algebraic consequences of `n` being the smallest metallic discriminant that is prime, not five separate
miracles **[banked B233]**. This is exactly the kind of "5 everywhere" observation that needs the discipline of §4
to be a *result* rather than numerology.

## 4. The specificity filter, and controls

### 4.1 The filter (the methodological contribution)

A framework coincidence is informative only if it is **specific to the object**, and specificity is *measurable*:
sweep the metallic parameter `m` and ask what survives **[banked B234]**.
- **Universal** (holds for all `m` / no `m`-dependence) → a ubiquity rhyme, demoted on sight. *Example:* the
  Fibonacci fusion category is unique, so it appears in *every* Fibonacci system (Read–Rezayi, `(G₂)₁`, Yang–Lee,
  and the Conway SCFT [lit: Angius et al. 2025]) — its appearance anywhere is not a connection to *this* object.
- **Object-specific** (lives only in `{ℚ(√5), ℚ(√−3)}`) → a genuine selection: the dual McKay `E₆+E₈`.
- **Golden-specific** (survives only at `m=1`) → the sharpest: the superconformal selection (§3.1), and the
  coincidence `n=5`.

The filter is the project's answer to the numerology charge: it is a stated criterion, applied uniformly, under
which most "5 everywhere" observations are demoted and only the selection survives.

### 4.2 The metallic table (controls)

| m | n=m²+4 | model | c | SUSY | trace field | McKay (field / group) | Seifert | \|H₁\| |
|---|---|---|---|---|---|---|---|---|
| 1 | 5 | M(4,5) | 7/10 | **yes** | ℚ(√5) | **2I=E₈ (group + field)** | S²(5,4,3) | 83 |
| 2 | 8 | M(7,8) | 25/28 | no | ℚ(√2) | 2O=E₇ (field only) | S²(8,7,3) | 227 |
| 3 | 13 | M(12,13) | 25/26 | no | ℚ(√13) | — | S²(13,12,3) | 627 |
| 4 | 20 | M(19,20) | 187/190 | no | ℚ(√5) | 2I=E₈ (field only) | S²(20,19,3) | 1523 |
| 5 | 29 | M(28,29) | 403/406 | no | ℚ(√29) | — | S²(29,28,3) | 3251 |
| 6 | 40 | M(39,40) | 259/260 | no | ℚ(√10) | — | S²(40,39,3) | 6243 |

SUSY is `m=1` only (`m²+2=3`). **[banked B235]**

**Field vs group (the discipline that defeats "5-worship").** The McKay column distinguishes a *field* match from a
*group* quotient. At silver (`m=2`), `ℚ(√2)` matches `2O`'s character field, but `π₁(silver bundle)` carries **no
`2O` quotient** (GAP `GQuotients`); its largest binary-polyhedral quotient is `S₄`, the octahedral *rotation*
group, not the binary `2O` **[banked B237]**. At `m=4`, `ℚ(√5)` matches `2I`'s field but the group does not close
(`n=20` not prime). Golden is the unique metallic member where `E₈` holds at **both** field and group level —
because `n=5` is prime.

**A false positive, rejected (controls cut both ways).** The ferromagnetic chain flows to the `Z_k` parafermion
CFT; a naive central-charge test flags silver-FM (`c=5/4`) as the super model `SM(6)` — but these are different
cosets (`SU(2)_6/U(1)` vs `(SU(2)_4×SU(2)_2)/SU(2)_6`), a `c`-coincidence not a CFT identity. The coset criterion
(§3.1) correctly rejects it, so the superconformal selection is robust to the AFM/FM choice **[banked B230]**.

### 4.3 A quantum-topological confirmation

Under level-rank duality `SU(2)₃ ↔ SU(3)₂` (shared `κ=k+N=5`; `c`-sum `9/5+16/5=5=c(SU(6)_1)`, the conformal
embedding), the closed figure-eight bundle's WRT invariant coincides: `Z(4₁;SU(2)₃)=Z(4₁;SU(3)₂)=−1/φ`. This is
**figure-eight-specific** — silver and bronze give different `SU(2)`/`SU(3)` invariants — and is rooted in the
shared golden `κ=5`. (Another golden-specific instance, on the quantum face.) **[banked B238]**

### 4.4 Golden integrality of the colored Jones — the filter at its sharpest

At the golden root `q=e^{2πi/5}`, the figure-eight's colored Jones `J_N`, weighted by the `SU(2)₃` quantum
dimension `[N]={1,φ,φ,1}`, is a vector of **integers**:
> `[N]·J_N(4₁; e^{2πi/5}) = {1, −2, −2, 1}` (N=1..4) — the `φ` cancels the `1/φ` in `J_N={1,−2/φ,−2/φ,1}`.

The mechanism is exact: `J_2 = 1−4\sin(π/5)\sin(3π/5)`, and `\sin(π/5)\sin(3π/5)=√5/4` (special to `n=5`, where the
cyclotomic field collapses to the quadratic `ℚ(√5)`) gives `J_2=1−√5=−2/φ`. **Golden-specific:** the other
metallic roots `n=8,13` give non-integers. **[banked B240]**

This is the specificity filter (§4.1) in its cleanest form, because the result *resolves into two tiers* under a
sweep of amphicheiral knots (a validated `U_q(sl₂)` R-matrix colored Jones; integrality decided rigorously by the
Galois action `√5↦−√5`):
- **amphichirality ⇒ real, in `ℤ[φ]`** — a property of the whole *class* (Habiro integrality intersected with the
  real field). Chiral knots (`3₁,5₂`) instead give non-real values in `ℚ(ζ₅)`.
- **the `√5`-part vanishing (pure `ℤ`) ⇒ figure-eight-specific** — among the amphicheiral knots through 10
  crossings with braid index ≤5 (`6₃,8₉,8₁₂,8₁₇,8₁₈,10₁₇`), **only `4₁`** is pure-integer; e.g. `8₁₈=(σ₁σ₂⁻¹)⁴`,
  which lies in the figure-eight's *own braid family* (`4₁=(σ₁σ₂⁻¹)²`), gives `−8+7φ`.

So the filter does exactly its job: it tells apart a generic class trait (real-valuedness, shared by all
amphicheiral knots) from the genuinely object-specific fact (pure integrality, the figure-eight alone). *(The
companion observation `Σ[N]·J_N = −2 = −χ` of Slavich's bounding 4-manifold is HELD/unverified — the raw sum is not
the normalized WRT invariant — and is not used here.)*

### 4.5 Three SU(3)'s, three faces — and what unifies the quantum one with amphichirality

The figure-eight carries **three distinct objects** that all read "SU(3)", one on each of three faces, and keeping
them apart is itself an instance of the discipline (§4.1): **(1)** the **SL(3,ℂ) character variety** (classical
geometry — `Fix(T₁²)`: three components of dimension 2, the geometric `Sym²` plus two Dehn-filling components)
**[banked B71]**; **(2)** the **level-rank gauge `SU(3)₂`** (quantum — a Chern–Simons group at level 2, dual to
`SU(2)₃` with shared `κ=5`) **[banked B238]**; **(3)** the **Gang–Yonekura flavor `SU(3)`** (a global flavor
symmetry of the 3d `N=2` theory `T[K]`, *universal across all hyperbolic twist knots*, from the `A₁` theory)
**[lit: arXiv:1803.04009; B241]**. These differ in *type* (variety / number / symmetry) and *specificity*
(golden / golden / twist-universal): (1)↔(2) are classical and quantum descriptions of the same SL(3) structure
(quantization; volume conjecture as `k→∞`), while (3) is genuinely separate — so the recurrence of "SU(3)" is
three objects, not one (a further check that the rhyme with the Standard-Model gauge group, §5.4, is not an
identification).

One clean relation closes the loop with §4.4. The fundamental `SU(N)_k` knot invariant is `HOMFLY(a=qᴺ, z=q−q⁻¹)`,
and the level-rank duality `SU(2)₃↔SU(3)₂` sends `a=qᴺ↦a=q^{5−N}=−q^{−N}`, i.e. `a²↦\overline{a²}` at `q=e^{iπ/5}`
— **the duality acts as complex conjugation.** Hence the two invariants coincide *exactly* iff the value is real
iff the knot is **amphicheiral**: for `4₁` (amphicheiral) `SU(2)₃=SU(3)₂=−2/φ`, while chiral knots give complex-
conjugate pairs. So *amphichirality is precisely the condition that makes the level-rank coincidence exact* —
binding the §4.4 amphichirality theme to the §4.3/B238 level-rank theme. **[banked B242]**

## 5. The boundary

### 5.1 The dimensional firewall

The selection terminates at **emergent 2d `N=1` superconformal symmetry** — a symmetry of a critical 1+1d lattice
model, **not** 3+1d spacetime supersymmetry. Every invariant in the chain is dimensionless (central charges,
quantum dimensions, discriminants, WRT invariants). No physical scale (mass, length, `Λ`) is produced: this is
structural, not a gap to be closed — topological invariants of 3-manifolds are dimensionless by construction (the
complex volume / Chern–Simons class is a dimensionless element of `ℂ/4π²ℤ`; all dimensionful content of the 3d–3d
correspondence lives in `ℏ↔k` and the squashing radius) **[banked B151/K018; lit: Gukov–Teschner–Zagier;
Dimofte; Córdova–Jafferis]**.

### 5.2 `E₇` is overdetermined-excluded

Three independent mechanisms each forbid `2O` (`↔E₇`):
1. **Group-order:** `|2O|=48 ≠ p(p²−1)`, so `2O` is never a congruence quotient `SL(2,F_p)`.
2. **Representation-theoretic:** `E₇` has **no complex representations** (`w₀=−1` ⟹ every irrep self-dual); its
   `56` is **pseudoreal** (Frobenius–Schur `−1`, symplectic — `E₇⊂Sp(56)`, Sage-verified **[banked B234]**), so it
   gives no chiral matter — the heterotic `E₇`-skip, from an independent direction.
3. **Trace-parity:** `2O`'s field `ℚ(√2)` has `disc 8 ≡ 0 (mod 4)`, requiring **even** trace (`t=±2` = silver
   `M₂`); the object's elements are odd-trace (`disc ≡ 1 mod 4`), so `ℚ(√2)` lives at silver/even-`m`, not here.

These act on different objects (a group order, a representation's reality, a field discriminant) — not one wall
seen three ways. **An honest caveat:** `E₇` *does* appear in the TCI itself, via the coset
`(E₇)_1⊕(E₇)_1/(E₇)_2` (`c=7/10`, verified **[banked B236]**) — a coset-algebra role, distinct from the
McKay/congruence role from which it is excluded; no contradiction.

### 5.3 The imaginary field ladder closes

By §3.2, a unimodular element's only imaginary quadratic trace fields are `ℚ(i)` and `ℚ(√−3)` (the `disc=−4`
floor); `ℚ(√−7)` (`disc −7`) is **below the floor**, unreachable. Computationally, every cover of `4₁` up to
degree 6 keeps invariant trace field `ℚ(√−3)` (`4₁` is arithmetic, Bianchi `PSL(2,O₃)`) **[banked B235]**. With
the real field `ℚ(√5)`, the dual McKay `E₆+E₈` **exhausts** the object's quadratic fields.

### 5.4 What is not claimed

That the selection produces a physical theory (gauge group, matter, `Λ`, equations of motion); that the `E₆+E₈`
McKay is the heterotic `E₈→SU(3)×E₆` breaking (same algebra, different role — a rhyme, not an identification); that
the emergent 2d SUSY crosses to 3+1d; that `5` has physical significance beyond its role as the metallic
discriminant. The claim is the selection theorem (§3.1), its arithmetic backbone (§3.2), and the criterion (§4)
that makes the recurrence a result rather than a coincidence.

## 6. Horizon (firewalled)

We keep the horizon visible — the motivation's honest endpoint — under the repository's one-way firewall: a
speculation → calculation table, where each lead is either computed to a verdict or flagged. Nothing here is a
claim; nothing crosses to scale.

| lead | the test | verdict |
|---|---|---|
| Kodama state level `k=3` sets `Λ`? | `k=6π/(GΛ)` at `k=3` | **HELD negative [banked]** — `Λ≈2π/l_P²` (Planck-scale); the observed `Λ` needs `k≈6.5×10¹²²`; scale lives in `k`, not the invariant. A *measured* firewall confirmation, not a lead — the ~10¹²² gap is near-tautological (any UV/IR ratio). |
| twist-knot `SU(3)` ↔ our level-rank `SU(3)₂`? | is the Gang–Yonekura twist-knot `SU(3)` the §4.3 `SU(2)₃↔SU(3)₂` dual? | **[resolved — distinct, B241]** No: Gang–Yonekura's [arXiv:1803.04009] is a global *flavor* symmetry of `T[K]`, **universal** across all hyperbolic twist knots; ours is a CS *gauge* level-rank dual, **figure-eight-specific** (golden, `κ=5`). Different type *and* specificity — within the twist family only `4₁` (the unique amphicheiral one) carries the golden structure. A clean distinction, not a bridge (and a further deflation of the SM-rhyme: even the two SU(3)'s do not unify). |
| a 4-manifold from the figure-eight's flat connections? | Slavich's hyperbolic 4-manifold bounded by `4₁` × the `SL(2,ℂ)` CS / 4-simplex constructions on `40a1` | **[open — mathematics, NEEDS-SPECIALIST]** left to specialists; no scale is asserted. |
| does any external framework feature the object's *specific* structures? | the specificity filter (§4) vs heterotic / F-theory / NCG / moonshine | **[banked]** every overlap is a structural rhyme; the firewall holds (`S041`). The one object-specific moonshine fact: the dual McKay `E₈+E₆` selects Monster + Fischer, excludes the Baby Monster. |

**The literature gate (now read).** §3.1's "modest organizing proposition" was the one item needing a by-hand
read. Done: the uniqueness *fact* is standard (FQS 1985 / Qiu 1986); the two cosets appear separately; and the
load-bearing paper (Lashkevich 1993, read in full) makes no reference to the ordinary GKO coset and no TCI
discussion. The same-coset observation is found stated nowhere — plausibly unstated but near-obvious — so it is
offered as organizing, not as a theorem (and the misattributed "Qiu via hep-th/0311129" citation is corrected to
FQS 1985 / Qiu 1986 directly). The mechanism itself is computationally closed (B236). **No open gate remains**;
everything above is verified and banked.

## References (by role; standard in the area)
Maclachlan–Reid, Reid (figure-eight arithmetic / unique arithmetic knot); Cantat 2009, Goldman, Fricke–Vogt
(character-variety trace map); Süto, Damanik–Gorodetski (Fibonacci-Hamiltonian); Jeffrey 1992 (WRT of torus
bundles); Habiro (cyclotomic expansion / integrality of the colored Jones); Feiguin–Trebst–Ludwig et al. 2007
(golden chain → TCI); Goddard–Kent–Olive 1986, Lashkevich hep-th/9301093 (cosets), Friedan–Qiu–Shenker 1985 / Qiu
1986 (the TCI as the unique ordinary+superconformal minimal model); McKay (the correspondence); Gukov–Teschner–
Zagier, Dimofte, Córdova–Jafferis (3d–3d / complex CS); Gang–Yonekura arXiv:1803.04009 (twist-knot flavor `SU(3)`),
Naculich–Schnitzer / arXiv:2106.15012 (level-rank duality of knot invariants). In-repo provenance: B210, B211,
B221–B224, B228, B230, B233–B242 (and `SYNTHESIS.md`, `ARITHMETIC_SELECTION.md`, `S041`).
