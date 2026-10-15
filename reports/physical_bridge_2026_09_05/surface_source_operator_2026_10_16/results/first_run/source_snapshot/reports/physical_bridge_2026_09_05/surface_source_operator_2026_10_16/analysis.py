"""Presealed source-component gate, not a source identification by assumption."""
import importlib.util,json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sp=importlib.util.spec_from_file_location('source_join_prior',HERE.parent/'surface_variational_join_2026_10_16/analysis.py')
prior=importlib.util.module_from_spec(sp);sp.loader.exec_module(prior)
NC=3;N=16*NC;E=s.Matrix([[0,1],[-1,0]])
J=s.Matrix([[0,1,0],[-1,0,1],[0,-1,0]])
def clean(x):
    if isinstance(x,s.MatrixBase):return x.applyfunc(clean)
    return s.simplify(s.expand_complex(x))
def zero(x):return all(v==0 or clean(v)==0 for v in x)
def enc(x):return [[str(clean(v)) for v in row] for row in x.tolist()]
def sparse(x):return [[i,j,str(clean(v))] for (i,j),v in sorted(x.todok().items()) if clean(v)!=0]
def witness(x):
    for (i,j),v in sorted(x.todok().items()):
        vv=clean(v)
        if vv!=0:return [i,j,str(vv)]
    return None
