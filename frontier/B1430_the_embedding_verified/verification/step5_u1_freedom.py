"""Step 4 continued: the u(1).

Fix one A2+A1 subsystem (all 720 are W-conjugate, proved in step 4a).
A subalgebra su(3)+su(2)+u(1) with that regular su(3)+su(2) is then
determined by a LINE R.Y in the 3-dimensional space V = (span A2+A1)^perp
inside the Cartan.  Two such are W-conjugate iff the lines are in the same
orbit of Stab_W(A2+A1).  We compute that stabiliser and its orbits on
lines, and we compute the branching of the 27 for each rational direction.
"""
from fractions import Fraction as F
from rootsys import *
from collections import Counter, defaultdict
from itertools import product
import json

simple = E6_simple()
roots = generate_roots(simple)
idx = {r: i for i, r in enumerate(roots)}
gens = simple_reflection_perms(roots, simple)
order, group = weyl_group_order(roots, simple)
A = cartan_matrix(simple)


def solve_exact(M, b):
    n = len(M)
    Mx = [list(map(F, M[i])) + [F(b[i])] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if Mx[i][c] != 0)
        Mx[c], Mx[piv] = Mx[piv], Mx[c]
        pv = Mx[c][c]
        Mx[c] = [x / pv for x in Mx[c]]
        for i in range(n):
            if i != c and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[c])]
    return [Mx[i][n] for i in range(n)]


def from_simple_coords(c):
    out = [F(0)] * len(simple[0])
    for ck, a in zip(c, simple):
        out = [x + ck * y for x, y in zip(out, a)]
    return tuple(out)


omegas = [from_simple_coords(solve_exact(A, [1 if k == i else 0 for k in range(6)]))
          for i in range(6)]


def weight_orbit(w):
    seen, q = {w}, [w]
    while q:
        x = q.pop()
        for a in simple:
            y = refl(x, a)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return sorted(seen)


W27 = weight_orbit(omegas[0])
assert len(W27) == 27

# ---- pick one A2+A1 and name its pieces ---------------------------------
A2 = a2_subsystems(roots)
A2A1 = a2_a1_subsystems(roots, A2)
rep = A2A1[0]
Srts = [roots[k] for k in rep]
# split into the A2 part and the A1 part
a2part = [g for g in A2 if g <= rep][0]
a2roots = [roots[k] for k in a2part]
a1roots = [roots[k] for k in rep if k not in a2part]
assert len(a1roots) == 2
# simple roots of the A2: b1, b2 with (b1,b2) = -1
b1 = a2roots[0]
b2 = next(r for r in a2roots if ip(b1, r) == -1)
gam = a1roots[0]
print("=== THE FIXED A2+A1 ===")
print("A2 simple roots:", b1, b2, " (b1,b2) =", ip(b1, b2))
print("A1 root:", gam, " orthogonal to A2:", all(ip(gam, r) == 0 for r in a2roots))

stab = [g for g in group if frozenset(g[k] for k in rep) == rep]
print("Stab_W(A2+A1) order:", len(stab))

# ---- V = orthogonal complement, and the lattice of integral directions ---
basisS = [b1, b2, gam]
print("rank of span(A2+A1) =", rank_of(basisS), " so dim V = 6 -",
      rank_of(basisS), "=", 6 - rank_of(basisS))

# integral coweights: Y = sum n_i omega_i ; (Y, alpha_j) = n_j
# condition Y _|_ (A2+A1)  <=>  (Y, b1) = (Y, b2) = (Y, gam) = 0
def simple_coeffs(r):
    return solve_exact(A, [ip(r, simple[j]) for j in range(6)])


conds = [[int(x) for x in simple_coeffs(r)] for r in basisS]
print("linear conditions on (n_1..n_6) for Y to commute with A2+A1:")
for c in conds:
    print("   ", c)

N = 3
Ys = []
for n in product(range(-N, N + 1), repeat=6):
    if any(sum(ci * ni for ci, ni in zip(c, n)) != 0 for c in conds):
        continue
    if all(x == 0 for x in n):
        continue
    from math import gcd
    g = 0
    for x in n:
        g = gcd(g, abs(x))
    if g != 1:
        continue
    Ys.append(n)
