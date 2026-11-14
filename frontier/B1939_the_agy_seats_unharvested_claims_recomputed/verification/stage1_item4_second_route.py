"""Adversarial verifier, item 4, own code from scratch (nothing imported from stage1/ or from the repository; the
record's B1929 json files are read as data).

1. Dedekind sums by the reciprocity (Euclid) algorithm; Rademacher Phi, Psi (B1737 lines 69-77's definition).
2. Phi by a second route: Phi(A) = integral of E2 from tau0 = (-d + i)/c to A tau0 = (a + i)/c (c > 0), since
   d/dtau log eta = (pi i/12) E2 and -i(c tau0 + d) = 1. Integrated numerically (mpmath.quad) on a three-leg path.
3. Meyer's signature cocycle in sympy; phi from the braid relation and S^4 = I.
4. B1929: sum over nontrivial characters of eta_A = -2 Im(Delta)/pi against -(1 + sgn tr M) Psi(M)/3 (self-cover).
Plants: Q3 (s(b,|c|) for s(d,|c|) in Phi), Q4 (omega(x1 - y1, .) in Meyer's form), Q5 (no orientation flip in 4).
"""
import json, sys
from fractions import Fraction as Fr
import mpmath as mp
import sympy as sp

PLANT = sys.argv[1] if len(sys.argv) > 1 else None
FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        FAILS.append(name)


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))


I2 = ((1, 0), (0, 1))
LET = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}
LET["l"], LET["r"] = inv(LET["L"]), inv(LET["R"])


def word(w):
    M = I2
    for ch in w:
        M = mul(M, LET[ch])
    return M


def sgn(x): return (x > 0) - (x < 0)


def ded_recip(h, k):
    """s(h, k), k > 0, by reciprocity: s(h,k) = s(h mod k, k); s(h,k) + s(k,h) = (h/k + k/h + 1/(hk))/12 - 1/4"""
    h %= k
    if h == 0 or k == 1:
        return Fr(0)
    return (Fr(h, k) + Fr(k, h) + Fr(1, h * k)) / 12 - Fr(1, 4) - ded_recip(k, h)


