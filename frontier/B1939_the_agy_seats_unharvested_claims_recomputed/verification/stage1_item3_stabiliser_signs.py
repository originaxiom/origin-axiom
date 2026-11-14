"""Item 3 of the stage-1 audit report: the weave triplet's weight-0 normalisations and the stabiliser signs.

Own code. Nothing from the agy lane is run or imported; nothing from main is imported either (main's triplet is
transcribed as data from join_scrutiny.py lines 318-319). Data-free.

Moves: L = [[1,1],[0,1]]: tau -> tau + 1; R = [[1,0],[1,1]]: tau -> tau/(tau+1); S = L R^-1 L: tau -> -1/tau.
"""
import itertools, json, sys
import mpmath as mp

mp.mp.dps = 30
OUT = {}
FAILS = []


def check(name, ok, detail=""):
    OUT.setdefault("checks", []).append({"name": name, "ok": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAILS.append(name)
    return ok

# ---------------------------------------------------------------- series (explicit, no library theta: branch-safe)
NT = 80


def ex(tau, x):                       # exp(pi i tau x)
    return mp.exp(mp.pi * 1j * tau * x)


def th2(t): return 2 * ex(t, mp.mpf(1) / 4) * mp.fsum(ex(t, n * (n + 1)) for n in range(NT))
def th3(t): return 1 + 2 * mp.fsum(ex(t, n * n) for n in range(1, NT))
def th4(t): return 1 + 2 * mp.fsum((-1) ** n * ex(t, n * n) for n in range(1, NT))
def eta(t): return ex(t, mp.mpf(1) / 12) * mp.fprod(1 - ex(t, 2 * n) for n in range(1, 4 * NT))
def E4(t):
    q = mp.exp(2j * mp.pi * t)
    return 1 + 240 * mp.fsum(mp.mpf(n) ** 3 * q ** n / (1 - q ** n) for n in range(1, 4 * NT))
def E6(t):
    q = mp.exp(2j * mp.pi * t)
    return 1 - 504 * mp.fsum(mp.mpf(n) ** 5 * q ** n / (1 - q ** n) for n in range(1, 4 * NT))


def Vvec(t):
    e3 = eta(t) ** 3
    return [th2(t) ** 2 / e3, th3(t) ** 2 / e3, th4(t) ** 2 / e3]


# g_m: weight 1/2, multiplier chi_m (L -> zeta_24^m); m = 1 mod 4
G = {1: lambda t: eta(t),
     5: lambda t: eta(t) ** 5 * E4(t) / E6(t),
     9: lambda t: eta(t) ** 9 / E4(t),
     13: lambda t: eta(t) ** 13 / E6(t),
     17: lambda t: eta(t) ** 17 / E4(t) ** 2,
     21: lambda t: eta(t) ** 21 / (E4(t) * E6(t))}


def Uvec(m, t):
    g = G[m](t)
    return [g * v for v in Vvec(t)]

# ---------------------------------------------------------------- fitting a 3x3 matrix from the functions
TAUS = [mp.mpc(0.13, 0.9), mp.mpc(-0.21, 1.1), mp.mpc(0.37, 0.8)]
FRESH = mp.mpc(0.05, 1.3)
MOB = {"L": lambda t: t + 1, "R": lambda t: t / (t + 1), "S": lambda t: -1 / t}


def fit(f, image, factor):
    A = mp.matrix(3, 3); B = mp.matrix(3, 3)
    for k, t in enumerate(TAUS):
        a = f(t); b = f(image(t)); w = factor(t)
        for i in range(3):
            A[i, k] = a[i]; B[i, k] = b[i] / w
    return B * mp.inverse(A)


def to_monomial(M, tol=mp.mpf(10) ** -20):
    """exact monomial form (perm, exps mod 24) with M e_j = zeta_24^exps[j] e_perm[j]; asserts the entries are 0 or 24th roots"""
    perm, exps, worst = [None] * 3, [None] * 3, mp.mpf(0)
    for j in range(3):
        nz = [i for i in range(3) if abs(M[i, j]) > mp.mpf("1e-10")]
        if len(nz) != 1:
            return None, None
        i = nz[0]; z = M[i, j]
        k = int(mp.nint(24 * mp.arg(z) / (2 * mp.pi))) % 24
        worst = max(worst, abs(z - mp.exp(2j * mp.pi * k / 24)), *[abs(M[r, j]) for r in range(3) if r != i])
        perm[j], exps[j] = i, k
    return (tuple(perm), tuple(exps)), worst


# ---------------------------------------------------------------- exact monomial arithmetic over the 24th roots
E3 = ((0, 1, 2), (0, 0, 0))
def mmul(A, B): return (tuple(A[0][B[0][j]] for j in range(3)), tuple((B[1][j] + A[1][B[0][j]]) % 24 for j in range(3)))
def minv(A):
    p, e = [0] * 3, [0] * 3
    for j in range(3): p[A[0][j]] = j; e[A[0][j]] = (-A[1][j]) % 24
    return (tuple(p), tuple(e))
def mscal(k, A): return (A[0], tuple((x + k) % 24 for x in A[1]))
def mneg(A): return mscal(12, A)
def mconj(A): return (A[0], tuple((-x) % 24 for x in A[1]))
def mpow(A, n):
    X = E3
    for _ in range(n): X = mmul(X, A)
    return X
def is_scalar(A): return A[0] == (0, 1, 2) and len(set(A[1])) == 1
def eig_on(A, j):                      # eigenvalue exponent of A on e_j, or None if e_j is not an eigenvector
    return A[1][j] if A[0][j] == j else None
def group(gens):
    seen = {E3}; fr = [E3]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = mmul(a, g)
                if x not in seen: seen.add(x); nx.append(x)
        fr = nx
    return seen

# exact traces in Q(zeta_24): reduce sum x^e modulo Phi_24(x) = x^8 - x^4 + 1
def cyc_reduce(exps):
    c = [0] * 24
    for e in exps: c[e % 24] += 1
    for d in range(23, 7, -1):          # x^d = x^(d-4) - x^(d-8)
        v = c[d]
        if v:
            c[d] = 0; c[d - 4] += v; c[d - 8] -= v
    return tuple(c[:8])
def trace(A): return cyc_reduce([A[1][j] for j in range(3) if A[0][j] == j])


def equivalent(pairA, pairB):
    """are L -> A_L, R -> A_R and L -> B_L, R -> B_R equivalent? exact characters over the group of pairs"""
    I2 = (E3, E3); seen = {I2}; fr = [I2]
    gens = [(pairA[0], pairB[0]), (pairA[1], pairB[1])]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = (mmul(a[0], g[0]), mmul(a[1], g[1]))
                if x not in seen: seen.add(x); nx.append(x)
        fr = nx
    return all(trace(a) == trace(b) for a, b in seen), len(seen)

# ---------------------------------------------------------------- Ind(psi) from Gamma_theta = <L^2, S>, own construction
def induced(e_L2, e_S, N=8):
    """Ind of psi (psi(L^2) = zeta_24^e_L2, psi(S) = zeta_24^e_S) from <L^2, S> to SL(2, Z), via SL(2, Z/N).
    Cosets <-> the three theta characteristics as lines in (Z/2)^2 acted on by g (row vector times g mod 2)."""
    def mm(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % N for j in range(2)) for i in range(2))
    def mi(A): return ((A[1][1] % N, -A[0][1] % N), (-A[1][0] % N, A[0][0] % N))
    I = ((1, 0), (0, 1)); L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); S = mm(mm(L, mi(R)), L); L2 = mm(L, L)
    psi = {I: 0}; fr = [I]
    while fr:                           # psi on the image of <L^2, S> mod N, by words; consistency tested
        nx = []
        for h in fr:
            for g, e in ((L2, e_L2), (mi(L2), -e_L2), (S, e_S), (mi(S), -e_S)):
                k = mm(h, g); v = (psi[h] + e) % 24
                if k in psi:
                    if psi[k] != v: return None
                else:
                    psi[k] = v; nx.append(k)
        fr = nx
    # H = <L^2, S> mod 2 = {I, S mod 2}; cosets g H, representatives
    reps = [I, L, R]
    def coset_of(g):
        for i, r in enumerate(reps):
            h = mm(mi(r), g)
            if h in psi: return i, h
        raise AssertionError("no coset")
    mats = []
    for x in (L, R):
        perm, exps = [None] * 3, [None] * 3
        for j, r in enumerate(reps):
            i, h = coset_of(mm(x, r))  # x r = r_i h
            perm[j], exps[j] = i, psi[h]
        mats.append((tuple(perm), tuple(exps)))
    return tuple(mats)


