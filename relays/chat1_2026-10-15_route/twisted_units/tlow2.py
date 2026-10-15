"""The low-thread instrument, stage 2 (chat1): ball arithmetic, factorised integrands, every charge assignment at once.

As tlow.py (stage 1): every form at the UNREDUCED point of the thread's period, the untwisted forms carried from the
reduced point as integer-weight ratios X_c / R_c by R's monomial map (S swaps i <-> j and multiplies by t^m, m = k + 1/2;
T^n swaps j <-> k for odd n; the Higgs modes also carry chi_i(S) = chi_i(T) = i), R and the theta constants with
characteristic evaluated directly by explicit sums (never jtheta). New here:
  - arb/acb arithmetic (python-flint) at a working precision set by the thread's height (rigorous rounding radii);
  - the theta constants with characteristic T_s(q) = theta_s[q lb/N, q la/N](0|tau) are computed once per point for
    every residue r = q mod N; the actual charge's value follows exactly: T_s(al + a, be + b) = (-1)^a [s = 4] *
    e^{2 pi i (sig_s + al + a) b} T_s(al, be), a, b integers, sig = 1/2 on theta2;
  - the per-field reading dresses each field's units and each Higgs mode by D_c(q) = (T_s(q) / theta_s(0))^2 (W92's
    z-form); D(q) and D(q mod N) differ by one constant phase on every component, which no singular value sees, so the
    dressing is taken per residue; R is the neutral kernel; THETA2 does not apply;
  - the minimal reading keeps the units and Higgs untwisted, with B1656's coupling vector
    v_s = -2 pi c_s T_s(qL + qR) T_s(qL - qR) / theta1'(0), c = (-1, -1, i) on (i, j, k), at the ACTUAL charges;
  - the Yukawa integrands are factorised, Y_ij = (v.b_j)(a_i.h*) + (v.a_i)(b_j.h*) - (a_i.b_j)(v.h*), so every sector
    of every assignment shares the per-residue and per-pair pieces.
Cells as THETA2's and the 15:17 instrument's: C1 = (3/2, 3/2) h5; C2 = (3/2, 7/2) h9 under E4 (c = 0), THETA2 (minimal
only) and ORTH; C3 = (-1/2, 7/2) h5 likewise. Masses: singular values of K_L^-1/2 Y (K_R^-1/2)^T.
"""
import math, cmath, json, pickle, sys, time
import flint
from flint import arb, acb

B = {"e_i": (1, 0, 0), "v+": (0, 1, -1j), "v-": (0, 1, 1j)}
SECTORS = {"up": ("Q", "u", "H"), "down": ("Q", "d", "Hbar"), "lepton": ("L", "e", "Hbar")}
SIG = {2: 0.5, 4: 0.0, 3: 0.0}
CS = (2, 4, 3)                                         # components i, j, k <-> theta 2, 4, 3
CC = (-1, -1, 1j)


def cx(z): return acb(z.real, z.imag) if isinstance(z, complex) else acb(z)


# ------------------------------------------------------------------ forms
class Forms:
    """W72's forms as {n8: [c0, c1, c2]} (line vectors folded in), parsed at the working precision"""
    def __init__(self, P, round53=False):
        self.P, self.round53 = P, round53
    def prepare(self):
        import mpmath as mp
        with mp.workdps(80):                           # parse the solve's coefficients at full precision, whatever the caller's dps
            return self._prepare(mp)
    def _prepare(self, mp):
        def prep(ser):
            out = {}
            for (l, n8), a in ser.items():
                z = mp.mpc(a)
                if self.round53: z = mp.mpc(float(z.real), float(z.imag))
                c = acb(arb(mp.nstr(z.real, 60)), arb(mp.nstr(z.imag, 60)))
                v = out.setdefault(n8, [acb(0), acb(0), acb(0)])
                for k in range(3):
                    if B[l][k] != 0: v[k] += c * cx(complex(B[l][k]))
            return out
        P = self.P
        self.F32 = [prep(s) for s in P["F32"]]; self.FM12 = [prep(s) for s in P["FM12"]]
        self.RB = [prep(s) for s in P["E4F"] + [P["fser"]]]
        self.h5, self.h9 = prep(P["h5"]), prep(P["h9"])
        self.beta = P["beta"]
        ex = set()
        for s in self.F32 + self.FM12 + self.RB + [self.h5, self.h9]: ex |= set(s)
        self.nmin, self.nmax = min(ex), max(ex)
        return self


