"""The web seat's check for its note on B1656's channel kernels and their norms (data-free; no measured value is read).

Notation. A sector with left and right twists x = (a_x, b_x), y = (a_y, b_y) (main's twist_of) has the summed twist
S = x + y = (a_S, b_S); on a flat line w = p1 tau - p2 (main's line_w), S = (q_L + q_R) w in twist coordinates:
a_S = (q_L + q_R) p1, b_S = -2 (q_L + q_R) p2, with q_L + q_R = -3 (up), +3 (down, leptons). Channel s has the theta
characteristic (a, b) = (a_S + alpha_s, b_S/2 + beta_s), (alpha_s, beta_s) = k (0, 0), j (0, 1/2), i (1/2, 0), 1 (1/2, 1/2),
with main's thc convention theta[a, b](u | tau) = sum_n exp(i pi tau (n + a)^2 + 2 pi i (n + a)(u + b)). Its multipliers
are K(u + 1) = exp(2 pi i lambda) K(u), K(u + tau) = exp(2 pi i mu) K(u) with lambda = frac(a + 1/2), mu = frac(1/2 - b).
The norm of a twisted Kronecker kernel with (lambda, mu) at tau is the SM seat's W177 series, written here as
    c(lambda, mu; tau) = c_inf(lambda) + pi sum_n [P(rho_n, phi_n) - 1] / |n + lambda|,
    c_inf(lambda) = -2 pi ln 2 pi - 2 pi gamma - pi [psi(lambda) + psi(1 - lambda)],
    rho_n = exp(-2 pi |n + lambda| Im tau), phi_n = 2 pi [(n + lambda) Re tau - mu], P(r, f) = (1 - r^2)/(1 - 2 r cos f + r^2).

It prints:
 (1) main's kernels are twisted Kronecker (Szego) kernels of S: P_s(u) theta_1(u)/theta[c_s](u) is constant in u, and
     main's a0_of equals d/du log theta[c_s](u) at 0 (random twists and tau);
 (2) the parity: a0 odd between up and down, the leptons equal to down, the norms shared, on three flat lines; and
     B1728's step 3 in the form used (P_s(-x, -y; u) = -P_s(x, y; -u));
 (3) the series above, in the channel map, against main's cA (random twists and tau);
 (4) the pair sums: (c_k + c_j)/2 = c(Lambda, 2M; 2 tau) and (c_1 + c_i)/2 = c(Lambda', 2M; 2 tau), Lambda = frac(a_S + 1/2),
     Lambda' = frac(a_S), M = frac(1/2 - b_S/2), main's cA on the left;
 (5) B1788's hypothesis (b): sigma_b = c_j + c_k - c_1 - c_i by main's cA on main's B1826 lines and on the order-8 lines
     (1/4, odd/8), with the closed form on 3 a_S = ... (see the note), its exponent, and the census count;
 (6) B1788's hypothesis (a): the decay exponents of c_k - c_j and c_i - c_1 fitted from the series, and the per-term
     inequalities over every slope with denominator <= 20, three sectors;
 (7) the cusp classes on P-512's slopes and P-512's constants in closed form.

Usage: python3 kernels_and_norms.py <main checkout>   (main at 0f3e71a24; b1656_funcs is byte-identical on main since B1691)
"""
import contextlib
import io
import math
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np
from mpmath import mp, mpf, psi, euler

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]
mp.dps = 40
OFF = {"k": (Fr(0), Fr(0)), "j": (Fr(0), Fr(1, 2)), "i": (Fr(1, 2), Fr(0)), "1": (Fr(1, 2), Fr(1, 2))}
SECT = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
HALF = Fr(1, 2)


def quiet(f, *a):
    with contextlib.redirect_stdout(io.StringIO()):
        return f(*a)


def M2(v):
    return mpf(v.numerator) / v.denominator if isinstance(v, Fr) else mpf(v)


def nn(v):
    v = v % 1
    return min(v, 1 - v)


def theta(a, b, u, t):
    return complex(np.asarray(B.thc(a, b, u, t)))


def lam_mu(a, b):
    return (a + 0.5) % 1.0, (0.5 - b) % 1.0


def cinf(lam):
    lam = M2(lam)
    return -2 * mp.pi * mp.log(2 * mp.pi) - 2 * mp.pi * euler - mp.pi * (psi(0, lam) + psi(0, 1 - lam))


