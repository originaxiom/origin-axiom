"""B1691's addendum (P-240 assessed, no data): at weight 7/2, the lowest with a D2R component, a = alpha E4 R + beta D2R and
the leading coefficients give (m1/m3)/(m2/m3)^2 = Im tau * const * |t r + r2|^3 / (|r| |c22/(2 d11) - t|^2 |...|), t = alpha/beta.
Its pole (a.a's leading coefficient vanishes) and its zero (|a|^2's leading coefficient vanishes) are distinct, so the
ratio takes every positive value as the section's free t varies: B1691's exponents alone predict no mass.  Also the one
parameter-free covariant direction with a non-zero m2: weight 3/2, a = DR (dim 1), with m1 = 0 and m2/m3 = c |q|^(1/2)."""
import io, json, contextlib, importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("te", HERE / "the_exponents.py"); m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
B, dot, S, F = m.B, m.dot, m.S, m.F
vp = lambda u: (u[1] + u[2] * S.c(0, 1)) * S.c(F(1, 2))
r, r2 = vp(B[0]).d[-1], vp(B[2]).d[-1]; c22, d11 = dot(B[2], B[2]).d[2], dot(B[1], B[1]).d[2]
cf = lambda p: complex(float(p[0]), float(p[1]))
pole = cf(c22) / (2 * cf(d11)); zero = -cf(r2) / cf(r)
# a = DR alone: m2/m3 -> c |q|^(1/2): c = |R|^2 |a.a| / s1^2 at leading order
rd = vp(B[1]).d[-1]
c_DR = (2 * abs(cf(r)) ** 2 * abs(cf(d11))) / (16 * abs(cf(r)) ** 2 * abs(cf(rd)) ** 2)
out = {"r": [str(x) for x in r], "r2": [str(x) for x in r2], "D2R.D2R_x2": [str(x) for x in c22], "DR.DR_x2": [str(x) for x in d11],
       "pole_t": [pole.real, pole.imag], "zero_t": [zero.real, zero.imag], "distinct": abs(pole - zero) > 1e-12,
       "DR_on_v+_x^-1": [str(x) for x in rd], "weight_3/2_m2/m3_over_|q|^(1/2)": c_DR}
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_coefficients_are_free.json", "w"), indent=1); print(json.dumps(out, indent=1))
