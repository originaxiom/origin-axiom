#!/usr/bin/env python3
"""B1658 -- THE TWISTED HALF BOUND: in B1656's twisted, quaternionic frame, a null matter residue M = p q^T and ANY Higgs
S give adj Y(S, M) = det S * A(M) with ||A|| = 2 ||M||^2, and ||Y(u v^T, p q^T)||^2 = (|u|^2|p|^2 + |u^dag p|^2)(2|v|^2|q|^2
- |v^T q|^2). So under equal framed data (P4') each sector's spectrum is exactly (1, m2/m3, 0) with sigma1 sigma2 =
2 |det S| ||M||^2, and for a nearly null Higgs m2/m3 -> k_s |d_S|, k_s = 2/((1 + x_s)(2 - y_s)) in [1/2, 2]: one Higgs
spreads the sectors' second generations by at most a factor 4. The census against HZ2021 (data seen; a scoreboard).

Loads B1656's sealed instrument's definitions (everything above its 'T0 = time.time()') without running its cells.
Writes the_twisted_half_bound.json beside itself after every cell."""
import json, math, os, pathlib, time
import numpy as np
import sympy as sp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "the_twisted_half_bound.json")
ROOT = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
B1656 = pathlib.Path(ROOT, "frontier", "B1656_the_electrons_zero", "verification")
HZ = pathlib.Path(ROOT, "frontier", "B1637_fits_on_the_ruled_branch", "received", "HZ2021_running_masses_MZ.json")
RES = {}


def save():
    RES["seconds"] = round(time.time() - T0, 1)
    json.dump(RES, open(OUT, "w"), indent=1, default=float)


src = (B1656 / "the_electrons_zero.py").read_text(encoding="utf-8")
NS = {"__file__": str(pathlib.Path(HERE, "b1656_head_namespace.py")), "__name__": "b1656_head"}
exec(compile(src.split("T0 = time.time()")[0], "b1656_head", "exec"), NS)
OM, line_w, sector_twists, residues, weighted_M, coupling, SIXY, SECTORS, QI, QJ, QK = (NS[k] for k in (
    "OM", "line_w", "sector_twists", "residues", "weighted_M", "coupling", "SIXY", "SECTORS", "QI", "QJ", "QK"))
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]


def MR_of(line, sec):
    w = line_w(*line, OM); fl, fr = SECTORS[sec]
    x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM)
    return R, weighted_M(R)


def r1(M):
    U, s, Vh = np.linalg.svd(M); return U[:, 0]*math.sqrt(s[0]), Vh[0]*math.sqrt(s[0])     # M = p q^T


# ================================================================ T0 plumbing (void below threshold)
t0 = {}
stored = json.load(open(B1656 / "the_electrons_zero.json"))["E7"]
dev, nul = 0.0, 0.0
for sec in ("up", "down", "lep"):
    R, M = MR_of((1/9, 1/9), sec)
    r1rel = abs(R["1"])/math.sqrt(sum(abs(R[s])**2 for s in R))
    dev = max(dev, abs(r1rel - stored[sec]["R1_rel"]))
    nul = max(nul, abs(np.linalg.det(M))/np.linalg.norm(M)**2)
t0["R1_rel_vs_B1656_stored"] = dev; t0["null_residues_max"] = nul
t0["void"] = bool(dev > 1e-9 or nul > 1e-13)
RES["T0"] = t0; save()

# ================================================================ T1 the factorisation (symbolic)
t1 = {}
I = sp.I
SQ = [sp.Matrix([[I, 0], [0, -I]]), sp.Matrix([[0, 1], [-1, 0]])]; SQ.append(SQ[0]*SQ[1])
SB = [SQ[1], SQ[0], SQ[2]]; SE = SQ[1]
def ycoup(S, M): return sp.Matrix(3, 3, lambda a, b: sum((SB[a].T*SE*S*SB[b]).multiply_elementwise(M)))
s = sp.symbols("s0:4"); p0, p1, q0, q1 = sp.symbols("p0 p1 q0 q1")
Sg = s[0]*sp.eye(2) + s[1]*SQ[0] + s[2]*SQ[1] + s[3]*SQ[2]; Mn = sp.Matrix([p0, p1])*sp.Matrix([[q0, q1]])
adjY = ycoup(Sg, Mn).adjugate(); detS = sp.expand(Sg.det())
A = adjY.applyfunc(lambda e: sp.factor(sp.expand(e))/detS).applyfunc(sp.simplify)
t1["adj_over_detS_free_of_S"] = bool(all(not (e.free_symbols & set(s)) for e in A))
P2 = (p0**2 + p1**2); Q2 = (q0**2 + q1**2)
pv = sp.Matrix([P2, 2*I*p0*p1, -I*(p0**2 - p1**2)]); qv = sp.Matrix([Q2, 2*I*q0*q1, -I*(q0**2 - q1**2)])
# the rows' quadratic forms: ||pv||^2 = 2 |p|^4, ||qv||^2 = 2 |q|^4 (checked symbolically with conjugates)
pc0, pc1 = sp.symbols("pc0 pc1")
npv = sp.expand(sum(e*e.subs({p0: pc0, p1: pc1}).subs(I, -I) for e in pv) - 2*(p0*pc0 + p1*pc1)**2)
t1["row_form_norm_identity"] = str(npv)
rng = np.random.default_rng(1658); ratio = []
for _ in range(20):
    p = rng.normal(size=2) + 1j*rng.normal(size=2); q = rng.normal(size=2) + 1j*rng.normal(size=2); M = np.outer(p, q)
    S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Y = coupling(S, M)
    adj = np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])
    ratio.append(np.linalg.norm(adj)/(abs(np.linalg.det(S))*np.linalg.norm(M)**2))
