"""B1957: the physical lane's withdrawn harmonic-transport draft of 2026-11-12 (preserved under failed_draft_01/).
The lane withdrew its conclusion (the full identification of the physical triplet and its mode table) for a missing
argument factor in the global section map.  Its exact group-theoretic statements are not withdrawn, and one of them is
a correction addressed to main's B1866 (finding F1).  They are tested here by main.  Data-free; nothing of the lane's is
run.  Conventions as the draft states them: F2 = <a, b>, L(a) = a, L(b) = ab, R(a) = ab, R(b) = b, s(a) = b^-1,
s(b) = a; rho(a) = I, rho(b) = J, K = IJ; E = {(phi, g): rho phi = Ad_g rho}, with (phi, g)(phi', g') = (phi phi', g g').
 H1  (L, (1+I)/sqrt2), (R, (1-J)/sqrt2) and (s, (1-K)/sqrt2) are in E.
 H2  Delta = L R^-1 L = Inn_a s as automorphisms of F2; its lift is I (1-K)/sqrt2 = (I+J)/sqrt2; s and Delta have the
     same homology matrix [[0, 1], [-1, 0]].
 H3  (s L)^3 = id on F2 with (g_s g_L)^3 = -1; s^4 = id with g_s^4 = -1; s^2 L s^-2 = Inn_(a^-1) L with the lifts;
     R = Inn_(b^-1) s L^-1 s^-1 with the lifts.
 H4  in Pin2 = U(1)_K + I U(1)_K: g_s is a rotation; g_Delta and g_(L^2) = I are reflections; so a character that is
     trivial on rotations and -1 on reflections is +1 on s and -1 on Delta and L^2.
 H5  the same on the 3 x 3 matrices of the draft's (13), which are B1866's F1 matrices: the word L R^-1 L has -1 on the
     branch it fixes, L^2 has -1 there, and the based s = Inn_a^-1 Delta has +1.
 H6  the two geometric lifts: (tau -> tau - 1, 1) and (tau -> -1/tau, sqrt tau) satisfy s^4 = (s t)^3 = (id, -1) and
     [s^2, t] = 1; negating both roots keeps the relations; negating one breaks (s t)^3.
 H7  the eta law v(gamma tau) = chi_-1 sigma v(tau), v = eta/|eta|: chi_-1 = e(-1/24) on t and e(-3/24) on s; the three
     check values at tau = i.
 H9  the draft's Szego function has residue 1 at the puncture, and its two quasi-periods.
 H8  (13) and (14): diag(-i, 1, i) conjugates A_L, A_R into the adjoint rotations of g_L, g_R on the axes (I, K, J);
     chi_21(L) A_L and chi_21(R) A_R are the triplet's exact monomial matrices as B1866 carries them."""
import functools, cmath, math
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
print = functools.partial(print, flush=True)

# ---- quaternions with rational coordinates times a power of 1/sqrt2: (w, x, y, z, k) means (w + xI + yJ + zK) / sqrt2^k
def qmul(p, q):
    a1, b1, c1, d1, k1 = p; a2, b2, c2, d2, k2 = q
    return norm((a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2, a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2, k1 + k2))
def norm(q):
    w, x, y, z, k = q
    while k >= 2 and all(Fr(v) % 2 == 0 for v in (w, x, y, z)): w, x, y, z, k = Fr(w) / 2, Fr(x) / 2, Fr(y) / 2, Fr(z) / 2, k - 2
    return (Fr(w), Fr(x), Fr(y), Fr(z), k)
def qinv(q): w, x, y, z, k = q; n = (w * w + x * x + y * y + z * z); return norm((w * 2 ** k / n, -x * 2 ** k / n, -y * 2 ** k / n, -z * 2 ** k / n, k))   # conj / |q|^2, |q|^2 = n / 2^k
ONE, QI, QJ, QK, MONE = norm((1, 0, 0, 0, 0)), norm((0, 1, 0, 0, 0)), norm((0, 0, 1, 0, 0)), norm((0, 0, 0, 1, 0)), norm((-1, 0, 0, 0, 0))
gL, gR, gs = norm((1, 1, 0, 0, 1)), norm((1, 0, -1, 0, 1)), norm((1, 0, 0, -1, 1))
qpow = lambda q, n: functools.reduce(qmul, [q] * n, ONE)
ad = lambda g, x: qmul(qmul(g, x), qinv(g))

