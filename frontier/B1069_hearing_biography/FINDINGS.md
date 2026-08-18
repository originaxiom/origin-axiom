# B1069 — THE HEARING BIOGRAPHY: ℚ(√5) as a number field, built exhaustively on new ground

**Date:** 2026-08-18 · **Seat:** cc (banking) · **Status:** computed (the field-masterplan's
W3 cell: 6 section agents + 2 verification lenses + assembler; 9 agents, 0 errors; every
verdict-bearing computation exact) · Gate 5 untouched — no physics anywhere.

**Provenance and verification record.** Six sections computed in parallel (splitting census
with triple-independent checks per prime; units-as-a-group; ray class at small conductors
incl. narrow variants; the Hecke palette mirror; orders ℤ+fφℤ against the metallic family;
CM-adjacent typing), then two adversarial lenses (recomputation of the eight most
load-bearing claims — ALL PASS; frame/F11-completeness adjudication — six FAIL rows, every
one either folded into the document as a flagged correction or scoped in the frame section).
The assembler received both lenses' findings; the bench verified the assembly carries them
(the four repair sites checked individually here). Bench re-verification beyond the cell:
**the B92 catch confirmed independently on this bench** — h(order of conductor 2, disc 20)
= 1 by the class-number formula (unit index 3 via φ³ = 1+2φ, norm −1 ⟹ narrow = wide),
the inflating imprimitive forms exhibited ((2,±6,2) = 2·(1,±3,1)); B92's h=2 is WRONG —
corrected beside B92 with an error-ledger instance this same bank.

**The headline numbers (all exact, all double-checked):** the hearing Hecke palette is
**1, 1, 2** at (2),(4),(8) against being's 1, 2, 8 — the discriminator is Dirichlet unit
rank (1 vs 0: a free unit permanently outraces the residue tower), NOT 2-inert (shared,
a control); narrow ray class at (4)·∞₁∞₂ = **ℤ/2 × ℤ/2 non-cyclic** (new ground); orders
f=3,4: h_wide = 1 with h_narrow = 2; h = h⁺ = 1 for the field, drawn in-sandbox.
**The F11-adjacent bridge, registered not claimed:** B737's own sister script
(p3_sister.py) uses the identical multiplier-ring construction as this arc's orders
table — the golden-side voice route (Hilbert modular / real multiplication) now has a
named on-ramp; F11 itself remains the golden ledger's one GAP, untouched here (B739's
character-rigidity governs what the palette cannot do).

---

# THE HEARING BIOGRAPHY

### ℚ(√5) — the object's other real place, censused against the K-biography's frame

*Draft. Unbanked exploratory scratch (no PREREGISTRATION, no hash, no PROGRESS_LOG entry —
WORKING_RULES §3–4). Assembled read-only against `(home)/origin-axiom`; every arithmetic
claim below was executed fresh in-sandbox (python3/sympy, several rows cross-validated against
PARI/GP and Sage as a second oracle) and independently re-verified in two passes, v1 and v2 (see
§Verification). This is the "hearing" side's census, paired against the corpus's own "being" side
(ℚ(√−3)) the way the K-biography pairs structure/value/seam primes of K.*

## Frame, method, and what this is not

**The falsifiable frame.** The corpus's golden ledger (B746) finds 10 of 12 FORCED-golden floors
computed and exactly one GAP: **F11 — "voice/emittance"** — sourced to B737 (Candidate Zero) and
B739 (Character Rigidity), both about the being side. This document was assembled to close
different, adjacent gaps (B1067's census roadmap, B1064's cusp-torus repose) and **was not aimed
at F11**. The verification pass below (v2) found real but *unrecognized* contact with F11's own
apparatus in one place (the Palette section) and a structural result that closes off one candidate
route to it while leaving the true open route (Hilbert modular / real multiplication) untouched.
That finding is reported honestly, not smoothed over.

The second banked pole this document must not contradict is **mutual blindness**: 5 is inert in
ℚ(√−3) and 3 is inert in ℚ(√5) — both directions reconfirmed fresh here, matching CHANGELOG:1791
and B857 verbatim.

**What this document does NOT claim.**
- **No resolution of F11.** No golden-side voice, scattering determinant, or L-function-of-a-cusp
  object is constructed anywhere below; the one L-value computed (§Structure, L(1,χ₅)) is a
  structurally different object, used only to cross-check the class-number formula.
- **No descent claims.** This is census/verification-tier work — the corpus's own "W1." Any actual
  construction (banking a new arc, extending the Hecke-palette reading into a real ray-class arc,
  writing the B92 correction upstream) is **W2/W3's** job, not this document's.
