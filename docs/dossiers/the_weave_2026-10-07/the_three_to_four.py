#!/usr/bin/env python3
"""W120 — from three dimensions to four (the script; `W120_RULE.md` was committed and pushed before it).

Part A, the cone, the thread as space:
- A1, A2 (exact, sympy): the Ricci tensor of -dt^2 + a(t)^2 g for g of constant curvature.
- A3 to A5 (SnapPy): every primitive cyclic word in L and R with both letters, length 2 to 10, both signs; volumes.
Part B, the fibre, the records' torus inside four dimensions:
- B1 (exact, sympy): the Euclidean metric e^phi |dz|^2 + (1/Im tau)|dx + tau dy|^2.
- B2 (40 digits): Im tau |eta(tau)|^4 under the moves.
- B3: the exponent of |eta|^4 at a pinched record, and Gauss-Bonnet's counts.
- B4 (exact): the abelianization SL(2, Z) -> Z/12.
- B5 (exact): the units on the closed solutions.

    python3 -B the_three_to_four.py      # writes the_three_to_four.json and the_three_to_four_run.txt beside itself
"""
import json, random
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
out, log = {"arc": "W120", "rule": "W120_RULE.md"}, []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    log.append(s)


def ricci(g, X):
    """the Ricci tensor R_bc = d_a G^a_bc - d_c G^a_ba + G^a_ad G^d_bc - G^a_cd G^d_ba"""
    n = len(X)
    gi = sp.simplify(g.inv())
    G = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(b, n):
            e = sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                    + sum(G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a] for d in range(n)) for a in range(n))
            R[b, c] = R[c, b] = sp.simplify(e)
    return R


def is_zero(M):
    return all(sp.simplify(sp.expand_trig(sp.simplify(M[i, j]))) == 0 for i in range(M.rows) for j in range(M.cols))


# ---------------- A1: the cone and its two curved siblings over the curvature -1 metric ----------------
t, x, y, z = sp.symbols("t x y z", positive=True)
X4 = (t, x, y, z)
A1 = {}
for name, a, lam in (("a = t", t, 0), ("a = sinh t", sp.sinh(t), 3), ("a = sin t", sp.sin(t), -3)):
    g = sp.diag(-1, a ** 2 / z ** 2, a ** 2 / z ** 2, a ** 2 / z ** 2)
    R = ricci(g, X4)
    ok = is_zero(R - lam * g)
    A1[name] = {"Ric = lambda g with lambda": lam, "holds": ok}
    say("A1", name, ": Ric =", lam, "g ->", ok)
out["A1"] = A1

# ---------------- A2: the cone over g_kappa (Ric = 2 kappa g) is Ricci-flat iff kappa = -1 ----------------
kap = sp.symbols("kappa", real=True)
xr, yr, zr = sp.symbols("x y z", real=True)
f = (1 + kap * (xr ** 2 + yr ** 2 + zr ** 2) / 4) ** 2
g3 = sp.eye(3) / f
R3 = ricci(g3, (xr, yr, zr))
einstein3 = is_zero(R3 - 2 * kap * g3)
g4 = sp.diag(-1, t ** 2 / f, t ** 2 / f, t ** 2 / f)
R4 = ricci(g4, (t, xr, yr, zr))
flat_at_m1 = is_zero(R4.subs(kap, -1))
mult = all(sp.simplify(sp.cancel(R4[i, j] / (kap + 1)).subs(kap, -1)).is_finite is not False
           and sp.simplify(sp.cancel(R4[i, j] / (kap + 1))).has(sp.zoo, sp.nan) is False
           for i in range(4) for j in range(4))
nonflat = {str(k0): not is_zero(R4.subs(kap, k0)) for k0 in (0, 1, -2)}
sample = sp.factor(sp.simplify(R4[1, 1]))
out["A2"] = {"g_kappa is Einstein with Ric = 2 kappa g": einstein3, "cone Ricci-flat at kappa = -1": flat_at_m1,
             "every component a multiple of kappa + 1": mult, "not flat at kappa": nonflat, "R_xx": str(sample)}
