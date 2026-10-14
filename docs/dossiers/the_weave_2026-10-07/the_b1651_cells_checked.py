"""W85: main's B1651 cells (U2 to U5) checked on this seat's own code, before main's run lands. The rule (W85_RULE.md)
was committed before this script; the predictions and priors are there.

  V0  each unit's multipliers under z -> z + pi and z -> z + pi tau: i (+, -), j (-, +), k (-, -)
  V1  isotropy |v.v| / |v|^2 < 1e-40 at the seven points (an identity)
  V2  the half-periods' directions (0, -1, i), (i, 0, 1), (i, -1, 0) at every tau; the puncture and the generic points
      move with tau (best overlap over V4 between two tau < 1 - 1e-6)
  V3  L: v(z | tau + 1) = e^{i pi/4} Ad(g_L)^-1 v(z | tau) at the seven points, with no V4 element
  V4  R: v(-z/(tau + 1) | tau/(tau + 1)) is proportional to Ad(g_R) v(z | tau), with no V4 element, and the scalar is
      one number at the six regular points
  V5  the group of Ad(g_L) and Ad(g_R): 24 rotations, V4 the kernel on the axes, S3 the image; over the 16 V4-twisted
      pairs exactly four common eigenlines, the body diagonals (exact)
  V6  Ad(g_L) and Ad(g_R) equal W64's banked L and R on M, and Ad(g_L)^-1 equals W64's post hoc tau + 1 matrix (exact)

The thetas are summed from their series at 60 digits, in the pi z convention (periods pi and pi tau), with the nome root
e^{i pi tau / 4} explicit, so no principal branch enters; a control compares them with mpmath's jtheta at
|Re tau| < 1/2.
The triplet is v_r(z | tau) = c_r theta_r(0) theta_r(z) / theta_1(z), units (i, j, k) <-> thetas (2, 4, 3),
c = (-1, -1, i) (B1651's); at the puncture it is the residue triplet c_r theta_r(0)^2 / theta_1'(0).

Run: python3 the_b1651_cells_checked.py  ->  the_b1651_cells_checked.json beside it.
"""
import itertools
import json
import random
from pathlib import Path

import mpmath as mp
import sympy as sy

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
OUT = HERE / "the_b1651_cells_checked.json"
I = mp.mpc(0, 1)
C = [mp.mpc(-1), mp.mpc(-1), I]
TH = [2, 4, 3]
UNITS = ["i", "j", "k"]
TIGHT = mp.mpf(10) ** -40
LOOSE = mp.mpf(10) ** -6
TIE = mp.mpf(10) ** -12
HALF = {"1/2": (mp.mpf(1) / 2, mp.mpf(0)), "tau/2": (mp.mpf(0), mp.mpf(1) / 2),
        "(1+tau)/2": (mp.mpf(1) / 2, mp.mpf(1) / 2)}
GENERIC = {"g1": (mp.mpf("0.13"), mp.mpf("0.29")), "g2": (mp.mpf("0.41"), mp.mpf("0.07")),
           "g3": (mp.mpf("0.23"), mp.mpf("0.61"))}
LABELS = ["0", "1/2", "tau/2", "(1+tau)/2", "g1", "g2", "g3"]
DIRECTIONS = {"1/2": [0, -1, I], "tau/2": [I, 0, 1], "(1+tau)/2": [I, -1, 0]}
V4 = {"1": (1, 1, 1), "i": (1, -1, -1), "j": (-1, 1, -1), "k": (-1, -1, 1)}
PRED_L = {"0": "0", "1/2": "1/2", "tau/2": "(1+tau)/2", "(1+tau)/2": "tau/2"}
PRED_R = {"0": "0", "1/2": "(1+tau)/2", "tau/2": "tau/2", "(1+tau)/2": "1/2"}


def sign(n):
    return 1 if n % 2 == 0 else -1


def thetas(z, t):
    """(theta_1, theta_2, theta_3, theta_4)(z | t) from their series; q^(1/4) := e^{i pi t / 4}"""
    a = mp.pi * mp.im(t)
    b = abs(mp.im(z))
    target = (mp.mp.dps + 20) * mp.log(10)
    N = int((b + mp.sqrt(b * b + a * target)) / a) + 6
    s1 = s2 = s3 = s4 = mp.mpc(0)
    for n in range(-N, N + 1):
        e2 = mp.exp(2 * I * n * z)
        qn2 = mp.exp(I * mp.pi * t * n * n)
        s3 += qn2 * e2
        s4 += sign(n) * qn2 * e2
        e21 = mp.exp(I * (2 * n + 1) * z)
        qnn = mp.exp(I * mp.pi * t * (n * n + n))
        s2 += qnn * e21
        s1 += sign(n) * qnn * e21
    q4 = mp.exp(I * mp.pi * t / 4)
    return (-I * q4 * s1, q4 * s2, s3, s4)


