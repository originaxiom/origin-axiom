#!/usr/bin/env python3
"""B1659 -- THE JOINT LAW: in B1656's twisted, quaternionic frame (B1658's coupling Y(S, M), bilinear, 3 x 3), for EVERY
Higgs S and EVERY matter M in M2(C):
  J1  det Y(S, M) = 4 det S det M tr(eps S M^T)                         (an antisymmetric pairing: tr(eps M M^T) = 0)
  J2  adj Y(S, M) = det S A(M) + det M P A(S),  P = diag(1, -1, -1),     A the explicit quadratic below
  J2b on null M = p q^T, A(M) = B1658's q~ p~^T (its T1), so J2 extends B1658's factorisation off the cone
  J3  on B1656's sector matter (W59's 18 lines at omega, P4 with L in {5, 50, 500}) J1, J2 hold numerically, and the
      squared singular values are the roots of x^3 - e1 x^2 + e2 x - e3 with e1 = ||Y||^2, e2 = ||det S A(M) + det M P A(S)||^2,
      e3 = 16 |det S det M tr(eps S M^T)|^2
  J4  corollaries: m1 = 0 whenever det S = 0, or det M = 0, or tr(eps S M^T) = 0 -- the last with BOTH defects non-zero
      (S = M non-null); and for S = S0 + e X, M = M0 + e Z with null S0, M0 both light masses are first order in e
  J5  controls that can fail: a symmetric perturbation of the coupling breaks J1; A in place of P A breaks J2; B1657's
      untwisted Y(a, v) = a v^T + v a^T - (a.v) 1 has det (a.a)(v.v)(a.v), a SYMMETRIC pairing, so the two frames differ
Writes the_joint_law.json and the_joint_law_run.txt. No data."""
import json, math, pathlib, sys, time
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(d for d in HERE.parents if (d / "frontier").is_dir())
OUT = HERE / "the_joint_law.json"; T0 = time.time(); RES = {}
def save(): RES["seconds"] = round(time.time() - T0, 1); json.dump(RES, open(OUT, "w"), indent=1, default=float)
def say(*a): print(*a, flush=True)
# ---- B1656's head (its coupling, residues, channel norms), as B1658 loads it
src = (ROOT / "frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text(encoding="utf-8")
assert src.count("T0 = time.time()") == 1
NS = {"__file__": str(HERE / "b1656_head_namespace.py"), "__name__": "b1656_head"}
exec(compile(src.split("T0 = time.time()")[0], "b1656_head", "exec"), NS)
OM, line_w, sector_twists, residues, weighted_M, coupling, SIXY, SECTORS, cA, UNITS = (NS[k] for k in (
    "OM", "line_w", "sector_twists", "residues", "weighted_M", "coupling", "SIXY", "SECTORS", "cA", "UNITS"))
EPS = np.array([[0, 1], [-1, 0]], dtype=complex); P = np.diag([1, -1, -1])
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
def A_np(M):
    m0, m1, m2, m3 = M.ravel(); I = 1j
    return np.array([[m0**2 + m1**2 + m2**2 + m3**2, 2*I*(m0*m2 + m1*m3), -I*(m0**2 + m1**2 - m2**2 - m3**2)],
                     [2*I*(m0*m1 + m2*m3), -4*m1*m2, 2*(m0*m1 - m2*m3)],
                     [-I*(m0**2 - m1**2 + m2**2 - m3**2), 2*(m0*m2 - m1*m3), -m0**2 + m1**2 + m2**2 - m3**2]])
def adj3(Y): return np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i + j) for j in range(3)] for i in range(3)])
def ell(S, M): return np.trace(EPS @ S @ M.T)
# ================================================================ J1, J2, J2b symbolic
s = sp.symbols("s0:4"); m = sp.symbols("m0:4"); S_ = sp.Matrix(2, 2, s); M_ = sp.Matrix(2, 2, m)
QI = sp.Matrix([[sp.I, 0], [0, -sp.I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI*QJ; E_ = QJ; BL = [QJ, QI, QK]
def Ysym(S, M): return sp.Matrix(3, 3, lambda a, b: sum((BL[a].T*E_*S*BL[b]).multiply_elementwise(M)))
def Asym(M):
    m0, m1, m2, m3 = M; I = sp.I
    return sp.Matrix([[m0**2 + m1**2 + m2**2 + m3**2, 2*I*(m0*m2 + m1*m3), -I*(m0**2 + m1**2 - m2**2 - m3**2)],
                      [2*I*(m0*m1 + m2*m3), -4*m1*m2, 2*(m0*m1 - m2*m3)],
                      [-I*(m0**2 - m1**2 + m2**2 - m3**2), 2*(m0*m2 - m1*m3), -m0**2 + m1**2 + m2**2 - m3**2]])
Y_ = Ysym(S_, M_).applyfunc(sp.expand)
j1 = sp.expand(Y_.det() - 4*S_.det()*M_.det()*(E_*S_*M_.T).trace())
Psym = sp.diag(1, -1, -1)
j2 = (Y_.adjugate() - S_.det()*Asym(m) - M_.det()*Psym*Asym(s)).applyfunc(sp.expand)
p0, p1, q0, q1 = sp.symbols("p0 p1 q0 q1")
Mn = sp.Matrix([[p0*q0, p0*q1], [p1*q0, p1*q1]])
An = Asym([Mn[0, 0], Mn[0, 1], Mn[1, 0], Mn[1, 1]]).applyfunc(sp.expand)
nrm = sp.expand(sum(sp.Abs(x)**2 for x in An)) if False else None
# B1658's T1: A(p q^T) = q~ p~^T with p~ = (p.p, 2i p0 p1, -i(p0^2 - p1^2)) and q~ from q's quadratic forms -- checked as rank one
rk1 = all(sp.expand(An[i, j]*An[k, l] - An[i, l]*An[k, j]) == 0 for i in range(3) for j in range(3) for k in range(3) for l in range(3))
RES["J1"] = {"residual_is_zero": bool(j1 == 0), "holds": bool(j1 == 0)}
RES["J2"] = {"residual_is_zero": bool(j2 == sp.zeros(3, 3)), "holds": bool(j2 == sp.zeros(3, 3))}
RES["J2b"] = {"A_on_null_M_rank_one": bool(rk1)}
say("J1", RES["J1"], "J2", RES["J2"], "J2b(rank one)", rk1, f"[{time.time()-T0:.0f}s]"); save()
# J2b numerically against B1658's stated form: ||A(p q^T)|| = 2 ||M||^2 and adj Y(S, pq^T) = det S A(pq^T)
rng = np.random.default_rng(1659); dev = 0.0; nr = 0.0
for _ in range(200):
    p, q = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2); M = np.outer(p, q)
    S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Y = coupling(S, M)
    dev = max(dev, np.abs(adj3(Y) - np.linalg.det(S)*A_np(M)).max()/np.abs(adj3(Y)).max())
    nr = max(nr, abs(np.linalg.norm(A_np(M))/(2*np.linalg.norm(M)**2) - 1))
RES["J2b"].update({"adj_on_null_vs_detS_A": dev, "normA_over_2normM2_minus_1": nr, "holds": bool(rk1 and dev < 1e-12 and nr < 1e-12)})
say("J2b", RES["J2b"]); save()
# ================================================================ J3 on the sector matter
DATA = {}
for ln in LINES18:
    w = line_w(*ln, OM); DATA[ln] = {}
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        DATA[ln][sec] = (R, c)
def Ms(ln, sec, L):
    R, c = DATA[ln][sec]; return weighted_M({k: (math.sqrt(2*np.pi*L + c[k])*R[k] if c[k] is not None else 0j) for k in UNITS})
j3 = {"det_law_over_Y3": 0.0, "adj_law_over_Y2": 0.0, "spectrum_rel": 0.0, "cases": 0}
for ln in LINES18:
    for sec in SECTORS:
        for L in (5.0, 50.0, 500.0):
            M = Ms(ln, sec, L)
            for _ in range(2):
                S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Y = coupling(S, M); n = np.linalg.norm(Y)
                dS, dM, l = np.linalg.det(S), np.linalg.det(M), ell(S, M)
                j3["det_law_over_Y3"] = max(j3["det_law_over_Y3"], abs(np.linalg.det(Y) - 4*dS*dM*l)/n**3)
                AD = dS*A_np(M) + dM*P @ A_np(S)
                j3["adj_law_over_Y2"] = max(j3["adj_law_over_Y2"], np.abs(adj3(Y) - AD).max()/n**2)
                e1, e2, e3 = n**2, np.linalg.norm(AD)**2, 16*abs(dS*dM*l)**2
                roots = np.sort(np.abs(np.roots([1, -e1, e2, -e3])))[::-1]; sv2 = np.linalg.svd(Y, compute_uv=False)**2
                j3["spectrum_rel"] = max(j3["spectrum_rel"], max(abs(roots[i] - sv2[i])/sv2[0] for i in range(3)))
                j3["cases"] += 1
j3["holds"] = bool(j3["det_law_over_Y3"] < 1e-13 and j3["adj_law_over_Y2"] < 1e-13 and j3["spectrum_rel"] < 1e-10)
RES["J3"] = j3; say("J3", j3, f"[{time.time()-T0:.0f}s]"); save()
# ================================================================ J4 corollaries
def m1_rel(S, M): sv = np.linalg.svd(coupling(S, M), compute_uv=False); return sv[2]/sv[0]
j4 = {}
X = [rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)) for _ in range(40)]
nul = [np.outer(rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)) for _ in range(40)]
j4["a_null_M_m1_max"] = max(m1_rel(X[i], nul[i]) for i in range(40))
j4["b_null_S_m1_max"] = max(m1_rel(nul[i], X[i]) for i in range(40))
j4["c_S_equals_M_nonnull_m1_max"] = max(m1_rel(X[i], X[i]) for i in range(40))
j4["c_S_equals_M_defect_min"] = min(abs(np.linalg.det(Z))/np.linalg.norm(Z)**2 for Z in X)
j4["generic_m1_min"] = min(m1_rel(X[i], X[(i + 1) % 40]) for i in range(40))
sl = []
for i in range(10):
    S0, M0 = nul[i], nul[(i + 7) % 40]; Xs, Zs = X[i], X[(i + 3) % 40]; v = []
    for e in (1e-3, 1e-4):
        sv = np.linalg.svd(coupling(S0 + e*Xs, M0 + e*Zs), compute_uv=False); v.append((sv[1]/sv[0], sv[2]/sv[0]))
    sl.append((math.log10(v[0][0]/v[1][0]), math.log10(v[0][1]/v[1][1])))
