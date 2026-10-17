"""Check 1: hand computations and exact identities of the paper.
A.2 commutator and sign; Lemma 11 (Jacobi isotropy); Theorem 12(1),(2),(3);
Theorem 20 (joint law: det, adj, symmetric form, polar identity, geometric masses);
Proposition 13 (Weierstrass identity sum rho_r^2 wp(z_r) = 0)."""
import sympy as sp
import numpy as np
import mpmath as mp

print("=== A.2: commutator, sign, balance points ===")
L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]])
A = L * R; B = R * L
C = A * B * A.inv() * B.inv()
print("LR =", A.tolist(), " RL =", B.tolist())
print("[LR,RL] =", C.tolist(), " trace =", C.trace())
U = -C
print("U = -[LR,RL]:", U.tolist(), " tr U =", U.trace(), " unipotent:", (U - sp.eye(2)) ** 2 == sp.zeros(2))
# the classical kernel check: commutator subgroup of SL(2,Z)
X1 = L * R.inv() * L; X2 = L.inv() * R
print("LR^-1L =", X1.tolist(), " square =", (X1 ** 2).tolist())
print("L^-1R =", X2.tolist(), " cube =", (X2 ** 3).tolist(), " 6th power =", (X2 ** 6).tolist())
# mirror: conjugation by diag(1,-1) sends L -> L^-1, R -> R^-1
Dm = sp.diag(1, -1)
print("mirror sends L->L^-1:", Dm * L * Dm == L.inv(), " R->R^-1:", Dm * R * Dm == R.inv())
print("tr[L,R] =", (L * R * L.inv() * R.inv()).trace())
# Fricke: tr[a,b] = x^2+y^2+z^2 - xyz - 2 with x,y,z = tr a, tr b, tr ab
x, y, z = A.trace(), B.trace(), (A * B).trace()
print("Fricke check: x^2+y^2+z^2-xyz-2 =", x**2 + y**2 + z**2 - x*y*z - 2, " (tr commutator =", C.trace(), ")")
# fixed points of LR^-1L and L^-1R
tau = sp.symbols('tau')
def mob(M, t): return (M[0,0]*t + M[0,1]) / (M[1,0]*t + M[1,1])
print("fixed points of LR^-1L:", sp.solve(sp.Eq(mob(X1, tau), tau), tau))
print("fixed points of L^-1R:", sp.solve(sp.Eq(mob(X2, tau), tau), tau))

print("\n=== Theorem 2 grid: torsion of H1 = |2 - tr B(a,b)| = ab ===")
a, b = sp.symbols('a b', positive=True, integer=True)
Bab = sp.Matrix([[1 + a*b, a], [b, 1]])
print("det B =", sp.simplify(Bab.det()), " tr B =", sp.expand(Bab.trace()), " det(B-I) =", sp.expand((Bab - sp.eye(2)).det()))
cnt = sum(1 for i in range(1, 13) for j in range(1, 13) if i*j == 1)
print("torsion-free closures on 12x12 grid:", cnt, "; all hyperbolic:", all(2 + i*j > 2 for i in range(1,13) for j in range(1,13)))
# H1 of the mapping torus of LR: Z + coker(A - I)
M = A - sp.eye(2)
from sympy.matrices.normalforms import smith_normal_form
print("Smith normal form of LR - I:", smith_normal_form(M, domain=sp.ZZ).tolist(), " -> torsion trivial")

print("\n=== Lemma 4: parity action of L, R on F_2^2 (row vectors, right action) ===")
par = [(1,0),(0,1),(1,1)]
def act(v, M):
    w = sp.Matrix([[v[0], v[1]]]) * M
    return (int(w[0]) % 2, int(w[1]) % 2)
for name, Mx in [("L", L), ("R", R), ("LR", A)]:
    print(name, {v: act(v, Mx) for v in par})

print("\n=== Lemma 11: Jacobi isotropy of the theta triplet ===")
mp.mp.dps = 30
def thetas(t):
    q = mp.exp(1j * mp.pi * t)
    return mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
