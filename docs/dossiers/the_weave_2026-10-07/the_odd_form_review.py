"""W77: the audit lane's odd complementary form, reviewed on this seat's instruments. The rule (W77_RULE.md) was
committed before this script.

  R1  the frame brackets by the structure equations de^k = -1/2 C_ij^k e^i ^ e^j, from the lane's coframe
  R2  the spin connection by the Koszul formula: the cubic part of sum c_i omega_i and its linear part
  R3  the cross form {V, H} in the chiral gamma representation, by normal ordering with R1's brackets
  R4  K3 and K4: skew-Hermitian, anticommuting with GammaV = i c3 c4, K^dagger K with eigenvalues {1, 1, 0, 0}/ell^2
  R5  the identity 2 Re <V psi, H psi> = <psi, F psi>, inequality (1) and the cross bound on 40 numerical test sections
  plus the read-outs: the smallest margin of (1) relative to |psi|^2, the largest cross ratio

The operator, metric and hypotheses are the audit lane's (`surface_odd_form_2026_10_14`, `upstream_total_metric.py`).

Run: python3 the_odd_form_review.py  ->  the_odd_form_review.json beside it.
"""
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_odd_form_review.json"
x, y, u, v = sp.symbols("x y u v", real=True)
y = sp.Symbol("y", positive=True)
ell, A = sp.symbols("ell A", positive=True)
beta = sp.Symbol("beta", real=True)
X = (x, y, u, v)
COF = sp.Matrix([[ell / y, 0, 0, 0], [0, ell / y, 0, 0],
                 [0, 0, sp.sqrt(A / y), x * sp.sqrt(A / y)], [0, 0, 0, sp.sqrt(A * y)]])   # row k: e^k
FRAME = COF.inv().T.applyfunc(sp.simplify)                                                 # row i: E_i
STATED = {(0, 1, 0): -1 / ell, (1, 2, 2): 1 / (2 * ell), (0, 3, 2): -1 / ell, (1, 3, 3): -1 / (2 * ell)}


def brackets():
    """C[i][j][k] with [E_i, E_j] = C_ij^k E_k, from de^k(E_i, E_j) = -C_ij^k."""
    C = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    for k in range(4):
        dek = [[sp.diff(COF[k, b], X[a]) - sp.diff(COF[k, a], X[b]) for b in range(4)] for a in range(4)]
        for i in range(4):
            for j in range(4):
                val = sum(dek[a][b] * FRAME[i, a] * FRAME[j, b] for a in range(4) for b in range(4))
                C[i][j][k] = sp.simplify(-val)
    return C


def chiral_gammas():
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    Z2, I2 = sp.zeros(2), sp.eye(2)
    def blk(a, b, c, d):
        return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
    g = [blk(Z2, -sp.I * s, sp.I * s, Z2) for s in (s1, s2, s3)] + [blk(Z2, I2, I2, Z2)]
    return [sp.I * g[3], sp.I * g[0], sp.I * g[1], sp.I * g[2]]      # c1, c2, c3, c4


def r1(C):
    want = dict(STATED)
    want.update({(j, i, k): -val for (i, j, k), val in STATED.items()})
    bad = [[i, j, k, str(C[i][j][k])] for i in range(4) for j in range(4) for k in range(4)
           if sp.simplify(C[i][j][k] - want.get((i, j, k), 0)) != 0]
    return {"mismatches": bad, "holds": not bad}


def r2(C, c):
    sqrtg = sp.sqrt(sp.simplify(COF.T * COF).det())
    div = [sp.simplify(sum(sp.diff(sqrtg * FRAME[j, a], X[a]) for a in range(4)) / sqrtg) for j in range(4)]
    G = [[[sp.Rational(1, 2) * (C[i][j][k] - C[j][k][i] + C[k][i][j]) for k in range(4)] for j in range(4)]
         for i in range(4)]
    omega = [sum((G[i][j][k] * c[j] * c[k] / 4 for j in range(4) for k in range(4)), sp.zeros(4)) for i in range(4)]
    K = sum((c[i] * omega[i] for i in range(4)), sp.zeros(4)).applyfunc(sp.simplify)
    def coeff(M):
        return sp.simplify((M.H * K).trace() / 4)
    lin = [coeff(c[j]) for j in range(4)]
    cub = coeff(c[0] * c[2] * c[3])
    lin_pred = [sp.simplify(div[j] / 2) for j in range(4)]
    remainder = K - sum((lin[j] * c[j] for j in range(4)), sp.zeros(4)) - cub * c[0] * c[2] * c[3]
    remainder = remainder.applyfunc(sp.simplify)
    ok = (sp.simplify(cub - 1 / (4 * ell)) == 0 and all(sp.simplify(lin[j] - lin_pred[j]) == 0 for j in range(4))
          and sp.simplify(lin[1] + 1 / (2 * ell)) == 0 and all(sp.simplify(lin[j]) == 0 for j in (0, 2, 3)))
    return {"divergences": [str(d) for d in div], "linear coefficients": [str(t) for t in lin],
            "cubic c1c3c4 coefficient": str(cub), "remainder is zero": remainder == sp.zeros(4), "holds": bool(ok)}


