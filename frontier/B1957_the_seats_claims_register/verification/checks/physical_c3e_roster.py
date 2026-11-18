"""B1957: the physical lane's P-C3e, the exact representation theory in its three files COMPLETE_PHYSICAL_KERNEL...,
COMPLETE_CUBIC... and NEUTRAL_STATIONARY_FAMILY_AND_FULL_E8_PENCIL, rebuilt by main from E8's own weights and from
explicit matrices.  Data-free.  Nothing of the lane's is run; its statements are read and the objects built here.

The setting, as the lane states it: E8 > E6 > D5 = so(10) > so(5) + so(5), acting on two orthogonal five-spaces; in each
so(5) the principal sl2 (the vector 5 is spin 2).  E_+ and E_- are the raising elements of the two factors; the lane's
reflection is A = (-i N) exp(-i pi H/4) with N the exchange of the two five-spaces and H the total weight operator.
 R1  the roster: so(10)'s adjoint under the two principal sl2 is (1,0)+(3,0)+(0,1)+(0,3)+(2,2), its spinor is
     (3/2,3/2); no summand (0,0): the two triples' centraliser in D5 has zero Lie algebra.
 R2  the reflection: Ad_A T_(j,+) = (-i)^j T_(j,-); on weight m the phase is i^(-m); a vector highest weight goes to
     the other five-space with phase i; the cross module's highest element has phase +1; the 2 x 2 actions of the
     kernel file's equation (1), and the signs for j = 1 and j = 3.
 R3  the spinor: in the 4 of so(5) the lowest element of the adjoint's spin-3 part is one non-zero matrix entry.
 R4  the channels of the cubic by charge, weight and the one-form-slot rule; the flat directions of the light cubic (5);
     the leading charged mass matrix Y1 and its rank.
 R5  the pencil: Tr_5 X^2 = 0 and Tr_5 X^4 = 4 a^3 b Tr(E^3 T) for X = a E + b T; eigenvalues 0, +-lam, +-i lam.
 R6  E8's 248 under one so(5): one adjoint, eleven vectors, thirty-two spinors, 55 trivial; the number of sl2 summands
     under one principal triple (100) and under the diagonal one (68); the ranks 148 and 180.
 R7  the traces at mu = i lam: 68, 4 and 1/4 times lam^8; Tr_248 (ad X)^8 = 120 lam^8 = (15/2)(Tr_5 X^4)^2, by the
     roster with explicit matrices AND directly from E8's weights; the fourth-power trace vanishes.
 R8  the section counts the files use, given the degrees they state (an elliptic curve: h0 = d for d > 0; for d = 0
     one section if the flat line is trivial and none otherwise; none for d < 0)."""
import itertools, functools, collections
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)


def spin(j2):
    """(J_z, J_+) of spin j2/2, basis m = j, j-1, ..., -j"""
    j = j2 / 2; ms = [j - k for k in range(j2 + 1)]; Jp = np.zeros((j2 + 1, j2 + 1), complex)
    for k in range(1, j2 + 1): Jp[k - 1, k] = np.sqrt((j - ms[k]) * (j + ms[k] + 1))
    return np.diag(ms).astype(complex), Jp


JZ, JP = spin(4); JM = JP.conj().T; Bf = np.zeros((5, 5)); 
for k in range(5): Bf[k, 4 - k] = (-1) ** k                               # the invariant symmetric form on spin 2
in_so5 = lambda X: np.abs(X.T @ Bf + Bf @ X).max() < 1e-12
Z5 = np.zeros((5, 5), complex); emb = lambda X, Y: np.block([[X, Z5], [Z5, Y]])
H10 = emb(2 * JZ, 2 * JZ); N10 = np.block([[Z5, np.eye(5)], [np.eye(5), Z5]]).astype(complex)
A10 = -1j * N10 @ np.diag(np.exp(-1j * np.pi * np.diag(H10) / 4)); A10i = np.linalg.inv(A10)


