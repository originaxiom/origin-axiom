#!/usr/bin/env python3
"""agy-002's second point, recomputed with own code (exact):
  K   the kernel K_k of Z(SU3) x Z(SU2) x U(1) on matter, U(1) charge k*6Y: finite? cyclic? order?  (k = 1..12)
  Q   the subgroups of K_1, i.e. the quotients the 27 descends to; which one is faithful
  E   E6 from its Cartan matrix: the 27, the two SM-singlet weights, the Smith form of their Dynkin rows, the SM recovered
      from the pair (roots orthogonal to both, Y), the Y circle and where it meets SU3 x SU2, the centre against H_SM
  C   planted controls
"""
import itertools, json
from fractions import Fraction as F
from math import gcd
from functools import reduce

OUT = {}
# (name, triality t of the SU3 rep: 3 -> 1, 3bar -> 2, singlet/adjoint -> 0; duality s: doublet 1; 6Y; dim)
SIXTEEN = [("Q", 1, 1, 1, 6), ("u^c", 2, 0, -4, 3), ("d^c", 2, 0, 2, 3), ("L", 0, 1, -3, 2), ("e^c", 0, 0, 6, 1), ("nu^c", 0, 0, 0, 1)]
TEN = [("H", 0, 1, 3, 2), ("Hbar", 0, 1, -3, 2), ("D", 1, 0, -2, 3), ("D^c", 2, 0, 2, 3)]
ONE = [("S", 0, 0, 0, 1)]
GEN15 = SIXTEEN[:-1]
ADJ = [("G", 0, 0, 0, 8), ("W", 0, 0, 0, 3), ("B", 0, 0, 0, 1)]
CONTENTS = {"27": SIXTEEN + TEN + ONE, "16": SIXTEEN, "10": TEN, "SM generation (15)": GEN15, "adjoint only": ADJ,
            "Q alone": [SIXTEEN[0]], "e^c alone": [SIXTEEN[4]]}

def kernel(content, k):
    """exact: elements (a mod 3, b mod 2, phi mod 1) with a t/3 + b s/2 + k q phi in Z for every field.
    phi must satisfy 6 k q phi in Z for every q (multiply the condition by 6), so phi in (1/(6 k g)) Z, g = gcd of charges;
    if every charge is 0, phi is unconstrained and the kernel contains the whole circle (infinite)."""
    g = reduce(gcd, [abs(f[3]) for f in content], 0)
    if g == 0:
        fin = [(a, b) for a in range(3) for b in range(2) if all((F(a * f[1], 3) + F(b * f[2], 2)).denominator == 1 for f in content)]
        return {"finite": False, "discrete_part": len(fin)}
    Nden = 6 * k * g
    els = []
    for a in range(3):
        for b in range(2):
            for j in range(Nden):
                phi = F(j, Nden)
                if all((F(a * f[1], 3) + F(b * f[2], 2) + k * f[3] * phi).denominator == 1 for f in content):
                    els.append((a, b, phi))
    def order(e):
        a, b, phi = e
        oa = 3 // gcd(a, 3); ob = 2 // gcd(b, 2); op = phi.denominator
        return oa * ob // gcd(oa, ob) * op // gcd(oa * ob // gcd(oa, ob), op)
    n = len(els); orders = [order(e) for e in els]
    gens = [e for e, o in zip(els, orders) if o == n]
    return {"finite": True, "order": n, "cyclic": bool(gens), "generator": [str(x) for x in gens[0]] if gens else None}

K = {}
for name, cont in CONTENTS.items():
    K[name] = {k: kernel(cont, k) for k in range(1, 13)}
OUT["K"] = {name: {str(k): v for k, v in d.items()} for name, d in K.items()}
OUT["K_summary"] = {name: [(k, v.get("order"), v.get("cyclic")) if v["finite"] else (k, "infinite") for k, v in d.items()]
                    for name, d in K.items()}
OUT["K_is_cyclic_6k"] = {name: all(v["finite"] and v["cyclic"] and v["order"] == 6 * k for k, v in d.items()) for name, d in K.items()}

