#!/usr/bin/env python3
"""B1527 controls, run BEFORE the seal on banked m004 data only (sm:B1509's extension points; Ballas' family at its banked
symmetric axis).  Nothing here touches another word state.

C1  the slice matrix in closed form against mpmath's expm (scan_lib.selftest): relative error < 1e-13.
C2  route Fox (cusp_lib) on Ballas' presentation reproduces sm:B1509's exact extension indices: at q = 17 +- 12 sqrt2 with
    mu = -1, I(W1) = -1 and I(W2) = +1, W1 data (a0, h1, t0, r1) = (0, 1, 1, 1); at q = 7 +- 4 sqrt3 with mu = i, I(W1) = 0.
C3  the isomorphism of Ballas' presentation onto route F's +LR (a = n m^-1, b = m n^-1 m n m^-2, t = m): the relators of +LR
    hold for rho_q transported (generic q), and the fibre boundary abAB has the power sums tr(L^k) = 3 q^k + q^-3k (k <= 4) of
    the eigenvalues q, q, q, q^-3 (sm:B1509 T1; the audit lane's R44): it is the knot's longitude, with that orientation.
    (Its first form compared eigenvalues at 1e-40; a Jordan block limits them to about 1e-30 at 60 digits, so it failed on its
    own design and was replaced by the power sums before any other state was touched.)
C4  W1 and W2 transported to +LR: route Fox and route W (wang_lib) agree, I(W1) = -1 and I(W2) = +1; every identity holds
    (B1297, r1 + q1 = t0 + s0, Lemma E).
C5  the type-one solver (scan_lib, then family_lib's 40-digit polish) at Ballas' axis reproduces Ballas' family: the traces of
    eleven words agree with rho_q transported, q read off the fibre boundary.
C6  (disclosed; it bears on Proposition Pi) at that point: the Jacobian nullity of the type-one system and of the b-free system,
    and the slice's centraliser (the gauge)."""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

import cusp_lib as L  # noqa: E402
import family_lib as FL  # noqa: E402
import scan_lib as S  # noqa: E402
import wang_lib as WL  # noqa: E402

mp.mp.dps = 60
OUT = {}
FAILED = []


def check(name, ok, detail):
    OUT[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        FAILED.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + json.dumps(detail, default=str)[:400], flush=True)


def ballas_twisted(q, mu):
    B = L.ballas(q)
    return L.Module({g: mu * B.M[g] for g in ("m", "n")})


def w1_w2(G, A):
    z, nz = L.cocycle_generator(G, A)
    W1 = L.extension(A, z)
    As = A.dual()
    zs, _ = L.cocycle_generator(G, As)
    W1s = L.extension(As, zs)
    return W1, W1s, nz


def transport(mod):
    """a module of Ballas' presentation as a module of route F's +LR presentation"""
    m, n = mod.M["m"], mod.M["n"]
    mi, ni = mp.inverse(m), mp.inverse(n)
    return L.Module({"a": n * mi, "b": m * ni * m * n * mi * mi, "t": m})


# ---------------------------------------------------------------------------------------------------------- C1
check("C1 slice closed form", S.selftest() < 1e-13, {"relative error": S.selftest()})

# ---------------------------------------------------------------------------------------------------------- C2
t0 = time.time()
rows = []
for label, q, mu, want in (("17+12sqrt2", 17 + 12 * mp.sqrt(2), -1, (-1, 1)), ("17-12sqrt2", 17 - 12 * mp.sqrt(2), -1, (-1, 1)),
                           ("7+4sqrt3", 7 + 4 * mp.sqrt(3), 1j, (0, 0))):
    A = ballas_twisted(q, mu)
    hA = L.class_index(L.BALLAS, A)
    W1, W1s, nz = w1_w2(L.BALLAS, A)
    r1 = L.class_index(L.BALLAS, W1)
    r1s = L.class_index(L.BALLAS, W1s)
    rows.append({"q": label, "mu": str(mu), "h1(A)": hA["V"]["h1"], "I(W1)": r1["I"], "I(W2) = -I(W1[A*])": -r1s["I"],
                 "W1 (a0,h1,t0,r1)": [r1["V"][k] for k in ("a0", "h1", "t0", "r1")], "checks": [all(r1["checks"].values()),
                 all(r1s["checks"].values())], "margins": r1["margins"]})
