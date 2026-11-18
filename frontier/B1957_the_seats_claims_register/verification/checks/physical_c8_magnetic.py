"""B1957: the physical lane's compact magnetic control and its cross-form packet (its branch at 01dc0774f), the finite steps
recomputed on main (data-free; the lane's notes are hand derivations and it ran no code; none of its files is imported).
The notes: LOCAL_ACTION_FIELD_MAP_AND_RELAXED_HIGGS_RESPONSE.md, FULL_E8_MAGNETIC_ROSTER_CONTROL.md,
COMMUTING_STABILIZER_AND_FERMION_PRICE.md (tick_higgs_alignment_2026_11_18) and STATIONARY_BRANCH_AND_VECTOR_RESPONSE.md
(neutral_cross_form_2026_11_18).  What is computed here is algebra: the commutators, the curvature and the energy on the two
paths as polynomials, the root counts, the weights.  NOT computed: that the fields are the lane's fields (the typing of q, r and
the connection form, the bundles, the spin and Wilson data), the existence of the response (a Poisson equation with a source of
zero mean, standard), anything on the cusp, and every analytic step of the cross-form proof.
 G1  the A2 block's commutators and traces.            G2  the frozen path: curvature, potential (4), canonical form (5).
 G3  the response path: curvature (8), R_f, energy (9), quartic (10), the sextic's density (11).
 G4  the mass of a root of charge q: the trace identity, and the block's twelve negative directions.
 G5  all of E8 by the charge of C = e1 - e3: the roster, Tr C^2, the 174 directions.
 G6  the cocharacter T: its weights on the two 56s, the roots it and C both kill, the masses for 2 v^2 > B.
 G7  the Koszul Laplacian of a scalar differential.    G8  the cross-form proof's finite steps."""
import itertools, sympy as sp
E = lambda i, j: sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i - 1, j - 1) else 0); comm = lambda X, Y: X * Y - Y * X
Cm = sp.diag(1, 0, -1); E12, E23, E31, E13, E21, E32 = E(1, 2), E(2, 3), E(3, 1), E(1, 3), E(2, 1), E(3, 2)
print("G1: [C, E12] = E12: %s; [C, E23] = E23: %s; [C, E31] = -2 E31: %s; [E31, E23] = -E21: %s; tr(E12 E21) = %s; [E31, E13] = -C: %s; tr C^2 = %s"
      % (comm(Cm, E12) == E12, comm(Cm, E23) == E23, comm(Cm, E31) == -2 * E31, comm(E31, E23) == -E21, (E12 * E21).trace(), comm(E31, E13) == -Cm, (Cm * Cm).trace()))
# ---- G2: a = f E31; f and its conjugate as independent symbols; rho = |f|^2
f, fb, t, B, AT, I4, g, io, H = sp.symbols("f fb t B A_T I4 g iota H"); bx, by = sp.symbols("beta_X beta_Y", real=True); rho = sp.Symbol("rho")
aX = (f * E31 + fb * E13) / 2; aY = (f * E31 - fb * E13) / (2 * sp.I); a = f * E31; ad = fb * E13
quad = sp.simplify(-sp.I * comm(aX, aY)); print("G2: -i [a_X, a_Y] = [a, a^dagger]/2 = -|f|^2 C/2: %s" % (sp.simplify(quad - comm(a, ad) / 2) == sp.zeros(3, 3) and sp.simplify(quad + f * fb * Cm / 2) == sp.zeros(3, 3)))
p, q_, pb, qb = sp.symbols("DXf DYf DXfb DYfb")                      # the covariant derivatives of f and of its conjugate, as symbols
lin = (p * E31 - pb * E13) / (2 * sp.I) - (q_ * E31 + qb * E13) / 2          # D_X a_Y - D_Y a_X
print("G2: the linear curvature D_X a_Y - D_Y a_X is ((D_X - i D_Y) f E31 - (D_X + i D_Y) fbar E13)/(2i): %s (it vanishes on the harmonic profile, as the note says)" % (sp.simplify(lin - ((p - sp.I * q_) * E31 - (pb + sp.I * qb) * E13) / (2 * sp.I)) == sp.zeros(3, 3)))
integ = lambda poly: sum(c * {0: AT, 1: 1, 2: I4}[m[0]] for m, c in sp.Poly(sp.expand(poly), rho).terms())     # integral over the torus: 1 -> A_T, rho -> 1, rho^2 -> I4
Ffro = (B - t**2 * rho / 2); Vfro = integ(io * Ffro**2 * (Cm * Cm).trace() / 2) / g**2                          # V = (1/(2 g^2)) int kappa(F, F), kappa = iota tr
print("G2: the frozen potential is (iota/g^2)(A_T B^2 - B t^2 + I4 t^4/4): %s; with t = H sqrt(2 g^2/iota) it is V0 - 2B H^2 + (g^2/iota) I4 H^4: %s"
      % (sp.simplify(Vfro - io / g**2 * (AT * B**2 - B * t**2 + I4 * t**4 / 4)) == 0, sp.simplify(Vfro.subs(t, H * sp.sqrt(2 * g**2 / io)) - (io * AT * B**2 / g**2 - 2 * B * H**2 + g**2 / io * I4 * H**4)) == 0))
