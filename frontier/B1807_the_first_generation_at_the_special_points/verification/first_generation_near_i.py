"""P-431 (exploratory, audit room; data-free; under B1691's tagged H-cov and B1654's large-L lift): the first generation near
tau = i.  B1691: m1 = |D||a.R|/(2 pi L |R|^2) and a.R = -f2 (dR.dR); B1806: dR.dR = eta^6/4.  So with D(i) != 0 (B1654 N5),
m1/m3's exponent at i is nu_i(f2), the order of the weight-(2n-4) form f2 at i -- PREDICTED odd (E6 divides f2) for k = 3/2 mod 4
and even for k = 7/2 mod 4.  Checked here with the exact s1 (SVD of B1646's Y(a)), never B1691's proxy (E93):
  (0) the identity a.R + f2 eta^6/4 = 0 exactly in q^(1/8)-series, for random sections at each weight;
  (1) the lift factor |a.R|/(s1 |R|^2)'s slope in |tau - i| at weights where the prediction was written before the run.
    python3 first_generation_near_i.py      # writes first_generation_near_i.json beside itself
"""
import json, pathlib, random, sys
from fractions import Fraction as F
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
B = sorted((HERE.parents[2] / "frontier").glob("B1691_*"))[0] / "verification"
sys.path.insert(0, str(B))
from qseries import S, theta2, theta3, E2, E4, E6, serre

mp.mp.dps = 50
th2, th3, th4 = theta2(), theta3(1), theta3(-1)
R = [-(th2 * th2) * (th2 * th3 * th4).inv(), -(th4 * th4) * (th2 * th3 * th4).inv(),
     (th3 * th3) * S.c(0, 1) * (th2 * th3 * th4).inv()]
e2, e4, e6 = E2(), E4(), E6()
Bs = [R, [serre(c, F(-1, 2), e2) for c in R]]
Bs.append([serre(c, F(3, 2), e2) for c in Bs[1]])
eta6 = (th2 * th3 * th4) * (th2 * th3 * th4) * S.c(F(1, 4))
dot = lambda u, v: u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def mono(a, b):
    f = S.c(1)
    for _ in range(a): f = f * e4
    for _ in range(b): f = f * e6
    return f


def Mbasis(w): return [mono(a, (w - 4 * a) // 6) for a in range(w // 4 + 1) if w >= 0 and (w - 4 * a) % 6 == 0]


def rnd(rng): return S.c(F(rng.randint(-9, 9) or 1, rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5)))


def section(n, seed, f2=None):
    """f0 R + f1 dR + f2 d2R at weight 2n - 1/2; f0, f1 random in M_{2n}, M_{2n-2}; f2 random unless given"""
    rng = random.Random(7000 * seed + n); fs = []
    for j in range(3):
        w = 2 * n - 2 * j
        if j == 2 and f2 is not None: fs.append(f2); continue
        f = S()
        for g in Mbasis(w): f = f + rnd(rng) * g
        fs.append(f)
    a = [S(), S(), S()]
    for j in range(3):
        for i in range(3): a[i] = a[i] + fs[j] * Bs[j][i]
    return a, fs[2]


def ev(s, tau):
    x = mp.exp(2j * mp.pi * tau / 8)
    return mp.fsum(mp.mpc(mp.mpf(p.numerator) / p.denominator, mp.mpf(q.numerator) / q.denominator) * x ** k for k, (p, q) in s.d.items())


def lift(a, tau):
    av = [ev(c, tau) for c in a]; Rv = [ev(c, tau) for c in R]
    aR = sum(u * v for u, v in zip(av, Rv)); nR = sum(abs(v) ** 2 for v in Rv)
    Y = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3): Y[r, c] = av[r] * Rv[c] + Rv[r] * av[c] - (aR if r == c else 0)
    s = sorted([abs(x) for x in mp.svd_c(Y, compute_uv=False)], reverse=True)
    return abs(aR) / (s[0] * nR), s[1] / s[0]


