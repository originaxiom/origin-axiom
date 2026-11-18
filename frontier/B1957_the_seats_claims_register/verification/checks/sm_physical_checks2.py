"""The SM seat's check of the physical lane's relative-rate and full-undo proofs (its branch at c9296d14a,
SM_CHECK_PHYSICAL_RELATIVE_RATES_AND_UNDO): the claims main computes beyond its own physical_primitives.py F1, F2.
Functions on S_2 = (Z/2)^2, states (x, r); F_x f(x, r) = f(x + 1, r), F_r f(x, r) = f(x, r + 1); Pi the uniform average;
L = a(F_x + F_r - 2I) + b(F_x F_r - I) + c(Pi - I); pullbacks (G f)(s) = f(g(s)); U(x, r) = (x, r + x), V(x, r) = (x + 1, r),
J(x, r) = (r, x).  Exact (sympy).  Nothing of either seat's is run.
 R1  F_x, F_r commute and square to I; L's off-diagonals a + c/4, b + c/4, c/4; rows and columns sum to 0; L symmetric;
     exp[t(F - I)] = ((1 + e^-2t)/2) I + ((1 - e^-2t)/2) F; Pi F = F Pi, Pi^2 = Pi; P_s = e^-cs P0_s + (1 - e^-cs) Pi.
 R2  <U, V, J> on S_2 has order 24 (all of S4); the mean of its 24 pullbacks is Pi; L's kernel is the constants (one);
     E[f(X0) f(Xs)] = e^(-lambda s) for f_x and f_p under the uniform law; L commutes with the pullbacks of V, of the
     r-translation and of J; conjugation by U fixes F_r and Pi and swaps F_x and F_x F_r; U L U^-1 - L = (a - b)(F_x F_r - F_x);
     I, F_x, F_r, F_x F_r independent; at a = b, L = (4a + c)(Pi - I).
 R3  the spectra at (1, 1, 1) and (1, 2, 1) and whether a permutation and one clock scaling can identify them.
 U1  for m = 2..7: J U J = (x + r, r); the table (0,0) -> (1,0) -> (1,1) -> (0,1) under V, U, V^-1; W = V^-1 U V has m fixed points
     (x = -1); q(J(x, r)) = r; with V, U only, the x output after any word depends on x alone; <U, V> has m^3 distinct maps
     T(a, b, c), with T^-1 = T(-a, -b, ba - c); V U V^-1 U^-1 = C^-1.
 U2  m = 2: <U, V> of order 8, (UV)^2 = C != id, UV of order 4, five involutions (D4; Q8 has one); U and J fix (0, 0);
     <U, V, J> transitive, of order 24, the stabiliser of (0, 0) of order 6; in S4, 6 of the 24 permutations send a given
     point to a given point."""
import itertools, functools
import sympy as sp
a, b, c, s, t = sp.symbols("a b c s t", positive=True)
St = [(x, r) for x in range(2) for r in range(2)]; ix = {q: i for i, q in enumerate(St)}
def pull(g): M = sp.zeros(4); [M.__setitem__((ix[q], ix[g(q)]), 1) for q in St]; return M
Fx = pull(lambda q: ((q[0] + 1) % 2, q[1])); Fr = pull(lambda q: (q[0], (q[1] + 1) % 2)); I4 = sp.eye(4); Pi = sp.ones(4, 4) / 4
L = a * (Fx + Fr - 2 * I4) + b * (Fx * Fr - I4) + c * (Pi - I4)
off = sorted({sp.simplify(L[i, j]) for i in range(4) for j in range(4) if i != j}, key=str)
ex = lambda M: sp.simplify((M).exp())
F = Fx; e1 = sp.simplify(ex(t * (F - I4)) - (((1 + sp.exp(-2 * t)) / 2) * I4 + ((1 - sp.exp(-2 * t)) / 2) * F))
L0 = a * (Fx + Fr - 2 * I4) + b * (Fx * Fr - I4)
P = ex(s * L); P0 = ex(s * L0); e3 = sp.simplify(P - (sp.exp(-c * s) * P0 + (1 - sp.exp(-c * s)) * Pi))
print("R1: Fx Fr = Fr Fx %s, squares I %s; off-diagonals %s; rows sum 0 %s, columns %s, symmetric %s; exp formula %s; Pi F = F Pi %s, Pi^2 = Pi %s; P_s = e^-cs P0_s + (1 - e^-cs) Pi: %s"
      % (Fx * Fr == Fr * Fx, Fx ** 2 == I4 and Fr ** 2 == I4, off, all(sp.simplify(sum(L.row(i))) == 0 for i in range(4)), all(sp.simplify(sum(L.col(i))) == 0 for i in range(4)), L == L.T, e1 == sp.zeros(4), Pi * Fx == Fx * Pi and Pi * Fr == Fr * Pi, Pi * Pi == Pi, e3 == sp.zeros(4)))
