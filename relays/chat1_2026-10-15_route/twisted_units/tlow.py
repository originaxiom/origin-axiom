"""The low-thread instrument (chat1; for the T-low family of DESIGN_DRAFT.md; built and validated at excluded orders).

The thread frame's cells on any closed geodesic, with every form evaluated at the UNREDUCED point of the period, where
the per-field dressing and the twisted coupling vector live, in double precision (sound for y_max <= 3, THETA2's
admitted range). The untwisted forms are known as q-series only near the fundamental domain, so each is carried from
the reduced point by R's own monomial map:
  - for a rho_R object X of weight k (units 3/2, -1/2, 7/2), the componentwise ratio X_c / R_c (R of weight -1/2) has
    the integer weight m = k + 1/2, and the monomial matrices cancel in it. Step by step (T: t -> t + n; S: t -> -1/t
    with f(-1/t) = t^k rho(S) f(t), the record's convention) the ratio picks up t^m at each S step and is permuted
    (S swaps i <-> j, T^n with n odd swaps j <-> k). So no square-root branch arises;
  - the Higgs modes live in rho' = rho_R (x) chi_i with chi_i(S) = chi_i(T) = i (the record's RS2/RT2 against RS/RT),
    so their ratio also picks up i at each S step and i^n at each T^n step;
  - R itself, the per-field dressing D_c and the twisted coupling vector are evaluated directly at the unreduced point
    by explicit theta sums (never jtheta).
Readings: "minimal" (untwisted units and Higgs, B1656's twisted coupling vector) and "per-field" (W92's dressing on
every unit and Higgs mode, R neutral, no THETA2).

Usage (self-tests at excluded orders): python3 tlow.py <forms.pkl> <theta2_completion.json> <units_cells.py dir>
"""
import json, math, pickle, sys, time
import numpy as np

B = {"e_i": (1, 0, 0), "v+": (0, 1, -1j), "v-": (0, 1, 1j)}
SECTORS = {"up": ("Q", "u", "H"), "down": ("Q", "d", "Hbar"), "lepton": ("L", "e", "Hbar")}
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
KK = np.arange(-40, 41)


# ------------------------------------------------------------------ forms (series keyed (line, exponent in eighths))
def np_series(ser):
    keys = list(ser)
    vec = np.array([[complex(ser[k]) * B[k[0]][c] for c in range(3)] for k in keys])
    ex = np.array([k[1] / 8 for k in keys])
    return ex, vec


def ev_series(S, T):
    ex, vec = S
    return np.exp(2j * np.pi * np.outer(T, ex)) @ vec                  # (len(T), 3)


# ------------------------------------------------------------------ thetas (z-convention, period 1), vectorised in tau
def E(x): return np.exp(1j * np.pi * x)
def theta(n, z, tau):
    z = np.asarray(z, complex)[..., None]; tau = np.asarray(tau, complex)[..., None]
    if n == 3: return np.sum(E(KK * KK * tau + 2 * KK * z), axis=-1)
    if n == 4: return np.sum((-1.0) ** (KK % 2) * E(KK * KK * tau + 2 * KK * z), axis=-1)
    h = KK + 0.5
    t = E(h * h * tau + 2 * h * z)
    return np.sum(t, axis=-1) if n == 2 else np.sum(-1j * (-1.0) ** (KK % 2) * t, axis=-1)
def th1p(tau):
    tau = np.asarray(tau, complex)[..., None]; h = KK + 0.5
    return np.sum(2 * np.pi * (-1.0) ** (KK % 2) * h * E(h * h * tau), axis=-1)
def Tc(n, al, be, tau): return E(al * al * tau + 2 * al * be) * theta(n, be + al * tau, tau)
CHS = [(2, -1.0), (4, -1.0), (3, 1j)]
def quat3(tau, ub, de):
    d = th1p(tau)
    return np.stack([c * Tc(n, ub[0], ub[1], tau) * Tc(n, de[0], de[1], tau) / d for n, c in CHS], axis=-1)
