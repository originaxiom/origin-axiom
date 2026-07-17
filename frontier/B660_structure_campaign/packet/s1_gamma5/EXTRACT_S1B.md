# S1b — EXTRACT: Γ₅′ = SL(2,5) = A₅′ representation-theoretic data

Prereg: `PREREG_SQ.md` (sha 711773fe), S1 clause (b). Sources fetched as full PDF text
(not abstracts/summaries) via arXiv:
- **[WYZ]** Wang, Yu, Zhou, "Double Covering of the Modular A₅ Group and Lepton Flavor
  Mixing in the Minimal Seesaw Model," arXiv:[2010.10159v2](https://arxiv.org/abs/2010.10159),
  Phys. Rev. D **103**, 076005 (2021). Read in full: title through Appendix B (pp.1–40 of 42;
  pp.40–42 are the reference list only, not read).
- **[YLD]** Yao, Liu, Ding, "Fermion Masses and Mixing from Double Cover and Metaplectic
  Cover of A₅ Modular Group," arXiv:[2011.03501v2](https://arxiv.org/abs/2011.03501),
  Phys. Rev. D **103**, 095013 (2021). Read pp.1–50 of 63 (through Appendix B, Kronecker
  product tables). **Not read**: pp.51–63 = Appendix C (theta-constant/Klein-form identity
  proofs) and Appendix D (explicit polynomial expressions of weight-4/5/6 forms and
  higher rational-weight forms) — these are pure formula listings per the paper's own
  §1 outline, not narrative claims, but I did not verify their contents directly.

Both papers were fully accessible (no paywall issue) once fetched as PDF and read via
page-image OCR; WebFetch's HTML-conversion pipeline could not parse the raw PDF stream,
so all data below comes from directly reading the rendered pages, not from a summarizer.

---

## 1. THE IRREP INVENTORY

Both papers agree exactly (same group, same character table). A₅′ = SL(2,5) has 120
elements, 9 conjugacy classes, 9 irreps: **1, 2̂, 2̂′, 3, 3′, 4, 4̂, 5, 6̂** (dimensions
1,2,2,3,3,4,4,5,6; sum of squares = 1+4+4+9+9+16+16+25+36=120 ✓).

Verbatim [WYZ §2.2, p.5]: *"The A′₅ group has 120 elements... nine distinct irreducible
representations, which are normally denoted as **1**, **2̂**, **2̂′**, **3**, **3′**, **4**,
**4̂**, **5** and **6̂** by their dimensions... the representations **1**, **3**, **3′**,
**4** and **5** with R=𝕀 coincide with those for A₅, whereas **2̂**, **2̂′**, **4̂** and
**6̂** are unique for A′₅ with R=−𝕀."* (R = S² is the central element that distinguishes
the double cover from A₅; identical statement appears in [YLD §2.2].)

**Galois-conjugacy of 2̂ and 2̂′**: NOT stated in prose in either paper — neither uses the
words "Galois" or "conjugate" to describe the 2̂/2̂′ pair. However, the printed character
tables ([WYZ Table 4, p.25] and [YLD Table 10, p.38], numerically identical) show the
relation implicitly: for irrep **2̂**, χ(12C₅)=−φ, χ(12C₅′)=1/φ; for irrep **2̂′**,
χ(12C₅)=1/φ, χ(12C₅′)=−φ — i.e. the two representations' character values are exactly
swapped between the two classes of order-5 elements under φ↔1/φ, with φ≡(1+√5)/2 defined
explicitly in both papers. This φ↔1/φ swap is the same structure that relates the ordinary
A₅ pair **3**,**3′** (χ(12C₅)=φ vs 1−φ) and the A₅′-only pair **4**,**4̂**. I am NOT
asserting this equals "√5↦−√5 Galois conjugation" in the strict field-automorphism sense
used elsewhere in the literature — that identification is standard folklore for A₅-type
groups but is not derived or named as such by either [WYZ] or [YLD]; it is a fact I read
off their character table, not a claim either paper makes.

The rep matrices [YLD Table 10 = WYZ Table 11] give explicit ρ(S) for **2̂**:
`(i/⁴√5)·[[√φ,√(φ−1)],[√(φ−1),−√φ]]`, ρ(T)=diag(ω²,ω³); for **2̂′**: ρ(S) with rows/cols
swapped `[[√(φ−1),√φ],[√φ,−√(φ−1)]]`, ρ(T)=diag(ω,ω⁴), ω≡e^(2πi/5). Both have ρ(R)=−𝕀₂ₓ₂.

---

## 2. THE WEIGHT TABLE

Both papers construct the SAME dimension-of-form-space table for level 5 (dim ℳ_k[Γ(5)]
= 5k+1) and decompose it into A₅′ irreps identically. Verbatim reproduction of
[YLD Table 1, p.7, "Summary of integral weight modular forms of level N=5 up to weight 6"]
(WYZ builds the identical content via prose subsections "For weight three/four/five/six..."
in §2.4, pp.8–10, without a single consolidated table — I cross-checked every entry and
they match):

