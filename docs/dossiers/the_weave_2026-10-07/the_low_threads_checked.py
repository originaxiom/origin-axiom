"""W97: the blind check of chat1's sealed TWISTED UNITS ON THE LOW THREADS (chat1/web-seat 0d83e6981), on this seat's
own instrument, before reading chat1's run. The rule (W97_RULE.md) was committed before this script.

Scope: the per-field reading, cell C1 = (3/2, 3/2) h5, the Standard Model's 6Y charges, all T-low configurations.

  Q1  this seat's enumeration of T-low against chat1's tlow_configurations.json (pre-seal file, read from git)
  Q2  closure of every integrand (K_L, K_R, Y; three sectors) between a point and its image under the word, 1e-20
  Q3  convergence: ln(m1/m3), ln(m2/m3) between floor(30 P) and floor(37.5 P) nodes, below 1e-6
  Q4  no zero mass: m1 > 1e-30 m3 in every sector of every configuration
  Q5  (evaluated later, after both outputs are committed) agreement with chat1's run to 1e-6
  read-outs: the Standard Model's S-mass under W66's predicate (a = 0.10) per configuration; W94's ratio

The instrument:
  - W72's units (F_i, F+, F- at 3/2; R at -1/2; h5 at 5/2) rebuilt by the_per_field_units.build_units and evaluated
    by their series only in the standard fundamental domain;
  - each point of the thread reduced by tau -> tau - n and tau -> -1/tau; each unit carried back with its own fitted
    matrices: F(tau + 1) = M_T F(tau), F(-1/tau) = sqrt(tau)^(2k) M_S F(tau) (principal root), fitted on the unit arc;
  - the dressing D_c(q) = [theta[a_s + al, b_s + be](0) e^(-2 pi i al b_s)]^2 / theta[a_s, b_s](0)^2 at the unreduced
    point by explicit sums, (al, be) = (q lb / N, q la / N), s = (2, 4, 3) on (i, j, k);
  - the path: the axis of the word's own matrix, one period, the line as listed (no carrying); trapezoid in arclength
    with nodes at half steps; 60 digits;
  - masses: singular values of K_L^(-1/2) Y (K_R^(-1/2))^T, ascending.

Run: python3 the_low_threads_checked.py  ->  the_low_threads_checked.json beside it (4 processes).
"""
import json
import math
import multiprocessing as mpr
import subprocess
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(HERE))
OUT = HERE / "the_low_threads_checked.json"
HZ = HERE / "received" / "HZ2021_running_masses_MZ.json"
CHAT1_SEAL = "0d83e6981"
CHAT1_CONF = "relays/chat1_2026-10-15_route/twisted_units/tlow_configurations.json"
DPS = 60
NAMES = ("F0", "F1", "F2", "R", "h5")
WEIGHT = {"F0": Fr(3, 2), "F1": Fr(3, 2), "F2": Fr(3, 2), "R": Fr(-1, 2), "h5": Fr(5, 2)}
COMP_S = (2, 4, 3)
CH = {2: (Fr(1, 2), Fr(0)), 4: (Fr(0), Fr(1, 2)), 3: (Fr(0), Fr(0))}
SECT = {"up": (1, -4, 3), "down": (1, 2, -3), "lepton": (-3, 6, -3)}
CHARGES = (1, -4, 2, -3, 6, 3)


# ------------------------------------------------------------------------------------------------ Q1
def mat(w):
    A, B, C, D = 1, 0, 0, 1
    for ch in w:
        if ch == "L":
            A, B, C, D = A + B, B, C + D, D
        else:
            A, B, C, D = A, A + B, C, C + D
    return A, B, C, D


def lyndon_words(nmax):
    """Lyndon words in L < R by brute force: strictly smaller than every proper rotation"""
    out = []
    for n in range(2, nmax + 1):
        for k in range(1 << n):
            w = "".join("R" if (k >> (n - 1 - i)) & 1 else "L" for i in range(n))
            if all(w < w[i:] + w[:i] for i in range(1, n)):
                out.append(w)
    return out


def height(w):
    best = None
    for i in range(len(w)):
        A, B, C, D = mat(w[i:] + w[:i])
        m = min(abs(B), abs(C))
        if best is None or m < best[0]:
            best = (m, A + D)
    c, t = best
    return math.sqrt(t * t - 4) / (2 * c)


