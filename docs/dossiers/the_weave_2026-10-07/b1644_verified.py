"""W63: main's B1644 (a Higgs in the multiplicity space M couples to the zero modes at the puncture) and B1645 (the half
bound) verified with the seat's own instruments; main's P-115 answered from the record. The rule (W63_RULE.md) was
committed before this script.

  V1  the residues of F^T eps u F: a contour route and the duplication closed forms; main's table; W21's branch
  V2  the structure: Y(a) symmetric, a non-zero diagonal, and Y(a) = a R^T + R a^T - (a.R) 1 in the units' labels
  V3  Jacobi: R.R = 0, Y(a) R = 0, det Y(a) = 0
  V4  the half bound for real directions; m = 1/2 in R's plane and 1 normal to it; m = 0 on the isotropic cone; the
      slope near the cone
  V5  W60's Higgs as a direction (P-115): m(e_u) >= 1/2; m(e_k) = 1/2 on the imaginary axis
  V6  main's printed S3c examples at tau = 4i
  plus the read-outs: m at omega and on W62's axis, R at the cusp, how near the cone the data's ratios would need

Run: python3 b1644_verified.py  ->  b1644_verified.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_holomorphic_triplet_periods as PS  # noqa: E402  (W21: the zero mode's branch by continuation)

OUT = HERE / "b1644_verified.json"
W62 = json.loads((HERE / "the_matter_and_the_shape.json").read_text(encoding="utf-8"))
MAIN = json.loads((HERE / "received" / "B1644_S3c_examples.json").read_text(encoding="utf-8"))
mp.mp.dps = 30
I = mp.mpc(0, 1)
QI = mp.matrix([[I, 0], [0, -I]])
QJ = mp.matrix([[0, 1], [-1, 0]])
QK = QI * QJ
EPS = QJ
UNITS = {"i": QI, "j": QJ, "k": QK}
BLOCKS = [("i", QI), ("j", QJ), ("k", QK)]  # the generations labelled by their units: (0, 1/2), (1/2, 0), (1/2, 1/2)
RAD, NPTS = mp.mpf("0.04"), 96


def th(n, z, t):
    """theta_n(z | t) with theta_1(z + 1) = -theta_1(z), by mpmath's jtheta"""
    return mp.jtheta(n, mp.pi * z, mp.exp(I * mp.pi * t))


def basic(z, t):
    """the single-valued products f^2, f f' (main's branch, c = i e^{-i pi t / 2}) and f'^2, with f' = f(z + t)"""
    a, b = th(3, z, 2 * t), th(3, z + t, 2 * t)
    t1 = th(1, z, t)
    return a * a / t1, a * b / (I * mp.exp(-I * mp.pi * t / 2) * mp.exp(-I * mp.pi * z) * t1), b * b / th(1, z + t, t)


def residues(t):
    s = [mp.mpc(0)] * 3
    for n in range(NPTS):
        z = RAD * mp.exp(2 * I * mp.pi * n / NPTS)
        for k, v in enumerate(basic(z, t)):
            s[k] += v * z
    return [x / NPTS for x in s]


def closed(t):
    t2, t3, t4 = th(2, 0, t), th(3, 0, t), th(4, 0, t)
    D = mp.pi * t2 * t3 * t4
    return [(t3 ** 2 + t4 ** 2) / (2 * D), -I * t2 ** 2 / (2 * D), -(t3 ** 2 - t4 ** 2) / (2 * D)], (t2, t3, t4, D)


def eta3(t):
    q = mp.exp(I * mp.pi * t)
    return (q ** (mp.mpf(1) / 12) * mp.nprod(lambda n: 1 - q ** (2 * n), [1, mp.inf])) ** 3


def res_of(M, r):
    """Res F^T M F from the three basic residues"""
    return M[0, 0] * r[0] + (M[0, 1] + M[1, 0]) * r[1] + M[1, 1] * r[2]


def Y_of(a, r):
    Phi = a[0] * QI + a[1] * QJ + a[2] * QK
    Y = mp.matrix(3, 3)
    for p, (_, Cp) in enumerate(BLOCKS):
        for q, (_, Cq) in enumerate(BLOCKS):
            Y[p, q] = res_of(Cp.T * EPS * Phi * Cq, r)
    return Y


