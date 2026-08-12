"""B1042 — PM3: the trit morphism. Exact arithmetic in Q(omega); no numerics.

V1: build 2T = the 24 Hurwitz units exactly; conjugacy classes; Q8 normal;
    2T/Q8 = Z/3; the SEVEN characters constructed and orthogonality-verified;
    the McKay graph COMPUTED (not cited) from tensoring with the faithful 2;
    the tensoring-by-1' permutation; graph-automorphism check; center-deletion
    -> three A2 components; the rotation permutes them in one 3-cycle.
V2: the value-group link (the 1-dims' values = <omega> = mu_3 in the field's mu_6)
    + the banked links cited at point of use.
CONTROL (the E8 end): SL(2,5) is PERFECT (computed) -> no nontrivial 1-dim
    characters -> the construction that yields the trit on the E6 end yields
    NOTHING on the golden end. Discriminating, so the carry is not generic.
V3: the B757 accident-detector adjudicated in FINDINGS from these outputs.
"""
from fractions import Fraction as F
from itertools import product

# ---------- Q(omega) exact arithmetic: numbers as (a, b) = a + b*omega,
# omega^2 = -1 - omega, conj(omega) = omega^2.
def qw(a, b=0):
    return (F(a), F(b))

def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x):    return (-x[0], -x[1])
def mul(x, y):
    a, b, c, d = x[0], x[1], y[0], y[1]
    # (a+bw)(c+dw) = ac + (ad+bc)w + bd w^2 ; w^2 = -1-w
    return (a * c - b * d, a * d + b * c - b * d)
def conj(x):   # omega -> omega^2 = -1-omega
    a, b = x
    return (a - b, -b)
ZERO, ONE = qw(0), qw(1)
OMEGA = qw(0, 1)
OMEGA2 = mul(OMEGA, OMEGA)

# ---------- 2T as exact quaternions (a,b,c,d) = a + bi + cj + dk, entries in Q
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2)
def qinv(p):  # unit quaternions: inverse = conjugate
    a, b, c, d = p
    return (a, -b, -c, -d)

H = F(1, 2)
units = [(F(s), F(0), F(0), F(0)) for s in (1, -1)]
for axis in range(1, 4):
    for s in (1, -1):
        q = [F(0)] * 4; q[axis] = F(s); units.append(tuple(q))
for signs in product((1, -1), repeat=4):
    units.append(tuple(F(s) * H for s in signs))
G = units
assert len(G) == 24 and len(set(G)) == 24
print(f"[V1] 2T built: {len(G)} Hurwitz units")

# conjugacy classes (brute force)
def conj_class(g):
    return frozenset(qmul(qmul(h, g), qinv(h)) for h in G)
classes, seen = [], set()
for g in G:
    if g not in seen:
        c = conj_class(g); classes.append(sorted(c)); seen |= set(c)
classes.sort(key=lambda c: (len(c), c))
print(f"[V1] conjugacy classes: {len(classes)} with sizes {[len(c) for c in classes]}")
assert len(classes) == 7

# element order
def qorder(g):
    p, n = g, 1
    e = (F(1), F(0), F(0), F(0))
    while p != e:
        p = qmul(p, g); n += 1
    return n
cl_order = [qorder(c[0]) for c in classes]
print(f"[V1] class element orders: {cl_order}")

# Q8 normal, quotient Z/3
Q8 = set(u for u in G if all(x * 2 == int(x * 2) for x in u) and sum(abs(x) for x in u) == 1)
assert len(Q8) == 8
assert all(qmul(qmul(h, g), qinv(h)) in Q8 for g in Q8 for h in G), "Q8 not normal"
# coset map: order-3 generator
gen3 = next(g for g in G if qorder(g) == 3)
cosets = {frozenset(qmul(g, q) for q in Q8) for g in G}
assert len(cosets) == 3
def coset_index(g):
    for k in range(3):
        p = (F(1), F(0), F(0), F(0))
        for _ in range(k):
            p = qmul(p, gen3)
        if any(qmul(qinv(p), g) in Q8 for _ in (0,)):
            if qmul(qinv(p), g) in Q8:
                return k
    raise ValueError