# ---- G3: the path A0 + t a + t^2 beta C
R = sp.simplify(-sp.I * (comm(bx * Cm, aY) + comm(aX, by * Cm))); Rnote = (bx - sp.I * by) * f * E31 + (bx + sp.I * by) * fb * E13
herm = sp.simplify(R.subs(fb, sp.conjugate(f)) - R.subs(fb, sp.conjugate(f)).H) == sp.zeros(3, 3)
print("G3: the order-t^3 curvature -i([b_X, a_Y] + [a_X, b_Y]) is (beta_X - i beta_Y) f E31 + (beta_X + i beta_Y) fbar E13: %s; Hermitian: %s; tr(C R) = %s; tr(R^2) = 2 |beta|^2 |f|^2: %s; no order t^4: [C, C] = 0"
      % (sp.simplify(R - Rnote) == sp.zeros(3, 3), herm, sp.simplify((Cm * R).trace()), sp.simplify((R * R).trace() - 2 * (bx**2 + by**2) * f * fb) == 0))
dbeta = (rho - 1 / AT) / 2; Fres = sp.expand(B - t**2 * rho / 2 + t**2 * dbeta); S6 = sp.Symbol("S6")                 # S6 = integral |beta|^2 |f|^2
Vres = io * AT * Fres**2 / g**2 + t**6 * (2 * io * S6) / (2 * g**2)
print("G3: with d beta = (|f|^2 - 1/A_T)/2 the C-coefficient is B - t^2/(2 A_T), free of the profile: %s; energy (9) in canonical H: V0 - 2B H^2 + (g^2/(iota A_T)) H^4 + (8 g^4/iota^2) S6 H^6: %s; the quartic equals (1/2)(2 e_C)^2 with e_C = g/sqrt(2 iota A_T): %s"
      % (sp.simplify(Fres - (B - t**2 / (2 * AT))) == 0, sp.simplify(Vres.subs(t, H * sp.sqrt(2 * g**2 / io)) - (io * AT * B**2 / g**2 - 2 * B * H**2 + g**2 / (io * AT) * H**4 + 8 * g**4 / io**2 * S6 * H**6)) == 0, sp.simplify(g**2 / (io * AT) - sp.Rational(1, 2) * (2 * g / sp.sqrt(2 * io * AT))**2) == 0))
print("G3: so the frozen quartic exceeds the quartic through the response by (g^2/iota)(I4 - 1/A_T) H^4, which is >= 0 by Cauchy-Schwarz (the integral of |f|^2 is 1) and depends on the direction; through the response the first direction-dependent term is the sextic")
# ---- G4
roots3 = {"E12": (E12, E21), "E23": (E23, E32), "E31": (E31, E13), "E21": (E21, E12), "E32": (E32, E23), "E13": (E13, E31)}
ch = {n: sp.simplify((comm(Cm, X) * Xd).trace() / (X * Xd).trace()) for n, (X, Xd) in roots3.items()}
idok = all(sp.simplify((Cm * comm(X, Xd)).trace() - ch[n] * (X * Xd).trace()) == 0 for n, (X, Xd) in roots3.items())
neg = {n: (int(c), -3 * int(c)) for n, c in ch.items() if c < 0}
print("G4: charges under C: %s; tr(C [E, E^dagger]) = q tr(E E^dagger) on all six: %s; so the mass squared of a root of charge q is q B (the frozen path's -B t^2 iota/g^2 over the norm iota t^2/(2 g^2) is -2B at q = -2); negative root lines of the block with their modes (-3q each): %s, in all %d"
      % ({n: int(c) for n, c in ch.items()}, idok, neg, sum(v[1] for v in neg.values())))
