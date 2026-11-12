#!/usr/bin/env python3
"""WP-1.8, first step, on main's own code: what the ladder's rule gives, what the agy lane's lattice-glue chain gives,
and what in each is supplied.

Exact arithmetic throughout: integers, fractions, and the Eisenstein integers for one affine representation.

PART 1, THE LADDER (the foundation's F-MC, the rule R1).  The moves' quotients by the N-th power of T are the triangle
groups (2, 3, N) = <S, T | S^2, (ST)^3, T^N>.  They are finite for N = 2, 3, 4, 5, of orders 6, 12, 24, 60, which are
the orders of PSL(2, Z/N); at N = 6 the group is infinite.  The lifts SL(2, Z/N) at N = 3, 4, 5 have the orders 24,
48, 120 of the binary tetrahedral, octahedral and icosahedral groups, whose McKay diagrams are E6, E7, E8.

PART 2, THE CONTAINER.  The diagram of E8 holds those of E7 and E6 as connected pieces, and no connected piece of the
diagrams of E6 or E7 is E8.  So among the three, E8 is the one that holds every rung's diagram.  That a single algebra
must hold them all is the rule's own clause, adopted by a ruling; nothing here derives it.

PART 3, THE GLUE (the agy lane's chain, read through main's mask, and re-derived here from the statement).  From the
root lattice D4 (24 roots, determinant 4): two copies have 48 roots and determinant 16; with the diagonal vector class
they are D8 (112 roots, determinant 4); with the spinor class as well they are an even lattice of determinant 1 with
240 roots, which is E8.  MAIN ADDS: the glue is not one more choice.  The classes of D4 are four, and its three
non-zero classes are permuted by a group of order six; the subgroups of order four of the classes of two copies on
which the norm form vanishes are exactly six, one for each such permutation, and EVERY one of them gives an even
lattice of determinant 1 with 240 roots.  So what is supplied is: the lattice D4, two copies of it, and that the
whole be even and self-dual.  Given those three, E8 is forced.

HOW IT COULD FAIL: the planted cases at the end.
"""
import itertools, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:200]) if detail else ""))

# =================================================================================================== 1. the ladder
def triangle_order(N, cap=5000):
    """the order of <S, T | S^2, (ST)^3, T^N> by enumerating cosets of the trivial subgroup (Todd-Coxeter, HLT style, small);
    returns None if more than `cap` cosets are needed"""
    from sympy.combinatorics.free_groups import free_group
    from sympy.combinatorics.fp_groups import FpGroup
    F, S, T = free_group("S, T")
    G = FpGroup(F, [S ** 2, (S * T) ** 3, T ** N])
    try:
        C = G.coset_enumeration([], max_cosets=cap)
        C.compress()
        return len(C.table)
    except Exception:
        return None

def psl_order(N):
    els = set()
    for a, b, c, d in itertools.product(range(N), repeat=4):
        if (a * d - b * c) % N == 1:
            m = (a, b, c, d); neg = tuple((-x) % N for x in m)
            els.add(min(m, neg))
    return len(els)

def sl_order(N):
    return sum(1 for a, b, c, d in itertools.product(range(N), repeat=4) if (a * d - b * c) % N == 1)

orders = {N: triangle_order(N) for N in (2, 3, 4, 5)}
check("1: the quotients of the moves by the N-th power of T have orders 6, 12, 24, 60 at N = 2, 3, 4, 5", orders == {2: 6, 3: 12, 4: 24, 5: 60}, orders)
check("1: these are the orders of PSL(2, Z/N)", {N: psl_order(N) for N in (2, 3, 4, 5)} == orders)
# N = 6: an affine representation over the Eisenstein integers with a translation in its image
# an element a + b*w with w^2 = -w - 1; an affine map z -> u z + t is the pair (u, t)
def emul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1])
def eadd(x, y): return (x[0] + y[0], x[1] + y[1])
ONE, ZERO, W = (1, 0), (0, 0), (0, 1)
def comp(f, g):                                   # (f o g)(z) = f(g(z))
    return (emul(f[0], g[0]), eadd(emul(f[0], g[1]), f[1]))
IDm = (ONE, ZERO)
def power(f, n):
    out = IDm
    for _ in range(n): out = comp(out, f)
    return out
Sm = ((-1, 0), ONE)                               # z -> -z + 1: a half turn about 1/2
Um = (W, ZERO)                                    # z -> w z: a third of a turn about 0; U = S T
Tm = comp(Sm, Um)                                 # T = S^-1 U = S U
check("1: at N = 6 there is a representation by motions of the plane: S of order 2, ST of order 3, T of order 6",
      power(Sm, 2) == IDm and power(Um, 3) == IDm and power(Tm, 6) == IDm and all(power(Tm, k) != IDm for k in range(1, 6)))
