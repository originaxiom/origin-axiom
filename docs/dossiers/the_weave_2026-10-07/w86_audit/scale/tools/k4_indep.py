"""Independent check of chat1's K4 local model and post hoc pointwise norm.
For radial functions f(r), d_z d_zbar f = (1/4)(f'' + f'/r). Hitchin's equation, diagonal h = diag(h1, h2), theta = phi dz,
coefficient of dz^dzbar:  -(log h_i)_{z zbar} + (phi phi*_h - phi*_h phi)_{ii} = 0 with phi*_h = H^-1 conj(phi)^T H.
Checks: (1) nilpotent phi = E12/z with h = diag(1/(L+b), L+b), L = -log r^2, for symbolic b; (2) the opposite sign fails;
(3) pointwise norm |theta(e)|_h on unit vectors of 4|dz|^2/(r^2 L^2): (1/(L+b))*(L/2); (4) semisimple diag(l,-l)/z with
flat h: solves, pointwise norm l*L/2; (5) the uniformising check: g = 1/(r^2 L^2), Phi = E21 dz, h = diag(g^-1/2, g^1/2)."""
import sympy as sp
r, b, l = sp.symbols("r b lambda", positive=True)
L = -sp.log(r ** 2)
def ddbar(f):  # radial Laplacian / 4
    return sp.simplify((sp.diff(f, r, 2) + sp.diff(f, r) / r) / 4)
def hitchin_radial(h1, h2, coeff_abs2, which, sign=1):
    """phi = c E12/z (which='12') or c E21/z ('21'); |c/z|^2 = coeff_abs2. Returns the (1,1) and (2,2) entries."""
    ratio = h1 / h2 if which == "12" else h2 / h1
    comm = coeff_abs2 * ratio          # phi phi* for E12: E11 * |c|^2 h1/h2 /r^2 ; for E21: E22 * ...
    if which == "12":
        e11 = -sign * ddbar(sp.log(h1)) + comm; e22 = -sign * ddbar(sp.log(h2)) - comm
    else:
        e11 = -sign * ddbar(sp.log(h1)) - comm; e22 = -sign * ddbar(sp.log(h2)) + comm
    return sp.simplify(e11), sp.simplify(e22)
res = {}
res["nilpotent_b_solves"] = hitchin_radial(1 / (L + b), L + b, 1 / r ** 2, "12")
res["nilpotent_opposite_sign"] = hitchin_radial(1 / L, L, 1 / r ** 2, "12", sign=-1)
res["nilpotent_wrong_power_h=diag(1/L^2, L^2)"] = hitchin_radial(1 / L ** 2, L ** 2, 1 / r ** 2, "12")
# pointwise norm: |E12|_h = sqrt(h1/h2); unit vector e of 4|dz|^2/(r^2 L^2) has |dz(e)| = r L / 2; |dz(e)/z| = L/2
res["pointwise_nilpotent_b"] = sp.simplify(sp.sqrt((1 / (L + b)) / (L + b)) * L / 2)
res["pointwise_nilpotent_b_limit_r->0"] = sp.limit(res["pointwise_nilpotent_b"], r, 0, "+")
# semisimple: phi = diag(l, -l)/z commutes with phi*, flat h solves trivially; pointwise norm = l * L/2
res["semisimple_pointwise"] = l * L / 2
# uniformising: Phi = E21 dz with h = diag(g^-1/2, g^1/2): comm uses h2/h1 = g
g = 1 / (r ** 2 * L ** 2)
res["uniformising_cusp_solves"] = hitchin_radial(g ** sp.Rational(-1, 2), g ** sp.Rational(1, 2), 1, "21")
res["horocycle_length"] = sp.simplify(sp.integrate(2 / (r * L) * r, (sp.Symbol("t"), 0, 2 * sp.pi)))
for k, v in res.items(): print(k, ":", v)