def e8_weights():
    W = [tuple([Fr(0)] * 8)] * 8
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((1, -1), repeat=2):
            v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); W.append(tuple(v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0: W.append(tuple(Fr(x, 2) for x in s))
    return W


def summands(W, h):
    """the number of irreducible sl2 summands of a module with weights W under the coweight h: #(0) + #(1)"""
    c = collections.Counter(sum(a * b for a, b in zip(h, w)) for w in W); return c[0] + c[1], c


def so10_weights():
    W = [tuple([Fr(0)] * 5)] * 5
    for i, j in itertools.combinations(range(5), 2):
        for si, sj in itertools.product((1, -1), repeat=2):
            v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj); W.append(tuple(v))
    S = [tuple(Fr(x, 2) for x in s) for s in itertools.product((1, -1), repeat=5) if s.count(-1) % 2 == 0]
    return W, S


def bispin(W, h1, h2):
    """the decomposition of a module with weights W under two commuting sl2 (coweights h1, h2; weights m = <h, w>/2)"""
    c = collections.Counter((sum(a * b for a, b in zip(h1, w)) / 2, sum(a * b for a, b in zip(h2, w)) / 2) for w in W); out = []
    while sum(c.values()):
        m1 = max(k[0] for k, v in c.items() if v); m2 = max(k[1] for k, v in c.items() if v and k[0] == m1); out.append((m1, m2))
        for a in range(int(2 * m1) + 1):
            for b in range(int(2 * m2) + 1):
                k = (m1 - a, m2 - b); assert c[k] > 0, (k, out); c[k] -= 1
    return sorted(out)


def spinor_rep():
    """the 4 of so(5): X (antisymmetric for the form Bf) -> (1/4) sum X'_ab g_a g_b in an orthonormal frame of Bf"""
    w, V = np.linalg.eigh(Bf); S = V @ np.diag(1 / np.sqrt(w.astype(complex)))                    # S^T Bf S = 1
    assert np.abs(S.T @ Bf @ S - np.eye(5)).max() < 1e-12
    s1, s2, s3, s0 = np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex), np.eye(2, dtype=complex)
    g = [np.kron(s1, s0), np.kron(s2, s0), np.kron(s3, s1), np.kron(s3, s2), np.kron(s3, s3)]
    for a in range(5):
        for b in range(5): assert np.abs(g[a] @ g[b] + g[b] @ g[a] - 2 * (a == b) * np.eye(4)).max() < 1e-12
    Si = np.linalg.inv(S)
    def rho(X):
        Xp = Si @ X @ S; return sum(Xp[a, b] * g[a] @ g[b] for a in range(5) for b in range(5)) / 4
    return rho