say("A2 g_kappa Einstein:", einstein3, "| cone flat at kappa = -1:", flat_at_m1, "| multiples of kappa + 1:", mult,
    "| not flat at 0, 1, -2:", nonflat, "| R_xx =", sample)

# ---------------- A3-A5: the census of every thread to length 10 ----------------
import snappy  # noqa: E402


def lyndon(n):
    """primitive cyclic words in L, R of length n, each class once (the minimal rotation)"""
    res = []
    for k in range(2 ** n):
        w = "".join("R" if (k >> i) & 1 else "L" for i in range(n))
        if "L" not in w or "R" not in w:
            continue
        rots = [w[i:] + w[:i] for i in range(n)]
        if w == min(rots) and len(set(rots)) == n:
            res.append(w)
    return res


words = [w for n in range(2, 11) for w in lyndon(n)]
rows = []
for w in words:
    for sign in ("+", "-"):
        name = f"b{sign}+{w}"
        try:
            M = snappy.Manifold(name)
            st = M.solution_type()
            v = float(M.volume())
            vh = float(M.high_precision().volume())
            rows.append({"word": w, "sign": sign, "name": name, "solution": st, "volume": v,
                         "high precision agrees": abs(v - vh) < 1e-10})
        except Exception as e:  # recorded, not hidden
            rows.append({"word": w, "sign": sign, "name": name, "error": repr(e)})
good = [r for r in rows if r.get("solution") == "all tetrahedra positively oriented" and r.get("high precision agrees")]
ids = {}
for nm in ("b++LR", "b-+LR"):
    try:
        ids[nm] = [str(m) for m in snappy.Manifold(nm).identify()]
    except Exception as e:
        ids[nm] = [repr(e)]
A3 = {"b++LR": ids["b++LR"], "b-+LR": ids["b-+LR"],
      "holds": any(s.startswith("m004") for s in ids["b++LR"]) and any(s.startswith("m003") for s in ids["b-+LR"])}
say("A3 identify:", ids, "->", A3["holds"])
vmin = min(r["volume"] for r in good)
at_min = sorted({(r["word"], r["sign"]) for r in good if abs(r["volume"] - vmin) < 1e-9})
A4 = {"words": len(words), "manifolds": len(rows), "geometric and checked": len(good), "least volume": vmin,
      "attained at": at_min, "holds": len(good) == len(rows) and at_min == [("LR", "+"), ("LR", "-")]
      and abs(vmin - 2.0298832128) < 1e-9}
say("A4 words", len(words), "manifolds", len(rows), "geometric and checked", len(good), "| least volume %.10f at" % vmin,
    at_min, "->", A4["holds"])
vals = sorted({round(r["volume"], 9) for r in good})
classes = {}
for r in good:
    classes.setdefault(round(r["volume"], 9), []).append(r["sign"] + r["word"])
A5 = {"distinct volumes": len(vals), "five smallest": [[v, sorted(classes[v])] for v in vals[:5]],
      "gap above the minimum": vals[1] - vals[0], "largest": vals[-1],
      "signs agree in volume for every word": all(abs(a["volume"] - b["volume"]) < 1e-9 for a in good for b in good
                                                  if a["word"] == b["word"] and a["sign"] != b["sign"])}
say("A5 distinct volumes", len(vals), "| five smallest", A5["five smallest"], "| gap %.6f" % A5["gap above the minimum"],
    "| largest %.6f" % vals[-1], "| the two signs agree for every word:", A5["signs agree in volume for every word"])
out["A3"], out["A4"], out["A5"], out["census"] = A3, A4, A5, rows

# ---------------- B1: the torus-fibred Euclidean metric ----------------
u, v, xx, yy = sp.symbols("u v x y", positive=True)
aa = sp.symbols("a", real=True)
X = (u, v, xx, yy)


def fibred(t1, t2, ephi):
    return sp.Matrix([[ephi, 0, 0, 0], [0, ephi, 0, 0],
                      [0, 0, 1 / t2, t1 / t2], [0, 0, t1 / t2, (t1 ** 2 + t2 ** 2) / t2]])