def series(lam, mu, t, N=40):
    """W177's series in double precision"""
    n = np.arange(-N, N + 1); m = n + float(lam)
    rho = np.exp(-2 * np.pi * np.abs(m) * t.imag); ph = 2 * np.pi * (m * t.real - float(mu))
    P = (1 - rho * rho) / (1 - 2 * rho * np.cos(ph) + rho * rho)
    return float(cinf(lam)) + np.pi * float(np.sum((P - 1) / np.abs(m)))


def series_mp(lam, mu, t, N=30):
    """W177's series at 40 digits"""
    lam = M2(lam); mu = M2(mu); t = mp.mpc(t); tot = cinf(lam)
    for n in range(-N, N + 1):
        m = n + lam; rho = mp.exp(-2 * mp.pi * abs(m) * t.imag); ph = 2 * mp.pi * (m * t.real - mu)
        tot += mp.pi * ((1 - rho ** 2) / (1 - 2 * rho * mp.cos(ph) + rho ** 2) - 1) / abs(m)
    return tot


def chan(aS, bS, s):
    return aS + OFF[s][0], bS / 2 + OFF[s][1]


def norms_on_line(p1, p2, t, sector):
    ql, qr = SECT[sector]
    w = B.line_w(p1, p2, t); x, y = quiet(B.sector_twists, w, t, ql, qr)
    R = quiet(B.residues, x, y, t); return quiet(B.cA, x, y, t, R)


def sigma_b(C):
    return C["j"] + C["k"] - C["1"] - C["i"]


rng = np.random.default_rng(20261103)


def random_point():
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.2, 3.0))
    return t, (rng.uniform(-1, 1), rng.uniform(-2, 2)), (rng.uniform(-1, 1), rng.uniform(-2, 2))


print("(1) main's kernels are twisted Kronecker kernels of S = x + y (6 random (x, y, tau), four channels)")
w1 = w2 = 0.0
for _ in range(6):
    t, x, y = random_point(); aS, bS = x[0] + y[0], x[1] + y[1]
    us = rng.uniform(0.05, 0.4, 8) * np.exp(2j * np.pi * rng.uniform(0, 1, 8))
    P = B.pairs(x, y, us, t); th1 = np.asarray(B.th1(us, t))
    R = B.residues(x, y, t); A0 = B.a0_of(x, y, t, R)
    for s in B.UNITS:
        a, b = chan(aS, bS, s)
        r = P[s] * th1 / np.array([theta(a, b, u, t) for u in us])
        w1 = max(w1, float(np.max(np.abs(r - r.mean())) / abs(r.mean())))
        h = 1e-3; f = lambda u: theta(a, b, u, t)
        dl = (-f(2 * h) + 8 * f(h) - 8 * f(-h) + f(-2 * h)) / (12 * h) / f(0.0)
        if A0[s] is not None:
            w2 = max(w2, abs(A0[s] - dl) / max(1.0, abs(A0[s])))
print("    max relative spread in u of P_s theta_1 / theta[c_s]: %.1e" % w1)
print("    max |a0_of - d log theta[c_s](0)| / max(1, |a0|): %.1e  (a0_of's circle mean, radius 0.05, 128 points)" % w2)

print("(2) the parity on flat lines (S(up) = -S(down) = -S(lepton)), and B1728's step 3")
for (p1, p2), t in (((Fr(3, 8), Fr(3, 8)), complex(0.093359375, 2.742578125)), ((Fr(1, 7), Fr(0)), complex(0.2, 1.9)),
                    ((Fr(2, 9), Fr(1, 3)), complex(0.3, 2.4))):
    w = B.line_w(p1, p2, t); A0 = {}; C = {}
    for sn, (ql, qr) in SECT.items():
        x, y = quiet(B.sector_twists, w, t, ql, qr); R = quiet(B.residues, x, y, t)
        A0[sn] = quiet(B.a0_of, x, y, t, R); C[sn] = quiet(B.cA, x, y, t, R)
    ok = [s for s in B.UNITS if all(A0[sn][s] is not None for sn in SECT)]
    print("    line (%s, %s), tau %.4f%+.4fi, channels %s: max |a0(up) + a0(down)| %.1e, max |a0(lepton) - a0(down)| %.1e, "
          "max |c_s(sector) - c_s(down)| %.1e, max |a0| %.2f"
          % (p1, p2, t.real, t.imag, "".join(ok), max(abs(A0["up"][s] + A0["down"][s]) for s in ok),
             max(abs(A0["lepton"][s] - A0["down"][s]) for s in ok),
             max(abs(C[sn][s] - C["down"][s]) for sn in SECT for s in ok), max(abs(A0["down"][s]) for s in ok)))
