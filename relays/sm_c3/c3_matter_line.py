#!/usr/bin/env python3
"""SM-C3, packet matter_line_compatibility (the fork lane @ 0c6570bab): this seat's own exact check, rebuilt from the
packet's PROOF.md, not from its verify.py.
(a) U^T J U = det(U) J for an arbitrary 2 x 2 U; (b) [aQ+bR, cQ+dR] = (ad - bc)[Q, R] for non-commuting Q, R;
(c) the superpotential W = (1/2) tr(Q DR - R DQ), D linear, scales by det(U) under X -> U X, so a fixed W needs det U = 1;
(d) U^dag U = I preserves [Q,Q^dag] + [R,R^dag]; a unitary of determinant i preserves the commutator's norm and changes
W by i (the packet's opposing control); a determinant-one non-unitary U changes the kinetic sum;
(e) the diagonal pairing condition H^T J + J H = (a+b) J, so a continuous circle has charges (a, -a);
(f) with nabla_Q = d + i a b, nabla_R = d - i a b, the change Q -> e^{i a th} Q, R -> e^{-i a th} R, b -> b - th' is
covariant; without the compensator it is not; the product Q R has no residual connection;
(g) the same line on both fields: determinant curvature 2F; the opposite twist: 0; the modular line F = -6 i n dA gives
-12 i n dA for the common twist;
(h) ad(Z) is a derivation; a scalar c I has defect -c[X,Y]; a scalar automorphism u I keeps the bracket only at u = 1;
[Z, X] = 2X and [Z, Y] = -2Y for the sl2 triple.
Planted: charges (a, a) must fail (e)."""
import json
import sys
from pathlib import Path

import sympy as sp

out = {}
a, b, c, d = sp.symbols("a b c d")
U = sp.Matrix([[a, b], [c, d]])
J = sp.Matrix([[0, 1], [-1, 0]])
z = lambda M: sp.expand(M) == sp.zeros(*M.shape)
out["(a)_UtJU=detU_J"] = z(U.T * J * U - U.det() * J)
n = 3
Q = sp.Matrix(n, n, sp.symbols("q0:9"))
R = sp.Matrix(n, n, sp.symbols("r0:9"))
comm = lambda A, B: A * B - B * A
out["(b)_commutator_scales_by_det"] = z(comm(a * Q + b * R, c * Q + d * R) - (a * d - b * c) * comm(Q, R))
DQ = sp.Matrix(n, n, sp.symbols("p0:9"))
DR = sp.Matrix(n, n, sp.symbols("s0:9"))
W = lambda q, r, dq, dr: sp.Rational(1, 2) * (q * dr - r * dq).trace()
Wp = W(a * Q + b * R, c * Q + d * R, a * DQ + b * DR, c * DQ + d * DR)
out["(c)_W_scales_by_det"] = sp.expand(Wp - U.det() * W(Q, R, DQ, DR)) == 0
# (d) exact unitaries over the Gaussian rationals
U1 = sp.Matrix([[3, 4 * sp.I], [4 * sp.I, 3]]) / 5               # unitary, det 1
Ui = sp.diag(1, sp.I)                                            # unitary, det i
Un = sp.Matrix([[2, 0], [0, sp.Rational(1, 2)]])                 # det 1, not unitary
Qn = sp.Matrix([[1 + sp.I, 2], [0, -1 - sp.I]])
Rn = sp.Matrix([[sp.I, 0], [3, -sp.I]])
DQn = sp.Matrix([[0, 1], [sp.I, 2]])
DRn = sp.Matrix([[1, -sp.I], [0, 1]])


def mix(M):
    return (M[0, 0] * Qn + M[0, 1] * Rn, M[1, 0] * Qn + M[1, 1] * Rn, M[0, 0] * DQn + M[0, 1] * DRn, M[1, 0] * DQn + M[1, 1] * DRn)


kin = lambda q, r: sp.simplify(comm(q, q.H) + comm(r, r.H))
w0 = sp.simplify(W(Qn, Rn, DQn, DRn))
d_checks = {}
for name, M in (("det1_unitary", U1), ("deti_unitary", Ui), ("det1_nonunitary", Un)):
    q, r, dq, dr = mix(M)
    d_checks[name] = {"unitary": sp.simplify(M.H * M - sp.eye(2)) == sp.zeros(2), "det": str(sp.simplify(M.det())),
                      "W_ratio": str(sp.simplify(W(q, r, dq, dr) / w0)),
                      "kinetic_sum_kept": sp.simplify(kin(q, r) - kin(Qn, Rn)) == sp.zeros(2),
                      "commutator_norm_kept": sp.simplify((comm(q, r).H * comm(q, r)).trace() - (comm(Qn, Rn).H * comm(Qn, Rn)).trace()) == 0}
