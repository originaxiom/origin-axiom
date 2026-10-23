#!/usr/bin/env python3
"""READING PRE-SCAN 2 (committed before its run; step 2a of THE_NEXT_ATTACK).  It reads no pinned value: it uses only
the Standard Model's coarse pattern (an up hierarchy, a down hierarchy, a CKM near the identity) as windows, at the
two pre-scan points 0.3 + 2.6i and 0.3 + 3.1i, which the reading test's grid will not contain.  On all 266 lines and
both horocycles (1 064 rows), with the Standard Model's reading (up sees conj h, down sees h):

  Lemma A (exact, every sector): B1736's Y satisfies Y h = Y^T h = (h.h) u, so for the left singular vectors l_k
  (singular values m_k) sum_k m_k^2 |<conj h, l_k>|^2 = |h.h|^2 |u|^2 (unit h), and the light left state lies within
  sin theta <= |h.h| |u| / m2 of conj h.  Under the Standard Model's reading the up light state is near h, the down
  light state near conj h, and |<h, conj h>| = |h.h|, so
      |V_ud| <= cos( arccos|h.h| - arcsin min(1, x_u) - arcsin min(1, x_d) )   (1 when the argument is negative),
  x_s = |h.h| |u_s| / m2_s.  Checked here on every sampled direction (A-check: the largest violation).

  Directions: the conic's tube coordinates h = h0(t) + s conj h0(t), h0(t) = (2t, 1 - t^2, i(1 + t^2)) (unit), with t
  on a 200-point Fibonacci lattice of the Riemann sphere, |s| = 10^(-4 + k/3) (k = 0..12), arg s in 8 steps; |h.h| =
  2|s| / (1 + |s|^2), so |s| = 1 is the real locus and the set covers CP^2; plus 2 000 random directions (seed 2026).
  Per row: the directions with an up hierarchy (up m2/m3 <= 1.5e-2 and m1/m3 <= 1e-4); among them the largest |V_ud|,
  and among those with |V_ud| > 0.9 the smallest |V_cb|; the count of directions in the coarse pattern P: up as above,
  down m2/m3 in [5e-3, 0.08] and m1/m3 <= 5e-3, |V_ud| > 0.9, |V_cb| < 0.2, |V_ub| < 0.05; the smallest |h.h| in P.
    python3 -B reading_prescan2.py [--workers 2]      # writes reading_prescan2.json and reading_prescan2_weights.npz"""
import contextlib, importlib.util, io, json, math, sys, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("cs", HERE / "channel_store.py"); cs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(cs)
sys.argv = _argv
LINES = [(tag, Fr(a), Fr(b)) for (tag, a, b) in cs.tic.LINES]
PTS = [(0.3, 2.6), (0.3, 3.1)]


def tube_dirs():
    n = 200; i = np.arange(n) + 0.5
    th = np.arccos(1 - 2 * i / n); ph = math.pi * (1 + 5 ** 0.5) * i
    cth, sth = np.cos(th / 2), np.sin(th / 2) * np.exp(1j * ph)          # t = sth / cth, homogeneous
    h0 = np.stack([2 * sth * cth, cth ** 2 - sth ** 2, 1j * (cth ** 2 + sth ** 2)], axis=1)
    h0 /= np.linalg.norm(h0, axis=1)[:, None]
    out = []
    for k in range(13):
        r = 10 ** (-4 + k / 3)
        for j in range(8):
            s = r * np.exp(2j * math.pi * j / 8)
            out.append(h0 + s * np.conj(h0))
    rng = np.random.default_rng(2026)
    z = rng.normal(size=(2000, 3)) + 1j * rng.normal(size=(2000, 3))
    H = np.concatenate(out + [z]); return H / np.linalg.norm(H, axis=1)[:, None]


HS = tube_dirs()


def Ybatch(u4, H):
    w, u = u4[0], u4[1:]
    uh = H @ u
    Y = u[None, :, None] * H[:, None, :] + H[:, :, None] * u[None, None, :] - uh[:, None, None] * np.eye(3)[None]
    cr = np.zeros((len(H), 3, 3), dtype=complex)
    cr[:, 0, 1], cr[:, 0, 2], cr[:, 1, 2] = -H[:, 2], H[:, 1], -H[:, 0]
    cr[:, 1, 0], cr[:, 2, 0], cr[:, 2, 1] = H[:, 2], -H[:, 1], H[:, 0]
    return Y + w * cr


