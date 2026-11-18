"""B1957: agy-002's gates 8 to 11 (its branch agy-002/foundations at ef2ea365b), the statements main can decide by its own
exact computation (data-free; nothing of the seat's is run or imported; its notes are read as text).
 G1  gate 8: with 6Y = diag(-2, -2, -2, 3, 3) on the five-dimensional space, the charges on the even exterior powers and on
     the first; their trace.
 G2  gate 8: the commutant in su(5) of the Weil representation of SL(2, F_5) (class 2x^2/5, main's B1951) and of its
     centre's image P.
 G3  gate 8: the fields Q(sqrt(k^2 + 4)), k = 1 to 12; the primes p whose split (p + 1)/2 + (p - 1)/2 is 3 + 2.
 G4  gate 8: in E8, four mutually orthogonal root reflections whose product has order 2 and determinant 1 and carries the
     centraliser of colour onto the centraliser of the second a2; that second a2 is orthogonal to every root of its
     centraliser.
 G5  gate 9: the kink's zero mode; the identity Y[2-i, 2-j, -k] = conj Y[j, i, k] on main's closed form at Re tau = 0 and
     an imaginary shift, and what it gives for a vector with v[-k] = conj v[k].
 G7  its audit of agy-exp's X-APEX-4 checker (the file read as text at 5de6493f5, not run): four of the lines it cites.
 G6  gate 10: the longitude of the figure-eight group in Riley's representation and in its other lift; the half-line zero
     mode of A^dagger A with A = d/dy + mu e^y, and its norm."""
import sys, pathlib, itertools, functools
from fractions import Fraction as F
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); import cim_closed as CC
print = functools.partial(print, flush=True); nrm = lambda A: float(np.abs(np.asarray(A)).max())
# ---- G1
q = [-2, -2, -2, 3, 3]; spec = lambda k: sorted(sum(q[i] for i in s) for s in itertools.combinations(range(5), k))
even = sorted(spec(0) + spec(2) + spec(4)); cnt = lambda L: {v: L.count(v) for v in sorted(set(L))}
print("G1: 6Y on the even exterior powers: %s (16 states, trace %d); on the first power: %s; on all 32 states the trace is %d" % (cnt(even), sum(even), cnt(spec(1)), sum(sum(spec(k)) for k in range(6))))
# ---- G2
z = np.exp(2j * np.pi / 5); x = np.arange(5); T = np.diag(z ** ((2 * x * x) % 5)); S = z ** (-(4 * np.outer(x, x)) % 5) / np.sqrt(5)   # bilinear form of 2x^2: B(x, y) = 4xy
g = (z ** ((2 * x * x) % 5)).sum() / np.sqrt(5); S = S * np.conj(g) / abs(g)
rel = min(nrm(np.linalg.matrix_power(S @ T, 3) - c * np.linalg.matrix_power(S, 2)) for c in (1, -1, 1j, -1j))
P = np.zeros((5, 5)); P[(-x) % 5, x] = 1
def commutant(ms):
    rows = []
    for M in ms: rows.append(np.kron(np.eye(5), M) - np.kron(M.T, np.eye(5)))
    sv = np.linalg.svd(np.vstack(rows), compute_uv=False); return int(np.sum(sv < 1e-9))
S2 = S @ S; par = min(nrm(S2 - c * P) for c in (1, -1, 1j, -1j))
print("G2: the Weil representation of the class 2x^2/5: (S T)^3 = S^2 up to a fourth root of unity (%.1e) and S^2 is the parity x -> -x up to one (%.1e); matrices commuting with T and S: a space of dimension %d in gl(5), so %d in su(5); commuting with the parity: %d in gl(5), so %d in su(5)"
      % (rel, par, commutant([T, S]), commutant([T, S]) - 1, commutant([P]), commutant([P]) - 1))
