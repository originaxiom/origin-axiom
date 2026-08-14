"""Higher-truncation run for the upper eigenvalues, with a VECTORISED K_ir."""
import numpy as np
exec(open('cc_verify_eigs.py').read().split('# ---------------- K_{ir}')[0])

def K_ir_vec(r, x):
    """Vectorised: shared u-grid, valid while x*cosh(umax) >> 1 for the SMALLEST x."""
    x = np.asarray(x, dtype=float)
    umax = min(float(np.arccosh(max(60.0 / max(x.min(), 1e-12), 1.0000001))), 9.0)
    u = np.linspace(0.0, umax, 1400)
    w = np.cos(r * u)
    E = np.exp(-np.outer(x, np.cosh(u)))
    return np.trapezoid(E * w, u, axis=1) if hasattr(np, "trapezoid") else np.trapz(E * w, u, axis=1)

def dual_modes(mmax):
    out = []
    P = int(mmax) + 2; Q = int(mmax * 2 * W3) + 2
    for p in range(-P, P + 1):
        for q in range(-Q, Q + 1):
            mu = complex(p, q / (2 * W3))
            if 0 < abs(mu) <= mmax: out.append(mu)
    return np.array(out)

def sigma_min(r, Y, mmax, npts, seed=11):
    mus = dual_modes(mmax); absmu = np.abs(mus)
    rng = np.random.default_rng(seed)
    zs = rng.random(npts) + 1j * (rng.random(npts) * 2 * W3)
    k1 = Y * K_ir_vec(r, 2 * np.pi * absmu * Y)
    rows = []
    for z in zs:
        zp, tp = pullback(z, Y)
        k2 = tp * K_ir_vec(r, 2 * np.pi * absmu * tp)
        e1 = np.exp(2j*np.pi*(mus.real*z.real + mus.imag*z.imag))
        e2 = np.exp(2j*np.pi*(mus.real*zp.real + mus.imag*zp.imag))
        rows.append(k1*e1 - k2*e2)
    V = np.array(rows); n = np.linalg.norm(V, axis=0); n[n==0]=1
    return np.linalg.svd(V/n, compute_uv=False)[-1]

Y, MMAX = 0.62, 5.4
NM = len(dual_modes(MMAX)); NP = int(2.5*NM)
print(f"HIGH-TRUNCATION: Y={Y} |mu|<={MMAX} modes={NM} points={NP}")
print(f"  Bessel margin at r=8.86: 2pi*{MMAX}*{Y} = {2*np.pi*MMAX*Y:.1f} vs r -> {2*np.pi*MMAX*Y/8.86:.2f}x\n")
print(f"{'r':>14} {'sigma_min':>12} {'ctrl(+.02)':>12} {'ctrl(-.02)':>12} {'ratio':>8}")
for r in (7.072004187, 8.863405356):
    s0=sigma_min(r,Y,MMAX,NP); sp=sigma_min(r+0.02,Y,MMAX,NP); sm=sigma_min(r-0.02,Y,MMAX,NP)
    print(f"{r:>14.9f} {s0:>12.3e} {sp:>12.3e} {sm:>12.3e} {min(sp,sm)/s0:>7.1f}x")