- **No physics.** Nothing here feeds `CLAIMS.md` or crosses Gate 5.
- **No conflation of ℚ(√5) with K.** K = ℚ[t]/μ (the sextic, resolvent √77, disc K =
  6237 = 3⁴·7·11) is a **different field** from this document's ℚ(√5). This is exactly the
  conflation class RETRACTED under E41/RETRACTED_PHRASES row 9 in the repo's own most recent
  commit at assembly time (694d513f, HEAD, 2026-08-18): *"True statements about ℚ(√5) ramifying at
  5 (disc 5) are a DIFFERENT field and unaffected."* Every K-fact below is quoted thematic
  motivation, tagged, never merged.
- **No unconditional proof that φ is the fundamental unit.** Every minimality claim below rests on
  a bounded box search (|a|,|b| ≤ 30, and separately ≤ 3); a continued-fraction route was
  attempted, mis-executed (an indexing slip that produced φ² instead of φ), and honestly **dropped
  rather than forced**.

**Computation-status legend** (every row below carries one or more of these tags):

| tag | meaning |
|---|---|
| **R** | REBUILT-here — executed fresh in this bench, independently checked ≥2 ways, several further cross-validated against PARI/GP and/or Sage |
| **C** | standard-cited — a classical/textbook fact, or a corpus fact confirmed present this session (grep or direct read), not itself re-derived here |
| **C[K]** | standard-cited **about K**, a different field — quoted as thematic motivation only |
| **P** | PROPOSED-NOT-BANKED — a role, label, or reading proposed by this document; not a filed theorem |
| **N/C** | NOT-COMPUTABLE-HERE — outside this bench's scope by construction |
| **N/C[K]** | NOT-COMPUTABLE-HERE because it is K's own internal construction (out of this census's scope) |

Setup, re-verified once and used throughout: f(x) = x² − x − 1 is φ's minimal polynomial;
disc(f) = 5 = disc(ℚ(√5)); O_K = ℤ[φ] **exactly** (index 1, confirmed via `round_two`), so
**Dedekind's theorem applies unconditionally at every prime**, including p = 2 and p = 5 where the
Legendre-symbol shortcut alone would not suffice. **R.**

---

## The role-typed prime table

Twelve programme primes, exact splitting in ℚ(√5), plus a role PROPOSED (not banked) against the
corpus's structure/value/seam vocabulary. Every splitting fact is triple-independently checked
(Dedekind factorization + Legendre/Kronecker symbol + brute-force quadratic-residue scan) for the
ten odd primes ≠ 5, and Dedekind-only (the sole unconditional method) at p = 2 and p = 5.

