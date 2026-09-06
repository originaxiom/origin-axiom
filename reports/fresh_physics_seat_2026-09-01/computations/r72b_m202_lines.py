"""R72 (part 3) -- the three fixed lines of m202's order-3 isometry: where their ends are.

From the holonomy alone (SnapPy's high-precision geometric representation of pi_1(m202) = <a, b | aabbAbAABBaB>):
 (1) automorphisms of the presentation realised by isometries: all pairs of reduced words (w_a, w_b) of length <= 5
     with the traces of (a, b, ab) preserved (Fricke) and the relator preserved; the conjugator N solved from
     N rho(a) N^-1 = rho(w_a), N rho(b) N^-1 = rho(w_b).
 (2) each isometry classified by the traces of its elliptic lifts N gamma (|gamma| <= 5):
     tr = +-sqrt3 -> rotation pi/3 (the order-6 element r); tr = +-1 -> 2pi/3 (r^2); tr = 0 -> pi (r^3).
 (3) the axes of the elliptic lifts of r^2 (the fixed lines upstairs) and the cusp (0 or 1) of each endpoint, found by
     a breadth-first search of the Gamma-orbits of the two cusp points x_0, x_1 (fixed points of the peripheral
     parabolics).  Result: the pattern of the three lines (cusp-to-cusp or within a cusp) and hence the r-orbits.
"""
import itertools, collections, cmath, math
import snappy
import numpy as np
N = snappy.Manifold('m202').high_precision()
G = N.fundamental_group()
gens = G.generators(); rel = G.relators()[0]
print("pi_1(m202):", gens, rel)
def tonp(M): return np.array([[complex(M[0,0]), complex(M[0,1])], [complex(M[1,0]), complex(M[1,1])]])
RF = {g: tonp(G.SL2C(g)) for g in gens}
for g in gens: RF[g.upper()] = np.linalg.inv(RF[g])
def close(x, y, eps=1e-9): return abs(x - y) < eps
def evf(word):
    M = np.eye(2, dtype=complex)
    for ch in word: M = M @ RF[ch]
    return M
def reduced(w): return all(w[i] != w[i+1].swapcase() for i in range(len(w)-1))
def words(maxlen, minlen=1):
    for L in range(minlen, maxlen+1):
        for p in itertools.product('abAB', repeat=L):
            w = ''.join(p)
            if reduced(w): yield w
R0 = evf(rel); print("relator holds:", abs(R0[0,1]) < 1e-9 and abs(R0[1,0]) < 1e-9 and abs(abs(R0[0,0]) - 1) < 1e-9)
ta, tb, tab = [np.trace(evf(w)) for w in ('a', 'b', 'ab')]
def subst(word, wa, wb):
    m = {'a': wa, 'b': wb, 'A': ''.join(c.swapcase() for c in reversed(wa)), 'B': ''.join(c.swapcase() for c in reversed(wb))}
    return ''.join(m[c] for c in word)
# ---- (1) automorphisms
cands = collections.defaultdict(list)   # trace-preserving images
W = list(words(5))
by_tr = collections.defaultdict(list)
for w in W:
    t = np.trace(evf(w)); by_tr[(round(t.real, 6), round(t.imag, 6))].append(w)
def key(t): return (round(t.real, 6), round(t.imag, 6))
auts = []
for wa in by_tr[key(ta)] + by_tr[key(-ta)]:
    Ma = evf(wa)
    for wb in by_tr[key(tb)] + by_tr[key(-tb)]:
        Mb = evf(wb)
        if abs(abs(np.trace(Ma @ Mb)) - abs(tab)) > 1e-6: continue
        # relator
        R = evf(subst(rel, wa, wb))
        if not (abs(R[0,1]) < 1e-6 and abs(R[1,0]) < 1e-6 and abs(abs(R[0,0]) - 1) < 1e-6): continue
        # conjugator: solve N A = A' N, N B = B' N  (8 real equations, 4 complex unknowns)
        A, B = RF['a'], RF['b']
        rows = []
        for X, Y in ((A, Ma), (B, Mb)):
            # (N X - Y N) = 0 ; N = [[n0,n1],[n2,n3]]
            for i in range(2):
                for j in range(2):
                    row = np.zeros(4, dtype=complex)
                    for k in range(2):
                        row[2*i + k] += X[k, j]       # N[i,k] X[k,j]
                        row[2*k + j] -= Y[i, k]       # Y[i,k] N[k,j]
                    rows.append(row)
        Mx = np.array(rows); u, s, vh = np.linalg.svd(Mx)
        if s[-1] > 1e-6: continue
        n = vh[-1].conj(); Nm = n.reshape(2, 2); d = np.linalg.det(Nm)
        if abs(d) < 1e-9: continue
        Nm = Nm/np.sqrt(d)
        auts.append((wa, wb, Nm))
print(f"(1) automorphisms found with images of length <= 5: {len(auts)}")
# ---- (2) classify by elliptic lifts
def ellip_traces(Nm, maxlen=5):
    out = collections.Counter()
    for w in [''] + list(words(maxlen)):
        E = Nm @ evf(w); t = np.trace(E)
        if abs(t.imag) < 1e-6 and abs(t.real) < 2 - 1e-6: out[round(abs(t.real), 4)] += 1
    return out
