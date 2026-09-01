#!/usr/bin/env python3
"""R02 blind recomputation, part 1: group/McKay foundations (B1032 / B997-adjacent half).

Written BLIND: no repo verification scripts were read before this file.

Claims to recompute independently:
  (a1) SL(2,3) has order 24, a UNIQUE involution, is isomorphic to the binary
       tetrahedral group 2T (unit quaternion model), and the McKay graph of its
       defining 2-dim spin rep is affine E6.
  (a2) SL(2,5) has order 120, a UNIQUE involution, is isomorphic to the binary
       icosahedral group 2I, and the McKay graph of its 2-dim spin rep is affine E8.
  (a3) SL(2,Z/4) has order 48 and SEVEN involutions, while the binary octahedral
       group 2O (order 48) has ONE — hence SL(2,Z/4) is NOT 2O.
  (b-foundation, B1032 V1/V2):
       trace set of V2(2T) = {-2,-1,0,1,2};
       trace set of V2(2I) = {-2,-phi,-1,-1/phi,0,1/phi,1,phi,2};
       five tones |tr V2(2I)|/2 in {0, 1/(2phi), 1/2, phi/2, 1} with ELEMENT census
       30/24/40/24/2 over the 120 elements;
       mirror menu |tr V2(2T)/2|*|tr V2(2I)/2| = 8 magnitudes
       {0, 1/4, 1/(4phi), 1/2, 1/(2phi), phi/4, phi/2, 1}.

All group arithmetic exact (F_q matrices; quaternions over Q(sqrt d) with Fractions).
Character tables via Burnside-Dixon: class constants exact, eigenvectors numeric,
McKay adjacency rounded to integers then re-verified exactly against dimension
identities (A d = 2 d, sum d_i^2 = |G|) and graph-isomorphism to the affine diagrams.

Control (exclusion claim a3): the involution counter must FIND the planted 7
involutions in SL(2,Z/4) and exactly 1 in 2O built independently over Q(sqrt2).
"""
import itertools, json, random
from fractions import Fraction as Fr

random.seed(2)

# ---------- exact quadratic field Q(sqrt d): elements (a, b) = a + b*sqrt(d) ----------
class Qd:
    __slots__ = ('a','b','d')
    def __init__(self, a, b, d):
        self.a = Fr(a); self.b = Fr(b); self.d = d
    def __add__(s,o): return Qd(s.a+o.a, s.b+o.b, s.d)
    def __sub__(s,o): return Qd(s.a-o.a, s.b-o.b, s.d)
    def __neg__(s): return Qd(-s.a, -s.b, s.d)
    def __mul__(s,o): return Qd(s.a*o.a + s.d*s.b*o.b, s.a*o.b + s.b*o.a, s.d)
    def __eq__(s,o): return s.a==o.a and s.b==o.b and s.d==o.d
    def __hash__(s): return hash((s.a, s.b, s.d))
    def float(s):
        import math
        return float(s.a) + float(s.b)*math.sqrt(s.d)
    def __repr__(s):
        return f"({s.a}+{s.b}*sqrt{s.d})"

def qz(d): return Qd(0,0,d)
def qo(d): return Qd(1,0,d)

# ---------- exact quaternions over Q(sqrt d) ----------
class Quat:
    __slots__ = ('w','x','y','z')
    def __init__(self, w,x,y,z): self.w=w; self.x=x; self.y=y; self.z=z
    def __mul__(p,q):
        return Quat(
            p.w*q.w - p.x*q.x - p.y*q.y - p.z*q.z,
            p.w*q.x + p.x*q.w + p.y*q.z - p.z*q.y,
            p.w*q.y - p.x*q.z + p.y*q.w + p.z*q.x,
            p.w*q.z + p.x*q.y - p.y*q.x + p.z*q.w)
    def __neg__(p): return Quat(-p.w,-p.x,-p.y,-p.z)
    def conj(p): return Quat(p.w, -p.x, -p.y, -p.z)
    def key(p): return (p.w.a,p.w.b,p.x.a,p.x.b,p.y.a,p.y.b,p.z.a,p.z.b)
    def __eq__(p,q): return p.key()==q.key()
    def __hash__(p): return hash(p.key())
    def norm(p): return p.w*p.w + p.x*p.x + p.y*p.y + p.z*p.z

def quat(d, w,x,y,z):
    def c(v):
        return v if isinstance(v, Qd) else Qd(v,0,d)
    return Quat(c(w),c(x),c(y),c(z))

