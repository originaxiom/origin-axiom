"""agy:B1764 / B1773 / B1774 / B1778 (data-free parts), from first principles (mpmath, sympy); no lane code.

E(tau, s) = sum'_{(m,n)} y^s / |m tau + n|^{2s}  (the normalisation of agy:B1774 sec 1; checked against a direct lattice sum).
Fourier: E = 2 zeta(2s) y^s + 2 sqrt(pi) Gamma(s-1/2) zeta(2s-1)/Gamma(s) y^{1-s}
             + (8 pi^s sqrt(y) / Gamma(s)) sum_{n>=1} n^{s-1/2} sigma_{1-2s}(n) K_{s-1/2}(2 pi n y) cos(2 pi n x).
 1. B1764: the word LLLLLRRLRLLR, its trace (110), the axis apex (1 + i sqrt 84)/3; B1764's A = [[115,-32],[18,-5]].
 2. B1774: the closed form t(y) = d_y E3 / d_y E2 from the constant terms; t at y* = sqrt(84)/3 (4.430013023724 claimed);
    the full value with Bessel terms at x = 1/3; t(y) monotone (B1784's negative: V = E3 - t E2 is radially stationary at every
    y for its own t, so it selects no Im tau unless t is chosen).
 3. B1764/B1773: the Hessian of V = E3 - t* E2 at tau*: d2V/dy2 (17.11 claimed), d2V/dx2 (-7.1e-5 claimed), saddle.
 4. B1773: the flux term.  For K = -ln(2 Im tau), W = N_F - tau N_H, the F-term potential e^K K^{tt} |D_t W|^2 (no-scale) and
    e^K (K^{tt} |D_t W|^2 - 3|W|^2) (N = 1 SUGRA), against the lane's V_flux = N_H^2 (x - N_F/N_H)^2 / (2y).
 5. B1778: W(tau*) = -i sqrt 84, d_tau K, D_tau W = -3/2, F^tau = -(3/2)(2y)^{3/2}."""
import json, math, pathlib
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
OUT = {}

# --- 1. the word ------------------------------------------------------------------------------------------------
Lm = sp.Matrix([[1, 0], [1, 1]]); Rm = sp.Matrix([[1, 1], [0, 1]])
word = "LLLLLRRLRLLR"; Wm = sp.eye(2)
for ch in word: Wm = Wm * (Lm if ch == "L" else Rm)
A = sp.Matrix([[115, -32], [18, -5]])
def apex(M):
    a, b, c, d = [sp.nsimplify(v) for v in M]; tr = a + d
    return sp.nsimplify((a - d) / (2 * c)), sp.sqrt(tr ** 2 - 4) / (2 * abs(c))
cW, rW = apex(Wm); cA_, rA = apex(A)
# is A conjugate to the word's matrix in SL(2,Z) by a translation T^k (which shifts the apex by k)?
conj = [k for k in range(-12, 13) if sp.Matrix([[1, k], [0, 1]]) * Wm * sp.Matrix([[1, -k], [0, 1]]) == A]
OUT["word"] = {"matrix": [int(v) for v in Wm], "trace": int(Wm.trace()), "apex_center": str(cW), "apex_radius": str(sp.simplify(rW)),
               "A_trace": int(A.trace()), "A_det": int(A.det()), "A_apex_center": str(cA_), "A_apex_radius": str(sp.simplify(rA)),
               "A_equals_Tk_W_T-k_for_k": conj}
print("1. word %s with L=[[1,0],[1,1]], R=[[1,1],[0,1]]: %s, trace %d, axis center %s radius %s"
      % (word, list(Wm), Wm.trace(), cW, sp.simplify(rW)))
print("   B1764's A: det %d trace %d center %s radius %s; A = T^k W T^-k for k in %s" % (A.det(), A.trace(), cA_, sp.simplify(rA), conj))