def eta(t):
    q = mp.exp(2j * mp.pi * t)
    return mp.exp(2j * mp.pi * t / 24) * mp.nprod(lambda n: 1 - q**n, [1, mp.inf])
def rho_vec(t):
    t2, t3, t4 = thetas(t); e = eta(t)
    return [-t2**2 / (2*mp.pi*e**3), -t4**2 / (2*mp.pi*e**3), 1j * t3**2 / (2*mp.pi*e**3)]
for t in [mp.mpc(0.13, 1.21), mp.mpc(-0.3, 0.9), mp.mpc(0, 1), mp.exp(2j*mp.pi/3)]:
    r = rho_vec(t)
    print("tau =", mp.nstr(t, 6), " rho.rho =", mp.nstr(sum(c*c for c in r), 5), " |rho|^2 =", mp.nstr(sum(abs(c)**2 for c in r), 10))

print("\n=== Theorem 12(1): det Y(a) = (rho.rho)(a.a)(rho.a) as a polynomial identity ===")
a1, a2, a3, r1, r2, r3 = sp.symbols('a1 a2 a3 r1 r2 r3')
av = sp.Matrix([a1, a2, a3]); rv = sp.Matrix([r1, r2, r3])
Y = av * rv.T + rv * av.T - (av.dot(rv)) * sp.eye(3)
print("det Y - (rho.rho)(a.a)(rho.a) =", sp.expand(Y.det() - rv.dot(rv) * av.dot(av) * rv.dot(av)))
print("Y rho (general rho) =", sp.simplify(Y * rv - (rv.dot(rv)) * av).T, " = (rho.rho) a  -> vanishes iff rho isotropic")

print("\n=== Theorem 12(2): singular value identities for real a, isotropic rho ===")
rng = np.random.default_rng(1)
for trial in range(5):
    # random isotropic complex rho: u + i v with |u|=|v|, u.v=0
    u = rng.normal(size=3); v = rng.normal(size=3); v -= v.dot(u)/u.dot(u)*u; v *= np.linalg.norm(u)/np.linalg.norm(v)
    rho = u + 1j*v; aa = rng.normal(size=3)
    Yn = np.outer(aa, rho) + np.outer(rho, aa) - (aa @ rho) * np.eye(3)
    s = np.linalg.svd(Yn, compute_uv=False)
    n2 = (np.abs(rho)**2).sum() * (aa**2).sum()
    kappa = 2*abs(aa @ rho)**2 / n2
    xi = np.roots([1, -(4 + kappa), 4]); m2 = min(xi)/max(xi)
    print(f"s=({s[0]:.4f},{s[1]:.4f},{s[2]:.1e}) s1*s2/(|rho|^2|a|^2)={s[0]*s[1]/n2:.6f} (s1^2+s2^2)/(|rho|^2|a|^2)-2={ (s[0]**2+s[1]**2)/n2 - 2:.6f} |a.rho|^2/(|rho|^2|a|^2)={abs(aa@rho)**2/n2:.6f}  m={s[1]/s[0]:.6f} vs sqrt(xi-/xi+)={np.sqrt(m2):.6f}  kappa={kappa:.4f}")

print("\n=== Theorem 20: the joint law ===")
s0, s1, s2, s3, m0, m1, m2, m3 = sp.symbols('s0 s1 s2 s3 m0 m1 m2 m3')
S = sp.Matrix([[s0, s1], [s2, s3]]); Mm = sp.Matrix([[m0, m1], [m2, m3]])
eps = sp.Matrix([[0, 1], [-1, 0]])
C1 = eps; C2 = sp.diag(sp.I, -sp.I); C3 = sp.diag(sp.I, -sp.I) * eps
Cs = [C1, C2, C3]
def Yjoint(S, M):
    Y = sp.zeros(3, 3)
    for ia in range(3):
        for ib in range(3):
            K = Cs[ia].T * eps * S * Cs[ib]
            Y[ia, ib] = sum(K[i, j] * M[i, j] for i in range(2) for j in range(2))
    return Y
