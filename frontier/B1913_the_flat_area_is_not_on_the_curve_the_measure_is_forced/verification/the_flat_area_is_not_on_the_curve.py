"""P-776, condition R6 (the place survives its chosen ingredients): is the chart's flat area an admissible ingredient?
Main's reading, written before the run: an ingredient of a read-out on the whole must be defined on the curve, that is,
unchanged by the group. The hyperbolic area is the only invariant area up to scale, and against it the state's density is
|f|^2, a function on the curve. The flat density |f|^2 / y^2 changes by |cz + d|^4 under a move, so it is not a function on
the curve, and its greatest place depends on which chart of the curve is drawn.
CHECKS: (1) |f|^2 is unchanged by two moves of Gamma0(5); (2) |f|^2 / y^2 is not; (3) the flat density's greatest place
found in the standard chart and in the chart moved by a group element, carried back, are two different points of the
curve, while the greatest place of |f|^2 is the same point in both charts. Uses B1885's construction of the state (its
code, main's own), imported; nothing is compared with any value of the modulus on record."""
import sys, pathlib, json
import mpmath as mp
from scipy.optimize import minimize
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]                   # verification -> the arc -> frontier -> the root
sys.path.insert(0, str(ROOT / "frontier" / "B1885_the_golden_state_on_the_whole_verified" / "verification"))
import golden_state_on_main as G
mp.mp.dps = 20
F5 = G.Field(5); f = G.Form(F5, 900)
def mob(g, z): return (g[0] * z + g[1]) / (g[2] * z + g[3])
def dens(z): return abs(f(z)) ** 2
def flat(z): return abs(f(z)) ** 2 / mp.im(z) ** 2
def run():
    OUT = {}
    z = mp.mpc("0.24", "0.40")
    for g in ((1, 0, 5, 1), (2, -1, 5, -2)):
        w = mob(g, z)
        OUT["move %s: |f|^2 ratio" % (g,)] = float(dens(w) / dens(z))
        OUT["move %s: flat density ratio" % (g,)] = float(flat(w) / flat(z))
        OUT["move %s: |cz+d|^4" % (g,)] = float(abs(g[2] * z + g[3]) ** 4)
    # the greatest place of each density, in the standard chart and in the chart moved by gam, carried back
    gam = (1, 0, 5, 1); gi = (1, 0, -5, 1)
    def argmax(fun, z0, chart):
        def neg(p):
            zz = mp.mpc(p[0], p[1]); w = mob(chart, zz) if chart else zz
            return -float(fun(w))
        r = minimize(neg, [float(mp.re(z0)), float(mp.im(z0))], method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 4000})
        return mp.mpc(r.x[0], r.x[1])
    zstar = mp.mpc("0.2515", "0.3698")
    for name, fun in (("|f|^2", dens), ("|f|^2/y^2", flat)):
        p_std = argmax(fun, zstar, None)                          # in the standard chart
        p_mov = argmax(fun, zstar, gam)                           # the density read in the moved chart: maximise fun(gam z), z near zstar
        OUT[name] = {"standard chart": [float(mp.re(p_std)), float(mp.im(p_std))], "moved chart, carried back": [float(mp.re(p_mov)), float(mp.im(p_mov))],
                     "distance between the two": float(abs(p_std - p_mov))}
        print(name, OUT[name], flush=True)
    for k, v in OUT.items():
        if not isinstance(v, dict): print(k, v)
    return OUT

if __name__ == "__main__":
    json.dump(run(), open(HERE / "the_flat_area_is_not_on_the_curve.json", "w"), indent=1)
