"""W45 (the rule: W45_RULE.md, committed before this script). The triplet's index on the weave's own surface.

  E1  structure: (L R^-1 L)^4 is an inner automorphism of F2, conjugation by a word u; on T its lift acts as -I for
      every choice of lift signs, while the inner automorphisms' own lifts (W40's construction, as W42's A4) are signs
      times parity signs, the c = 1 ones of determinant 1, and u read through them never gives -I, whatever lifts are
      chosen; (L R^-1 L)^8 acts as 1. So T is a genuine representation of the metaplectic group, not a local system on
      M_{1,2} itself.
  E2  the Riemann-Roch number of vector-valued modular forms,
        chi_k(rho) = d(k-1)/12 + 1/4 Re[e^{i pi k/2} tr rho(S)] + 2/(3 sqrt3) Re[e^{i pi (2k+1)/6} tr rho(ST)]
                     + d/2 - sum_j lambda_j      (rho(T) = diag e^{2 pi i lambda_j}, 0 <= lambda_j < 1),
      calibrated on the trivial representation (k = 0, 2, 12), eta and W41's Weil representation (k = 1/2).
  E3  rho_T from W38's normal form (sigma1 = L, sigma2 = R^-1, S~ = L R^-1 L): the four identifications S <-> S~^{+-1},
      T <-> L^{+-1}; a convention is kept when chi_k is an integer at every weight up to 15/2 its central character
      rho(S)^2 = e^{-i pi k} allows, and when rho(S)^2 = (rho(S) rho(T))^3.
  E4  the dimensions dim M_k and dim S_k, numerically: q-expansions with each component's exponent, the relation
      f(-1/tau) = tau^k rho(S) f(tau) imposed on the unit arc, the null singular values counted with their gap;
      calibrated on eta and the Weil representation first.

Run: python3 the_index_on_the_weaves_surface.py  ->  the_index_on_the_weaves_surface.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_breaking_verified as BV  # noqa: E402  (W42: the exact normal form of the weave's group)

CP = BV.CP
OUT = HERE / "the_index_on_the_weaves_surface.json"
WEIGHTS = [Fraction(n, 2) for n in range(0, 16)]           # 0, 1/2, ..., 15/2


# ---------------------------------------------------------------- E1

def compose_all(*auts):
    out = {1: [1], 2: [2]}
    for a in auts:
        out = CP.compose(out, a)
    return out


def inner_word(phi):
    """u with phi(x) = u x u^-1 for x = a, b, or None. phi(a) reduces to v a v^-1 with v not ending in a^+-1, and
    u = v a^m; m is bounded by the length of phi(b)."""
    x = phi[1]
    n = len(x)
    if n % 2 == 0 or x[n // 2] != 1:
        return None
    v = x[:n // 2]
    if CP.reduce(v + [1] + CP.inv(v)) != x:
        return None
    for m in range(-len(phi[2]) - 1, len(phi[2]) + 2):
        u = CP.reduce(v + ([1] * m if m > 0 else [-1] * (-m)))
        if CP.reduce(u + [2] + CP.inv(u)) == phi[2]:
            return u
    return None


def word_text(u):
    return " ".join({1: "a", 2: "b", -1: "a^-1", -2: "b^-1"}[x] for x in u) or "1"


def E1():
    L = CP.AUT["L"]
    Rinv = {1: [1, -2], 2: [2]}
    St = compose_all(L, Rinv, L)                          # the automorphism L o R^-1 o L
    St4 = compose_all(St, St, St, St)
    St8 = compose_all(St4, St4)
    u4 = inner_word(St4)
    G, _, encode, named = BV.the_group_exact()
    gL, gR = named["L"], named["R"]
    ident = (0, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    minus_I = (12, ident[1])
    lifts = {}
    for sL, sR in itertools.product((0, 12), (0, 12)):
        xL, xR = ((gL[0] + sL) % 24, gL[1]), ((gR[0] + sR) % 24, gR[1])
        xRinv = next(y for y in G if BV.emul(xR, y) == ident)
        s = BV.emul(BV.emul(xL, xRinv), xL)
        s4 = BV.emul(BV.emul(s, s), BV.emul(s, s))
        s8 = BV.emul(s4, s4)
        lifts["L sign %d, R sign %d" % (sL // 12, sR // 12)] = {"S~^4": s4, "S~^8": s8}
    # the fibre's loops: the inner automorphisms' lifts on T, every lift, from W40's construction (as W42's A4)
    named_T, _ = BV.H.triplets()
    C = named_T["T"]
    Qt = C.conj().T @ BV.H.gram_V() @ C
    Kc = np.linalg.cholesky((Qt + Qt.conj().T) / 2).conj().T
    inner_lifts = {g: [encode(BV.MV.on_T(C, Kc, BV.CT.on_V(CP.inner([g]), x))) for x in CP.extend(CP.inner([g]))]
                   for g in (1, 2)}
    diagonal = all(BV.perm_of(x[1]) == (0, 1, 2) for v in inner_lifts.values() for x in v)
    c1_dets = sorted({int(round(np.linalg.det(np.array(x[1])))) for v in inner_lifts.values() for x in v if x[0] == 0})
    # the word u read through the inner lifts, for every choice of lift for a and for b
    through = []
    if u4 is not None:
        for xa, xb in itertools.product(inner_lifts[1], inner_lifts[2]):
            img = ident
            for letter in u4:
                y = {1: xa, 2: xb}[abs(letter)]
                if letter < 0:
                    y = next(z for z in G if BV.emul(y, z) == ident)
                img = BV.emul(img, y)
            through.append(img)
    det_of = lambda x: complex(np.exp(2j * np.pi * 3 * x[0] / 24) * np.linalg.det(np.array(x[1])))
    show = lambda x: {"k": x[0], "S": [list(r) for r in x[1]]}
    return {
        "S~ = L o R^-1 o L, its H1 matrix": (np.array(CP.MAT["L"]) @ np.linalg.inv(np.array(CP.MAT["R"]))
                                             @ np.array(CP.MAT["L"])).round().astype(int).tolist(),
        "S~^4 is inner: the conjugating word u": word_text(u4) if u4 is not None else None,
        "S~^8 is inner": inner_word(St8) is not None,
        "the lifted S~^4 and S~^8 on T, for every lift sign": {n: {m: show(x) for m, x in v.items()}
                                                              for n, v in lifts.items()},
        "S~^4 acts as -I for every lift sign": all(v["S~^4"] == minus_I for v in lifts.values()),
        "S~^8 acts as 1 for every lift sign": all(v["S~^8"] == ident for v in lifts.values()),
        "the inner automorphisms' lifts (every lift)": {("inner by a", "inner by b")[g - 1]: [show(x) for x in v]
                                                       for g, v in inner_lifts.items()},
        "every inner lift is a sign times a diagonal sign matrix": bool(diagonal),
        "the c = 1 inner lifts (the parity signs) have determinant": c1_dets,
        "u through the inner lifts, for every choice of lift": [show(x) for x in through],
        "u through the inner lifts: determinants": sorted({round(det_of(x).real, 9) for x in through}),
        "the lifted S~^4: determinant": round(det_of(minus_I).real, 9),
        "u through the inner lifts is never -I": bool(through) and all(x != minus_I for x in through),
    }


# ---------------------------------------------------------------- E2 and E3: the formula

def chi(k, rS, rT):
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    d = rS.shape[0]
    lam = sorted(float(np.angle(z) / (2 * np.pi)) % 1.0 for z in np.linalg.eigvals(rT))
    lam = [0.0 if abs(x - 1) < 1e-9 or abs(x) < 1e-9 else x for x in lam]
    kf = float(k)
    val = (d * (kf - 1) / 12 + 0.25 * np.real(np.exp(1j * np.pi * kf / 2) * np.trace(rS))
           + 2 / (3 * np.sqrt(3)) * np.real(np.exp(1j * np.pi * (2 * kf + 1) / 6) * np.trace(rS @ rT))
           + d / 2 - sum(lam))
    return float(val), lam


def allowed(k, rS):
    """the central character: rho(S)^2 = e^{-i pi k} (a scalar)"""
    S2 = np.array(rS) @ np.array(rS)
    return bool(np.allclose(S2, np.exp(-1j * np.pi * float(k)) * np.eye(len(S2)), atol=1e-9))


def E2():
    out = {}
    one = [[1.0]]
    for k, want in ((0, 1), (2, 0), (12, 2)):
        out["trivial, k = %d" % k] = [round(chi(Fraction(k), one, one)[0], 9), want]
    eta_S, eta_T = [[np.exp(-1j * np.pi / 4)]], [[np.exp(2j * np.pi / 24)]]
    out["eta, k = 1/2"] = [round(chi(Fraction(1, 2), eta_S, eta_T)[0], 9), 1]
    WS = np.exp(-1j * np.pi / 4) / np.sqrt(2) * np.array([[1, 1], [1, -1]])
    WT = np.diag([1, 1j])
    out["W41's Weil representation, k = 1/2"] = [round(chi(Fraction(1, 2), WS, WT)[0], 9), 1]
    ok = all(abs(v[0] - v[1]) < 1e-9 for v in out.values())
    return out, ok, (eta_S, eta_T), (WS, WT)


def E3():
    G, _, encode, named = BV.the_group_exact()
    gL, gR = named["L"], named["R"]
    ident = (0, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    gRinv = next(y for y in G if BV.emul(gR, y) == ident)
    gLinv = next(y for y in G if BV.emul(gL, y) == ident)
    A = BV.emul(BV.emul(gL, gRinv), gL)                   # the record's matrix of S~ = L R^-1 L
    Ainv = next(y for y in G if BV.emul(A, y) == ident)
    num = lambda x: np.exp(2j * np.pi * x[0] / 24) * np.array(x[1], dtype=complex)
    combos = {"S <-> S~, T <-> L": (A, gL), "S <-> S~, T <-> L^-1": (A, gLinv),
              "S <-> S~^-1, T <-> L": (Ainv, gL), "S <-> S~^-1, T <-> L^-1": (Ainv, gLinv)}
    out, kept = {}, {}
    for name, (xs, xt) in combos.items():
        rS, rT = num(xs), num(xt)
        rel = bool(np.allclose(rS @ rS, np.linalg.matrix_power(rS @ rT, 3), atol=1e-9))
        table, integral = {}, True
        for k in WEIGHTS:
            if allowed(k, rS):
                v, lam = chi(k, rS, rT)
                table[str(k)] = round(v, 9)
                integral &= abs(v - round(v)) < 1e-9
        out[name] = {"rho(S)^2 = (rho(S) rho(T))^3": rel, "allowed weights and chi_k": table,
                     "integral at every allowed weight": bool(integral),
                     "tr rho(S)": [round(float(np.real(np.trace(rS))), 9), round(float(np.imag(np.trace(rS))), 9)],
                     "tr rho(ST)": [round(float(np.real(np.trace(rS @ rT))), 9),
                                    round(float(np.imag(np.trace(rS @ rT))), 9)],
                     "exponents of rho(T)": [round(x, 9) for x in chi(Fraction(0), rS, rT)[1]]}
        if integral and rel and table:
            kept[name] = (rS, rT)
    return out, kept


# ---------------------------------------------------------------- E4: the dimensions, numerically

def dims(rS, rT, k, cusp=False, N=24, M=120):
    """dim of the holomorphic (or cusp) vector-valued forms of weight k: f(tau + 1) = rho(T) f(tau),
    f(-1/tau) = tau^k rho(S) f(tau)"""
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    d = rS.shape[0]
    w, P = np.linalg.eig(rT)
    P = np.linalg.qr(P)[0] if np.allclose(rT @ rT.conj().T, np.eye(d)) else P
    lam = [float(np.angle(z) / (2 * np.pi)) % 1.0 for z in w]
    lam = [0.0 if abs(x - 1) < 1e-9 or abs(x) < 1e-9 else x for x in lam]
    cols = [(j, n) for j in range(d) for n in range(N) if not (cusp and lam[j] == 0.0 and n == 0)]
    h0 = np.sqrt(3) / 2

    def phi(j, n, t):
        e = n + lam[j]
        return np.exp(2j * np.pi * e * t) * np.exp(2 * np.pi * e * h0)

    thetas = np.linspace(np.pi / 3 + 0.02, 2 * np.pi / 3 - 0.02, M)
    rows = []
    for th in thetas:
        t = np.exp(1j * th)
        ts = -1 / t
        tk = np.exp(float(k) * np.log(t))
        block = np.zeros((d, len(cols)), dtype=complex)
        for c, (j, n) in enumerate(cols):
            block[:, c] = P[:, j] * phi(j, n, ts) - tk * (rS @ P[:, j]) * phi(j, n, t)
        rows.append(block)
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    s = s / s[0]
    null = int(sum(s < 1e-9))
    gap = [float(s[len(s) - null - 1]) if null < len(s) else None, float(s[-null]) if null else None]
    return null, gap


def E4(eta, weil, kept):
    out = {"eta, M_1/2": dims(*eta, Fraction(1, 2)), "Weil, M_1/2": dims(*weil, Fraction(1, 2))}
    for name, (rS, rT) in kept.items():
        rows = {}
        for k in WEIGHTS:
            if allowed(k, rS) and Fraction(1, 2) <= k <= Fraction(9, 2):
                Mk = dims(rS, rT, k)
                dual = (np.conj(rS), np.conj(rT))
                Sk = dims(*dual, 2 - k, cusp=True) if allowed(2 - k, dual[0]) and 2 - k > 0 else (0, None)
                rows[str(k)] = {"dim M_k (null count, gap)": Mk, "dim S_(2-k) of the dual (null count, gap)": Sk,
                                "dim M_k - dim S_(2-k)": Mk[0] - Sk[0]}
        out[name] = rows
    return out


def main():
    e1 = E1()
    e2, e2_ok, eta, weil = E2()
    e3, kept = E3()
    e4 = E4(eta, weil, kept)
    hands = {}
    for name, v in e3.items():
        if name in kept:
            hands[name] = v["allowed weights and chi_k"]
    agree = all(abs(e3[n]["allowed weights and chi_k"][k] - r["dim M_k - dim S_(2-k)"]) < 1e-9
                for n, rows in e4.items() if n in kept for k, r in rows.items())
    lowest = {n: min(v.items(), key=lambda kv: float(Fraction(kv[0]))) for n, v in hands.items()}
    checks = {
        "E1: S~^4 is inner and acts as -I for every lift sign, while u read through the inner lifts (parity signs, "
        "determinant 1 at c = 1) never does; S~^8 acts as 1": bool(
            e1["S~^4 is inner: the conjugating word u"] is not None and e1["S~^4 acts as -I for every lift sign"]
            and e1["S~^8 acts as 1 for every lift sign"] and e1["every inner lift is a sign times a diagonal sign matrix"]
            and e1["the c = 1 inner lifts (the parity signs) have determinant"] == [1]
            and e1["u through the inner lifts is never -I"]),
        "E2: the formula reproduces 1, 0, 2 (trivial), 1 (eta), 1 (Weil)": bool(e2_ok),
        "E3: integrality keeps exactly one identification per hand, (S~, L^-1) and (S~^-1, L)": sorted(kept) == sorted(
            ["S <-> S~, T <-> L^-1", "S <-> S~^-1, T <-> L"]),
        "E3: chi at the lowest allowed weights is 0 for both hands": bool(lowest) and all(
            abs(v[1]) < 1e-9 for v in lowest.values()),
        "E3: chi_7/2 = 1 for rho_T and chi_9/2 = 1 for its conjugate": bool(
            kept and e3.get("S <-> S~, T <-> L^-1", {}).get("allowed weights and chi_k", {}).get("7/2") == 1
            and e3.get("S <-> S~^-1, T <-> L", {}).get("allowed weights and chi_k", {}).get("9/2") == 1),
        "E4: the calibrations give dimension 1 (eta, Weil)": e4["eta, M_1/2"][0] == 1 and e4["Weil, M_1/2"][0] == 1,
        "E4: the numerical dimensions agree with chi at every weight computed": bool(kept) and bool(agree),
    }
    out = {"status": "W45: the triplet's index on the weave's own surface (the rule first)",
           "E1: the structure": e1, "E2: the formula's calibration": e2, "E3: the four identifications": e3,
           "E3: the kept identifications and their chi_k": hands, "E4: the dimensions": e4,
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
