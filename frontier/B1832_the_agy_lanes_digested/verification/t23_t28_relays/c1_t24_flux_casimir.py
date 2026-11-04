"""c1: Theorem 24 (toe_closure.py:4638-4853 @ 18c607040) re-derived from first principles with mpmath (no lane code).

V(tau; beta) = 2 pi^2 N_flux^2 / Im tau + N_gen * sum_f n_f [ 2 ln|theta1(a_f tau - b_f | tau) / eta(tau)| - 2 pi a_f^2 Im tau ],
a_f = (q_f alpha) mod 1 centred in (-1/2, 1/2], b_f = (q_f beta) mod 1, alpha = 2/5, (n_f, q_f) = (6,1),(3,-4),(3,2),(2,-3),(1,6)
(the lane's definition, l. 4659-4664).  Checks:
  (1) T-equivariance V(tau + m_j; beta_j) = V(tau; 1/2), m_j = (-1, 2, 0, -2, 1)
  (2) on beta = 1/2, V(-x, y) = V(x, y) (so d_x V = 0 at x = 0 by symmetry); the critical point y*, the Hessian
  (3) the critical point of line j = 0 at x = m_0 = -1 (2D Newton from the lane's start x = m_j + 0.18)
  (4) the 1D root along Re tau = 1/sqrt5 on beta = 1/10
  (5) the dependence of y* on the chosen integers (N_flux, N_gen) -- what fixes y*
  (6) the docstring's 'sum_p |theta_p/eta|^4 = 8 along Re tau = 1/sqrt5'
"""
import math
import pathlib
import mpmath as mp

mp.mp.dps = 25
SM = [(6, 1), (3, -4), (3, 2), (2, -3), (1, 6)]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def centred(v):
    v = v - mp.floor(v)
    return v - 1 if v > mp.mpf("0.5") else v

def log_abs_eta(tau):
    q = mp.exp(1j * mp.pi * tau)
    return mp.log(abs(mp.jtheta(1, 0, q, 1)) / 2) / 3          # theta1'(0) = 2 pi eta^3 in z-units; jtheta takes pi z

def V(x, y, beta, nflux=2, ngen=3, alpha=mp.mpf(2) / 5):
    x, y = mp.mpf(x), mp.mpf(y); tau = mp.mpc(x, y); q = mp.exp(1j * mp.pi * tau)
    le = log_abs_eta(tau); vf = mp.mpf(0)
    for n, qy in SM:
        a = centred(qy * alpha); b = (qy * mp.mpf(beta)) - mp.floor(qy * mp.mpf(beta))
        z = a * tau - b
        vf += n * (2 * (mp.log(abs(mp.jtheta(1, mp.pi * z, q))) - le) - 2 * mp.pi * a * a * y)
    return 2 * mp.pi ** 2 * nflux ** 2 / y + ngen * vf

def grad_hess(f, x, y, h=mp.mpf("1e-6")):
    fx = (f(x + h, y) - f(x - h, y)) / (2 * h); fy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    fxx = (f(x + h, y) - 2 * f(x, y) + f(x - h, y)) / h ** 2; fyy = (f(x, y + h) - 2 * f(x, y) + f(x, y - h)) / h ** 2
    fxy = (f(x + h, y + h) - f(x + h, y - h) - f(x - h, y + h) + f(x - h, y - h)) / (4 * h * h)
    return fx, fy, fxx, fxy, fyy

betas = [mp.mpf(2 * j + 1) / 10 for j in range(5)]; mj = [-1, 2, 0, -2, 1]
# (1) T-equivariance
worst = 0
for (x0, y0) in ((0.31, 2.15), (-0.2, 1.7), (0.47, 3.1)):
    ref = V(x0, y0, mp.mpf(1) / 2)
    for b, m in zip(betas, mj):
        worst = max(worst, abs(V(x0 + m, y0, b) - ref))
