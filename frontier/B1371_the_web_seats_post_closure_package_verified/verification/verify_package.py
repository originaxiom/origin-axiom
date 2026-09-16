#!/usr/bin/env python3
"""B1371 -- THE WEB SEAT'S POST-CLOSURE PACKAGE, VERIFIED ON THIS BENCH (2026-09-16).

The owner handed this seat the web seat's post-closure package of 2026-09-15 (four documents, thirteen scripts). The web seat has no
branch, no arc numbers and limited compute, and asked to be verified. Every claim below is re-derived with this bench's own code (not
the package's scripts), including the negatives.  Sections:
  (1)  Humbert's volume of the Bianchi orbifold and the indices of the class members (m004 12, m003 12, m202 24, s959 36, v3551 42,
       s596 30); the members outside the class (v3461, t10829, t12582) by the invariant trace field.
  (2)  The four-property table: symmetry groups, amphicheirality, order-3 elements, the 2T door (surjections onto SL(2,3)), the
       Weeks manifold's 2I door (surjections onto SL(2,5)).
  (3)  The m + s census scan: chiral + 2T door + order-3 isometry; the det(A - I) of the cusp-fixing order-3 maps; the fields.
  (4)  2T's centre versus the Kac grading: tensoring by the linear characters fixes the 3-dimensional irrep; det(Cartan E6) = 3;
       the order-3 elements of SL(2, F_3) are the unipotents and none lies in Q_8.
  (5)  Lefschetz numbers of the order-3 isometries of m202 and s959 from the action on H_1 and H_2 (this bench's instrument).
  (6)  Fox calculus: the unipotent (non-semisimple) modules over F_3 and over Q(omega) against their semisimplifications.
  (7)  The I-26 decision table's inputs: chi(M) = 0, the fixed-point counts, the cusp swap and the hexagonal shapes; s596.
  (8)  The covering negative: the degree-2 and degree-3 covers of m004 and m003; is m202 (s959) a cover of either?
  (9)  The Sol boundary m004(0,1): are all SU(2) representations reducible?  (the package says yes)
  (10) The Chern-Simons validity gate on m004(p,1), the slope law on the eight hyperbolic slopes, the homology ladder, p = 5.
  (11) The commutator trace of m004's generating pair (kappa - 2 a cube root of unity) and its Nielsen invariance.
  (12) The det(A - I) = 3 scan over the classic census (4 815 manifolds, all cusp numbers): the hits, the hexagonal counts, and the
       parity of fixed ends.
Usage: python3 verify_package.py   (about a minute)"""
import os, sys, itertools, cmath, math, warnings, time
warnings.filterwarnings("ignore")
import numpy as np
import sympy as sp
import snappy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1369_the_siblings_in_the_sm_frame", "verification"))
from family_isometries import FamilyMember, FACES, VBITS

T0 = time.time()
def stamp(): return f"[{time.time() - T0:6.0f} s]"
def vol(M): return float(M.volume())
def reduce_tau(t):
    t = complex(t)
    if t.imag < 0: t = -t
    for _ in range(500):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12: t = -1 / t
        else: break
    return t
HEX = complex(0.5, math.sqrt(3) / 2)
def hexagonal(M): return all(abs(abs(reduce_tau(s).real) - 0.5) < 1e-7 and abs(reduce_tau(s).imag - math.sqrt(3) / 2) < 1e-7 for s in M.cusp_info('shape'))   # e^{i pi/3} or e^{2 i pi/3}: the same lattice

# ---------------------------------------------------------------- (1) Humbert and the indices
print("=== (1) Humbert's formula and the indices in PSL(2, O_3) ===")
import mpmath as mp
mp.mp.dps = 30
L2 = mp.dirichlet(2, [0, 1, -1])                      # L(2, chi_{-3})
zetaK2 = mp.zeta(2) * L2
v0 = mp.mpf(3) ** mp.mpf(1.5) * zetaK2 / (4 * mp.pi ** 2)
print(f"  L(2, chi_-3) = {mp.nstr(L2, 12)}, zeta_K(2) = {mp.nstr(zetaK2, 12)}, vol(H^3/PSL(2,O_3)) = |D|^(3/2) zeta_K(2)/(4 pi^2) = {mp.nstr(v0, 12)} (the package: 0.169156934)")
v0f = float(v0)
idx = {}
for name in ["m004", "m003", "m202", "s959", "v3551", "s596", "v3461", "t10829", "t12582", "m129", "m125"]:
    M = snappy.Manifold(name); r = vol(M) / v0f
    idx[name] = r
    print(f"  {name:7s} vol {vol(M):.9f}  vol/v0 = {r:9.4f}  {'integral' if abs(r - round(r)) < 1e-6 else 'not integral'}")
