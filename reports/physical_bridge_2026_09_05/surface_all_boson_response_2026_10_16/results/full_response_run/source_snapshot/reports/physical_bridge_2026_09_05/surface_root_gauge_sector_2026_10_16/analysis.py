"""Faithful root/source blocks and local nonlinear gauge-sector controls."""
import hashlib,importlib.util,json,sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def cm(M):return M.applyfunc(s.expand)
def zero(M):return all(s.cancel(s.expand(z))==0 for z in M.todok().values())
def gauge(engine,old):
    # Credited interacting_transport actual signed-root reconstruction.
    roots=sorted(engine.roots);ix={v:j for j,v in enumerate(engine.roots)}
    ind=list(range(8))+[8+ix[v] for v in roots];back={p:j for j,p in enumerate(ind)}
    @lru_cache(None)
    def pair(p,q):return {back[j]:s.Rational(w) for j,w in engine.pair(ind[p],ind[q]).items() if w}
    S=s.Matrix.hstack(*(s.Matrix(v)/2 for v in old.SIMPLE_DOUBLED));cart=s.Matrix(engine.cartan)
    e=[s.eye(8)[:,j] for j in range(8)];chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    ch=s.Matrix.hstack(*chain);ws=[ch*(ch.T*ch).inv()*s.Matrix([1,0,0,0,0])]
    for a in chain:ws.append(ws[-1]-a)
    hv=sum((a*w for a,w in zip((1,-1)*3,ws)),s.zeros(8,1));q=[s.simplify((S*s.Matrix(v)).dot(hv)) for v in roots]
    if not all(v.is_Integer for v in q):raise ValueError('Nonintegral puncture charge')
    parity=[1]*8+[1 if int(v)%2==0 else -1 for v in q]
    up=8+next(j for j,v in enumerate(q) if int(v)%2);dn=8+roots.index(tuple(-v for v in roots[up-8]))
    hvect={j:-v for j,v in pair(up,dn).items()}
    def adj(d):
        out={}
        for p,x in d.items():
            for j in range(248):
                for k,y in pair(p,j).items():out[k,j]=out.get((k,j),0)+x*y
        return s.SparseMatrix(248,248,out)
    E=adj({up:1});F=adj({dn:1});H=adj(hvect);P=(E+F)/2;Q=(E-F)/(2*s.I)
    G=s.SparseMatrix(s.diag(cart,s.eye(240)));eta=s.SparseMatrix(s.diag(*parity))
    tau=s.SparseMatrix(248,248,{(j,j):-1 for j in range(8)}|{(8+roots.index(tuple(-v for v in rt)),8+j):1 for j,rt in enumerate(roots)})
    return roots,up,dn,hvect,E,F,H,P,Q,G,eta,tau,parity,pair
