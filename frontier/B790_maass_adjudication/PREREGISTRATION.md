# B788 — THE MAASS SPECTRUM PROGRAMME — PREREGISTRATION (sealed before compute)

Processing the Chat-1 MAASS_SPECTRUM_HANDOFF (2026-07-25) at owner-selected FULL scope:
Steps 1–3 and Tests 1–5, value-facing tests INCLUDED. Gate 5 + Gate 5-Q binding.
Sealed hash in ARTIFACT_HASHES.txt + docs/SEAL_LEDGER.md. Base-rate honesty is the first law.

Owner decision (2026-07-28): run the full handoff including Tests 1–2 (SM value matching).
Gate 5 is NOT suspended by this. Gate 5 governs what may enter CLAIMS.md; it does not forbid
a preregistered, base-rate-controlled, two-outcome COMPUTATION. Nothing from this arc reaches
CLAIMS.md. The firewall blocks overclaims, not computation.

---

## 0. The thesis conflict — declared up front, not discovered later

The handoff's thesis is "the SM values ARE spectral data of the manifold." The programme's
own banked position (B713–B716, C-chain) is that the object is **valueless**: SM values are
artifacts of the observer–object coupling, not properties of the object. These are in direct
tension. This arc does NOT presume either. It is registered as a **test of the handoff's
thesis against the banked position**, and the banked position is the null:

- **H0 (banked, the null):** the Maass spectrum of m004 is generic — no programme-field
  algebraicity, no SM matches beyond base rate, spacing consistent with the arithmetic
  expectation. Consistent with Wave-5/R6' already finding the CONTINUOUS spectrum generic.
- **H1 (the handoff):** the discrete spectrum carries knot-specific structure that lands on
  programme fields and/or SM values.

H0 is the prior. H1 must clear base rate to be recorded, and clears nothing into CLAIMS.

---

## 1. The precision gate (governs Tests 1, 2, 3) — THE CRITICAL FALSE-FAILURE CLAUSE

Tests 1–3 require individual eigenvalues r_n. Per the handoff's own Pitfall 5 and the repo's
rule 7 (an unearned negative is as bad as numerology):

- PSLQ / value matching may only run on r_n known to **≥ 20 significant digits**.
- "Not algebraic" may only be concluded from r_n known to **≥ 50 digits**, with the stated
  degree/height search bound.
- **If eigenvalues at the required precision are NOT obtainable, Tests 1–3 return VACUOUS —
  explicitly NOT "no match" and NOT a negative.** A vacuous test is recorded as
  DATA-UNAVAILABLE with the blocker named. Reporting "no SM match" from absent or
  low-precision data is a prereg violation and is forbidden by this document.

Absence of computed data ≠ absence of eigenvalues. The discrete spectrum is provably
non-empty by the Weyl law.

## 2. Base-rate control (applies to Tests 1, 2, 5)

Before any matching, the anchor set and window are enumerated and the expected chance-hit
count E is computed and PRINTED:

- Target set: SM dimensionless ratios used, stated as an explicit finite list.
- Candidate set: for Test 1, N eigenvalues (r_n and λ_n = 1+r_n²); for Test 2, the N(N−1)/2
  ratios r_m/r_n — the look-elsewhere budget scales with N², and this is stated BEFORE.
- Programme algebraic fields for Test 3: ℚ(√5), ℚ(√3), ℚ(√−3), ℚ(√15), ℚ(ζ₁₅)⁺, ℚ(√(2+φ)),
  ℚ(√φ), with PSLQ degree ≤ 8 and height bound stated.
