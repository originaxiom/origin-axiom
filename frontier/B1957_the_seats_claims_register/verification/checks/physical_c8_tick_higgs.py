"""B1957: the physical lane's package on the tick and the Higgs (its card PHYSICAL-C8; six notes at aa9facef6), the
statements main can decide by its own computation.  Data-free.  Nothing of the lane's is run (it says it ran nothing: hand
derivations).  The matrices are main's own six-mode T6, S6, U; the overlap is main's closed form (cim_closed.py).
 K1  the six modes as 2 x 3: T6 = diag(1, -i) (x) diag(1, w, w), F6 = F2 (x) conj(F3) under k = 3a + 4b; U = A2 (x) A3; the
     characteristic polynomial, the order, the parity's odd plane.
 K2  S6^2 = -i P; T6 S6 K and P T6 S6 K both square to U, agree on the ground pair, differ on the odd plane; the three
     half-period lifts on the ground pair: overlap 1/3, leak 2/3, no exchange; Z^3 X^3 = -X^3 Z^3.
 K3  on the ground plane E: the Hermitian forms kept by the tick; the pairs (H+, H-) carried into each other by it; J.
 K4  the real polynomials on E invariant under the common phase, U and the tick, by degree: the quartic ones; the first
     that see the relative phase.
 K5  the lane's coherent vector h*: in E, with overlaps 1/sqrt(2) on v+ and v-; the support of v+ and v-.
 K6  THE DECIDING ONE: the cusp exponents of the contracted matrices at the mark for v+, v-, h* and a random vector of E;
     the lepton matrix as the transpose of the down matrix.
 K7  the scalar average of the bubble over the four lifts, from the closed form.
 K9  the lane's finding C8-03 on main's own mode functions (cim_overlap.psi, flux 6, spin (0, 0)): which reflection of z
     gives plain conjugation of the coefficients and which gives conjugation with the parity; the frame's factor under S.
 K8  smaller steps: the 2-torsion under the act; halves in the 5-torsion; the Gaussian moments behind the connection and
     the geometric term; the phase along the golden axis; the relaxed quartic's infimum as a projection."""
import sys, pathlib, itertools, functools
import numpy as np, sympy as sp, mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); import cim_closed as CC
print = functools.partial(print, flush=True); nrm = lambda A: float(np.abs(np.asarray(A)).max()); inv = np.linalg.inv
k = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k ** 2 / 6)); F = lambda N: np.exp(-2j * np.pi * np.outer(np.arange(N), np.arange(N)) / N) / np.sqrt(N)
S6 = np.exp(-1j * np.pi / 4) * F(6); U = T6 @ inv(S6) @ inv(T6) @ S6; w3 = np.exp(2j * np.pi / 3)
# ---- K1
perm = np.zeros((6, 6)); idx = {}
for a in range(2):
    for b in range(3): perm[(3 * a + 4 * b) % 6, 3 * a + b] = 1; idx[(a, b)] = (3 * a + 4 * b) % 6        # column (a, b) -> row k
to23 = lambda A: perm.T @ A @ perm
T2, T3 = np.diag([1, -1j]), np.diag([1, w3, w3]); A2 = T2 @ F(2) @ np.diag([1, 1j]) @ F(2); A3 = T3 @ F(3) @ inv(T3) @ inv(F(3))
A2_lane = np.array([[1 + 1j, 1 - 1j], [-1 - 1j, 1 - 1j]]) / 2
lam = sp.Symbol("lambda"); w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
A2s = sp.Matrix([[1 + sp.I, 1 - sp.I], [-1 - sp.I, 1 - sp.I]]) / 2; c = (1 - w ** 2) / 3
A3s = sp.diag(w ** 2, 1, 1) + c * sp.Matrix([1, w, w]) * sp.Matrix([[1, 1, 1]])
det = lambda Mx: sp.factor(sp.expand(sp.radsimp(sp.expand((lam * sp.eye(Mx.shape[0]) - Mx).det(method="berkowitz")))))
cp, cp3 = det(A2s), det(A3s)
r2_, r3_ = sp.roots(sp.Poly(sp.expand(cp), lam)), sp.roots(sp.Poly(sp.expand(cp3), lam))
cpU = sp.factor(sp.expand(sp.prod([sp.expand((lam - a * b)) for a in r2_ for b in r3_])))          # the eigenvalues of A2 (x) A3 are the products
cpU_num = np.round(np.poly(U), 9)
order = next(n for n in range(1, 49) if nrm(np.linalg.matrix_power(U, n) - np.eye(6)) < 1e-12)
P = np.zeros((6, 6)); P[(-k) % 6, k] = 1; ev, V = np.linalg.eig(U)
odd = [np.angle(ev[i]) / np.pi for i in range(6) if abs(np.vdot(V[:, i], P @ V[:, i]) + 1) < 1e-9]
print("K1: under k = 3a + 4b: |T6 - diag(1,-i) (x) diag(1,w,w)| = %.1e; |F6 - F2 (x) conj(F3)| = %.1e; |U - A2 (x) A3| = %.1e; |A2 - the lane's matrix| = %.1e; |A3 - the lane's form| = %.1e"
      % (nrm(to23(T6) - np.kron(T2, T3)), nrm(to23(F(6)) - np.kron(F(2), F(3).conj())), nrm(to23(U) - np.kron(A2, A3)), nrm(A2 - A2_lane), nrm(A3 - np.array(A3s.evalf(30).tolist(), dtype=complex))))
