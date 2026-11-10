"""B1866 -- the agy lane's relay on the register-to-field join (P-753), scrutinised with main's own code.

Nothing of the lane's is run or imported. Each part computes, from main's own objects or from standard definitions, one
claim the relay makes. Data-free: integers, roots of unity, theta constants; no measured number.

Part 1  the moves on the four sign characters of the torus and on its four spin structures (exact, integers mod 2);
        the two coherent lifts of the physical lane's own formula give ONE unordered pair of lines.
Part 2  the E8 lattice: (-1 in Spin(10)) and (-1 in SU(4)) are the same element of E8 (exact, the 240 roots).
Part 3  main's triplet T (B1610's matrices): its group, its centre, its projective image, the braid element, and the
        census of all 24 twists of the symmetric square of the level-2 doublet.
Part 4  the vector (theta_2^2, theta_3^2, theta_4^2)/eta^3: its two transformation matrices, fitted from the functions
        themselves, against T.
"""
import cmath
import importlib.util
import itertools
import math
import pathlib

import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
out = []
say = out.append

# ------------------------------------------------------------------ Part 1: characters and spin structures
Lm, Rm = ((1, 1), (0, 1)), ((1, 0), (1, 1))                      # the moves on H_1 = Z^2, column vectors
def mat2(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 2 for j in range(2)) for i in range(2))
def inv2(A): return ((A[1][1] % 2, (-A[0][1]) % 2), ((-A[1][0]) % 2, A[0][0] % 2))
G2 = {((1, 0), (0, 1))}
frontier = list(G2)
while frontier:
    nxt = []
    for g in frontier:
        for h in (tuple(tuple(x % 2 for x in r) for r in Lm), tuple(tuple(x % 2 for x in r) for r in Rm)):
            k = mat2(g, h)
            if k not in G2:
                G2.add(k); nxt.append(k)
    frontier = nxt
assert len(G2) == 6                                                # SL(2, Z/2) = S_3
# a sign character chi_(p,q): chi(a) = (-1)^p, chi(b) = (-1)^q; a mapping class g pulls it back to (p, q) g
def pull(pq, g): return ((pq[0] * g[0][0] + pq[1] * g[1][0]) % 2, (pq[0] * g[0][1] + pq[1] * g[1][1]) % 2)
orbits = {}
for pq in itertools.product((0, 1), repeat=2):
    orbits[pq] = sorted({pull(pq, g) for g in G2})
