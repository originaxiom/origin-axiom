# P-NATURALVALUES — preregistration (SEALED before any comparison)

**Probe cell of THE VALUE-PROBING WAVE** (`VALUE_PROBE_WAVE_CHARTER.md`, owner: "run both
instrument and two-ended tower and all around them"). This is the "all around" leg: V-3
(B1126) already proved, exhaustively, that no *tower period / growth-rate / coefficient-ratio*
of the object equals an SM ratio. This probe asks the complementary question: do the object's
own **natural, single-level, already-published-form invariants** — the numbers that appear as
headline results in the object's own arcs, not tower asymptotics — land on any SM number?

Frozen BEFORE any comparison is run. The executing script (`naturalvalues.py`) is adversarial:
its job is to rule out matches, and to report a match only if it survives every clause below.

## A. The object-side invariant menu (frozen — EXACTLY the charter's list, no scanning outward)

Every entry below is read from an already-banked arc (never re-derived from scratch), with its
exact closed form (or, where no closed form exists, its highest-precision banked numeric value)
and provenance. This is the *entire* candidate set — nothing added, nothing dropped, from what
the charter names, except where a menu item resolves to a value **identical to** another (noted,
not double-counted) or where fair, symmetric completions are required for a signed quantity
(noted below, decided from the arc's own content, before any target-side comparison).

| # | Name | Exact form | Value (approx) | Provenance |
|---|------|-----------|-----------------|------------|
| 1 | `Vol` | 9√3·ζ_K(2)/π² = (3√3/2)L(χ₋₃,2) | 2.02988321281930725... | B1117 (32-digit verified, this bench); B1116 |
| 2 | `m(A_41)` | Vol/π | 0.64613189443890102... | B698 Leg A / B1116/B1120 (the K₃ Borel regulator, Zagier/Boyd) |
| 3 | `L(chi_-3,2)` | ζ_K(2)/ζ(2), Hurwitz-zeta closed form `[ζ(2,1/3)-ζ(2,2/3)]/9` | 0.78130201928...† | B1117/B698 (classical factorization ζ_K=ζ·L(χ₋₃,·), object-side) |
| 4 | `Lp_15a_0` | L'(15a,0) — the K₂ Beilinson regulator, level 15 | 0.251330433713252231374872566669336294636860391 | B698 Leg A / B683 `threeway.py` (sage/LMFDB 15.a7, 45 digits, cross-checked; not independently re-derived here — no elementary closed form) |
| 5 | `h_Q_sqrt_m15` | class number / genus residue h(ℚ(√−15)) | 2 (exact integer) | B698 Leg A (verified two ways: reduced binary quadratic forms + sage class group) |
| 6 | `tone_0` | 0 | 0 | LAW_MAP "the twist-frame tone law" / B641/B654/B1011 |
| 7 | `tone_1` | 1/(2φ), φ=(1+√5)/2 | 0.30901699437494742... | ditto |
| 8 | `tone_2` | 1/2 | 0.5 | ditto |
| 9 | `tone_3` | φ/2 | 0.80901699437494742... | ditto |
| 10 | `tone_4` | 1 | 1 | ditto |
| 11 | `C0_kashaev` | 3^(−1/4) = \|disc ℚ(√−3)\|^(−1/4) | 0.75983568565159254... | B1120/L180 (Kashaev tower leading coefficient) |
| 12 | `dim_g` | dim M(𝕆,ℂ) (the full build) | 78 | B904 Stage 4 (Cartan-matrix match to E₆, exact) |
| 13 | `dim_27` | dim of the minimal/fundamental rep of E₆ (the exceptional Jordan algebra J₃(𝕆), Aut=F₄) | 27 | classical (Freudenthal/Jacobson; cited, not independently recomputed here) — the real form is E₆(−26)=EIV=M(𝕆,ℂ), and this bench's OWN signature computation (B1125/B1127: (26,52) split, 26 noncompact + 52 compact = 78) independently reproduces the "−26" Cartan index (26−52=−26), corroborating the real-form identification that carries "27" as its natural module |
| 14 | `dim_so8` | dim so(8) (the tri(𝕆) block) | 28 | B904 Stage 1 (`stage1_dims.json`: dim_soN=28) |
| 15 | `dim_u1sq` | dim tri(ℂ′) (=u(1)²) | 2 | B904 Stage 1 |
| 16 | `dim_3x16` | dim of the three 16-tiles ((𝕆⊗ℂ)₁⊕₂⊕₃) | 48 | B904 / B882 (28+2+3·16=78 ✓) |
| 17 | `lam` | λ (cross-product scale, all 3 slots) | 1 | B904 Stage 2c (`stage2c_results.json`: lam0=lam1=lam2=1, jacobi_failures=0) — genuinely solved-for alongside μ,ν in one linear system, not a pre-fixed convention (verified by reading `stage2c_final.py`: mu,nu,lam are co-equal free symbols in the same Jacobi-consistency solve) |
| 18 | `mu` | μ (tri(𝕆)-dual scale) | −24 | B904 Stage 2c (`stage2c_results.json`: mu0=mu1=mu2=−24) |
| 19 | `abs_mu` | \|μ\| | 24 | completion (see "signed-quantity rule" below) |
| 20 | `nu` | ν (tri(ℂ′)-dual scale) | −12 | B904 Stage 2c (`stage2c_results.json`: nu0=nu1=nu2=−12) |
| 21 | `abs_nu` | \|ν\| | 12 | completion |
| 22 | `det_phi` | det φ, the E₆-isomorphism determinant | −2/3 | B904 Stage 4 (`FINDINGS.md`: "0 mismatches; det φ = −2/3", exact rational, over ℚ) |
| 23 | `abs_det_phi` | \|det φ\| | 2/3 | completion |

†Numerically identical to `m(A_41)/(3√3/2π)`... — no: **identity note**: the charter's own text
states `ζ_K(2)/ζ(2) = L(χ₋₃,2)` as a classical factorization identity, and separately
`m(A_41) = Vol/π = (3√3/2π)·L(χ₋₃,2)` (B698) — so `L(χ_-3,2)` (row 3) and `m(A_41)` (row 2)
are **different real numbers** (related by the exact factor 3√3/(2π) ≈ 0.8270, not equal), and
are tested as two independent candidates. This is verified by direct computation below, not
assumed.

**Value-identity notes (declared before comparison, so no post-hoc surprise is hidden):**
`h_Q_sqrt_m15` (row 5) and `dim_u1sq` (row 15) are both the integer **2** — different objects,
same number, flagged. `lam` (row 17) and `tone_4` (row 10) are both **1** — different objects,
same number, flagged. These are reported once each as distinct candidates (each has independent
provenance and meaning) but the coincidence-accounting in Part D treats them honestly: a look-
elsewhere correction is computed on the *actual* grid, so a value that appears twice in the
candidate column contributes two rows, not hidden.

**The signed-quantity rule (declared in advance, applied uniformly to avoid cherry-picking):**
of the 23 candidates, exactly three (`mu`, `nu`, `det_phi`) are *signed by construction* — their
sign is an artefact of an orientation/basis convention in the B904 computation (Chevalley
generator normalization, a "direct sign choice" that "succeeded" per FINDINGS.md — i.e. an
arbitrary choice that could have gone the other way), not a substantive fact. Every SM target in
Part B is non-negative (couplings, angles, mass ratios, Koide). To compare fairly, **all three**
signed structure constants are tested BOTH signed and unsigned (`abs_mu`, `abs_nu`,
`abs_det_phi`) — decided here, uniformly, BEFORE any comparison is run, specifically so that if
one of the three happens to hit a target only in its unsigned form, that cannot be read as
selective dressing (the other two get the identical treatment regardless of outcome).

**Explicitly excluded from the menu (declared, so no accusation of hidden cherry-picking):**
nothing was found and left out. The one candidate that could look like an omission — the "13³"
constant / cubic-discriminant data of B854/B877/B900 ("the First Measurement Theorem") — is
**excluded** because it belongs to a *different* structure (the charge-measurement cubic étale
algebra, not the M(𝕆,ℂ)/magic-square algebra the charter names) and is not part of the charter's
stated menu; including it would be scanning outward, which the task explicitly forbids.

## B. The SM-side targets (frozen — adopted verbatim from the sealed, same-day V-3/B1126 table)

Rather than re-fetch identical external facts, this probe **adopts the already-verified,
live-sourced SM target table from `frontier/B1126_identification/b1126_compare.py`
(sealed 2026-08-21, PDG 2024 / NuFIT 6.0 / CODATA 2022, sources cited inline)**, unchanged, for
cross-probe consistency within the same wave (P-INSTRUMENT, P-TWOENDED, P-NATURALVALUES share
one frozen SM-side ledger per the charter's "~18 dimensionless ratios" ceiling). All 22 entries,
values + 1σ + source, are reproduced literally in `naturalvalues.py` Part B. Re-verified here
by inspection of the source script (not blindly trusted): every value carries an inline citation
and a disclosed uncertainty-conversion rule (CL90%→1σ via /1.645 where PDG quotes 90% CL).

Groups: (1) couplings — sin²θ_W(M_Z), α_em(M_Z) [both conventions], α_em(0) [both conventions],
α_s(M_Z); (2) CKM — Cabibbo, |Vcb|, |Vub|; (3) PMNS — sin θ₁₂, θ₂₃, θ₁₃ (NuFIT 6.0); (4) charged
lepton ratios — m_e/m_μ, m_μ/m_τ, m_e/m_τ; (5) quark mass ratios — m_u/m_d, m_s/((m_u+m_d)/2),
m_c/m_s, m_b/m_c, m_t/m_b; (6) Koide — the exact 2/3 target (σ=0) AND the empirical Q_emp from
PDG lepton masses. 22 targets total, spanning magnitude range ≈ [0.00365, 137.04].

## C. The instrument principle (identical to the charter / V-3's operational reading)

A MATCH is not "an object-invariant is numerically ≈ an SM target." Per the charter's rule 2,
comparison is **differential-first**: candidates are compared in their already-natural closed
forms (as banked), never multiplied/divided by an invented constant chosen to improve the fit.
No fitted dressing is applied anywhere in this script — every value in Part A is exactly what
its source arc already reports, full stop. A candidate reaching numeric proximity to a target
is *at most* evidence requiring a principled instrument (a listener map built from the object's
own data, calibrated on ONE input, predicting the rest) before it can be promoted past
NAMED-CANDIDATE — no such instrument exists on record connecting any Part-A domain (knot
volumes, elliptic-curve regulators, McKay tone tables, E₆ structure constants) to any Part-B
domain (electroweak couplings, CKM/PMNS mixing, quark/lepton masses). This mirrors V-3's own
adjudication machinery exactly (reused, not reinvented, for wave-wide consistency).

## D. The coincidence discipline (stated in advance, exact accounting at run time)

23 candidates × 22 targets = **506 pairs**. Per-pair chance of reaching ≥n significant figures
by pure chance, under the equidistribution heuristic already used by V-3: ~10⁻ⁿ. Expected hits
at ≥2 sig figs ≈ 506×10⁻² ≈ 5.06; at ≥3 sig figs ≈ 0.506; at ≥4 ≈ 0.0506. A pair below 2 sig
figs is NOISE, full stop. A pair reaching ≥3 sig figs is escalated to a full C-instrument
adjudication (look-elsewhere p-value computed on the ACTUAL 506-pair grid; a check of whether
the target's own measurement coarseness is doing the work; an instrument-existence search;
and a pre-commitment check). Per D(iv) (the seal's own disqualifier, inherited from V-3):
**any hit found by this exhaustive scan automatically fails strict pre-commitment** — no
specific pair is named or expected in advance in this document — so the ceiling for anything
found here is NAMED-CANDIDATE, never an outright positive, on this run alone.

**A dedicated note, entered here BEFORE running anything (not after seeing a result):** several
Part-A candidates are exact or near-exact small rationals (0, 1/2, 1, 2, 12, 24, 27, 28, 48, 78,
2/3), and two Part-B targets are themselves small-denominator exact or near-exact rationals
(Koide's 2/3 target, σ=0; and several CKM/PMNS central values that are "round" only to 3-4 sig
figs). A rational-vs-rational exact hit among a pool with several 2,3-smooth small integers is
**expected** at non-negligible rate under the null (both sides are drawn from "attractively
simple" numbers for independent structural reasons — the object's ℚ(√−3) arithmetic is 2,3-smooth
by construction (disc=−3), and Koide's target was historically chosen by physicists BECAUSE 2/3
is attractively simple) — this is registered in advance as the specific alternative explanation
to weigh against "physical," should such a hit occur.

## E. The outcomes (typed in advance; the charter's own three, operationalized)

- **A-NATURAL-VALUE-IS-PHYSICAL** — a candidate matches a target, differential-first (C),
  survives the coincidence discipline (D) INCLUDING pre-commitment, AND a principled instrument
  is identified. Prior: LOW (nothing here builds an instrument; V-3's precedent found none for
  a much larger, dedicated search). Any such finding is flagged for cc3's mandatory 3rd opinion
  before banking (owner's standing rule) — this script does not self-certify a positive.
- **NATURAL-VALUES-DISJOINT** — no candidate survives (D); the object's own natural invariants,
  like its tower periods (V-3), are disjoint from the SM's dimensionless numbers. Prior: HIGH,
  matching V-3's own honest prior and the task brief's stated expectation.
- **NAMED-CANDIDATE** — a candidate is numerically suggestive (reaches the ≥3-sig-fig escalation
  bar) but fails look-elsewhere and/or instrument-existence and/or strict pre-commitment (as
  every candidate here must, per D) — named for the record, explicitly NOT claimed, relayed to
  cc3 per the owner's 3rd-opinion rule for any positive-looking artefact.

The headline verdict is menu-wide (DISJOINT unless something truly survives); zero or more
NAMED-CANDIDATEs may be reported alongside it, exactly as V-3 reported its one near-miss
alongside its DISJOINT headline. Gate 5 throughout: no SM quantity enters any object-side
computation (Part A is fully computed, in its own code block, before Part B is ever read).
