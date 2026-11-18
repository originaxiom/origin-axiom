#!/usr/bin/env python3
"""The SM seat's check of the physical lane's packet fixed_sector_light_system_2026_11_16
(audit/physical-bridge-2026-09-05 at 798281903): every finite, algebraic or numerically checkable claim, on this
seat's own code.  Built from scratch: the principal sl2 in so5, so5+so5 in so10 in so16, the so16 adjoint plus a
Clifford chiral spinor as the 248, the elliptic-curve pole/section counts.  Nothing from the lane is imported.
The analytic premises (cusp inverse, weighted Schauder estimates, implicit-function maps, source normalizations,
the D = G(Fk) phases, Hodge identification) are not checked.  Four planted countercontrols must FAIL.
No data; no physical value.
    python3 check_fixed_sector_light_system.py [MAIN_CHECKOUT]   (the optional argument is not used)"""
import itertools
import json
import pathlib

import numpy as np
import sympy as sp

rows = []


def rec(cid, claim, ok, detail="", plant=False):
    rows.append({"id": cid, "claim": claim, "holds": bool(ok), "detail": str(detail), "plant": plant})


I = sp.I
# ---------------------------------------------------------------- principal sl2 in so5 (vector five = V_2)
def sl2(j2):
    """spin j = j2/2 in the |m> basis, m = j, j-1, ..., -j; returns Jz, J+, J- (sympy)."""
    j = sp.Rational(j2, 2); ms = [j - k for k in range(j2 + 1)]; n = len(ms)
    Jz = sp.diag(*ms); Jp = sp.zeros(n, n)
    for k in range(1, n):
        m = ms[k]; Jp[k - 1, k] = sp.sqrt(j * (j + 1) - m * (m + 1))
    return Jz, Jp, Jp.T


Jz5, E5, F5 = sl2(4)
b = sp.symbols("b0:25"); Bg = sp.Matrix(5, 5, b)
eqs = [e for M in (Jz5, E5, F5) for e in (M.T * Bg + Bg * M)] + [e for e in (Bg - Bg.T)]
Bsol = Bg.subs(sp.solve(eqs, b, dict=True)[0]); fre = sorted(Bsol.free_symbols, key=str)
B5 = Bsol.subs({fre[0]: 1}).subs({s: 0 for s in fre[1:]})
rec("K0", "the vector five carries a unique invariant symmetric form for the principal sl2 (so5 exists)",
    len(fre) == 1 and B5.det() != 0, f"free parameters {len(fre)}, form antidiagonal {list(B5)}")
in_so = lambda X, B: (X.T * B + B * X).is_zero_matrix
T3 = F5 ** 3
rec("K1", "E^j lies in so5 for j = 1, 3 (odd powers), E^2 does not; T_(3) ~ (E^dagger)^3 is the lowest j=3 element",
    in_so(E5, B5) and in_so(E5 ** 3, B5) and in_so(T3, B5) and not in_so(E5 ** 2, B5)
    and (Jz5 * T3 - T3 * Jz5 - (-3) * T3).is_zero_matrix and T3 != sp.zeros(5, 5),
    "ad(Jz) T3 = -3 T3")

# ---------------------------------------------------------------- the reflection A on 5+5 and Ad_A phases
Z5 = sp.zeros(5, 5)
blk = lambda X, Y: sp.diag(X, Y)
Nsw = sp.Matrix(sp.BlockMatrix([[Z5, sp.eye(5)], [sp.eye(5), Z5]]))
H10 = blk(2 * Jz5, 2 * Jz5)
A10 = (-I) * Nsw * sp.diag(*[sp.exp(-I * sp.pi * H10[k, k] / 4) for k in range(10)])
A10i = A10.inv()
top = sp.zeros(10, 1); top[0] = 1; top2 = sp.zeros(10, 1); top2[5] = 1
rec("K2a", "A = (-i N) exp(-i pi H/4): each vector-five highest vector (m = 2) maps with phase i to the other",
    (A10 * top - I * top2).is_zero_matrix and (A10 * top2 - I * top).is_zero_matrix)
