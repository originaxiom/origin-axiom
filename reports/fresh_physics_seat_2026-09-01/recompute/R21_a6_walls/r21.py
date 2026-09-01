import snappy, json
from fractions import Fraction
out={}
# (a) base rate: first 200 one-cusped orientable census manifolds, orientation-aware test
def amph(M):
    try: return bool(M.symmetry_group().is_amphicheiral())
    except Exception as e: return None
slices={}
mans=[M for M in snappy.OrientableCuspedCensus(cusps=1)][:200]
res=[amph(M) for M in mans]
slices['first200_1cusped']=dict(num=sum(1 for r in res if r),den=len(res),none=sum(1 for r in res if r is None),
    names=[M.name() for M,r in zip(mans,res) if r])
# alt slice: first 200 of full orientable census regardless of cusps
mans2=[M for M in snappy.OrientableCuspedCensus()][:200]
res2=[amph(M) for M in mans2]
slices['first200_any']=dict(num=sum(1 for r in res2 if r),den=200,names=[M.name() for M,r in zip(mans2,res2) if r])
# planted positive: m004 and m003 known amphichiral? check they are in the count
slices['planted']={n:amph(snappy.Manifold(n)) for n in ['m003','m004']}
out['a']=slices
# (b) cell2: Gieseking m000 non-orientable, orientation cover == m004, vol ratio 2
G=snappy.Manifold('m000'); C=G.orientation_cover(); m4=snappy.Manifold('m004')
out['b_cell2']=dict(m000_orientable=G.is_orientable(), cover_is_m004=bool(C.is_isometric_to(m4)),
    vol_ratio=float(C.volume()/G.volume()))
# (b') CS mod 1/2 on covers of m004 deg 2..5
def csmod(x,mod):
    x=float(x)%mod
    return round(min(x,mod-x),6)
cs={}
for d in range(2,6):
    covs=m4.covers(d)
    cs[d]=[dict(name=c.name(),cover_type=c.cover_info()['type'] if hasattr(c,'cover_info') else None,
                cs=round(float(c.chern_simons()),8), dist_to_halfint=csmod(c.chern_simons(),0.5),
                amph=amph(c)) for c in covs]
out['b_cs_covers']=cs
json.dump(out,open('r21_results.json','w'),indent=1)
print(json.dumps({k:v for k,v in out.items() if k!='b_cs_covers'},indent=1))
for d in cs: print(d,[(c['cs'],c['dist_to_halfint'],c['amph']) for c in cs[d]])