# ---- G3
sqf = lambda n: sp.Integer(n) // max(d * d for d in range(1, 40) if n % (d * d) == 0)
fields = {k: int(sqf(k * k + 4)) for k in range(1, 13)}
print("G3: the squarefree part of k^2 + 4 for k = 1 to 12: %s; it is 5 at k = %s; the primes p below 60 with (p + 1)/2 = 3 and (p - 1)/2 = 2: %s" % (fields, [k for k, v in fields.items() if v == 5], [p for p in sp.primerange(3, 60) if (p + 1) // 2 == 3 and (p - 1) // 2 == 2]))
# ---- G4
e = lambda i: tuple(F(int(k == i)) for k in range(8)); sub = lambda a, b: tuple(u - v for u, v in zip(a, b)); dot = lambda a, b: sum(u * v for u, v in zip(a, b))
roots = [tuple((si if k == i else sj if k == j else F(0)) for k in range(8)) for i, j in itertools.combinations(range(8), 2) for si in (F(1), F(-1)) for sj in (F(1), F(-1))]
roots += [tuple(F(s, 2) for s in sg) for sg in itertools.product((1, -1), repeat=8) if sum(1 for s in sg if s < 0) % 2 == 0]; RS = set(roots)
a2 = lambda tr: [sub(e(i), e(j)) for i in tr for j in tr if i != j]; COL, HID = a2((0, 1, 2)), a2((3, 4, 5))
cent = {r for r in roots if all(dot(r, c) == 0 for c in COL)}; gut = {r for r in roots if all(dot(r, c) == 0 for c in HID)}
four = [sub(e(0), e(3)), sub(e(1), e(4)), sub(e(2), e(5)), sub(e(6), e(7))]
refl = lambda a, v: tuple(vi - 2 * dot(a, v) / dot(a, a) * ai for vi, ai in zip(v, a))
def W(v):
    for a in four: v = refl(a, v)
    return v
M = sp.Matrix([[int(c) if c.denominator == 1 else sp.Rational(c.numerator, c.denominator) for c in W(e(i))] for i in range(8)]).T
print("G4: E8 has %d roots; the four roots e0 - e3, e1 - e4, e2 - e5, e6 - e7 are roots (%s) and mutually orthogonal (%s); the product W of their reflections has determinant %s, W^2 = 1 (%s), carries roots to roots (%s) and the centraliser of colour (%d roots) onto the centraliser of the second a2 (%d roots): %s"
      % (len(roots), all(a in RS for a in four), all(dot(a, b) == 0 for a, b in itertools.combinations(four, 2)), M.det(), M * M == sp.eye(8), all(W(r) in RS for r in roots), len(cent), len(gut), {W(r) for r in cent} == gut))
print("G4: every root of the second a2 is orthogonal to every root of its centraliser (%s) and no sum or difference of the two kinds is a root (%s): the two commute; 248 = 78 + 8 + 162" % (all(dot(h, r) == 0 for h in HID for r in gut), not any(tuple(u + s * v for u, v in zip(h, r)) in RS for h in HID for r in gut for s in (1, -1))))
# ---- G5
s_, M0 = sp.symbols("s M_0", positive=True); f = 1 / sp.cosh(M0 * s_)
print("G5: (d/ds + M0 tanh(M0 s)) sech(M0 s) = %s" % sp.simplify(sp.diff(f, s_) + M0 * sp.tanh(M0 * s_) * f))
tau = 2j * np.sqrt(3); worst = 0; herm = 0; dets = []
for xi in (0.23j, 0.41j, -0.17j):
    Y = CC.Y(tau, xi)
    for i in range(3):
        for j in range(3):
            for k in range(6): worst = max(worst, abs(Y[2 - i, 2 - j, (-k) % 6] - np.conj(Y[j, i, k])))
    rng = np.random.default_rng(8); v = rng.normal(size=6) + 1j * rng.normal(size=6); v = v + np.conj(v[(-np.arange(6)) % 6])      # v[-k] = conj v[k]
    Mf = np.einsum("ijk,k->ij", Y, v); J = np.fliplr(np.eye(3)); herm = max(herm, nrm(J @ Mf @ J - Mf.conj().T)); dets.append(np.linalg.det(Mf))
off = CC.Y(0.3 + 2j * np.sqrt(3), 0.23j); woff = max(abs(off[2 - i, 2 - j, (-k) % 6] - np.conj(off[j, i, k])) for i in range(3) for j in range(3) for k in range(6))
print("G5: on main's closed form at tau = 2 sqrt(3) i and three imaginary shifts: |Y[2-i, 2-j, -k] - conj Y[j, i, k]| at most %.1e (at Re tau = 0.3 it fails by %.2f); for a vector with v[-k] = conj v[k] the contracted matrix M obeys J M J = M^dagger with J the reversal (%.1e), so its determinant is real: imaginary parts over moduli %s"
      % (worst, woff, herm, ["%.0e" % abs(d_.imag / abs(d_)) for d_ in dets]))
# ---- G6
w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2; X = sp.Matrix([[1, 1], [0, 1]]); Yr = sp.Matrix([[1, 0], [-w, 1]])
def word(Xm, Ym): return sp.simplify(Ym * Xm.inv() * Ym.inv() * Xm ** 2 * Ym.inv() * Xm.inv() * Ym)
relator = sp.simplify(X * Yr.inv() * X.inv() * Yr * X * Yr.inv() * X.inv() * Yr * X.inv() * Yr.inv())      # one writing of the figure-eight relation; reported, not assumed
lam1, lam2 = word(X, Yr), word(-X, -Yr)
print("G6: Riley's pair x = [[1,1],[0,1]], y = [[1,0],[-w,1]]: the word y x^-1 y^-1 x^2 y^-1 x^-1 y is %s, trace %s; with both generators negated (the other lift) it is the same matrix: %s; it commutes with x: %s; its exponent sum in x and in y: %d and %d"
      % (lam1.tolist(), sp.simplify(lam1.trace()), lam1 == lam2, sp.simplify(lam1 * X - X * lam1) == sp.zeros(2, 2), -1 + 2 - 1, 1 - 1 - 1 + 1))
y_, mu = sp.symbols("y mu", positive=True); psi = sp.exp(-mu * (sp.exp(y_) - 1))
import mpmath as mp
m_ = mp.pi / (2 * mp.sqrt(3)); n2 = mp.exp(2 * m_) * mp.e1(2 * m_); n2q = mp.quad(lambda t: mp.exp(-2 * m_ * (mp.exp(t) - 1)), [0, 1, 2, 4]); assert abs(n2 - n2q) < mp.mpf(10) ** -10      # the integral is e^(2 mu) E1(2 mu); beyond y = 4 the integrand is below 1e-80
print("G6: A = d/dy + mu e^y: A psi0 = %s for psi0 = exp(-mu (e^y - 1)); its squared norm on the half-line at mu = pi/(2 sqrt 3) is %s, finite: a zero mode of A^dagger A when no wall is put at y = 0; a Dirichlet wall only raises the lowest value (the form domain shrinks)"
      % (sp.simplify(sp.diff(psi, y_) + mu * sp.exp(y_) * psi), mp.nstr(n2, 12)))
# ---- G7
import subprocess
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
L = subprocess.run(["git", "show", "5de6493f5:relays/x_apex_4_verify/verify_x_apex_4.py"], capture_output=True, text=True, cwd=ROOT).stdout.split("\n")
cites = [(701, "Fraction(4, 15), Fraction(8, 15)", "the point (4/15, 8/15) typed in (its defect D3)"), (3881, "1.0 / (4.0 * math.pi)", "the loop factor 1/(4 pi) typed in (D2)"),
         (4039, "0 if d < 0", "a literal zero witness (D6)"), (2355, "np.sum(g_inv_sqrt, axis=1)", "the earlier vector (1, 1, 1) still built (D2)")]
if len(L) < 4000: print("G7: agy-exp's branch is not fetched here")
else:
    print("G7: agy-exp's X-APEX-4 checker has %d lines; of the lines agy-002 cites, read as text: %s" % (len(L), "; ".join("line %d holds %s: %s" % (n, what, t in L[n - 1]) for n, t, what in cites)))