# ---- G5: E8
half = sp.Rational(1, 2); roots = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1): v = [0] * 8; v[i] = si; v[j] = sj; roots.append(tuple(sp.Integer(x) for x in v))
nint = len(roots)
for s in itertools.product((1, -1), repeat=8):
    if s.count(-1) % 2 == 0: roots.append(tuple(half * x for x in s))
Cv = (1, 0, -1, 0, 0, 0, 0, 0); Tv = (0, 1, 0, 1, 1, 1, 1, -1); dot = lambda u, v: sum(x * y for x, y in zip(u, v)); isint = lambda r: all(x.is_integer for x in r)
byq = {}
for r in roots: byq.setdefault(int(dot(Cv, r)), []).append(r)
print("G5: E8 has %d roots (%d of the first kind, %d half-integer); by the charge r_1 - r_3: %s; of the first kind: %s; half-integer: %s; with the eight Cartan coefficients at charge 0: %s, sum %d"
      % (len(roots), nint, len(roots) - nint, {k: len(v) for k, v in sorted(byq.items())}, {k: sum(isint(r) for r in v) for k, v in sorted(byq.items())}, {k: sum(not isint(r) for r in v) for k, v in sorted(byq.items())},
         {k: len(v) + (8 if k == 0 else 0) for k, v in sorted(byq.items())}, len(roots) + 8))
trC2 = sum(dot(Cv, r)**2 for r in roots)
print("G5: the adjoint trace of C^2 is %s, and tr_3 C^2 = 2, so iota = %s; negative directions at degree 3q: charge -1: %d roots x 3 = %d; charge -2: %d root x 6 = %d; in all %d complex, %d real"
      % (trC2, trC2 / 2, len(byq[-1]), 3 * len(byq[-1]), len(byq[-2]), 6 * len(byq[-2]), 3 * len(byq[-1]) + 6 * len(byq[-2]), 2 * (3 * len(byq[-1]) + 6 * len(byq[-2]))))
# ---- G6: T
cnt = lambda rs: {int(k): sum(1 for r in rs if dot(Tv, r) == k) for k in sorted({dot(Tv, r) for r in rs}, reverse=True)}
print("G6: T = %s: integer entries of even sum (%d), so in the E8 lattice; C.T = %d; its weights on the 56 roots of charge +1: %s (first kind: %s; half-integer: %s); on those of charge -1: %s; on the two roots of charge +-2: %s"
      % (Tv, sum(Tv), dot(Cv, Tv), cnt(byq[1]), cnt([r for r in byq[1] if isint(r)]), cnt([r for r in byq[1] if not isint(r)]), cnt(byq[-1]), [int(dot(Tv, r)) for r in byq[2] + byq[-2]]))
both = [r for r in byq[0] if dot(Tv, r) == 0]; M = sp.Matrix([list(r) for r in both]); seen = {both[0]}; todo = [both[0]]
while todo:
    x = todo.pop()
    for y in both:
        if y not in seen and dot(x, y) != 0: seen.add(y); todo.append(y)
print("G6: roots killed by both C and T: %d (%d of the first kind, %d half-integer); they span rank %d and are one connected system: %s (72 roots of rank 6: E6); with the eight Cartans the centraliser has dimension %d = 78 + 1 + 1"
      % (len(both), sum(isint(r) for r in both), sum(not isint(r) for r in both), M.rank(), len(seen) == len(both), len(both) + 8))
v = sp.Symbol("v", positive=True); m2 = lambda r: dot(Cv, r) * B + 2 * v**2 * dot(Tv, r)**2
low = {sp.simplify(m2(r)) for r in byq[-1]}; six = {sp.simplify(m2(r)) for r in byq[-2]}
print("G6: with m^2 = q_C B + 2 v^2 q_T^2: the masses on the 56 roots of charge -1 are %s, the least of them 2 v^2 - B, positive exactly when 2 v^2 > B; on the root of charge -2: %s, for every v; roots of charge +-1 with q_T = 0: %d (so every one of the flux-three blocks is shifted, bosons and, by the same weight, fermions)"
      % (sorted(low, key=str), six, sum(1 for r in byq[1] + byq[-1] if dot(Tv, r) == 0)))
# ---- G7: Koszul
def koszul(n, c):
    basis = [frozenset(s) for k in range(n + 1) for s in itertools.combinations(range(n), k)]; ix = {b: i for i, b in enumerate(basis)}; D = sp.zeros(len(basis), len(basis))
    for b in basis:
        if 0 not in b: D[ix[b | {0}], ix[b]] = c                         # c e_0 wedge; e_0 is first, so no sign
    return D