def R_at(tau): return -2 * np.pi * quat3(tau, (0.0, 0.0), (0.0, 0.0))     # W72's normalisation
def dressing(tau, q, line, N):
    la, lb = line
    al, be = q * lb / N, q * la / N
    return np.stack([(Tc(s, al, be, tau) / theta(s, 0.0, tau)) ** 2 for s in (2, 4, 3)], axis=-1)


# ------------------------------------------------------------------ reduction with every step recorded
def reduce_steps(t):
    """t_red = g t; returns (t_red, steps) with steps a list of ("T", n) and ("S", t_before)"""
    steps = []
    for _ in range(10000):
        n = round(t.real)
        if n:
            steps.append(("T", n)); t = t - n
        if abs(t) < 1 - 1e-14:
            steps.append(("S", t)); t = -1 / t
        else:
            break
    return t, steps


def carry(X_red, R_red, R_un, steps, m, higgs):
    """X at the unreduced point from X at the reduced one, through the integer-weight ratio X_c / R_c.
    Going forward (unreduced -> reduced) the ratio r obeys: T^n: r'(t+n) = P_T^n r(t); S: r'(-1/t) = t^m P_S r(t)
    (times chi = i^n and i for the Higgs), with P_S swapping components 0, 1 and P_T swapping 1, 2 for odd n."""
    r = X_red / R_red
    for kind, val in reversed(steps):                     # undo the steps, last first
        if kind == "T":                                   # forward: r(t - n) = chi^-n P_T^n r(t); undone: x chi^n
            if higgs:
                r = r * (1j ** (val % 4))
            if val % 2:
                r = r[[0, 2, 1]]
        else:
            fac = val ** m * (1j if higgs else 1.0)
            r = r / fac
            r = r[[1, 0, 2]]
    return r * R_un


# ------------------------------------------------------------------ the forms
class Forms:
    def __init__(self, P):
        self.F32 = [np_series(s) for s in P["F32"]]
        self.FM12 = [np_series(s) for s in P["FM12"]]
        self.RB = [np_series(s) for s in P["E4F"] + [P["fser"]]]
        self.h5, self.h9 = np_series(P["h5"]), np_series(P["h9"])
        self.beta = P["beta"]


def matrix(word):
    M = np.array([[1, 0], [0, 1]], dtype=object)
    for ch in word:
        M = M.dot(np.array([[1, 0], [1, 1]] if ch == "L" else [[1, 1], [0, 1]], dtype=object))
    return M


def thread_points(word, Npts):
    best = None
    for k in range(len(word)):
        rot = word[k:] + word[:k]; M = matrix(rot)
        if best is None or abs(M[1, 0]) < abs(best[1][1, 0]): best = (rot, M)
    rot, M = best
    a, b, c, d = (int(x) for x in M.flatten()); tr = a + d
    x0 = (a - d) / (2 * c); rho = math.sqrt(tr * tr - 4) / (2 * abs(c)); Pl = 2 * math.acosh(tr / 2)
    s = -Pl / 2 + Pl * np.arange(Npts) / Npts
    return x0 + rho * (np.tanh(s) + 1j / np.cosh(s)), Pl / Npts, (a, b, c, d), rot


def evaluate_unreduced(F, Tun):
    """every untwisted form at the unreduced points (carried), plus R there; also the reduced values for checks"""
    red = [reduce_steps(t) for t in Tun]
    Tr = np.array([r[0] for r in red])
    Rr, Ru = R_at(Tr), R_at(Tun)
    out = {"Tr": Tr, "R_un": Ru, "R_red": Rr}
    def carried(S, k, higgs=False):
        Xr = ev_series(S, Tr)
        m = int(k + 0.5)
        return np.array([carry(Xr[p], Rr[p], Ru[p], red[p][1], m, higgs) for p in range(len(Tun))]), Xr
    out["F32"] = [carried(S, 1.5) for S in F.F32]
    out["FM12"] = [carried(S, -0.5) for S in F.FM12]
    out["RB"] = [carried(S, 3.5) for S in F.RB]
    out["h5"] = carried(F.h5, 2.5, True); out["h9"] = carried(F.h9, 4.5, True)
    return out


def dot(X, Y): return np.sum(X * Y, axis=-1)
def Gp(X, Y, v): return dot(v, Y)[:, None] * X + dot(v, X)[:, None] * Y - dot(X, Y)[:, None] * v