B1 = {}
for name, t1, t2, ephi, expect in (
        ("tau = z, e^phi = Im tau |e^{az}|^2", u, v, v * sp.exp(2 * aa * u), True),
        ("tau = z^2, e^phi = Im tau |e^{az}|^2", u ** 2 - v ** 2, 2 * u * v, 2 * u * v * sp.exp(2 * aa * u), True),
        ("control: tau = z, e^phi = (Im tau)^2", u, v, v ** 2, False),
        ("control: tau = u + i(1 + v^2), e^phi = Im tau", u, 1 + v ** 2, 1 + v ** 2, False)):
    R = ricci(fibred(t1, t2, ephi), X)
    flat = is_zero(R)
    B1[name] = {"Ricci-flat": flat, "as predicted": flat == expect}
    say("B1", name, ": Ricci-flat", flat, "(predicted", expect, ")")
out["B1"] = B1

# ---------------- B2: Im tau |eta|^4 under the moves ----------------
mp.mp.dps = 40


def eta(tau):
    q = mp.exp(2j * mp.pi * tau)
    p, n = mp.mpf(1), 1
    while True:
        qn = q ** n
        p *= 1 - qn
        if abs(qn) < mp.mpf(10) ** (-48):
            break
        n += 1
    return mp.exp(2j * mp.pi * tau / 24) * p


Lm = lambda s: s / (s + 1)  # noqa: E731  L = ((1,0),(1,1))
Rm = lambda s: s + 1  # noqa: E731        R = ((1,1),(0,1))
rnd = random.Random(120)
taus = [mp.mpc(rnd.uniform(-1, 1), rnd.uniform(0.4, 2.0)) for _ in range(20)]


def F(s, p, q):
    return mp.im(s) ** p * abs(eta(s)) ** (2 * q)


worst = max(abs(F(m(s), 1, 2) / F(s, 1, 2) - 1) for s in taus for m in (Lm, Rm))
ctrl_im = max(abs(mp.im(Lm(s)) / mp.im(s) - 1) for s in taus)
ctrl_eta = max(abs(abs(eta(Lm(s))) ** 4 / abs(eta(s)) ** 4 - 1) for s in taus)
grid = {}
for p in (1, 2, 3):
    for q in range(1, 7):
        grid[f"{p},{q}"] = bool(max(abs(F(Lm(s), p, q) / F(s, p, q) - 1) for s in taus[:6]) < mp.mpf(10) ** (-25))
inv = sorted(k for k, ok in grid.items() if ok)
B2 = {"worst relative change of Im tau |eta|^4": float(worst), "control Im tau": float(ctrl_im),
      "control |eta|^4": float(ctrl_eta), "invariant (p, q)": inv,
      "holds": worst < mp.mpf(10) ** (-25) and ctrl_im > 1e-3 and ctrl_eta > 1e-3 and inv == ["1,2", "2,4", "3,6"]}
say("B2 worst %.3g | controls %.3g, %.3g | invariant (p, q):" % (worst, ctrl_im, ctrl_eta), inv, "->", B2["holds"])
out["B2"] = B2

# ---------------- B3: the pinched record ----------------
ex = []
for k in (4, 8, 16, 24, 40):
    zz = mp.mpf(10) ** (-k) * mp.exp(0.7j)
    tz = mp.log(zz) / (2j * mp.pi)
    ex.append([k, float(mp.log(abs(eta(tz)) ** 4) / mp.log(abs(zz)))])
dev = max(abs(e - 1 / 6) for k, e in ex if k >= 8)
deficit = Fr(1, 12)  # in units of 2 pi
B3 = {"exponent of |z| at |z| = 10^-k": ex, "deviation from 1/6 at k >= 8": dev,
      "deficit per unit (units of 2 pi)": str(deficit), "units closing a sphere": str(Fr(2) / deficit),
      "units for a flat cylindrical end": str(Fr(1) / deficit),
      "holds": dev < 1e-3 and Fr(2) / deficit == 24 and Fr(1) / deficit == 12}
say("B3 exponents", ex, "| deviation %.3g" % dev, "| sphere", Fr(2) / deficit, "units, cylinder", Fr(1) / deficit,
    "->", B3["holds"])