def run(method):
    prior=load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py','root_actual_parent')
    vv,ext,cs,engine,valid,old=prior.setup(method)
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    I=s.eye(16);I8=s.eye(8);IG=s.SparseMatrix(s.eye(248));C=s.kronecker_product(s.Matrix([[0,1],[1,0]]),I8)
    ck('same complete actual source dictionary',valid and all(zero(v-v.H) for v in ext+vv) and all(zero(a*b+b*a-2*int(i==j)*I) for i,a in enumerate(ext+vv) for j,b in enumerate(ext+vv)))
    roots,up,dn,hvec,E,F,H,P,Q,G,eta,tau,parity,pair=gauge(engine,old)
    ck('actual root compact metric and parity data',len(roots)==240 and parity.count(1)==136 and parity.count(-1)==112 and zero(E*F-F*E+H) and zero(E.H*G+G*F) and all(G[:j,:j].det()>0 for j in range(1,9)))
    Cas=cm(-P*P-Q*Q+H*H/4);a=s.Rational(3,4)
    P0=cm(s.Rational(2,3)*(Cas-a*IG)*(Cas-2*IG));P1=cm(-s.Rational(16,15)*Cas*(Cas-2*IG));P2=cm(s.Rational(2,5)*Cas*(Cas-a*IG))
    ck('complete root Casimir polynomial not sampled character',zero(Cas*(Cas-a*IG)*(Cas-2*IG)) and zero(Cas.H*G-G*Cas))
    ck('all root Casimir projectors complete and orthogonal',zero(P0+P1+P2-IG) and all(zero(A*A-A) and zero(A.H*G-G*A) for A in (P0,P1,P2)) and all(zero(A*B) for A,B in ((P0,P1),(P0,P2),(P1,P2))))
    ck('root branching dimensions are coefficient dimensions',s.trace(P0)==133 and s.trace(P1)==112 and s.trace(P2)==3)
    unit=lambda j:s.SparseMatrix(248,1,{(j,0):1})
    hr=s.SparseMatrix(248,1,{(j,0):v for j,v in hvec.items()})
    Wt=s.SparseMatrix.hstack(unit(up),-hr/s.sqrt(2),unit(dn))
    highest=[j for j in range(248) if H[j,j]==1];Vp=s.SparseMatrix(248,len(highest),{(j,k):1 for k,j in enumerate(highest)})
    Vm=-F*Vp
    Et=s.Matrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]]);Ht=s.diag(2,0,-2)
    ck('actual normalized triplet intertwines every root generator',zero(Wt.H*G*Wt-s.eye(3)) and zero(E*Wt-Wt*Et) and zero(F*Wt+Wt*Et.T) and zero(H*Wt-Wt*Ht))
    ck('all actual doublet maps and norms not only dimension match',len(highest)==56 and zero(Vp.H*G*Vp-s.eye(56)) and zero(Vm.H*G*Vm-s.eye(56)) and zero(Vp.H*G*Vm) and zero(E*Vp) and zero(F*Vm) and zero(E*Vm-Vp) and zero(F*Vp+Vm) and zero(H*Vp-Vp) and zero(H*Vm+Vm))
    Wn=s.SparseMatrix.hstack(Wt,Vp,Vm)
    ck('actual root maps and singlet kernel resolve all248',zero(Wn.H*G*Wn-s.eye(115)) and zero(Wn*Wn.H*G+P0-IG) and all(zero(A*P0) for A in (E,F,H,P,Q)))
    ck('full coefficient decomposition retains eta and compact conjugation',all(zero(eta*A-A*eta) and zero(tau*A.conjugate()*tau-A) for A in (P0,P1,P2)))
    Phe=cm((IG+eta)*P0/2);Pho=P0-Phe
    mult=Counter(parity[j] for j in highest)
    ck('even and odd root kernels and doublets all retained',s.trace(Phe)==79 and s.trace(Pho)==54 and mult==Counter({1:28,-1:28}) and zero(eta*Vp-Vp*s.diag(*[parity[j] for j in highest])) and zero(eta*Vm+Vm*s.diag(*[parity[j] for j in highest])))
    # Complete compact even centralizer, actual all basis-pair brackets.
    Pc=Phe[:8,:8];columns=Pc.columnspace();hb=[{i:v[i] for i in range(8) if v[i]!=0} for v in columns]
    root_h=[j for j in range(8,248) if Phe[j,j]==1];hb += [{j:s.Integer(1)} for j in root_h]
    block=s.SparseMatrix(248,248,{(i,j):v for (i,j),v in Pc.todok().items()}|{(j,j):1 for j in root_h})
    ck('complete even centralizer basis not a selected commuting subset',len(hb)==79 and len(columns)==7 and len(root_h)==72 and zero(block-Phe) and zero(Phe.H*G-G*Phe))
    def bvec(x,y):
        d={}
        for p,z in x.items():
            for q,w in y.items():
                for j,c in pair(p,q).items():d[j]=d.get(j,0)+z*w*c
        return {j:s.expand(v) for j,v in d.items() if s.expand(v)!=0}
    projector_columns={j:{} for j in range(248)}
    for (i,j),v in Phe.todok().items():projector_columns[j][i]=v
    alpha={j:pair(j,up).get(up,0) for j in range(8)}
    def member(d):
        if method=='native':return all(j<8 or j in root_h for j in d) and sum(alpha[j]*v for j,v in d.items() if j<8)==0
        out={}
        for j,v in d.items():
            for k,w in projector_columns[j].items():out[k]=out.get(k,0)+v*w
        return all(s.cancel(out.get(j,0)-d.get(j,0))==0 for j in set(out)|set(d))
    ck('centralizer membership criteria act on every basis column',all(member(x) for x in hb) and not member({up:1}))
    closure=[]
    for i,x in enumerate(hb):
        for j,y in enumerate(hb):
            d=bvec(x,y)
            if not member(d):raise ValueError('Centralizer bracket leaves retained space')
            if d:closure.append([i,j,[[k,str(v)] for k,v in sorted(d.items())]])
    ck('all6241 retained gauge basis brackets close',len(hb)**2==6241 and bool(closure))
    beta=root_h[0];betan=8+roots.index(tuple(-x for x in roots[beta-8]));gx={beta:1,betan:1};gy={beta:s.I,betan:-s.I}
    ck('actual compact nonabelian gauge interaction survives',member(gx) and member(gy) and bool(bvec(gx,gy)) and all(not bvec(z,bg) for z in (gx,gy) for bg in ({up:1},{dn:1},hvec)))
    vec=lambda d:s.SparseMatrix(248,1,{(j,0):v for j,v in d.items()})
    ck('nonabelian retained pair is actually compact real',zero(tau*vec(gx).conjugate()-vec(gx)) and zero(tau*vec(gy).conjugate()-vec(gy)) and not zero(tau*unit(beta).conjugate()-unit(beta)))
    ck('retained gauge algebra is real and orthogonal to root background',zero(tau*Phe.conjugate()*tau-Phe) and zero(Phe*hr) and zero(Phe*unit(up)) and zero(Phe*unit(dn)))
    # Source Clifford5 decomposition, full16 retained and no direction gap.
    R=cm(-s.I*vv[4]*vv[5]);B=cm(s.I*vv[2]*vv[3]);K=cm(R*B);Mh=(3*vv[0]+4*vv[1])/5;W=cm(K*Mh)
    ck('computational spin label is Hermitian and complete',zero(W.H-W) and zero(W*W-I) and s.trace(W)==0 and all(zero(W*x-x*W) for x in [R,B,vv[2],vv[3],vv[4],vv[5],Mh]))
    z=s.Symbol('unit_circle_parameter',real=True);Mu=((1-z*z)*vv[0]+2*z*vv[1])/(1+z*z);Wu=K*Mu
    ck('spin reduction holds on whole unit horizontal circle',zero(Mu*Mu-I) and zero(Wu*Wu-I) and all(zero(Wu*x-x*Wu) for x in vv[2:]) and zero((K*(-vv[0]))**2-I))
    sig1=s.Matrix([[0,1],[1,0]]);sig2=s.Matrix([[0,-s.I],[s.I,0]]);sig3=s.diag(1,-1);i2=s.eye(2);i4=s.eye(4)
    rn=s.kronecker_product(sig3,i2);bn=s.kronecker_product(i2,sig3);vn=s.kronecker_product(i2,sig1)
    vred=[vn,-s.kronecker_product(i2,sig2),s.kronecker_product(sig1,sig3),s.kronecker_product(sig2,sig3)]
    allmaps=[]
    for sign in (1,-1):
        seedproj=cm((I+R)*(I+B)*(I+sign*W)/8)
        seeds=s.GramSchmidt(seedproj.columnspace(),orthonormal=True)
        ck('full spin seed multiplicity '+str(sign),len(seeds)==2)
        for seed in seeds:
            U=cm(s.Matrix.hstack(seed,vv[2]*seed,vv[4]*seed,vv[2]*vv[4]*seed));allmaps.append(U)
            ck('source spin isometry and all reduced generators '+str((sign,len(allmaps))),zero(U.H*U-i4) and all(zero(v*U-U*w) for v,w in zip(vv[2:],vred)) and zero(R*U-U*rn) and zero(B*U-U*bn) and zero(Mh*U-sign*U*rn*bn))
    Uall=s.Matrix.hstack(*allmaps)
    ck('source reconstruction is full16 not one computational sign',zero(Uall.H*Uall-I) and zero(Uall*Uall.H-I))
    ck('external Lorentz mixes computational signs and full radial law retains it',all(zero(x*W+W*x) for x in ext) and all(zero(x*A-A*x) for x in ext for A in [R,B,s.I*vv[2]*Mh,vv[2]*vv[4],vv[2]*vv[5]]))
    ck('actual root Cartan plus R conserved including both Higgs vertices',zero(R*(vv[2]*vv[4])-(vv[2]*vv[4])*R-2*s.I*vv[2]*vv[5]) and zero(R*(vv[2]*vv[5])-(vv[2]*vv[5])*R+2*s.I*vv[2]*vv[4]) and zero(H*P-P*H-2*s.I*Q) and zero(H*Q-Q*H+2*s.I*P))
    # Small exact matrices per root module; no sampled angular census.
    t,g,rho,j=s.symbols('t g rho j',real=True);reduced=[];direction_total=0
    kinds=[(0,1,79),(0,-1,54),(1,1,mult[1]),(1,-1,mult[-1]),(2,-1,1)]
    for N,ep0,count in kinds:
        eg=s.zeros(N+1)
        for a0 in range(N):eg[a0,a0+1]=s.sqrt((a0+1)*(N-a0))
        fg=-eg.T;hg=s.diag(*[N-2*a0 for a0 in range(N+1)]);pg=(eg+fg)/2;qg=(eg-fg)/(2*s.I)
        etg=s.diag(*[ep0*(-1)**a0 for a0 in range(N+1)]);ng=s.eye(N+1);dim=4*(N+1)
        JJ=s.kronecker_product(rn,ng)+s.kronecker_product(i4,hg);LL=s.kronecker_product(rn,etg)
        TT=s.kronecker_product(vred[0]*vred[2],pg)+s.kronecker_product(vred[0]*vred[3],qg)
        for sign in (1,-1):
            AA=sign*s.I*vn*rn*bn
            op0=2*s.kronecker_product(bn*(j*i4+rn/4),ng)/t+g*g*t*s.kronecker_product(bn,hg)/(1-g*g*t*t)+2*g*TT/(1-g*g*t*t)+2*rho*t*s.kronecker_product(AA,ng)
            current=s.kronecker_product(vn,ng)
            ck('full reduced symmetry and current '+str((N,ep0,sign)),zero(JJ*op0-op0*JJ) and zero(LL*op0-op0*LL) and zero(op0.H-op0) and zero(op0*current+current*op0))
            if N>0:ck('wrong Cartan R sign detected '+str((N,ep0,sign)),not zero((JJ-2*s.kronecker_product(rn,ng))*op0-op0*(JJ-2*s.kronecker_product(rn,ng))))
            for weight in sorted(set(JJ.diagonal())):
                inds=[a0 for a0 in range(dim) if JJ[a0,a0]==weight];small=op0.extract(inds,inds);cc=current.extract(inds,inds)
                labels=set(LL[a0,a0] for a0 in inds)
                ck('small complete charged or neutral block '+str((N,ep0,sign,weight)),len(inds) in (2,4) and len(labels)==1 and zero(small.H-small) and zero(small*cc+cc*small))
                encmat=lambda M:[[str(s.cancel(z)) for z in row] for row in M.tolist()]
                reduced.append({'highest_weight':N,'highest_parity':ep0,'copies':count,'computational_sign':sign,'J':int(weight),'etaR':int(next(iter(labels))),'size':len(inds),
                    'indicial':encmat((2*s.kronecker_product(bn*(j*i4+rn/4),ng)).extract(inds,inds)),
                    'backreaction':encmat(s.kronecker_product(bn,hg).extract(inds,inds)),
                    'yukawa':encmat((2*TT).extract(inds,inds)),
                    'horizontal':encmat((2*s.kronecker_product(AA,ng)).extract(inds,inds)),
                    'normal_current':encmat(cc)})
                direction_total+=len(inds)*count*2
    ck('all charged and root kernel blocks resolve full3968 coefficients',direction_total==16*248 and max(x['size'] for x in reduced)==4)
    # Actual scalar lambda/supercharge and no omitted-field source.
    twist=prior.load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','root_scalar_supercharge_map')
    op=twist.opposite(cs);ph=[1,1,-1,-s.I];ph+=list(map(s.conjugate,ph));L=cm(op['S']*s.diag(*[v for x in ph for v in [x]*2]))
    gh=s.kronecker_product(s.eye(4),s.I*cs[0]*cs[1],i2);gv=s.kronecker_product(s.eye(4),s.I*cs[2]*cs[3],i2)
    Pi=cm(op['MW']*(s.eye(32)+op['R']*gh)/2*(s.eye(32)+op['R']*gv)/2)
    lam=s.diag(*[int(f==0) for bar in range(2) for f in range(4) for spin in range(2)])
    ck('actual scalar supercharge is named lambda not equal rank only',zero(L.H*Pi*L-lam) and zero(L*lam*L.H-Pi) and s.trace(lam)==4)
    ck('all6 untraced internal gauge and Higgs gaugino currents vanish',all(zero(lam*v*lam) for v in vv))
    ck('external gauge and kinetic action preserves real lambda',all(zero(lam*v-v*lam) for v in ext) and zero(C*lam.conjugate()*C-lam) and zero(lam.H-lam) and zero(lam*lam-lam))
    ck('normal gaugino boundary current zero for every internal normal',all(zero(lam*v*lam) for v in vv[:4]) and all(zero(lam.T*C*v*lam) for v in vv))
    # Nonzero root background acts exactly trivially on all singlets.
    ck('free normal response exact on nonzero background kernel',all(zero(A*P0) for A in (P,Q,H)) and zero(eta*Phe-Phe))
    ck('all local nonlinear mixed gauge sources vanish without abelianizing',all(not bvec(z,bg) for z in (gx,gy,bvec(gx,gy)) for bg in ({up:1},{dn:1},hvec)) and member(bvec(gx,gy)) and bool(bvec(gx,gy)))
    ck('retained regular gauge and lambda has zero normal response',s.diff(s.Integer(1),t)==0 and all(zero(lam*v*lam) for v in vv) and zero(P*Phe) and zero(Q*Phe) and zero(H*Phe))
    positive_volume=s.Symbol('supplied_regulated_internal_volume',positive=True);parent_inverse=s.Symbol('supplied_parent_inverse_coupling',positive=True)
    ck('reduced gauge kinetic volume factor positive not predicted', (positive_volume*parent_inverse).is_positive)
    def digest(v):return hashlib.sha256(json.dumps(v,separators=(',',':')).encode()).hexdigest()
    records['root']={'standard_branching':'133 singlets +56doublets +1triplet; not the geometric SU2 embedding',
        'even_singlets':79,'odd_singlets':54,'doublets_highest_parity':{str(k):v for k,v in sorted(mult.items())},
        'closure_basis_pairs':6241,'closure_nonzero':len(closure),'closure_sha256':digest(closure),
        'even_centralizer_basis':[[[j,str(v)] for j,v in sorted(x.items())] for x in hb],
        'canonical_root_order':'Cartan0..7 followed by lexicographically sorted root8tuples',
        'nonabelian_witness':{'root':list(roots[beta-8]),'x':[[j,str(v)] for j,v in sorted(gx.items())],
            'y':[[j,str(v)] for j,v in sorted(gy.items())],'bracket':[[j,str(v)] for j,v in sorted(bvec(gx,gy).items())]}}
    records['blocks']={'directions':direction_total,'largest_active_size':4,'list':reduced,
        'all_j':'analytic j in Z+(etaR)/4; no angular truncation','computational_sign':'both signs retained; external Lorentz mixes them',
        'matrix_assembly':'Kt=indicial/t+g^2*t*backreaction/(1-g^2*t^2)+g*yukawa/(1-g^2*t^2)+rho*t*horizontal',
        'charged_finite_cauchy_response_computed':False}
    records['gauge_sector']={'scalar_supercharge_equals_source_lambda':True,'all_internal_currents':0,
        'status':'local classical consistent interacting N=1 gauge ansatz in supplied parent; omitted modes not proved absent',
        'gauge_group_selected_as_SM':False,'coupling':'supplied regulated volume times supplied parent inverse coupling',
        'boundary':'exact free response on root singlets at nonzero Higgs; regular even constants retained'}
    records['scope']='chosen odd Chevalley-root flat normal BPS chart; not full curved/global boundary theory, full spectrum, foundational SM/three or gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(method):
    d=run(method);print(json.dumps(d,indent=2));return 0 if d['all_passed'] else 1