def R_of(r):
    return [res_of(EPS * U, r) for U in (QI, QJ, QK)]


def to_np(M):
    return np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def m_of(Y):
    s = np.linalg.svd(Y, compute_uv=False)
    return float(s[1] / s[0]), [float(x / s[0]) for x in s]


def taus():
    rng = np.random.default_rng(6301)
    axis = [m for m in W62["the family"]["members"] if m[0] == "axis y = 2.0207"][0][4]
    out = {"i": mp.mpc(0, 1), "omega": mp.mpc(-0.5, mp.sqrt(3) / 2), "4i": mp.mpc(0, 4),
           "2.0207i (W62)": mp.mpc(axis[0], axis[1])}
    while len(out) < 10:
        x, y = rng.uniform(-0.5, 0.5), rng.uniform(0.8, 2.0)
        if x * x + y * y >= 1:
            out[f"random {len(out) - 3}"] = mp.mpc(x, y)
    return out


def w21_signs(t):
    """the cross term's sign in W21's F: (a) principal roots per factor at 20 points on the contour, as W61's Q3
    evaluates F; (b) W21's continuation from its base point, as its periods() fixes the branch"""
    c = I * mp.exp(-I * mp.pi * t / 2)
    pr = []
    for n in range(20):
        z = RAD * mp.exp(2 * I * mp.pi * (n + 0.5) / 20)
        prod = mp.sqrt(th(1, z, t)) * mp.sqrt(th(1, z + t, t))
        pr.append(int(round(float(mp.re(prod / (c * mp.exp(-I * mp.pi * z) * th(1, z, t)))))))
    x0 = PS.ALPHA + PS.BETA * t
    s = mp.sqrt(th(1, x0, t))
    nst = 2000
    for k in range(1, nst + 1):
        r = mp.sqrt(th(1, x0 + t * k / nst, t))
        s = -r if abs(r - s) > abs(r + s) else r
    cont = mp.sqrt(th(1, x0, t)) * s / (c * mp.exp(-I * mp.pi * x0) * th(1, x0, t))
    return pr, int(round(float(mp.re(cont))))