say("Part 1. the moves on the four sign characters chi_(p,q) of the torus:")
say("  orbits: %s" % sorted({tuple(v) for v in orbits.values()}))
stab11 = [g for g in G2 if pull((1, 1), g) == (1, 1)]
say("  the stabiliser of chi_(1,1) in SL(2, Z/2) has order %d, index %d" % (len(stab11), 6 // len(stab11)))
Smod = ((0, 1), (1, 0))                                            # S = [[0,-1],[1,0]] mod 2
L2 = mat2(tuple(tuple(x % 2 for x in r) for r in Lm), tuple(tuple(x % 2 for x in r) for r in Lm))
say("  S fixes chi_(1,1): %s; L^2 fixes it: %s; L alone fixes it: %s; R alone fixes it: %s" % (
    pull((1, 1), Smod) == (1, 1), pull((1, 1), L2) == (1, 1), pull((1, 1), tuple(tuple(x % 2 for x in r) for r in Lm)) == (1, 1),
    pull((1, 1), tuple(tuple(x % 2 for x in r) for r in Rm)) == (1, 1)))
assert sorted({tuple(v) for v in orbits.values()}) == [((0, 0),), ((0, 1), (1, 0), (1, 1))] and len(stab11) == 2
# spin structures = quadratic refinements q of the intersection form on H_1(T; Z/2): q(x + y) = q(x) + q(y) + x.y
vecs = list(itertools.product((0, 1), repeat=2))
def qval(qa, qb, x): return (x[0] * qa + x[1] * qb + x[0] * x[1]) % 2          # q(x a + y b) = x q(a) + y q(b) + x y
def act(g, x): return ((g[0][0] * x[0] + g[0][1] * x[1]) % 2, (g[1][0] * x[0] + g[1][1] * x[1]) % 2)
def push(q, g):                                                    # (g.q)(x) = q(g^-1 x)
    gi = inv2(g)
    a, b = act(gi, (1, 0)), act(gi, (0, 1))
    return (qval(q[0], q[1], a), qval(q[0], q[1], b))
arf = lambda q: (q[0] * q[1]) % 2
spin_orbits = sorted({tuple(sorted({push(q, g) for g in G2})) for q in vecs})
say("  the four spin structures (q(a), q(b)), Arf = q(a) q(b): orbits %s" % spin_orbits)
say("  the odd one (1, 1), Arf 1, is fixed by every move: %s; the three even ones are one orbit: %s" % (
    all(push((1, 1), g) == (1, 1) for g in G2), ((0, 0), (0, 1), (1, 0)) in spin_orbits))
assert spin_orbits == [((0, 0), (0, 1), (1, 0)), ((1, 1),)] and all(arf(push(q, g)) == arf(q) for q in vecs for g in G2)
# the physical lane's own formula (its equation (2)): L_+ at (alpha chi_R(a), alpha chi_R(b)), L_- at (-alpha chi_R(a), -alpha chi_R(b)),
# with alpha^2 = 1 for the coherent lifts. As sign characters, with chi_R trivial (the singlet coefficient):
def lines(alpha): return {(0, 0) if alpha == 1 else (1, 1), (1, 1) if alpha == 1 else (0, 0)}
say("  the unordered pair of lines {L_+, L_-} at alpha = +1: %s; at alpha = -1: %s; the same pair: %s" % (
    sorted(lines(1)), sorted(lines(-1)), lines(1) == lines(-1)))
pairs_orbit = sorted({tuple(sorted({pull(c, g) for c in lines(1)})) for g in G2})
say("  that pair under the moves: %d pairs, %s" % (len(pairs_orbit), pairs_orbit))
assert lines(1) == lines(-1) and len(pairs_orbit) == 3
say("  => for either lift one line is trivial and one sits at chi_(1,1); the moves carry it to three backgrounds. Neither lift is kept by every move.")

# ------------------------------------------------------------------ Part 2: E8
roots = []
for i, j in itertools.combinations(range(8), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        v = [0] * 8; v[i], v[j] = si, sj; roots.append(tuple(v))
half = [tuple(s) for s in itertools.product((1, -1), repeat=8) if sum(1 for x in s if x == -1) % 2 == 0]
assert len(roots) == 112 and len(half) == 128
def cls(v, spinor):
    if spinor: return "(16,4)+(16bar,4bar)"
    idx = [k for k in range(8) if v[k] != 0]
    return "(45,1)" if max(idx) <= 4 else ("(1,15)" if min(idx) >= 5 else "(10,6)")
count = {}
for v in roots: count[cls(v, False)] = count.get(cls(v, False), 0) + 1
count["(16,4)+(16bar,4bar)"] = len(half)
th5, th3 = (1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0)       # -1 in Spin(10) (D5 on coordinates 1..5); -1 in SU(4) = Spin(6) (D3 on 6..8)
def phase(theta, v, spinor): return (-1) ** (sum(t * x for t, x in zip(theta, v)) if spinor else 2 * sum(t * x for t, x in zip(theta, v)))
same = all(phase(th5, v, False) == phase(th3, v, False) for v in roots) and all(phase(th5, v, True) == phase(th3, v, True) for v in half)
minus = {c: set() for c in count}
for v in roots: minus[cls(v, False)].add(phase(th5, v, False))
minus["(16,4)+(16bar,4bar)"] = {phase(th5, v, True) for v in half}
say("Part 2. E8's 240 roots under D5 x D3: %s" % ", ".join("%s %d" % kv for kv in sorted(count.items())))
say("  -1 in Spin(10) acts on them by %s" % ", ".join("%s: %s" % (k, sorted(v)) for k, v in sorted(minus.items())))
say("  -1 in SU(4) acts by the same sign on every root: %s  => the two are one element of E8; flipping the sign of an SU(4) central lift is multiplying by the Spin(10) centre" % same)
assert same and sum(count.values()) == 240 and minus["(16,4)+(16bar,4bar)"] == {-1} and minus["(10,6)"] == {1}
say("  the lift's two eigenvalues on the 4 of SU(4): exp(3 pi i/4) on the singlet over exp(-pi i/4) on the triplet = %s, for either sign of the lift" % (
    "%+.0f" % (cmath.exp(3j * math.pi / 4) / cmath.exp(-1j * math.pi / 4)).real))

# ------------------------------------------------------------------ Part 3: main's triplet
spec = importlib.util.spec_from_file_location("hands", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
TB = H.PIECES["T"]
TL, TR = TB.conj().T @ H.W.ML @ TB, TB.conj().T @ H.W.MR @ TB
I3 = np.eye(3, dtype=complex)
def key(M): return tuple(np.round(np.asarray(M).flatten(), 7).view(float))
def group(gens, n, cap=5000):
    I = np.eye(n, dtype=complex); seen = {key(I): I}; fr = [I]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = a @ g; k = key(x)
                if k not in seen:
                    seen[k] = x; nx.append(x)
                    if len(seen) > cap: return None
        fr = nx
    return list(seen.values())
def is_scalar(M): return abs(abs(np.trace(M)) - M.shape[0]) < 1e-8 and np.abs(M - M[0, 0] * np.eye(M.shape[0])).max() < 1e-8
GT = group([TL, TR], 3)
centre = [g for g in GT if is_scalar(g)]
def proj_order(g):
    x = np.eye(g.shape[0], dtype=complex)
    for k in range(1, 200):
        x = x @ g
        if is_scalar(x): return k
proj = {}
for g in GT:                                                       # classes modulo scalars
    k = key(g / g.flat[np.flatnonzero(np.abs(g.flatten()) > 1e-6)[0]])
    proj.setdefault(k, proj_order(g))
profile = sorted((o, list(proj.values()).count(o)) for o in set(proj.values()))
say("Part 3. main's triplet T (B1610's construction): the two moves generate a group of order %d; its scalars: %d, as %s; modulo scalars %d, with element orders %s" % (
    len(GT), len(centre), sorted({int(round(cmath.phase(g[0, 0]) / (math.pi / 2))) % 4 for g in centre}), len(proj), profile))
assert len(GT) == 96 and len(centre) == 4 and len(proj) == 24 and profile == [(1, 1), (2, 9), (3, 8), (4, 6)]      # S_4's profile
S1, S2 = TL @ np.linalg.inv(TR) @ TL, np.linalg.inv(TR) @ TL @ np.linalg.inv(TR)
p = lambda M, k: np.linalg.matrix_power(M, k)
say("  the braid relation L R^-1 L = R^-1 L R^-1 holds on T: %s" % (np.abs(S1 - S2).max() < 1e-10))
say("  S_T = T_L T_R^-1 T_L: S_T^2 = %s; S_T^4 = %s; S_T^8 = %s" % tuple(
    ("%+.0f%+.0fi times 1" % (p(S1, k)[0, 0].real, p(S1, k)[0, 0].imag)) if is_scalar(p(S1, k)) else "not a scalar" for k in (2, 4, 8)))
assert np.abs(S1 - S2).max() < 1e-10 and np.abs(p(S1, 4) + I3).max() < 1e-10 and np.abs(p(S1, 8) - I3).max() < 1e-10
say("  => S_T^4 = -1 while S^4 = 1 in SL(2, Z): T is a module of the double cover and does not factor through SL(2, Z)")
# the level-2 doublet and its symmetric square, with all 24 twists chi_m: L -> zeta_24^m, R -> zeta_24^-m
Hd = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
DL, DR = np.diag([1, 1j]), Hd @ np.diag([1, -1j]) @ Hd
def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]; r2 = math.sqrt(2)
    return np.array([[a * a, r2 * a * b, b * b], [r2 * a * c, a * d + b * c, r2 * b * d], [c * c, r2 * c * d, d * d]])
GD = group([DL, DR], 2)
SD = DL @ np.linalg.inv(DR) @ DL
say("  the doublet D (L -> diag(1, i), R = H diag(1, -i) H): group of order %d; braid relation %s; S_D^4 = %s, S_D^8 = %s" % (
    len(GD), np.abs(SD - np.linalg.inv(DR) @ DL @ np.linalg.inv(DR)).max() < 1e-10,
    "+1" if np.abs(p(SD, 4) - np.eye(2)).max() < 1e-10 else ("-1" if np.abs(p(SD, 4) + np.eye(2)).max() < 1e-10 else "other"),
    "+1" if np.abs(p(SD, 8) - np.eye(2)).max() < 1e-10 else "other"))
z24 = cmath.exp(2j * math.pi / 24)
def equivalent(AL, AR, BL, BR):
    """are the representations L -> AL, R -> AR and L -> BL, R -> BR equivalent? by characters over the group of pairs"""
    seen = {key(np.concatenate([I3.flatten(), I3.flatten()])): (I3, I3)}; fr = [(I3, I3)]
    while fr:
        nx = []
        for a in fr:
            for g in ((AL, BL), (AR, BR)):
                x = (a[0] @ g[0], a[1] @ g[1]); k = key(np.concatenate([x[0].flatten(), x[1].flatten()]))
                if k not in seen:
                    seen[k] = x; nx.append(x)
                    if len(seen) > 3000: return False, None
        fr = nx
    worst = max(abs(np.trace(a) - np.trace(b)) for a, b in seen.values())
    return worst < 1e-9, len(seen)
census = {}
for name, (XL, XR) in (("Sym2(D)", (sym2(DL), sym2(DR))), ("Sym2(conj D)", (sym2(DL.conj()), sym2(DR.conj())))):
    for m in range(24):
        AL, AR = z24 ** m * XL, z24 ** (-m) * XR
        G = group([AL, AR], 3)
        eqT, _ = equivalent(TL, TR, AL, AR)
        eqTb, _ = equivalent(TL.conj(), TR.conj(), AL, AR)
        census[(name, m)] = (len(G) if G else None, eqT, eqTb)
for name in ("Sym2(D)", "Sym2(conj D)"):
    say("  %s twisted by chi_m, m = 0..23: group orders %s" % (name, [census[(name, m)][0] for m in range(24)]))
    say("     equivalent to T at m = %s; to conj T at m = %s" % ([m for m in range(24) if census[(name, m)][1]], [m for m in range(24) if census[(name, m)][2]]))
even_orders = sorted({census[(n, m)][0] for n in ("Sym2(D)", "Sym2(conj D)") for m in range(0, 24, 2)})
odd96 = sorted({(n, m) for (n, m), v in census.items() if v[0] == 96})
say("  over the even twists the orders are %s: never 96. The untwisted symmetric square has order %d." % (even_orders, census[("Sym2(D)", 0)][0]))
say("  every twist equivalent to T or to conj T is odd: %s" % all(m % 2 == 1 for (n, m), v in census.items() if v[1] or v[2]))
assert 96 not in even_orders and all(m % 2 == 1 for (n, m), v in census.items() if v[1] or v[2])
assert any(v[1] for v in census.values()) and any(v[2] for v in census.values())
# a symmetric square over the braid group all the same: t D with t^2 the odd twist; t D is a module of the fourfold cover, not of the double cover
mT = [m for m in range(24) if census[("Sym2(D)", m)][1]]
t = cmath.exp(2j * math.pi * mT[0] / 48)
eq, n = equivalent(TL, TR, sym2(t * DL), sym2(DR / t))
StD = (t * DL) @ np.linalg.inv(DR / t) @ (t * DL)
say("  with t = zeta_48^%d (t^2 = chi_%d on L): T is equivalent to Sym2(t D): %s (pairs: %d); (t D)(S)^8 = %s, (t D)(S)^16 = %s" % (
    mT[0], mT[0], eq, n, "+1" if np.abs(p(StD, 8) - np.eye(2)).max() < 1e-9 else ("-1" if np.abs(p(StD, 8) + np.eye(2)).max() < 1e-9 else "other"),
    "+1" if np.abs(p(StD, 16) - np.eye(2)).max() < 1e-9 else "other"))
assert eq
say("  => T is a twist, by an odd character, of the symmetric square of the level-2 doublet. It is the symmetric square of a doublet of the braid group")
say("     (a module of a further double cover), and of no 2-dimensional module of the double cover of SL(2, Z).")

# ------------------------------------------------------------------ Part 4: the theta vector
mp.mp.dps = 30
def V(tau):
    """the series themselves, each prefactor an explicit function of tau: a library's q^(1/4) takes the principal branch of
    the nome, which jumps when tau is moved by 1"""
    e = lambda x: mp.exp(mp.pi * 1j * tau * x)
    th2 = 2 * e(mp.mpf(1) / 4) * mp.nsum(lambda n: e(n * (n + 1)), [0, mp.inf])
    th3 = 1 + 2 * mp.nsum(lambda n: e(n * n), [1, mp.inf])
    th4 = 1 + 2 * mp.nsum(lambda n: (-1) ** int(n) * e(n * n), [1, mp.inf])
    eta = e(mp.mpf(1) / 12) * mp.nprod(lambda n: 1 - e(2 * n), [1, mp.inf])
    return np.array([complex(th2 ** 2 / eta ** 3), complex(th3 ** 2 / eta ** 3), complex(th4 ** 2 / eta ** 3)])
taus = [mp.mpc(0.13, 0.9), mp.mpc(-0.21, 1.1), mp.mpc(0.37, 0.8)]
def fit(image, weight):
    """the matrix M with V(image(tau)) = weight(tau) M V(tau), from three sample points"""
    A = np.array([V(t) for t in taus]).T                           # columns V(tau_k)
    B = np.array([np.array(V(image(t))) / complex(weight(t)) for t in taus]).T
    return B @ np.linalg.inv(A)
ML = fit(lambda t: t + 1, lambda t: 1)
MR = fit(lambda t: t / (t + 1), lambda t: (t + 1) ** mp.mpf(-0.5))
check_tau = mp.mpc(0.05, 1.3)
resid = max(np.abs(V(check_tau + 1) - ML @ V(check_tau)).max(), np.abs(V(check_tau / (check_tau + 1)) - complex((check_tau + 1) ** mp.mpf(-0.5)) * (MR @ V(check_tau))).max())
def show(M):                                                       # entries as eighth roots of unity, e(k/8) = exp(2 pi i k/8): integers only in the output
    def ent(z):
        if abs(z) < 1e-9: return "0"
        k = round(8 * cmath.phase(z) / (2 * math.pi))
        assert abs(z - cmath.exp(2j * math.pi * k / 8)) < 1e-9
        return "e(%+d/8)" % k
    return "[" + "; ".join(" ".join(ent(z) for z in row) for row in M) + "]"
say("Part 4. V = (theta_2^2, theta_3^2, theta_4^2)/eta^3, weight -1/2: V(tau + 1) = M_L V(tau), V(tau/(tau + 1)) = (tau + 1)^(-1/2) M_R V(tau)")
say("  M_L = %s, M_R = %s   (e(x) = exp(2 pi i x); the fit holds at a fourth point to better than 1e-12: %s)" % (show(ML), show(MR), resid < 1e-12))
mono = all(sum(1 for z in row if abs(z) > 1e-9) == 1 for M in (ML, MR) for row in M) and all(abs(abs(z) - 1) < 1e-9 for M in (ML, MR) for z in M.flatten() if abs(z) > 1e-9)
say("  both are monomial with entries eighth roots of unity: %s" % (mono and all(abs((z ** 8) - 1) < 1e-8 for M in (ML, MR) for z in M.flatten() if abs(z) > 1e-9)))
variants = {}
for nm, (a, b) in (("(M_L, M_R)", (ML, MR)), ("conjugates", (ML.conj(), MR.conj())), ("inverse transposes", (np.linalg.inv(ML).T, np.linalg.inv(MR).T))):
    for sgn in (1, -1):
        variants[(nm, sgn)] = (equivalent(TL, TR, a, sgn * b)[0], equivalent(TL.conj(), TR.conj(), a, sgn * b)[0])
say("  as a representation L -> a, R -> +-b: equivalent to T for %s; to conj T for %s" % (
    [k for k, v in variants.items() if v[0]], [k for k, v in variants.items() if v[1]]))
assert resid < 1e-12 and mono and any(v[0] or v[1] for v in variants.values())

# ------------------------------------------------------------------ Part 5: the triplets induced over the three backgrounds
# The relay induces a line from the stabiliser of one background (index 3) to all the moves, for a character psi of the stabiliser
# given by its signs on L^2 and on S. That is abstract algebra and is computed here; WHICH mode of the lanes' operator carries which
# character is the lanes' analysis and is not checked.
N8 = 8
def m8(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % N8 for j in range(2)) for i in range(2))
def inv8(A): return ((A[1][1] % N8, (-A[0][1]) % N8), ((-A[1][0]) % N8, A[0][0] % N8))
L8, R8 = ((1, 1), (0, 1)), ((1, 0), (1, 1))
S8 = m8(m8(L8, inv8(R8)), L8)                                      # L R^-1 L = [[0, 1], [-1, 0]]
L2_8 = m8(L8, L8)
I8 = ((1, 0), (0, 1))
def induced(e1, e2):
    """Ind of psi (psi(L^2) = e1, psi(S) = e2) from the stabiliser of chi_(1,1) to the group of the moves, as 3 x 3 monomial matrices"""
    psi = {I8: 1}; fr = [I8]                                       # psi on the stabiliser's image mod 8, by a search over words in L^2, S
    while fr:
        nx = []
        for h in fr:
            for g, e in ((L2_8, e1), (S8, e2), (inv8(L2_8), e1), (inv8(S8), e2)):
                k = m8(h, g); v = psi[h] * e
                if k in psi:
                    if psi[k] != v: return None                    # psi is not a character of the stabiliser mod 8
                else:
                    psi[k] = v; nx.append(k)
        fr = nx
    reps = {(1, 1): I8, (1, 0): L8, (0, 1): R8}                    # chi_(1,1) g_c = c
    def red(g): return tuple(tuple(x % 2 for x in r) for r in g)
    assert all(pull((1, 1), red(g)) == c for c, g in reps.items())
    order3 = [(1, 1), (1, 0), (0, 1)]
    mats = []
    for x in (L8, R8):
        M = np.zeros((3, 3), dtype=complex)
        for i, c2 in enumerate(order3):
            c = pull(c2, red(x)); h = m8(m8(reps[c2], x), inv8(reps[c]))
            if h not in psi: return None
            M[i, order3.index(c)] = psi[h]
        mats.append(M)
    return mats
say("Part 5. a line induced from the stabiliser of one background (index 3) to all the moves, psi = (sign on L^2, sign on S):")
for e1, e2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
    r = induced(e1, e2)
    if r is None:
        say("  psi = (%+d, %+d): not a character of the stabiliser" % (e1, e2)); continue
    G = group(r, 3); pr = {}
    for g in G:
        pr.setdefault(key(g / g.flat[np.flatnonzero(np.abs(g.flatten()) > 1e-6)[0]]), 1)
    tw = [m for m in range(24) if equivalent(TL, TR, z24 ** m * r[0], z24 ** (-m) * r[1])[0]]
    twb = [m for m in range(24) if equivalent(TL.conj(), TR.conj(), z24 ** m * r[0], z24 ** (-m) * r[1])[0]]
    say("  psi = (%+d, %+d): a group of order %d, modulo scalars %d; equivalent to T after a twist chi_m for m = %s; to conj T for m = %s" % (e1, e2, len(G), len(pr), tw, twb))
# ------------------------------------------------------------------ Part 6: the physical lane's review of the same relay (added the same evening)
# Its findings F1, F4 and F5, checked here; and the orders of parts 3 and 5 recomputed in EXACT arithmetic (its F6 applies to any
# order read off rounded floating-point matrices, main's own among them).
# Exact monomial matrices with entries powers of zeta_24: (perm, exps) with M e_j = zeta_24^exps[j] e_perm[j].
def mmul(A, B): return (tuple(A[0][B[0][j]] for j in range(3)), tuple((B[1][j] + A[1][B[0][j]]) % 24 for j in range(3)))
def minv(A):
    perm = [0] * 3; exps = [0] * 3
    for j in range(3): perm[A[0][j]] = j; exps[A[0][j]] = (-A[1][j]) % 24
    return (tuple(perm), tuple(exps))
def mscal(k, A): return (A[0], tuple((e + k) % 24 for e in A[1]))
E3 = ((0, 1, 2), (0, 0, 0))
def mgroup(gens):
    seen = {E3}; fr = [E3]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = mmul(a, g)
                if x not in seen: seen.add(x); nx.append(x)
        fr = nx
    return seen
def mscalar(A): return A[0] == (0, 1, 2) and len(set(A[1])) == 1
# the triplet in its monomial form, from part 4: T_L = conj M_L, T_R = conj M_R; eighth roots are multiples of 3 in exponents mod 24
XL = ((0, 2, 1), (-3 % 24, 3, 3))                                  # e_1 -> e(-1/8) e_1, e_2 -> e(+1/8) e_3, e_3 -> e(+1/8) e_2
XR = ((1, 0, 2), (-3 % 24, -3 % 24, 3))                            # e_1 -> e(-1/8) e_2, e_2 -> e(-1/8) e_1, e_3 -> e(+1/8) e_3
def dense(A):
    M = np.zeros((3, 3), dtype=complex)
    for j in range(3): M[A[0][j], j] = z24 ** A[1][j]
    return M
assert np.abs(dense(XL) - ML.conj()).max() < 1e-9 and np.abs(dense(XR) - MR.conj()).max() < 1e-9 and equivalent(TL, TR, dense(XL), dense(XR))[0]
GX = mgroup([XL, XR])
SX = mmul(mmul(XL, minv(XR)), XL)
pw = lambda A, k: E3 if k == 0 else mmul(A, pw(A, k - 1))
exact_orders = [len(mgroup([mscal(k, XL), mscal(-k, XR)])) for k in range(24)]
say("Part 6. exact arithmetic (monomial matrices over the 24th roots): the triplet's group has order %d, %d scalars, %d modulo scalars; S^4 = -1: %s; S^8 = 1: %s" % (
    len(GX), sum(1 for g in GX if mscalar(g)), len({(g[0], tuple((e - g[1][0]) % 24 for e in g[1])) for g in GX}),
    pw(SX, 4) == ((0, 1, 2), (12, 12, 12)), pw(SX, 8) == E3))
say("  the orders of its 24 twists chi_k, exactly: %s; the twists with order 96 are k = %s, all even shifts of the triplet itself" % (exact_orders, [k for k in range(24) if exact_orders[k] == 96]))
numeric = [census[("Sym2(D)", m)][0] for m in range(24)]
say("  they are part 3's floating-point orders, shifted by the triplet's own twist 15: %s" % (numeric == [exact_orders[(m - 15) % 24] for m in range(24)]))
assert len(GX) == 96 and numeric == [exact_orders[(m - 15) % 24] for m in range(24)] and pw(SX, 4) == ((0, 1, 2), (12, 12, 12))
# F1: the agy lane's inserted one-form matrices, as the physical lane's review displays them: A_L = w T_L, A_R = w^-1 T_R, w = e(1/8)
AL, AR = mscal(3, XL), mscal(-3, XR)
# they are tied to what the review displays, not only to that formula: the entries its text shows are AL[2][3] = AL[3][2] = i and
# AR[1][2] = AR[2][1] = -i (rows, columns from 1); and its remark that diag(i, 1, i) conjugates both into real signed permutations of det 1
ent = lambda A, r, c: A[1][c - 1] if A[0][c - 1] == r - 1 else None       # the exponent of the entry in row r, column c, or None for 0
assert (ent(AL, 2, 3), ent(AL, 3, 2), ent(AR, 1, 2), ent(AR, 2, 1)) == (6, 6, 18, 18) and ent(AL, 3, 3) is None and ent(AR, 1, 1) is None
dg = (6, 0, 6)
cj = lambda A: (A[0], tuple((A[1][j] + dg[A[0][j]] - dg[j]) % 24 for j in range(3)))
def sdet(A):                                                       # determinant of a signed permutation matrix (exponents 0 or 12 only)
    inv = sum(1 for a in range(3) for b in range(a + 1, 3) if A[0][a] > A[0][b])
    return (-1) ** (inv + sum(1 for e_ in A[1] if e_ == 12))
real_signed = all(e_ in (0, 12) for A in (cj(AL), cj(AR)) for e_ in A[1])
say("  F1. the displayed matrices, conjugated by diag(i, 1, i), are real signed permutations: %s, of determinant %s; they generate a group of order %d (the rotations of the cube)" % (
    real_signed, [sdet(cj(AL)), sdet(cj(AR))], len(mgroup([cj(AL), cj(AR)]))))
assert real_signed and [sdet(cj(AL)), sdet(cj(AR))] == [1, 1] and len(mgroup([cj(AL), cj(AR)])) == 24
SA = mmul(mmul(AL, minv(AR)), AL)
fixed = [j for j in range(3) if SA[0][j] == j]
L2 = mmul(AL, AL)
say("  F1. the inserted one-form matrices A_L = e(1/8) T_L, A_R = e(-1/8) T_R: a group of order %d; S fixes branch %s with eigenvalue e(%d/24); L^2 acts on it by e(%d/24)" % (
    len(mgroup([AL, AR])), [j + 1 for j in fixed], SA[1][fixed[0]], L2[1][fixed[0]]))
say("      so on the fixed branch S = -1 and L^2 = -1: the signs are (-1, -1), not the (-1, +1) the relay states. Negating both matrices gives S = +1: %s" % (
    mmul(mmul(mscal(12, AL), minv(mscal(12, AR))), mscal(12, AL))[1][fixed[0]] == 0))
say("      the triplet is chi_21 times the displayed pair and chi_9 times the negated pair, exactly: %s, %s" % (
    (mscal(21, AL), mscal(-21, AR)) == (XL, XR), (mscal(9, mscal(12, AL)), mscal(-9, mscal(12, AR))) == (XL, XR)))
assert len(fixed) == 1 and SA[1][fixed[0]] == 12 and L2[1][fixed[0]] == 12 and (mscal(21, AL), mscal(-21, AR)) == (XL, XR)
# F5: the full kernel of Spin(10) x Spin(6) -> E8 has order 4: theta = (1/2)^8 pairs integrally with every root, and its double is the (-1, -1) element
from fractions import Fraction as Fq
th = [Fq(1, 2)] * 8
ok4 = all(sum(t_ * x for t_, x in zip(th, v)).denominator == 1 for v in roots) and all((sum(t_ * x for t_, x in zip(th, v)) / 2).denominator == 1 for v in half)
dbl = [2 * x for x in th]
same2 = all(phase(th5, v, False) * phase(th3, v, False) == 1 for v in roots) and all(phase(th5, v, True) * phase(th3, v, True) == 1 for v in half)
# its order: an element theta of the torus is the identity of Spin(10) x Spin(6) when each block (coordinates 1..5, 6..8) is an integer
# vector of even sum (the coroot lattices of D5 and D3)
def is_identity(v): return all(x.denominator == 1 for x in v) and sum(v[:5]) % 2 == 0 and sum(v[5:]) % 2 == 0
order = next(k for k in range(1, 9) if is_identity([k * x for x in th]))
sq_is_pair = is_identity([2 * x - a - b for x, a, b in zip(th, th5, th3)])          # 2 theta is the pair (-1 of Spin(10), -1 of SU(4)) of part 2
say("  F5. the element (1/2)^8 of the two centres acts trivially on all 240 roots: %s; its order in Spin(10) x Spin(6) is %d; its square is the pair (-1, -1) of part 2: %s, also trivial: %s  => the kernel contains a Z_4, not only that Z_2" % (ok4, order, sq_is_pair, same2))
assert ok4 and same2 and order == 4 and sq_is_pair
# F4: fixed points on the torus of flat U(1) characters (u, v) mod 1: under ALL moves, and under the stabiliser of one background (L^2 and S)
grid = [(Fq(a, 4), Fq(b, 4)) for a in range(4) for b in range(4)]                  # 2u = 0 or 4u = 0 is forced below, so quarters suffice
def actL(c): return (c[0], (c[1] + c[0]) % 1)                                    # chi o L on (a, b): a -> a, b -> a + b
def actR(c): return ((c[0] + c[1]) % 1, c[1])
def actS(c): return actL(actRinv(actL(c)))
def actRinv(c): return ((c[0] - c[1]) % 1, c[1])
all_fixed = [c for c in grid if actL(c) == c and actR(c) == c]
stab_fixed = [c for c in grid if actL(actL(c)) == c and actS(c) == c]
say("  F4. flat characters fixed by every move: %s; fixed by the stabiliser of one background alone (L^2 and S): %s" % (
    [tuple(str(x) for x in c) for c in all_fixed], [tuple(str(x) for x in c) for c in stab_fixed]))
say("      so 'kept by every move' singles out the trivial character, and on one background it does not: chi_(1,1) is fixed there too. Being kept is a fixed-point statement, not a selection.")
assert all_fixed == [(Fq(0), Fq(0))] and sorted(stab_fixed) == [(Fq(0), Fq(0)), (Fq(1, 2), Fq(1, 2))]
# the 6-dimensional space V = T + conj T itself (main's W.ML, W.MR)
GV = group([H.W.ML, H.W.MR], H.W.ML.shape[0])
say("  (the moves on main's whole 6-dimensional space: a group of order %d)" % len(GV))
assert len(GV) == 96
print("\n".join(out))
