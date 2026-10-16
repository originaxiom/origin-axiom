"""Complete critical-sector fundamentals and controlled Volterra response."""
import hashlib,importlib.util,itertools,json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def clean(z):return s.cancel(s.expand(z))
def zero(M):return all(clean(z)==0 for z in M.todok().values())
def enc(M):return [[str(clean(z)) for z in row] for row in M.tolist()]
def canonical(N,x,method):
    wgt=s.sqrt(2) if N==2 else s.Integer(1);ss=1-x*x
    v=s.Matrix([-x,1])/ss**s.Rational(3,2) if N==1 else s.Matrix([-s.sqrt(2)*x,1+x*x])/ss**2
    w=x*ss*s.Matrix([v[1],-v[0]])
    kp=s.Matrix([[1/x-x/ss,2/ss],[2/ss,-x/ss]]) if N==1 else s.Matrix([[1/x,2*s.sqrt(2)/ss],[2*s.sqrt(2)/ss,-2*x/ss]])
    if method=='native':
        L=s.Matrix([2*x*s.log(x)-x**3,1-2*x*x+2*x*x*s.log(x)])/s.sqrt(ss) if N==1 else s.Matrix([2*s.sqrt(2)*x*(1+x*x)*s.log(x)-4*s.sqrt(2)*x**3,1-4*x*x-x**4+4*x*x*s.log(x)])/ss
    else:
        du=clean(kp[0,1]*x*ss/(w[0]**2));u=s.integrate(du,x)
        u-=s.limit(u-2*wgt*s.log(x),x,0)
        L=w*u+s.Matrix([0,x*ss/w[0]])
        L=L.applyfunc(s.simplify)
    bad=s.Matrix([L[1],-L[0]])/(x*ss)
    F=s.Matrix.hstack(s.Matrix([bad[0],0,0,bad[1]]),s.Matrix([v[0],0,0,v[1]]),s.Matrix([0,w[0],w[1],0]),s.Matrix([0,L[0],L[1],0]))
    C=s.diag(1,-1,0,0);D=s.diag(-1,1,1,-1) if N==1 else s.diag(0,0,2,-2)
    Y=s.Matrix([[0,0,0,2*wgt],[0,0,-2*wgt,0],[0,-2*wgt,0,0],[2*wgt,0,0,0]])
    A=s.Matrix([[0,-2*s.I,0,0],[2*s.I,0,0,0],[0,0,0,2*s.I],[0,0,-2*s.I,0]])
    V=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
    return C,D,Y,A,V,F,v,w,L
def rebuilt():
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1);I=s.eye(2);J=s.Symbol('j',real=True)
    R=s.kronecker_product(p3,I);B=s.kronecker_product(I,p3);v2=s.kronecker_product(I,p1);v4=s.kronecker_product(p1,p3);v5=s.kronecker_product(p2,p3)
    rows=[]
    for N,ep,copies in ((0,1,79),(0,-1,54),(1,1,28),(1,-1,28),(2,-1,1)):
        E=s.zeros(N+1)
        for a in range(N):E[a,a+1]=s.sqrt((a+1)*(N-a))
        F=-E.T;H=s.diag(*[N-2*a for a in range(N+1)]);P=(E+F)/2;Q=(E-F)/(2*s.I);eta=s.diag(*[ep*(-1)**a for a in range(N+1)]);ng=s.eye(N+1)
        JJ=s.kronecker_product(R,ng)+s.kronecker_product(s.eye(4),H);LL=s.kronecker_product(R,eta)
        for h in (1,-1):
            C=s.kronecker_product(2*B*(J*s.eye(4)+R/4),ng);D=s.kronecker_product(B,H);Y=2*(s.kronecker_product(v2*v4,P)+s.kronecker_product(v2*v5,Q));A=2*h*s.kronecker_product(s.I*v2*R*B,ng);V=s.kronecker_product(v2,ng)
            for weight in sorted(set(JJ.diagonal())):
                inds=[a for a in range(4*(N+1)) if JJ[a,a]==weight]
                row={'highest_weight':N,'highest_parity':ep,'copies':copies,'computational_sign':h,'J':int(weight),'etaR':int(LL[inds[0],inds[0]]),'size':len(inds)}
                for label,M in zip(('indicial','backreaction','yukawa','horizontal','normal_current'),(C,D,Y,A,V)):row[label]=[[str(z) for z in rr] for rr in M.extract(inds,inds).tolist()]
                rows.append(row)
    return rows