print("K1: exactly: det(lambda - A2) = %s; det(lambda - A3) = %s; the product over the pairs of roots = %s; numerically the characteristic polynomial of U has coefficients %s; the order of U is %d; the parity's odd plane carries the phases %s pi" % (cp, cp3, cpU, [complex(x).real if abs(complex(x).imag) < 1e-9 else complex(x) for x in cpU_num], order, sorted(round(float(x), 4) for x in odd)))
# ---- K2
ph = np.angle(ev) / np.pi; vp = V[:, int(np.argmin(abs(ph - 1 / 6)))]; vm = V[:, int(np.argmin(abs(ph + 1 / 6)))]; vp, vm = vp / np.linalg.norm(vp), vm / np.linalg.norm(vm)
A = T6 @ S6; B = P @ T6 @ S6; PE = np.outer(vp, vp.conj()) + np.outer(vm, vm.conj()); oddvec = [V[:, i] for i in range(6) if abs(np.vdot(V[:, i], P @ V[:, i]) + 1) < 1e-9]
Z3 = np.diag((-1.0) ** k); X3 = np.roll(np.eye(6), 3, axis=0)
print("K2: |S6^2 + i P| = %.1e; |(T S K)^2 - U| = %.1e, |(P T S K)^2 - U| = %.1e; the two agree on the ground pair (%.1e) and differ on the odd plane (%.2f)"
      % (nrm(S6 @ S6 + 1j * P), nrm(A @ A.conj() - U), nrm(B @ B.conj() - U), max(nrm(A @ v.conj() - B @ v.conj()) for v in (vp, vm)), max(nrm(A @ v.conj() - B @ v.conj()) for v in oddvec)))
print("K2: the lifts Z^3, X^3, Z^3 X^3 on v+: |<v+, g v+>|^2 = %s; |<v-, g v+>| = %s; norm^2 outside the ground plane = %s; |Z^3 X^3 + X^3 Z^3| = %.1e"
      % (["%.6f" % abs(np.vdot(vp, g @ vp)) ** 2 for g in (Z3, X3, Z3 @ X3)], ["%.0e" % abs(np.vdot(vm, g @ vp)) for g in (Z3, X3, Z3 @ X3)], ["%.6f" % np.linalg.norm((np.eye(6) - PE) @ g @ vp) ** 2 for g in (Z3, X3, Z3 @ X3)], nrm(Z3 @ X3 + X3 @ Z3)))
