# B951 — Prior-art scouting report for L132

**Cell scouted:** L132 (registered, NOT yet run). The object's "second measurement"
yields `su(3) ⊕ su(2) ⊕ u(1)³` (dim 14, rank 6) inside an E₆ structure. The seat
intends to ask whether the object's charges satisfy the Standard Model
anomaly-cancellation conditions, and whether the correct hypercharge Y falls out —
including a principled identification of *which* u(1) in the rank-3 abelian sector
is hypercharge.

**Prepared by:** the scouting panel (adversarial prior-art seat).
**Status:** scouting report on a literature the seat is about to walk into.
This is **not** a novelty audit of a result.

---

## BOTTOM LINE UP FRONT

Three facts, verified in-sandbox, govern everything below.

1. **`su(3) ⊕ su(2) ⊕ u(1)³` is a Levi subalgebra of e₆** — precisely the
   centralizer in e₆ of a 3-dimensional torus. Verified by explicit root-system
   computation (72 roots; the A₂+A₁ node-subsets each give an 8-root subsystem,
   8 + 6 Cartan = 14). Arriving at this algebra from E₆ is classified structure
   (Borel–de Siebenthal 1949; Dynkin 1952), and is the standard rank-6 GUT chain.

2. **E₆ is anomaly-safe.** It has no symmetrised third-order Casimir, so it is
   anomaly-free as a gauge group (Georgi & Glashow 1972; Okubo 1977 names E₆
   explicitly). **Consequence, verified in-sandbox:** for a *complete* **27**,
   every U(1) in the rank-3 abelian sector, every mixed cubic combination, the
   gravitational conditions, `[SU(3)]²U(1)`, `[SU(2)]²U(1)`, and the Witten
   SU(2) parity all vanish **identically** (see §Q4.0). If the object's charges
   come from complete **27**s, *the anomaly check cannot fail.*

3. **The centralizer condition does not single out Y in E₆.** The centralizer of
   `su(3) ⊕ su(2)` in `su(5)` is 1-dimensional — this is the textbook
   Georgi–Glashow identification of hypercharge. But the centralizer of
   `su(3) ⊕ su(2)` in **e₆** is **9-dimensional** (`su(3) ⊕ u(1)`), verified
   in-sandbox. So "the u(1) that commutes with colour and isospin" is *not* a
   definition of Y inside E₆. An extra input is required, and in the literature
   that input is always the choice of the SU(5) (or SO(10)) subgroup.

**Therefore:** the anomaly half of L132 is at high risk of being vacuous, and the
"algebra arrives" half is textbook. The only place novelty can live is a
*principled, stated-in-advance* selection of which u(1) is Y.

---

## SEARCH RECORD

### Databases actually reached

| Database | Endpoint | Reached? | Use |
|---|---|---|---|
| INSPIRE-HEP | `inspirehep.net/api/literature` | **Yes** — primary | Q1/Q2 citation-graph closure; `a`/`t`/`refersto recid` query syntax |
| arXiv | `export.arxiv.org/api/query` | **Yes** | verbatim abstracts (7 key papers by id_list) |
| ar5iv full text | `ar5iv.labs.arxiv.org/html/<id>` | **Yes** | full text of Langacker RMP 81 (2009), Todorov 2021, Todorov 1911.13124 |
| OpenAlex | `api.openalex.org/works` | **Yes** | cross-check sweep on Q3, citation counts |
| zbMATH | `api.zbmath.org/v1/document/_search` | **Yes** (returned records) | spot-check only; not load-bearing |
| Semantic Scholar | `api.semanticscholar.org/graph/v1` | **Reached, unusable** — returned `total: None` with no `data` array for the test query | **not relied upon** |
| MathSciNet | `mathscinet.ams.org/.../search` | **NO — HTTP 302 to authentication wall** | **not consulted; no claim rests on it** |

### Method

Per the standing lesson that keyword ranking is near-worthless on this topic,
the primary instrument was **citation-graph closure**: pick the paper the
community must cite, get its INSPIRE recid, enumerate the complete citing set
with `refersto recid <n>`, and read titles/abstracts individually.

### Control (must-pass)

**PASSED.** The method found the canonical anomaly-fixes-hypercharge results
without being told their titles:

- `a Geng and a Marshak` → **Geng & Marshak, PRD 39 (1989) 693** (recid 24389,
  170 citations) — the target control.
- `refersto recid 24389` → enumerated all **170** citing works, which returned
  the entire Q1 cluster in one pass: Minahan–Ramond–Warner, Babu–Mohapatra,
  Foot–Joshi–Lew–Volkas, Rudaz, Golowich–Pal, Hucks, Nowakowski–Pilaftsis,
  Sladkowski–Zralek, Lohitsiri–Tong, Costa–Dobrescu–Fox, Batra–Dobrescu–Spivak,
  Ibáñez.

**Second control (Q2 axis), also PASSED.** The method independently surfaced the
canonical E₆ vocabulary by citation weight: London & Rosner (487), Hewett & Rizzo
(1524), Langacker Z′ review (1544), Slansky (1466), Gürsey–Ramond–Sikivie (871).

Both nulls reported below are therefore meaningful *as far as the searched
corpus goes* — see the honesty caveat in §Q3.

### Noise note

