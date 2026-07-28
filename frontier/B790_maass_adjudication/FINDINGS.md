# B790 — MAASS SPECTRUM PROGRAMME: cc's ADJUDICATION RECEIPT (on B788)

> **RENUMBERED 2026-07-28.** This arc was originally banked as B788. **B788 now denotes the
> external Gates 0–9R Maass bank** (`frontier/B788_maass_spectrum_programme`), which carries 62
> recorded artifact hashes and internal cross-references that renumbering would break. This
> arc carries no such cost, so it moved. It is a **receipt on B788**, not a competing programme.
>
> **The sealed `PREREGISTRATION.md` is deliberately NOT edited** — its bytes are hash-pinned
> (sha256[0:16] = `d91a8b99e8170b9e`, SEAL_LEDGER) and still say "B788". Preserving a seal
> outranks cosmetic renumbering; a sealed artifact that gets rewritten is no longer sealed.
> Same for `ARTIFACT_HASHES.txt` and the compute scripts' header citations.
>
> Related receipts: **B791** (Weyl completeness criterion + independent verification of the
> B788 bank). cc3's independent Step-2 re-derivation is logged as replication in B791.

Processing of the Chat-1 MAASS_SPECTRUM_HANDOFF (2026-07-25) at owner-selected FULL scope
(Tests 1–2 included). Prereg sealed BEFORE compute: `PREREGISTRATION.md`,
sha256[0:16] = **d91a8b99e8170b9e**. Gate 5 + Gate 5-Q binding. **Nothing here reaches CLAIMS.md.**

## Headline

The handoff's thesis (H1: "the SM values ARE spectral data of the manifold") is **not
supported by anything computed**. The banked null (H0: the object is valueless; SM values live
in the observer–object coupling) **stands**. Separately, the handoff's own three-step plan is
**structurally mis-scoped** in two places, both established by computation rather than opinion.

No mathematical discovery is claimed in this arc. It is an adjudication: it settles what is
known, what is computable, what is blocked, and what the blocked thing would cost.

---

## Verdict table

| Cell | Verdict | Basis |
|---|---|---|
| Step 1 LIBRARY | **B** — no usable data | LMFDB has *zero* Laplace data for any Bianchi group; d=3 exists only at ~3 digits; m004 never computed |
| Step 2 INDEX | **A** — exact | index = 12 by Humbert volume; NOT principal congruence; library ceiling 1/12 |
| Step 3 COMPUTE | **B** — blocked | Hejhal-on-H³ not in-sandbox; NEEDS-SPECIALIST *after* exhausting what is computable |
| Test 1 direct match | **VACUOUS** | prereg §1: needs ≥20 digits; none exist. **Not** a negative |
| Test 2 ratios | **VACUOUS** | same |
| Test 3 algebraicity (eigenvalues) | **VACUOUS** | needs ≥50 digits |
| Test 4 discrimination | **A** — achieved | done *without* eigenvalues, via length spectra |
| Test 5 Hecke | **VACUOUS** | LMFDB Hecke data is weight-2 cohomological, not Maass |
| L1 isospectrality | m004 ≠ m003 | length spectra differ |
| L2 algebraicity (lengths) | **A** — exact | all 284 traces in ℤ[ω], worst dev 2.6e-15 |
| L3 value matching | **B** — earned MISS | surrogate-null calibrated |

---

## 1. Step 1 — the library route is built on a conflation

