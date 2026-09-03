#!/usr/bin/env python3
"""L199 -- THE TWO EARNING COMPUTATIONS FOR PRICED IDENTIFICATIONS (B1242).

B1241 registered I-15 and I-16 UNEARNED and named, for each, the one finite computation that turns the
name-match into a map or kills it (docs/OPEN_LEADS.md, L199).  This script runs both, with two-sided
controls (E52 rule), exact arithmetic in every decisive step, and writes l199.json.

  PART A  (I-16, B675 "SU(4)_1 IS the silver's stage"):
          the discriminant form of the silver knot's cusp lattice vs A3's (Z/4, q = 3/8).
  PART B  (I-15, B715 "E6(C) CS ... exactly what it should be as 3d Euclidean quantum gravity"):
          the Dynkin index of the principal sl2 in e6 by THREE independent routes, the E6 invariant of
          the promoted holonomy as (index)*(Vol + i CS) + (the rest), B715's adjoint trace REPRODUCED.

Nothing here touches Gate 5 (no measured value); nothing earns I-13.
"""
import cmath, itertools, json, math, os, subprocess, sys
from fractions import Fraction as Fr
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}
def say(*a):
    print(*a); sys.stdout.flush()

# =====================================================================================================
# PART A -- I-16: the silver cusp lattice's discriminant form vs A3's
# =====================================================================================================
say("=" * 100)
say("PART A -- I-16: the discriminant form of the silver knot's cusp lattice vs A3's (Z/4, q = 3/8)")
say("=" * 100)

# A1. the cusp shapes, numerically at two precisions (corroborating B675 2B / B672: tau_silver = 2i,
#     tau_golden = 2 sqrt(-3), both EXACT there); a two-sided check: tau^2 is -4 / -12, and NOT -1 / -3.
try:
    import snappy
    shapes = {}
    for name, key in (("m136", "silver"), ("m004", "golden")):
        M = snappy.Manifold(name)
        t2 = {"silver": 4, "golden": 12, "silver_wrong": 1, "golden_wrong": 3}
        z_lo = M.cusp_info()[0]["shape"]                       # double precision
        z_hi = M.high_precision().cusp_info()[0]["shape"]      # quad precision (both in SnapPy's own Number type)
        want, wrong = t2[key], t2[key + "_wrong"]
        shapes[key] = {"manifold": name, "shape_double": str(z_lo), "shape_quad": str(z_hi), "volume": float(M.volume()),
                       "tau2_plus_%d_double" % want: float(abs(z_lo ** 2 + want)), "tau2_plus_%d_quad" % want: float(abs(z_hi ** 2 + want)),
                       "tau2_plus_%d_quad_(wrong_target)" % wrong: float(abs(z_hi ** 2 + wrong))}
        say(f"A1. SnapPy {name} ({key}): shape {z_lo} (double), {str(z_hi)[:40]}... (quad);  |tau^2 + {want}| = "
            f"{float(abs(z_lo**2 + want)):.1e} / {float(abs(z_hi**2 + want)):.1e} at the two precisions;  |tau^2 + {wrong}| = {float(abs(z_hi**2 + wrong)):.2f} (wrong target, two-sided)")
        assert float(abs(z_lo ** 2 + want)) < 1e-9 and float(abs(z_hi ** 2 + want)) < 1e-25 and float(abs(z_hi ** 2 + wrong)) > 1
    OUT["A1_cusp_shapes"] = shapes
except ImportError:
    say("A1. snappy unavailable on this bench -- the exact tau (B675 2B, B672) is used without the numeric corroboration")
    OUT["A1_cusp_shapes"] = "snappy unavailable"

# A2. the lattices.  A cusp lattice is a similarity class: Lambda = Z + Z tau in C with the real inner
#     product Re(z conj(w)).  Gram matrices in the basis {1, tau}; the MINIMAL EVEN rescaling is what
#     carries a discriminant (quadratic) form -- an odd lattice has only a bilinear one.
def gram_of(tau2_neg):          # tau = i*sqrt(t), t = -tau^2 > 0: Gram diag(1, t)
    return sp.Matrix([[1, 0], [0, tau2_neg]])
