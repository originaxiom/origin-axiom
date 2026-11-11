#!/usr/bin/env python3
"""SM-C1, harvest row 1425 (SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS @ f06ce63e6, amended at beb0b98b8): this
seat's own check of (a) the spin table's heat coefficients tr[(1/2)E^2 + (1/12)Omega^2] per unit Omega^2 for a complex
scalar, a Dirac fermion (explicit Euclidean gamma matrices) and a vector, (b) the log-det weights and the normalised
+1, -3 (and the ghostless -8/3 control), (c) the massless vector light vector (0, -6, -9) from -3 C2, (d) the finite U(1)
D-flat control. Abelian background: Omega_{mu nu} = i F_{mu nu} times a scalar charge; the coefficient of
sum_{mu nu} F_{mu nu}^2 is extracted exactly (sympy). Planted: a vector-multiplet weight of -2 must be caught."""
import json
import sys
from pathlib import Path

import sympy as sp

# a generic antisymmetric field strength (6 components), anti-Hermitian convention Omega = -i F
f = sp.symbols("f01 f02 f03 f12 f13 f23", real=True)
F = sp.zeros(4, 4)
idx = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
for (m, n), v in zip(idx, f):
    F[m, n], F[n, m] = v, -v
Om = -sp.I * F
F2 = sum(F[m, n] ** 2 for m in range(4) for n in range(4))   # sum F_{mu nu}^2

# Euclidean gamma matrices (Hermitian, {g_mu, g_nu} = 2 delta)
s1, s2, s3 = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
I2, Z2 = sp.eye(2), sp.zeros(2)
kron = lambda A, B: sp.Matrix(sp.BlockMatrix([[A[i, j] * B for j in range(A.shape[1])] for i in range(A.shape[0])]))
g = [kron(s1, s1), kron(s1, s2), kron(s1, s3), kron(s2, I2)]
for m in range(4):
    for n in range(4):
        assert sp.simplify(g[m] * g[n] + g[n] * g[m] - 2 * (1 if m == n else 0) * sp.eye(4)) == sp.zeros(4)
gmn = lambda m, n: (g[m] * g[n] - g[n] * g[m]) / 2


def coeff(expr):
    return sp.nsimplify(sp.simplify(sp.expand(expr) / F2))


# (a) heat coefficients
scalar = coeff(sp.Rational(1, 12) * sum(Om[m, n] * Om[m, n] for m in range(4) for n in range(4)))
E_spin = sum((gmn(m, n) * Om[m, n] for m in range(4) for n in range(4)), sp.zeros(4)) / 2
dirac = coeff(sp.Rational(1, 2) * (E_spin * E_spin).trace()
              + sp.Rational(1, 12) * 4 * sum(Om[m, n] * Om[m, n] for m in range(4) for n in range(4)))
E_vec = 2 * Om                                   # E_{mu nu} = 2 Omega_{mu nu} acting on the vector index
vector = coeff(sp.Rational(1, 2) * (E_vec * E_vec).trace()
               + sp.Rational(1, 12) * 4 * sum(Om[m, n] * Om[m, n] for m in range(4) for n in range(4)))
out = {"heat_coefficient": {"complex_scalar": str(scalar), "dirac": str(dirac), "vector": str(vector)},
       "claimed": {"complex_scalar": "-1/12 x (-1) convention", "dirac": "-2/3", "vector": "-5/3"}}
# with Omega = -iF, Omega^2 = -F^2: the scalar's tr(1/12 Omega^2) = -(1/12) F^2; the item states coefficients per
# Omega_{mu nu}Omega_{mu nu} (i.e. per -F^2): convert
per_Om2 = {k: -sp.Rational(v) for k, v in out["heat_coefficient"].items()}
out["per_Omega2"] = {k: str(v) for k, v in per_Om2.items()}
# (b) log-det weights and products
w = {"complex_scalar": 1, "weyl": sp.Rational(-1, 4), "vector": sp.Rational(1, 2), "fp_pair": -1}
prod = {"complex_scalar": per_Om2["complex_scalar"] * w["complex_scalar"], "weyl": per_Om2["dirac"] * w["weyl"],
        "vector": per_Om2["vector"] * w["vector"], "fp_pair": per_Om2["complex_scalar"] * w["fp_pair"]}
Pc = prod["complex_scalar"] + prod["weyl"]
Pv = prod["vector"] + prod["fp_pair"] + prod["weyl"]
out["products"] = {k: str(v) for k, v in prod.items()}
out["P_c_total"], out["P_v_total"] = str(Pc), str(Pv)
out["normalised_weights"] = [str(Pc / Pc), str(Pv / Pc)]
out["ghostless_control"] = str((prod["vector"] + prod["weyl"]) / Pc)
# (c) the massless vector multiplets' light vector: -3 C2(G) per factor
C2 = {"u1": 0, "su2": 2, "su3": 3}
b_vec = [-3 * C2["u1"], -3 * C2["su2"], -3 * C2["su3"]]
out["b_vector"] = b_vec
out["h21_h31_vector"] = [b_vec[1] - b_vec[0], b_vec[2] - b_vec[0]]
# (d) the finite U(1) D-flat control
gg, v = sp.symbols("g v", positive=True)
h_, pi_ = sp.symbols("h pi", real=True)
k = sp.Matrix([sp.I * gg * v, -sp.I * gg * v])
Pv_fin = sp.simplify(2 * (k.H * k)[0])
# x_- = (dphi+ - dphi-)/sqrt2 = (h + i pi)/sqrt2 with dphi+ = -dphi- = (h + i pi)/2
dpp, dpm = (h_ + sp.I * pi_) / 2, -(h_ + sp.I * pi_) / 2
dmu = sp.simplify(gg * (2 * v * sp.re(dpp) - 2 * v * sp.re(dpm)))
gx = sp.simplify(2 * sp.re((k.H * sp.Matrix([dpp, dpm]))[0]))
out["finite_u1"] = {"P_v": str(Pv_fin), "delta_mu": str(dmu), "g_of_x": str(gx),
                    "half_squares": str(sp.simplify((dmu ** 2 + gx ** 2) / 2))}
ok = (per_Om2["complex_scalar"] == sp.Rational(1, 12) and per_Om2["dirac"] == sp.Rational(-2, 3)
      and per_Om2["vector"] == sp.Rational(-5, 3) and Pc == sp.Rational(1, 4) and Pv == sp.Rational(-3, 4)
      and Pv / Pc == -3 and (prod["vector"] + prod["weyl"]) / Pc == sp.Rational(-8, 3)
      and b_vec == [0, -6, -9] and Pv_fin == 4 * gg ** 2 * v ** 2 and sp.simplify(dmu - 2 * gg * v * h_) == 0
      and sp.simplify(gx - 2 * gg * v * pi_) == 0)
# planted: a vector-multiplet weight of -2 (e.g. an FP pair weighted -1/2 instead of -1) must be caught
Pv_bad = prod["vector"] + per_Om2["complex_scalar"] * sp.Rational(-1, 2) + prod["weyl"]
out["PLANTED_wrong_ghost_weight"] = {"normalised": str(Pv_bad / Pc), "caught": bool(Pv_bad / Pc != -3)}
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_wrong_ghost_weight"]["caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
