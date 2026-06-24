# B204 — novelty / prior-art assessment (adversarial deep-research, 2026-06-24)

**Bottom line: the framework and the proof mechanism are KNOWN prior art (Jeffrey 1992). The explicit
`(a,b)`-period formula and the metallic-reality observation are at best a new explicit corollary /
specialization — NOT a new phenomenon — and even that is `NEEDS-SPECIALIST` (the period likely falls out of
Jeffrey's 1992 Gauss-sum formula by inspection).** An adversarial 99-agent deep-research pass (5 angles, 17
primary sources, 25 claims 3-vote-verified) found the anticipated reference and deflated the novelty.

## A framing correction (verified, banked here)

`Z_k(R^a L^b) = tr(ρ_k(R^a L^b))` with the closed-torus Kac–Peterson `S,T` is — by Turaev (Funar 2013,
Geom. Topol. 17, Lemma 3.2: `RT_C(M_A)=Tr(ρ_C(A))`) — the WRT invariant of the **mapping torus of the CLOSED
torus** `T²` with monodromy `A=R^a L^b` (a Sol 3-manifold for `|Tr|>2`). This is **Jeffrey 1992's object.**
It is *not* the WRT invariant of the cusped hyperbolic once-punctured-torus bundle (e.g. the figure-eight knot
complement for `RL`); those share the **monodromy** `R^a L^b ∈ SL(2,ℤ)=MCG(Σ_{1,1})` but are different
3-manifolds. So B204's earlier "once-punctured-torus bundle" phrasing is imprecise: the **monodromy family**
is metallic/`R^m L^m`; the **invariant** `Z_k` is the closed-torus mapping-torus (Jeffrey) invariant. The
result (the period of `tr(T^a S T^-b S^-1)`) is unaffected — only the topological label is corrected.

## Per-question verdicts

