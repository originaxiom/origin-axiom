"""S304 PRIORITY 1 (value-free; MAIN's code + first principles; the lane's code is NOT run).

Theorem 81 (agy, 55431c8c7) says: the channel norm's 'formal L2 norm' is the Epstein-Kronecker zeta
Z_s(s; tau) = sum_{(p,r) in (alpha+Z) x (beta+Z)} Im(tau)^s / |r - p tau|^(2s), and 'subtracting the universal 1/(s-1) pole
at horocycle renormalisation scale L' gives 2 pi L + c_s exactly; its code inserts the factor (2 pi e^gamma)^(-2(s-1)) on the
1-D Hurwitz part.  Questions:
  Q1  Is c_s (main's Hadamard finite part, b1656_funcs.cA: the flat disc cut, minus 2 pi log 1/eps, plus pi eps^2 |a0|^2)
      equal to  -pi [psi(nu) + psi(1-nu)] - 2 pi (gamma + log 2 pi) + 2 pi * tail  (the closed form the lane's numbers encode)?
      Derived here independently: Fourier coefficients y/(r - p conj tau) (from dbar K = pi delta), Parseval weight
      y/|r - p tau|^2, exact Poisson summation in r, a sharp cut in p.  The multipliers (A, B) of K are read off main's K.
  Q2  What does the lane's OWN Epstein Z_s give under honest analytic continuation (Chowla-Selberg, Gamma factors kept)?
      Prediction (derived by hand): FP Z_s(1) = c_s + 2 pi (gamma + log pi) - pi log Im tau.
  Q3  The flat Laplacian's spectral zeta (eigenvalues 4 pi^2 |r - p tau|^2 / y^2, metric |du|^2, mu = 1):
      prediction FP = c_s + 2 pi (gamma - log 2).
  Q4  The end each scheme implies: L_scheme = (FP_scheme - c_s) / (2 pi), against B1667's L_max and L_2.
No firewalled quantity: c_s, residues and L are frame constants of the frame's channel norms, not targets.
    OPENBLAS_NUM_THREADS=1 nice -n 10 python3 -B p1_zeta_end.py
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import sys, json, math, cmath, pathlib, io, contextlib
import numpy as np
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
_argv = sys.argv; sys.argv = ["x"]
with contextlib.redirect_stdout(io.StringIO()):
    import b1656_funcs as B
sys.argv = _argv
mp.mp.dps = 30
EG = float(mp.euler)


def multipliers(x, y, t, s, R):
    """K_s = P_s/R_s; A, B with K(u+1) = e^{2 pi i A} K(u), K(u+tau) = e^{2 pi i B} K(u); returns (A, B, |mult|-1 max)"""
    us = np.array([0.13 + 0.21j, -0.27 + 0.08j, 0.05 - 0.3j])
    K0 = B.pairs(x, y, us, t)[s] / R[s]; K1 = B.pairs(x, y, us + 1, t)[s] / R[s]; Kt = B.pairs(x, y, us + t, t)[s] / R[s]
    m1, mt = K1 / K0, Kt / K0
    dev = max(np.max(np.abs(np.abs(m1) - 1)), np.max(np.abs(np.abs(mt) - 1)), np.ptp(np.angle(m1)), np.ptp(np.angle(mt)))
    return (np.angle(m1[0]) / (2 * np.pi)) % 1.0, (np.angle(mt[0]) / (2 * np.pi)) % 1.0, float(dev)


def c_fourier(nu, Bm, t, nmax=200):
    """-pi[psi(nu)+psi(1-nu)] - 2 pi (gamma + log 2 pi) + 2 pi sum_p Re(z_p/(1-z_p))/|p|"""
    tail = 0.0
    for n in range(nmax):
        p = n + nu; q = n + 1 - nu
        zp = cmath.exp(2j * math.pi * (p * t - Bm)); zm = cmath.exp(2j * math.pi * (q * t + Bm))
        tail += (zp / (1 - zp)).real / p + (zm / (1 - zm)).real / q
    return float(-math.pi * (mp.digamma(nu) + mp.digamma(1 - nu)) - 2 * math.pi * (EG + math.log(2 * math.pi)) + 2 * math.pi * tail)


def epstein(sv, nu, Bm, t, nmax=40, kmax=30):
    """Z(s) = sum_{p in nu+Z} sum_{r in B+Z} y^s / |r - p tau|^(2s), by Chowla-Selberg (exact Poisson in r), any s near 1"""
    sv = mp.mpf(sv); x, y = mp.mpf(t.real), mp.mpf(t.imag)
    head = mp.sqrt(mp.pi) * mp.gamma(sv - 0.5) / mp.gamma(sv) * y ** (1 - sv) * (mp.zeta(2 * sv - 1, nu) + mp.zeta(2 * sv - 1, 1 - nu))
    bes = mp.mpf(0)
    for n in range(nmax):
        for p in (n + nu, -(n + 1 - nu)):
            c = abs(p) * y
            for k in range(1, max(kmax, int(40 / (2 * float(mp.pi) * float(c))) + 5)):
                term = (k / c) ** (sv - 0.5) * mp.besselk(sv - 0.5, 2 * mp.pi * k * c)
                bes += 2 * term * mp.cos(2 * mp.pi * k * (Bm - p * x))
    return head + y ** sv * 2 * mp.pi ** sv / mp.gamma(sv) * bes


def fp(fun, d1=mp.mpf("1e-3"), d2=mp.mpf("2e-3")):
    """finite part at s = 1 of a function with a simple pole: symmetric average, Richardson in delta^2"""
    a1 = (fun(1 + d1) + fun(1 - d1)) / 2; a2 = (fun(1 + d2) + fun(1 - d2)) / 2
    return (4 * a1 - a2) / 3


# --- points: generic, not the candidate's address; lines of orders 7, 9, 12 and one order-5 line off its offset
POINTS = [complex(0.13, 1.30), complex(0.31, 2.05), complex(0.42, 2.85)]
LINES = [(1 / 7, 3 / 7), (2 / 9, 1 / 3), (5 / 12, 1 / 4)]
print("S304 P1 -- the zeta-regularised end, on main's b1656_funcs (Hadamard cA) and first principles\n")
rows = []
q1max = 0.0
for t in POINTS:
    for (a, b) in LINES:
        w = a * t + b
        for sec, (lf, rf) in (("down", ("Q", "d")), ("up", ("Q", "u"))):
            x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
            for s in B.UNITS:
                if c[s] is None: continue
                A, Bm, dev = multipliers(x, yy, t, s, R)
                nu = A if A > 1e-9 else None
                if nu is None or abs(nu - 1) < 1e-9: continue
                cf = c_fourier(nu, Bm, t)
                cf_flip = c_fourier(nu, (-Bm) % 1.0, t)
                err = abs(cf - c[s]); q1max = max(q1max, err)
                rows.append(dict(t=t, line=(a, b), sec=sec, ch=s, nu=nu, B=Bm, dev=dev, cA=c[s], cF=cf, err=err, err_flip=abs(cf_flip - c[s])))
print("Q1  main's cA (Hadamard, flat disc) vs the Fourier/Hurwitz closed form with scale 2 pi e^gamma:")
print("    %d channel cases (3 tau x 3 lines x up/down x 4 channels, nu = A not in Z); multiplier unimodularity max dev %.1e"
      % (len(rows), max(r["dev"] for r in rows)))
print("    max |c_F - cA| = %.2e   (with B -> -B instead: max %.2e, i.e. the sign convention is discriminated)"
      % (q1max, max(r["err_flip"] for r in rows)))
print("    nu values seen:", sorted(set(round(r["nu"], 6) for r in rows))[:12])

# Q2, Q3 on a subset (Chowla-Selberg is slow in mpmath)
print("\nQ2/Q3  honest analytic continuation (Chowla-Selberg, Gamma factors kept), on 6 cases:")
sub = [rows[i] for i in (0, 9, 30, 41, 60, 71) if i < len(rows)]
q2, q3 = [], []
for r in sub:
    t, nu, Bm, cs = r["t"], mp.mpf(r["nu"]), mp.mpf(r["B"]), r["cA"]
    y = t.imag
    Z = lambda sv: epstein(sv, nu, Bm, t)
    fpZ = float(fp(Z))
    ZL = lambda sv: (4 * mp.pi ** 2) ** (1 - sv) * mp.mpf(y) ** (sv - 1) * Z(sv)     # (4pi^2/y) sum lambda^-s, lambda = 4pi^2|.|^2/y^2
    fpL = float(fp(ZL))
    predZ = cs + 2 * math.pi * (EG + math.log(math.pi)) - math.pi * math.log(y)
    predL = cs + 2 * math.pi * (EG - math.log(2))
    q2.append(abs(fpZ - predZ)); q3.append(abs(fpL - predL))
    print("    tau=%s ch=%s nu=%.4f: FP Z_s - cA = %+.6f (pred %+.6f) ; FP Laplacian - cA = %+.6f (pred %+.6f)"
          % (r["t"], r["ch"], r["nu"], fpZ - cs, predZ - cs, fpL - cs, predL - cs))
print("    max |FP Z_s - prediction| = %.1e ; max |FP Laplacian - prediction| = %.1e" % (max(q2), max(q3)))
print("    => the lane's own Z_s, minimally subtracted, differs from c_s by 2 pi (gamma + log pi) - pi log Im tau (tau-DEPENDENT);")
print("       the factor (2 pi e^gamma)^(-2(s-1)) of its code is not what Poisson summation of Z_s gives")
print("       (Poisson gives sqrt(pi) Gamma(s-1/2)/Gamma(s) * Im tau^(1-s)); it is the factor that reproduces the flat-disc Hadamard c_s.")

# Q4: the end each scheme implies, against B1667's canonical radii on its Re tau = 1/4 column
col = sorted((p["tau"][1], p["L_max"], p["L_2"], p["cusp_area"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
print("\nQ4  the end L each scheme implies (FP = 2 pi L + c_s), against B1667 (Re tau = 1/4 column):")
print("    Im tau   L_max     L_2      L[Epstein Z_s, MS]   L[flat Laplacian, mu=1]   L[lane's 2 pi e^gamma scheme]")
for (yy, lm, l2, ar) in col:
    print("    %5.2f   %.4f   %.4f        %.4f                 %.4f                 free (any L, by construction)"
          % (yy, lm, l2, EG + math.log(math.pi) - 0.5 * math.log(yy), EG - math.log(2)))

# geometric facts from B1667's json (all 54 points)
pts = json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"]
grid = [p for p in pts if p.get("L_max") is not None]
eps = [math.exp(-p["L_max"]) for p in grid]
ident = max(abs((p["L_2"] - p["L_max"]) - math.pi * (1 - 2 / p["cusp_area"])) for p in grid)
print("\nGEO  B1667's %d points: e^{-L_max} in [%.4f, %.4f]; the lattice Z + tau Z has min length 1 (|tau| >= 1), so the Dirichlet"
      " cell's inradius is 1/2: the flat disc of radius e^{-L_max} is NOT embedded at any point (min - 1/2 = %+.4f)." % (len(grid), min(eps), max(eps), min(eps) - 0.5))
print("     e^{-L_2} in [%.4f, %.4f] (embedded)." % (min(math.exp(-p["L_2"]) for p in grid), max(math.exp(-p["L_2"]) for p in grid)))
print("     identity L_2 - L_max = pi (1 - 2 / A_cusp) (A_cusp = lam * min|c|): max dev %.1e over %d points (omega: A = 6 -> 2 pi/3; i: A = 4 sqrt2)."
      % (ident, len(grid)))
json.dump(dict(q1_max=q1max, q1_cases=len(rows), q2_max=max(q2), q3_max=max(q3), geo_eps_min=min(eps), geo_identity_dev=ident),
          open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