def enumerate_tlow():
    words = [w for w in lyndon_words(12) if "L" in w and "R" in w and height(w) <= 3.0]
    out = {}
    for N in (9, 11, 12):
        rows = []
        for w in words:
            A, B, C, D = mat(w)
            seen = set()
            for la in range(N):
                for lb in range(N):
                    if math.gcd(math.gcd(la, lb), N) != 1:
                        continue
                    key = min((la, lb), ((-la) % N, (-lb) % N))
                    if key in seen:
                        continue
                    seen.add(key)
                    img = ((la * D + lb * B) % N, (la * C + lb * A) % N)
                    if img not in ((la % N, lb % N), ((-la) % N, (-lb) % N)):
                        continue
                    if (C * la * la + (A - D) * la * lb - B * lb * lb) % (N * N) == 0:
                        rows.append((w, key))
        out[N] = rows
    return out


def chat1_configurations():
    raw = subprocess.run(["git", "show", f"{CHAT1_SEAL}:{CHAT1_CONF}"], cwd=REPO, capture_output=True, text=True,
                         check=True).stdout
    d = json.loads(raw)
    return {int(N): [(r[0], tuple(r[2])) for r in rows] for N, rows in d.items()}


# ------------------------------------------------------------------------------------------------ units and transport
def fr(x):
    return mp.mpf(x.numerator) / x.denominator


class Units:
    def __init__(self):
        import the_per_field_units as PF
        mp.mp.dps = 40
        U = PF.build_units()
        mp.mp.dps = DPS
        self.resid = {k: float(v) for k, v in U["resid"].items()}
        src = {"F0": U["F32"][0], "F1": U["F32"][1], "F2": U["F32"][2], "R": U["FM12"][1], "h5": U["h5"]}
        self.U = {n: {e: v for e, v in PF.to_comp(s).items()} for n, s in src.items()}
        self.MT, self.MS, self.fitres = {}, {}, {}
        for n in NAMES:
            for step in ("T", "S"):
                M, res = self.fit(n, step)
                (self.MT if step == "T" else self.MS)[n] = M
                self.fitres[f"{n} {step}"] = float(res)
        self.MSinv = {n: self.MS[n] ** -1 for n in NAMES}

    def ev(self, n, t):
        out = [mp.mpc(0)] * 3
        for e, v in self.U[n].items():
            z = mp.exp(2j * mp.pi * fr(e) * t)
            out = [out[k] + v[k] * z for k in range(3)]
        return out

    def fit(self, n, step):
        k = WEIGHT[n]
        pts = [r * mp.expjpi(mp.mpf(th) / 180) for r, th in ((1, 68), (1, 79), (1, 93), (1, 107), (1.03, 84),
                                                              (0.98, 99), (1.02, 112), (0.99, 72))]
        X, Bv = [], []
        for t in pts:
            g, fac = (t + 1, mp.mpf(1)) if step == "T" else (-1 / t, mp.sqrt(t) ** (2 * fr(k)))
            X.append(self.ev(n, t))
            Bv.append([x / fac for x in self.ev(n, g)])
        A = mp.matrix(X)
        M = mp.zeros(3, 3)
        worst = mp.mpf(0)
        for r in range(3):
            b = mp.matrix([row[r] for row in Bv])
            sol = mp.lu_solve(A.H * A, A.H * b)
            for c in range(3):
                M[r, c] = sol[c]
            worst = max(worst, mp.norm(A * sol - b) / mp.norm(b))
        return M, worst

    def at(self, t):
        steps, u = [], t
        for _ in range(10000):
            n = int(mp.nint(u.real))
            if n:
                u = u - n
                steps.append(("T", n))
            if abs(u) < 1 - mp.mpf(10) ** -40:
                steps.append(("S", u))
                u = -1 / u
            else:
                break
        out = {}
        for n in NAMES:
            v = mp.matrix(self.ev(n, u))
            k2 = 2 * fr(WEIGHT[n])
            for kind, val in reversed(steps):
                v = (self.MT[n] ** val) * v if kind == "T" else self.MSinv[n] * v / mp.sqrt(val) ** k2
            out[n] = [v[i] for i in range(3)]
        return out


def theta_char(a, b, t):
    M = int(math.sqrt((DPS + 10) * math.log(10) / (math.pi * float(t.imag)))) + 4 + int(abs(a))
    n0 = -int(mp.floor(a))
    return mp.fsum(mp.exp(1j * mp.pi * ((n + a) ** 2 * t + 2 * (n + a) * b)) for n in range(n0 - M, n0 + M + 1))


