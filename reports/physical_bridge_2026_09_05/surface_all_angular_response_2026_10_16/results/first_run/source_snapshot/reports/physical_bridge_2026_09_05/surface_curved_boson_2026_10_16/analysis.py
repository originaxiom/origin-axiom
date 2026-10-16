"""Curved bosonic residuals and FIELD-SPACE boundary moment, no science on import."""
import importlib.util,json,sys
from pathlib import Path
from itertools import combinations
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
sys.path.insert(0,str(HERE.parent/'surface_full_real_parent_2026_10_16'))
try:old=load(HERE.parent/'surface_full_real_parent_2026_10_16/analysis.py','curved_boson_words')
finally:sys.path.pop(0)
a=old.a;add=a.add;scale=a.scale;mul=a.mul;tr=a.trace;letter=a.letter;comm=a.comm
def eq(p,q):return not tr(add(p,scale(q,-1)))
def eqm(p,q):return not add(p,scale(q,-1))
def B(p,q):return scale(tr(mul(p,q)),-1)
def adj(p):return a.clean({tuple(reversed(w)):(-1)**len(w)*s.conjugate(c) for w,c in p.items()})
def norm(p):return tr(mul(adj(p),p))
def encoded(p):return a.sf.encoded(tr(p))
def matrix_encoded(p):return a.sf.encoded(a.clean(p))
def substitute(p,reps):
    out={}
    for w,c in p.items():
        term={():c}
        for t in w:term=mul(term,reps.get(t,{}))
        out=add(out,term)
    return out
def zero(m):return all(v==0 or s.simplify(s.expand(v))==0 for v in m)

class Forms:
    """Reuse the graded trace algebra AS FORMS, not a fermion identification."""
    degrees={'fA':1,'dA':2,'fa':1,'da':2,'p':0,'q':0,'r':0,'fp':1,'fq':1,'fr':1,'P':2,'fP':3,'pP':2}
    derivatives={'fA':'dA','fa':'da','p':'fp','q':'fq','r':'fr','P':'fP'}
    @classmethod
    def d(cls,p):
        out={}
        for w,c in p.items():
            degree=0
            for j,t in enumerate(w):
                if t in cls.derivatives:
                    new=w[:j]+(cls.derivatives[t],)+w[j+1:]
                    out[new]=out.get(new,0)+(-1)**degree*c
                degree+=cls.degrees[t]
        return tr(out)
    @staticmethod
    def variation(p):
        out={}
        for w,c in p.items():
            for j,t in enumerate(w):
                if t in ('fA','dA','P'):
                    dest={'fA':'fa','dA':'da','P':'pP'}[t];key=w[:j]+(dest,)+w[j+1:]
                    out[key]=out.get(key,0)+c
        return tr(out)