j4["first_order_slopes_m2_m1"] = [min(min(a) for a in sl), max(max(a) for a in sl)]
j4["holds"] = bool(j4["a_null_M_m1_max"] < 1e-12 and j4["b_null_S_m1_max"] < 1e-12 and j4["c_S_equals_M_nonnull_m1_max"] < 1e-12
                   and j4["c_S_equals_M_defect_min"] > 1e-3 and j4["generic_m1_min"] > 1e-4
                   and abs(j4["first_order_slopes_m2_m1"][0] - 1) < 0.02 and abs(j4["first_order_slopes_m2_m1"][1] - 1) < 0.02)
RES["J4"] = j4; say("J4", j4); save()
# ================================================================ J5 controls
j5 = {}
Wsym = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); Wsym = Wsym + Wsym.T
bad1 = []
for i in range(20):
    S, M = X[i], X[(i + 5) % 40]; Y = coupling(S, M) + 0.1*np.linalg.norm(coupling(S, M))*Wsym/np.linalg.norm(Wsym)
    bad1.append(abs(np.linalg.det(Y) - 4*np.linalg.det(S)*np.linalg.det(M)*ell(S, M))/np.linalg.norm(Y)**3)
j5["a_perturbed_coupling_det_law_min"] = min(bad1)
bad2 = []
for i in range(20):
    S, M = X[i], X[(i + 5) % 40]; Y = coupling(S, M)
    bad2.append(np.abs(adj3(Y) - np.linalg.det(S)*A_np(M) - np.linalg.det(M)*A_np(S)).max()/np.linalg.norm(Y)**2)
