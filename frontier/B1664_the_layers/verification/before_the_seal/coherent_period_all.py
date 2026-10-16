"""EXPLORATION (P-179), coherent_period.py from a generic start s0 = 0.37 l (away from omega's orbit, where D = 0), on
every Lyndon word in L, R to length 8: is g(s0 + l)/g(s0) = i^(#L - #R) on every thread (eps = +1 throughout)?"""
import math, itertools, mpmath as mp
from d_automorphy import D
mp.mp.dps = 20
MAT = {"L": (1, 1, 0, 1), "R": (1, 0, 1, 1)}
def mul(A, B): a, b, c, d = A; e, g, h, k = B; return (a*e + b*h, a*g + b*k, c*e + d*h, c*g + d*k)
def lyndon(n):
    return ["".join(w) for w in itertools.product("LR", repeat=n)
            if "L" in w and "R" in w and all("".join(w) < "".join(w)[i:] + "".join(w)[:i] for i in range(1, n))]
def phase(word, K=240):
    M = (1, 0, 0, 1)
    for ch in word: M = mul(M, MAT[ch])
    a, b, c, d = M; tr = a + d; disc = math.sqrt(tr*tr - 4)
    xa, xr = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c); ell = 2*math.acosh(tr/2)
    z = lambda s: (xa*1j*math.exp(s) + xr)/(1j*math.exp(s) + 1)
    zp = lambda s, h=1e-6: (z(s + h) - z(s - h))/(2*h)
    s0 = 0.37*ell; prev = mp.sqrt(mp.mpc(zp(s0)))
    for n in range(1, K + 1):
        r = mp.sqrt(mp.mpc(zp(s0 + n*ell/K)))
        if abs(r - prev) > abs(-r - prev): r = -r
        prev = r
    g0 = D(z(s0))/mp.sqrt(mp.mpc(zp(s0))); g1 = D(z(s0 + ell))/prev
    return g1/g0, 1j**(word.count("L") - word.count("R"))
bad = 0; n_all = 0; surv = []
for n in range(2, 9):
    for w in lyndon(n):
        ph, chi = phase(w); n_all += 1
        if abs(ph - chi) > 1e-6: bad += 1; print("MISMATCH", w, mp.nstr(ph, 8), chi)
        if abs(chi - 1) < 1e-9: surv.append(w)
print(f"{n_all} primitive threads to length 8: period phase = i^(#L-#R) on {n_all - bad}, mismatches {bad}")
print(f"threads with #L = #R mod 4 (coherent amplitude survives): {len(surv)}: {' '.join(surv)}")