| p | splitting in ℚ(√5) | role (proposed) | status | note |
|---|---|---|---|---|
| **2** | INERT — 𝔭=(2), 𝔽₄ | STRUCTURE (weak) | R + P | No ℚ(√5)-specific finding located by grep. Only available motivation: 2's *absence* from ramification (disc 5 odd — the "clean" golden ring). Decoration (non-discriminating): 2I=SL(2,5) is perfect, but 2 is the universal doubling prime of every binary-polyhedral cover. |
| **3** | INERT | **SEAM** | R + P + C[K] | Member of K's ramified triple {3,7,11}, disc K = 3⁴·7·11 [N/C[K]]. Ramified in ℚ(√−3) itself ((x+1)² mod 3, verified fresh). The mutual-blindness pole. x²+3 irreducible over ℚ(√5) [B1003] ⟺ √−3∉ℚ(√5), consistent with ℚ(√5,√−3)'s real subfield = ℚ(√5) exactly [B743]. Sharpest-evidenced SEAM row. |
| **5** | RAMIFIED — 𝔭²=(5), 𝔭=(5,φ−3) | STRUCTURE (definitional) | R + C | The field's own defining prime. HEAD commit (694d513f) affirms this exact statement while retracting the K look-alike (E41). Fenced decoration: 2I=SL(2,5) perfect vs 2T=SL(2,3) abelianized ℤ/3 — thematic only. |
| **7** | INERT | SEAM (paired w/ 11) | R + P + C[K] | {3,7,11} ⊂ K's ramified set; 7·11=77 = K's resolvent (K025). B1067 itself flags the 7/11 ramification *shapes* as under-documented — the weakest-evidenced SEAM pair, reported honestly. |
| **11** | SPLIT — 𝔭₁𝔭₂ | SEAM (paired w/ 7) | R + P + C[K] | Same motivating set as 7. |
| **13** | INERT | STRUCTURE | R + P + C[K] | K's own literal label — one of {13,17,19}, inert in K [LAW_MAP row 201]. 13⁶ = leading numerator of α_μ [B910]; rescaling constant "theirs(13t) − 2197·mine(t) = 0" [B872]. HEAD commit warns 13⁶ in disc(μ) is **model-borne**, not a K-ramification fact — the exact order/conductor trap flagged in the HOUSE GUARDS, caught here. Coincidence of label across two fields; no causal link examined. |
| **17** | INERT | STRUCTURE | R + P + C[K] | Shares K's triple; weakest-evidenced of the three — no bespoke decoration found beyond shared membership. |
| **19** | SPLIT — 𝔭₁𝔭₂ | STRUCTURE | R + P + C[K] | K's third structure prime (inert in K); 19⁶ = leading numerator of the compact-wall α_κ [B910], paired with 13 (17 unpaired). **19 SPLITS here while INERT in K** — the cleanest single illustration in this table that "structure prime" is K-scoped, zero implication for ℚ(√5). |
| **41** | SPLIT | **NO ROLE FOUND** (hint corrected) | R + C | The task's own offered hint ("41 in B479's held-breath field") is **FALSE**. B479's erratum [F4; T-BREATH-TORSION] gives the genuine d=5 held-breath field as **degree-4**, quadratic subfield ℚ(√5) itself (min poly z⁴−3z³+7z²−4z+4, disc 5²·41); "41" was only the coprime-to-5 part of that discriminant, mislabeled ℚ(√41) in an early draft. High-confidence corrected trap, reported as the deliverable of the grep-then-open instruction — not an oversight. |
| **953** | INERT | **VALUE** | R + C[K] | First of K's value primes, split[1,2] in K [LAW_MAP 201-202]. B918's OBSERVER'S-PLACE THEOREM: 953 is literally "the pole" — den(V) = 𝔭₁(953)⁴ — **confirms** the task's hint verbatim-adjacent. K's class group is OPEN exactly here (principality of 𝔭₁(953) undecided, B1067). |
| **1129** | SPLIT — 𝔭₁𝔭₂ | VALUE | R + C[K] | Second value prime, split[1,2] in K; B918: "the e₂-zero of the V-residues." |
| **421493** | INERT | VALUE | R + C[K] | Third value prime, split[1,2] in K; B918: "the trace-zero" place. |
| **77 = 7×11** (note) | not prime; both factors above | thematic restatement only | R + N/C[K] | K's own resolvent integer (K025: "one field K, one resolvent √77"; disc K = 81×77 = 6237). Not a ℚ(√5) fact; no new census row required. |