if __name__ == "__main__":
    # R1
    W45, W16 = so10_weights(); h1, h2 = (4, 2, 0, 0, 0), (0, 0, 4, 2, 0)
    d45 = bispin(W45, h1, h2); d16 = bispin(W16, h1, h2)
    print("R1: so(10)'s adjoint under the two principal sl2: %s (dimensions sum to %d); its spinor: %s; a summand (0, 0): %s" % ([(str(a), str(b)) for a, b in d45], sum((2 * a + 1) * (2 * b + 1) for a, b in d45), [(str(a), str(b)) for a, b in d16], (0, 0) in d45))
    print("R1: E6's adjoint: 1 + 45 + 16 + 16 = %d" % (1 + 45 + 16 + 16))
    # R2
    assert in_so5(JP) and in_so5(JM) and in_so5(JP @ JP @ JP) and not in_so5(JP @ JP)
    for j in (1, 3):
        Tp, Tm = emb(np.linalg.matrix_power(JP, j), Z5), emb(Z5, np.linalg.matrix_power(JP, j)); L = A10 @ Tp @ A10i
        print("R2: j = %d: |Ad_A T_(j,+) - (-i)^j T_(j,-)| = %.1e; down the string, the phase at each weight m against i^(-m): %.1e" % (j, np.abs(L - (-1j) ** j * Tm).max(),
              max(np.abs(A10 @ (lambda X: X)(functools.reduce(lambda X, _: emb(JM, Z5) @ X - X @ emb(JM, Z5), range(k), Tp)) @ A10i - 1j ** (-(j - k)) * functools.reduce(lambda X, _: emb(Z5, JM) @ X - X @ emb(Z5, JM), range(k), Tm)).max() for k in range(2 * j + 1))))
    e = np.zeros(10, complex); e[0] = 1; ep = np.zeros(10, complex); ep[5] = 1
    print("R2: the vector's highest weight: A e = %s e' (the lane: i); the cross module's highest element e ^ e' goes to %s times itself (the lane: +1)" % (np.round((A10 @ e)[5], 12), np.round((np.outer(A10 @ e, A10 @ ep) - np.outer(A10 @ ep, A10 @ e))[0, 5], 12)))
    for j in (1, 3):
        ap, am = 1j * 1j ** (-j), 1j * 1j ** j; beta = (-1) ** ((j + 1) // 2)
        print("R2: j = %d: A_(+j) = %s sigma_x, A_(-j) = %s sigma_x (the lane: i^(1-j), i^(1+j)); beta_j = %+d; in a sigma_x eigenline the two core phases at w = -j are (%s, %s): %s" % (j, np.round(ap, 12), np.round(am, 12), beta, np.round(am, 12).real, np.round(beta * am, 12).real, "opposite, a non-trivial flat line" if beta == -1 else "equal, the characters (delta, delta)"))
    # R3
    rho = spinor_rep(); X1, X2 = JP + 0.3 * JM @ JM @ JM, JM + 0.7 * JP @ JP @ JP - 0.2 * JZ
    hom = np.abs(rho(X1 @ X2 - X2 @ X1) - (rho(X1) @ rho(X2) - rho(X2) @ rho(X1))).max(); w, V = np.linalg.eig(rho(JZ)); o = np.argsort(-w.real); Vv = V[:, o]
    L3 = np.linalg.inv(Vv) @ rho(JM @ JM @ JM) @ Vv; nz = [(a, b) for a in range(4) for b in range(4) if abs(L3[a, b]) > 1e-9]
    print("R3: the 4 of so(5) built from Clifford matrices: a homomorphism to %.1e; its weights %s; the lowest spin-3 element has non-zero entries at %s of modulus %.4f (one entry, from weight 3/2 to -3/2)" % (hom, np.round(w.real[o], 6).tolist(), nz, abs(L3[nz[0]])))
    # R4
    form = {"A": (0, 0), "B": (0, 4), "P": (1, 3), "R": (-1, 3)}; spn = {"N": (0, -3), "S": (1, 0), "T": (-1, 0)}
    ch = sorted({(f,) + tuple(sorted((u, v))) for f in form for u in spn for v in spn if form[f][0] + spn[u][0] + spn[v][0] == 0 and form[f][1] + spn[u][1] + spn[v][1] == 0})
    print("R4: one form slot and two spin slots, total charge and total weight zero: the channels are %s (the lane: A S T, N T P, N S R)" % [" ".join(c) for c in ch])
    A_, S_, T_, Nc, Nd, Pc, Ps, Rc, Rs, y, lp, lm, t, nc, nd = sp.symbols("A S T N_c N_d P_c P_s R_c R_s y lambda_p lambda_m t nu_c nu_d")
    W3 = y * A_ * S_ * T_ + lp * Nc * Pc * T_ + lm * Nd * Rc * S_; flat = {S_: 0, T_: 0, Nc: 0, Nd: 0}
    print("R4: with S = T = N_c = N_d = 0 every first derivative of the light cubic vanishes for all A, P, R: %s" % all(sp.simplify(sp.diff(W3, v).subs(flat)) == 0 for v in (A_, S_, T_, Nc, Nd, Pc, Ps, Rc, Rs)))
    Y1 = sp.Matrix(3, 3, lambda i, k: sp.diff(W3.subs({Nc: t * nc, Nd: t * nd, A_: 0}), [Pc, Ps, S_][i], [Rc, Rs, T_][k])) / t
    print("R4: on N_c = t nu_c, N_d = t nu_d the charged mass matrix over t, rows (P_c, P_s, S), columns (R_c, R_s, T): %s; rank %d; (Y Y^T) eigenvalues %s" % (Y1.tolist(), Y1.rank(), sorted(map(str, (Y1 * Y1.T).eigenvals()))))
    # R5
    rng = np.random.default_rng(5); a, b = rng.normal(size=2) + 1j * rng.normal(size=2); T3 = JM @ JM @ JM; X = a * JP + b * T3
    tr = lambda M, k: np.trace(np.linalg.matrix_power(M, k)); c3 = np.trace(JP @ JP @ JP @ T3).real; ev = np.linalg.eigvals(X); lam4 = tr(X, 4) / 4
    print("R5: X = a E + b T: |Tr X^2| = %.1e; |Tr X^4 - 4 a^3 b Tr(E^3 T)| = %.1e with Tr(E^3 T) = %.0f > 0; the eigenvalues' fourth powers against (0, lam^4 four times): %.1e" % (abs(tr(X, 2)), abs(tr(X, 4) - 4 * a ** 3 * b * c3), c3, np.abs(np.sort_complex(ev ** 4) - np.sort_complex(np.array([0] + [lam4] * 4))).max()))
    # R6
    W = e8_weights(); assert len(W) == 248
    x, yv = sp.symbols("x y"); proj = collections.Counter(sp.expand(w[0] * x + w[1] * yv) for w in W)
    adj = [0, 0] + [s * x for s in (1, -1)] + [s * yv for s in (1, -1)] + [s * x + u * yv for s in (1, -1) for u in (1, -1)]; vec = [0, x, -x, yv, -yv]; spi = [sp.expand((s * x + u * yv) / 2) for s in (1, -1) for u in (1, -1)]
    ros = collections.Counter(); 
    for mult, ws in ((1, adj), (11, vec), (32, spi), (55, [0])):
        for wv in ws: ros[sp.expand(wv)] += mult
    print("R6: E8's 248 weights restricted to one so(5) (the first two coordinates) equal 1 adjoint + 11 vectors + 32 spinors + 55 trivial as multisets: %s (10 + 55 + 128 + 55 = %d)" % (proj == ros, 10 + 55 + 128 + 55))
    n1, c1 = summands(W, (4, 2, 0, 0, 0, 0, 0, 0)); n2, c2 = summands(W, (4, 2, 4, 2, 0, 0, 0, 0))
    print("R6: sl2 summands of the 248: under one principal triple %d (weight 0: %d, weight 1: %d), so its raising element has rank %d; under the diagonal triple %d (weight 0: %d, weight 1: %d), rank %d (the lane: 100 and 148; 68 and 180)" % (n1, c1[0], c1[1], 248 - n1, n2, c2[0], c2[1], 248 - n2))
    # the diagonal triple's raising element is z1 E_+ + z2 E_- for any non-zero z1, z2: conjugate by the torus exp(s H_+ + s' H_-)
    # R7
    def ad10(Xm):
        basis = []
        for i in range(5):
            for k in range(5):
                M = np.zeros((5, 5), complex); M[i, k] = 1; basis.append(M)
        K = np.array([(M.T @ Bf + Bf @ M).ravel() for M in basis]).T; u, s, vh = np.linalg.svd(K); ns = vh[np.sum(s > 1e-10):].conj()   # so(5) as the kernel
        assert ns.shape[0] == 10
        G = np.array([sum(cf * M for cf, M in zip(v, basis)).ravel() for v in ns]).T
        return np.linalg.lstsq(G, np.array([(Xm @ g.reshape(5, 5) - g.reshape(5, 5) @ Xm) for g in G.T]).reshape(10, 25).T, rcond=None)[0]
    lam8 = lam4 ** 2; t10, t5, t4 = tr(ad10(X), 8), tr(X, 8), tr(rho(X), 8); full = t10 + 11 * t5 + 32 * t4
    print("R7: explicit matrices, random a and b: Tr_10 (ad X)^8/lam^8 = %.6f (68); Tr_5 X^8/lam^8 = %.6f (4); Tr_4 X^8/lam^8 = %.6f (1/4); by the roster Tr_248 (ad X)^8/lam^8 = %.6f (120), and over (Tr_5 X^4)^2: %.6f (15/2)" % (abs(t10 / lam8), abs(t5 / lam8), abs(t4 / lam8), abs(full / lam8), abs(full / tr(X, 4) ** 2)))
    q4 = tr(ad10(X), 4) + 11 * tr(X, 4) + 32 * tr(rho(X), 4); print("R7: the fourth power: Tr_10 + 11 Tr_5 + 32 Tr_4 of X^4 over lam^4 = %.1e (parts %.4f, %.4f, %.4f: the lane's cancellation)" % (abs(q4 / lam4), (tr(ad10(X), 4) / lam4).real, (11 * tr(X, 4) / lam4).real, (32 * tr(rho(X), 4) / lam4).real))
    l = sp.symbols("lam"); hh = (l, sp.I * l, 0, 0, 0, 0, 0, 0); p8 = sp.expand(sum(sum(a_ * b_ for a_, b_ in zip(hh, w)) ** 8 for w in W)); p4 = sp.expand(sum(sum(a_ * b_ for a_, b_ in zip(hh, w)) ** 4 for w in W)); p2 = sp.expand(sum(sum(a_ * b_ for a_, b_ in zip(hh, w)) ** 2 for w in W))
    print("R7: directly from E8's 248 weights at the Cartan element (lam, i lam, 0, ..., 0): sum of eighth powers = %s; of fourth powers = %s; of squares = %s" % (p8, p4, p2))
    xx, yy = sp.symbols("x y"); g8 = sp.expand(sum((w[0] * xx + w[1] * yy) ** 8 for w in W)); t54 = 2 * xx ** 4 + 2 * yy ** 4; rem = sp.rem(sp.expand(g8 - sp.Rational(15, 2) * t54 ** 2), xx ** 2 + yy ** 2, xx)
    print("R7: as polynomials in the two eigenvalues: Tr_248 (ad X)^8 - (15/2)(Tr_5 X^4)^2 is divisible by x^2 + y^2 = Tr_5 X^2 / 2: remainder %s (so the identity holds on the whole family Tr_5 X^2 = 0)" % rem)
    s_, t_ = sp.symbols("s t"); hh2 = (s_, sp.I * s_, t_, sp.I * t_, 0, 0, 0, 0); b8 = sp.factor(sp.expand(sum(sum(a_ * b_ for a_, b_ in zip(hh2, w)) ** 8 for w in W)))
    print("R7: the pencil z1 q' + z2 r' with both neutral amplitudes on (eigenvalues s, i s in one factor and t, i t in the other): Tr_248 (ad)^8 = %s; fourth powers: %s (zero for the reference pencil, where s = t = 0)" % (b8, sp.expand(sum(sum(a_ * b_ for a_, b_ in zip(hh2, w)) ** 4 for w in W))))
    print("R5: the moment's linear term: |[T_(3), E^dagger]| = %.1e and |[T_(3)^dagger, E]| = %.1e; factors commute: |[E_+, T_(3,-)]| = %.1e" % (np.abs(T3 @ JM - JM @ T3).max(), np.abs(T3.conj().T @ JP - JP @ T3.conj().T).max(), np.abs(emb(JP, Z5) @ emb(Z5, T3) - emb(Z5, T3) @ emb(JP, Z5)).max()))
    # R8
    h0 = lambda d, trivial=False: d if d > 0 else (1 if (d == 0 and trivial) else 0)
    print("R8: section counts on an elliptic curve at the degrees the files state: spin j = 1 (degree 0, non-trivial flat line): %d and %d; j = 3 at w = +3 (degree -2): %d; at w = -3 (S^4 L_delta with one pole, degree 1): %d for each delta, so %d neutral spin modes; the cross module's forms (degree 2): %d; the charged forms' target (degree 2): %d" % (h0(0), h0(0), h0(-2), h0(1), 2 * h0(1), h0(2), h0(2)))
    print("R8: the count: neutral A, B1, B2, N_+, N_- = 5; charged 3 + 3; one gaugino: %d in all, %d chiral; without the two charged spin modes %d chiral" % (5 + 3 + 3 + 1, 11, 9))