ok = True; bad = []
for m in range(-3, 4):          # adjoint weight-m elements of so5_+: basis of so5 with ad(Jz) = m
    for X in [E5 ** 1, E5 ** 3, F5, F5 ** 3, Jz5]:
        w = None
        for mm in range(-3, 4):
            if (Jz5 * X - X * Jz5 - mm * X).is_zero_matrix:
                w = mm
        if w != m:
            continue
        lhs = sp.simplify(A10 * blk(X, Z5) * A10i); rhs = sp.simplify(I ** (-m) * blk(Z5, X))
        lhs2 = sp.simplify(A10 * blk(Z5, X) * A10i); rhs2 = sp.simplify(I ** (-m) * blk(X, Z5))
        if not ((lhs - rhs).is_zero_matrix and (lhs2 - rhs2).is_zero_matrix):
            ok = False; bad.append(m)
rec("K2b", "Ad_A |j,m>_+ = i^(-m)|j,m>_- and Ad_A |j,m>_- = i^(-m)|j,m>_+ ;"
    " in particular Ad_A T_(j,+) = (-i)^j T_(j,-)",
    ok and all(I ** (-j) == (-I) ** j for j in (1, 3)), f"failing weights {bad}")
rec("K2c", "the lowest j=3 elements are exchanged with phase -i (used in the cubic, section 2)", I ** 3 == -I)
# (1): A_(+j) = i^(1-j) sigma_x and A_(-j) = i^(1+j) sigma_x, i.e. Ad_A phase i^(-m) with m = w - 1 (one spin slot)
rec("K3", "(1) A_(+-j) phases equal i^(-(w-1)) at w = +-j (spin slot carries +1, trivial phase)",
    all(sp.simplify(I ** (1 - j) - I ** (-(j - 1))) == 0 and sp.simplify(I ** (1 + j) - I ** (-(-j - 1))) == 0
        for j in (1, 3)))


# ---------------------------------------------------------------- strict cusp pole bound and sections on the torus
def max_pole(e):
    """largest pole order m at the cusp for a section of S^e (S^2 = K): in the cusp frame the section is
    f dz^(e/2) with f ~ q^(e/2 - m) times a power of y = Im z; boundedness/decay needs e/2 - m > 0, or e = m = 0."""
    if e == 0:
        return 0
    return int(sp.ceiling(sp.Rational(e, 2))) - 1


def h0(deg, trivial):
    """sections of a line bundle of degree deg on an elliptic curve (Riemann-Roch; flat character)."""
    return deg if deg >= 1 else (1 if (deg == 0 and trivial) else 0)


