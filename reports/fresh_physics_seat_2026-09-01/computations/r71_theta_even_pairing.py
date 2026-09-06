"""R71 (part 2) -- what R70's pairing is, as a theorem, and where it stops.

Setting (R69/R70): a theta-even U(1) direction u in the E6 Cartan, charges on the two Fix(theta) arcs with equal signs;
Pantev-Wijnholt's count gives net(R_q) = +2 for q > 0 and -2 for q < 0 (or all signs flipped), so the left-handed
spectrum is  S(u) = 2 (+)_{q>0} 27_q  (+)  2 (+)_{q<0} conj(27_q).

THEOREM (pure representation theory).  theta is outer on E6, so 27 o theta = 27bar; theta fixes u, so it preserves
the charge grading; hence conj(27_{-q}) = (27_q) o theta and  S(u) = 2 (+)_{q>0} ( 27_q  (+)  27_q o theta ).
Every charged component comes with its theta-twist.  Whether that makes S(u) self-conjugate under the unbroken group
C(u) is a separate question, answered here at three levels for many theta-even u:
  (i)   under the semisimple part C(u)'            (T''-weights: the values <lambda, alpha^vee> on the roots of C(u))
  (ii)  under the centre of C(u) orthogonal to u    (the extra U(1)s, if any)
  (iii) under U(1)_u itself                         (always chiral: that is the anomalous U(1) of PW's abelian toy)

Everything is in Bourbaki E6 Dynkin labels (integers); sympy only for nullspaces over Q.
"""
import itertools, random, collections
from fractions import Fraction as Fr
import sympy as sp

C = sp.Matrix([[ 2, 0,-1, 0, 0, 0],
               [ 0, 2, 0,-1, 0, 0],
               [-1, 0, 2,-1, 0, 0],
               [ 0,-1,-1, 2,-1, 0],
               [ 0, 0, 0,-1, 2,-1],
               [ 0, 0, 0, 0,-1, 2]])
Cinv = C.inv()
rows = [tuple(int(x) for x in C.row(i)) for i in range(6)]
def refl(lam, i):  # s_i on Dynkin labels: lam - lam_i * alpha_i, alpha_i = row i of C
    return tuple(l - lam[i]*r for l, r in zip(lam, rows[i]))
def orbit(hw):
    seen = {hw}; frontier = [hw]
    while frontier:
        new = []
        for lam in frontier:
            for i in range(6):
                mu = refl(lam, i)
                if mu not in seen: seen.add(mu); new.append(mu)
        frontier = new
    return sorted(seen)
W27 = orbit((1,0,0,0,0,0)); ROOTS = orbit((0,1,0,0,0,0))
assert len(W27) == 27 and len(ROOTS) == 72
FLIP = [5, 1, 4, 3, 2, 0]                       # Bourbaki 1<->6, 3<->5
theta = lambda lam: tuple(lam[FLIP[i]] for i in range(6))
assert set(theta(l) for l in W27) == set(tuple(-x for x in l) for l in W27), "27 o theta = 27bar (theta outer)"
assert set(theta(a) for a in ROOTS) == set(ROOTS)
print("E6 in Bourbaki Dynkin labels: 27 weights, 72 roots; theta = diagram flip, 27 o theta = 27bar: True")
neg = lambda v: tuple(-x for x in v)
dot = lambda a, b: sum(x*y for x, y in zip(a, b))
def root_coords(alpha):   # simple-root coefficients of a root given by its Dynkin labels
    v = Cinv*sp.Matrix(alpha); return tuple(Fr(int(x.p), int(x.q)) for x in v)
RC = {a: root_coords(a) for a in ROOTS}
assert all(all(x.denominator == 1 for x in RC[a]) for a in ROOTS)
RC27 = {l: root_coords(l) for l in W27}            # weights of the 27 in simple-root coordinates (thirds)
# <lambda, omega_k^vee> = the alpha_k-coefficient of lambda (NOT its Dynkin label, which is <lambda, alpha_k^vee>)
assert all(dot(FrC := (1,0,0,0,0,0), RC27[l]) in (Fr(4,3), Fr(1,3), Fr(-2,3)) for l in W27)