dt={(0,):1,(1,):s.I};dz={(2,):1,(3,):s.I}
bt={(0,):1,(1,):-s.I};bz={(2,):1,(3,):-s.I}
omega={(0,1):1,(2,3):1}
form_product=prior.wedge
def const(f):return {(k,()):s.sympify(v) for k,v in f.items()}
def add(*xs):
    out={}
    for a in xs:
        for k,v in a.items():out[k]=out.get(k,0)+v
    return {k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
def scale(a,c):return {k:s.expand(c*v) for k,v in a.items() if s.expand(c*v)!=0}
def mul(a,b,graded):
    out={}
    for (f,g),v in a.items():
        for (h,k),w in b.items():
            ff=form_product({f:1},{h:1});gg=form_product({g:1},{k:1})
            for fp,fs in ff.items():
                for gp,gs in gg.items():
                    key=(fp,gp)
                    out[key]=out.get(key,0)+v*w*fs*gs*(-1)**(graded*len(f)*len(k))
    return {k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
forms=[{():1},bt,bz,form_product(dt,dz)]
barforms=[{():1},dt,dz,form_product(bt,bz)]
norm=[s.sqrt(2),s.Integer(2),s.Integer(2),s.Integer(2)]
def field(i,alpha,c,bar=False):
    gen=((4*int(bar)+i)*2+alpha)*NC+c
    return {(f,(gen,)):v/norm[i] for f,v in (barforms if bar else forms)[i].items()}
def action(i,alpha,c,bar=False):return add(*(scale(field(i,alpha,b,bar),J[c,b]) for b in range(NC)))
def derivative(i,alpha,c,bar,direction,holomorphic,graded):
    if direction>=4:return {}
    line=0 if direction<2 else 1
    coframe=([dt,dz] if holomorphic else [bt,bz])[line]
    factor=s.Rational(1,2) if direction%2==0 else (-s.I if holomorphic else s.I)/2
    return scale(mul(const(coframe),action(i,alpha,c,bar),graded),factor)
def phi_action(i,alpha,c,bar,direction,conjugate_phi,sigma,zeta,graded):
    if direction<4:return {}
    factor=(s.Integer(1) if direction==4 else (-s.I if conjugate_phi else s.I))/2
    factor*=sigma*s.conjugate(zeta) if conjugate_phi else zeta
    coframe=form_product(bt,bz) if conjugate_phi else form_product(dt,dz)
    return scale(mul(const(coframe),action(i,alpha,c,bar),graded),factor)
def matrix(a):
    out=s.MutableSparseMatrix(N,N,{})
    for (f,g),v in a.items():
        if f!=(0,1,2,3) or len(g)!=2:raise ValueError('Action term is not a top form/quadratic fermion')
        out[g[0],g[1]]+=v;out[g[1],g[0]]-=v
    return clean(out)
def source_time(graded):
    out={};ww=mul(const(omega),const(omega),graded)
    for a in range(2):
        for c in range(NC):
            out=add(out,scale(mul(ww,mul(action(0,a,c),field(0,a,c,True),graded),graded),-s.I))
            out=add(out,scale(mul(action(3,a,c),field(3,a,c,True),graded),-s.I))
            for i in (1,2):
                out=add(out,scale(mul(const(omega),mul(action(i,a,c,True),field(i,a,c),graded),graded),-2))
    return matrix(out)
def source_internal(direction,w,graded,sigma,zeta):
    out={}
    for a in range(2):
        for b in range(2):
            e=E[a,b]
            if not e:continue
            for c in range(NC):
                # Tr=-delta. Upper/lower dotted contractions are -E.
                out=add(out,scale(mul(field(0,a,c),phi_action(3,b,c,False,direction,True,sigma,zeta,graded),graded),s.sqrt(2)*e))
                out=add(out,scale(mul(field(0,a,c,True),phi_action(3,b,c,True,direction,False,sigma,zeta,graded),graded),-s.sqrt(2)*e))
                for i in (1,2):
                    eta_psi=mul(derivative(0,a,c,False,direction,True,graded),field(i,b,c),graded)
                    bar_psi_eta=mul(field(i,a,c,True),derivative(0,b,c,True,direction,False,graded),graded)
                    out=add(out,scale(mul(const(omega),eta_psi,graded),2*s.I*s.sqrt(2)*e),
                        scale(mul(const(omega),bar_psi_eta,graded),-2*s.I*s.sqrt(2)*e))
                    out=add(out,scale(mul(field(3,a,c),derivative(i,b,c,False,direction,False,graded),graded),w*e),
                        scale(mul(field(3,a,c,True),derivative(i,b,c,True,direction,True,graded),graded),-w*e))
                    for j in (1,2):
                        out=add(out,scale(mul(field(i,a,c),phi_action(j,b,c,False,direction,False,sigma,zeta,graded),graded),w*e/2),
                            scale(mul(field(i,a,c,True),phi_action(j,b,c,True,direction,True,sigma,zeta,graded),graded),w*e/2))
    return matrix(out)

def phase_map(actual,canonical):
    ratios={};bad=None
    for j,(a,b) in enumerate(zip(actual,canonical)):
        # Chiral block only. The entire conjugate block is a SEPARATE gate.
        for i in range(8*NC):
            for k in range(8*NC):
                av,bv=a[i,k],b[i,k]
                if av==0 and bv==0:continue
                if bv==0:return None,['support',j,i,k,str(av)]
                ratio=clean(av/bv);pair=tuple(sorted((i//(2*NC),k//(2*NC))))
                if pair[0]==pair[1]:return None,['diagonal flavour',j,i,k,str(ratio)]
                if pair in ratios and clean(ratios[pair]-ratio)!=0:
                    return None,['inconsistent edge',j,i,k,str(ratio),str(ratios[pair])]
                ratios[pair]=ratio
    if any(k not in ratios for k in ((0,1),(0,2),(1,2),(0,3))):
        return None,['missing phase triangle',str(ratios)]
    if any(clean(v*s.conjugate(v)-1)!=0 for v in ratios.values()):
        return None,['nonunit edge',[[list(k),str(v)] for k,v in ratios.items()]]
    first=clean(s.sqrt(clean(ratios[0,1]*ratios[0,2]/ratios[1,2])))
    phases=[first]+[clean(ratios[0,j]/first) for j in range(1,4)]
    if any(clean(phases[i]*phases[j]-r)!=0 for (i,j),r in ratios.items()):
        return None,['triangle cycle',[[list(k),str(v)] for k,v in ratios.items()]]
    U=s.diag(*[v for ph in phases+[s.conjugate(x) for x in phases] for v in [ph]*(2*NC)])
    for j,(a,b) in enumerate(zip(actual,canonical)):
        residual=clean((a-U.T*b*U)[:8*NC,:8*NC])
        if not zero(residual):return None,['coefficient',j,witness(residual)]
    return phases,None
def complete(a):
    n=a.rows//2;L=a[:n,:n]
    return s.diag(L,-L.conjugate())

def run(cs,setup_valid):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    I2=s.eye(2);I4=s.eye(4);I32=s.eye(32);p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]];g5=clean(s.I*s.prod(gam))
    G0=s.kronecker_product(gam[0],I4,p3)
    G=[s.kronecker_product(g5,s.I*c,p3) for c in cs]+[s.kronecker_product(I4,I4,p1),s.kronecker_product(I4,I4,p2)]
    B=clean(s.kronecker_product(gam[0]*gam[1]*gam[3],cs[1]*cs[3],p2))
    MW=clean((I32-s.kronecker_product(g5,-s.prod(cs),p3))/2)
    L=s.Matrix.hstack(*((I4+g5)/2).columnspace())
    W=s.Matrix.hstack(*[s.kronecker_product(L,s.eye(4)[:,i],s.eye(2)[:,r]) for i,r in ((3,1),(1,0),(2,0),(0,1))])
    S=W.row_join(B*W.conjugate());Bn=clean(S.T*B.H*S)
    ck('actual frame supplied',setup_valid)
    ck('actual normalized full MW Nambu frame',zero(S.H*S-s.eye(16)) and zero(S*S.H-MW))
    swap=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8))
    ck('actual induced Nambu time and reality',zero(Bn-swap) and zero(B*S.conjugate()-S*swap))
    can=[clean(s.kronecker_product(-s.I*S.T*B.H*G0*g*S,J)) for g in G]
    clock=clean(s.I*s.kronecker_product(Bn,J));Bfull=s.kronecker_product(Bn,s.eye(NC))
    ck('canonical quadratic action antisymmetric',all(zero(a+a.T) for a in can+[clock]))
    ck('canonical action equals its actual real completion',all(zero(a-complete(a)) for a in can))
    records['canonical_six_action_matrices']=[sparse(a) for a in can]
    times=[source_time(k) for k in (0,1)]
    ck('graded signed time is canonical positive contour',zero(times[1]-clock))
    ck('ordinary naive contour has a real signed mismatch',not zero(times[0]-clock))
    # Basic algebra controls, including differential from the LEFT.
    f=field(1,0,0);h=field(2,1,1)
    ck('graded one form fermion product reverses ordinary sign',mul(f,h,1)==scale(mul(f,h,0),-1))
    ck('Grassmann overlap vanishes',not mul(field(0,0,0),field(0,0,0),1))
    ck('graded internal differential has its induced sign',derivative(0,0,0,False,0,True,1)==scale(derivative(0,0,0,False,0,True,0),-1))
    planted=[1,s.I,-1,1]
    U0=s.diag(*[v for ph in planted+[s.conjugate(x) for x in planted] for v in [ph]*(2*NC)])
    planted_A=[clean(U0.T*a*U0) for a in can]
    found,why=phase_map(planted_A,can)
    ck('phase solver recovers planted all direction map',found is not None and why is None)
    wrong=[a.copy() for a in planted_A];nonzero=next((i,j) for (i,j),v in wrong[0].todok().items() if i<8*NC and j<8*NC and v!=0)
    i,j=nonzero;wrong[0][i,j]*=2;wrong[0][j,i]=-wrong[0][i,j]
    rejected,whybad=phase_map(wrong,can)
    ck('phase solver rejects magnitude changing planted defect',rejected is None and whybad is not None)
    # Actual source census, not checks declared true by expected physical outcome.
    cases=[];t=s.Symbol('t',positive=True)
    T=s.diag(*[v for bar in range(2) for i in range(4) for v in [1/t if i==0 else t]*(2*NC)])
    for grade in (0,1):
        for sigma in (-1,1):
            for zeta in (s.Integer(1),s.I):
                source=[source_internal(j,s.Integer(2),grade,sigma,zeta) for j in range(6)]
                ck('actual source contains no floating coefficients '+str((grade,sigma,zeta)),not any(a.has(s.Float) for a in source))
                ck('actual source six quadratic coefficients antisymmetric '+str((grade,sigma,zeta)),all(zero(a+a.T) for a in source))
                phases,why=phase_map(source,can)
                time_ok=zero(times[grade]-clock)
                row={'graded':grade,'scalar_bar_sign':sigma,'scalar_phase':str(zeta),'positive_time_in_declared_contour':time_ok,
                    'chiral_phase_map':phases is not None,'phase_witness':why,'phases':None if phases is None else [str(x) for x in phases],
                    'full_printed_match':False,'printed_witness':None,'completion_congruence':None}
                row['six_action_matrices']=[sparse(a) for a in source]
                if phases is not None:
                    U=s.diag(*[v for ph in phases+[s.conjugate(x) for x in phases] for v in [ph]*(2*NC)])
                    ck('actual phases unitary and preserve time '+str((grade,sigma,zeta)),zero(U.H*U-s.eye(N)) and zero(U.T*Bfull*U-Bfull))
                    full=[clean(a-U.T*b*U) for a,b in zip(source,can)]
                    row['full_printed_match']=all(zero(x) for x in full)
                    row['printed_witness']=next(([j,witness(x)] for j,x in enumerate(full) if not zero(x)),None)
                    # This is EXPLICIT Hermitian completion, not a silent source fix.
                    variable=[source_internal(j,2*t*t,grade,sigma,zeta) for j in range(6)]
                    completed=[complete(a) for a in variable]
                    baseline=[clean(U.T*a*U) for a in can]
                    variable_printed=[clean(a-T*b*T) for a,b in zip(variable,baseline)]
                    if not all(zero(x) for x in variable_printed):
                        row['full_printed_match']=False
                        if row['printed_witness'] is None:
                            row['printed_witness']=next((['all-w',j,witness(x)] for j,x in enumerate(variable_printed) if not zero(x)),None)
                    congruences=[clean(a-T*b*T) for a,b in zip(completed,baseline)]
                    row['completion_congruence']=all(zero(x) for x in congruences)
                    ck('actual completed congruence all six '+str((grade,sigma,zeta)),row['completion_congruence'])
                    # Selfadjointness/C apply only with the declared positive time.
                    if time_ok:
                        H=[clean(-Bfull*a) for a in completed]
                        ck('actual completed Hermiticity '+str((grade,sigma,zeta)),all(zero(h.H-h) for h in H))
                        ck('actual completed full real Hamiltonian '+str((grade,sigma,zeta)),all(zero(Bfull*h.conjugate()*Bfull+h) for h in H))
                        J2=s.Matrix([[0,0,1],[0,0,0],[-1,0,0]]);J3=J*J2-J2*J
                        coeff=[J,J2,J3,J+J2,J2+J3,J-J3]
                        extract=lambda a:s.Matrix(16,16,lambda i,j:a[i*NC,j*NC+1])
                        lhs=sum((s.kronecker_product(extract(h),jj) for h,jj in zip(H,coeff)),s.zeros(N))
                        rhs=T*sum((s.kronecker_product(extract(-Bfull*b),jj) for b,jj in zip(baseline,coeff)),s.zeros(N))*T
                        ck('actual noncommuting simultaneous coefficient control '+str((grade,sigma,zeta)),not zero(J3) and zero(lhs-rhs))
                else:ck('actual no map has exact witness '+str((grade,sigma,zeta)),why is not None)
                row['source_boson_and_fermion_join']=bool(time_ok and sigma==1 and row['full_printed_match'])
                row['grade']='FULL_SOURCE_MAP' if row['source_boson_and_fermion_join'] else 'PARTIAL_COMPLETION_ONLY' if time_ok and phases is not None else 'NOT_EARNED_IN_THIS_DICTIONARY'
                cases.append(row)
    records['source_census']=cases
    records['source_reading']='Both declared tensor readings, both scalar bar signs/phases; not every convention, physical contour or parent'
    # Actual spinor T, not a scalar on the whole physical state space.
    eta=clean(W[:,:2]*W[:,:2].H+(B*W[:,:2].conjugate())*(B*W[:,:2].conjugate()).H)
    Tphys=clean(I32+(1/t-1)*eta+(t-1)*(MW-eta))
    ck('actual eta full conjugate projector rank4',eta.rank()==4 and zero(eta*eta-eta) and zero(B*eta.conjugate()-eta*B))
    ck('actual T Weyl and full reality',zero(Tphys*MW-MW*Tphys) and zero(B*Tphys.conjugate()-Tphys*B))
    rr=s.kronecker_product(I4,I4,p3);vv=s.kronecker_product(I4,s.I*cs[2]*cs[3],I2)
    laws=[];green=s.I*G0*G[2]
    for ep in (-1,1):
        P=clean(MW*(I32+ep*rr*vv)/2)
        ck('actual T paired plane preserved '+str(ep),zero(Tphys*P-P*Tphys))
        ck('actual transported Green current '+str(ep),zero(P.H*Tphys.H*green*Tphys*P))
        laws.append({'epsilon':ep,'complex_rank':P.rank()})
    minus=clean(MW*(I32-rr*vv)/2)
    ck('actual epsilon minus T is common scalar',zero(Tphys*minus-t*minus))
    gh=s.kronecker_product(I4,s.I*cs[0]*cs[1],I2)
    Pi=clean(MW*(I32+rr*gh)/2*(I32+rr*vv)/2)
    ck('all active BPS tangents have same T scalar',all(zero((Tphys-t*I32)*G0*G[j]*Pi) for j in (2,3,4,5)))
    u2=[cs[0]*cs[1],cs[2]*cs[3],cs[0]*cs[2]+cs[1]*cs[3],cs[0]*cs[3]-cs[1]*cs[2]]
    ck('actual U2 degree and R transition commute',all(zero(Tphys*s.kronecker_product(I4,x,I2)-s.kronecker_product(I4,x,I2)*Tphys) for x in u2) and zero(Tphys*rr-rr*Tphys))
    ck('printed w1 T not a kinetic isometry',not zero((Tphys.H*Tphys-I32).subs(t,1/s.sqrt(2))*MW))
    ck('canonical w2 T identity',zero(Tphys.subs(t,1)-I32))
    # Bounded positive congruence and nonunitary spectrum controls.
    A=s.diag(0,1,3);tt=s.diag(2,s.Rational(1,2),3);Bb=tt*A*tt
    ck('finite positive congruence preserves kernel not masses',Bb.rank()==A.rank() and Bb.nullspace()==A.nullspace() and Bb.eigenvals()!=A.eigenvals())
    records['domain']={'paired_laws':laws,'eta_complex_rank':eta.rank(),
        'T':'t^-1 eta plus t all other MW fields, w=2t^2','scope':'authored selfadjoint fixed-fibre transport ONLY when actual operator congruence and positive time are earned'}
    records['time']={'ordinary_mismatch':witness(times[0]-clock),'graded_matches':zero(times[1]-clock)}
    records['time']['both_actual_action_matrices']=[sparse(a) for a in times]
    records['status']='explicit source component gate and conditional completed-operator transport; not automatic printed action/SUSY/global spectrum or SM acceptance'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(cs,valid):
    result=run(cs,valid);print(json.dumps(result,indent=2));return 0 if result['all_passed'] else 1
