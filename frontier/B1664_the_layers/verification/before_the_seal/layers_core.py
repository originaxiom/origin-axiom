"""Design (P-183 steps 1-2; disclosed): along a thread's closed geodesic, g(s) = D(z) (dz/ds)^(-1/2), evaluated at the
reduced point w = gamma z (D(w) (dw/ds)^(-1/2) = +-chi(gamma) g), with the piecewise phase fixed by continuity (the jump
at a domain crossing rounded to the nearest 8th root of unity). Returns <f>, the coherence |int g|/int|g| and the period
phase g(s0 + l)/g(s0)."""
import math, cmath
import numpy as np
_N = np.arange(-12, 13); _K = np.arange(1, 60)
def Df(t):
    q = np.exp(1j*np.pi*t)
    t3 = np.sum(q**(_N**2)); t4 = np.sum((-1.0)**_N*q**(_N**2)); t2 = np.sum(np.exp(1j*np.pi*t*(_N + 0.5)**2))
    eta = np.exp(1j*np.pi*t/12)*np.prod(1 - np.exp(2j*np.pi*t*_K))
    lam = t2**4/t3**4; h = lam*np.log(abs(lam)) + (1 - lam)*np.log(abs(1 - lam))
    D = -t3**4*h/(4*np.pi*eta**6); Rn = (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/abs(2*np.pi*eta**3)**2
    return complex(D), float(abs(D)/Rn)
CHI_T, CHI_S = 1j, 1j          # D's multiplier: chi(z -> z+1) = i; chi(S0: z -> -1/z, matrix [[0,-1],[1,0]]) = i (d_automorphy.py)
def reduce_track(z):
    """reduce z to the standard domain; return w = gamma z, the integer matrix gamma and chi(gamma)"""
    a, b, c, d = 1, 0, 0, 1; chi = 1 + 0j
    for _ in range(400):
        n = round(z.real); z = z - n; a, b, c, d = a - n*c, b - n*d, c, d; chi *= CHI_T**(-n)
        if abs(z) < 1 - 1e-15: z = -1/z; a, b, c, d = -c, -d, a, b; chi *= CHI_S
        else: return z, (a, b, c, d), chi
    return z, (a, b, c, d), chi
def thread(word, step=0.02):
    MAT = {"L": (1, 1, 0, 1), "R": (1, 0, 1, 1)}
    M = (1, 0, 0, 1)
    for ch in word:
        a, b, c, d = M; e, g, h, k = MAT[ch]; M = (a*e + b*h, a*g + b*k, c*e + d*h, c*g + d*k)
    a, b, c, d = M; tr = a + d; ell = 2*math.acosh(tr/2); disc = math.sqrt(tr*tr - 4)
    xa, xr = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c)
    n = max(200, int(ell/step)); ds = ell/n
    zs = lambda s: (xa*1j*math.exp(s) + xr)/(1j*math.exp(s) + 1)
    def vel(s): w = 1j*math.exp(s); return (xa - xr)*w/(w + 1)**2
    s0 = -ell/2 + 0.123*ell
    vals, fs, prev_r = [], [], None
    for j in range(n + 1):
        s = s0 + j*ds; z = zs(s); w, (ga, gb, gc, gd), chi = reduce_track(z); Dw, fv = Df(w)
        Dz = (gc*z + gd)*Dw/chi                       # D(z) = chi(gamma)^-1 (cz + d) D(gamma z)
        r = cmath.sqrt(vel(s))
        if prev_r is not None and abs(r - prev_r) > abs(-r - prev_r): r = -r
        prev_r = r; vals.append(Dz/r); fs.append(fv)
    vals = np.array(vals); fs = np.array(fs)
    wts = np.full(n + 1, ds); wts[0] = wts[-1] = ds/2
    I = np.sum(wts*vals); A = np.sum(wts*np.abs(vals))
    return dict(f=float(np.sum(wts*fs)/ell), coh=float(abs(I)/A), phase=complex(vals[-1]/vals[0]), ell=ell, tr=tr)
if __name__ == "__main__":
    for w in ["LR", "LLR", "LRR", "LLRR", "LLLRRR", "LLRLRR", "LLRLR", "LLLLLR"]:
        r = thread(w); nL, nR = w.count("L"), w.count("R")
        print(f"{w:8s} tr {r['tr']:3d} <f> {r['f']:.4f} coh {r['coh']:.3f} phase {r['phase']:.4f} vs i^(#L-#R) {1j**(nL - nR):.0f}")
