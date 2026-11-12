#!/usr/bin/env python3
"""SM-C3, packet puncture_symmetry (the fork lane @ 0c6570bab): this seat's own exact check, rebuilt from the packet's
PROOF.md, not from its verify.py.  Moves L = Pi13 x (I2 + iZ)/sqrt2, R = Pi23 x (I2 - iY)/sqrt2 on C6 (parity block basis).
(a) L^2 = I3 x iZ, R^2 = I3 x (-iY); (b) the commutant of {L, R} in M6(C) is span(P2, P4), P2 = (1/3) J3 x I2, P4 = I - P2,
by an exact nullspace; (c) the projectors in it are 0, P2, P4, I only, so the invariant subspaces are 0, V2, V4, C6;
(d) with Phi = diag(U1, U2, U3), the U_i the quaternion units i sigma_x, i sigma_y, i sigma_z, the X in M3(C) whose
F_X = Phi (X x I2) Phi^-1 keeps V2 are the scalars, and likewise for V4; (e) D = diag(1,-1,-1) x I2 is unitary, of order
two, equals F_X for X = diag(1,-1,-1) with det X = 1, the (1,2) block of [D, P2] is (2/3) I2, and the commutant of
{L, R, D} is the scalars; with only dim(Lambda+) in {0, 6} the stipulated index dim(Lambda+) - 3 is -3 or +3;
(f) the doubled model: B((u,v),(u',v')) = u^dag v' + v^dag u', L_t = {(u, i t u)} is null and invariant for real t, the
grading Gamma(u,v) = (u,-v) sends L_t to L_-t, and the real graph (u, t u) has B = 2 t u^dag u'.
Not checked here: the SU6 embedding into compact E8 (the packet's own verifier marks it not reconstructed).
Planted: a scalar phase in place of D must leave the commutant two-dimensional (V2 and V4 still available)."""
import json
import sys
from pathlib import Path

import sympy as sp

out = {}
I2, I3 = sp.eye(2), sp.eye(3)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
kron = sp.kronecker_product
Pi13 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
Pi23 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
L = kron(Pi13, (I2 + sp.I * sz) / sp.sqrt(2))
R = kron(Pi23, (I2 - sp.I * sy) / sp.sqrt(2))
z = lambda M: sp.simplify(M) == sp.zeros(*M.shape)
out["(a)_squares"] = z(L * L - kron(I3, sp.I * sz)) and z(R * R - kron(I3, -sp.I * sy))


def commutant(gens, n=6):
    syms = sp.symbols(f"k0:{n * n}")
    K = sp.Matrix(n, n, syms)
    eqs = []
    for G in gens:
        eqs += list(sp.expand(K * G - G * K))
    A, _ = sp.linear_eq_to_matrix(eqs, syms)
    ns = A.nullspace()
    return [sp.Matrix(n, n, list(v)) for v in ns]


basis = commutant([L, R])
J3 = sp.ones(3, 3)
P2 = kron(J3, I2) / 3
P4 = sp.eye(6) - P2
in_span = lambda M, B: sp.Matrix.hstack(*[sp.Matrix(list(b)) for b in B]).rank() == sp.Matrix.hstack(*[sp.Matrix(list(b)) for b in B], sp.Matrix(list(M))).rank()
out["(b)_commutant_dim"] = len(basis)
out["(b)_P2_P4_span_it"] = len(basis) == 2 and in_span(P2, basis) and in_span(P4, basis)
# (c) projectors a P2 + b P4 with (aP2+bP4)^2 = itself: a, b in {0,1}
aa, bb = sp.symbols("a b")
Pg = aa * P2 + bb * P4
sols = sp.solve(list(sp.expand(Pg * Pg - Pg)), [aa, bb], dict=True)
out["(c)_projectors"] = sorted([(int(s_[aa]), int(s_[bb])) for s_ in sols])
c_ok = out["(c)_projectors"] == [(0, 0), (0, 1), (1, 0), (1, 1)]
# (d) scalar stabilisers
U = [sp.I * sx, sp.I * sy, sp.I * sz]
Phi = sp.diag(*U)
Xs = sp.Matrix(3, 3, sp.symbols("x0:9"))
FX = Phi * kron(Xs, I2) * Phi.inv()
V2b = kron(sp.Matrix([1, 1, 1]), I2)                                   # columns span V2
V4b = sp.Matrix.hstack(kron(sp.Matrix([1, -1, 0]), I2), kron(sp.Matrix([1, 0, -1]), I2))


