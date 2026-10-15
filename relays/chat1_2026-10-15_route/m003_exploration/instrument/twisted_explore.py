"""EXPLORATION (unsealed, disclosed): the twisted thread-frame instrument, validated at excluded orders only.

B1656's twisted coupling vector carried along a thread in place of R, in W72's and THETA2's cells (the minimal reading):
  u_s(tau) = c_s T_s(ubar) T_s(delta) / theta1'(0),  s = i, j, k <-> theta2, theta4, theta3,  c = (-1, -1, i),
  T(alpha, beta) = e^{i pi alpha^2 tau + 2 pi i alpha beta} theta(beta + alpha tau | tau)   (theta constants of characteristic),
  ubar = (qL + qR) w, delta = (qL - qR) w, w = (a + b tau)/N in the marking of the unreduced point.
u is evaluated at the unreduced point of the thread's period and carried to the reduced point by the monomial map that
carries B1654's R there (read off R itself), then scaled to W72's normalisation (W72's R = -2 pi x B1654's).
Matter and Higgs modes are untwisted and evaluated at the reduced point, as in LIFT.

Usage: python3 twisted_explore.py   (reads forms.pkl built by build_forms.py)
"""
import io, math, pathlib, pickle, subprocess, sys, tarfile, tempfile, time, json
import numpy as np

t0 = time.time()
HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path("<repo>")
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="tw_sm_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", SMC, "docs/dossiers/the_weave_2026-10-07", "frontier"],
                      check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
import os
DOSS = TMP / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSS)); os.chdir(DOSS)
import the_surface_yukawa as SY  # noqa: E402
P = pickle.load(open(HERE / "forms.pkl", "rb"))
ev = SY.np_eval
F32n = [ev(s) for s in P["F32"]]; FM12n = [ev(s) for s in P["FM12"]]
RBn = [ev(s) for s in P["E4F"] + [P["fser"]]]
Rn, h5n, h9n = ev(P["Rser"]), ev(P["h5"]), ev(P["h9"])
beta = P["beta"]

# ------------------------------------------------------------------ thetas (numpy, z-convention periods 1 and tau)
K = np.arange(-40, 41)
def E(x): return np.exp(1j * np.pi * x)
def theta(n, z, tau):
    z = np.asarray(z)[..., None]; tau = np.asarray(tau)[..., None]
    if n == 3: return np.sum(E(K*K*tau + 2*K*z), axis=-1)
    if n == 4: return np.sum((-1.0)**(K % 2) * E(K*K*tau + 2*K*z), axis=-1)
    if n == 2: return np.sum(E((K+0.5)**2*tau + 2*(K+0.5)*z), axis=-1)
    if n == 1: return np.sum(-1j*(-1.0)**(K % 2) * E((K+0.5)**2*tau + 2*(K+0.5)*z), axis=-1)
def th1p(tau):
    tau = np.asarray(tau)[..., None]
    return np.sum(2*np.pi*(-1.0)**(K % 2)*(K+0.5)*E((K+0.5)**2*tau), axis=-1)
def T(n, al, be, tau): return E(al*al*tau + 2*al*be) * theta(n, be + al*tau, tau)
CHS = [(2, -1.0), (4, -1.0), (3, 1j)]                     # channels i, j, k
def quat3(tau, ub, de):
    d = th1p(tau)
    return np.stack([c * T(n, ub[0], ub[1], tau) * T(n, de[0], de[1], tau) / d for n, c in CHS], axis=-1)

# ------------------------------------------------------------------ reduction with the move tracked
def reduce_g(t):
    """reduce t into the fundamental domain; return (t_red, g, perm) with t_red = g t and the channel permutation
    R(t_red)_s = f_s R(t)_{perm[s]}: T flips j <-> k (theta3 <-> theta4), S swaps i <-> j (theta2 <-> theta4)"""
    g = np.array([[1, 0], [0, 1]], dtype=object)
    moves = []
    for _ in range(10000):
        n = round(t.real); t = t - n
        g = np.array([[1, -n], [0, 1]], dtype=object).dot(g)
        if n % 2: moves.append("T")
        if abs(t) < 1 - 1e-14:
            t = -1 / t; g = np.array([[0, -1], [1, 0]], dtype=object).dot(g); moves.append("S")
        else:
            break
    perm = [0, 1, 2]                                   # perm[s] = original channel feeding reduced channel s
    PT, PS = [0, 2, 1], [1, 0, 2]
    for m in reversed(moves):                          # the last move acts first on the reduced index
        pm = PT if m == "T" else PS
        perm = [perm[pm[x]] for x in range(3)] if False else perm
    # compose explicitly: R(m_k ... m_1 t)_s = f R(t)_{p_1(p_2(...p_k(s)))}
    def apply(s_):
        for m in reversed(moves):
            s_ = (PT if m == "T" else PS)[s_]
        return s_
    perm = [apply(x) for x in range(3)]
    return t, g, perm