def analyse(c, label, verbose=True):
    """c = coweight coefficients of u = sum c_k omega_k^vee. Charges q(lambda) = <lambda, u> = c . (root coordinates of lambda)."""
    c = tuple(Fr(x) for x in c)
    even = tuple(c[FLIP[i]] for i in range(6)) == c
    q = {l: dot(c, RC27[l]) for l in W27}
    bycharge = collections.Counter(q.values())
    # the spectrum S(u): multiset of T-weights
    S = []
    for l in W27:
        if q[l] > 0: S += [l, l]
        elif q[l] < 0: S += [neg(l), neg(l)]
    # theorem check: {-lambda : q < 0} == {theta(mu) : q(mu) > 0}
    thm = collections.Counter(neg(l) for l in W27 if q[l] < 0) == collections.Counter(theta(l) for l in W27 if q[l] > 0)
    # C(u): roots with q = 0
    cu = [a for a in ROOTS if dot(c, RC[a]) == 0]
    # (i) T''-signatures
    sig = lambda l: tuple(dot(RC[a], l) for a in cu)
    Ssig = collections.Counter(sig(l) for l in S)
    vl_semisimple = Ssig == collections.Counter(neg(s) for s in Ssig.elements())
    # rank of the semisimple part = rank of the root span
    rk = sp.Matrix([list(a) for a in cu]).rank() if cu else 0
    # (ii) centre of C(u): h = sum d_k omega_k^vee with d . alpha = 0 for all alpha in cu; Killing-orthogonal to u: d^T Cinv c = 0
    cons = [[sp.Rational(x.numerator, x.denominator) for x in RC[a]] for a in cu] + [list((Cinv*sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in c])).T)]
    Z = sp.Matrix(cons).nullspace() if cons else []
    extra = []
    for h in Z:
        d = tuple(Fr(int(x.p), int(x.q)) for x in h)
        ch = collections.Counter(dot(d, l) for l in S)
        extra.append(ch == collections.Counter(-x for x in ch.elements()))
    if Z:
        d = tuple(sum(Fr(int(h[i].p), int(h[i].q))*random.randint(-5, 5) for h in Z) for i in range(6))
        ch = collections.Counter(dot(d, l) for l in S); extra.append(ch == collections.Counter(-x for x in ch.elements()))
    vl_extra = all(extra) if extra else None
    # (iii) U(1)_u itself
    chu = collections.Counter(q[l] if q[l] > 0 else -q[l] for l in W27 if q[l] != 0)
    tot = sum(dot(c, RC27[l]) if l in RC27 else -dot(c, RC27[neg(l)]) for l in S)
    if verbose:
        print(f"[u = {label}] theta-even: {even}; 27 by charge: {dict(sorted(bycharge.items()))}; "
              f"C(u): {len(cu)} roots, rank {rk} (dim {6 + len(cu)}); centre dim {6 - rk} (of which orthogonal to u: {len(Z)})")
        print(f"      S = 2(+)_{{q>0}}(27_q (+) 27_q o theta): {thm};  vector-like under C(u)': {vl_semisimple};  "
              f"under the extra centre U(1)s: {vl_extra};  net U(1)_u charge of S: {tot}")
    return dict(even=even, thm=thm, vl=vl_semisimple, vl_extra=vl_extra, roots=len(cu), rank=rk, centre=6 - rk, tot=tot)

E = [0]*6
def cw(*ks):  # sum of fundamental coweights (1-based)
    v = [0]*6
    for k in ks: v[k-1] += 1
    return v
random.seed(7)
print("\n== R70's four theta-even coweight directions ==")
res = {}
for lab, c in (("w2", cw(2)), ("w4", cw(4)), ("w1+w6", cw(1, 6)), ("w3+w5", cw(3, 5))):
    res[lab] = analyse(c, lab)
assert all(r['even'] and r['thm'] for r in res.values())
assert res['w2']['vl'] and res['w1+w6']['vl'] and not res['w4']['vl'] and not res['w3+w5']['vl']
print("   -> R70's pairing claim holds at the representation level for w2 (A5) and w1+w6 (D4) and FAILS for w4 (A2+A2+A1) and w3+w5 (A1+A2+A1):")
print("      R70 paired the charged components by dimension; the theta-twist is conjugation on A5 and D4 but swaps the two A2's.")
print("\n== control: theta-odd / mixed directions (R69's count does not apply; shown so the test can fail) ==")
for lab, c in (("w1 (D5 x U(1), the 16-direction)", cw(1)), ("w6", cw(6)), ("w3", cw(3)), ("w5", cw(5)), ("w1-w6 (theta-odd)", [1,0,0,0,0,-1])):
    r = analyse(c, lab); assert not r['even']
    res[lab] = r
assert not res["w1 (D5 x U(1), the 16-direction)"]['vl'] and not res["w1 (D5 x U(1), the 16-direction)"]['thm']   # 2(1 + 16 + 10bar): chiral, and no theta-pairing

# ---------- decomposition of S(u) into irreps of C(u)' and its chiral part
POS = [a for a in ROOTS if all(x >= 0 for x in RC[a])]
def cu_simple(cu):
    pos = [a for a in cu if a in POS]
    simple = [a for a in pos if not any((b != a and tuple(x - y for x, y in zip(RC[a], RC[b])) in {RC[r] for r in pos}) for b in pos)]
    return pos, simple