def theta1_prime0(t):
    a = mp.pi * mp.im(t)
    N = int(mp.sqrt((mp.mp.dps + 20) * mp.log(10) / a)) + 6
    s = mp.mpc(0)
    for n in range(-N, N + 1):
        s += sign(n) * (2 * n + 1) * mp.exp(I * mp.pi * t * (n * n + n))
    return mp.exp(I * mp.pi * t / 4) * s


def point(label, t):
    """the point on the fibre t; None is the puncture"""
    if label == "0":
        return None
    m, n = HALF[label] if label in HALF else GENERIC[label]
    return mp.pi * (m + n * t)


def triplet_at(z, t):
    th0 = thetas(mp.mpc(0), t)
    if z is None:
        d = theta1_prime0(t)
        return [C[r] * th0[TH[r] - 1] ** 2 / d for r in range(3)]
    thz = thetas(z, t)
    return [C[r] * th0[TH[r] - 1] * thz[TH[r] - 1] / thz[0] for r in range(3)]


def apply(M, v):
    return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]


def overlap(u, w):
    num = abs(sum(mp.conj(a) * b for a, b in zip(u, w)))
    return num / (mp.sqrt(sum(abs(a) ** 2 for a in u)) * mp.sqrt(sum(abs(b) ** 2 for b in w)))


def rel(u, w):
    return max(abs(a - b) for a, b in zip(u, w)) / max(abs(a) for a in u)


def isotropy(v):
    return abs(sum(x * x for x in v)) / sum(abs(x) ** 2 for x in v)


def lattice_class(z, t):
    """z = pi (m + n t): the class of (2m, 2n) mod 2 as a fixed-point name, and the distance from the half-lattice"""
    w = z / mp.pi
    n = mp.im(w) / mp.im(t)
    m = mp.re(w) - n * mp.re(t)
    M2, N2 = int(mp.nint(2 * m)), int(mp.nint(2 * n))
    name = {(0, 0): "0", (1, 0): "1/2", (0, 1): "tau/2", (1, 1): "(1+tau)/2"}[(M2 % 2, N2 % 2)]
    return name, max(abs(2 * m - M2), abs(2 * n - N2))


