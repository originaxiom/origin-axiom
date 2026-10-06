"""Does s961's firing come down to m025? (PREREG efd8be94). chat1's own F_p code, s961 = ker w in pi1(m025)."""
import itertools, os, snappy
from collections import Counter

SRC = open(os.path.join(os.path.dirname(__file__), '..', 'chat1_2026-10-06_nonorientable_index', 'nonor_index.py')).read()
NS = {}
exec(SRC.split("M0 = snappy.Manifold('m000')")[0], NS)          # library part only (no runs)

def fourth_roots(p):
    i = next(x for x in range(2, p) if x * x % p == p - 1)
    return [1, i, p - 1, (p - i) % p]

def run(p):
    NS['p'] = p
    setup, pair_data, evw, nullspace, rank, dual = (NS[k] for k in ('setup', 'pair_data', 'evw', 'nullspace', 'rank', 'dual'))
    N3 = snappy.Manifold('m000').covers(3, cover_type='cyclic')[0]
    S = setup(N3, 'bAcb')
    hg, hrels, (cw, cg, cr) = S['hg'], S['hrels'], S['Mcusp']
    gens, w, SY = S['gens'], S['w'], S['SY']
    t = next(g for g in gens if w[g] == 1)
    # sigma: conjugation by t, rewritten in the Schreier symbols
    rw = lambda word: _rw(word, S)
    tconj = {s: rw([(t, 1)] + SY[s] + [(t, -1)]) for s in hg}
    # ---- characters of M trivial on the peripheral group (values in 4th roots of unity) ----
    R4 = fourth_roots(p)
    chars = []
    for vals in itertools.product(R4, repeat=len(hg)):
        ch = {s: [[v]] for s, v in zip(hg, vals)}
        if all(evw(ch, r, 1) == [[1]] for r in hrels) and all(evw(ch, c, 1) == [[1]] for c in cw):
            chars.append(tuple(vals))
    key = lambda ch: tuple(ch)
    inv = lambda v: pow(v, p - 2, p)
    def cdiv(a, b): return tuple((x * inv(y)) % p for x, y in zip(a, b))
    def csq(a): return tuple((x * x) % p for x in a)
    squares = {csq(c) for c in chars}
    def order(c):
        k = 1; cur = c
        while any(v != 1 for v in cur): cur = tuple((x * y) % p for x, y in zip(cur, c)); k += 1
        return k
    def sig_char(c):
        cd = dict(zip(hg, c)); return tuple(evw({s: [[cd[s]]] for s in hg}, tconj[s], 1)[0][0] for s in hg)
    # ---- extensions ----
    def ext(alpha, beta):
        A, B = dict(zip(hg, alpha)), dict(zip(hg, beta))
        def rep_of(cv): return {g: [[A[g], cv[i]], [0, B[g]]] for i, g in enumerate(hg)}
        C = [[evw(rep_of([int(i == k) for i in range(len(hg))]), R, 2)[0][1] for k in range(len(hg))] for R in hrels]
        Z = nullspace(C, len(hg)); b = [(A[g] - B[g]) % p for g in hg]
        span = [b] if any(b) else []; out = []
        for z in Z:
            if rank(span + [z]) > rank(span): out.append(rep_of(z)); span = span + [z]
        return out
    def index(V):
        n = len(V[hg[0]])
        U = pair_data(V, hg, hrels, cw, cg, cr, n); Ud = pair_data(dual(V), hg, hrels, cw, cg, cr, n)
        return (U['a1'] - U['r1']) - (Ud['a1'] - Ud['r1'])
    def h1(c):
        return NS['coh']({s: [[v]] for s, v in zip(hg, c)}, hg, hrels, 1)['a1']
    def iso(V, Wm):   # is there an invertible X with X V(g) = W(g) X for all g?
        rows = []
        for g in hg:
            for i in range(2):
                for j in range(2):   # (X V - W X)_{ij} as linear form in X entries x00 x01 x10 x11
                    row = [0] * 4
                    for k in range(2):
                        row[2 * i + k] = (row[2 * i + k] + V[g][k][j]) % p
                        row[2 * k + j] = (row[2 * k + j] - Wm[g][i][k]) % p
                    rows.append(row)
        B = nullspace(rows, 4)
        for coeffs in itertools.product(range(p), repeat=len(B)):
            X = [sum(c * b[k] for c, b in zip(coeffs, B)) % p for k in range(4)]
            if (X[0] * X[3] - X[1] * X[2]) % p: return True
        return False
    def sigma(V): return {s: evw(V, tconj[s], 2) for s in hg}
    def induce(V):   # Ind_M^N V on cosets {1, t}; block (j, i) = V(t^-j g t^i) when g t^i lies in t^j M
        out = {}
        for g in gens:
            Mx = [[0] * 4 for _ in range(4)]
            for i in (0, 1):
                j = (i + w[g]) % 2
                word = [(t, -1)] * j + [(g, 1)] + [(t, 1)] * i
                h = evw(V, rw(word), 2)
                for a in range(2):
                    for b2 in range(2): Mx[2 * j + a][2 * i + b2] = h[a][b2]
            out[g] = Mx
        return out
    Nc = S['Ncusp']
    def indexN(U):
        n = len(U[gens[0]])
        A = pair_data(U, gens, S['rels'], *Nc, n); D = pair_data(dual(U), gens, S['rels'], *Nc, n)
        return (A['a1'] - A['r1']) - (D['a1'] - D['r1'])
    # ---- the census ----
    loci = [l for l in chars if h1(l) >= 1]
    h1s = Counter(h1(l) for l in loci)
    res = {}
    for order_name, sub in (('alpha-sub', True), ('beta-sub', False)):
        firing = []
        for lam in loci:
            for alpha in chars:
                beta = cdiv(alpha, lam)
                for V in (ext(alpha, beta) if sub else ext(beta, alpha)):
                    I = index(V)
                    if I: firing.append((lam, alpha, V, I))
        res[order_name] = firing
    fixedchars = [c for c in chars if sig_char(c) == c]
    print(f"\np = {p}: Schreier gens {hg}; peripheral-trivial characters {len(chars)}; loci {len(loci)} (h1 {dict(h1s)});"
          f" non-square loci {sum(l not in squares for l in loci)}")
    for name, F in res.items():
        per = Counter(f[0] for f in F)
        print(f"  C1 [{name}] firing {len(F)} of {len(loci) * len(chars)}; on non-square loci {sum(f[0] not in squares for f in F)};"
              f" per locus {sorted(Counter(per.values()).items())}; index values {dict(Counter(f[3] for f in F))}")
    print(f"  D1 sigma-fixed characters {len(fixedchars)}, orders {sorted(order(c) for c in fixedchars)}; "
          f"all order<=2 characters {sum(order(c) <= 2 for c in chars)}")
    for name, F in res.items():
        fixed = 0; pairs_eq = 0; partner_found = 0; ind_ok = 0
        for lam, alpha, V, I in F:
            sV = sigma(V)
            if iso(V, sV): fixed += 1
            partners = [f for f in F if iso(sV, f[2])]
            if partners: partner_found += 1; pairs_eq += all(f[3] == I for f in partners)
            ind_ok += (indexN(induce(V)) == I)
        print(f"  D2 [{name}] sigma-fixed firing modules {fixed}; sigma*V found among firing {partner_found}/{len(F)}; "
              f"same index as partner {pairs_eq}/{len(F)}")
        print(f"  D3 [{name}] I(m025; Ind V) = I(s961; V): {ind_ok}/{len(F)}")
    return res

def _rw(word, S):
    w = S['w']; triv = [s for s, wd in S['SY'].items() if len(wd) == 2 and wd[0][0] == wd[1][0] and wd[0][1] == -wd[1][1]]
    cur = 0; out = []
    for g, e in word:
        if e == 1: out.append((f"s{cur}{g}", 1)); cur = (cur + w[g]) % 2
        else: nw = (cur - w[g]) % 2; out.append((f"s{nw}{g}", -1)); cur = nw
    assert cur == 0
    return [(s, e) for s, e in out if s not in triv]

if __name__ == '__main__':
    for p in (13, 29, 37):
        run(p)
