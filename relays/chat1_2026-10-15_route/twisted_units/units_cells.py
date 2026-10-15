"""The twisted-units instrument (chat1; built before any twisted unit exists; tested only at excluded orders).

Carries matter units supplied per field (any rational q-exponents) along an L.R^n tower thread, in W72's and THETA2's
cells, in ball arithmetic (python-flint), with every form evaluated at the unreduced point of the thread's period
(sound where the period stays at y >~ 1, i.e. min |C| = 1: the L.R^n towers). It generalises
m003_exploration/deep_cusp/deep_cusp.py:
  - left and right units come from different fields (C1: 3/2 x 3/2; C2: 3/2 x 7/2; C3: -1/2 x 7/2);
  - units, Higgs modes and coupling vector are supplied by a UnitSource (the SM seat's construction, when it exists);
  - the sectors come from a charge assignment (6Y: Q, u^c, d^c, L, e^c, H), so the null's assignments run the same way;
  - per configuration: closure of every Y integrand over one period, and r_calc (Npts vs 1.25 Npts; full coefficients
    vs coefficients rounded to 53 bits).

Usage (the self-test, excluded orders only):  python3 units_cells.py <forms.pkl> <deep_cusp_deep.json>
"""
import json, math, pickle, sys, time
from fractions import Fraction
import flint
from flint import arb, acb
import mpmath as mp

B = {"e_i": (1, 0, 0), "v+": (0, 1, -1j), "v-": (0, 1, 1j)}
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u", "H"), "down": ("Q", "d", "Hbar"), "lepton": ("L", "e", "Hbar")}


# ------------------------------------------------------------------ series: {(line, Fraction exponent): coefficient}
def to_acb(z, round53=False):
    z = mp.mpc(z)
    if round53:
        z = mp.mpc(float(z.real), float(z.imag))
    return acb(arb(mp.nstr(z.real, 60)), arb(mp.nstr(z.imag, 60)))


def prep(series, round53=False):
    """-> {Fraction exponent: [c0, c1, c2]} with the line vectors folded in"""
    out = {}
    for (l, e), a in series.items():
        e = Fraction(e)
        v = out.setdefault(e, [acb(0), acb(0), acb(0)])
        for c in range(3):
            if B[l][c] != 0:
                v[c] += to_acb(a, round53) * acb(B[l][c].real, B[l][c].imag)
    return out


def ev(ser, pw):
    v = [acb(0), acb(0), acb(0)]
    for e, c in ser.items():
        p = pw[e]
        v[0] += c[0] * p; v[1] += c[1] * p; v[2] += c[2] * p
    return v


# ------------------------------------------------------------------ thetas with characteristic (as the instruments)
KMAX = 40
def E(x): return (acb.pi() * acb(0, 1) * x).exp()
def theta(n, z, tau):
    s = acb(0)
    for k in range(-KMAX, KMAX + 1):
        if n == 3: s += E(k * k * tau + 2 * k * z)
        elif n == 4: s += (-1) ** (k % 2) * E(k * k * tau + 2 * k * z)
        else:
            h = arb(k) + arb(0.5); t = E(h * h * tau + 2 * h * z)
            s += t if n == 2 else acb(0, -1) * (-1) ** (k % 2) * t
    return s
def th1p(tau):
    s = acb(0)
    for k in range(-KMAX, KMAX + 1):
        h = arb(k) + arb(0.5); s += 2 * acb.pi() * (-1) ** (k % 2) * h * E(h * h * tau)
    return s
def Tc(n, al, be, tau): return E(al * al * tau + 2 * al * be) * theta(n, be + al * tau, tau)
CHS = [(2, acb(-1)), (4, acb(-1)), (3, acb(0, 1))]
def quat3(tau, ub, de, d): return [c * Tc(n, ub[0], ub[1], tau) * Tc(n, de[0], de[1], tau) / d for n, c in CHS]
def dot(X, Y): return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]
def Gp(X, Y, v):
    a, b, c = dot(v, Y), dot(v, X), dot(X, Y)
    return [a * X[i] + b * Y[i] - c * v[i] for i in range(3)]