j5["b_A_for_PA_adj_law_min"] = min(bad2)
def Y57(a, v): return np.outer(a, v) + np.outer(v, a) - (a @ v)*np.eye(3)
b3 = []
for i in range(20):
    a, v = rng.normal(size=3) + 1j*rng.normal(size=3), rng.normal(size=3) + 1j*rng.normal(size=3)
    b3.append(abs(np.linalg.det(Y57(a, v)) - (a @ a)*(v @ v)*(a @ v))/abs(np.linalg.det(Y57(a, v))))
j5["c_B1657_det_symmetric_pairing_max"] = max(b3)
j5["c_B1657_Y_vv_m1_over_m3_min"] = min((lambda sv: sv[2]/sv[0])(np.linalg.svd(Y57(v, v), compute_uv=False))
                                          for v in (rng.normal(size=3) + 1j*rng.normal(size=3) for _ in range(20)))
j5["holds"] = bool(j5["a_perturbed_coupling_det_law_min"] > 1e-4 and j5["b_A_for_PA_adj_law_min"] > 1e-3
                   and j5["c_B1657_det_symmetric_pairing_max"] < 1e-12 and j5["c_B1657_Y_vv_m1_over_m3_min"] > 1e-4)
RES["J5"] = j5; say("J5", j5); save()
RES["all_hold"] = all(RES[k]["holds"] for k in ("J1", "J2", "J2b", "J3", "J4", "J5")); say("ALL", RES["all_hold"]); save()
