"""B638 closure, full system: the sigma*-law over ALL 10 triples with the
complete exact matrix. Question: does the solution space = (one real
scale) x (the banked table)? That is the honest uniqueness statement."""
import itertools as it
import sympy as sp

r = sp.sqrt(-3)
z6 = (1 + r) / 2
z6b = (1 - r) / 2
# the banked sigma*-matrix rows (sigma*(i) = sum_j M[i][j] rep_j)
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

# unknowns: Y[ijk] for i<j<k as complex (real+imag parts)
trips = list(it.combinations(range(5), 3))
Yv = {}
syms = []
for t in trips:
    a = sp.symbols(f"a_{t[0]}{t[1]}{t[2]}", real=True)
    b = sp.symbols(f"b_{t[0]}{t[1]}{t[2]}", real=True)
    Yv[t] = a + b * r
    syms += [a, b]


def Yof(i, j, k):
    """alternating lookup."""
    perm = (i, j, k)
    srt = tuple(sorted(perm))
    if len(set(perm)) < 3:
        return sp.Integer(0)
    # sign of the permutation
    sign = 1
    p = list(perm)
    for x in range(3):
        for y in range(x + 1, 3):
            if p[x] > p[y]:
                sign = -sign
    return sign * Yv[srt]


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

sol = sp.linsolve(eqs, syms)
print("solution space:")
for s in sol:
    print(" ", s)
# free symbols in the solution = the dimension over R
free = set()
for s in sol:
    for comp in s:
        free |= comp.free_symbols
print(f"free parameters: {sorted(str(f) for f in free)}  "
      f"(dim_R = {len(free)})")

# does the banked table satisfy the FULL system? (numeric substitution)
banked = {(0, 1, 2): 0, (0, 1, 3): 0, (0, 1, 4): 0,
          (0, 2, 3): sp.Rational(-7983360, 13) + sp.Rational(2661120, 13) * r,
          (0, 2, 4): 0,
          (0, 3, 4): sp.Rational(2, 3) * r,
          (1, 2, 3): sp.Rational(221760, 13) * r,
          (1, 2, 4): sp.Rational(2, 3) * r,
          (1, 3, 4): sp.Rational(1, 24) + sp.Rational(1, 72) * r,
          (2, 3, 4): sp.Rational(5332879641600, 13)
                     + sp.Rational(8106192460800, 13) * r}
subs = {}
for t in trips:
    a = sp.symbols(f"a_{t[0]}{t[1]}{t[2]}", real=True)
    b = sp.symbols(f"b_{t[0]}{t[1]}{t[2]}", real=True)
    val = banked[t]
    subs[a] = sp.re(val)
    subs[b] = sp.im(val) / sp.im(r) * 1 if sp.im(val) != 0 else 0
    # cleaner: coefficients in the r-basis
    subs[a] = sp.simplify(val + sp.conjugate(val)) / 2
    subs[b] = sp.simplify((val - sp.conjugate(val)) / (2 * r))
viol = 0
for e in eqs:
    if sp.simplify(e.subs(subs)) != 0:
        viol += 1
print(f"banked unbent table satisfies the full sigma*-system: "
      f"{viol == 0} (violations {viol}/{len(eqs)})")