def conjv(X): return [x.conjugate() for x in X]


# ------------------------------------------------------------------ unit sources
class UntwistedSource:
    """W72's untwisted forms for every field (the minimal reading) and B1656's twisted coupling vector."""
    def __init__(self, P, round53=False):
        e8 = lambda ser: {(l, Fraction(n8, 8)): a for (l, n8), a in ser.items()}   # the pickle keys exponents in eighths
        self.F32 = [prep(e8(s), round53) for s in P["F32"]]
        self.FM12 = [prep(e8(s), round53) for s in P["FM12"]]
        self.RB = [prep(e8(s), round53) for s in P["E4F"] + [P["fser"]]]
        self.h5, self.h9 = prep(e8(P["h5"]), round53), prep(e8(P["h9"]), round53)
        self.beta = P["beta"]
    def units(self, field, weight, charge, line, N):
        return {"3/2": self.F32, "-1/2": self.FM12, "7/2": self.RB}[weight]
    def higgs(self, weight, charge, line, N):
        return {"5/2": self.h5, "9/2": self.h9}[weight]
    def coupling(self, tau, qL, qR, line, N, d1):
        la, lb = line
        ub = (arb((qL + qR) * lb) / N, arb((qL + qR) * la) / N)
        de = (arb((qL - qR) * lb) / N, arb((qL - qR) * la) / N)
        return [-2 * acb.pi() * x for x in quat3(tau, ub, de, d1)]
    def completion_beta(self, field, charge, line, N):
        return self.beta


# ------------------------------------------------------------------ one configuration: (thread L.R^n with sign, line, N)
def matrix_LRn(n): return 1, n, 1, n + 1


