#!/usr/bin/env python3
"""
Standard Model gauge coupling RGE running (pure gauge content, no thresholds).

Runs measured PDG-2024 central values of the SM gauge couplings at M_Z
up to declared reference scales, at 1-loop and 2-loop (gauge-only 2-loop
matrix; no Yukawa/quartic contributions; no intermediate thresholds).

GUT normalization: alpha_1 = (5/3) alpha_Y.

Values only. No comparison to any framework/theory quantity is performed
here -- this script produces frozen numerical targets for a later, separate
sealed comparison.
"""
import math

# ----------------------------------------------------------------------
# Inputs: PDG 2024 central values at M_Z
# ----------------------------------------------------------------------
alpha_em_MZ   = 1.0 / 127.951
sin2thW_MZ    = 0.23122
alpha_s_MZ    = 0.1180
M_Z           = 91.1876  # GeV

# ----------------------------------------------------------------------
# Convert to GUT-normalized alpha_1, alpha_2, alpha_3 at M_Z
#   alpha_em = alpha_2 * sin^2(thetaW) = alpha_Y * cos^2(thetaW)
#   alpha_1  = (5/3) * alpha_Y
# ----------------------------------------------------------------------
cos2thW_MZ = 1.0 - sin2thW_MZ

alpha_2_MZ = alpha_em_MZ / sin2thW_MZ
alpha_Y_MZ = alpha_em_MZ / cos2thW_MZ
alpha_1_MZ = (5.0 / 3.0) * alpha_Y_MZ
alpha_3_MZ = alpha_s_MZ

# ----------------------------------------------------------------------
# SM RGE coefficients (GUT-normalized g1, pure gauge content, no thresholds)
# ----------------------------------------------------------------------
# 1-loop:  d(alpha_i^-1)/dt = -b_i/(2 pi)
b1 = (41.0/10.0, -19.0/6.0, -7.0)

# 2-loop matrix (gauge-only; standard SM values, e.g. Jones 1982 / Machacek-Vaughn,
# GUT-normalized convention):
#          j=1        j=2       j=3
b2 = (
    (199.0/50.0,  27.0/10.0,  44.0/5.0),   # i=1
    (9.0/10.0,    35.0/6.0,   12.0    ),   # i=2
    (11.0/10.0,   9.0/2.0,   -26.0    ),   # i=3
)

TWO_PI = 2.0 * math.pi
EIGHT_PI2 = 8.0 * math.pi * math.pi


def dalpha_dt(alphas, loop_order):
    """
    d(alpha_i)/dt for t = ln(mu).
    1-loop: dalpha_i/dt = b_i alpha_i^2 / (2 pi)
    2-loop: + alpha_i^2 * sum_j b_ij alpha_j / (8 pi^2)
    """
    a1, a2, a3 = alphas
    d = [0.0, 0.0, 0.0]
    for i in range(3):
        ai = alphas[i]
        term1 = b1[i] * ai * ai / TWO_PI
        term = term1
        if loop_order == 2:
            s = sum(b2[i][j] * alphas[j] for j in range(3))
            term2 = ai * ai * s / EIGHT_PI2
            term = term1 + term2
        d[i] = term
    return d


def rk4_step(alphas, t, h, loop_order):
    def f(a):
        return dalpha_dt(a, loop_order)

    k1 = f(alphas)
    a2v = [alphas[i] + 0.5 * h * k1[i] for i in range(3)]
    k2 = f(a2v)
    a3v = [alphas[i] + 0.5 * h * k2[i] for i in range(3)]
    k3 = f(a3v)
    a4v = [alphas[i] + h * k3[i] for i in range(3)]
    k4 = f(a4v)
    return [alphas[i] + (h / 6.0) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(3)]


def run(alphas0, t0, t1, loop_order, n_steps=200000):
    alphas = list(alphas0)
    h = (t1 - t0) / n_steps
    t = t0
    for _ in range(n_steps):
        alphas = rk4_step(alphas, t, h, loop_order)
        t += h
    return alphas