OpenAlex keyword queries surfaced several apparently machine-generated preprints
with zero citations ("Paper CCCXVIII: The OOB Gauge Group…", "Self-Reconstructing
Codazzi Defects…"). These are **not** treated as prior art and are recorded here
only so a later reader does not mistake their absence for an oversight.

---

## Q1 — To what extent does anomaly cancellation FIX the SM hypercharges?

### The short answer

It fixes the **ratios** of hypercharges, **up to normalisation**, **for one
generation**, **given exactly the SM representation content**, and even then the
minimal-content result admits a **second, non-standard solution** that must be
excluded by an extra assumption. At three generations with massless neutrinos the
forcing **fails outright**.

### What each source actually establishes, and under what assumptions

**Geng & Marshak, PRD 39 (1989) 693** (recid 24389, 170 cites) — *"Uniqueness of
quark and lepton representations in the standard model from the anomalies
viewpoint."*
Establishes: the minimal Weyl representations **and their charges** are uniquely
determined by three conditions — (1) triangle anomaly cancellation, (2) absence
of the global SU(2) (Witten) anomaly, (3) the mixed gauge-gravitational anomaly.
Assumptions: *minimal* Weyl representation content; the analysis is conducted
*prior to* spontaneous breaking of the electroweak subgroup; effectively one
generation / family-universal Y. **The mixed gauge-gravitational condition is
load-bearing** in this derivation (it is what pins the quark/lepton hypercharge
ratios).

**Minahan, Ramond & Warner, PRD 41 (1990) 715** (recid 279403, 96 cites) — the
key caveat, and the one most often forgotten.
Establishes verbatim: *"In the absence of any reference to Higgs particles,
anomaly cancellation, including the mixed gravitational anomaly, among the
standard-model fermions yields **two possible hypercharge assignments**, one of
which is the standard one. The uniqueness of the hypercharge assignments is
recovered by extending the standard-model fermions by a right-handed neutrino and
enlarging the gauge group to SU(2)_L × SU(2)_R × U(1)."*
**So the forcing is not unique on the minimal content alone.** Killing the second
("bizarre") solution requires either Higgs/Yukawa input or a group enlargement.

**Geng & Marshak, PRD 41 (1990) 717** (recid 300063) — the Reply, explaining why
the second solution was rejected in the original paper.

**Babu & Mohapatra, PRL 63 (1989) 938** (recid 278994, 135 cites) and
**PRD 41 (1990) 271** (recid 280087, 124 cites).
Establishes: in gauge models whose group contains an **explicit U(1) factor**
contributing to U(1)_em, charge is *not* automatically quantised; anomaly
cancellation "reduces the arbitrariness considerably, [but] is still not
restrictive enough to fix all the quark and lepton charges." With ν_R present,
quantisation follows **only if the neutrino is Majorana**. Additional assumption
used: **non-vanishing fermion masses**.

**Foot, Joshi, Lew & Volkas, MPLA 5 (1990) 2721** (recid 28541, 109 cites) and
**Foot, Lew & Volkas, J.Phys.G 19 (1993) 361** (recid 337955, 127 cites) — the
definitive assumption catalogue.
Establishes verbatim: *"charge may be **de-quantized in the three-generation
standard model with massless neutrinos**, because differences in
family-lepton-numbers are anomaly-free."* Restoring quantisation requires
family-lepton-number differences to be **explicitly broken** (e.g. Majorana ν_R).
**This is the single most important assumption caveat for L132**: the "anomalies
fix Y" result is a *one-generation* statement.

**Sladkowski & Zralek, PRD 45 (1992) 1701** (recid 315630).
Establishes: with three generations, SM extensions with **more than one Higgs
doublet** and/or **at least one ν_R with a Majorana mass term** uniquely fix the
fermion electric charge; the mixed gauge-gravitational cancellation is then
automatic. Assumption made explicit: number of Higgs doublets matters.

**Rudaz, PRD 41 (1990) 2619** (recid 303703) and **Golowich & Pal, PRD 41 (1990)
3537** (recid 306130).
Establish the hypercharge assignments **without** using electric-charge
assignments or Higgs-sector constraints as input — i.e. the cleanest "anomalies
alone" versions, at the cost of the MRW second-solution ambiguity.

**Lohitsiri & Tong, SciPost Phys. 8 (2020) 009** (recid 1742120) — the modern
sharpening.
Establishes: the gauge-anomaly constraints can be recast as `x³ + y³ = z³`. **If
hypercharge is quantised**, x, y, z are integers, and by Fermat's Last Theorem
for n=3 the only solutions (x=0 or y=0) reproduce the observed assignments.
Notably: **this argument does not use the mixed gauge-gravitational anomaly**,
which is automatically satisfied once Y is quantised and the gauge anomalies
vanish. Assumption: **hypercharge quantisation** — which is an input, not an
output.

**Costa, Dobrescu & Fox, PRL 123 (2019) 151601** (recid 1737609, 77 cites) —
*"General solution to the U(1) anomaly equations."*
Establishes: the full Diophantine solution set, parametrised by n−2 integers for
n Weyl fermions, **proved most general**. This is the correct frame for
understanding *why* the SM case is rigid: rigidity comes from the **restricted
representation content**, not from the anomaly equations themselves, which have
an enormous solution space in general. See also **Batra, Dobrescu & Spivak,
JMP 47 (2006) 082301** (recid 695152).

**Hucks, PRD 43 (1991) 2709** (recid 29002) — global structure of the SM,
anomalies, and charge quantisation (the ℤ₆ quotient thread).

**Textbook layer:** Weinberg, *QTF* vol. 2 §22.4; Peskin & Schroeder ch. 20;
Langacker, Phys.Rept. 72 (1981) 185 (GUT review); Slansky, Phys.Rept. 79 (1981) 1
(recid 10204, 1466 cites — the branching-rule reference).

### The assumptions, consolidated

Any claim that "anomaly cancellation forces Y" silently requires **all** of:

1. **Fixed representation content** — exactly the SM multiplets per generation,
   no extra chiral fermions. (Relaxing this is the whole content of
   Costa–Dobrescu–Fox.)
2. **One generation, or family-universal Y.** At three generations with massless
   neutrinos the forcing **fails** — L_e − L_μ and friends are anomaly-free
   (Foot–Lew–Volkas).
3. **Hypercharge quantisation** (integrality/rationality) for the Fermat-style
   argument; without it, continuous families survive.
4. **Treatment of ν_R.** Present-and-massless reopens the freedom; a **Majorana**
   mass is what closes it (Babu–Mohapatra).
5. **Higgs sector input** — either used (Yukawa invariance / number of doublets)
   or explicitly excluded, and this changes the answer (MRW vs Geng–Marshak).
6. **Which anomaly conditions are admitted** — the mixed gauge-gravitational
   condition is essential to Geng–Marshak but redundant under Lohitsiri–Tong's
   quantisation assumption.
7. **Normalisation is never fixed.** The anomaly conditions are homogeneous
   (degree 1 and degree 3), so `Y → λY` is a solution whenever Y is. **Anomaly
   cancellation can only ever fix ratios.** Normalisation comes from the
   embedding — GUT normalisation `√(5/3)`, `sin²θ_W = 3/8` (Georgi–Quinn–Weinberg
   1974).

---

## Q2 — Identifying hypercharge among SEVERAL U(1)s, in E₆ descent

**This is the load-bearing question for L132, and the E₆ literature has a fully
developed standard vocabulary for exactly this situation.**

### The standard decomposition chain

```
E₆  ⊃  SO(10) × U(1)_ψ
SO(10) ⊃  SU(5)  × U(1)_χ
SU(5)  ⊃  SU(3)_C × SU(2)_L × U(1)_Y
```

giving the rank-6 abelian sector spanned by **{Y, Q_χ, Q_ψ}** — i.e. exactly the
`su(3) ⊕ su(2) ⊕ u(1)³` of the L132 cell. Rank check: 2 + 1 + 3 = 6 = rank E₆.

**The 27 decomposes as 27 → 16 + 10 + 1** under SO(10), and under SU(5):
`16 → 10 + 5* + 1`, `10 → 5 + 5*`, `1 → 1`.

### The θ_E6 parametrisation — the canonical vocabulary

**London & Rosner, PRD 34 (1986) 1530** (recid 228974, **487 cites**) is the
paper that introduced the standard parametrisation: with two extra U(1)s in E₆,
a single extra low-energy Z can be any mixture, parametrised by an angle θ:

> `Q(θ_E6) = cos θ_E6 · Q_χ + sin θ_E6 · Q_ψ`

**Hewett & Rizzo, Phys.Rept. 183 (1989) 193** (recid 268529, **1524 cites**) is
the comprehensive review of the low-energy phenomenology.
**Langacker, Rev.Mod.Phys. 81 (2009) 1199** (recid 777086, **1544 cites**) is the
modern canonical reference; its **Table 2** gives the complete charge table for
the **27** under SO(10) and SU(5) together with Q_χ, Q_ψ, Q_η, Q_I, Q_N, Q_S.

Transcribed from that table (integer normalisations `2√10 Q_χ`, `2√6 Q_ψ`):

| SO(10) | SU(5) | states | 2√10 Q_χ | 2√6 Q_ψ |
|---|---|---|---|---|
| **16** | 10 | u, d, uᶜ, e⁺ | −1 | 1 |
| **16** | 5* | dᶜ, ν, e⁻ | 3 | 1 |
| **16** | 1 | νᶜ | −5 | 1 |
| **10** | 5 | D, H_u | 2 | −2 |
| **10** | 5* | Dᶜ, H_d | −2 | −2 |
| **1** | 1 | S | 0 | 4 |

Named models in standard use (θ_E6 values from Langacker Table 2 / text):

- **χ model**: θ_E6 = 0.
- **ψ model**: θ_E6 = π/2. Has chiral exotics, requires three full **27**-plets.
- **η model**: `Q_η = √(3/8) Q_χ − √(5/8) Q_ψ`, θ_E6 = π − arctan√(5/3) ≈ 0.71π.
  Arises in Calabi–Yau compactifications of the heterotic string when E₆ breaks
  **directly to a rank-5 group** via the Wilson line / Hosotani mechanism
  (Witten 1985).
- **inert model** `U(1)_I`: θ_E6 = arctan√(3/5) ≈ 0.21π; charge orthogonal to
  Q_η; follows from an alternative E₆ breaking pattern (Robinett & Rosner 1982).
- **neutral-N model**: θ_E6 = arctan√15 ≈ 0.42π; νᶜ has zero charge, permitting a
  large Majorana mass.
- **secluded sector model**: θ_E6 = arctan(√15/9) ≈ 0.13π (Erler et al. 2002).

### How hypercharge is conventionally identified — and the honest answer

**Y is not identified by any property intrinsic to the abelian sector.** It is
fixed by *choosing the SU(5) ⊂ SO(10) ⊂ E₆ chain*. Inside SU(5), Y is then the
unique (up to scale) generator commuting with SU(3) × SU(2) — the original
Georgi–Glashow (1974) identification, and genuinely a centralizer definition,
because the centralizer of `su(3) ⊕ su(2)` in `su(5)` is 1-dimensional.

**But that argument does not transplant to E₆.** Verified in-sandbox on the
explicit 72-root E₆ system:

- centralizer of `su(3) ⊕ su(2)` in **e₆** = **9-dimensional** (`su(3) ⊕ u(1)`),
  not `u(1)³`;
- `su(3) ⊕ su(2) ⊕ u(1)³` is the centralizer of a **3-torus** — a Levi
  subalgebra — dim 8 (subsystem roots) + 6 (Cartan) = 14;
- all ten A₂+A₁ node-subsets of the E₆ Dynkin diagram give a dim-14 Levi.

So inside E₆ the condition "commutes with colour and isospin" leaves a
3-parameter family, and **selecting Y requires an extra principle**. In the
literature that principle is always: pick the SU(5)/SO(10) subgroup, or
equivalently demand that the **27** reproduce the observed SM quantum numbers.

### The kinetic-mixing ambiguity — a trap for any "identification" claim

Langacker's general model in this class is, verbatim:

> `Q₂ = cos θ_E6 · Q_χ + sin θ_E6 · Q_ψ − ε·Y`, where ε can result from
> **kinetic mixing**

**The split between "hypercharge" and "the extra U(1)" is therefore not
basis-canonical.** Kinetic mixing (Holdom 1986) mixes them, ε is
renormalisation-scale dependent, and any statement "this combination is Y" is
implicitly a choice of basis convention. A claim to have *uniquely identified*
hypercharge must state and defend that convention.

Coupling normalisation, from the same source: one expects `g₂ = √(5/3) g′` at the
unification scale, where `√(5/3) g′` is the GUT-normalised hypercharge coupling.

### Which U(1) combinations are "safe" vs anomalous

**All of them are safe on complete 27s**, and this is forced, not fortunate:

- **Georgi & Glashow, PRD 6 (1972) 429** (recid 75931, 516 cites) — *"Gauge
  theories without anomalies"*: identifies the class of anomaly-free gauge
  theories.
- **Okubo, PRD 16 (1977) 3528** (recid 120964, 172 cites): proves the existence
  or absence of the triangle anomaly is equivalent to the same question for the
  **symmetrised third-order Casimir invariant**, that SU(n≥3) is the *only*
  simple Lie group with a possible triangle anomaly, and states verbatim that
  *"the best candidates for anomaly-free simple gauge groups are **E₆**,
  SO(4n+2) (n≥2), and the vectorlike SU(n) theories."*
- See also Banks & Georgi, PRD 14 (1976) 1159; Kephart, PLB 151 (1985) 267.

Anomalies become non-trivial **only** when the spectrum is *not* complete **27**s
— incomplete multiplets, projected-out exotics, string constructions. Anomalous
U(1)′s in string constructions are handled by the Green–Schwarz mechanism
(Langacker §III.6.3). The E₆ literature is fully aware of this: Langacker's own
framing of the E₆ charge assignments is *"one can simply view the charges and
exotics as an example of an anomaly-free construction."*

Section III.2 of that review ("Anomaly-Free Sets") catalogues the many authors
who build U(1)′ models by *imposing* anomaly cancellation on chosen exotic
content — Appelquist et al. 2003; Cvetič et al. 1997; Barr et al. 1986; Cheng et
al. 1998, 1999; Erler 2000; Joshipura et al. 2000; Ma 2002; Carena et al. 2004;
Demir et al. 2005; Batra et al. 2006; Morrissey & Wells 2006; Kang et al. 2008;
Lee et al. 2008; Langacker et al. 2008.

### The exotics in 10 + 1, and the requirement that they be heavy

The **10 + 1** beyond the familiar **16** contains: a colour-triplet, Q = −1/3
isosinglet quark pair **D, Dᶜ** (Robinett's "h" quark); the extra
lepton-doublet/Higgs-doublet pair **H_u, H_d** (the charged and neutral exotic
leptons E, ν_E in non-SUSY language); and the SO(10) singlet **S**.

**The constraint, verbatim from Langacker RMP 81 (2009):**

> In a full E₆ grand unified theory the exotic D, Dᶜ partners of the Higgs
> doublets would have **diquark** Yukawa couplings such as `W_DQ ~ DQQ` or
> `Dᶜuᶜdᶜ`, as well as **leptoquark** couplings `W_LQ ~ Duᶜeᶜ` or `DᶜQL`, which
> are related by E₆ to the ordinary Higgs Yukawa couplings. These would lead to
> **rapid proton decay** mediated by the D and Dᶜ **unless their masses (and
> therefore the U(1)′ breaking scale) is comparable to the unification scale**. A
> TeV-scale Z′ therefore requires that the GUT Yukawa relations are not
> respected, so that either the leptoquark or the diquark couplings (or both) are
> absent.

Supporting specialist literature on exotic mixing and its experimental limits:
Robinett, PRD 33 (1986) 1908 (recid 17444) on mixing of the exotic h, E, ν_E with
d, e, ν_e and the resulting FCNCs; Rizzo, PRD 33 (1986) 3329 (exotic
contributions to lepton g−2, μ→eγ) and PRD 34 (1986) 2163 (mass limits);
Hewett & Rizzo, Phys.Rept. 183 (1989) 193 (comprehensive); Rosner, PRD 61 (2000)
097303 on explaining the (d,s,b) vs (u,c,t) mass splitting via mixing with E₆
exotics.

---

## Q3 — Has anyone derived hypercharge from a "measurement"/centralizer/
## superselection construction inside E₆?

Searched adversarially, on the assumption that it *has* been done.

### The decisive hit — a superselection derivation of hypercharge exists

**Todorov, "Superselection of the weak hypercharge and the algebra of the
Standard Model", JHEP 04 (2021) 164, arXiv:2010.15621** (recid 1827024).

Verbatim from the paper body (retrieved full text):

> In the present paper we promote the exactly conserved weak hypercharge to a
> **superselection rule: Y commutes with all observables and all symmetry
> transformations**, and explore its consequences. As a first corollary we obtain
> a u(1) extension of the gauge Lie algebra of the SM: **the centralizer of Y in
> so(10) is g = u(2) ⊕ u(3)**.

Note what that algebra is: `u(2) ⊕ u(3) = su(3) ⊕ su(2) ⊕ u(1) ⊕ u(1)` — **the
Standard Model algebra plus one extra abelian factor, obtained as a centralizer
(i.e. a superselection / commutant) construction.** This is structurally the same
move L132 proposes, one extra u(1) short, and carried out in so(10) rather than
e₆. The paper also gives Y explicitly as a difference of normalised number
operators:

> `½Y = ⅓ Σ_{j=1..3} b*_j b_j − ½ Σ_{α=1,2} a*_α a_α`

and explicitly connects the trace conditions on Y to anomaly cancellation
("The sum of tr Y for all left (or right) chiral particle IRs (leptons and three
coloured quarks) does vanish, reflecting the cancellation of anomalies between
quarks and leptons"). The superselection framing is credited to Wick–Wightman–
Wigner and to Haag's algebraic-QFT superselection sectors.

### The surrounding school — commutant/idempotent constructions of G_SM

- **Todorov & Dubois-Violette, IJMPA 33 (2018) 1850118, arXiv:1806.09450**
  (recid 1679412, 74 cites) — *"Deducing the symmetry of the standard model from
  the automorphism and structure groups of the exceptional Jordan algebra."*
  Argues the SM symmetry can be **deduced** from **Borel–de Siebenthal theory of
  maximal connected subgroups**. E₆ is the reduced structure group of J₃(𝕆), so
  this is E₆-*adjacent*; but the extraction runs through F₄ = Aut(J₃(𝕆)) and
  Spin(9), not through E₆'s abelian sector.
- **Todorov, arXiv:1911.13124** (recid 1767717) — the maximal-rank subgroup of F₄
  respecting the lepton-quark splitting is `(SU(3)_c × SU(3)_ew)/ℤ₃`; restricted
  to J₂⁸ it is **precisely `S(U(3) × U(2))`**, the SM group. Gives Y explicitly:
  `Y = ⅔ Σ_j a*_j a_j − a*₀a₀ − a*₈a₈`. The 32 **primitive idempotents** give the
  first-generation states — idempotents being projections, this is an explicitly
  measurement-flavoured construction.
- **Krasnov, JMP 62 (2021) 021703, arXiv:1912.11282** (recid 1773011) — *"SO(9)
  characterisation of the standard model gauge group."* Verbatim: *"The group
  G_SM is the **subgroup of Spin(9) that commutes with** a certain complex
  structure J in the space 𝕆² of Spin(9) spinors."* An explicit **commutant**
  characterisation of the entire SM gauge group.
- **Dubois-Violette & Todorov, Nucl.Phys.B 938 (2019) 751** (recid 1691269, 52
  cites); **Dubois-Violette & Todorov, Nucl.Phys.B 957 (2020) 115065**
  (superconnection / spin factors); **Todorov, Universe 9 (2023) 222**
  (arXiv:2206.06912) — survey of the whole programme.
- **Boyle, arXiv:2006.16265** (recid 1804327, 48 cites) — exceptional Jordan
  algebra ↔ SM, its minimal LR-symmetric extension, and Spin(10); three
  generations from SO(8) triality.
- **Furey, arXiv:1611.09182** (recid 1500576, 82 cites); **Furey & Hughes, PLB
  827 (2022) 136959**; **Furey & Hughes, "Division algebraic symmetry breaking",
  PLB 831 (2022) 137186** (recid 2090701) — a **sequence of complex structures**
  inducing Spin(10) ↦ Pati–Salam ↦ Left-Right ↦ SM + B−L; **Furey,
  arXiv:2607.18450** derives `g_SM = su(3)_C ⊕ su(2)_L ⊕ u(1)_Y` by annihilating
  highest-grade volume elements and imposing an **equal-trace condition** on
  anti-hermitian operators.
- **Gresnigt et al.** (recids 1728675, 1739592, 2671346, 2803926) — ℂℓ(8) /
  sedenion constructions; **primitive idempotent constructed by selecting a
  special direction**.
- **Manogue & Dray, arXiv:0911.2253** (recid 836807, 56 cites) — *"Octonions, E₆
  and particle physics"*; **Dray & Manogue, arXiv:0911.2255**; **Manogue, Dray &
  Wilson, JMP 63 (2022) 081703** (recid 2066206, 30 cites) — *"Octions: an E₈
  description of the Standard Model"*, identifying `su(3) ⊕ su(2) ⊕ u(1)` inside
  e₈(−24) via a complex structure.
- **Baez & Huerta, Bull.AMS 47 (2010) 483** (recid 817629, 164 cites) —
  expository; Y in SU(5) as the generator commuting with SU(3) × SU(2).
- **Georgi & Glashow (1974)** — the original: Y as the unique generator of su(5)
  commuting with su(3) ⊕ su(2). Textbook.

### Verdict on Q3

**A superselection/centralizer derivation of hypercharge is PUBLISHED PRIOR ART
(Todorov 2021), and commutant characterisations of the whole SM gauge group are
published prior art (Krasnov 2021; Dubois-Violette–Todorov 2018).** The seat must
not treat "hypercharge from a measurement/commutant construction" as a novel
move — it is a live, cited research programme with a decade of output.

What I did **not** find, after (i) full citation-graph closure on Todorov 2021
(all 9 citing works enumerated and read), (ii) INSPIRE title searches on
`hypercharge`+`centralizer` and `hypercharge`+`commutant` (both **0 hits**),
(iii) INSPIRE `superselection`+`gauge group` (3 hits, none relevant), and
(iv) OpenAlex cross-sweeps, is a construction that does **both** of:

- **(a)** work inside **E₆'s rank-6 Cartan specifically** (the school above works
  in F₄ / Spin(9) / so(10) / Cℓ(6) / Cℓ(8) / Cℓ(10) / e₈ — E₆ appears only as the
  *structure group* of J₃(𝕆), never as the arena for the abelian-sector
  selection); **and**
- **(b)** single out **which** of the three u(1)s is hypercharge by an intrinsic
  or measurement-theoretic principle, rather than by choosing the SU(5)/SO(10)
  subgroup or by matching the observed SM charges.

**Honesty caveat — this null is NOT certified.** The octonion/Jordan-algebra
literature is large, fast-moving, substantially posted outside INSPIRE's core
indexing, and includes many low-citation preprints. The null rests on the
searches recorded above, not on a proof of absence. MathSciNet was unreachable
(auth wall) and was not consulted. Treat (a)+(b) as "not found by this sweep",
not as "does not exist".

---

## Q4 — The honest verdict: what is the MOST L132 could claim?

### Q4.0 — The vacuity gate (read this first)

Computed in-sandbox on a complete **27** with the Langacker Table 2 charges, all
as left-handed Weyl fermions (27 states confirmed):

| Condition | Value |
|---|---|
| Σ Y, Σ χ, Σ ψ (gravitational) | 0, 0, 0 |
| Σ Y³, Σ χ³, Σ ψ³ | 0, 0, 0 |
| Σ Y²χ, Σ Yχ², Σ Y²ψ, Σ Yψ² | 0, 0, 0, 0 |
| Σ χ²ψ, Σ χψ², Σ Yχψ | 0, 0, 0 |
| [SU(3)]² U(1)_Y / _χ / _ψ | 0, 0, 0 |
| [SU(2)]² U(1)_Y / _χ / _ψ | 0, 0, 0 |
| Witten SU(2) global | 6 weak doublets — **even, safe** |

**Every condition vanishes identically**, exactly as forced by Okubo's theorem
that E₆ has no symmetrised third-order Casimir.

**Therefore: if the object's charges form complete 27s, the L132 anomaly question
CANNOT FAIL, and is vacuous as a test.** Per the programme's own MB12 rule
(a criterion must be able to pass *and* to fail), **the seat must establish
non-vacuity before running** — i.e. determine whether the object's spectrum
decomposes into complete **27**s or into incomplete multiplets. That
determination is the real gate, and it is cheap.

### (a) Would be REPRODUCING TEXTBOOK MATERIAL — report as "reproduced", never "predicted"

1. The SM anomaly-cancellation conditions themselves (Weinberg vol. 2 §22.4;
   Peskin & Schroeder ch. 20).
2. The chain E₆ ⊃ SO(10)×U(1)_ψ ⊃ SU(5)×U(1)_χ×U(1)_ψ ⊃ SM×U(1)², and
   **27 → 16 + 10 + 1 → 10 + 5* + 1 + 5 + 5* + 1** (Slansky 1981).
3. **`su(3) ⊕ su(2) ⊕ u(1)³` is a maximal-rank Levi subalgebra of e₆** = the
   centralizer of a 3-torus. Classified by Borel–de Siebenthal (1949) and Dynkin
   (1952). *Arriving at this algebra from E₆ is not a finding.*
4. **E₆ is anomaly-safe** (Georgi & Glashow 1972; Okubo 1977) ⇒ anomaly
   cancellation on complete **27**s is a forced group-theoretic identity (§Q4.0).
5. Y as the unique generator of su(5) commuting with su(3)⊕su(2)
   (Georgi–Glashow 1974).
6. GUT normalisation `√(5/3)`, `sin²θ_W = 3/8` (Georgi–Quinn–Weinberg 1974).
7. That anomaly conditions are **homogeneous** and so can never fix the
   normalisation of Y — only ratios.

### (b) Would be REPRODUCING SPECIALIST LITERATURE — cite, report as "reproduced"

1. The θ_E6 parametrisation `Q = cos θ Q_χ + sin θ Q_ψ` and the named models
   χ / ψ / η / inert / neutral-N / secluded (London & Rosner 1986; Hewett & Rizzo
   1989; Langacker 2009 Table 2).
2. The **kinetic-mixing ambiguity** `− εY`: the Y / extra-U(1) split is not
   basis-canonical (Holdom 1986; Langacker 2009).
3. The exotics constraint: D, Dᶜ carry both leptoquark and diquark couplings
   related by E₆ to ordinary Yukawas ⇒ proton decay ⇒ masses (and the U(1)′
   breaking scale) must be near M_GUT unless the GUT Yukawa relations are broken
   (Langacker 2009; Hewett & Rizzo 1989; Robinett 1986; Rizzo 1986).
4. The anomalies-fix-Y results **together with their failure modes**:
   Geng–Marshak 1989; the MRW second solution; Babu–Mohapatra's Majorana
   requirement; Foot–Lew–Volkas' three-generation dequantisation;
   Lohitsiri–Tong's `x³+y³=z³` under quantisation; Costa–Dobrescu–Fox's general
   solution.
5. **The superselection/centralizer derivation of Y and its u(1)-extended SM
   algebra** (Todorov 2021, JHEP 04 (2021) 164) — structurally the closest prior
   art to L132's own move.
6. The commutant characterisation of G_SM (Krasnov 2021).

### (c) POTENTIALLY NEW — narrow, and conditional

1. **A principled, stated-in-advance selection of which u(1) in E₆'s rank-3
   abelian sector is hypercharge**, derived from the object's own measurement
   structure rather than by choosing an SU(5)/SO(10) subgroup or by matching
   observed SM charges. **This is the only place novelty can live.** It is
   meaningful *only* if the selection principle is fixed **before** looking at
   which combination gives the right answer — otherwise it is postdiction.
2. **If the object's spectrum does NOT decompose into complete 27s**, then
   anomaly cancellation becomes a genuine, non-vacuous constraint, and its
   satisfaction *would* be informative. Establishing which case obtains is the
   decisive first computation.
3. The **provenance** — how this algebra arises from the object's second
   measurement — may be new as a construction, but the **target algebra is
   classified structure** and the arrival must be reported as landing on a known
   object.

### Warnings the seat must not get wrong

- **Vacuity first.** Complete **27**s ⇒ the anomaly check cannot fail. Verify
  non-vacuity before computing anything else.
- **"Reproduced", never "predicted"**, for everything in (a) and (b).
- **Normalisation of Y is not determined by anomalies.** Do not claim it.
- **Do not claim "hypercharge falls out"** if an SU(5)/SO(10) subgroup was chosen
  — including implicitly, e.g. by reading charges off the standard branching
  tables. That choice *is* the identification.
- **The u(1)³ ⊃ Y split is kinetic-mixing-ambiguous.** Any "unique" identification
  requires a stated and defended basis convention.
- **"Hypercharge from a commutant/superselection construction" is prior art**
  (Todorov 2021). Novelty, if any, is in doing it *in E₆'s abelian sector* and in
  *selecting among three u(1)s* — not in the genre.

---

## BIBLIOGRAPHY — what each source actually establishes

Ordered by role. INSPIRE recids given for re-retrieval.

### Q1 — anomalies and hypercharge

| Source | recid | Establishes | Requires |
|---|---|---|---|
| Geng & Marshak, PRD 39 (1989) 693 | 24389 | Minimal Weyl reps + charges uniquely determined by triangle + global-SU(2) + mixed-grav anomalies | Minimal content; pre-SSB; one generation |
| Minahan, Ramond & Warner, PRD 41 (1990) 715 | 279403 | **Two** hypercharge solutions from anomalies alone; uniqueness needs ν_R **and** group enlargement to SU(2)_L×SU(2)_R×U(1) | No Higgs reference |
| Geng & Marshak, PRD 41 (1990) 717 | 300063 | Reply: why the second ("bizarre") solution was rejected | — |
| Babu & Mohapatra, PRL 63 (1989) 938 | 278994 | With explicit U(1) + ν_R, quantisation follows **only if ν is Majorana** | Non-vanishing fermion masses |
| Babu & Mohapatra, PRD 41 (1990) 271 | 280087 | Anomalies reduce but **do not fix** all quark/lepton charges when an explicit U(1) is present | As above |
| Foot, Joshi, Lew & Volkas, MPLA 5 (1990) 2721 | 28541 | Review contrasting classical vs anomaly vs vector-like-EM constraints | — |
| Foot, Lew & Volkas, J.Phys.G 19 (1993) 361 | 337955 | **Charge de-quantises in the 3-generation SM with massless neutrinos** (family-lepton-number differences are anomaly-free) | — |
| Sladkowski & Zralek, PRD 45 (1992) 1701 | 315630 | 3 generations: >1 Higgs doublet and/or Majorana ν_R uniquely fix charges | Higgs content |
| Rudaz, PRD 41 (1990) 2619 | 303703 | Charge quantisation from renormalisability logic of the minimal chiral content | Minimal content |
| Golowich & Pal, PRD 41 (1990) 3537 | 306130 | Y assignments without electric-charge or Higgs input | — |
| Hucks, PRD 43 (1991) 2709 | 29002 | Global structure, anomalies, charge quantisation (ℤ₆ thread) | — |
| Nowakowski & Pilaftsis, PRD 48 (1993) 259 | 33573 | Note on charge quantisation through anomaly cancellation | — |
| Lohitsiri & Tong, SciPost Phys. 8 (2020) 009 | 1742120 | Gauge anomalies ⇔ `x³+y³=z³`; only trivial integer solutions = Nature's Y; mixed-grav is **redundant** | **Y quantised** |
| Costa, Dobrescu & Fox, PRL 123 (2019) 151601 | 1737609 | **General** solution of the U(1) Diophantine anomaly equations, proved most general | — |
| Batra, Dobrescu & Spivak, JMP 47 (2006) 082301 | 695152 | Anomaly-free fermion sets | — |
| Slansky, Phys.Rept. 79 (1981) 1 | 10204 | The branching-rule reference for all of the above | — |

### Q2 — E₆ descent and the extra U(1)s

| Source | recid | Establishes |
|---|---|---|
| Gürsey, Ramond & Sikivie, PLB 60 (1976) 177 | 100124 | The original E₆ unification model; 27-plet assignments |
| Robinett & Rosner, PRD 25 (1982) 3036 | 168975 | SU(3)×SU(2)×U(1)×U(1) from SO(10); two neutral vector bosons |
| Robinett & Rosner, PRD 26 (1982) 2396 | 177363 | **All E₆ breakdown patterns through maximal subgroups catalogued**, with mass-scale bounds |
| **London & Rosner, PRD 34 (1986) 1530** | 228974 | **The canonical θ parametrisation** of the extra U(1) mixture in E₆ |
| Hewett, Rizzo & Robinson, PRD 34 (1986) 2179 | 17590 | SUSY/non-SUSY E₆ breaking patterns giving an extra U(1) |
| **Hewett & Rizzo, Phys.Rept. 183 (1989) 193** | 268529 | **The comprehensive review** of superstring-inspired E₆ phenomenology: Z′, exotic fermions, Higgs |
| **Langacker, Rev.Mod.Phys. 81 (2009) 1199** | 777086 | **Modern canonical reference.** Table 2 = full 27 charge table (χ, ψ, η, I, N, S); `Q₂ = cosθ Q_χ + sinθ Q_ψ − εY`; the D/Dᶜ proton-decay constraint; `g₂ = √(5/3) g′`; anomaly-free-set literature |
| Robinett, PRD 33 (1986) 1908 | 17444 | Mixing of E₆ exotics (h, E, ν_E) with d, e, ν_e; FCNC constraints |
| Rizzo, PRD 33 (1986) 3329 | 219732 | Exotic contributions to lepton g−2 and μ→eγ |
| Rizzo, PRD 34 (1986) 2163 | 227115 | Mass limits on light E₆ exotics |
| Rosner, PRD 61 (2000) 097303 | 525750 | (d,s,b) vs (u,c,t) mass splitting from mixing with E₆ exotics |
| **Georgi & Glashow, PRD 6 (1972) 429** | 75931 | **The anomaly-free gauge theory classification** |
| **Okubo, PRD 16 (1977) 3528** | 120964 | **Anomaly ⇔ symmetrised 3rd-order Casimir; SU(n≥3) is the only simple group with one; E₆ named anomaly-free** |
| Banks & Georgi, PRD 14 (1976) 1159 | 115974 | SU(N) anomaly coefficient for general reps |
| Kephart, PLB 151 (1985) 267 | 216189 | Safe groups in even dimensions |

### Q3 — measurement / centralizer / superselection constructions

| Source | recid | Establishes |
|---|---|---|
| **Todorov, JHEP 04 (2021) 164** (arXiv:2010.15621) | 1827024 | **Y promoted to a superselection rule; the centralizer of Y in so(10) is u(2)⊕u(3)** = SM algebra + one extra u(1). Explicit Y formula. **Closest prior art to L132.** |
| Todorov & Dubois-Violette, IJMPA 33 (2018) 1850118 | 1679412 | SM symmetry **deduced** from Aut/structure groups of J₃(𝕆) via Borel–de Siebenthal |
| Todorov, arXiv:1911.13124 | 1767717 | Max-rank subgroup of F₄ respecting lepton-quark split; restriction to J₂⁸ gives exactly `S(U(3)×U(2))`; explicit Y; 32 primitive idempotents = states |
| Dubois-Violette & Todorov, NPB 938 (2019) 751 | 1691269 | Exceptional quantum geometry II — 3 generations |
| Dubois-Violette & Todorov, NPB 957 (2020) 115065 | 1785624 | Quillen superconnection in the spin-factor approach |
| Todorov, Universe 9 (2023) 222 | 2667356 | Survey of the octonion internal-space-algebra programme |
| Todorov & Drenska, AACA 28 (2018) 82 | 1673689 | F₄, its Borel–de Siebenthal maximal subgroups, applied to fermion/boson classification |
| **Krasnov, JMP 62 (2021) 021703** | 1773011 | **G_SM = the subgroup of Spin(9) commuting with a complex structure J on 𝕆²** — explicit commutant characterisation |
| Boyle, arXiv:2006.16265 | 1804327 | Exceptional Jordan algebra ↔ SM, LR extension, Spin(10), triality/3 generations |
| Furey, arXiv:1611.09182 | 1500576 | SM reps from ℝ⊗ℂ⊗ℍ⊗𝕆 acting on itself; Y from generalised ideals |
| Furey & Hughes, PLB 831 (2022) 137186 | 2090701 | Sequence of complex structures ⇒ Spin(10) ↦ PS ↦ LR ↦ SM+B−L |
| Furey, arXiv:2607.18450 | 3182230 | `g_SM` from annihilating volume elements + equal-trace condition |
| Gillard & Gresnigt, EPJC 79 (2019) 446 | 1728675 | Primitive idempotent from a selected special direction; 3 generations from ℂ⊗𝕊 |
| Manogue & Dray, arXiv:0911.2253 | 836807 | Octonions, E₆ and particle physics (E₆ as preserving structure on J₃(𝕆)) |
| Manogue, Dray & Wilson, JMP 63 (2022) 081703 | 2066206 | `su(3)⊕su(2)⊕u(1)` inside e₈(−24) via a complex structure |
| Baez & Huerta, Bull.AMS 47 (2010) 483 | 817629 | Expository; Y in SU(5) as the generator commuting with SU(3)×SU(2) |

### In-sandbox verifications performed (not literature)

- E₆ root system generated from Bourbaki simple roots: **72 roots** ✓.
- `su(3)⊕su(2)⊕u(1)³` = centralizer of a 3-torus in e₆; **dim 14** (8 subsystem
  roots + 6 Cartan); all ten A₂+A₁ node-subsets of the E₆ diagram give dim 14.
- Centralizer of `su(3)⊕su(2)` in e₆ = **9-dimensional** (6 roots + 3 Cartan),
  i.e. `su(3)⊕u(1)` — **not** `u(1)³`.
- All 13 U(1) cubic/mixed/gravitational anomaly conditions, both non-abelian
  mixed conditions, and the Witten SU(2) parity vanish identically on a complete
  **27** (Langacker Table 2 charges). Table in §Q4.0.
