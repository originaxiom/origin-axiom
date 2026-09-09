"""B1296 / T3+T5 (+ the spectral half of THE PARITY LOCK) -- the charge spectra of the 27 and the 78 of E6 under the Cartan directions the
chirality question names, computed INDEPENDENTLY of the physics seat's icosian realisation:
Bourbaki's R^8 model of E6, exact rationals, the 27 as the Weyl orbit of omega_1 (minuscule),
theta = the diagram automorphism (1<->6, 3<->5). Reference values: the physics seat's r70/r70b
(norm-1 roots, so its charges are HALF of the standard-normalisation charges printed here)."""
import itertools, json, sys
from fractions import Fraction as Fr

H = Fr(1, 2)
def e(i): v = [Fr(0)] * 8; v[i] = Fr(1); return v
def add(a, b): return [x + y for x, y in zip(a, b)]
def sub(a, b): return [x - y for x, y in zip(a, b)]
def scale(c, a): return [c * x for x in a]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def key(v): return tuple(v)

# Bourbaki simple roots of E6 (Planche V)
a1 = add(scale(H, add(e(0), e(7))), scale(-H, [sum(x) for x in zip(e(1), e(2), e(3), e(4), e(5), e(6))]))
a2 = add(e(0), e(1)); a3 = sub(e(1), e(0)); a4 = sub(e(2), e(1)); a5 = sub(e(3), e(2)); a6 = sub(e(4), e(3))
S = [a1, a2, a3, a4, a5, a6]
C = [[dot(a, b) for b in S] for a in S]                   # Cartan matrix (simply laced, norm^2 2)
E6_CARTAN = [[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
assert C == [[Fr(x) for x in row] for row in E6_CARTAN], C

def refl(v, a): return sub(v, scale(dot(v, a), a))       # norm^2(a) = 2
def orbit(start):
    seen = {key(start): start}; frontier = [start]
    while frontier:
        nxt = []
        for v in frontier:
            for a in S:
                w = refl(v, a)
                if key(w) not in seen: seen[key(w)] = w; nxt.append(w)
        frontier = nxt
    return list(seen.values())

roots = orbit(a1); assert len(roots) == 72
# inverse Cartan matrix, exact
def inv(M):
    n = len(M); A = [[Fr(x) for x in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for i in range(n):
        p = next(r for r in range(i, n) if A[r][i] != 0); A[i], A[p] = A[p], A[i]
        A[i] = [x / A[i][i] for x in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0: A[r] = [x - A[r][i] * y for x, y in zip(A[r], A[i])]
    return [row[n:] for row in A]
Cinv = inv(E6_CARTAN)
omega = [[sum((Cinv[k][j] * S[j][i] for j in range(6)), Fr(0)) for i in range(8)] for k in range(6)]
for k in range(6): assert [dot(omega[k], a) for a in S] == [Fr(int(j == k)) for j in range(6)]
W27 = orbit(omega[0]); assert len(W27) == 27
W27bar = orbit(omega[5]); assert len(W27bar) == 27
# simple-root coordinates of a root
def coords(r): return tuple(dot(r, omega[k]) for k in range(6))
FLIP = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
def theta(v):  # diagram automorphism on the span of the simple roots: permute simple-root coordinates
    c = [dot(v, omega[k]) for k in range(6)]; ct = [c[FLIP[k]] for k in range(6)]
    return [sum((ct[k] * S[k][i] for k in range(6)), Fr(0)) for i in range(8)]
rk = {key(r) for r in roots}
assert all(key(theta(r)) in rk for r in roots) and all(theta(theta(r)) == r for r in roots)
fixed_roots = sum(1 for r in roots if theta(r) == r)
# theta on the Cartan: fixed / anti-fixed dimensions (act on the coweight basis)
even = [add(omega[0], omega[5]), omega[1], add(omega[2], omega[4]), omega[3]]
odd = [sub(omega[0], omega[5]), sub(omega[2], omega[4])]
assert all(theta(u) == u for u in even) and all(theta(u) == scale(Fr(-1), u) for u in odd)
# theta swaps 27 <-> 27bar (outer)
assert {key(theta(w)) for w in W27} == {key(w) for w in W27bar}

def spectrum(u):
    from collections import Counter
    q27 = Counter(dot(w, u) for w in W27); q78 = Counter(dot(r, u) for r in roots); q78[Fr(0)] += 6
    cent = 6 + sum(1 for r in roots if dot(r, u) == 0)
    return q27, q78, cent
def fmt(c): return "{" + ", ".join(f"{str(q)}: {n}" for q, n in sorted(c.items())) + "}"
def report(name, u, parity):
    q27, q78, cent = spectrum(u)
    print(f"[u = {name}] theta-{parity}; centralizer dim {cent}\n     27: {fmt(q27)}\n     78: {fmt(q78)}")
    return {"name": name, "parity": parity, "centralizer_dim": cent,
            "q27": {str(q): n for q, n in sorted(q27.items())}, "q78": {str(q): n for q, n in sorted(q78.items())}}

out = {"fixed_roots": fixed_roots, "even_cartan_dim": len(even), "odd_cartan_dim": len(odd), "spectra": []}
print(f"E6 in R^8: 72 roots, 27 = W.omega_1 (27 weights), theta = diagram flip: involution on roots, fixed roots {fixed_roots}, "
      f"fixed Cartan dim {len(even)}, odd Cartan dim {len(odd)}, theta(27) = 27bar: True")
for name, u, p in (("omega_1^vee (mixed: theta -> omega_6^vee)", omega[0], "MIXED"),
                   ("omega_1^vee - omega_6^vee", odd[0], "ODD"), ("omega_3^vee - omega_5^vee", odd[1], "ODD"),
                   ("omega_2^vee", omega[1], "EVEN"), ("omega_4^vee", omega[3], "EVEN"),
                   ("omega_1^vee + omega_6^vee", even[0], "EVEN"), ("omega_3^vee + omega_5^vee", even[2], "EVEN")):
    out["spectra"].append(report(name, u, p))
# T5: the generic theta-odd ray
generic = add(scale(Fr(7), odd[0]), scale(Fr(3), odd[1]))
out["spectra"].append(report("generic theta-odd ray 7(w1-w6) + 3(w3-w5)", generic, "ODD"))
# every ray in the odd plane: centralizer as a function of (a:b); list the special rays
special = {}
for a, b in itertools.product(range(-6, 7), repeat=2):
    if (a, b) == (0, 0): continue
    from math import gcd
    if gcd(abs(a), abs(b)) != 1: continue
    u = add(scale(Fr(a), odd[0]), scale(Fr(b), odd[1])); cent = spectrum(u)[2]
    special.setdefault(cent, []).append((a, b))
print("\n[T5] centralizer dims on the theta-odd plane a(w1-w6)+b(w3-w5), primitive (a,b) in [-6,6]^2:")
for cent in sorted(special): print(f"     dim {cent}: {len(special[cent])} rays, e.g. {special[cent][:4]}")
out["odd_plane_centralizers"] = {str(k): v[:8] for k, v in special.items()}

# T3: the toggled singular-frame count. net(R_q) = -sgn(q) * (eps_1 + eps_2) with eps the arc signs (fc R69's rule,
# net = chi(Delta^-) - chi(Delta^+), each arc chi = 1).  Tabulate for u = omega_1^vee, signs (+,+).
def toggled(u, eps=(+1, +1)):
    q27, q78, _ = spectrum(u); s = sum(eps)
    rows = []
    for src, q in (("27", q27), ("78", q78)):
        for charge, mult in sorted(q.items()):
            if charge == 0: continue
            net = -(1 if charge > 0 else -1) * s
            rows.append({"source": src, "charge": str(charge), "dim": mult, "net_chirality": net})
    return rows
tog = toggled(omega[0]); out["toggled_omega1_signs_pp"] = tog
print("\n[T3] singular frame, theta-equivariance DROPPED, Delta = Fix(theta) two arcs signed (+,+), u = omega_1^vee:")
for r in tog: print(f"     {r['source']}: charge {r['charge']:>5} dim {r['dim']:>2}  net = {r['net_chirality']:+d}")
# identify the SO(10) content: under omega_1 the 27 splits 1 + 16 + 10 by charge {4/3, 1/3, -2/3}; the 78 splits 45+1 (0) + 16 (1) + 16bar (-1)
so10 = {"27": {"4/3": "1", "1/3": "16", "-2/3": "10"}, "78": {"1": "16", "-1": "16bar", "0": "45+1"}}
print("     SO(10) reading: 27 -> 1_{4/3} + 16_{1/3} + 10_{-2/3};  78 -> (45+1)_0 + 16_{+1} + 16bar_{-1}")
print("     => two chiral 16s of SO(10) from the 78 alone (|net| = 2 on 16_{+1}); with a 27 present, two more 16_{1/3}: COUNT 2 either way")
for name, u in (("omega_1^vee - omega_6^vee (ODD, special ray)", odd[0]), ("omega_3^vee - omega_5^vee (ODD, special ray)", odd[1])):
    t = toggled(u); out["toggled_" + name.split(" ")[0] + "_signs_pp"] = t
    print(f"     [same rule, u = {name}]: " + "; ".join(f"{r['source']}:{r['charge']}x{r['dim']} net {r['net_chirality']:+d}" for r in t))
t = toggled(omega[0], (+1, -1)); out["toggled_omega1_signs_pm"] = t
print(f"     [u = omega_1^vee, arcs signed (+,-)]: every net = {sorted({r['net_chirality'] for r in t})}  (fc R69 section 4: the sign pair is the closer's)")

# THE PARITY LOCK, spectral half: theta_G u = u  =>  theta_G(27_q) = 27bar_q = conj(27_{-q})  =>  dim 27_q = dim 27_{-q}
# (the charge spectrum of every theta-EVEN direction is symmetric, fc R70's vector-like class); theta_G u = -u gives
# theta_G(27_q) = 27bar_{-q} = conj(27_q): no constraint, and the odd plane is asymmetric on every primitive ray tested.
def symmetric(u):
    q27 = spectrum(u)[0]; return all(q27[q] == q27[-q] for q in q27)
import random; random.seed(1296)
def ray(basis, cs): return [sum((Fr(c) * v[i] for c, v in zip(cs, basis)), Fr(0)) for i in range(8)]
even_rays = list(even) + [ray(even, [random.randint(-9, 9) for _ in even]) for _ in range(40)]
odd_rays = [add(scale(Fr(a), odd[0]), scale(Fr(b), odd[1])) for a, b in itertools.product(range(-6, 7), repeat=2) if (a, b) != (0, 0)]
mixed = [omega[0], omega[5], omega[2], omega[4]]
ev = [symmetric(u) for u in even_rays]; od = [symmetric(u) for u in odd_rays]; mx = [symmetric(u) for u in mixed]
odd_sym = [(a, b) for (a, b), u in zip([ab for ab in itertools.product(range(-6, 7), repeat=2) if ab != (0, 0)], odd_rays) if symmetric(u)]
print(f"     odd rays with a SYMMETRIC spectrum: {odd_sym}")
for a, b in odd_sym[:3]:
    u = add(scale(Fr(a), odd[0]), scale(Fr(b), odd[1])); q27, q78, cent = spectrum(u)
    print(f"        ({a},{b}): centralizer {cent}; 27: {fmt(q27)}")
print(f"\n[PARITY LOCK, spectral half] q <-> -q symmetry of the 27's charge spectrum:")
print(f"     theta-even directions: {sum(ev)}/{len(ev)} symmetric (4 basis coweights + 40 random integer rays)")
print(f"     theta-odd plane:       {sum(od)}/{len(od)} symmetric (all (a,b) in [-6,6]^2 minus 0)")
print(f"     mixed omega_1,6,3,5^vee: {sum(mx)}/{len(mx)} symmetric")
assert all(ev) and not any(mx)
out["parity_lock_spectral"] = {"even_symmetric": f"{sum(ev)}/{len(ev)}", "odd_symmetric": f"{sum(od)}/{len(od)}", "mixed_symmetric": f"{sum(mx)}/{len(mx)}"}
# T5b: the odd plane IS the restricted-root plane of the symmetric pair (E6, F4): project the 72 roots onto it
proj = {}
for r in roots:
    b = scale(H, sub(r, theta(r)))                          # component along the -1 eigenspace of theta
    if any(x != 0 for x in b): proj.setdefault(key(b), 0); proj[key(b)] += 1
rest = [list(k) for k in proj]; mults = sorted(set(proj.values()))
n2 = {dot(b, b) for b in rest}
angles = sorted({round(float(dot(b1, b2)) / float(dot(b1, b1)), 6) for b1 in rest for b2 in rest})
print(f"     restricted roots on the odd plane: {len(rest)} distinct, multiplicities {mults}, norm^2 {sorted(str(x) for x in n2)}, cosines {angles}  (A2 x 8: 6 roots, cos in {{-1,-1/2,1/2,1}})")
assert len(rest) == 6 and mults == [8] and angles == [-1.0, -0.5, 0.5, 1.0]
wall = lambda u: any(dot(u, b) == 0 for b in rest)         # u on a reflecting wall of the restricted A2
rootline = lambda u: any(all(u[i] * b[j] == u[j] * b[i] for i in range(8) for j in range(8)) for b in rest)   # u parallel to a restricted root
cls = {}
for (a, b_), u in zip([ab for ab in itertools.product(range(-6, 7), repeat=2) if ab != (0, 0)], odd_rays):
    c = ("WALL" if wall(u) else "ROOT-LINE" if rootline(u) else "generic", spectrum(u)[2], symmetric(u))
    cls.setdefault(c, []).append((a, b_))
for c in sorted(cls, key=lambda k: -len(cls[k])): print(f"     {c[0]:9} centralizer {c[1]}  q<->-q symmetric {str(c[2]):5}: {len(cls[c])} rays, e.g. {cls[c][:3]}")
assert set(cls) == {("WALL", 46, False), ("ROOT-LINE", 30, True), ("generic", 30, False)}
w27 = {key(w) for w in W27}; w27b = {key(w) for w in W27bar}
conj = {"omega_3^vee - omega_5^vee in W.omega_1": key(odd[1]) in w27, "omega_1^vee - omega_6^vee in W.omega_6": key(odd[0]) in w27b,
        "omega_1^vee - omega_6^vee in W.omega_1": key(odd[0]) in w27, "omega_3^vee - omega_5^vee in W.omega_6": key(odd[1]) in w27b}
print(f"     Weyl conjugacy of the walls to the minuscule coweights: {conj}")
out["restricted_A2"] = {"classes": {f"{k[0]}|cent{k[1]}|sym{k[2]}": v[:6] for k, v in cls.items()}, "weyl_conjugacy": conj}
# a sigma-odd function's quadratic part at a point of Fix(sigma) is s*(a x + b y): Hessian rank <= 2, never Morse
import numpy as np
ranks = {int(np.linalg.matrix_rank(np.array([[0, 0, a], [0, 0, b], [a, b, 0]], float))) for a, b in itertools.product(range(-3, 4), repeat=2) if (a, b) != (0, 0)}
print(f"     odd quadratic forms s(ax+by) in (x,y,s): Hessian ranks {sorted(ranks)} (< 3: a sigma-odd closed 1-form has no Morse zero on Fix(sigma))")
assert ranks == {2}; out["odd_quadratic_hessian_ranks"] = sorted(ranks)

# T6: VECTOR-LIKE OR CHIRAL under the centraliser's SEMISIMPLE part C_ss (fc R70's convention: U(1)_u itself is
# sgn(q)-weighted by the rule, hence anomalous/Stueckelberg, and is not the group one grades by).  Roots of C =
# {alpha : <alpha,u> = 0}; the C_ss-weight of a weight w is its orthogonal projection onto span(roots of C).
# Left-handed content under fc R69's rule with arcs (+,+):  78 (real 7d field: sectors q and -q are CPT-conjugate,
# count q > 0 once) -> sum_{q>0} net_q [78_q];  27 (complex) -> sum_{q != 0} net_q [27_q].
# VECTOR-LIKE iff the signed C_ss-weight multiset V is closed under negation (V(w) = V(-w)); the chiral excess is
# C(w) = V(w) - V(-w) and chiral_dim = sum_w max(C(w), 0) = the dimension of the net chiral representation.
from collections import Counter
def gram_schmidt(vs):
    basis = []
    for v in vs:
        w = list(v)
        for b in basis: w = sub(w, scale(dot(w, b) / dot(b, b), b))
        if any(x != 0 for x in w): basis.append(w)
    return basis
def css_projector(u):
    B = gram_schmidt([r for r in roots if dot(r, u) == 0])
    return lambda w: key([sum((dot(w, b) / dot(b, b) * b[i] for b in B), Fr(0)) for i in range(8)]), len(B)
def left_handed(u, eps=(+1, +1)):
    proj, rank_css = css_projector(u); s = sum(eps); V = {"78": Counter(), "27": Counter()}
    for r in roots:
        q = dot(r, u)
        if q > 0: V["78"][proj(r)] += -s                     # net_q = -sgn(q) s, q > 0 counted once
    for w in W27:
        q = dot(w, u)
        if q != 0: V["27"][proj(w)] += -(1 if q > 0 else -1) * s
    res = {"rank_css": rank_css}
    for src, cnt in V.items():
        neg = lambda w: key([-x for x in w])
        keys = set(cnt) | {neg(w) for w in cnt}
        chiral = {w: cnt[w] - cnt[neg(w)] for w in keys}
        res[src] = {"vectorlike": all(c == 0 for c in chiral.values()), "chiral_dim": sum(max(c, 0) for c in chiral.values()),
                    "left_handed_weights": sum(1 for w, m in cnt.items() if m != 0)}
    return res
print("\n[T6] vector-like or chiral under C_ss (rule (+,+); 78 counted over q > 0, 27 over q != 0):")
out["vectorlike_test"] = {}
table = [("omega_1^vee (MIXED)", omega[0]), ("omega_1^vee - omega_6^vee (ODD wall)", odd[0]), ("omega_3^vee - omega_5^vee (ODD wall)", odd[1]),
         ("omega_2^vee (EVEN)", omega[1]), ("omega_4^vee (EVEN)", omega[3]), ("omega_1^vee + omega_6^vee (EVEN)", even[0]), ("omega_3^vee + omega_5^vee (EVEN)", even[2]),
         ("odd root line (1,1)", add(odd[0], odd[1])), ("odd root line (2,-1)", sub(scale(Fr(2), odd[0]), odd[1])), ("odd generic (7,3)", generic)]
for name, u in table:
    r = left_handed(u); out["vectorlike_test"][name] = r
    print(f"     {name:38s} C_ss rank {r['rank_css']}: 78 -> {'VECTOR-LIKE' if r['78']['vectorlike'] else 'CHIRAL dim ' + str(r['78']['chiral_dim'])}; "
          f"27 -> {'VECTOR-LIKE' if r['27']['vectorlike'] else 'CHIRAL dim ' + str(r['27']['chiral_dim'])}")
vt = out["vectorlike_test"]
assert vt["omega_1^vee (MIXED)"]["78"]["chiral_dim"] == 32 and vt["omega_1^vee (MIXED)"]["27"]["chiral_dim"] == 32   # 2 x 16bar each
assert vt["omega_2^vee (EVEN)"]["78"]["vectorlike"] and vt["omega_1^vee + omega_6^vee (EVEN)"]["78"]["vectorlike"]
assert not vt["omega_4^vee (EVEN)"]["78"]["vectorlike"] and not vt["omega_3^vee + omega_5^vee (EVEN)"]["78"]["vectorlike"]   # PRE-REGISTRATION WRONG: even != vector-like
assert all(vt[n]["78"]["vectorlike"] and vt[n]["27"]["vectorlike"] for n in vt if "root line" in n or "generic" in n)

# T7: THE F4 CHAMBER.  The theta-even Cartan is the Cartan of F4 = E6^theta; its four fundamental coweights are the four
# theta-invariant combinations omega_2, omega_4, omega_1+omega_6, omega_3+omega_5 (the theta-stable Levi types).  Every
# theta-EVEN direction is Weyl(F4)-conjugate to a generic point of one of the 15 faces of the F4 chamber.  For each face:
# C_ss (the E6 Levi on the complementary theta-stable nodes), vector-like or chiral under the (+,+) rule, and the cubic
# (non-abelian) anomaly of the left-handed content L = sum_{q>0} 78_q: P3(x) = sum_{w in L} <w,x>^3 on each simple
# factor's Cartan (P3 == 0 iff no cubic anomaly; D_n / A_1 have none); Witten's SU(2) anomaly = #doublets mod 2.
def simple_roots_of(rootsC):
    pos = [r for r in rootsC if next(x for x in coords(r) if x != 0) > 0]
    posk = {key(r) for r in pos}
    return pos, [r for r in pos if not any(key(sub(r, t)) in posk for t in pos if t != r)]
def components(simple):
    comps, left = [], list(range(len(simple)))
    while left:
        comp = [left.pop()]; grew = True
        while grew:
            grew = False
            for j in list(left):
                if any(dot(simple[i], simple[j]) != 0 for i in comp): comp.append(j); left.remove(j); grew = True
        comps.append(sorted(comp))
    return comps
def factor_type(simple, comp):
    n = len(comp)
    if n == 4 and any(sum(1 for j in comp if j != i and dot(simple[i], simple[j]) != 0) == 3 for i in comp): return "D4"
    if n == 5 and any(sum(1 for j in comp if j != i and dot(simple[i], simple[j]) != 0) == 3 for i in comp): return "D5"
    return f"A{n}"
def face_report(u, label):
    rootsC = [r for r in roots if dot(r, u) == 0]
    pos, simple = simple_roots_of(rootsC); comps = components(simple)
    types = [factor_type(simple, c) for c in comps]
    L = [r for r in roots if dot(r, u) > 0]                                 # left-handed content of the 78 per unit |net|
    vl = left_handed(u)
    anomalies, witten = [], []
    for comp, typ in zip(comps, types):
        if typ.startswith("A") and len(comp) >= 2:
            P = []
            for trial in range(4):
                x = ray([simple[i] for i in comp], [random.randint(1, 7) for _ in comp])
                P.append(sum(dot(w, x) ** 3 for w in L))
            anomalies.append((typ, [str(v) for v in P]))
        if typ == "A1":
            a = simple[comp[0]]; doublets = sum(1 for w in L if dot(w, a) != 0) // 2   # weights +-1 under the A1: 2 per doublet
            witten.append(doublets % 2)
    cubic_free = all(all(v == "0" for v in P) for _, P in anomalies)
    print(f"     {label:34s} C_ss = {' x '.join(types) if types else '(abelian)':16s} "
          f"78: {'VECTOR-LIKE' if vl['78']['vectorlike'] else 'CHIRAL dim %d' % vl['78']['chiral_dim']:16s} "
          f"cubic anomaly {'none' if cubic_free else 'YES ' + str([(t, P[0]) for t, P in anomalies if P[0] != '0'])}  Witten {witten}")
    return {"C_ss": types, "vectorlike_78": vl["78"]["vectorlike"], "chiral_dim_78": vl["78"]["chiral_dim"], "cubic_anomaly_free": cubic_free,
            "cubic_P3_samples": anomalies, "witten_mod2": witten}
print("\n[T7] the F4 chamber: every theta-even direction, by face (generic point; rule (+,+), count |net| = 2 per sector):")
F4 = [("w2", omega[1]), ("w4", omega[3]), ("w1+w6", even[0]), ("w3+w5", even[2])]
out["F4_chamber"] = {}
for k in range(1, 5):
    for S in itertools.combinations(range(4), k):
        label = "+".join(F4[i][0] for i in S)
        res = None
        for trial in range(2):   # the generic point of the face: independent of the positive coefficients
            cs = [random.randint(1, 9) for _ in S]; u = ray([F4[i][1] for i in S], cs)
            r = face_report(u, label if trial == 0 else "   (again, other coefficients)")
            if res is not None: assert (r["C_ss"], r["vectorlike_78"], r["cubic_anomaly_free"]) == (res["C_ss"], res["vectorlike_78"], res["cubic_anomaly_free"])
            res = r
        out["F4_chamber"][label] = res
fc = out["F4_chamber"]
chiral_faces = [k for k, v in fc.items() if not v["vectorlike_78"]]; anomalous_faces = [k for k, v in fc.items() if not v["cubic_anomaly_free"]]
print(f"     chiral faces: {chiral_faces}\n     cubic-anomalous faces: {anomalous_faces}")
assert set(chiral_faces) == set(anomalous_faces), (chiral_faces, anomalous_faces)     # THE LOCK: on the even Cartan chiral <=> anomalous
# the mixed / odd-wall SO(10) direction for contrast: chiral AND cubic-anomaly-free (D5 has no cubic invariant)
r = face_report(omega[0], "omega_1^vee (MIXED, non-equivariant)"); out["F4_chamber"]["omega_1^vee (mixed)"] = r
assert not r["vectorlike_78"] and r["cubic_anomaly_free"]
r = face_report(odd[0], "w1-w6 (ODD wall, non-equivariant)"); out["F4_chamber"]["w1-w6 (odd wall)"] = r
assert not r["vectorlike_78"] and r["cubic_anomaly_free"]
out["parity_lock_spectral"]["F4_chamber_summary"] = {"faces": len(fc) - 2, "chiral": chiral_faces, "cubic_anomalous": anomalous_faces}


# T8: THE SECTOR ANOMALY TABLE.  Per face, the left-handed content of the two sectors separately -- the 78 (PW's frame: the
# 7d gauge multiplet's charged components, one copy per unit |net|) and the 27 (the heterotic-type matter frame) -- and their
# anomaly coefficients NORMALISED to the fundamental of each factor (exact, x-independent: the cubic/quadratic invariants of
# A_n are unique).  Question answered: can multiplicities (n_78, n_27) cancel every non-abelian anomaly on a chiral face?
def factor_fund_weights(simple, comp):
    n = len(comp); a = [simple[i] for i in comp]
    mu1 = [sum((Fr(n + 1 - j, n + 1) * a[j - 1][i] for j in range(1, n + 1)), Fr(0)) for i in range(8)]   # (C^-1)_{1j} = (n+1-j)/(n+1)
    ws, w = [mu1], mu1
    for j in range(n):
        w = sub(w, a[j]); ws.append(w)
    return ws                                                                    # the n+1 weights of the fundamental
def sector_contents(u):
    L78 = [r for r in roots if dot(r, u) > 0]
    L27 = [w for w in W27 if dot(w, u) > 0] + [[-x for x in w] for w in W27 if dot(w, u) < 0]
    return {"78": L78, "27": L27}
def anomaly_table(u, label):
    rootsC = [r for r in roots if dot(r, u) == 0]
    pos, simple = simple_roots_of(rootsC); comps = components(simple); types = [factor_type(simple, c) for c in comps]
    secs = sector_contents(u); row = {"C_ss": types, "factors": [], "abelian": {}}
    for comp, typ in zip(comps, types):
        fac = {"type": typ}
        if typ.startswith("A") and len(comp) >= 2:
            fund = factor_fund_weights(simple, comp)
            for name, L in secs.items():
                vals = []
                while len(vals) < 2:
                    x = ray([simple[i] for i in comp], [random.randint(1, 11) for _ in comp])
                    d3 = sum(dot(m, x) ** 3 for m in fund)
                    if d3 == 0: continue                                          # x on a wall of the factor: resample
                    vals.append(sum(dot(w, x) ** 3 for w in L) / d3)
                assert vals[0] == vals[1], (label, typ, vals)               # x-independent => a genuine anomaly coefficient
                fac["A3_" + name] = str(vals[0])
        if len(comp) >= 1:
            fund = factor_fund_weights(simple, comp) if typ.startswith("A") else None
            for name, L in secs.items():
                x = ray([simple[i] for i in comp], [random.randint(1, 11) for _ in comp])
                if fund is not None:
                    d2 = sum(dot(m, x) ** 2 for m in fund)
                    fac["mixed_uG2_" + name] = str(sum(dot(w, u) * dot(w, x) ** 2 for w in L) / d2)   # U(1)_u - G^2, in fundamental-index units
        if typ == "A1":
            a = simple[comp[0]]
            for name, L in secs.items():
                fac["witten_" + name] = (sum(1 for w in L if dot(w, a) != 0) // 2) % 2
        row["factors"].append(fac)
    for name, L in secs.items():
        row["abelian"]["u3_" + name] = str(sum(dot(w, u) ** 3 for w in L)); row["abelian"]["grav_u_" + name] = str(sum(dot(w, u) for w in L))
    # cancellation: is there (n78, n27) in Z_{>=0}^2 \ 0 killing every cubic (A_n, n>=2) anomaly and every Witten parity?
    cub = [(Fr(f["A3_78"]), Fr(f["A3_27"])) for f in row["factors"] if "A3_78" in f]
    wit = [(f["witten_78"], f["witten_27"]) for f in row["factors"] if "witten_78" in f]
    sols = [(n78, n27) for n78 in range(0, 7) for n27 in range(0, 19) if (n78, n27) != (0, 0)
            and all(n78 * a + n27 * b == 0 for a, b in cub) and all((n78 * a + n27 * b) % 2 == 0 for a, b in wit)]
    prim = sorted(set((a // math.gcd(a, b), b // math.gcd(a, b)) for a, b in sols))
    unconstrained = all(a == 0 and b == 0 for a, b in cub) and all(a == 0 and b == 0 for a, b in wit)
    row["cancelling_multiplicities_primitive"] = "unconstrained" if unconstrained else prim
    cubs = "  ".join(f"{f['type']}: A3(78)={f['A3_78']} A3(27)={f['A3_27']}" for f in row["factors"] if "A3_78" in f) or "no cubic invariant"
    print(f"     {label:22s} C_ss = {' x '.join(types) if types else '(abelian)':16s} {cubs:58s} cancelling (n78:n27) = {row['cancelling_multiplicities_primitive']}")
    return row
import math
print("\n[T8] sector anomalies per face, normalised to the fundamental (78-sector | 27-sector), and the multiplicities that cancel them:")
out["sector_anomalies"] = {}
for label, u in [(k, v) for k, v in F4] + [("w2+w4", ray([F4[0][1], F4[1][1]], [2, 3])), ("w1+w6+w3+w5", ray([F4[2][1], F4[3][1]], [3, 2])),
                                          ("w2+w1+w6", ray([F4[0][1], F4[2][1]], [2, 5])), ("interior (all 4)", ray([f[1] for f in F4], [1, 2, 3, 5])),
                                          ("omega_1^vee (mixed)", omega[0]), ("w1-w6 (odd wall)", odd[0]), ("odd generic (7,3)", generic)]:
    out["sector_anomalies"][label] = anomaly_table(u, label)
sa = out["sector_anomalies"]
assert sa["w4"]["cancelling_multiplicities_primitive"] == [(1, 3)] and sa["w2+w4"]["cancelling_multiplicities_primitive"] == [(1, 3)]
assert sa["w3+w5"]["cancelling_multiplicities_primitive"] == [] and sa["w1+w6+w3+w5"]["cancelling_multiplicities_primitive"] == []
assert all(sa[k]["cancelling_multiplicities_primitive"] == "unconstrained" for k in ("w2", "w1+w6", "w2+w1+w6", "interior (all 4)", "omega_1^vee (mixed)", "w1-w6 (odd wall)", "odd generic (7,3)"))
# the 1:3 is a ratio between two FRAMES (PW's 7d adjoint sector vs the heterotic-type 27 sector); the parent adjoints that
# contain both give 27-sector multiplicity 2 (E7: 133 = 78+1+27+27bar) or 6 (E8: 248 = (78,1)+(1,8)+(27,3)+(27bar,3bar)),
# because the 27bar-sector's left-handed weight multiset equals the 27-sector's (shown), so neither parent cancels.
u4 = F4[1][1]; L27 = sector_contents(u4)["27"]
L27bar = [w for w in W27bar if dot(w, u4) > 0] + [[-x for x in w] for w in W27bar if dot(w, u4) < 0]
assert sorted(map(key, L27)) == sorted(map(key, L27bar))
a78, a27 = [Fr(f["A3_78"]) for f in sa["w4"]["factors"] if "A3_78" in f][0], [Fr(f["A3_27"]) for f in sa["w4"]["factors"] if "A3_27" in f][0]
parents = {"E7 (133 = 78+1+27+27bar): n27 = 2": str(a78 + 2 * a27), "E8 (248 = (78,1)+(1,8)+(27,3)+(27bar,3bar)): n27 = 6": str(a78 + 6 * a27)}
out["sector_anomalies"]["parent_frames_on_w4_first_A2"] = parents
print("     on w4 the 27bar-sector's left-handed weights coincide with the 27-sector's; the parent adjoints give SU(3)_a cubic anomaly:", parents)
assert all(v != "0" for v in parents.values())

json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "e6_theta_spectra.json", "w"), indent=1)
print("\nSELFTEST: PASS")