def op_mul(P, Q, C):
    """Product of operators {(): const, (i,): coeff of E_i, (i, j) i <= j: coeff of E_i E_j}; coefficients constant."""
    R = {}
    def add(key, M):
        R[key] = R.get(key, sp.zeros(4)) + M
    for kp, A_ in P.items():
        for kq, B_ in Q.items():
            if len(kp) + len(kq) > 2:
                raise ValueError("first-order operators only")
            if kp == () or kq == ():
                add(kp + kq, A_ * B_)
                continue
            i, j = kp[0], kq[0]
            if i <= j:
                add((i, j), A_ * B_)
            else:
                add((j, i), A_ * B_)
                for k in range(4):
                    if C[i][j][k] != 0:
                        add((k,), A_ * B_ * C[i][j][k])
    return R


def r3_r4(C, c):
    c1, c2, c3, c4 = c
    V = {(2,): c3, (3,): c4}
    H = {(0,): c1, (1,): c2, (): -c2 / (2 * ell) + c1 * c3 * c4 / (4 * ell) + sp.I * beta * c1 / ell}
    PQ, QP = op_mul(V, H, C), op_mul(H, V, C)
    F = {k: (PQ.get(k, sp.zeros(4)) + QP.get(k, sp.zeros(4))).applyfunc(sp.simplify) for k in set(PQ) | set(QP)}
    K3 = (c2 * c3 - c1 * c4) / (2 * ell)
    K4 = -(c2 * c4 + c1 * c3) / (2 * ell)
    nonzero = sorted(str(k) for k, M in F.items() if M != sp.zeros(4))
    ok3 = (F.get((2,), sp.zeros(4)) - K3).applyfunc(sp.simplify) == sp.zeros(4)
    ok4 = (F.get((3,), sp.zeros(4)) - K4).applyfunc(sp.simplify) == sp.zeros(4)
    others = all(M == sp.zeros(4) for k, M in F.items() if k not in ((2,), (3,)))
    clifford = all(((c[i] * c[j] + c[j] * c[i]) + (2 * sp.eye(4) if i == j else sp.zeros(4))).applyfunc(sp.simplify)
                   == sp.zeros(4) for i in range(4) for j in range(4))
    r3 = {"Clifford relations (c^2 = -1) in the chiral representation": clifford, "nonzero terms of {V, H}": nonzero,
          "E3 coefficient = K3": ok3, "E4 coefficient = K4": ok4, "no other term": others,
          "holds": bool(clifford and ok3 and ok4 and others)}
    GV = sp.I * c3 * c4
    out4 = {}
    for name, K in (("K3", K3), ("K4", K4)):
        skew = (K.H + K).applyfunc(sp.simplify) == sp.zeros(4)
        flip = (GV * K + K * GV).applyfunc(sp.simplify) == sp.zeros(4)
        ev = sorted((sp.simplify(e * ell ** 2) for e, m in (K.H * K).eigenvals().items() for _ in range(m)),
                    key=lambda t: float(t))
        out4[name] = {"skew-Hermitian": skew, "anticommutes with GammaV": flip,
                      "eigenvalues of K^dagger K times ell^2": [str(e) for e in ev],
                      "ok": bool(skew and flip and ev == [0, 0, 1, 1])}
    out4["holds"] = all(out4[n]["ok"] for n in ("K3", "K4"))
    return r3, out4, (K3, K4)


def simpson_weights(n, h):
    w = np.ones(n)
    w[1:-1:2], w[2:-1:2] = 4, 2
    return w * h / 3