Two hint-audit outcomes worth stating together: the corpus's own offered "41" lead was a
**corrected trap** (traced to B479's erratum), while "953 the observer's place" was **confirmed
verbatim-adjacent** to B918. Both outcomes are the deliverable of the grep-then-open instruction,
not a gap in this pass.

---

## The structure table

### Units and the class number of O_K = ℤ[φ]

| # | fact | status | key computation | caveat |
|---|---|---|---|---|
| 1 | O_K^× = {±1} × ⟨φ⟩, rank 1 (Dirichlet) | R + C | φ²=φ+1 exact; a bounded box search (coefficients up to 30 in absolute value) finds no unit strictly between 1 and φ | box search ≠ proof; a continued-fraction attempt was tried, mis-executed (an indexing slip producing φ² not φ), and **dropped rather than forced** |
| 2 | N(φ)=φφ′=−1 ⟹ sign map {±1}²-surjective ⟹ Cl⁺(K) ≅ Cl(K) | R | exact symbolic product = −1; explicit closure of {sgn(−1), sgn(φ)} = full {±1}² (order 4); control run on ℚ(√3) (fund. unit norm +1) correctly finds the sign map **non**-surjective, h⁺=2h there | mechanism verified to discriminate, not assumed to always return "equal" |
| 3 | h(ℚ(√5)) = 1 | R | Minkowski bound √5/2 ≈ 1.118 < 2; independently, reduced indefinite forms of disc 5: 2 forms, 1 SL(2,ℤ) orbit; cross-validated against 4 control discriminants (8, 12, 40, 60), 5/5 match | — |
| 4 | Reg(K) = log φ; 4·Reg = 1.92485 matches banked B420 line exactly | R | N(4·Reg, 30dp) matches; L(1,χ₅) computed **two** independent closed forms (digamma/Hurwitz-zeta at 60dp; sine-product 2/√5·log φ), agree to 60 digits | a consistency check across h=1/Reg/L(1,χ), not a re-proof of h=1 (would be circular) |
| 5 | Totally positive units = ⟨φ²⟩ = ⟨φ+1⟩, index 4 | R | φ²=φ+1 exact; sign table n=−4..4: σ₁(φⁿ)=+1 always, σ₂(φⁿ)=(−1)ⁿ; −φⁿ never totally positive | index 4 = 2^{r₁}, realized *because* the sign map is surjective (row 2) |
| 6 | torsion(O_K^×) = {±1}; μ₄, μ₆ excluded | R + C | K is totally real (both embeddings real, disc 5 > 0); no non-real root of unity can lie in a totally real field | one-line classical argument, freshly stated |

### Ray class groups Cl_m at m ∈ {(2), (3), (√5), (4), (5)}

Setup (**R**): O = ℤ[φ] maximal; O^× = ⟨−1⟩×⟨φ⟩, N(φ)=−1; h(K)=1; sign map surjective ⟹
h⁺(K)=h(K)=1; torsion={±1}; splitting 2-inert/3-inert/5-ramified/11-split all re-derived, matching
the banked frame verbatim.

| modulus | (O/m)^× | Cl_m (S=∅) | Cl_{m,{1}} | Cl_{m,{2}} | Cl_{m,{1,2}} (narrow) | status |
|---|---|---|---|---|---|---|
| (2) | ℤ/3 (𝔽₄) | 1 | 1 | 1 | 1 | R |
| (3) | ℤ/8 (𝔽₉, cyclic) | 1 | 1 | 1 | **ℤ/2** | R |
| (√5) | ℤ/4 (𝔽₅) | 1 | 1 | 1 | **ℤ/2** | R |
| (4) | ℤ/2×ℤ/6, order 12, **non-cyclic** | 1 | **ℤ/2** | **ℤ/2** | **ℤ/2×ℤ/2**, order 4, non-cyclic | R — flagged |
| (5) | ℤ/20 (order-25 local ring, cyclic) | 1 | 1 | 1 | **ℤ/2** | R |

**The pattern.** (2) alone is wholly unaffected by real places. (3), (√5), (5) share an
**identical** narrow signature: ordinary and single-place variants trivial, ℤ/2 only when both real
places are combined. (4) is the outlier: non-cyclic, single-place-sensitive, and doubled at
{1,2}. The single fork explaining all of this is whether φ alone generates (O/m)^×
(true for (2),(3),(√5),(5): absent-or-half correction) or not (true only for (4): maximal
correction) — reduced, and verified element-by-element, to **residue degree**: 3, √5, 5 all have
f=1 at their respective primes (cyclic local unit filtration); 2 alone has f=2 (non-cyclic
(ℤ/2)² kernel). This mechanism is offered as this session's reading; per its own caveat it "should
get a second pass before being banked as a stated theorem" — the most-worked derivation in the
sweep. **P** for the mechanism-as-theorem; **R** for every number.

A bonus (2,4,8)-tower comparison against being's banked shape (1,2,8) — genuinely computed, not
one of the 5 requested moduli — is reported in full under **§The palette** below rather than
duplicated here; it does **not** numerically match being's shape.

Caveats: (√5) and (5) are **ideals of the maximal order** — not the order-conductor f of
§The orders' suborders ℤ+fφℤ (HOUSE GUARDS flag, doubly relevant at (5), where the numeral 5 names
both senses). A verification-method note flags two narrative overreaches in pre-existing scratch
files that should **not** be carried into any future banked write-up verbatim: (i) a claim that
"there is no hidden narrow-vs-wide correction term" is true only for the S=∅-only palette and the
global narrow class group — this sweep directly falsifies the broader reading (4 of 5 moduli *do*
pick up a narrow correction at nonempty S); (ii) disc-12/disc-60 control rows marked "CHECK" are a
labeling artifact (h⁺=2h there, not an error), not a defect — and do not touch ℚ(√5) itself.

### Typing: ℚ(√5) among its CM neighbors — the F11 frame's structural half