def ev(ser, pw):
    v = [acb(0), acb(0), acb(0)]
    for n8, c in ser.items():
        p = pw[n8]
        v[0] += c[0] * p; v[1] += c[1] * p; v[2] += c[2] * p
    return v


# ------------------------------------------------------------------ thetas
def E(x): return (acb.pi() * acb(0, 1) * x).exp()


def theta_char(s, al, be, tau, K):
    """theta_s[al, be](0 | tau) = sum_n eps_s(n) e^{i pi (n + sig + al)^2 tau + 2 pi i (n + sig + al) be}; al, be arb"""
    sig = arb(SIG[s])
    c = -int(math.floor(float((al + sig).mid()) + 0.5))
    tot = acb(0)
    for n in range(c - K, c + K + 1):
        x = arb(n) + sig + al
        t = E(x * x * tau + 2 * x * be)
        tot += -t if (s == 4 and n % 2) else t
    return tot


def th1p(tau, K):
    tot = acb(0)
    for n in range(-K - 1, K + 1):
        h = arb(n) + arb(0.5)
        t = 2 * acb.pi() * h * E(h * h * tau)
        tot += -t if n % 2 else t
    return tot


def char_factor(s, r, q, lb, la, N):
    """T_s at the actual charge q from its value at the residue r = q mod N (exact; see the docstring)"""
    k = (q - r) // N
    a, b = k * lb, k * la
    al_r = arb(r * lb) / N
    sgn = -1 if (s == 4 and a % 2) else 1
    return sgn * E(2 * (arb(SIG[s]) + al_r + a) * b)


# ------------------------------------------------------------------ reduction, every step recorded (decided in double)
def reduce_steps(t):
    steps = []
    for _ in range(10000):
        tc = complex(float(t.real.mid()), float(t.imag.mid()))
        n = round(tc.real)
        if n:
            steps.append(("T", n)); t = t - n; tc -= n
        if abs(tc) < 1 - 1e-12:
            steps.append(("S", t)); t = -1 / t
        else:
            break
    return t, steps


def carry(X_red, R_red, R_un, steps, m, higgs):
    r = [X_red[c] / R_red[c] for c in range(3)]
    for kind, val in reversed(steps):
        if kind == "T":
            if higgs: r = [x * cx(1j ** (val % 4)) for x in r]
            if val % 2: r = [r[0], r[2], r[1]]
        else:
            f = val ** m if m else acb(1)
            if higgs: f = f * acb(0, 1)
            r = [x / f for x in r]
            r = [r[1], r[0], r[2]]
    return [r[c] * R_un[c] for c in range(3)]


def R_from(tau, K):
    d1 = th1p(tau, K)
    z = arb(0)
    return [-2 * acb.pi() * cx(CC[c]) * theta_char(CS[c], z, z, tau, K) ** 2 / d1 for c in range(3)], d1


# ------------------------------------------------------------------ products
def dot(X, Y): return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]
def conjv(X): return [x.conjugate() for x in X]


def matrix(word):
    A, B_, C, D = 1, 0, 0, 1
    for ch in word:
        if ch == "L": A, B_, C, D = A + B_, B_, C + D, D
        else: A, B_, C, D = A, A + B_, C, C + D
    return A, B_, C, D


