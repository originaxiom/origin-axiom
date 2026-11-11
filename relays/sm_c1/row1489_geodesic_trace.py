#!/usr/bin/env python3
"""SM-C1, harvest row 1489 (RELATIVE_GEODESIC_TRACE_AND_COUPLING_PRODUCT @ 4572f758c): this seat's own check of
(1) y^(a/2) K_a^0 y^(-a/2) = -y^2 Delta + i a y d_x + a(a-2)/4 (sympy), (3) the orbital heat coefficient
ell exp(-t/4 - L^2/4t) / [2 sinh(L/2) sqrt(4 pi t)] by direct numerical integration of the H2 heat kernel over Fermi
coordinates, the arcsin integral pi/sqrt(B), (7) the Laplace integral and the product logarithm, (9) the assembly of
L_C into products at 1, 2, 3/2, 5/2, and the relative vacuum weights 0 and 0. Planted: dropping the scalar's
exp(-t/4) must move the arguments and change (9)."""
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

out = {}
# (1)
X, Y = sp.symbols("x y", real=True)
a = sp.Symbol("a")
f = sp.Function("f")(X, Y)
Db = lambda h: sp.diff(h, X) + sp.I * sp.diff(h, Y)
Dz = lambda h: sp.diff(h, X) - sp.I * sp.diff(h, Y)
K0 = lambda h: -Y ** (2 - a) * Dz(Y ** a * Db(h))
conj = Y ** (a / 2) * K0(Y ** (-a / 2) * f)
target = -Y ** 2 * (sp.diff(f, X, 2) + sp.diff(f, Y, 2)) + sp.I * a * Y * sp.diff(f, X) + a * (a - 2) / 4 * f
out["eq1_residual"] = str(sp.simplify(sp.expand(conj - target)))
# arcsin integral
A_, B_, xx = sp.symbols("A B x", positive=True)
arc = sp.simplify(sp.integrate(1 / sp.sqrt(A_ - B_ * xx ** 2), (xx, -sp.sqrt(A_ / B_), sp.sqrt(A_ / B_))))
out["arcsin_integral"] = str(arc)
# (3) numerically
mp.mp.dps = 20


def kt(t, rho):
    pre = mp.sqrt(2) * mp.e ** (-t / 4) / (4 * mp.pi * t) ** mp.mpf(1.5)
    # substitute u = rho + w^2 to remove the endpoint singularity
    # cosh(rho + w^2) - cosh(rho) = 2 sinh(rho + w^2/2) sinh(w^2/2); the factor 2w / sqrt(...) has the limit 2/sqrt(sinh rho)
    def g(w):
        u = rho + w * w
        if w == 0:
            ratio = 2 / mp.sqrt(mp.sinh(rho))
        else:
            ratio = 2 * w / mp.sqrt(2 * mp.sinh(rho + w * w / 2) * mp.sinh(w * w / 2))
        return u * mp.e ** (-u ** 2 / (4 * t)) * ratio
    return pre * mp.quad(g, [0, 1, 4, mp.inf])


def orbital(t, L, ell):
    B = 2 * mp.sinh(L / 2) ** 2
    def integrand(r):
        rho = mp.acosh(mp.cosh(L) + B * mp.sinh(r) ** 2)
        return kt(t, rho) * mp.cosh(r)
    return ell * 2 * mp.quad(integrand, [0, 1, 3, 8])


cases = []
for t, L, ell in ((mp.mpf("0.7"), mp.mpf("1.3"), mp.mpf("1.3")), (mp.mpf("1.9"), mp.mpf("2.6"), mp.mpf("1.3"))):
    num = orbital(t, L, ell)
    closed = ell * mp.e ** (-t / 4 - L ** 2 / (4 * t)) / (2 * mp.sinh(L / 2) * mp.sqrt(4 * mp.pi * t))
    cases.append({"t": str(t), "L": str(L), "ell": str(ell), "numeric": mp.nstr(num, 14), "closed": mp.nstr(closed, 14),
                  "rel_dev": mp.nstr(abs(num / closed - 1), 3)})