# ---- free-group words: tuples of (generator, +-1), reduced
def red(w):
    out = []
    for t in w:
        if out and out[-1][0] == t[0] and out[-1][1] == -t[1]: out.pop()
        else: out.append(t)
    return tuple(out)
inv = lambda w: tuple((g, -e) for g, e in reversed(w))
a, b = (("a", 1),), (("b", 1),)
def auto(ia, ib): return {"a": ia, "b": ib}
def app(phi, w): return red(sum(((phi[g] if e == 1 else inv(phi[g])) for g, e in w), ()))
comp = lambda *phis: functools.reduce(lambda f, g: auto(app(f, g["a"]), app(f, g["b"])), phis)           # comp(f, g) = f o g (g first)
L, R, S = auto(a, red(a + b)), auto(red(a + b), b), auto(inv(b), a); Rinv, Linv, Sinv = auto(red(a + inv(b)), b), auto(a, red(inv(a) + b)), auto(b, inv(a))
inn = lambda h: auto(red(h + a + inv(h)), red(h + b + inv(h))); ID = auto(a, b)
rho = lambda w: functools.reduce(qmul, [(QI if g == "a" else QJ) if e == 1 else qinv(QI if g == "a" else QJ) for g, e in w], ONE)
homology = lambda phi: [[sum(e for g, e in phi[x] if g == y) for x in "ab"] for y in "ab"]            # columns are the images
in_E = lambda phi, g: all(rho(phi[x]) == ad(g, rho(w)) for x, w in (("a", a), ("b", b)))