print(f"[V1] Q8 normal; 2T/Q8 = Z/3 (3 cosets); generator order {qorder(gen3)}")

# ---------- the seven characters, exact in Q(omega)
# 1-dims: omega^(coset), omega^(2*coset). Faithful 2: trace of the SU(2) image
# = 2 * scalar part (exact rational). 2' = 2 x 1', 2'' = 2 x 1''.
# 3 = Sym^2(2): chi3(g) = (chi2(g)^2 + chi2(g^2)) / 2.
def chi2(g):   return qw(2 * g[0])
def chi1(g):   return ONE
def chi1p(g):  return (OMEGA, OMEGA2, ONE)[0] if False else [ONE, OMEGA, OMEGA2][coset_index(g)]
def chi1pp(g): return [ONE, OMEGA2, OMEGA][coset_index(g)]
def chi2p(g):  return mul(chi2(g), chi1p(g))
def chi2pp(g): return mul(chi2(g), chi1pp(g))
def chi3(g):
    g2 = qmul(g, g)
    s = add(mul(chi2(g), chi2(g)), chi2(g2))
    return (s[0] / 2, s[1] / 2)
irreps = [("1", chi1), ("1p", chi1p), ("1pp", chi1pp),
          ("2", chi2), ("2p", chi2p), ("2pp", chi2pp), ("3", chi3)]

def inner(f1, f2):
    tot = ZERO
    for g in G:
        tot = add(tot, mul(f1(g), conj(f2(g))))
    return (tot[0] / 24, tot[1] / 24)
ortho_ok = all(inner(f, h) == (ONE if n1 == n2 else ZERO)
               for n1, f in irreps for n2, h in irreps)
print(f"[V1] character orthogonality over Q(omega), all 49 pairs exact: {'PASS' if ortho_ok else 'FAIL'}")
assert ortho_ok

# ---------- the McKay graph, COMPUTED: A[i][j] = <chi2 * chi_i, chi_j>
names = [n for n, _ in irreps]
A = {}
for n1, f1 in irreps:
    for n2, f2 in irreps:
        m = inner(lambda g, f1=f1: mul(chi2(g), f1(g)), f2)
        assert m[1] == 0 and m[0] == int(m[0])
        A[(n1, n2)] = int(m[0])
edges = sorted({tuple(sorted((i, j))) for i in names for j in names if A[(i, j)] and i != j})
print(f"[V1] McKay graph edges (computed): {edges}")
deg = {n: sum(A[(n, m)] for m in names if m != n) for n in names}
assert A[("1", "2")] == 1 and A[("3", "2")] == 1  # legs meet the center via the 2's
# affine E6 shape: center '3' has degree 3; the three 2's degree 2; the three 1's degree 1
shape_ok = (deg["3"] == 3 and all(deg[x] == 2 for x in ("2", "2p", "2pp"))
            and all(deg[x] == 1 for x in ("1", "1p", "1pp")))
print(f"[V1] graph IS affine E6 (center deg 3, middles deg 2, tips deg 1): {'PASS' if shape_ok else 'FAIL'}")
assert shape_ok

# ---------- the tensoring-by-1' permutation
pi = {}
for n1, f1 in irreps:
    prod_char = lambda g, f1=f1: mul(f1(g), chi1p(g))
    for n2, f2 in irreps:
        if inner(prod_char, f2) == ONE:
            pi[n1] = n2
print(f"[V1] tensoring by 1' permutes irreps: {pi}")
# order 3, fixes the center
def apply_n(p, n, k):
    for _ in range(k):
        n = p[n]
    return n
assert pi["3"] == "3" and all(apply_n(pi, n, 3) == n for n in names)
assert any(pi[n] != n for n in names)
# graph automorphism check
auto_ok = all(A[(i, j)] == A[(pi[i], pi[j])] for i in names for j in names)
print(f"[V1] the permutation is an order-3 automorphism of the McKay graph fixing the center: {'PASS' if auto_ok else 'FAIL'}")
assert auto_ok

