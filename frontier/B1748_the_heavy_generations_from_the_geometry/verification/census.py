"""B1748 census: the heavy generations from the geometry alone (P-362).  At the apex points of FRESH thread classes
(B1720's rule: Im tau = Lagrange/2; words of length 10 and 11 with apex height in [2.0, 3.6], none among B1720's 121
classes of length 2-9 that B1741 used; distinct (Re tau mod 1, Im tau)), on every one of B1713's 266 lines, with the Higgs
EXACTLY NULL -- h = n = (0, 1, i)/sqrt2 (rho(T)'s null eigenline, the cusp limit of every null-led form) or its conjugate
n-bar (the other reading) -- in every sector, on both horocycles (B1667's L_max and L_2), B1656's frame (B1740's instrument,
B1742's channel code): per row the heavy observables m_c/m_t, m_s/m_b, m_mu/m_tau (before the lepton factor) and |V_cb|.
The first generation is massless with a null Higgs (det Y = 0, B1744) and is not read.
    python3 -B census.py [--workers 8]      # writes census.jsonl, control.json, census_run.txt (via stdout)
Importing computes nothing."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
N0 = (0.0, 1 / math.sqrt(2), 1j / math.sqrt(2))
HEIGHT = (2.0, 3.6)


def _imports():
    import numpy as np
    sys.path.insert(0, str(ROOT / "frontier" / "B1742_two_higgs_verified_on_main" / "verification"))
    sys.path.insert(0, str(ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification"))
    import repro as R
    import thread_geometry as TG
    return np, R, TG


def apex_points():
    """the fresh apex points: words of length 10 and 11 (B1720's necklaces), apex height in HEIGHT, each with its representative
    A and apex tau; distinct (Re tau mod 1, Im tau) to 9 digits; B1720's own classes (lengths 2-9) excluded by length"""
    np, R, TG = _imports(); pts = {}
    for k in (10, 11):
        for w in TG.necklaces(k, k):
            h = TG.lagrange(w) / 2
            if not (HEIGHT[0] <= h <= HEIGHT[1]): continue
            r, A = TG.representative(w, h); assert abs(r - h) < 1e-9, (w, r, h)
            a, b, c, d = A; xc = (a - d) / (2 * c); key = (round(xc % 1, 9), round(h, 9))
            pts.setdefault(key, {"words": [], "Re_tau": round(xc % 1, 9), "Im_tau": h})["words"].append(w)
    return sorted(pts.values(), key=lambda p: (p["Im_tau"], p["Re_tau"]))


def heavy(re_t, im_t, a, b):
    np, R, TG = _imports(); B, col = R.CEN._modules()["B"], R.CEN._modules()["col"]; t = complex(re_t, im_t); w = float(a) * t + float(b)
    pre = {}
    for sec, (lf, rf) in R.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, t); pre[sec] = (Rr, B.cA(x, yy, t, Rr))
    out = {}
    for hor, ix in (("L_max", 1), ("L_2", 2)):
        L = float(np.interp(im_t, [q[0] for q in col], [q[ix] for q in col]))
        M = {}
        for sec, (Rr, c) in pre.items():
            u = {s: (math.sqrt(2 * math.pi * L + c[s]) * Rr[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
            M[sec] = B.weighted_M(u)
        for rd, h in (("n", N0), ("nbar", tuple(complex(z).conjugate() for z in N0))):
            S = R.Smat(list(h), B); Y = {sec: B.coupling(S, M[sec]) for sec in M}
            sv = {sec: np.linalg.svd(Y[sec], compute_uv=False) for sec in Y}
            Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
            out[f"{hor}|{rd}"] = [float(sv["up"][1] / sv["up"][0]), float(sv["down"][1] / sv["down"][0]), float(sv["lep"][1] / sv["lep"][0]), float(abs(V[1, 2]))]
    return out


def task(t):
    k, re_t, im_t = t; np, R, TG = _imports(); a, b = R.CEN.lines()[k]
    return {"line": k, "Re_tau": re_t, "Im_tau": im_t, **heavy(re_t, im_t, a, b)}


def control():
    """C1: B1741's apex 3.4 + 2.993i on (2/5, 9/10), L_max, n: the values main read post hoc (V_cb 0.0384, m_s/m_b 0.0206,
    m_c/m_t 0.00350, the leptons' m2/m3 x 3 = 0.0617) reproduced; C2: B1724's T-law, (tau, (alpha, b)) ~ (tau + 1, (alpha, b - alpha))"""
    np, R, TG = _imports()
    h1 = heavy(3.4, 2.993325909, Fr(2, 5), Fr(9, 10))["L_max|n"]
    ref = [0.00350, 0.0206, 0.0617 / 3, 0.0384]
    c1 = max(abs(x / y - 1) for x, y in zip(h1, ref))
    p = apex_points()[len(apex_points()) // 2]; a, b = Fr(2, 5), Fr(3, 10)
    x1 = heavy(p["Re_tau"], p["Im_tau"], a, b); x2 = heavy(p["Re_tau"] + 1, p["Im_tau"], a, (b - a) % 1)
    c2 = max(abs(math.log(u / v)) for k in x1 for u, v in zip(x1[k], x2[k]))
    return {"C1_B1741_apex_reproduced_rel": c1, "C1_values": h1, "C2_T_covariance": c2, "apex_points": len(apex_points())}


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    np, R, TG = _imports(); pts = apex_points(); nl = len(R.CEN.lines())
    out = HERE / "census.jsonl"; done = set()
    if out.exists():
        for l in out.read_text(encoding="utf-8").splitlines():
            r = json.loads(l); done.add((r["line"], r["Re_tau"], r["Im_tau"]))
    tasks = [(k, p["Re_tau"], p["Im_tau"]) for p in pts for k in range(nl) if (k, p["Re_tau"], p["Im_tau"]) not in done]
    print("%d apex points x %d lines = %d points; %d done; %d to do" % (len(pts), nl, len(pts) * nl, len(done), len(tasks)), flush=True)
    with open(out, "a", encoding="utf-8") as fh, Pool(nw) as P:
        for i, r in enumerate(P.imap_unordered(task, tasks, chunksize=8)):
            fh.write(json.dumps(r) + "\n")
            if i % 5000 == 0: fh.flush(); print("row", i, flush=True)
    c = control(); (HERE / "control.json").write_text(json.dumps(c, indent=1) + "\n")
    print("control:", c, flush=True); print("census exit 0")