print("primitive integral coweight vectors with |n_i| <= %d orthogonal to "
      "the A2+A1: %d" % (N, len(Ys)))

Yvecs = {}
for n in Ys:
    v = [F(0)] * 8
    for ni, w in zip(n, omegas):
        v = [x + ni * y for x, y in zip(v, w)]
    Yvecs[n] = tuple(v)
    assert all(ip(Yvecs[n], r) == 0 for r in Srts)

# ---- lines: identify n and -n -------------------------------------------
lines = {}
for n in Ys:
    key = min(n, tuple(-x for x in n))
    lines[key] = Yvecs[n]
lineslist = sorted(lines)
print("distinct LINES R.Y among them:", len(lineslist))

# ---- Stab acts on V; realise the action on coweight vectors -------------
# a Weyl element is a permutation of roots; recover its linear action from
# images of the simple roots
perm_to_lin = {}


def lin_of_perm(g):
    images = [roots[g[idx[a]]] for a in simple]   # w(alpha_i)

    def act(v):
        c = simple_coeffs(v)
        out = [F(0)] * 8
        for ck, im in zip(c, images):
            out = [x + ck * y for x, y in zip(out, im)]
        return tuple(out)
    return act


stab_lin = [lin_of_perm(g) for g in stab]
# sanity: stabiliser really fixes the subsystem setwise
for act in stab_lin[:5]:
    assert set(map(act, Srts)) == set(Srts)

vec_to_line = {v: k for k, v in lines.items()}
# orbits of Stab on the enumerated lines (only lines whose image stays in
# the enumerated box are merged; we also record escapes)
parent = {k: k for k in lineslist}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb


escapes = 0
for k in lineslist:
    v = lines[k]
    for act in stab_lin:
        w = act(v)
        if w in vec_to_line:
            union(k, vec_to_line[w])
        elif tuple(-x for x in w) in vec_to_line:
            union(k, vec_to_line[tuple(-x for x in w)])
        else:
            escapes += 1
orbs = defaultdict(list)
for k in lineslist:
    orbs[find(k)].append(k)
print("Stab-orbits on those lines (images outside the box: %d):" % escapes,
      len(orbs))
print("orbit sizes:", sorted(Counter(len(v) for v in orbs.values()).items()))

# ---- branching of the 27 ------------------------------------------------
w3 = [(0, 0)], None


def su3_orbit(lab):
    # Dynkin labels, reflections s1:(a,b)->(-a,a+b), s2:(a,b)->(a+b,-b)
    seen, q = {lab}, [lab]
    while q:
        a, b = q.pop()
        for y in ((-a, a + b), (a + b, -b)):
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


LIB3 = {(0, 0): {(0, 0)}, (1, 0): su3_orbit((1, 0)), (0, 1): su3_orbit((0, 1))}
LIB2 = {0: [0], 1: [1, -1]}
NAME3 = {(0, 0): "1", (1, 0): "3", (0, 1): "3b"}


def labels(w, Y):
    return (ip(w, b1), ip(w, b2), ip(w, gam), ip(w, Y))


def branch(Y):
    """Return the branching of the 27 as a sorted tuple of
    (su3 name, su2 dim, charge)."""
    bylevel = defaultdict(list)
    for w in W27:
        a, b, c, y = labels(w, Y)
        bylevel[y].append((a, b, c))
    out = []
    for y, ws in bylevel.items():
        M = Counter(ws)
        while sum(M.values()):
            dom = [t for t in M if t[0] >= 0 and t[1] >= 0 and t[2] >= 0]
            if not dom:
                return None            # non-minuscule / unidentified
            hw = max(dom, key=lambda t: (t[0] + t[1] + t[2], t))
            l3, l2 = (hw[0], hw[1]), hw[2]
            if l3 not in LIB3 or l2 not in LIB2:
                return None
            for p in LIB3[l3]:
                for q in LIB2[l2]:
                    t = (p[0], p[1], q)
                    if M[t] <= 0:
                        return None
                    M[t] -= 1
                    if M[t] == 0:
                        del M[t]
            out.append((NAME3[l3], l2 + 1, y))
    return tuple(sorted(out, key=lambda t: (t[2], t[0], t[1])))