# ---- K3   coordinates on E in the basis (v+, v-): Sigma(z+ v+ + z- v-) = conj(z+) Sigma v+ + conj(z-) Sigma v-
c1 = np.vdot(vm, A @ vp.conj()); c2 = np.vdot(vp, A @ vm.conj())                      # Sigma v+ = c1 v-, Sigma v- = c2 v+
Sg = np.array([[0, c2], [c1, 0]])                                                       # acts as z -> Sg conj(z)
th = np.pi / 6; UE = np.diag([np.exp(1j * th), np.exp(-1j * th)]); J = (UE - UE.conj().T) / (2j * np.sin(th))
herm = [np.array([[1, 0], [0, 0]], complex), np.array([[0, 0], [0, 1]], complex), np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex)]
conjH = lambda H: Sg @ H.conj() @ inv(Sg)                                              # Sigma H Sigma^-1 for the antiunitary z -> Sg conj(z)
vec = lambda H: np.concatenate([H.real.flatten(), H.imag.flatten()])
M1 = np.array([vec(conjH(H) - H) for H in herm]).T; d1 = 4 - np.linalg.matrix_rank(M1, tol=1e-9)
M2 = np.zeros((16, 8))                                                                 # pairs (H+, H-): H- = Sigma H+ Sigma^-1 and H+ = Sigma H- Sigma^-1
for i, H in enumerate(herm):
    M2[:8, i] = vec(conjH(H)); M2[:8, 4 + i] = -vec(H); M2[8:, i] = -vec(H); M2[8:, 4 + i] = vec(conjH(H))
d2 = 8 - np.linalg.matrix_rank(M2, tol=1e-9)
print("K3: Sigma v+ = c1 v-, Sigma v- = c2 v+ with |c1| = %.6f, |c2| = %.6f and c2 conj(c1) = e^(i pi %.4f); Hermitian forms on E kept by the tick: a space of dimension %d (the multiples of the identity: %s); pairs (H+, H-) exchanged by it: dimension %d (alpha I + kappa eps J: %s); J = diag%s and Sigma J Sigma^-1 = -J: %s; the eigenvalues of U on E are e^(+-i pi/6), neither is 1, so the tick fixes no ray of E"
      % (abs(c1), abs(c2), np.angle(c2 * np.conj(c1)) / np.pi, d1, nrm(conjH(np.eye(2)) - np.eye(2)) < 1e-12, d2, nrm(conjH(J) + J) < 1e-12, np.round(np.diag(J).real, 6).tolist(), nrm(conjH(J) + J) < 1e-12))
# ---- K4
rng = np.random.default_rng(11)
def invariants(n, with_tick=True):
    mons = [(a, n - a, cc, n - cc) for a in range(n + 1) for cc in range(n + 1)]; half = [m for m in mons if (m[0], m[1]) >= (m[2], m[3])]    # one of each conjugate pair
    def feats(z):
        out = []
        for a, b, cc, d in half:
            m = z[0] ** a * z[1] ** b * np.conj(z[0]) ** cc * np.conj(z[1]) ** d; out.append(m.real)
            if (a, b) != (cc, d): out.append(m.imag)
        return np.array(out)                                                             # a basis of the real polynomials of bidegree (n, n)
    rows = []
    for _ in range(4 * len(mons)):
        z = rng.normal(size=2) + 1j * rng.normal(size=2); z /= np.linalg.norm(z)
        rows.append(feats(UE @ z) - feats(z))
        if with_tick: rows.append(feats(Sg @ z.conj()) - feats(z))
    sv = np.linalg.svd(np.array(rows), compute_uv=False); return int(len(feats(np.ones(2))) - np.sum(sv > 1e-9 * sv[0]))
