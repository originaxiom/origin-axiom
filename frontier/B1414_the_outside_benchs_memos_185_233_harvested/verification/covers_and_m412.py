#!/usr/bin/env python3
"""Memo 231 cell 1 (cyclic covers of m004 n=2..30 all amphichiral; covers to degree 7: 28, chiral 18 in 9 mirror pairs)
and cell 5/6 facts about m412 and L12n2208, plus P_2T(m412) and its det multiset. Own code."""
import snappy, json, itertools, time
def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def cm(iso,i):
    c=iso.cusp_maps()[i]; return [[int(c[0][0]),int(c[0][1])],[int(c[1][0]),int(c[1][1])]]
def amphichiral(M):
    return any(det2(cm(iso,0))==-1 for iso in M.isomorphisms_to(M))
def det_multiset(M):
    vals=[]
    for iso in M.isomorphisms_to(M):
        for i in range(M.num_cusps()):
            if iso.cusp_images()[i]!=i: continue
            A=cm(iso,i)
            if det2(A)!=1: continue
            vals.append(abs(det2([[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]])))
    return sorted(vals)
res={}
M=snappy.Manifold('m004'); v0=float(M.volume())
t0=time.time(); cyc=[]
for n in range(2,31):
    C=M.covers(n,cover_type='cyclic'); assert len(C)==1
    c=C[0]; cyc.append((n, abs(float(c.volume())-n*v0)<1e-6, amphichiral(c), str(c.homology())))
res['cyclic_2_30']={'all_vol_ok':all(r[1] for r in cyc),'amphichiral':sum(r[2] for r in cyc),'chiral':sum(not r[2] for r in cyc),'H1_last':cyc[-1][3],'seconds':round(time.time()-t0)}
print(res['cyclic_2_30'])
# covers to degree 7
t0=time.time(); allc=[]
for d in range(2,8):
    for c in M.covers(d):
        allc.append({'deg':d,'type':c.cover_info()['type'],'amph':amphichiral(c),'vol':float(c.volume()),'H1':str(c.homology()),'M':c})
tab={}
for c in allc: tab[(c['type'],c['amph'])]=tab.get((c['type'],c['amph']),0)+1
print('covers to 7:', len(allc), {f'{k[0]}/{"amph" if k[1] else "chiral"}':v for k,v in tab.items()})
# mirror pairs among chiral covers: a chiral cover C and its mirror (reverse orientation) are isometric to a DIFFERENT cover
chir=[c for c in allc if not c['amph']]; pairs=0; unpaired=0; used=set()
for i,c in enumerate(chir):
    if i in used: continue
    mir=c['M'].copy(); mir.reverse_orientation(); found=None
    for j,c2 in enumerate(chir):
        if j==i or j in used or c2['deg']!=c['deg']: continue
        if mir.is_isometric_to(c2['M']): found=j; break
    if found is None: unpaired+=1
    else: pairs+=1; used|={i,found}
res['covers_to_7']={'n':len(allc),'table':{f'{k[0]}/{"amph" if k[1] else "chiral"}':v for k,v in tab.items()},'chiral':len(chir),'mirror_pairs':pairs,'unpaired':unpaired,'seconds':round(time.time()-t0)}
print(res['covers_to_7'])
# m412 and L12n2208
for name in ('m412','L12n2208'):
    X=snappy.Manifold(name); X.high_precision() if False else None
    shapes=[s.min_polynomial() if hasattr(s,'min_polynomial') else None for s in []]
    G=X.symmetry_group()
    polys=set()
    try:
        for f in snappy.ManifoldHP(name).tetrahedra_field_gens().find_field(200,20,optimize=True)[:1]: pass
    except Exception as e: pass
    import mpmath as mp
    mp.mp.dps=60
    HP=snappy.ManifoldHP(name)
    for z in HP.tetrahedra_shapes('rect'):
        z=mp.mpc(str(z.real()).replace(' ',''),str(z.imag()).replace(' ',''))
        # test z^2 - z + 1 = 0 or conjugate
        polys.add(bool(abs(z*z-z+1)<mp.mpf(10)**-40))
    isos=X.isomorphisms_to(X); signs=[det2(cm(i,0)) for i in isos]
    row={'cusps':X.num_cusps(),'vol':float(X.volume()),'vol/m004':float(X.volume())/v0,'H1':str(X.homology()),'sym_order':G.order(),'snappy_is_amphicheiral':bool(G.is_amphicheiral()),
         'self_isometries':len(isos),'orientation_reversing':signs.count(-1),'amphichiral_by_isometry':(-1 in signs),'all_shapes_x2-x+1':(polys=={True}),'det_multiset':det_multiset(X)}
    res[name]=row; print(name,row)
# P_2T on m412: count homs pi_1 -> SL(2,3) that are surjective, via the group table
els=[]
for a,b,c,d in itertools.product(range(3),repeat=4):
    if (a*d-b*c)%3==1: els.append((a,b,c,d))
idx={e:i for i,e in enumerate(els)}
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y; return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
def inv(x):
    for y in els:
        if mul(x,y)==(1,0,0,1): return y
def ev(word,img):
    r=(1,0,0,1)
    for ch in word:
        g=img[ch.lower()]; r=mul(r, g if ch.islower() else inv(g))
    return r
def gen(S):
    seen={(1,0,0,1)}; fr=[(1,0,0,1)]
    while fr:
        nx=[]
        for s in fr:
            for g in S:
                t=mul(s,g)
                if t not in seen: seen.add(t); nx.append(t)
        fr=nx
    return len(seen)
for name in ('m004','m412'):
    G=snappy.Manifold(name).fundamental_group(); gens=G.generators(); rels=G.relators()
    cnt=0
    for imgs in itertools.product(els,repeat=len(gens)):
        img=dict(zip(gens,imgs))
        if all(ev(r,img)==(1,0,0,1) for r in rels) and gen(imgs)==24: cnt+=1
    res[f'2T_raw_{name}']=cnt; print(name,'2T raw surjections',cnt,'gens',len(gens))
json.dump(res,open(__import__('pathlib').Path(__file__).with_suffix('.json'),'w'),indent=1,default=str)