def canon(sig):
    """canonical form up to positive rescaling of Y and up to Y -> -Y"""
    if sig is None:
        return None
    chs = [t[2] for t in sig]
    m = max(abs(c) for c in chs)
    def norm(s, sgn):
        return tuple(sorted((t[0], t[1], sgn * t[2] / m) for t in s))
    return min(norm(sig, 1), norm(sig, -1))


sigs = {}
for k in lineslist:
    s = branch(lines[k])
    sigs[k] = canon(s)
bad = [k for k in lineslist if sigs[k] is None]
print()
print("=== BRANCHING OF THE 27 ===")
print("lines tested:", len(lineslist), " unidentified branchings:", len(bad))
distinct = set(s for s in sigs.values() if s is not None)
print("DISTINCT branching signatures (up to scale and sign of Y):",
      len(distinct))

# su(3)xsu(2) content is Y-independent: compute it once with a generic Y
content = Counter()
for k in lineslist:
    s = branch(lines[k])
    if s:
        content = Counter((t[0], t[1]) for t in s)
        break
print("su(3)xsu(2) content of the 27 (Y-independent):", dict(content))

# the Standard Model target (EXTERNAL PHYSICS INPUT, not an E6 computation):
# 27 = 10 + 5bar + 5bar + 5 + 1 + 1 of SU(5), i.e. under SU(3)xSU(2)xU(1)_Y
SM = sorted([("3", 2, F(1, 6)), ("3b", 1, F(-2, 3)), ("1", 1, F(1)),
             ("3b", 1, F(1, 3)), ("1", 2, F(-1, 2)),
             ("3b", 1, F(1, 3)), ("1", 2, F(-1, 2)),
             ("3", 1, F(-1, 3)), ("1", 2, F(1, 2)),
             ("1", 1, F(0)), ("1", 1, F(0))])
assert sum({"1": 1, "3": 3, "3b": 3}[a] * b for a, b, _ in SM) == 27


def sm_like(sig_raw):
    """does this line reproduce the SM hypercharge pattern, for SOME
    normalisation and either orientation of the su(3) and of Y?"""
    if sig_raw is None:
        return False
    for flip3 in (False, True):
        for sgn in (1, -1):
            s = [({"3": "3b", "3b": "3", "1": "1"}[a] if flip3 else a,
                  b, sgn * c) for a, b, c in sig_raw]
            # normalise so the (3,2) piece has charge 1/6
            q = [c for a, b, c in s if a == "3" and b == 2]
            if len(q) != 1 or q[0] == 0:
                continue
            lam = F(1, 6) / q[0]
            t = sorted((a, b, lam * c) for a, b, c in s)
            if t == SM:
                return True
    return False


hits = [k for k in lineslist if sm_like(branch(lines[k]))]
print()
print("lines whose 27-branching IS exactly the SM pattern",
      "(1 generation + 10 + 1):", len(hits))
if hits:
    hit_orbits = set(find(k) for k in hits)
    print("they fall into", len(hit_orbits), "Stab-orbit(s) ->",
          len(hit_orbits), "W-conjugacy class(es) of su(3)+su(2)+u(1)_Y",
          "subalgebras with the SM branching (within the search box)")
    k0 = hits[0]
    print("example hypercharge direction, coweight coords n =", k0)
    print("its branching:")
    for t in sorted(branch(lines[k0]), key=lambda t: t[2]):
        print("    (%-2s, %d)_Y=%s" % (t[0], t[1], t[2]))

json.dump({"n_lines": len(lineslist), "n_stab_orbits": len(orbs),
           "n_distinct_signatures": len(distinct), "n_sm_hits": len(hits)},
          open("step5_summary.json", "w"))