# ---------- delete the center -> components
rem = [n for n in names if n != "3"]
adj = {n: [m for m in rem if m != n and A[(n, m)]] for n in rem}
comps = []
unvisited = set(rem)
while unvisited:
    stack = [unvisited.pop()]; comp = set(stack)
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y in unvisited:
                unvisited.discard(y); comp.add(y); stack.append(y)
    comps.append(sorted(comp))
comps.sort()
print(f"[V1] delete the center node -> components: {comps}")
assert len(comps) == 3 and all(len(c) == 2 for c in comps)  # three A2 diagrams = su(3)^3
# the rotation permutes the three components in ONE 3-cycle
comp_of = {n: i for i, c in enumerate(comps) for n in c}
img = {i: comp_of[pi[comps[i][0]]] for i in range(3)}
cyc = {0}; k = img[0]
while k not in cyc:
    cyc.add(k); k = img[k]
print(f"[V1] the rotation permutes the three A2 components in one {len(cyc)}-cycle")
assert len(cyc) == 3

# ---------- V2: the value-group link (exact)
vals = sorted({chi1p(g) for g in G} | {chi1pp(g) for g in G})
print(f"[V2] the 1-dims' value set = {vals} = {{1, omega, omega^2}} = <omega> = mu_3 (exact)")
assert set(vals) == {ONE, OMEGA, OMEGA2}

# ---------- CONTROL: SL(2,5) is perfect -> the golden end has NO such characters
def sl2(p):
    els = [((a, b), (c, d)) for a in range(p) for b in range(p)
           for c in range(p) for d in range(p) if (a * d - b * c) % p == 1]
    return els
def mmulp(x, y, p):
    (a, b), (c, d) = x; (e, f), (g, h) = y
    return (((a * e + b * g) % p, (a * f + b * h) % p),
            ((c * e + d * g) % p, (c * f + d * h) % p))
def minvp(x, p):  # det 1: inverse = adjugate
    (a, b), (c, d) = x
    return ((d % p, (-b) % p), ((-c) % p, a % p))
S = sl2(5)
print(f"[CTRL] |SL(2,5)| = {len(S)}")
comm = set()
for x in S[:len(S)]:
    for y in S:
        comm.add(mmulp(mmulp(x, y, 5), mmulp(minvp(x, 5), minvp(y, 5), 5), 5))
    if len(comm) == len(S):
        break
# close under multiplication (commutators generate; check closure reached whole group)
grown = set(comm)
frontier_set = set(comm)
while frontier_set:
    new = set()
    for x in frontier_set:
        for y in comm:
            z = mmulp(x, y, 5)
            if z not in grown:
                new.add(z); grown.add(z)
    frontier_set = new
print(f"[CTRL] commutator subgroup of SL(2,5) has order {len(grown)} -> "
      f"{'PERFECT: the golden end admits NO nontrivial 1-dim characters' if len(grown) == len(S) else 'NOT PERFECT'}")
assert len(grown) == len(S)

print()
print("[V3] VERDICT INPUTS:")
print("  link 1 (field -> group): the Z/3 quotient's characters take values EXACTLY")
print("    in <omega> = mu_3, the field's own cube-root group inside mu_6.")
print("  link 2 (group -> diagram): tensoring by those characters IS the affine-E6")
print("    rotation (computed McKay graph; order-3 automorphism fixing the center).")
print("  link 3 (diagram -> trit): center-deletion = su(3)^3; the rotation permutes")
print("    the three A2 factors in one 3-cycle = the banked factor rotation (B897).")
print("  CONTROL: SL(2,5) perfect -> the identical construction on the E8 end yields")
print("    NOTHING -- the carry is discriminating, not generic (the B757 shape fails")
print("    to apply: this is a functorial chain with a control, not a conjugacy")
print("    coincidence).")
print("==== B1042 compute done ====")
