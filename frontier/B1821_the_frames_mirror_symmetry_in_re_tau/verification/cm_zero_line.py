"""P-449, the rigid arm (data-free; audit room, 2026-10-29): FR-FIB at every CM point of cm_table.py's list (the forced fields
Q(sqrt-3), Q(sqrt-15) and eight control fields; |D| <= 800; Im tau in [1.5, 6]) on the ZERO line (no Wilson line: the
parameter-free choice), for B1810's thirteen declared directions (DR, a0, R, t = -5/288 and B1730's zero-free F_a at n = 1),
B1667's two radii (interpolated along its Re tau = 1/4 column, as B1726 does), and the eight readings.  The machinery is
B1810's, rebuilt here from the same modules (B1691's q-series sections, b1656_funcs' four-channel coupling), and its
evaluator is checked against B1810's committed table at (i, 0) before any CM point is run.  Per row: (m1/m3, m2/m3) per
sector, |V_us|, |V_cb|, |V_ub|, J.  No measured number is read; nothing is compared."""
import contextlib, glob, importlib.util, io, itertools, json, math, os, pathlib, sys
from fractions import Fraction as F
from multiprocessing import Pool
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
OUT = HERE / "cm_zero_line.jsonl"
sys.path.insert(0, str(HERE))
import cm_table as CT

_M = {}
def mods():
    if not _M:
        V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1691_*" / "verification"))[0]); C = V / "correction"
        sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); argv = sys.argv; sys.argv = ["x"]
        spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
        import b1656_funcs as B
        sys.argv = argv
        mp.mp.dps = 30
        col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
        S_ = te.S
        Q = {"DR": te.B[1], "a0": [te.B[2][j] + S_.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)], "R": te.B[0],
             "t=-5/288": [te.B[2][j] + S_.c(F(-5, 288)) * te.e4 * te.B[0][j] for j in range(3)]}
        _M.update(te=te, B=B, col=col, Q=Q)
    return _M


DIRS = ["DR", "a0", "R", "t=-5/288"] + ["F_%d" % a for a in (-10, -6, -2, 6, 10, 14, 18, 22, 26)]
SECTORS = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]


def direction(name, tau):
    M = mods(); te = M["te"]
    if name in M["Q"]: return [complex(te.ev(c, mp.mpc(tau.real, tau.imag))) for c in M["Q"][name]]
    a_ = int(name[2:]); q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag)); eps = 1j ** ((a_ + 2) // 2)
    th2, th3, th4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return [complex(eps * th2 ** a_), complex(eps * th4 ** a_), complex(1j * th3 ** a_)]


def radii(tau):
    col = mods()["col"]
    return float(np.interp(tau.imag, [c[0] for c in col], [c[1] for c in col])), float(np.interp(tau.imag, [c[0] for c in col], [c[2] for c in col]))


def rows_at(tau, line, Ls=None):
    B = mods()["B"]
    ch = {}
    for sn, ql, qr in SECTORS:
        w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R); ch[sn] = (R, c)
    Lmax, L2 = Ls if Ls else radii(tau)
    out = []
    for d in DIRS:
        a = direction(d, tau)
        for Ln, L in (("L_max", Lmax), ("L_2", L2)):
            for rd in itertools.product((0, 1), repeat=3):
                row = {"direction": d, "radius": Ln, "reading": "".join("S~" if r else "S" for r in rd)}
                U = {}; deg = []
                for (sn, ql, qr), r in zip(SECTORS, rd):
                    R, c = ch[sn]
                    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
                    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
                    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
                    Y = B.coupling(Sm, B.weighted_M(u))
                    u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); s = s[o]; U[sn] = u_[:, o]
                    row[sn] = [float(s[0] / s[2]), float(s[1] / s[2])]
                    if min((s[1] - s[0]) / s[2], (s[2] - s[1]) / s[2]) < 1e-8: deg.append(sn)
                Vm = U["up"].conj().T @ U["down"]
                row["V defined"] = not any(x in deg for x in ("up", "down"))
                row["V"] = [float(abs(Vm[0, 1])), float(abs(Vm[1, 2])), float(abs(Vm[0, 2]))]
                row["J"] = float(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])))
                out.append(row)
    return out


def control():
    """B1810's committed table at (i, 0): every (direction, radius, reading) row must agree with this evaluator"""
    ref = json.loads(next(ROOT.glob("frontier/B1810_*/verification/symmetry_selection_table.json")).read_text())
    rr = [r for r in (ref["rows"] if isinstance(ref, dict) else ref) if r["config"] == "(i, 0)"]
    p = next(p for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(complex(*p["tau"]) - 1j) < 1e-9)
    mine = {(r["direction"], r["radius"], r["reading"]): r for r in rows_at(1j, (0, 0), (p["L_max"], p["L_2"]))}
    worst = 0.0
    for r in rr:
        m = mine[(r["direction"], r["radius"], r["reading"])]
        for sn in ("up", "down", "lepton"):
            for x, y in zip(r[sn], m[sn]): worst = max(worst, abs(x - y) / max(abs(x), 1e-6) if abs(x) > 1e-9 else abs(y))
    return len(rr), worst


def task(p):
    tau = complex(p["tau"][0], p["tau"][1])
    try:
        return dict(p, forced=p["field"] in CT.FORCED.values(), line="zero", rows=rows_at(tau, (0, 0)))
    except Exception as ex:
        return dict(p, line="zero", error=repr(ex)[:200])


if __name__ == "__main__":
    n, worst = control()
    print("control at (i, 0) against B1810's table:", n, "rows; worst relative difference", worst, flush=True)
    assert n == 208 and worst < 1e-4, (n, worst)
    P = CT.points(); done = set()
    if OUT.exists(): done = {tuple(json.loads(l)["form"]) for l in OUT.read_text().splitlines()}
    jobs = [p for p in P if tuple(p["form"]) not in done]
    print("points", len(P), "to run", len(jobs), flush=True)
    with Pool(int(os.environ.get("CM_WORKERS", "2"))) as Pl, open(OUT, "a") as fh:
        for k, row in enumerate(Pl.imap_unordered(task, jobs, chunksize=1)):
            fh.write(json.dumps(row) + "\n"); fh.flush()
            if k % 20 == 0: print(k, row.get("field"), row.get("form"), flush=True)
    print("done", flush=True)