out["(d)"] = d_checks
d_ok = (w0 != 0 and d_checks["det1_unitary"]["W_ratio"] == "1" and d_checks["det1_unitary"]["kinetic_sum_kept"]
        and d_checks["deti_unitary"]["W_ratio"] == "I" and d_checks["deti_unitary"]["commutator_norm_kept"]
        and not d_checks["det1_nonunitary"]["kinetic_sum_kept"])
# (e) the diagonal pairing condition


def pairing_defect(ch1, ch2):
    H = sp.diag(ch1, ch2)
    return sp.simplify(H.T * J + J * H)


aa, bb = sp.symbols("alpha beta")
out["(e)_defect"] = str(pairing_defect(aa, bb))
e_ok = sp.simplify(pairing_defect(aa, bb) - (aa + bb) * J) == sp.zeros(2) and pairing_defect(aa, -aa) == sp.zeros(2)
# (f) local covariance in one variable x
x, ch = sp.symbols("x a", real=True)
th, bfun = sp.Function("theta")(x), sp.Function("b")(x)
q, r = sp.Function("Q")(x), sp.Function("R")(x)
nab = lambda f, sgn, bb_: sp.diff(f, x) + sgn * sp.I * ch * bb_ * f
qp, rp, bp = sp.exp(sp.I * ch * th) * q, sp.exp(-sp.I * ch * th) * r, bfun - sp.diff(th, x)
f_cov = (sp.simplify(nab(qp, 1, bp) - sp.exp(sp.I * ch * th) * nab(q, 1, bfun)) == 0
         and sp.simplify(nab(rp, -1, bp) - sp.exp(-sp.I * ch * th) * nab(r, -1, bfun)) == 0)
f_without = sp.simplify(nab(qp, 1, bfun) - sp.exp(sp.I * ch * th) * nab(q, 1, bfun)) != 0
f_product = sp.simplify(qp * rp - q * r) == 0
out["(f)"] = {"covariant_with_compensator": f_cov, "fails_without": f_without, "product_has_no_residual_phase": f_product}
# (g) determinant curvature
Fb, nn, dA = sp.symbols("F n dA")
same = sp.diag(Fb, Fb).trace()
opposite = sp.diag(ch * Fb, -ch * Fb).trace()
modular = 2 * (-6 * sp.I * nn * dA)
out["(g)"] = {"same_line_det_curvature": str(same), "opposite_twist": str(opposite), "modular_common_twist": str(modular)}
g_ok = same == 2 * Fb and opposite == 0 and sp.expand(modular + 12 * sp.I * nn * dA) == 0
# (h) derivations and scalars on sl2
X = sp.Matrix([[0, 1], [0, 0]]); Y = sp.Matrix([[0, 0], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
cc, u = sp.symbols("c u")
ad = lambda A: (lambda B: comm(A, B))
deriv = all(z(ad(Z)(comm(A, B)) - comm(ad(Z)(A), B) - comm(A, ad(Z)(B))) for A in (X, Y, Z) for B in (X, Y, Z))
scalar_defect = sp.simplify(cc * comm(X, Y) - comm(cc * X, Y) - comm(X, cc * Y) + cc * comm(X, Y)) == sp.zeros(2)
aut = sp.solve(sp.Eq(u * comm(X, Y)[0, 0], comm(u * X, u * Y)[0, 0]), u)
out["(h)"] = {"ad_Z_is_a_derivation": deriv, "scalar_defect_is_-c[X,Y]": scalar_defect, "scalar_automorphism_u": [str(v) for v in aut],
              "[Z,X]=2X,[Z,Y]=-2Y": z(comm(Z, X) - 2 * X) and z(comm(Z, Y) + 2 * Y)}
h_ok = deriv and scalar_defect and sorted(aut, key=str) == [0, 1] and out["(h)"]["[Z,X]=2X,[Z,Y]=-2Y"]
checks = {"a": out["(a)_UtJU=detU_J"], "b": out["(b)_commutator_scales_by_det"], "c": out["(c)_W_scales_by_det"],
          "d": d_ok, "e": e_ok, "f": f_cov and f_without and f_product, "g": g_ok, "h": h_ok}
out["checks_ok"] = checks
out["PLANTED_same_charges_(a,a)_defect"] = str(pairing_defect(aa, aa))
out["PLANTED_caught"] = pairing_defect(aa, aa) != sp.zeros(2)
out["all_claims_hold_and_plants_caught"] = bool(all(checks.values()) and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