| weight k | irreps present (dim total = 5k+1) |
|---|---|
| 1 | **6̂** (dim 6) |
| 2 | **3**, **3′**, **5** (dim 11) |
| 3 | **4̂**, **6̂**(×2, labeled 6̂I,6̂II) (dim 16) |
| 4 | **1**, **3**, **3′**, **4**, **5**(×2, 5I,5II) (dim 21) |
| 5 | **2̂**, **2̂′**, **4̂**, **6̂**(×3, 6̂I,6̂II,6̂III) (dim 26) |
| 6 | **1**, **3**(×2), **3′**(×2), **4**, **4̂**(×2), **5**(×2) (dim 31) |

**Key finding**: the two 2-dimensional irreps **2̂ and 2̂′ FIRST appear at weight k=5**,
not at weight 1 (weight 1 is pure **6̂**). This is directly shown by both papers'
explicit construction, not inferred: WYZ derives Y₂̂^(5) and Y₂̂′^(5) explicitly by name
in §2.4 eq.(2.24) [p.9]; YLD's Table 1 lists them at k=5 only.

**Odd/even weight ↔ primed/spinorial statement**: WYZ derives (eq.2.10-2.11, p.5) that
ρ_r(R)=(−1)^k, i.e. R = +𝕀 for even k, R = −𝕀 for odd k, in any given irrep multiplet.
Combined with the §1 fact that {1,3,3′,4,5} have R=𝕀 and {2̂,2̂′,4̂,6̂} have R=−𝕀, this
jointly implies (I am combining two separately-stated facts, not quoting a single
sentence): the four "primed/spinorial" R=−𝕀 irreps 2̂,2̂′,4̂,6̂ can only appear at ODD
weight, and the five R=𝕀 irreps 1,3,3′,4,5 only at EVEN weight. The table above confirms
this exactly (k=1,3,5 odd → only 2̂,2̂′,4̂,6̂ appear; k=2,4,6 even → only 1,3,3′,4,5
appear). Neither paper states the odd/even split as a single headline sentence — it is
a direct logical consequence of two facts each paper does state plainly, and the table
verifies it holds at every weight up to 6.

---

## 3. THE q-EXPANSIONS

