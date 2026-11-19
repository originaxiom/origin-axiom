"""The physical lane's native-register law probe (its note NATIVE_RATE_CONE_AND_PARITY_QUOTIENT.md at 60d8afc6f, a hand
derivation the lane marks not independently checked): its finite claims checked on main's own code, exactly (sympy).
Nothing of the lane's is run.
 R1  G, the proper signed permutations of three coordinates, has 24 elements, and its ordered-pair orbits on
     X6 = {+e_i, -e_i} are exactly three: equal, antipodal, perpendicular (sizes 6, 6, 24)
 R2  the 6 x 6 real matrices commuting with every permutation matrix of G form a space of dimension 3 (one value per
     pair orbit); with zero row sums, a 2-parameter family: L = a (antipode - id) + b (perpendicular - 4 id)
 R3  its spectrum, with multiplicities: 0 [1], -6b [2], -(2a + 4b) [3]; the even functions carry 0 and -6b, the odd ones
     -(2a + 4b)
 R4  the normalised correlations: C_signed(t) = exp(-(2a + 4b) t) and C_axis(t) = exp(-6 b t) (stationary uniform law)
 R5  R = (2a + 4b)/(6b) = (a + 2b)/(3b); a = b gives 1 and a = 2b gives 4/3
 R6  irreducible exactly when b > 0 (b = 0: the three axis pairs do not communicate)
 R7  the three-axis quotient is lumpable, and its generator (rate 2b to each other axis) does not depend on a
 R8  the group-jump implementation (its (12)): L = 6b (Pi - I) + (3/2)(a - b)(H - I), Pi the average over G, H over the three
     half turns about the coordinate axes
 R9  the quarter-turn control: the six quarter turns about the coordinate axes, each at rate r0, give L with a = 0, b = r0,
     so R = 2/3; the six-label set is closed under conjugation in G
 R10 L is symmetric, the uniform law is stationary, and exp(tL) has every entry positive when b > 0 (three rational points)
 R11 the stabiliser of a signed axis in G has order 4
 Controls: a matrix with a different rate on one perpendicular pair does not commute with G; the spectrum's
 multiplicities are not (1, 2, 3) for a G-breaking perturbation.
    python3 -B physical_rate_cone.py > physical_rate_cone_run.txt"""
import itertools
import sympy as sp

X = [(s, i) for i in range(3) for s in (1, -1)]                       # +e_i, -e_i
vec = lambda x: tuple(x[0] if k == x[1] else 0 for k in range(3))
G = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = sp.zeros(3)
        for r in range(3): M[r, perm[r]] = signs[r]
        if M.det() == 1: G.append(M)
act = lambda M, x: next(y for y in X if vec(y) == tuple(M * sp.Matrix(vec(x))))
orbits = {}
for x, y in itertools.product(X, X):
    key = frozenset((act(M, x), act(M, y)) for M in G); orbits.setdefault(key, set()).add((x, y))
kinds = sorted(len(v) for v in orbits.values())
print("R1: |G| = %d; ordered-pair orbits: %d, sizes %s (expected 6, 6, 24)" % (len(G), len(orbits), kinds))
P = [sp.Matrix(6, 6, lambda i, j: 1 if act(M, X[j]) == X[i] else 0) for M in G]
cs = sp.symbols("c0:36"); C = sp.Matrix(6, 6, cs)
eqs = [e for Q in P for e in (Q * C - C * Q)]
sol = sp.solve(eqs, cs, dict=True)[0]; Cg = C.subs(sol); free = sorted(Cg.free_symbols, key=str)
print("R2: the commutant of G has dimension %d" % len(free))
a, b, t = sp.symbols("a b t", nonnegative=True)
anti = sp.Matrix(6, 6, lambda i, j: 1 if X[i][1] == X[j][1] and X[i][0] == -X[j][0] else 0)
perp = sp.Matrix(6, 6, lambda i, j: 1 if X[i][1] != X[j][1] else 0)
L = a * (anti - sp.eye(6)) + b * (perp - 4 * sp.eye(6))
print("R2: L = a (antipode - id) + b (perpendicular - 4 id) commutes with G: %s; zero row sums: %s" % (
    all(sp.simplify(Q * L - L * Q) == sp.zeros(6) for Q in P), all(sp.simplify(sum(L.row(i))) == 0 for i in range(6))))