def thread_geometry(word, kforce=None):
    """the rotation with the smallest |C| (its period's axis is highest, so its unreduced points stay farthest from the
    real axis), its matrix and radius, the prefix moved to the end, and the geodesic's true height in the fundamental
    domain (min over rotations of min(|B|, |C|)), which sets the working precision"""
    best, hmin = None, None
    for k in range(len(word)):
        rot = word[k:] + word[:k]; M = matrix(rot)
        if best is None or abs(M[2]) < abs(best[1][2]): best = (rot, M, k)
        m_ = min(abs(M[1]), abs(M[2]))
        hmin = m_ if hmin is None else min(hmin, m_)
    if kforce is not None:                             # a chosen rotation (for the rotation-invariance control)
        rot = word[kforce:] + word[:kforce]; best = (rot, matrix(rot), kforce)
    rot, (a, b, c, d), k = best
    tr = a + d
    rho = math.sqrt(tr * tr - 4) / (2 * abs(c))
    height = math.sqrt(tr * tr - 4) / (2 * hmin)
    return rot, (a, b, c, d), rho, k, height


def line_in_rotation(word, k, line, N):
    """a line (a, b) in the marking of word's own matrix (the closure law's action (a, b) -> (aD + bB, aC + bA)),
    carried to the rotation word[k:] + word[:k], whose matrix is P^-1 M P with P = matrix(word[:k]): (a, b) -> f_P(a, b)"""
    A, B_, C, D = matrix(word[:k])
    a, b = line
    return ((a * D + b * B_) % N, (a * C + b * A) % N)


def bits_for(height): return int(2 * math.pi * 2.6 * height / math.log(2)) + 140