def configuration(src, n, line, N, charges, Npts):
    a, b, c, d = matrix_LRn(n); tr = a + d
    rho = math.sqrt(tr * tr - 4) / 2
    flint.ctx.prec = int(2 * math.pi * 2.0 * rho / math.log(2)) + 260
    x0 = arb(a - d) / 2; rhoA = arb(tr * tr - 4).sqrt() / 2; PlA = 2 * (arb(tr) / 2).acosh()
    # the series each sector needs
    need = {}
    for sec, (fl, fr, hh) in SECTORS.items():
        qL, qR = charges[fl], charges[fr]
        qH = charges["H"] if hh == "H" else -charges["H"]
        need[sec] = {"qL": qL, "qR": qR,
                     "L32": src.units(fl, "3/2", qL, line, N), "LM12": src.units(fl, "-1/2", qL, line, N),
                     "R32": src.units(fr, "3/2", qR, line, N), "R72": src.units(fr, "7/2", qR, line, N),
                     "h5": src.higgs("5/2", qH, line, N), "h9": src.higgs("9/2", qH, line, N),
                     "beta": src.completion_beta(fr, qR, line, N)}
    exps = set()
    for nd in need.values():
        for key in ("L32", "LM12", "R32", "R72"):
            for ser in nd[key]: exps |= set(ser)
        exps |= set(nd["h5"]) | set(nd["h9"])
    acc = {sec: {} for sec in SECTORS}
    first, last = {}, {}
    def point(tau, store):
        y = tau.imag
        pw = {e: (2 * acb.pi() * acb(0, 1) * tau * arb(e.numerator) / e.denominator).exp() for e in exps}
        d1 = th1p(tau)
        yp = {k: y ** k for k in (1.5, -0.5, 3.5, 2.5, 4.5)}
        for sec, nd in need.items():
            L32 = [ev(f, pw) for f in nd["L32"]]; LM = [ev(f, pw) for f in nd["LM12"]]
            R32 = [ev(f, pw) for f in nd["R32"]]; R72 = [ev(f, pw) for f in nd["R72"]]
            h5c, h9c = conjv(ev(nd["h5"], pw)), conjv(ev(nd["h9"], pw))
            v = src.coupling(tau, nd["qL"], nd["qR"], line, N, d1)
            vals = {
                "KL32": [[dot(L32[i], conjv(L32[k])) * yp[1.5] for k in range(3)] for i in range(3)],
                "KR32": [[dot(R32[i], conjv(R32[k])) * yp[1.5] for k in range(3)] for i in range(3)],
                "KLM12": [[dot(LM[i], conjv(LM[k])) * yp[-0.5] for k in range(3)] for i in range(3)],
                "KR72": [[dot(R72[i], conjv(R72[k])) * yp[3.5] for k in range(4)] for i in range(4)],
                "Y1": [[dot(Gp(L32[i], R32[k], v), h5c) * yp[2.5] for k in range(3)] for i in range(3)],
                "Y2x": [[dot(Gp(L32[i], R72[k], v), h9c) * yp[4.5] for k in range(4)] for i in range(3)],
                "Y3x": [[dot(Gp(LM[i], R72[k], v), h5c) * yp[2.5] for k in range(4)] for i in range(3)]}
            store(sec, vals)
    def add(sec, vals):
        A = acc[sec]
        for key, Mv in vals.items():
            if key not in A: A[key] = [[acb(0)] * len(Mv[0]) for _ in Mv]
            for i in range(len(Mv)):
                for k in range(len(Mv[0])): A[key][i][k] += Mv[i][k]
        if sec not in first: first[sec] = vals
    for j in range(Npts):
        s = -PlA / 2 + PlA * j / Npts
        point(x0 + rhoA * acb(s.tanh(), 1 / s.cosh()), add)
    s = PlA / 2
    point(x0 + rhoA * acb(s.tanh(), 1 / s.cosh()), lambda sec, vals: last.__setitem__(sec, vals))
    clos = {}
    for sec in SECTORS:
        worst = 0.0
        for key in ("Y1", "Y2x", "Y3x"):
            A0, A1 = first[sec][key], last[sec][key]
            num = max(float(abs(A1[i][k] - A0[i][k]).mid()) for i in range(len(A0)) for k in range(len(A0[0])))
            den = max(float(abs(A0[i][k]).mid()) for i in range(len(A0)) for k in range(len(A0[0])))
            worst = max(worst, num / den)
        clos[sec] = worst
    w = PlA / Npts
    for sec in SECTORS:
        for key in acc[sec]: acc[sec][key] = [[x * w for x in row] for row in acc[sec][key]]
    return {"rho": rho, "bits": flint.ctx.prec, "closure": clos, "acc": acc, "beta": {s: need[s]["beta"] for s in need}}


# ------------------------------------------------------------------ cells (as the instruments), in mpmath
def to_mp(Mx):
    nd = mp.mp.dps + 10
    return mp.matrix([[mp.mpc(mp.mpf(x.real.mid().str(nd, radius=False)), mp.mpf(x.imag.mid().str(nd, radius=False)))
                       for x in row] for row in Mx])
def inv_sqrt(K):
    E_, U = mp.eighe(K); ev_ = [E_[i] for i in range(E_.rows)]
    if min(ev_) <= 0: return None
    return U * mp.diag([e ** -0.5 for e in ev_]) * U.transpose_conj()