ok = all(sp.simplify(koszul(n, sp.Symbol("c")) * koszul(n, sp.conjugate(sp.Symbol("c"))).T + koszul(n, sp.conjugate(sp.Symbol("c"))).T * koszul(n, sp.Symbol("c")) - sp.Symbol("c") * sp.conjugate(sp.Symbol("c")) * sp.eye(2**n)) == sp.zeros(2**n, 2**n) for n in (1, 2, 3))
print("G7: for the differential c e wedge on the exterior algebra of 1, 2 or 3 directions, delta delta^dagger + delta^dagger delta = |c|^2 on every degree: %s (the note's (4) adds the parent's metrics and a factor 2, not computed here)" % ok)
# ---- G8: the cross-form proof's finite steps
e4 = lambda i, j: sp.Matrix(4, 4, lambda a, b: 1 if (a, b) == (i - 1, j - 1) else 0); pp, rr = sp.symbols("p r"); chain = pp * e4(1, 2) + rr * e4(2, 3) + pp * e4(3, 4); X = e4(1, 3) + e4(2, 4); Xm = e4(1, 3) - e4(2, 4)
ket = lambda i: sp.Matrix(4, 1, lambda a, b: 1 if a == i else 0); XX = sp.kronecker_product(X, X); kk = lambda i, j: sp.kronecker_product(ket(i), ket(j))      # index 0..3 is m = 3/2, 1/2, -1/2, -3/2
u1, u2, v1, v2 = kk(3, 2), kk(2, 3), kk(0, 1), kk(1, 0)
print("G8: [p e12 + r e23 + p e34, e13 + e24] = 0: %s; with e13 - e24 it is -2p e14: %s; (X x X) sends |-3/2, -1/2> to |1/2, 3/2> and |-1/2, -3/2> to |3/2, 1/2> with one coefficient: %s"
      % (comm(chain, X) == sp.zeros(4, 4), sp.simplify(comm(chain, Xm) + 2 * pp * e4(1, 4)) == sp.zeros(4, 4), XX * u1 == v2 and XX * u2 == v1))
al = sp.Symbol("alpha"); A2 = sp.I * al * sp.Matrix([[0, 1], [1, 0]]); D2 = sp.diag(sp.I, -sp.I)
common = [vec for vec in (sp.Matrix([1, 0]), sp.Matrix([0, 1])) if sp.Matrix.hstack(A2.subs(al, 1) * vec, vec).det() == 0]   # an eigenline of D that sigma_x keeps
u = sp.Symbol("u"); a0, a1, a2, c0, c1, c2 = sp.symbols("a0 a1 a2 c0 c1 c2"); F = a0 / u + a1 + a2 * u; Hh = c0 / u + c1 + c2 * u; W = sp.expand(u * (F * sp.diff(Hh, u) - Hh * sp.diff(F, u)))
lam = sp.Symbol("Lambda"); blk = sp.Matrix([[0, sp.conjugate(lam)], [lam, 0]])
print("G8: det of i alpha sigma_x at alpha = +-1: %s; det diag(i, -i) = %s; eigenlines of diag(i, -i) kept by sigma_x: %d (no common line); for f = u^(1/2) F, g = u^(1/2) H with poles of order at most one, W = u(F H' - H F') has lowest power u^%s (at most a simple pole; the cubic pole cancels); the block ((0, conj Lambda), (Lambda, 0)) has eigenvalues squared %s"
      % ({sp.simplify(A2.subs(al, s).det()) for s in (1, -1)}, D2.det(), len(common), min(sp.Poly(sp.expand(W * u**3), u).monoms())[0] - 3, {sp.simplify(x**2) for x in blk.eigenvals()}))
# ---- G9: further small steps of the same notes, and of the lane's reply to M12 (its M12_RECORD_REVIEW.md)
qL, qR = sp.symbols("q_L q_R"); Dw = sp.diag(2 * qL + qR, -qL + qR, -qL - 2 * qR)
print("G9: a line of curvature B on area A_T has degree B A_T/(2 pi) = %s at B = 6 pi/A_T, so the root degrees are 3q = %s for E12, E23, E31; the Wilson Cartan diag(2q_L + q_R, -q_L + q_R, -q_L - 2q_R) is traceless: %s, with adjacent root weights %s, %s and closing weight %s"
      % (sp.simplify(6 * sp.pi / AT * AT / (2 * sp.pi)), [3 * int(ch[n]) for n in ("E12", "E23", "E31")], Dw.trace() == 0, Dw[0, 0] - Dw[1, 1], Dw[1, 1] - Dw[2, 2], sp.expand(Dw[2, 2] - Dw[0, 0])))