ok = all(r["I(W1)"] == w[0] and r["I(W2) = -I(W1[A*])"] == w[1] and all(r["checks"]) for r, w in
         zip(rows, ((-1, 1), (-1, 1), (0, 0))))
ok = ok and rows[0]["W1 (a0,h1,t0,r1)"] == [0, 1, 1, 1] and rows[2]["W1 (a0,h1,t0,r1)"] == [0, 0, 1, 0]
check("C2 sm:B1509 extension indices, route Fox, Ballas' presentation", ok, {"rows": rows, "seconds": round(time.time() - t0)})

# ---------------------------------------------------------------------------------------------------------- C3
G, img = FL.word_group("+", "LR")
qg = mp.mpf("2.37")
T3 = transport(L.ballas(qg))
res = L.relator_residual(G, T3)
Lw = T3.word("abAB")
# power sums tr(L^k), k = 1..4, against those of (q, q, q, q^-3): well conditioned, unlike the eigenvalues of a Jordan block
ps, Lk = [], mp.eye(4)
for k in range(1, 5):
    Lk = Lk * Lw
    ps.append(sum(Lk[i, i] for i in range(4)))
evd = max(abs(ps[k - 1] - (3 * qg ** k + qg ** (-3 * k))) for k in range(1, 5))
evd_inv = max(abs(ps[k - 1] - (3 * qg ** -k + qg ** (3 * k))) for k in range(1, 5))
check("C3 Ballas -> +LR isomorphism", res < mp.mpf(10) ** -50 and evd < mp.mpf(10) ** -45,
      {"relator residual": mp.nstr(res, 3), "tr(abAB^k) vs 3q^k + q^-3k, k <= 4": mp.nstr(evd, 3),
       "vs the inverse": mp.nstr(evd_inv, 3)})

# ---------------------------------------------------------------------------------------------------------- C4
t0 = time.time()
q = 17 + 12 * mp.sqrt(2)
A = ballas_twisted(q, -1)
W1, W1s, _ = w1_w2(L.BALLAS, A)
out4 = {}
for name, mod, want in (("W1", W1, -1), ("W1[A*]", W1s, 1)):
    TM = transport(mod)
    fox = L.class_index(G, TM)
    wang = WL.index_wang(img, G.cusp, {g: TM.M[g] for g in "abt"})
    out4[name] = {"Fox": fox["I"], "W": wang["I"], "Fox checks": fox["checks"], "W data": {k: wang[k] for k in
                  ("h1(V)", "h1(V*)", "a0", "b0", "t0", "s0")}, "relator residual": fox["relator residual"]}
ok = (out4["W1"]["Fox"] == out4["W1"]["W"] == -1 and -out4["W1[A*]"]["Fox"] == -out4["W1[A*]"]["W"] == 1
      and all(out4["W1"]["Fox checks"].values()) and all(out4["W1[A*]"]["Fox checks"].values()))
check("C4 W1, W2 on +LR, routes Fox and W", ok, {"rows": out4, "seconds": round(time.time() - t0)})