t1["numeric_normA_over_detS_M2"] = [min(ratio), max(ratio)]
t1["holds"] = bool(t1["adj_over_detS_free_of_S"] and t1["row_form_norm_identity"] == "0" and abs(min(ratio) - 2) < 1e-10 and abs(max(ratio) - 2) < 1e-10)
RES["T1"] = t1; save()

# ================================================================ T2 the norm law and its range
t2 = {}
u0, u1, v0, v1 = sp.symbols("u0 u1 v0 v1"); uc0, uc1, vc0, vc1, qc0, qc1 = sp.symbols("uc0 uc1 vc0 vc1 qc0 qc1")
Ys = ycoup(sp.Matrix([u0, u1])*sp.Matrix([[v0, v1]]), Mn)
conj = {u0: uc0, u1: uc1, v0: vc0, v1: vc1, p0: pc0, p1: pc1, q0: qc0, q1: qc1}
lhs = sp.expand(sum(e*sp.expand(e.subs(conj, simultaneous=True)).subs(I, -I) for e in Ys))
uu = u0*uc0 + u1*uc1; vv = v0*vc0 + v1*vc1; pp = p0*pc0 + p1*pc1; qq = q0*qc0 + q1*qc1
udp = (uc0*p0 + uc1*p1)*(u0*pc0 + u1*pc1)                      # |u^dag p|^2
vtq = (v0*q0 + v1*q1)*(vc0*qc0 + vc1*qc1)                      # |v^T q|^2
rhs = sp.expand((uu*pp + udp)*(2*vv*qq - vtq))
t2["symbolic_norm_law_residual"] = str(sp.expand(lhs - rhs))
rng = np.random.default_rng(2); res = []; vals = []
unit = lambda: (lambda z: z/np.linalg.norm(z))(rng.normal(size=2) + 1j*rng.normal(size=2))
for _ in range(400):
    u, v, p, q = unit(), unit(), unit(), unit()
    Y2 = np.linalg.norm(coupling(np.outer(u, v), np.outer(p, q)))**2
    res.append(abs(Y2 - (1 + abs(np.vdot(u, p))**2)*(2 - abs(v @ q)**2))); vals.append(Y2)
e = np.array([1, 0], dtype=complex); f = np.array([0, 1], dtype=complex)
t2["numeric_max_residual"] = max(res); t2["range_sampled"] = [min(vals), max(vals)]
t2["attained_min"] = float(np.linalg.norm(coupling(np.outer(e, e), np.outer(f, e)))**2)      # u ⟂ p (x = 0), v^T q = 1 -> 1
t2["attained_max"] = float(np.linalg.norm(coupling(np.outer(e, e), np.outer(e, f)))**2)      # u = p (x = 1), v^T q = 0 -> 4
t2["holds"] = bool(t2["symbolic_norm_law_residual"] == "0" and max(res) < 1e-12 and abs(t2["attained_min"] - 1) < 1e-12
                   and abs(t2["attained_max"] - 4) < 1e-12 and min(vals) >= 1 - 1e-12 and max(vals) <= 4 + 1e-12)
RES["T2"] = t2; save()