CELLS = [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"), ("C3", "ORTH")]
def cells(acc, beta):
    res = {}
    for cell, comp in CELLS:
        name = cell if comp is None else f"{cell}/{comp}"
        if cell == "C1":
            KL, Y, KR = to_mp(acc["KL32"]), to_mp(acc["Y1"]), to_mp(acc["KR32"])
        else:
            if comp == "THETA2" and beta is None: res[name] = None; continue
            Kx = to_mp(acc["KR72"])
            cc = [0, 0, 0] if comp == "E4" else ([mp.mpc(b_) for b_ in beta] if comp == "THETA2"
                                                 else [-Kx[i, 3] / Kx[3, 3] for i in range(3)])
            P3 = mp.matrix(3, 4)
            for i in range(3): P3[i, i] = 1; P3[i, 3] = cc[i]
            KR = P3 * Kx * P3.transpose_conj()
            KL, Y = (to_mp(acc["KL32"]), to_mp(acc["Y2x"]) * P3.T) if cell == "C2" else (to_mp(acc["KLM12"]), to_mp(acc["Y3x"]) * P3.T)
        A_, B_ = inv_sqrt(KL), inv_sqrt(KR)
        if A_ is None or B_ is None: res[name] = None; continue
        Mx = A_ * Y * B_.T
        U, S, V = mp.svd_c(Mx)
        o = sorted(range(S.rows), key=lambda i: -abs(S[i]))
        res[name] = {"s": [abs(S[i]) for i in o], "UL": [[U[r, i] for i in o] for r in range(U.rows)], "A": A_}
    return res


def run(src, n, line, N, charges, Npts, src53=None):
    """one configuration with r_calc: Npts vs 1.25 Npts, and (if given) the 53-bit source"""
    outs = [configuration(src, n, line, N, charges, Npts),
            configuration(src, n, line, N, charges, int(Npts * 1.25) // 4 * 4)]
    if src53 is not None:
        outs.append(configuration(src53, n, line, N, charges, int(Npts * 1.25) // 4 * 4))
    mp.mp.dps = outs[1]["bits"] // 3
    res = {"rho": outs[1]["rho"], "closure": outs[1]["closure"], "sectors": {}}
    for sec in SECTORS:
        cs = [cells(o["acc"][sec], o["beta"][sec]) for o in outs]
        row = {}
        for name in cs[1]:
            if cs[1][name] is None: row[name] = None; continue
            s = cs[1][name]["s"]
            R2, R1 = s[1] / s[0], s[2] / s[0]
            rc = 0.0
            for alt in (cs[0], cs[2] if len(cs) > 2 else None):
                if alt is None or alt[name] is None: continue
                sa = alt[name]["s"]
                rc = max(rc, float(abs(mp.log((sa[1] / sa[0]) / R2))), float(abs(mp.log((sa[2] / sa[0]) / R1))))
            row[name] = {"ln R2": float(mp.log(R2)), "ln R1": float(mp.log(R1)), "r_calc": rc}
        res["sectors"][sec] = row
    return res


if __name__ == "__main__":
    t0 = time.time()
    P = pickle.load(open(sys.argv[1], "rb"))
    REF = json.load(open(sys.argv[2]))
    flint.ctx.prec = 800
    src, src53 = UntwistedSource(P), UntwistedSource(P, round53=True)
    print("sources ready", round(time.time() - t0, 1), flush=True)
    # self-test at excluded orders: untwisted units for every field must reproduce deep_cusp (same field both sides)
    worst = 0.0
    for n, N, npts in ((9, 3, 448), (25, 5, 952)):
        r = run(src, n, (0, 1), N, SM, npts, src53)
        key = "L" + "R" * n + f" N={N}"
        for sec in ("up", "down", "lepton"):
            for name, d in r["sectors"][sec].items():
                ref = REF[key][sec]["cells"][name]
                if d is None or ref is None or ref["conv (ln, Npts vs 0.8 Npts)"] > 1e-20: continue   # rank-two noise
                dv = max(abs(d["ln R2"] - ref["ln s2/s1"]), abs(d["ln R1"] - ref["ln s3/s1"]))
                worst = max(worst, dv)
            print(f"L.R^{n} N={N} {sec}: closure {r['closure'][sec]:.1e}  C1 ln R2 {r['sectors'][sec]['C1']['ln R2']:.6f}"
                  f"  r_calc(C1) {r['sectors'][sec]['C1']['r_calc']:.1e}", flush=True)
    print("worst |difference| from deep_cusp_deep.json in ln R2, ln R1 (rank-three cells):", worst)
    print("seconds", round(time.time() - t0, 1))
