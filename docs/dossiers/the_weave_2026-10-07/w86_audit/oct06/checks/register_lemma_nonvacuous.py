"""Audit: a NON-vacuous instance of chat1's register lemma I(M; p*U) = I_w(N;U) + I_w(N;U(x)w), using nonor_index.py's own
library (loaded exactly as firing_descent.py loads it). U = Ind_M^N V for every firing V on s961 = ker w in pi1(m025),
alpha-sub stacking order, p = 13. Expected: I(M; p*U) = I(V) + I(sigma*V) = 2 I(V) = +-2, and I_w(U) = I_w(Uw) = I(V)."""
import sys, itertools, snappy
from collections import Counter
SRC = open(sys.argv[1]).read(); NS = {}
exec(SRC.split("M0 = snappy.Manifold('m000')")[0], NS)
FD = open(sys.argv[2]).read(); FDNS = {}
exec(FD.split("if __name__ == '__main__':")[0].replace("SRC = open(os.path.join(os.path.dirname(__file__), '..', 'chat1_2026-10-06_nonorientable_index', 'nonor_index.py')).read()", "SRC = open(%r).read()" % sys.argv[1]), FDNS)
p = 13; NS['p'] = p
setup, pair_data, evw, nullspace, rank, dual, twist = (NS[k] for k in ('setup', 'pair_data', 'evw', 'nullspace', 'rank', 'dual', 'twist'))
N3 = snappy.Manifold('m000').covers(3, cover_type='cyclic')[0]
S = setup(N3, 'bAcb'); hg, hrels, Mc, gens, w, SY, Nc = S['hg'], S['hrels'], S['Mcusp'], S['gens'], S['w'], S['SY'], S['Ncusp']
cw, cg, cr = Mc
t = next(g for g in gens if w[g] == 1)
rw = lambda word: FDNS['_rw'](word, S)
i4 = next(x for x in range(2, p) if x * x % p == p - 1); R4 = [1, i4, p - 1, (p - i4) % p]
chars = []
for vals in itertools.product(R4, repeat=len(hg)):
    ch = {s: [[v]] for s, v in zip(hg, vals)}
    if all(evw(ch, r, 1) == [[1]] for r in hrels) and all(evw(ch, c, 1) == [[1]] for c in cw): chars.append(tuple(vals))
inv = lambda v: pow(v, p - 2, p)
def ext(alpha, beta):
    A, B = dict(zip(hg, alpha)), dict(zip(hg, beta))
    def rep_of(cv): return {g: [[A[g], cv[i]], [0, B[g]]] for i, g in enumerate(hg)}
    C = [[evw(rep_of([int(i == k) for i in range(len(hg))]), R, 2)[0][1] for k in range(len(hg))] for R in hrels]
    Z = nullspace(C, len(hg)); b = [(A[g] - B[g]) % p for g in hg]; span = [b] if any(b) else []; out = []
    for z in Z:
        if rank(span + [z]) > rank(span): out.append(rep_of(z)); span = span + [z]
    return out
def n_(U, gs, rels, cusp, d): D = pair_data(U, gs, rels, *cusp, d); return D['a1'] - D['r1']
def IM(V, d): return n_(V, hg, hrels, Mc, d) - n_(dual(V), hg, hrels, Mc, d)
def Iw(U, d): return n_(U, gens, S['rels'], Nc, d) - n_(twist(dual(U), w), gens, S['rels'], Nc, d)
def induce(V):
    out = {}
    for g in gens:
        Mx = [[0] * 4 for _ in range(4)]
        for i in (0, 1):
            j = (i + w[g]) % 2; h = evw(V, rw([(t, -1)] * j + [(g, 1)] + [(t, 1)] * i), 2)
            for a in range(2):
                for b2 in range(2): Mx[2 * j + a][2 * i + b2] = h[a][b2]
        out[g] = Mx
    return out
def pull(U): return {s: evw(U, SY[s], 4) for s in hg}
res = Counter(); ok = 0; n = 0
for lam in chars:
    if NS['coh']({s: [[v]] for s, v in zip(hg, lam)}, hg, hrels, 1)['a1'] < 1: continue
    for alpha in chars:
        beta = tuple((x * inv(y)) % p for x, y in zip(alpha, lam))
        for V in ext(alpha, beta):
            IV = IM(V, 2)
            if not IV: continue
            U = induce(V); lhs = IM(pull(U), 4); a = Iw(U, 4); b = Iw(twist(U, w), 4)
            n += 1; ok += (lhs == a + b); res[(IV, lhs, a, b)] += 1
print(f"firing V on s961 (alpha-sub, p={p}): {n}; register lemma I(M;p*U) = I_w(U) + I_w(Uw) holds on {ok}/{n}")
print("distribution of (I(V), I(M;p*Ind V), I_w(N;Ind V), I_w(N;Ind V (x) w)):", dict(res))
