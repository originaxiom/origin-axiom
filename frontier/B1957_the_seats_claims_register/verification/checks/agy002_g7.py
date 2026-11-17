"""B1957: agy-002's gates 7 and 7B, recomputed by main.  Data-free.
G7.1   the count of the Standard Model's parameters from the rank of the flavour group's action on the Yukawa matrices,
       in exact integer arithmetic; the same with the neutrino operator.
G7.2   the seat's table of 46 nodes: its propagated ranks follow from the table by one rule (a node's rank is the largest
       of its own and its parents'); the table is the seat's classification, read from its script's text; and what the
       histogram becomes under main's verdicts on gates 2 and 5.
G7B.1  one more scale of the same dimension: the rank stays 1 and the number of free ratios rises by one.
G7B.2  the closed integral for the Casimir curve's slope, against the Bessel sum.
G7B.3  the first column's drift: the perturbative formula, the seat's 32 states, and the near-degenerate case.
G7B.4  E8's roots: the 27 beside the centraliser's colour has no colour singlet; the 27 with colour inside E6 has nine."""
import sys, pathlib, math, ast, itertools, functools, collections
from fractions import Fraction as F
import numpy as np, sympy as sp, mpmath as mp
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    # G7.1: exact ranks at an integer point
    rng = np.random.default_rng(20261117); ri = lambda: sp.Matrix(3, 3, lambda i, j: int(rng.integers(-5, 6)) + sp.I * int(rng.integers(-5, 6)))
    Yu, Yd, Ye = ri(), ri(), ri(); A = ri(); Kap = A + A.T; gens = []
    for i in range(3): gens.append(sp.Matrix(3, 3, lambda a, b: sp.I if (a, b) == (i, i) else 0))
    for i in range(3):
        for j in range(i + 1, 3):
            gens.append(sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else (-1 if (a, b) == (j, i) else 0)))
            gens.append(sp.Matrix(3, 3, lambda a, b: sp.I if (a, b) in ((i, j), (j, i)) else 0))
    z = sp.zeros(3, 3); flat = lambda M: [sp.re(x) for x in M] + [sp.im(x) for x in M]
    cs, ce = [], []
    for slot in range(5):                                                  # Q, u, d, L, e
        for G in gens:
            dYu = G * Yu if slot == 0 else (-Yu * G if slot == 1 else z); dYd = G * Yd if slot == 0 else (-Yd * G if slot == 2 else z); dYe = G * Ye if slot == 3 else (-Ye * G if slot == 4 else z)
            dK = G * Kap + Kap * G.T if slot == 3 else z; v = flat(dYu) + flat(dYd) + flat(dYe); k6 = [dK[r, c] for r in range(3) for c in range(r, 3)]
            cs.append(v); ce.append(v + [sp.re(x) for x in k6] + [sp.im(x) for x in k6])
    rs, re_ = sp.Matrix(cs).rank(), sp.Matrix(ce).rank()
    print("G7.1: 45 generators acting on 54 real Yukawa entries at an integer point: rank %d, so %d unbroken and %d physical; with the gauge couplings, the Higgs's two and the strong phase: %d" % (rs, 45 - rs, 54 - rs, 54 - rs + 6))
    print("      with the neutrino operator's 12 more: rank %d, %d unbroken, %d physical, %d in all (the seat: 41, 44; 19 and 28)" % (re_, 45 - re_, 66 - re_, 66 - re_ + 6))
    # G7.2: the table, parsed from the script's text
    import subprocess
    src = subprocess.run(["git", "show", "origin/agy-002/closure:relays/agy002_closure_g7/verify_closure_g7.py"], capture_output=True, text=True).stdout or None   # read as text; parsed, never run
    if src:
        tree = ast.parse(src); fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "build_canonical_dag")
        lst = next(n.value for n in ast.walk(fn) if isinstance(n, ast.AnnAssign) and getattr(n.target, "id", "") == "nodes"); nodes = list(ast.literal_eval(lst))
        fl = ["SM01:y_u", "SM02:y_c", "SM03:y_t", "SM04:y_d", "SM05:y_s", "SM06:y_b", "SM07:y_e", "SM08:y_mu", "SM09:y_tau", "SM10:V_us", "SM11:V_cb", "SM12:V_ub", "SM13:delta_CKM"]
        nodes += [(s, "SM_TARGET", 0, ["OP:CIM_33m6_Triple_Overlap", "OP:Level6_Higgs_v_plus_pi6", "OP:BPV_MV_2Loop_RGE", "S:Torsion_Tau_SU2R_Break", "S:Bidoublet_Angle_Beta"], True) for s in fl]
        nodes += [(s, "SM_TARGET", 0, ["PR-3:PatiSalam_2Loop_Corridor", "S:Unified_Coupling_Alpha_U", "S:Collar_Modulus_Delta_PS", "S:EWSB_Scale_Anchor_vEW"], True) for s in ("SM14:g_1", "SM15:g_2", "SM16:g_3")]
        nodes += [("SM17:m_H_over_vEW", "SM_TARGET", 0, ["PR-4:Dterm_Higgs_IR_Envelope", "S:Bidoublet_Angle_Beta", "SM03:y_t", "SM16:g_3"], True), ("SM18:v_EW", "SM_TARGET", 0, ["PR-10:Picard_Casimir_Scale_Law", "S:EWSB_Scale_Anchor_vEW"], True), ("SM19:bar_theta_QCD", "SM_TARGET", 0, ["PR-2:3Fam_Strong_CP_Zero"], True)]
        def ranks(nodes, override=None):
            nm = {n[0]: n for n in nodes}; memo = {}
            def r(i, stack=()):
                assert i not in stack, "cycle"
                if i not in memo: memo[i] = max([(override or {}).get(i, nm[i][2])] + [r(p, stack + (i,)) for p in nm[i][3]])
                return memo[i]
            return {i: r(i) for i in nm}
        hist = lambda rk, cat: [sum(1 for n in nodes if n[1] == cat and rk[n[0]] == k) for k in range(4)]
        rk = ranks(nodes); cats = collections.Counter(n[1] for n in nodes)
        print("G7.2: the table in the seat's script: %d nodes (%s), no cycle; propagated ranks: relations %s, targets %s (the seat: [2, 6, 2, 0] and [0, 0, 1, 18])" % (len(nodes), ", ".join("%d %s" % (v, k) for k, v in cats.items()), hist(rk, "RELATION"), hist(rk, "SM_TARGET")))
        rk2 = ranks(nodes, {"OP:Level6_Higgs_v_plus_pi6": 2})
        print("      with the Higgs-mode node at one bit (main's verdict on gate 2): relations %s, targets %s; the node is a parent of all thirteen flavour targets, which were at rank 3 already" % (hist(rk2, "RELATION"), hist(rk2, "SM_TARGET")))
        print("      the ranks at the roots are assigned in the table, not computed: the histogram is the table's own classification propagated")
    # G7B.1
    D19 = sp.Matrix([[1] * 9 + [0] * 7 + [1, 1, 0]]); D20 = sp.Matrix([[1] * 9 + [0] * 7 + [1, 1, 0, 1]])
    print("G7B.1: one row of mass dimensions: 19 quantities, rank %d, %d free ratios; a twentieth of dimension one: rank %d, %d free ratios" % (D19.rank(), 19 - D19.rank(), D20.rank(), 20 - D20.rank()))
    # G7B.2
    from scipy.special import kv
    def dVA(L, m=1.0):
        C = 4 * L; k = np.arange(1, int(60 / (C * m)) + 2); x = k * C * m
        return 4 * (-4 * 28 * math.pi ** 2 / 90 / C ** 5 + (-1.0) * 76 * ((-1.0) ** k * m ** 4 * (-kv(3, x) / x ** 2) * k * m).sum() / (2 * math.pi ** 2))
    worst = 0.0
    for L in (0.2, 1.0, 3.0):
        integ = mp.quad(lambda t: mp.log(1 + mp.exp(-4 * L * mp.cosh(t))) * mp.cosh(3 * t), [0, 2, 6, 12]); closed = -7 * math.pi ** 2 / (1440 * L ** 5) - 19 / (2 * math.pi ** 2 * L ** 2) * float(integ)
        worst = max(worst, abs(dVA(L) / closed - 1))
    x = sp.Symbol("x", positive=True); ident = sp.simplify(sp.diff(sp.besselk(2, x) / x ** 2, x) + sp.besselk(3, x) / x ** 2)
    print("G7B.2: d/dx [K_2(x)/x^2] + K_3(x)/x^2 = %s; the slope of branch A, Bessel sum against -(7 pi^2)/(1440 L^5) - (19/(2 pi^2 L^2)) integral: relative difference at L = 1/5, 1, 3 at most %.1e; both terms are negative for every L" % (ident, worst))
    # G7B.3
    m1, m2, p = sp.symbols("m1 m2 p", positive=True); K0 = sp.diag(m1, m2); P = sp.Matrix([[0, p], [p, 0]]); dK = -sp.Rational(3, 2) * (P * K0 + K0 * P)
    rot = sp.simplify((dK * K0 + K0 * dK)[0, 1] / (m2 ** 2 - m1 ** 2)); print("G7B.3: the first-order rotation between two neutrino states: %s (it grows as the two masses approach)" % sp.factor(rot))
    th = math.pi / 8; s6, s3, s2 = 6 ** 0.5, 3 ** 0.5, 2 ** 0.5
    U = np.array([[2 / s6, math.cos(th) / s3, math.sin(th) / s3], [-1 / s6, math.cos(th) / s3 - math.sin(th) / s2, math.sin(th) / s3 + math.cos(th) / s2], [-1 / s6, math.cos(th) / s3 + math.sin(th) / s2, math.sin(th) / s3 - math.cos(th) / s2]], complex)
    def drift(ms, phs, yt):
        K = U @ np.diag([m * np.exp(1j * ph) for m, ph in zip(ms, phs)]) @ U.T; D = np.diag([1, 1, math.exp(-3 * yt * yt * (-30) / (32 * math.pi ** 2))]); Kir = D @ K @ D
        ev = np.linalg.eigh(Kir.conj().T @ Kir)[1]; slot = int(np.where(np.argsort([m * m for m in ms]) == 0)[0][0]); return abs(abs(ev[0, slot]) ** 2 - 2 / 3)
    spec = ((1, 2, 5), (0, 1, 5), (1, 3, 9), (2, 4, 1)); phs = ((0, 0, 0), (0, math.pi / 3, math.pi / 2), (0, math.pi, 0), (math.pi / 4, math.pi / 2, math.pi))
    d20 = max(drift(a, b, 1 / 20) for a in spec for b in phs); d5 = max(drift(a, b, 1 / 5) for a in spec for b in phs)
    print("      the seat's 32 states (four spectra, four sets of phases, two values of y_tau, 30 e-folds): largest drift of |U_e1|^2 from 2/3: %.2e at y_tau = 1/20, %.2e at 1/5 (the seat's bars 1/1000 and 1/50); with m2/m1 = 1 + 1e-5: %.3f" % (d20, d5, drift((1, 1.00001, 5), (0, 0, 0), 1 / 20)))
    # G7B.4
    roots = [tuple(2 * s1 if k == i else (2 * s2 if k == j else 0) for k in range(8)) for i in range(8) for j in range(i + 1, 8) for s1 in (-1, 1) for s2 in (-1, 1)]
    roots += [s for s in itertools.product((-1, 1), repeat=8) if sum(1 for x in s if x < 0) % 2 == 0]; dot = lambda u, v: sum(a * b for a, b in zip(u, v))
    a2 = [(2, -2, 0, 0, 0, 0, 0, 0), (0, 2, -2, 0, 0, 0, 0, 0)]; e6 = [r for r in roots if dot(r, a2[0]) == 0 and dot(r, a2[1]) == 0]; A2 = [r for r in roots if r[3:] == (0,) * 5 and sum(r[:3]) == 0]
    rem = [r for r in roots if r not in set(e6) and r not in set(A2)]; wt = collections.Counter((dot(r, a2[0]), dot(r, a2[1])) for r in rem); key = sorted(wt)[0]; one27 = [r for r in rem if (dot(r, a2[0]), dot(r, a2[1])) == key]
    g = [(0, 0, 0, 2, -2, 0, 0, 0), (0, 0, 0, 0, 2, -2, 0, 0)]
    print("G7B.4: E8's %d roots: %d of the first SU(3), %d of its centraliser E6, %d others in six sets of %d; in one such 27, states neutral under the first SU(3): %d; neutral under an SU(3) inside E6: %d (the seat: 6, 72, 162, 27; 0 and 9)" % (
        len(roots), len(A2), len(e6), len(rem), len(one27), sum(1 for r in one27 if dot(r, a2[0]) == 0 and dot(r, a2[1]) == 0), sum(1 for r in one27 if dot(r, g[0]) == 0 and dot(r, g[1]) == 0)))
