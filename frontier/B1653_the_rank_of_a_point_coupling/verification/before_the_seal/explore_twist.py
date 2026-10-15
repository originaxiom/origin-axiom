"""P-128 exploration (UNSEALED, main's hand derivation's numeric support; to be disclosed as worked before the seal).
B1642's conventions: period-1 thetas, F = (f(z), f(z+tau)), f(z) = th3(z; 2tau)/sqrt(th1(z; tau)); pairings are read
through bilinears only (no branch of sqrt(th1) is ever taken beyond B1642's fixed one for f(z)f(z+tau)).
Step 1: the untwisted doublet's holonomies, measured on the bilinears.
Step 2: twisted numerators th[a,b](z; 2tau) and their holonomies.
"""
import mpmath as mp
mp.mp.dps = 30
I = mp.mpc(0, 1); NS = range(-25, 26)
e = lambda x: mp.exp(I * mp.pi * x)


def thc(a, b, z, T):
    """theta with characteristics: sum_n exp(i pi T (n+a)^2 + 2 pi i (n+a)(z+b))"""
    return mp.fsum(e(T * (n + a) ** 2 + 2 * (n + a) * (z + b)) for n in NS)


def th1(z, t): return -thc(mp.mpf(1) / 2, mp.mpf(1) / 2, z, t)   # = -i * sum (-1)^n ...; sign fixed below by a check
def th(n, z, t):
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in NS)
    if n == 2: return mp.fsum(e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in NS)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * z) for k in NS)
    if n == 4: return mp.fsum((-1) ** k * e(t * k * k + 2 * k * z) for k in NS)


t = mp.mpc(0.13, 1.07); z = mp.mpc(0.21, 0.17)
# the numerator's multipliers on the 2tau lattice, as a check of thc
for (a, b) in [(0, 0), (mp.mpf("0.1"), mp.mpf("0.3"))]:
    A = thc(a, b, z, 2 * t)
    m1 = thc(a, b, z + 1, 2 * t) / A
    m2 = thc(a, b, z + 2 * t, 2 * t) / A
    print("ab", (float(a), float(b)), "z+1:", mp.nstr(m1, 8), " expect", mp.nstr(e(2 * a), 8))
    print("   z+2tau:", mp.nstr(m2, 8), " expect", mp.nstr(e(-2 * t - 2 * (z + b)), 8))

# ---- step 3: the twisted pairings in the record's quaternion frame (hand derivation: the twisted doublet's b-holonomy
# is e^{2 pi i beta} D QJ D^-1 with beta = -b/2, D = diag(1, e^{-i pi b}); so the standard-frame doublet is
# (f(z), e^{i pi b} f(z + tau)), and the invariant pairing F~_x^T eps C F~_y carries e^{i pi (b_x + b_y)} in the j and
# k parities but e^{i pi b_x}, e^{i pi b_y} separately in the i parity)
def bil(x, y, z, t):
    (ax, bx), (ay, by) = x, y
    T = 2 * t; t1 = th(1, z, t)
    den = I * e(-t / 2) * e(-z) * t1                                   # B1642's branch for sqrt(th1(z) th1(z + tau))
    X0, X1 = thc(ax, bx, z, T), thc(ax, bx, z + t, T)
    Y0, Y1 = thc(ay, by, z, T), thc(ay, by, z + t, T)
    return {"00": X0 * Y0 / t1, "01": X0 * Y1 / den, "10": X1 * Y0 / den, "11": X1 * Y1 / th(1, z + t, t)}


def pairings(x, y, z, t):
    B = bil(x, y, z, t); bx, by = x[1], y[1]
    return {"j": -(B["00"] + e(bx + by) * B["11"]),
            "k": I * (B["00"] - e(bx + by) * B["11"]),
            "i": -I * (e(by) * B["01"] + e(bx) * B["10"])}


TH_OF = {"i": 2, "j": 4, "k": 3}; C_OF = {"i": -1, "j": -1, "k": I}
print("untwisted check against B1642's R2, c th_r(0) th_r(z)/th_1(z):")
P = pairings((0, 0), (0, 0), z, t)
for u in "ijk":
    ref = C_OF[u] * th(TH_OF[u], 0, t) * th(TH_OF[u], z, t) / th(1, z, t)
    print("  ", u, mp.nstr(abs(P[u] / ref - 1), 3))


def wpt(ab, t): return ab[0] * t + ab[1] / 2                       # the field's line point w = a tau + b/2