Yj = Yjoint(S, Mm)
detS = S.det(); detM = Mm.det(); pairing = (eps * S * Mm.T).trace()
print("det Y - 4 det S det M tr(eps S M^T) =", sp.expand(Yj.det() - 4 * detS * detM * pairing))
P = sp.diag(1, -1, -1)
def Aq(M):
    m0, m1, m2, m3 = M[0,0], M[0,1], M[1,0], M[1,1]
    return sp.Matrix([
        [m0**2 + m1**2 + m2**2 + m3**2, 2*sp.I*(m0*m2 + m1*m3), -sp.I*(m0**2 + m1**2 - m2**2 - m3**2)],
        [2*sp.I*(m0*m1 + m2*m3), -4*m1*m2, 2*(m0*m1 - m2*m3)],
        [-sp.I*(m0**2 - m1**2 + m2**2 - m3**2), 2*(m0*m2 - m1*m3), -m0**2 + m1**2 + m2**2 - m3**2]])
adjY = Yj.adjugate()
diff = sp.expand(adjY - (detS * Aq(Mm) + detM * P * Aq(S)))
print("adj Y - (det S A(M) + det M P A(S)) =", diff.tolist())
# try the transpose variant to see if the stated form (or its transpose) holds
diffT = sp.expand(adjY.T - (detS * Aq(Mm) + detM * P * Aq(S)))
print("transpose variant residual zero?", diffT == sp.zeros(3,3))
# symmetric form: Y(S, N eps^-1) = Y(N, S eps^-1) with N = M eps
N = Mm * eps
print("symmetric form holds:", sp.expand(Yjoint(S, N * eps.inv()) - Yjoint(N, S * eps.inv())) == sp.zeros(3, 3))
polar = ((S + N).det() - S.det() - N.det())
print("det Y + 4 det S det N polar(S,N) =", sp.expand(Yj.det() + 4 * S.det() * N.det() * polar))
print("tr(eps S M^T) + polar(S,N) =", sp.expand(pairing + polar))
# rank-one M = p q^T: adj Y = det S * A(M); check A(pq^T) is rank one & its norm relation ||A|| = 2||M||^2
p1, p2, q1, q2 = sp.symbols('p1 p2 q1 q2')
Mn = sp.Matrix([p1, p2]) * sp.Matrix([q1, q2]).T
An = sp.simplify(Aq(Mn))
print("rank of A(pq^T):", An.rank(), " det M (null):", sp.simplify(Mn.det()))
Mnum = np.array([[0.3+0.2j, -1.1], [0.7, 0.4j]]) ; Mnum = np.outer(Mnum[:,0], Mnum[0,:])  # a rank-one numeric matrix
An_num = np.array(sp.N(Aq(sp.Matrix(Mnum))).tolist(), dtype=complex)
print("||A(M)||_F =", np.linalg.norm(An_num), " 2||M||_F^2 =", 2*np.linalg.norm(Mnum)**2)
# item 3: at the coincident point N = S the masses are geometric, m1 m3 = m2^2
Snum = np.array([[0.4+0.9j, -1.2+0.1j], [0.33-0.7j, 1.1+0.2j]])
epsn = np.array([[0, 1], [-1, 0]], dtype=complex)
Mcoinc = Snum @ np.linalg.inv(epsn)   # N = M eps = S  =>  M = S eps^-1
Ynum = np.array(sp.N(Yjoint(sp.Matrix(Snum), sp.Matrix(Mcoinc))).tolist(), dtype=complex)
sv = np.linalg.svd(Ynum, compute_uv=False)
print("singular values at N=S:", sv, " m1*m3 - m2^2 =", sv[0]*sv[2] - sv[1]**2)
# cubic coefficients e1,e2,e3
Mrand = np.array([[0.5-0.3j, 0.8], [-0.2j, 1.3+0.4j]])
Ynum = np.array(sp.N(Yjoint(sp.Matrix(Snum), sp.Matrix(Mrand))).tolist(), dtype=complex)
sv = np.linalg.svd(Ynum, compute_uv=False)
e1 = np.linalg.norm(Ynum)**2
adjn = np.array(sp.N(Yjoint(sp.Matrix(Snum), sp.Matrix(Mrand)).adjugate()).tolist(), dtype=complex)
e2 = np.linalg.norm(adjn)**2
e3 = abs(np.linalg.det(Ynum))**2
print("roots of x^3 - e1 x^2 + e2 x - e3:", np.sort(np.roots([1, -e1, e2, -e3]).real), " vs squared singular values:", np.sort(sv**2))
# Gram spectrum of S -> Y(S,M) for null M: {1,2,2,4}||M||^2
pv = np.array([0.6+0.1j, -0.9]); qv = np.array([1.2j, 0.4-0.5j]); Mnull = np.outer(pv, qv)
G = np.zeros((4, 4), dtype=complex)
basis = [np.array([[1,0],[0,0]]), np.array([[0,1],[0,0]]), np.array([[0,0],[1,0]]), np.array([[0,0],[0,1]])]
cols = [np.array(sp.N(Yjoint(sp.Matrix(E.astype(complex)), sp.Matrix(Mnull))).tolist(), dtype=complex).reshape(-1) for E in basis]
Cmat = np.array(cols).T
G = Cmat.conj().T @ Cmat
print("Gram eigenvalues / ||M||^2:", np.sort(np.linalg.eigvalsh(G)) / np.linalg.norm(Mnull)**2)