dims = {2 * n: invariants(n) for n in (1, 2, 3, 4, 5, 6, 7)}; plain = {2 * n: n // 2 + 1 for n in (1, 2, 3, 4, 5, 6, 7)}
print("K4: real polynomials on E invariant under the common phase, U and the tick, by degree: %s; polynomials in N and Delta^2 alone: %s; so the quartic ones are A N^2 + B Delta^2 (dimension %d) and the first invariants that see the relative phase are at degree %d (%d more: Delta Re w^6 and Delta Im w^6)"
      % (dims, plain, dims[4], min(dg for dg in dims if dims[dg] > plain[dg]), dims[14] - plain[14]))
# on the circle Delta = 0: w -> e^(i pi/6) w under the tick, so the first non-constant harmonic of arg w is the twelfth
print("K4: under the tick w = z+ conj(z-) goes to e^(i pi %.4f) w and Delta to -Delta; under U, w goes to e^(i pi %.4f) w: on the circle Delta = 0 the first invariant harmonic is w^12 (degree 24), and Delta w^6 is invariant at degree 14" % (np.angle(c2 * np.conj(c1)) / np.pi, 2 * th / np.pi))
# ---- K5
hs = np.array([1 / np.sqrt(2), np.exp(1j * np.pi / 12) / 2, 0, 0, 0, np.exp(1j * np.pi / 12) / 2]); Hm = (U + U.conj().T) / 2
r0 = 1 / np.sqrt(3); tab = {"0": ((1 - r0) ** 2 / 4, (1 + r0) ** 2 / 4), "1,5": ((1 + r0) ** 2 / 8, (1 - r0) ** 2 / 8), "2,4": (1 / 12, 1 / 12), "3": (1 / 6, 1 / 6)}
sup = max(max(abs(abs(vp[int(i)]) ** 2 - tab[key][0]), abs(abs(vm[int(i)]) ** 2 - tab[key][1])) for key in tab for i in key.split(","))
print("K5: h* has norm %.12f; |(U + U^dagger)/2 h* - (sqrt 3/2) h*| = %.1e; |<v+, h*>|^2 = %.12f, |<v-, h*>|^2 = %.12f; the lane's table of |components|^2 of v+ and v-: worst difference %.1e; least |component| of v+ %.4f, of v- %.4f"
      % (np.linalg.norm(hs), nrm(Hm @ hs - np.sqrt(3) / 2 * hs), abs(np.vdot(vp, hs)) ** 2, abs(np.vdot(vm, hs)) ** 2, sup, np.abs(vp).min(), np.abs(vm).min()))
# ---- K6
mp.mp.dps = 80; DELTA = {"up": 5, "down": -1, "lepton": -9}
def Ymp(tau, xi):
    y = mp.im(tau); pre = (3 * y) ** mp.mpf("0.25"); res = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                kk = (i + j + 1 + 3 * m) % 6; a = mp.mpf((i - j + 3 * m) % 6) / 6; n0 = mp.nint(a + mp.im(xi) / y); s = mp.mpf(0)
                for n_ in range(-25, 26):
                    n = n_ + a - n0; s += mp.exp(6j * mp.pi * xi * mp.im(xi) / y + 6j * mp.pi * n ** 2 * tau + 12j * mp.pi * n * xi)
                res[(i, j, kk)] = pre * mp.exp(2j * mp.pi * kk / 6) * s
    return res
def Msec(tau, a, b, sec, h):
    xi = mp.mpf(DELTA[sec]) * (mp.mpf(a) * tau + mp.mpf(b)) / 2; Y = Ymp(tau, xi)
    return mp.matrix([[sum(Y.get((i, j, kk), 0) * h[kk] for kk in range(6)) for j in range(3)] for i in range(3)])
svals = lambda M: sorted((abs(x) for x in mp.svd_c(M, compute_uv=False)), reverse=True)
e12 = mp.exp(1j * mp.pi / 12); hstar = [1 / mp.sqrt(2), e12 / 2, mp.mpc(0), mp.mpc(0), mp.mpc(0), e12 / 2]
mpv = lambda v: [mp.mpc(complex(x)) for x in v]; rnd = (0.6 * np.exp(0.7j)) * vp + (0.8 * np.exp(-1.9j)) * vm
print("K6: exponents E = -(1/pi) d log(s_i/s_1)/d Im tau at the mark (2/5, 4/5), unshifted lift, from heights 8 -> 11 and 11 -> 14 (Re tau = 0.13):")
for name, h in (("v+", mpv(vp)), ("v-", mpv(vm)), ("h*", hstar), ("a random vector of E", mpv(rnd))):
    for sec in ("up", "down", "lepton"):
        L = {y: svals(Msec(mp.mpc("0.13", y), mp.mpf(2) / 5, mp.mpf(4) / 5, sec, h)) for y in (8, 11, 14)}
        E = lambda y0, y1, i: float(-(mp.log(L[y1][i] / L[y1][0]) - mp.log(L[y0][i] / L[y0][0])) / (mp.pi * (y1 - y0)))
        print("  %-21s %-6s: E2 %+.6f, %+.6f; E3 %+.6f, %+.6f" % (name, sec, E(8, 11, 1), E(11, 14, 1), E(8, 11, 2), E(11, 14, 2)))
print("K6: the lane's values for h*: up (0, 4/3) = (0, %.6f); down and lepton (1/5, 4/5)" % (4 / 3))
worst = 0
for trial in range(4):
    h = mpv(rng.normal(size=6) + 1j * rng.normal(size=6)); tau = mp.mpc("0.13", 3 + trial); a_, b_ = mp.mpf(1 + trial) / 5, mp.mpf(4 - trial) / 5
    Md, Ml = Msec(tau, a_, b_, "down", h), Msec(tau, a_, b_, "lepton", h); ratio = Ml[0, 1] / Md[1, 0]
    worst = max(worst, float(max(abs(Ml[i, j] - ratio * Md[j, i]) for i in range(3) for j in range(3)) / abs(Ml[0, 1])))
print("K6: for four random coefficient vectors (not only ground vectors) and four points of order 5: the lepton matrix is one phase times the transpose of the down matrix: worst relative difference %.1e" % worst)
# ---- K7
worst = 0; worst_raw = 0
for trial in range(10):
    tau = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 1.6)); xi = complex(rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3)); Y = CC.Y(tau, xi)
    Bm = np.einsum("ijk,ijl->kl", Y.conj(), Y); Tw = sum(g @ Bm @ g.conj().T for g in (np.eye(6), Z3, X3, Z3 @ X3)) / 4
    worst = max(worst, nrm(Tw - np.trace(Bm) / 6 * np.eye(6)) / abs(np.trace(Bm))); worst_raw = max(worst_raw, nrm(Bm - np.trace(Bm) / 6 * np.eye(6)) / abs(np.trace(Bm)))