print("G9: the tangent's norm: tr(a_X^2) + tr(a_Y^2) = |f|^2: %s (so its kinetic norm is iota/(2 g^2) for a unit profile); the gauge divergence D_X a_X + D_Y a_Y is ((D_X - i D_Y) f E31 + (D_X + i D_Y) fbar E13)/2: %s; the cubic's canonical factor (iota/g^2) A_T^(-1/2) / (sqrt(iota/g^2)^2 sqrt(iota/(2 g^2))) = sqrt(2) g/sqrt(iota A_T): %s"
      % (sp.simplify((aX * aX).trace() + (aY * aY).trace() - f * fb) == 0, sp.simplify((p * E31 + pb * E13) / 2 + (q_ * E31 - qb * E13) / (2 * sp.I) - ((p - sp.I * q_) * E31 + (pb + sp.I * qb) * E13) / 2) == sp.zeros(3, 3),
         (lambda gp, ip, Ap: sp.simplify((ip / gp**2) / sp.sqrt(Ap) / ((ip / gp**2) * sp.sqrt(ip / (2 * gp**2))) - sp.sqrt(2) * gp / sp.sqrt(ip * Ap)) == 0)(*sp.symbols('g iota A_T', positive=True))))   # positive symbols: g, iota and the area
ratio = {n: sp.simplify(sp.Poly(sp.expand(io * ((B * Cm + t**2 * rho * comm(X, Xd) / 2)**2).trace() / 2), t).coeff_monomial(t**2) / (io * rho * (X * Xd).trace() / 2)) for n, (X, Xd) in roots3.items()}
print("G9: for each root of the block, the t^2 term of (1/2) kappa(F, F) with F = B C + t^2 |f|^2 [E, E^dagger]/2, over the tangent's norm: %s (the mass squared is q B on each)" % {n: str(v) for n, v in ratio.items()})
plus = [r for r in byq[1] if isint(r)]; zero = byq[0]; Mz = sp.Matrix([list(r) for r in zero]); seenz = {zero[0]}; todo = [zero[0]]
while todo:
    x = todo.pop()
    for y in zero:
        if y not in seenz and dot(x, y) != 0: seenz.add(y); todo.append(y)
print("G9: roots of the first kind at charge +1: with r_1 = 1: %d; with r_3 = -1: %d; the %d roots of charge 0 span rank %d and are one connected system: %s (126 roots of rank 7: E7; with the Cartans 134 = 133 + 1)"
      % (sum(1 for r in plus if r[0] == 1), sum(1 for r in plus if r[2] == -1), len(zero), Mz.rank(), len(seenz) == len(zero)))
s_, Hs, Es = sp.symbols("s H E", commutative=False); sc = sp.Symbol("s_c")                                         # [H, E] = 2E: i s E - i [s H/2, E] = i s E - i s (2E)/2
print("G9: with the spin connection s = omega/2 and A_spin = s H/2, i s E - i [A_spin, E] = i s E - i (s/2)(2E) = %s when [H, E] = 2E (the factor of two the lane says must be carried)" % sp.simplify(sp.I * sc - sp.I * (sc / 2) * 2))
import numpy as np
k6 = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k6**2 / 6)); S6 = np.exp(-1j * np.pi / 4) * np.exp(-2j * np.pi * np.outer(k6, k6) / 6) / np.sqrt(6); P6 = np.zeros((6, 6)); P6[k6, (-k6) % 6] = 1
U6 = T6 @ np.linalg.inv(S6) @ np.linalg.inv(T6) @ S6; near = lambda X_, Y_: float(np.abs(X_ - Y_).max())
print("G9: on the six modes: |S^2 + i P| = %.0e; |[P, T]| = %.0e; |S U S^-1 - U^-1| = %.0e (U = T S^-1 T^-1 S); det of the modular S on the base, ((0, -1), (1, 0)): %d"
      % (near(S6 @ S6, -1j * P6), near(P6 @ T6, T6 @ P6), near(S6 @ U6 @ np.linalg.inv(S6), np.linalg.inv(U6)), round(np.linalg.det(np.array([[0, -1], [1, 0]])))))