ev = L.eigenvals(); evs = {sp.simplify(k): v for k, v in ev.items()}
print("R3: spectrum %s (expected {0: 1, -6b: 2, -(2a + 4b): 3})" % evs)
even = [sp.Matrix([1 if X[i][1] == k else 0 for i in range(6)]) for k in range(3)]
odd = [sp.Matrix([X[i][0] if X[i][1] == k else 0 for i in range(6)]) for k in range(3)]
e_ok = all(sp.simplify(L * (even[0] - even[1]) + 6 * b * (even[0] - even[1])) == sp.zeros(6, 1) for _ in [0]) and sp.simplify(L * sum(even, sp.zeros(6, 1))) == sp.zeros(6, 1)
o_ok = all(sp.simplify(L * w + (2 * a + 4 * b) * w) == sp.zeros(6, 1) for w in odd)
print("R3: the even sum-zero plane has eigenvalue -6b and the constants 0: %s; the odd space -(2a + 4b): %s" % (e_ok, o_ok))
E = (L * t).exp()
f = [sp.Matrix([sp.Integer(vec(x)[k]) for x in X]) for k in range(3)]
g = [sp.Matrix([sp.Integer(1 if x[1] == k else 0) - sp.Rational(1, 3) for x in X]) for k in range(3)]
mu = sp.Rational(1, 6)
Cs = sp.simplify(sum((mu * (fk.T * E * fk))[0] for fk in f)); Ca = sp.simplify(sp.Rational(3, 2) * sum((mu * (gk.T * E * gk))[0] for gk in g))
print("R4: C_signed(t) = %s; C_axis(t) = %s" % (Cs, Ca))
print("R4: as stated: %s, %s" % (sp.simplify(Cs - sp.exp(-(2 * a + 4 * b) * t)) == 0, sp.simplify(Ca - sp.exp(-6 * b * t)) == 0))
Rr = sp.simplify((2 * a + 4 * b) / (6 * b))
print("R5: R = %s; at a = b: %s; at a = 2b: %s" % (Rr, sp.simplify(Rr.subs(a, b)), sp.simplify(Rr.subs(a, 2 * b))))
L0 = L.subs(b, 0); comp = lambda M: len([1 for i in range(6)])
reach = lambda M: (sp.eye(6) + M.applyfunc(lambda z: 1 if z != 0 else 0)) ** 6
print("R6: b = 0 connects +e_1 to +e_2: %s; b = 1, a = 0 connects all: %s" % (
    reach(L0.subs(a, 1))[0, 2] != 0, all(v != 0 for v in reach(L.subs({a: 0, b: 1})))))
Q3 = sp.Matrix(3, 6, lambda i, j: 1 if X[j][1] == i else 0)
lump = all(sp.simplify(sum(L[j, k] for k in range(6) if X[k][1] == m) - sum(L[j2, k] for k in range(6) if X[k][1] == m)) == 0
           for m in range(3) for j in range(6) for j2 in range(6) if X[j][1] == X[j2][1])
Lq = sp.Matrix(3, 3, lambda i, m: sum(L[next(j for j in range(6) if X[j][1] == i), k] for k in range(6) if X[k][1] == m))
print("R7: lumpable to the three axes: %s; quotient generator %s; depends on a: %s" % (lump, Lq.tolist(), a in Lq.free_symbols))
Lbad = L + sp.Matrix(6, 6, lambda i, j: 1 if (i, j) in ((0, 2), (2, 0)) else 0) - sp.Matrix(6, 6, lambda i, j: 1 if i == j and i in (0, 2) else 0)
evb = Lbad.subs({a: 1, b: 1}).eigenvals()
print("control: a changed rate on one perpendicular pair commutes with G: %s; its multiplicities at a = b = 1: %s" % (
    all(sp.simplify(Q * Lbad - Lbad * Q) == sp.zeros(6) for Q in P), sorted(evb.values())))
Pi = sum(P, sp.zeros(6)) / 24
half = [M for M in G if M != sp.eye(3) and (M * M) == sp.eye(3) and all(M[i, j] == 0 for i in range(3) for j in range(3) if i != j)]
Hh = sum((P[G.index(M)] for M in half), sp.zeros(6)) / 3
r8 = sp.simplify(6 * b * (Pi - sp.eye(6)) + sp.Rational(3, 2) * (a - b) * (Hh - sp.eye(6)) - L) == sp.zeros(6)
print("R8: three half turns about the axes: %d; L = 6b(Pi - I) + (3/2)(a - b)(H - I): %s" % (len(half), r8))
r0 = sp.symbols("r0", positive=True)
quarter = [M for M in G if (M ** 4) == sp.eye(3) and (M * M) != sp.eye(3) and any(M[i, i] != 0 for i in range(3))]
Lq4 = sum((r0 * (P[G.index(M)] - sp.eye(6)) for M in quarter), sp.zeros(6))
r9 = sp.simplify(Lq4 - L.subs({a: 0, b: r0})) == sp.zeros(6)
conj = all(any((g * M * g.inv()) == Q for Q in quarter) for M in quarter for g in G)
print("R9: quarter turns about the axes: %d; their generator is L(a = 0, b = r0): %s; R there %s; closed under conjugation: %s" % (
    len(quarter), r9, sp.simplify(Rr.subs(a, 0)), conj))
sym = L == L.T; stat = (sp.Matrix([[sp.Rational(1, 6)] * 6]) * L) == sp.zeros(1, 6)
pos = all(all(v > 0 for v in (L.subs({a: av, b: bv}) * tv).exp().evalf(30)) for av, bv, tv in ((1, 1, sp.Rational(1, 2)), (0, 1, sp.Rational(1, 3)), (3, sp.Rational(1, 5), 1)))
print("R10: L symmetric: %s; uniform stationary: %s; exp(tL) entrywise positive at three points with b > 0: %s" % (sym, stat, pos))
stab = [M for M in G if act(M, X[0]) == X[0]]
print("R11: the stabiliser of +e_1 in G has order %d" % len(stab))
ok = r8 and r9 and conj and sym and stat and pos and len(stab) == 4 and len(G) == 24 and kinds == [6, 6, 24] and len(free) == 3 and e_ok and o_ok and lump and a not in Lq.free_symbols
print("ALL HOLD:", ok)