**Q1 — KNOWN.** WRT/RT SU(2)_k invariants of torus-bundle mapping tori = trace of the monodromy in the
SL(2,ℤ) modular representation, evaluated as **quadratic Gauss sums via Gauss reciprocity**. This is exactly
**Jeffrey, *Chern–Simons–Witten invariants of lens spaces and torus bundles, and the semiclassical
approximation*, Commun. Math. Phys. 147 (1992) 563–604** — Theorem 4.1 / eq (4.8) gives the explicit
Gauss-sum form for the hyperbolic case `|Tr U|>2` (our `R^a L^b`, trace `2+ab>2`), with normalization
`1/√|d+a∓2|` and inner sum `γ=1..|d+a∓2|`; Remark 5.1: "the mechanism is the reciprocity formula for Gauss
sums." **So our proof IS the Jeffrey method, independently re-derived** — the Gauss-reciprocity reduction is
not novel. Corroborated: Andersen–Jørgensen 2012 (arXiv:1206.2552, "by methods similar to Lisa Jeffrey … a
generalization of the quadratic reciprocity law of Gauss sums by Jeffrey [Jef92]"); Funar 2013.

**Q2 — PARTIALLY-KNOWN.** The homology-controlled level-dependence is recorded, but (i) for the **abelian/MOO
U(1)** invariant (Funar 2013: `|Z_k(M,q)| = |H¹(M;ℤ/kℤ)|^{1/2}`, with `gcd(|Tr A−2|,k)` control and
`det(A−I)=Tr−2` the H₁-torsion order), and (ii) the **congruence subgroup property** (Ng–Schauenburg 2010;
Dong–Lin–Ng 2015: `ρ_k` factors through the finite `SL(2,ℤ/Nℤ)`, `N=ord(T)`) — the abstract reason traces
are eventually periodic. **No source states the exact-periodicity-in-`k` of the SU(2)_k invariant as a
theorem**; the Jeffrey lineage pursues the *opposite* (large-`k` asymptotic / AEC / growth-rate) regime.

**Q3 — APPEARS-NOVEL but NEEDS-SPECIALIST (likely a Jeffrey corollary).** The specific
`P = lcm(a,b)(4+ab)/gcd(4+ab,4)` as a function of the word was found in no source. **But** Jeffrey's eq (4.8)
already carries **both** `|Tr∓2|` moduli — i.e. both `ab=det(A−I)` *and* `4+ab=det(A+I)` — so the period very
plausibly drops out of the **conductor of her 1992 Gauss sum** by inspection. The `4+ab=det(A+I)` (rather than
the abelian `Tr−2`) is the genuinely SU(2)_k-specific feature (the `ρ`-shift in `h_i=i(i+2)/(4(k+2))` and the
`(i+1)(j+1)` in `S`). **A specialist must check whether `P` follows directly from Jeffrey (4.8) before any
novelty is claimed.**

**Q4 — APPEARS-NOVEL but NEEDS-SPECIALIST (likely folklore).** No source singles out `a=b` (metallic/
`R^m L^m`) as where the invariant is real/periodic. Likely a known consequence of complex-conjugation/Galois
symmetry on the modular data + the palindromic/amphichiral structure of `R^m L^m` — to be checked against the
amphichiral-fibered-knot literature.

## Honest novelty tier for the package
- **Framework + mechanism (Gauss-sum reduction):** `KNOWN` — Jeffrey 1992. Our proof re-derives it.
- **Exact SU(2)_k level-periodicity with homology-set period:** `PARTIALLY-KNOWN` (phenomenon known in
  principle via congruence + abelian Funar; exact SU(2)_k statement unrecorded).
- **The explicit `(a,b)`-period formula + metallic reality:** `NEEDS-SPECIALIST` — at best a new explicit
  corollary/specialization, plausibly implicit in Jeffrey (4.8).

## What a specialist must still do (and the gaps this pass did NOT cover)
1. Check whether `lcm(a,b)(4+ab)/gcd(4+ab,4)` reads off directly from the conductor of Jeffrey eq (4.8).
2. **Two prior-art clusters were NOT retrieved and are the highest-probability hiding places** (so Q3/Q4 are
   absence-of-evidence, not evidence-of-absence): (a) the **Coste–Gannon Galois action** on WRT invariants +
   the **quantum-modular-forms** line (Zagier; Garoufalidis–Zagier; Lawrence–Zagier); (b) **Hikami / Rozansky
   / Garoufalidis** Gauss-sum / Eichler-integral evaluations (named in the query, not fetched).
3. Check the amphichiral-fibered-knot literature for the `a=b` reality fact.

## Primary-source verification — direct read of Jeffrey 1992 (2026-06-24)

Per "verify the agents, scrutinize Jeffrey" — the paper was read directly (scanned PDF, CMP 147), **not
taken on the agents' word**. Findings, all from the primary source:
- **§4.1, eq (4.3):** the SU(2) torus-bundle formula is for a **general** `U=[[a,b],[c,d]] ∈ SL(2,ℤ)`,
  `a+d≠±2` — *not* trace-only. (An earlier mid-investigation guess that her formula was the `U=T^pS`
  trace-only case was a **misreading** — that is §4.2, the general-group case — and is **retracted**.)
- **eq (4.5):** `Z(Σ_U,r;ψ(U)) = Tr ℛ(U)` — definitional. **eq (4.8)** (Theorem 4.1) is the explicit closed
  form for `|Tr U|>2`: a double Gauss sum `Σ_± (1/(2|c|√|d+a∓2|)) Σ_{β mod c} Σ_{γ=1}^{|d+a∓2|} e^{2πir(−cγ²+(a−d)γβ+bβ²)/(d+a∓2)}`,
  with the two moduli `d+a∓2 = Tr∓2 = det(U∓I)` — for `U=R^aL^b` these are exactly **`ab` and `4+ab`**. Confirms
  the deep-research's claim verbatim.
- **Matrix-level identity (airtight):** Jeffrey's S (eq 4.9) with the SU(2) inner product `⟨λ,μ⟩=λμ/2` and
  `|vol Λ^w/vol Λ^R|^{1/2}=1/√2` reduces to `√(2/r) sin(π(λ+1)(μ+1)/r)` = **our S**; her T (4.10) = our T. So
  `Tr ℛ(R^aL^b) = tr(T^a S T^{-b} S^{-1})` = **our `Z_k` exactly** (up to the projective framing phase, which
  `|·|` kills). **Our `Z` IS Jeffrey's torus-bundle invariant.**
- **Focus:** the paper's stated objective is the `r→∞` semiclassical limit; "period"/"periodic" never refers to
  the level dependence (only to alcoves / flat-connection conditions). So the **level-periodicity itself is not
  Jeffrey's subject** — but it is a corollary of her (4.8) (the period of that Gauss sum in `r`). The exact
  period is **not** a trivial denominator read-off: same-trace words differ (`Z_k(R^1L^4)≠Z_k(R^2L^2)`, periods
  8 vs 4, both trace 6 — verified), and the `(2,2)` period `4 < lcm(ab,4+ab)=8` shows real Gauss-sum
  cancellation; but it is derivable from (4.8).
- **Honest caveat:** a direct numerical re-implementation of the *evaluated* (4.8) did **not** reproduce
  `|Z_k|` (it returned reciprocal metallic-mean values, e.g. `φ` vs our `1/φ`) — an unresolved
  convention/normalization bug in transcribing her framing-laden closed form. This does **not** affect the
  conclusion: the identity `Z=Tr ℛ(U)` is established at the matrix level above, independent of (4.8).

**Net (confirmed by primary source):** the V199 deflation **stands and is strengthened** — our `Z` is Jeffrey's
invariant, the mechanism and moduli are hers, the period is a derivable (non-trivial, unstated-by-her)
corollary. The only genuine residual prior-art risk is the two **unexamined** clusters (Coste–Gannon Galois /
quantum-modular-forms; Hikami/Rozansky), where the level-periodicity may already be recorded.

## Source-hygiene note
The original B204 citation guess ("Jeffrey … J. Math. Phys. 1992 … representation of the mapping class
group") had the **wrong venue/subtitle** — corrected above to CMP 147 (1992), "…and the semiclassical
approximation." (One deep-research source URL was also mislabeled Zagier-vs-Funar, and one congruence claim on
it was refuted 0-3; the math was re-verified against the correct primary sources.)