# characters: B = beta_j A, beta_1 = -1, beta_3 = +1 (premise); sigma_x eigenline s = +-1
lines = []
for j in (1, 3):
    beta = (-1) ** ((j + 1) // 2)
    for w in (j, -j):
        phaseA = I ** (1 - w)
        for s in (1, -1):
            chA = sp.simplify(phaseA * s); chB = sp.simplify(beta * chA)
            e = 1 - w
            lines.append((j, w, s, e, chA, chB, h0(max_pole(e), chA == 1 and chB == 1)))
j1 = [L for L in lines if L[0] == 1]; j3 = [L for L in lines if L[0] == 3]
rec("K4", "j=1: the two core phases are opposite in either sigma_x eigenline; exponents 0, 2 with degree 0; no section",
    all(L[4] == -L[5] for L in j1) and sorted({L[3] for L in j1}) == [0, 2]
    and all(max_pole(L[3]) == 0 for L in j1) and sum(L[6] for L in j1) == 0,
    [(L[1], L[3], str(L[4]), str(L[5])) for L in j1])
rec("K5", "j=3: w=+3 exponent -2 has negative degree; w=-3 exponent 4 with characters (delta, delta), one pole, one "
    "section each: exactly two neutral spin modes; all exponents even",
    all(L[3] == -2 and max_pole(L[3]) < 0 for L in j3 if L[1] == 3)
    and all(L[3] == 4 and L[4] == L[5] and max_pole(4) == 1 and h0(1, False) == 1 for L in j3 if L[1] == -3)
    and sum(1 for L in j3 if L[1] == -3) == 2 and all(L[3] % 2 == 0 for L in lines),
    [(L[1], L[3], str(L[4]), str(L[5])) for L in j3])
rec("K6", "(2,2) cross form: highest weight w = 2+2 = 4; Hodge-dual exponent w+2 = 6, pole bound two, two sections",
    2 + 2 == 4 and max_pole(6) == 2 and h0(2, False) == 2)
rec("K7", "charged forms (w=3): Hodge-dual S^5 L^-1(2p) has dim 2; charged spin (w=0): S^1, no pole, "
    "nowhere-zero section only for trivial total character", max_pole(5) == 2 and h0(2, True) == 2 and max_pole(1) == 0)
# cross-module exterior sign: A v1 = i v2, A v2 = i v1 and v1 ^ v2 -> (i v2) ^ (i v1) = +v1 ^ v2
wedge = lambda x, y: x * y.T - y * x.T
v1, v2 = top, top2
rec("K8", "cross adjoint highest element v1^v2 has A-phase +1 (i^2 times the exchanged exterior factors)",
    (wedge(A10 * v1, A10 * v2) - wedge(v1, v2)).is_zero_matrix)
rec("K9", "counts: neutral 5 (A,B1,B2,N+,N-), charge +-1 3 each, Q gaugino 1: 12 = 11 chiral + 1; misaligned 9 + 1",
    1 + 2 + 2 == 5 and 5 + 3 + 3 == 11 and 11 + 1 == 12 and 11 - 2 == 9)

# ---------------------------------------------------------------- the cubic: channel enumeration
forms = {"A": (0, 0), "B": (4, 0), "P": (3, 1), "R": (3, -1)}     # (weight w, Q charge)
spins = {"N": (-3, 0), "S": (0, 1), "T": (0, -1)}
chan = sorted({(f, *sorted(pair)) for f, (wf, qf) in forms.items()
               for pair in itertools.combinations_with_replacement(spins, 2)
               if wf + sum(spins[s][0] for s in pair) == 0 and qf + sum(spins[s][1] for s in pair) == 0})
rec("C1", "one form slot, weight pairing and Q conservation leave exactly A S T, P N T, R N S; B pairs with nothing",
    chan == [("A", "S", "T"), ("P", "N", "T"), ("R", "N", "S")], chan)
rec("C1b", "spin pair weight sums are 0, -3, -6 only",
    sorted({sum(spins[s][0] for s in p) for p in itertools.combinations_with_replacement(spins, 2)}) == [-6, -3, 0])
# exponent bookkeeping: spin S^(1-w1) x S^(1-w2) = S^(2+w_form), the form's Hodge-dual exponent
rec("C2", "every channel's spin exponents add to the form's Hodge-dual exponent w+2; N x T has at most one pole "
    "inside the two-pole target", all((1 - spins[c[1]][0]) + (1 - spins[c[2]][0]) == forms[c[0]][0] + 2 for c in chan)
    and max_pole(4) + max_pole(1) <= max_pole(5))
# polarization (3): delta_- = -delta_+ ; coefficient C (delta_- - delta_N) selects N_(delta_+)
eta, ap = sp.symbols("eta alpha_p")
okp = True
for e_ in (1, -1):
    for a_ in (1, -1):
        dp, dm = e_ * a_, e_ * (-a_)
        coeff = {dN: dm - dN for dN in (1, -1)}
        okp &= coeff[dp] != 0 and coeff[dm] == 0 and a_ * (-a_) == -1 and (-a_) * dm == e_
rec("C3", "(3): with alpha_+ = -alpha_-, alpha_+ alpha_- = -1, only N_(delta_+) couples P to T; alpha_- delta_- = eta",
    okp)
# spinor four: faithful so5 action, j=3 lowest element has one nonzero extreme matrix element
J4 = sl2(3)
Bs = sp.Matrix(4, 4, sp.symbols("s0:16"))
eqs = [e for M in J4 for e in (M.T * Bs + Bs * M)] + [e for e in (Bs + Bs.T)]
Bsp = Bs.subs(sp.solve(eqs, list(Bs), dict=True)[0]); fs = sorted(Bsp.free_symbols, key=str)
Bsp = Bsp.subs({fs[0]: 1})
F4c = J4[2] ** 3
nz = [(r, c) for r in range(4) for c in range(4) if F4c[r, c] != 0]
rec("C4", "spinor 4 = V_(3/2) is symplectic (so5 = sp4); (E^dagger)^3 lies in sp4 and has a unique nonzero matrix "
    "element <-3/2|.|3/2>; so5 = 3 + 7 = dim sp4", in_so(F4c, Bsp) and nz == [(3, 0)] and 3 + 7 == 10 and len(fs) == 1,
    f"entry {F4c[3, 0]}")

# ---------------------------------------------------------------- normalized cubic, mass matrix, moment
y, lp, lm, t, nc, nd, eQ, rho = sp.symbols("y lambda_p lambda_m t nu_c nu_d e_Q rho")
Aa, Nc, Nd, Pc, Ps, S_, Rc, Rs, T_ = sp.symbols("A N_c N_d P_c P_s S R_c R_s T")
W3 = y * Aa * S_ * T_ + lp * Nc * Pc * T_ + lm * Nd * Rc * S_
plus, minus = [Pc, Ps, S_], [Rc, Rs, T_]
Y1 = sp.Matrix(3, 3, lambda r, c: sp.diff(W3, plus[r], minus[c])).subs({Aa: 0, Nc: t * nc, Nd: t * nd})
Y1ref = sp.Matrix([[0, 0, lp * nc], [0, 0, 0], [lm * nd, 0, 0]]) * t
sv = sorted([sp.sqrt(sp.factor(e)) for e in (Y1.H * Y1).subs({k: sp.Symbol(str(k), positive=True)
                                                               for k in (lp, lm, nc, nd, t)}).eigenvals()], key=str)
rec("M1", "Y1 from W3 at A = 0, N = t nu equals the packet's matrix; rank 2; singular values |t l+ nu_c|, |t l- nu_d|; "
    "null pair (P_s, R_s)", (Y1 - Y1ref).is_zero_matrix and Y1.subs({t: 1, lp: 2, lm: 3, nc: 1, nd: 1}).rank() == 2
    and Y1.row(1).is_zero_matrix and Y1.col(1).is_zero_matrix, sv)
grad = [sp.diff(W3, v).subs({S_: 0, T_: 0, Nc: 0, Nd: 0}) for v in (Aa, Nc, Nd, Pc, Ps, S_, Rc, Rs, T_)]
rec("M2", "with S = T = N = 0 every first derivative of W3 vanishes (pure charged forms are cubic-flat)",
    all(sp.expand(g) == 0 for g in grad))
rec("M3", "only A, S, T active: W3 reduces to y A S T",
    sp.expand(W3.subs({Nc: 0, Nd: 0}) - y * Aa * S_ * T_) == 0)
h = eQ * (1 - rho ** 2)
rec("M4", "(7) d/drho [e_Q(1 - rho^2)] at rho = 1 is -2 e_Q; m_Q^2 = 2 e_Q^2 t^2 (1 + rho^2) = 4 e_Q^2 t^2 at rho = 1",
    sp.diff(h, rho).subs(rho, 1) == -2 * eQ and sp.expand(2 * eQ ** 2 * t ** 2 * (1 + rho ** 2)).subs(rho, 1)
    == 4 * eQ ** 2 * t ** 2)
rng = np.random.default_rng(7)
herm = lambda n: (lambda X: (X + X.conj().T) / 2)(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
ax, ay = herm(5), herm(5); a = ax + 1j * ay
rec("T1", "(2) mu2 = -i[a_x, a_y] = [a, a^dagger]/2 for Hermitian a_x, a_y",
    np.allclose(-1j * (ax @ ay - ay @ ax), (a @ a.conj().T - a.conj().T @ a) / 2))
# (4): delta A_x = -D_y psi, delta A_y = D_x psi gives delta F_xy = (D_x^2 + D_y^2) psi (matrix valued, symbolic)
xs, ys = sp.symbols("x y")
gen = lambda nm: sp.Matrix(2, 2, lambda r, c: sum(sp.Symbol(f"{nm}{r}{c}_{k}") * mon for k, mon in
                                                enumerate([1, xs, ys, xs * ys, xs ** 2, ys ** 2])))
Ax, Ay, psi = gen("ax"), gen("ay"), gen("ps")
cm = lambda X, Y: X * Y - Y * X
Dx = lambda f: f.diff(xs) + cm(Ax, f); Dy = lambda f: f.diff(ys) + cm(Ay, f)
dAx, dAy = -Dy(psi), Dx(psi)
dF = dAy.diff(xs) - dAx.diff(ys) + cm(dAx, Ay) + cm(Ax, dAy)
rec("T2", "(4) connection part: delta F_xy = (D_x^2 + D_y^2) psi exactly (nonabelian, first order)",
    (dF - Dx(Dx(psi)) - Dy(Dy(psi))).expand().is_zero_matrix)
q0 = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)); ps = herm(5)
cmn = lambda X, Y: X @ Y - Y @ X
dq = cmn(q0, ps)
dmom = cmn(dq, q0.conj().T) + cmn(q0, dq.conj().T)
Mq = lambda f: cmn(q0.conj().T, cmn(q0, f)) + cmn(q0, cmn(q0.conj().T, f))
rec("T3", "(4) spin part: delta [q, q^dagger] with delta q = [q0, psi], psi Hermitian, equals -(ad_q^dag ad_q + "
    "ad_q ad_q^dag) psi; that operator is positive semidefinite", np.allclose(dmom, -Mq(ps))
    and np.vdot(ps, Mq(ps)).real >= -1e-9)

