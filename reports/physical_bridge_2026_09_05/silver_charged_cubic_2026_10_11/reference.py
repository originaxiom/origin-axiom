"""Separate Fraction/exterior-word transgression with polynomial zero certificates."""
import importlib.util,json,hashlib
from itertools import combinations,product
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).resolve().parent;OLD=HERE.parent
spec=importlib.util.spec_from_file_location('charged_cubic_fraction_pencils',OLD/'silver_charged_pair_lift_2026_10_11/reference.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
c=r.c;K=c.K;PAIRS=list(combinations(range(5),2))
def plus(a,b):return [x+y for x,y in zip(a,b)]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def sub(a,rows,cols):return [[a[i][j] for j in cols] for i in rows]
def determinant(a):
    a=[[K(x) if not isinstance(x,K) else x for x in row] for row in a];out=K(1)
    for j in range(len(a)):
        k=next((k for k in range(j,len(a)) if a[k][j]),None)
        if k is None:return K(0)
        if k!=j:a[j],a[k]=a[k],a[j];out=-out
        v=a[j][j];out*=v
        for i in range(j+1,len(a)):
            q=a[i][j]/v
            if q:a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return out
def poly_matrix(C0,C1,t):return c.add(C0,c.scale(C1,t))
def plane_hash(M):
    rows=c.reduced(c.tr(M))[0]
    pairs=[[[str((x if isinstance(x,K) else K(x)).a),str((x if isinstance(x,K) else K(x)).b)] for x in row] for row in rows]
    return hashlib.sha256(json.dumps(pairs,separators=(',',':')).encode()).hexdigest()
def wedge(a,b):
    out={}
    for ix,x in a.items():
        for iy,y in b.items():
            joined=ix+iy
            if len(set(joined))<len(joined):continue
            sign=(-1)**sum(joined[i]>joined[j] for i in range(len(joined)) for j in range(i+1,len(joined)))
            key=tuple(sorted(joined));out[key]=out.get(key,0)+sign*x*y
    return out
def ext(v,degree):
    ix=[(i,) for i in range(5)] if degree==1 else PAIRS
    return {k:x for k,x in zip(ix,v) if x}
def tensor(kind,a,b,d):
    if kind=='up':
        w=wedge(ext(a,1),ext(b,1));return sum(w.get(k,0)*x for k,x in zip(PAIRS,d))
    return wedge(wedge(ext(a,1),ext(b,2)),ext(d,2)).get((0,1,2,3,4),0)
def vertex(kind,f,g,h,profiles,t):
    X=[p['a'] for p in profiles];Y=[c.add(p['b'],c.scale(c.I(len(p['a'])),p['h']*t)) for p in profiles]
    return tensor(kind,f,mv(X[1],g),mv(Y[2],h))-tensor(kind,f,mv(Y[1],g),mv(X[2],h))
def build(block,h):
    a,b,M=block['a'],block['b'],block['M'];n=len(a)
    N=c.tr(c.null(c.tr(M)));C0=c.mm(N,c.stack(a,b));C1=c.mm(N,c.stack(c.Z(n),c.scale(c.I(n),h)))
    points=[(t,c.reduced(poly_matrix(C0,C1,t))[1]) for t in range(1,n+2)]
    t,piv=max(points,key=lambda x:len(x[1]));rank=len(piv);V=poly_matrix(C0,C1,t)
    rows=c.reduced(c.tr(sub(V,list(range(len(V))),piv)))[1]
    free=[j for j in range(n) if j not in piv]
    return dict(a=a,b=b,M=M,N=N,C0=C0,C1=C1,h=h,r=rank,rows=rows,piv=piv,free=free)
def evaluate(p,t):
    C=poly_matrix(p['C0'],p['C1'],t);P=sub(C,p['rows'],p['piv']);d=determinant(P)
    if not d:return None
    tail=sub(C,p['rows'],p['free']);x=c.mm(c.inverse(P),tail);F=c.Z(len(p['a']),len(p['free']))
    for k,j in enumerate(p['free']):
        F[j][k]=d
        for i,v in enumerate(p['piv']):F[v][k]=-d*x[i][k]
    assert c.zero(c.mm(C,F)), 'whole pencil equations'
    beta=c.mm(c.stack(p['a'],c.add(p['b'],c.scale(c.I(len(p['a'])),p['h']*t))),F)
    assert c.zero(c.mm(p['N'],beta)), 'fixed plane'
    return F
@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    data,w,P,Q,A,B=c.literal();model=json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    blocks={};hashes={}
    for name,a,b,subset in [('W',A,B,model['W_plane']),('Fcolor',c.wedge_derivative(A),c.wedge_derivative(B),model['F_color_plane']),('Fweak',c.wedge_derivative(A),c.wedge_derivative(B),model['F_weak_plane'])]:
        E=r.boundary(a,b);D=r.boundary(c.scale(c.tr(a),-1),c.scale(c.tr(b),-1));L=r.subset(E['H'],subset);M=c.cat(E['U'],L)
        blocks[name]=dict(a=a,b=b,M=M);hashes[name]=plane_hash(M)
        if name=='Fweak':
            LD,_=r.paired_plane(E,D,L);MD=c.cat(D['U'],LD)
            blocks['Fweakdual']=dict(a=c.scale(c.tr(a),-1),b=c.scale(c.tr(b),-1),M=MD);hashes['Fweakdual']=plane_hash(MD)
    fields={}
    for label,block,h,n in [('Q','W',-1,1),('u','W',4,1),('e','W',-6,1),('d','Fcolor',-2,1),('weak','Fweak',3,2),('Hu','Fweakdual',-3,1)]:
        fields[label]=build(blocks[block],h)
        ck(label+'_degree_one_rank_certificate_and_actual_kernel',len(fields[label]['free'])==n and fields[label]['r']+n==len(fields[label]['a']))
    channels={'up':('up',['Q','u','Hu']),'down':('down',['Q','d','weak']),'lepton':('down',['e','weak','weak']),'udd':('down',['u','d','d'])};ranks={};certs={}
    for name,(kind,labels) in channels.items():
        ps=[fields[k] for k in labels];D=sum(x['r'] for x in ps)+2;needed=D+1;points=[];any_nonzero=False
        ck(name+'_physical_charge_sum',sum(x['h'] for x in ps)==0)
        for t in range(1,D+sum(x['r'] for x in ps)+3):
            fs=[evaluate(x,t) for x in ps]
            if any(x is None for x in fs):continue
            entries=[]
            for ijk in product(*(range(len(f[0])) for f in fs)):
                vs=[[row[ijk[j]] for row in fs[j]] for j in range(3)]
                entries.append(vertex(kind,*vs,ps,t))
            if name=='lepton':ck('lepton_exchange_at_'+str(t),entries[0]==0 and entries[3]==0 and entries[1]==-entries[2])
            any_nonzero|=any(bool(x) for x in entries);points.append(t)
            if len(points)==needed:break
        ck(name+'_enough_distinct_nonsingular_degree_points',len(points)==needed and len(set(points))==needed)
        ranks[name]=(2 if name=='lepton' else 1) if any_nonzero else 0
        certs[name]=dict(degree_bound=D,distinct_points=points,zero_certified=not any_nonzero,rank=ranks[name],fixed_minor_ranks=[x['r'] for x in ps])
    ck('repeated_single_family_udd_zero',ranks['udd']==0)
    a=[[int(i==j)*(1 if i==0 else -1 if i==1 else 0) for j in range(5)] for i in range(5)]
    af=c.wedge_derivative(a);ps=[dict(a=a,b=c.Z(5),h=4),dict(a=a,b=c.Z(5),h=-1),dict(a=c.scale(c.tr(af),-1),b=c.Z(10),h=-3)]
    u=[1,0,0,0,0];v=[0,1,0,0,0];d=[1]+[0]*9
    ck('nonzero_exterior_dictionary_transgression_recovery',vertex('up',u,v,d,ps,2)==6)
    ck('phase_omission_opposing_control',vertex('up',u,v,d,ps,0)==0)
    # Degree certificate is two-sided: D points can hide a degree-D polynomial.
    D=7
    def bad(t):
        out=1
        for j in range(1,D+1):out*=t-j
        return out
    ck('zero_certificate_needs_degree_plus_one',all(bad(t)==0 for t in range(1,D+1)) and bad(D+1)!=0)
    ck('no_Higgs_line_selected_from_weak_dimension',len(fields['weak']['free'])==2 and len(fields['Hu']['free'])==1)
    return dict(facts=facts,predicates_passed=len(facts),boundary_plane_sha256=hashes,channel_ranks=ranks,zero_certificates=certs,new_native_imported=False,conditional_charged_overlap=True,absolute_normalized_Yukawas=False,neutral_cubic_computed=False,complete_light_potential=False,generated_selection=False,outside_review=False,global_PDE_solved=False,full_goal_achieved=False)
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