# ---------- generic finite-group utilities (elements hashable, mul callable) ----------
def close_group(gens, mul):
    elems = set(gens); frontier = list(gens)
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                for p in (mul(g,h),):
                    if p not in elems:
                        elems.add(p); new.append(p)
        frontier = new
    return elems

def element_order(g, mul, ident):
    p = g; n = 1
    while p != ident:
        p = mul(p,g); n += 1
        if n > 10**6: raise RuntimeError
    return n

def conjugacy_classes(elems, mul, inv):
    elems = list(elems); eset = set(elems)
    seen = set(); classes = []
    for g in elems:
        if g in seen: continue
        orb = {g}; stack=[g]
        while stack:
            x = stack.pop()
            for h in elems:
                y = mul(mul(h,x), inv(h))
                if y not in orb:
                    orb.add(y); stack.append(y)
        seen |= orb
        classes.append(sorted(orb, key=lambda e: repr(e) if not hasattr(e,'key') else str(e.key())))
    return classes

# ---------- Burnside–Dixon character table (numeric eigenvectors, exact constants) ----------
def character_table(elems, mul, inv, ident):
    import numpy as np
    classes = conjugacy_classes(elems, mul, inv)
    # identity class first
    classes.sort(key=lambda C: (len(C), 0 if ident in C else 1))
    idx = None
    for i,C in enumerate(classes):
        if ident in C: idx = i
    classes = [classes[idx]] + [C for i,C in enumerate(classes) if i != idx]
    r = len(classes)
    which = {}
    for i,C in enumerate(classes):
        for g in C: which[g] = i
    reps = [C[0] for C in classes]
    n = len(elems)
    # class constants c[i][j][k] = #{(x,y) in Ci x Cj : x y = z_k}
    M = [ [[0]*r for _ in range(r)] for _ in range(r) ]
    for i,Ci in enumerate(classes):
        for k,zk in enumerate(reps):
            # count x in Ci with x^{-1} z_k in Cj
            for x in Ci:
                j = which[ mul(inv(x), zk) ]
                M[i][k][j] += 1   # (M_i)_{k,j} wait orient below
    # We need matrices N_i with (N_i)_{j,k} = c_{ij}^k acting on vector (omega_k):
    # omega_i * omega_j = sum_k c_{ij}^k omega_k.
    # c_{ij}^k = #{(x,y) in Ci x Cj: xy = z_k} = #{x in Ci : x^{-1} z_k in Cj}.
    # Above, M[i][k][j] counts x in Ci with x^{-1} z_k in Cj  -> c_{ij}^k = M[i][k][j].
    Ns = []
    for i in range(r):
        Ni = np.zeros((r,r), dtype=complex)
        for j in range(r):
            for k in range(r):
                Ni[j,k] = M[i][k][j]
        Ns.append(Ni)
    # random real combination -> distinct eigenvalues generically
    for attempt in range(20):
        coeffs = [random.random() for _ in range(r)]
        A = sum(c*Ni for c,Ni in zip(coeffs,Ns))
        w, V = np.linalg.eig(A)
        if min(abs(w[a]-w[b]) for a in range(r) for b in range(a+1,r)) > 1e-8:
            break
    chars = []
    sizes = [len(C) for C in classes]
    for col in range(r):
        v = V[:,col]
        v = v / v[0]     # omega on identity class = 1
        # chi(1) = sqrt( n / sum_k |v_k|^2/|C_k| )
        s = sum(abs(v[k])**2/sizes[k] for k in range(r))
        d = (n/s)**0.5
        chi = [d*v[k]/sizes[k] for k in range(r)]
        chars.append(chi)
    return classes, reps, sizes, chars

def mckay_adjacency(classes, sizes, chars, chi2_vals, n):
    """a_ij = <chi2 * chi_i, chi_j> exact-integer (rounded from high-accuracy floats)."""
    r = len(classes)
    A = [[0]*r for _ in range(r)]
    for i in range(r):
        for j in range(r):
            s = sum(sizes[k]*chi2_vals[k]*chars[i][k]*chars[j][k].conjugate()
                    for k in range(r))/n
            a = round(s.real)
            assert abs(s - a) < 1e-6, (i,j,s)
            A[i][j] = a
    return A