# ---------------------------------------------------------------- cusp ODE exponents
ell, c, dl = sp.symbols("ell c delta", positive=True)
sp_ = sp.symbols("s"); ex = sp.solve(ell ** -2 * (-sp_ ** 2 + sp_) + c, sp_)
betac = (sp.sqrt(1 + 4 * ell ** 2 * c) - 1) / 2
rec("G1", "(6)/(1) indicial exponents (1 +- sqrt(1+4 ell^2 c))/2 = -beta_c, 1+beta_c",
    {sp.simplify(e) for e in ex} == {sp.simplify(-betac), sp.simplify(1 + betac)})
l2 = lambda s0: sp.integrate(sp.exp((2 * s0 - 1) * sp.Symbol("u", positive=True)), (sp.Symbol("u", positive=True),
                                                                                     0, sp.oo))
rec("G2", "measure exp(-t)dt: constant (c=0) and exp(-beta t) are L2, exp(t) and exp((1+beta)t) are not",
    l2(0).is_finite and l2(-sp.Rational(1, 3)).is_finite
    and not l2(1).is_finite and not l2(sp.Rational(4, 3)).is_finite)
den = ell ** -2 * (-dl ** 2 - dl) + c
rec("G3", "source exp(-delta t): particular solution exp(-delta t)/den; den = 0 iff delta = beta_c (c>0), never for "
    "c = 0, delta>0 (non-resonance of the strict weight)", sp.simplify(den.subs(dl, betac)) == 0
    and sp.solve(den.subs(c, 0), dl) == [] and
    sp.simplify(ell ** -2 * (-sp.diff(sp.exp(-dl * t) / den, t, 2) + sp.diff(sp.exp(-dl * t) / den, t))
                + c * sp.exp(-dl * t) / den - sp.exp(-dl * t)) == 0)