w3 = 0.0
for _ in range(6):
    t, x, y = random_point(); us = rng.uniform(0.05, 0.4, 6) * np.exp(2j * np.pi * rng.uniform(0, 1, 6))
    P = B.pairs(x, y, us, t); Pm = B.pairs((-x[0], -x[1]), (-y[0], -y[1]), -us, t)
    for s in B.UNITS:
        w3 = max(w3, float(np.max(np.abs(Pm[s] + P[s]) / np.abs(P[s]))))
print("    B1728's step 3 as used: max |P_s(-x, -y; -u) + P_s(x, y; u)| / |P_s| over 6 random points: %.1e" % w3)

print("(3) W177's series in the channel map against main's cA (8 random (x, y, tau), four channels)")
w4 = 0.0
for _ in range(8):
    t, x, y = random_point(); aS, bS = x[0] + y[0], x[1] + y[1]
    C = B.cA(x, y, t, B.residues(x, y, t))
    for s in B.UNITS:
        if C[s] is None: continue
        w4 = max(w4, abs(series(*lam_mu(*chan(aS, bS, s)), t) - C[s]))
print("    max |series - cA|: %.1e" % w4)

print("(4) the pair sums against the norm at 2 tau (6 random (x, y, tau); main's cA on the left)")
w5 = 0.0
for _ in range(6):
    t, x, y = random_point(); aS, bS = x[0] + y[0], x[1] + y[1]
    C = B.cA(x, y, t, B.residues(x, y, t))
    Lam, Lp, M = (aS + 0.5) % 1.0, aS % 1.0, (0.5 - bS / 2) % 1.0
    w5 = max(w5, abs((C["k"] + C["j"]) / 2 - float(series_mp(Lam, (2 * M) % 1.0, 2 * t))),
             abs((C["1"] + C["i"]) / 2 - float(series_mp(Lp, (2 * M) % 1.0, 2 * t))))
print("    max |(c_k + c_j)/2 - c(Lambda, 2M; 2tau)|, |(c_1 + c_i)/2 - c(Lambda', 2M; 2tau)|: %.1e" % w5)

print("(5) B1788's hypothesis (b): sigma_b = c_j + c_k - c_1 - c_i")
TAUS = (complex(0.13, 1.9), complex(0.31, 2.6), complex(0.0, 2.2), complex(0.5, 2.2))
print("    (5a) main's cA, down sector, at tau = " + ", ".join("%.2f%+.2fi" % (t.real, t.imag) for t in TAUS))
for p1, p2 in ((Fr(1, 12), Fr(0)), (Fr(1, 12), Fr(1, 12)), (Fr(5, 12), Fr(1, 3)), (Fr(1, 4), Fr(0)), (Fr(1, 4), Fr(1, 2)),
               (Fr(1, 4), Fr(1, 8)), (Fr(1, 4), Fr(3, 8)), (Fr(1, 4), Fr(5, 8)), (Fr(1, 4), Fr(7, 8))):
    vals = []; spread = 0.0
    for t in TAUS:
        Cs = {sn: norms_on_line(p1, p2, t, sn) for sn in SECT}
        v = sigma_b(Cs["down"]); vals.append(v); spread = max(spread, max(abs(sigma_b(Cs[sn]) - v) for sn in SECT))
    print("        line (%s, %s), 12 p2 %s: %s   (three sectors agree to %.0e)"
          % (p1, p2, "integer    " if (12 * p2).denominator == 1 else "not integer",
             "  ".join("%+.3e" % v for v in vals), spread))


def sigma_b_closed(Lam, M, t, K=12, N=30):
    """8 pi sum_k sin(2 pi k 2M) sum_n rho_n(2 tau)^k sin(2 pi k (n + Lam) Re 2tau)/|n + Lam|, valid when Lambda' = 1 - Lambda"""
    T = 2 * mp.mpc(t); tot = mpf(0)
    for k in range(1, K + 1):
        sk = mp.sin(2 * mp.pi * k * 2 * M2(M))
        for n in range(-N, N + 1):
            m = n + M2(Lam); tot += sk * mp.exp(-2 * mp.pi * k * abs(m) * T.imag) * mp.sin(2 * mp.pi * k * m * T.real) / abs(m)
    return 8 * mp.pi * tot


