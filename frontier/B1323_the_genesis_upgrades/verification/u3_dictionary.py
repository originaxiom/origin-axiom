#!/usr/bin/env python3
"""B1323 U3 -- the dictionary lemma between the genesis chain C1-C5 and the uniqueness theorem's A1-A6
(pre-registered in DESIGN.md section 5; exact integer arithmetic, SnapPy for the one identification).

(i)   St = <E, G, Gt> (Mignosi-Seebold): incidence matrices are non-negative GL(2,Z) matrices, each a product of L, R, P;
      conversely every non-negative GL(2,Z) matrix with entries <= 13 is realised by an explicit morphism of St.
(ii)  Fibonacci a->ab, b->a has matrix L.P (det -1); (LP)^2 = LR = A, (PL)^2 = RL, PLP = R -- A7 is the swap's placement.
(iii) H1(S_{1,1}) = Z^2 and the once-punctured-torus bundle a*B is m004 (twister + identify).
(iv)  the cutting sequence of the expanding eigenline of A is the Fibonacci word (up to the a/b naming).
"""
import io, contextlib, itertools, json, math, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent

# ---------- morphisms and matrices ----------
E = {'a': 'b', 'b': 'a'}; G = {'a': 'a', 'b': 'ab'}; Gt = {'a': 'a', 'b': 'ba'}
GENS = {'E': E, 'G': G, 'Gt': Gt}
def compose(f, g):            # (f o g)(x) = f(g(x))
    return {x: ''.join(f[c] for c in g[x]) for x in 'ab'}
def incidence(f):             # M = [[|f(a)|_a, |f(b)|_a], [|f(a)|_b, |f(b)|_b]]
    return ((f['a'].count('a'), f['b'].count('a')), (f['a'].count('b'), f['b'].count('b')))
def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def det(A): return A[0][0] * A[1][1] - A[0][1] * A[1][0]
L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); P = ((0, 1), (1, 0)); I = ((1, 0), (0, 1))
def nonneg(A): return all(x >= 0 for row in A for x in row)

def lrp_word(M):
    """Decide membership of a non-negative GL(2,Z) matrix in the monoid <L, R, P> by Euclidean peeling.
    Returns the word (list of 'L','R','P') with M = product, or None."""
    word = []
    A = tuple(tuple(r) for r in M)
    for _ in range(10_000):
        if A == I: return word
        if A == P: return word + ['P']
        r0, r1 = A
        if r0[0] >= r1[0] and r0[1] >= r1[1] and r1 != (0, 0) and r0 != r1:
            word.append('L'); A = ((r0[0] - r1[0], r0[1] - r1[1]), r1)          # A = L * A'
        elif r1[0] >= r0[0] and r1[1] >= r0[1] and r0 != (0, 0) and r0 != r1:
            word.append('R'); A = (r0, (r1[0] - r0[0], r1[1] - r0[1]))          # A = R * A'
        else:
            return None
    return None

def st_morphism_from_lrp(word):
    """Realise an <L,R,P>-word as a morphism of St: L -> G, R -> E G E, P -> E (matrices multiply in the same order)."""
    f = {'a': 'a', 'b': 'b'}
    for w in word:
        g = {'L': G, 'R': compose(E, compose(G, E)), 'P': E}[w]
        f = compose(f, g)
    return f

def part_i():
    out = {}
    # generate St to word length 7
    morphs = {(): {'a': 'a', 'b': 'b'}}
    frontier = [()]
    for _ in range(7):
        nxt = []
        for w in frontier:
            for name, g in GENS.items():
                ww = w + (name,); morphs[ww] = compose(morphs[w], g); nxt.append(ww)
        frontier = nxt
    mats = {}
    bad_det = bad_nonneg = bad_lrp = 0
    for w, f in morphs.items():
        M = incidence(f); mats.setdefault(M, w)
        if abs(det(M)) != 1: bad_det += 1
        if not nonneg(M): bad_nonneg += 1
        if lrp_word(M) is None: bad_lrp += 1
    out['st_words'] = len(morphs); out['distinct_matrices'] = len(mats)
    out['matrices_not_in_GL2Z'] = bad_det; out['matrices_not_nonneg'] = bad_nonneg; out['matrices_not_in_LRP_monoid'] = bad_lrp
    # every matrix of St to length 7 also checked to be a {L,P}-word (the generators' images): M(E)=P, M(G)=M(Gt)=L
    out['M(E)'] = incidence(E); out['M(G)'] = incidence(G); out['M(Gt)'] = incidence(Gt)
    # converse: every non-negative GL(2,Z) matrix with entries <= 13 is realised by a morphism of St
    B = 13; total = realised = failed = 0; witness_fail = None
    for a, b, c, d in itertools.product(range(B + 1), repeat=4):
        M = ((a, b), (c, d))
        if abs(det(M)) != 1: continue
        total += 1
        w = lrp_word(M)
        if w is None: failed += 1; witness_fail = witness_fail or M; continue
        f = st_morphism_from_lrp(w)
        if incidence(f) == M: realised += 1
        else: failed += 1; witness_fail = witness_fail or M
    out['nonneg_GL2Z_entries_le_13'] = total; out['realised_by_St'] = realised; out['not_realised'] = failed; out['first_failure'] = witness_fail
    out['PASS'] = (bad_det == 0 and bad_nonneg == 0 and bad_lrp == 0 and failed == 0)
    return out