if __name__ == "__main__":
    assert comp(R, Rinv) == ID and comp(L, Linv) == ID and comp(S, Sinv) == ID
    print("H1: in E: (L, (1+I)/sqrt2) %s; (R, (1-J)/sqrt2) %s; (s, (1-K)/sqrt2) %s; and not with a wrong sign: (R, (1+J)/sqrt2) %s" % (in_E(L, gL), in_E(R, gR), in_E(S, gs), in_E(R, norm((1, 0, 1, 0, 1)))))
    Delta = comp(L, Rinv, L); gD = qmul(qmul(gL, qinv(gR)), gL)
    print("H2: Delta = L R^-1 L sends a -> %s, b -> %s; Inn_a s is the same automorphism: %s; s Inn_a is: %s; its lift g_L g_R^-1 g_L = %s = I g_s: %s = (I+J)/sqrt2: %s; homology of s %s and of Delta %s" % (
        Delta["a"], Delta["b"], Delta == comp(inn(a), S), Delta == comp(S, inn(a)), gD, gD == qmul(QI, gs), gD == norm((0, 1, 1, 0, 1)), homology(S), homology(Delta)))
    print("H2: the draft's own rejecting control: the based word s with Delta's quaternion is NOT in E: %s; nor Delta with s's quaternion: %s (equal homology matrices do not make equal lifts)" % (not in_E(S, gD), not in_E(Delta, gs)))
    sL = comp(S, L); s2 = comp(S, S)
    print("H3: (s L)^3 = id: %s with (g_s g_L)^3 = -1: %s; s^4 = id: %s with g_s^4 = -1: %s; s^2 L s^-2 = Inn_(a^-1) L: %s with lifts g_s^2 g_L g_s^-2 = rho(a^-1) g_L: %s; R = Inn_(b^-1) s L^-1 s^-1: %s with lifts: %s" % (
        comp(sL, sL, sL) == ID, qpow(qmul(gs, gL), 3) == MONE, comp(s2, s2) == ID, qpow(gs, 4) == MONE, comp(s2, L, comp(Sinv, Sinv)) == comp(inn(inv(a)), L),
        qmul(qmul(qpow(gs, 2), gL), qinv(qpow(gs, 2))) == qmul(qinv(QI), gL), R == comp(inn(inv(b)), S, Linv, Sinv), gR == qmul(qmul(qmul(qinv(QJ), gs), qinv(gL)), qinv(gs))))
    com = lambda g: "rotation" if qmul(g, QK) == qmul(QK, g) else ("reflection" if qmul(g, QK) == qmul(MONE, qmul(QK, g)) else "neither")
    print("H4: in Pin2 about the axis K: g_s is a %s, g_Delta a %s, g_(L^2) = %s a %s, g_L itself %s; so the character (+1 on rotations, -1 on reflections) is %+d on s, %+d on Delta, %+d on L^2 (the draft's (11): +1, -1, -1)" % (
        com(gs), com(gD), qpow(gL, 2), com(qpow(gL, 2)), com(gL), *[1 if com(g) == "rotation" else -1 for g in (gs, gD, qpow(gL, 2))]))
    def axis_sign(g):
        img = []
        for x in (QI, QJ, QK):
            y = ad(g, x); img.append([k for k, z in enumerate((QI, QJ, QK)) if y[:4] in (z[:4], qmul(MONE, z)[:4])][0])
        return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if img[i] > img[j])
    print("H4: the sign of the permutation of the three unoriented axes: L^2 %+d, s %+d, Delta %+d (the draft's middle spin line: +1, -1, -1)" % (axis_sign(qpow(gL, 2)), axis_sign(gs), axis_sign(gD)))
    AL = np.array([[1, 0, 0], [0, 0, 1j], [0, 1j, 0]]); AR = np.array([[0, -1j, 0], [-1j, 0, 0], [0, 0, 1]]); iv = np.linalg.inv
    SD = AL @ iv(AR) @ AL; fixed = [k for k in range(3) if abs(abs(SD[k, k]) - 1) < 1e-12]; Ss = iv(AL @ AL) @ SD; k0 = fixed[0]
    print("H5: on the draft's 3 x 3 matrices (axes I, K, J): the word L R^-1 L fixes branch %s (the axis K) with eigenvalue %s; L^2 there: %s; the based s = Inn_a^-1 Delta, that is A_L^-2 times it: %s (B1866's F1 found -1 and -1 for the word; the relay's text said +1, which is the based s)" % (
        [k + 1 for k in fixed], np.round(SD[k0, k0], 12), np.round((AL @ AL)[k0, k0], 12), np.round(Ss[k0, k0], 12)))
    # ---- H6: the geometric lifts
    mp.mp.dps = 30
    def lift(g, root): return (g, root)
    def mul(x, y):
        (g1, b1), (g2, b2) = x, y; g = [[sum(g1[i][k] * g2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        return (g, lambda t, b1=b1, b2=b2, g2=g2: b1((g2[0][0] * t + g2[0][1]) / (g2[1][0] * t + g2[1][1])) * b2(t))
    def val(x, t): return (x[0], complex(x[1](t)))
    for name, sg_s, sg_t in (("q0", 1, 1), ("q1 (both roots negated)", -1, -1), ("one root negated", -1, 1)):
        tq = lift([[1, -1], [0, 1]], lambda t: mp.mpf(sg_t)); sq = lift([[0, -1], [1, 0]], lambda t: sg_s * mp.sqrt(t)); t0 = mp.mpc("0.37", "1.21")
        s4 = functools.reduce(mul, [sq] * 4); st = mul(sq, tq); st3 = functools.reduce(mul, [st] * 3); s2q = mul(sq, sq); c1, c2 = mul(s2q, tq), mul(tq, s2q)
        print("H6: %s: s^4 = (%s, %.6f); (s t)^3 = (%s, %.6f); s^2 t against t s^2: bases %s, roots differ by %.1e" % (name, s4[0], val(s4, t0)[1].real, st3[0], val(st3, t0)[1].real, c1[0] == c2[0], abs(val(c1, t0)[1] - val(c2, t0)[1])))
    # ---- H7: the eta law
    eta = lambda t: mp.exp(2j * mp.pi * t / 24) * mp.qp(mp.exp(2j * mp.pi * t)); v = lambda t: eta(t) / abs(eta(t)); t0 = mp.mpc("0.37", "1.21")
    ct = v(t0 - 1) / v(t0); cs = v(-1 / t0) / (mp.sqrt(t0) / abs(mp.sqrt(t0)) * v(t0)); e = lambda x: cmath.exp(2j * math.pi * x)
    print("H7: v(tau - 1)/v(tau) = e(%.6f/24) (chi_-1(L) = e(-1/24)); v(-1/tau)/(sigma v(tau)) = e(%.6f/24) (chi_-1(s) = chi_-1(L)^3 = e(-3/24)); at tau = i: sigma_s = e(%.4f) (1/8)" % (
        float(mp.arg(ct) * 24 / (2 * mp.pi)), float(mp.arg(cs) * 24 / (2 * mp.pi)), float(mp.arg(mp.sqrt(1j)) / (2 * mp.pi))))
    sig = e(1 / 8); x1 = sig ** -3 * 1; x2 = sig ** -3 * -1; x3 = e(-3 * 2 / 24) * -1
    print("H7: the three check values: the simple pole under s: sigma^-3 = e(%.4f) (the draft: exp(-3 pi i/4) = e(-0.375)); under Delta: e(%.4f) (exp(pi i/4) = e(0.125)); under L^2 in the eta frame: %s (i)" % (cmath.phase(x1) / (2 * math.pi), cmath.phase(x2) / (2 * math.pi), np.round(x3, 12)))
    # ---- H8
    Dg = np.diag([-1j, 1, 1j]); basis = [QI, QK, QJ]
    def rot(g):
        M = np.zeros((3, 3))
        for c, x in enumerate(basis):
            y = ad(g, x)
            for r, z in enumerate(basis): M[r, c] = float(sum(u * w for u, w in zip(y[:4], z[:4])))
        return M
    X_L = np.array([[e(-1 / 8), 0, 0], [0, 0, e(1 / 8)], [0, e(1 / 8), 0]]); X_R = np.array([[0, e(-1 / 8), 0], [e(-1 / 8), 0, 0], [0, 0, e(1 / 8)]])   # B1866's XL, XR written out
    print("H8: |D A_L D^-1 - Ad(g_L)| = %.1e, |D A_R D^-1 - Ad(g_R)| = %.1e on the axes (I, K, J), D = diag(-i, 1, i); |chi_21(L) A_L - T_L| = %.1e, |chi_21(R) A_R - T_R| = %.1e with the triplet's monomial matrices as B1866 carries them" % (
        np.abs(Dg @ AL @ iv(Dg) - rot(gL)).max(), np.abs(Dg @ AR @ iv(Dg) - rot(gR)).max(), np.abs(e(21 / 24) * AL - X_L).max(), np.abs(e(-21 / 24) * AR - X_R).max()))
    mp.mp.dps = 30; tt = mp.mpc("0.21", "1.3"); qn = mp.exp(1j * mp.pi * tt)
    S3 = lambda z: mp.pi * mp.jtheta(1, 0, qn, 1) * mp.jtheta(3, mp.pi * z, qn) / (mp.jtheta(3, 0, qn) * mp.jtheta(1, mp.pi * z, qn)); z0 = mp.mpc("1e-9", "2e-9")
    print("H9: the draft's Szego function pi theta_1'(0) theta_3(pi z)/(theta_3(0) theta_1(pi z)): z S(z) at small z = %s (residue 1); quasi-periods S(z + 1)/S(z) = %s, S(z + tau)/S(z) = %s (the character of its flat line)" % (
        mp.nstr(z0 * S3(z0), 12), mp.nstr(S3(mp.mpc("0.13", "0.2") + 1) / S3(mp.mpc("0.13", "0.2")), 8), mp.nstr(S3(mp.mpc("0.13", "0.2") + tt) / S3(mp.mpc("0.13", "0.2")), 8)))
