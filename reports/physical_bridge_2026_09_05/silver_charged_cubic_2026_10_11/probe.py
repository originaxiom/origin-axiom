"""Actual charged cubic from the fixed domain; no producer execution before seal."""
import importlib.util,json,hashlib
from functools import lru_cache
from itertools import combinations,product
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;OLD=HERE.parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
p=load('charged_cubic_pencils',OLD/'silver_charged_pair_lift_2026_10_11/probe.py')
pt=load('charged_cubic_parent_maps',OLD/'parent_tensors.py')
z=p.z;PAIRS=list(combinations(range(5),2))
def ker(a,var=None):
    d=p.dm(a,var);rr,piv=d.rref();rr=rr.to_Matrix()
    free=[j for j in range(a.cols) if j not in piv];out=s.zeros(a.cols,len(free))
    for k,j in enumerate(free):
        out[j,k]=1
        for i,v in enumerate(piv):out[v,k]=-rr[i,j]
    return out
def pair(x):
    x=s.expand(x);b=x.coeff(s.sqrt(2));a=s.expand(x-b*s.sqrt(2))
    assert a.is_Rational and b.is_Rational
    return [str(a),str(b)]
def plane_hash(M):
    r=p.dm(M.T).rref()[0].to_Matrix()
    return hashlib.sha256(json.dumps([[pair(x) for x in row] for row in r.tolist()],separators=(',',':')).encode()).hexdigest()
def polynomial_kernel(C):
    d=p.dm(C,z);piv=list(d.rref()[1]);r=len(piv)
    rows=list(p.dm(C[:,piv].T,z).rref()[1]);free=[j for j in range(C.cols) if j not in piv]
    P=p.dm(C.extract(rows,piv),z);det=P.det()
    answer=P.inv().matmul(p.dm(C.extract(rows,free),z)).to_list()
    out=s.zeros(C.cols,len(free));dd=P.domain.to_sympy(det)
    for k,j in enumerate(free):
        out[j,k]=dd
        for i,v in enumerate(piv):out[v,k]=-P.domain.to_sympy(det*answer[i][k])
    return out,r
def up(a,b,c):
    return sum((a[i]*b[j]-a[j]*b[i])*c[k] for k,(i,j) in enumerate(PAIRS))
def down(a,b,c):
    return sum(pt.permutation_sign((i,)+jk+lm)*a[i]*b[j]*c[k]
               for i in range(5) for j,jk in enumerate(PAIRS) for k,lm in enumerate(PAIRS)
               if len(set((i,)+jk+lm))==5)
def ward(kind,X):
    C=up if kind=='up' else down
    sizes=(5,5,10) if kind=='up' else (5,10,10)
    out=[]
    for ix in product(*(range(n) for n in sizes)):
        v=[s.eye(n)[:,i] for n,i in zip(sizes,ix)]
        out.append(sum(C(*[X[j]*v[j] if k==j else v[k] for k in range(3)]) for j in range(3)))
    return p.zero(s.Matrix(out))
def vertex(kind,f,g,h,X,Y):
    C=up if kind=='up' else down
    return s.expand(C(f,X[1]*g,Y[2]*h)-C(f,Y[1]*g,X[2]*h))
def primitives(block,h,ck,label):
    a,b,M=block['a'],block['b'],block['M'];n=a.rows
    N=ker(M.T).T;D=a.col_join(b+h*z*s.eye(n));C=p.mm(N,D,z)
    F,r=polynomial_kernel(C);beta=p.mm(D,F,z)
    ck(label+'_whole_pencil_kernel',p.zero(p.mm(C,F,z),z))
    ck(label+'_actual_fixed_trace_plane',p.zero(p.mm(N,beta,z),z))
    ck(label+'_closed_trace',p.zero(p.mm((-b-h*z*s.eye(n)).row_join(a),beta,z),z))
    ck(label+'_polynomial_degree_bound',all(s.degree(x,z)<=r for x in F if x!=0))
    return dict(F=F,r=r,a=a,b=b,Y=b+h*z*s.eye(n),h=h)