print("\n=== Proposition 13: sum_r rho_r^2 wp(z_r) = 0 with wp at the half periods ===")
def wp_and_consts(t):
    q = mp.exp(1j*mp.pi*t)
    # Weierstrass wp for lattice (1, tau) via -(log theta1)'' with the standard constant:
    # wp(z) = -d^2/dz^2 log theta1(pi z, q) * pi^2 + c ,  c = (pi^2/3) * theta1'''(0)/theta1'(0)  ... use known: c = -(pi^2/3) * (theta1'''/theta1')? compute numerically from Laurent expansion instead
    def lt1(z): return mp.log(mp.jtheta(1, mp.pi*z, q))
    def wp_raw(z): return -mp.diff(lt1, z, 2)
    # fix constant by requiring wp(z) - 1/z^2 -> 0 as z -> 0
    z0 = mp.mpf('1e-3')
    c = -(wp_raw(z0) - 1/z0**2)   # error O(z0^2)
    z0b = mp.mpf('5e-4'); cb = -(wp_raw(z0b) - 1/z0b**2)
    c = (4*cb - c)/3  # Richardson
    return (lambda z: wp_raw(z) + c)
for t in [mp.mpc(0.13, 1.21), mp.mpc(-0.3, 0.9), mp.mpc(0.2, 1.5)]:
    wp = wp_and_consts(t)
    t2, t3, t4 = thetas(t)
    e_half = wp(mp.mpf(1)/2); e_tau = wp(t/2); e_mix = wp((1+t)/2)
    # standard half-period values for lattice (1,tau)
    E1 = mp.pi**2/3*(t3**4 + t4**4); E2 = -mp.pi**2/3*(t2**4 + t3**4); E3 = mp.pi**2/3*(t2**4 - t4**4)
    print("tau=", mp.nstr(t,5), " wp(1/2)-(pi^2/3)(t3^4+t4^4)=", mp.nstr(e_half - E1, 3), " wp(tau/2)+(pi^2/3)(t2^4+t3^4)=", mp.nstr(e_tau - E2, 3), " wp((1+tau)/2)-(pi^2/3)(t2^4-t4^4)=", mp.nstr(e_mix - E3, 3))
    r = rho_vec(t)
    s_paper = r[0]**2 * e_half + r[1]**2 * e_tau + r[2]**2 * e_mix
    s_swap = r[1]**2 * e_half + r[0]**2 * e_tau + r[2]**2 * e_mix   # i<->j swapped
    s_other = r[0]**2 * e_mix + r[1]**2 * e_tau + r[2]**2 * e_half
    print("   paper's assignment:", mp.nstr(s_paper, 3), "  i<->j swapped:", mp.nstr(s_swap, 3), "  another:", mp.nstr(s_other, 3))