def dressings(line, N, t):
    la, lb = line
    base = [theta_char(fr(CH[s][0]), fr(CH[s][1]), t) ** 2 for s in COMP_S]
    out = {}
    for q in CHARGES:
        al, be = Fr(q * lb, N), Fr(q * la, N)
        row = []
        for c, s in enumerate(COMP_S):
            a_s, b_s = CH[s]
            num = theta_char(fr(a_s + al), fr(b_s + be), t) * mp.expjpi(-2 * fr(al * b_s))
            row.append(num ** 2 / base[c])
        out[q] = row
    return out


def dot(X, Y):
    return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]


def Gp(X, Y, v):
    a, b, c = dot(v, Y), dot(v, X), dot(X, Y)
    return [a * X[i] + b * Y[i] - c * v[i] for i in range(3)]


def integrands(UN, line, N, t):
    vals = UN.at(t)
    D = dressings(line, N, t)
    y = t.imag
    cj = lambda X: [mp.conj(x) for x in X]
    F = [vals["F0"], vals["F1"], vals["F2"]]
    out = {}
    for sec, (qL, qR, qH) in SECT.items():
        L = [[f[c] * D[qL][c] for c in range(3)] for f in F]
        Rr = [[f[c] * D[qR][c] for c in range(3)] for f in F]
        h = [mp.conj(vals["h5"][c] * D[qH][c]) for c in range(3)]
        KL = [[dot(L[i], cj(L[k])) * y ** mp.mpf(1.5) for k in range(3)] for i in range(3)]
        KR = [[dot(Rr[i], cj(Rr[k])) * y ** mp.mpf(1.5) for k in range(3)] for i in range(3)]
        Y = [[dot(Gp(L[i], Rr[k], vals["R"]), h) * y ** mp.mpf(2.5) for k in range(3)] for i in range(3)]
        out[sec] = (KL, KR, Y)
    return out


def geometry(word):
    A, B, C, D = mat(word)
    tr = A + D
    x0 = mp.mpf(A - D) / (2 * C)
    rho = mp.sqrt(tr * tr - 4) / (2 * abs(C))
    P = 2 * mp.acosh(mp.mpf(tr) / 2)
    return (lambda s: x0 + rho * (mp.tanh(s) + 1j / mp.cosh(s))), (lambda t: (A * t + B) / (C * t + D)), P


def masses_of(acc):
    def isqrt(K):
        K = (K + K.H) / 2
        ev, Uh = mp.eighe(K)
        return Uh * mp.diag([1 / mp.sqrt(x) for x in ev]) * Uh.H, min(ev)
    out = {}
    for sec, (KL, KR, Y) in acc.items():
        IL, eL = isqrt(KL)
        IR, eR = isqrt(KR)
        sv = sorted(abs(x) for x in mp.svd_c(IL * Y * IR.T, compute_uv=False))
        out[sec] = {"s": sv, "posdef": bool(eL > 0 and eR > 0)}
    return out


UN = None


def one_configuration(args):
    N, word, line = args
    mp.mp.dps = DPS
    t0 = time.time()
    tau, g, P = geometry(word)
    row = {"N": N, "word": word, "line": list(line), "period": float(P),
           "|g tau(-P/2) - tau(P/2)|": float(abs(g(tau(-P / 2)) - tau(P / 2)))}
    s0 = -P / 2 + mp.mpf("0.137")
    I0, I1 = integrands(UN, line, N, tau(s0)), integrands(UN, line, N, g(tau(s0)))
    clo = mp.mpf(0)
    for sec in SECT:
        for a in range(3):
            A0, A1 = I0[sec][a], I1[sec][a]
            den = max(abs(x) for r in A0 for x in r)
            clo = max(clo, max(abs(A1[i][k] - A0[i][k]) for i in range(3) for k in range(3)) / den)
    row["closure"] = float(clo)
    res = {}
    for label, npts in (("n1", int(30 * P)), ("n2", int(37.5 * P))):
        acc = {s: [mp.zeros(3, 3), mp.zeros(3, 3), mp.zeros(3, 3)] for s in SECT}
        for j in range(npts):
            I = integrands(UN, line, N, tau(-P / 2 + (j + mp.mpf(1) / 2) * P / npts))
            for sec in SECT:
                for a in range(3):
                    for i in range(3):
                        for k in range(3):
                            acc[sec][a][i, k] += I[sec][a][i][k]
        res[label] = (npts, masses_of(acc))
    row["npts"] = [res["n1"][0], res["n2"][0]]
    row["sectors"] = {}
    for sec in SECT:
        s1, s2 = res["n1"][1][sec]["s"], res["n2"][1][sec]["s"]
        l1 = [mp.log(s2[0] / s2[2]), mp.log(s2[1] / s2[2])]
        l0 = [mp.log(s1[0] / s1[2]), mp.log(s1[1] / s1[2])]
        row["sectors"][sec] = {"ln m1/m3": mp.nstr(l1[0], 30), "ln m2/m3": mp.nstr(l1[1], 30),
                               "r_calc": float(max(abs(l1[0] - l0[0]), abs(l1[1] - l0[1]))),
                               "m1/m3": float(s2[0] / s2[2]),
                               "posdef": res["n1"][1][sec]["posdef"] and res["n2"][1][sec]["posdef"]}
    row["seconds"] = round(time.time() - t0, 1)
    return row