tr = comp(comp(Sm, Um), comp(Sm, power(Um, 2)))   # S U S U^-1
check("1: and its image holds a translation that is not the identity, so the group (2, 3, 6) is infinite", tr[0] == ONE and tr[1] != ZERO, tr)
check("1: the lifts SL(2, Z/N) at N = 3, 4, 5 have the orders 24, 48, 120 of 2T, 2O, 2I", [sl_order(N) for N in (3, 4, 5)] == [24, 48, 120])

# ================================================================================================= 2. the container
def diagram(kind):
    """the Dynkin diagram of E_n as a set of edges on nodes 0..n-1: a chain 0-1-...-(n-2) with node n-1 joined to node 2"""
    n = int(kind[1])
    return n, {(i, i + 1) for i in range(n - 2)} | {(2, n - 1)}
def connected(nodes, edges):
    nodes = set(nodes)
    if not nodes: return False
    seen, stack = set(), [next(iter(nodes))]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x)
        stack += [b if a == x else a for a, b in edges if (a == x or b == x) and a in nodes and b in nodes]
    return seen == nodes
def canon(nodes, edges):
    """a canonical form of the induced subgraph, by the sorted degree sequence with the sorted distances from the branch node"""
    nodes = sorted(nodes); E = [(a, b) for a, b in edges if a in nodes and b in nodes]
    deg = {x: sum(1 for e in E if x in e) for x in nodes}
    best = None
    for perm in itertools.permutations(range(len(nodes))):
        m = {x: perm[i] for i, x in enumerate(nodes)}
        key = tuple(sorted(tuple(sorted((m[a], m[b]))) for a, b in E))
        best = key if best is None or key < best else best
    return (len(nodes), best)
def pieces(kind, size):
    n, E = diagram(kind)
    return {canon(c, E) for c in itertools.combinations(range(n), size) if connected(c, E)}
e6, e7, e8 = (canon(range(diagram(k)[0]), diagram(k)[1]) for k in ("E6", "E7", "E8"))
check("2: the diagram of E8 holds those of E7 and E6 as connected pieces", e7 in pieces("E8", 7) and e6 in pieces("E8", 6))
check("2: and E7 holds E6, while neither holds E8", e6 in pieces("E7", 6) and e8 not in pieces("E7", 7) | pieces("E6", 6))

# ====================================================================================================== 3. the glue
def norm(v): return sum(x * x for x in v)
def add(u, v): return tuple(a + b for a, b in zip(u, v))
H = Fr(1, 2)
D4_CLASSES = {"0": (Fr(0),) * 4, "v": (Fr(1), Fr(0), Fr(0), Fr(0)), "s": (H, H, H, H), "c": (H, H, H, -H)}
def in_D4(v): return all(x.denominator == 1 for x in v) and sum(v) % 2 == 0
def _block_candidates(rep):
    """the vectors of norm at most 2 in the block's coset rep + D4, as (vector, norm): an integer block of norm 0, 1 or 2,
    or a block of four halves, of norm 1.  (A coset vector of larger norm cannot be part of a vector of norm 2.)"""
    out = []
    if all(x.denominator == 1 for x in rep):
        ints = [(0, 0, 0, 0)]
        for i in range(4):
            for s1 in (1, -1):
                v = [0, 0, 0, 0]; v[i] = s1; ints.append(tuple(v))
                for j in range(i + 1, 4):
                    for s2 in (1, -1):
                        w = [0, 0, 0, 0]; w[i] = s1; w[j] = s2; ints.append(tuple(w))
        cands = [tuple(Fr(x) for x in v) for v in ints]
    else:
        cands = [tuple(Fr(sg, 2) for sg in signs) for signs in itertools.product((1, -1), repeat=4)]
    for v in cands:
        if in_D4(tuple(a - b for a, b in zip(v, rep))):
            out.append((v, norm(v)))
    return out


def roots_of(cosets, dim):
    """the vectors of norm 2 in the union of the cosets rep + (D4 in each block of four coordinates)"""
    out = set()
    for rep in cosets:
        blocks = [_block_candidates(rep[i:i + 4]) for i in range(0, dim, 4)]
        for combo in itertools.product(*blocks):
            if sum(n for v, n in combo) == 2:
                out.add(tuple(x for v, n in combo for x in v))
    return out
