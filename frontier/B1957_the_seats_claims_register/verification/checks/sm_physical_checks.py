"""The SM seat's checks of the physical lane (its branch at b3385948b: SM_CHECK_PHYSICAL_W_P1, _NATIVE_REGISTER,
_HISTORY_AND_REGISTER): what main computes of their claims beyond its own earlier checks (physical_native_action.py N1 to N7;
physical_c8_tick_higgs.py K2 to K4; physical_primitives.py F3).  Main's own six-mode T6, S6, U from physical_c8_tick_higgs.py.
Nothing of either seat's is run.
 W1  on the ground plane E (main's v+, v-), both tick conventions (T6 S6 K and P T6 S6 K): Sigma^2 = U, U^6 = -I, Sigma^12 = -I.
 W2  on 50 random h in E: N is kept and Delta changes sign under the tick, so |Delta|/N is constant on each orbit and d_k = (-1)^k d_0.
 W3  the normalised average of |Sigma^k h><Sigma^k h| over k = 0..11 is I_E/2; the two-time statistic averaged over a period is
     (-1)^l d_0^2.
 W4  no conjugate of [[2, 1], [1, 1]] in SL(2, Z) has c = 0 (an upper-triangular integer matrix of trace 3 and determinant 1
     would have integer eigenvalues; x^2 - 3x + 1 has none); the fixed points of [[a, b], [c, d]] are separated by
     sqrt((a + d)^2 - 4)/abs(c).
 H1  a random 5-state, 3-update model in exact rationals: W(hk; x) = W(h; x) W(k; T_h x), sum over a of W(ha; x) = W(h; x), and the
     weights of each length sum to 1.
 H2  the same-length control: with moves a, a^-1, b, b^-1 of weights p, p, q, q (2p + 2q = 1), W(a a^-1) = p^2 and W(b b^-1) = q^2;
     at p = 1/5: 1/25 and 9/100; W(u u^-1) = p(1 - p) at p = 1/3 is 2/9; sum of rho (1 - rho)^n = 1.
 (The lumpability criterion, (1) <=> (2), is not tested here: it is immediate from the definitions, since row x of K q* is the
 block sums of K's row x and row x of q* Kbar is Kbar's row q(x); a random test of it, built from the same block sums, could not
 fail.)"""
import random, itertools, pathlib
from fractions import Fraction as Fr
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "physical_c8_tick_higgs.py").read_text(); g = {"__name__": "c8", "__file__": str(HERE / "physical_c8_tick_higgs.py")}
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("rng = np.random.default_rng(11)")], g)
U, vp, vm, A, B, inv = g["U"], g["vp"], g["vm"], g["A"], g["B"], np.linalg.inv
E = np.column_stack([vp, vm]); nrm = lambda X: float(np.abs(X).max())
UE = E.conj().T @ U @ E
def sig(Mx):   # the antiunitary h -> Mx conj(h) on E, in the basis (v+, v-): z -> Sg conj(z)
    return E.conj().T @ Mx @ E.conj()
out = []
for name, Mx in (("T6 S6 K", A), ("P T6 S6 K", B)):
    Sg = sig(Mx); S2 = Sg @ Sg.conj()
    S12 = np.eye(2, dtype=complex)
    for _ in range(6): S12 = S12 @ S2
    out.append("%s: |Sigma^2 - U| = %.1e, |U^6 + I| = %.1e, |Sigma^12 + I| = %.1e, E kept: %.1e" % (name, nrm(S2 - UE), nrm(np.linalg.matrix_power(UE, 6) + np.eye(2)), nrm(S12 + np.eye(2)), nrm(Mx @ E.conj() - E @ (E.conj().T @ Mx @ E.conj()))))
print("W1: " + "; ".join(out))
rng = np.random.default_rng(5); w2 = w3 = w4 = 0.0
for name, Mx in (("T6 S6 K", A), ("P T6 S6 K", B)):
    Sg = sig(Mx)
    for _ in range(50):
        z = rng.normal(size=2) + 1j * rng.normal(size=2); orbit = [z]
        for k_ in range(23): orbit.append(Sg @ orbit[-1].conj())
        N = [np.vdot(o, o).real for o in orbit]; D = [abs(o[0]) ** 2 - abs(o[1]) ** 2 for o in orbit]; d = [D[i] / N[i] for i in range(24)]
        w2 = max(w2, max(abs(N[i] - N[0]) for i in range(24)), max(abs(d[i] - (-1) ** i * d[0]) for i in range(24)))
        avg = sum(np.outer(o, o.conj()) for o in orbit[:12]) / sum(N[:12]); w3 = max(w3, nrm(avg - np.eye(2) / 2))
        for l in range(4): w4 = max(w4, abs(np.mean([d[k_] * d[k_ + l] for k_ in range(12)]) - (-1) ** l * d[0] ** 2))
print("W2: on 50 random h, both conventions: worst change of N along an orbit and of d_k - (-1)^k d_0: %.1e" % w2)
print("W3: worst |average - I_E/2| %.1e; worst |two-time statistic - (-1)^l d_0^2| %.1e" % (w3, w4))
x = sp.Symbol("x"); a, b_, c_, d_ = sp.symbols("a b c d")
fp = sp.solve(sp.Eq(c_ * x ** 2 + (d_ - a) * x - b_, 0), x); sep = sp.simplify((fp[0] - fp[1]) ** 2 - ((a + d_) ** 2 - 4) / c_ ** 2)
print("W4: integer roots of x^2 - 3x + 1: %s; (z1 - z2)^2 - ((a + d)^2 - 4)/c^2 with ad - bc = 1: %s" % ([r for r in sp.roots(x ** 2 - 3 * x + 1) if r.is_integer], sp.simplify(sep.subs(b_, (a * d_ - 1) / c_))))
random.seed(7); S, M = 5, 3
pr = {s: (lambda w: [Fr(v, sum(w)) for v in w])([random.randint(1, 9) for _ in range(M)]) for s in range(S)}; T = {(s, m): random.randrange(S) for s in range(S) for m in range(M)}
def W(h, s):
    w = Fr(1)
    for m in h: w *= pr[s][m]; s = T[(s, m)]
    return w, s
ok2 = ok3 = ok_len = True
for s in range(S):
    for L in range(4):
        for h in itertools.product(range(M), repeat=L):
            wh, sh = W(h, s); ok3 &= sum(W(h + (m,), s)[0] for m in range(M)) == wh
            for k in itertools.product(range(M), repeat=2): ok2 &= W(h + k, s)[0] == wh * W(k, sh)[0]
    for L in range(5): ok_len &= sum(W(h, s)[0] for h in itertools.product(range(M), repeat=L)) == 1
print("H1: composition %s; consistency %s; each length sums to 1 (lengths 0 to 4) %s" % (ok2, ok3, ok_len))
p, q, rho, n = sp.Rational(1, 5), sp.Rational(3, 10), sp.Symbol("rho", positive=True), sp.Symbol("n", integer=True, nonnegative=True)
print("H2: 2p + 2q = %s; W(a a^-1) = %s, W(b b^-1) = %s; p(1 - p) at 1/3 = %s; sum rho (1 - rho)^n = %s (for 0 < rho < 1)"
      % (2 * p + 2 * q, p ** 2, q ** 2, sp.Rational(1, 3) * sp.Rational(2, 3), sp.simplify(sp.summation(rho * (1 - rho) ** n, (n, 0, sp.oo)).subs(rho, sp.Rational(1, 4)))))