def configuration(F, word, line, N, assignments, Npts, readings=("per-field", "minimal"), kforce=None, carry_line=True):
    """Integrals for every sector of every assignment (dict name -> charges) in both readings on one (word, line).
    kforce: integrate over a chosen rotation; carry_line=False skips carrying the line into the rotation (the negative
    control only)."""
    rot, (a, b, c, d), rho, kshift, height = thread_geometry(word, kforce)
    tr = a + d
    x0 = arb(a - d) / (2 * c); rhoA = arb(tr * tr - 4).sqrt() / (2 * abs(c)); PlA = 2 * (arb(tr) / 2).acosh()
    la, lb = line_in_rotation(word, kshift, line, N) if carry_line else tuple(line)
    # the triples each reading needs
    pf_keys, mn_keys = set(), set()
    plan = {}
    for name, ch in assignments.items():
        for sec, (fl, fr, hh) in SECTORS.items():
            qL, qR = ch[fl], ch[fr]
            qH = ch["H"] if hh == "H" else -ch["H"]
            k_pf = (qL % N, qR % N, qH % N)
            k_mn = (qL + qR, qL - qR)
            plan[(name, sec)] = (k_pf, k_mn)
            pf_keys.add(k_pf); mn_keys.add(k_mn)
    residues = sorted(set(k for t in pf_keys for k in t))
    acc_pf = {k: {} for k in pf_keys}; acc_mn = {k: {} for k in mn_keys}
    accK_pf = {r: {} for r in residues}; accK_mn = {}
    first_last = {}

    def add(store, key, M):
        if key not in store: store[key] = [[acb(0)] * len(M[0]) for _ in M]
        S = store[key]
        for i in range(len(M)):
            for j in range(len(M[0])): S[i][j] += M[i][j]

    def point(tau, sink):
        y = tau.imag
        K = int(math.ceil(math.sqrt(flint.ctx.prec * 0.6932 / (math.pi * float(y.mid()))))) + 3
        t_red, steps = reduce_steps(tau)
        R_un, d1 = R_from(tau, K)
        Kr = int(math.ceil(math.sqrt(flint.ctx.prec * 0.6932 / (math.pi * float(t_red.imag.mid()))))) + 3
        R_red, _ = R_from(t_red, Kr)
        q8 = (2 * acb.pi() * acb(0, 1) * t_red / 8).exp(); q8i = 1 / q8
        pw = {0: acb(1)}
        for n in range(1, F.nmax + 1): pw[n] = pw[n - 1] * q8
        for n in range(1, -F.nmin + 1): pw[-n] = pw[-n + 1] * q8i
        car = lambda ser, k, h=False: carry(ev(ser, pw), R_red, R_un, steps, int(k + 0.5), h)
        A32 = [car(s, 1.5) for s in F.F32]; AM = [car(s, -0.5) for s in F.FM12]; BR = [car(s, 3.5) for s in F.RB]
        H5 = car(F.h5, 2.5, True); H9 = car(F.h9, 4.5, True)
        th0 = [theta_char(s, arb(0), arb(0), tau, K) for s in CS]
        T = {}
        for r in range(N):
            al, be = arb(r * lb) / N, arb(r * la) / N
            T[r] = [theta_char(s, al, be, tau, K) for s in CS]
        y15, ym05, y35, y25, y45 = y ** 1.5, y ** -0.5, y ** 3.5, y ** 2.5, y ** 4.5
        out = {"pf": {}, "mn": {}, "Kpf": {}, "Kmn": None}
        # --- per-field: dressed pieces per residue
        if "per-field" in readings:
            D = {r: [(T[r][c] / th0[c]) ** 2 for c in range(3)] for r in residues}
            dr = lambda X, r: [X[c] * D[r][c] for c in range(3)]
            a32 = {r: [dr(X, r) for X in A32] for r in residues}
            am = {r: [dr(X, r) for X in AM] for r in residues}
            br = {r: [dr(X, r) for X in BR] for r in residues}
            h5c = {r: conjv(dr(H5, r)) for r in residues}; h9c = {r: conjv(dr(H9, r)) for r in residues}
            v = R_un
            for r in residues:
                out["Kpf"][r] = {
                    "K32": [[dot(a32[r][i], conjv(a32[r][j])) * y15 for j in range(3)] for i in range(3)],
                    "KM12": [[dot(am[r][i], conjv(am[r][j])) * ym05 for j in range(3)] for i in range(3)],
                    "K72": [[dot(br[r][i], conjv(br[r][j])) * y35 for j in range(4)] for i in range(4)]}
            va = {r: [dot(v, X) for X in a32[r]] for r in residues}
            vm = {r: [dot(v, X) for X in am[r]] for r in residues}
            vb = {r: [dot(v, X) for X in br[r]] for r in residues}
            vh5 = {r: dot(v, h5c[r]) for r in residues}; vh9 = {r: dot(v, h9c[r]) for r in residues}
            cache = {}
            def pair(tag, fn, *k):
                key = (tag,) + k
                if key not in cache: cache[key] = fn()
                return cache[key]
            for (rL, rR, rH) in pf_keys:
                ah5 = pair("ah5", lambda: [dot(X, h5c[rH]) for X in a32[rL]], rL, rH)
                bh5 = pair("bh5", lambda: [dot(X, h5c[rH]) for X in a32[rR]], rR, rH)
                ab = pair("ab", lambda: [[dot(Xa, Xb) for Xb in a32[rR]] for Xa in a32[rL]], rL, rR)
                Y1 = [[(va[rR][j] * ah5[i] + va[rL][i] * bh5[j] - ab[i][j] * vh5[rH]) * y25 for j in range(3)] for i in range(3)]
                ah9 = pair("ah9", lambda: [dot(X, h9c[rH]) for X in a32[rL]], rL, rH)
                rh9 = pair("rh9", lambda: [dot(X, h9c[rH]) for X in br[rR]], rR, rH)
                arr = pair("ar", lambda: [[dot(Xa, Xb) for Xb in br[rR]] for Xa in a32[rL]], rL, rR)
                Y2 = [[(vb[rR][j] * ah9[i] + va[rL][i] * rh9[j] - arr[i][j] * vh9[rH]) * y45 for j in range(4)] for i in range(3)]
                mh5 = pair("mh5", lambda: [dot(X, h5c[rH]) for X in am[rL]], rL, rH)
                rh5 = pair("rh5", lambda: [dot(X, h5c[rH]) for X in br[rR]], rR, rH)
                mr = pair("mr", lambda: [[dot(Xa, Xb) for Xb in br[rR]] for Xa in am[rL]], rL, rR)
                Y3 = [[(vb[rR][j] * mh5[i] + vm[rL][i] * rh5[j] - mr[i][j] * vh5[rH]) * y25 for j in range(4)] for i in range(3)]
                out["pf"][(rL, rR, rH)] = {"Y1": Y1, "Y2x": Y2, "Y3x": Y3}
        # --- minimal: untwisted units and Higgs, B1656's coupling vector at the actual charges
        if "minimal" in readings:
            h5c, h9c = conjv(H5), conjv(H9)
            out["Kmn"] = {"K32": [[dot(A32[i], conjv(A32[j])) * y15 for j in range(3)] for i in range(3)],
                          "KM12": [[dot(AM[i], conjv(AM[j])) * ym05 for j in range(3)] for i in range(3)],
                          "K72": [[dot(BR[i], conjv(BR[j])) * y35 for j in range(4)] for i in range(4)]}
            ah5 = [dot(X, h5c) for X in A32]; ah9 = [dot(X, h9c) for X in A32]; mh5 = [dot(X, h5c) for X in AM]
            rh9 = [dot(X, h9c) for X in BR]; rh5 = [dot(X, h5c) for X in BR]
            ab = [[dot(Xa, Xb) for Xb in A32] for Xa in A32]
            arr = [[dot(Xa, Xb) for Xb in BR] for Xa in A32]; mr = [[dot(Xa, Xb) for Xb in BR] for Xa in AM]
            def Tact(s_idx, q):
                r = q % N
                return T[r][s_idx] * char_factor(CS[s_idx], r, q, lb, la, N)
            for (u, dl) in mn_keys:
                if (u, dl) == (0, 0):
                    v = R_un
                else:
                    v = [-2 * acb.pi() * cx(CC[c]) * Tact(c, u) * Tact(c, dl) / d1 for c in range(3)]
                va = [dot(v, X) for X in A32]; vm = [dot(v, X) for X in AM]; vb = [dot(v, X) for X in BR]
                vh5, vh9 = dot(v, h5c), dot(v, h9c)
                Y1 = [[(va[j] * ah5[i] + va[i] * ah5[j] - ab[i][j] * vh5) * y25 for j in range(3)] for i in range(3)]
                Y2 = [[(vb[j] * ah9[i] + va[i] * rh9[j] - arr[i][j] * vh9) * y45 for j in range(4)] for i in range(3)]
                Y3 = [[(vb[j] * mh5[i] + vm[i] * rh5[j] - mr[i][j] * vh5) * y25 for j in range(4)] for i in range(3)]
                out["mn"][(u, dl)] = {"Y1": Y1, "Y2x": Y2, "Y3x": Y3}
        sink(out)

    def accumulate(out):
        for k, M in out["pf"].items():
            for key in M: add(acc_pf[k], key, M[key])
        for r, M in out["Kpf"].items():
            for key in M: add(accK_pf[r], key, M[key])
        for k, M in out["mn"].items():
            for key in M: add(acc_mn[k], key, M[key])
        if out["Kmn"] is not None:
            for key in out["Kmn"]: add(accK_mn, key, out["Kmn"][key])

    first = {}
    for j in range(Npts):
        s = -PlA / 2 + PlA * j / Npts
        tau = x0 + rhoA * acb(s.tanh(), 1 / s.cosh())
        if j == 0:
            point(tau, lambda o: (first.__setitem__("o", o), accumulate(o)))
        else:
            point(tau, accumulate)
    last = {}
    s = PlA / 2
    point(x0 + rhoA * acb(s.tanh(), 1 / s.cosh()), lambda o: last.__setitem__("o", o))
    # closure: every Y integrand one period on
    clos = {}
    for tag in ("pf", "mn"):
        for k in first["o"][tag]:
            worst = 0.0
            for key in ("Y1", "Y2x", "Y3x"):
                A0, A1 = first["o"][tag][k][key], last["o"][tag][k][key]
                num = max(float(abs(A1[i][jj] - A0[i][jj]).mid()) for i in range(len(A0)) for jj in range(len(A0[0])))
                den = max(float(abs(A0[i][jj]).mid()) for i in range(len(A0)) for jj in range(len(A0[0])))
                worst = max(worst, num / den)
            clos[(tag, k)] = worst
    w = PlA / Npts
    scale = lambda S: {key: [[x * w for x in row] for row in M] for key, M in S.items()}
    return {"rot": rot, "rho": rho, "height": height, "line_in_rotation": (la, lb), "bits": flint.ctx.prec,
            "Npts": Npts, "plan": plan, "closure": clos,
            "pf": {k: scale(v) for k, v in acc_pf.items()}, "Kpf": {r: scale(v) for r, v in accK_pf.items()},
            "mn": {k: scale(v) for k, v in acc_mn.items()}, "Kmn": scale(accK_mn) if accK_mn else None}


