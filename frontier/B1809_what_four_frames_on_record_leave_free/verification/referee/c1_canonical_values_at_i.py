"""Referee of P-406's CENSUS_DRAFT (read-only; audit room; data-free).  c1: the census's (S1) and its F1 row at the
CANONICAL end radius.  Reuses the record's machinery read-only, exactly as B1691's S248 script does
(frontier/B1691_*/verification/correction_s248/near_points_finite_L_main.py): B1656's four-channel coupling via
b1656_funcs (sector_twists at the zero line, residues, cA, coupling) and B1691's own q-series sections (the_exponents).

Questions:
 (a) values at the configuration-fixed point tau = i (zero line) at B1667's two canonical radii L_max(i) = 0.68839,
     L_2(i) = 2.71926 (B1667's JSON) for: a = R (weight -1/2), a = eta^6 R (same ratios), the a.a == 0 section
     t = -5/288 at 7/2, a0 = D2R - E4 R/48, DR, f2 = 0 sections at 15/2 and 23/2 (two seeds each), generic 7/2, 19/2.
 (b) the census's "the isotropic sections (R, t = -5/288, eta^6 R) give m2 == m1 == 0": at finite L, away from i too.
     Algebra: a.a = 0 => Y(a,u) a = u (a.a) = 0, so m1 == 0 at every L; m2 is lifted by a.u != 0 at finite L.
"""
import contextlib, glob, importlib.util, io, json, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[4]
V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1691_*" / "verification"))[0]); C = V / "correction"
sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import b1656_funcs as B

b1667 = json.load(open(ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json"))
pts = b1667["points"]
def canon(tau):
    for p in (pts if isinstance(pts, list) else pts.values()):
        if isinstance(p, dict) and "tau" in p and abs(complex(*p["tau"]) - tau) < 1e-9:
            return p["L_max"], p["L_2"]
    return None
LI = canon(1j); LW = canon(complex(-0.5, math.sqrt(3) / 2)) or canon(complex(0.5, math.sqrt(3) / 2))
print("canonical radii at i:", LI, " at omega:", LW)


def masses(sec, tau, L):
    t = complex(tau); x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in sec]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(Sm, B.weighted_M(u)), compute_uv=False)
    return float(sv[2] / sv[0]), float(sv[1] / sv[0])


S = te.S
Rsec = te.B[0]
eta6R = None  # same ratios as R (the coupling is linear in a); checked through f0 R below
tneg = [S.c(F(-5, 288)) * te.e4 * te.B[0][j] + te.B[2][j] for j in range(3)]   # a.a == 0 (B1691 addendum; B1806)
a0 = [te.B[2][j] + S.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)]       # B1697
E4R = [te.e4 * te.B[0][j] for j in range(3)]                                      # f0 R at 7/2: a(i) on R(i)'s line
secs = {"R (k=-1/2)": Rsec, "E4 R (k=7/2, f2=0, f1=0)": E4R, "t=-5/288 (k=7/2, a.a==0)": tneg,
        "a0 (k=7/2)": a0, "DR (k=3/2)": te.B[1]}
with contextlib.redirect_stdout(io.StringIO()):
    for seed in (3, 4):
        secs[f"15/2 f2=0 seed{seed}"] = te.section(4, seed, drop=(2,))[0]
        secs[f"23/2 f2=0 seed{seed}"] = te.section(6, seed, drop=(2,))[0]
    for seed in (1, 2):
        secs[f"7/2 generic seed{seed}"] = te.section(2, seed)[0]
        secs[f"19/2 generic seed{seed}"] = te.section(5, seed)[0]

out = {"canonical_radii": {"i": LI, "omega": LW}, "at_i": {}, "isotropic_away_from_i": {}}
for name, sec in secs.items():
    row = {}
    for Ln, L in (("L_max(i)", LI[0]), ("L_2(i)", LI[1]), ("L=40", 40.0), ("L=2560", 2560.0)):
        m1, m2 = masses(sec, 1j, L)
        row[Ln] = {"m1/m3": "%.6g" % m1, "m2/m3": "%.6g" % m2}
    out["at_i"][name] = row
    print("tau=i", name, json.dumps(row), flush=True)

# (b) the isotropic sections away from i, at the canonical radii of each point (B1667's grid values)
probe = [complex(0.25, 1.25), complex(0.05, 2.0), complex(0.35, 1.5)]
for tau in probe:
    LL = canon(tau)
    if LL is None:
        LL = (0.67, 2.5); tag = "(L not on B1667's grid; 0.67, 2.5 used)"
    else:
        tag = "(B1667 grid)"
    for name in ("R (k=-1/2)", "t=-5/288 (k=7/2, a.a==0)"):
        row = {}
        for Ln, L in (("L_max", LL[0]), ("L_2", LL[1]), ("L=2560", 2560.0)):
            m1, m2 = masses(secs[name], tau, L)
            row[Ln + " = %.4f" % L] = {"m1/m3": "%.3g" % m1, "m2/m3": "%.6g" % m2}
        out["isotropic_away_from_i"][f"{name} @ {tau} {tag}"] = row
        print("tau=", tau, tag, name, json.dumps(row), flush=True)

json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
