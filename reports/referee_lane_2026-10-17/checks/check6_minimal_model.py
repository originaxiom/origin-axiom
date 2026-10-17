"""The zero-coefficient model: the unique weight-1 Yukawa form Y1 in M_1(rhobar x rhobar) (L, R both in T).
Masses are the singular values of Y1(tau) up to one overall scale per sector.
Scan tau over the fundamental domain and compare (m1/m3, m2/m3) with the data at M_Z (Huang-Zhou 2021)."""
import numpy as np, mpmath as mp, itertools, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from check5_yukawa_dims import form_space, with_cusp_condition, rho_u_t, rho_u_s, monomials

Rt = np.kron(rho_u_t.conj(), rho_u_t.conj()); Rs = np.kron(rho_u_s.conj(), rho_u_s.conj())
K = 10
null, monos = form_space(Rt, Rs, K)
nullc = with_cusp_condition(null, monos, 9, 3)
assert nullc.shape[1] == 1
v = nullc[:, 0]; n = len(monos)
coef = v.reshape(9, n)
# print the form's monomial content
print("monomials of F = eta^18 Y1 (weight 10):")
for i in range(9):
    terms = [(monos[m], coef[i, m]) for m in range(n) if abs(coef[i, m]) > 1e-9]
    print(f"  F[{i//3},{i%3}]: " + ", ".join(f"{np.round(c,4)}*X^{a}Y^{b}Z^{c_}" for (a,b,c_), c in terms))

mp.mp.dps = 20
def XYZ(t):
    q = mp.exp(1j*mp.pi*t)
    return mp.jtheta(2,0,q)**2, mp.jtheta(3,0,q)**2, mp.jtheta(4,0,q)**2
def eta(t):
    q = mp.exp(2j*mp.pi*t); return mp.exp(2j*mp.pi*t/24)*mp.nprod(lambda k: 1-q**k, [1, mp.inf])
def Y1(t):
    X, Y, Z = XYZ(t); e18 = eta(t)**18
    M = np.zeros((3, 3), dtype=complex)
    for i in range(9):
        val = sum(coef[i, m]*complex(X**a * Y**b * Z**c) for m, (a, b, c) in enumerate(monos) if abs(coef[i, m]) > 1e-12)
        M[i//3, i%3] = val/complex(e18)
    return M
# check: symmetric, and the covariance under T and S (weight 1, rhobar x rhobar)
t0 = mp.mpc(0.17, 1.23)
M0 = Y1(t0); print("\nsymmetric:", np.abs(M0 - M0.T).max() < 1e-9*np.abs(M0).max())
chi_t = np.exp(2j*np.pi/24); chi_s = np.exp(-1j*np.pi/4)
rb_t = (chi_t**3) * rho_u_t.conj(); rb_s = (chi_s**3) * rho_u_s.conj()
def vec(M): return M.reshape(-1)
lhsT = vec(Y1(t0 + 1)); rhsT = np.kron(rb_t, rb_t) @ vec(M0)
lhsS = vec(Y1(-1/t0)); rhsS = np.kron(rb_s, rb_s) @ vec(M0) * complex(t0)**1
print("covariance T:", np.abs(lhsT - rhsT).max()/np.abs(rhsT).max(), " covariance S:", np.abs(lhsS - rhsS).max()/np.abs(rhsS).max())

def ratios(t):
    s = np.linalg.svd(Y1(t), compute_uv=False)
    return s[2]/s[0], s[1]/s[0], s   # m1/m3, m2/m3
print("\nratios at special points:")
for name, t in [("i", mp.mpc(0,1)), ("omega", mp.exp(2j*mp.pi/3)), ("2i", mp.mpc(0,2)), ("3i", mp.mpc(0,3)), ("0.5+2i", mp.mpc(0.5,2)), ("0.5+3i", mp.mpc(0.5,3))]:
    r1, r2, s = ratios(t); print(f"  tau={name}: m1/m3={r1:.3e}, m2/m3={r2:.3e}")
# scan
data = {"up": (1.23e-3/168.26, 0.620/168.26), "down": (2.67e-3/2.839, 53.16e-3/2.839), "lep": (0.48307e-3/1.72856, 0.101766/1.72856)}
print("\ndata (m1/m3, m2/m3):", {k: (f"{a:.2e}", f"{b:.2e}") for k, (a, b) in data.items()})
best = {k: (1e9, None) for k in data}
grid = []
for x in np.linspace(-0.5, 0.5, 41):
    for y in np.linspace(0.87, 6.0, 120):
        if x*x + y*y < 1: continue
        t = mp.mpc(x, y); r1, r2, s = ratios(t)
        grid.append((x, y, r1, r2))
        for k, (d1, d2) in data.items():
            dist = (np.log(r1/d1))**2 + (np.log(r2/d2))**2
            if dist < best[k][0]: best[k] = (dist, (x, y, r1, r2))
grid = np.array(grid)
print("\nrange over the fundamental domain (y <= 6): m2/m3 in [%.2e, %.2e], m1/m3 in [%.2e, %.2e]" % (grid[:,3].min(), grid[:,3].max(), grid[:,2].min(), grid[:,2].max()))
for k, (dist, pt) in best.items():
    x, y, r1, r2 = pt
    print(f"  closest to {k}: tau = {x:.3f} + {y:.3f}i -> (m1/m3, m2/m3) = ({r1:.2e}, {r2:.2e}); log-distance {np.sqrt(dist):.2f}")
# how do the ratios scale toward the cusp along the imaginary axis and along x=1/2?
print("\ncusp behaviour (q = e^{-pi y}):")
for y in (2, 3, 4, 5):
    for x in (0.0, 0.5):
        r1, r2, s = ratios(mp.mpc(x, y)); print(f"  tau={x}+{y}i: m1/m3={r1:.2e}  m2/m3={r2:.2e}   e^(-pi y)={np.exp(-np.pi*y):.1e}  e^(-pi y/2)={np.exp(-np.pi*y/2):.1e}")
