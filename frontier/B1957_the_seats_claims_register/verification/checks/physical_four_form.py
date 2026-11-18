"""B1957: the physical lane's package 'four form register' (PHYSICAL-C7, 2026-11-17): the finite mathematics of its
six hand derivations, rebuilt on main along the discriminators its own review brief asks for.  Nothing of the lane's
is run.  NOT verified here: the nonlinear family (its implicit-function steps on the lane's weighted spaces), the
complete fermion domain, and that these four coefficients are the lane's physical form modes with this kinetic term.
 G1  the quotient: Z = P R^t has determinant 0; a balanced representative of a rank-one matrix exists and is unique up
     to the circle; the Kahler potential 2 sqrt(tr Z Z^dagger) is |P|^2 + |R|^2 there.
 G2  the Gauss connection: minimising |dP - i b P|^2 + |dR + i b R|^2 over b gives b = [Im(P^dagger dP) - Im(R^dagger dR)]/N
     and the metric |dP|^2 + |dR|^2 - J^2/N; with a plus sign on the negative charge the minimiser is another one;
     a local phase change shifts the connection by d phi.
 G3  the primitive period: on v = conj(u) the connection is the Hopf one, with curvature integral 2 pi; keeping one of
     the two Hopf terms gives half of it; the latitude's holonomy is exp(-i pi (1 - cos theta0)).
 G4  the centre: on E8 the charges Q = (2/3)(e1 + e2 + e3) are 0, +-1/3, +-2/3, +-1, +-4/3, so exp(2 pi i Q) has order 3
     and is 1 on the charges +-1; under V -> diag(det V^-1, V) the phase V = exp(-i phi/3) has charges +1 and -1/3; the
     transition diag(exp(i x), exp(-i x), 1, 1) has determinant 1 and closes.
 G5  the reduced symplectic potential t^2 (a_u + a_v) vanishes on v = conj(u); the connection does not change when the
     action is scaled.
 G6  the direct pair map: U(exp(i phi) u) = U(u) D_phi; on the orbit of (i, j) the commutator trace is 2 - 4 cos^2 phi;
     with a reference phase carried the pair is invariant, and with the reference left fixed it is not; with a reference
     of weight nu^2 the Gauss field is (J + nu^2 dchi)/(N + nu^2) and the added term N nu^2/(N + nu^2) (dchi - A)^2; the
     shear (X, Y) -> (X, X + Y) preserves |Y - tau X|^2/Im tau when tau -> tau + 1.
 G7  the composite A = U J U^-1, W = U U(conj v)^-1: invariant on the circle's orbits; the quotient metric is
     (t^2/2)(|DA|^2 + |k|^2) with DA = dA - [k, A]/2, and the connection a_u - <A, k>/2 (finite differences on a random
     curve); tr[A, W] = 2 - 4(|w|^2 - (n.w)^2); v -> i v is (A, W) -> (A, A W), of order 4; at W = -A the product A W is 1.
 G8  the radial chart: under v -> exp(i theta(t)) v the leading metric changes by t^2 theta' dt (a_u + a_v) +
     (t^2/2) theta'^2 dt^2 (a random tangent).
 G9  the constrained phase: with int b = beta fixed the least extra energy is Delta^2 / int dx/N, attained at
     b = a + Delta/(R N); two intervals sew to (beta - I1 - I2)^2/(R1 + R2)."""
import functools, itertools, math
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
rng = np.random.default_rng(49)
cvec = lambda n=2: rng.normal(size=n) + 1j * rng.normal(size=n)
unit = lambda: (lambda x: x / np.linalg.norm(x))(cvec())
Um = lambda u: np.array([[u[0], -np.conj(u[1])], [u[1], np.conj(u[0])]])
Dp = lambda ph: np.diag([np.exp(1j * ph), np.exp(-1j * ph)])
Jm = np.diag([1j, -1j]); ip = lambda X, Y: float((-np.trace(X @ Y) / 2).real)
com = lambda X, Y: X @ Y - Y @ X; gc = lambda X, Y: X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y)

