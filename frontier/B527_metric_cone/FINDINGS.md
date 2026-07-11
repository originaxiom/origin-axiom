# B527 — The complete Stein-compatible metric cone (chat3 package, verified 2026-07-12)

**What arrived.** A chat3 package (`COMPLETE_METRIC_CONE.zip`: report, handoff, reproducer, test) that
*classifies* the metrics for which M_* is a positive one-step Stein (dissipative) evolution — sharpening,
and partly narrowing, the B526 no-go. Every load-bearing claim **independently recomputed** here
(`independent_verify.py`, my own E_s basis + Lyapunov operator — not by re-running their script).
Firewalled; nothing to `CLAIMS.md`.

## Headline: metric COMPATIBILITY is solved; metric SELECTION is open
On the stable space E_s = ker ℓ^T (dim 3), M̄ = M_*|_{E_s} has all eigenvalue moduli **< 1** (the |h|, |γ|,
|γ| stable spectrum — verified [0.786, 0.786, 0.44]). So the discrete Lyapunov operator
**𝓛(S) = S − M̄ᵀSM̄** on Sym(E_s) ≅ Sym(3) (6-dim) is invertible (verified det 𝓛 = 0.193 ≠ 0), with
𝓛⁻¹(Q) = Σₙ (M̄ᵀ)ⁿ Q M̄ⁿ (verified: 𝓛⁻¹(I) equals the series sum). Hence:

- **The cone of Stein-compatible spatial metrics is 𝓒 = 𝓛⁻¹(PSD(3)), dimension 6** (interior = 𝓛⁻¹(SPD(3))).
  Its extreme rays are S_v = 𝓛⁻¹(vvᵀ), a **continuous ℝP² family** — so 𝓒 is **not polyhedral** and has no
  finite list of distinguished metrics. ⟹ **Stein compatibility alone cannot select one metric.** *(This
  follows because 𝓛 is a linear isomorphism carrying PSD(3)'s rank-1 extreme rays, parameterized by ℝP², to
  𝓒's extreme rays — verified 𝓛 invertible.)*
- **The full compatible Lorentzian family is G_{S,α} = S − αℓℓᵀ** (S ∈ int 𝓒, α > 0): signature **(3,1)** and
  **G_{S,α} − M_*ᵀG_{S,α}M_* = 𝓛(S) + α(β²−1)ℓℓᵀ > 0** (both verified). Six spatial + one timelike parameter
  = **dim 7** before the units quotient.
- **α is a coordinate/unit choice, not a prediction.** With P_t = rℓᵀ, P_s = I − P_t, T_c = P_s + cP_t:
  **T_cᵀ G_{S,1} T_c = G_{S,c²}** exactly (verified, err 1e-16) — changing α just rescales the Perron/time
  coordinate. G(r,r) = −1 sets α = 1 only by declaring one Perron step the unit of proper time.
- **The four alphabet letters are NOT equivalent null rays.** Making letter e_i null needs α_i = S_ii/ℓ_i²;
  the four values are all different (verified [7.24, 24.39, 9.31, 35.58]). No single α makes all four letters
  null — weakening "the letters are elementary light rays."

## Where the affine tetrahedral metric sits (and the B526 reconciliation)
The affine regular-tetrahedral metric **S_aff = ½AᵀA, A = I − r𝟙ᵀ/(𝟙ᵀr)** has driver
Q_aff = S_aff − M̄ᵀS_aff M̄ that is **positive definite** (verified eigenvalues [0.086, 0.273, 0.387]) ⟹
**S_aff lies in the INTERIOR of 𝓒 — it IS Stein-compatible**, but as an interior point it is *not* an extreme
ray, so its distinction comes entirely from the separate **affine-isotropy** requirement
(‖[e_i]−[e_j]‖² = const), **not from Stein evolution**.

**This narrows B526** (verified reconciliation): B526's no-go used the *Perron-weighted* metric
S_tet = D_r⁻¹(I−¼𝟙𝟙ᵀ)D_r⁻¹, whose driver on E_s has signature **(2,1)** — indefinite, so **S_tet ∉ 𝓒**
(recomputed here). So B526's "isotropy–Stein incompatibility" is **metric-specific to S_tet, not a general
no-go**: the affine isotropic metric S_aff *is* Stein-positive, and a whole 6-dim cone of Stein-compatible
Lorentzian metrics exists. **M_* CAN be a positive-Stein Lorentzian evolution — for the right metric.** The
"M_* = renormalization, not time" reading is therefore *one option, not forced by a no-go.* (B526 corrected.)

## Honest status of the metric question
| | verdict |
|---|---|
| **compatibility** (does a Stein-positive Lorentzian metric exist?) | **YES** — a 6-dim cone (7-dim with the time normalization) |
| **uniqueness** (does Stein select one?) | **NO** — non-polyhedral, ℝP² of extreme rays |
| **conditional selection** | affine regularity picks **one** spatial ray up to scale |
| **physical selection** | **UNRESOLVED** — no theorem says why physical reality must choose that ray |

This agrees with the program's standing finding (K025) that the object's trivial symbolic symmetry leaves the
metric-selection cone unconstrained: the geometry is a *compatible family*, not a *forced value*. Consistent
with PHYS-REFUTED (the object does not select the physical metric).

## Disposition
Math **correct** (independently verified); framing **honest** (compatibility yes / selection open — no
overclaim, unlike the earlier "UNDENIABLE" package). Banked as **STRUCTURE**, firewalled. The next gate is
exactly what B526's forward program named: **LOCALITY — derive the exact Rauzy neighbor/contact automaton**
and test whether the substitution/clock admits a bounded-radius reversible/unitary realization on it. Lock
`tests/test_b527.py`. Reproducers: theirs + `independent_verify.py`. Cross-refs: [[B526]] (narrowed),
[[B524]] (M_*, β, E_s), [[K025]] (metric cone unconstrained), docs/CLOSURE_2026-07-11 (PHYS-REFUTED).