I = mp.mpc(0, 1); out = {"identity a.R + f2 eta^6/4 = 0": {}, "slopes": {}}
for n in range(0, 12):
    a, f2 = section(n, 1)
    resid = dot(a, R) + f2 * eta6 * S.c(F(1, 4))
    out["identity a.R + f2 eta^6/4 = 0"][str(F(4 * n - 1, 2))] = (resid.ord() is None or resid.ord() > 200)
# the predictions, written before the run: (n, f2 or None for random, predicted slope of the lift factor at i)
cases = [(5, None, 1, "19/2, f2 in M6 = <E6>"), (7, None, 1, "27/2, f2 in M10 = <E4 E6>"),
         (9, None, 1, "35/2, f2 in M14 = <E4^2 E6>"), (11, None, 1, "43/2, f2 random in M18"),
         (11, mono(0, 3), 3, "43/2, f2 = E6^3"), (11, mono(3, 1), 1, "43/2, f2 = E4^3 E6"),
         (4, None, 0, "15/2, f2 in M4 = <E4>"), (8, None, 0, "31/2, f2 random in M12"),
         (8, mono(0, 2), 2, "31/2, f2 = E6^2"), (10, mono(1, 2), 2, "39/2, f2 = E4 E6^2"),
         (1, None, None, "3/2 (no f2: m1 = 0 identically)"), (3, None, None, "11/2 (no f2: m1 = 0 identically)")]
for n, f2, pred, name in cases:
    row = {"predicted": pred}
    for seed in (1, 2):
        a, _ = section(n, seed, f2)
        sl, m23 = [], None
        for th in (0.3, 1.9, 4.1):
            v = [lift(a, I + mp.mpf(10) ** -e * mp.exp(1j * th)) for e in (5, 6)]
            if m23 is None: m23 = v[1][1]
            sl.append(None if v[1][0] < mp.mpf(10) ** -40 else round(float(mp.log(v[0][0] / v[1][0]) / mp.log(10)), 3))
        row["seed%d" % seed] = {"slope_lift_in_eps": sl, "m2/m3_exact_at_eps_1e-6": mp.nstr(m23, 6)}
    obs = [row["seed%d" % s]["slope_lift_in_eps"] for s in (1, 2)]
    row["holds"] = all(all(x is None for x in o) for o in obs) if pred is None else all(all(x is not None and abs(x - pred) < 0.01 for x in o) for o in obs)
    out["slopes"][name] = row
# POST HOC (labelled; seen in the first launch, not predicted): in the k = 7/2 mod 4 class f1(i) = 0 always (E6 divides
# M_{2n-2}), so f2(i) = 0 puts a(i) = f0(i) R(i) on R(i)'s isotropic line: m2/m3 should then vanish like |tau - i|^2
dd = dot(Bs[1], Bs[1]) * eta6.inv()
out["dR.dR / eta^6"] = {"constant": len([k for k in dd.d if k <= 150]) == 1 and dd.ord() == 0, "value": [str(v) for v in dd.lead()]}
ph = {}
for n, f2, name in ((8, mono(0, 2), "31/2, f2 = E6^2"), (10, mono(1, 2), "39/2, f2 = E4 E6^2"), (8, None, "31/2, f2 random (control)")):
    row = {}
    for seed in (1, 2):
        a, _ = section(n, seed, f2); sl = []
        for th in (0.3, 1.9, 4.1):
            v = [lift(a, I + mp.mpf(10) ** -e * mp.exp(1j * th))[1] for e in (5, 6)]
            sl.append(round(float(mp.log(v[0] / v[1]) / mp.log(10)), 3))
        row["seed%d" % seed] = sl
    ph[name] = row
out["POST HOC m2/m3 slope in eps"] = ph
out["all_hold"] = all(out["identity a.R + f2 eta^6/4 = 0"].values()) and all(r["holds"] for r in out["slopes"].values())
(HERE / "first_generation_near_i.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(json.dumps(out, indent=1))
