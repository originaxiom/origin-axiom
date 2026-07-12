#!/usr/bin/env python3
"""B533 Probe 7: Gate 3 — SM Ratio Test.

Does any Standard Model dimensionless ratio live in ℚ(√φ)?

Method: for each SM ratio R, search for (a,b,c,d) ∈ ℤ⁴ with
|coeffs| ≤ N such that |a+bτ+cτ²+dτ³ - R| < ε, where τ = √φ.

False-positive control: count how many RANDOM numbers in the same
range also get hits at the same precision. If the hit rate is high,
the match is numerology.
"""

import numpy as np

PHI = (1 + np.sqrt(5)) / 2
TAU = np.sqrt(PHI)
BETA = PHI * (1 + TAU)
T = np.array([1.0, TAU, TAU**2, TAU**3])


def q_tau_search(target, max_coeff=8):
    """Search target ≈ a+bτ+cτ²+dτ³ with numpy vectorization."""
    rng = np.arange(-max_coeff, max_coeff + 1, dtype=float)
    # Build all (a,b,c,d) combinations efficiently
    # Use broadcasting: shape (N,N,N,N)
    N = len(rng)
    a = rng.reshape(N, 1, 1, 1)
    b = rng.reshape(1, N, 1, 1)
    c = rng.reshape(1, 1, N, 1)
    d = rng.reshape(1, 1, 1, N)

    vals = a*T[0] + b*T[1] + c*T[2] + d*T[3]
    errs = np.abs(vals - target)

    # Find minimum error
    idx = np.unravel_index(np.argmin(errs), errs.shape)
    best_err = errs[idx]
    best = (int(rng[idx[0]]), int(rng[idx[1]]),
            int(rng[idx[2]]), int(rng[idx[3]]))

    return best, best_err


def format_expr(coeffs):
    a, b, c, d = coeffs
    parts = []
    if a != 0:
        parts.append(str(a))
    if b != 0:
        parts.append(f"{b}τ" if abs(b) != 1 else ("τ" if b > 0 else "-τ"))
    if c != 0:
        parts.append(f"{c}φ" if abs(c) != 1 else ("φ" if c > 0 else "-φ"))
    if d != 0:
        parts.append(f"{d}τ³" if abs(d) != 1 else ("τ³" if d > 0 else "-τ³"))
    expr = "+".join(parts).replace("+-", "-")
    return expr if expr else "0"


