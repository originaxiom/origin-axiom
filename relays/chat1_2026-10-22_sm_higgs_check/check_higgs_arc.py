#!/usr/bin/env python3
"""COMPUTED, no data: chat1's independent check of the core mathematics in the SM seat's Higgs arc (W128, W130 on the
seat's branch at 82cd8ab97), written from the textbook definitions, not from the seat's code.
  W130 H0  Hitchin's equation for the uniformizing bundle E = K^1/2 + K^-1/2, metric diag(y, 1/y) on the upper half
           plane (curvature -1), Phi = c N dz with N = [[0,0],[1,0]]: |c|^2 = 1/4, and |Phi| = |c| pointwise.
  W130 H3  with a constant (flat) metric the equation forces c = 0.
  W130 H2  the image of the once-punctured torus group <A, B> in PSL(2, Z/6) has order 12 (index 6, area 2 pi), so the
           parabolic degree is Area/(4 pi) = 1/2 and the integral of |Phi|^2 is Area/4 = pi/2.
  W130 H1  traces and commutator of the geometry's generators, the quaternion point, and the Markov images of
           (3, 3, 3) under the Vieta moves to depth 6 (every trace >= 3, tr[A, B] = -2).
  W130 H4  the square roots h of N under -h (x) eps(h, .), with eps(h, v) = b v1 - a v2.
  W128 C1  the hypercharge anomaly cubic after the linear conditions, and the Yukawa bilinears' hypercharges.
    python3 -B check_higgs_arc.py      # writes check_higgs_arc_run.txt"""
import itertools, pathlib
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
LOG = []


def say(s):
    LOG.append(s); print(s)


# --- W130 H0 and H3 ---
x, y = sp.symbols("x y", real=True, positive=True)
k = sp.symbols("k", nonnegative=True)                     # k = |c|^2
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)       # d_z d_zbar = Laplacian / 4
h = [y, 1 / y]                                            # metric on dz^(1/2), dz^(-1/2)
F = [sp.simplify(lap(sp.log(hi)) / 4) for hi in h]        # coefficient of dzbar ^ dz
N = sp.Matrix([[0, 0], [1, 0]])
H = sp.diag(*h)
Nstar = H.inv() * N.H * H                                 # adjoint with respect to h
comm = sp.simplify(k * (Nstar * N - N * Nstar))           # [Phi, Phi*] coefficient of dzbar ^ dz
eq = [sp.simplify(F[i] + comm[i, i]) for i in range(2)]
sol = sp.solve(eq[0], k)
say(f"H0: F = diag({F[0]}, {F[1]}); [Phi, Phi*] = diag({comm[0, 0]}, {comm[1, 1]}); Hitchin's equation holds iff |c|^2 = {sol}; off-diagonal terms {sp.simplify(comm[0, 1])}, {sp.simplify(comm[1, 0])}")
norm2 = sp.simplify(k * (N * Nstar).trace() * y**2)      # |Phi|^2 = |c|^2 tr(N N*) |dz|^2_g, |dz|^2_g = y^2
say(f"    |Phi|^2 pointwise = {norm2} -> |Phi| = {sp.sqrt(norm2.subs(k, sol[0]))}")
Fflat = [0, 0]
say(f"H3: with a constant metric F = 0, so k * diag(1, -1) * const = 0 forces |c|^2 = 0")

# --- W130 H2: the image of <A, B> in PSL(2, Z/6) ---
A = sp.Matrix([[1, 1], [1, 2]]); Bm = sp.Matrix([[1, -1], [-1, 2]])
def key(M):
    a = tuple(int(v) % 6 for v in M); b = tuple(int(-v) % 6 for v in M)
    return min(a, b)
gens = [A, Bm, A.inv(), Bm.inv()]
seen = {key(sp.eye(2))}; frontier = [sp.eye(2)]
while frontier:
    new = []
    for M in frontier:
        for g in gens:
            P = (M * g).applyfunc(lambda v: v % 6)
            kk = key(P)
            if kk not in seen:
                seen.add(kk); new.append(P)
    frontier = new
Ssl = [sp.Matrix(2, 2, list(t)) for t in itertools.product(range(6), repeat=4)]
psl6 = {key(M) for M in Ssl if (M.det() % 6) == 1}
say(f"H2: |PSL(2, Z/6)| = {len(psl6)}; the image of <A, B> has order {len(seen)}; index {len(psl6) // len(seen)}; "
    f"area = index x pi/3 = {sp.Rational(len(psl6), len(seen))}*pi/3; degree = area/(4 pi) = {sp.Rational(len(psl6), len(seen)) / 12}; "
    f"integral of |Phi|^2 = area/4 = {sp.Rational(len(psl6), len(seen)) * sp.pi / 12}")

# --- W130 H1 ---
C = A * Bm * A.inv() * Bm.inv()
say(f"H1: tr A = {A.trace()}, tr B = {Bm.trace()}, tr AB = {(A * Bm).trace()}; [A, B] = {C.tolist()}, trace {C.trace()}; "
    f"-[A, B] - I nilpotent: {((-C - sp.eye(2))**2).is_zero_matrix} and non-zero: {not (-C - sp.eye(2)).is_zero_matrix}")
QI = sp.Matrix([[sp.I, 0], [0, -sp.I]]); QJ = sp.Matrix([[0, 1], [-1, 0]])
Cq = QI * QJ * QI.inv() * QJ.inv()
say(f"    quaternion point: [a, b] = {Cq.tolist()}, unitary: {sp.simplify(QI * QI.H) == sp.eye(2) and sp.simplify(QJ * QJ.H) == sp.eye(2)}")
trip = {(3, 3, 3)}; layer = {(3, 3, 3)}
for _d in range(6):
    nxt = set()
    for (a, b, c) in layer:
        for t in ((b * c - a, b, c), (a, a * c - b, c), (a, b, a * b - c)):
            if t not in trip:
                nxt.add(t)
    trip |= nxt; layer = nxt
kappa = {a * a + b * b + c * c - a * b * c - 2 for (a, b, c) in trip}
say(f"    Markov images of (3, 3, 3) under the three Vieta moves to depth 6: {len(trip)} triples, least entry "
    f"{min(min(t) for t in trip)}, commutator traces {sorted(kappa)}")

# --- W130 H4 ---
a, b = sp.symbols("a b")
M = sp.Matrix([[-a * b, a**2], [-b**2, a * b]])            # -h (x) eps(h, .) with eps(h, v) = b v1 - a v2
roots = sp.solve(list(M - N), [a, b], dict=True)
say(f"H4: the square roots of N: {roots}")

# --- W128 C1 ---
yQ, yu = sp.symbols("y_Q y_u")
yd = -2 * yQ - yu; yL = -3 * yQ; ye = 6 * yQ                # SU(3)^2 U(1), SU(2)^2 U(1), grav^2 U(1)
cubic = sp.factor(6 * yQ**3 + 3 * yu**3 + 3 * yd**3 + 2 * yL**3 + ye**3)
say(f"W128 C1: after the linear conditions the cubic is {cubic}")
sm = {yQ: sp.Rational(1, 6), yu: sp.Rational(-2, 3)}
say(f"    at the Standard Model's y_Q = 1/6, y_u = -2/3: y_d = {yd.subs(sm)}, y_L = {yL.subs(sm)}, y_e = {ye.subs(sm)}; "
    f"the Higgs needed by Q u^c: {-(yQ + yu).subs(sm)}, by Q d^c: {-(yQ + yd).subs(sm)}, by L e^c: {-(yL + ye).subs(sm)}")
(HERE / "check_higgs_arc_run.txt").write_text("\n".join(LOG) + "\n")