lattices = {
    "silver cusp Z+2iZ (odd, primitive)":           gram_of(4),
    "silver cusp, minimal even rescaling (x2)":     2 * gram_of(4),
    "golden cusp Z+2sqrt(-3)Z (odd, primitive)":    gram_of(12),
    "golden cusp, minimal even rescaling (x2)":     2 * gram_of(12),
    "A3 Coxeter plane Z[i] (even: 2 Re z conj w)":  sp.Matrix([[2, 0], [0, 2]]),
    "A2 Coxeter plane Z[zeta3] (even: 2 Re z conj w)": sp.Matrix([[2, 1], [1, 2]]),
}

def cartan(kind, n):
    C = sp.zeros(n, n)
    for i in range(n):
        C[i, i] = 2
        if i + 1 < n:
            C[i, i + 1] = C[i + 1, i] = -1
    if kind == "E" and n == 6:          # Bourbaki: chain 1-3-4-5-6, node 2 on node 4
        C = sp.zeros(6, 6)
        for i in range(6): C[i, i] = 2
        for a, b in ((0, 2), (2, 3), (3, 4), (4, 5), (1, 3)):
            C[a, b] = C[b, a] = -1
    if kind == "E" and n == 8:          # chain 1-3-4-5-6-7-8, node 2 on node 4
        C = sp.zeros(8, 8)
        for i in range(8): C[i, i] = 2
        for a, b in ((0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 3)):
            C[a, b] = C[b, a] = -1
    return C

A3, A2, E8 = cartan("A", 3), cartan("A", 2), cartan("E", 8)
lattices["A3 root lattice (Cartan matrix)"] = A3
lattices["A2 root lattice (Cartan matrix)"] = A2
lattices["A3 + E8 (control: same form, different lattice)"] = sp.diag(A3, E8)
lattices["<4> rank 1 (control: same group Z/4, other q)"] = sp.Matrix([[4]])
lattices["-A3 (control: signature 5)"] = -A3

# A3. discriminant forms: D = L*/L with q(x) = x.G.x/2 mod 1; invariants: group type (SNF), |D|, level
#     (smallest N with N q = 0), the multiset of q-values, and the Gauss-sum signature mod 8 (Milgram:
#     sum_x e^{2 pi i q(x)} = sqrt|D| e^{2 pi i sig/8}).
def disc_form(G):
    G = sp.Matrix(G); n = G.shape[0]
    assert G == G.T and all(G[i, i] % 2 == 0 for i in range(n)), "even lattice required"
    d = abs(int(G.det()))
    Gi = [[Fr(int(e.p), int(e.q)) for e in row] for row in G.inv().tolist()]     # exact, plain Fractions
    elems = {}
    # L*/L = G^-1 Z^n / Z^n: x = G^-1 v mod 1, q(x) = v.G^-1.v / 2 mod 1; the box [0,d)^n covers the quotient
    # (d v = 0 in Z^n/G Z^n); stop once all d classes are in hand, and assert that count
    for v in itertools.product(range(d), repeat=n):
        gv = [sum(Gi[i][j] * v[j] for j in range(n)) for i in range(n)]
        x = tuple(c % 1 for c in gv)
        if x in elems: continue
        elems[x] = (sum(v[i] * gv[i] for i in range(n)) / 2) % 1
        if len(elems) == d: break
    assert len(elems) == d, (len(elems), d)
    snf = smith_normal_form(G, domain=sp.ZZ)
    inv_factors = sorted(abs(int(snf[i, i])) for i in range(n) if abs(int(snf[i, i])) != 1)
    level = 1
    while any((level * q) % 1 != 0 for q in elems.values()): level += 1
    # Milgram: sum_x e^{2 pi i q(x)} = sqrt|D| e^{2 pi i sig/8}; float Gauss sum, exact q-values
    gs = sum(cmath.exp(2j * cmath.pi * float(q)) for q in elems.values()) / math.sqrt(d)
    sig = round(8 * cmath.phase(gs) / (2 * cmath.pi)) % 8
    assert abs(abs(gs) - 1) < 1e-9 and abs(cmath.exp(2j * cmath.pi * sig / 8) - gs) < 1e-9, (gs, sig)
    order_of = lambda x: min(k for k in range(1, d + 1) if all((k * c) % 1 == 0 for c in x))
    qvals = sorted(elems.values())
    return {"order": d, "group": inv_factors, "level": level, "signature_mod_8": int(sig),
            "q_values": [f"{q.numerator}/{q.denominator}" for q in qvals],
            "generator_q": None if len(inv_factors) != 1 else
                sorted({f"{q.numerator}/{q.denominator}" for x, q in elems.items() if order_of(x) == d})}