print("  the shape field (= the invariant trace field of a cusped manifold, Neumann-Reid): is every tetrahedron shape in Q(sqrt-3)? (200-bit shapes, PSLQ)")
def in_Qsqrt3(z, prec_bits=200):
    """z in Q(sqrt-3) iff Re z in Q and Im z in Q sqrt 3: integer relations by PSLQ at 200 bits"""
    mp.mp.prec = prec_bits + 20
    def num(v):
        return mp.mpf(str(v).replace(' ', ''))
    x = num(z.real()) if hasattr(z, 'real') and callable(z.real) else num(z.real)
    y = num(z.imag()) if hasattr(z, 'imag') and callable(z.imag) else num(z.imag)
    def is_multiple(u, base):
        # u = (p/q) base with a small integer relation, or u = 0 (a purely imaginary or purely real shape)
        if abs(u) < mp.mpf(10) ** (-50): return True
        r = mp.pslq([u, base], maxcoeff=10 ** 9, maxsteps=10 ** 5)
        return r is not None and r[0] != 0
    return is_multiple(x, mp.mpf(1)) and is_multiple(y, mp.sqrt(3))
fields = {}
for name in ["m004", "m003", "m202", "s959", "v3551", "s596", "v3461", "t10829", "t12582", "m129"]:
    M = snappy.Manifold(name)
    shapes = M.tetrahedra_shapes('rect', bits_prec=220)
    flags = [in_Qsqrt3(z) for z in shapes]
    fields[name] = all(flags)
    print(f"    {name:7s} {len(shapes):2d} tetrahedra, shapes in Q(sqrt-3): {sum(flags)}/{len(flags)} -> {'the class of m004' if all(flags) else 'NOT the class of m004'}")
print(f"  in the class: {[n for n, f in fields.items() if f]}; outside: {[n for n, f in fields.items() if not f]} (the package: v3461, t10829, t12582 outside, 4-5 distinct shape polynomials each; s596 inside)")
vols = {}
for M in snappy.OrientableCuspedCensus:
    v = round(vol(M), 6); vols.setdefault(v, []).append(M.name())
def at_volume(k):
    return sorted(n for v, ns in vols.items() for n in ns if abs(v - k * v0f) < 2e-6)
print(f"  census manifolds of volume 12 v0 = 2 v_tet: {at_volume(12)} (the package: exactly m003 and m004)")
print(f"  census manifolds of volume 24 v0: {len(at_volume(24))} {at_volume(24)}; of volume 36 v0: {len(at_volume(36))} {at_volume(36)} (the package: 7 and 12); volume 30 v0: {at_volume(30)}; 42 v0: {at_volume(42)}")

# ---------------------------------------------------------------- finite-group tools: SL(2, p)
def sl2(p):
    els = [(a, b, c, d) for a, b, c, d in itertools.product(range(p), repeat=4) if (a * d - b * c) % p == 1]
    return els
def mulp(g, h, p):
    a, b, c, d = g; e, f, x, y = h
    return ((a * e + b * x) % p, (a * f + b * y) % p, (c * e + d * x) % p, (c * f + d * y) % p)
def invp(g, p):
    a, b, c, d = g; return (d % p, (-b) % p, (-c) % p, a % p)
def word_eval(w, img, p):
    r = (1, 0, 0, 1)
    for ch in w:
        g = img[ch.lower()]
        r = mulp(r, g if ch.islower() else invp(g, p), p)
    return r