def score(row):
    hz = json.loads(HZ.read_text(encoding="utf-8"))["masses_GeV"]
    v, sg = hz["value"], hz["sigma"]
    names = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
    z2, zs = 0.0, {}
    for sec, (f1, f2, f3) in names.items():
        S = row["sectors"][sec]
        for lab, fi, key in (("R1", f1, "ln m1/m3"), ("R2", f2, "ln m2/m3")):
            data = math.log(v[fi] / v[f3])
            rd = math.hypot(sg[fi] / v[fi], sg[f3] / v[f3])
            z = (float(S[key]) - data) / math.sqrt(S["r_calc"] ** 2 + rd ** 2 + 0.10 ** 2)
            zs[f"{sec} {lab}"] = z
            z2 += z * z
    w94 = math.exp((float(row["sectors"]["lepton"]["ln m2/m3"]) - float(row["sectors"]["down"]["ln m2/m3"])))
    return {"z": zs, "sum z^2": z2, "passes S-mass": bool(z2 <= 12.592), "W94 ratio": w94}


def main():
    global UN
    t0 = time.time()
    out = {"rule": "W97_RULE.md", "status": "one run", "chat1 seal": CHAT1_SEAL,
           "chat1's output": "not read before this output is committed"}
    mine, theirs = enumerate_tlow(), chat1_configurations()
    q1 = {}
    for N in (9, 11, 12):
        a, b = set(mine[N]), set(theirs[N])
        q1[str(N)] = {"this seat": len(a), "chat1": len(b), "words": len({w for w, _ in a}),
                      "only here": sorted(a - b), "only chat1's": sorted(b - a)}
    out["Q1"] = {"by N": q1, "holds": all(v["only here"] == [] and v["only chat1's"] == [] for v in q1.values())
                 and [q1[str(N)]["this seat"] for N in (9, 11, 12)] == [18, 40, 32]}
    UN = Units()
    out["units"] = {"section residuals": UN.resid, "fit residuals": UN.fitres, "build seconds": round(time.time() - t0)}
    jobs = [(N, w, tuple(l)) for N in (9, 11, 12) for w, l in mine[N]]
    with mpr.get_context("fork").Pool(4) as pool:
        rows = pool.map(one_configuration, jobs, chunksize=1)
    for r in rows:
        r["read-out"] = score(r)
    out["configurations"] = rows
    out["Q2"] = {"max closure": max(r["closure"] for r in rows), "holds": all(r["closure"] < 1e-20 for r in rows)}
    rc = max(s["r_calc"] for r in rows for s in r["sectors"].values())
    out["Q3"] = {"max r_calc": rc, "holds": bool(rc < 1e-6)}
    m13 = min(s["m1/m3"] for r in rows for s in r["sectors"].values())
    pd = all(s["posdef"] for r in rows for s in r["sectors"].values())
    out["Q4"] = {"min m1/m3": m13, "norm matrices positive definite": pd, "holds": bool(m13 > 1e-30 and pd)}
    out["read-outs"] = {"S-mass passes (C1, per-field, SM)": sum(r["read-out"]["passes S-mass"] for r in rows),
                        "by N": {str(N): sum(r["read-out"]["passes S-mass"] for r in rows if r["N"] == N)
                                 for N in (9, 11, 12)},
                        "smallest sum z^2": min(r["read-out"]["sum z^2"] for r in rows)}
    out["seconds"] = round(time.time() - t0)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n")
    print({c: out[c]["holds"] for c in ("Q1", "Q2", "Q3", "Q4")}, out["seconds"], "s")


if __name__ == "__main__":
    main()
