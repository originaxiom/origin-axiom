"""Item 4 of the stage-1 audit report: Rademacher's Psi, Meyer's signature cocycle and the eta invariant on
L^k R L R and L^m R^m. Own code; data-free. Exact rationals (fractions) except the analytic eta-log route (mpmath).

L = [[1,1],[0,1]], R = [[1,0],[1,1]] (the record's convention, checked against B1929's population).
"""
import ast, itertools, json, random, re, sys
from fractions import Fraction as Fr
import mpmath as mp

ROOT = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/"
B1929_POP = ROOT + "frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/verification/received_sm/population.json"
B1737_RUN = ROOT + "frontier/B1737_the_slope_is_a_zeta_value/verification/the_slope_is_a_zeta_value_run.txt"
PLANT = sys.argv[1] if len(sys.argv) > 1 else None
FAILS = []
OUT = {}


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok: FAILS.append(name)
    return ok


def mul(A, B): return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
                       (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))
def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def neg(A): return ((-A[0][0], -A[0][1]), (-A[1][0], -A[1][1]))
I2 = ((1, 0), (0, 1))
Lm, Rm = ((1, 1), (0, 1)), ((1, 0), (1, 1))
if PLANT == "P4d":                        # the transposed convention: L and R swapped
    Lm, Rm = Rm, Lm
LET = {"L": Lm, "R": Rm, "l": inv(Lm), "r": inv(Rm)}
J = ((0, 1), (1, 0))


def word(w):
    M = I2
    for ch in w: M = mul(M, LET[ch])
    return M