def generated_size(gs, p, full):
    S = {(1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        x = fr.pop()
        for g in gs:
            y = mulp(x, g, p)
            if y not in S:
                S.add(y); fr.append(y)
                if len(S) == full: return full
    return len(S)
def surjections(G, p, max_gens=3):
    gens = list(G.generators()); rels = G.relators(); E = sl2(p); full = len(E)
    if len(gens) > max_gens: return None
    cnt = 0
    for img_t in itertools.product(E, repeat=len(gens)):
        img = dict(zip(gens, img_t))
        if all(word_eval(r, img, p) == (1, 0, 0, 1) for r in rels) and generated_size(img_t, p, full) == full:
            cnt += 1
    return cnt

# ---------------------------------------------------------------- (2) the four-property table
print(f"\n=== (2) the four-property table {stamp()} ===")
def sym_data(M):
    S = M.symmetry_group(); n = S.order()
    def order_of(k):
        cur = k
        for j in range(2, 25):
            cur = S.multiply_elements(cur, k)
            if cur == 0: return j
        return None
    n3 = sum(1 for k in range(1, n) if order_of(k) == 3)
    return n, S.is_amphicheiral(), n3, str(S)
table = {}
for name in ["m004", "m003(-3,1)", "m129", "m125", "m202", "s959"]:
    M = snappy.Manifold(name)
    n, amph, n3, desc = sym_data(M)
    G = M.fundamental_group()
    s2T = surjections(G, 3)
    s2I = surjections(G, 5) if name == "m003(-3,1)" else None
    table[name] = (n, amph, n3, s2T, s2I)
    print(f"  {name:11s} H_1 {str(M.homology()):>14s} |Sym| {n:3d} ({desc:>4s}) amphicheiral {str(amph):5s} order-3 elements {n3}  surjections onto 2T = SL(2,3): {s2T}" + (f"  onto 2I = SL(2,5): {s2I}" if s2I is not None else ""))
print("  the package's row: m004 (forced, achiral, 48, 0); Weeks (forced, chiral, 0 onto 2I, 2 order-3); m129/m125 (chiral, 192, 0); m202/s959 (chiral, 96/576, 2)")

# ---------------------------------------------------------------- (4) 2T's centre vs the Kac grading (group theory, own construction)
print(f"\n=== (4) 2T: the linear characters' tensoring action, the order-3 elements of SL(2, F_3), det(Cartan E6) {stamp()} ===")
# 2T as unit quaternions in SU(2): {+-1, +-i, +-j, +-k, (+-1 +-i +-j +-k)/2}
def q(a, b, c, d): return np.array([[a + b * 1j, c + d * 1j], [-c + d * 1j, a - b * 1j]])
els2T = [s * q(1, 0, 0, 0) for s in (1, -1)] + [s * q(0, 1, 0, 0) for s in (1, -1)] + [s * q(0, 0, 1, 0) for s in (1, -1)] + [s * q(0, 0, 0, 1) for s in (1, -1)]
els2T += [q(a / 2, b / 2, c / 2, d / 2) for a, b, c, d in itertools.product((1, -1), repeat=4)]
assert len(els2T) == 24
def adjoint3(g):
    # the SO(3) action on the imaginary quaternions (the 3-dimensional irrep): R_ij = (1/2) tr(sigma_i g sigma_j g^{-1})
    sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    return np.array([[0.5 * np.trace(sig[i] @ g @ sig[j] @ np.linalg.inv(g)).real for j in range(3)] for i in range(3)])
def order(g):
    x = np.eye(2)
    for k in range(1, 13):
        x = x @ g
        if np.allclose(x, np.eye(2)): return k
Q8 = [g for g in els2T if order(g) in (1, 2, 4)]
assert len(Q8) == 8
# the linear characters: 2T/Q8 = Z/3, chi(g) = omega^k where g Q8 has order k in the quotient; label cosets by the order-3 part
def coset_label(g):
    # find k in {0,1,2} with g in c^k Q8 for a fixed order-3 element c
    for k in range(3):
        x = np.linalg.matrix_power(np.linalg.inv(c3), k) @ g
        if any(np.allclose(x, h) for h in Q8): return k
c3 = next(g for g in els2T if order(g) == 3)
omega = cmath.exp(2j * math.pi / 3)
chi2 = [np.trace(g) for g in els2T]                  # the natural 2-dimensional character
chi3 = [np.trace(adjoint3(g)) for g in els2T]        # the 3-dimensional character
lin = [omega ** coset_label(g) for g in els2T]       # a non-trivial linear character
prod3 = [a * b for a, b in zip(chi3, lin)]; prod2 = [a * b for a, b in zip(chi2, lin)]
print(f"  3 (x) chi == 3 as characters: {all(abs(a - b) < 1e-9 for a, b in zip(prod3, chi3))}; 2 (x) chi == 2: {all(abs(a - b) < 1e-9 for a, b in zip(prod2, chi2))} (the package: the centre Z/3 fixes the 3-dimensional irrep and cycles the 2-dimensional ones)")
E3 = sl2(3)
order3 = [g for g in E3 if mulp(mulp(g, g, 3), g, 3) == (1, 0, 0, 1) and g != (1, 0, 0, 1)]
traces = {(g[0] + g[3]) % 3 for g in order3}
unip = all(mulp(tuple((x - y) % 3 for x, y in zip(g, (1, 0, 0, 1))), tuple((x - y) % 3 for x, y in zip(g, (1, 0, 0, 1))), 3) == (0, 0, 0, 0) for g in order3)
Q8_3 = [g for g in E3 if g == (1, 0, 0, 1) or mulp(g, g, 3) == (2, 0, 0, 2) or mulp(mulp(g, g, 3), mulp(g, g, 3), 3) == (1, 0, 0, 1) and mulp(g, g, 3) != (1, 0, 0, 1)]
print(f"  SL(2, F_3): {len(order3)} elements of order 3, traces mod 3 {traces} (= -1), all unipotent ((A - I)^2 = 0): {unip}; none of them in Q_8 (the elements of order 1, 2, 4): {not any(g in Q8_3 for g in order3)}")
cartanE6 = sp.Matrix([[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, -1], [0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 2]])
print(f"  det(Cartan E6) = {cartanE6.det()}")

# ---------------------------------------------------------------- (5) Lefschetz numbers on m202 and s959
print(f"\n=== (5) Lefschetz numbers of the isometries of m202 and s959 from H_1 and H_2 (this bench's instrument) {stamp()} ===")
def aut_order(FM, aut):
    def compose(a, b):        # a after b
        out = {}
        for ti in a:
            s, p = b[ti]; s2, p2 = a[s.Index]
            out[ti] = [s2, p2 * p]
        return out
    cur = aut
    for k in range(1, 30):
        if all(cur[ti][0].Index == ti and cur[ti][1].tuple() == (0, 1, 2, 3) for ti in cur): return k
        cur = compose(aut, cur)
def h2_action(FM, aut):
    """the action on H_2 = ker d_2 of the dual 2-complex (2-cells = edge classes), from the chain map on 1-cells"""
    G1 = FM.action_on_C1(aut)
    Z2 = FM.E.nullspace()
    if not Z2: return sp.zeros(0, 0)
    Zm = sp.Matrix.hstack(*Z2)
    # the image of a 2-cycle z: G1 * E z is E * (G2 z) for the induced signed permutation G2 on edges; we need G2
    # edges map to edges: e -> e' with sign s where G1 * E[:, e] == s * E[:, e']
    ne = FM.ne; G2 = sp.zeros(ne, ne)
    for e in range(ne):
        col = G1 * FM.E[:, e]
        found = False
        for e2 in range(ne):
            if col == FM.E[:, e2]: G2[e2, e] = 1; found = True; break
            if col == -FM.E[:, e2]: G2[e2, e] = -1; found = True; break
        assert found, "edge image not found"
    A = sp.zeros(len(Z2), len(Z2))
    left = (Zm.T * Zm).inv() * Zm.T
    for j, z in enumerate(Z2):
        x = left * (G2 * z); assert Zm * x == G2 * z
        A[:, j] = x
    return A
for name in ["m202", "s959"]:
    FM = FamilyMember(name, canonical=True)
    S = FM.M.symmetry_group()
    assert len(FM.auts) == S.order()
    # finite vertices of the retriangulation: the dual 2-complex is a spine of M minus those points, whose H_2 gains one sphere class
    # per finite vertex; an automorphism fixing a finite vertex fixes its sphere class, so tr H_2(M) = tr H_2(dual) - (fixed finite vertices)
    finite = [v.Index for v in FM.mc.Vertices if FM.mc.LinkGenera[v.Index] == 0]
    def fixed_finite(aut):
        cnt = 0
        for vi in finite:
            c = FM.mc.Vertices[vi].Corners[0]; ti, vb = c.Tetrahedron.Index, c.Subsimplex
            s2, p2 = aut[ti]
            if FM.tets[s2.Index].Class[p2.image(vb)].Index == vi: cnt += 1
        return cnt
    rows = []
    for aut in FM.auts:
        k = aut_order(FM, aut); perm = FM.cusp_permutation(aut)
        A1 = FM.action_on_H1(aut); A2 = h2_action(FM, aut)
        tr1 = A1.trace(); tr2 = (A2.trace() if A2.rows else 0) - fixed_finite(aut)
        L = 1 - tr1 + tr2
        rows.append((k, tuple(perm.values()), tr1, tr2, L))
    from collections import Counter
    b2 = len(FM.E.nullspace()) - len(finite)
    print(f"  {name}: canonical retriangulation with {len(finite)} finite vertices; b_1 {FM.b1}, b_2 {b2}; (order, cusp permutation, tr H_1, tr H_2, L(g)) with multiplicity: {sorted(Counter(rows).items())}")
    o3 = [r for r in rows if r[0] == 3]
    print(f"    order-3 isometries: {len(o3)}; their (tr H_1, tr H_2, L) = {sorted(set((r[2], r[3], r[4]) for r in o3))} (the package: tr_1 = -1 (omega, omega^2), tr_2 = 1, L = 3 = the three fixed arcs)")

# ---------------------------------------------------------------- (6) Fox calculus: unipotent modules over F_3 and over Q(omega)
print(f"\n=== (6) non-semisimple modules by Fox calculus: over F_3 and over Q(omega) {stamp()} ===")
from sympy.polys.matrices import DomainMatrix
from sympy import GF, QQ
def fox_matrices(G, rep, n, domain):
    """d1 = the Fox Jacobian (relators x generators blocks), d0 = the column of rep(g) - I; ranks over the given domain"""
    gens = list(G.generators()); rels = G.relators()
    def fox(w, var):
        D = sp.zeros(n, n); P = sp.eye(n)
        for ch in w:
            low = ch.lower(); g = rep(low)
            if ch.islower():
                if low == var: D = D + P
                P = P * g
            else:
                gi = g.inv()
                if low == var: D = D - P * gi
                P = P * gi
        return D
    d1 = sp.Matrix.vstack(*[sp.Matrix.hstack(*[fox(r, v) for v in gens]) for r in rels])
    d0 = sp.Matrix.vstack(*[rep(g) - sp.eye(n) for g in gens])
    return d1, d0, len(gens)
def rank_over(Mx, domain):
    if domain == "F3":
        dm = DomainMatrix([[GF(3)(int(x) % 3) for x in Mx.row(i)] for i in range(Mx.rows)], Mx.shape, GF(3))
        return dm.rank()
    return Mx.rank(simplify=True)
def h1_of(G, rep, n, domain):
    d1, d0, ng = fox_matrices(G, rep, n, domain)
    return ng * n - rank_over(d1, domain) - rank_over(d0, domain)
def abelianise(word, gens):
    v = [0] * len(gens)
    for ch in word:
        i = gens.index(ch.lower()); v[i] += 1 if ch.islower() else -1
    return v
for name in ["m202", "s959"]:
    M = snappy.Manifold(name); G = M.fundamental_group(); gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels])
    # all non-trivial homomorphisms H_1 -> F_3 (through the abelianisation): vectors v in F_3^gens with R v = 0 mod 3
    homs = [v for v in itertools.product(range(3), repeat=len(gens)) if any(v) and all(sum(R[i, j] * v[j] for j in range(len(gens))) % 3 == 0 for i in range(R.rows))]
    results = set()
    for v in homs:
        def rep(g, v=v):
            t = v[gens.index(g)] % 3
            return sp.Matrix([[1, t], [0, 1]])
        results.add(h1_of(G, rep, 2, "F3"))
    triv = h1_of(G, lambda g: sp.eye(2), 2, "F3")
    dimH1F3 = len(gens) - rank_over(R, "F3")
    print(f"  {name} over F_3: {len(homs)} non-trivial homomorphisms pi_1 -> F_3; h^1 of the unipotent module U(t) over them: {sorted(results)}; semisimplification (trivial 2-dim): {triv} = 2 dim H^1(M; F_3) = {2 * dimH1F3} (the package: m202 2 vs 4, s959 5 vs 6)")
    # characteristic zero: an additive character phi: pi_1 -> C with values in {0, 1, omega} on the generators, U(word) = exp(phi N)
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    ns = R.nullspace()
    found = None
    for vals in itertools.product([sp.Integer(0), sp.Integer(1), w], repeat=len(gens)):
        if all(x == 0 for x in vals): continue
        vec = sp.Matrix(vals)
        if all(sp.simplify((R * vec)[i]) == 0 for i in range(R.rows)): found = vals; break
    if found is None:
        # no {0, 1, omega}-valued additive character: take a rational one from the nullspace of the abelianised relators
        found = tuple(sp.nsimplify(x) for x in ns[0])
    if found is not None:
        out = []
        for d in ((2, 3, 4) if name == "m202" else (2,)):
            def rep(g, d=d, vals=found):
                t = vals[gens.index(g)]
                Mx = sp.zeros(d, d)
                for i in range(d):
                    for j in range(i, d): Mx[i, j] = t ** (j - i) / sp.factorial(j - i)
                return Mx
            out.append((d, h1_of(G, rep, d, "QQ"), h1_of(G, lambda g, d=d: sp.eye(d), d, "QQ")))
        print(f"  {name} over Q(omega): phi on the generators = {[str(x) for x in found]}; (dim, h^1 unipotent, h^1 trivial) = {out} (the package: m202 (2, 2, 4), (3, 2, 6), (4, 2, 8); s959 (2, 2, 4))")