# ------------------------------------------------------------------ cells and masses (mpmath at the working precision)
def to_mp(M, mp):
    nd = mp.mp.dps + 10
    return mp.matrix([[mp.mpc(mp.mpf(x.real.mid().str(nd, radius=False)), mp.mpf(x.imag.mid().str(nd, radius=False)))
                       for x in row] for row in M])


def cells_for(KL32, KR32, KLM12, KR72, Y, beta, reading, mp):
    def inv_sqrt(K):
        E_, U = mp.eighe(K); ev_ = [E_[i] for i in range(E_.rows)]
        if min(ev_) <= 0: return None
        return U * mp.diag([e ** -0.5 for e in ev_]) * U.transpose_conj()
    res = {}
    for cell, comp in [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"),
                       ("C3", "ORTH")]:
        name = cell if comp is None else f"{cell}/{comp}"
        if comp == "THETA2" and reading == "per-field":
            continue
        if cell == "C1":
            KL, Ym, KR = KL32, Y["Y1"], KR32
        else:
            Kx = KR72
            if comp == "E4": cc = [0, 0, 0]
            elif comp == "THETA2": cc = [mp.mpc(b_) for b_ in beta]
            else: cc = [-Kx[i, 3] / Kx[3, 3] for i in range(3)]
            P3 = mp.matrix(3, 4)
            for i in range(3): P3[i, i] = 1; P3[i, 3] = cc[i]
            KR = P3 * Kx * P3.transpose_conj()
            KL, Ym = (KL32, Y["Y2x"] * P3.T) if cell == "C2" else (KLM12, Y["Y3x"] * P3.T)
        A_, B_ = inv_sqrt(KL), inv_sqrt(KR)
        if A_ is None or B_ is None:
            res[name] = None; continue
        Mx = A_ * Ym * B_.T
        U, S, V = mp.svd_c(Mx)
        o = sorted(range(S.rows), key=lambda i: abs(S[i]))                # ascending: generation 1, 2, 3
        res[name] = {"s": [abs(S[i]) for i in o], "U": [[U[r_, i] for i in o] for r_ in range(U.rows)]}
    return res


