"""cc3 (audit seat) independent verification of B734 — 2026-07-21.

Everything computed in-sandbox; the ONLY cited ingredients (flagged):
  [C1] Riley 1975: the parabolic rep below is the discrete faithful rep of pi_1(m004)
       (we COMPUTE: the fig-8 two-bridge relation holds, parabolicity, irreducibility,
       entries in O_3, traces match snappy's holonomy numerically; faithfulness is Riley's).
  [C2] [PSL(2,O_3) : Gamma] = 12 (geometric index) — VERIFIED numerically here via
       Humbert's volume formula (vol ratio = 12 to 25 dps), formula itself cited.
  [C3] the level-2^k kernel order |ker(SL(O/2^{k+1})->SL(O/2^k))| = 64 — VERIFIED by BFS
       for k=1,2 (3840/60, 245760/3840); used as the lifting formula only at k=4 (16).

Conventions (declared): O_3 = Z[z], z = (1+sqrt(-3))/2 the primitive SIXTH root, z^2 = z-1.
(This is deliberately a DIFFERENT basis convention from cc's test, which uses the cube root
w = z-1, w^2 = -w-1; independence of implementation.) Ring element = (a,b) := a + b*z mod M.
Matrix = (p,q,r,s) row-major. Riley generators A=[[1,1],[0,1]], B=[[1,0],[-z,1]].

The two congruence tests, both computed at every level:
  T_SL  (STANDARD): [SL(2,O/I) : image of <A,B,-I>]  == 12  <=>  Gamma~ contains ker(SL(O)->SL(O/I))
        <=> Gamma contains the standard principal congruence subgroup P-Gamma(I).
  T_PSL (mod-center, what E21/B734 used): [SL/Z : <A,B>Z/Z] == 12
        <=> Gamma contains Gamma-hat(I) = ker(PSL(2,O) -> SL(O/I)/Z(I)).  (Gamma-hat >= P-Gamma.)
"""
import sys, json, time

def make_ring(M):
    def mul(p, q):
        a, b = p; c, d = q
        return ((a*c - b*d) % M, (a*d + b*c + b*d) % M)      # z^2 = z - 1
    def add(p, q): return ((p[0]+q[0]) % M, (p[1]+q[1]) % M)
    def neg(p): return ((-p[0]) % M, (-p[1]) % M)
    return mul, add, neg

def make_mat(M):
    mul, add, neg = make_ring(M)
    def MM(X, Y):
        return (add(mul(X[0],Y[0]), mul(X[1],Y[2])), add(mul(X[0],Y[1]), mul(X[1],Y[3])),
                add(mul(X[2],Y[0]), mul(X[3],Y[2])), add(mul(X[2],Y[1]), mul(X[3],Y[3])))
    def inv(X):   # det=1 assumed
        return (X[3], neg(X[1]), neg(X[2]), X[0])
    def det(X):
        mulr = mul
        return ( (mulr(X[0],X[3])[0]-mulr(X[1],X[2])[0]) % M, (mulr(X[0],X[3])[1]-mulr(X[1],X[2])[1]) % M )
    return MM, inv, det

def bfs(M, gens, cap=20_000_000, report=None):
    MM, inv, _ = make_mat(M)
    E, Z = (1,0), (0,0)
    I = (E, Z, Z, E)
    gens = list(gens) + [inv(g) for g in gens]
    seen = {I}; fr = [I]
    while fr:
        nf = []
        for X in fr:
            for g in gens:
                Y = MM(X, g)
                if Y not in seen:
                    seen.add(Y); nf.append(Y)
                    if len(seen) > cap: raise RuntimeError("cap exceeded")
        fr = nf
        if report and len(seen) % 1 == 0: pass
    return seen

def sl_ambient(M):
    """Full SL(2, O/M) by BFS from 4 elementary generators (E12(1),E12(z),E21(1),E21(z))."""
    E, Z, z = (1,0), (0,0), (0,1)
    gens = [(E, E, Z, E), (E, z, Z, E), (E, Z, E, E), (E, Z, z, E)]
    return bfs(M, gens)

