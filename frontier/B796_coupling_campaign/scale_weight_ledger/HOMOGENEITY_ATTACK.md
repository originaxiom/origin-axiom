# THE HOMOGENEITY ATTACK — adjudication of three adversarial runs against the weight ledger

Adjudicator seat, 2026-08-09. Target of attack: the claim in `FINDINGS.md` §2 —
*"A scale exists iff the object forces a relation between quantities of different
weight. Hyperbolic geometry is exactly scale-covariant, so no internal relation can
be weight-inhomogeneous, on any face. Therefore the object cannot fix R from inside."*

Three agents (geom-arith, spectral, value-layer) attacked it across ~40 banked
relations. All three chunks completed; no slice failed. Every candidate was
re-derived against `origin/main` in this seat.

---

## 1. Verdict

**The claim survives.** Not one of the three reported HITs is a scale-fixer, and no
fourth candidate emerged under adjudication. Every geometry↔arithmetic bridge in the
corpus — volume vs L-value, systole vs regulator, eigenvalue vs Weyl law, NZ deficit
vs cusp geometry, scattering residue vs covolume — reduces to the single normal form
**(metric quantity of weight w) = Rʷ × (weight-0 invariant of the discrete faithful
representation)**. That form is scale-covariant by construction and has no solution
for R; it is a *conversion*, not an *equation*. The three places where an
inhomogeneity genuinely survives R-restoration — the BTZ entropy `S = ℓ/4G₃`, the
held `core = (G·Λ)/3` (H78), and the B915/B925 GeV ladder — each import a
dimensionful constant from **outside** the object (G, M_Z). That is the claim
restated, not a counterexample: the object fixes R only in units of something it does
not own. The strongest confirmation is that the programme already ran the search
itself: `frontier/B922_lambda2_receipt/spot_checks.py:16-25` PSLQs λ₂ (weight −2)
against Vol (weight +3) with a constant term at 26 dps, |coeff| ≤ 10⁴, and returns
**clean**. What the attack did produce is **three defects in banked or pending text**,
listed in §3. None changes a number; two change a type, one is off by a factor of 4.

---

## 2. Every candidate, adjudicated