def integrals(EU, Tun, w, line, N, sector_charges, reading):
    """K and Y for one sector (qL, qR, qH) at the unreduced points, in the given reading"""
    qL, qR, qH = sector_charges
    y = Tun.imag
    def D(q):
        return dressing(Tun, q, line, N) if (reading == "per-field" and q) else 1.0
    DL, DR, DH = D(qL), D(qR), D(qH)
    a32 = [X[0] * DL for X in EU["F32"]]; am = [X[0] * DL for X in EU["FM12"]]
    b32 = [X[0] * DR for X in EU["F32"]]; br = [X[0] * DR for X in EU["RB"]]
    h5c, h9c = np.conj(EU["h5"][0] * DH), np.conj(EU["h9"][0] * DH)
    if reading == "per-field" or (qL, qR) == (0, 0):
        v = EU["R_un"]
    else:
        la, lb = line
        ub = ((qL + qR) * lb / N, (qL + qR) * la / N); de = ((qL - qR) * lb / N, (qL - qR) * la / N)
        v = -2 * np.pi * quat3(Tun, ub, de)
    S = lambda arr: w * np.sum(arr)
    r = {"KL32": np.array([[S(dot(a32[i], np.conj(a32[j])) * y ** 1.5) for j in range(3)] for i in range(3)]),
         "KR32": np.array([[S(dot(b32[i], np.conj(b32[j])) * y ** 1.5) for j in range(3)] for i in range(3)]),
         "KLM12": np.array([[S(dot(am[i], np.conj(am[j])) * y ** -0.5) for j in range(3)] for i in range(3)]),
         "KR72": np.array([[S(dot(br[i], np.conj(br[j])) * y ** 3.5) for j in range(4)] for i in range(4)]),
         "Y1": np.array([[S(dot(Gp(a32[i], b32[j], v), h5c) * y ** 2.5) for j in range(3)] for i in range(3)]),
         "Y2x": np.array([[S(dot(Gp(a32[i], br[j], v), h9c) * y ** 4.5) for j in range(4)] for i in range(3)]),
         "Y3x": np.array([[S(dot(Gp(am[i], br[j], v), h5c) * y ** 2.5) for j in range(4)] for i in range(3)])}
    return r


def inv_sqrt(K):
    e, U = np.linalg.eigh(K)
    return None if e.min() <= 0 else U @ np.diag(e ** -0.5) @ U.conj().T


def cells(r, beta, reading):
    res = {}
    for cell, comp in [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"),
                       ("C3", "ORTH")]:
        name = cell if comp is None else f"{cell}/{comp}"
        if comp == "THETA2" and reading == "per-field":
            res[name] = None; continue
        if cell == "C1":
            KL, Y, KR = r["KL32"], r["Y1"], r["KR32"]
        else:
            Kx = r["KR72"]
            cc = {"E4": np.zeros(3, complex), "THETA2": np.array(beta, complex), "ORTH": -Kx[:3, 3] / Kx[3, 3]}[comp]
            P3 = np.hstack([np.eye(3), cc.reshape(3, 1)]); KR = P3 @ Kx @ P3.conj().T
            KL, Y = (r["KL32"], r["Y2x"] @ P3.T) if cell == "C2" else (r["KLM12"], r["Y3x"] @ P3.T)
        A, Bm = inv_sqrt(KL), inv_sqrt(KR)
        if A is None or Bm is None: res[name] = None; continue
        sv = np.sort(np.linalg.svd(A @ Y @ Bm.T, compute_uv=False))[::-1]
        res[name] = sv
    return res