# --- 2. E(tau, s) and t(y) --------------------------------------------------------------------------------------
def sigma(n, a): return mp.fsum(mp.mpf(d) ** a for d in range(1, n + 1) if n % d == 0)
def E(x, y, s, nmax=30):
    s = mp.mpf(s); x = mp.mpf(x); y = mp.mpf(y)
    c = 2 * mp.zeta(2 * s) * y ** s + 2 * mp.sqrt(mp.pi) * mp.gamma(s - 0.5) * mp.zeta(2 * s - 1) / mp.gamma(s) * y ** (1 - s)
    f = 8 * mp.pi ** s * mp.sqrt(y) / mp.gamma(s) * mp.fsum(mp.mpf(n) ** (s - 0.5) * sigma(n, 1 - 2 * s) * mp.besselk(s - 0.5, 2 * mp.pi * n * y) * mp.cos(2 * mp.pi * n * x) for n in range(1, nmax + 1))
    return c + f
def E_direct(x, y, s, R=600):
    tot = mp.mpf(0); tau = mp.mpc(x, y)
    for m in range(-R, R + 1):
        for n in range(-R, R + 1):
            if m == 0 and n == 0: continue
            tot += 1 / abs(m * tau + n) ** (2 * s)
    return tot * mp.mpf(y) ** s
# normalisation cross-check at a modest height (direct sum truncation error ~ R^{2-2s})
mp.mp.dps = 15
chk = {s: (E(0.21, 1.1, s), E_direct(0.21, 1.1, s, R=150)) for s in (3,)}
mp.mp.dps = 30
OUT["normalisation_check_s3"] = [str(chk[3][0]), str(chk[3][1])]
print("2. E(0.21+1.1i, 3): Fourier %s, direct lattice sum (|m|,|n|<=150) %s" % (mp.nstr(chk[3][0], 12), mp.nstr(chk[3][1], 12)))
def t_closed(y):
    y = mp.mpf(y)
    return ((2 * mp.pi ** 6 / 315) * y ** 2 - (3 * mp.pi / 2) * mp.zeta(5) * y ** -3) / ((2 * mp.pi ** 4 / 45) * y - mp.pi * mp.zeta(3) * y ** -2)
ys = mp.sqrt(84) / 3; xs = mp.mpf(1) / 3
dyE = lambda s: mp.diff(lambda yy: E(xs, yy, s), ys)
t_full = dyE(3) / dyE(2); t_cl = t_closed(ys); t_lead = 2 * mp.pi ** 2 / mp.sqrt(21)
OUT["t"] = {"closed": str(t_cl), "full_x=1/3": str(t_full), "leading_2pi2/sqrt21": str(t_lead), "diff_full_closed": str(t_full - t_cl)}
print("   t(y*) closed form %s ; full (Bessel, x=1/3) %s ; diff %s ; leading 2pi^2/sqrt21 = %s"
      % (mp.nstr(t_cl, 13), mp.nstr(t_full, 13), mp.nstr(t_full - t_cl, 3), mp.nstr(t_lead, 13)))
# monotonicity of t(y) (closed form; exponential terms < 1e-5 relative for y >= 2)
grid = [1 + 0.05 * k for k in range(0, 381)]
tv = [t_closed(y) for y in grid]
mono = all(tv[i + 1] > tv[i] for i in range(len(tv) - 1))
dmin = min(tv[i + 1] - tv[i] for i in range(len(tv) - 1))
inv = [y for y in grid if 3.205 <= t_closed(y) <= 4.624]
OUT["t_monotone_y_1_to_20"] = mono
OUT["W154_window_maps_to_y"] = [min(inv), max(inv)]
print("   t(y) strictly increasing on y in [1, 20] (closed form): %s (min step %s); the window t in [3.205, 4.624] <-> y in [%.2f, %.2f]"
      % (mono, mp.nstr(dmin, 3), min(inv), max(inv)))