# ---------------------------------------------------------------- (7) the I-26 decision table's inputs; s596
print(f"\n=== (7) the decision table's inputs: chi(M), fixed points of the order-3 maps, cusp swap, shapes {stamp()} ===")
for name in ["m004", "m202", "s959", "v3551", "s596", "v3461"]:
    M = snappy.Manifold(name); G = M.fundamental_group(); chi = 1 - len(G.generators()) + len(G.relators())
    S = M.symmetry_group(); isos = S.isometries()
    def order_of(k):
        cur = k
        for j in range(2, 25):
            cur = S.multiply_elements(cur, k)
            if cur == 0: return j
    dets = {}
    for k in range(len(isos)):
        iso = isos[k]
        if list(iso.cusp_images()) != list(range(M.num_cusps())): continue
        o = order_of(k) if k else 1
        ds = tuple(abs(int((cm[0, 0] - 1) * (cm[1, 1] - 1) - cm[0, 1] * cm[1, 0])) for cm in iso.cusp_maps())
        dets.setdefault(o, set()).add(ds)
    perms = {tuple(iso.cusp_images()) for iso in isos}
    shapes = [reduce_tau(s) for s in M.cusp_info('shape')]
    print(f"  {name:6s} chi(M) = {chi}, |Sym| {S.order()} ({S}), cusp-fixing |det(A - I)| by order {dict(sorted(dets.items()))}, cusp permutations {sorted(perms)}, reduced shapes {[f'{s.real:+.4f}{s.imag:+.4f}i' for s in shapes]} hexagonal {hexagonal(M)}")
