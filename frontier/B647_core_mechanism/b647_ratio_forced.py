"""B647 cell 1 (R20-5): is the 24 zeta_6 ratio FORCED by the swap law
PLUS the banked zero pattern?

B638's closure: the swap law alone leaves a 10-dim real solution space
(20 unknowns). New question: impose the ZERO LAW as constraints
(Y[012] = Y[013] = Y[014] = Y[024] = 0, the weld-none pattern) and ask
whether the constrained solution space forces Y[023]/Y[123] = 24 zeta_6
(and Y[034]/Y[134] — the B645 spectator extension).
"""
import itertools as it
import sympy as sp

r = sp.sqrt(-3)
z6 = (1 + r) / 2
z6b = (1 - r) / 2
M = [
    [z6, 0, 0, 0, 0],
    [r / 24, z6b, 0, 0, 0],
    [sp.Integer(1256617152000) + 1267793856000 * r,
     sp.Integer(268240896000), -z6, 0, 0],
    [sp.Rational(-46189483200, 13) + 465696000 * r,
     sp.Integer(11176704000) - 11176704000 * r, 0, -z6b, 0],
    [sp.Integer(1068480) - 514080 * r,
     sp.Integer(-6652800) - 6652800 * r, 0, 0, 1],
]

trips = list(it.combinations(range(5), 3))
Yv, syms = {}, []
for t in trips:
    a = sp.symbols(f"a_{t[0]}{t[1]}{t[2]}", real=True)
    b = sp.symbols(f"b_{t[0]}{t[1]}{t[2]}", real=True)
    Yv[t] = a + b * r
    syms += [a, b]


def Yof(i, j, k):
    perm = (i, j, k)
    if len(set(perm)) < 3:
        return sp.Integer(0)
    sign, p = 1, list(perm)
    for x in range(3):
        for y in range(x + 1, 3):
            if p[x] > p[y]:
                sign = -sign
    return sign * Yv[tuple(sorted(perm))]


eqs = []
for (i, j, k) in trips:
    lhs = sp.conjugate(Yv[(i, j, k)])
    rhs = sp.Integer(0)
    for (p, q, s) in it.product(range(5), repeat=3):
        c = M[i][p] * M[j][q] * M[k][s]
        if c == 0:
            continue
        rhs += c * Yof(p, q, s)
    e = sp.expand(lhs - rhs)
    eqs.append(sp.re(e))
    eqs.append(sp.im(e))

# the zero law (weld-none / silent-class pattern)
ZERO = [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 4)]
for t in ZERO:
    a = sp.Symbol(f"a_{t[0]}{t[1]}{t[2]}", real=True)
    b = sp.Symbol(f"b_{t[0]}{t[1]}{t[2]}", real=True)
    eqs += [a, b]

sol = sp.linsolve(eqs, syms)
assert len(sol) == 1
vec = list(sol)[0]
free = sorted(set().union(*[v.free_symbols for v in vec]), key=str)
print(f"solution space over R: dim = {len(free)}; free = {free}")

subs = dict(zip(syms, vec))
Y023 = (sp.Symbol("a_023", real=True) + sp.Symbol("b_023", real=True) * r).subs(subs)
Y123 = (sp.Symbol("a_123", real=True) + sp.Symbol("b_123", real=True) * r).subs(subs)
Y034 = (sp.Symbol("a_034", real=True) + sp.Symbol("b_034", real=True) * r).subs(subs)
Y134 = (sp.Symbol("a_134", real=True) + sp.Symbol("b_134", real=True) * r).subs(subs)

core = sp.simplify(sp.expand(Y023 - 24 * z6 * Y123))
spect = sp.simplify(sp.expand(Y034 - 24 * z6 * Y134))
print(f"Y[023] - 24 z6 Y[123] on the constrained space: {core}")
print(f"Y[034] - 24 z6 Y[134] on the constrained space: {spect}")
if core == 0:
    print("=> THE CORE RATIO IS FORCED by swap law + zero law")
else:
    print("=> not forced; residual expression above")
if spect == 0:
    print("=> THE SPECTATOR EXTENSION IS FORCED as well")