print("    (5b) the closed form on 3 alpha = 1/4 mod 1/2 against main's cA (down sector, lines (1/4, k/8))")
w6 = 0.0
for p2 in (Fr(1, 8), Fr(3, 8), Fr(0), Fr(1, 2)):
    aS, bS = 3 * Fr(1, 4), -6 * p2
    for t in TAUS:
        cl = float(sigma_b_closed((aS + HALF) % 1, (HALF - bS / 2) % 1, t))
        w6 = max(w6, abs(cl - sigma_b(norms_on_line(Fr(1, 4), p2, t, "down"))))
print("        max |closed form - main's sigma_b| over 4 lines x 4 tau: %.1e" % w6)
aS, bS = Fr(3, 4), -6 * Fr(1, 8)
d6 = sigma_b_closed((aS + HALF) % 1, (HALF - bS / 2) % 1, complex(0.13, 6))
d7 = sigma_b_closed((aS + HALF) % 1, (HALF - bS / 2) % 1, complex(0.13, 7))
print("        exponent of sigma_b on (1/4, 1/8) at Re tau 0.13 (Im tau 6 -> 7, B1788's convention): %.4f" % float(-mp.log(abs(d7 / d6)) / (2 * mp.pi)))
print("        mirror: sigma_b(-conj tau) + sigma_b(tau) on (1/4, 1/8) at 0.13 + 1.9i: %.1e"
      % abs(sigma_b(norms_on_line(Fr(1, 4), Fr(1, 8), complex(-0.13, 1.9), "down")) + sigma_b(norms_on_line(Fr(1, 4), Fr(1, 8), complex(0.13, 1.9), "down"))))
orbits = {}
for N in range(1, 13):
    for a in range(N):
        for b in range(N):
            p = (Fr(a, N), Fr(b, N))
            if np.lcm(p[0].denominator, p[1].denominator) > 12: continue
            key = min(p, ((-p[0]) % 1, (-p[1]) % 1))
            orbits[key] = True
on = [l for l in orbits if (3 * l[0]) % HALF == Fr(1, 4)]
keep = sorted(l for l in on if (12 * l[1]).denominator != 1)
fmt = lambda l: "(%s, %s)" % l
print("    (5c) census lines of order <= 12 up to the torus involution: %d; on the slopes 3 alpha = 1/4 mod 1/2: %d; with 12 p2 an "
      "integer: %d; not: %d: %s" % (len(orbits), len(on), len(on) - len(keep), len(keep), ", ".join(fmt(l) for l in keep)))


def excluded(ql, qr, p1, p2):
    """B1788's exclusion: q alpha in {0, 1/2} with 2 q b = 1/2 mod 1 (w = alpha tau + b, so b = -p2)"""
    return any((q * p1) % HALF == 0 and (2 * q * (-p2)) % 1 == HALF for q in (ql, qr))


print("        B1788's excluded line-sectors (a theta constant vanishes) on those lines: %s"
      % ", ".join("%s %s" % (fmt(l), sn) for l in keep for sn, (ql, qr) in SECT.items() if excluded(ql, qr, *l)))

print("(6) B1788's hypothesis (a)")
print("    (6a) decay exponents fitted from the series (Re tau 0.17, Im tau 6 -> 7), against ||a_S + 1/2|| and ||a_S||")
for p1, p2 in ((Fr(2, 5), Fr(0)), (Fr(1, 7), Fr(1, 7)), (Fr(4, 9), Fr(1, 3)), (Fr(1, 8), Fr(3, 8)), (Fr(3, 10), Fr(1, 5))):
    for sn, (ql, qr) in SECT.items():
        aS, bS = (ql + qr) * p1, -2 * (ql + qr) * p2; out = []
        for s1, s2, pred in (("k", "j", nn(aS + HALF)), ("i", "1", nn(aS))):
            d = [series_mp(*lam_mu_exact, complex(0.17, yy)) - series_mp(*lam_mu_exact2, complex(0.17, yy))
                 for yy in (6, 7) for lam_mu_exact, lam_mu_exact2 in
                 [(((chan(aS, bS, s1)[0] + HALF) % 1, (HALF - chan(aS, bS, s1)[1]) % 1),
                   ((chan(aS, bS, s2)[0] + HALF) % 1, (HALF - chan(aS, bS, s2)[1]) % 1))]]
            out.append("c_%s - c_%s %.4f (pred %s)" % (s1, s2, float(-mp.log(abs(d[1] / d[0])) / (2 * mp.pi)), pred))
        print("        line (%s, %s) %-6s: %s" % (p1, p2, sn, ";  ".join(out)))