U2_ = lambda q: (q[0], (q[1] + q[0]) % 2); V2_ = lambda q: ((q[0] + 1) % 2, q[1]); J2_ = lambda q: (q[1], q[0])
gens = [pull(U2_), pull(V2_), pull(J2_)]; G = {sp.ImmutableMatrix(I4)}; fr = [I4]
while fr:
    nw = []
    for g in fr:
        for h in gens:
            k = sp.ImmutableMatrix(g * h)
            if k not in G: G.add(k); nw.append(k)
    fr = nw
fx = sp.Matrix([(-1) ** q[0] for q in St]); fp = sp.Matrix([(-1) ** (q[0] + q[1]) for q in St]); mu = sp.ones(1, 4) / 4
corr = lambda f: sp.simplify((mu * sp.diag(*f) * P * f)[0])
Up = pull(U2_); Ui = Up.inv(); Rt = pull(lambda q: (q[0], (q[1] + 1) % 2))
indep = sp.Matrix([list(M) for M in (I4, Fx, Fr, Fx * Fr)]).rank() == 4
print("R2: |<U, V, J>| = %d; mean of its pullbacks = Pi: %s; dim ker L = %d; E[f f(s)]: f_x %s, f_p %s; L commutes with V, the r-translation, J: %s; U Fr U^-1 = Fr %s, U Pi U^-1 = Pi %s, U Fx U^-1 = Fx Fr %s; U L U^-1 - L - (a - b)(Fx Fr - Fx) = 0: %s; independent %s; at a = b, L - (4a + c)(Pi - I) = 0: %s"
      % (len(G), sum(G, sp.zeros(4)) / len(G) == Pi, 4 - L.subs({a: 1, b: 2, c: 1}).rank(), corr(fx), corr(fp), all(sp.simplify(L * M - M * L) == sp.zeros(4) for M in (pull(V2_), Rt, pull(J2_))),
         Up * Fr * Ui == Fr, Up * Pi * Ui == Pi, sp.simplify(Up * Fx * Ui - Fx * Fr) == sp.zeros(4) or sp.simplify(Up * Fx * Ui - Fx) == sp.zeros(4) and False, sp.simplify(Up * L * Ui - L - (a - b) * (Fx * Fr - Fx)) == sp.zeros(4), indep, sp.simplify(L.subs(b, a) - (4 * a + c) * (Pi - I4)) == sp.zeros(4)))
spec = lambda v: sorted(L.subs(dict(zip((a, b, c), v))).eigenvals().items(), key=lambda kv: kv[0])
s1, s2 = spec((1, 1, 1)), spec((1, 2, 1)); m1 = sorted(m for _, m in s1); m2 = sorted(m for _, m in s2)
print("R3: spectra (eigenvalue: multiplicity) at (1, 1, 1) %s, at (1, 2, 1) %s; multiplicity patterns %s and %s, so no permutation and clock scaling identifies them: %s" % (s1, s2, m1, m2, m1 != m2))
res = {}
for m in range(2, 8):
    S = [(x, r) for x in range(m) for r in range(m)]
    V = lambda q: ((q[0] + 1) % m, q[1]); Vi = lambda q: ((q[0] - 1) % m, q[1]); U = lambda q: (q[0], (q[1] + q[0]) % m); Ui = lambda q: (q[0], (q[1] - q[0]) % m); J = lambda q: (q[1], q[0])
    comp = lambda *fs: (lambda q: functools.reduce(lambda acc, f: f(acc), reversed(fs), q))
    W = comp(Vi, U, V); Cc = lambda q: (q[0], (q[1] + 1) % m); Cinv = lambda q: (q[0], (q[1] - 1) % m)
    T = lambda A, B, Cq: (lambda q: ((q[0] + A) % m, (q[1] + B * q[0] + Cq) % m))
    grp = {tuple(S)}; frontier = [tuple(S)]                                   # the group generated by U and V, closed under composition
    while frontier:
        nw = []
        for g_ in frontier:
            for h in (U, V):
                k_ = tuple(h(q) for q in g_)
                if k_ not in grp: grp.add(k_); nw.append(k_)
        frontier = nw
    Ts = {tuple(T(A, B, Cq)(q) for q in S) for A in range(m) for B in range(m) for Cq in range(m)}
    xdep = all(len({comp(*w)((x, r))[0] for r in range(m)}) == 1 for L_ in range(1, 5) for w in itertools.product((U, V), repeat=L_) for x in range(m))
    res[m] = {"JUJ": all(comp(J, U, J)(q) == ((q[0] + q[1]) % m, q[1]) for q in S), "table": [V((0, 0)), U(V((0, 0))), Vi(U(V((0, 0))))] == [(1 % m, 0), (1 % m, 1 % m), (0, 1 % m)],
              "W fixed": sorted(q for q in S if W(q) == q) == [((m - 1), r) for r in range(m)], "qJ": all(J(q)[0] == q[1] for q in S), "x alone": xdep,
              "m^3": grp == Ts and len(Ts) == m ** 3, "T^-1": all(comp(T(-A, -B, B * A - Cq), T(A, B, Cq))(q) == q for A in range(m) for B in range(m) for Cq in range(m) for q in S),
              "VUV^-1U^-1 = C^-1": all(comp(V, U, Vi, Ui)(q) == Cinv(q) for q in S)}