print("K7: the bubble B = Y^dagger Y from main's closed form at 10 random (tau, xi): averaged over I, Z^3, X^3, Z^3 X^3 it is tr(B)/6 times the identity (worst relative difference %.1e); unaveraged it is not (%.2f)" % (worst, worst_raw))
# ---- K8
M2m = sp.Matrix([[2, 1], [1, 1]]) % 2; nz = [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([1, 1])]; orbit = [nz[0]]
for _ in range(2): orbit.append((M2m * orbit[-1]) % 2)
chars = [l for l in itertools.product((0, 1), repeat=2) if all(((sp.Matrix([list(l)]) * (M2m - sp.eye(2))) % 2)[0, i] == 0 for i in range(2))]
print("K8: the act on the 2-torsion is %s: it carries (1,0) -> %s -> %s (the three non-zero points in one cycle); characters to Z/2 invariant under it: %s (only zero, det(M - I) mod 2 = %d)" % (M2m.tolist(), list(orbit[1]), list(orbit[2]), chars, (M2m - sp.eye(2)).det() % 2))
print("K8: in the 5-torsion 2 * 3 = %d mod 5, so the half of w that stays of order 5 is 3w; with zeta_H = 3 q_s w, zeta_L' = q_L w + q_s lambda, zeta_R' = q_R w and 5w = lambda: 2 zeta_H - zeta_L' - zeta_R' = %s" % ((2 * 3) % 5, sp.simplify(2 * 3 * (sp.Symbol("qL") + sp.Symbol("qR")) * sp.Symbol("w") - (sp.Symbol("qL") * sp.Symbol("w") + (sp.Symbol("qL") + sp.Symbol("qR")) * 5 * sp.Symbol("w")) - sp.Symbol("qR") * sp.Symbol("w"))))
r, N, y = sp.symbols("r N y", positive=True); wgt = sp.exp(-2 * sp.pi * N * y * r ** 2); Z = sp.integrate(wgt, (r, -sp.oo, sp.oo)); mom = lambda f: sp.simplify(sp.integrate(f * wgt, (r, -sp.oo, sp.oo)) / Z)
r2, r4 = mom(r ** 2), mom(r ** 4)
print("K8: for the weight exp(-2 pi N y r^2): <r^2> = %s, <r^4> = %s, variance of r^2 = %s; so <psi, d_X psi> = i pi N <r^2> = i (%s); pi^2 N^2 var(r^2) = %s (the coefficient of |d tau|^2); (2 pi N)^2 <r^2> = %s (the coefficient of |d xi + tau d eta|^2)"
      % (r2, r4, sp.simplify(r4 - r2 ** 2), sp.simplify(sp.pi * N * r2), sp.simplify(sp.pi ** 2 * N ** 2 * (r4 - r2 ** 2)), sp.simplify((2 * sp.pi * N) ** 2 * r2)))
