"""Main's S92 verified with this seat's code: B1613 (TM1's forward prediction, falsifier P10) and B1614 (the observer layer
on the weave). A VERIFICATION, not blind: both read-outs were read first (main @ 6df00941).

B1613. TM1 is the column (2/3, 1/6, 1/6) of |U|^2 (W35 rebuilt it from W21). In the standard parametrization:
  |U_e1|^2 = c12^2 c13^2 = 2/3                      ->  sin^2 t12 = 1 - 2/(3 c13^2)
  |U_mu1|^2 - |U_tau1|^2 = (s12^2 - c12^2 s13^2) cos 2t23 + 2 s12 c12 s13 sin 2t23 cos d = 0
derived here from the matrix entries, and the Jarlskog J = s12 c12 s23 c23 s13 c13^2 sin d. Recomputed at B1613's inputs
(NuFIT 6.1 via the record's B1066: sin^2 t13 = 0.02248, sin^2 t23 = 0.470) at 50 digits, and the column checked on the
full matrix.

B1614. With exact arithmetic:
  - the moves' joint fixed points on the SL(2) character variety (x, y, z) = (tr a, tr b, tr ab);
  - for each local system at the common point (the trivial line, a parity line, the adjoint, the doublet, a matter
    block chi_p (x) rho_Q): dim H^1(F2; V) and the rank of the restriction to the puncture's H^1 = V/(rho(c) - 1)V, so
    the visible and the private parts;
  - the holomorphic triplet's characters at L, R and LR, with W21's lifts (on W21's T, through W35's construction);
  - the odd classes: det and the sign of the parities' permutation, as homomorphisms of <L, R, P> to F2.

Run: python3 the_tm1_prediction_and_observer_layer_verified.py  ->  .json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.polys.domains import QQ_I

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402  (the moves, their trace maps)
import the_observer_layer_on_the_weave as OL  # noqa: E402  (exact Q(i) linear algebra, rho_Q, Fox derivatives)

OUT = HERE / "the_tm1_prediction_and_observer_layer_verified.json"
mp.mp.dps = 50


# ---------------------------------------------------------------------------------------------- B1613
def U(t12, t13, t23, d):
    s12, c12, s13, c13, s23, c23 = mp.sin(t12), mp.cos(t12), mp.sin(t13), mp.cos(t13), mp.sin(t23), mp.cos(t23)
    e = mp.expj(d)
    return mp.matrix([[c12 * c13, s12 * c13, s13 / e],
                      [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                      [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def b1613():
    s13sq, s23sq = mp.mpf("0.02248"), mp.mpf("0.470")
    t13, t23 = mp.asin(mp.sqrt(s13sq)), mp.asin(mp.sqrt(s23sq))
    s12sq = 1 - mp.mpf(2) / (3 * mp.cos(t13) ** 2)
    t12 = mp.asin(mp.sqrt(s12sq))
    s12, c12, s13 = mp.sin(t12), mp.cos(t12), mp.sin(t13)
    cosd = -(s12 ** 2 - c12 ** 2 * s13 ** 2) * mp.cos(2 * t23) / (2 * s12 * c12 * s13 * mp.sin(2 * t23))
    d1 = mp.acos(cosd)
    out = {"inputs": {"sin^2 t13": "0.02248", "sin^2 t23": "0.470"},
           "sin^2 t12 (TM1)": mp.nstr(s12sq, 8), "theta23 (deg)": mp.nstr(mp.degrees(t23), 6),
           "cos delta": mp.nstr(cosd, 8)}
    branches = []
    for d in (d1, 2 * mp.pi - d1):
        M = U(t12, t13, t23, d)
        col = [abs(M[i, 0]) ** 2 for i in range(3)]
        dev = max(abs(col[0] - mp.mpf(2) / 3), abs(col[1] - mp.mpf(1) / 6), abs(col[2] - mp.mpf(1) / 6))
        J = mp.im(M[0, 0] * M[1, 1] * mp.conj(M[0, 1]) * mp.conj(M[1, 0]))
        Jf = s12 * c12 * mp.sin(t23) * mp.cos(t23) * s13 * mp.cos(t13) ** 2 * mp.sin(d)
        branches.append({"delta (deg)": mp.nstr(mp.degrees(d), 6), "the column's deviation from TM1": mp.nstr(dev, 3),
                         "J from the matrix": mp.nstr(J, 6), "J from the formula": mp.nstr(Jf, 6)})
    out["branches"] = branches
    out["checks"] = {
        "sin^2 t12 = 0.318": abs(s12sq - mp.mpf("0.318")) < mp.mpf("0.0005"),
        "cos delta = -0.1303": abs(cosd - mp.mpf("-0.13028")) < mp.mpf("0.00001"),
        "delta = 97.49 or 262.51": abs(mp.degrees(d1) - mp.mpf("97.49")) < mp.mpf("0.01"),
        "the TM1 column holds on both branches": all(mp.mpf(b["the column's deviation from TM1"]) < mp.mpf(10) ** -40
                                                     for b in branches),
        "J = +-0.03378": abs(abs(mp.mpf(branches[0]["J from the matrix"])) - mp.mpf("0.03378")) < mp.mpf("0.00001"),
    }
    return out


# ---------------------------------------------------------------------------------------------- B1614
def fixed_points():
    x, y, z = CP.x, CP.y, CP.z
    eqs = []
    for m in ("L", "R", "P"):
        T = CP.TR[m]
        eqs += [sp.expand(T[0] - x), sp.expand(T[1] - y), sp.expand(T[2] - z)]
    sols = sp.solve(eqs, [x, y, z], dict=True)
    return sorted({(int(s[x]), int(s[y]), int(s[z])) for s in sols})


def local_system(Ra, Rb):
    """H^1(F2; V) and the restriction to the puncture c = [a, b], for V given by the images of a and b (lists of rows)"""
    d = len(Ra)
    I = OL.eye(d)
    Ainv = OL.mscale(OL.adj2(Ra), OL.Z1 / OL.det2(Ra)) if d == 2 else [[OL.Z1 / Ra[0][0]]] if d == 1 else None
    Binv = OL.mscale(OL.adj2(Rb), OL.Z1 / OL.det2(Rb)) if d == 2 else [[OL.Z1 / Rb[0][0]]] if d == 1 else None
    if Ainv is None:
        Ainv = [list(r) for r in sp.Matrix([[sp.nsimplify(str(v)) for v in row] for row in Ra]).inv().tolist()]
    rho = {1: Ra, 2: Rb, -1: Ainv, -2: Binv}

    def word(w):
        M = I
        for t in w:
            M = OL.mmul(M, rho[t])
        return M

    # Fox derivatives of c = a b a^-1 b^-1
    pre, Fa, Fb = I, OL.zeros(d, d), OL.zeros(d, d)
    for t in OL.PUNCTURE:
        if t > 0:
            if t == 1:
                Fa = OL.madd(Fa, pre)
            else:
                Fb = OL.madd(Fb, pre)
            pre = OL.mmul(pre, rho[t])
        else:
            pre = OL.mmul(pre, rho[t])
            if t == -1:
                Fa = OL.madd(Fa, pre, -OL.Z1)
            else:
                Fb = OL.madd(Fb, pre, -OL.Z1)
    rc = word(OL.PUNCTURE)
    B = OL.vstack(OL.madd(Ra, I, -OL.Z1), OL.madd(Rb, I, -OL.Z1))
    rB = OL.rank(B)
    h1 = 2 * d - rB
    Rres = OL.hstack(Fa, Fb)
    Cc = OL.madd(rc, I, -OL.Z1)
    rank_res = OL.rank(OL.hstack(Rres, Cc)) - OL.rank(Cc)
    return {"dim V": d, "rho(c)": "1" if rc == I else ("-1" if rc == OL.mscale(I, -OL.Z1) else "other"),
            "dim H1": h1, "visible (rank to the puncture)": rank_res, "private": h1 - rank_res}


def b1614():
    Z1, ZI, Z0 = OL.Z1, OL.ZI, OL.Z0
    QI, QJ = OL.QI, OL.QJ
    chi = {"chi0": (1, 1), "chi1": (-1, 1), "chi2": (1, -1), "chi3": (-1, -1)}
    systems = {}
    for name, (ca, cb) in chi.items():
        systems["the line " + name] = local_system([[OL.q(ca)]], [[OL.q(cb)]])
    systems["the doublet rho_Q"] = local_system(QI, QJ)
    for name, (ca, cb) in list(chi.items())[1:]:
        systems["the matter block " + name + " (x) rho_Q"] = local_system(OL.mscale(QI, OL.q(ca)), OL.mscale(QJ, OL.q(cb)))
    adj = OL.Block(1)
    systems["the adjoint (Sym^2)"] = {"dim V": 3, "rho(c)": "1", "dim H1": adj.h1, "visible (rank to the puncture)":
                                      adj.rank_res, "private": adj.private}
    # the triplet's characters at L, R, LR (W21's lifts, W35's construction)
    import the_mixing_patterns_verified as MV
    named, _ = MV.H.triplets()
    C = named["T"]
    G0 = MV.H.gram_V()
    Qt = C.conj().T @ G0 @ C
    K = np.linalg.cholesky((Qt + Qt.conj().T) / 2).conj().T
    (_, gL, gR) = MV.H.lift_choices()[0]
    lifts = {"L": MV.CT.on_V(MV.CP.AUT["L"], gL), "R": MV.CT.on_V(MV.CP.AUT["R"], gR)}
    chars = {}
    for w in ("L", "R", "LR"):
        t = complex(np.trace(MV.on_T(C, K, MV.word(lifts, w))))
        chars[w] = [round(t.real, 9) + 0.0, round(t.imag, 9) + 0.0]
    e = np.exp(1j * np.pi / 4)
    # the odd classes: det and the sign of the parities' permutation on L, R, P (over F2: 1 = odd)
    def sgn(perm):
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
        return inv % 2

    mats = {m: OL.abel(CP.AUT[m]) for m in ("L", "R", "P")}
    classes = {m: ((0 if (M[0][0] * M[1][1] - M[0][1] * M[1][0]) == 1 else 1), sgn(OL.parity_perm(M))) for m, M in mats.items()}
    rank2 = len({v for v in classes.values() if v != (0, 0)}) >= 2 and classes["L"] != classes["P"]
    out = {"the moves' joint fixed points (x, y, z)": fixed_points(), "local systems at the common point": systems,
           "the triplet's characters at L, R, LR (re, im)": chars,
           "the odd classes (det, the parities' sign) on L, R, P": classes}
    out["checks"] = {
        "fixed points: the trivial character and the common point": out["the moves' joint fixed points (x, y, z)"] == [
            (0, 0, 0), (2, 2, 2)],
        "the adjoint and the parity lines wholly visible": all(
            v["private"] == 0 for k, v in systems.items() if k.startswith("the line chi") and k != "the line chi0") and
        systems["the adjoint (Sym^2)"]["private"] == 0,
        "the doublet and the matter blocks wholly private (H1 = 2 each)": all(
            v["dim H1"] == 2 and v["visible (rank to the puncture)"] == 0 for k, v in systems.items()
            if k.startswith("the doublet") or k.startswith("the matter")),
        "the trivial line wholly private": systems["the line chi0"]["private"] == systems["the line chi0"]["dim H1"] == 2,
        "chi_T(L) = e^(-i pi/4), chi_T(R) = e^(+i pi/4), chi_T(LR) = 0": (
            np.allclose(complex(*chars["L"]), np.conj(e), atol=1e-8) and np.allclose(complex(*chars["R"]), e, atol=1e-8)
            and np.allclose(complex(*chars["LR"]), 0, atol=1e-8)),
        "the odd classes have rank 2 over F2": rank2,
    }
    return out


def main():
    res = {"status": "VERIFICATION of main's B1613 and B1614 (read first), with this seat's code",
           "B1613": b1613(), "B1614": b1614()}
    res["every check holds"] = all(v for part in ("B1613", "B1614") for v in res[part]["checks"].values())
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
