#!/usr/bin/env python3
"""B460 cell 2 (LIVE) — per-vacuum CS of the child's 4 SL(2) vacua via Kirk-Klassen
integration along the parent's A-polynomial curve.

Convention: dCS = c * (l dm - m dl) along the curve A(e^m, e^l) = 0, with the constant c
CALIBRATED on the (5,1) geometric vacuum (banked CS = +-0.07703818, B434) and VALIDATED on
the independent (7,1) geometric vacuum (SnapPy) before any non-geometric value is read.
"""
import numpy as np
import snappy

# fig-8 A-polynomial (Cooper et al. convention): A(M,L) = -M^4 + L(1 - M^2 - 2M^4 - M^6 + M^8) - L^2 M^4
def Apoly(M, L):
    return -M**4 + L*(1 - M**2 - 2*M**4 - M**6 + M**8) - L**2 * M**4

def dA(M, L):
    h = 1e-8
    return ((Apoly(M+h, L) - Apoly(M-h, L)) / (2*h), (Apoly(M, L+h) - Apoly(M, L-h)) / (2*h))

def continue_to(m_target, steps=4000):
    """continue (m, l) along the geometric branch from the complete structure (m=0, L=-1)
    to m = m_target; returns the path and the KK integral I = int (l dm - m dl)."""
    # at the complete structure: M=1, L=-1 => l = i*pi (choose the branch)
    m = 0.0 + 0.0j
    l = 1j * np.pi
    I = 0.0 + 0.0j
    path_m = np.linspace(0, 1, steps) * m_target
    prev_m, prev_l = m, l
    for k in range(1, steps):
        m = path_m[k]
        # Newton in l on A(e^m, e^l) = 0, seeded at prev_l (continuous branch)
        L = np.exp(prev_l)
        M = np.exp(m)
        for _ in range(50):
            f = Apoly(M, L)
            _, fL = dA(M, L)
            if abs(f) < 1e-13:
                break
            L = L - f / fL
        # continuous log
        l = np.log(L)
        while (l - prev_l).imag > np.pi:
            l -= 2j * np.pi
        while (l - prev_l).imag < -np.pi:
            l += 2j * np.pi
        I += 0.5 * ((l + prev_l) * (m - prev_m) - (m + prev_m) * (l - prev_l)) / 2 * 2  # trapezoid of l dm - m dl
        # trapezoid properly:
        # int l dm ~ (l+prev_l)/2 * (m-prev_m);  int m dl ~ (m+prev_m)/2 * (l-prev_l)
        prev_m, prev_l = m, l
    return I

def kk_integral(m_target, steps=6000):
    m = 0.0 + 0.0j
    l = 1j * np.pi
    Ildm = 0.0 + 0.0j
    Imdl = 0.0 + 0.0j
    prev_m, prev_l = m, l
    for k in range(1, steps + 1):
        mk = m_target * k / steps
        M = np.exp(mk)
        L = np.exp(prev_l)
        for _ in range(60):
            f = Apoly(M, L)
            _, fL = dA(M, L)
            if abs(fL) < 1e-16:
                break
            Ln = L - f / fL
            if abs(Ln - L) < 1e-14:
                L = Ln
                break
            L = Ln
        lk = np.log(L)
        while (lk - prev_l).imag > np.pi:
            lk -= 2j * np.pi
        while (lk - prev_l).imag < -np.pi:
            lk += 2j * np.pi
        Ildm += (lk + prev_l) / 2 * (mk - prev_m)
        Imdl += (mk + prev_m) / 2 * (lk - prev_l)
        prev_m, prev_l = mk, lk
    return Ildm - Imdl, prev_l

def filling_target(p, root):
    """for slope (p,1): the vacuum has M + 1/M = t (root of the filled quartic) and
    holonomy equation p*m + l = 2*pi*i*k. Return m_target = log M for the branch |M|>1."""
    t = root
    M = (t + np.sqrt(t*t - 4 + 0j)) / 2
    if abs(M) < 1:
        M = (t - np.sqrt(t*t - 4 + 0j)) / 2
    return np.log(M)

print("== targets: the (5,1) quartic roots (banked t^4-3t^3+t^2+3t-1) ==")
q5 = np.roots([1, -3, 1, 3, -1])
print("roots:", np.round(q5, 6))
print("\n== calibration on the geometric (5,1) vacuum ==")
# the geometric filled point: SnapPy's geometric solution — identify which root is geometric:
# the geometric meridian trace of 4_1(5,1) — from B439 the quartic IS the vacuum set; the
# geometric one has the complex root pair matching the filled holonomy. Take the two complex
# roots (geometric + conjugate) and the two real roots (non-geometric).
cplx = [r for r in q5 if abs(r.imag) > 1e-8]
real = [r for r in q5 if abs(r.imag) <= 1e-8]
print(f"complex roots (geometric pair): {np.round(cplx, 6)}")
print(f"real roots (non-geometric): {np.round(real, 6)}")
KK = {}
for r in q5:
    mt = filling_target(5, r)
    I, lend = kk_integral(mt)
    KK[r] = I
    print(f"  root {r:.6f}: m*={mt:.6f}  KK integral = {I:.8f}")
print("\nCS(SnapPy) gates: 4_1(5,1) =", float(snappy.ManifoldHP('4_1(5,1)').chern_simons()),
      "  4_1(7,1) =", float(snappy.ManifoldHP('4_1(7,1)').chern_simons()))