def graph_iso(A, dimsA, B, dimsB):
    """brute-force iso between labelled (by dim) undirected multigraphs"""
    r = len(A)
    if sorted(dimsA) != sorted(dimsB): return None
    # backtracking
    perm = [None]*r; used=[False]*r
    def ok(i, p):
        for i2 in range(i):
            if A[i][i2] != B[p][perm[i2]] or A[i2][i] != B[perm[i2]][p]:
                return False
        return A[i][i] == B[p][p]
    def bt(i):
        if i == r: return True
        for p in range(r):
            if not used[p] and dimsA[i]==dimsB[p] and ok(i,p):
                used[p]=True; perm[i]=p
                if bt(i+1): return True
                used[p]=False; perm[i]=None
        return False
    return perm if bt(0) else None

# ================= SL(2, Z/m) =================
def sl2(m):
    els = []
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    if (a*d - b*c) % m == 1 % m:
                        els.append((a,b,c,d))
    return els

def sl2_mul(m):
    def mul(p,q):
        a,b,c,d = p; e,f,g,h = q
        return ((a*e+b*g)%m,(a*f+b*h)%m,(c*e+d*g)%m,(c*f+d*h)%m)
    return mul

def sl2_inv(m):
    def inv(p):
        a,b,c,d = p
        return (d%m, (-b)%m, (-c)%m, a%m)
    return inv

def involutions(els, mul, ident):
    return [g for g in els if g != ident and mul(g,g) == ident]

# ================= quaternion groups 2T, 2O, 2I =================
def build_2T():
    d = 5  # field choice irrelevant for 2T (rational entries)
    E = []
    for signs in itertools.product([1,-1],repeat=1):
        pass
    units = []
    for i in range(4):
        for s in (1,-1):
            v = [0,0,0,0]; v[i] = s
            units.append(quat(d, *v))
    half = []
    for s in itertools.product([Fr(1,2),Fr(-1,2)],repeat=4):
        half.append(quat(d, *s))
    E = units + half
    assert len(set(E)) == 24
    return E, d

def build_2O():
    d = 2
    T,_ = build_2T()
    # re-embed 2T coefficients into Q(sqrt2)
    T2 = [quat(d, q.w.a, q.x.a, q.y.a, q.z.a) for q in T]
    h = Qd(0, Fr(1,2), d)   # 1/sqrt2 = sqrt2/2
    extra = []
    for (i,j) in itertools.combinations(range(4),2):
        for si in (1,-1):
            for sj in (1,-1):
                v = [qz(d)]*4
                v[i] = Qd(0, Fr(si,2), d); v[j] = Qd(0, Fr(sj,2), d)
                extra.append(Quat(*v))
    E = T2 + extra
    assert len(set(E)) == 48, len(set(E))
    return E, d

def build_2I():
    d = 5
    T,_ = build_2T()
    phi   = Qd(Fr(1,2), Fr(1,2), d)     # (1+sqrt5)/2
    iphi  = Qd(Fr(-1,2), Fr(1,2), d)    # (sqrt5-1)/2 = 1/phi
    one   = qo(d); zero = qz(d)
    half  = Qd(Fr(1,2),0,d)
    vals = [zero, one, iphi, phi]       # times 1/2 with even permutations
    evens = [p for p in itertools.permutations(range(4))
             if sum(1 for a in range(4) for b in range(a+1,4) if p[a]>p[b]) % 2 == 0]
    extra = set()
    for p in evens:
        base = [vals[p.index(i)] for i in range(4)]  # place 0,1,1/phi,phi by perm
        # base[j] = vals[k] where p[k] = j  -> equivalent formulations; just permute directly:
        base = [vals[p[i]] for i in range(4)]
        for signs in itertools.product([1,-1],repeat=4):
            v = []
            for c,s in zip(base, signs):
                c2 = Qd(c.a*Fr(1,2)*s, c.b*Fr(1,2)*s, d)
                v.append(c2)
            extra.add(Quat(*v))
    E = list(set(T) | extra)
    return E, d

def quat_group_checks(E, name):
    ident = E[0]
    for q in E:
        if q.key() == quat(5,1,0,0,0).key() or (q.w.a==1 and q.w.b==0 and q.x.a==0 and q.x.b==0 and q.y.a==0 and q.y.b==0 and q.z.a==0 and q.z.b==0):
            ident = q
    mul = lambda p,q: p*q
    inv = lambda p: p.conj()   # unit quaternions
    # closure
    S = set(E)
    for a in random.sample(E, min(len(E),30)):
        for b in random.sample(E, min(len(E),30)):
            assert a*b in S, f"{name} not closed"
    # norms
    for q in E:
        nn = q.norm()
        assert nn.a == 1 and nn.b == 0, f"{name} non-unit"
    return ident, mul, inv

