"""POST HOC (not sealed; written after the_scale_check.py's one run, and labelled so).

Why: the seal's reading of K4 took the residue's norm in h (1/L, decaying into the cusp) as "the field's size". The
audit lane's cusp condensate (weave_cusp_condensate_2026_10_08) shows the other natural measure: its coordinate field
q = E/(2 sqrt y) decays while the physical q-hat = E/2 is covariantly parallel. The same split must hold here: the
field theta = Res dz/z is a 1-form, and dz/z grows into the cusp. This computes the field's pointwise norm on unit
vectors of the complete hyperbolic metric 4|dz|^2/(|z|^2 L^2), for the nilpotent model (h = diag(1/L, L)) and for the
uniformising Higgs field (sign control of K4d), exactly.
"""
import json, pathlib
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
x, y = sp.symbols("x y", real=True)
r2 = x ** 2 + y ** 2
Lf = -sp.log(r2)
out = {}

# unit tangent vectors of 4|dz|^2/(|z|^2 L^2): |d/dx| = 2/(|z| L), so e = (|z| L / 2) d/dx and e' = (|z| L / 2) d/dy
s = sp.sqrt(r2) * Lf / 2
dz_e, dz_ep = s, sp.I * s                                   # dz(e), dz(e')
z = x + sp.I * y

# nilpotent model: theta = E12 dz/z, h = diag(1/L, L); operator norm of E12 in h is sqrt(h1/h2) = 1/L (K4b)
res_norm = 1 / Lf
pt_e = sp.simplify(res_norm * sp.Abs(dz_e / z))
pt_ep = sp.simplify(res_norm * sp.Abs(dz_ep / z))
out["nilpotent_model_pointwise_norm_on_unit_vectors"] = [str(pt_e), str(pt_ep)]
PTS = [(sp.Rational(1, 3), sp.Rational(1, 5)), (sp.Rational(1, 100), sp.Rational(1, 200)), (sp.Rational(-2, 5), sp.Rational(1, 7))]
out["nilpotent_model_numeric"] = [float(sp.N(pt_e.subs({x: a, y: b}), 20)) for a, b in PTS]
out["residue_norm_in_h_numeric"] = [float(sp.N(res_norm.subs({x: a, y: b}), 20)) for a, b in PTS]
out["dz_over_z_on_unit_vector_numeric"] = [float(sp.N(sp.Abs(dz_e / z).subs({x: a, y: b}), 20)) for a, b in PTS]

# uniformising Higgs field in K4d's normalisation: Phi = E21 dz, h = diag(g^-1/2, g^1/2), metric g |dz|^2 with
# g = 1/(|z|^2 L^2) (curvature -4).  |E21|_h = sqrt(h2/h1) = sqrt(g); a unit vector of g|dz|^2 has |dz(e)| = 1/sqrt(g)
g = 1 / (r2 * Lf ** 2)
uni = sp.simplify(sp.sqrt(g) * (1 / sp.sqrt(g)))
out["uniformising_pointwise_norm"] = str(uni)
out["holds_post_hoc"] = bool(all(abs(v - 0.5) < 1e-15 for v in out["nilpotent_model_numeric"]) and uni == 1)
(HERE / "post_hoc_pointwise.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