def quot(P, R, dP, dR):
    J = (np.vdot(P, dP)).imag - (np.vdot(R, dR)).imag; N = np.vdot(P, P).real + np.vdot(R, R).real
    return np.vdot(dP, dP).real + np.vdot(dR, dR).real - J * J / N, J / N

if __name__ == "__main__":
    P, R = cvec(), cvec(); Z = np.outer(P, R); lam = (np.vdot(R, R).real / np.vdot(P, P).real) ** 0.25; Pb, Rb = lam * P, R / lam
    print("G1: |det Z| = %.1e; the balanced representative has |P|^2 - |R|^2 = %.1e and the same Z (%.1e); 2 sqrt(tr Z Z^dagger) minus (|P|^2 + |R|^2) there: %.1e" % (
        abs(np.linalg.det(Z)), np.vdot(Pb, Pb).real - np.vdot(Rb, Rb).real, np.abs(np.outer(Pb, Rb) - Z).max(), 2 * math.sqrt(np.trace(Z @ Z.conj().T).real) - (np.vdot(Pb, Pb).real + np.vdot(Rb, Rb).real)))
    dP, dR = cvec(), cvec(); en = lambda b, sgn=1: np.vdot(dP - 1j * b * P, dP - 1j * b * P).real + np.vdot(dR + sgn * 1j * b * R, dR + sgn * 1j * b * R).real
    g, A = quot(P, R, dP, dR); bs = np.linspace(A - 1, A + 1, 20001); bmin = bs[np.argmin([en(b) for b in bs])]; bwrong = bs[np.argmin([en(b, -1) for b in bs])]
    ph, dph = 0.7, 0.3; P2, R2 = np.exp(1j * ph) * P, np.exp(-1j * ph) * R; dP2, dR2 = np.exp(1j * ph) * (dP + 1j * dph * P), np.exp(-1j * ph) * (dR - 1j * dph * R)
    print("G2: the minimiser by search %.4f against the formula %.4f; the least energy %.6f against the metric %.6f; with a plus sign on the negative charge the minimiser is %.4f; after a phase change with d phi = %.1f the connection moves by %.6f and the metric by %.1e" % (bmin, A, en(A), g, bwrong, dph, quot(P2, R2, dP2, dR2)[1] - A, quot(P2, R2, dP2, dR2)[0] - g))
    th, vp = sp.symbols("theta varphi", real=True); u = sp.Matrix([sp.cos(th / 2), sp.exp(sp.I * vp) * sp.sin(th / 2)])
    a_u = lambda var: sp.simplify(sp.im((u.H * u.diff(var))[0])); Aphi = a_u(vp); F = sp.simplify(sp.diff(Aphi, th)); per = sp.integrate(sp.integrate(F, (th, 0, sp.pi)), (vp, 0, 2 * sp.pi)) / (2 * sp.pi)
    th0 = sp.symbols("theta0", positive=True); hol = sp.simplify(2 * sp.pi * Aphi.subs(th, th0) - sp.pi * (1 - sp.cos(th0)))
    print("G3: a_u = %s d varphi (and %s d theta); the curvature %s; its integral over the sphere divided by 2 pi: %s; with one Hopf term only: %s; the latitude's phase minus pi (1 - cos theta0): %s" % (Aphi, a_u(th), F, per, per / 2, hol))
    roots = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); roots.add(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0: roots.add(tuple(Fr(s, 2) for s in signs))
    Q = sorted({Fr(2, 3) * (r[0] + r[1] + r[2]) for r in roots}); order = sp.ilcm(*[q.denominator for q in Q])
    x = 0.9; tr = np.diag([np.exp(1j * x), np.exp(-1j * x), 1, 1])
    print("G4: the charges on E8: %s; exp(2 pi i Q) has order %d and is 1 on the charges +-1: %s; V = exp(-i phi/3) on the four: charges (+1, -1/3, -1/3, -1/3), sum %s; the transition has determinant %.1f and returns to 1 at x = 2 pi" % ([str(q) for q in Q], order, all((q * 1).denominator == 1 for q in Q if abs(q) == 1), 1 + 3 * Fr(-1, 3), np.linalg.det(tr).real))
    uu = unit(); du = cvec(); du -= uu * np.vdot(uu, du).real; vv = np.conj(uu); dv = np.conj(du); au = np.vdot(uu, du).imag; av = np.vdot(vv, dv).imag; t = 0.8
    g1, A1 = quot(t * uu, t * vv, t * du, t * dv); g5, A5 = quot(2.3 * t * uu, 2.3 * t * vv, 2.3 * t * du, 2.3 * t * dv)
    print("G5: on v = conj(u): t^2 (a_u + a_v) = %.1e while the connection is a_u (difference %.1e); the fields scaled by 2.3: the connection changes by %.1e" % (t * t * (au + av), A1 - au, A5 - A1))
    u1 = unit(); ok6 = np.abs(Um(np.exp(1j * 0.4) * u1) - Um(u1) @ Dp(0.4)).max()
    qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); trs = [(float(np.trace(gc(qi @ Dp(p), qj @ Dp(-p))).real), 2 - 4 * math.cos(p) ** 2) for p in (0.0, 0.5, math.pi / 2)]
    Ar, Br = Um(unit()), Um(unit()); zeta = np.exp(0.3j); rel = lambda A_, B_, z: (A_ @ np.linalg.inv(np.diag([z, 1 / z])), B_ @ np.diag([z, 1 / z])); p = 0.9
    inv_with = max(np.abs(a - b).max() for a, b in zip(rel(Ar, Br, zeta), rel(Ar @ Dp(p), Br @ Dp(-p), zeta * np.exp(1j * p)))); inv_without = max(np.abs(a - b).max() for a, b in zip(rel(Ar, Br, zeta), rel(Ar @ Dp(p), Br @ Dp(-p), zeta)))
    b_, J_, N_, nu, dchi = sp.symbols("b J N nu dchi", real=True); Eb = N_ * b_ ** 2 - 2 * b_ * J_ + nu ** 2 * (dchi - b_) ** 2; bst = sp.solve(sp.diff(Eb, b_), b_)[0]
    red = sp.simplify(Eb.subs(b_, bst) - (-J_ ** 2 / N_ + N_ * nu ** 2 / (N_ + nu ** 2) * (dchi - J_ / N_) ** 2))
    tau = 0.3 + 1.2j; X6, Y6 = rng.normal(size=3), rng.normal(size=3); Gt = lambda tt, X_, Y_: np.linalg.norm(Y_ - tt * X_) ** 2 / tt.imag
    print("G6: U(exp(i phi) u) = U(u) D_phi to %.1e; the commutator trace on the orbit of (i, j) at phi = 0, 0.5, pi/2 against 2 - 4 cos^2: %s; the relational pair moves by %.1e with the reference carried and by %.2f with it fixed; the Gauss field with a reference: %s, and the reduced energy minus the note's: %s; the period metric before and after the shear: %.6f, %.6f" % (
        ok6, [(round(a, 6), round(b, 6)) for a, b in trs], inv_with, inv_without, sp.simplify(bst), red, Gt(tau, X6, Y6), Gt(tau + 1, X6, X6 + Y6)))
    # G7: a random curve on S^3 x S^3
    def curve(s, seed=(unit(), unit(), cvec(), cvec())):
        u0, v0, d1, d2 = seed; u_ = u0 + s * d1 + s * s * d2; v_ = v0 + s * d2 - s * s * d1; return u_ / np.linalg.norm(u_), v_ / np.linalg.norm(v_)
    AW = lambda u_, v_: (Um(u_) @ Jm @ np.linalg.inv(Um(u_)), Um(u_) @ np.linalg.inv(Um(np.conj(v_))))
    h = 1e-5; (um, vm), (u0, v0), (up_, vp_) = curve(-h), curve(0.0), curve(h); du_, dv_ = (up_ - um) / (2 * h), (vp_ - vm) / (2 * h)
    A0_, W0_ = AW(u0, v0); dA = (AW(up_, vp_)[0] - AW(um, vm)[0]) / (2 * h); dW = (AW(up_, vp_)[1] - AW(um, vm)[1]) / (2 * h); k = dW @ np.linalg.inv(W0_); DA = dA - com(k, A0_) / 2
    lhs, conn = quot(t * u0, t * v0, t * du_, t * dv_); rhs = t * t / 2 * (ip(DA, DA) + ip(k, k)); conn2 = np.vdot(u0, du_).imag - ip(A0_, k) / 2
    inv7 = max(np.abs(x_ - y_).max() for x_, y_ in zip(AW(u0, v0), AW(np.exp(0.6j) * u0, np.exp(-0.6j) * v0)))
    W7 = Um(unit()); trAW = np.trace(gc(A0_, W7)).real
    # imaginary vector of a unit quaternion a + b i + c j + d k as the matrix [[a + b i, c + d i], [-c + d i, a - b i]]
    imv = lambda M: np.array([M[0, 0].imag, M[0, 1].real, M[0, 1].imag]); nA, wv = imv(A0_), imv(W7)
    shear = np.abs(AW(u0, 1j * v0)[1] - A0_ @ W0_).max(); four = max(np.abs(a - b).max() for a, b in zip(AW(u0, (1j) ** 4 * v0), AW(u0, v0)))
    print("G7: the composite is unchanged on a circle orbit to %.1e; the quotient metric %.8f against (t^2/2)(|DA|^2 + |k|^2) = %.8f; the connection %.8f against a_u - <A, k>/2 = %.8f; tr[A, W] = %.6f against 2 - 4(|w|^2 - (n.w)^2) = %.6f; v -> i v gives (A, A W) to %.1e and has order 4 (%.1e); at W = -A: A W = 1 to %.1e" % (
        inv7, lhs, rhs, conn, conn2, trAW, 2 - 4 * (wv @ wv - (nA @ wv) ** 2), shear, four, np.abs(A0_ @ (-A0_) - np.eye(2)).max()))
    # G8
    tv, dt, thp = 0.7, 0.4, 1.3; au8, av8 = np.vdot(u0, du_).imag, np.vdot(v0, dv_).imag
    g_before, _ = quot(tv * u0, tv * v0, dt * u0 + tv * du_, dt * v0 + tv * dv_); e8 = np.exp(0.5j); g_after, _ = quot(tv * u0, tv * e8 * v0, dt * u0 + tv * du_, e8 * (dt * v0 + tv * dv_ + tv * 1j * thp * dt * v0))
    print("G8: the change of the metric under v -> exp(i theta(t)) v on a random tangent: %.8f against t^2 theta' dt (a_u + a_v) + (t^2/2) theta'^2 dt^2 = %.8f" % (g_after - g_before, tv * tv * thp * dt * (au8 + av8) + tv * tv / 2 * thp * thp * dt * dt))
    # G9
    xs = np.linspace(0, 1, 4001); Nx = 1.5 + np.sin(5 * xs) ** 2; ax = 0.3 * np.cos(3 * xs); beta = 1.1; trap = lambda f: float(np.sum((f[1:] + f[:-1]) / 2) * (xs[1] - xs[0]))
    Rg = trap(1 / Nx); Delta = beta - trap(ax); bstar = ax + Delta / (Rg * Nx); extra = trap(Nx * (bstar - ax) ** 2); other = ax + Delta + 0.4 * np.sin(2 * np.pi * xs); extra2 = trap(Nx * (other - ax) ** 2)
    half = len(xs) // 2; tr2 = lambda f, a_, b_: float(np.sum((f[a_ + 1:b_ + 1] + f[a_:b_]) / 2) * (xs[1] - xs[0])); R1, R2 = tr2(1 / Nx, 0, half), tr2(1 / Nx, half, len(xs) - 1); I1, I2 = tr2(ax, 0, half), tr2(ax, half, len(xs) - 1)
    b1s = np.linspace(-2, 3, 50001); sew = min((b1 - I1) ** 2 / R1 + (beta - b1 - I2) ** 2 / R2 for b1 in b1s)
    print("G9: the extra energy at b* = %.8f against Delta^2/R = %.8f, with int b* = %.6f (beta = %.1f); another field with the same integral costs %.4f; two intervals: the least sum %.8f against (beta - I1 - I2)^2/(R1 + R2) = %.8f" % (extra, Delta ** 2 / Rg, trap(bstar), beta, extra2, sew, (beta - I1 - I2) ** 2 / (R1 + R2)))