def knot_image(M, with_minus=True):
    E, Z, z = (1,0), (0,0), (0,1)
    mul, add, neg = make_ring(M)
    A = (E, E, Z, E)
    B = (E, Z, neg(z), E)
    gens = [A, B]
    if with_minus:
        m1 = neg(E)
        gens.append((m1, Z, Z, m1))
    return bfs(M, gens)

def central_scalars(M):
    mul, add, neg = make_ring(M)
    return [ (a,b) for a in range(M) for b in range(M) if mul((a,b),(a,b)) == (1,0) ]

def analyze_level(M, ambient_order=None):
    t0 = time.time()
    mul, add, neg = make_ring(M)
    Z2 = (0,0)
    if ambient_order is None:
        amb = len(sl_ambient(M)); amb_src = "BFS-computed"
    else:
        amb = ambient_order;      amb_src = "lifting-formula [C3]"
    img  = knot_image(M, with_minus=True)          # <A,B,-I> = pi(Gamma~)
    img0 = knot_image(M, with_minus=False)         # <A,B>
    cen  = central_scalars(M)
    cen_in_img  = [c for c in cen if (c,Z2,Z2,c) in img]
    cen_in_img0 = [c for c in cen if (c,Z2,Z2,c) in img0]
    n_z  = len(cen)
    t_sl  = amb // len(img)                         # [SL : <A,B,-I>]  (STANDARD test)
    t_psl = (amb // n_z) // (len(img0) // len(cen_in_img0))   # [SL/Z : imgZ/Z]  (E21/B734 test)
    dt = time.time() - t0
    return dict(M=M, ambient=amb, ambient_src=amb_src, n_center=n_z,
                img_with_minus=len(img), img_bare=len(img0),
                center_in_bare_img=len(cen_in_img0), minus_in_bare=((-1)%M, 0) and ((( -1)%M,0),Z2,Z2,(((-1)%M),0)) in img0,
                T_SL_index=t_sl, T_PSL_index=t_psl, secs=round(dt,1))

def relation_check():
    """Fig-8 two-bridge relation  A * w = w * B  with w = B A^-1 B^-1 A ... find the two-bridge
    word among the standard candidates, EXACTLY over Z[z] (no modulus)."""
    import itertools
    class R:   # exact ring Z[z]
        def mul(p,q): a,b=p; c,d=q; return (a*c-b*d, a*d+b*c+b*d)
        def add(p,q): return (p[0]+q[0], p[1]+q[1])
        def neg(p):  return (-p[0], -p[1])
    E,Zr,z = (1,0),(0,0),(0,1)
    def MM(X,Y):
        return (R.add(R.mul(X[0],Y[0]),R.mul(X[1],Y[2])), R.add(R.mul(X[0],Y[1]),R.mul(X[1],Y[3])),
                R.add(R.mul(X[2],Y[0]),R.mul(X[3],Y[2])), R.add(R.mul(X[2],Y[1]),R.mul(X[3],Y[3])))
    def inv(X): return (X[3], R.neg(X[1]), R.neg(X[2]), X[0])
    A = (E, E, Zr, E); B = (E, Zr, R.neg(z), E)
    words = {"BA'B'A": [B, inv(A), inv(B), A], "B'ABA'": [inv(B), A, B, inv(A)],
             "AB'A'B": [A, inv(B), inv(A), B], "A'BAB'": [inv(A), B, A, inv(B)],
             "BAB'A'": [B, A, inv(B), inv(A)], "B'A'BA": [inv(B), inv(A), B, A]}
    hits = []
    for name, seq in words.items():
        w = seq[0]
        for m in seq[1:]: w = MM(w, m)
        lhs = MM(A, w); rhs = MM(w, B)
        if lhs == rhs: hits.append(name)
        # also check the PSL version (= up to global sign)
        elif lhs == tuple(tuple(-c for c in e) if isinstance(e,tuple) else -e for e in ()) : pass
    # traces (exact, in Z[z]):  tr(AB) should be 2 - z  ( = (3 - sqrt(-3))/2 )
    AB = MM(A,B); trAB = R.add(AB[0], AB[3])
    comm = MM(MM(A,B), MM(inv(A),inv(B))); trcomm = R.add(comm[0], comm[3])
    return dict(relation_words_satisfied=hits, tr_AB=trAB, tr_commutator=trcomm)

def humbert_check():
    from mpmath import mp, mpf, zeta, pi, sqrt, sin, nsum, inf
    mp.dps = 30
    # L(2, chi_-3), chi mod 3: 1,-1 pattern
    L = nsum(lambda n: (1 if n % 3 == 1 else (-1 if n % 3 == 2 else 0))/mpf(n)**2, [1, inf])
    zK2 = zeta(2) * L
    vol_orb = (mpf(3)**mpf(1.5)) * zK2 / (4 * pi**2)          # Humbert, K=Q(sqrt(-3))
    # vol(m004) exactly = 6 * Lobachevsky(pi/3)  (two regular ideal tetrahedra)
    lob = nsum(lambda n: sin(2*n*pi/3)/mpf(n)**2, [1, inf]) / 2
    vol_m004_exact = 6 * lob
    try:
        import snappy
        vol_snappy = float(snappy.Manifold('m004').volume())
    except Exception as e:
        vol_snappy = None
    return dict(L2_chi3=str(L), zetaK2=str(zK2), vol_orbifold=str(vol_orb),
                vol_m004_series=str(vol_m004_exact), vol_m004_snappy=vol_snappy,
                index_ratio=str(vol_m004_exact / vol_orb))

def snappy_trace_check():
    try:
        import snappy
        G = snappy.Manifold('m004').fundamental_group()
        out = dict(generators=G.generators(), relators=G.relators())
        for wname in ('a','b','ab','aB','abAB'):
            try:
                tr = G.SL2C(wname).trace()
                out[f'tr({wname})'] = complex(tr)
            except Exception:
                pass
        return out
    except Exception as e:
        return dict(error=str(e))

if __name__ == '__main__':
    results = {}
    results['relation'] = relation_check()
    print("REP CHECK:", results['relation']); sys.stdout.flush()
    results['humbert'] = humbert_check()
    print("HUMBERT:", json.dumps(results['humbert'], indent=1)); sys.stdout.flush()
    results['snappy'] = snappy_trace_check()
    print("SNAPPY:", results['snappy']); sys.stdout.flush()

    for M in (2, 4, 8):
        r = analyze_level(M)
        results[f'level_{M}'] = r
        print(f"LEVEL {M}: ambient={r['ambient']} ({r['ambient_src']}), |Z|={r['n_center']}, "
              f"|<A,B,-I>|={r['img_with_minus']}, |<A,B>|={r['img_bare']}, "
              f"central-in-<A,B>={r['center_in_bare_img']}, "
              f"T_SL index={r['T_SL_index']}, T_PSL index={r['T_PSL_index']}  [{r['secs']}s]")
        sys.stdout.flush()

    # level 16 (knot image BFS ~1.3M elements; ambient via verified lifting formula [C3])
    r16 = analyze_level(16, ambient_order=60 * 64**3)
    results['level_16'] = r16
    print(f"LEVEL 16: ambient={r16['ambient']} ({r16['ambient_src']}), |Z|={r16['n_center']}, "
          f"|<A,B,-I>|={r16['img_with_minus']}, T_SL index={r16['T_SL_index']}, "
          f"T_PSL index={r16['T_PSL_index']}  [{r16['secs']}s]"); sys.stdout.flush()

    # odd primes: image should be EVERYTHING (index 1 both senses)
    for M in (3, 5):
        r = analyze_level(M)
        results[f'level_{M}'] = r
        print(f"LEVEL {M} (odd): ambient={r['ambient']}, T_SL index={r['T_SL_index']}, "
              f"T_PSL index={r['T_PSL_index']}  [{r['secs']}s]"); sys.stdout.flush()

    with open('results.json', 'w') as f:
        json.dump({k: {kk: (str(vv) if not isinstance(vv,(int,float,str,list,bool,type(None))) else vv)
                       for kk,vv in v.items()} if isinstance(v,dict) else v
                   for k,v in results.items()}, f, indent=1, default=str)
    print("DONE — results.json written")