def one(task):
    k, (re_t, im_t) = task
    tag, a, b = LINES[k]
    U = cs.weights(re_t, im_t, float(a), float(b))
    rows = []
    hh = np.abs(np.einsum("ni,ni->n", HS, HS))
    for ih, hor in enumerate(cs.HORS):
        up, dn = U[0, ih], U[1, ih]
        Uu, su, _ = np.linalg.svd(Ybatch(up, np.conj(HS))); Ud, sd, _ = np.linalg.svd(Ybatch(dn, HS))
        V = np.abs(np.einsum("nji,njk->nik", np.conj(Uu[:, :, ::-1]), Ud[:, :, ::-1]))
        # Lemma A check: light left state of each sector against conj(its Higgs), and the |V_ud| bound
        worst = 0.0; bound = np.ones(len(HS))
        ang = np.zeros(len(HS))
        for Ul, sv, hs, u4 in ((Uu, su, HS, up), (Ud, sd, np.conj(HS), dn)):      # up's Higgs conj h: conj of it is h
            ov = np.abs(np.einsum("ni,ni->n", np.conj(hs), Ul[:, :, 2]))           # <conj(Higgs), l1>, Higgs = conj hs
            sin_t = np.sqrt(np.clip(1 - ov ** 2, 0, 1))
            x = hh * np.linalg.norm(u4[1:]) / np.maximum(sv[:, 1], 1e-300)
            ok = sv[:, 1] > 1e-12 * sv[:, 0]
            worst = max(worst, float(np.max(np.where(ok, sin_t - x, -1.0))))
            ang += np.arcsin(np.minimum(1.0, x))
        arg = np.arccos(np.minimum(1.0, hh)) - ang
        bound = np.where(arg > 0, np.cos(np.clip(arg, 0, None)), 1.0)
        okb = (su[:, 1] > 1e-12 * su[:, 0]) & (sd[:, 1] > 1e-12 * sd[:, 0])
        bviol = float(np.max(np.where(okb, V[:, 0, 0] - bound, -1.0)))
        r2u, r1u, r2d, r1d = su[:, 1] / su[:, 0], su[:, 2] / su[:, 0], sd[:, 1] / sd[:, 0], sd[:, 2] / sd[:, 0]
        hier = (r2u <= 1.5e-2) & (r1u <= 1e-4)
        P = hier & (r2d >= 5e-3) & (r2d <= 0.08) & (r1d <= 5e-3) & (V[:, 0, 0] > 0.9) & (V[:, 1, 2] < 0.2) & (V[:, 0, 2] < 0.05)
        al = hier & (V[:, 0, 0] > 0.9)
        rows.append({"line": f"({a}, {b})", "order": tag, "tau": [re_t, im_t], "hor": hor,
                     "Lemma A: largest (sin theta - |h.h||u|/m2) over sectors and directions": worst,
                     "the |V_ud| bound: largest (|V_ud| - bound)": bviol,
                     "directions with an up hierarchy": int(hier.sum()),
                     "largest |V_ud| among them": float(V[hier, 0, 0].max()) if hier.any() else None,
                     "smallest |V_cb| among those with |V_ud| > 0.9": float(V[al, 1, 2].min()) if al.any() else None,
                     "directions in the coarse pattern P": int(P.sum()),
                     "smallest |h.h| in P": float(hh[P].min()) if P.any() else None})
    return rows, U


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    tasks = [(k, p) for k in range(len(LINES)) for p in PTS]
    rows, W = [], np.zeros((len(tasks), 3, 2, 4), dtype=complex)
    with Pool(nw) as Pl:
        for i, (rr, U) in enumerate(Pl.imap(one, tasks, chunksize=2)):
            rows.extend(rr); W[i] = U
    np.savez_compressed(HERE / "reading_prescan2_weights.npz", W=W, tasks=np.array([[k, p[0], p[1]] for k, p in tasks]))
    by = {}
    for r in rows:
        s = by.setdefault(r["order"], {"rows": 0, "rows with an up hierarchy": 0, "rows with |V_ud| > 0.9 under it": 0, "rows in P": 0, "lines in P": set()})
        s["rows"] += 1
        s["rows with an up hierarchy"] += r["directions with an up hierarchy"] > 0
        s["rows with |V_ud| > 0.9 under it"] += (r["largest |V_ud| among them"] or 0) > 0.9
        s["rows in P"] += r["directions in the coarse pattern P"] > 0
        if r["directions in the coarse pattern P"] > 0:
            s["lines in P"].add(r["line"])
    summ = {o: {**{kk: vv for kk, vv in s.items() if kk != "lines in P"}, "lines in P": sorted(s["lines in P"])} for o, s in sorted(by.items(), key=lambda kv: int(kv[0][2:]))}
    out = {"points": PTS, "directions per row": int(len(HS)),
           "Lemma A, worst over all rows": max(r["Lemma A: largest (sin theta - |h.h||u|/m2) over sectors and directions"] for r in rows),
           "the |V_ud| bound, worst over all rows": max(r["the |V_ud| bound: largest (|V_ud| - bound)"] for r in rows),
           "summary by order": summ, "rows": rows}
    (HERE / "reading_prescan2.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written")