def main():
    T = taus()
    rng = np.random.default_rng(6302)
    cplx = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(5)]
    out = {"status": "W63: B1644 and B1645 verified with the seat's own instruments; P-115 answered (the rule "
                     "W63_RULE.md first; one run)", "taus": {k: [float(v.real), float(v.imag)] for k, v in T.items()}}
    v1, v2, v3, v4 = {}, {}, {}, {}
    ok1 = ok2 = ok3 = ok4 = True
    Rs = {}
    for name, t in T.items():
        r = residues(t)
        rc, (t2, t3, t4, D) = closed(t)
        dev = max(abs(r[k] - rc[k]) / abs(rc[k]) for k in range(3))
        R = R_of(r)
        Rs[name] = R
        main_tab = [-t2 ** 2 / D, -t4 ** 2 / D, I * t3 ** 2 / D]
        mdev = max(abs(R[k] - main_tab[k]) / abs(main_tab[k]) for k in range(3))
        zero = abs(res_of(EPS * mp.eye(2), r)) / abs(R[0])
        etad = abs(2 * mp.pi * eta3(t) / D - 1)
        pr, cont = w21_signs(t)
        v1[name] = {"contour against closed forms (relative)": float(dev), "R against main's table (relative)":
                    float(mdev), "Res F^T eps F / |R_i|": float(zero), "2 pi eta^3 / (pi th2 th3 th4) - 1": float(etad),
                    "W21 principal-root signs at 20 contour points": pr, "W21 continuation sign": cont}
        ok1 &= dev < 1e-20 and mdev < 1e-20 and zero < 1e-20 and etad < 1e-20 and len(set(pr)) == 1
        # V2, V3
        nR = mp.sqrt(sum(abs(x) ** 2 for x in R))
        RR = abs(sum(x * x for x in R)) / nR ** 2
        worst = {"asym": 0.0, "form": 0.0, "YR": 0.0, "det": 0.0, "min diag": 1.0}
        dirs = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] + [[mp.mpc(c.real, c.imag) for c in a] for a in cplx]
        for a in dirs:
            a = [mp.mpc(x) for x in a]
            Y = Y_of(a, r)
            nY = max(abs(Y[i, j]) for i in range(3) for j in range(3))
            aR = sum(a[k] * R[k] for k in range(3))
            form = max(abs(Y[i, j] - (a[i] * R[j] + R[i] * a[j] - (aR if i == j else 0))) for i in range(3)
                       for j in range(3)) / nY
            worst["asym"] = max(worst["asym"], float(max(abs(Y[i, j] - Y[j, i]) for i in range(3)
                                                         for j in range(3)) / nY))
            worst["form"] = max(worst["form"], float(form))
            worst["min diag"] = min(worst["min diag"], float(min(abs(Y[i, i]) for i in range(3)) / nY))
            YR = max(abs(sum(Y[i, j] * R[j] for j in range(3))) for i in range(3)) / (nY * nR)
            worst["YR"] = max(worst["YR"], float(YR))
            worst["det"] = max(worst["det"], float(abs(mp.det(Y)) / nY ** 3))
        v2[name] = {k: worst[k] for k in ("asym", "form", "min diag")}
        v3[name] = {"|R.R| / |R|^2": float(RR), "Y(a) R": worst["YR"], "det Y(a)": worst["det"]}
        ok2 &= worst["asym"] < 1e-20 and worst["form"] < 1e-20 and worst["min diag"] > 1e-6
        ok3 &= RR < 1e-20 and worst["YR"] < 1e-20 and worst["det"] < 1e-20
        # V4
        Yu = [to_np(Y_of([1 if k == u else 0 for k in range(3)], r)) for u in range(3)]
        Rn = np.array([complex(x) for x in R])
        Ya = lambda a: sum(a[k] * Yu[k] for k in range(3))  # noqa: E731
        N = 2000
        ms = []
        for n in range(N):
            zc = 1 - 2 * (n + 0.5) / N
            rr = math.sqrt(1 - zc * zc)
            ph = n * math.pi * (3 - math.sqrt(5))
            ms.append(m_of(Ya(np.array([rr * math.cos(ph), rr * math.sin(ph), zc])))[0])
        re_, im_ = Rn.real, Rn.imag
        plane = [m_of(Ya(math.cos(f) * re_ / np.linalg.norm(re_) + math.sin(f) * im_ / np.linalg.norm(im_)))[0]
                 for f in np.linspace(0.1, 3.0, 10)]
        normal = m_of(Ya(np.cross(re_, im_)))[0]
        cone = []
        slopes = []
        for _ in range(200):
            u = rng.normal(size=3)
            v = rng.normal(size=3)
            v -= (v @ u) / (u @ u) * u
            v *= np.linalg.norm(u) / np.linalg.norm(v)
            a0 = u + 1j * v
            cone.append(m_of(Ya(a0))[0])
            if len(slopes) < 3:
                b = rng.normal(size=3) + 1j * rng.normal(size=3)
                xs, mv = [], []
                for dl in (1e-2, 1e-3, 1e-4):
                    a = a0 + dl * b
                    xs.append(abs(a @ a) / np.linalg.norm(a) ** 2)
                    mv.append(m_of(Ya(a))[0])
                slopes.append(float(np.polyfit(np.log(xs), np.log(mv), 1)[0]))
        v4[name] = {"min m (real)": min(ms), "max m (real)": max(ms), "m in R's plane (largest |m - 1/2|)":
                    max(abs(x - 0.5) for x in plane), "m normal to R's plane": normal, "max m on the cone": max(cone),
                    "slopes near the cone": slopes}
        ok4 &= (min(ms) >= 0.5 - 1e-10 and max(ms) <= 1 + 1e-12 and max(abs(x - 0.5) for x in plane) < 1e-10
                and abs(normal - 1) < 1e-10 and max(cone) < 1e-10 and all(abs(s - 1) < 0.02 for s in slopes))
    out.update({"V1": dict(v1, holds=bool(ok1)), "V2": dict(v2, holds=bool(ok2)), "V3": dict(v3, holds=bool(ok3)),
                "V4": dict(v4, holds=bool(ok4))})

    # V5
    pts = {"i": mp.mpc(0, 1), "1.5i": mp.mpc(0, 1.5), "2.0207i": T["2.0207i (W62)"], "4i": mp.mpc(0, 4),
           "omega": T["omega"]}
    for m in W62["the family"]["members"]:
        if m[0].startswith("arc"):
            pts[m[0]] = mp.mpc(m[4][0], m[4][1])
    v5, ok5 = {}, True
    for name, t in pts.items():
        r = residues(t)
        row = {}
        for u, e in (("i", [1, 0, 0]), ("j", [0, 1, 0]), ("k", [0, 0, 1])):
            row[u] = m_of(to_np(Y_of(e, r)))[0]
        v5[name] = row
        ok5 &= min(row.values()) >= 0.5 - 1e-10
        if name in ("i", "1.5i", "2.0207i", "4i"):
            ok5 &= abs(row["k"] - 0.5) < 1e-10
    out["V5"] = dict(v5, holds=bool(ok5))

    # V6
    r = residues(mp.mpc(0, 4))
    Yu = [to_np(Y_of(e, r)) for e in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]
    N = 400
    dirs = []
    for n in range(N):
        zc = 1 - 2 * (n + 0.5) / N
        rr = math.sqrt(1 - zc * zc)
        ph = n * math.pi * (3 - math.sqrt(5))
        dirs.append(np.array([rr * math.cos(ph), rr * math.sin(ph), zc]))
    rows, ok6 = [], True
    for ex in MAIN["examples"]:
        match = [a for a in dirs if [round(float(x), 4) for x in a] == ex[:3]]
        if len(match) != 1:
            rows.append({"printed": ex, "matched directions": len(match)})
            ok6 = False
            continue
        _, s = m_of(sum(match[0][k] * Yu[k] for k in range(3)))
        d = max(abs(s[k] - ex[3 + k]) for k in range(3))
        rows.append({"printed": ex, "the seat's": s, "largest difference": d})
        ok6 &= d < 1e-7
    out["V6"] = {"rows": rows, "holds": bool(ok6)}

    out["cells"] = {k: out[k]["holds"] for k in ("V1", "V2", "V3", "V4", "V5", "V6")}
    out["every cell holds"] = all(out["cells"].values())
    out["read-outs"] = readouts(T, out)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


