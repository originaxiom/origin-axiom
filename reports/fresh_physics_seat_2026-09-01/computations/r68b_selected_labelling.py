"""R68 addendum -- the selected two-sided A2^3 in B1264's coordinates: the labelling(s) c in {0,1,2}^6 whose zero-root set is the selected subsystem."""
import io, contextlib, itertools, collections, random, sys
from fractions import Fraction as Fr
# R68's selection (re-run silently)
src = open('r68_g_stable_a2cubed.py').read().split("S_sel = subsystem_roots(both[0])")[0]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(src)
S_sel = subsystem_roots(both[0])
# R66's matching of the icosian E6 simple roots to Bourbaki (re-derive here)
sys.path.insert(0, 'rec/B351_exact_e6_chevalley'); import exact_e6 as X6
A = X6.A
for seed in range(7, 300):
    random.seed(seed); f = [Fr(random.randint(-97, 97)) for _ in range(8)]
    if all(sum(a*b for a, b in zip(f, [Fr(c) for c in vec(r)])) != 0 for r in E6r): break
fval = lambda q: sum(a*b for a, b in zip(f, [Fr(c) for c in vec(q)]))
posE6 = [r for r in E6r if fval(r) > 0]; assert len(posE6) == 36
def qadd(p, q): return tuple(fadd(a, b) for a, b in zip(p, q))
simpleE6 = [r for r in posE6 if not any(qadd(s, t) == r for s in posE6 for t in posE6)]; assert len(simpleE6) == 6
cart = [[int(2*B(a, b)) for b in simpleE6] for a in simpleE6]
perms = [p for p in itertools.permutations(range(6)) if all(cart[p[i]][p[j]] == A[i][j] for i in range(6) for j in range(6))]
print("Bourbaki matchings (two, related by the diagram flip):", len(perms))
import sympy as sp
results = []
for perm in perms:
    simpleB = [simpleE6[perm[i]] for i in range(6)]
    G = sp.Matrix(6, 6, lambda i, j: sp.Rational(2*B(simpleB[i], simpleB[j])))
    def coords6(r):
        c = G.solve(sp.Matrix([sp.Rational(2*B(r, s)) for s in simpleB])); assert all(x.is_integer for x in c); return tuple(int(x) for x in c)
    sel_coords = {coords6(r) for r in S_sel}
    # B1264's labellings: zero-root set {alpha : sum c_i alpha_i = 0 mod 3}
    hits = []
    for c in itertools.product(range(3), repeat=6):
        if not any(c): continue
        zero = {a for a in X6.ROOTS if sum(c[i]*a[i] for i in range(6)) % 3 == 0}
        if zero == sel_coords: hits.append(c)
    results.append((perm, hits))
    print(f"  matching {perm}: labellings whose centralizer is the selected A2^3: {hits}")
# the 9+9+9 partition of the 27 under the selected labelling (B1264's formula), in the 27's fundamental-weight coordinates
Cinv = sp.Matrix(A).inv()
def reflect(wt, i): return tuple(wt[j] - wt[i]*A[i][j] for j in range(6))
w0 = tuple(int(j == 0) for j in range(6)); W27, fr = {w0}, [w0]
while fr:
    v = fr.pop()
    for i in range(6):
        u = reflect(v, i)
        if u not in W27: W27.add(u); fr.append(u)
W27 = sorted(W27)
for perm, hits in results[:1]:
    for c in hits[:1]:
        coef = Cinv * sp.Matrix(6, 1, list(c))
        vals = [int(sum(W27[a][i] * coef[i] for i in range(6))) % 3 for a in range(27)]
        parts = collections.defaultdict(list)
        for w, v in zip(W27, vals): parts[v].append(w)
        print(f"  labelling c = {c}: 27 splits by <lambda, h_c> mod 3 into sizes {[len(parts[k]) for k in (0,1,2)]}")
        for k in (0, 1, 2): print(f"    class {k}: {parts[k]}")
open('r68b_result.txt', 'w').write(repr(results))