print("  rows A-F of the table are then arithmetic: A/B/C 0; D = -(sum of fixed points) (m202, s959: 6); E one cusp (3); F = -(number of cusps)")

# ---------------------------------------------------------------- (8) the covering negative
print(f"\n=== (8) the covering negative: low-degree covers of m004 and m003 {stamp()} ===")
targets = {n: snappy.Manifold(n) for n in ["m202", "s959"]}
for base in ["m004", "m003"]:
    B = snappy.Manifold(base)
    for d in (2, 3):
        cs = B.covers(d)
        desc = [(c.num_cusps(), round(vol(c), 6), str(c.homology())) for c in cs]
        hits = {t: any(c.is_isometric_to(T) for c in cs) for t, T in targets.items() if abs(vol(T) - d * vol(B)) < 1e-6}
        print(f"  {base} degree {d}: {len(cs)} cover(s) {desc}; isometric to a target of that volume: {hits}")

# ---------------------------------------------------------------- (9) the Sol boundary m004(0,1): SU(2) representations
print(f"\n=== (9) m004(0,1): SU(2) representations through the binary dihedral groups Dic_n (n = 2..6) {stamp()} ===")
M0 = snappy.Manifold("m004(0,1)"); G0 = M0.fundamental_group(); gens0 = list(G0.generators()); rels0 = G0.relators()
print(f"  pi_1(m004(0,1)) = <{', '.join(gens0)} | {', '.join(rels0)}>, H_1 = {M0.homology()}")
def dic(n):
    """the binary dihedral group of order 4n in SU(2): <a, b | a^{2n} = 1, b^2 = a^n, b a b^{-1} = a^{-1}>"""
    a = np.array([[cmath.exp(1j * math.pi / n), 0], [0, cmath.exp(-1j * math.pi / n)]]); b = np.array([[0, -1], [1, 0]])
    els = [np.linalg.matrix_power(a, k) for k in range(2 * n)] + [np.linalg.matrix_power(a, k) @ b for k in range(2 * n)]
    return els
