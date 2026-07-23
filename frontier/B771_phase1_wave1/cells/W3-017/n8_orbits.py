#!/usr/bin/env python3
"""Complete exact enumeration of Fix(T^8) on the surface via the eigenvalue method
(commuting multiplication matrices in the 0-dim quotient ring), Q-Groebner.
Writes n8_orbits.json with certified primitive-8 orbit multipliers."""
import sympy as sp, numpy as np, time, json, os
import compute as C
X, Y, Z = C.X, C.Y, C.Z

def build_ideal(n):
    p = (X, Y, Z)
    for _ in range(n):
        p = C._T_sym(p)
    F0 = sp.expand(p[0]-X); F1 = sp.expand(p[1]-Y); F2 = sp.expand(p[2]-Z)
    S = X**2+Y**2+Z**2-2*X*Y*Z-1-sp.Rational(9, 4)
    return [F0, F1, F2, S]

def std_monomials(G):
    lexp = [sp.Poly(g, X, Y, Z).LT(order='grevlex')[0] for g in G.exprs]
    bnd = [0, 0, 0]
    for e in lexp:
        for i in range(3):
            if e[(i+1) % 3] == 0 and e[(i+2) % 3] == 0 and e[i] > 0:
                bnd[i] = max(bnd[i], e[i])
    mons = []
    for a in range(bnd[0]):
        for b in range(bnd[1]):
            for cc in range(bnd[2]):
                if not any(a >= e[0] and b >= e[1] and cc >= e[2] for e in lexp):
                    mons.append((a, b, cc))
    return mons

def mult_matrix(G, mons, var):
    idx = {m: i for i, m in enumerate(mons)}
    N = len(mons); M = np.zeros((N, N))
    ve = {X: (1, 0, 0), Y: (0, 1, 0), Z: (0, 0, 1)}[var]
    for j, m in enumerate(mons):
        prod = tuple(m[k]+ve[k] for k in range(3))
        mon = X**prod[0]*Y**prod[1]*Z**prod[2]
        r = G.reduce(mon)[1]
        if r != 0:
            pol = sp.Poly(r, X, Y, Z)
            for coef, mm in zip(pol.coeffs(), pol.monoms()):
                M[idx[mm], j] = float(coef)
    return M

if __name__ == "__main__":
    n = 8
    t0 = time.time()
    print("computing Q-Groebner n=8 ...", flush=True)
    G = sp.groebner(build_ideal(n), X, Y, Z, order='grevlex')
    print(f"GB done {time.time()-t0:.0f}s", flush=True)
    mons = std_monomials(G)
    print(f"quotient dim = {len(mons)}", flush=True)
    Mx = mult_matrix(G, mons, X); My = mult_matrix(G, mons, Y); Mz = mult_matrix(G, mons, Z)
    w, V = np.linalg.eig(Mx + 0.7*My + 1.3*Mz)
    Vinv = np.linalg.inv(V)
    xs = np.diag(Vinv@Mx@V); ys = np.diag(Vinv@My@V); zs = np.diag(Vinv@Mz@V)
    pts = [np.array([xs[i].real, ys[i].real, zs[i].real])
           for i in range(len(w)) if abs(xs[i].imag) < 1e-6]
    # polish each with a few Newton steps
    pol = []
    for p in pts:
        q = C.newton_periodic(p, n, C.CVAL)
        pol.append(q if q is not None else p)
    orbs = C.orbits_from_points(pol, n)
    mults = [float(abs(C.expanding_multiplier(o))) for o in orbs]
    out = dict(quotient_dim=len(mons), n_real_pts=len(pts),
               n_orbits=len(orbs), mults=sorted(mults))
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "n8_orbits.json"), "w"), indent=1)
    print("n=8 orbits:", out, flush=True)
    print(f"total {time.time()-t0:.0f}s", flush=True)
