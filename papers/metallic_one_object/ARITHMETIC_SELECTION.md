# Why Golden: the arithmetic selection of the metallic once-punctured-torus object

**A draft / status-labelled note.** Dritëro M. (with AI-assisted computation). 2026-06-27.

A companion to *The metallic once-punctured-torus object, seen four ways* (`SYNTHESIS.md`). That note assembles the
**four faces** of the object `φ_m = RᵐLᵐ ∈ SL(2,ℤ)`; this one answers a single question the four-faces picture
raises but does not settle: **why is the golden (`m=1`) member special on every face?** The answer is one
parameter — the metallic discriminant `n = m²+4` — and one elementary congruence. Standalone mathematics; **no
physics; nothing to `../../CLAIMS.md`; the program's physics aims are firewalled and not invoked** (§7).

## 0. Status labels
- **[banked B#/V#]** — established + verified in this repo at the cited stage (tests under `../../tests/`).
- **[literature]** — a known result of the named authors; used, not claimed.
- **[open / NEEDS-SPECIALIST]** — a genuine frontier; flagged, not claimed.

---

## 1. Introduction — the question

The golden mean recurs across every face of the object (`SYNTHESIS.md`): the monodromy field `ℚ(√5)`, the anyon
level `SU(2)₃`, the tricritical-Ising CFT `c=7/10`, the conductor `40=2³·5`, the McKay group `E₈`. The natural
suspicion is a *pile-up of coincidences*. We show it is not: **every appearance traces to the single discriminant
`n=m²+4` at `m=1`, and the few genuinely independent facts about the value `5` are an elementary congruence away
from each other.** The object **selects** golden — and the selection rule is `arithmetic`, not decoration.

## 2. The object and the metallic family

`φ_m = RᵐLᵐ = [[1+m², m],[m, 1]]`, `tr φ_m = m²+2`, a hyperbolic class in `MCG(Σ_{1,1})=SL(2,ℤ)` whose larger
eigenvalue is the `m`-th metallic mean `λ_m=(m+√(m²+4))/2`. The homological monodromy `M_m=[[m,1],[1,0]]` has trace
`m`, `det −1`, characteristic polynomial `x²−mx−1`, discriminant `n=m²+4`. The figure-eight knot complement is
`m=1` **[banked, standard]**. The eigenvalue/trace field is `ℚ(√(m²+4))` **[banked K002]**.

## 3. Why 5 — the trace-1 congruence law (the conceptual backbone)

**The single root.** Tracing every appearance of `5` to `n=m²+4` **[banked B233/B234]**:

| face | where `5` appears | traces to `n=5` via |
|---|---|---|
| golden ratio / monodromy field | `√5`, `ℚ(√5)` | `disc(x²−x−1)=5` |
| anyon level | `SU(2)₃`, `q⁵=1` | `k=n−2=3`, `q=e^{2πi/n}` |
| ordinary / super minimal model | `M(4,5)=SM(3,5)` | `P=n=5`, `q=n=5`, `p=n−2=3` |
| character-variety conductor | `5 ∣ 40` | branch locus `x²=n=5` |
| congruence / McKay | `SL(2,F₅)=2I=E₈` | `p=n=5` |

**The trace-1 congruence law `[banked B234/V—; verified]`.** The object's two arithmetic fields are *one fact with
a sign*. A **trace-1** integer quadratic `x²−x+det` has discriminant `disc = 1−4·det`, which is **always
`≡1 (mod 4)`**. The monodromy `M_1` (`det=−1`) gives `disc 5 → ℚ(√5) → E₈`; the cusp shape (`det=+1`, the figure-
eight tetrahedron `z=e^{iπ/3}` solving `z²−z+1=0`) gives `disc −3 → ℚ(√−3) → E₆`. The two number fields the object
carries are exactly the two **unit determinants** `det = ∓1`.

**The "why-5" verdict — one cascade plus one coincidence (not a pile-up) `[banked B233]`.** Eight of eight `5`-faces
cascade from the single root `n=m²+4=5` (the field `ℚ(√5)`). The *only* genuinely independent fact is that
`min_m(m²+4)=5` is **also** the largest prime `p` for which `SL(2,F_p)` is an exceptional McKay group (`p∈{3,5}`;
`SL(2,F₅)=2I=E₈`). So the recurrence is **one parameter with three properties** — `n=5` is simultaneously the
smallest metallic discriminant, prime (`⟹ SL(2,F₅)=2I=E₈`), and `≡1 (mod 4)` (`⟹ ℚ(√5)` totally real) — not eight
miracles.

## 4. The metallic family table `[banked B235]`

The complete data package, `m=1..6` (`n=m²+4`):

| m | n | minimal model | c | SUSY | trace field | McKay (field / group) | Seifert dual | \|H₁\| |
|---|---|---|---|---|---|---|---|---|
| 1 | 5 | M(4,5) | 7/10 | **yes** | ℚ(√5) | **2I=E₈ (group + field)** | S²(5,4,3) | 83 |
| 2 | 8 | M(7,8) | 25/28 | no | ℚ(√2) | 2O=E₇ (field only) | S²(8,7,3) | 227 |
| 3 | 13 | M(12,13) | 25/26 | no | ℚ(√13) | none | S²(13,12,3) | 627 |
| 4 | 20 | M(19,20) | 187/190 | no | ℚ(√5) | 2I=E₈ (field only) | S²(20,19,3) | 1523 |
| 5 | 29 | M(28,29) | 403/406 | no | ℚ(√29) | none | S²(29,28,3) | 3251 |
| 6 | 40 | M(39,40) | 259/260 | no | ℚ(√10) | none | S²(40,39,3) | 6243 |

The **field-vs-group** distinction is the table's discipline: `m=1` is the only row where the E₈ *group*
`2I=SL(2,F₅)` closes (`n=5` prime) **and** the chain is supersymmetric (`= TCI`); `m=4` carries the E₈ *field*
`ℚ(√5)` (`squarefree(20)=5`) but neither the group nor SUSY; `m=2` carries E₇'s *field* `ℚ(√2)` but never the group
`2O`. Sources: minimal model + SUSY `[B224/B228]`, trace field `[B206]`, Seifert dual `S²(m²+4,m²+3,3)` and
`|H₁|=(2m²+7)²+2` `[B227/B229]`, McKay field/group `[B210/B234]`.

## 5. The boundary — what the object does *not* produce

**E₇ is excluded, and overdetermined `[banked B234]`.** Three independent obstructions each forbid `E₇=2O`:
1. **Group-order (Diophantine):** `|2O|=48 ≠ p(p²−1)`, so `2O` is never a congruence quotient `SL(2,F_p)`.
2. **Representation-theoretic:** `E₇`'s `56` is real (non-chiral) **[literature]**.
3. **Field-congruence:** `2O`'s character field `ℚ(√2)` has `disc 8 ≡ 0 (mod 4)`, but the object (trace-1) reaches
   only `disc ≡ 1 (mod 4)` (§3), so `ℚ(√2)` is unreachable.
These are distinct objects (a group order, a representation, a field discriminant) — not one wall seen three ways.
**Computational confirmation `[banked B237]`:** GAP `GQuotients` finds π₁(silver bundle) carries **no `2O`
quotient** (the `ℚ(√2)` match is field-only); the binary-polyhedral quotient structure is manifold-specific
(golden → `2T=E₆`; silver → `S₄`, the octahedral *rotation* group, never the binary `2O`; bronze → `2T`+`2I`), and
`2O` is absent from all of them.

**A nuance: E₇ *does* appear in the TCI — as a coset algebra `[banked B236]`.** The tricritical Ising model has the
alternative coset realization `(E₇)₁⊕(E₇)₁/(E₇)₂` (c=7/10, verified). So `E₇` has a genuine **coset-algebra** role
*inside* the object's golden CFT, even though `E₇=2O` is excluded from the object's **McKay / congruence-quotient**
arithmetic. This is a different role for `E₇` (coset algebra vs binary-polyhedral group) and does **not** contradict
the exclusion — a worthwhile honest caveat.

**The field ladder closes `[banked B235]`.** The trace-1 ladder's discriminant `1−4det` is realized only at the two
unit determinants (`det=+1→−3`, `det=−1→+5`). The next imaginary rung `ℚ(√−7)` (`det=2`) needs a non-unimodular
element the object does not have; and computationally (SnapPy) every cover of the figure-eight up to degree 6 keeps
the invariant trace field `ℚ(√−3)` (`4₁` is **arithmetic**, Bianchi `PSL(2,O₃)`). So the object's arithmetic is
*closed* on `{ℚ(√5), ℚ(√−3)}` — exactly the two unit determinants — with a reason (unimodularity + arithmeticity),
not an accident.

**The dimensional firewall `[banked K018; B151]`.** No invariant of the object carries a scale: the complex
volume / Chern–Simons class is a dimensionless element of `ℂ/4π²ℤ`; all scale lives in the external quantization
level `k`. The object reaches physics as a *symmetry* (the `SL(2,ℤ)` trace map = the `N=2*` class-S S-duality
action, `[B150]`) and stops at the *scale* wall. This paper claims no physical content.

## 6. Discussion — moonshine, and the specificity filter

**One object-specific moonshine fact `[banked B210]`.** The object's two number fields select two of McKay's three
sporadic-seeding diagrams: `ℚ(√5)→2I=E₈` (Monster) and `ℚ(√−3)→2T=E₆` (Fischer), excluding `E₇` (Baby Monster).
This is the object's *actual arithmetic*, so it is a genuine selection.

**A generic rhyme, correctly demoted `[banked B234]`.** The object's golden/Fibonacci `SU(2)₃` data also appears as
Fibonacci defect lines in the Conway SCFT (Angius et al., arXiv:2512.19640) — **but** the Fibonacci fusion category
is *unique* (one F-matrix up to gauge), so every Fibonacci system carries it; this is **Fibonacci ubiquity, not an
object↔Conway connection.** It is an instance of "golden = the minimal nontrivial structure, hence everywhere."

**The specificity filter (the method) `[banked B234/H28]`.** The discriminator that separates the two: sweep `m`.
An overlap is *object-specific* only if it survives the sweep — `golden-specific` (only `m=1`: SUSY, `n=5`),
`object-specific` (only `{ℚ(√5),ℚ(√−3)}`: the dual McKay), or `universal` (no `m`-dependence: the Fibonacci
category) — the last is a rhyme and is demoted on sight. The exceptional-group footprint is **3/5** (G₂ = Fibonacci
`(G₂)₁`, E₆, E₈; E₇ excluded; **F₄ retracted** — no `SU(3)_k ⊂ (F₄)₁` conformal embedding, `c(SU(3)_k)≠26/5`)
`[B235]`.

**A quantum-topology instance of the same `5` `[banked B238]`.** Under level-rank duality `SU(2)₃ ↔ SU(3)₂` (shared
`κ=k+N=5`, the golden cyclotomic; `c`-sum `=5=c(SU(6)₁)`), the closed figure-eight-bundle WRT invariant **coincides**
`Z(4₁;SU(2)₃)=Z(4₁;SU(3)₂)=−1/φ` — but **only** at the figure-eight: silver (`RRLL`) and bronze (`RRRLLL`) give
*different* SU(2)/SU(3) traces. So the level-rank coincidence is itself **golden-specific**, again rooted in the
shared `κ=5` — one more entry in the "`5`" table, on the quantum face.

**The coset-coincidence mechanism — references found, verified `[banked B236]`.** The ordinary GKO coset
`M(m,m+1)=(SU(2)_{m-2}×SU(2)_1)/SU(2)_{m-1}` and the super coset `SM_k=(SU(2)_k×SU(2)_2)/SU(2)_{k+2}` (Lashkevich,
hep-th/9301093) **coincide as the same coset `(SU(2)_1×SU(2)_2)/SU(2)_3` uniquely at the TCI** — verified by central
charges and a uniqueness sweep (the only such `(m,k)` is `(4,1)`). The uniqueness *fact* (TCI both conformal and
superconformal) is Qiu 1986 (via Johnson–Clifford); the two coset formulas appear separately in the literature; the
**mechanistic observation** that the coincidence *is* the two cosets being equal at `SU(2)₃` is, to our search, not
stated as a proposition — so it is offered as a **modest original organizing observation**, not a deep theorem.
*(Resolves the earlier `NEEDS-SPECIALIST` gate; the remaining residue is only whether a specialist deems the
mechanism "obvious.")*

## 7. Firewall and what is not claimed

The **form** side only (scale-free character-variety / arithmetic / fusion-category mathematics). No claim that the
object *is* heterotic / F-theory / NCG / a moonshine module, or that it *produces* the Standard Model, a gauge
group, or a scale. McKay `E₆/E₇/E₈` are representation-theoretic, not physics. No `[proved]` on any physics reading;
nothing promotes to `../../CLAIMS.md`; `P1–P16` are untouched. The one-way firewall (`../../ARCHITECTURE.md`) holds:
this note cites the proven mathematics; the mathematics never cites back.

## 8. References
- **The object / four faces:** `SYNTHESIS.md` (this folder) + its references (Fricke–Vogt; Goldman; Cantat 2009;
  Suto; Damanik–Gorodetski; Jeffrey 1992).
- **Arithmetic selection (this note):** in-repo `B206` (trace fields), `B210` (dual McKay), `B224/B228` (SUSY
  uniqueness), `B227/B229` (Seifert duals), `B233` (why-5 cascade), `B234` (trace-1 congruence law, specificity
  filter, E₇ overdetermination), `B235` (the table, the `ℚ(√−7)` closure, the F₄ retraction).
- **Literature:** McKay correspondence (`2T/2O/2I ↔ E₆/E₇/E₈`); Dechant (arXiv:1603.04805) + Arnold (trinities);
  Fominykh et al. (arXiv:1502.00383, `4₁` trace field); Qiu 1986 / Johnson–Clifford (hep-th/0311129); Feiguin et
  al. (cond-mat/0612341, golden chain → TCI); Ostrik (Fibonacci-category uniqueness).