def wordmat(w, img):
    r = np.eye(2, dtype=complex)
    for ch in w:
        g = img[ch.lower()]
        r = r @ (g if ch.islower() else np.linalg.inv(g))
    return r
total_irr = 0
for n in range(2, 7):
    els = dic(n); irr = 0; red = 0
    for img_t in itertools.product(range(len(els)), repeat=len(gens0)):
        img = {g: els[i] for g, i in zip(gens0, img_t)}
        if all(np.allclose(wordmat(r, img), np.eye(2), atol=1e-9) for r in rels0):
            # irreducible iff the images do not commute pairwise (for a group generated by these matrices, non-abelian image)
            mats = list(img.values())
            nonab = any(not np.allclose(A @ B, B @ A, atol=1e-9) for A in mats for B in mats)
            if nonab: irr += 1
            else: red += 1
    total_irr += irr
    print(f"  Dic_{n} (order {4 * n}): homomorphisms with a non-abelian image {irr}, with an abelian image {red}")
print(f"  irreducible SU(2) representations of m004(0,1) found through binary dihedral images: {total_irr} (the package: 'every SU(2) flat connection on m004(0,1) is reducible')")
# the prediction: the monodromy A of the figure-eight fibration has det(A + I) = 5, so the characters chi of Z^2 with chi o A = chi^-1
# number |det(A + I)| - 1 = 4 non-trivial ones, giving binary dihedral representations with a_1 of order 5 or 10 -> Dic_5
A = sp.Matrix([[2, 1], [1, 1]])
print(f"  monodromy [[2,1],[1,1]]: det(A - I) = {(A - sp.eye(2)).det()} (abelian characters: H_1 = Z), det(A + I) = {(A + sp.eye(2)).det()} (characters with chi o A = chi^-1: {abs((A + sp.eye(2)).det()) - 1} non-trivial -> irreducible binary dihedral representations)")