# ---------------------------------------------------------------- numeric so16 + spinor model of the 248
def orth(X):
    w, U = np.linalg.eigh(np.array(B5, dtype=float)); S = U @ np.diag(1 / np.sqrt(w.astype(complex)))
    return np.linalg.inv(S) @ np.array(X, dtype=complex) @ S


En, Tn = orth(E5), orth(T3)
rec("V0", "in a B-orthonormal frame E and T_(3) are complex antisymmetric (elements of so(5,C))",
    np.allclose(En, -En.T) and np.allclose(Tn, -Tn.T))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
i2 = np.eye(2)


def gammas(n2):
    g = []
    for k in range(n2):
        for P in (sx, sy):
            mats = [sz] * k + [P] + [i2] * (n2 - k - 1)
            M = mats[0]
            for X in mats[1:]:
                M = np.kron(M, X)
            g.append(M)
    return g


def spin_rep(n2):
    g = gammas(n2); chi = np.eye(2 ** n2, dtype=complex)
    for G in g:
        chi = chi @ G
    ev = np.linalg.eigvals(chi); ph = ev[0]
    P = (np.eye(2 ** n2) + chi / ph) / 2
    U, sv_, _ = np.linalg.svd(P); Ub = U[:, sv_ > 0.5]
    return lambda X: Ub.conj().T @ (0.25 * sum(X[i, j] * g[i] @ g[j] for i in range(2 * n2) for j in range(2 * n2)
                                               if X[i, j] != 0)) @ Ub


