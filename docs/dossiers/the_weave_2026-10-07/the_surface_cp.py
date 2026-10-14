"""W74: the surface frame's CP and the strong phase (I-18's Yukawa half). The involution f -> C conj f(-conj tau),
C = diag(1, 1, -1), on the record's representations; the reality of W72's stored Yukawa and Higgs mode; and the
consequences for arg det(M_u M_d) and the CKM phase with one coupling. The rule (W74_RULE.md) was committed before
this script.

  V1  the involution, exact: C L C = L^-1, C P C = P, the S-phase condition per weight, C conj B[l] = B[l]
  V2  the reality in W72's stored data: Y in both settings, and h's coefficients
  V3  the consequences: arg det(Y Y), and the CKM matrix and J of two identical sectors
  plus the read-outs: the determinant and eigenvalue signs of W72's Y and of W73's H-end form

Run: python3 the_surface_cp.py  ->  the_surface_cp.json beside it.
"""
import json
from pathlib import Path

import numpy as np
import sympy as sy

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_surface_cp.json"


def main():
    out = {"status": "W74: the surface frame's CP (the rule W74_RULE.md first; one run)"}
    C = sy.diag(1, 1, -1)
    Linv = sy.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    L = Linv.inv()
    P = sy.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    ipi = sy.I * sy.pi
    def cond(k, phase):                     # e^{-i pi k} conj(phase) == phase, checked to 50 digits
        return abs(complex(sy.N(sy.exp(-ipi * k) * sy.conjugate(phase) - phase, 50))) < 1e-40
    rhoR = sy.exp(ipi / 4)
    rhoP = sy.exp(3 * ipi / 4)
    weights = {"rho_R, k = -1/2": cond(sy.Rational(-1, 2), rhoR), "rho_R, k = 3/2": cond(sy.Rational(3, 2), rhoR),
               "rho_R, k = 7/2": cond(sy.Rational(7, 2), rhoR), "rho', k = 5/2": cond(sy.Rational(5, 2), rhoP),
               "control rho_R, k = 1/2": cond(sy.Rational(1, 2), rhoR), "control rho_R, k = 1": cond(1, rhoR)}
    B = {"e_i": sy.Matrix([1, 0, 0]), "v+": sy.Matrix([0, 1, -sy.I]), "v-": sy.Matrix([0, 1, sy.I])}
    basis_ok = {l: (C * v.conjugate() - v) == sy.zeros(3, 1) for l, v in B.items()}
    v1 = {"C L C = L^-1": C * L * C == Linv, "C P C = P": C * P * C == P, "S-phase condition": weights,
          "C conj B[l] = B[l]": basis_ok}
    v1_ok = (v1["C L C = L^-1"] and v1["C P C = P"] and all(basis_ok.values())
             and all(v for k, v in weights.items() if not k.startswith("control"))
             and not any(v for k, v in weights.items() if k.startswith("control")))
    out["V1"] = {**{k: (v if not isinstance(v, dict) else {kk: bool(vv) for kk, vv in v.items()})
                    for k, v in v1.items()}, "holds": bool(v1_ok)}
    w = json.loads((HERE / "the_surface_yukawa.json").read_text(encoding="utf-8"))
    Y2 = np.array([[complex(*z) for z in row] for row in w["X4"]["Y (Y0 = 2.0)"]])
    parts = w["read-outs"]["the parts above and below Y0"]
    Y1 = np.zeros((3, 3), dtype=complex)
    for a in range(3):
        for b in range(a, 3):
            p = parts[f"1.25:{a}{b}"]
            Y1[a, b] = Y1[b, a] = complex(*p["above"]) + complex(*p["below"])
    imY = {"Y0 = 2.0": float(np.max(np.abs(Y2.imag)) / np.max(np.abs(Y2))),
           "Y0 = 1.25": float(np.max(np.abs(Y1.imag)) / np.max(np.abs(Y1)))}
    hco = w["read-outs"]["h's first coefficients"]
    imh = max(abs(v[1]) for v in hco.values())
    out["V2"] = {"largest |Im Y| / largest |Y|": imY, "largest |Im| of h's stored coefficients": imh,
                 "holds": bool(max(imY.values()) < 1e-12 and imh < 1e-30)}
    detYY = np.linalg.det(Y2 @ Y2)
    arg = float(np.angle(detYY))
    U = np.linalg.svd(Y2)[0]
    V = U.conj().T @ U
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    out["V3"] = {"arg det(Y Y)": arg, "|V - 1| (two identical sectors)": float(np.max(np.abs(V - np.eye(3)))), "J": J,
                 "holds": bool(abs(arg) < 1e-12 and np.max(np.abs(V - np.eye(3))) < 1e-12 and abs(J) < 1e-12)}
    D = np.diag([1, 2 ** -0.5, 2 ** -0.5])
    Yh = D @ Y2.real @ D
    out["read-outs"] = {"det Y (real part)": float(np.linalg.det(Y2.real)), "eigenvalues of Y": sorted(
        np.linalg.eigvalsh(Y2.real).tolist()), "det of the H-end form": float(np.linalg.det(Yh)),
        "eigenvalues of the H-end form": sorted(np.linalg.eigvalsh(Yh).tolist())}
    out["cells"] = {k: out[k]["holds"] for k in ("V1", "V2", "V3")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
