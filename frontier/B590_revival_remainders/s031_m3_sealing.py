"""B590-R1 — S031 sealing at bronze m=3 (the corrected framing; see prereg).

The bronze SL(2) trace field K3 (b++R^3L^3; DEGREE 6 per B578-D6 — the
retracted Q(sqrt13) claim was the SCALE field) is computed in-sandbox from the
polished holonomy; the B137 off-sublocus SL(3) search (MB7 irreducibility
filter) runs at m=3; every converged irreducible point is mpmath-polished and
its nine Lawton traces classified by pari `lindep` membership in Q(gamma),
with positive and negative controls, plus the m=1 pipeline-validation run.

Run: python3 s031_m3_sealing.py (pyenv + snappy + cypari, ~10-20 min).
Nothing to CLAIMS.md.
"""
import math

import numpy as np
from scipy.optimize import least_squares
import mpmath as mp
import cypari
import snappy

pari = cypari.pari
pari.set_real_precision(90)
mp.mp.dps = 60
DPS_POLISH = 60
LINDEP_MAXH = 10 ** 6          # coefficient-height acceptance gate
RESID_GATE = mp.mpf(10) ** (-25)


# ---------------- the bronze SL(2) trace field, in-sandbox ----------------
# (snappy's polished_holonomy hits a lift bug on this manifold; we polish the
#  holonomy ourselves: pin a 3-complex gauge slice at the double-precision
#  values and Newton-solve the two relators at dps 80 — traces are
#  conjugation-invariant, so the slice choice is immaterial.)
def _mat(G, gen):
    m = G.SL2C(gen)
    return [[mp.mpc(complex(m[0, 0])), mp.mpc(complex(m[0, 1]))],
            [mp.mpc(complex(m[1, 0])), mp.mpc(complex(m[1, 1]))]]