def r5(c, K3, K4):
    cn = [np.array(sp.N(m), dtype=complex) for m in c]
    k3 = np.array(sp.N(K3.subs(ell, 1)), dtype=complex)
    k4 = np.array(sp.N(K4.subs(ell, 1)), dtype=complex)
    c1, c2, c3, c4 = cn
    mixed = c1 @ c3 @ c4 / 4
    N = 501
    xs, ys = np.linspace(-1, 1, N), np.linspace(1, 4, N)
    Xg, Yg = np.meshgrid(xs, ys, indexing="ij")
    W = np.outer(simpson_weights(N, xs[1] - xs[0]), simpson_weights(N, ys[1] - ys[0])) / Yg ** 2   # ell^2 A / y^2
    rng = np.random.default_rng(75077)
    modes_all = [(m, n) for m in range(-2, 3) for n in range(-2, 3)]
    def ip(F, G):
        return complex(np.sum(W * np.einsum("aij,aij->ij", F.conj(), G)))
    rows = []
    for s in range(20):
        nmodes = int(rng.integers(2, 4))
        picks = rng.choice(len(modes_all), size=nmodes, replace=False)
        prof = []
        for p in picks:
            bumps = [(rng.uniform(-0.5, 0.5), rng.uniform(1.5, 3.0),
                      rng.normal(size=4) + 1j * rng.normal(size=4)) for _ in range(2)]
            prof.append((modes_all[p], bumps))
        for b in (0.0, 0.75):
            tot = {"D": 0.0, "V": 0.0, "H": 0.0, "F": 0.0, "0": 0.0}
            for (m, n), bumps in prof:
                F0 = np.zeros((4, N, N), complex)
                Fx = np.zeros((4, N, N), complex)
                Fy = np.zeros((4, N, N), complex)
                for x0, y0, chi in bumps:
                    g = np.exp(-((Xg - x0) ** 2 + (Yg - y0) ** 2) / (2 * 0.12 ** 2))
                    F0 += chi[:, None, None] * g
                    Fx += chi[:, None, None] * g * (-(Xg - x0) / 0.12 ** 2)
                    Fy += chi[:, None, None] * g * (-(Yg - y0) / 0.12 ** 2)
                e3 = np.sqrt(Yg) * 2j * np.pi * m                      # E3 = sqrt(y/A) d_u, A = 1
                e4 = 2j * np.pi * (n - Xg * m) / np.sqrt(Yg)           # E4 = (d_v - x d_u)/sqrt(A y)
                def mat(M, G):
                    return np.einsum("ab,bij->aij", M, G)
                Vp = mat(c3, F0) * e3 + mat(c4, F0) * e4
                Hp = (mat(c1, Fx) * Yg + mat(c2, Fy) * Yg - mat(c2, F0) / 2 + mat(mixed, F0) + 1j * b * mat(c1, F0))
                Fp = mat(k3, F0) * e3 + mat(k4, F0) * e4
                tot["D"] += ip(Vp + Hp, Vp + Hp).real
                tot["V"] += ip(Vp, Vp).real
                tot["H"] += ip(Hp, Hp).real
                tot["F"] += ip(F0, Fp).real
                tot["0"] += ip(F0, F0).real
            ident = abs(tot["D"] - tot["V"] - tot["H"] - tot["F"]) / tot["D"]
            margin = (tot["D"] - tot["V"] / 2 - tot["H"] + 4 * tot["0"]) / tot["0"]
            cross = abs(tot["F"]) / (2 * math.sqrt(2) * math.sqrt(tot["0"] * tot["V"]))
            rows.append({"section": s, "beta": b, "identity residual": ident, "margin of (1) / |psi|^2": margin,
                         "cross ratio": cross})
    ok = (all(r["identity residual"] < 1e-6 for r in rows) and all(r["margin of (1) / |psi|^2"] >= 0 for r in rows)
          and all(r["cross ratio"] <= 1 for r in rows))
    return {"pairs": len(rows), "largest identity residual": max(r["identity residual"] for r in rows),
            "rows": rows, "holds": bool(ok)}


def main():
    out = {"status": "W77: the audit lane's odd form, reviewed (the rule W77_RULE.md first; one run)"}
    C = brackets()
    c = chiral_gammas()
    out["R1"] = r1(C)
    out["R2"] = r2(C, c)
    out["R3"], out["R4"], (K3, K4) = r3_r4(C, c)
    out["R5"] = r5(c, K3, K4)
    rows = out["R5"]["rows"]
    out["read-outs"] = {"smallest margin of (1) / |psi|^2": min(r["margin of (1) / |psi|^2"] for r in rows),
                        "largest cross ratio": max(r["cross ratio"] for r in rows)}
    out["cells"] = {k: out[k]["holds"] for k in ("R1", "R2", "R3", "R4", "R5")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
