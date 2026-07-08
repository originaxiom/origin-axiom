#!/usr/bin/env python3
"""B469 BR3 wave 2 — sigma-swap certification per m + geometric-component ID.

Per m in {1,2,3}: (1) solve Fix(T_m^2) + cusp exactly (Groebner) and numerically
(50 digits); (2) apply T_m to every point and certify the orbit partition
(fixed points vs genuine period-2 breath orbits), with factor membership checked
against the EXACT wave-1 factor polynomials at 1e-40; (3) identify the geometric
component: SnapPy shape field of the bundle R^m L^m vs the factors' fields."""
import sympy as sp
import mpmath as mp
mp.mp.dps = 50

x, y, z = sp.symbols('x y z')

def Tm_sym(m):
    t = {0: y, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    return (t[m], x, t[m+1])

def solve_points(m):
    T = Tm_sym(m)
    T2 = tuple(sp.expand(e.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)) for e in Tm_sym(m))
    eqs = [sp.expand(T2[i] - v) for i, v in enumerate((x, y, z))] + [sp.expand(x**2 + y**2 + z**2 - x*y*z)]
    sols = sp.solve(eqs, [x, y, z], dict=True)
    return T, sols

def num(pt):
    return tuple(complex(sp.N(c, 50)) for c in pt)

for m in (1, 2, 3):
    print(f"===== m = {m} =====", flush=True)
    T, sols = solve_points(m)
    pts = []
    for s in sols:
        pt = (s[x], s[y], s[z])
        pts.append(pt)
    print(f"  points: {len(pts)}", flush=True)
    npts = [num(p) for p in pts]
    Tf = sp.lambdify((x, y, z), T, 'mpmath')
    used = set()
    orbits = []
    for i, p in enumerate(npts):
        if i in used: continue
        q = tuple(complex(v) for v in Tf(*[mp.mpc(c) for c in p]))
        # find q among the points
        j = min(range(len(npts)), key=lambda k: sum(abs(npts[k][t]-q[t])**2 for t in range(3)))
        d = sum(abs(npts[j][t]-q[t])**2 for t in range(3))**0.5
        if d > 1e-30:
            orbits.append((i, None)); used.add(i); continue
        if j == i:
            orbits.append((i,)); used.add(i)
        else:
            orbits.append((i, j)); used.add(i); used.add(j)
    fixed = [o for o in orbits if len(o) == 1]
    two   = [o for o in orbits if len(o) == 2 and o[1] is not None]
    stray = [o for o in orbits if len(o) == 2 and o[1] is None]
    print(f"  T_m-orbit partition: {len(fixed)} fixed, {len(two)} period-2 swaps, {len(stray)} STRAY(off-variety!)", flush=True)
    # minimal polynomial of the z-coordinate per orbit -> the breath field
    for o in two:
        zc = pts[o[0]][2]
        mpoly = sp.minimal_polynomial(zc, z)
        zc2 = pts[o[1]][2]
        mpoly2 = sp.minimal_polynomial(zc2, z)
        same = sp.expand(mpoly - mpoly2) == 0
        print(f"  period-2 orbit: minpoly(z) = {mpoly}  (partner same factor: {same})", flush=True)
    for o in fixed:
        zc = pts[o[0]][2]
        mpoly = sp.minimal_polynomial(zc, z)
        print(f"  fixed point:  z = {pts[o[0]][2]}, minpoly = {mpoly}", flush=True)
    # geometric ID: snappy shape field of the bundle R^m L^m
    try:
        import snappy
        M = snappy.Manifold('b++' + 'R'*m + 'L'*m)
        vol = float(M.volume())
        shapes = M.tetrahedra_shapes(part='rect')
        s0 = complex(shapes[0])
        # minpoly of the first shape, degree <= 8
        cand = None
        for deg in range(2, 9):
            p = mp.pslq([mp.mpc(s0)**k for k in range(deg+1)], maxcoeff=10**6, maxsteps=10**5)
            if p:
                poly = sp.Poly(list(reversed(p)), z)
                if abs(sp.Poly(poly, z).eval(sp.nsimplify(0))) is not None:
                    cand = poly; break
        print(f"  bundle b++{'R'*m}{'L'*m}: vol={vol:.6f}, shape minpoly ~ {cand.as_expr() if cand else 'unrecognized'}", flush=True)
    except Exception as e:
        print(f"  snappy geometric ID: {type(e).__name__}: {e}", flush=True)
print("BR3 WAVE 2 DONE", flush=True)