def transport(T_un, T_red, G, u_un, perms):
    """carry u from the unreduced points to the reduced ones by the monomial map that carries B1654's R
    (the permutation from the tracked moves; the factors read off R itself); also check |f| = |J|^(-1/2)"""
    R_un, R_red = quat3(T_un, (0, 0), (0, 0)), quat3(T_red, (0, 0), (0, 0))
    out = np.zeros_like(u_un); worst = 0.0
    for p in range(len(T_un)):
        J = complex(G[p][1, 0]) * T_un[p] + complex(G[p][1, 1])
        for s_ in range(3):
            t_ = perms[p][s_]
            f = R_red[p, s_] / R_un[p, t_]
            worst = max(worst, abs(abs(f) * abs(J) ** 0.5 - 1))
            out[p, s_] = f * u_un[p, t_]
    return out, worst

# ------------------------------------------------------------------ the cells (as LIFT, one coupling vector per point)
def dot(X, Y): return np.sum(X * Y, axis=1)
def Gp(X, Y, v): return dot(v, Y)[:, None]*X + dot(v, X)[:, None]*Y - dot(X, Y)[:, None]*v
Lm = np.array([[1, 0], [1, 1]], dtype=object); Rm_ = np.array([[1, 1], [0, 1]], dtype=object)
def matrix(word):
    M = np.array([[1, 0], [0, 1]], dtype=object)
    for ch in word: M = M.dot(Lm if ch == "L" else Rm_)
    return M

def raw(word, Npts, line, charges, Nord):
    """cycle integrals for one sector on one thread; also the closure check (integrand at s and s + P)"""
    best = None
    for k in range(len(word)):
        rot = word[k:] + word[:k]; M = matrix(rot)
        if best is None or abs(M[1, 0]) < abs(best[1][1, 0]): best = (rot, M)
    rot, M = best
    a, b, c, d = (int(x) for x in M.flatten()); tr = a + d
    x0 = (a - d) / (2*c); rho = math.sqrt(tr*tr - 4) / (2*abs(c)); Pl = 2*math.acosh(tr/2)
    s = -Pl/2 + Pl*np.arange(Npts)/Npts
    Tun = x0 + rho*(np.tanh(s) + 1j/np.cosh(s))
    red = [reduce_g(t) for t in Tun]; Tr = np.array([r[0] for r in red]); G = [r[1] for r in red]; PR = [r[2] for r in red]
    # the line in the marking of the rotation's own period; characteristics (alpha, beta) = q (b, a)/N
    (la, lb) = line; qL, qR = charges
    ub = ((qL+qR)*lb/Nord, (qL+qR)*la/Nord); de = ((qL-qR)*lb/Nord, (qL-qR)*la/Nord)
    u_un = quat3(Tun, ub, de)
    v_red, tworst = transport(Tun, Tr, G, u_un, PR)
    v = -2*np.pi*v_red                                         # W72's normalisation
    y = Tr.imag
    Rw = Rn(Tr)
    rcheck = float(np.max(np.linalg.norm(v - Rw, axis=1) / np.linalg.norm(Rw, axis=1))) if (qL, qR) == (0, 0) else None
    a32 = [f(Tr) for f in F32n]; am = [f(Tr) for f in FM12n]; ar = [f(Tr) for f in RBn]
    v5, v9 = np.conj(h5n(Tr)), np.conj(h9n(Tr))
    w_ = Pl/Npts
    S = lambda arr: w_*np.sum(arr)
    out = {"y_max": float(np.max(y)), "transport_worst": tworst, "R check (zero twist)": rcheck, "_v": v, "_u": u_un,
           "K32": np.array([[S(dot(a32[i], np.conj(a32[j]))*y**1.5) for j in range(3)] for i in range(3)]),
           "KM12": np.array([[S(dot(am[i], np.conj(am[j]))*y**-0.5) for j in range(3)] for i in range(3)]),
           "K72": np.array([[S(dot(ar[i], np.conj(ar[j]))*y**3.5) for j in range(4)] for i in range(4)])}
    out["Y1"] = np.array([[S(dot(Gp(a32[i], a32[j], v), v5)*y**2.5) for j in range(3)] for i in range(3)])
    out["Y2x"] = np.array([[S(dot(Gp(a32[i], ar[j], v), v9)*y**4.5) for j in range(4)] for i in range(3)])
    out["Y3x"] = np.array([[S(dot(Gp(am[i], ar[j], v), v5)*y**2.5) for j in range(4)] for i in range(3)])
    # closure: the coupling vector at s and at s + P, both carried to their reduced points
    s2 = np.array([-0.3, 0.1]); Ta = x0 + rho*(np.tanh(s2) + 1j/np.cosh(s2))
    Tb = (a*Ta + b) / (c*Ta + d)                               # gamma moves along the geodesic by one period
    ra = [reduce_g(t) for t in Ta]; rb = [reduce_g(t) for t in Tb]
    va, _ = transport(Ta, np.array([r[0] for r in ra]), [r[1] for r in ra], quat3(Ta, ub, de), [r[2] for r in ra])
    vb, _ = transport(Tb, np.array([r[0] for r in rb]), [r[1] for r in rb], quat3(Tb, ub, de), [r[2] for r in rb])
    # same reduced point? then the carried vectors must agree (closure)
    same = [abs(ra[i][0] - rb[i][0]) for i in range(2)]
    out["closure"] = {"reduced points agree": float(max(same)),
                      "carried vectors relative difference": float(np.max(np.abs(va - vb)) / np.max(np.abs(va)))}
    return out