The handoff assigns CC2 a week to mine LMFDB for "Bianchi modular forms … weight 0 (Maass
forms)". **That data does not exist there.** LMFDB's Bianchi section is weight-2 *cohomological*
forms carrying **Hecke** eigenvalues a_𝔭 (Cremona's modular symbols, tied to elliptic curves).
No spectral parameter r appears anywhere, for any d. Şengün (arXiv:1204.6697), the handoff's
cited computational reference, is likewise homology-torsion / Hecke data. **The Hecke-vs-Laplace
distinction is the crux, and the handoff's Step 1 falls on the wrong side of it.**

What *does* exist:
- **Grunewald–Huntebrinker**, *Experimental Mathematics* **5**(1) 57–80 (1996), Table 3: 36
  Laplace eigenvalues for PSL(2,O₃) itself, λ up to 675. Finite-element; the authors caveat
  that the last digit is untrustworthy — **~3 significant digits**.
- **Aurich–Steiner–Then** (arXiv:gr-qc/0404020): 13,950 eigenvalues at 8–13 digits — but for
  the **Picard group d=1 only**. Never extended to d=3.
- **For m004 itself: nothing.** Recorded as NOT-COMPUTED, explicitly **not** non-existence —
  the discrete spectrum is provably infinite by the Weyl law.

Consequence: prereg §1 bites as written. Three-digit data, for the *parent* group rather than
our manifold, is exactly the regime the handoff's own Pitfall 5 calls meaningless. Tests 1–3
are **VACUOUS = DATA-UNAVAILABLE**, never "no match".

## 2. Step 2 — closed exactly, and it caps the handoff's own plan

By Humbert's formula, vol(PSL(2,O₃)\H³) = |d|^{3/2}ζ_K(2)/(4π²) = 0.169156934401608937…, and

    [PSL(2,O_3) : Gamma_41] = 2.029883212819307 / 0.169156934401609 = 12.000000000000000

exactly (Riley 1975 — confirmed, not cited). The handoff budgets CC3 half a session for this;
it is one volume ratio.

Two refinements the handoff does not have:

- **Γ₄₁ is NOT the principal congruence subgroup of level √−3.** Reducing the Riley holonomy
  mod (√−3), the image is *all* of SL(2,𝔽₃) (order 24 of 24), so Γ₄₁ surjects onto
  PSL(2,𝔽₃) ≅ A₄. Γ₄₁ and Γ(√−3) both have index 12 and are different subgroups. Any
  "restrict level-1 forms" argument must handle a non-congruence, non-regular cover.
- **The library route is capped at ~8%.** Weyl scales with volume, so level-1 Bianchi forms can
  supply at most 1/12 of m004's eigenvalues — and only those that are Γ₄₁-invariant. **~92% of
  the spectrum requires direct computation regardless.** The handoff's false-failure note only
  triggers this concern at index > 100; it should trigger at 12.

## 3. The length spectrum — what the handoff demotes is what is actually computable

The handoff files the Selberg trace formula as a "consistency check". It is the one place where
the programme's question is decidable today, because SnapPy computes length spectra exactly and
the trace formula makes length and eigenvalue spectra mutually determining.

**L1 — m004 and m003 are NOT isospectral**, despite equal volume (2.029883212819307…) and the
same trace field. Systole(m004) = 1.087070144995739 > systole(m003) = 0.862554627662061; they
share the geodesic at 1.087070144995739 (they are commensurable). This *is* the handoff's Test 4
discrimination, obtained with no eigenvalues at all.

**L2 — the length spectrum is exactly algebraic over the programme's own field ℚ(√−3).**
Using tr(γ) = 2cosh(ℓ/2), all 134 (m004) and 150 (m003) geodesic traces to cutoff Re(ℓ) ≤ 5 lie
in ℤ[ω] exactly; worst deviation 2.6 × 10⁻¹⁵.

**Honesty note: this is forced, not discovered.** Γ₄₁ ⊂ PSL(2,O₃) *makes* traces lie in ℤ[ω];
L2 is a confirmation of arithmeticity and a validation that the pipeline reproduces an exactly
known answer. Its real value is the **contrast**: the same manifold has an *algebraic* length
spectrum and a *believed-transcendental* eigenvalue spectrum. The arithmetic structure the
programme cares about lives on the geodesic side, not the spectral side.

**Trace-norm multisets discriminate.** With N(a+bω) = a²−ab+b²:
- norms present for m004 only: {4, 16, 48, 64, 112, 144} — every one ≡ 0 (mod 4)
- norms present for m003 only: {1, 9, 13, 21, 25, 37, 49, 57, 61, 73, 81, 93, 97, 109, 117,
  121, 129, 133} — every one odd
- min trace-norm: m004 = 3 (the ramified prime), m003 = 1 (a unit)

The mod-4 / odd split is recorded as an **OBSERVATION on truncated data, not a law** — it is a
pattern in one cutoff and has not been proved or checked for stability. Follow-up registered.

## 4. L3 — the value-facing test, and why the discipline earned its keep

Tests 1–2 were run in their computable form: the full matching protocol against 8 enumerated SM
dimensionless ratios, window ±10⁻³ relative, fixed **before** looking, over 2555 candidates
(70 distinct lengths, their exponentials, and all pairwise ratios).

**Four apparent matches surfaced. One of them is:**

    l_0 / l_51 = 0.2312719501   vs   sin^2(theta_W) = 0.23122        (4 significant figures)

Also `l_0/l_58 = 0.2249626 ~ sin θ_C = 0.22500` and `l_3/l_45 = 0.4741996 ~ m_u/m_d = 0.474`.

Without base-rate control, a seat banks the sin²θ_W hit as the programme's first quantitative
prediction.

**Self-correction, recorded rather than quietly fixed.** The first pass reported the analytic
budget E = targets × candidates × 2·TOL ≈ 40.9 and concluded the observation was "an order of
magnitude below chance". **That estimate was wrong** — it assumes the candidate values are
uniform near each target, and ratios ℓ_i/ℓ_j are strongly non-uniform. The prereg (§2) demanded
an empirical surrogate null precisely for this reason. Running it (`compute_surrogate_null.py`,
3000 + 1000 trials):

| null model | mean | 5–95% | observed | P(null ≥ obs) |
|---|---|---|---|---|
| Surrogate A — uniform on the observed range | 4.63 | [1, 9] | 4 | **0.658** |
| Surrogate B — Weyl-matched (density ~ e^ℓ) | 1.52 | [0, 4] | 4 | **0.094** |

So the honest numbers are 4 observed against 4.63 (uniform) and 1.52 (Weyl-matched) — not
"10× below chance". Under the more realistic Weyl-matched null the count sits at the *upper* end
of the range (90.6th percentile). That is a mild upward fluctuation, **not** evidence: it clears
no conventional threshold, there is no mechanism, and the prereg requires an exact algebraic
identity or a residual far below chance *with* a stated mechanism. Reported at its true strength
rather than at the more flattering one.

**VERDICT L3: OUTCOME B, an EARNED negative** — pre-stated window, exact data, empirical null.
This is the single most useful thing in the arc: it is a live demonstration that a 4-significant-
figure match to a real SM parameter is *expected noise* at this look-elsewhere budget. Test 2 as
the handoff specifies it (all N(N−1)/2 eigenvalue ratios) has exactly this pathology and would
have produced exactly this false positive.

## 5. Thesis verdict

**H0 stands; H1 unsupported.** Nothing computed supports "the SM values are spectral data of the
manifold". Consistent with Wave-5/R6' already finding the *continuous* spectrum generic, and with
the banked B713–B716 position that the object is valueless.

This is **not** a claim that the discrete spectrum is generic — that remains VACUOUS and
genuinely open, blocked on data nobody has computed. The honest state: the handoff's "last door"
is still shut, and we now know precisely what it would take to open it.

## 6. What the specialist question actually is (revised)

The handoff's framing is right in spirit but should be sharpened by Step 2:

> Individual Maass eigenvalues for the **figure-eight knot complement m004** = Γ₄₁\H³, where
> Γ₄₁ ⊂ PSL(2,O₃) is Riley's index-12 **non-congruence** subgroup, to ≥20 significant digits.
> Existing d=3 data (Grunewald–Huntebrinker 1996) is ~3 digits and for the *parent* Bianchi
> group; the high-precision Hejhal-type machinery (Aurich–Steiner–Then) has only been run at
> d=1. The specific gap: **extend the d=1 method to d=3 and to a fixed non-congruence
> finite-index subgroup.**

Natural contacts unchanged (Strömbergsson, Then, Şengün, Voight). Not sent — owner-gated,
alongside the pending GSWZ query.

## 7. Registered follow-ups

1. Stability of the mod-4 / odd trace-norm split under increasing cutoff (cheap, in-sandbox).
2. Whether the trace-norm multiset is a complete commensurability-class invariant here.
3. The BKL hook: JHEP 11 (2025) 160 / arXiv:2507.08788 identifies the 5D BKL billiard with
   PSL(2,O) for Gaussian **or** Eisenstein integers — d=3 is one of two, so the handoff's
   "the programme's knot and quantum cosmology share the same arithmetic group" **overstates
   specificity**. The paper is formal, with no eigenvalue tables. Recorded as a [HOOK], not a
   result.

— cc, 2026-07-28

---

# ADDENDUM (2026-07-28) — four corrections from Chat-1, the null saga, and the screening pass

Chat-1 challenged the first pass on four points. **All four are conceded.** Recorded here in
full rather than patched silently, because three of them are errors in the *permissive*
direction — the direction nobody audits, since no one re-checks a MISS.

## C1 — wrong null, permissive choice (the one that mattered)

Prereg §2 named the **density-matched** null as primary ("matched surrogate spectrum … the same
Weyl density"). The first pass reported its verdict off a **uniform** null that was never
pre-registered, and called the result "ordinary noise". That is a permissive choice.

Worse, on inspection the "Weyl-matched" null was itself miscoded: density ~e^ℓ, whereas the
prime geodesic theorem on H³ gives ~e^{2ℓ} (entropy = n−1 = 2). **Neither null reported in the
first pass was the one the prereg committed to.**

**The repair took three attempts, and the two intermediate nulls were both wrong:**

| null | mean | obs | p | defect |
|---|---|---|---|---|
| B′ parametric, corrected e^{2ℓ} | 0.56 | 5 | 0.005 | **over-concentrated** — e^{2ℓ} piles all lengths at the top of [1.09, 5.0]; ratios cluster in [0.8,1.0] and cannot reach targets at 0.005–0.47. The asymptotic density has not engaged at this cutoff (m004 counts run 16→50→134 over ℓ≤3,4,5 ≈ 2.7×/unit, not the ~5.9× e^{2ℓ} implies) |
| C empirical, unmatched | 29.25 | 5 | 1.000 | **pool-size uncontrolled** — manifolds with 200 lengths get ~20 000 ratios vs m004's 2 415 |

Reporting either would have manufactured a false alarm (p=0.005) or an over-permissive pass
(p=1.000). **A 200× disagreement between two nulls is itself the finding**: it says the
calibration, not the data, was the problem.

**Pool-matched repair (v2), and the two now agree:**

| null | mean | 5–95% | obs | p |
|---|---|---|---|---|
| C2 — 20 real census manifolds truncated to m004's 70 lengths | 1.95 | [0, 5] | 4 | **0.20** |
| D — gap-shuffle of m004's own spectrum (preserves range + gap multiset) | 5.43 | [2, 10] | 4 | **0.75** |

**CORRECTED VERDICT L3: MISS, now earned.** The ℓ₀/ℓ₅₁ ≈ sin²θ_W four-figure coincidence is
ordinary at this look-elsewhere budget. Chat-1's own figure (p≈0.07, "marginal") derived from
cc's broken e^ℓ null; under a properly matched null it is 0.20–0.75.

*Stability note:* de-duplicating lengths at 12 dp gives 88 "distinct" values, at 9 dp gives 70 —
double-precision noise in the last digits. 9 dp is used (still 6 orders tighter than the 10⁻³
window) and restores observed = 4, matching the first pass.

## C2 — "unsupported" should read "untested"

Conceded. Tests 1–3 were VACUOUS; "unsupported" implies evidence was sought on the eigenvalue
channel and not found. The honest split: **on the length-spectrum channel H1 was tested and not
supported; on the Laplace channel it is UNTESTED.** Length and Laplace spectra are related by
the trace formula, not interchangeable. The headline blurred them.

## C3 — null-scope import (the sharpest)

Conceded. B713–B716 are negatives about the **character variety, the fibre-functor torsor, and
the algebraic tower**. Making them H0 for a question about the **Laplacian's discrete spectrum**
imports a scope — the same error class as "abelianization is not a proxy", and against the
Register's own rule to cite scopes rather than headlines. The closing caveat did not repair it,
because the H0/H1 framing had already encoded a decided question. **The correct null for a
spectral question is generic-spectrum; B713–B716 is context, not the null.**

## C4 — base-rate category

Conceded. The 1-for-21 record governs **mechanism proposals** — claimed identities between
programme quantities and SM values. "Compute an object nobody has computed, under a
pre-registered protocol" is a different category. The "proposal #22" jab is **struck**.

## The screening pass (S1–S3) — the gap Chat-1 identified

**S1 — PARENT-SPECTRUM INJECTION.** Γ₄₁ ⊂ PSL(2,O₃) is a genuine **subgroup** of index 12, so a
Γ_B-invariant eigenfunction pulls back to a Γ₄₁-invariant one with the same eigenvalue:

    spec_disc(PSL(2,O_3)\H^3)  ⊆  spec_disc(m004)

**This corrects Step 1.** "m004 has never been computed" becomes *"never computed DIRECTLY;
~1/12 of its spectrum is inherited from the parent and has been in the literature since 1996."*
Rigorous consequence: **λ₁(m004) ≤ 51.014**. (Reached independently three ways — this argument,
the external bank's `SPECTRAL_STATUS` correction, and Chat-1's V₁ sector.)

**S2 — Selberg heat trace on the exact length spectrum.** Θ(t) with h(r)=e^{−(1+r²)t}: the
identity (Weyl) term dominates at small t (geo/ident = 0.0005 at t = 0.05) and the geodesic sum
overtakes by t ≈ 0.4. Pipeline consistent. **It constrains but does not determine** — the
omitted cusp/Eisenstein terms grow exactly where a λ₁ readout would need them.

**S3 — λ₁ screening.** Weyl heuristic r₁ ≈ 3.078, λ₁ ≈ 10.48; consistent with the rigorous
≤ 51.014. Screen against 9 programme anchors: nearest is π at 2.0% relative. **NOWHERE NEAR**,
and no match verdict is admissible at this precision by construction.

## Net effect on the arc's verdict

- Step 1: **corrected** (inheritance; m004 is not eigenvalue-free after all).
- Step 3: **superseded** — see the separate note on the external Gates 0–9R bank. "Blocked on
  data nobody has computed" is wrong; the blocker is wall-clock and checkpointing.
- L3: **MISS stands**, now on a null that survives scrutiny.
- H0/H1 framing: **withdrawn as scope-importing**. The Laplace channel is UNTESTED, not
  unsupported, and the discrete spectrum is not claimed generic.