# ---------------------------------------------------------------- (10) the Chern-Simons gate, the slope law, the homology ladder
print(f"\n=== (10) m004(p,1): solution types, volumes, Chern-Simons, homology; the slope law {stamp()} ===")
def filled(p, q):
    M = snappy.Manifold("m004")
    try: M.chern_simons()                      # seed the Chern-Simons computation on the cusped manifold, as the package does
    except Exception: pass
    M.dehn_fill((p, q)); return M
for p in range(0, 7):
    M = filled(p, 1)
    try: cs = f"{float(M.chern_simons()):+.9f}"
    except Exception: cs = "n/a"
    print(f"  p = {p}: {M.solution_type()[:34]:34s} vol {vol(M):10.7f} cs {cs:>13s} H_1 = {M.homology()}")
ok = 0; tested = 0
for (p, q) in [(5, 1), (7, 1), (7, 2), (9, 1), (5, 2), (8, 3), (11, 2), (13, 4)]:
    A_ = filled(p, q); B_ = filled(p, -q)
    hyp = A_.solution_type().startswith("all tetrahedra positively") and B_.solution_type().startswith("all tetrahedra positively")
    if not hyp: continue
    tested += 1
    try:
        s = (float(A_.chern_simons()) + float(B_.chern_simons())) % 1.0; s = min(s, 1 - s)
        ok += s < 1e-8
    except Exception as e:
        print(f"    ({p},{q}): Chern-Simons unavailable ({str(e)[:50]})")
print(f"  slope law CS(p,-q) = -CS(p,q) mod 1 on the hyperbolic slopes: {ok}/{tested} (the package: 8/8)")

# ---------------------------------------------------------------- (11) the commutator trace of m004's generating pair
print(f"\n=== (11) kappa = tr[a, b] for m004's generating pair, and Nielsen invariance {stamp()} ===")
M = snappy.Manifold("m004"); G = M.fundamental_group(); a, b = G.SL2C('a'), G.SL2C('b')
def to_np(X): return np.array([[complex(X[i, j]) for j in range(2)] for i in range(2)])
a, b = to_np(a), to_np(b)
comm = a @ b @ np.linalg.inv(a) @ np.linalg.inv(b)
kap = np.trace(comm)
print(f"  tr[a,b] = {kap:.9f}; kappa - 2 = {kap - 2:.9f}; omega = {omega:.9f}; a cube root of unity: {min(abs(kap - 2 - omega), abs(kap - 2 - omega.conjugate())) < 1e-9}")
inv = np.linalg.inv
def tr_comm(x, y): return np.trace(x @ y @ inv(x) @ inv(y))
print(f"  Nielsen moves preserve it: (b,a) {tr_comm(b, a):.6f}, (a^-1, b) {tr_comm(inv(a), b):.6f}, (ab, b) {tr_comm(a @ b, b):.6f}, (a, ab) {tr_comm(a, a @ b):.6f}")