# ================================================================ T3 the exact spectrum under P4' on W59's lines
t3 = {"identity_max": 0.0, "m1_max": 0.0, "k_rel_err_max": 0.0, "k_range": [9.0, 0.0]}
rng = np.random.default_rng(3)
for line in LINES18:
    for sec in ("up", "down", "lep"):
        R, M = MR_of(line, sec); p, q = r1(M)
        for trial in range(3):
            S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
            sv = np.linalg.svd(coupling(S, M), compute_uv=False)
            t3["m1_max"] = max(t3["m1_max"], sv[2]/sv[0])
            t3["identity_max"] = max(t3["identity_max"], abs(sv[0]*sv[1]/(2*abs(np.linalg.det(S))*np.linalg.norm(M)**2) - 1),
                                     abs((sv[0]**2 + sv[1]**2)/np.linalg.norm(coupling(S, M))**2 - 1))
            uu_, vv_ = r1(np.outer(rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)))
            S0 = np.outer(uu_, vv_); S0 = S0/np.linalg.norm(S0); X = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
            Sn = S0 + 1e-5*X/np.linalg.norm(X); sv = np.linalg.svd(coupling(Sn, M), compute_uv=False)
            dS = abs(np.linalg.det(Sn))/np.linalg.norm(Sn)**2
            x = abs(np.vdot(uu_/np.linalg.norm(uu_), p/np.linalg.norm(p)))**2; y = abs((vv_/np.linalg.norm(vv_)) @ (q/np.linalg.norm(q)))**2
            k = 2/((1 + x)*(2 - y)); t3["k_rel_err_max"] = max(t3["k_rel_err_max"], abs((sv[1]/sv[0])/(k*dS) - 1))
            t3["k_range"] = [min(t3["k_range"][0], k), max(t3["k_range"][1], k)]
t3["holds"] = bool(t3["m1_max"] < 1e-12 and t3["identity_max"] < 1e-10 and t3["k_rel_err_max"] < 1e-3
                   and t3["k_range"][0] >= 0.5 - 1e-12 and t3["k_range"][1] <= 2 + 1e-12)
RES["T3"] = t3; save()

# ================================================================ T4 the census against HZ2021 (a scoreboard: the data were seen)
t4 = {}
hz = json.load(open(HZ))["masses_GeV"]; v_, s_ = hz["value"], hz["sigma"]
def rat(a, b): r = v_[a]/v_[b]; return r, r*math.hypot(s_[a]/v_[a], s_[b]/v_[b])
m2 = {"up": rat("c", "t"), "down": rat("s", "b"), "lep": rat("mu", "tau")}
pairs = {}
for a, b in (("down", "up"), ("lep", "up"), ("lep", "down")):
    r = m2[a][0]/m2[b][0]; e_ = r*math.hypot(m2[a][1]/m2[a][0], m2[b][1]/m2[b][0])
    pairs["%s/%s" % (a, b)] = {"ratio": r, "sigma": e_, "z_above_4": (r - 4)/e_}
t4["m2_over_m3"] = m2; t4["pairs"] = pairs
t4["refuted_at_3sigma"] = bool(any(p["z_above_4"] > 3 for p in pairs.values()))
RES["T4"] = t4; save()

# ================================================================ T5 control: three sector-specific Higgs fields can fit
t5 = {}
target = {sec: m2[sec][0] for sec in m2}; got = {}
for sec in ("up", "down", "lep"):
    R, M = MR_of((1/9, 1/9), sec); p, q = r1(M)
    u = p/np.linalg.norm(p); v = rng.normal(size=2) + 1j*rng.normal(size=2); v = v/np.linalg.norm(v)
    S0 = np.outer(u, v); X = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); X = X/np.linalg.norm(X)
    lo, hi = 0.0, 0.5                                                   # bisect eps so that m2/m3 hits the target
    for _ in range(80):
        mid = 0.5*(lo + hi); sv = np.linalg.svd(coupling(S0 + mid*X, M), compute_uv=False)
        if sv[1]/sv[0] < target[sec]: lo = mid
        else: hi = mid
    sv = np.linalg.svd(coupling(S0 + lo*X, M), compute_uv=False); got[sec] = sv[1]/sv[0]
t5["fitted_m2_over_m3"] = got
t5["holds"] = bool(all(abs(got[s]/target[s] - 1) < 1e-6 for s in got))
RES["T5"] = t5; save()

for k in ("T0", "T1", "T2", "T3", "T5"):
    print(k, "void" if k == "T0" and RES[k]["void"] else ("HOLDS" if RES[k].get("holds", not RES[k].get("void")) else "FAILS"))
print("T4 census:", {k: round(v["z_above_4"], 2) for k, v in RES["T4"]["pairs"].items()}, "refuted at 3 sigma:", RES["T4"]["refuted_at_3sigma"])
print("seconds", RES["seconds"])
