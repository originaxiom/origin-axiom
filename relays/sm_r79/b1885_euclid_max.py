"""SM-R79 own check of B1885 A5: the continuous maximum of f^2/y^2 near the peak, f taken from the arc's own construction
(Field, Form, imported from its script), the maximum found by Newton on the gradient from the grid's best point.
Usage: b1885_euclid_max.py PATH/TO/golden_state_on_main.py (from a checkout of main at 323f92327)."""
import importlib.util, sys
import mpmath as mp
spec = importlib.util.spec_from_file_location("g", sys.argv[1])
g = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]
spec.loader.exec_module(g)            # defines the classes; main() is guarded by __name__
mp.mp.dps = 30
F5 = g.Field(5)
f = g.Form(F5, 720)
zs = mp.mpc("0.251539778143593605", "0.369767142958202424")     # the peak as B1885's run prints it (line 15)
peak = f(zs) ** 2
E = lambda x, y: f(mp.mpc(x, y)) ** 2 / y ** 2
x0, y0 = mp.mpf("0.255"), mp.mpf("0.31293")
gx = lambda x, y: mp.diff(lambda t: E(t, y), x)
gy = lambda x, y: mp.diff(lambda t: E(x, t), y)
xm, ym = mp.findroot([gx, gy], (x0, y0))
zm = mp.mpc(xm, ym)
print("continuous max of f^2/y^2 at z =", mp.nstr(zm, 12), " |z|^2 =", mp.nstr(abs(zm) ** 2, 8),
      " distance from the peak =", mp.nstr(abs(zm - zs), 8))
print("value there over the grid point's:", mp.nstr(E(xm, ym) / E(x0, y0), 12))
print("grid point: |z|^2 =", mp.nstr(abs(mp.mpc(x0, y0)) ** 2, 8), " distance =", mp.nstr(abs(mp.mpc(x0, y0) - zs), 8))
