#!/usr/bin/env python3
"""B1484 -- the one-loop unification ratio by field content, and the colour triplet's weights in the 27 of E6.

The coefficients are DERIVED here from the field content (the owner's rule of 2026-10-06: no published number is
load-bearing).  Conventions: d(1/alpha_i)/d ln(mu) = -b_i / (2 pi); hypercharge in the SU(5) normalisation,
T_1 = (3/5) * sum Y^2 over components; T(fundamental) = 1/2, C_2(SU(N)) = N.
  non-supersymmetric:  b_i = -(11/3) C_2 + (2/3) sum_{Weyl fermions} T_i + (1/3) sum_{complex scalars} T_i
  supersymmetric:      b_i = -3 C_2 + sum_{chiral superfields} T_i
If the three couplings meet at one scale, (1/a2 - 1/a3) / (1/a1 - 1/a2) at M_Z equals B = (b2 - b3) / (b1 - b2)."""
import json, pathlib
from fractions import Fraction as F
HERE = pathlib.Path(__file__).resolve().parent

# a field: (dim under SU(3), dim under SU(2), hypercharge Y)
GEN = [(3, 2, F(1, 6)), (3, 1, F(-2, 3)), (3, 1, F(1, 3)), (1, 2, F(-1, 2)), (1, 1, F(1))]     # Q, u^c, d^c, L, e^c
HU, HD = (1, 2, F(1, 2)), (1, 2, F(-1, 2)); D, DBAR = (3, 1, F(-1, 3)), (3, 1, F(1, 3)); NUC = (1, 1, F(0))


def T(field):
    d3, d2, y = field
    t3 = F(1, 2) * d2 if d3 == 3 else F(0)
    t2 = F(1, 2) * d3 if d2 == 2 else F(0)
    t1 = F(3, 5) * d3 * d2 * y * y
    return (t1, t2, t3)


def add(*ts): return tuple(sum(t[i] for t in ts) for i in range(3))
def scale(c, t): return tuple(c * x for x in t)
C2 = (F(0), F(2), F(3))


def b_nonsusy(fermions, scalars):
    f, s = add(*map(T, fermions)) if fermions else (0, 0, 0), add(*map(T, scalars)) if scalars else (0, 0, 0)
    return tuple(-F(11, 3) * C2[i] + F(2, 3) * f[i] + F(1, 3) * s[i] for i in range(3))


def b_susy(chirals):
    c = add(*map(T, chirals))
    return tuple(-3 * C2[i] + c[i] for i in range(3))


def ratio(b): return (b[1] - b[2]) / (b[0] - b[1])


spectra = {
    "the Standard Model, a desert (B915)": b_nonsusy(GEN * 3, [HU]),
    "supersymmetric; Higgs doublets light, colour triplets heavy": b_susy(GEN * 3 + [HU, HD]),
    "supersymmetric; one light Higgs pair AND one light colour-triplet pair (one complete 5 + 5bar)": b_susy(GEN * 3 + [HU, HD, D, DBAR]),
    "supersymmetric; three complete 27s light": b_susy((GEN + [NUC, HU, HD, D, DBAR, NUC]) * 3),
    "supersymmetric gauge sector plus complete multiplets only": b_susy(GEN * 3 + [HU, HD, D, DBAR]),
}
# measured inputs at M_Z (data, cited as data): 1/alpha_em = 127.95, sin^2 theta_W = 0.23122, alpha_s = 0.1180
inv_aem, sw2, als = 127.95, 0.23122, 0.1180
a1, a2, a3 = 0.6 * (1 - sw2) * inv_aem, sw2 * inv_aem, 1 / als
out = dict(measured=dict(B=(a2 - a3) / (a1 - a2), inv_alpha=(a1, a2, a3)), spectra={})
for k, b in spectra.items():
    B = ratio(b); out["spectra"][k] = dict(b=[str(x) for x in b], B=str(B), B_float=float(B), alpha_s_implied=1 / (a2 - float(B) * (a1 - a2)))

# a complete SU(5) multiplet shifts the three coefficients equally, so it never changes B
five, ten = add(T(D), T(HU)), add(T((3, 2, F(1, 6))), T((3, 1, F(-2, 3))), T((1, 1, F(1))))
out["complete_multiplets"] = dict(five=[str(x) for x in five], ten=[str(x) for x in ten], equal=len(set(five)) == 1 and len(set(ten)) == 1)

# the 27 of E6 under (Y, chi, psi), the three abelian directions commuting with SU(3) x SU(2)
W = {"Q": (F(1, 6), -1, 1), "u^c": (F(-2, 3), -1, 1), "e^c": (F(1), -1, 1), "d^c": (F(1, 3), 3, 1), "L": (F(-1, 2), 3, 1), "nu^c": (F(0), -5, 1),
     "H_u": (F(1, 2), 2, -2), "D": (F(-1, 3), 2, -2), "H_d": (F(-1, 2), -2, -2), "Dbar": (F(1, 3), -2, -2), "N": (F(0), 0, 4)}
out["weights"] = dict(w_D_is_minus_two_w_Q=all(W["D"][i] == -2 * W["Q"][i] for i in range(3)), H_u_and_D_differ_only_in_Y=W["H_u"][1:] == W["D"][1:] and W["H_u"][0] != W["D"][0],
                      w_Dbar_is_two_w_Q=all(W["Dbar"][i] == 2 * W["Q"][i] for i in range(3)))
json.dump(out, open(HERE / "unification_ratio.json", "w"), indent=1)
print("measured B = %.4f" % out["measured"]["B"])
for k, v in out["spectra"].items(): print("  B = %-7s = %.4f  b = %-22s alpha_s -> %.4f   %s" % (v["B"], v["B_float"], "(" + ", ".join(v["b"]) + ")", v["alpha_s_implied"], k))
print("complete multiplets shift all three equally:", out["complete_multiplets"]); print("weights:", out["weights"])
assert spectra["the Standard Model, a desert (B915)"] == (F(41, 10), F(-19, 6), F(-7)) and spectra["supersymmetric; Higgs doublets light, colour triplets heavy"] == (F(33, 5), F(1), F(-3))
assert out["complete_multiplets"]["equal"] and out["weights"]["w_D_is_minus_two_w_Q"]
