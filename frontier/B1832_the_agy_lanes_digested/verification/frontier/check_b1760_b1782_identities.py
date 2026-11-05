"""agy:B1760 sec 3.2 restates five identities from the physical-bridge lane's October 24-26 notes; agy:B1782 sec 1 the trace-free
cancellation.  sympy / numpy from first principles (data-free).
 (1) Weyl response: M(l) = l (H + Q)^{-1}, Q = sqrt(H^2 - l^2): M' = (1 + M^2)/(2Q) = H/(Q(H + Q)) > 0 on |l| < h; M(0) = 0; M'(0) = 1/(2H).
 (2) mode elimination: S(l) = (A00 - l G00) - (A0p - l G0p)(App - l Gpp)^{-1}(Ap0 - l Gp0); -S'(0) = Pi^dag G Pi, Pi = (I; -App^{-1} Ap0)
     -- stated without hypotheses; checked for hermitian A, G and for non-hermitian A (the domain).
 (3) g(x) = (R^2/pi) dE/dx - e for E = (pi/R^2)[x(3x - 1)/(1 - x)^3 + e x]: g = (3x^2 + 4x - 1)/(1 - x)^4, g' = 6x(x + 3)/(1 - x)^5,
     g((sqrt 7 - 2)/3) = 0, g(1/4) = 16/27, g(1/2) = 28.
 (4) the BPS pair: A_wbar = -(k w/(2s)) H, Q_w = (4 l/s) E_+, s = 1 - k|w|^2, k = 4 l^2: dbar_A Q = 0 and F_xy - (i/2)[Q, Q^dag] = 0.
 (5) agy:B1782: T_vac = -rho g gives T - g T/4 = 0 identically (trace-free Einstein equations)."""
import json, pathlib
import numpy as np
import sympy as sp
OUT = {}
l, h = sp.symbols("lambda h", positive=True)
Q = sp.sqrt(h ** 2 - l ** 2); M = l / (h + Q); Mp = sp.diff(M, l)
OUT["1"] = {"M'-(1+M^2)/(2Q)": str(sp.simplify(Mp - (1 + M ** 2) / (2 * Q))), "M'-h/(Q(h+Q))": str(sp.simplify(Mp - h / (Q * (h + Q)))),
            "M(0)": str(M.subs(l, 0)), "M'(0)": str(sp.simplify(Mp.subs(l, 0)))}
print("(1)", OUT["1"])

rng = np.random.default_rng(1)
def herm(n): X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return X + X.conj().T
def check2(hermitian):
    n0, n1 = 2, 3; A = herm(5) if hermitian else rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)); G = herm(5)
    def S(lv):
        Al = A - lv * G
        return Al[:n0, :n0] - Al[:n0, n0:] @ np.linalg.inv(Al[n0:, n0:]) @ Al[n0:, :n0]
    d = 1e-6; Sp = (S(d) - S(-d)) / (2 * d)
    Pi = np.vstack([np.eye(n0), -np.linalg.inv(A[n0:, n0:]) @ A[n0:, :n0]])
    return float(np.abs(-Sp - Pi.conj().T @ G @ Pi).max())
OUT["2"] = {"hermitian_A_G_dev": check2(True), "nonhermitian_A_dev": check2(False)}
print("(2) -S'(0) vs Pi^dag G Pi: hermitian A, G: %.1e ; non-hermitian A: %.2e" % (OUT["2"]["hermitian_A_G_dev"], OUT["2"]["nonhermitian_A_dev"]))

x, R, e = sp.symbols("x R e", positive=True)
Ef = sp.pi / R ** 2 * (x * (3 * x - 1) / (1 - x) ** 3 + e * x)
g = sp.simplify(R ** 2 / sp.pi * sp.diff(Ef, x) - e)
OUT["3"] = {"g-claimed": str(sp.simplify(g - (3 * x ** 2 + 4 * x - 1) / (1 - x) ** 4)), "g'-claimed": str(sp.simplify(sp.diff(g, x) - 6 * x * (x + 3) / (1 - x) ** 5)),
            "g((sqrt7-2)/3)": str(sp.simplify(g.subs(x, (sp.sqrt(7) - 2) / 3))), "g(1/4)": str(g.subs(x, sp.Rational(1, 4))), "g(1/2)": str(g.subs(x, sp.Rational(1, 2)))}
print("(3)", OUT["3"])

X, Y, lam = sp.symbols("x y lambda", real=True); k = 4 * lam ** 2; w = X + sp.I * Y; s = 1 - k * (X ** 2 + Y ** 2)
H = sp.Matrix([[1, 0], [0, -1]]); Ep = sp.Matrix([[0, 1], [0, 0]])
Awb = -(k * w / (2 * s)) * H; Qw = (4 * lam / s) * Ep
dwb = lambda F: (sp.diff(F, X) + sp.I * sp.diff(F, Y)) / 2
bps1 = sp.simplify(dwb(Qw) + Awb * Qw - Qw * Awb)
Ax = -sp.I * k * Y / s * H; Ay = sp.I * k * X / s * H
Fxy = sp.diff(Ay, X) - sp.diff(Ax, Y) + Ax * Ay - Ay * Ax
bps2 = sp.simplify(Fxy - sp.I / 2 * (Qw * Qw.H - Qw.H * Qw))
# A = ik(-y dx + x dy)/s H must agree with A_wbar: A_wbar = (A_x + i A_y)/2
cons = sp.simplify((Ax + sp.I * Ay) / 2 - Awb)
OUT["4"] = {"dbar_A Q": str(bps1), "F - i/2 [Q,Q^dag]": str(bps2), "A_wbar consistency": str(cons)}
print("(4)", OUT["4"])

rho = sp.symbols("rho"); gm = sp.diag(-1, 1, 1, 1); T = -rho * gm; trT = sum((gm.inv() * T)[i, i] for i in range(4))
OUT["5"] = {"T - g T/4": str(sp.simplify(T - gm * trT / 4))}
print("(5)", OUT["5"])
json.dump(OUT, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print("exit 0")