| relation | where | weights (L vs R) | agent verdict | ADJUDICATION |
|---|---|---|---|---|
| **Vol + i·CS ∈ ℂ/4π²ℤ; S(k) = exp(−(k/2π)·Vol)** | `knowledge/K006:56`; `frontier/B775_phase2_wave1/cells/P2W4-L38/_prior_v1/compute.py:83,86,198`; `docs/HINT_LEDGER.md:120` (H47) | ledger reads (+3)⊕(0) vs 0 | HIT (value-layer) | **FALSE ALARM as a scale-fixer — UPHELD as a ledger typing defect.** Verified: B775 computes this "Vol" as **Bloch–Wigner `2 Im Li₂(e^{iπ/3})`** (cross-checked against `6Λ(π/3)` and SnapPy), i.e. the Borel regulator of the shape parameters — cross-ratios of ideal points, metric-free. `K006:56` says so verbatim: *"the complex volume / CS invariant is a **dimensionless** element of ℂ/4π²ℤ."* Under `g→k²g` the holonomy rep, the shapes and the Bloch class are all unchanged ⟹ **Vol_Bloch is weight 0**. Both summands weight 0; the exponent is legal. But the ledger's table has one row "volume +3" and no row for Vol_Bloch. Fix in §3. |
| **NZ deficit vol(4₁) − vol(4₁(p,1)) ≈ C/L², C = π²·2√3 = 34.19, L² = 12+p²** | `frontier/B718_child_program/FINDINGS.md:50`; `b718_probe4_out.txt` (Richardson C = 34.17644 vs 34.18931) | +3 vs 0 as written | HIT-adjacent (geom-arith) | **FALSE ALARM as a scale-fixer — UPHELD as a dimensional mislabel.** NZ's constant is `π² × (maximal cusp AREA)`, weight +2: deficit = π²R³·A/L² = π²R³/L̂², L̂ = normalized length — homogeneous. B718's output line reads `C = pi^2 * (2*sqrt3) = pi^2 * (cusp longitude)`, typing a weight-+2 area as a weight-+1 length. Numerically undetectable because `frontier/B486_cusp_hexagonal_verdict/FINDINGS.md:10` records the maximal-cusp translations as **(i, 3.464) — meridian length 1**, so |longitude| = area = 2√3 exactly. Right number, wrong object. Fix in §3. |
| **continuous spectrum "[1/4, ∞)"** | `frontier/B735_emittance/FINDINGS.md:16`; `docs/LAW_MAP.md:170`; `frontier/B738_pathfinder_compiler/SHORTLIST.md:120`; `frontier/B738_pathfinder_compiler/kill_graph.json:2702`; `PROGRESS_LOG.md:8885` | −2 vs −2 | HIT-adjacent (spectral) | **FALSE ALARM as a scale-fixer — UPHELD as a banked numerical error.** Both sides weight −2, so scale-covariance is untouched. But the spectral bottom is ρ² = ((n−1)/2)², = 1/4 on **H²** and **1 on H³**. Internally contradicted: `frontier/B737_candidate_zero/p1_scatter.py:83` writes *"λ = 1+t², matching B735's [1,inf)"* — B737 cites a value B735 does not state. Wrong by a factor 4 in five places. Fix in §3. |
| BTZ `S = arccosh(x/2)`, x=5 → log((5+√21)/2) | `frontier/B520_handoff_verification/FINDINGS.md` §4 | 0 vs +1 | CLEARED-with-caveat | **FALSE ALARM, and the caveat is correct and important.** Stays inhomogeneous under R alone; repaired by restoring `4G₃` (a length in 3d): S = ℓ/4G₃. G is imported, so R is fixed only *in units of G*. This is the claim's own escape clause, correctly identified. |
| `core = 2π/n = (G·Λ)/3` under k=n | `docs/HINT_LEDGER.md:151` (H78 / B290) | +1 vs −1 | flagged INHOMOGENEOUS but held | **NOT a counterexample — confirmed HELD.** Verified the ledger line reads *"**HELD**: under k=n … a coincidence with the 122-order gap, **NOT banked**"*, and it imports G. Correctly firewalled. It is nevertheless the best existing sketch of what a real scale-fixer would look like (§4). |
| systole = 2 log\|λ\|, λ root of z²−κz+1, κ=(3+√−3)/2 | `frontier/B850_length_spectrum_type/FINDINGS.md` §1; `B735` fact 1 | +1 vs 0 | CLEARED | **CLEARED, re-derived here at 30 dps:** κ = √3·e^{iπ/6}, |λ| = 1.722083805739042245, 2 log|λ| = **1.0870701449957390998** ✓ banked. Repair ℓ = 2R·log|λ|. (Note the prompt's trap fires: `2·arccosh(|κ|/2)` is *not* the systole — |κ|/2 < 1; the complex trace is required.) |
| systole/entropy = 4 log φ = 4·Reg(ℚ(√5)) = 2√5·L(1,χ₅) | `frontier/B401_sixth_angle/FINDINGS.md` §P4; `frontier/B233…/verify_five.py:78`; `B416`, `B109` | +1 vs 0 **or** 0 vs 0 | CLEARED (both agents) | **CLEARED, with a label collision worth recording.** B401/B109/B416 are unambiguous: this is the **Lyapunov exponent per iterate of the trace map** — weight 0, no R anywhere. `verify_five.py:78` labels the same number *"dynamically extremal (systole 4 log φ)"*; m004's actual systole is 1.0870701…, not 1.92485…. A string in a cascade table, not a computed result; low severity, listed in §3 for completeness. |
| Vol(4₁) = 2Λ(π/3)·3 = (3√3/2)L(2,χ₋₃); Humbert; index 12; m(A_{4₁}) = Vol/π | `B250`, `docs/LAW_MAP.md:56-58,156`, `B147:95`, `B878:279` | +3 vs 0 | CLEARED | **CLEARED.** Vol = R³ × (Borel regulator). Index 12 and the covering law are vol/vol ratios, weight 0. |
| Res φ = 2√3/vol = 2π²/(9ζ_K(2)) | `docs/LAW_MAP.md:173`; `docs/THEOREM_LEDGER.md:70`; B739 | −1 vs 0 | CLEARED (pre-cleared) | **CLEARED.** 2√3 is the cusp covolume (weight +2) ⟹ +2−3 = −1; restore R⁻¹. B739's own note that covol/vol is covering-invariant is the weight-0 statement. |
| Weyl `N(r) = vol·r³/(6π²)`; scattering-corrected staircase | `frontier/B943_maass_priority_correction/verify.py:41`; `…/B792…/weyl_scattering_check.py:77,88` | 0 vs +3 | CLEARED | **CLEARED.** Standard N(λ) ~ vol·λ^{3/2}/6π²; λ^{3/2} is weight −3. Restored: N = (vol/R³)·r³/6π². The load-bearing B943 numbers are unaffected. |
| `λ = 1+r²`, λ₂ = 25.0108366633, λ₁ ≥ 3/4 | weight ledger; `B922`, `B878` | −2 vs 0 | CLEARED | **CLEARED, and decisive.** All 43 banked Maass eigenvalues are reported as **r**, which is weight 0. Twenty-five certified digits of r fix nothing about R. |
| φ(s) = Λ_K(s−1)/Λ_K(s), Λ = (√3/2π)^s Γ(s)ζ_K(s) | `…/B792…/weyl_scattering_check.py:20`; `docs/LAW_MAP.md:173` | 0 vs 0 | CLEARED | **CLEARED — trap checked.** This √3 is |d_K|^{1/2}, arithmetic; **not** the cusp covolume 2√3. |
| ℓ_ℂ(1,n) = 2πi/n + (π/√3)/n² + …; coeff = 2π/\|τ_cusp\| | `docs/HINT_LEDGER.md:151` (B290); `B286_the_seam` "scale" row | +1 vs 0 | CLEARED | **CLEARED.** Every NZ term carries one R; τ enters as a *shape*. B286's row header "scale" is a misnomer — the closing yields ℓ/R, a hierarchy. |
| slope length √(12+p²); 6-theorem crossing p > 2√6 | `B718` probe 4(b) | +1 vs 0 | CLEARED | **CLEARED.** 12 = |τ|² is the weight-0 shape; the bare "6" is 6R. |
| horoball radii 1/(2N), N an Eisenstein norm | `docs/PRACTICES.md:393`; `docs/views/VERDICT_LEDGER.md:580` | 0 vs 0 | CLEARED | **CLEARED.** Euclidean heights relative to the maximal cusp — ratios; R cancels identically. |
| B922 PSLQ basket: a·λ₂ + b·Vol + n = 0 over π², ζ(3), log φ, √21 | `frontier/B922_lambda2_receipt/spot_checks.py:16-25` | −2 / +3 / 0 | CLEARED | **CLEARED, and it is the programme's own falsifier.** A search for exactly the counterexample this attack wanted. **Clean at 26 dps, |coeff| ≤ 10⁴.** |
| B915 M_U triangle; B925 ρ₃ = M₅/M_U, M_U/M_Pl; B914 ratio table T; H-B914-DEEP √T | `frontier/B915`, `B925`, `B914`; `docs/HINT_LEDGER.md:594` | 0 vs 0 | CLEARED | **CLEARED, and B925 *supports* the claim**: *"M_U is free … recorded as the free interval — no number to bank."* B914 additionally runs its own R-restoration test (`T_gauge_invariance` under per-atom rescaling) and it passes exactly. |
| seam values ⊂ ℚ(ζ₆₀); Gram/bright-dark; ℤ/7 sine kernel; B947 holders; `m²=κ√5` | `B359`, `B361`, `B358`, `B385`, `B572/589/594/578`, `B947`, `docs/views/CLOSED_DOORS.md:61` | 0 vs 0 | CLEARED | **CLEARED.** No metric quantity appears on either side anywhere in the seam/value layer. |

---

## 3. DIMENSIONAL / FACTUAL ERRORS — correction list for cc

Three items. None changes a banked number; all three change what a number *is*.

**E1 — `[1/4,∞)` should be `[1,∞)` (five files).** The continuous spectrum of a
finite-volume cusped hyperbolic **3**-manifold begins at ρ² = ((n−1)/2)² = **1**, not
1/4 (the H² value). Correct at:
- `frontier/B735_emittance/FINDINGS.md:16` (origin)
- `docs/LAW_MAP.md:170`
- `frontier/B738_pathfinder_compiler/SHORTLIST.md:120`
- `frontier/B738_pathfinder_compiler/kill_graph.json:2702`
- `PROGRESS_LOG.md:8885`

Already inconsistent in-repo: `frontier/B737_candidate_zero/p1_scatter.py:83` cites
"B735's [1,inf)". B739, B792, B922 all use [1,∞) correctly. No downstream number is
affected (no banked computation reads the 1/4), but the emittance face's headline fact
is stated wrong in the two most-read index files.

**E2 — the NZ constant is π²·(cusp AREA), not π²·(cusp longitude).** In
`frontier/B718_child_program/FINDINGS.md:50` and `b718_probe4_out.txt`, replace
`C = pi^2 * (2*sqrt3) = pi^2 * (cusp longitude)` with
`C = pi^2 * (maximal cusp AREA 2*sqrt3)`, and state the deficit in normalized form
`vol(M) − vol(M_{p,1}) = π²/L̂² + O(L̂⁻⁴)`, `L̂ = L/√A` (weight 0). The numerical
identity holds only because m004's maximal-cusp meridian has length exactly 1
(`B486…/FINDINGS.md:10`). This is the corpus's sharpest live instance of the **2√3
trap**: the same constant is a length in B486, an area in B739/B718, and a shape
modulus |τ| in B290 — three weights, one number.

**E3 — the weight ledger's own table needs a Vol_Bloch row.** `FINDINGS.md` §"The
ledger" lists `volume +3` and `Chern–Simons 0`, which mis-grades the standard object
`Vol + i·CS ∈ ℂ/4π²ℤ` as an inhomogeneous sum and would mis-grade
`S(k) = exp(−(k/2π)Vol)`, the volume conjecture, and every L-value identity in
`LAW_MAP.md:56–58`. Add:

| weight | quantity |
|---|---|
| **+3** | Riemannian volume `vol_g` |
| **0** | **complex volume / Borel regulator `Vol_Bloch + i·CS` (function of the holonomy rep only; `vol_g = R³ · Vol_Bloch`)** |

Low severity, for the same file family: `frontier/B233_synthesis_split_and_five/verify_five.py:78`
labels the weight-0 Lyapunov exponent `4 log φ` as a "systole" (weight +1). m004's
systole is 1.0870701449957391, verified here at 30 dps. Reword the table string.

---

## 4. What a genuine scale-fixer would have to look like

For a future seat, so the next attack is cheaper. A real counterexample must satisfy
**all four**:

1. **Two weights, one equation.** `A = c·B` with weight(A) ≠ weight(B) and c a pure
   number, so `R^{w_A − w_B} = c·(B/A)` has a unique positive root.
2. **Both sides owned by the object.** No G, no ℏ, no M_Z, no l_P. Every inhomogeneity
   found in this corpus (BTZ §4, H78, B915/B925) fails here and only here — which is
   why the claim keeps surviving rather than being vacuous.
3. **Survives R-restoration.** Write both sides as `R^w × (weight-0 invariant of the
   discrete faithful PSL(2,ℂ) representation)`. If both reduce to the same power, it
   is a conversion, not an equation. This kills ~90% of candidates in one line.
4. **The weight-0 side must not be a metric quantity in disguise, and vice versa.**
   Check what each constant *is* before grading it: 2√3 is simultaneously a length, an
   area and a shape in this repo (E2); "Vol" is a volume in B250 and a regulator in
   B775 (E3); `4 log φ` is a Lyapunov exponent, not a systole (§3); `arccosh(tr/2)` is
   a length though `tr` is not.

Structurally, condition 2 is the hard one, and it is hard for a reason: R is fixed by
the *curvature normalization* K = −1, which is a choice of unit, not a fact about the
manifold. Anything that fixes it must break scale-covariance, and nothing internal to
a hyperbolic structure does. The realistic place to look is therefore not a new
identity but a face where a **second geometry** with its own natural length enters —
a physical coupling, a quantization condition on k, an arithmetic minimum with
dimensions. H78 is the shape of that hope, and it carries a 122-order gap.

---

## 5. Coverage — honest statement

**Searched.** Volume formulas (Lobachevsky, Humbert, L-values, Mahler measure,
covering index); the cusp (lattice, covolume, maximal cusp, horoball radii, shape τ);
Neumann–Zagier (core length series, volume deficit, slope lengths, 6-theorem); the
length spectrum and trace↔length relations; Laplace eigenvalues, Weyl law, spectral
gap bounds, the scattering function and its residue; entropy/Lyapunov/Anosov data;
Chern–Simons, complex volume, torsion, η; the seam/value/cascade layer; the K-layer
(K002, K006, K009, K010); `docs/LAW_MAP.md`, `docs/HINT_LEDGER.md`,
`docs/THEOREM_LEDGER.md`, `docs/views/VERDICT_LEDGER.md`, `docs/views/CLOSED_DOORS.md`;
B914/B915/B925 crossing cells. Three independent slices, no chunk failed.

**Not searched.** (a) The **speculations/** tree and `PHYSICS_BRIDGE_MAP.md` — held
material by construction, and the one place where external dimensionful constants are
deliberately in play; any inhomogeneity there is expected and uninformative, but it was
not enumerated. (b) The full `PROGRESS_LOG.md` / `CHANGELOG.md` narrative history —
searched by targeted grep only, not read; a stray inhomogeneous prose claim could
survive there. (c) Numerical near-coincidences never written down as a relation — no
systematic PSLQ was run in this seat beyond re-reading B922's, which covers λ₂ and Vol
against a 6-constant basis at 26 dps but does **not** cover systole, cusp area,
λ_parent, or the seven weight-0 observables of `FINDINGS.md` §4. (d) `frontier/`
directories outside the ~35 cells the three agents named — the frontier is large and
coverage there is by-citation, not exhaustive.

**Confidence.** High that no scale-fixer exists among *banked* relations; the
structural argument (condition 2 above) is stronger than the enumeration. Moderate
that no *stated* dimensional error remains — three were found in one pass, which
suggests the density of such errors in prose is not zero.