def cyclic_iso(F1, F2):
    """two CYCLIC discriminant forms are isomorphic iff some generator of each has equal q (a generator
    determines the form on Z/d); returns the matching generator q or None."""
    if F1["group"] != F2["group"] or len(F1["group"]) != 1: return None
    common = set(F1["generator_q"]) & set(F2["generator_q"])
    return sorted(common)[0] if common else None

forms = {}
say("\nA3. discriminant forms of the even lattices (|D|, group, level, signature mod 8, q on generators):")
for name, G in lattices.items():
    if any(G[i, i] % 2 for i in range(G.shape[0])):
        # odd lattice: only the bilinear discriminant form exists; report |D| and the group, and move on
        d = abs(int(G.det())); snf = smith_normal_form(G, domain=sp.ZZ)
        grp = sorted(abs(int(snf[i, i])) for i in range(G.shape[0]) if abs(int(snf[i, i])) != 1)
        forms[name] = {"order": d, "group": grp, "odd_lattice": True}
        say(f"    {name:58s} |D| = {d:3d}  group Z/{grp}  ODD lattice (no quadratic discriminant form)")
        continue
    F = disc_form(G); forms[name] = F
    say(f"    {name:58s} |D| = {F['order']:3d}  group {F['group']}  level {F['level']:2d}  sig {F['signature_mod_8']}  gen q {F['generator_q']}")
OUT["A3_discriminant_forms"] = forms

a3 = forms["A3 root lattice (Cartan matrix)"]
assert a3 == {**a3, "order": 4, "group": [4], "level": 8, "signature_mod_8": 3} and "3/8" in a3["generator_q"], a3
say("\n    A3's form is (Z/4, q(gen) = 3/8), level 8, signature 3: the SU(4)_1 datum (h = {0, 3/8, 1/2, 3/8}, c = 3).")

# A4. the comparison, both directions
say("\nA4. THE TEST (L199(a)): is A3's form the discriminant form of the silver cusp lattice at ANY scale?")
silver_even = forms["silver cusp, minimal even rescaling (x2)"]
say(f"    silver cusp lattice, minimal even scaling 2x^2 + 8y^2: |D| = {silver_even['order']}, group {silver_even['group']}, "
    f"level {silver_even['level']}, signature {silver_even['signature_mod_8']}")