def decompose(c, S):
    c = tuple(Fr(x) for x in c)
    cu = [a for a in ROOTS if dot(c, RC[a]) == 0]
    pos, simple = cu_simple(cu)
    def refl_c(l, a):  # reflection in the root a (Dynkin labels of l; <l, a^vee> = RC[a] . l)
        k = dot(RC[a], l); return tuple(x - k*y for x, y in zip(l, a))
    def dom(l): return all(dot(RC[a], l) >= 0 for a in simple)
    def orbit_c(l):
        seen = {l}; fr = [l]
        while fr:
            new = []
            for m in fr:
                for a in simple:
                    n = refl_c(m, a)
                    if n not in seen: seen.add(n); new.append(n)
            fr = new
        return seen
    def weyl_dim(l):
        num = den = Fr(1)
        for a in pos:
            num *= dot(RC[a], l) + 1; den *= 1     # <l + rho, a^vee> = <l,a^vee> + ht(a) for simply laced; use rho via heights
        # proper: <rho, a^vee> = height of a in C(u)'s simple roots; compute heights by solving
        return None
    left = collections.Counter(S)
    irreps = []
    while left:
        # highest weight: maximal for the partial order given by pos; pick the dominant weight with max height
        cands = [l for l in left if dom(l)]
        assert cands, "no dominant weight left"
        hw = max(cands, key=lambda l: sum(dot(RC[a], l) for a in pos))
        O = orbit_c(hw)
        # the irrep must have all its weights in `left`; for our minuscule-type restrictions the irrep IS the orbit -- verify no
        # dominant weight strictly below hw is 'missing' by checking the orbit is contained and consuming it
        assert all(left[m] >= 1 for m in O), ("irrep not a single orbit", hw)
        for m in O: 
            left[m] -= 1
            if left[m] == 0: del left[m]
        irreps.append((hw, len(O)))
    # names: Dynkin labels w.r.t. C(u)' simple roots (ordered as found) plus dimension; conjugate = highest weight of orbit of -hw
    def labels(hw): return tuple(int(dot(RC[a], hw)) for a in simple)
    def conj_hw(hw):
        O = orbit_c(neg(hw)); return next(m for m in O if dom(m))
    out = collections.Counter(); chiral = collections.Counter()
    for hw, d in irreps: out[(labels(hw), d)] += 1
    for hw, d in irreps:
        chiral[(labels(hw), d)] += 1; chiral[(labels(conj_hw(hw)), d)] -= 1
    chiral = {k: v for k, v in chiral.items() if v != 0}
    return simple, out, chiral
def factors(simple):
    """split C(u)'s simple roots into connected components (simple factors), each as an ordered chain where possible"""
    n = len(simple); adj = {i: [j for j in range(n) if j != i and dot(RC[simple[i]], simple[j]) != 0] for i in range(n)}
    comps = []; seen = set()
    for i in range(n):
        if i in seen: continue
        comp = []; st = [i]
        while st:
            k = st.pop()
            if k in seen: continue
            seen.add(k); comp.append(k); st += adj[k]
        comps.append(sorted(comp))
    out = []
    for comp in comps:
        ends = [i for i in comp if len([j for j in adj[i] if j in comp]) <= 1]
        branched = any(len([j for j in adj[i] if j in comp]) == 3 for i in comp)
        if branched: out.append((f'D{len(comp)}' if len(comp) <= 5 else 'E6', comp)); continue     # D4/D5 inside E6: no cubic anomaly
        # order the chain from one end
        chain = [ends[0]]
        while len(chain) < len(comp):
            nxt = [j for j in adj[chain[-1]] if j in comp and j not in chain]; chain.append(nxt[0])
        out.append((f'A{len(comp)}', chain))
    return out
def cubic_anomaly(S, simple, fac):
    """A(S) under an A_{N-1} factor, normalised to A(fundamental) = 1, via h = sum_i (N-i) alpha_i^vee."""
    typ, chain = fac
    if not typ.startswith('A') or len(chain) < 2: return 0
    N = len(chain) + 1
    h = [(N - i) for i in range(1, N)]
    tr = sum(sum(ci*dot(RC[simple[k]], l) for ci, k in zip(h, chain))**3 for l in S)
    return Fr(tr, (N - 1)*N*(N - 2))