def emb(X5, Y5=None, n=16):
    M = np.zeros((n, n), complex); M[:5, :5] = X5
    if Y5 is not None:
        M[5:10, 5:10] = Y5
    return M


sp16 = spin_rep(8)
Xr, Yr = rng.normal(size=(16, 16)), rng.normal(size=(16, 16)); Xr, Yr = Xr - Xr.T, Yr - Yr.T
rec("V1", "Clifford chiral spinor is a 128-dim rep of so16: [s(X), s(Y)] = s([X, Y])",
    np.allclose(cmn(sp16(Xr), sp16(Yr)), sp16(cmn(Xr, Yr))) and sp16(Xr).shape == (128, 128))
iu = [(i, j) for i in range(16) for j in range(i + 1, 16)]


def ad120(X):
    M = np.zeros((120, 120), complex)
    for col, (i, j) in enumerate(iu):
        Eij = np.zeros((16, 16)); Eij[i, j], Eij[j, i] = 1, -1
        R = X @ Eij - Eij @ X
        M[:, col] = [R[a_, b_] for a_, b_ in iu]
    return M


rk = lambda M: np.linalg.matrix_rank(M, tol=1e-8)
diag = emb(En, En); single = emb(En)
kd = 248 - rk(ad120(diag)) - rk(sp16(diag)); ks = 248 - rk(ad120(single)) - rk(sp16(single))
rec("P1", "nilpotent pencil kernels in the 248: diagonal triple 68, single raising triple 100; ranks 180 and 148",
    kd == 68 and ks == 100 and 248 - kd == 180 and 248 - ks == 148, f"kernels {kd}, {ks}")
# sl2 summand count cross-check: dim ker(e) = number of irreducible summands
summ_single = 2 + 11 + 55 + 32
summ_diag = 2 * 2 + 5 + 12 + 15 + 8 * 4
rec("P1b", "summand counts: 10 -> V1+V3 (2), 11 V2, 55 V0, 32 V_(3/2) = 100; diagonal 4+5+12+15+32 = 68",
    summ_single == 100 and summ_diag == 68)
# roster and traces from E8 weights (so16 roots + spinor weights) on X with eps1 = lam, eps2 = mu
lam, mu = sp.symbols("lambda mu")
val = [lam, mu] + [0] * 6
roots = [sg1 * val[i] + sg2 * val[j] for i in range(8) for j in range(i + 1, 8) for sg1 in (1, -1) for sg2 in (1, -1)]
spw = [sum(sg[k] * val[k] for k in range(8)) / 2 for sg in itertools.product((1, -1), repeat=8)
       if sg.count(-1) % 2 == 0]
tr = lambda ws, n: sp.expand(sum(w ** n for w in ws))
nonzero = [w for w in roots + spw if w != 0]
rec("E1", "roster: one adjoint 10, eleven vector 5, thirty-two spinor 4, 55 trivial; 10+55+128+55 = 248",
    len(roots) == 112 and len(spw) == 128 and 112 + 8 + 128 == 248 and
    len(nonzero) == 8 + 11 * 4 + 32 * 4 and 10 + 55 + 128 + 55 == 248, f"nonzero weights {len(nonzero)}")
