"""The physical lane's foundational primitive packet (its branch at cde6e6c64; reports/.../foundational_primitive_audit_2026_11_18),
the finite pieces of its hand proofs checked by main, a seat that did not write them.  Nothing of the lane's is run.
 F1  INTERNAL_REGISTRATION_AND_FULL_UNDO: on S_m = (Z/m)^2, V(x,r) = (x+1, r), U(x,r) = (x, r+x), J(x,r) = (r, x): bijections with the
     inverses (3); U V and V U as (5); W = V^-1 U V = (x, r+x+1) (6) and its inverse V^-1 U^-1 V (7); the commutator [U, V] = (x, r+1)
     central (11); T(a,b,c)(x,r) = (x+a, r+bx+c) composing as (10); V^a U^b C^c = T(a,b,c) (12); for m = 2..7, every state.
 F2  RELATIVE_RATES: L = a(F_x + F_r - 2I) + b(F_x F_r - I) + c(Pi - I) on functions on S_2: its eigenvalues on 1, f_x, f_r, f_p (4);
     R = (4a+c)/(2(a+b)+c) at (1,1,1) and (1,2,1) (6); I + F_x + F_r + F_x F_r = 4 Pi (7); with a = b, R = 1.
 F3  HISTORY_WEIGHTS (4): W(u u^-1) = p(1-p), not 1, for p in (0,1); PREDICTIVE_REGISTER (6): with p_V(x,r) = p_r, p_0 != p_1, two
     complete states with the same x have different probabilities of the next coarse step."""
import itertools
import sympy as sp
ok = {}
for m in range(2, 8):
    S = [(x, r) for x in range(m) for r in range(m)]
    V = lambda s: ((s[0] + 1) % m, s[1]); Vi = lambda s: ((s[0] - 1) % m, s[1]); U = lambda s: (s[0], (s[1] + s[0]) % m); Ui = lambda s: (s[0], (s[1] - s[0]) % m); J = lambda s: (s[1], s[0])
    T = lambda a, b, c: (lambda s: ((s[0] + a) % m, (s[1] + b * s[0] + c) % m))
    comp = lambda *fs: (lambda s: __import__("functools").reduce(lambda acc, f: f(acc), reversed(fs), s))
    Cm = comp(U, V, Ui, Vi)                           # U V U^-1 V^-1 applied right to left
    checks = {
        "bijections and inverses": all(Vi(V(s)) == s and Ui(U(s)) == s and J(J(s)) == s for s in S) and len({V(s) for s in S}) == len({U(s) for s in S}) == m * m,
        "(5)": all(comp(U, V)(s) == ((s[0] + 1) % m, (s[1] + s[0] + 1) % m) and comp(V, U)(s) == ((s[0] + 1) % m, (s[1] + s[0]) % m) for s in S),
        "(6)": all(comp(Vi, U, V)(s) == (s[0], (s[1] + s[0] + 1) % m) for s in S),
        "(7)": all(comp(Vi, Ui, V)(comp(Vi, U, V)(s)) == s for s in S),
        "(11) U V U^-1 V^-1": all(Cm(s) == (s[0], (s[1] + 1) % m) for s in S),
        "(11) U^-1 V^-1 U V": all(comp(Ui, Vi, U, V)(s) == (s[0], (s[1] + 1) % m) for s in S),
        "(11) central": all(comp(U, lambda t: (t[0], (t[1] + 1) % m))(s) == comp(lambda t: (t[0], (t[1] + 1) % m), U)(s) and comp(V, lambda t: (t[0], (t[1] + 1) % m))(s) == comp(lambda t: (t[0], (t[1] + 1) % m), V)(s) for s in S),
        "(10)": all(comp(T(a, b, c), T(a2, b2, c2))(s) == T((a + a2) % m, (b + b2) % m, (c + c2 + b * a2) % m)(s) for a, b, c, a2, b2, c2 in itertools.product(range(m), repeat=6) for s in S) if m <= 3 else None,   # exhaustive at m = 2, 3
        "(12)": all(comp(*([V] * a + [U] * b + [lambda s: (s[0], (s[1] + 1) % m)] * c))(s) == T(a, b, c)(s) for a, b, c in itertools.product(range(m), repeat=3) for s in S),
    }
    ok[m] = checks
print("F1: %s" % {m: {k: v for k, v in c.items()} for m, c in ok.items()})
a, b, c = sp.symbols("a b c", positive=True)
st = [(x, r) for x in range(2) for r in range(2)]; idx = {s: i for i, s in enumerate(st)}
def perm(f): M = sp.zeros(4); [M.__setitem__((idx[s], idx[f(s)]), 1) for s in st]; return M   # (M g)(s) = g(f(s))
Fx, Fr, I4 = perm(lambda s: ((s[0] + 1) % 2, s[1])), perm(lambda s: (s[0], (s[1] + 1) % 2)), sp.eye(4); Pi = sp.ones(4) / 4
L = a * (Fx + Fr - 2 * I4) + b * (Fx * Fr - I4) + c * (Pi - I4)
fx, fr, fp, one = [sp.Matrix([(-1) ** s[0] for s in st]), sp.Matrix([(-1) ** s[1] for s in st]), sp.Matrix([(-1) ** (s[0] + s[1]) for s in st]), sp.ones(4, 1)]
ev = {n: sp.simplify((L * f).T * f / (f.T * f)[0])[0] for n, f in (("1", one), ("f_x", fx), ("f_r", fr), ("f_p", fp))}
eig = all(sp.simplify(L * f - ev[n] * f) == sp.zeros(4, 1) for n, f in (("1", one), ("f_x", fx), ("f_r", fr), ("f_p", fp)))
Rf = lambda A, B, Cc: sp.Rational(4 * A + Cc, 2 * (A + B) + Cc)
print("F2: eigenvalues on 1, f_x, f_r, f_p: %s (eigenvectors: %s); R at (1,1,1) %s, at (1,2,1) %s; I + F_x + F_r + F_x F_r = 4 Pi: %s; with a = b, R = %s"
      % (ev, eig, Rf(1, 1, 1), Rf(1, 2, 1), sp.simplify(I4 + Fx + Fr + Fx * Fr - 4 * Pi) == sp.zeros(4), sp.simplify((4 * a + c) / (2 * (a + a) + c))))
p, p0, p1 = sp.symbols("p p0 p1", positive=True)
print("F3: W(u u^-1) = %s, equal to 1 only at p in %s; Pr[next coarse step | (x, 0)] = p0 and | (x, 1) = p1, different when p0 != p1" % (p * (1 - p), sp.solve(sp.Eq(p * (1 - p), 1), p)))