def ded_direct(h, k):
    def saw(x):
        return Fr(0) if x.denominator == 1 else x - (x.numerator // x.denominator) - Fr(1, 2)
    return sum(saw(Fr(r, k)) * saw(Fr(h * r, k)) for r in range(1, k))


from math import gcd
pairs = [(h, k) for k in range(1, 40) for h in range(-5, 45) if gcd(h, k) == 1]
bad = [(h, k) for h, k in pairs if ded_recip(h, k) != ded_direct(h, k)]
check("own Dedekind reciprocity = direct sum on %d coprime pairs (reciprocity needs gcd 1; SL(2,Z) has gcd(d,c) = 1)" % len(pairs), not bad, str(bad[:3]))


def Phi(A):
    (a, b), (c, d) = A
    if c == 0:
        return Fr(b, d)
    arg = b if PLANT == "Q3" else d                # Q3: s(b,|c|) in place of s(d,|c|)
    return Fr(a + d, c) - 12 * sgn(c) * ded_recip(arg, abs(c))


def Psi(A):
    (a, b), (c, d) = A
    return Phi(A) - 3 * sgn(c * (a + d))


# ------------------------------------------------------------------ 1. the asked values
fam_k = {k: word("L" * k + "RLR") for k in range(1, 5)}
fam_m = {m: word("L" * m + "R" * m) for m in range(1, 5)}
print("  L^k R L R:", {k: (A, str(Phi(A)), str(Psi(A))) for k, A in fam_k.items()})
print("  L^m R^m:  ", {m: (A, str(Phi(A)), str(Psi(A))) for m, A in fam_m.items()})
check("X5 Psi(L^k R L R) = 0, 1, 2, 3 (k = 1..4) and Psi(L^m R^m) = 0 (m = 1..4), exact" + (" [PLANT Q3]" if PLANT == "Q3" else ""),
      [Psi(fam_k[k]) for k in range(1, 5)] == [0, 1, 2, 3] and all(Psi(fam_m[m]) == 0 for m in range(1, 5)))

# ------------------------------------------------------------------ 2. second route: the E2 integral
mp.mp.dps = 30


def E2(t):
    q = mp.exp(2j * mp.pi * t)
    N = int(mp.ceil(32 * mp.log(10) / (2 * mp.pi * mp.im(t)))) + 10
    s, qn = mp.mpf(0), mp.mpf(1)
    for n in range(1, N):
        qn *= q
        s += sum(dd for dd in range(1, n + 1) if n % dd == 0) * qn
    return 1 - 24 * s


def Phi_E2(A):
    (a, b), (c, d) = A
    assert c > 0
    t0 = mp.mpc(-d, 1) / c
    t1 = mp.mpc(a, 1) / c
    H = mp.mpf(1)                                  # path: up to height 1, across, down (path-independence: E2 holomorphic)
    p0, p1, p2, p3 = t0, mp.mpc(mp.re(t0), H), mp.mpc(mp.re(t1), H), t1
    tot = 0
    for u, v in ((p0, p1), (p1, p2), (p2, p3)):
        tot += mp.quad(lambda s: E2(u + s * (v - u)) * (v - u), [0, 1])
    return tot


worst = 0
rows = []
for nm, A in [("L^%dRLR" % k, fam_k[k]) for k in fam_k] + [("L^%dR^%d" % (m, m), fam_m[m]) for m in fam_m]:
    v = Phi_E2(A)
    err = abs(v - mp.mpf(Phi(A).numerator) / Phi(A).denominator)
    worst = max(worst, err)
    rows.append((nm, mp.nstr(v, 15), str(Phi(A))))
print("  E2-integral Phi:", rows)
check("X5 Phi by the E2 integral equals the exact Dedekind Phi on all eight words (worst %s)" % mp.nstr(worst, 3)
      + (" [PLANT Q3]" if PLANT == "Q3" else ""), worst < mp.mpf(10) ** -18)

# ------------------------------------------------------------------ 3. Meyer's cocycle, sympy
J = sp.Matrix([[0, 1], [-1, 0]])
ASYM = [0]


def tau(A, B):
    A, B = sp.Matrix(A), sp.Matrix(B)
    I = sp.eye(2)
    Msys = (A.inv() - I).row_join(B - I)
    basis = Msys.nullspace()
    if not basis:
        return 0
    sg = -1 if PLANT == "Q4" else 1                # Q4: omega(x1 - y1, .) in place of omega(x1 + y1, .)

    def form(v, w):
        x1, y1, y2 = v[:2, 0], v[2:, 0], w[2:, 0]
        return ((x1 + sg * y1).T * J * ((I - B) * y2))[0, 0]
    G = sp.Matrix(len(basis), len(basis), lambda i, j: form(basis[i], basis[j]))
    if G != G.T:
        ASYM[0] += 1
    G = (G + G.T) / 2
    ev = G.eigenvals()
    return sum(mult * (1 if e > 0 else -1 if e < 0 else 0) for e, mult in ev.items())


x, y = sp.symbols("x y")
base = {"L": x, "R": y}
base["l"] = -x + tau(LET["L"], LET["l"])          # phi(AB) = phi(A) + phi(B) - tau(A,B), phi(I) = 0
base["r"] = -y + tau(LET["R"], LET["r"])


def phi_word(w, b=base):
    M, tot = I2, 0
    for ch in w:
        tot += b[ch] - tau(M, LET[ch])
        M = mul(M, LET[ch])
    return tot


assert word("LrL") == word("rLr") and word("LrL" * 4) == I2
sol = sp.solve([sp.Eq(phi_word("LrL"), phi_word("rLr")), sp.Eq(phi_word("LrL" * 4), 0)], [x, y], dict=True)
print("  Meyer phi(L), phi(R) from the braid relation and S^4 = I:", sol)
ok_meyer = len(sol) == 1
if ok_meyer:
    b = {k: sp.nsimplify(v.subs(sol[0])) for k, v in base.items()}
    phk = {k: phi_word("L" * k + "RLR", b) for k in range(1, 5)}
    phm = {m: phi_word("L" * m + "R" * m, b) for m in range(1, 5)}
    # consistency on relations not used: (L r)^6 = I, and conjugation invariance
    extra = [phi_word("Lr" * 6, b), phi_word("rL" * 6, b)]
    conj = [phi_word(c + "L" * k + "RLR" + "".join(ch.swapcase() for ch in reversed(c)), b) - phk[k] for k in (2, 3) for c in ("R", "lR", "LLr")]
    print("  phi(L) = %s, phi(R) = %s; phi(L^k R L R) = %s; phi(L^m R^m) = %s; (Lr)^6, (rL)^6 -> %s; conjugation changes %s" % (
        b["L"], b["R"], [str(phk[k]) for k in range(1, 5)], [str(phm[m]) for m in range(1, 5)], extra, conj))
    ok_meyer = (all(phk[k] == sp.Rational(-(Psi(fam_k[k]).numerator), 3 * Psi(fam_k[k]).denominator) for k in phk)
                and all(phm[m] == 0 for m in phm) and extra == [0, 0] and all(c == 0 for c in conj))
tagq4 = " [PLANT Q4]" if PLANT == "Q4" else ""
check("X6 Meyer's form symmetric on every V_{A,B} met" + tagq4, ASYM[0] == 0, "asymmetric: %d" % ASYM[0])
check("X6 Meyer phi = -Psi/3 on L^k R L R, L^m R^m; (Lr)^6 -> 0; class function" + tagq4, ok_meyer)

# ------------------------------------------------------------------ 4. B1929: the self-cover identity
ROOT = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/" + "frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/verification/"
pop = json.load(open(ROOT + "received_sm/population.json"))
sieg = {(tuple(r["level"]), r["i"], r["j"]): r["Delta"] for r in json.load(open(ROOT + "main_siegel.json"))}
lev = {}
for o in pop:
    lev.setdefault(tuple(o["level"]), []).append(o)
worst4, all4, nchar = 0.0, True, 0
for key, os_ in sorted(lev.items()):
    M = tuple(tuple(r) for r in os_[0]["M"]); N = os_[0]["N"]
    (a, b_), (c, d) = M
    tr = a + d
    chars = {(o["i"] % N, o["j"] % N) for o in os_}
    allfixed = {(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0)
                and ((a - 1) * i + c * j) % N == 0 and (b_ * i + (d - 1) * j) % N == 0}
    full = chars == allfixed and len(chars) + 1 == abs(2 - tr)
    s = sum(-2 * sieg[(key, o["i"], o["j"])][1] / mp.pi for o in os_)
    nchar += len(os_)
    flip = 0 if PLANT == "Q5" else (1 if tr > 2 else 0)   # Q5: no orientation flip
    pred = -2 * flip * Psi(M) / 3
    err = abs(s - float(pred))
    worst4 = max(worst4, err)
    ok = full and err < 1e-9
    all4 &= ok
    print("  %-14s tr=%5d |C|=%4d all M^T-fixed chars present: %s  Psi=%s  sum_{c!=0} eta_A = %+.12f  predicted %s  %s" % (
        key, tr, len(chars) + 1, full, Psi(M), float(s), pred, "ok" if ok else "MISMATCH"))
check("X7 sum_{c != 0} eta_A(c) = -2 Psi(M)/3 (tr > 2), 0 (tr < -2) on all %d levels, %d characters (worst %.1e)" % (
    len(lev), nchar, worst4) + (" [PLANT Q5]" if PLANT == "Q5" else ""), all4)
print("FAILED CHECKS:", FAILS if FAILS else "none")