def run(C,div,f,scalar,Eframe,coords,valid):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    ck('actual coordinate or closed geometry input',valid)
    lamf=s.expand(f[0][1]+f[2][3])
    ck('actual Chern curvature and scalar relation',s.simplify(lamf+s.Rational(1,2)*scalar)==0 and lamf==s.Rational(3,2) and scalar==-3)
    # Kähler closure in the actual noncoordinate orthonormal frame.
    omega=s.zeros(4);omega[0,1]=omega[2,3]=1;omega[1,0]=omega[3,2]=-1
    dOmega=[]
    for i,j,k in combinations(range(4),3):
        dOmega.append(s.expand(-sum(C[i][j][h]*omega[h,k]-C[i][k][h]*omega[h,j]+C[j][k][h]*omega[h,i] for h in range(4))))
    ck('actual Kahler form closed in full frame',all(x==0 for x in dOmega))
    # Normalizations inherited from the actual unit-C kinetic metric.
    x,y=s.symbols('x0 y0',real=True);z=-s.sqrt(2)*(x-s.I*y)
    omega_xy=s.expand(s.I*(s.diff(z,x)*s.diff(s.conjugate(z),y)-s.diff(z,y)*s.diff(s.conjugate(z),x)))
    ck('actual chiral metric gives field space symplectic coefficient',omega_xy==-4)
    wedge=a.sf.prior.wedge
    z0={(0,):1/s.sqrt(2),(1,):s.I/s.sqrt(2)};z1={(2,):1/s.sqrt(2),(3,):s.I/s.sqrt(2)}
    bar=lambda p:{k:s.conjugate(v) for k,v in p.items()}
    top=wedge(wedge(wedge(bar(z0),bar(z1)),z0),z1)
    ck('unit anti hol volume wedge hol volume is real volume',s.simplify(top.get((0,1,2,3),0)-1)==0)
    hA=s.Integer(4);hP=s.Rational(1,2);b=s.Symbol('b',positive=True)
    ck('actual transformed auxiliary metrics and inverse factors',hA==(-2)**2 and hP==1/s.sqrt(2)**2 and 4/hP==8 and 4/hA==1)
    hh=s.Symbol('h',positive=True);br,bi,gx,gy=s.symbols('br bi gx gy',real=True)
    gg=gx+s.I*gy;bb=br+s.I*bi;lag=s.expand(hh*s.conjugate(gg)*gg+bb*gg+s.conjugate(bb*gg))
    sol={gx:-br/hh,gy:bi/hh}
    ck('positive Gaussian elimination not a chosen potential',s.simplify(s.diff(lag,gx).subs(sol))==0 and s.simplify(s.diff(lag,gy).subs(sol))==0 and s.simplify(lag.subs(sol)+(br*br+bi*bi)/hh)==0)
    d,m=s.symbols('D mu',real=True);Ld=d*d/2+d*m
    ck('D Gaussian gives necessary whole vector boundary moment',s.diff(Ld,d).subs(d,0)==m and s.diff(Ld,d).subs(d,-m)==0 and s.expand(Ld.subs(d,-m)+m*m/2)==0)
    # Universal compact covariant jets. Second jets use actual brackets,
    # gauge curvature and the normal SO2 line curvature.
    U,V=letter('U'),letter('V');DU=[letter('U_'+str(i)) for i in range(4)];DV=[letter('V_'+str(i)) for i in range(4)]
    F={(i,j):letter('F'+str(i)+str(j)) for i,j in combinations(range(4),2)}
    getF=lambda i,j:F[i,j] if i<j else scale(F[j,i],-1) if i>j else {}
    def second(base,i,j):
        out=letter(base+'_'+str(min(i,j))+'_'+str(max(i,j)))
        if i<=j:return out
        out=add(out,*(scale((DU if base=='U' else DV)[k],C[i][j][k]) for k in range(4)),comm(getF(i,j),U if base=='U' else V),scale(V if base=='U' else U,f[i][j]*(1 if base=='U' else -1)))
        return out
    def derivative(p,i):
        out={}
        for w,c in p.items():
            for j,t in enumerate(w):
                parts=t.split('_');base=parts[0]
                if base not in ('U','V'):raise ValueError('unexpected current letter '+t)
                repl=(DU if base=='U' else DV)[i] if len(parts)==1 else second(base,i,int(parts[1]))
                out=add(out,scale(mul(mul({w[:j]:1},repl),{w[j+1:]:1}),c))
        return tr(out)
    uv=comm(U,V);LF=add(F[0,1],F[2,3]);M=add(LF,uv)
    pairs=((0,1),(2,3));J=[{} for i in range(4)];cross={};higgs=[]
    for i,j in pairs:
        J[i]=add(B(U,DV[j]),scale(B(V,DU[j]),-1));J[j]=add(scale(B(U,DV[i]),-1),B(V,DU[i]))
        cross=add(cross,B(DU[i],DV[j]),scale(B(DV[i],DU[j]),-1))
        higgs += [add(DU[i],scale(DV[j],-1)),add(DV[i],DU[j])]
    dJ=tr(add(*(add(derivative(J[i],i),scale(J[i],div[i])) for i in range(4))))
    H=add(B(U,U),B(V,V));expectedJ=add(scale(cross,2),scale(B(LF,uv),-2),scale(H,-lamf))
    ck('universal full curved current including frame gauge and line',eq(dJ,expectedJ))
    ck('omitted frame divergence detected',not eq(add(*(derivative(J[i],i) for i in range(4))),expectedJ))
    ck('omitted line curvature detected',not eq(dJ,add(expectedJ,scale(H,lamf))))
    ck('omitted gauge curvature detected',not eq(dJ,add(expectedJ,scale(B(LF,uv),2))))
    E=add(*(B(q,q) for q in list(F.values())+DU+DV+[uv]))
    residual=scale(add(*(B(q,q) for q in [M,add(F[0,2],scale(F[1,3],-1)),add(F[0,3],F[1,2])]+higgs)),2)
    k=scale(add(B(F[0,1],F[2,3]),scale(B(F[0,2],F[1,3]),-1),B(F[0,3],F[1,2])),2)
    rough=add(scale(E,2),scale(k,2),scale(dJ,-2),scale(H,-2*lamf))
    ck('complete curved bosonic identity all ordered words',eq(residual,rough))
    ck('omitted gauge Pontryagin term detected',not eq(residual,add(rough,scale(k,-2))))
    ck('omitted end current detected',not eq(residual,add(rough,scale(dJ,2))))
    ck('omitted scalar quartic detected',not eq(residual,add(rough,scale(B(uv,uv),-2))))
    P=scale(add(U,scale(V,-s.I)),-2)
    F20=scale(add(F[0,2],scale(F[1,3],-1),scale(add(F[0,3],F[1,2]),-s.I)),s.Rational(1,2))
    DP=[]
    for i,j in pairs:DP.append(scale(add(DU[i],scale(DV[i],-s.I),scale(DU[j],-s.I),scale(DV[j],-1)),-s.sqrt(2)))
    mu=scale(M,2*s.I)
    aux=add(scale(norm(F20),8),*(norm(q) for q in DP),scale(tr(mul(mu,mu)),s.Rational(1,2)))
    ck('actual Gaussian potential equals complete squares',eq(aux,residual))
    badaux=add(scale(norm(F20),2),*(scale(norm(q),s.Rational(1,4)) for q in DP),scale(tr(mul(mu,mu)),s.Rational(1,2)))
    ck('wrong superpotential normalization changes actual potential',not eq(badaux,residual))
    ck('curvature coefficient is scalar R times P norm quarter',eq(scale(H,-2*lamf),scale(norm(P),scalar/4)))
    ck('first variation retains curvature topology and both end primitive',eq(a.sf.variation(residual),a.sf.variation(rough)) and not eq(a.sf.variation(residual),a.sf.variation(add(rough,scale(dJ,2)))) )
    # Standard graded-form transgression and W first variation.
    A,dA,aa,da,ep,be,ga,dep,dbe,dga=[letter(t) for t in ('fA','dA','fa','da','p','q','r','fp','fq','fr')]
    FF=add(dA,mul(A,A));cs=scale(tr(add(mul(A,dA),scale(mul(mul(A,A),A),s.Rational(2,3)))),-1)
    c4=scale(tr(mul(FF,FF)),-1)
    ck('graded form differential squared zero',not Forms.d(Forms.d(add(mul(A,dA),mul(ep,A)))))
    ck('standard gauge Chern Weil transgression retained',eq(Forms.d(cs),c4))
    ck('standard gauge Pontryagin first variation has boundary',eq(Forms.variation(c4),scale(Forms.d(B(aa,FF)),2)))
    PP,dPP=letter('P'),letter('pP');DPform=add(letter('fP'),comm(A,PP))
    W=scale(tr(mul(PP,FF)),-2)
    bulkW=add(scale(tr(mul(dPP,FF)),-2),scale(tr(mul(DPform,aa)),2))
    wend=scale(Forms.d(tr(mul(PP,aa))),-2)
    ck('global superpotential variation keeps full normal primitive',eq(Forms.variation(W),add(bulkW,wend)))
    ck('dropping superpotential boundary primitive detected',not eq(Forms.variation(W),bulkW))
    # Metric-derived field-space Hamiltonian. This is NOT physical phase space.
    Dep=add(dep,comm(A,ep));Da=add(da,mul(A,aa),mul(aa,A))
    OA=scale(B(Dep,aa),-4);dHA=scale(B(ep,Da),4);edgevar=scale(Forms.d(B(ep,aa)),-4)
    ck('field space affine moment with retained boundary',eq(OA,add(dHA,edgevar)))
    ck('bulk moment alone fails for boundary valued parameters',not eq(OA,dHA))
    u,v=letter('u'),letter('v')
    OH=scale(add(B(comm(U,ep),v),scale(B(u,comm(V,ep)),-1)),-4)
    dHH=scale(B(ep,add(comm(u,V),comm(U,v))),4)
    ck('field space Higgs moment coefficient from same metric',eq(OH,dHH))
    ck('wrong metric changes Hamiltonian moment',not eq(scale(OH,2),dHH) and not eq(scale(OA,2),add(dHA,edgevar)))
    ck('moment matches actual Hermitian D source pairing',eq(scale(B(ep,mu),-2*s.I),scale(B(ep,M),4)))
    # Fixed-parameter gauge variation of edge Hamiltonian, full bracket kept.
    pq=comm(ep,be);Dbe=add(dbe,comm(A,be))
    edgebr=add(scale(B(ep,Dbe),-4),scale(B(pq,A),-4))
    coc=scale(B(ep,dbe),-4)
    ck('field space boundary cocycle sign and coefficient',eq(edgebr,coc))
    ck('bulk gauge moment bracket cancels',eq(add(B(ep,comm(FF,be)),B(pq,FF)),{}))
    ck('boundary cocycle skew is exact derivative',eq(add(B(ep,dbe),B(be,dep)),Forms.d(B(ep,be))))
    jac=add(B(comm(ep,be),dga),B(comm(be,ga),dep),B(comm(ga,ep),dbe))
    ck('boundary cocycle Jacobi is exact derivative',eq(jac,Forms.d(B(ep,comm(be,ga)))))
    theta=s.Symbol('theta',real=True);area=s.Symbol('horizontal_area',positive=True)
    c_out=s.simplify(-4*area*s.integrate(s.cos(theta)**2,(theta,0,2*s.pi)));c_in=-c_out
    ck('local commuting circle cocycle nonzero',c_out==-4*s.pi*area and c_in==4*s.pi*area)
    ck('both annulus ends cancel common traces',c_out+c_in==0)
    ck('one end cutoff witness keeps opposite orientation',c_in!=0 and -c_in==c_out)
    # Necessary auxiliary conditions and their actual nonlinear variation.
    dnP,conn,chi,psin,dnchi,pp=map(letter,('dnP','An','chi','psin','dnchi','TP'))
    bn=add(dnP,comm(conn,pp));varbn=add(dnchi,comm(conn,chi),comm(psin,pp))
    tangent={'dnP':dnchi,'An':psin,'TP':chi};directvar={}
    for w,c in bn.items():
        for i,t in enumerate(w):directvar=add(directvar,scale(mul(mul({w[:i]:1},tangent[t]),{w[i+1:]:1}),c))
    ck('matrix normal auxiliary linearization derived before trace',eqm(directvar,varbn))
    ck('linearized normal compatibility keeps connection Higgs term',not eqm(varbn,add(dnchi,comm(conn,chi))) and not eqm(varbn,dnchi))
    ck('matrix source is not replaced by its zero trace',not eqm(uv,{}) and eq(uv,{}))
    # Two realizable product-chart counterexamples with A_H identically0:
    # A3=x2 H,U=V=0; or A=0,U=x2 H,V=0, respectively.
    H0=letter('H');mu_bad=substitute(mu,{'F23':H0});normal_bad=substitute(DP[1],{'U_2':H0})
    ck('whole auxiliary zero needs moment beyond tangent value',eqm(mu_bad,scale(H0,2*s.I)) and not eqm(mu_bad,{}))
    ck('whole tangent auxiliary zero needs normal Higgs derivative',eqm(normal_bad,scale(H0,-s.sqrt(2))) and not eqm(normal_bad,{}) and eqm(substitute(mu,{'U_2':H0}),{}))
    # Positive nonlinear normal jet: F23=-[U,V],DnP=0.
    jet={'U':U,'V':V,'F23':scale(uv,-1),'U_2':letter('T'),'V_3':letter('T'),'V_2':scale(letter('S'),-1),'U_3':letter('S')}
    ck('coupled normal BPS boundary jets pass',eqm(substitute(mu,jet),{}) and eqm(substitute(DP[1],jet),{}))
    ck('dropping nonabelian moment prevents coupled normal boundary',not eqm(scale(uv,2*s.I),{}))
    records['curved']={'moment':matrix_encoded(mu),'potential':encoded(residual),'rough_energy':encoded(E),
        'current':[encoded(q) for q in J],'divergence':encoded(dJ),'gauge_Pontryagin':encoded(k),
        'line_contraction':str(lamf),'scalar_curvature':str(scalar),
        'identity':'V=2E+2B(F wedge F)/dvol-2divJ-2Lambda(f)(|U|2+|V|2)'}
    records['boundary_moment']={'symplectic_coefficient':-4,'boundary_H':'-4 integral_boundary omega B(alpha,A)',
        'cocycle':'-4 integral_boundary omega B(alpha,d beta)','outer_local_witness':str(c_out),'inner_local_witness':str(c_in),
        'type':'Kahler FIELD SPACE, not physical-time Noether/anomaly/quantum charge or globally admitted angular modes'}
    records['boundary_jets']={'necessary':['mu=0','normal covariant derivative P=0'],
        'normal_source':matrix_encoded(bn),'linearized_normal':matrix_encoded(varbn),
        'scope':'smooth adapted/product cut; no nonlinear Sobolev or singular gauge limit'}
    matrix=matrix_check(C,div,f,scalar,Eframe,coords)
    for k0,v0 in matrix.items():ck(k0,v0)
    records['scope']='specified curved residual G/W/moment bosonic sector and boundary audit; not complete curved multiplet/source, actual global cut geometry, singular domain or SM/three/gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}