def show(c, label):
    c = tuple(Fr(x) for x in c)
    q = {l: dot(c, RC27[l]) for l in W27}
    S = []
    for l in W27:
        if q[l] > 0: S += [l, l]
        elif q[l] < 0: S += [neg(l), neg(l)]
    simple, out, chiral = decompose(c, S)
    # simple roots of C(u) as E6 root coordinates -> the type is read off their Cartan matrix blocks
    cm = [[dot(RC[a], b) for b in simple] for a in simple]
    print(f"[u = {label}] C(u)' simple roots (E6 root coords): {[tuple(int(x) for x in RC[a]) for a in simple]}")
    print(f"      S(u) = " + " + ".join(f"{m} x {d}{lab}" for (lab, d), m in sorted(out.items(), key=lambda kv: -kv[0][1])))
    print(f"      chiral part S - conj(S) = " + (" + ".join(f"{m:+d} x {d}{lab}" for (lab, d), m in sorted(chiral.items(), key=lambda kv: -kv[0][1])) if chiral else "0  (vector-like)"))
    fac = factors(simple)
    an = {f"{typ}[{','.join(str(k+1) for k in ch)}]": cubic_anomaly(S, simple, (typ, ch)) for typ, ch in fac}
    print(f"      C(u)' factors (by position in the simple-root list): {[t for t, _ in fac]};  cubic anomaly of S per SU(N>=3) factor: { {k: str(v) for k, v in an.items() if not k.startswith('A1') and not k.startswith('D')} }")
    return chiral, an
print("\n== the spectra decomposed under C(u)' (labels = Dynkin labels on C(u)'s simple roots, in the order listed) ==")
for lab, c in (("w2", cw(2)), ("w4", cw(4)), ("w1+w6", cw(1, 6)), ("w3+w5", cw(3, 5)), ("control w1", cw(1))):
    show(c, lab)

print("\n== all other theta-even directions spanned by the four with small coefficients (sums, differences, generic) ==")
basis4 = [cw(2), cw(4), cw(1, 6), cw(3, 5)]
seen = set(); rows_out = []
for coeffs in itertools.product([-2, -1, 0, 1, 2, 3], repeat=4):
    if all(x == 0 for x in coeffs): continue
    c = tuple(sum(k*b[i] for k, b in zip(coeffs, basis4)) for i in range(6))
    # normalise sign/scale: skip if a positive multiple already seen, and skip the negative (S -> conj S)
    g = 0
    for x in c: g = sp.gcd(g, x)
    cn = tuple(x // g for x in c)
    if cn in seen or neg(cn) in seen: continue
    seen.add(cn)
    r = analyse(cn, str(coeffs), verbose=False)
    assert r['even'] and r['thm']
    # anomaly under the SU(N>=3) factors of C(u)'
    cq = {l: dot(cn, RC27[l]) for l in W27}
    Sw = []
    for l in W27:
        if cq[l] > 0: Sw += [l, l]
        elif cq[l] < 0: Sw += [neg(l), neg(l)]
    cu_ = [a for a in ROOTS if dot(cn, RC[a]) == 0]; pos_, simple_ = cu_simple(cu_)
    fac = factors(simple_)
    r['types'] = '+'.join(sorted(t for t, _ in fac)) or '-'
    r['anom'] = any(cubic_anomaly(Sw, simple_, f) != 0 for f in fac)
    rows_out.append((coeffs, cn, r))
byC = collections.defaultdict(list)
for coeffs, cn, r in rows_out: byC[(r['types'], r['roots'], r['rank'])].append((coeffs, cn, r))
print(f"{'C(u)prime type':16} {'roots':6} {'#dirs':6} {'vector-like':12} {'chiral+anomalous':17} {'chiral+anomaly-free'}")
tot_chiral_free = 0
for key in sorted(byC, key=lambda k: (-k[1], k[0])):
    L = byC[key]
    nvl = sum(1 for _, _, r in L if r['vl']); nca = sum(1 for _, _, r in L if not r['vl'] and r['anom']); ncf = sum(1 for _, _, r in L if not r['vl'] and not r['anom'])
    tot_chiral_free += ncf
    print(f"{key[0]:16} {key[1]:<6} {len(L):<6} {nvl:<12} {nca:<17} {ncf}")
print(f"\ntheta-even directions tested: {len(rows_out)};  theorem S = 2(+)_{{q>0}}(27_q (+) 27_q o theta) holds for all: True")
print(f"chiral under C(u)' AND free of cubic anomalies under every SU(N>=3) factor: {tot_chiral_free}")
# which chiral+anomaly-free cases exist, if any, and what C(u)' they have
for coeffs, cn, r in rows_out:
    if not r['vl'] and not r['anom']: print("   chiral, anomaly-free:", coeffs, "C(u)' =", r['types'])
print("\nSELFTEST: PASS")