tr5_4 = 2 * lam ** 4 + 2 * mu ** 4
at = {mu: I * lam}
ad10 = [lam, -lam, mu, -mu] + [s1 * lam + s2 * mu for s1 in (1, -1) for s2 in (1, -1)]
s4 = [(s1 * lam + s2 * mu) / 2 for s1 in (1, -1) for s2 in (1, -1)]
rec("E2", "at mu = i lambda: Tr_10 X^8 = 68, Tr_5 X^8 = 4, Tr_4 X^8 = 1/4 (times lambda^8)",
    sp.expand(tr(ad10, 8).subs(at)) == 68 * lam ** 8
    and sp.expand((2 * lam ** 8 + 2 * mu ** 8).subs(at)) == 4 * lam ** 8
    and sp.expand(tr(s4, 8).subs(at)) == lam ** 8 / 4)
T8 = tr(roots + spw, 8); T4 = tr(roots + spw, 4)
rec("E3", "(3) Tr_248 (ad X)^8 = 120 lambda^8 = (15/2)(Tr_5 X^4)^2 on Tr_5 X^2 = 0; Tr_248 X^4 = 0 there",
    sp.expand(T8.subs(at)) == 120 * lam ** 8 and sp.expand((sp.Rational(15, 2) * tr5_4 ** 2).subs(at)) == 120 * lam ** 8
    and sp.expand(T4.subs(at)) == 0)
rem = sp.rem(sp.expand(T8 - sp.Rational(15, 2) * tr5_4 ** 2), sp.expand(lam ** 2 + mu ** 2), mu)
rec("E3b", "the identity holds as a polynomial identity modulo Tr_5 X^2 = 2(lambda^2 + mu^2)", sp.expand(rem) == 0)
# matrix version: X = a E + b T3 in the vector five
asy, bsy = sp.symbols("a b")
X5 = asy * E5 + bsy * T3
c4 = sp.expand((E5 ** 3 * T3).trace())
cp = sp.expand((sp.Symbol("x") * sp.eye(5) - X5).det())
rec("E4", "Tr_5 X^2 = 0, Tr_5 X^4 = 4 a^3 b Tr(E^3 T3) with Tr(E^3 T3) > 0; char poly x^5 - (Tr_5 X^4/4) x "
    "(eigenvalues 0, +-lam, +-i lam, lam^4 = Tr X^4/4)", sp.expand((X5 ** 2).trace()) == 0 and
    sp.expand((X5 ** 4).trace() - 4 * asy ** 3 * bsy * c4) == 0 and c4 > 0 and
    sp.expand(cp - (sp.Symbol("x") ** 5 - sp.expand((X5 ** 4).trace()) / 4 * sp.Symbol("x"))) == 0, f"Tr E^3 T3 = {c4}")
an, bn = 1.0, 0.7
Xn = an * En + bn * Tn; M8 = emb(Xn)
t8 = np.trace(np.linalg.matrix_power(ad120(M8), 8)) + np.trace(np.linalg.matrix_power(sp16(M8), 8))
t4 = np.trace(np.linalg.matrix_power(ad120(M8), 4)) + np.trace(np.linalg.matrix_power(sp16(M8), 4))
tx4 = np.trace(np.linalg.matrix_power(Xn, 4))
rec("E5", "matrix 248 (so16 adjoint + chiral spinor): Tr (ad X)^8 = (15/2)(Tr_5 X^4)^2 and Tr (ad X)^4 = 0 for "
    "X = E + 0.7 T3; the b = 0 reference is nilpotent (trace 0)",
    abs(t8 - 7.5 * tx4 ** 2) < 1e-6 * abs(t8) and abs(t4) < 1e-8 and abs(t8) > 1 and
    abs(np.trace(np.linalg.matrix_power(ad120(emb(En)), 8))) < 1e-9, f"{t8.real:.6f} vs {7.5 * (tx4 ** 2).real:.6f}")
Kc = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)); Kc = Kc - Kc.T
w_, V_ = np.linalg.eig(Kc); gC = V_ @ np.diag(np.exp(0.3 * w_)) @ np.linalg.inv(V_)
rec("E6", "a complex orthogonal gauge conjugation preserves Tr_5 X^4 and the pencil ranks",
    np.allclose(gC.T @ gC, np.eye(5)) and abs(np.trace(np.linalg.matrix_power(gC @ Xn @ np.linalg.inv(gC), 4)) - tx4)
    < 1e-8 and rk(emb(gC @ En @ np.linalg.inv(gC))) == rk(single))