# every even lattice similar to Z+2iZ has Gram c*diag(1,4) with c in 2Z, |D| = 4c^2 >= 16; and every
# positive-definite rank-2 lattice has signature 2 mod 8 (Milgram) -- two independent exclusions.
scale_orders = {c: abs(int((c * gram_of(4)).det())) for c in (2, 4, 6, 8)}
say(f"    |D| across even scalings c*diag(1,4), c even: {scale_orders}  -- never 4")
sigs_rank2 = {name: F["signature_mod_8"] for name, F in forms.items() if not F.get("odd_lattice") and lattices[name].shape[0] == 2}
say(f"    signatures of every rank-2 positive-definite form computed: {sorted(set(sigs_rank2.values()))}  -- never 3")
assert all(v >= 16 for v in scale_orders.values()) and set(sigs_rank2.values()) == {2}
# positive controls: the detector says YES where it should
pos1 = cyclic_iso(a3, forms["A3 + E8 (control: same form, different lattice)"])
neg1 = cyclic_iso(a3, forms["<4> rank 1 (control: same group Z/4, other q)"])
neg2 = cyclic_iso(a3, forms["-A3 (control: signature 5)"])
say(f"    controls: A3 vs A3+E8 -> iso via generator q = {pos1} (YES, as it must: E8 is unimodular);")
say(f"              A3 vs <4> (same group Z/4, q = 1/8) -> {neg1} (NO: the detector separates on q, not on the group);")
say(f"              A3 vs -A3 (q = 5/8, sig 5) -> {neg2} (NO: orientation is seen)")
assert pos1 == "3/8" and neg1 is None and neg2 is None
# the golden control: the SAME test on B672's golden -> A2 quantization
golden_even = forms["golden cusp, minimal even rescaling (x2)"]
a2 = forms["A2 root lattice (Cartan matrix)"]; plane_a2 = forms["A2 Coxeter plane Z[zeta3] (even: 2 Re z conj w)"]
plane_a3 = forms["A3 Coxeter plane Z[i] (even: 2 Re z conj w)"]
say(f"\n    THE GOLDEN CONTROL (B672: golden quantizes A2, index 4): golden cusp even form |D| = {golden_even['order']} vs A2's |D| = {a2['order']}"
    f" -> the cusp lattice itself does NOT carry A2's form either;")
say(f"    but A2's Coxeter plane Z[zeta3] IS the A2 root lattice: plane form {plane_a2['group']} q {plane_a2['generator_q']} == A2 form {a2['group']} q {a2['generator_q']}: "
    f"{cyclic_iso(plane_a2, a2) is not None}")
say(f"    while A3's Coxeter plane Z[i] is A1+A1: form group {plane_a3['group']}, q-values {plane_a3['q_values']} (SU(2)_1 x SU(2)_1's datum, c = 2) -- NOT A3's.")
assert cyclic_iso(plane_a2, a2) == "1/3" and plane_a3["group"] == [2, 2] and golden_even["order"] == 48

# A5. the modular data each lattice actually produces (T-spectrum of the Weil representation:
#     T_x = exp 2 pi i (q(x) - sig/24)); ord(T) is the datum B675 heard as "conductor 8".
def ordT(F):
    c = Fr(F["signature_mod_8"], 24)
    N = 1
    while any(((Fr(q) - c) * N) % 1 != 0 for q in F["q_values"]): N += 1
    return N
modular = {k: {"anyons": F["order"], "c_mod_8": F["signature_mod_8"], "ordT": ordT(F)}
           for k, F in forms.items() if not F.get("odd_lattice")}
say("\nA5. the modular datum each even lattice produces (Weil representation): anyons, c mod 8, ord(T):")
for k, m in modular.items():
    say(f"    {k:58s} anyons {m['anyons']:3d}  c = {m['c_mod_8']} mod 8  ord(T) = {m['ordT']}")