# ---------- explicit isomorphism search ----------
def find_isomorphism(elsA, mulA, invA, identA, elsB, mulB, invB, identB):
    """Try to find iso A -> B. Returns dict or None. Small groups only."""
    # find generating pair of A
    elsA = list(elsA); elsB = list(elsB)
    ordA = {g: element_order(g, mulA, identA) for g in elsA}
    ordB = {g: element_order(g, mulB, identB) for g in elsB}
    genpair = None
    for g1 in elsA:
        for g2 in elsA:
            gen = close_group({g1,g2}, mulA)
            if len(gen) == len(elsA):
                genpair = (g1,g2); break
        if genpair: break
    assert genpair, "no generating pair"
    g1,g2 = genpair
    cands1 = [b for b in elsB if ordB[b]==ordA[g1]]
    cands2 = [b for b in elsB if ordB[b]==ordA[g2]]
    for h1 in cands1:
        for h2 in cands2:
            # BFS word extension with consistency check
            img = {identA: identB, g1: h1, g2: h2}
            if ordA[g1]==1 or ordA[g2]==1: continue
            frontier = [g1,g2]; ok = True
            while frontier and ok:
                nf = []
                for a in frontier:
                    for s,hs in ((g1,h1),(g2,h2)):
                        na = mulA(a,s); nb = mulB(img[a],hs)
                        if na in img:
                            if img[na] != nb: ok=False; break
                        else:
                            img[na] = nb; nf.append(na)
                    if not ok: break
                frontier = nf
            if not ok or len(img) != len(elsA): continue
            if len(set(img.values())) != len(elsB): continue
            # full homomorphism check
            good = True
            for a in elsA:
                for b in elsA:
                    if img[mulA(a,b)] != mulB(img[a], img[b]):
                        good = False; break
                if not good: break
            if good:
                return img
    return None

# ================= run everything =================
out = {}

# ---- SL(2,3) ----
E3 = sl2(3); m3, i3 = sl2_mul(3), sl2_inv(3); id3 = (1,0,0,1)
inv3 = involutions(E3, m3, id3)
out['SL23'] = {'order': len(E3), 'num_involutions': len(inv3),
               'involutions': inv3}

# ---- SL(2,5) ----
E5 = sl2(5); m5, i5 = sl2_mul(5), sl2_inv(5); id5 = (1,0,0,1)
inv5 = involutions(E5, m5, id5)
out['SL25'] = {'order': len(E5), 'num_involutions': len(inv5), 'involutions': inv5}

# ---- SL(2,Z/4) ----
E4 = sl2(4); m4, i4 = sl2_mul(4), sl2_inv(4); id4 = (1,0,0,1)
inv4 = involutions(E4, m4, id4)
out['SL2Z4'] = {'order': len(E4), 'num_involutions': len(inv4), 'involutions': inv4}

# ---- quaternion models ----
T, dT = build_2T(); idT, mT, invT = quat_group_checks(T, '2T')
O, dO = build_2O(); idO, mO, invO = quat_group_checks(O, '2O')
I2, dI = build_2I(); idI, mI, invI = quat_group_checks(I2, '2I')
out['2T'] = {'order': len(T), 'num_involutions': len(involutions(T, mT, idT))}
out['2O'] = {'order': len(O), 'num_involutions': len(involutions(O, mO, idO))}
out['2I'] = {'order': len(I2), 'num_involutions': len(involutions(I2, mI, idI))}

# ---- isomorphisms ----
isoT = find_isomorphism(E3, m3, i3, id3, T, mT, invT, idT)
out['SL23_iso_2T'] = isoT is not None
isoI = find_isomorphism(E5, m5, i5, id5, I2, mI, invI, idI)
out['SL25_iso_2I'] = isoI is not None
# SL(2,Z/4) vs 2O: involution counts differ -> not isomorphic (invariant).
out['SL2Z4_vs_2O'] = {
    'orders_equal': len(E4) == len(O),
    'involutions_SL2Z4': len(inv4), 'involutions_2O': len(involutions(O, mO, idO)),
    'isomorphic': None}
# direct confirmation (control): the iso-searcher itself must FAIL here
isoO = find_isomorphism(E4, m4, i4, id4, O, mO, invO, idO)
out['SL2Z4_vs_2O']['isomorphic'] = isoO is not None

# ---- trace sets and value menus (exact over Q(sqrt5)) ----
def trace_half(q):  # tr V2 / 2 = Re q  (exact Qd)
    return q.w
