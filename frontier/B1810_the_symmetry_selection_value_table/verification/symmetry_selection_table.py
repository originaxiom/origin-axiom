"""P-432 -- THE SYMMETRY-SELECTION VALUE TABLE (data-free; exploratory until landed; no data read).  Every configuration of
B1656's flat fibre frame fixed by the object's symmetry (B1809 § 2: (i, 0), (omega, 0), (i, (1/2, 1/2)), (omega, (1/3, 2/3))
up to the group, lines up to sign; omega taken as e^{i pi/3}, B1667's point), the record's parameter-free Higgs directions
(DR, a0, R, t = -5/288, B1730's F_6, F_10, F_14, F_22), B1667's two canonical radii at the point, and the eight readings
(each sector S or S~ = eps S* eps^T; B1790).  Per row: (m1/m3, m2/m3) in the up (1, -4), down (1, 2) and lepton (-3, 6)
sectors, and the CKM moduli |V_us|, |V_cb|, |V_ub| and J from the up and down left singular vectors (light to heavy).
The record's machinery read-only: B1656's four-channel coupling (b1656_funcs, as B1691's S164 correction uses it),
B1691's q-series sections, B1667's radii.
    python3 symmetry_selection_table.py      # writes symmetry_selection_table.json beside itself"""
import contextlib, glob, importlib.util, io, itertools, json, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir())
V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1691_*" / "verification"))[0]); C = V / "correction"
sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import b1656_funcs as B

mp.mp.dps = 30
b1667 = json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())
pts = b1667["points"]; pts = pts if isinstance(pts, list) else list(pts.values())


def canon(tau):
    for p in pts:
        if isinstance(p, dict) and "tau" in p and abs(complex(*p["tau"]) - tau) < 1e-9: return p["L_max"], p["L_2"]
    raise KeyError(tau)


I = 1j; W = complex(0.5, math.sqrt(3) / 2)
CONFIGS = [("(i, 0)", I, (0, 0)), ("(omega, 0)", W, (0, 0)), ("(i, (1/2, 1/2))", I, (0.5, 0.5)), ("(omega, (1/3, 2/3))", W, (1 / 3, 2 / 3))]
SECTORS = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]
S_ = te.S
QSECS = {"DR": te.B[1], "a0": [te.B[2][j] + S_.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)], "R": te.B[0],
         "t=-5/288": [te.B[2][j] + S_.c(F(-5, 288)) * te.e4 * te.B[0][j] for j in range(3)]}


def direction(name, tau):
    if name in QSECS: return [complex(te.ev(c, mp.mpc(tau.real, tau.imag))) for c in QSECS[name]]
    a_ = int(name[2:]); q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag)); eps = 1j ** ((a_ + 2) // 2)
    th2, th3, th4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return [complex(eps * th2 ** a_), complex(eps * th4 ** a_), complex(1j * th3 ** a_)]


DIRS = ["DR", "a0", "R", "t=-5/288"] + ["F_%d" % a_ for a_ in (-10, -6, -2, 6, 10, 14, 18, 22, 26)]   # B1730's n = 1 zero-free members (F_2 is R)
cache = {}


def chan(tau, line, ql, qr):
    key = (tau, line, ql, qr)
    if key not in cache:
        w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R); cache[key] = (R, c)
    return cache[key]


def coupling(a, tau, line, ql, qr, L, tilde):
    R, c = chan(tau, line, ql, qr)
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if tilde: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(Sm, B.weighted_M(u))


def fmt(z): return float("%.6g" % z)