# ---------------------------------------------------------------- (3) and (12): the census scans
print(f"\n=== (3) + (12) census scans {stamp()} ===")
census = snappy.OrientableCuspedCensus
N = len(census)
print(f"  OrientableCuspedCensus: {N} manifolds; the classic census (up to 7 tetrahedra) = the first 4815; m + s = the first {sum(1 for i in range(1400) if census[i].name()[0] in 'ms')}")
hits3 = []; hex_count = 0; hex2 = 0; hex2_o3 = 0; det3_by_cusps = {}; chiral_door_o3 = []; n_ms = 0
for i in range(4815):
    M = census[i]; name = M.name()
    try:
        S = M.symmetry_group(); n = S.order()
    except Exception:
        continue
    isos = S.isometries()
    def order_of(k):
        cur = k
        for j in range(2, 25):
            cur = S.multiply_elements(cur, k)
            if cur == 0: return j
    o3 = [k for k in range(1, n) if order_of(k) == 3]
    ishex = hexagonal(M)
    if ishex:
        hex_count += 1
        if M.num_cusps() == 2:
            hex2 += 1
            if o3: hex2_o3 += 1
    dets = set()
    for k in o3:
        iso = isos[k]
        if list(iso.cusp_images()) != list(range(M.num_cusps())): continue
        for cm in iso.cusp_maps():
            dets.add(abs(int((cm[0, 0] - 1) * (cm[1, 1] - 1) - cm[0, 1] * cm[1, 0])))
    if 3 in dets:
        hits3.append((name, M.num_cusps(), round(vol(M) / v0f, 3), str(M.homology()), str(S)))
        det3_by_cusps[M.num_cusps()] = det3_by_cusps.get(M.num_cusps(), 0) + 1
    if name[0] in "ms":
        n_ms += 1
        if o3 and not S.is_amphicheiral():
            s2T = surjections(M.fundamental_group(), 3)
            if s2T:
                chiral_door_o3.append((name, s2T, sorted(dets), str(M.homology())))
print(f"  det(A - I) = 3 for a cusp-fixing order-3 isometry, first 4815: {[(h[0], h[1], h[2]) for h in hits3]}; by number of cusps {det3_by_cusps} (the package: m202, s959, v3461, v3551; none 1- or 3-cusped)")
for h in hits3: print(f"    {h[0]:8s} cusps {h[1]} vol/v0 {h[2]:8.3f} H_1 {h[3]:>16s} Sym {h[4]}")
print(f"  hexagonal manifolds (every cusp e^(i pi/3)) in the first 4815: {hex_count}; two-cusped among them: {hex2}; of those with an order-3 isometry: {hex2_o3} (the package at 6000: 11, 5, 4)")
print(f"  m + s census ({n_ms} manifolds): chiral + order-3 isometry + 2T door: {[(c[0], c[1], c[2]) for c in chiral_door_o3]} (the package: exactly m202, s776, s784, s959; det 3 for m202/s959, 0 for s776/s784)")
def in_Qsqrt(z, d, prec_bits=200):
    mp.mp.prec = prec_bits + 20
    def num(v): return mp.mpf(str(v).replace(' ', ''))
    x = num(z.real()) if callable(getattr(z, 'real', None)) else num(z.real)
    y = num(z.imag()) if callable(getattr(z, 'imag', None)) else num(z.imag)
    def is_multiple(u, base):
        if abs(u) < mp.mpf(10) ** (-50): return True
        r = mp.pslq([u, base], maxcoeff=10 ** 9, maxsteps=10 ** 5)
        return r is not None and r[0] != 0
    return is_multiple(x, mp.mpf(1)) and is_multiple(y, mp.sqrt(d))
for c in chiral_door_o3:
    shapes = snappy.Manifold(c[0]).tetrahedra_shapes('rect', bits_prec=220)
    f3 = sum(in_Qsqrt(z, 3) for z in shapes); f7 = sum(in_Qsqrt(z, 7) for z in shapes)
    field = "Q(sqrt-3)" if f3 == len(shapes) else ("Q(sqrt-7)" if f7 == len(shapes) else f"neither (shapes in Q(sqrt-3): {f3}/{len(shapes)}, in Q(sqrt-7): {f7}/{len(shapes)})")
    print(f"    {c[0]}: surjections onto 2T {c[1]}, |det(A-I)| of cusp-fixing order-3 maps {c[2]}, H_1 {c[3]}, shape field {field} (the package: m202/s959 Q(sqrt-3), s776/s784 Q(sqrt-7))")
print("  parity of fixed ends: an orientation-preserving isometry of finite order fixes a union of geodesics, closed or proper arcs with two ends at cusps, so the total number of fixed points on the cusp tori is even; a single cusp with |det(A - I)| = 3 is impossible, as is [3, 3, 3] on three cusps -- the package's empirical 'no 1- or 3-cusped det = 3' is a theorem.")
print(f"\nDONE {stamp()}")