print("U1: %s" % {m: [k for k, v in r_.items() if not v] or "all hold" for m, r_ in res.items()})
m = 2; S = St
V = lambda q: ((q[0] + 1) % m, q[1]); U = lambda q: (q[0], (q[1] + q[0]) % m); J = lambda q: (q[1], q[0]); comp = lambda *fs: (lambda q: functools.reduce(lambda acc, f: f(acc), reversed(fs), q))
els = {tuple(comp(*w)(q) for q in S) for L_ in range(0, 9) for w in itertools.product((U, V), repeat=L_)}; idt = tuple(S)
mul = lambda g, h: tuple(g[S.index(h[i])] for i in range(4))
UV = tuple(comp(U, V)(q) for q in S); UV2 = mul(UV, UV); Cc = tuple((q[0], (q[1] + 1) % 2) for q in S)
order = lambda g: next(n for n in range(1, 25) if functools.reduce(lambda acc, _: mul(g, acc), range(n), idt) == idt)
full = {tuple(comp(*w)(q) for q in S) for L_ in range(0, 9) for w in itertools.product((U, V, J), repeat=L_)}
stab = [g for g in full if g[0] == (0, 0)]
print("U2: |<U, V>| = %d; (UV)^2 = C: %s, != id: %s; order of UV %d; involutions %d; U and J fix (0, 0): %s; |<U, V, J>| = %d, transitive %s, stabiliser %d; in S4 the permutations sending 0 to 1: %d of 24"
      % (len(els), UV2 == Cc, UV2 != idt, order(UV), sum(1 for g in els if g != idt and mul(g, g) == idt), U((0, 0)) == (0, 0) and J((0, 0)) == (0, 0), len(full), len({g[0] for g in full}) == 4, len(stab), sum(1 for p in itertools.permutations(range(4)) if p[0] == 1)))
# added for the four-form and cyclic-mass notes: the claims main computes beyond physical_four_form.py G1 to G9 and
# physical_cyclic_mass.py C1 to C7
#  X1  the four-form note's section 2 identity: |al|^2 + |al - be|^2 - (2 al3 - be3)^2/2 = 2|al_perp - be_perp/2|^2 + |be|^2/2
#  X2  the shear s = [[1, 0], [1, 1]] on pairs: every symmetric form with s^T B s = B is degenerate; s^n = [[1, 0], [n, 1]]
#  X3  E8 (the even coordinates): 3Q = 2(e1 + e2 + e3) is in the lattice and Q = (2/3)(e1 + e2 + e3) is not
#  X4  main's seat page for the physical lane at 613c4f41 carries M4 and M5
al = sp.symbols("al1:4", real=True); be = sp.symbols("be1:4", real=True); n2 = lambda v: sum(x * x for x in v)
lhs = n2(al) + n2([al[i] - be[i] for i in range(3)]) - (2 * al[2] - be[2]) ** 2 / 2
rhs = 2 * n2([al[i] - be[i] / 2 for i in range(2)]) + n2(be) / 2
b11, b12, b22, nn = sp.symbols("b11 b12 b22 n"); Bq = sp.Matrix([[b11, b12], [b12, b22]]); sh = sp.Matrix([[1, 0], [1, 1]])
solB = sp.solve(list(sh.T * Bq * sh - Bq), [b11, b12, b22], dict=True)
inE8 = lambda v: (all(x == int(x) for x in v) and sum(v) % 2 == 0) or (all((x - sp.Rational(1, 2)) == int(x - sp.Rational(1, 2)) for x in v) and sum(v) % 2 == 0)
Q = [sp.Rational(2, 3)] * 3 + [0] * 5
import subprocess
pg = subprocess.run(["git", "show", "613c4f41:docs/seats/physical.md"], capture_output=True, text=True).stdout
print("X1: lhs - rhs = %s" % sp.expand(lhs - rhs))
print("X2: invariant symmetric forms: %s (det %s); s^5 = %s" % ([Bq.subs(x).tolist() for x in solB], [sp.simplify(Bq.subs(x).det()) for x in solB], (sh ** 5).tolist()))
print("X3: 3Q in E8: %s; Q in E8: %s" % (inE8([3 * x for x in Q]), inE8(Q)))
print("X4: at 613c4f41 the page carries M4: %s, M5: %s" % ("### M4 " in pg or "### M4 —" in pg, "### M5 " in pg or "### M5 —" in pg))