out["eq3_cases"] = cases
eq3_ok = all(mp.mpf(c["rel_dev"]) < mp.mpf("1e-8") for c in cases)
# (7): the Laplace integral and the product-log identity
t_, L_, a_ = sp.symbols("t L a", positive=True)
lap = sp.simplify(sp.integrate(sp.exp(-a_ ** 2 * t_ - L_ ** 2 / (4 * t_)) / (t_ * sp.sqrt(4 * sp.pi * t_)), (t_, 0, sp.oo)))
out["laplace_integral"] = str(lap)
z_, l_ = sp.symbols("z ell", positive=True)
# POST HOC (disclosed): .rewrite(exp) added after the first run, whose residual was zero but left unsimplified
geo = sp.simplify((sp.exp(-z_ * l_) / (1 - sp.exp(-l_)) - sp.exp(-(z_ - sp.Rational(1, 2)) * l_) / (2 * sp.sinh(l_ / 2)))
                  .rewrite(sp.exp))
out["geometric_identity_residual"] = str(geo)
# (9) assembly: x^k E_q -> -A_q(z_E(k)), x^k O_q -> -B_q(z_O(k)) with z_E(k) = 1/2 + sqrt(k + 1/4), z_O(k) = 1/2 + sqrt(k)
def assemble(zE, zO):
    Asym = lambda q, r, z: sp.Symbol("A_%d%d(%s)" % (q, r, z))
    Bsym = lambda q, r, z: sp.Symbol("B_%d%d(%s)" % (q, r, z))
    # By (7): int x^k (E_q - E_r) dt/t = -A_qr(z_E(k)); int x^k (O_q - O_r) dt/t = -B_qr(z_O(k)).
    # I_Psi = int (Psi_3 - Psi_2) dt/t, Psi_q = 2[(1 + x^2) E_q - (x + x^4) O_q]
    I_Psi = 2 * (-(Asym(3, 2, zE(0)) + Asym(3, 2, zE(2))) + (Bsym(3, 2, zO(1)) + Bsym(3, 2, zO(4))))
    # I_T = int (T_1 - T_3) dt/t, T_q = 2[x O_q - x^2 E_q]
    I_T = 2 * (-Bsym(1, 3, zO(1)) + Asym(1, 3, zE(2)))
    # L_C = -int B_C dt/t with B_C = -(6/5)(Psi_3 - Psi_2) - (9/5)(T_1 - T_3), so L_C = (6/5) I_Psi + (9/5) I_T.
    # POST HOC (written after the first run, disclosed): the first version negated this through stacked signs; this
    # seat's hand derivation in the review note gives this line, which agrees with the item's (9).
    return sp.expand(sp.Rational(6, 5) * I_Psi + sp.Rational(9, 5) * I_T)


zE = lambda k: sp.nsimplify(sp.Rational(1, 2) + sp.sqrt(sp.Rational(k) + sp.Rational(1, 4)))
zO = lambda k: sp.nsimplify(sp.Rational(1, 2) + sp.sqrt(sp.Rational(k)))
LC = assemble(zE, zO)
S_ = lambda n: sp.Symbol(n)
claim = (-sp.Rational(12, 5) * (S_("A_32(1)") + S_("A_32(2)")) + sp.Rational(12, 5) * (S_("B_32(3/2)") + S_("B_32(5/2)"))
         - sp.Rational(18, 5) * S_("B_13(3/2)") + sp.Rational(18, 5) * S_("A_13(2)"))
out["eq9_L_C"] = str(LC)
eq9_ok = sp.simplify(LC - claim) == 0
out["eq9_holds"] = eq9_ok
# vacuum weights
vac_c = 1 - sp.Rational(1, 4) * 4
vac_v = sp.Rational(1, 2) * 4 - 1 - sp.Rational(1, 4) * 4
out["vacuum_weights"] = [str(vac_c), str(vac_v)]
# planted: drop the scalar exp(-t/4): z_E(k) = 1/2 + sqrt(k)
LC_bad = assemble(lambda k: zO(k), zO)
out["PLANTED_no_exp_minus_t_over_4_caught"] = bool(sp.simplify(LC_bad - claim) != 0)
ok = (out["eq1_residual"] == "0" and arc == sp.pi / sp.sqrt(B_) and eq3_ok
      and sp.simplify(lap - sp.exp(-a_ * L_) / L_) == 0 and geo == 0 and eq9_ok and vac_c == 0 and vac_v == 0)
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_no_exp_minus_t_over_4_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
