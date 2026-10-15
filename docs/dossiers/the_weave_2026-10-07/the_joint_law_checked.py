"""W96: main's B1659 (the joint law, P-168; sealed f4b12d788, not yet run) on this seat's own code, blind to main's
output. The rule (W96_RULE.md) was committed before this script; the predictions and priors are there. No data.

  Q1  J1, sympy: det Y - 4 det S det M tr(eps S M^T) = 0 over eight complex symbols, on W93's frame
  Q2  J2, sympy: adj Y - det S A(M) - det M P A(S) = 0, with main's A as copied in the rule
  Q3  J2b: A(p q^T) = q~ p~^T exactly (and not p~ q~^T); numerically on 200 null M: adj Y = det S A(M), ||A|| = 2||M||^2
  Q4  J2c, sympy: Y(S, N eps^-1) = Y(N, S eps^-1); tr(eps S M^T) + polar(S, N) = 0 at M = N eps^-1;
      det(N eps^-1) = det N
  Q5  the corollaries at 40 draws each: null M, null S, S = M give m1/m3 < 1e-12; N = S is geometric;
      m1 = |det Y|/(m2 m3)
  Q6  on this seat's sector matter at omega under P4' (W93's residues, 40 digits): J1 and J2 hold; every sector null
  Q7  controls that can fail: a 10% perturbation breaks J1; A in place of P A breaks J2; N != S is not geometric
  read-outs: the pairing's size on the sector matter; the range of m1/m3 off the null cone

Q1-Q5 and Q7 are identities of the frame; Q6 is read at one tau (omega): a frozen piece. Built on W93's frame.

Run: python3 the_joint_law_checked.py  ->  the_joint_law_checked.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_twisted_half_bound_checked as W93  # noqa: E402

OUT = HERE / "the_joint_law_checked.json"
mp.mp.dps = 40


def A_of(M, I):
    """main's quadratic A(M) (B1659's preregistration, section 1), for M = [[m0, m1], [m2, m3]]"""
    m0, m1, m2, m3 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return [[m0 ** 2 + m1 ** 2 + m2 ** 2 + m3 ** 2, 2 * I * (m0 * m2 + m1 * m3),
             -I * (m0 ** 2 + m1 ** 2 - m2 ** 2 - m3 ** 2)],
            [2 * I * (m0 * m1 + m2 * m3), -4 * m1 * m2, 2 * (m0 * m1 - m2 * m3)],
            [-I * (m0 ** 2 - m1 ** 2 + m2 ** 2 - m3 ** 2), 2 * (m0 * m2 - m1 * m3),
             -m0 ** 2 + m1 ** 2 + m2 ** 2 - m3 ** 2]]


def tilde(p, I):
    return [p[0] ** 2 + p[1] ** 2, 2 * I * p[0] * p[1], -I * (p[0] ** 2 - p[1] ** 2)]


PDIAG = (1, -1, -1)


# ------------------------------------------------------------------------------------------------ sympy
QI_s = sp.Matrix([[sp.I, 0], [0, -sp.I]])
QJ_s = sp.Matrix([[0, 1], [-1, 0]])
QK_s = QI_s * QJ_s
EPS_s = QJ_s
EPSI_s = -QJ_s
BLK_s = [QJ_s, QI_s, QK_s]


def Y_sym(S, M):
    return sp.Matrix(3, 3, lambda a, b: sum(((BLK_s[a].T * EPS_s * S * BLK_s[b])[m, n] * M[m, n])
                                            for m in range(2) for n in range(2)))


def symbolic():
    s = sp.symbols("s0:4")
    m = sp.symbols("m0:4")
    S = sp.Matrix([[s[0], s[1]], [s[2], s[3]]])
    M = sp.Matrix([[m[0], m[1]], [m[2], m[3]]])
    Y = Y_sym(S, M)
    trp = (EPS_s * S * M.T).trace()
    q1 = sp.expand(Y.det() - 4 * S.det() * M.det() * trp) == 0
    AM, AS = sp.Matrix(A_of(M, sp.I)), sp.Matrix(A_of(S, sp.I))
    PAS = sp.Matrix(3, 3, lambda i, j: PDIAG[i] * AS[i, j])
    q2 = sp.expand(Y.adjugate() - S.det() * AM - M.det() * PAS) == sp.zeros(3, 3)
    p = sp.symbols("p0:2")
    q = sp.symbols("q0:2")
    Mn = sp.Matrix(2, 1, list(p)) * sp.Matrix(1, 2, list(q))
    An = sp.Matrix(A_of(Mn, sp.I))
    pt, qt = sp.Matrix(tilde(p, sp.I)), sp.Matrix(tilde(q, sp.I))
    q3_exact = sp.expand(An - qt * pt.T) == sp.zeros(3, 3)
    q3_transposed_differs = sp.expand(An - pt * qt.T) != sp.zeros(3, 3)
    N = M
    Mfrom = N * EPSI_s
    q4_sym = sp.expand(Y_sym(S, N * EPSI_s) - Y_sym(N, S * EPSI_s)) == sp.zeros(3, 3)
    polar = (S + N).det() - S.det() - N.det()
    q4_polar = sp.expand((EPS_s * S * Mfrom.T).trace() + polar) == 0
    q4_det = sp.expand(Mfrom.det() - N.det()) == 0
    return {"Q1": {"det Y - 4 det S det M tr(eps S M^T) == 0": q1, "holds": bool(q1)},
            "Q2": {"adj Y - det S A(M) - det M P A(S) == 0": q2, "holds": bool(q2)},
            "Q3 exact": {"A(p q^T) == q~ p~^T": q3_exact, "A(p q^T) != p~ q~^T": q3_transposed_differs},
            "Q4": {"Y(S, N eps^-1) == Y(N, S eps^-1)": q4_sym, "tr(eps S M^T) + polar(S, N) == 0": q4_polar,
                   "det(N eps^-1) == det N": q4_det, "holds": bool(q4_sym and q4_polar and q4_det)}}


# ------------------------------------------------------------------------------------------------ numpy
EPSN = W93.EPSN
EPSIN = -W93.EPSN


def A_np(M):
    return np.array(A_of(M, 1j))


def PA_np(M):
    return np.diag(PDIAG) @ A_np(M)


def svals(Y):
    return np.sort(np.linalg.svd(Y, compute_uv=False))


def cplx(rng, shape):
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


def numeric(rng):
    fro = np.linalg.norm
    # Q3 numeric
    worst_adj, worst_norm = 0.0, 0.0
    for _ in range(200):
        p, q = cplx(rng, 2), cplx(rng, 2)
        M = np.outer(p, q)
        S = cplx(rng, (2, 2))
        Y = W93.coupling_np(S, M)
        worst_adj = max(worst_adj, fro(W93.adjugate(Y) - np.linalg.det(S) * A_np(M)) / fro(Y) ** 2)
        worst_norm = max(worst_norm, abs(fro(A_np(M)) - 2 * fro(M) ** 2) / fro(M) ** 2)
    q3 = {"200 null M: max ||adj Y - det S A(M)|| / ||Y||^2": worst_adj,
          "max | ||A(M)|| - 2||M||^2 | / ||M||^2": worst_norm}
    # Q5
    r = {"null M": [], "null S": [], "S = M": [], "N = S geometric": [], "m1 = |det Y|/(m2 m3)": [],
         "generic m1/m3": []}
    for _ in range(40):
        S = cplx(rng, (2, 2))
        M = np.outer(cplx(rng, 2), cplx(rng, 2))
        s = svals(W93.coupling_np(S, M)); r["null M"].append(s[0] / s[2])
        S0 = np.outer(cplx(rng, 2), cplx(rng, 2)); M0 = cplx(rng, (2, 2))
        s = svals(W93.coupling_np(S0, M0)); r["null S"].append(s[0] / s[2])
        S1 = cplx(rng, (2, 2))
        s = svals(W93.coupling_np(S1, S1)); r["S = M"].append(s[0] / s[2])
        S2 = cplx(rng, (2, 2))
        s = svals(W93.coupling_np(S2, S2 @ EPSIN)); r["N = S geometric"].append(abs(s[0] * s[2] / s[1] ** 2 - 1))
        S3, M3 = cplx(rng, (2, 2)), cplx(rng, (2, 2))
        Y = W93.coupling_np(S3, M3); s = svals(Y)
        r["m1 = |det Y|/(m2 m3)"].append(abs(abs(np.linalg.det(Y)) / (s[1] * s[2]) / s[0] - 1))
        r["generic m1/m3"].append(s[0] / s[2])
    q5 = {"max m1/m3, null M": max(r["null M"]), "max m1/m3, null S": max(r["null S"]),
          "max m1/m3, S = M": max(r["S = M"]), "max |m1 m3/m2^2 - 1| at N = S": max(r["N = S geometric"]),
          "max relative error of m1 = |det Y|/(m2 m3)": max(r["m1 = |det Y|/(m2 m3)"])}
    q5["holds"] = bool(q5["max m1/m3, null M"] < 1e-12 and q5["max m1/m3, null S"] < 1e-12
                       and q5["max m1/m3, S = M"] < 1e-12 and q5["max |m1 m3/m2^2 - 1| at N = S"] < 1e-10
                       and q5["max relative error of m1 = |det Y|/(m2 m3)"] < 1e-10)
    readout5 = {"generic m1/m3: min": min(r["generic m1/m3"]), "max": max(r["generic m1/m3"])}
    # Q7
    j1v, j2v, geo = [], [], []
    for _ in range(40):
        S, M = cplx(rng, (2, 2)), cplx(rng, (2, 2))
        Y = W93.coupling_np(S, M)
        E = cplx(rng, (3, 3))
        Yp = Y + 0.1 * fro(Y) * E / fro(E)
        lhs = 4 * np.linalg.det(S) * np.linalg.det(M) * np.trace(EPSN @ S @ M.T)
        j1v.append(abs(np.linalg.det(Yp) - lhs) / fro(Y) ** 3)
        j2v.append(fro(W93.adjugate(Y) - np.linalg.det(S) * A_np(M) - np.linalg.det(M) * A_np(S)) / fro(Y) ** 2)
        N2 = cplx(rng, (2, 2))
        s = svals(W93.coupling_np(cplx(rng, (2, 2)), N2 @ EPSIN))
        geo.append(abs(s[0] * s[2] / s[1] ** 2 - 1))
    q7 = {"(a) min J1 violation / ||Y||^3 with a 10% perturbation": min(j1v),
          "(b) min J2 violation / ||Y||^2 with A in place of P A": min(j2v),
          "(c) median |m1 m3/m2^2 - 1| with N != S": float(np.median(geo))}
    q7["holds"] = bool(q7["(a) min J1 violation / ||Y||^3 with a 10% perturbation"] > 1e-5
                       and q7["(b) min J2 violation / ||Y||^2 with A in place of P A"] > 1e-3
                       and q7["(c) median |m1 m3/m2^2 - 1| with N != S"] > 0.05)
    return q3, q5, readout5, q7


# ------------------------------------------------------------------------------------------------ mpmath, Q6
def mdet3(Y):
    return mp.det(Y)


def madj(Y):
    out = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            rows = [r for r in range(3) if r != j]
            cols = [c for c in range(3) if c != i]
            sub = mp.matrix([[Y[r, c] for c in cols] for r in rows])
            out[i, j] = (-1) ** (i + j) * mp.det(sub)
    return out


def mA(M):
    return mp.matrix(A_of(M, mp.mpc(0, 1)))


def sector_matter(rng):
    worst1, worst2, worst_det, worst_m = mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)
    pair = []
    cases = 0
    P = mp.diag([1, -1, -1])
    for line in W93.LINES18:
        for sec in W93.SECTORS:
            M = W93.M_of(W93.residues(line, sec))
            worst_det = max(worst_det, abs(W93.det2(M)) / W93.fro(M) ** 2)
            for _ in range(2):
                X = cplx(rng, (2, 2))
                S = mp.matrix([[mp.mpc(complex(X[i, j])) for j in range(2)] for i in range(2)])
                Y = W93.coupling_mp(S, M)
                nY = W93.fro(Y)
                trp = sum((W93.EPSM * S * M.T)[i, i] for i in range(2))
                worst1 = max(worst1, abs(mdet3(Y) - 4 * W93.det2(S) * W93.det2(M) * trp) / nY ** 3)
                R = madj(Y) - W93.det2(S) * mA(M) - W93.det2(M) * (P * mA(S))
                worst2 = max(worst2, W93.fro(R) / nY ** 2)
                U, sv, V = mp.svd_c(Y)
                s = sorted([abs(sv[i]) for i in range(3)])
                worst_m = max(worst_m, s[0] / s[2])
                pair.append(float(abs(trp) / (W93.fro(S) * W93.fro(M))))
                cases += 1
    q6 = {"cases": cases, "max |det Y - 4 det S det M tr| / ||Y||^3": float(worst1),
          "max ||adj Y - det S A(M) - det M P A(S)|| / ||Y||^2": float(worst2),
          "max |det M| / ||M||^2 (every sector)": float(worst_det), "max m1/m3": float(worst_m)}
    q6["holds"] = bool(cases == 108 and worst1 < mp.mpf(10) ** -25 and worst2 < mp.mpf(10) ** -25
                       and worst_det < mp.mpf(10) ** -25 and worst_m < mp.mpf(10) ** -20)
    readout6 = {"pairing |tr(eps S M^T)| / (||S|| ||M||): min": min(pair), "max": max(pair)}
    return q6, readout6


def main():
    out = {"rule": "W96_RULE.md", "status": "one run", "main's B1659": "sealed f4b12d788, not run when this ran"}
    out.update(symbolic())
    rng = np.random.default_rng(96)
    q3n, q5, r5, q7 = numeric(rng)
    out["Q3"] = dict(out.pop("Q3 exact"), **q3n)
    out["Q3"]["holds"] = bool(out["Q3"]["A(p q^T) == q~ p~^T"] and out["Q3"]["A(p q^T) != p~ q~^T"]
                              and q3n["200 null M: max ||adj Y - det S A(M)|| / ||Y||^2"] <= 1e-12
                              and q3n["max | ||A(M)|| - 2||M||^2 | / ||M||^2"] <= 1e-12)
    out["Q5"] = q5
    out["Q6"], r6 = sector_matter(rng)
    out["Q7"] = q7
    out["read-outs"] = {"Q5": r5, "Q6": r6}
    cells = ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7")
    out["all cells hold"] = all(out[c]["holds"] for c in cells)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n")
    print({c: out[c]["holds"] for c in cells})


if __name__ == "__main__":
    main()