def inv_sqrt(Kmat):
    e, U = np.linalg.eigh(Kmat)
    return None if e.min() <= 0 else U @ np.diag(e**-0.5) @ U.conj().T

def cells(r):
    res = {}
    for cell, comp in [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"), ("C3", "ORTH")]:
        name = cell if comp is None else f"{cell}/{comp}"
        if cell == "C1":
            KL, Y, KR = r["K32"], r["Y1"], r["K32"]
        else:
            Kx = r["K72"]
            cc = {"E4": np.zeros(3, complex), "THETA2": np.array(beta, complex), "ORTH": -Kx[:3, 3]/Kx[3, 3]}[comp]
            P3 = np.hstack([np.eye(3), cc.reshape(3, 1)]); KR = P3 @ Kx @ P3.conj().T
            KL, Y = (r["K32"], r["Y2x"] @ P3.T) if cell == "C2" else (r["KM12"], r["Y3x"] @ P3.T)
        A, B = inv_sqrt(KL), inv_sqrt(KR)
        if A is None or B is None: res[name] = None; continue
        Mx = A @ Y @ B.T
        U, sv, Vh = np.linalg.svd(Mx); o = np.argsort(sv)[::-1]
        res[name] = {"s": sv[o], "UL": (np.linalg.inv(A) @ U[:, o]) if False else U[:, o], "A": A}
    return res

if __name__ == "__main__":
    report = {}
    # 1. zero twist must reproduce the untwisted cells (LR, LLR) against THETA2's stored ratios
    t2 = json.loads((REPO / "relays/chat1_2026-10-14_step3/theta2_completion.json").read_text())["per thread"]
    for word in ("LR", "LLR"):
        r = raw(word, 384, (0, 1), (0, 0), 5)
        cs = cells(r)
        cmp = {}
        for name, key in (("C2/E4", "H-E4 C2"), ("C3/E4", "H-E4 C3"), ("C3/THETA2", "H-THETA2 C3"), ("C2/THETA2", "H-THETA2 C2")):
            m23 = cs[name]["s"][1]/cs[name]["s"][0]
            cmp[name] = (float(m23), t2[word][key]["m2/m3"])
        report[f"zero twist {word}"] = {"cells m2/m3 (this, THETA2)": cmp, "transport_worst": r["transport_worst"], "closure": r["closure"], "R check": r["R check (zero twist)"]}
        print(word, report[f"zero twist {word}"], flush=True)
    # 2. excluded orders only: N = 5 on L R^25 (line (0,1)/5) and N = 3 on L R^9 (line (0,1)/3): closure and d = e at N = 5
    for word, line, Nord in (("L" + "R"*25, (0, 1), 5), ("L" + "R"*9, (0, 1), 3)):
        for sector, ch in (("up", (1, -4)), ("down", (1, 2)), ("lepton", (-3, 6))):
            r = raw(word, 512, line, ch, Nord)
            print(f"N={Nord} {word[:6]}.. {sector}: closure {r['closure']}  transport_worst {r['transport_worst']:.1e}  y_max {r['y_max']:.2f}", flush=True)
    print("seconds", round(time.time() - t0, 1))
