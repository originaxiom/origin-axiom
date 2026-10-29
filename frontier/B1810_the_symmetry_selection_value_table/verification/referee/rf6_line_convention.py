"""rf6: which line transformation does b1656_funcs' frame actually obey?  At a generic tau0 and line p, with the
covariant section DR (k = 3/2), compare the spectra at (tau0, p) with those at (g tau0, p') for g = T and S and the
candidate p' of the w/(c tau + d) convention [(p1,p2) = [[a,-c],[-b,d]] (p1',p2')], against wrong conventions as
controls.  Same L (a number) on both sides.  Then the order-3 element g = [[1,-1],[1,0]] at e^{i pi/3}: g.(1/3,2/3)."""
import numpy as np
from rf_common import *
def spec(tau, p, L=2.5, sec="DR", q=(1, -4)):
    a = direction(sec, tau); s = np.linalg.svd(Ymat(a, tau, p, q[0], q[1], L), compute_uv=False); return s / s[0]
def conv(g, p):          # p' = M^{-1} p with M = [[a,-c],[-b,d]]
    a, b, c, d = g; M = np.array([[a, -c], [-b, d]], float); return tuple(np.linalg.solve(M, np.array(p, float)))
def act(g, tau): a, b, c, d = g; return (a * tau + b) / (c * tau + d)
tau0 = complex(0.23, 1.17); p = (0.1, 0.3)
for nm, g in (("T", (1, 1, 0, 1)), ("S", (0, -1, 1, 0))):
    t1 = act(g, tau0); pr = conv(g, p)
    for lab, pp in (("w/(c tau+d) convention", pr), ("its negative", (-pr[0], -pr[1])), ("control: p unchanged", p),
                    ("control: transpose convention", tuple(np.array([[g[0], g[2]], [g[1], g[3]]], float) @ np.array(p)))):
        for q in ((1, -4), (1, 2), (-3, 6)):
            d = np.max(abs(spec(tau0, p, q=q) - spec(t1, pp, q=q)))
            print("%s: (%.3f%+.3fi, %s) vs (%.3f%+.3fi, (%.4f, %.4f)) %-30s sector %s  max diff %.1e" % (nm, tau0.real, tau0.imag, p, t1.real, t1.imag, pp[0] % 1, pp[1] % 1, lab, q, d))
g3 = (1, -1, 1, 0); print("order-3 element fixes e^{i pi/3}:", abs(act(g3, W) - W)); print("g3.(1/3,2/3) =", tuple(x % 1 for x in conv(g3, (1/3, 2/3))))
print("S fixes i:", abs(act((0, -1, 1, 0), I) - I), " S.(1/2,1/2) =", tuple(x % 1 for x in conv((0, -1, 1, 0), (0.5, 0.5))))