d4_roots = roots_of([D4_CLASSES["0"]], 4)
brute = {v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0 and sum(x * x for x in v) == 2}
check("3: the 24 roots of D4 are the same when every integer vector with coordinates from -2 to 2 is listed", brute == {tuple(int(x) for x in v) for v in d4_roots} and len(brute) == 24)
check("3: D4 has 24 roots and four classes, the three non-zero ones of norm 1", len(d4_roots) == 24 and [norm(D4_CLASSES[k]) for k in "vsc"] == [1, 1, 1])
# the classes form the group (Z/2)^2: v + s = c up to D4
check("3: the classes of D4 form a group of order four: v + s is in the class of c", in_D4(tuple(a + b - c for a, b, c in zip(D4_CLASSES["v"], D4_CLASSES["s"], D4_CLASSES["c"]))))
names = ["0", "v", "s", "c"]
def cls_add(x, y):
    if x == "0": return y
    if y == "0": return x
    if x == y: return "0"
    return ({"v", "s", "c"} - {x, y}).pop()
q = {"0": 0, "v": 1, "s": 1, "c": 1}                                  # the norm of a class, mod 2
pairs = [(x, y) for x in names for y in names]                        # the sixteen classes of D4 + D4
def padd(a, b): return (cls_add(a[0], b[0]), cls_add(a[1], b[1]))
def qq(a): return (q[a[0]] + q[a[1]]) % 2
subgroups = set()
for a, b in itertools.combinations([p for p in pairs if p != ("0", "0")], 2):
    Hs = frozenset({("0", "0"), a, b, padd(a, b)})
    if len(Hs) == 4: subgroups.add(Hs)
iso = [Hs for Hs in subgroups if all(qq(x) == 0 for x in Hs)]
check("3: the classes of two copies have 35 subgroups of order four, and the norm vanishes on exactly six of them", (len(subgroups), len(iso)) == (35, 6))
graphs = []
for perm in itertools.permutations("vsc"):
    sig = dict(zip("vsc", perm)); sig["0"] = "0"
    graphs.append(frozenset((x, sig[x]) for x in names))
check("3: the six are the graphs of the six permutations of the three non-zero classes", set(iso) == set(graphs))
def lattice_facts(Hs):
    reps = [D4_CLASSES[a] + D4_CLASSES[b] for a, b in Hs]
    r = roots_of(reps, 8)
    even = all(norm(rep) % 2 == 0 for rep in reps)                    # the norm is even on a whole coset once it is on its representative and on the roots
    det = Fr(16, len(Hs) ** 2)
    return {"roots": len(r), "even": even, "determinant": det}
facts = [lattice_facts(Hs) for Hs in graphs]
check("3: every one of the six gives an even lattice of determinant 1 with 240 roots", all(f == {"roots": 240, "even": True, "determinant": 1} for f in facts), facts[0])
two = lattice_facts(frozenset({("0", "0")})); d8 = lattice_facts(frozenset({("0", "0"), ("v", "v")}))
check("3: two copies alone have 48 roots and determinant 16; with the diagonal vector class, 112 roots and determinant 4", (two["roots"], two["determinant"], d8["roots"], d8["determinant"]) == (48, 16, 112, 4), (two, d8))
ident = frozenset((x, x) for x in names)
check("3: the lane's chain is the identity permutation: its lattice has the 112 integer roots and 128 with half-integer coordinates",
      (lambda r: (sum(1 for v in r if all(x.denominator == 1 for x in v)), sum(1 for v in r if all(x.denominator == 2 for x in v))))(roots_of([D4_CLASSES[a] + D4_CLASSES[b] for a, b in ident], 8)) == (112, 128))
check("3: a class of norm 1 added to the whole makes it odd: the vector class of D8 does not glue", norm(D4_CLASSES["v"] + D4_CLASSES["0"]) == 1)

# ========================================================================================================= planted
bad = frozenset({("0", "0"), ("v", "0"), ("0", "v"), ("v", "v")})
check("planted: a subgroup of order four on which the norm does not vanish gives a lattice that is not even", bad in subgroups and bad not in iso and lattice_facts(bad)["even"] is False)
check("planted: at N = 6 the enumeration of cosets does not close within 3,000, as it must not for an infinite group", triangle_order(6, cap=3000) is None)
check("planted: the diagram of D8 does not hold that of E8",
      e8 not in {canon(c, {(i, i + 1) for i in range(6)} | {(5, 7)}) for c in itertools.combinations(range(8), 8)})
res = {"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]], "orders of the triangle groups": orders,
       "subgroups of order four": len(subgroups), "on which the norm vanishes": len(iso)}
(HERE / "the_parent_on_main.json").write_text(json.dumps(res, indent=1, default=str) + "\n", encoding="utf-8")
print("\n%d checks, %d failing" % (len(CHECKS), len(res["failing"])))
sys.exit(1 if res["failing"] else 0)