**Weight-1 sextet Y₆̂^(1)** — the actual lowest-weight A₅′ modular multiplet (not a
doublet; see §2) — identical normalization in both papers [WYZ eq.2.15-2.21, p.6-7;
YLD eq.99, p.29, which YLD explicitly notes reproduces the same result "obtained from
the Dedekind eta function and Klein forms" of WYZ's method]:

```
Y1 = 1 + 5q + 10q³ − 5q⁴ + 5q⁵ + ...
Y2 = 2 + 5q + 10q² + 5q⁴ + 5q⁵ + ...
Y3 = 5q^(1/5)(1 + 2q + 2q² + q³ + 2q⁴ + 2q⁵ + ...)
Y4 = 5√2 q^(2/5)(1 + q + q² + q³ + 2q⁴ + q⁶ + ...)
Y5 = −5√2 q^(3/5)(1 + q² + q³ + q⁴ − q⁵ + ...)
Y6 = 5q^(4/5)(1 − q + 2q² + 2q⁶ − 2q⁷ + ...)
```

No φ appears in these numerical coefficients themselves (small integers and √2 only).

**Golden-ratio combinations appear in the S-transformation, not the coefficients.**
Identical in both papers [WYZ eq.2.13; YLD eq.13, both p.5]:
```
F1(τ) --S--> (−τ)^(1/5) e^(iπ/10) √(1/(√5φ)) · [φF1(τ) + F2(τ)]
F2(τ) --S--> (−τ)^(1/5) e^(iπ/10) √(1/(√5φ)) · [F1(τ) − φF2(τ)]
```
with φ ≡ (1+√5)/2 defined explicitly, where F1,F2 are the fundamental weight-1/5
generators of the whole level-5 ring (all weight-k forms are degree-5k polynomials in
F1,F2). φ also appears explicitly in the ê_i-basis S-transformation [WYZ eq.2.18, p.7]
and pervasively in the **2̂**,**2̂′**,**4̂**,**6̂** representation matrices ρ(S)
[Table 10/11, e.g. **6̂**: ρ(S) = (i/⁴√(5√5φ))·[matrix with entries √φ, √(φ−1), √(2φ),
√(2(φ−1)), 1/φ, etc.]] — i.e. φ and 1/φ=φ−1 saturate the S-matrices of every irrep with
R=−𝕀 plus the pair 3,3′,4′.

**The weight-5 doublets 2̂,2̂′ are given as closed-form polynomials in Y1...Y6, not as
separately printed q-series** [WYZ eq.2.24, p.9]:
```
Y₂̂^(5) = (√6/4)(Y1²−4Y1Y6−Y6²)² · (Y3, Y4)ᵀ
Y₂̂′^(5) = (3/4)(Y1²−4Y1Y6−Y6²) · (Y2(7Y1²−3Y1Y6−2Y6²), Y5(2Y1²−3Y1Y6−7Y6²))ᵀ
```
Substituting the printed Y3~q^(1/5), Y4~q^(2/5) series gives leading powers q^(1/5),
q^(2/5) for the two doublet components, but neither paper prints this composed series
numerically — I did not hand-expand it further to avoid presenting unverified arithmetic
as the paper's own result.

---

## 4. THE STABILIZER DATA

**This is the weakest-evidenced item.** Neither paper contains a systematic discussion of
residual symmetry at τ=i∞, τ=ω=e^(2πi/3), τ=i for the double-cover group, and I found
**no mention anywhere of "Z₁₀" or of stabilizer orders being doubled** relative to the
single-cover A₅ case. This should be reported as an absence, not filled in from outside
knowledge (the honesty rule for this task forbids reconstruction from memory).

The **only explicit residual-symmetry/stabilizer statement found in either paper**:
[YLD §5, p.26, discussing the quark-lepton unification benchmark model, eq.74]: at the
best-fit point ⟨τ⟩ = −0.499996 + 0.894400i, *"It is interesting to note that the common
value of τ is very close to the fixed point τ_ST = e^(2πi/3) which preserves a **Z₃^ST**
residual symmetry."* No dimension/order is given beyond "Z₃"; no statement is made about
what this order would be for τ=i∞ or τ=i, nor about how/whether it differs from the
single-cover Γ₅≃A₅ case. [WYZ] contains no equivalent stabilizer remark anywhere in the
pages read (full paper through Appendix B).

---

## 5. sin²θ₁₂ OUTCOMES

**[WYZ]**, single model family (L~**3**, N^c~**2̂′**, minimal seesaw), three fit
scenarios:
| Scenario | free real params | sin²θ₁₂ best-fit | fit level |
|---|---|---|---|
| General (10-param) | 10 | ≈0.3049 (θ₁₂=33.51°, [Table 3]) | 1σ, NO only |
| Case A (Λ̃=0) | 8 | 0.3316 (θ₁₂=35.17°) | 3σ only, NOT 1σ |
| Case B (γ̃=0) | 8 | 0.3009 (θ₁₂=33.28°) | 1σ, NO |

None of these is flagged by WYZ as targeting or coinciding with any special closed-form
value; each is a straightforward χ² best fit to the NuFIT central value (0.304).

**[YLD]**, systematic 720-model scan (see LIT_GATE_S1.md for full model-count context):
25 models viable at 3σ for NO (15 w/9 params + 10 w/10 params), 49 for IO (not detailed
in tables I read); individual best-fit sin²θ₁₂ across the 25 NO models range roughly
0.290–0.331 across [Tables 5–7, pp.19–22] (e.g. L₉₄=0.2975 lowest seen, L₂₀₈=0.3311
highest seen; most cluster 0.30–0.306). With generalized CP imposed, 19/25 remain viable
(9 w/7 params + 10 w/8 params, [Tables 8-9, pp.23-24]).

Two named benchmark models are closer to 0.309017=(√5−1)/4:
- **Quark-lepton unification model** [§5, eq.75, p.26]: sin²θ₁₂^l = 0.3019, using 15
  dimensionless + 4 overall-scale real parameters (19 total, both quark and lepton
  sectors simultaneously fit).
- **Metaplectic rational-weight benchmark** [§6.1, eq.106, p.31], using Γ̃₅≅A₅′×Z₅
  symmetry with weight-2/5 forms: **sin²θ₁₂ = 0.30398**, with **8 real free parameters**
  stated explicitly [p.31: "Hence this model effectively depends on 8 free real
  parameters at low energy"] (τ complex + g2/g1 complex, with α,β,γ,g1 rendered real by
  phase redefinition). This is the single closest value to 0.309017 found in either
  paper — a difference of ≈0.005 — but it is explicitly the outcome of an 8-parameter χ²
  best-fit scan over τ and g2/g1, not a value the paper derives in closed form or
  identifies with (√5−1)/4, 1/(2φ), or any golden-ratio expression. The paper does not
  comment on the numerical proximity to 0.309 at all.

---

## Honesty notes / what was not seen
- Both papers' core physics content (irreps, weight construction, model classification,
  numerical fits, appendix A group theory) was read directly from rendered PDF pages —
  high confidence, verbatim quotes marked as such above.
- YLD Appendix C (theta/Klein identity proofs) and Appendix D (explicit weight-4/5/6 and
  higher rational-weight polynomial expressions, pp.51–63) were **not read** — low prior
  that they contain new narrative claims (they are formula listings per the paper's own
  §1 outline) but this is unverified, not confirmed absent.
- The Galois-conjugacy language in §1 and the "doubled stabilizer order" question in §4
  are the two places where the founding papers say **less** than the task's framing
  hypothesis assumed — flagged explicitly rather than filled in.