def dbl(t): return Qd(2*t.a, 2*t.b, t.d)
trT = sorted({dbl(trace_half(q)).float() for q in T})
trI_vals = sorted({ (dbl(trace_half(q)).a, dbl(trace_half(q)).b) for q in I2 })
out['traceset_2T'] = trT
out['traceset_2I_exact_a_plus_b_sqrt5'] = [[str(a),str(b)] for a,b in trI_vals]
out['traceset_2I_floats'] = sorted({ (Qd(a,b,5)).float() for a,b in trI_vals })

# five tones |tr|/2 with element census
from collections import Counter
tone_census = Counter()
for q in I2:
    t = trace_half(q)   # in [-1,1]
    v = (abs(t.a) if t.b==0 else None)
    # canonical |a + b sqrt5|: evaluate sign numerically (exact would compare a^2 vs 5b^2)
    x = t.float()
    key = (abs(t.a), abs(t.b)) if (t.a*t.b >= 0 or t.a == 0 or t.b == 0) else None
    # safer: use exact abs: if x < 0 negate exactly
    tt = t if x >= 0 else Qd(-t.a, -t.b, 5)
    tone_census[(tt.a, tt.b)] += 1
out['five_tones_census'] = { f"{a}+{b}*sqrt5": c for (a,b),c in sorted(tone_census.items(), key=lambda kv: (Qd(kv[0][0],kv[0][1],5)).float()) }

# mirror menu |trT/2| * |trI/2| over element pairs
mirror = set()
for qt in T:
    for qi in I2:
        a = trace_half(qt); b = trace_half(qi)
        x = a.float()*b.float()
        prod = a*b
        if x < 0: prod = Qd(-prod.a, -prod.b, 5)
        mirror.add((prod.a, prod.b))
out['mirror_menu_exact'] = sorted([f"{a}+{b}*sqrt5" for a,b in mirror],
                                  key=lambda s: 0)
out['mirror_menu_floats'] = sorted({ Qd(a,b,5).float() for a,b in mirror })
out['mirror_menu_size'] = len(mirror)

# ---- McKay graphs ----
def run_mckay(E, mul, inv, ident, name):
    classes, reps, sizes, chars = character_table(E, mul, inv, ident)
    dims = [round(c[0].real) for c in chars]
    assert sum(d*d for d in dims) == len(E)
    chi2 = [ 2*reps[k].w.float() for k in range(len(reps)) ]  # tr V2 on class reps
    A = mckay_adjacency(classes, sizes, chars, chi2, len(E))
    # exact identity check: A d = 2 d
    for i in range(len(dims)):
        assert sum(A[i][j]*dims[j] for j in range(len(dims))) == 2*dims[i], name
    return A, dims, sizes

A_T, dims_T, sizes_T = run_mckay(T, mT, invT, idT, '2T')
A_I, dims_I, sizes_I = run_mckay(I2, mI, invI, idI, '2I')

out['2T_irrep_dims'] = sorted(dims_T)
out['2T_class_sizes'] = sorted(sizes_T)
out['2I_irrep_dims'] = sorted(dims_I)
out['2I_class_sizes'] = sorted(sizes_I)
out['2T_mckay_adjacency'] = A_T
out['2I_mckay_adjacency'] = A_I

# affine E6: nodes dims 3,2,2,2,1,1,1 with edges 3-2 (x3), 2-1 pairs
E6_dims = [3,2,2,2,1,1,1]
E6_adj = [[0]*7 for _ in range(7)]
for (a,b) in [(0,1),(0,2),(0,3),(1,4),(2,5),(3,6)]:
    E6_adj[a][b] = E6_adj[b][a] = 1
# affine E8: chain 1-2-3-4-5-6-4-2 with 3 hanging off the 6
E8_dims = [1,2,3,4,5,6,4,2,3]
E8_adj = [[0]*9 for _ in range(9)]
for (a,b) in [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8)]:
    E8_adj[a][b] = E8_adj[b][a] = 1

permT = graph_iso(A_T, dims_T, E6_adj, E6_dims)
permI = graph_iso(A_I, dims_I, E8_adj, E8_dims)
out['2T_mckay_is_affine_E6'] = permT is not None
out['2I_mckay_is_affine_E8'] = permI is not None

# control for the McKay-graph instrument: it must NOT match the wrong diagram
out['control_2T_vs_E8'] = graph_iso(A_T, dims_T, E8_adj, E8_dims) is not None
out['control_2I_vs_E6'] = graph_iso(A_I, dims_I, E6_adj, E6_dims) is not None

with open(__file__.replace('blind_groups.py','blind_groups_out.json'), 'w') as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