if __name__ == "__main__":
    t0 = time.time()
    P = pickle.load(open(sys.argv[1], "rb")); T2 = json.load(open(sys.argv[2]))["per thread"]
    sys.path.insert(0, sys.argv[3])
    F = Forms(P)
    report = {}
    # (1) pointwise invariance at zero twist: the carried integrands at the unreduced points equal the direct ones
    #     at the reduced points (K and Y, every cell's ingredients)
    worst = 0.0
    for word in ("LLR", "LLRLR", "LLRLRR", "LLLRLRRR"):
        Tun, w, M, rot = thread_points(word, 64)
        EU = evaluate_unreduced(F, Tun)
        for key, k in (("F32", 1.5), ("FM12", -0.5), ("RB", 3.5)):
            for X in EU[key]:
                un, red = X
                worst = max(worst, float(np.max(np.abs(np.sum(np.abs(un) ** 2, 1) * Tun.imag ** k
                                                       - np.sum(np.abs(red) ** 2, 1) * EU["Tr"].imag ** k)
                                                / (np.sum(np.abs(red) ** 2, 1) * EU["Tr"].imag ** k))))
        y_un, y_r = Tun.imag, EU["Tr"].imag
        a = [X[0] for X in EU["F32"]]; ar = [X[1] for X in EU["F32"]]
        Iu = dot(Gp(a[0], a[1], EU["R_un"]), np.conj(EU["h5"][0])) * y_un ** 2.5
        Ir = dot(Gp(ar[0], ar[1], EU["R_red"]), np.conj(EU["h5"][1])) * y_r ** 2.5
        worst_Y = float(np.max(np.abs(Iu - Ir) / np.abs(Ir)))
        report[f"invariance {word}"] = {"K worst": worst, "Y1[0,1] worst": worst_Y, "y_un min": float(Tun.imag.min())}
        print(word, report[f"invariance {word}"], flush=True)
    # (2) zero twist against THETA2's stored m2/m3 on admitted threads
    for word in ("LR", "LLR", "LLRR", "LLRLR", "LLLRR", "LLRLRR"):
        if word not in T2 or T2[word].get("y_max", 9) > 3.0: continue
        Tun, w, M, rot = thread_points(word, 512)
        EU = evaluate_unreduced(F, Tun)
        cs = cells(integrals(EU, Tun, w, (0, 1), 5, (0, 0, 0), "minimal"), F.beta, "minimal")
        cmp_ = {}
        for name, key in (("C2/E4", "H-E4 C2"), ("C3/E4", "H-E4 C3"), ("C3/THETA2", "H-THETA2 C3"), ("C2/THETA2", "H-THETA2 C2")):
            s = cs[name]; cmp_[name] = (float(s[1] / s[0]), T2[word][key]["m2/m3"], float(abs(s[1] / s[0] / T2[word][key]["m2/m3"] - 1)))
        report[f"THETA2 {word}"] = cmp_
        print(word, {k: f"{v[2]:.1e}" for k, v in cmp_.items()}, flush=True)
    # (3) against the ball-arithmetic instrument (units_cells.py, forms at the unreduced point directly) on L R^n
    #     towers, both readings, SM charges, excluded orders: the same integrals by two routes
    import units_cells as UC, flint
    flint.ctx.prec = 800
    for n, N, line in ((4, 3, (0, 1)), (5, 5, (0, 1)), (5, 5, (1, 2)), (4, 7, (1, 3))):
        word = "L" + "R" * n
        Tun, w, M, rot = thread_points(word, 600)
        EU = evaluate_unreduced(F, Tun)
        for reading, src in (("minimal", UC.UntwistedSource(P)), ("per-field", UC.PerFieldFactoredSource(P))):
            ref = UC.configuration(src, n, line, N, SM, 600)
            mp_acc = ref["acc"]
            worst = 0.0
            for sec, (fl, fr, hh) in SECTORS.items():
                qH = SM["H"] if hh == "H" else -SM["H"]
                r = integrals(EU, Tun, w, line, N, (SM[fl], SM[fr], qH), reading)
                for key in ("KL32", "KR32", "KLM12", "KR72", "Y1", "Y2x", "Y3x"):
                    A = np.array([[complex(float(x.real.mid()), float(x.imag.mid())) for x in row] for row in mp_acc[sec][key]])
                    worst = max(worst, float(np.max(np.abs(r[key] - A)) / np.max(np.abs(A))))
            report[f"two routes L R^{n} N={N} line {line} {reading}"] = worst
            print(f"two routes L R^{n} N={N} line {line} {reading}: worst relative {worst:.1e}", flush=True)
    report["seconds"] = round(time.time() - t0, 1)
    json.dump(report, open("tlow_selftest.json", "w"), indent=1)
    print("seconds", report["seconds"])