| object | type | status | key fact | note |
|---|---|---|---|---|
| ℚ(√5) itself | STANDARD — totally real, never CM | R + C | min poly has two real roots; N(φ)=−1 confirms K⊂ℝ | grep: never mislabeled as a CM field anywhere in 21 corpus hits |
| ℚ(√5,√−3) | **BANKED** [B743/LAW_MAP:71] — degree-4 CM field, real subfield **exactly** ℚ(√5) | R (2nd independent method) | min poly x⁴−4x²+64, degree 4; roots {±√5±i√3} (30dp numeric match); embedding+conjugation route: Fixed(κ) = ℚ(√5), agrees with the independent real-span computation | full agreement with B743, no discrepancy found by the second route |
| ℚ(√−15) "the seam" | **BANKED** [CLAIMS P17/P18/P19/P65; B530] — 3rd quadratic subfield of ℚ(√5,√−3), disc −15 | R | full Galois group (ℤ/2)² built directly; all 3 fixed-field computations agree | — |
| ℚ(√−5), disc −20 | BANKED (present, one arc: B530) but **flagged**: NOT a parallel construction to ℚ(√−15) | R | disjointness proved: −5/5, −5/−3, −5/−15 all non-square ⟹ genuinely a 4th, independent field, not a subfield of ℚ(√5,√−3) (a different quartic, B530's D₄, disc −400) | corrects a framing risk in how the question was posed — B743 and B530 were never actually conflated *in the repo itself* |
| Real multiplication | STANDARD fact, classical sense **absent** from corpus | R + C | K⊗ℝ ≅ ℂ iff K imaginary quadratic (the dimension-1 CM/RM dichotomy, freshly stated) — bars ℚ(√5) **by type**, not by absent search, from ever being End(Λ) of a complex 1-torus | the phrase 'real multiplication' occurs exactly once (B672 — a *dynamical trace-field* usage, an Anosov cat-map on H₁(T²)=ℤ², not the classical abelian-surface construction); 'abelian surface' 0 hits; 'Hilbert modular' exactly 1 hit (B1067's own sentence declaring its absence) — genuinely open territory, **N/C** |

This is the decisive structural result of the document (confirmed sound by v2, §Verification):
**ℚ(√5) is totally real, hence can never be a CM field, hence can never be the multiplier ring of a
complex cusp torus** the way B1064 gate-1's ℤ+4ωℤ (order in ℚ(√−3)) sits inside a genuine complex
lattice. This rules out one specific transplant of that construction to the golden side — it does
**not** rule out real multiplication on a real ℤ²-lattice, which is a live, banked construction
(§The orders, below).

---

## The palette

The Hecke-palette mirror: |(O/2^k)^× / im(units)| on the hearing side (ℚ(√5)) against the
already-banked being side (ℚ(√−3), B1067's 1, 2, 8).

| item | status | note | caveat |
|---|---|---|---|
| 2 inert (2-way check) | R | Dedekind + D mod 8 shortcut; cross-checked against the ℚ(√−3) control (2 also inert there) | — |
| h=1, h⁺=1, drawn in-sandbox | R | Minkowski bound + sign-surjectivity; fills a B1067 census gap ("never computed by reduced forms or Minkowski bound," "the narrow-class conclusion is never drawn") | — |
| ℤ[φ]/(2) = 𝔽₄ enumerated | R | 4 elements {0,1,φ,1+φ}; 3 nonzero = 3 units | — |
| **Being's palette rebuilt: 1, 2, 8** at k=1,2,3 | R (method validation) | independent code, reproduces the banked B1067 numbers exactly; ω³=1 verified as a genuine algebraic-integer identity, not a mod-n artifact | — |
| **Hearing mirror: 1, 1, 2** at k=1,2,3 | R | ord(φ mod 2^k) = 3, 6, 12, confirmed two independent routes (ring brute force + the Fibonacci identity φⁿ = Fₙφ + Fₙ₋₁, checked against `sympy.fibonacci` for n=0..19) | — |
| Hearing closed form, k=1..8: **1, 1, 2, 4, 8, 16, 32, 64** | R | quotient = 2^{k−2} for k≥2; a fast gcd-norm test and the Fibonacci-order route agree at all 8 computed points | exact fit to 8 data points, not a proof for all k |
| mod-(√5) palette = 1 | R | explicit hom O→𝔽₅ verified over all 625 ordered pairs; φ↦3 has order 4, the full order of 𝔽₅ˣ | — |
| mod-(5) palette = 1 | R | Pisano period π(5)=20 re-derived (not looked up), equals the full unit-group order, so φ alone fills the group | — |
| Shape comparison: being ~4^k vs hearing ~2^k | R | root cause = **Dirichlet unit rank**: 0 (ω has finite order 3, saturates) vs 1 (φ has infinite order, keeps growing) — **not** the shared fact "2 is inert," which is identical on both sides and controls, rather than explains, the comparison | P as a future ray-class-arc seed |
| 2I = SL(2,5) perfect ⟹ no abelian receiver for its characters | R | 120 elements, 9 conjugacy classes [1,1,12,12,12,12,20,20,30]; commutator closure = full group; matches banked B1042; contrast 2T=SL(2,3), commutator = Q8 (order 8), abelianized ℤ/3 | **see correction below** |

**Correction (v2).** The 2I-perfect argument answers a *different* corpus question (B1042's
McKay/trit descent), not any voice question. More sharply: **B739** — one of F11's own two source
arcs — already proved, on the being side itself, that **no** conductor-(4)/(8) Hecke character of
exactly this kind appears anywhere in the continuous spectrum ("character-rigidity," 0/3 refuted by
three independent skeptics), redirecting the whole voice question to the discrete newform spectrum
— **independently of, and prior to,** this section. So even a rich golden-side palette would not,
per the corpus's own theorem, feed a continuous-spectrum voice. The hearing mirror (1, 1, 2)
computed here is a genuine new number, but it was **unrecognized until this verification pass**
that being's palette (1, 2, 8) is not a generic ring fact — it is **B737 P3's own object-specific
voice datum**, the one feeding lead L2 (see §Honest gaps).

---

## The orders

Orders ℤ+fφℤ of ℚ(√5), f = 1..5 (and f = 8 by extension), exact.

Preliminaries (**R**): h_K=1 re-derived (Minkowski bound); N(φ)=φφ′=−1 confirmed symbolically; no
unit strictly between 1 and φ found in a bounded scan (|a|,|b|≤3 here — a smaller box than
§Structure's row 1, same non-proof caveat).

| f | disc | unit index [O_K^×:O_f^×] | h_wide | h_narrow | status | note |
|---|---|---|---|---|---|---|
| 1 | 5 | 1 | 1 | 1 | R | O₁=O_K, baseline |
| 2 | 20 | 3 (odd) | 1 | 1 | R | **corrects B92's stated h=2** — see below |
| 3 | 45 | 4 (even) | 1 | **2** | R | first narrow≠wide instance; PARI/Sage cross-validated |
| 4 | 80 | 6 (even) | 1 | **2** | R | direct numeric analog of B1064 gate-1's ℤ+4ωℤ |
| 5 | 125 | 5 (odd) | 1 | 1 | R | conductor = the field's own ramified prime; the Kronecker factor degenerates cleanly |
| 8 | 320 | 6 (even) | **2** | **4** | R | = B666/cellW35's own m=4 order — the one case where h_wide ≠ 1 |

**The unifying mechanism**, stated once (**C**, classical; **R**, verified at every row via
Fibonacci rank-of-apparition matching each index — F₃=2, F₄=3, F₆=8, F₅=5, and 8's own rank is also
6): unit index **odd** ⟺ φ^{index} has norm (−1)^{odd}=−1 ⟹ O_f^× contains a norm-(−1) unit
⟹ h_narrow = h_wide; unit index **even** ⟹ no such unit ⟹ h_narrow = 2·h_wide.

**The B92 correction.** `B92_metallic_classification`'s own self-audit states h=2 at disc 20 (its
"m=4" companion order) via Sage `BinaryQF_reduced_representatives(20)` with no flags → 2 forms, the
second **imprimitive** (content gcd=2, literally 2×the disc-5 principal form); `primitive_only=True`
(not used by B92) leaves 1. An algebraic identity closes the loop: λ₄ = 2+√5 (root of B92's own
x²−4x−1 at m=4) satisfies ℤ[λ₄] = ℤ[√5] = ℤ+2φℤ **exactly** — B92's "m=4" order **is** this
table's f=2 order, same ring, true h=1 (PARI `qfbclassno(20)`=1). **R** — the bug is reproduced
directly, not merely alleged; v1 independently re-verified it "exactly as described" (§Verification).
No test in the repo locks the h=2 claim (grepped, zero hits) — nothing load-bearing breaks; a short
correction note upstream on B92's own FINDINGS.md would close this, not made here (read-only bench).

**The structural half.** ℚ(√5)'s total reality bars it, by type, from ever being End(Λ) of a
complex 1-torus — see §Structure's Typing subsection, cross-referenced rather than repeated. Per
grep, stated in that explicit form for the first time.

**The banked real-multiplication analog.** Two already-banked, independently-parameterized
constructions land ℤ²'s multiplier ring in a non-maximal ℚ(√5) order: (1) B92's companion matrix
M_m=[[m,1],[1,0]], Latimer–MacDuffee multiplier ring ℤ[λ_m]; at m=4, = O₂ (f=2, disc 20, identity
verified above). (2) B666/cellW35's independently-parameterized bundle word; at its own m=4, lands
on f=8, disc 320 (the f=8 row above). **R** (the identity + the f=8 computation) + **C** (the two
constructions themselves, quoted). Caveat: B92's "m" and B666's "m" are *different*
parameterizations sharing only the label "4" by coincidence — order-conductors differ (2 vs 8)
precisely because the constructions differ; neither is B997's m²+4 shadow-modulus sense; neither
arc uses "multiplier ring," a Gram matrix, or period-lattice language explicitly.

**Citation-precision correction (v2), flagged prominently.** This section's own notes claimed a
grep for `'multiplier ring'` returns "exactly 3 files, all three the B1012/B1064 case." **Rerunning
that grep returns 8 files** — including `frontier/B737_candidate_zero/p3_sister.py:123,142`
("multiplier ring of ℤ+2√−3ℤ is the ORDER ℤ+4·O_K"), **B737's own working script**, using the
identical construction and vocabulary as B1064 gate-1. This is the **specific, locatable miss** that
explains why this material never connected its own CM-type-obstruction result to F11 despite
searching the one phrase that would have led there directly (see §Honest gaps).

**B214's WRT period law** detects f=3 and f=8 structure via a genuinely *computed* period, not just
a ring label: t=7, D=45, f=3, periods {45,15} (**test-locked**,
`tests/test_b214_general_word_period_law.py::test_conductor_split_refinement`, both assertions
pass). t=18, D=320, f=8, periods {80,40} (stated in FINDINGS, arc-computed, **not** independently
lock-tested in the current test file). **C** (B214 itself) + **R** (the D=45/f=3 and D=320/f=8
matches to this table's own rows, cross-checked here). Caveat: B214 reports only 2 periods {80,40}
at f=8 while this table's h_narrow(O₈)=4 — not necessarily a contradiction (a trace-valued period
can be coarser than the class group), but the exact collapse mechanism is **unresolved** by either
B214 or this bench — "the exact split divisor d|f per class is the open question," B214's own
words.

**Verdict.** YES, with a type-shift and two caveats. A banked golden-side ℤ²-lattice object
(companion-matrix / bundle-word) **does** have a non-maximal-order multiplier ring at specific
members (f=2, f=8, both found at "m=4" in two independently-parameterized banked families), and
B214 shows this is detectable by an actual computed period invariant. Caveat (a), structural: this
is **real multiplication** on a real ℤ²-lattice, never CM on a complex cusp torus (barred by
K⊗ℝ≅ℝ×ℝ). Caveat (b), provenance: the identification "companion/bundle order = multiplier ring" is
**this document's own reading**, connecting three never-before-assembled banked arcs
(B92, B666/cellW35, B214) — **P**, would need its own preregistration to bank. Closes the exact gap
B1067 named ("orders by conductor: present only piecemeal") — see §Honest gaps.

---

## Verification pass

**v1** — 10 targeted re-derivations of this document's own arithmetic, independently rebuilt from
the raw claims, several cross-validated against PARI/GP and Sage as a second computer-algebra
oracle. **10/10 CONFIRMED**, no discrepancies:

Cl_(4) = ℤ/2×ℤ/2 non-cyclic (element-order check [2,1,2,2]) · Cl_(3) = ℤ/2 · Cl_(√5) = ℤ/2 ·
hearing palette 1,1,2 · being palette 1,2,8 (and matches the actual repo file content directly —
`frontier/B1067_rayclass_harvest/FINDINGS.md:25,42` and `w1_results.json` — not just a paraphrase
of it) · order class numbers at f=3 (1/2) and f=4 (1/2), PARI-cross-validated · the B92/f=2
correction reproduced exactly (imprimitive form, true h=1) · N(φ)=−1 ⟹ Cl⁺(K)=Cl(K)=1, PARI
`bnfnarrow` returns `[1,[],[]]` directly · splitting census 5-ramifies/3-inert/11-splits matches
the banked frame exactly · mutual blindness confirmed both directions.

**v2** — 17 checks at the framing/citation/synthesis level, a genuinely **mixed** verdict; every
correction below has already been folded into the relevant section above.

*Confirmed true (6 of 17; 5 more — the "GAP" confirmations — are folded into §Honest gaps below
rather than repeated here):* F11's own identity/status grounding · being's palette (1,2,8) **is**
B737's own object-specific voice datum, real contact with F11's apparatus, unrecognized until this
pass · the CM type-obstruction (totally real ⟹ never CM) is sound, decisive, and — per its own
grep — new to the corpus in this explicit form · the Hilbert-modular/real-multiplication route
remains genuinely open, not ruled out · both top-level syntheses (the "touch, not explain" split
verdict on F11; the 5-item honest-gaps list, below).

*Corrected (6 of 17), each addressed at point of use above:* this document constructs **no**
voice/L-function object anywhere (§Palette's L(1,χ₅) is a structurally different object) · none of
the six source sections cites F11/B746/B737/B739 by name — this document is the first to state the
connection explicitly · a citation-precision check on this document's own cross-references found
two slips (folded into one v2 check): the "multiplier ring" grep undercounted 3 files as 8, missing
B737's own script (§Orders), and a B1042 line was formatted as a verbatim quote when it is in fact a
fair paraphrase (the actual line 35 reads "SL(2,5) is PERFECT"; the characters/rotation/trit clause
is on line 37) · the "perfect 2I ⟹ no abelian receiver" argument does **not** settle F11 — B739's
redirect does the real work (§Palette) · "2 is inert" is **not** the cause of the being/hearing
palette-shape divergence — Dirichlet unit rank is (§Palette) · the orders-by-conductor tower is
**no longer a gap** — B1067's "present only piecemeal" flag is genuinely closed by §The orders.

---

## The honest gaps

**Still open (5), reconfirmed after this document:**

1. **ζ_K special values beyond s=1.** No ζ_K(0), no ζ_K(−1); B1067's flagged link to B366's real
   1/30 spin-twist shift (confirmed present, `frontier/B366_invariant_spin_sector/s_transformation.py:31`)
   is still unjoined.
2. **Explicit ray class fields and concrete Artin reciprocity.** §Structure computes only abstract
   group *orders* (1, 2, 4, ...) at 5 moduli — no generating polynomial, unlike being's closed loop
   (explicit H₋₄₈(x) identified with ℚ(ζ₁₂)).
3. **The different ideal 𝔡_{K/ℚ} = (√5).** Never named or used; the ramified factorization
   (5)=𝔭² stops short of it.
4. **Fundamental-unit minimality of φ, proved unconditionally.** Every claim in this document rests
   on a bounded box search (≤30, ≤3); the one continued-fraction attempt was mis-executed and
   honestly dropped (§Structure, row 1).
5. **K-theory, local completions/root numbers, and any genuine discrete-spectrum automorphic
   object for ℚ(√5).** Untouched anywhere below. Per B739, this is **exactly** the layer — the
   discrete newform spectrum, "owner-gated, Hejhal-class" — where even the being-side voice
   question (F11) itself remains open: the single most on-point missing piece for any future
   golden-side analogue.

**Closed by this document (1):** the orders-by-conductor tower, B1067's own flag ("present only
piecemeal: B92... B214... B666-W35..."), is now unified into one f=1..5(+8) table with wide **and**
narrow class numbers, PARI/Sage cross-validated, including a live correction to B92 (§The orders).

**Precision corrections surfaced by verification, reported rather than hidden:**

- The `'multiplier ring'` grep undercount (3 files claimed → 8 actual) is the specific, locatable
  reason this material touched F11's own construction (B1064/B737 share the same m004 cusp object)
  without ever recognizing the adjacency. The one-line grep fix is trivial; making the recognition
  itself is **out of this document's remit** — it is exactly the kind of construction step reserved
  for W2/W3, not this census.
- A B1042 citation was formatted as a verbatim quote when it is a fair paraphrase (line 35 vs the
  actual clause on line 37). Does not change the substantive math; flagged for precision, per rule
  12 ("report faithfully").

**Restating the frame.** This document does not resolve F11; it structurally closes one candidate
route to a golden-side analogue of the being-side CM construction (§Structure's Typing subsection)
while leaving the actual GL(2) analogue — Hilbert modular forms for ℚ(√5) — completely
unattempted, not shown impossible. No descent claims are made; no physics is touched; ℚ(√5)'s
arithmetic is never merged with K's.

---

## Fences

Read-only against `(home)/origin-axiom` throughout (Read/grep only, per the source material's
own repeated statements and this assembly pass); all computation lives in the session scratchpad
(python3/sympy, cross-validated against PARI/GP and Sage where noted). No PR, no
PREREGISTRATION, no hash — this document is itself unbanked exploratory scratch, offered as a
candidate biography draft, not a filed arc. The K/√5 field-tag discipline (C[K] vs the fresh
computation) is held in every row above. No descent claims (W2/W3's task, not this one's); no
physics; no claim anywhere that ℚ(√5)'s splitting or unit-group behavior equals K's.
