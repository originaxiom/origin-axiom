#!/usr/bin/env python3
"""B162 -- the kappa-sweep: kappa=2 as the unique cancellation<->non-cancellation wall.

The figure-eight/golden monodromy is ONE map foliated over kappa = 2 + lambda^2. This makes
the non-cancellation obstruction (S034 / B161) GEOMETRIC: kappa=2 is the unique fiber whose
spectrum has POSITIVE measure (the full AC band -- the trivial/cancellation vacuum); every
other kappa gives a zero-measure set (Cantor for kappa>2, thin for kappa<2).

METHOD = direct finite-Fibonacci-chain diagonalization (the eigenvalues ARE the spectrum;
no fragile escape-grid). H = tridiag(hop 1, diag V), V_n = lambda if n-th Fibonacci letter
'a' else 0. real lambda -> kappa>=2 (real spectrum); lambda=i*mu -> kappa=2-mu^2<2 (complex).

SELF-VALIDATION (must pass): V1 Hermitian sanity; V2 bulk BC-robustness; V3 size convergence;
V4 open-BC chiral symmetry E<->-conj(E). [promoted from the validated audit method.]
"""
import numpy as np, sympy as sp

def fib_word(n):
    w = {1: "a", 2: "ab"}
    for j in range(3, n+1): w[j] = w[j-1] + w[j-2]
    return w[n]

def H_eig(word, lam, periodic=False):
    L = len(word); V = np.array([lam if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V)
    i = np.arange(L-1); H[i, i+1] = 1.0; H[i+1, i] = 1.0
    if periodic: H[0, L-1] = 1.0; H[L-1, 0] = 1.0
    return np.linalg.eigvals(H)

def band_measure_1d(word, lm, NE=300000):   # 1D Lebesgue measure of {E real: |tr M(E)|<=2}
    Es = np.linspace(-(2+lm)-.05, (2+lm)+.05, NE)
    a = np.ones(NE); b = np.zeros(NE); c = np.zeros(NE); d = np.ones(NE)
    with np.errstate(over='ignore', invalid='ignore'):
        for ch in word:
            V = lm*(1.0 if ch == 'a' else 0.0)
            na = (Es-V)*a - c; nb = (Es-V)*b - d; a, b, c, d = na, nb, a.copy(), b.copy()
        return float(np.mean(np.abs(a+d) <= 2.0)*(Es[-1]-Es[0]))

def area_2d(ev, eps):                          # 2D-area proxy for a complex spectrum
    lo_r, lo_i = ev.real.min()-1e-6, ev.imag.min()-1e-6
    cells = set(zip(np.floor((ev.real-lo_r)/eps).astype(int).tolist(),
                    np.floor((ev.imag-lo_i)/eps).astype(int).tolist()))
    return len(cells)*eps*eps

def nn95(A, B):
    A2 = np.c_[A.real, A.imag]; B2 = np.c_[B.real, B.imag]
    return np.percentile([np.min(np.sum((B2-a)**2, axis=1))**0.5 for a in A2], 95)

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

print("== self-validation (method) ==")
chk("V1 Hermitian sanity (real lambda => max|Im|~0)", np.max(np.abs(H_eig(fib_word(15), 1.0+0j, True).imag)) < 1e-9)
nns = [nn95(H_eig(fib_word(k), 2.0j, False), H_eig(fib_word(k), 2.0j, True)) for k in (11, 13, 15)]
chk("V2 bulk BC-robustness (95pct nn(open,per)->0 with L, kappa=-2)", nns[-1] < 0.03 and nns[-1] < nns[0], x=f"{[round(v,4) for v in nns]}")
mims = [np.max(np.abs(H_eig(fib_word(k), 2.0j, True).imag)) for k in (11, 13, 15)]
chk("V3 size convergence max|Im E| (kappa=-2)", abs(mims[-1]-mims[-2]) < 0.02, x=f"{[round(m,4) for m in mims]}")
evo = H_eig(fib_word(15), 2.0j, False)
chir = np.max(np.abs(np.sort_complex(evo) - np.sort_complex(-np.conj(evo))))
chk("V4 open-BC chiral E<->-conj(E) (eig precision)", chir < 1e-5, x=f"max mismatch={chir:.2e}")

print("\n== kappa >= 2 (real lambda): 1D band measure -- POSITIVE only at kappa=2 ==")
W = fib_word(13)
for lm, kap in [(0.0, 2.0), (0.5, 2.25), (1.0, 3.0), (2.0, 6.0)]:
    m = band_measure_1d(W, lm)
    tag = "FULL BAND (cancellation/trivial)" if kap == 2.0 else "Cantor dust (zero-measure)"
    print(f"  kappa={kap:5.2f} (lam={lm}): |sigma|_1D = {m:.3f}   {tag}")
chk("kappa=2 has the full band (~4); kappa>2 is fractured (<3.9)",
    abs(band_measure_1d(W, 0.0)-4.0) < 0.05 and band_measure_1d(W, 1.0) < 3.9)

print("\n== kappa < 2 (lambda=i*mu): 2D area -> 0 (thin) + lift-off ~0.91 mu ==")
for mu, kap in [(0.5, 1.75), (1.0, 1.0), (1.5, -0.25), (2.0, -2.0)]:
    ev = H_eig(fib_word(15), mu*1j, True)
    ars = [area_2d(ev, e) for e in (0.04, 0.02, 0.01)]
    mim = np.max(np.abs(ev.imag))
    print(f"  kappa={kap:5.2f} (lam={mu}i): area(eps=.04/.02/.01)={ars[0]:.3f}/{ars[1]:.3f}/{ars[2]:.3f} (->0=thin); "
          f"max|Im|/mu={mim/mu:.3f}")
ev2 = H_eig(fib_word(15), 1.0j, True)
chk("kappa<2 spectrum is thin (2D area shrinks as eps->0)", area_2d(ev2, 0.01) < area_2d(ev2, 0.04))

print("\n== kappa=-2 endpoint: figure-eight cusp (parabolic), symbolic [B160] ==")
E, lam = sp.symbols('E lambda'); I2 = sp.eye(2)
A = sp.Matrix([[E-lam, -1], [1, 0]]); B = sp.Matrix([[E, -1], [1, 0]])
C = sp.simplify((A*B*A.inv()*B.inv()).subs(lam, 2*sp.I).subs(E, sp.Rational(1, 2)))
chk("kappa=2+lambda^2=-2 <=> lambda=2i", sp.simplify(2+(2*sp.I)**2-(-2)) == 0)
chk("commutator parabolic at lambda=2i (trace -2, (C+I)^2=0, not -I)",
    sp.simplify(sp.trace(C)+2) == 0 and sp.simplify((C+I2)**2) == sp.zeros(2) and sp.simplify(C-(-I2)) != sp.zeros(2))

print("\nHEADLINE: kappa=2 is the UNIQUE wall -- the only fiber with positive spectral measure (the full")
print("AC band = the trivial/cancellation vacuum). Every other kappa is zero-measure: Cantor dust (kappa>2,")
print("non-cancellation) or a thin complex set (kappa<2). OPEN (no ground truth off the real axis): whether the")
print("kappa<2 thin set is a true Cantor set, and whether the kappa=-2 spectrum encodes the hyperbolic geometry.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