# Q: subgroups of K_1 on the 27; each acts trivially, so the 27 descends to G/Gamma; faithful only for Gamma = K_1
K1 = kernel(CONTENTS["27"], 1)
n1 = K1["order"]
OUT["Q"] = {"K_1_order": n1, "subgroups_of_cyclic_K1": [d for d in range(1, n1 + 1) if n1 % d == 0],
            "descends_to_all": True, "faithful_only_for": n1}

# ---------------------------------------------------------------- E6
EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]      # Bourbaki
Cm = [[2 if i == j else 0 for j in range(6)] for i in range(6)]
for i, j in EDGES:
    Cm[i - 1][j - 1] = Cm[j - 1][i - 1] = -1

def mat_inv(M):
    n = len(M); A = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0); A[c], A[p] = A[p], A[c]
        piv = A[c][c]; A[c] = [x / piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]
def det(M):
    n = len(M); A = [[F(x) for x in row] for row in M]; d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: A[c], A[p] = A[p], A[c]; d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return d
Ci = mat_inv(Cm)
def ip(l, m): return sum(l[i] * Ci[i][j] * m[j] for i in range(6) for j in range(6))
ALPHA = [tuple(Cm[i]) for i in range(6)]          # simple roots in Dynkin coordinates
def reflect(l, i): return tuple(l[j] - l[i] * ALPHA[i][j] for j in range(6))
def orbit(start):
    seen = {start}; fr = [start]
    while fr:
        nx = []
        for l in fr:
            for i in range(6):
                r = reflect(l, i)
                if r not in seen: seen.add(r); nx.append(r)
        fr = nx
    return sorted(seen)
W27 = orbit((1, 0, 0, 0, 0, 0))
ROOTS = orbit(ALPHA[0])
OUT["E"] = {"det_Cartan": str(det(Cm)), "n_weights_27": len(W27), "n_roots": len(ROOTS),
            "norm_27": sorted({str(ip(w, w)) for w in W27})}
assert len(W27) == 27 and len(ROOTS) == 72