out["B3"] = B3

# ---------------- B4: the abelianization SL(2, Z) -> Z/12 ----------------
I2 = ((1, 0), (0, 1))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def inv2(A):
    return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))


S = ((0, -1), (1, 0))
T = ((1, 1), (0, 1))
L = ((1, 0), (1, 1))
Sinv = inv2(S)


def Tpow(k):
    return ((1, k), (0, 1))


def chi(A):
    """write A = T^k1 S T^k2 S ... (+-1) T^b and sum: chi(T) = 1, chi(S) = 9, chi(-I) = 6 (mod 12)"""
    tot, M = 0, A
    while M[1][0] != 0:
        k = M[0][0] // M[1][0]
        M = mul(Tpow(-k), M)
        tot += k
        M = mul(Sinv, M)
        tot += 9
    eps = M[0][0]
    tot += (6 if eps == -1 else 0) + eps * M[0][1]
    return tot % 12


def rand_sl2(r):
    A = I2
    for _ in range(r.randint(1, 12)):
        A = mul(A, r.choice([S, T, L, inv2(T), inv2(L), Sinv]))
    return A


hom = all(chi(mul(A, B)) == (chi(A) + chi(B)) % 12 for A, B in ((rand_sl2(rnd), rand_sl2(rnd)) for _ in range(200)))
conj = all(chi(mul(mul(G, T), inv2(G))) == 1 for G in (rand_sl2(rnd) for _ in range(100)))
RLi = mul(T, inv2(L))
p3, p6 = I2, I2
for _ in range(3):
    p3 = mul(p3, RLi)
for _ in range(6):
    p6 = mul(p6, RLi)
B4 = {"homomorphism on 200 pairs": hom, "chi(R)": chi(T), "chi(L)": chi(L), "chi(S)": chi(S), "chi(-I)": chi(((-1, 0), (0, -1))),
      "chi(LR)": chi(mul(L, T)), "every sampled conjugate of R has chi 1": conj,
      "(R L^-1)^3": [list(r) for r in p3], "(R L^-1)^6": [list(r) for r in p6]}
B4["holds"] = (hom and conj and B4["chi(R)"] == 1 and B4["chi(L)"] == 11 and B4["chi(S)"] == 9 and B4["chi(-I)"] == 6
               and B4["chi(LR)"] == 0 and p3 == ((-1, 0), (0, -1)) and p6 == I2)
say("B4", {k: B4[k] for k in ("homomorphism on 200 pairs", "chi(R)", "chi(L)", "chi(S)", "chi(-I)", "chi(LR)",
                              "every sampled conjugate of R has chi 1")}, "| (RL^-1)^3 =", p3, "| (RL^-1)^6 =", p6,
    "->", B4["holds"])
out["B4"] = B4

# ---------------- B5: the units on the closed solutions ----------------
B5 = {"rational elliptic surface": {"chi(O_S)": 1, "units 12 chi": 12, "e(S)": 12},
      "K3": {"chi(O_S)": 2, "units 12 chi": 24, "e(S)": 24},
      "least positive count by B4": 12, "(R L^-1)^6 = I uses": 12}
B5["holds"] = (B5["rational elliptic surface"]["units 12 chi"] == B5["rational elliptic surface"]["e(S)"]
               and B5["K3"]["units 12 chi"] == B5["K3"]["e(S)"] and B4["chi(R)"] == 1 and chi(inv2(L)) == 1
               and p6 == I2 and min(n for n in range(1, 25) if n % 12 == 0) == 12)
say("B5", B5)
out["B5"] = B5

out["verdict"] = {c: out[c].get("holds") for c in ("A3", "A4", "B2", "B3", "B4", "B5")}
out["verdict"].update({"A1": all(r["holds"] for r in A1.values()),
                       "A2": einstein3 and flat_at_m1 and mult and all(nonflat.values()),
                       "B1": all(r["as predicted"] for r in B1.values())})
say("verdict", out["verdict"])
(HERE / "the_three_to_four.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
(HERE / "the_three_to_four_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