print("    (6b) per term over every slope p1 in (0, 1/2] with denominator <= 20 and 2 a_S not an integer, three sectors")
cases = t2 = t1 = both = 0; m2 = m1 = Fr(1); worded = []
for q in range(1, 21):
    for p in range(1, q + 1):
        al = Fr(p, q)
        if al.denominator != q or al > HALF: continue
        for sn, (ql, qr) in SECT.items():
            aS = (ql + qr) * al
            if (2 * aS).denominator == 1: continue
            dx, dy = nn(ql * al), nn(qr * al)
            Ejk, E1i = nn(aS + HALF), nn(aS)
            g2, g1 = Ejk - abs(dx + dy - HALF), E1i - abs(dx - dy)
            cases += 1; m2 = min(m2, g2); m1 = min(m1, g1)
            t2 += g2 == 0; t1 += g1 == 0; both += (g2 == 0 and g1 == 0)
            if E1i < abs(dx + dy - HALF) or Ejk < abs(dx + dy - HALF):
                worded.append("%s %s" % (al, sn))
print("        cases %d; min of E(c_j - c_k) - |E00 - E11|: %s; min of E(c_1 - c_i) - |E01 - E10|: %s" % (cases, m2, m1))
print("        ties: the j-k term %d, the 1-i term %d, both %d, neither %d" % (t2, t1, both, cases - t2 - t1 + both))
print("        as worded (both differences against |E00 - E11|) it fails in %d cases: %s" % (len(worded), ", ".join(worded)))

print("(7) the cusp classes and P-512's constants")
for al in (Fr(1, 8), Fr(3, 8)):
    aS = 3 * al
    lam = {s: (aS + OFF[s][0] + HALF) % 1 for s in B.UNITS}
    C = norms_on_line(al, Fr(137, 1000), complex(0.1, 10.0), "down")
    print("    slope %s, Im tau 10: " % al + "  ".join("%s lambda %s c %+.6f c_inf %+.6f" % (s, lam[s], C[s], float(cinf(lam[s]))) for s in B.UNITS))
r2 = mp.sqrt(2) * mp.log(1 + mp.sqrt(2)); l8 = mp.log(mpf(8) / mp.pi)
gauss = lambda p, q: 2 * mp.pi * mp.log(mpf(q) / mp.pi) - 4 * mp.pi * mp.fsum(mp.cos(2 * mp.pi * k * p / q) * mp.log(mp.sin(mp.pi * k / q)) for k in range(1, (q - 1) // 2 + 1))
print("    c_inf(3/8): digamma %s, Gauss %s, 2 pi (ln(8/pi) - sqrt2 ln(1+sqrt2)) %s" % (mp.nstr(cinf(Fr(3, 8)), 14), mp.nstr(gauss(3, 8), 14), mp.nstr(2 * mp.pi * (l8 - r2), 14)))
print("    c_inf(1/8): digamma %s, Gauss %s, 2 pi (ln(8/pi) + sqrt2 ln(1+sqrt2)) %s" % (mp.nstr(cinf(Fr(1, 8)), 14), mp.nstr(gauss(1, 8), 14), mp.nstr(2 * mp.pi * (l8 + r2), 14)))
for name, L in (("L_max", mpf("0.643051")), ("L_2", mpf("2.292257"))):
    xv = (L + l8 - r2) / (L + l8 + r2)
    print("    x at %s = %s: %s" % (name, L, mp.nstr(xv, 9)))
print("    x > 0 iff L > sqrt2 ln(1+sqrt2) - ln(8/pi) = %s; x = 1/4 at L = (5 sqrt2 ln(1+sqrt2) - 3 ln(8/pi))/3 = %s"
      % (mp.nstr(r2 - l8, 9), mp.nstr((5 * r2 - 3 * l8) / 3, 9)))