def ad(w, x, y, z):
    M = sy.Matrix([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                   [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                   [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
    return M.applyfunc(sy.simplify)


S2 = 1 / sy.sqrt(2)
AL = ad(S2, S2, 0, 0)            # g_L = (1 + i)/sqrt2
AR = ad(S2, 0, -S2, 0)           # g_R = (1 - j)/sqrt2
ALi = AL.inv()


def as_int(M):
    return tuple(tuple(int(M[i, j]) for j in range(3)) for i in range(3))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def fl(x):
    return float(x)


def cpx(x):
    return [float(mp.re(x)), float(mp.im(x))]


def control(taus):
    worst = mp.mpf(0)
    for t in taus:
        q = mp.exp(I * mp.pi * t)
        for z in (mp.mpc("0.3", "0.2"), mp.mpc("1.1", "-0.15"), mp.mpc(0)):
            ours = thetas(z, t)
            for n in range(1, 5):
                ref = mp.jtheta(n, z, q)
                worst = max(worst, abs(ours[n - 1] - ref) / max(abs(ref), mp.mpf(1)))
        d = theta1_prime0(t)
        worst = max(worst, abs(d - mp.jtheta(1, 0, q, 1)) / abs(d))
    return {"worst relative difference against mpmath's jtheta": fl(worst), "holds": bool(worst < mp.mpf(10) ** -50)}


def V0(taus):
    want = {"i": (1, -1), "j": (-1, 1), "k": (-1, -1)}
    worst = mp.mpf(0)
    for t in taus:
        for g in GENERIC:
            z = point(g, t)
            v, va, vb = triplet_at(z, t), triplet_at(z + mp.pi, t), triplet_at(z + mp.pi * t, t)
            for r, u in enumerate(UNITS):
                worst = max(worst, abs(va[r] / v[r] - want[u][0]), abs(vb[r] / v[r] - want[u][1]))
    return {"predicted multipliers": want, "worst deviation": fl(worst), "holds": bool(worst < TIGHT)}


def V1(taus):
    worst = mp.mpf(0)
    rows = {}
    for t in taus:
        for lab in LABELS:
            x = isotropy(triplet_at(point(lab, t), t))
            worst = max(worst, x)
            rows[lab] = max(rows.get(lab, 0), fl(x))
    return {"worst |v.v| / |v|^2 per point": rows, "worst": fl(worst), "holds": bool(worst < TIGHT)}


def V2(taus):
    a_worst = mp.mpf(0)
    for t in taus:
        for lab, d in DIRECTIONS.items():
            a_worst = max(a_worst, 1 - overlap(triplet_at(point(lab, t), t), d))
    best = {}
    for lab in ["0", "g1", "g2", "g3"]:
        trip = [triplet_at(point(lab, t), t) for t in taus]
        b = mp.mpf(0)
        for x, y in itertools.combinations(range(len(taus)), 2):
            for D in V4.values():
                b = max(b, overlap(trip[x], [D[k] * trip[y][k] for k in range(3)]))
        best[lab] = fl(1 - b)
    control_holds = all(v > LOOSE for v in best.values())
    return {"worst 1 - overlap with the predicted directions": fl(a_worst),
            "the negative control: 1 - best overlap over V4 between two tau": best,
            "holds": bool(a_worst < TIGHT and control_holds)}


def ties(lhs, v, A):
    """for each power of the move, every V4 element whose overlap passes 1 - 1e-12"""
    out = {}
    for s, M in (("-1", as_int(A.inv())), ("+1", as_int(A))):
        w = apply(M, v)
        out[s] = [nm for nm, D in V4.items() if overlap(lhs, [D[k] * w[k] for k in range(3)]) > 1 - TIE]
    return out


def V3(taus):
    ph = mp.exp(I * mp.pi / 4)
    Mi = as_int(ALi)
    worst, rows, classes_ok, dist = mp.mpf(0), [], True, mp.mpf(0)
    for t in taus:
        for lab in LABELS:
            z = point(lab, t)
            v, lhs = triplet_at(z, t), triplet_at(z, t + 1)
            rhs = [ph * x for x in apply(Mi, v)]
            r = rel(lhs, rhs)
            worst = max(worst, r)
            row = {"tau": cpx(t), "point": lab, "relative residual": fl(r), "V4 ties": ties(lhs, v, AL)}
            if lab in HALF:
                name, d = lattice_class(z, t + 1)
                row["class on the new fibre"] = name
                classes_ok = classes_ok and name == PRED_L[lab]
                dist = max(dist, d)
            rows.append(row)
    no_v4 = all("1" in row["V4 ties"]["-1"] for row in rows)
    return {"worst relative residual": fl(worst), "the half-periods' classes as predicted": classes_ok,
            "their distance from the half-lattice": fl(dist), "s = -1 with no V4 element at every row": no_v4,
            "rows": rows, "holds": bool(worst < TIGHT and classes_ok and dist < TIGHT and no_v4)}


def V4cell(taus):
    M = as_int(AR)
    worst, spread, rows, classes_ok, dist = mp.mpf(0), mp.mpf(0), [], True, mp.mpf(0)
    for t in taus:
        tp = t / (t + 1)
        lams = []
        for lab in LABELS:
            z = point(lab, t)
            zp = None if z is None else -z / (t + 1)
            v, lhs = triplet_at(z, t), triplet_at(zp, tp)
            rhs = apply(M, v)
            lam = sum(mp.conj(a) * b for a, b in zip(rhs, lhs)) / sum(abs(a) ** 2 for a in rhs)
            o = 1 - overlap(lhs, rhs)
            worst = max(worst, o)
            row = {"tau": cpx(t), "point": lab, "1 - overlap": fl(o), "scalar": cpx(lam),
                   "V4 ties": ties(lhs, v, AR)}
            if lab != "0":
                lams.append(lam)
            if lab in HALF:
                name, d = lattice_class(zp, tp)
                row["class on the new fibre"] = name
                classes_ok = classes_ok and name == PRED_R[lab]
                dist = max(dist, d)
            rows.append(row)
        spread = max(spread, max(abs(x - lams[0]) for x in lams) / abs(lams[0]))
    no_v4 = all("1" in row["V4 ties"]["+1"] for row in rows)
    return {"worst 1 - overlap": fl(worst), "the scalar's spread over the six regular points": fl(spread),
            "the half-periods' classes as predicted": classes_ok, "their distance from the half-lattice": fl(dist),
            "s = +1 with no V4 element at every row": no_v4, "rows": rows,
            "holds": bool(worst < TIGHT and spread < TIGHT and classes_ok and dist < TIGHT and no_v4)}


def V5():
    L, R = as_int(AL), as_int(AR)
    E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    G, frontier = {E}, [E]
    while frontier:
        new = []
        for g in frontier:
            for h in (L, R):
                x = mul(g, h)
                if x not in G:
                    G.add(x)
                    new.append(x)
        frontier = new
    rotations = all(round(sy.Matrix(g).det()) == 1 for g in G)
    kernel = {g for g in G if all(g[i][j] == 0 for i in range(3) for j in range(3) if i != j)}
    v4 = {tuple(tuple(d[i] if i == j else 0 for j in range(3)) for i in range(3)) for d in V4.values()}

    def perm(g):
        return tuple(next(i for i in range(3) if g[i][j] != 0) for j in range(3))
    image = {perm(g) for g in G}
    lines, per_pair, dims_one, real = set(), {}, True, True
    for (n1, d1), (n2, d2) in itertools.product(V4.items(), V4.items()):
        A = sy.diag(*d1) * AL
        B = sy.diag(*d2) * AR
        found = []
        for lam in A.eigenvals():
            for mu in B.eigenvals():
                ns = (A - lam * sy.eye(3)).col_join(B - mu * sy.eye(3)).nullspace()
                if ns:
                    dims_one = dims_one and len(ns) == 1
                    vec = ns[0]
                    piv = next(x for x in reversed(list(vec)) if sy.simplify(x) != 0)
                    vec = (vec / piv).applyfunc(sy.simplify)
                    real = real and all(sy.im(x) == 0 for x in vec)
                    key = tuple(str(x) for x in vec)
                    found.append({"line": list(key), "eigenvalues": [str(lam), str(mu)]})
                    lines.add(key)
        per_pair[f"{n1}·L, {n2}·R"] = found
    diagonals = {tuple(str(x) for x in (r, s, 1)) for r in (1, -1) for s in (1, -1)}
    return {"rotations": len(G), "all of determinant 1": rotations, "the kernel on the axes is V4": kernel == v4,
            "the image on the axes": len(image), "common lines over the 16 twisted pairs": sorted(lines),
            "per pair": per_pair, "each joint eigenspace one-dimensional": dims_one, "real": real,
            "holds": bool(len(G) == 24 and rotations and kernel == v4 and len(image) == 6 and lines == diagonals
                          and dims_one and real)}


def V6():
    w64 = json.loads((HERE / "the_cusp_unit_as_a_vector.json").read_text(encoding="utf-8"))
    ph = json.loads((HERE / "the_cusp_unit_as_a_vector_posthoc.json").read_text(encoding="utf-8"))
    Lw = tuple(tuple(r) for r in w64["K1"]["L on M"])
    Rw = tuple(tuple(r) for r in w64["K1"]["R on M"])
    T1 = tuple(tuple(r) for r in ph["PH2 (K2 re-scored)"]["its matrix"])
    a, b, c = as_int(AL) == Lw, as_int(AR) == Rw, as_int(ALi) == T1
    return {"Ad(g_L) is W64's L": a, "Ad(g_R) is W64's R": b, "Ad(g_L)^-1 is W64's post hoc tau + 1 matrix": c,
            "holds": bool(a and b and c)}


def main():
    rng = random.Random(85)
    taus = [mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 1.8)) for _ in range(5)]
    out = {"status": "W85: main's B1651 cells checked on this seat's own theta series "
                     "(script committed before its one run)",
           "dps": mp.mp.dps, "taus": [cpx(t) for t in taus],
           "Ad(g_L)": [list(r) for r in as_int(AL)], "Ad(g_R)": [list(r) for r in as_int(AR)]}
    out["control"] = control(taus)
    out["V0"] = V0(taus)
    out["V1"] = V1(taus)
    out["V2"] = V2(taus)
    out["V3"] = V3(taus)
    out["V4"] = V4cell(taus)
    out["V5"] = V5()
    out["V6"] = V6()
    out["cells"] = {k: out[k]["holds"] for k in ("V0", "V1", "V2", "V3", "V4", "V5", "V6")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps({"control": out["control"]["holds"], **out["cells"]}, indent=1))


if __name__ == "__main__":
    main()