def run(plant=None):
    res = {}
    # ---- the record's triplet T (B1866 part 6, transcribed) and V's fitted matrices
    XL = ((0, 2, 1), ((-3) % 24, 3, 3)); XR = ((1, 0, 2), ((-3) % 24, (-3) % 24, 3))
    ML = fit(Vvec, MOB["L"], lambda t: 1)
    MR = fit(Vvec, MOB["R"], lambda t: mp.sqrt(t + 1) ** -1)
    (mL, wL), (mR, wR) = to_monomial(ML), to_monomial(MR)
    check("E3.1 V's fitted M_L, M_R are monomial in 24th roots (worst residual %.1e, %.1e)" % (wL, wR), wL < 1e-20 and wR < 1e-20)
    check("E3.1 V's fitted matrices are the conjugates of the record's triplet (XL, XR)", (mconj(mL), mconj(mR)) == (XL, XR),
          "M_L = %s, M_R = %s" % (mL, mR))
    # predicted M_L from the transformation laws: theta_2^2 -> e(1/4) theta_2^2, theta_3^2 <-> theta_4^2, eta^3 -> e(3/24) eta^3
    eta_T = 2 if plant == "P3a" else 1   # P3a: eta(tau+1) = e(1/12) eta instead of e(1/24)
    pred_ML = ((0, 2, 1), ((6 - 3 * eta_T) % 24, (-3 * eta_T) % 24, (-3 * eta_T) % 24))
    check("E3.1 predicted M_L (theta and eta laws) equals the series fit" + (" [PLANT P3a]" if plant == "P3a" else ""), pred_ML == mL)
    GV = group([mL, mR]); GT = group([XL, XR])
    SV = mmul(mmul(mL, minv(mR)), mL); ST = mmul(mmul(XL, minv(XR)), XL)
    res["V"] = {"M_L": mL, "M_R": mR, "group_order": len(GV), "S^2": mpow(SV, 2), "S^4": mpow(SV, 4)}
    res["T"] = {"group_order": len(GT), "S^2": mpow(ST, 2), "S^4": mpow(ST, 4)}
    check("record's T: group of order 96, S^2 = i, S^4 = -1", len(GT) == 96 and mpow(ST, 2) == ((0, 1, 2), (6, 6, 6)) and mpow(ST, 4) == ((0, 1, 2), (12, 12, 12)))
    # eigenphases of V's L (E3.8)
    # M_L = e(1/8) on e_1, and the 2-3 block [[0, a],[a, 0]] with a = e(-1/8): eigenvalues +a, -a
    a = mL[1][1]
    ph = sorted({mL[1][0] / 24, (a % 24) / 24, ((a + 12) % 24) / 24})
    res["V"]["L_eigenphases"] = ph
    check("E3.8 V's L-eigenphases are {1/8, 3/8, 7/8}", ph == [0.125, 0.375, 0.875], str(ph))

    # ---- the weight-0 normalisations U_m
    res["U"] = {}
    for m in (1, 5, 9, 13, 17, 21):
        f = lambda t, m=m: Uvec(m, t)
        mats = {}
        for nm in ("L", "R", "S"):
            M, w = to_monomial(fit(f, MOB[nm], lambda t: 1))
            assert M is not None and w < 1e-18, (m, nm, w)
            mats[nm] = M
        rL, rR, rS = mats["L"], mats["R"], mats["S"]
        word_S = mmul(mmul(rL, minv(rR)), rL)
        twist_ok = (rL == mscal(m, mL) and rR == mscal(-m, mR))
        psl = (mpow(rS, 2) == E3 and mpow(mmul(rS, rL), 3) == E3 and word_S == rS)
        if plant == "P3d" and m == 9:
            rS = mneg(rS)
        # re-check rho(S) at a fresh point
        u0, u1 = f(FRESH), f(MOB["S"](FRESH))
        Sd = [[0] * 3 for _ in range(3)]
        for j in range(3): Sd[rS[0][j]][j] = mp.exp(2j * mp.pi * rS[1][j] / 24)
        resid = max(abs(u1[i] - sum(Sd[i][j] * u0[j] for j in range(3))) for i in range(3))
        slot = 0 if plant == "P3b" else 1                 # P3b: theta_2's slot instead of theta_3's
        eL2, eS = eig_on(mpow(rL, 2), slot), eig_on(rS, slot)
        Gm = group([rL, rR])
        res["U"][m] = {"rho_L": rL, "rho_R": rR, "rho_S": rS, "group_order": len(Gm), "twist_of_V_by_chi_m": twist_ok,
                       "PSL": psl, "S_fresh_residual": float(resid), "slot": slot + 1,
                       "L2_on_slot_exp24": eL2, "S_on_slot_exp24": eS}
        tagm = (" [PLANT P3d]" if plant == "P3d" and m == 9 else "")
        check("U_%d: rho(S) re-checked at a fresh point (residual %.1e)%s" % (m, resid, tagm), resid < 1e-20)
        check("U_%d: rho = chi_%d (x) rho_V; a PSL(2,Z) module (S^2 = 1, (SL)^3 = 1, S = L R^-1 L)" % (m, m), twist_ok and psl)
        check("U_%d: slot %d is a common eigenvector of L^2 and S%s" % (m, slot + 1, " [PLANT P3b]" if plant == "P3b" else ""),
              eL2 is not None and eS is not None, "L^2 -> e(%s/24), S -> e(%s/24)" % (eL2, eS))
    # ---- E3.3: signs only for m = 9, 21; (-1,+1) at 9, (-1,-1) at 21
    if plant not in ("P3b",):
        signs = {m: (v["L2_on_slot_exp24"], v["S_on_slot_exp24"]) for m, v in res["U"].items()}
        sign_ms = [m for m, (a2, s2) in signs.items() if a2 in (0, 12) and s2 in (0, 12)]
        check("E3.3 the stabiliser acts by signs only for m in {9, 21}", sign_ms == [9, 21], str(signs))
        check("E3.3 U_9: (-1 on L^2, +1 on S); U_21: (-1 on L^2, -1 on S)", signs[9] == (12, 0) and signs[21] == (12, 12))
        U9 = res["U"][9]
        check("E3.5 U_9: T_u = [[-1,0,0],[0,0,i],[0,i,0]], S_u = (1 3), T_u^2 = diag(1,-1,-1)",
              U9["rho_L"] == ((0, 2, 1), (12, 6, 6)) and U9["rho_S"] == ((2, 1, 0), (0, 0, 0)) and mpow(U9["rho_L"], 2) == ((0, 1, 2), (0, 12, 12)))
    # ---- E3.4: equivalence with Ind(psi), own construction
    ind = {}
    for e1, e2 in ((12, 0), (12, 12), (0, 0), (0, 12)):
        ind[(e1, e2)] = induced(e1, e2)
    U9p = (res["U"][9]["rho_L"], res["U"][9]["rho_R"]); U21p = (res["U"][21]["rho_L"], res["U"][21]["rho_R"])
    target = ind[(12, 12)] if plant == "P3c" else ind[(12, 0)]
    eq9, n9 = equivalent(U9p, target)
    check("E3.4 rho_{U_9} equivalent to Ind(-1,+1)%s" % (" [PLANT P3c: tested against Ind(-1,-1)]" if plant == "P3c" else ""), eq9, "pairs %d" % n9)
    eq21, _ = equivalent(U21p, ind[(12, 12)])
    check("E3.4 rho_{U_21} equivalent to Ind(-1,-1)", eq21)
    check("E3.4 Ind(-1,+1), Ind(-1,-1): groups of order 24; Ind(+1,+-1): order 6",
          [len(group(list(ind[k]))) for k in ((12, 0), (12, 12), (0, 0), (0, 12))] == [24, 24, 6, 6],
          str([len(group(list(ind[k]))) for k in ((12, 0), (12, 12), (0, 0), (0, 12))]))
    # B1866 part 5: chi_9 (x) Ind(-1,+1) = T, chi_21 (x) Ind(-1,-1) = T
    i9 = ind[(12, 0)]; i21 = ind[(12, 12)]
    b9, _ = equivalent((mscal(9, i9[0]), mscal(-9, i9[1])), (XL, XR))
    b21, _ = equivalent((mscal(21, i21[0]), mscal(-21, i21[1])), (XL, XR))
    check("E3.4 B1866 part 5 reproduced: chi_9 (x) Ind(-1,+1) = T and chi_21 (x) Ind(-1,-1) = T", b9 and b21)
    tw = {k: [m for m in range(24) if equivalent((mscal(m, ind[k][0]), mscal(-m, ind[k][1])), (XL, XR))[0]] for k in ((12, 0), (12, 12))}
    res["twists_to_T"] = {str(k): v for k, v in tw.items()}
    # ---- E3.7 parity: chi_m(S~^4) = zeta_24^(12 m)
    par = all((12 * m) % 24 == (0 if m % 2 == 0 else 12) for m in range(24))
    check("E3.7 chi_m factors through SL(2,Z) iff m even (chi_m(S~^4) = (-1)^m)", par)
    return res


if __name__ == "__main__":
    plant = sys.argv[1] if len(sys.argv) > 1 else None
    res = run(plant)
    print("RESULT", json.dumps({k: (v if k != "U" else {m: {kk: vv for kk, vv in d.items()} for m, d in v.items()}) for k, v in res.items()}, default=str))
    print("FAILED CHECKS:", FAILS if FAILS else "none")