def masses(conf, F, assignments, N, mp):
    """per assignment, reading, sector and cell: the singular values (ascending) and the left vectors (for the CKM)"""
    mp.mp.dps = conf["bits"] // 3
    out = {}
    Kmn = {k: to_mp(v, mp) for k, v in conf["Kmn"].items()} if conf["Kmn"] else None
    Kpf = {r: {k: to_mp(v, mp) for k, v in M.items()} for r, M in conf["Kpf"].items()}
    for name in assignments:
        for reading in ("per-field", "minimal"):
            for sec in SECTORS:
                k_pf, k_mn = conf["plan"][(name, sec)]
                if reading == "per-field":
                    if k_pf not in conf["pf"]: continue
                    rL, rR, rH = k_pf
                    Y = {k: to_mp(v, mp) for k, v in conf["pf"][k_pf].items()}
                    c = cells_for(Kpf[rL]["K32"], Kpf[rR]["K32"], Kpf[rL]["KM12"], Kpf[rR]["K72"], Y, F.beta, reading, mp)
                else:
                    if Kmn is None or k_mn not in conf["mn"]: continue
                    Y = {k: to_mp(v, mp) for k, v in conf["mn"][k_mn].items()}
                    c = cells_for(Kmn["K32"], Kmn["K32"], Kmn["KM12"], Kmn["K72"], Y, F.beta, reading, mp)
                out[(name, reading, sec)] = c
    return out