def _mmul(X, Y):
    return [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
            [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]


def _minv2(X):
    d = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    return [[X[1][1] / d, -X[0][1] / d], [-X[1][0] / d, X[0][0] / d]]


def _word(mats, w):
    M = [[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]]
    for ch in w:
        X = mats[ch.lower()]
        M = _mmul(M, X if ch.islower() else _minv2(X))
    return M


def trace_field(word, maxdeg=16):
    mp.mp.dps = 80
    M = snappy.Manifold(word)
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    seed = {g: _mat(G, g) for g in gens}

    # parametrize [[p, q], [r, (1+qr)/p]]; pin p for gens[1:], leave gens[0]'s
    # p free, and impose COMPLETENESS: tr(gens[1]) = 2 (the parabolic; the seed
    # has it exactly). Without the parabolic equation the rep variety near the
    # seed is 1-dimensional (the Dehn family) and Newton polishes a
    # non-complete rep -- the first run's junk-field bug.
    assert abs(complex(seed[gens[1]][0][0] + seed[gens[1]][1][1]) - 2) < 1e-9, \
        "gens[1] is not the parabolic -- adjust the completeness equation"
    pins = {g: seed[g][0][0] for g in gens[1:]}

    def build(vals):
        mats = {}
        it = iter(vals)
        p0 = next(it)
        for g in gens:
            q, r = next(it), next(it)
            pcur = p0 if g == gens[0] else pins[g]
            mats[g] = [[pcur, q], [r, (1 + q * r) / pcur]]
        return mats

    def F(*vars):
        vals = [mp.mpc(vars[2 * i], vars[2 * i + 1]) for i in range(len(vars) // 2)]
        mats = build(vals)
        out = []
        for rel in rels:
            R = _word(mats, rel)
            for z in (R[0][0] - 1, R[0][1], R[1][0]):
                out.extend([z.real, z.imag])
        pb = mats[gens[1]]
        z = pb[0][0] + pb[1][1] - 2                     # completeness
        out.extend([z.real, z.imag])
        return out

    x0 = [seed[gens[0]][0][0].real, seed[gens[0]][0][0].imag]
    for g in gens:
        x0.extend([seed[g][0][1].real, seed[g][0][1].imag,
                   seed[g][1][0].real, seed[g][1][0].imag])
    sol = mp.findroot(F, [mp.mpf(v) for v in x0], tol=mp.mpf(10) ** (-60),
                      solver='mdnewton', verify=False)
    vals = [mp.mpc(sol[2 * i], sol[2 * i + 1]) for i in range(len(x0) // 2)]
    mats = build(vals)
    # gate: relators really are the identity at high precision
    for rel in rels:
        R = _word(mats, rel)
        resid = max(abs(R[0][0] - 1), abs(R[0][1]), abs(R[1][0]), abs(R[1][1] - 1))
        assert resid < mp.mpf(10) ** (-50), f"relator residual {resid}"

    def tr(X):
        return X[0][0] + X[1][1]

    a, b = mats[gens[0]], mats[gens[1]]
    trs = [tr(a), tr(b), tr(_mmul(a, b))]
    for coeffs in ((1, 3, 7), (1, 5, 11), (2, 3, 5)):
        gam = sum(c * t for c, t in zip(coeffs, trs))
        gp = pari(mp.nstr(gam.real, 70)) + pari(mp.nstr(gam.imag, 70)) * pari("I")
        # incremental degree: the first d whose algdep is irreducible, has
        # modest height, and evaluates below a strict residual gate
        for d in range(2, maxdeg + 1):
            pl = gp.algdep(d)
            if not pari.polisirreducible(pl):
                continue
            hgt = max(abs(int(c)) for c in pari.Vec(pl))
            if hgt > 10 ** 12:
                continue
            res = abs(complex(pl.subst('x', gp)))
            if res < 1e-40:
                return gam, pl, int(pari.poldegree(pl)), trs
    raise RuntimeError("no primitive element found")


print("computing the bronze SL(2) trace field (b++RRRLLL, self-polished holonomy)...")
GAMMA, MINPOLY, DEG, TRS = trace_field("b++RRRLLL")
print(f"  trace-field primitive element found: degree {DEG}")
print(f"  minpoly: {MINPOLY}")

GAM = pari(mp.nstr(GAMMA.real, 70)) + pari(mp.nstr(GAMMA.imag, 70)) * pari("I")
POWERS = [GAM ** j for j in range(DEG)]


def in_field(z, tag=""):
    """pari lindep membership of complex z in Q(GAMMA), with height+residual gates."""
    v = POWERS + [pari(str(mp.nstr(z.real, 50))) + pari(str(mp.nstr(z.imag, 50))) * pari("I")]
    rel = pari.lindep(v)
    coeffs = [int(rel[j]) for j in range(DEG + 1)]
    if coeffs[-1] == 0:
        return False
    if max(abs(c) for c in coeffs) > LINDEP_MAXH:
        return False
    resid = abs(complex(sum(pari(c) * v[j] for j, c in enumerate(coeffs))))
    return resid < 1e-30


# controls (prereg falsifier: if these fail, STOP)
print("membership-classifier controls:")
g = complex(GAMMA.real, GAMMA.imag)
ok_pos = all(in_field(mp.mpc(*divmod(0, 1)) + mp.mpc(v.real, v.imag))
             for v in (g, g * g - 3, 2 * g ** 3 + g - 7))
rng0 = np.random.default_rng(7)
ok_neg = not any(in_field(mp.mpc(x, y)) for x, y in rng0.normal(size=(3, 2)))
print(f"  known elements pass: {ok_pos};  random numbers fail: {ok_neg}")
assert ok_pos and ok_neg, "classifier controls FAILED -- stopping (prereg)"


# ---------------- the B137 search, m generic (numpy stage) ----------------
def tcoords_np(A, B):
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
    AB = A @ B
    return np.array([np.trace(A), np.trace(B), np.trace(Ai), np.trace(Bi), np.trace(AB),
                     np.trace(Bi @ Ai), np.trace(A @ Bi), np.trace(Ai @ B),
                     np.trace(A @ B @ Ai @ Bi)], dtype=complex)


def unpack_np(x):
    zc = x[0::2] + 1j * x[1::2]
    a, b = zc[0], zc[1]
    A = np.diag([a, b, 1.0 / (a * b)])
    B = zc[2:11].reshape(3, 3)
    return A, B / np.linalg.det(B) ** (1 / 3)


def residual_np(x, m):
    A, B = unpack_np(x)
    Am = np.linalg.matrix_power(A, m)
    r = tcoords_np(A, B) - tcoords_np(Am @ B, A)
    return np.concatenate([r.real, r.imag])


def algdim(A, B):
    mats, fr = [np.eye(3)], [np.eye(3)]
    for _ in range(6):
        nf = []
        for M in fr:
            for gmat in (A, B):
                nf.append(M @ gmat); mats.append(M @ gmat)
        fr = nf
        if np.linalg.matrix_rank(np.array([mm.flatten() for mm in mats]), tol=1e-6) >= 9:
            return 9
    return int(np.linalg.matrix_rank(np.array([mm.flatten() for mm in mats]), tol=1e-6))


# ---------------- mpmath polish ----------------
def polish_mp(x0, m):
    def F(*vars):
        x = [mp.mpf(v) for v in vars]
        zc = [mp.mpc(x[2 * i], x[2 * i + 1]) for i in range(11)]
        a, b = zc[0], zc[1]
        A = mp.matrix([[a, 0, 0], [0, b, 0], [0, 0, 1 / (a * b)]])
        B = mp.matrix(3, 3)
        detB = mp.mpc(1)
        for i in range(3):
            for j in range(3):
                B[i, j] = zc[2 + 3 * i + j]
        dB = (B[0, 0] * (B[1, 1] * B[2, 2] - B[1, 2] * B[2, 1])
              - B[0, 1] * (B[1, 0] * B[2, 2] - B[1, 2] * B[2, 0])
              + B[0, 2] * (B[1, 0] * B[2, 1] - B[1, 1] * B[2, 0]))
        s = dB ** (mp.mpf(1) / 3)
        for i in range(3):
            for j in range(3):
                B[i, j] = B[i, j] / s

        def tr(M):
            return M[0, 0] + M[1, 1] + M[2, 2]

        def minv(M):
            d = (M[0, 0] * (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
                 - M[0, 1] * (M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0])
                 + M[0, 2] * (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0]))
            C = mp.matrix(3, 3)
            C[0, 0] = (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1]) / d
            C[0, 1] = -(M[0, 1] * M[2, 2] - M[0, 2] * M[2, 1]) / d
            C[0, 2] = (M[0, 1] * M[1, 2] - M[0, 2] * M[1, 1]) / d
            C[1, 0] = -(M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0]) / d
            C[1, 1] = (M[0, 0] * M[2, 2] - M[0, 2] * M[2, 0]) / d
            C[1, 2] = -(M[0, 0] * M[1, 2] - M[0, 2] * M[1, 0]) / d
            C[2, 0] = (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0]) / d
            C[2, 1] = -(M[0, 0] * M[2, 1] - M[0, 1] * M[2, 0]) / d
            C[2, 2] = (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) / d
            return C

        def tc(A, B):
            Ai, Bi = minv(A), minv(B)
            AB = A * B
            return [tr(A), tr(B), tr(Ai), tr(Bi), tr(AB), tr(Bi * Ai),
                    tr(A * Bi), tr(Ai * B), tr(A * B * Ai * Bi)]

        Am = A ** m
        r = [u - v for u, v in zip(tc(A, B), tc(Am * B, A))]
        out = []
        for z in r:
            out.extend([z.real, z.imag])
        return out[:22]

    sol = mp.findroot(F, [mp.mpf(v) for v in x0], tol=mp.mpf(10) ** (-45),
                      solver='mdnewton', verify=False)
    return [mp.mpf(sol[i]) for i in range(22)]


def traces_mp(xs, m):
    zc = [mp.mpc(xs[2 * i], xs[2 * i + 1]) for i in range(11)]
    a, b = zc[0], zc[1]
    A = np.array([[complex(a), 0, 0], [0, complex(b), 0], [0, 0, complex(1 / (a * b))]])
    # high-precision traces via mp matrices (reuse the polished coordinates)
    Amp = mp.matrix([[a, 0, 0], [0, b, 0], [0, 0, 1 / (a * b)]])
    Bmp = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            Bmp[i, j] = zc[2 + 3 * i + j]
    dB = (Bmp[0, 0] * (Bmp[1, 1] * Bmp[2, 2] - Bmp[1, 2] * Bmp[2, 1])
          - Bmp[0, 1] * (Bmp[1, 0] * Bmp[2, 2] - Bmp[1, 2] * Bmp[2, 0])
          + Bmp[0, 2] * (Bmp[1, 0] * Bmp[2, 1] - Bmp[1, 1] * Bmp[2, 0]))
    s = dB ** (mp.mpf(1) / 3)
    for i in range(3):
        for j in range(3):
            Bmp[i, j] = Bmp[i, j] / s

    def tr(M):
        return M[0, 0] + M[1, 1] + M[2, 2]

    Ai = Amp ** -1
    Bi = Bmp ** -1
    return [tr(Amp), tr(Bmp), tr(Ai), tr(Bi), tr(Amp * Bmp), tr(Bi * Ai),
            tr(Amp * Bi), tr(Ai * Bmp), tr(Amp * Bmp * Ai * Bi)]


def sealing_run(m, starts, seed, field_test):
    rng = np.random.default_rng(seed)
    irred = escapes = red_ignored = polish_fail = 0
    for _ in range(starts):
        x0 = np.empty(22)
        z = rng.normal(size=11) + 1j * rng.normal(size=11)
        x0[0::2], x0[1::2] = z.real, z.imag
        sol = least_squares(residual_np, x0, args=(m,), method="trf",
                            ftol=1e-14, xtol=1e-14, gtol=1e-14, max_nfev=6000)
        if np.linalg.norm(sol.fun) > 1e-9:
            continue
        A, B = unpack_np(sol.x)
        if algdim(A, B) != 9:
            red_ignored += 1
            continue
        irred += 1
        try:
            xs = polish_mp(list(sol.x), m)
        except Exception:
            polish_fail += 1
            continue
        trs = traces_mp(xs, m)
        if not all(field_test(t) for t in trs):
            escapes += 1
    return {"m": m, "irreducible": irred, "escapes": escapes,
            "reducible_ignored": red_ignored, "polish_failures": polish_fail}


# ---------------- m=1 pipeline validation (must reproduce sealing) ----------------
print("\nm=1 pipeline validation (Q(sqrt-3); must be sealed):")
w3 = mp.sqrt(-3)


def in_qsqrtm3(z):
    v = [pari("1"), pari("I*sqrt(3)"),
         pari(str(mp.nstr(z.real, 50))) + pari(str(mp.nstr(z.imag, 50))) * pari("I")]
    rel = pari.lindep(v)
    c = [int(rel[j]) for j in range(3)]
    if c[-1] == 0 or max(abs(x) for x in c) > LINDEP_MAXH:
        return False
    return abs(complex(pari(c[0]) + pari(c[1]) * pari("I*sqrt(3)")
                       + pari(c[2]) * v[2])) < 1e-30


r1 = sealing_run(1, starts=60, seed=20260714, field_test=in_qsqrtm3)
print(f"  {r1}")
assert r1["irreducible"] >= 5 and r1["escapes"] == 0, "m=1 validation FAILED"
print("  m=1 SEALED (pipeline validated)")

# ---------------- the m=3 run (two seeds, per the rigor memory) ----------------
print("\nm=3 bronze sealing run (the degree-%d trace field):" % DEG)
for seed in (20260714, 31415926):
    r3 = sealing_run(3, starts=120, seed=seed, field_test=in_field)
    print(f"  seed {seed}: {r3}")
    verdict = "SEALED" if (r3["escapes"] == 0 and r3["irreducible"] >= 5) else \
        ("NOT-SEALED" if r3["escapes"] > 0 else "UNSTABLE(too few points)")
    print(f"  verdict at this seed: {verdict}")
print("\nDONE")