def sgn(x): return (x > 0) - (x < 0)
def saw(x):
    x = Fr(x)
    return Fr(0) if x.denominator == 1 else x - (x.numerator // x.denominator) - Fr(1, 2)
def dedekind(h, k):
    assert k > 0
    return sum(saw(Fr(r, k)) * saw(Fr(h * r, k)) for r in range(1, k))


def Phi(A):
    (a, b), (c, d) = A
    if c == 0: return Fr(b, d)
    s = 1 if PLANT == "P4a" else -1       # P4a: the wrong sign on the Dedekind term
    return Fr(a + d, c) + s * 12 * sgn(c) * dedekind(d, abs(c))


def Psi(A):
    (a, b), (c, d) = A
    if PLANT == "P4b": return Phi(A)      # P4b: Phi used in place of Psi
    return Phi(A) - 3 * sgn(c * (a + d))


def eta_bohn(A):
    """the record's untwisted eta of T^2_A (B1929 received_sm/run_c9.py, eta_untw), re-typed: (a+d)/(3c) - 4 sgn(c) s(a,c) - sgn(c(a+d)),
    with run_c9's dedekind(a, c) = sum_{k=1}^{|c|-1} P1(a k/c) P1(k/c) for either sign of c"""
    (a, b), (c, d) = A
    s = sum(saw(Fr(a * k, c)) * saw(Fr(k, c)) for k in range(1, abs(c)))
    return Fr(a + d, 3 * c) - 4 * sgn(c) * s - sgn(c * (a + d))


# ------------------------------------------------------------------ 1. the asked values
res = {"LmRm": {}, "LkRLR": {}}
for m in range(1, 9):
    A = word("L" * m + "R" * m); res["LmRm"][m] = {"M": A, "Phi": str(Phi(A)), "Psi": str(Psi(A))}
for k in range(1, 9):
    A = word("L" * k + "RLR"); res["LkRLR"][k] = {"M": A, "Phi": str(Phi(A)), "Psi": str(Psi(A))}
print("Psi(L^m R^m), m = 1..8:", [res["LmRm"][m]["Psi"] for m in range(1, 9)])
print("Psi(L^k R L R), k = 1..8:", [res["LkRLR"][k]["Psi"] for k in range(1, 9)])
print("Phi(L^k R L R), k = 1..8:", [res["LkRLR"][k]["Phi"] for k in range(1, 9)])
check("E4.1 Psi(L^m R^m) = 0 for m = 1..8", all(Fr(res["LmRm"][m]["Psi"]) == 0 for m in range(1, 9)))
check("E4.1 Psi(L^k R L R) = k - 1 for k = 1..8", all(Fr(res["LkRLR"][k]["Psi"]) == k - 1 for k in range(1, 9)))

# ------------------------------------------------------------------ 2. Psi = #L - #R on every positive hyperbolic word up to length 10
bad = 0; n = 0
for length in range(2, 11):
    for w in itertools.product("LR", repeat=length):
        if "L" in w and "R" in w:
            n += 1
            if Psi(word(w)) != w.count("L") - w.count("R"): bad += 1
check("E4.1 Psi = #L - #R on all %d positive words with both letters, length <= 10" % n, bad == 0, "mismatches %d" % bad)

# ------------------------------------------------------------------ 3. class function and the orientation swap
rnd = random.Random(20261114)
cls_bad = 0; trials = 0
for k in list(range(1, 6)):
    A = word("L" * k + "RLR")
    for _ in range(40):
        B = word("".join(rnd.choice("LRlr") for _ in range(rnd.randint(1, 8))))
        trials += 1
        if Psi(mul(mul(B, A), inv(B))) != Psi(A): cls_bad += 1
check("E4.3 Psi(B A B^-1) = Psi(A) on %d random conjugates of L^k R L R" % trials, cls_bad == 0, "mismatches %d" % cls_bad)
phi_moves = sum(1 for k in range(1, 6) for B in (Lm, Rm, mul(Lm, Rm)) if Phi(mul(mul(B, word("L" * k + "RLR")), inv(B))) != Phi(word("L" * k + "RLR")))
print("  (Phi itself changes under conjugation in %d of 15 cases)" % phi_moves)
sw = all(Psi(mul(mul(J, word(w)), J)) == -Psi(word(w)) for w in ["L" * k + "RLR" for k in range(1, 7)] + ["L" * m + "R" * m for m in range(1, 7)] + ["LLLRRLR", "LRRRLLLR"])
check("E4.4 Psi(J A J) = -Psi(A) (J the orientation-reversing swap)", sw)
amph = all(mul(mul(J, word("L" * m + "R" * m)), J) == word("R" * m + "L" * m) for m in range(1, 7))
check("E4.4 J L^m R^m J = R^m L^m, a cyclic rotation (conjugate) of L^m R^m: amphichiral, so Psi = 0 is forced", amph)

# ------------------------------------------------------------------ 4. the analytic route: Phi from log eta (Rademacher's transformation law)
mp.mp.dps = 30
def logeta(t):
    q = mp.exp(2j * mp.pi * t)
    N = int(30 * 2.4 / (2 * mp.pi * mp.im(t))) + 20
    return mp.pi * 1j * t / 12 + mp.fsum(mp.log(1 - q ** n) for n in range(1, N))
def Phi_analytic(A, t):
    (a, b), (c, d) = A
    if c < 0: (a, b), (c, d) = neg(A)
    At = (a * t + b) / (c * t + d)
    val = (logeta(At) - logeta(t) - mp.log(-1j * (c * t + d)) / 2) * 12 / (mp.pi * 1j)
    return val
worst = mp.mpf(0); worst_geo = mp.mpf(0); rows = []
tests = [word("L" * k + "RLR") for k in range(1, 7)] + [word("L" * m + "R" * m) for m in range(1, 7)] + [word("LR"), word("R"), word("LLR")]
for A in tests:
    v = Phi_analytic(A, mp.mpc(0.1, 0.9))
    worst = max(worst, abs(v - Phi(A)))
    # on the act's geodesic: the point symmetric to its image about the top
    (a, b), (c, d) = A
    tr = a + d
    if abs(tr) > 2:
        D = tr * tr - 4
        r1 = ((a - d) + mp.sqrt(D)) / (2 * c); r2 = ((a - d) - mp.sqrt(D)) / (2 * c)
        cen, Rr = (r1 + r2) / 2, abs(r1 - r2) / 2
        ell = 2 * mp.log((abs(tr) + mp.sqrt(D)) / 2)
        z = lambda s: mp.mpc(cen + Rr * mp.tanh(s), Rr / mp.cosh(s))
        z0 = z(-ell / 2) if abs((a * z(-ell / 2) + b) / (c * z(-ell / 2) + d) - z(ell / 2)) < 1e-20 else z(ell / 2)
        vg = Phi_analytic(A, z0)
        worst_geo = max(worst_geo, abs(vg - Phi(A)))
check("E4.2 Phi from log eta equals the exact Dedekind-sum Phi at a generic point (worst %.1e)" % worst + (" [PLANT P4a]" if PLANT == "P4a" else ""), worst < 1e-20)
check("E4.2 the same on each act's own geodesic (worst %.1e)" % worst_geo, worst_geo < 1e-20)

# ------------------------------------------------------------------ 5. Meyer's signature cocycle, from its definition, exact
def nullspace(rows_, ncols):
    """exact nullspace basis of a rational matrix given as a list of rows"""
    M = [[Fr(x) for x in r] for r in rows_]; piv = []; r = 0
    for col in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        M[r] = [x / M[r][col] for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                f = M[i][col]; M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(col); r += 1
        if r == len(M): break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fr(0)] * ncols; v[fcol] = Fr(1)
        for i, pc in enumerate(piv): v[pc] = -M[i][fcol]
        basis.append(v)
    return basis


def signature(G):
    G = [row[:] for row in G]; n = len(G); pos = neg_ = 0
    while n:
        i = next((i for i in range(n) if G[i][i] != 0), None)
        if i is None:
            pr = next(((i, j) for i in range(n) for j in range(n) if G[i][j] != 0), None)
            if pr is None: break
            i, j = pr                     # congruence: row/col i += row/col j makes the diagonal 2 G[i][j] != 0
            for k in range(n): G[i][k] += G[j][k]
            for k in range(n): G[k][i] += G[k][j]
            continue
        p = G[i][i]
        if p > 0: pos += 1
        else: neg_ += 1
        for a in range(n):
            if a != i:
                f = G[a][i] / p
                for b in range(n): G[a][b] -= f * G[i][b]
        for a in range(n):
            if a != i: G[i][a] = Fr(0); G[a][i] = Fr(0)
        idx = [k for k in range(n) if k != i]
        G = [[G[a][b] for b in idx] for a in idx]; n -= 1
    return pos - neg_


def omega(u, v): return u[0] * v[1] - u[1] * v[0]
ASYM = [0]
def meyer_tau(A, B):
    Ai = inv(A)
    rows_ = [[Ai[0][0] - 1, Ai[0][1], B[0][0] - 1, B[0][1]], [Ai[1][0], Ai[1][1] - 1, B[1][0], B[1][1] - 1]]
    basis = nullspace(rows_, 4)
    s = 1 if PLANT == "P4c" else -1      # P4c: (I + B) in place of (I - B)
    def form(v1, v2):
        x1, y1 = v1[:2], v1[2:]; y2 = v2[2:]
        w = ((y2[0] + s * (B[0][0] * y2[0] + B[0][1] * y2[1])), (y2[1] + s * (B[1][0] * y2[0] + B[1][1] * y2[1])))
        return omega((x1[0] + y1[0], x1[1] + y1[1]), w)
    G = [[form(u, v) for v in basis] for u in basis]
    if any(G[i][j] != G[j][i] for i in range(len(G)) for j in range(len(G))): ASYM[0] += 1
    Gs = [[(G[i][j] + G[j][i]) / 2 for j in range(len(G))] for i in range(len(G))]
    return signature(Gs)


def make_phi(eps):
    def phi_word(w, base):
        M = I2; tot = Fr(0)
        for ch in w:                      # phi(M g) = phi(M) + phi(g) + eps tau(M, g); tau(I, g) = 0 for the true form
            tot += eps * meyer_tau(M, LET[ch]) + base[ch]; M = mul(M, LET[ch])
        return tot
    # base values: phi(L) = x, phi(R) = y, phi(l) = -x - eps tau(L, l), phi(r) = -y - eps tau(R, r)
    def base_of(x, y):
        return {"L": x, "R": y, "l": -x - eps * meyer_tau(Lm, inv(Lm)), "r": -y - eps * meyer_tau(Rm, inv(Rm))}
    # phi is affine in (x, y) along any word: solve phi((L r)^6) = 0 and phi((L r L)^4) = 0
    def lin(w):
        c0 = phi_word(w, base_of(Fr(0), Fr(0))); cx = phi_word(w, base_of(Fr(1), Fr(0))) - c0; cy = phi_word(w, base_of(Fr(0), Fr(1))) - c0
        return cx, cy, c0
    a1, b1, c1 = lin("Lr" * 6); a2, b2, c2 = lin("LrL" * 4)
    det = a1 * b2 - a2 * b1
    x = (-c1 * b2 + c2 * b1) / det; y = (-a1 * c2 + a2 * c1) / det
    base = base_of(x, y)
    return (lambda w: phi_word(w, base)), base


assert word("Lr" * 6) == I2 and word("LrL" * 4) == I2
mey = {}
for eps in (1, -1):
    phi, base = make_phi(eps)
    rel = [phi("LrL" + "RlR"), phi("LrL" * 2 + "R"), phi("lRl" * 4), phi("rL" * 6)]     # LrL (rLr)^-1 = I; (LrL)^2 = -I vs ...; more words equal to I
    # (LrL)^2 R = -R: compare with phi(-R) through another word: (rLr)^2 R
    rel_ok = rel[0] == 0 and rel[2] == 0 and rel[3] == 0 and phi("LrL" * 2 + "R") == phi("rLr" * 2 + "R")
    cls_ok = all(phi(b + "L" * k + "RLR" + "".join(c.swapcase() for c in reversed(b))) == phi("L" * k + "RLR") for k in range(1, 5) for b in ("L", "R", "LR", "rl", "LLr"))
    vals_k = {k: phi("L" * k + "RLR") for k in range(1, 9)}; vals_m = {m: phi("L" * m + "R" * m) for m in range(1, 9)}
    ratio = sorted({str(vals_k[k] / Psi(word("L" * k + "RLR"))) for k in range(2, 9)})
    mey[eps] = {"phi_L": str(base["L"]), "phi_R": str(base["R"]), "relations_hold": rel_ok, "class_function": cls_ok,
                "phi(L^k R L R)": {k: str(v) for k, v in vals_k.items()}, "phi(L^m R^m)": {m: str(v) for m, v in vals_m.items()},
                "phi / Psi on L^k R L R (k >= 2)": ratio,
                "phi = -Psi/3 on all": all(vals_k[k] == -Psi(word("L" * k + "RLR")) / 3 for k in vals_k) and all(vals_m[m] == -Psi(word("L" * m + "R" * m)) / 3 for m in vals_m)}
    print("Meyer eps = %+d: phi(L) = %s, phi(R) = %s; relations hold: %s; class function: %s; phi(L^k R L R), k = 1..8: %s; phi(L^m R^m): %s; phi/Psi = %s" % (
        eps, base["L"], base["R"], rel_ok, cls_ok, [str(vals_k[k]) for k in range(1, 9)], [str(vals_m[m]) for m in range(1, 9)], ratio))
tag = " [PLANT P4c]" if PLANT == "P4c" else ""
check("E4.5 Meyer's form is symmetric on every V_{A,B} met%s" % tag, ASYM[0] == 0, "asymmetric forms met: %d" % ASYM[0])
check("E4.5 Meyer's phi is consistent: words equal to I give 0, two words for -R agree, phi is a class function (both eps)%s" % tag,
      all(mey[e]["relations_hold"] and mey[e]["class_function"] for e in (1, -1)))
check("E4.5 phi = -Psi/3 on L^k R L R and L^m R^m for exactly one eps", sum(mey[e]["phi = -Psi/3 on all"] for e in (1, -1)) == 1,
      "eps with phi = -Psi/3: %s" % [e for e in (1, -1) if mey[e]["phi = -Psi/3 on all"]])
OUT["meyer"] = mey

# ------------------------------------------------------------------ 6. the record: B1929's acts and Bohn's eta; B1737's Psi table
pop = json.load(open(B1929_POP))
acts = {}
for o in pop: acts[(o["level"][0], o["level"][1])] = tuple(tuple(r) for r in o["M"])
def from_name(name, lev):
    sign, w = name[0], name[1:]
    A = word(w * lev)
    if sign == "-" and lev % 2 == 1: A = neg(A)
    return A
conv = all(from_name(n, l) == M for (n, l), M in acts.items())
check("record convention: every act of B1929's population is its named word with L = [[1,1],[0,1]], R = [[1,0],[1,1]]" + (" [PLANT P4d]" if PLANT == "P4d" else ""), conv)
bohn = {"%s %d" % k: (str(eta_bohn(M)), str(Psi(M) / 3)) for k, M in sorted(acts.items())}
check("E4.6 the record's Bohn eta(T^2_M) = Psi(M)/3 on all %d acts of B1929's population" % len(acts), all(a == b for a, b in bohn.values()), json.dumps(bohn))
rec = []
for line in open(B1737_RUN):
    mm = re.match(r"^(\[.*?\]) (\d+) (\[\[.*?\]\]) (\S+) (\S+)$", line.strip())
    if mm:
        lev = ast.literal_eval(mm.group(1)); rec.append((lev[0], lev[1], float(mm.group(4)), float(mm.group(5))))
mis = [(n, l, z, p, float(-Psi(from_name(n, l)) / 12)) for n, l, z, p in rec if abs(p - float(-Psi(from_name(n, l)) / 12)) > 1e-9 or abs(z - float(-Psi(from_name(n, l)) / 12)) > 1e-9]
check("E4.6 my Psi from the word names reproduces B1737's recorded -Psi/12 and its independent Shintani zeta(0) on all %d levels" % len(rec) + (" [PLANT P4d]" if PLANT == "P4d" else ""),
      len(rec) == 16 and not mis, "mismatches: %s" % mis[:4])
OUT["values"] = res; OUT["bohn"] = bohn
print("RESULT", json.dumps(OUT, default=str))
print("FAILED CHECKS:", FAILS if FAILS else "none")
