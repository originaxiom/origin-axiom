# B1816 — THE CANONICAL END'S ACCESSORY PARAMETER IS A WEIL–PETERSSON PRIMITIVE (P-481; T2's open question; data-free): ON ITS UNIFORMISING BRANCH, B1667's ACCESSORY PARAMETER SATISFIES ∂C/∂τ̄ = i·h_WP(τ) WITH C = 2c — CHECKED AGAINST THE FENCHEL–NIELSEN ROUTE TO 10⁻¹¹, AND ITS VOLUME CLOSES ON π²/12 — SO WEIL–PETERSSON VOLUME (DEPTH TAIL ≈ 3/(Y + 4 ln 2/π)², 0.20 AT Y = 3) STANDS BESIDE HYPERBOLIC AREA (3/(πY), 0.32) AS A FRAME-NATIVE CLOCK. NOTHING HERE RANKS THEM: THE CLOCK STAYS CHOSEN, AND NO CLOCK STUDIED PICKS A POINT

**Verdict: PROVED (computed).**
- Verified numerically:
  - to ≤ 10⁻⁸ at four points by main's 2-point stencil, an error that is the stencil's own;
  - to ≤ 4 × 10⁻¹¹ at six off-axis points by the referee's 5-point stencil, regenerated on main;
  - the total volume closes to 2 × 10⁻⁶;
  - the branch is certified by B1667's uniformisation gate at every point used.
- Consistent with McMullen's Theorem 1.5 and Takhtajan–Zograf. Derived from them modulo one step (the ℘-reference's
  holomorphy) and one normalisation convention, which the numerics fix.
- Not a proof for the punctured torus. Not preregistered.

cc (main), 2026-10-29. Refereed hostile, PASS WITH CORRECTIONS (§ 5). Data-free. **0 of 19.**

## 1. The question
- T2 (B1815 § 3(b)) found that FR-FIB, the frame that computes the masses, never sees word length. Its canonical end
  (B1667) is built from the fibre's continuous hyperbolic geometry.
- Two continuous measures on τ are canonical for that geometry:
  - **hyperbolic area:** the Teichmüller metric, defined by the conformal structure;
  - **Weil–Petersson:** defined by the fibre's hyperbolic metric.
- Does the frame's own instrument carry either one?

## 2. The relation, and the checks
- **The canonical end.** B1667's canonical end is built from the accessory parameter c(τ) of y″ + (℘(z)/4 + c)y = 0.
  This Lamé-type equation uniformises the punctured torus of modulus τ when its monodromy is Fuchsian and passes the
  uniformisation gate.
- **The claim** (the reader, `verification/WP_AT_SOURCE.md`). With C = 2c, ∂C/∂τ̄ = i·h, where
  h = ½∣∂(ℓ, t)/∂(Re τ, Im τ)∣ and (ℓ, t) are the Fenchel–Nielsen coordinates of the holonomy:
  - ℓ = 2 arccosh(x/2);
  - t = 2 arcsinh((2z − xy)/(2x));
  - x, y, z are the absolute Fricke traces.

  Equivalently, Re ∂C/∂τ̄ = 0 and Im ∂C/∂τ̄ = h.
- **The normalisation, stated explicitly.**
  - h dx∧dy = ½ dℓ∧dt is Wolpert's ω_WP = ½Σdℓ∧dτ (his 2008 survey, read by the reader).
  - In the normalisation ω = dℓ∧dt (McMullen, Mirzakhani), ∂C/∂τ̄ = (i/2)·h(dℓ∧dt).
  - The derivation from McMullen's Theorem 1.5 (stated for general S, the moduli spaces M_{g,n}) fixes this factor only
    through a pairing convention. The numerics fix it.
  - Fırat (arXiv:2306.08599 § 3.3, read by the reader and the referee) states the relation for the one-bordered torus
    (the punctured torus at L = 0) as not proven. He fixes its constant at the cusp.