rows = []
for cname, tau, line in CONFIGS:
    Lmax, L2 = canon(tau)
    for d in DIRS:
        a = direction(d, tau)
        for Ln, L in (("L_max", Lmax), ("L_2", L2)):
            for rd in itertools.product((0, 1), repeat=3):          # 0 = S, 1 = S~ ; (up, down, lepton)
                row = {"config": cname, "direction": d, "radius": Ln, "L": L, "reading": "".join("S~" if r else "S " for r in rd).replace(" ", "")}
                U = {}
                for (sn, ql, qr), r in zip(SECTORS, rd):
                    Y = coupling(a, tau, line, ql, qr, L, r)
                    u_, s, _ = np.linalg.svd(Y); order = np.argsort(s)    # light to heavy
                    s = s[order]; U[sn] = u_[:, order]
                    row[sn] = [fmt(s[0] / s[2]), fmt(s[1] / s[2])]
                    gaps = [(s[1] - s[0]) / s[2], (s[2] - s[1]) / s[2]]
                    if min(gaps) < 1e-8: row.setdefault("degenerate sectors (V undefined)", []).append(sn)
                Vm = U["up"].conj().T @ U["down"]
                row["V defined"] = not any(sn in row.get("degenerate sectors (V undefined)", []) for sn in ("up", "down"))
                row["|V_us|, |V_cb|, |V_ub|"] = [fmt(abs(Vm[0, 1])), fmt(abs(Vm[1, 2])), fmt(abs(Vm[0, 2]))]
                row["|V| (3x3)"] = [[fmt(abs(Vm[i_, j_])) for j_ in range(3)] for i_ in range(3)]
                row["J"] = fmt(float(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1]))))
                rows.append(row)
    print(cname, "done", flush=True)
# ---- summaries, computed here (the referee's C6) -------------------------------------------------------------------
def z(v): return 0.0 if abs(v) < 1e-9 else float("%.5g" % v)
def key(x, with_v):
    k = tuple(z(v) for sn in ("up", "down", "lepton") for v in x[sn])
    return k + (tuple(z(v) for r_ in x["|V| (3x3)"] for v in r_) if with_v and x["V defined"] else ())
summary = {"rows": len(rows), "directions": DIRS}
for c in [c[0] for c in CONFIGS] + ["all"]:
    sel = [x for x in rows if c == "all" or x["config"] == c]
    summary["distinct outputs " + c] = {"masses": len({key(x, False) for x in sel}), "masses + V": len({key(x, True) for x in sel})}
vd = [x for x in rows if x["V defined"]]
isperm = lambda M: all(min(abs(v), abs(1 - v)) < 1e-6 for r_ in M for v in r_)
exc = [x for x in vd if not isperm(x["|V| (3x3)"])]
summary["V defined"] = len(vd); summary["V a permutation (full 3x3, 1e-6)"] = len(vd) - len(exc)
summary["max |J| where V is defined"] = max(abs(x["J"]) for x in vd) if vd else None
summary["exceptions"] = [{k: x[k] for k in ("config", "direction", "radius", "reading", "up", "|V| (3x3)")} for x in exc]
summary["distinct exception |V| matrices"] = len({tuple(z(v) for r_ in x["|V| (3x3)"] for v in r_) for x in exc})
# the controls (B1809's Table T; the first referee's r3)
def g(c, d, r, rd="SSS"): return [x for x in rows if x["config"] == c and x["direction"] == d and x["radius"] == r and x["reading"] == rd][0]
assert g("(i, 0)", "DR", "L_2")["up"][1] == 1.0
assert g("(i, 0)", "a0", "L_2")["up"] == [0.075318, 0.658298]
assert g("(i, 0)", "R", "L_2")["up"][1] == 0.0190689
assert g("(i, (1/2, 1/2))", "DR", "L_2")["up"] == [0.0381377, 0.519069]
summary["controls"] = "hold"
# the exception angle's scope in L (a0's class at (i, (1/2, 1/2)), the record's reading)
ang = {}
a = direction("a0", I)
for L in (canon(I)[1], 40.0, 2560.0):
    Us = []
    for (sn, ql, qr), r in zip(SECTORS[:2], (1, 0)):
        u_, s_, _ = np.linalg.svd(coupling(a, I, (0.5, 0.5), ql, qr, L, r)); Us.append(u_[:, np.argsort(s_)])
    Vm = Us[0].conj().T @ Us[1]; ang["L = %g" % L] = sorted(fmt(abs(v)) for v in Vm.flatten() if 1e-9 < abs(v) < 1 - 1e-9)
summary["a0 at (i, (1/2, 1/2)), S~SS: the non-0/1 |V| entries by L"] = ang
(HERE / "symmetry_selection_table.json").write_text(json.dumps({"summary": summary, "rows": rows, "radii": {c[0]: canon(c[1]) for c in CONFIGS}}, indent=1), encoding="utf-8")
print(json.dumps({k: v for k, v in summary.items() if k != "exceptions"}, indent=1))