assert modular["A3 root lattice (Cartan matrix)"] == {"anyons": 4, "c_mod_8": 3, "ordT": 8}          # SU(4)_1: B675's ord(T) = 8 REPRODUCED
assert modular["silver cusp, minimal even rescaling (x2)"] == {"anyons": 16, "c_mod_8": 2, "ordT": 48}
OUT["A5_modular_data"] = modular
OUT["A_verdict"] = {
    "I-16": "REFUTED",
    "discriminating_facts": [
        "silver cusp lattice (any even scaling): |D| = 4c^2 >= 16, A3: |D| = 4",
        "silver cusp lattice: rank 2 positive definite => signature 2 mod 8 (Milgram); A3's form has signature 3",
        "silver cusp lattice, minimal even scaling: level 16, 16 anyons, c = 2 mod 8, ord(T) = 48; SU(4)_1: level 8, 4 anyons, c = 3, ord(T) = 8",
        "what B675 proved (Z[2i] inside Z[i], index 2) is a COXETER-PLANE statement; A3's Coxeter plane is A1+A1 (SU(2)_1^2), not A3",
        "the golden control explains the slip: A2's Coxeter plane IS its root lattice (rank 2 = rank 2), A3's is not (rank 2 < rank 3)",
    ],
    "what_stands_in_B675": "tau = -2i exact; the cusp field Q(i); the index-2 Z[i]-equivariant embedding into A3's Coxeter plane; the A2/A4 exclusions; index = conductor (2 instances)",
}
say("\n    VERDICT A: I-16 REFUTED -- the conductor matched the level and nothing else; B675's lattice results stand as Coxeter-plane facts.")

# =====================================================================================================
# PART B -- I-15: the Dynkin index of the principal sl2 in e6, three routes; the promoted invariant
# =====================================================================================================
say("\n" + "=" * 100)
say("PART B -- I-15: the principal sl2 in e6 -- Dynkin index (3 routes), the promoted CS invariant, B715's trace")
say("=" * 100)
C = cartan("E", 6); Cinv = C.inv(); n = 6
assert C.det() == 3

# B1. roots (W-orbit closure of the simple roots, Dynkin-label coordinates), exponents two ways
def refl(i, m):                       # simple reflection s_i on a weight in Dynkin labels
    return tuple(m[j] - m[i] * C[i, j] for j in range(n))
simple = [tuple(C[i, j] for j in range(n)) for i in range(n)]      # alpha_i in Dynkin labels = row i of C
roots = set(simple); frontier = list(simple)
while frontier:
    new = []
    for r in frontier:
        for i in range(n):
            s = refl(i, r)
            if s not in roots: roots.add(s); new.append(s)
    frontier = new
def rootcoords(m): return Cinv * sp.Matrix(m)          # m = C c  =>  c = C^-1 m
def height(m): return sum(rootcoords(m))
pos = [r for r in roots if height(r) > 0]
assert len(roots) == 72 and len(pos) == 36
dim_g = len(roots) + n
hts = [int(height(r)) for r in pos]
count_by_h = {k: hts.count(k) for k in range(1, max(hts) + 1)}
exps_kostant = sorted(k for k in count_by_h for _ in range(count_by_h[k] - count_by_h.get(k + 1, 0)))
# Coxeter element eigenvalues
cox = sp.eye(n)
for i in range(n):
    Si = sp.eye(n)
    for j in range(n): Si[i, j] = (1 if i == j else 0) - C[i, j]     # s_i on Dynkin labels: m -> m - m_i * row_i
    cox = Si * cox
h = max(hts) + 1
eig_args = sorted(round(float(sp.arg(ev)) * h / (2 * float(sp.pi))) % h for ev in cox.eigenvals(multiple=True))
say(f"B1. E6: {len(roots)} roots, dim g = {dim_g}, Coxeter number h = {h}; exponents by height counts {exps_kostant}, by Coxeter eigenvalues {eig_args}")
assert exps_kostant == eig_args == [1, 4, 5, 7, 8, 11] and dim_g == 78 and h == 12
exps = exps_kostant
hdual = h                                                  # simply laced

# B2. the basic form on weights: (mu, nu) = m^T C^-1 n (roots of norm 2); Dynkin index I(V) = sum (lam,lam)/rank;
#     the sl2 weight of a weight mu under the principal h = 2 rho^vee is 2*height(mu).
def form(m1, m2): return (sp.Matrix(m1).T * Cinv * sp.Matrix(m2))[0, 0]
def index_of(weights): return sum(form(w, w) for w in weights) / n
def sl2_decompose(sl2_weights):
    """multiset of sl2 weights (integers) -> dict {n: multiplicity of V_n}"""
    from collections import Counter
    cnt = Counter(sl2_weights); out = {}
    for k in sorted(cnt, reverse=True):
        if k < 0: break
        m = cnt[k] - cnt.get(k + 2, 0)
        if m: out[k] = m
    return out