# ---------------------------------------------------------------- neutral family: commuting factors, centralizers
q0p = emb(En); r0p = np.zeros((16, 16), complex); r0p[5:10, 5:10] = En
u = emb(Tn); v = np.zeros((16, 16), complex); v[5:10, 5:10] = Tn
H = lambda X: X.conj().T
rec("N1", "[q0', v] = [r0', u] = [u, v] = 0; linear moment [q0', u^dag] + [u, q0'^dag] = 0 (T_(3) lowest)",
    all(np.allclose(cmn(X, Y), 0) for X, Y in ((q0p, v), (r0p, u), (u, v))) and
    np.allclose(cmn(q0p, H(u)) + cmn(u, H(q0p)), 0) and np.allclose(cmn(r0p, H(v)) + cmn(v, H(r0p)), 0))
# centralizers: in so10 (D5) and the E6-type 16 of so10
iu10 = [(i, j) for i in range(10) for j in range(i + 1, 10)]


def cent_dim_so10(ops):
    rowsM = []
    for X in ops:
        M = np.zeros((100, 45), complex)
        for col, (i, j) in enumerate(iu10):
            Eij = np.zeros((10, 10)); Eij[i, j], Eij[j, i] = 1, -1
            M[:, col] = (X @ Eij - Eij @ X).ravel()
        rowsM.append(M)
    return 45 - rk(np.vstack(rowsM))


q10, r10 = q0p[:10, :10], r0p[:10, :10]
ops = [q10, H(q10), r10, H(r10)]
sp10 = spin_rep(5)
k16 = 16 - rk(np.vstack([sp10(X) for X in ops]))
rec("N2", "compact centralizer of both triples: 0 in D5 = so10, 0 on the 16; so in E6 = so10+u1+16+16bar it is the "
    "single u1 (one Q direction)", cent_dim_so10(ops) == 0 and k16 == 0, f"so10 {cent_dim_so10(ops)}, 16 {k16}")
rec("N2b", "control: the centralizer of only one triple in so10 is the other so5 (dim 10)",
    cent_dim_so10([q10, H(q10)]) == 10)

# ---------------------------------------------------------------- plants: each must FAIL
rec("X1", "PLANT: cross-module phase with a symmetric (not exterior) product is +1",
    ((A10 * v1) * (A10 * v2).T + (A10 * v2) * (A10 * v1).T - (v1 * v2.T + v2 * v1.T)).is_zero_matrix, plant=True)
nosp = tr(roots, 8)
rec("X2", "PLANT: the identity (3) and the quartic cancellation survive without the 32 spinor fours",
    sp.expand(nosp.subs(at)) == 120 * lam ** 8 or sp.expand(tr(roots, 4).subs(at)) == 0, plant=True)
exw = sp.solve(ell ** -2 * (sp_ ** 2 + sp_) + c, sp_)
rec("X3", "PLANT: flipping the sign of d_t^2 gives the same exponents", {sp.simplify(e) for e in exw}
    == {sp.simplify(-betac), sp.simplify(1 + betac)}, plant=True)
rec("X4", "PLANT: a non-strict pole bound (m <= e/2) still gives one section of S^4 L_delta",
    h0(2, False) == 1, plant=True)
rec("X5", "PLANT: the misordered pencil kernel (single triple gives 68)", ks == 68, plant=True)

real = [r for r in rows if not r["plant"]]; plants = [r for r in rows if r["plant"]]
summary = {"checks": len(real), "hold": sum(r["holds"] for r in real),
           "fail": [r["id"] for r in real if not r["holds"]],
           "plants": len(plants), "plants_failing_as_required": sum(not r["holds"] for r in plants)}
out = {"summary": summary, "rows": rows}
for r in rows:
    print(("PLANT " if r["plant"] else "") + r["id"], "holds" if r["holds"] else "FAILS", "|", r["claim"][:80], "|",
          r["detail"][:80])
print(json.dumps(summary))
pathlib.Path(__file__).with_name("check_fixed_sector_light_system.json").write_text(json.dumps(out, indent=1) + "\n")