worst = 0
for phi0 in (0.4, 1.1, 1.9, 2.6):
    t0 = 0.5 + np.sqrt(5) / 2 * np.exp(1j * phi0); t1 = (2 * t0 + 1) / (t0 + 1); on = abs(abs(t1 - 0.5) - np.sqrt(5) / 2); phi1 = np.angle(t1 - 0.5)
    worst = max(worst, on, abs(np.exp(1j * (phi1 - phi0)) - np.exp(-2j * np.angle(t0 + 1))))
print("K8: on the axis tau = 1/2 + (sqrt 5/2) e^(i phi): M tau stays on it and phi changes by -2 arg(tau + 1) (worst %.1e at four points); with dX/y = -d phi the integral of i dX/(4y) is i arg(tau + 1)/2, the phase the lane's (9) carries" % worst)
worst = 0
for trial in range(5):
    Lm = rng.normal(size=(7, 4)) + 1j * rng.normal(size=(7, 4)); Lm[:, 3] = Lm[:, 0] + Lm[:, 1]; q = rng.normal(size=7) + 1j * rng.normal(size=7)
    beta = -np.linalg.pinv(Lm) @ q; u_, s_, _ = np.linalg.svd(Lm); ker = u_[:, np.sum(s_ > 1e-10):]
    worst = max(worst, abs(np.linalg.norm(Lm @ beta + q) ** 2 - np.linalg.norm(ker.conj().T @ q) ** 2))
print("K8: inf over beta of |L beta + Q|^2 equals |P_ker(L^dagger) Q|^2 (five random rank-deficient cases, worst %.1e)" % worst)
# ---- K9
import cim_overlap as CO
worst_a = worst_b = worst_c = 0
for trial in range(6):
    tau = complex(rng.uniform(-0.4, 0.4), rng.uniform(0.7, 1.5)); zeta = complex(rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3)); z = rng.uniform(-0.5, 0.5, size=5) + 1j * rng.uniform(-0.5, 0.5, size=5)
    base = CO.psi(6, 0.0, 0.0, z, tau, zeta); taur = -np.conj(tau)
    a_ = CO.psi(6, 0.0, 0.0, -np.conj(z), taur, -np.conj(zeta)); b_ = CO.psi(6, 0.0, 0.0, np.conj(z), taur, np.conj(zeta))
    worst_a = max(worst_a, nrm(a_ - base.conj())); worst_b = max(worst_b, nrm(b_ - base.conj()[(-k) % 6])); worst_c = max(worst_c, nrm(b_ - base.conj()))
print("K9: main's flux-6 modes at 6 random (tau, zeta), 5 points each: psi_j(-conj z; -conj tau; -conj zeta) = conj psi_j (worst %.1e): z -> -conj(z) gives plain conjugation K; psi_j(conj z; -conj tau; conj zeta) = conj psi_(-j) (worst %.1e), and is not conj psi_j (%.2f): z -> conj(z) gives P K"
      % (worst_a, worst_b, worst_c))
res = []
for tau in (0.3 + 1.1j, -0.2 + 0.9j, 0.45 + 1.4j):
    W = CO.transport(6, 0.0, 0.0, tau, 0.0, "S", n=64); best = None
    for name, cand in (("S6", S6), ("S6^-1", inv(S6))):
        i = np.unravel_index(np.argmax(np.abs(cand)), cand.shape); ph_ = W[i] / cand[i]
        if nrm(W - ph_ * cand) < 1e-8: best = (name, ph_)
    res.append((tau, best[0], best[1], np.sqrt(tau / abs(tau)))) if best else res.append((tau, None, None, None))
print("K9: main's transport matrix of the flux-6 modes under S (<mode at -1/tau | mode at tau>), three points: %s" % "; ".join("tau = %s: %s times %.6f%+.6fi, and sqrt(tau/|tau|) = %.6f%+.6fi (conjugate: %s)" % (t, nme, c_.real, c_.imag, r_.real, r_.imag, abs(c_ - np.conj(r_)) < 1e-8) if nme else "tau = %s: neither S6 nor its inverse up to a factor" % t for t, nme, c_, r_ in res))