def I_sl2(nn): return sp.Rational(nn * (nn + 1) * (nn + 2), 6)      # Dynkin index of V_n over sl2, basic form
adj_weights = list(roots) + [tuple([0] * n)] * n
I_adj = index_of(adj_weights)
adj_sl2 = sl2_decompose([2 * int(height(r)) for r in roots] + [0] * n)
say(f"B2. adjoint: I(78) = {I_adj} (= 2 h^vee = {2*hdual}); restricted to the principal sl2: {adj_sl2} (dims {[k+1 for k in adj_sl2]}, sum {sum(k+1 for k in adj_sl2)})")
assert I_adj == 24 and adj_sl2 == {2 * e: 1 for e in exps}
j_adj = sum(I_sl2(k) * m for k, m in adj_sl2.items()) / I_adj
say(f"    ROUTE 1 (adjoint): j = sum_i I(V_(2 e_i)) / I(78) = {sum(I_sl2(k) * m for k, m in adj_sl2.items())} / {I_adj} = {j_adj}")

# B3. the 27 (minuscule: the W-orbit of omega_1), its sl2 decomposition and index
w1 = tuple(1 if i == 0 else 0 for i in range(n))
wts = {w1}; frontier = [w1]
while frontier:
    new = []
    for m in frontier:
        for i in range(n):
            if m[i] > 0:
                s = tuple(m[j] - C[i, j] for j in range(n))
                if s not in wts: wts.add(s); new.append(s)
    frontier = new
assert len(wts) == 27
I_27 = index_of(list(wts))
sl2_27 = sl2_decompose([int(2 * height(m)) for m in wts])
j_27 = sum(I_sl2(k) * m for k, m in sl2_27.items()) / I_27
say(f"B3. the 27: I(27) = {I_27}; under the principal sl2: {sl2_27} (dims {[k+1 for k in sl2_27]});  ROUTE 2: j = {sum(I_sl2(k)*m for k,m in sl2_27.items())} / {I_27} = {j_27}")
assert I_27 == 6 and sl2_27 == {16: 1, 8: 1, 0: 1}

# B4. the Weyl vector: (rho, rho) = 1^T C^-1 1; j = (2 rho^vee, 2 rho^vee)/(alpha^vee, alpha^vee) = 2 (rho, rho)
rho = tuple([1] * n)
rr = form(rho, rho)
j_rho = 2 * rr
say(f"B4. (rho, rho) = sum of the entries of C^-1 = {rr} (Freudenthal-de Vries h^vee dim g / 12 = {sp.Rational(hdual*dim_g, 12)});  ROUTE 3: j = 2 (rho, rho) = {j_rho}")
assert rr == sp.Rational(hdual * dim_g, 12) and j_adj == j_27 == j_rho == 156
J = int(j_adj)

# B5. the center: -1 in SL(2) acts on every principal-sl2 isotypic piece of the 27 and the 78 by (-1)^n, n even
even_only = all(k % 2 == 0 for k in list(adj_sl2) + list(sl2_27))
say(f"B5. all sl2 weights even on 27 and 78: {even_only} -> the principal map factors through PSL(2,C) = Isom+(H^3) (B428's integer-spin fact, re-derived)")
assert even_only

# B6. B715's adjoint trace REPRODUCED (tr Ad(rho(a)), tr rho(a) = 1 + sqrt(-3)), and the 27-trace recorded
t = 1 + sp.sqrt(3) * sp.I
def chi(nn, tr):                       # character of V_n at an SL2 element of trace tr: U_n(tr/2)
    return sp.expand(sp.chebyshevu(nn, tr / 2))