- **Surrogate null:** the identical pipeline is run against a matched surrogate spectrum
  (GOE/GUE-sampled with the same Weyl density, and/or the sister m003's data when available).
  A HIT must beat the surrogate distribution, not merely "look close."

A match counts as a HIT only if (i) it is an EXACT algebraic identity, or (ii) its residual is
far below the chance expectation E **with a stated mechanism**. A ~0.3–1% coincidence at
base-rate density is a MISS and is recorded as such.

## 3. Per-step / per-test two-outcome criteria

**Step 1 — LIBRARY.** A: usable numerical Laplace-eigenvalue data for PSL(2,O₃) or m004
exists publicly at stated precision and count. B: only Hecke/cohomological Bianchi data exists
(no Laplace eigenvalues) ⇒ recorded as NOT-COMPUTED, not as non-existence. The Hecke-vs-Laplace
distinction is the crux and must be stated explicitly in the verdict either way.

**Step 2 — INDEX.** A: [PSL(2,O₃):Γ₄₁] computed exactly, with the congruence status and the
regularity of the cover determined. B: index indeterminate. (Pre-registered expectation: 12,
classical — this step is expected to CONFIRM, and its value is the congruence/regularity
refinement plus the spectral bookkeeping consequence, not the index itself.)

**Step 3 — COMPUTE.** A: individual eigenvalues obtained in-sandbox at ≥20 digits by some
method. B: not obtainable in-sandbox; the specific blocker is named and the arc terminates
at NEEDS-SPECIALIST **after** the in-sandbox computation is exhausted (never as a first move).

**Test 1 — direct match.** A: some r_n or λ_n matches a stated SM ratio exactly or beats base
rate with mechanism. B: no match beyond base rate. VACUOUS if §1 unmet.

**Test 2 — ratios.** A: some r_m/r_n matches beyond the N² look-elsewhere budget. B: within
budget ⇒ MISS. VACUOUS if §1 unmet.

**Test 3 — algebraicity.** A: some r_n is algebraic in a programme field at the stated degree
/height bound. B: no algebraic relation found within bounds — reported as "none within
bound D, height H", never as "transcendental". VACUOUS if §1 unmet.

**Test 4 — spectral discrimination m004 vs m003.** A: the two manifolds are distinguished by
computed spectral data, with the discriminating quantity exhibited. B: no computable
distinction found. **This test does NOT depend on §1** — it may be run on the LENGTH SPECTRUM,
which is exactly computable in-sandbox, since by the Selberg trace formula the length spectrum
and the eigenvalue spectrum determine each other.

**Test 5 — Hecke at programme primes.** A: a_p at p | 3, 5, 15 shows structure beyond
Ramanujan–Petersson genericity. B: generic. VACUOUS if no Hecke data.

## 4. Length-spectrum extension (registered addition, not in the handoff)

The handoff demotes the trace formula to a consistency check. Registered here as a first-class
cell because it is exactly computable in-sandbox where the eigenvalues are not:

- **L1:** compute length spectra of m004 and m003 to a stated cutoff; decide isospectrality.
- **L2:** complex lengths satisfy 2cosh(ℓ/2) = tr(γ) with tr(γ) ∈ ℤ[ω] for Γ₄₁ ⊂ PSL(2,O₃).
  Test whether the geodesic length spectrum is ALGEBRAIC over the programme field ℚ(√−3) —
  the exact analogue of Test 3, runnable now. Two-outcome: A each 2cosh(ℓ/2) lies in ℤ[ω]
  (exhibited); B some does not (would contradict arithmeticity — a red flag to be chased).
- **L3:** run the Test-1/Test-2 matching protocol, with the full base-rate control of §2, on
  the LENGTH spectrum instead of the eigenvalue spectrum. Same two-outcome rules. This is the
  in-sandbox realisation of the owner's "include Tests 1–2" instruction and is where the
  value-facing question can actually be decided today.

## 5. What may be banked

- Exact structural facts (index, congruence status, regularity, isospectrality, algebraicity
  of the length spectrum) → FINDINGS + LAW_MAP row if they are laws + a lock in tests/.
- Any HIT → FINDINGS + HINT_LEDGER only, pending adversarial verification. **Nothing to
  CLAIMS.md.** No SM value, no phenomenological reading, no "prediction" language.
- Any MISS → recorded as a MISS with the base-rate number that killed it.
- Any VACUOUS → recorded as DATA-UNAVAILABLE with the named blocker. Never as a negative.

## 6. Completion

Complete when: Steps 1–3 each have a verdict; Tests 1–5 each have a verdict or an explicit
VACUOUS with blocker; the length-spectrum cells L1–L3 have verdicts; and the arc states
plainly whether the handoff's thesis (H1) or the banked position (H0) is better supported by
what was actually computed.

— cc, 2026-07-28