def part_ii():
    Fib = {'a': 'ab', 'b': 'a'}
    M = incidence(Fib)
    facts = {
        'M(Fib)': M, 'M(Fib) == L.P': M == mul(L, P), 'det M(Fib)': det(M),
        '(LP)^2': mul(mul(L, P), mul(L, P)), 'LR': mul(L, R), 'A': ((2, 1), (1, 1)),
        '(LP)^2 == LR == A': mul(mul(L, P), mul(L, P)) == mul(L, R) == ((2, 1), (1, 1)),
        '(PL)^2': mul(mul(P, L), mul(P, L)), 'RL': mul(R, L), '(PL)^2 == RL': mul(mul(P, L), mul(P, L)) == mul(R, L),
        'PLP == R': mul(mul(P, L), P) == R, 'PRP == L': mul(mul(P, R), P) == L,
        'LR and RL conjugate by P': mul(mul(P, mul(L, R)), P) == mul(R, L),
        'charpoly LR': 't^2 - %dt + %d' % (mul(L, R)[0][0] + mul(L, R)[1][1], det(mul(L, R))),
        # the based invariant (B979): Mobius fixed-point polynomials of LR and RL
        'mobius fixed-point poly LR (z -> (2z+1)/(z+1))': 'z^2 - z - 1',
        'mobius fixed-point poly RL (z -> (z+1)/(z+2))': 'z^2 + z - 1',
    }
    # verify the two fixed-point polynomials symbolically-by-integers: for M=((p,q),(r,s)), fixed points of z->(pz+q)/(rz+s): r z^2 + (s-p) z - q = 0
    def fp(Mx):
        (p, q), (r, s) = Mx; return (r, s - p, -q)
    facts['fp coefficients LR (r, s-p, -q)'] = fp(mul(L, R)); facts['fp coefficients RL'] = fp(mul(R, L))
    facts['PASS'] = all(facts[k] for k in ['M(Fib) == L.P', '(LP)^2 == LR == A', '(PL)^2 == RL', 'PLP == R', 'PRP == L', 'LR and RL conjugate by P']) \
        and fp(mul(L, R)) == (1, -1, -1) and fp(mul(R, L)) == (1, 1, -1)
    return facts

def part_iii():
    out = {'H1 rank formula 2g+p-1 for (1,1)': 2 * 1 + 1 - 1}
    try:
        import snappy
        from snappy import twister
        S = twister.Surface('S_1_1')
        M = S.bundle(monodromy='a*B')
        for _ in range(20):
            if 'positively' in M.solution_type(): break
            M.randomize()
        out['a*B solution'] = M.solution_type(); out['a*B volume'] = float(M.volume()); out['a*B identify'] = [str(x) for x in M.identify()]
        out['a*B homology'] = str(M.homology()); out['a*B cusps'] = M.num_cusps()
        m004 = snappy.Manifold('m004'); out['isometric to m004'] = bool(M.is_isometric_to(m004))
        out['PASS'] = out['isometric to m004'] and out['a*B cusps'] == 1
    except Exception as e:
        out['error'] = repr(e); out['PASS'] = False
    return out

def part_iv():
    # Fibonacci word (fixed point of a->ab, b->a) vs the cutting sequence of the expanding eigenline of A = LR
    w = 'a'
    while len(w) < 2000: w = ''.join({'a': 'ab', 'b': 'a'}[c] for c in w)
    fib = w[:600]
    phi = (1 + 5 ** 0.5) / 2
    # A = [[2,1],[1,1]]: eigenvector for phi^2 is (phi, 1): slope 1/phi. Cutting sequence of y = x/phi from the origin,
    # 'a' at each vertical grid line x = n, 'b' at each horizontal line y = m, ordered by the parameter x.
    events = []
    N = 600
    for n in range(1, N): events.append((n, 'a'))
    m = 1
    while m * phi < N: events.append((m * phi, 'b')); m += 1
    events.sort()
    cut = ''.join(t for _, t in events)[:600]
    swap = cut.translate(str.maketrans('ab', 'ba'))
    out = {'eigenvector of A for phi^2': '(phi, 1), slope 1/phi', 'cutting == fib': cut == fib, 'cutting(swapped) == fib': swap == fib,
           'fib[:40]': fib[:40], 'cut[:40]': cut[:40]}
    # the eigenline's slope as a continued fraction: 1/phi = [0; 1, 1, 1, ...]
    x = 1 / phi; cf = []
    for _ in range(12):
        a = math.floor(x); cf.append(a); x = 1 / (x - a) if x - a > 1e-12 else 0
    out['cf(1/phi)'] = cf
    out['PASS'] = (cut == fib or swap == fib) and cf[1:11] == [1] * 10
    return out

if __name__ == '__main__':
    res = {'i': part_i(), 'ii': part_ii(), 'iii': part_iii(), 'iv': part_iv()}
    res['PASS'] = all(res[k]['PASS'] for k in 'i ii iii iv'.split())
    (HERE / 'u3_dictionary.json').write_text(json.dumps(res, indent=1, default=str), encoding='utf-8')
    for k in 'i ii iii iv'.split():
        print(f"[{'PASS' if res[k]['PASS'] else 'FAIL'}] part ({k})")
        for kk, v in res[k].items():
            if kk != 'PASS': print(f"    {kk}: {v}")
    print('U3 DICTIONARY:', 'PASS' if res['PASS'] else 'FAIL')
    sys.exit(0 if res['PASS'] else 1)
