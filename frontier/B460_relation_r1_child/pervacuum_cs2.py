#!/usr/bin/env python3
"""B460 cell 2, refined: robust paths (radial in M with small imaginary detour),
higher resolution, the (7,1) independent validation, and mod-1 recognition."""
import numpy as np
from fractions import Fraction
import snappy

def Apoly(M, L):
    return -M**4 + L*(1 - M**2 - 2*M**4 - M**6 + M**8) - L**2 * M**4

def kk(m_target, steps=20000, detour=0.13):
    """integrate l dm - m dl along m(s) = s*m_target + i*detour*sin(pi s) (branch-avoiding)."""
    l = 1j * np.pi
    prev_m = 0.0 + 0j
    prev_l = l
    I = 0.0 + 0j
    L = np.exp(l)
    for k in range(1, steps + 1):
        s = k / steps
        mk = s * m_target + 1j * detour * np.sin(np.pi * s)
        M = np.exp(mk)
        for _ in range(80):
            f = Apoly(M, L)
            h = 1e-7
            fL = (Apoly(M, L + h) - Apoly(M, L - h)) / (2 * h)
            Ln = L - f / fL
            if abs(Ln - L) < 1e-15:
                L = Ln
                break
            L = Ln
        lk = np.log(L)
        while (lk - prev_l).imag > np.pi:
            lk -= 2j * np.pi
        while (lk - prev_l).imag < -np.pi:
            lk += 2j * np.pi
        I += (lk + prev_l) / 2 * (mk - prev_m) - (mk + prev_m) / 2 * (lk - prev_l)
        prev_m, prev_l = mk, lk
    return I

def targets(p):
    """meridian-log targets for the slope-(p,1) vacua from the filled A-poly quartic."""
    import sympy as sp
    t, Msym, Lsym = sp.symbols('t M L')
    A = -Msym**4 + Lsym*(1 - Msym**2 - 2*Msym**4 - Msym**6 + Msym**8) - Lsym**2 * Msym**4
    # filling: M^p L = 1 -> L = M^(-p); resultant in M, convert to trace t = M + 1/M
    Af = sp.expand(A.subs(Lsym, Msym**(-p)) * Msym**(2*p))
    poly = sp.Poly(Af, Msym)
    roots = []
    for fac, mult in sp.factor_list(poly.as_expr())[1]:
        pf = sp.Poly(fac, Msym)
        if pf.degree() == 0:
            continue
        import numpy as _np
        cs_ = [complex(c) for c in pf.all_coeffs()]
        roots.extend([complex(r) for r in _np.roots(cs_)])
    # keep one representative per trace value with |M| >= 1
    out = {}
    for M in roots:
        if abs(M) < 1 - 1e-9:
            continue
        tval = M + 1/M
        key = (round(tval.real, 8), round(tval.imag, 8))
        out[key] = np.log(M)
    return out

TWO_PI2 = 2 * np.pi**2

for p, cs_snappy in [(5, None), (7, None)]:
    M = snappy.Manifold('4_1')
    _ = M.chern_simons()          # prime the cusped CS (known = 0 for 4_1)
    M.dehn_fill((p, 1))
    cs_geo = float(M.chern_simons())
    print(f"===== slope ({p},1): SnapPy geometric CS = {cs_geo:.10f} =====")
    for key, mt in sorted(targets(p).items()):
        I = kk(mt)
        cs = (I.real / TWO_PI2)
        vol_drop = I.imag
        # reduce mod 1 to [-0.5, 0.5)
        csm = (cs + 0.5) % 1 - 0.5
        tag = ""
        if abs(vol_drop - 2.02988) < 0.01 and abs(key[1]) < 1e-6:
            tag = " [SU(2)-type vacuum]"
        if abs(csm - cs_geo) < 1e-4 or abs(csm + cs_geo) < 1e-4:
            tag += " <== GEOMETRIC GATE"
        print(f"  t={key[0]:+.6f}{key[1]:+.6f}i  m*={mt:.6f}  CS={csm:+.8f}  Im/voldrop={vol_drop:.6f}{tag}")
    print()

# ---- multi-path consistency pass (appended): accept a CS value only if >=3 detours agree ----
def kk_consistent(mt, detours=(0.05, 0.13, 0.22, -0.13, -0.05)):
    vals = []
    for d in detours:
        I = kk(mt, steps=20000, detour=d)
        vals.append(((I.real / TWO_PI2 + 0.5) % 1 - 0.5, I.imag))
    # cluster by CS value
    from collections import Counter
    key = [round(v[0], 6) for v in vals]
    cnt = Counter(key)
    best, n = cnt.most_common(1)[0]
    consistent = [v for v in vals if round(v[0], 6) == best]
    return best, n, len(detours), consistent[0][1]

if __name__ == '__main__' or True:
    print("\n===== MULTI-PATH CONSISTENCY (the binding pass) =====")
    for p in (5, 7):
        M = snappy.Manifold('4_1')
        _ = M.chern_simons()
        M.dehn_fill((p, 1))
        cs_geo = float(M.chern_simons())
        print(f"-- slope ({p},1), SnapPy geometric CS = {cs_geo:.10f} --")
        for key, mt in sorted(targets(p).items()):
            cs, n, tot, vd = kk_consistent(mt)
            tag = " [SU(2)]" if abs(abs(vd) - 2.02988) < 0.01 and abs(key[1]) < 1e-6 else ""
            gate = " <== GATE" if (abs(cs - cs_geo) < 5e-5 or abs(cs + cs_geo) < 5e-5) else ""
            ok = "OK" if n >= 3 else f"INCONSISTENT({n}/{tot})"
            print(f"  t={key[0]:+.6f}{key[1]:+.6f}i  CS={cs:+.8f}  paths={ok}  voldrop={vd:+.5f}{tag}{gate}", flush=True)