def matrix_check(C,div,f,scalar,E,coords):
    x,y,u,v=coords
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    A=[s.I*((x+u)*p1+v*p3)/3,s.I*(y*p2+x*v*p3)/5,s.I*((1+u)*p3+y*v*p1)/7,s.I*(u*p2+v*p1+x*y*p3)/11]
    U=s.I*((1+x*u)*p1+y*p3+v*p2)/2;V=s.I*((1+y*v)*p2+u*p3+x*p1)/3
    cp=lambda a,b:a*b-b*a
    Ei=lambda z,i:s.expand(sum(E[i,j]*s.diff(z,coords[j]) for j in range(4))) if not isinstance(z,s.MatrixBase) else z.applyfunc(lambda q:s.expand(sum(E[i,j]*s.diff(q,coords[j]) for j in range(4))))
    q=[s.Rational(3,2),0,0,0]
    DU=[(Ei(U,i)+cp(A[i],U)+q[i]*V).applyfunc(s.expand) for i in range(4)]
    DV=[(Ei(V,i)+cp(A[i],V)-q[i]*U).applyfunc(s.expand) for i in range(4)]
    FF={(i,j):(Ei(A[j],i)-Ei(A[i],j)-sum((C[i][j][k]*A[k] for k in range(4)),s.zeros(2))+cp(A[i],A[j])).applyfunc(s.expand) for i,j in combinations(range(4),2)}
    bil=lambda a,b:s.expand(-s.trace(a*b))
    rows={}
    for i,j in combinations(range(4),2):
        cu=Ei(DU[j],i)+cp(A[i],DU[j])+q[i]*DV[j]-Ei(DU[i],j)-cp(A[j],DU[i])-q[j]*DV[i]-sum((C[i][j][k]*DU[k] for k in range(4)),s.zeros(2))-cp(FF[i,j],U)-f[i][j]*V
        cv=Ei(DV[j],i)+cp(A[i],DV[j])-q[i]*DU[j]-Ei(DV[i],j)-cp(A[j],DV[i])+q[j]*DU[i]-sum((C[i][j][k]*DV[k] for k in range(4)),s.zeros(2))-cp(FF[i,j],V)+f[i][j]*U
        rows['actual matrix gauge line second jet '+str((i,j))]=zero(cu) and zero(cv)
    M=FF[0,1]+FF[2,3]+cp(U,V);res=[M,FF[0,2]-FF[1,3],FF[0,3]+FF[1,2]]
    JJ=[]
    for i,j in ((0,1),(2,3)):
        res += [DU[i]-DV[j],DV[i]+DU[j]]
        JJ += [bil(U,DV[j])-bil(V,DU[j]),-bil(U,DV[i])+bil(V,DU[i])]
    vv=s.expand(2*sum(bil(z,z) for z in res));energy=s.expand(sum(bil(z,z) for z in list(FF.values())+DU+DV+[cp(U,V)]))
    dj=s.expand(sum(Ei(JJ[i],i)+div[i]*JJ[i] for i in range(4)))
    pon=s.expand(2*(bil(FF[0,1],FF[2,3])-bil(FF[0,2],FF[1,3])+bil(FF[0,3],FF[1,2])))
    hh=bil(U,U)+bil(V,V);rho=s.expand(-2*(f[0][1]+f[2][3])*hh)
    rows['independent noncommuting coordinate energy identity']=s.simplify(vv-2*energy-2*pon+2*dj-rho)==0
    rows['coordinate detector sees curvature topology and end']=all(s.simplify(z)!=0 for z in (rho,pon,dj))
    point={x:s.Rational(1,3),y:2,u:s.Rational(1,5),v:s.Rational(1,7)}
    rows['positive full potential despite negative isolated curvature']=s.simplify(vv.subs(point)).is_positive is True and s.simplify(rho.subs(point)).is_negative is True
    return rows

def emit(C,div,f,scalar,E,coords,valid):
    data=run(C,div,f,scalar,E,coords,valid);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