def snf_2(rows):
    """invariant factors of a 2 x n integer matrix: d1 = gcd of entries, d1 d2 = gcd of 2x2 minors."""
    a, b = rows
    d1 = reduce(gcd, [abs(x) for x in a + b], 0)
    minors = reduce(gcd, [abs(a[i] * b[j] - a[j] * b[i]) for i in range(len(a)) for j in range(i + 1, len(a))], 0)
    return [d1, minors // d1 if d1 else 0]

S0 = W27[0]
types = {}
for w in W27:
    if w == S0: continue
    types.setdefault(str(ip(S0, w)), []).append(w)
OUT["E"]["pair_types_from_one_weight"] = {k: len(v) for k, v in types.items()}
OUT["E"]["snf_by_type_from_one_weight"] = {k: sorted({tuple(snf_2([list(S0), list(w)])) for w in v}) for k, v in types.items()}
# all pairs of the 27, by inner product
allp = {}
for w, v in itertools.combinations(W27, 2):
    allp.setdefault(str(ip(w, v)), set()).add(tuple(snf_2([list(w), list(v)])))
OUT["E"]["snf_all_pairs_by_type"] = {k: sorted(v) for k, v in allp.items()}

# Recover the SM from a 16-type pair: roots orthogonal to both; Y orthogonal to both and to those roots
nu = types["1/3"][0]
orth_roots = [r for r in ROOTS if ip(r, S0) == 0 and ip(r, nu) == 0]
OUT["E"]["pair_used"] = {"S": S0, "nu^c": nu}
OUT["E"]["roots_orthogonal_to_pair"] = len(orth_roots)
# decompose the orthogonal roots: A2 + A1 means 8 roots; check the root graph splits as 6 + 2
def comps(rs):
    rs = list(rs); left = set(rs); out = []
    while left:
        x = left.pop(); comp = {x}; fr = [x]
        while fr:
            y = fr.pop()
            for z in list(left):
                if ip(y, z) != 0: left.discard(z); comp.add(z); fr.append(z)
        out.append(len(comp))
    return sorted(out)
OUT["E"]["orth_root_components"] = comps(orth_roots)
# Y: solve for y (Dynkin coords, rational) with ip(y, S0) = ip(y, nu) = 0 and ip(y, r) = 0 for the orthogonal roots
def nullspace_Q(rows, n):
    piv = {}; rows = [[F(x) for x in r] for r in rows]
    R = []
    for r in rows:
        for c, pr in piv.items():
            if r[c] != 0:
                f = r[c]; r = [x - f * y for x, y in zip(r, pr)]
        c0 = next((c for c in range(n) if r[c] != 0), None)
        if c0 is None: continue
        r = [x / r[c0] for x in r]
        for c in list(piv):
            if piv[c][c0] != 0:
                f = piv[c][c0]; piv[c] = [x - f * y for x, y in zip(piv[c], r)]
        piv[c0] = r
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * n; v[fc] = F(1)
        for c, pr in piv.items(): v[c] = -pr[fc]
        out.append(v)
    return out
def ip_row(l):  # row vector of ip(l, .) in Dynkin coordinates
    return [sum(l[i] * Ci[i][j] for i in range(6)) for j in range(6)]
# the pair fixes an A4 (SU(5)); the SM is the centraliser in it of a Y splitting the A4 chain as A2 + A1
gen_f = [F(7), F(-3), F(11), F(2), F(-5), F(13)]                      # a generic functional on Dynkin coordinates
pos = [r for r in orth_roots if sum(a * b for a, b in zip(gen_f, r)) > 0]
simple = [r for r in pos if not any(tuple(a - b for a, b in zip(r, s)) in pos for s in pos)]
assert len(simple) == 4
nbr = {i: [j for j in range(4) if j != i and ip(simple[i], simple[j]) != 0] for i in range(4)}
end = next(i for i in range(4) if len(nbr[i]) == 1)
chain = [end]
while len(chain) < 4:
    chain.append(next(j for j in nbr[chain[-1]] if j not in chain))
b1, b2, b3, b4 = [simple[i] for i in chain]
ys = nullspace_Q([ip_row(S0), ip_row(nu), ip_row(b1), ip_row(b2), ip_row(b4)], 6)
assert len(ys) == 1
y = ys[0]
sm_roots = [r for r in orth_roots if ip(r, y) == 0]
OUT["E"]["A4_simple_chain_found"] = True
OUT["E"]["SM_roots_after_Y"] = len(sm_roots)
OUT["E"]["SM_root_components"] = comps(sm_roots)
orth_roots_A4 = orth_roots
orth_roots = sm_roots
ch = [ip(w, y) for w in W27]
den = reduce(lambda a, b: a * b // gcd(a, b), [c.denominator for c in ch], 1)
chi_int = [int(c * den) for c in ch]
g = reduce(gcd, [abs(c) for c in chi_int], 0)
chi_int = [c // g for c in chi_int]
from collections import Counter
got = Counter(chi_int)
expect = Counter({1: 6, -4: 3, 2: 6, -3: 4, 6: 1, 0: 2, 3: 2, -2: 3})
flip = Counter({-k: v for k, v in got.items()})
OUT["E"]["sixY_multiset"] = dict(sorted(got.items()))
OUT["E"]["sixY_matches_SM_27"] = got == expect or flip == expect
sign = 1 if got == expect else -1
sixY = {w: sign * c for w, c in zip(W27, chi_int)}
OUT["E"]["pair_has_Y_zero"] = (sixY[S0], sixY[nu])
# the Y coweight in simple-coroot coordinates: <w, sum c_i a_i^v> = sum w_i c_i = 6Y(w)
cY = nullspace_Q([list(w) + [-sixY[w]] for w in W27], 7)
assert len(cY) == 1
cY = [x / cY[0][6] for x in cY[0][:6]]
OUT["E"]["Y_coweight_in_simple_coroots"] = [str(x) for x in cY]
OUT["E"]["Y_coweight_integral_primitive"] = all(x.denominator == 1 for x in cY) and reduce(gcd, [abs(int(x)) for x in cY]) == 1
# where the Y circle exp(2 pi i t cY) meets SU3 x SU2: t cY in span_R(coroots of the orthogonal roots) + Z^6
# coroot of a root r (simply laced) in simple-coroot coordinates = its expansion in simple roots: r = sum n_i alpha_i
def root_coeffs(r):  # solve r = sum n_i ALPHA[i] (Dynkin coords): n = r * C^{-1} (C symmetric)
    return [sum(r[i] * Ci[i][j] for i in range(6)) for j in range(6)]
ss_coroots = [root_coeffs(r) for r in orth_roots]
# t * cY in V + Z^6 for t = j/N: test j/N for N up to 36
def in_V_plus_Z(vec):
    # does there exist z in Z^6 with vec - z in V = span(ss_coroots)?  V has a rational basis; the condition is that the
    # image of vec in R^6 / V lies in the image of Z^6.  Use the annihilator: linear forms vanishing on V.
    ann = nullspace_Q(ss_coroots, 6)                       # forms phi with phi(v) = 0 on V (as row vectors)
    vals = [sum(a[i] * vec[i] for i in range(6)) for a in ann]
    # image of Z^6 under ann: lattice generated by the columns; check vals in it by brute force over a box of z
    # (the annihilator has rank 2 here; solve exactly with a small search)
    # exact lattice membership: scale to integers, column-reduce (Hermite), then solve triangularly
    D = reduce(lambda a, b: a * b // gcd(a, b), [x.denominator for a in ann for x in a] + [v.denominator for v in vals], 1)
    M = [[int(x * D) for x in a] for a in ann]; t = [int(v * D) for v in vals]
    cols = [[M[r][c] for r in range(len(M))] for c in range(6)]
    basis = []
    for r in range(len(M)):
        live = [c for c in cols if c[r] != 0]
        rest = [c for c in cols if c[r] == 0]
        while len(live) > 1:
            live.sort(key=lambda c: abs(c[r]))
            p = live[0]
            new = [p]
            for c in live[1:]:
                q = c[r] // p[r]
                c2 = [x - q * y for x, y in zip(c, p)]
                (new if c2[r] != 0 else rest).append(c2)
            live = new
        if live: basis.append((r, live[0]))
        cols = rest
    for r, b in basis:
        if t[r] % b[r] != 0: return False
        k = t[r] // b[r]; t = [x - k * y for x, y in zip(t, b)]
    return all(x == 0 for x in t)
hits = [F(j, 36) for j in range(1, 37) if in_V_plus_Z([F(j, 36) * x for x in cY])]
OUT["E"]["Y_circle_meets_SU3xSU2_at_t"] = [str(h) for h in hits]
# H_SM and the centre: the centre Z3 of E6^sc acts on every 27 weight by e^{2 pi i/3} (one class mod the root lattice);
# H_SM fixes the singlet S, so the centre's generator is not in H_SM
cls = sorted({str(ip(w, (1, 0, 0, 0, 0, 0)) % 1) for w in W27})       # 27 weights' pairing class with omega_1
fund_in_root_lattice = [all(x.denominator == 1 for x in root_coeffs(tuple(int(i == j) for j in range(6)))) for i in range(6)]
OUT["E"]["fundamental_weights_in_root_lattice"] = fund_in_root_lattice
OUT["E"]["27_weights_root_lattice_classes"] = sorted({tuple(str(x % 1) for x in root_coeffs(w)) for w in W27})

# ---------------------------------------------------------------- C: planted controls
CT = {}
CT["C5a_adjoint_cyclic_6k"] = OUT["K_is_cyclic_6k"]["adjoint only"]
CT["C5b_snf_(S,2nu)"] = snf_2([list(S0), [2 * x for x in nu]])
CT["C5b_check_snf_11"] = CT["C5b_snf_(S,2nu)"] == [1, 1]
CT["C5c_wrong_charge_Y_in_sixths_k1_e^c"] = None   # not meaningful: the U(1) action is not defined for fractional charges
CT["caught"] = {"C5a": not CT["C5a_adjoint_cyclic_6k"], "C5b": not CT["C5b_check_snf_11"]}
OUT["C"] = CT
print(json.dumps(OUT, indent=1, default=str))
json.dump(json.loads(json.dumps(OUT, default=str)), open(__file__.replace(".py", "_out.json"), "w"), indent=1)
