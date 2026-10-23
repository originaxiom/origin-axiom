#!/usr/bin/env python3
"""FRAME LOCK (data-free; step 1 of THE_NEXT_ATTACK: the canonical frame banked with locks).  Each lock re-derives one
statement of THE_NEXT_ATTACK.md §1 and fails loudly (exit status 1) if it no longer holds.  Nothing here reads a target.
Exact statements are checked symbolically (sympy); statements about the stored channels are checked on the channel
store of TWO_HIGGS's grid (the ten (2/5, k/10) lines, 1 280 points, both horocycles: 2 560 rows), which is their scope.
  K1  §1.1  F^dagger Y F in the frame (f1 = n-bar, f2 = e1, f3 = n) equals the canonical matrix, symbolically.
  K2  §1.2  det Y = (h.h)(u.h)(u.u + w^2) for every u, h, w, symbolically (B1659's J1 in vector form).
  K3  §1.4  |V_cb| = |kappa_u - kappa_d| under the null Higgs n (one reading) on the 2 560 stored rows: median relative
            error below 1%, largest below 3%.
  K4  §1.4  the up channel on the store: w = 0 exactly on the order-5 lines, a2 = 0 exactly on the order-10 lines
            (relative 1e-12); its triplet nearly n (|u.u|/|u|^2 below 0.2 on every row).
  K5  §1.6  the idealised up channel u = a3 n, w = 0: the frame matrix is a3 [[0,0,0],[c2,-c1,0],[2c3,c2,0]] and
            ||Y||_F^2 = |a3|^2 (4|c3|^2 + 2|c2|^2 + |c1|^2), symbolically; hence m1 = 0, the light left state is n-bar,
            m2 m3 = |a3|^2 |h.h| and m2/m3 >= |h.h|/4 (checked on 20 000 random unit h).
  K6  §1.7  on the store: the leptons' channel weights equal the down quarks' up to one complex factor of modulus one,
            with w -> -w on order-5 lines and u_i -> -u_i on order-10 lines (relative 1e-12); consequence for the
            record's directions (DR, F_6, F_22, F_-2, as stored and conjugated): equal singular-value ratios (order 5)
            and equal at h -> diag(-1, 1, 1) h (order 10), relative 1e-9.
  K7  §1.5  the record's forms at the cusp (Re tau 0.3, Im tau 3.5 and 4): R = F_2: delta/r^(1/2) = 2 sqrt 2,
            eps/r = 4; DR: 4 sqrt 2 and 20; F_6: eps/r = 12, r = exp(-pi Im tau) (relative 1e-3).
    python3 -B frame_lock.py      # writes frame_lock.json; exit status 0 only if every lock holds"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
OUT, FAIL = {}, []


def lock(name, ok, detail):
    OUT[name] = {"holds": bool(ok), "detail": detail}
    if not ok:
        FAIL.append(name)


# symbolic frame
I_ = sp.I
f1s = sp.Matrix([0, 1, -I_]) / sp.sqrt(2); f2s = sp.Matrix([1, 0, 0]); f3s = sp.Matrix([0, 1, I_]) / sp.sqrt(2)
Fs = sp.Matrix.hstack(f1s, f2s, f3s)


def Ysym(u, h, w):
    cr = sp.Matrix([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])
    return u * h.T + h * u.T - (u.T * h)[0] * sp.eye(3) + w * cr


# K1
a1, a2, a3, w, de, ep = sp.symbols("a1 a2 a3 w delta epsilon")
u = a3 * f3s + a2 * f2s + a1 * f1s; h = f3s + de * f2s + ep * f1s
M = sp.Matrix([[de * (I_ * w - a2), de * a1 + ep * (a2 - I_ * w), 2 * ep * a1],
               [a2 - I_ * w + de * a3, de * a2 - ep * a3 - a1, de * a1 + ep * (a2 + I_ * w)],
               [2 * a3, a2 + I_ * w + de * a3, -de * (a2 + I_ * w)]])
D1 = sp.simplify(sp.expand(Fs.H * Ysym(u, h, w) * Fs - M))
lock("K1 canonical matrix (symbolic)", D1 == sp.zeros(3, 3), "F^dagger Y F - M simplifies to zero" if D1 == sp.zeros(3, 3) else str(D1))

# K2
U1, U2, U3, H1, H2, H3 = sp.symbols("u1 u2 u3 h1 h2 h3")
ug, hg = sp.Matrix([U1, U2, U3]), sp.Matrix([H1, H2, H3])
dd = sp.expand(Ysym(ug, hg, w).det() - (hg.T * hg)[0] * (ug.T * hg)[0] * ((ug.T * ug)[0] + w ** 2))
lock("K2 det Y = (h.h)(u.h)(u.u + w^2) (symbolic)", dd == 0, "difference expands to zero" if dd == 0 else str(dd))

# K5 (symbolic part)
c1, c2, c3 = sp.symbols("c1 c2 c3")
hc = c3 * f3s + c2 * f2s + c1 * f1s
D5 = sp.simplify(sp.expand(Fs.H * Ysym(a3 * f3s, hc, 0) * Fs - a3 * sp.Matrix([[0, 0, 0], [c2, -c1, 0], [2 * c3, c2, 0]])))
hh = sp.expand((hc.T * hc)[0])
k5_sym = D5 == sp.zeros(3, 3) and sp.simplify(hh - (2 * c1 * c3 + c2 ** 2)) == 0

# numeric
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)


def cross(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def closed(u4, v):
    ww, uu = u4[0], u4[1:]
    return np.outer(uu, v) + np.outer(v, uu) - (uu @ v) * np.eye(3) + ww * cross(v)


rng = np.random.default_rng(20261023)
worst_ratio, worst_prod, worst_light = 9.0, 0.0, 0.0
for _ in range(20000):
    v = rng.normal(size=3) + 1j * rng.normal(size=3); v /= np.linalg.norm(v)
    A3 = complex(rng.normal(), rng.normal())
    Uy, s, _ = np.linalg.svd(closed(np.concatenate([[0], A3 * F3]), v))
    worst_prod = max(worst_prod, abs(s[0] * s[1] - abs(A3) ** 2 * abs(v @ v)) / abs(A3) ** 2)
    worst_ratio = min(worst_ratio, (s[1] / s[0]) / (abs(v @ v) / 4))
    worst_light = max(worst_light, 1 - abs(np.vdot(F1, Uy[:, 2])))
lock("K5 idealised up channel lemma", k5_sym and worst_prod < 1e-12 and worst_ratio >= 1 - 1e-9 and worst_light < 1e-6,
     {"symbolic frame matrix and h.h = 2 c1 c3 + c2^2": bool(k5_sym), "max |m2 m3 - |a3|^2 |h.h|| / |a3|^2": worst_prod,
      "min (m2/m3) / (|h.h|/4)": worst_ratio, "max 1 - |<n-bar, light left state>|": worst_light})

# the store
st = np.load(HERE / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
DIRS, tasks = I["dirs"], I["tasks"]
errs = []; w5, a10, uu_max = 0.0, 0.0, 0.0
for p, (k, re_t, im_t) in enumerate(tasks):
    for ih in range(2):
        kap = {}
        for i_s, sec in enumerate(("up", "down")):
            ww, uu = U[p, i_s, ih, 0], U[p, i_s, ih, 1:]
            b1, b2, b3 = np.vdot(F1, uu), np.vdot(F2, uu), np.vdot(F3, uu)
            r2 = np.array([b2 - 1j * ww, -b1]); r3 = np.array([2 * b3, b2 + 1j * ww])
            kap[sec] = np.vdot(r3, r2) / np.vdot(r3, r3)
            if sec == "up":
                nu = np.linalg.norm(uu); uu_max = max(uu_max, abs(uu @ uu) / nu ** 2)
                if k % 2 == 0:
                    w5 = max(w5, abs(ww) / nu)
                else:
                    a10 = max(a10, abs(b2) / nu)
        Uu = np.linalg.svd(closed(U[p, 0, ih], F3))[0]; Ud = np.linalg.svd(closed(U[p, 1, ih], F3))[0]
        V = np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1]
        errs.append(abs(abs(V[1, 2]) - abs(kap["up"] - kap["down"])) / abs(V[1, 2]))
lock("K3 |V_cb| = |kappa_u - kappa_d| under n (2 560 stored rows)", np.median(errs) < 0.01 and max(errs) < 0.03,
     {"median relative error": float(np.median(errs)), "largest": float(max(errs))})
lock("K4 the stored up channel: w = 0 on order 5, a2 = 0 on order 10, triplet nearly n", w5 < 1e-12 and a10 < 1e-12 and uu_max < 0.2,
     {"max |w|/|u| on order-5 lines": w5, "max |a2|/|u| on order-10 lines": a10, "max |u.u|/|u|^2": uu_max})

P = np.diag([-1.0, 1.0, 1.0]).astype(complex)
pat = {0: np.array([-1, 1, 1, 1]), 1: np.array([1, -1, 1, 1])}
dev, cmod, sv = 0.0, 0.0, 0.0
for p, (k, re_t, im_t) in enumerate(tasks):
    for ih in range(2):
        dn, lp = U[p, 1, ih], U[p, 2, ih]
        x = pat[k % 2] * dn; c = np.vdot(x, lp) / np.vdot(x, x)
        dev = max(dev, float(np.max(np.abs(lp - c * x)) / np.max(np.abs(lp)))); cmod = max(cmod, abs(abs(c) - 1))
        for d in ("dR", "F_6", "F_22", "F_-2"):
            for v in (H[p, DIRS.index(d)], np.conj(H[p, DIRS.index(d)])):
                se = np.linalg.svd(closed(lp, v), compute_uv=False); se = se[1:] / se[0]
                sd = np.linalg.svd(closed(dn, v if k % 2 == 0 else P @ v), compute_uv=False); sd = sd[1:] / sd[0]
                sv = max(sv, float(np.max(np.abs(se / sd - 1))))
lock("K6 leptons as the down quarks (w -> -w on order 5, u_i -> -u_i on order 10)", dev < 1e-12 and cmod < 1e-12 and sv < 1e-9,
     {"max relative deviation of the channel weights": dev, "max ||c| - 1|": cmod, "max relative difference of singular-value ratios": sv})

# K7
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", HERE.parent / "chat1_2026-10-23_zero_free_frame" / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
sys.argv = _argv


def dep(v):
    c = np.array([np.vdot(F2, v), np.vdot(F3, v), np.vdot(F1, v)])
    lead = 1 if abs(c[1]) >= abs(c[2]) else 2
    return abs(c[0] / c[lead]), abs(c[3 - lead] / c[lead])


want = {"F_2": (2 * math.sqrt(2), 4.0), "dR": (4 * math.sqrt(2), 20.0), "F_6": (None, 12.0)}
k7, ok7 = {}, True
for d, (dw, ew) in want.items():
    for y in (3.5, 4.0):
        r = math.exp(-math.pi * y); dv, ev = dep(zfc.direction(d, 0.3, y))
        row = {"delta/r^(1/2)": dv / math.sqrt(r), "eps/r": ev / r}
        ok7 &= abs(ev / r / ew - 1) < 1e-3 and (dw is None or abs(dv / math.sqrt(r) / dw - 1) < 1e-3)
        k7[f"{d} at 0.3 + {y}i"] = row
lock("K7 cusp coefficients of R = F_2, DR, F_6", ok7, k7)

OUT["failed"] = FAIL
(HERE / "frame_lock.json").write_text(json.dumps(OUT, indent=1, default=float) + "\n")
print("all locks hold" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