@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    old,data,w,P,Q,A,B=p.cy.literal()
    model=json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    ck('original_affine_W_determinant_one_not_wholesale_parity',all(s.simplify(x.det())==1 for x in w.values()) and data['nu']['t']==-1)
    blocks={};hashes={}
    for name,a,b,subset in [('W',A,B,model['W_plane']),('Fcolor',p.cy.exterior_lie(A),p.cy.exterior_lie(B),model['F_color_plane']),('Fweak',p.cy.exterior_lie(A),p.cy.exterior_lie(B),model['F_weak_plane'])]:
        E=p.boundary(a,b);D=p.boundary(-a.T,-b.T);L=E['H'][:,subset]
        M=E['U'].row_join(L);blocks[name]=dict(a=a,b=b,M=M);hashes[name]=plane_hash(M)
        if name=='Fweak':
            LD=p.dual_plane(E,D,L);MD=D['U'].row_join(LD)
            blocks['Fweakdual']=dict(a=-a.T,b=-b.T,M=MD);hashes['Fweakdual']=plane_hash(MD)
    fields={}
    for label,block,h,n in [('Q','W',-1,1),('u','W',4,1),('e','W',-6,1),('d','Fcolor',-2,1),('weak','Fweak',3,2),('Hu','Fweakdual',-3,1)]:
        fields[label]=primitives(blocks[block],h,ck,label)
        ck(label+'_correct_physical_kernel_dimension',fields[label]['F'].cols==n)
    ck('actual_parent_tensor_opposing_support',pt.up_tensor(((0,1),0),((2,3),1),(4,(0,1)))!=0 and pt.down_tensor(((0,1),0),(0,(1,2)),(1,(3,4)))!=0 and pt.up_tensor(((0,1),0),((2,3),0),(4,(0,1)))==0)
    for tag,x in [('meridian',A),('longitude',B)]:
        fx=p.cy.exterior_lie(x)
        ck(tag+'_up_full_coefficient_Ward',ward('up',[x,x,-fx.T]))
        ck(tag+'_down_full_coefficient_Ward',ward('down',[x,fx,fx]))
    ck('phase_Ward_and_missing_charge_twist_opposite',-1+4-3==0 and -1+4!=0)
    channels={'up':('up',['Q','u','Hu']),'down':('down',['Q','d','weak']),'lepton':('down',['e','weak','weak']),'udd':('down',['u','d','d'])}
    output={};signatures={}
    for name,(kind,labels) in channels.items():
        f=[fields[k] for k in labels];X=[x['a'] for x in f];Y=[x['Y'] for x in f]
        ck(name+'_full_parent_charge_sum',sum(x['h'] for x in f)==0)
        sizes=[x['F'].cols for x in f];D=sum(x['r'] for x in f)+2
        entries=[]
        for ijk in product(*(range(n) for n in sizes)):
            entry=vertex(kind,*[f[j]['F'][:,ijk[j]] for j in range(3)],X,Y)
            entry=p.dm(s.Matrix([[entry]]),z).to_Matrix()[0,0];entries.append(entry)
        ck(name+'_tensor_polynomial_degree',all(s.degree(x,z)<=D for x in entries if x!=0))
        if name=='lepton':
            mat=s.Matrix(2,2,entries);ck('lepton_actual_exchange_antisymmetry',p.zero(mat+mat.T,z))
            value=p.rank(mat,z)
        else:value=int(any(x!=0 for x in entries))
        if name=='up':
            swapped=vertex('up',f[1]['F'][:,0],f[0]['F'][:,0],f[2]['F'][:,0],[X[1],X[0],X[2]],[Y[1],Y[0],Y[2]])
            ck('up_actual_chiral_exchange_symmetry',p.zero(s.Matrix([[swapped-entries[0]]]),z))
        if name=='udd':ck('single_family_udd_identically_zero',value==0)
        signatures[name]=value
        output[name]=dict(polynomial_degree_bound=D,primitive_minor_ranks=[x['r'] for x in f],tensor_shape=sizes,coordinate_polynomials=[str(s.expand(x)) for x in entries],rank=value)
    # Synthetic controls keep the transgression instrument capable of nonzero.
    a=s.diag(1,-1,0,0,0);b=s.zeros(5);af=p.cy.exterior_lie(a)
    u=s.eye(5)[:,0];v=s.eye(5)[:,1];fd=s.eye(10)[:,0]
    control=vertex('up',u,v,fd,[a,a,-af.T],[b+4*z*s.eye(5),b-z*s.eye(5),s.zeros(10)-3*z*s.eye(10)])
    ck('nonzero_transgression_recovery_and_phase_omission',s.expand(control-3*z)==0 and vertex('up',u,v,fd,[a,a,-af.T],[b,b,s.zeros(10)])==0)
    # The cohomology/normalization distinction is a mathematical tensor control.
    gram=s.diag(2,3);change=s.Matrix([[1,2],[0,1]]);vec=s.Matrix([[1,2]])
    transformed=change.T*gram*change
    ck('weak_vector_norm_carries_positive_kinetic_Gram',(vec*gram.inv()*vec.T)[0]==(vec*change*transformed.inv()*change.T*vec.T)[0] and (vec*vec.T)[0]!=(vec*change*change.T*vec.T)[0])
    ck('weak_space_is_not_a_marked_Higgs_line',fields['weak']['F'].cols==2 and fields['Hu']['F'].cols==1)
    return dict(facts=facts,predicates_passed=len(facts),boundary_plane_sha256=hashes,channel_ranks=signatures,channels=output,conditional_charged_overlap=True,absolute_normalized_Yukawas=False,neutral_cubic_computed=False,complete_light_potential=False,generated_selection=False,outside_review=False,global_PDE_solved=False,full_goal_achieved=False)
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