say("(1) max |V(tau + m_j; beta_j) - V(tau; 1/2)| over 3 points x 5 lines = %.2e" % worst)
# (2) symmetry and the critical point on beta = 1/2
sym = max(abs(V(x0, y0, 0.5) - V(-x0, y0, 0.5)) for x0, y0 in ((0.13, 2.2), (0.37, 2.9), (0.44, 1.6)))
say("(2) max |V(x,y;1/2) - V(-x,y;1/2)| = %.2e  (so d_x V(0, y; 1/2) = 0 exactly)" % sym)
f2 = lambda x, y: V(x, y, mp.mpf(1) / 2)
ystar = mp.findroot(lambda y: grad_hess(f2, mp.mpf(0), y)[1], mp.mpf("2.4"))
g = grad_hess(f2, mp.mpf(0), ystar); H = mp.matrix([[g[2], g[3]], [g[3], g[4]]]); ev = mp.eig(H)[0]
say("    y* (N_flux 2, N_gen 3) = %s ; lane: 2.411869510346569 ; |diff| = %.1e" % (mp.nstr(ystar, 16), abs(ystar - mp.mpf("2.411869510346569"))))
say("    Hessian eigenvalues at (0, y*): %s ; lane: [0.491575, 10.763756]" % [mp.nstr(mp.re(e), 7) for e in sorted(ev, key=lambda e: mp.re(e))])
# (3) 2D Newton on line j = 0 from x = m_0 + 0.18
f0 = lambda x, y: V(x, y, betas[0])
x, y = mp.mpf(-1) + mp.mpf("0.18"), mp.mpf("2.15")
for _ in range(12):
    fx, fy, fxx, fxy, fyy = grad_hess(f0, x, y)
    det = fxx * fyy - fxy ** 2
    x, y = x - (fyy * fx - fxy * fy) / det, y - (-fxy * fx + fxx * fy) / det
say("(3) line j=0 (beta 1/10): 2D Newton -> (%s, %s); expected (m_0, y*) = (-1, %s)" % (mp.nstr(x, 12), mp.nstr(y, 12), mp.nstr(ystar, 12)))
# (4) 1D root on Re tau = 1/sqrt5, beta = 1/10
xg = 1 / mp.sqrt(5)
y1 = mp.findroot(lambda y: grad_hess(f0, xg, y)[2 - 1], mp.mpf("2.4"))
d2 = grad_hess(f0, xg, y1)[4]
say("(4) Re tau = 1/sqrt5, beta = 1/10: d_y V = 0 at y = %s (lane 2.455567408910715), d2V/dy2 = %s (lane +10.812655)" % (mp.nstr(y1, 16), mp.nstr(d2, 8)))
# (5) what fixes y*: integers and the flux normalisation
say("(5) y* on beta = 1/2, x = 0, as the chosen integers vary (large-y slope of the Casimir part: 7 pi/5 per generation;"
    " estimate y* ~ N_flux * sqrt(10 pi / (7 N_gen))):")
for ng in (1, 2, 3):
    row = []
    for nf in (1, 2, 3, 4):
        f = lambda x, y, nf=nf, ng=ng: V(x, y, mp.mpf(1) / 2, nflux=nf, ngen=ng)
        try:
            ys = mp.findroot(lambda y: grad_hess(f, mp.mpf(0), y)[1], mp.mpf(nf) * mp.sqrt(10 * mp.pi / (7 * ng)))
            row.append("N_flux=%d: %s" % (nf, mp.nstr(ys, 6)))
        except Exception as e:
            row.append("N_flux=%d: no root (%s)" % (nf, type(e).__name__))
    say("    N_gen=%d: " % ng + "; ".join(row))
say("    flux coefficient c in c*N_flux^2/Im tau (lane: c = 2 pi^2), N_flux 2, N_gen 3:")
for c in (mp.pi ** 2, 2 * mp.pi ** 2, 4 * mp.pi ** 2, 2 * mp.pi):
    f = lambda x, y, c=c: V(x, y, mp.mpf(1) / 2, nflux=0) + c * 4 / y
    ys = mp.findroot(lambda y: grad_hess(f, mp.mpf(0), y)[1], mp.sqrt(c * 4 / (3 * 7 * mp.pi / 5)))
    say("      c = %s: y* = %s" % (mp.nstr(c, 6), mp.nstr(ys, 6)))
# (6) sum_p |theta_p / eta|^4 along Re tau = 1/sqrt5
for yy in (mp.mpf(1), (3 + mp.sqrt(5)) / 2, mp.mpf(4)):
    tau = mp.mpc(xg, yy); q = mp.exp(1j * mp.pi * tau); eta = mp.exp(log_abs_eta(tau))
    s = sum(abs(mp.jtheta(p, 0, q)) ** 4 for p in (2, 3, 4)) / eta ** 4
    say("(6) Re tau = 1/sqrt5, Im tau = %s: sum_p |theta_p/eta|^4 = %s" % (mp.nstr(yy, 8), mp.nstr(s, 10)))

pathlib.Path(__file__).with_name("c1_t24_flux_casimir_out.txt").write_text("\n".join(out) + "\n")