# ---------------------------------------------------------------------------------------------------------- C5, C6
t0 = time.time()
cache = {}
_, _, W, u0, orient = S.hyperbolic_seed("+", "LR", 0.0, cache)
th = -np.angle(S.frame_reading(u0, False)["zl"])
G, img, W, u0, orient = S.hyperbolic_seed("+", "LR", th, cache)
a_val = 0.01
u, f, it = S.solve(u0, a_val, W, False)
mp.mp.dps = 40
U = mp.matrix([mp.mpf(float(x)) for x in u])
Up, fp, itp, _ = FL.solve_type_one(U, mp.mpf(a_val), G, img)
mats, XY = FL.unpack(Up)
mod = L.Module(mats)
evl = FL.eig_sorted(mod.word("abAB"))
qread = [e for e in evl if abs(mp.im(e)) < mp.mpf(10) ** -20]
# q: the eigenvalue of multiplicity three
qq = min(qread, key=lambda e: sum(abs(e - x) for x in qread))
qq = mp.re(qq)
ref = transport(L.ballas(qq))
words = ["a", "b", "ab", "aB", "ta", "tb", "tab", "taB", "aab", "abb", "tAb"]
tr_err = max(abs(mp.re(sum(mod.word(w)[i, i] for i in range(4))) - mp.re(sum(ref.word(w)[i, i] for i in range(4))))
             for w in words)
tr_err_inv = max(abs(mp.re(sum(mod.word(w)[i, i] for i in range(4))) - mp.re(sum(transport(L.ballas(1 / qq)).word(w)[i, i]
                 for i in range(4)))) for w in words)
check("C5 the type-one solver reproduces Ballas' family", min(tr_err, tr_err_inv) < mp.mpf(10) ** -30 and fp < mp.mpf(10) ** -28,
      {"a": a_val, "float64 |F|": f, "polished |F|": mp.nstr(fp, 3), "q read": mp.nstr(qq, 15),
       "trace error (q)": mp.nstr(tr_err, 3), "trace error (1/q)": mp.nstr(tr_err_inv, 3), "X_t (section unipotent)":
       mp.nstr(XY[2], 3), "seconds": round(time.time() - t0)})
mp.mp.dps = 60

J1 = S.jacobian(u, a_val, W, False)
s1 = np.linalg.svd(J1, compute_uv=False)
ub, fb, _ = S.solve(np.concatenate([u0, [0.0]]), a_val, W, True)
J2 = S.jacobian(ub, a_val, W, True)
s2 = np.linalg.svd(J2, compute_uv=False)


def nullity(s):
    return int(np.sum(s < 1e-8 * s[0])), float(s[s < 1e-8 * s[0]].max()) if np.any(s < 1e-8 * s[0]) else None, \
        float(s[s >= 1e-8 * s[0]].min())


def centraliser_dim(a, b):
    Nx = np.zeros((4, 4)); Nx[0, 1] = 1; Nx[1, 1] = a; Nx[1, 3] = 1  # noqa: E702
    Ny = np.zeros((4, 4)); Ny[0, 2] = 1; Ny[2, 2] = b; Ny[2, 3] = 1  # noqa: E702
    cols = []
    for i in range(4):
        for j in range(4):
            E = np.zeros((4, 4)); E[i, j] = 1  # noqa: E702
            cols.append(np.concatenate([(E @ Nx - Nx @ E).ravel(), (E @ Ny - Ny @ E).ravel(), [np.trace(E)]]))
    M = np.array(cols).T
    s = np.linalg.svd(M, compute_uv=False)
    return 16 - int(np.sum(s > 1e-10 * s[0]))


rb = S.frame_reading(ub, True)
check("C6 (disclosed) nullities at Ballas' axis", True,
      {"type-one: (nullity, largest null sv, smallest kept sv)": nullity(s1),
       "b-free: (nullity, largest null sv, smallest kept sv)": nullity(s2),
       "centraliser of the slice group (gauge)": [centraliser_dim(0.3, 0.0), centraliser_dim(0.3, 0.2)],
       "b-free landing point: b, frame offset (rad), b/(a * offset)": [rb["b"], float(np.angle(rb["zl"])),
                                                                       rb["b"] / (a_val * float(np.angle(rb["zl"])))]})

OUT["all controls pass"] = not FAILED
OUT["failed"] = FAILED
(HERE / "controls.json").write_text(json.dumps(OUT, indent=1, default=str))
print("ALL PASS" if not FAILED else "FAILED: " + ", ".join(FAILED))