def readouts(T, out):
    ro = {"m(e_u) at omega": out["V5"]["omega"]}
    axis = {}
    for m in W62["the family"]["members"]:
        if m[0].startswith("axis"):
            r = residues(mp.mpc(m[4][0], m[4][1]))
            axis[m[0]] = {u: m_of(to_np(Y_of(e, r)))[0] for u, e in (("i", [1, 0, 0]), ("j", [0, 1, 0]),
                                                                     ("k", [0, 0, 1]))}
    ro["m(e_u) on W62's axis members"] = axis
    cusp = {}
    for y in (4, 8):
        R = R_of(residues(mp.mpc(0, y)))
        nR = mp.sqrt(sum(abs(x) ** 2 for x in R))
        cusp[f"{y}i"] = {"R / |R|": [[float(mp.re(x / nR)), float(mp.im(x / nR))] for x in R],
                         "R_i / R_j": [float(mp.re(R[0] / R[1])), float(mp.im(R[0] / R[1]))],
                         "R_k / R_j": [float(mp.re(R[2] / R[1])), float(mp.im(R[2] / R[1]))]}
    ro["R toward the cusp (main's limit (0, -1, i) up to scale)"] = cusp
    rng = np.random.default_rng(6303)
    near = {}
    for name in ("i", "4i"):
        r = residues(T[name])
        Yu = [to_np(Y_of(e, r)) for e in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]
        u = rng.normal(size=3)
        v = rng.normal(size=3)
        v -= (v @ u) / (u @ u) * u
        v *= np.linalg.norm(u) / np.linalg.norm(v)
        a0 = u + 1j * v
        b = rng.normal(size=3) + 1j * rng.normal(size=3)
        cs = []
        for dl in (1e-2, 1e-3):
            a = a0 + dl * b
            x = abs(a @ a) / np.linalg.norm(a) ** 2
            cs.append(m_of(sum(a[k] * Yu[k] for k in range(3)))[0] / x)
        C = float(np.mean(cs))
        near[name] = {"m / (|a.a| / |a|^2) near the cone": cs,
                      "|a.a| / |a|^2 for m = 0.004, 0.02, 0.06": [0.004 / C, 0.02 / C, 0.06 / C]}
    ro["how near the cone the data's ratios would need (context, not a test)"] = near
    return ro


if __name__ == "__main__":
    main()