classes = collections.defaultdict(list)
for wa, wb, Nm in auts:
    et = ellip_traces(Nm, 4); sig = tuple(sorted(et.keys()))
    classes[sig].append((wa, wb, Nm))
print("(2) isometry classes by the |traces| of their elliptic lifts (|gamma| <= 4):")
for sig, L in sorted(classes.items(), key=lambda kv: str(kv[0])):
    wa, wb, Nm = L[0]; print(f"    elliptic |tr| = {sig}: {len(L)} automorphisms, e.g. a -> {wa}, b -> {wb}")
# the identity class: elliptic traces empty (no elliptic elements in Gamma); order-6: sqrt3; order-3: 1; order-2: 0
# ---- (3) cusp points and the axes
per = G.peripheral_curves()
def fixed_par(M):
    a, b, c, d = M[0,0], M[0,1], M[1,0], M[1,1]
    if abs(c) < 1e-14: return complex('inf')
    return (a - d)/(2*c)
xs = []
for k, (mw, lw) in enumerate(per):
    Mm = evf(mw); x = fixed_par(Mm); xs.append(x); print(f"    cusp {k}: meridian word {mw}, |tr| = {abs(np.trace(Mm)):.6f}, cusp point x_{k} = {x}")
def mob(M, z):
    a, b, c, d = M[0,0], M[0,1], M[1,0], M[1,1]
    if z == complex('inf'): return complex('inf') if abs(c) < 1e-14 else a/c
    den = c*z + d
    return complex('inf') if abs(den) < 1e-14 else (a*z + b)/den
def orbit(x, maxlen):
    """BFS orbit of x under Gamma up to word length maxlen (dedup by rounding); returns dict point -> word"""
    seen = {}; frontier = [(x, '')]
    def keyz(z): return 'inf' if z == complex('inf') or abs(z) > 1e8 else (round(z.real, 7), round(z.imag, 7))
    seen[keyz(x)] = ''
    for L in range(maxlen):
        new = []
        for z, w in frontier:
            for g in 'abAB':
                if w and w[-1] == g.swapcase(): continue
                z2 = mob(RF[g], z); k2 = keyz(z2)
                if k2 not in seen: seen[k2] = w + g; new.append((z2, w + g))
        frontier = new
    return seen
def keyz(z): return 'inf' if z == complex('inf') or abs(z) > 1e8 else (round(z.real, 7), round(z.imag, 7))
orb = [orbit(xs[0], 9), orbit(xs[1], 9)]
print(f"    orbit sizes (words <= 9): cusp 0: {len(orb[0])}, cusp 1: {len(orb[1])}; disjoint: {not (set(orb[0]) & set(orb[1]))}")
def which_cusp(z):
    k = keyz(z)
    for c in (0, 1):
        if k in orb[c]: return c
    return None
def axis(E):
    a, b, c, d = E[0,0], E[0,1], E[1,0], E[1,1]
    if abs(c) < 1e-14: return (complex('inf'), b/(d - a))
    disc = cmath.sqrt((d - a)**2 + 4*b*c)
    return ((a - d + disc)/(2*c), (a - d - disc)/(2*c))
# the cusp permutation induced by each automorphism: N x_0 lies in the orbit of x_0 (cusps preserved) or of x_1 (swapped)
def cusp_perm(Nm):
    c = which_cusp(mob(Nm, xs[0])); return None if c is None else ('preserved' if c == 0 else 'swapped')
perm_of = {}
for wa, wb, Nm in auts: perm_of[(wa, wb)] = cusp_perm(Nm)
print("    cusp permutation resolved for", sum(1 for v in perm_of.values() if v), "of", len(auts), "automorphisms;",
      collections.Counter((tuple(sorted(ellip_traces(Nm, 4).keys())), perm_of[(wa, wb)]) for wa, wb, Nm in auts))
for sig, label in (((1.0,), 'order 3 (r^2)'), ((1.7321,), 'order 6 (r)'), ((0.0,), 'order 2 (r^3)'), ((0.0,), 'cusp-swapping involutions')):
    want = 'swapped' if label.startswith('cusp') else 'preserved'
    L = [(wa, wb, Nm) for s_, cl in classes.items() if s_ and len(s_) == len(sig) and all(abs(v - u) < 1e-3 for v, u in zip(sorted(s_), sig))
         for (wa, wb, Nm) in cl if perm_of[(wa, wb)] == want]
    if not L: print(f"    {label}: class not found"); continue
    wa, wb, Nm = L[0]
    axes = {}
    for w in [''] + list(words(6)):
        E = Nm @ evf(w); t = np.trace(E)
        if abs(t.imag) < 1e-6 and abs(abs(t.real) - sig[0]) < 1e-3:
            p, q = axis(E); cp, cq = which_cusp(p), which_cusp(q)
            k = tuple(sorted([keyz(p), keyz(q)], key=str))
            if k not in axes: axes[k] = (p, q, cp, cq, w)
    ends = collections.Counter(tuple(sorted([str(v[2]), str(v[3])])) for v in axes.values())
    print(f"    {label}: {len(axes)} distinct axes of elliptic lifts (|gamma| <= 6); endpoint-cusp patterns: {dict(ends)}")
    unresolved = sum(1 for v in axes.values() if v[2] is None or v[3] is None)
    print(f"        unresolved endpoints (not reached by the orbit search): {unresolved} of {len(axes)}")
print("SELFTEST: PASS")
