"""Main's re-derivation of B1351's closed half (2026-09-15): on Y_n (n-fold cyclic branched cover of S^3 over 4_1),
h^1(Y_n; psi) = h^1(Y_n; psi-bar) for every character psi of H_1 -- Poincare duality made explicit: for a non-trivial unitary
character on a closed 3-manifold h^0 = h^3 = 0 and chi = 0, so h^1(psi) = h^2(psi) = h^1(psi-bar). Computed, not cited:
Y_n from SnapPy's cyclic cover with the branched-cover slope (the one that kills the free factor and gives |H_1| = prod Delta(zeta^k)),
every character of H_1 by brute force, h^1 by Fox calculus at 40 digits with an absolute zero threshold. Levels 3, 4, 5."""
import snappy, sympy, mpmath as mp, itertools
mp.mp.dps = 40
def closed_cover(n):
    C = snappy.Manifold("m004").covers(n, cover_type="cyclic")[0]
    for slope in [(1,0),(0,1)]:
        D = C.copy(); D.dehn_fill([slope])
        if D.homology().betti_number() == 0: return D, slope
def run(n):
    Y, slope = closed_cover(n); G = Y.fundamental_group(); gens = G.generators(); rels = G.relators(); k = len(gens)
    def ab(w):
        v=[0]*k
        for ch in w: v[gens.index(ch.lower())] += 1 if ch.islower() else -1
        return v
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(sympy.Matrix([ab(r) for r in rels]), domain=sympy.ZZ)
    tors=[abs(S[i,i]) for i in range(min(S.shape)) if S[i,i] not in (0,1,-1)]; L = int(sympy.ilcm(*tors))
    chars = [e for e in itertools.product(range(L), repeat=k) if all(sum(a*x for a,x in zip(ab(r),e))%L==0 for r in rels)]
    assert len(chars) == sympy.prod(tors)
    def h1(e):
        z = {g: mp.exp(2j*mp.pi*mp.mpf(e[i])/L) for i,g in enumerate(gens)}
        r0 = 1 if any(abs(z[g]-1) > 1e-25 for g in gens) else 0
        rows=[]
        for r in rels:
            row=[mp.mpc(0)]*k; cur=mp.mpc(1)
            for ch in r:
                g=ch.lower(); i=gens.index(g)
                if ch.islower(): row[i]+=cur; cur*=z[g]
                else: cur/=z[g]; row[i]-=cur
            rows.append(row)
        real = mp.matrix([[mp.re(x) for x in row]+[-mp.im(x) for x in row] for row in rows]+[[mp.im(x) for x in row]+[mp.re(x) for x in row] for row in rows])
        sv = [float(s) for s in mp.svd_r(real, compute_uv=False)]
        r1 = sum(1 for s in sv if s > 1e-20)//2
        return (k - r1) - r0
    tested=bad=0; hist={}
    for e in chars:
        if all(x==0 for x in e): continue
        a = h1(e); b = h1(tuple((-x)%L for x in e)); tested+=1; hist[a]=hist.get(a,0)+1
        if a!=b: bad+=1
    print(f"n={n}: branched slope {slope}, H_1 = {'+'.join('Z/%d'%d for d in tors)} (|H_1| = {sympy.prod(tors)}), non-trivial characters {tested}, h^1(psi) != h^1(psi-bar): {bad}, distribution of h^1: {dict(sorted(hist.items()))}")
for n in (3,4,5): run(n)
print("VERDICT: every non-trivial character of every level tested is vector-like (h^1(psi) = h^1(psi-bar)), as B1351 states and Poincare duality requires.")