def shape(x, y, t, zs):
    """P_r(z) th1(z) e^{-2 pi i A z} / th_r(z + w_x + w_y): constant in z if the expected form holds"""
    A = x[0] + y[0]; s = wpt(x, t) + wpt(y, t); out = {}
    for u in "ijk":
        vals = [pairings(x, y, zz, t)[u] * th(1, zz, t) * e(-2 * A * zz) / th(TH_OF[u], zz + s, t) for zz in zs]
        out[u] = (vals[0], max(abs(v / vals[0] - 1) for v in vals[1:]))
    return out


zs = [mp.mpc(0.21, 0.17), mp.mpc(0.33, -0.12), mp.mpc(-0.4, 0.29), mp.mpc(0.05, 0.41)]
x = (mp.mpf("0.13"), mp.mpf("0.31")); y = (mp.mpf("-0.07"), mp.mpf("0.22"))
S = shape(x, y, t, zs)
print("twisted: is P_r th1 e^{-2 pi i A z}/th_r(z + w_x + w_y) constant in z?")
for u in "ijk": print("  ", u, "spread", mp.nstr(S[u][1], 3), " N =", mp.nstr(S[u][0], 10))

# ---- step 4: the normalisation N_r against c_r th_r(w_x - w_y) (a common factor across r is allowed)
def norm_ratio(x, y, t):
    S = shape(x, y, t, zs[:2]); d = wpt(x, t) - wpt(y, t)
    return {u: S[u][0] / (C_OF[u] * th(TH_OF[u], d, t)) for u in "ijk"}


for (x, y) in [((mp.mpf("0.13"), mp.mpf("0.31")), (mp.mpf("-0.07"), mp.mpf("0.22"))),
               ((mp.mpf("0.4"), mp.mpf("-0.15")), (mp.mpf("0.25"), mp.mpf("0.6"))),
               ((mp.mpf("0.0"), mp.mpf("0.5")), (mp.mpf("0.0"), mp.mpf("0.0")))]:
    Rr = norm_ratio(x, y, t)
    vals = list(Rr.values())
    print("x", [float(v) for v in x], "y", [float(v) for v in y], " ratios equal across r:",
          mp.nstr(max(abs(v / vals[0] - 1) for v in vals), 3), " common =", mp.nstr(vals[0], 8))

# ---- step 5: the quartic identity's signs, and R.R from contour residues against th1(u)^2 th1(d)^2
X, Y = mp.mpc(0.17, 0.23), mp.mpc(-0.31, 0.12)
lhs = th(3, X, t) ** 2 * th(3, Y, t) ** 2 + th(1, X, t) ** 2 * th(1, Y, t) ** 2
rhs = th(2, X, t) ** 2 * th(2, Y, t) ** 2 + th(4, X, t) ** 2 * th(4, Y, t) ** 2
print("identity th3^2th3^2 + th1^2th1^2 = th2^2th2^2 + th4^2th4^2:", mp.nstr(abs(lhs / rhs - 1), 3))


def residues(x, y, t, rad=mp.mpf("0.03"), N=64):
    out = {}
    for u in "ijk":
        s = 0
        for n in range(N):
            zz = rad * e(2 * mp.mpf(n) / N); s += pairings(x, y, zz, t)[u] * zz
        out[u] = s / N
    return out


d1 = mp.diff(lambda w: th(1, w, t), 0)
for (x, y) in [((mp.mpf("0.13"), mp.mpf("0.31")), (mp.mpf("-0.07"), mp.mpf("0.22"))),
               ((mp.mpf("0.02"), mp.mpf("0.01")), (mp.mpf("-0.01"), mp.mpf("0.03")))]:
    R = residues(x, y, t); RR = sum(R[u] ** 2 for u in "ijk")
    ub, dl = wpt(x, t) + wpt(y, t), wpt(x, t) - wpt(y, t)
    kap = norm_ratio(x, y, t)["i"]
    pred = (kap / d1) ** 2 * th(1, ub, t) ** 2 * th(1, dl, t) ** 2
    print("R.R / [kappa^2 th1(u)^2 th1(d)^2 / th1'(0)^2] =", mp.nstr(RR / pred, 12), "  |R.R|/|R|^2 =",
          mp.nstr(abs(RR) / sum(abs(R[u]) ** 2 for u in "ijk"), 4))
R0 = residues((0, 0), (0, 0), t); print("untwisted |R.R|/|R|^2 =", mp.nstr(abs(sum(R0[u] ** 2 for u in "ijk")) / sum(abs(R0[u]) ** 2 for u in "ijk"), 3))