tr_ad = sp.expand(sum(chi(k, t) * m for k, m in adj_sl2.items()))
tr_27 = sp.expand(sum(chi(k, t) * m for k, m in sl2_27.items()))
target = 37437270 + 38799960 * sp.sqrt(3) * sp.I
say(f"B6. tr Ad_e6(rho(a)) = {tr_ad}  ==  B715's 37437270 + 38799960 sqrt(3) i: {sp.simplify(tr_ad - target) == 0}")
say(f"    tr_27(rho(a)) = {tr_27}  (non-real as well)")
assert sp.simplify(tr_ad - target) == 0 and sp.im(tr_27) != 0

# B7. the promoted invariant: the CS 3-form is linear in the invariant form, and phi^*(basic form of e6)
#     = j * (basic form of sl2) BY DEFINITION of j; so CS_E6(phi o rho) = 156 * CS_SL2(rho), the rest = 0.
vol_m004 = 2.029883212819307    # B1239 / r51: m004, CS = 0 (amphichiral)
say(f"B7. E6 complex CS of the promoted m004 holonomy = {J} * (CS + i Vol)(m004) + 0 = {J} * (0 + i*{vol_m004}) = i*{J*vol_m004:.12f}")
say(f"    the coefficient is the Dynkin index (canonical, three routes agree); 'the rest' is identically zero -- the map ACTS.")

# B8. the field content: what the identity '==' would need
sectors = {2 * e: 2 * e + 1 for e in exps}
say(f"B8. E6(C) CS field content along the principal sl2: 78 = {' + '.join(str(v) for v in sectors.values())};"
    f" the sl2 (spin-2, gravity) sector is {sectors[2]} of 78; the other five carry sl2-spin e_i for e_i in {exps[1:]}"
    f" (Drinfeld-Sokolov weights e_i + 1 = {[e + 1 for e in exps[1:]]} -- higher-spin sectors, CITED framing).")
OUT["B"] = {
    "exponents": exps, "h": h, "dim": dim_g, "I_adj": int(I_adj), "I_27": int(I_27),
    "adjoint_under_principal_sl2": {str(k): v for k, v in adj_sl2.items()},
    "the_27_under_principal_sl2": {str(k): v for k, v in sl2_27.items()},
    "dynkin_index_principal_sl2": {"route_adjoint": int(j_adj), "route_27": int(j_27), "route_rho": int(j_rho)},
    "rho_rho": int(rr), "factors_through_PSL2": even_only,
    "tr_Ad_rho_a": str(tr_ad), "tr_27_rho_a": str(tr_27), "B715_trace_reproduced": True,
    "promoted_invariant": {"coefficient": J, "rest": 0, "m004_vol": vol_m004, "E6_invariant_imag": J * vol_m004},
    "field_content_dims": {str(k): v for k, v in sectors.items()},
}
OUT["B_verdict"] = {
    "I-15": "REFUTED as '==' ; the containment is EARNED",
    "discriminating_facts": [
        "the map exists and is canonical: the principal sl2 (B430 forced), factoring through PSL(2,C) (all sl2 weights even)",
        "it acts: CS_E6(principal o rho) = 156 * CS_SL2(rho) exactly, the rest = 0; 156 by three independent routes",
        "'==' fails by counting: E6(C) CS has 78 field components, 3d gravity (PSL(2,C) CS) has 3; the other 75 are five sectors of sl2-spin 4,5,7,8,11",
        "what B715 needed for its verdict (non-real adjoint trace => no real form) is untouched and REPRODUCED here",
    ],
}
say("\n    VERDICT B: I-15 as '==' REFUTED (78 != 3); '3d gravity = the principal spin-2 sector of E6(C) CS, level ratio 156' is exhibited and acts.")

json.dump(OUT, open(os.path.join(HERE, "l199.json"), "w"), indent=1, default=str)
say("\nwrote l199.json")
say("REPRODUCES")