- **Main's check** (`verification/verify_wp.py`, `.json`, `_out.txt`).
  - B1667's sealed instrument is imported unchanged. Central differences with step 10⁻⁴·Im τ, at four points off
    Re τ = 0, where the instrument's Newton is degenerate (the referee's τ = 1.5i gives h < 0 there).
  - Roots are continued from B1667's stored, gated roots.

  | τ | c (true root) | Im ∂C/∂τ̄ ÷ h | ∣Re∣/∣∂C/∂τ̄∣ | gate: min Im u | h | (π²/2)/(y + δ)³ | (π/4)/y² (area, same volume) |
  |---|---|---|---|---|---|---|---|
  | 0.25 + 1.2i | 0.20563 | 1 + 4 × 10⁻⁹ | 2.3 × 10⁻⁸ | — | 0.6643 | 0.5464 | 0.5454 |
  | 0.25 + 2i | 0.51624 | 1 + 5 × 10⁻⁹ | 2.6 × 10⁻⁹ | — | 0.2221 | 0.2060 | 0.1963 |
  | 0.15 + 3i | 0.65668 | 1 + 6 × 10⁻⁹ | 1.3 × 10⁻⁹ | 0.126 | 0.0870 | 0.0843 | 0.0873 |
  | 0.3 + 5i | 0.75090 | 1 + 9 × 10⁻⁹ | 2.3 × 10⁻¹⁰ | 0.115 | 0.0245 | 0.0242 | 0.0314 |

  - δ = 4 ln 2/π. The gate values come from the referee's `chk2.py`, rerun on main.
- **The referee's check** (`verification/referee/chk1.py`; a 5-point Richardson stencil with relative steps 2 × 10⁻³ and
  5 × 10⁻⁴; regenerated on main in `referee/main_rerun/`).
  - Ratio 1 − 4 × 10⁻¹¹ at 0.4 + 1.5i and at −0.2 + 1.1i; ∣Re∣/∣·∣ ≤ 1.3 × 10⁻¹¹.
  - The determinant is positive, so the absolute value hides no sign.
  - The gate (`chk2.py`) gives min Im u = 0.096, 0.116, 0.143, 0.126 and 0.115 at the true roots. The Markov relation
    holds to 10⁻¹⁴ and tr P₀ = −2.
- **The control: what the identity alone does and does not show.**
  - At 0.15 + 3i, Newton from c = 0 lands on another real-holonomy root, c = −4.1224. Its gate fails: min Im u = −0.58.
  - The two routes agree there too: ratio 1 + 9 × 10⁻⁹, ∣Re∣/∣·∣ = 4 × 10⁻¹², with h = 3.0985 against 0.0870 on the
    true root.
  - So the pointwise identity is a property of any real-holonomy branch: the holonomy pull-back of the Fenchel–Nielsen
    form. Kawai and Goldman were not read at source.
  - It is the Weil–Petersson density **of τ** only where the holonomy is the uniformisation of the torus of modulus τ.
    Two things certify that independently:
    - the gate at every point used;
    - **the volume.**