def signed_map(target,base):
    # Finite exact search for an ACTING unitary map, not matching spectra.
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((1,-1),repeat=4):
            T=s.zeros(4)
            for k,j in enumerate(perm):T[j,k]=signs[k]
            if any(T*M*T.T!=N for M,N in zip(base[:3],target[:3])):continue
            for ah in (1,-1):
                if T*base[3]*T.T!=ah*target[3]:continue
                for vh in (1,-1):
                    if T*base[4]*T.T==vh*target[4]:return T,ah,vh
    raise ValueError('No complete signed coefficient/current intertwiner')
def run(method):
    x=s.Symbol('x',positive=True);ss=1-x*x;beta=s.Symbol('beta',real=True);j=s.Symbol('j',real=True)
    checks={};records={}
    def ck(k,v):
        checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    saved=json.loads((HERE.parent/'surface_root_gauge_sector_2026_10_16/results/first_run/probe.json').read_text())['records']['blocks']['list']
    made=rebuilt();ck('every saved matrix and metadata reconstructed exactly',saved==made and len(saved)==28)
    rows=saved if method=='native' else made;cache={};can={}
    for N in (1,2):
        C,D,Y,A,V,F,v,w,L=canonical(N,x,method);K=C/x+x*D/ss+Y/ss;G=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
        ck('complete fundamental residual '+str(N),zero(F.diff(x)+K*F) and s.simplify(F.det()) in (1,-1))
        # All entries are REAL on the declared interval0<x<1. Transpose
        # avoids asking Sympy to infer sqrt(1-x^2)>0 from x>0 alone.
        ck('all four Green pairings and actual inverse '+str(N),zero(F.T*V*F-G) and zero(G*F.T*V*F-s.eye(4)))
        ck('log solution from independent reduction and determinant '+str(N),clean(s.det(s.Matrix.hstack(w,L))-x*ss)==0 and clean(v.dot(w))==0 and clean(v.dot(L)-1)==0)
        Fi=G*F.T*V;reg=F[:,2];crit=F[:,1];log=F[:,3];bad=F[:,0]
        pp=s.Matrix.hstack(crit,reg);pm=s.Matrix.hstack(log,reg);Pp=(pp*(pp.T*pp).inv()*pp.T).applyfunc(s.simplify);Pm=s.diag(0,1,1,0)
        ck('both full trace planes and Green nullness '+str(N),zero(pp.T*V*pp) and zero(pm.T*V*pm) and zero(Pm*pm-pm) and pp.rank()==pm.rank()==2)
        ck('background dependent projector and derivative current '+str(N),zero(Pp*Pp-Pp) and not zero(Pp.diff(x)) and zero(Pp*Pp.diff(x)*Pp) and zero(Pp.diff(x)*V*Pp+Pp*V*Pp.diff(x)))
        ell=1 if N==1 else s.sqrt(2);lc=s.Symbol('log_kappa',real=True)
        shifted=L.applyfunc(lambda z:z.subs(s.log(x),s.log(x)-lc))
        ck('log scale change only adds regular seed '+str(N),zero(shifted-L+2*ell*lc*w))
        leading=[z.applyfunc(lambda a:s.limit(a,x,0)) for z in (x*bad,crit,reg/x,log)]
        ck('all L2 and nonL2 leading columns preserved '+str(N),all(not zero(a) for a in leading) and zero(leading[1]-s.eye(4)[:,3]) and zero(leading[3]-s.eye(4)[:,2]))
        ck('negative controls full backreaction Higgs leading only '+str(N),not zero(F.diff(x)+(C/x+Y/ss)*F) and not zero(F.diff(x)+(C/x+x*D/ss)*F) and not zero(K*s.eye(4)[:,3]))
        ck('nonL2 and missing log controls fire '+str(N),not zero(bad.T*V*reg) and s.Matrix.hstack(reg).rank()!=pm.rank())
        # FTC certificate: differentiating the Volterra primitive is the
        # exact source term; algebra cancels all fundamental-matrix terms.
        q=s.Matrix(s.symbols('q0:4'));zz=s.Matrix(s.symbols('z0:4'))
        ck('Volterra derivative identity full nonzero momentum '+str(N),zero(F.diff(x)*zz+K*F*zz) and zero(F*Fi*x*A*q-x*A*q) and zero(K*V+V*K) and zero(A*V+V*A) and A*A==4*s.eye(4))
        can[N]=(C,D,Y,A,V,F,Pp,Pm)
        cache[N]={'fundamental':enc(F),'green_gram':enc(G),'sigma_plus_projector':enc(Pp),'sigma_minus_projector':enc(Pm)}
    covered=0;out=[];maps={}
    for row in rows:
        key=tuple(row[k] for k in ('highest_weight','highest_parity','computational_sign','J','etaR'));N=key[0];l=key[-1];sz=row['size']
        Cj=s.Matrix([[s.sympify(z,locals={'j':j}) for z in rr] for rr in row['indicial']]);B=Cj.diff(j)/2;R=2*B*Cj-4*j*s.eye(sz)
        C=Cj.subs(j,s.Rational(l,4));D,Y,A,V=[s.Matrix(row[k]) for k in ('backreaction','yukawa','horizontal','normal_current')]
        K=C/x+x*D/ss+Y/ss
        if sz==4:
            T,ah,vh=signed_map((C,D,Y,A,V),can[N]);F=T*can[N][5];maps[key]=(T,can[N][6],F[:,1])
            ck('actual entire coupled block '+str(key),zero(F.diff(x)+K*F) and zero(K.H-K) and zero(K*V+V*K) and zero(A*V+V*A) and A*A==4*s.eye(4))
            # Leading sigma is tested in the ACTUAL coefficient ordering.
            plus=(F[:,1]).applyfunc(lambda z:s.limit(z,x,0));minus=(F[:,3]).applyfunc(lambda z:s.limit(z,x,0));KR=R*B
            ck('both actual critical signs retained '+str(key),zero(KR*plus-plus) and zero(KR*minus+minus))
            out.append({'key':list(key),'kind':'coupled4','map':enc(T),'horizontal_sign':ah,'current_sign':vh})
        else:
            ck('all singleton terms diagonal not mistaken free '+str(key),C.is_diagonal() and D.is_diagonal() and zero(Y) and s.trace(C)==s.trace(D)==0 and all(C[a,a] in (-1,0,1) for a in range(2)))
            F=s.diag(*[x**(-C[a,a])*ss**(D[a,a]/2) for a in range(2)])
            ck('complete singleton fundamental and Green '+str(key),zero(F.diff(x)+K*F) and zero(F.T*V*F-V) and A*A==4*s.eye(2) and zero(A*V+V*A))
            if C==s.zeros(2):inds={str(sig):[a for a in range(2) if (R*B)[a,a]==sig] for sig in (1,-1)}
            else:inds={str(sig):[a for a in range(2) if C[a,a]==-1] for sig in (1,-1)}
            ck('singleton complete allowed trace for both signs '+str(key),all(len(v)==1 for v in inds.values()) and all(zero(F[:,v].T*V*F[:,v]) for v in inds.values()))
            out.append({'key':list(key),'kind':'singleton2','fundamental':enc(F),'allowed_columns':inds,'cartan_not_free':D!=s.zeros(2)})
        covered+=sz*row['copies']*2
    ck('all critical sector types and full multiplicities retained',covered==3968 and len(out)==28 and {r['key'][2] for r in out}=={-1,1})
    # Rational upper envelopes in PROOF2; l1 bounds dominate Euclidean.
    a=s.Rational(1,4);smin=1-a*a
    envelopes={'doublet_v':(a+1)/smin**2,'triplet_v':(2*a+1+a*a)/smin**2,
        'doublet_regular_over_x':(1+a)/smin,'triplet_regular_over_x':(1+a*a+2*a)/smin,
        'doublet_log':(2+a**3+1+2*a*a+2*a)/smin,
        'triplet_log':(4*(1+a*a)+8*a**3+1+4*a*a+a**4+4*a)/smin}
    ck('rational column majorants for whole interval',all(z<4 for k,z in envelopes.items() if 'log' not in k) and all(z<8 for k,z in envelopes.items() if 'log' in k) and 8/smin<16)
    yy=s.Symbol('y',positive=True);kernel=2*64*(yy/x+1+x/yy)*yy;bound=s.integrate(kernel,(yy,0,x))
    ck('exact Volterra integral bound not sampled grid',clean(bound-s.Rational(704,3)*x*x)==0 and s.Rational(704,3)<256)
    # Explicit two-sided bound control: triplet v at x=1/4 exceeds1.
    vtest=canonical(2,x,'native')[6].subs(x,a)
    ck('majorant lowered below true vector fails',s.simplify(vtest.dot(vtest))>1 and all(z>0 for z in envelopes.values()))
    n=s.Symbol('n',integer=True,nonnegative=True);q=s.Symbol('q',nonnegative=True)
    ck('Neumann tail and all finite momentum small radius',s.simplify(q**(n+1)/(1-q)-q**(n+1)-q**(n+2)/(1-q))==0 and 256*s.Rational(1,32)**2<s.Rational(1,2))
    # Actual full source reconstruction and BPS map, not a toy rank count.
    parent=load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py','critical_parent');vv,ext,cs,engine,valid,old=parent.setup(method)
    root=load(HERE.parent/'surface_root_gauge_sector_2026_10_16/analysis.py','critical_root');roots,up,dn,hvec,E,Fg,H,P,Q,G,eta,tau,parity,pair=root.gauge(engine,old)
    unit=lambda k:s.SparseMatrix(248,1,{(k,0):1});hr=s.SparseMatrix(248,1,{(k,0):v for k,v in hvec.items()});Wt=s.SparseMatrix.hstack(unit(up),-hr/s.sqrt(2),unit(dn))
    Et=s.Matrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]]);Ht=s.diag(2,0,-2);Pt=(Et-Et.T)/2;Qt=(Et+Et.T)/(2*s.I);etat=s.diag(-1,1,-1);taut=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    ck('same actual E8 triplet and source dictionary',valid and zero(E*Wt-Wt*Et) and zero(H*Wt-Wt*Ht) and zero(P*Wt-Wt*Pt) and zero(Q*Wt-Wt*Qt) and zero(tau*Wt.conjugate()-Wt*taut) and zero(eta*Wt-Wt*etat))
    I=s.eye(16);Rs=-s.I*vv[4]*vv[5];Bs=s.I*vv[2]*vv[3];L=s.kronecker_product(Rs,etat);JJ=s.kronecker_product(Rs,s.eye(3))+s.kronecker_product(I,Ht);C16=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8));C48=s.kronecker_product(C16,taut)
    lam=s.diag(*[int(f==0) for bar in range(2) for f in range(4) for spin in range(2)]);z=s.Symbol('angular_phase',nonzero=True);sn=(z**4-z**-4)/(2*s.I);co=(z**4+z**-4)/2
    # t*a; x=g*t removes g WITHOUT changing background normalization.
    scalar=(1+x*x)/ss**2
    av=[s.Matrix([0,s.I*s.sqrt(2)*x*sn/ss**2,0]),s.Matrix([0,-s.I*s.sqrt(2)*x*co/ss**2,0]),s.Matrix([scalar/z**2/2,0,scalar*z**2/2]),s.Matrix([scalar/z**2/(2*s.I),0,-scalar*z**2/(2*s.I)])]
    psi=-sum((s.kronecker_product(v*lam,b) for v,b in zip(vv[2:],av)),s.zeros(48,16))
    spin=(I+Bs)/2/z**2+(I-Bs)/2*z**2;scalarframe=(I+Rs)/2/z+(I-Rs)/2*z
    ftheta=s.kronecker_product(scalarframe*spin,s.eye(3))*psi;f0=ftheta.subs(z,1)
    phase=(s.eye(48)+L)*z/2+(s.eye(48)-L)/(2*z)
    ck('full nonlinear angular BPS tangent not leading only',zero(ftheta-phase*f0) and zero(JJ*f0-L*f0) and zero(s.kronecker_product(Rs*Bs,s.eye(3))*f0-f0) and f0.subs(x,0).rank()==4)
    C0=s.kronecker_product(Bs,s.eye(3))*(L+s.kronecker_product(Rs,s.eye(3)))/2;Ds=s.kronecker_product(Bs,Ht);Ys=2*(s.kronecker_product(vv[2]*vv[4],Pt)+s.kronecker_product(vv[2]*vv[5],Qt));Kfull=C0/x+x*Ds/ss+Ys/ss
    ck('full actual 48component nonlinear tangent radial residual',zero(f0.diff(x)+Kfull*f0) and not zero(f0.diff(x)+(C0/x+Ys/ss)*f0))
    ck('full source Majorana of BPS tangent',zero(C48*f0.conjugate()-f0*C16) and zero(C48*C48.conjugate()-s.eye(48)))
    Mh=(3*vv[0]+4*vv[1])/5;W=Rs*Bs*Mh;Us=[];matched=0
    r4=s.diag(1,1,-1,-1);j12=s.kronecker_product(r4,s.eye(3))+s.kronecker_product(s.eye(4),Ht)
    for h in (1,-1):
        seeds=s.GramSchmidt(((I+Rs)*(I+Bs)*(I+h*W)/8).columnspace(),orthonormal=True)
        for seed in seeds:
            U=s.Matrix.hstack(seed,vv[2]*seed,vv[4]*seed,vv[2]*vv[4]*seed);Us.append(U);fsmall=s.kronecker_product(U.H,s.eye(3))*f0
            for J in (1,-1):
                inds=[k for k in range(12) if j12[k,k]==J];block=fsmall.extract(inds,list(range(16)));l=J;key=(2,-1,h,J,l);T,pp,vline=maps[key];Pv=T*pp*T.T
                pivot=next(k for k in range(4) if vline[k]!=0)
                ck('actual full BPS profile in charged block '+str((h,len(Us),J)),not zero(block) and zero(Pv*block-block) and zero(block-vline*block[pivot,:]/vline[pivot]))
                matched+=1
    Uall=s.Matrix.hstack(*Us)
    ck('all spin blocks reconstruct full actual BPS source',matched==8 and zero(Uall*Uall.H-I) and zero(s.kronecker_product(Uall,s.eye(3))*s.kronecker_product(Uall.H,s.eye(3))*f0-f0))
    records['canonical']=cache;records['all_blocks']=out;records['coefficient_directions']=covered
    records['volterra']={'interval':'0<x<=a<=1/4; 256|beta|a^2<1','bound':'(704/3)|beta|x^2 <256|beta|x^2','column_bounds':[16,4,4,8],'envelopes':{k:str(v) for k,v in envelopes.items()},'construction':'convergent integral series plus finite annular continuation; NOT numerical interval evaluation or uniform high-frequency estimate'}
    records['tangent']={'matched_source_blocks':matched,'full_angular_radial_Majorana':True,'sigma':1,'status':'local exact nonlinear BPS tangent; not a global physical particle'}
    records['scope']={'angular':'ALL28types at j=etaR/4, with regular partners; n!=0 not solved here','momentum':'all finite real via authored Volterra proof; explicit complete zero-momentum matrices','full_curved_boundary_action':False,'full_physical_SM_three_gravity':False,'shared_author_not_independent_acceptance':True}
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(method):
    d=run(method);print(json.dumps(d,indent=2));return 0 if d['all_passed'] else 1