# --- 3. the Hessian at tau* --------------------------------------------------------------------------------------
V = lambda x, y: E(x, y, 3) - t_full * E(x, y, 2)
Vx = mp.diff(lambda x: V(x, ys), xs); Vy = mp.diff(lambda y: V(xs, y), ys)
Vxx = mp.diff(lambda x: V(x, ys), xs, 2); Vyy = mp.diff(lambda y: V(xs, y), ys, 2)
Vxy = mp.diff(lambda x: mp.diff(lambda y: V(x, y), ys), xs)
det = Vxx * Vyy - Vxy ** 2
OUT["hessian"] = {k: str(v) for k, v in dict(Vx=Vx, Vy=Vy, Vxx=Vxx, Vyy=Vyy, Vxy=Vxy, det=det).items()}
print("3. V = E3 - t E2 at tau* (t = t_full): Vx %s Vy %s Vxx %s Vyy %s Vxy %s det %s"
      % tuple(mp.nstr(v, 6) for v in (Vx, Vy, Vxx, Vyy, Vxy, det)))

# --- 4. the flux potential (sympy) ---------------------------------------------------------------------------------
x, y, NF, NH = sp.symbols("x y N_F N_H", real=True); tau = x + sp.I * y; taub = x - sp.I * y
K = -sp.log(2 * y); W = NF - tau * NH; Wb = NF - taub * NH
K_t = sp.Rational(1, 2) * (sp.diff(K, x) - sp.I * sp.diff(K, y))                     # d/dtau = (d_x - i d_y)/2
K_ttb = sp.Rational(1, 4) * (sp.diff(K, x, 2) + sp.diff(K, y, 2))                     # d_tau d_taubar = Laplacian/4
DW = -NH + K_t * W; DWb = sp.conjugate(DW)
V_noscale = sp.simplify(sp.exp(K) / K_ttb * DW * DWb)
V_sugra = sp.simplify(sp.exp(K) * (DW * DWb / K_ttb - 3 * W * Wb))
V_lane = NH ** 2 * (x - NF / NH) ** 2 / (2 * y)
r = {"V_noscale": str(sp.factor(V_noscale)), "V_sugra": str(sp.factor(V_sugra)), "noscale_minus_lane": str(sp.simplify(V_noscale - V_lane))}
sub = {NF: 1, NH: 3}
dyn = sp.diff(V_noscale.subs(sub), y).subs({x: sp.Rational(1, 3)}); dxx_s = sp.diff(V_sugra.subs(sub), x, 2)
r["noscale_dV/dy_at_x=1/3_(1,3)"] = str(sp.simplify(dyn)); r["sugra_d2V/dx2_(1,3)"] = str(sp.simplify(dxx_s))
OUT["flux"] = r
print("4. K = -ln 2y, W = N_F - tau N_H:  no-scale V = %s ; SUGRA V = %s" % (r["V_noscale"], r["V_sugra"]))
print("   no-scale minus the lane's V_flux = %s ; at (N_F,N_H) = (1,3), x = 1/3: dV/dy = %s (not 0); SUGRA d2V/dx2 = %s (< 0)"
      % (r["noscale_minus_lane"], r["noscale_dV/dy_at_x=1/3_(1,3)"], r["sugra_d2V/dx2_(1,3)"]))

# --- 5. B1778's covariant derivative --------------------------------------------------------------------------------
ts = sp.Rational(1, 3) + sp.I * sp.sqrt(84) / 3
W5 = (1 - 3 * tau).subs({x: sp.Rational(1, 3), y: sp.sqrt(84) / 3})
Kt5 = K_t.subs({y: sp.sqrt(84) / 3}); DW5 = sp.nsimplify(sp.simplify(-3 + Kt5 * W5))
F5 = sp.simplify(sp.exp(K / 2) / K_ttb * DW).subs({NF: 1, NH: 3, x: sp.Rational(1, 3), y: sp.sqrt(84) / 3})
OUT["b1778"] = {"W": str(sp.simplify(W5)), "dK": str(sp.simplify(Kt5)), "DW": str(DW5), "F": str(sp.nsimplify(sp.simplify(F5))), "F_num": float(sp.N(F5))}
print("5. W(tau*) = %s, d_tau K = %s, D_tau W = %s, e^{K/2} K^{tt} D W = %s = %.6f" % (sp.simplify(W5), sp.simplify(Kt5), DW5, sp.simplify(F5), float(sp.N(F5))))
json.dump(OUT, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print("exit 0")