# ----------------------------------------------------------------------
# Declared scales
# ----------------------------------------------------------------------
tau_ratio = 3.8597e14 / 1.0  # |tau_8|/|tau_4| as a GeV number (Lambda_A itself)
Lambda_A = 3.8597e14   # GeV
Lambda_B = 3.520e16    # GeV   (= (|tau_8|/|tau_4|) * M_Z, frozen input value)
mu_ref   = 1.0e16      # GeV

scales = [
    ("Lambda_A", Lambda_A),
    ("Lambda_B", Lambda_B),
    ("mu_ref",   mu_ref),
]

alphas_MZ = (alpha_1_MZ, alpha_2_MZ, alpha_3_MZ)

results = {}
for name, scale in scales:
    t0 = 0.0
    t1 = math.log(scale / M_Z)
    row = {}
    for loop in (1, 2):
        a_final = run(alphas_MZ, t0, t1, loop, n_steps=400000)
        row[loop] = a_final
    results[name] = row

# ----------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------
def fmt(x, digits=10):
    return f"{x:.{digits}g}"

print("=" * 100)
print("INPUTS (PDG 2024 central, at M_Z)")
print("=" * 100)
print(f"alpha_em(M_Z)       = {alpha_em_MZ:.10g}   (1/alpha_em = {1.0/alpha_em_MZ:.10g})")
print(f"sin^2 theta_W(M_Z)  = {sin2thW_MZ:.10g}")
print(f"alpha_s(M_Z)        = {alpha_s_MZ:.10g}")
print(f"M_Z                 = {M_Z:.10g} GeV")
print()
print("GUT-normalized couplings at M_Z (derived):")
print(f"alpha_1(M_Z) = {alpha_1_MZ:.10g}   1/alpha_1(M_Z) = {1.0/alpha_1_MZ:.10g}")
print(f"alpha_2(M_Z) = {alpha_2_MZ:.10g}   1/alpha_2(M_Z) = {1.0/alpha_2_MZ:.10g}")
print(f"alpha_3(M_Z) = {alpha_3_MZ:.10g}   1/alpha_3(M_Z) = {1.0/alpha_3_MZ:.10g}")
print()
print("RGE coefficients used:")
print(f"  1-loop b_i        = {b1}")
print(f"  2-loop matrix b_ij (gauge-only, GUT-normalized):")
for row_ in b2:
    print(f"    {row_}")
print()

for name, scale in scales:
    print("=" * 100)
    print(f"SCALE {name} = {scale:.10g} GeV   (t = ln(scale/M_Z) = {math.log(scale/M_Z):.10g})")
    print("=" * 100)
    for loop in (1, 2):
        a1, a2, a3 = results[name][loop]
        inv1, inv2, inv3 = 1.0/a1, 1.0/a2, 1.0/a3
        sin2th = a1 * (3.0/5.0) / (a2 + a1*(3.0/5.0))  # alpha_Y/(alpha_2+alpha_Y), alpha_Y=(3/5)alpha_1
        print(f"--- {loop}-loop ---")
        print(f"  alpha_1 = {a1:.10g}    1/alpha_1 = {inv1:.10g}")
        print(f"  alpha_2 = {a2:.10g}    1/alpha_2 = {inv2:.10g}")
        print(f"  alpha_3 = {a3:.10g}    1/alpha_3 = {inv3:.10g}")
        print(f"  1/alpha_1 - 1/alpha_2 = {inv1-inv2:.10g}")
        print(f"  1/alpha_1 - 1/alpha_3 = {inv1-inv3:.10g}")
        print(f"  1/alpha_2 - 1/alpha_3 = {inv2-inv3:.10g}")
        print(f"  sin^2 theta_W(scale) = {sin2th:.10g}")
    print()