def stabiliser_dim(Vb, comp):
    # F_X Vb lies in span(Vb): its component along the complement must vanish
    img = FX * Vb
    eqs = list(sp.expand(comp * img))
    A, _ = sp.linear_eq_to_matrix(eqs, list(Xs))
    ns = A.nullspace()
    return len(ns), [list(v) for v in ns]


d2, ns2 = stabiliser_dim(V2b, P4)
d4, ns4 = stabiliser_dim(V4b, P2)
identity_vec = [1, 0, 0, 0, 1, 0, 0, 0, 1]
out["(d)_stabiliser_dims"] = {"V2": d2, "V4": d4}
proportional_to_identity = lambda v: sp.Matrix.hstack(sp.Matrix(v), sp.Matrix(identity_vec)).rank() == 1
d_ok = d2 == 1 and d4 == 1 and all(proportional_to_identity(v) for v in ns2 + ns4)
# (e) the sign D
D = kron(sp.diag(1, -1, -1), I2)
Xd = sp.diag(1, -1, -1)
e = {"unitary": z(D.H * D - sp.eye(6)), "order_two": z(D * D - sp.eye(6)), "D_is_F_X": z(Phi * kron(Xd, I2) * Phi.inv() - D),
     "det_X": int(Xd.det()), "block12_of_[D,P2]": str(((D * P2 - P2 * D)[0:2, 2:4]))}
basisD = commutant([L, R, D])
e["commutant_with_D_dim"] = len(basisD)
e["indices"] = sorted({dim - 3 for dim in (0, 6)})
out["(e)"] = e
e_ok = (e["unitary"] and e["order_two"] and e["D_is_F_X"] and e["det_X"] == 1 and z((D * P2 - P2 * D)[0:2, 2:4] - sp.Rational(2, 3) * I2)
        and len(basisD) == 1 and e["indices"] == [-3, 3])
# (f) the doubled model, with symbolic vectors
uu = sp.Matrix(sp.symbols("u0:6")); up = sp.Matrix(sp.symbols("w0:6"))
t = sp.Symbol("t", real=True)
Bf = lambda p, q: (p[0].H * q[1] + p[1].H * q[0])[0]
Lt = lambda v: (v, sp.I * t * v)
null_ok = sp.simplify(Bf(Lt(uu), Lt(up))) == 0
G = sp.Matrix(6, 6, lambda i, j: sp.Symbol(f"g{i}{j}"))
inv_ok = z(G * (sp.I * t * uu) - sp.I * t * (G * uu))
grade = lambda p: (p[0], -p[1])
gam_ok = z(grade(Lt(uu))[1] - (-sp.I * t) * uu)
real_graph = sp.simplify(Bf((uu, t * uu), (up, t * up)) - 2 * t * (uu.H * up)[0])
out["(f)"] = {"L_t_null": null_ok, "L_t_invariant": inv_ok, "Gamma_L_t=L_-t": gam_ok, "real_graph_B=2t_u^dag_u'": real_graph == 0}
f_ok = null_ok and inv_ok and gam_ok and real_graph == 0
out["checks_ok"] = {"a": out["(a)_squares"], "b": out["(b)_P2_P4_span_it"], "c": c_ok, "d": d_ok, "e": e_ok, "f": f_ok}
phase = sp.exp(sp.I * sp.pi / 5) * sp.eye(6)
out["PLANTED_scalar_phase_commutant_dim"] = len(commutant([L, R, phase]))
out["PLANTED_caught"] = out["PLANTED_scalar_phase_commutant_dim"] == 2
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