- **The volume closes** (the referee's `chk4.py` and `chk6.py`, regenerated on main).
  - Gauss quadrature of h over F ∩ {Im τ < 1} gives 0.04552443. The x-average of Re c at Im τ = 1 gives 0.04552451.
    That is Stokes with ϑ = (i/2)C dτ, which is T- and S-invariant.
  - A free fit of c out to Im τ = 15 (`chk5`, the referee's run) gives c(∞) = 0.82242. Against π²/12 = 0.822467, ∫_F h
    is Wolpert's volume π²/12 in this normalisation (π²/6 in ω = dℓ∧dt).
  - With δ fixed the fit gives B = 2.4697, against 3π²/12 = 2.4674. Here, too, nothing theoretical enters the check.
- **The depth tail,** given the relation: P_WP(Im τ > Y) = 1 − (6/π²)⟨C⟩_x(Y), exact on Y ≥ 1.

  | Y | B1667's stored grid | 3/(Y + δ)² |
  |---|---|---|
  | 2 | 0.3723 | 0.3611 |
  | 3 | 0.2016 | 0.1990 |
  | 3.5 | 0.1576 | 0.1562 |
  | 4 | 0.1267 | 0.1258 |

  - The asymptotic form's relative error falls to 1.9 × 10⁻⁴ at Y = 15.
  - π/ℓ − y approaches δ slowly (0.858, 0.863, 0.867 at Y = 3, 3.5, 4).
  - Re c is x-independent to 1.6 × 10⁻⁴ at Y = 2.

## 3. What it means
- **On its uniformising branch, the accessory parameter is a primitive of the Weil–Petersson Kähler form, not of the
  hyperbolic area form.**
  - The quantity B1667 solves for at every τ is, up to the factor fixed above, the gradient of a WP potential.
  - That is a genuine identification. The same identity holds on any real-holonomy branch, and the gate and the volume
    certify it as WP of τ.
- **It does not rank the clocks.** Hyperbolic area is equally native, through the conformal structure, and the clock
  stays CHOSEN.
  - Within FR-FIB the native continuous candidates are area and WP.
  - The move clock is foreign to the frame (T2).
- **The three clocks' depth tails:**

  | clock | P(Im τ > Y) | at Y = 3 |
  |---|---|---|
  | the move clock | ∼ 4^(−Y)/√Y | 0.035 (B1815) |
  | Weil–Petersson | ≈ 3/(Y + 0.88)² | 0.20 |
  | hyperbolic area | 3/(πY) | 0.32 |

  The fitted strip (Im τ ≈ 3, a choice-dependent fit, P-373) is an ordinary tail under either frame-native clock. This
  is a statement about typicality; it compares no data.
- **No clock studied here selects a point.** The WP-to-area density ratio ρ = h·y² is:
  - 0.961 at i;
  - 0.966 near ω, its maximum, a 0.5% variation (the referee's `chk7`, regenerated on main);
  - 0.957 at 0.5 + 1.2i, 0.889 at Im τ 2 and 0.783 at Im τ 3, falling to 0 into the cusp.

  It is not constant, but the variation is far too small to select anything.
- **The flows.**
  - The Fenchel–Nielsen twist and earthquake flows preserve WP. The WP geodesic flow on M(1,1) is ergodic (Burns–Masur–
    Wilkinson, read by the reader).
  - The Teichmüller and horocycle flows preserve area.
  - A frame-native dynamics on τ, if one exists, would therefore be a WP flow or a Teichmüller flow. Door A's horocycle
    flow stays CHOSEN (B1815 T3).

## 4. Scope
- FR-FIB's canonical end (B1667's instrument), the once-punctured torus, and points off Re τ = 0.
- The identity is verified numerically:
  - at 4 + 2 points on main;
  - at 13 by the reader's scratch check;
  - with one off-branch control;
  - with volume closure.
- Derived from McMullen through one step and one normalisation not found stated in any source.

## 5. The referee (hostile, read-only; `verification/referee/REPORT.md`; checks regenerated on main in `referee/main_rerun/`)

**Verdict: PASS WITH CORRECTIONS.** All corrections are applied.
1. **OK.** The identity was regenerated with an independent 5-point stencil at new points (including Re τ < 0) to 10⁻¹¹.
   Main's 10⁻⁸ offsets are its own stencil's error.
2. **OK.** The branch is the uniformising one: gate positive at every point; the control fails it. **MINOR, applied:**
   `verify_wp.py` does not call the gate itself; the gate values come from `chk2`.
3. **Wording, applied.** The identity holds on any real-holonomy branch, so "WP of τ" rests on the gate and the volume.
4. **OK, applied as a strengthening.** The volume closure.
5. **OK.** The tail table and δ.
6. **MINOR, applied.** The normalisation's provenance (the factor ½ fixed numerically).
7. **Literature.** Fırat confirmed. "Monte Carlo volume" was not found in his text, so the draft's phrase is dropped.
   McMullen's theorem is stated for general S.
8. **CONFIRMED-PROBLEM, applied.** The draft's "monotone, no interior extremum" was vacuous: the raw density is not an
   invariant. Replaced by the invariant ratio ρ.
9. **MINOR, applied.** "PROVED" is scoped to what is verified.
10. **CONFIRMED-PROBLEM, applied.** The draft's label "ADMITTED by naturality" did not discriminate between WP and area.
    Replaced by the identification itself.

## Seen first
`VERDICT topic-sweep /Weil.Petersson|accessory parameter|Liouville action|Zograf|Takhtajan|Fenchel.Nielsen|Wolpert/ (full text): 4 of 1562 arcs on main match (NEGATIVE 1, PROVED 3); 3 register rows match (DONE 1, QUEUED 2)`.

**Bearing on it:**
- B1667 (the instrument);
- B21 (the Goldman/Weil–Petersson bracket on Fricke–Vogt coordinates, the same symplectic structure);
- B1815 (T2, T3);
- P-481 (this arc's question), P-439, P-185.

B737 matches only on a word.

**Literature:**
- Read at source:
  - by the reader: McMullen (Annals 2000; arXiv:math/0010022); Wolpert (arXiv:math/0502528, arXiv:0801.0175);
    Burns–Masur–Wilkinson (arXiv:1004.5343); Wright (arXiv:1905.01753); Park–Takhtajan–Teo (arXiv:1508.02102);
  - by the reader and the referee: Fırat (arXiv:2306.08599).
- Not read: Takhtajan–Zograf's 1987 originals; Kawai (1996); Goldman (1984); Keen–Rauch–Vasquez (1979).

## Files
- `verification/verify_wp.py` → `verify_wp.json`, `verify_wp_out.txt`: main's check.
- `verification/WP_AT_SOURCE.md`: the reader's literature report, with `reader_scratch/` (its unsealed 13-point check).
- `verification/referee/`: the report, `chk1`–`chk7`, and `main_rerun/`.

The lock: `tests/test_b1816_the_canonical_ends_accessory_parameter_is_a_wp_primitive.py`.