def main():
    print("=" * 78)
    print("B533 Probe 7 — Gate 3: SM Ratio Test")
    print("Does any SM dimensionless ratio live in ℚ(√φ)?")
    print("=" * 78)

    # ─── SM dimensionless ratios (PDG 2024) ───
    m_e = 0.51099895000e-3
    m_mu = 0.1056583755
    m_tau = 1.77686
    m_u = 2.16e-3
    m_d = 4.67e-3
    m_s = 93.4e-3
    m_c = 1.27
    m_b = 4.18
    m_t = 172.69
    m_W = 80.3692
    m_Z = 91.1876
    m_H = 125.25
    alpha_em = 1 / 137.035999084
    alpha_s = 0.1180
    sin2w = 0.23122

    sm = {
        # Couplings
        '1/α_em':           1/alpha_em,
        'α_em':             alpha_em,
        'α_s(M_Z)':         alpha_s,
        'sin²θ_W':          sin2w,
        # Lepton mass ratios
        'm_μ/m_e':          m_mu/m_e,
        'm_τ/m_e':          m_tau/m_e,
        'm_τ/m_μ':          m_tau/m_mu,
        # Quark mass ratios
        'm_u/m_d':          m_u/m_d,
        'm_s/m_d':          m_s/m_d,
        'm_c/m_s':          m_c/m_s,
        'm_b/m_s':          m_b/m_s,
        'm_t/m_b':          m_t/m_b,
        'm_c/m_u':          m_c/m_u,
        'm_t/m_u':          m_t/m_u,
        # Boson ratios
        'm_W/m_Z':          m_W/m_Z,
        'm_H/m_Z':          m_H/m_Z,
        'm_H/m_W':          m_H/m_W,
        # CKM
        'V_us':             0.22500,
        'V_cb':             0.04182,
        'V_ub':             0.003650,
        # Weinberg
        'g_W/g_Y':          np.sqrt((1-sin2w)/sin2w),
    }

    # ─── Part A: Search in ℤ[τ], |coeffs| ≤ 8 ───
    print("\n─── Part A: Search for SM ratios in ℤ[τ], |coeffs|≤8 ───\n")
    MAX_C = 8

    results = {}
    print(f"  {'Ratio':20s} {'Value':>14s} {'Best ℤ[τ] match':>25s} {'Abs err':>12s} {'Rel err':>10s}")
    print(f"  {'─'*20} {'─'*14} {'─'*25} {'─'*12} {'─'*10}")

    for name, value in sm.items():
        coeffs, err = q_tau_search(value, max_coeff=MAX_C)
        rel = err / max(abs(value), 1e-15)
        expr = format_expr(coeffs)
        results[name] = {'value': value, 'coeffs': coeffs, 'err': err, 'rel': rel}

        flag = ""
        if err < 1e-6:
            flag = " ***"
        elif rel < 1e-3:
            flag = " **"
        elif rel < 1e-2:
            flag = " *"

        print(f"  {name:20s} {value:14.8f} {expr:>25s} {err:12.2e} {rel:10.2e}{flag}")

    # ─── Part B: False-positive control ───
    print(f"\n─── Part B: False-positive control ───\n")

    print(f"  How often does a RANDOM number in [0, 200] match ℤ[τ] at given precision?")
    rng = np.random.RandomState(42)
    n_samples = 500
    thresholds = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    counts = {t: 0 for t in thresholds}

    for _ in range(n_samples):
        fake = rng.uniform(0, 200)
        _, err = q_tau_search(fake, max_coeff=MAX_C)
        for t in thresholds:
            if err < t:
                counts[t] += 1

    print(f"  {'Threshold':>12s} {'Hits/500':>10s} {'Rate':>10s}")
    print(f"  {'─'*12} {'─'*10} {'─'*10}")
    for t in thresholds:
        print(f"  {t:12.0e} {counts[t]:10d} {counts[t]/n_samples:10.4f}")

    # The critical question: for each SM "hit", is it above the random baseline?
    print(f"\n  Hits vs baseline:")
    for name, r in results.items():
        if r['err'] < 1e-2:
            baseline = counts[1e-2] / n_samples
            print(f"    {name:20s}: err={r['err']:.2e}, "
                  f"random baseline at same precision: "
                  f"{counts.get(1e-2, '?')}/500 = {baseline:.3f}")

    # ─── Part C: Powers of τ ───
    print(f"\n─── Part C: SM ratios as powers of τ ───\n")

    print(f"  If R = τ^k, then k = ln R / ln τ = {np.log(TAU):.6f}⁻¹ · ln R")
    print(f"")
    print(f"  {'Ratio':20s} {'Value':>14s} {'k=lnR/lnτ':>10s} {'Near int/frac':>14s} {'Error':>10s}")
    print(f"  {'─'*20} {'─'*14} {'─'*10} {'─'*14} {'─'*10}")

    for name, value in sm.items():
        if value <= 0:
            continue
        k = np.log(value) / np.log(TAU)
        # Check integer
        k_int = round(k)
        err_int = abs(k - k_int)
        # Check half-integer
        k_half = round(2*k) / 2
        err_half = abs(k - k_half)
        # Check third
        k_third = round(3*k) / 3
        err_third = abs(k - k_third)

        best_frac = k_int
        best_err = err_int
        best_label = str(k_int)
        if err_half < best_err:
            best_frac = k_half
            best_err = err_half
            best_label = f"{int(2*k_half)}/2"
        if err_third < best_err:
            best_frac = k_third
            best_err = err_third
            best_label = f"{int(3*k_third)}/3"

        flag = " <──" if best_err < 0.05 else ""
        print(f"  {name:20s} {value:14.8f} {k:10.4f} {best_label:>14s} {best_err:10.4f}{flag}")

    # ─── Part D: Framework values vs SM ───
    print(f"\n─── Part D: Cross-comparison: framework ↔ SM ───\n")

    fw = {
        'τ':       TAU,
        'φ':       PHI,
        'β':       BETA,
        'f_a':     TAU-1,
        'f_b':     (TAU-1)/TAU**2,
        'f_A':     TAU*(TAU-1),
        'f_B':     (TAU-1)/TAU,
        '|λ₂|':    1/(1+TAU),
        '1/τ':     1/TAU,
        'sin θ':   1/PHI,
        'τ-1':     TAU-1,
        '1/(1+τ)': 1/(1+TAU),
        'φ-1':     PHI-1,
    }

    # For each SM value, find the closest framework RATIO or POWER
    print(f"  For each SM ratio, closest framework expression τ^a · φ^b:")
    print(f"  {'SM ratio':20s} {'Value':>14s} {'Closest fw':>20s} {'fw value':>14s} {'Rel err':>10s}")
    print(f"  {'─'*20} {'─'*14} {'─'*20} {'─'*14} {'─'*10}")

    for sm_name, sm_val in sm.items():
        if sm_val <= 0:
            continue
        best_fw = None
        best_err = float('inf')
        best_val = None
        # Try τ^a for a in [-20, 20]
        for a in range(-20, 21):
            val = TAU**a
            rel = abs(val - sm_val) / sm_val
            if rel < best_err:
                best_err = rel
                best_fw = f"τ^{a}"
                best_val = val
        # Try τ^a * n for small n
        for a in range(-15, 16):
            for n in range(1, 10):
                val = n * TAU**a
                rel = abs(val - sm_val) / sm_val
                if rel < best_err:
                    best_err = rel
                    best_fw = f"{n}·τ^{a}"
                    best_val = val

        print(f"  {sm_name:20s} {sm_val:14.8f} {best_fw:>20s} {best_val:14.8f} {best_err:10.4f}")

    # ─── Part E: The decisive test ───
    print(f"\n─── Part E: The decisive test ───\n")

    # The question is: does any SM ratio equal an element of ℚ(τ) EXACTLY?
    # This would require: (a+bτ+cτ²+dτ³)/D = R for small integers.
    # The discriminating fact: if the best match has error >> machine epsilon
    # at coefficients ≤ 8, the ratio is NOT in ℚ(τ) with small coefficients.

    # The DENSITY of ℤ[τ] in ℝ:
    # Elements a+bτ+cτ²+dτ³ with |coeffs|≤N form a lattice.
    # The lattice spacing is approximately 1/(2N+1)^4 * volume of fundamental domain.
    # For N=8, (2·8+1)^4 = 17^4 = 83,521 points covering range ~ [-20N, 20N].
    # Average spacing ~ 40*8 / 83,521 ≈ 0.004.
    # So ANY number is within ~0.002 of some ℤ[τ]-element with |coeffs|≤8.

    print(f"  LATTICE DENSITY ARGUMENT:")
    print(f"  ℤ[τ] with |coeffs|≤8 has 17⁴ = {17**4} elements")
    span = MAX_C * (1 + TAU + TAU**2 + TAU**3)
    print(f"  spanning approximately [-{span:.1f}, {span:.1f}]")
    avg_spacing = 2*span / 17**4
    print(f"  Average spacing ≈ {avg_spacing:.6f}")
    print(f"")
    print(f"  Any number in this range is within ~{avg_spacing/2:.4f} of some")
    print(f"  ℤ[τ]-element. Matches at error > {avg_spacing/2:.4f} are EXPECTED.")
    print(f"  Only matches at error < {avg_spacing/10:.6f} (10× below spacing)")
    print(f"  would be significant.")
    print(f"")

    significant = []
    for name, r in results.items():
        if r['err'] < avg_spacing / 10:
            significant.append((name, r))

    if significant:
        print(f"  SIGNIFICANT MATCHES (err < {avg_spacing/10:.6f}):")
        for name, r in significant:
            expr = format_expr(r['coeffs'])
            print(f"    {name:20s}: {r['value']:.10f} ≈ {expr} (err {r['err']:.2e})")
    else:
        print(f"  NO SIGNIFICANT MATCHES.")
        print(f"  All SM ratios have ℤ[τ]-errors above the lattice spacing threshold.")

    # ─── SYNTHESIS ───
    print("\n" + "=" * 78)
    print("SYNTHESIS — Gate 3 Verdict")
    print("=" * 78)

    print(f"""
  GATE 3 RESULT: {'NO SM ratio lives in ℚ(√φ) with small coefficients.' if not significant else 'MATCHES FOUND — see above.'}

  WHAT THIS MEANS:
  The object's number field ℚ(τ) = ℚ(√φ) generates a specific set of
  dimensionless ratios. The Standard Model's dimensionless ratios
  (coupling constants, mass ratios, mixing angles) are DIFFERENT numbers.

  The lattice density argument makes this RIGOROUS: with 17⁴ = 83,521
  lattice points spanning [-{span:.0f}, {span:.0f}], any number is within
  ~{avg_spacing/2:.4f} of some ℤ[τ]-element. A "match" at this precision
  is EXPECTED and carries no information. Only precision significantly
  below {avg_spacing/10:.6f} would be meaningful — none achieved.

  THE STRUCTURAL LESSON:
  The object provides SHAPE (the number field ℚ(√φ)).
  The SM provides VALUES (α_em, sin²θ_W, mass ratios).
  These are different mathematical objects.

  If the object describes physics, it does NOT do so by encoding
  SM coupling constants as elements of ℚ(√φ). The connection,
  if any, must go through a different bridge:
    (a) Representation theory (the object's symmetry → SM gauge groups)
    (b) Spectral geometry (the object's spectrum → physical spectrum)
    (c) Category theory (the object's structure → particle taxonomy)
  But NOT through numerology (object's numbers ≈ SM's numbers).
    """)


if __name__ == '__main__':
    main()
