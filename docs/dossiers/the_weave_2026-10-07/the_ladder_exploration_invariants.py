"""EXPLORATORY (not a recorded arc): is PF1's commutator one wording among many, or the one the joint action fixes?
(1) polynomials in (x,y,z) = (tr a, tr b, tr ab) of degree <= 6 fixed by both moves L, R;
(2) conjugacy classes of F2 (up to inversion), length <= 12, fixed by both L and R;
(3) rank 3: balanced classes of F3, length <= 8, fixed by every elementary Nielsen transvection."""
import itertools, sympy as sp, time

x, y, z = sp.symbols("x y z")
Lp = {x: x, y: z, z: x*z - y}          # a->a, b->ab : (tr a, tr ab, tr a.ab)
Rp = {x: z, y: y, z: y*z - x}          # a->ab, b->b : (tr ab, tr b, tr ab.b)
kappa = x**2 + y**2 + z**2 - x*y*z - 2
assert sp.expand(kappa.subs(Lp, simultaneous=True) - kappa) == 0
assert sp.expand(kappa.subs(Rp, simultaneous=True) - kappa) == 0
mons = [x**i*y**j*z**k for i in range(7) for j in range(7) for k in range(7) if i+j+k <= 6]
cs = sp.symbols(f"c0:{len(mons)}")
P = sum(c*m for c, m in zip(cs, mons))
eqs = []
for mv in (Lp, Rp):
    d = sp.Poly(sp.expand(P.subs(mv, simultaneous=True) - P), x, y, z)
    eqs += d.coeffs()
sol = sp.solve(eqs, cs, dict=True)[0]
free = [c for c in cs if c not in sol]
inv = [sp.expand(P.subs(sol).subs({f: (1 if f == g else 0) for f in free})) for g in free]
print("(1) dim of invariant polynomials of degree <= 6:", len(free))
for q in inv:
    print("    ", sp.factor(q), "  in terms of kappa:", sp.simplify(q.subs(z, sp.solve(sp.Symbol('k') - kappa, z)[0])) if False else "")
K = sp.Symbol("K")
basis_ok = all(any(sp.expand(q - sp.expand(e)) == 0 for e in []) for q in [])
span = sp.Matrix([[sp.Poly(sp.expand(q), x, y, z).as_expr().coeff(m) for m in mons] for q in inv]).rank()
span2 = sp.Matrix([[sp.Poly(sp.expand(q), x, y, z).as_expr().coeff(m) if True else 0 for m in mons] for q in inv + [sp.Integer(1), kappa, sp.expand(kappa**2)]]).rank()
print("    rank of the invariants:", span, "; with 1, kappa, kappa^2 added:", span2)

def red(w):
    out = []
    for t in w:
        if out and out[-1] == -t: out.pop()
        else: out.append(t)
    return out
def cyc(w):
    w = red(w)
    while len(w) > 1 and w[0] == -w[-1]: w = w[1:-1]
    return w
def inv_(w): return [-t for t in reversed(w)]
def canon(w):
    w = cyc(w)
    if not w: return ()
    cands = []
    for u in (w, inv_(w)):
        cands += [tuple(u[i:] + u[:i]) for i in range(len(u))]
    return min(cands)
def apply(img, w):
    out = []
    for t in w:
        out += img[t] if t > 0 else inv_(img[-t])
    return out

# (2) F2: letters 1 = a, 2 = b
L2 = {1: [1], 2: [1, 2]}; R2 = {1: [1, 2], 2: [2]}
t0 = time.time(); fixed = []; seen = set()
def words(n, k):
    letters = [l for i in range(1, k+1) for l in (i, -i)]
    def rec(w):
        if len(w) == n: yield w; return
        for l in letters:
            if w and w[-1] == -l: continue
            yield from rec(w + [l])
    yield from rec([])
for n in range(2, 13, 2):
    for w in words(n, 2):
        c = canon(w)
        if len(c) != n or c in seen: continue
        seen.add(c)
        if sum(c) != 0 and False: pass
        if all(canon(apply(m, list(c))) == c for m in (L2, R2)):
            fixed.append(c)
print(f"(2) F2 classes up to inversion of length <= 12: {len(seen)}; fixed by L and R: {len(fixed)} ({time.time()-t0:.1f}s)")
for c in fixed: print("    ", "".join({1:'a',-1:'A',2:'b',-2:'B'}[t] for t in c))

# (3) F3, balanced classes of length <= 8, every transvection x_i -> x_i x_j^e and x_i -> x_j^e x_i
moves = []
for i, j in itertools.permutations((1, 2, 3), 2):
    for e in (1, -1):
        img = {k: [k] for k in (1, 2, 3)}; img[i] = [i, e*j]; moves.append(img)
        img = {k: [k] for k in (1, 2, 3)}; img[i] = [e*j, i]; moves.append(img)
t0 = time.time(); seen3 = set(); fixed3 = []; best = None
for n in range(2, 9, 2):
    for w in words(n, 3):
        c = canon(w)
        if len(c) != n or c in seen3: continue
        if any(sum(1 if t == k else -1 if t == -k else 0 for t in c) for k in (1, 2, 3)): continue
        seen3.add(c)
        moved = sum(canon(apply(m, list(c))) != c for m in moves)
        if moved == 0: fixed3.append(c)
        if best is None or moved < best[0]: best = (moved, c)
print(f"(3) F3 balanced classes of length <= 8: {len(seen3)}; fixed by all {len(moves)} transvections: {len(fixed3)};"
      f" fewest moved by: {best[0]} ({best[1]}) ({time.time()-t0:.1f}s)")
# control: the rank-3 analogue of the commutator, the product of commutators, and a surface word
for name, w in (("[a,b]", [1, 2, -1, -2]), ("[a,b][b,c][c,a]", [1, 2, -1, -2, 2, 3, -2, -3, 3, 1, -3, -1])):
    print("    control", name, "moved by", sum(canon(apply(m, w)) != canon(w) for m in moves), "of", len(moves))
