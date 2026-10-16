"""Declared full-parent reality and local interacting trace questions.

Shared authored formulation, not independent analytic or physical acceptance.
No original producer is executed on import.
"""
import importlib.util,json,sys
from itertools import product
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
SIMPLE_DOUBLED=((1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),
 (-2,2,0,0,0,0,0,0),(0,-2,2,0,0,0,0,0),(0,0,-2,2,0,0,0,0),
 (0,0,0,-2,2,0,0,0),(0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0))
def load(path,name,analysis=None):
    old=sys.modules.get('analysis')
    if analysis is not None:sys.modules['analysis']=analysis
    try:
        spec=importlib.util.spec_from_file_location(name,path)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
    finally:
        if analysis is not None:
            if old is None:sys.modules.pop('analysis',None)
            else:sys.modules['analysis']=old
def clean(x):
    if isinstance(x,s.MatrixBase):return x.applyfunc(lambda a:s.simplify(s.expand_complex(a)))
    return s.simplify(s.expand_complex(x))
def zero(x):return all(clean(a)==0 for a in x)
def enc(x):return [[str(clean(a)) for a in row] for row in x.tolist()]
def sparse_add(out,k,v):
    out[k]=out.get(k,0)+v
    if not out[k]:del out[k]

def run(cs,setup_valid,engine):
    checks={}
    def ck(n,v):checks[n]=bool(v)
    I2=s.eye(2);I4=s.eye(4);I16=s.eye(16);I32=s.eye(32)
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    ck('actual Fock input map earned',setup_valid)
    for j,k in product(range(4),repeat=2):
        ck(f'internal Clifford {j},{k}',zero(cs[j]*cs[k]+cs[k]*cs[j]+(2*I4 if j==k else s.zeros(4))))
    gx=clean(-cs[0]*cs[1]*cs[2]*cs[3]);gh=clean(s.I*cs[0]*cs[1]);gv=clean(s.I*cs[2]*cs[3])
    bx=clean(cs[1]*cs[3])
    ck('Euclidean spin reality square minus one',zero(bx*bx.conjugate()+I4))
    for j,c in enumerate(cs):ck('Euclidean spin reality Clifford '+str(j),zero(bx*c.conjugate()-c*bx))
    ck('Euclidean reality flips both plane gradings',zero(bx*gv.conjugate()+gv*bx) and zero(bx*gh.conjugate()+gh*bx))
    ck('Euclidean reality preserves total internal chirality',zero(bx*gx.conjugate()-gx*bx))
    herm=[s.I*c for c in cs];gam=[s.I*herm[0],herm[1],herm[2],herm[3]]
    g5=clean(s.I*s.prod(gam));b4=clean(gam[0]*gam[1]*gam[3])
    ck('Lorentz4 reality square one',zero(b4*b4.conjugate()-I4))
    for j,g in enumerate(gam):ck('Lorentz4 reality Clifford '+str(j),zero(b4*g.conjugate()-g*b4))
    ck('Lorentz4 reality flips external chirality',zero(b4*g5.conjugate()+g5*b4))
    gs=[s.kronecker_product(g,I4,p3) for g in gam]
    gs += [s.kronecker_product(g5,s.I*c,p3) for c in cs]
    gs += [s.kronecker_product(I16,p1),s.kronecker_product(I16,p2)]
    for j,k in product(range(10),repeat=2):
        rhs=2*(-1 if j==0 else 1)*I32 if j==k else s.zeros(32)
        ck(f'Lorentz10 Clifford {j},{k}',zero(gs[j]*gs[k]+gs[k]*gs[j]-rhs))
    chir=clean(s.prod(gs));pm=clean((I32+chir)/2)
    ck('actual ten dimensional Weyl tensor map',zero(chir+s.kronecker_product(g5,gx,p3)))
    ck('ten dimensional Weyl rank16',pm.rank()==16 and zero(pm*pm-pm))
    b10=clean(s.kronecker_product(b4,bx,p2))
    ck('full Majorana reality square one',zero(b10*b10.conjugate()-I32))
    ck('full Majorana antiunitary',zero(b10.H*b10-I32))
    ck('Majorana preserves actual Weyl constraint',zero(b10*pm.conjugate()-pm*b10))
    for j,g in enumerate(gs):
        ck('Majorana kinetic reality '+str(j),zero(b10*(s.I*g).conjugate()-s.I*g*b10))
    for j in range(1,10):
        h=s.I*gs[0]*gs[j]
        ck('Majorana Hamiltonian opposite sign '+str(j),zero(b10*h.conjugate()+h*b10))
    multiplier=-s.kronecker_product(g5,I4,p3)
    for j in range(4):
        ck('actual Euler to normal graph derivative '+str(j),zero(multiplier*s.I*gs[4+j]-s.kronecker_product(I4,cs[j],I2)))
    for j,want in [(8,s.kronecker_product(g5,I4,p2)),(9,-s.kronecker_product(g5,I4,p1))]:
        ck('actual Euler to Higgs graph coefficient '+str(j),zero(multiplier*s.I*gs[j]-want))
        ck('full real Higgs coefficient covariance '+str(j),zero(b10*want.conjugate()-want*b10))
        h=s.I*gs[0]*gs[j]
        ck('compact gauge Higgs Hamiltonian Hermiticity '+str(j),zero(h.H+h))
    rr=s.kronecker_product(I16,p3);vv=s.kronecker_product(I4,gv,I2)
    ck('full reality flips R charge',zero(b10*rr.conjugate()+rr*b10))
    ck('full reality flips normal chirality',zero(b10*vv.conjugate()+vv*b10))
    ck('full reality flips external chirality',zero(b10*s.kronecker_product(g5,I4,I2).conjugate()+s.kronecker_product(g5,I4,I2)*b10))
    spin=clean(cs[0]*cs[1]+cs[2]*cs[3]/2)
    ck('canonical full form transition weights',zero(spin+3*s.I*I4/2-s.diag(0,2*s.I,s.I,3*s.I)))
    transition=s.kronecker_product(I4,spin,I2)+3*s.I*rr/2
    ck('full geometric spin and R transition covariance',zero(b10*transition.conjugate()-transition*b10))
    ck('wrong same R phase fails reality',not zero(b10*(s.kronecker_product(I4,spin,I2)+3*s.I*I32/2).conjugate()-(s.kronecker_product(I4,spin,I2)+3*s.I*I32/2)*b10))
    kappa=s.Symbol('kappa',real=True)
    zeroth=-cs[1]/2+cs[0]*cs[2]*cs[3]/4
    paired=s.kronecker_product(I4,zeroth,I2)+s.I*kappa*s.kronecker_product(I4,cs[0],p3)
    ck('paired full internal differential connection',zero(b10*paired.conjugate()-paired*b10))
    ck('single same-sign canonical block is not full reality',not zero(bx*(zeroth+3*s.I*cs[0]/4).conjugate()-(zeroth+3*s.I*cs[0]/4)*bx))
    current=clean(s.I*gs[0]*gs[6])
    ck('actual Hamiltonian normal Green matrix nondegenerate',current.det()!=0 and zero(current.H+current))
    laws=[]
    for eps in (-1,1):
        P=clean((I32+eps*rr*vv)/2);bad=clean((I32+eps*vv)/2);PW=clean(P*pm)
        ck('real paired trace law '+str(eps),zero(b10*P.conjugate()-P*b10))
        ck('paired trace commutes Weyl '+str(eps),zero(P*pm-pm*P))
        ck('paired trace is half on Weyl '+str(eps),PW.rank()==8 and zero(PW*PW-PW))
        ck('actual parent current cancels '+str(eps),zero(PW.H*current*PW))
        ck('same extreme in both R blocks fails reality '+str(eps),not zero(b10*bad.conjugate()-bad*b10))
        ck('wrong full unconstrained plane has current '+str(eps),not zero(pm.H*current*pm))
        independent=clean(PW*(I32+rr)/2)
        ck('only four independent complex trace components '+str(eps),independent.rank()==4)
        laws.append({'epsilon':eps,'allowed_Weyl_complex_rank':8,'independent_Rplus_complex_rank':4,
                     'Rplus_normal_gamma':eps,'Rminus_normal_gamma':-eps})
    # The canonical block is the source's (bar eta,psi_H,psi_V,bar chi) dictionary.
    names=['bar_eta','psi_H','psi_V','bar_chi'];slots=[]
    for j,name in enumerate(names):
        selector=s.kronecker_product(I4,s.eye(4)[:,j]*s.eye(4)[:,j].T,(I2+p3)/2)*pm
        left=clean(s.kronecker_product((I4+g5)/2,I4,I2)*selector).rank()
        right=clean(s.kronecker_product((I4-g5)/2,I4,I2)*selector).rank()
        expected=(2,0) if j in (1,2) else (0,2)
        ck('actual source form and spacetime slot '+name,(left,right)==expected)
        slots.append({'field':name,'external_left_rank':left,'external_right_rank':right,
                      'vertical_gamma':int(gv[j,j])})

    # Compact E8 conjugation on ALL248, not componentwise conjugation of a 6.
    roots=engine.roots;ix={r:i for i,r in enumerate(roots)};tau=list(range(248));sign=[-1]*8+[1]*240
    for j,r in enumerate(roots):tau[8+j]=8+ix[tuple(-x for x in r)]
    ck('whole240 roots and248 reality map',len(roots)==240 and len(set(roots))==240 and all(tau[tau[j]]==j and sign[j]*sign[tau[j]]==1 for j in range(248)))
    S=s.Matrix.hstack(*(s.Matrix(v)/2 for v in SIMPLE_DOUBLED));cart=s.Matrix(engine.cartan)
    ck('actual E8 simple frame',S.T*S==cart and cart.det()==1)
    ck('compact full coefficient Hermitian metric positive',all(cart[:j,:j].det()>0 for j in range(1,9)))
    e=[s.eye(8)[:,j] for j in range(8)];chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    C=s.Matrix.hstack(*chain);weights=[C*(C.T*C).inv()*s.Matrix([1,0,0,0,0])]
    for a in chain:weights.append(weights[-1]-a)
    hv=sum((v*w for v,w in zip((1,-1)*3,weights)),s.zeros(8,1))
    parity=[0]*8+[int((S*s.Matrix(r)).dot(hv))%2 for r in roots]
    ck('real full136 regular and112 critical coefficient directions',parity.count(0)==136 and parity.count(1)==112 and all(parity[tau[j]]==parity[j] for j in range(248)))
    tensor=[];tau_ok=True;grade_ok=True
    for p,q in product(range(248),repeat=2):
        row=engine.pair(p,q);lhs={tau[k]:sign[k]*v for k,v in row.items() if v}
        rhs={k:sign[p]*sign[q]*v for k,v in engine.pair(tau[p],tau[q]).items() if v}
        tau_ok=tau_ok and lhs==rhs
        grade_ok=grade_ok and all(parity[k]==(parity[p]+parity[q])%2 for k in row)
        if row:tensor.append([p,q,[[k,str(v)] for k,v in sorted(row.items()) if v]])
    ck('full61504 signed compact conjugation bracket identities',tau_ok)
    ck('full61504 actual Z2 bracket grading identities',grade_ok)
    metric=s.MutableSparseMatrix(s.diag(cart,s.eye(240)))
    def adbasis(p):
        values={}
        for q in range(248):
            for k,v in engine.pair(p,q).items():values[k,q]=s.Rational(v)
        return s.MutableSparseMatrix(248,248,values)
    for j in range(8):
        sr=tuple(int(i==j) for i in range(8));up=8+ix[sr];dn=tau[up]
        mats=[s.I*adbasis(j),adbasis(up)+adbasis(dn),s.I*(adbasis(up)-adbasis(dn))]
        for k,m in enumerate(mats):
            residual=m.H*metric+metric*m
            ck('actual compact simple generator skew Hermitian '+str((j,k)),all(clean(v)==0 for v in residual.todok().values()))
    m=adbasis(8+ix[(1,0,0,0,0,0,0,0)])+adbasis(8+ix[(-1,0,0,0,0,0,0,0)])
    wrong=m.H+m
    ck('naive identity coefficient metric rejected',any(clean(v)!=0 for v in wrong.todok().values()))
    simple=(1,0,0,0,0,0,0,0);q=8+ix[simple];row=engine.pair(0,q)
    wrong_lhs={tau[k]:v for k,v in row.items()};wrong_rhs=engine.pair(0,tau[q])
    ck('wrong plus Cartan conjugation rejected',bool(row) and wrong_lhs!=wrong_rhs)
    odd=next(j for j in range(8,248) if parity[j]);op=tau[odd]
    nonzero=engine.pair(odd,op)
    ck('actual odd root and conjugate do not commute',bool(nonzero) and all(k<8 for k in nonzero))
    # X=E+ + E- is compact-real and normal; Y=i(E+ - E-) is also compact-real.
    # [X,Y]=-2i[E+,E-], so the full parent retains a genuine Yukawa action.
    def coefficient_bracket(u,v):
        out={}
        for p,x in u.items():
            for q,y in v.items():
                for k,w in engine.pair(p,q).items():sparse_add(out,k,s.simplify(x*y*w))
        return out
    xx={odd:1,op:1};yy={odd:s.I,op:-s.I}
    ck('normal compact Higgs positive comparator',sign[odd]==sign[op]==1 and not coefficient_bracket(xx,xx))
    ck('nonabelian charged interaction retained',bool(coefficient_bracket(xx,yy)))
    ck('commuting Yukawa channel is retained as positive control',not coefficient_bracket(xx,xx))
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]])
    A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    P13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]);P23=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    X=s.kronecker_product(P13,(I2+a)/s.sqrt(2));Y=s.kronecker_product(P23,(I2+b)/s.sqrt(2));Z=A.H*X
    for name,g in [('a',A),('b',B),('X',X),('Y',Y),('Z',Z)]:
        ck('actual specified lift compact '+name,zero(g.H*g-s.eye(6)) and clean(g.det())==1)
    ck('bare fundamental conjugation is not full E8 reality',not zero(A.conjugate()-A))
    ck('noncompact determinant one is not sufficient',s.diag(2,s.Rational(1,2),1,1,1,1).det()==1 and not zero(s.diag(4,s.Rational(1,4),1,1,1,1)-s.eye(6)))

    # Nonzero normal Higgs: actual leading Euler/graph dressing, not D_V g abuse.
    rad=s.Symbol('r',positive=True);th=s.Symbol('theta',real=True)
    c3=s.kronecker_product(I4,cs[2],I2);c4=s.kronecker_product(I4,cs[3],I2)
    def nd(F):return clean((c3*s.cos(th)+c4*s.sin(th))*F.diff(rad)+(-c3*s.sin(th)+c4*s.cos(th))*F.diff(th)/rad)
    V=(s.kronecker_product(g5,I4,p2)*s.cos(th/2)+s.kronecker_product(g5,I4,p1)*s.sin(th/2))/s.sqrt(rad)
    dress=[]
    for rcharge,gamma in product((-1,1),repeat=2):
        proj=clean(pm*(I32+rcharge*rr)/2*(I32+gamma*vv)/2)
        profile=s.exp(-s.I*gamma*th/2)/s.sqrt(rad)
        source0=s.I*rcharge*s.kronecker_product(g5,I4,p1)*proj
        source=s.exp(-s.I*(rcharge+gamma)*th/2)*source0/rad
        eps=rcharge*gamma;phi=s.log(rad) if eps==1 else s.exp(s.I*gamma*th)
        correction=c3*source0*phi
        ck('actual critical normal solution '+str((rcharge,gamma)),zero(nd(profile*proj)))
        ck('actual full Higgs source '+str((rcharge,gamma)),zero(V*profile*proj-source))
        ck('actual dressed nonintegrable source cancels '+str((rcharge,gamma)),zero(nd(correction)+source))
        ck('dressing keeps actual parent Weyl '+str((rcharge,gamma)),zero(pm*correction-correction))
        target_proj=clean(pm*(I32-rcharge*rr)/2*(I32-gamma*vv)/2)
        target_phi=s.log(rad) if eps==1 else s.exp(-s.I*gamma*th)
        target=c3*(-s.I*rcharge*s.kronecker_product(g5,I4,p1)*target_proj)*target_phi
        ck('dressing commutes full Majorana '+str((rcharge,gamma)),zero(b10*correction.conjugate()-target*b10))
        dress.append({'R':rcharge,'gamma':gamma,'epsilon':eps,'correction_type':'log' if eps==1 else 'bounded_angular'})
    # Actual Wirtinger derivatives, not a premise hidden by treating f as constant.
    f=rad**(-s.Rational(1,2))*s.exp(-s.I*th/2);fb=s.conjugate(f)
    dz=lambda h:clean(s.exp(-s.I*th)*(s.diff(h,rad)-s.I*s.diff(h,th)/rad)/2)
    db=lambda h:clean(s.exp(s.I*th)*(s.diff(h,rad)+s.I*s.diff(h,th)/rad)/2)
    ck('holomorphic Higgs and antiholomorphic normal connection leading equations',db(f)==0 and dz(fb)==0)
    ck('wrong tangential scalar derivative detected',dz(f)!=0 and db(fb)!=0)
    epscut,R=s.symbols('epsilon R',positive=True)
    norm_density=clean(rad*f*fb)
    grad_density=clean(rad*(s.diff(f,rad)*s.conjugate(s.diff(f,rad))+s.diff(f,th)*s.conjugate(s.diff(f,th))/rad**2))
    product_density=clean(rad*(f*fb)**2)
    L2=clean(2*s.pi*s.integrate(norm_density,(rad,epscut,R)))
    energy=clean(2*s.pi*s.integrate(grad_density,(rad,epscut,R)))
    logenergy=clean(2*s.pi*s.integrate(product_density,(rad,epscut,R)))
    ck('actual radial integrals from the profile',norm_density==1 and grad_density==1/(2*rad**2) and product_density==1/rad)
    ck('critical trace finite positive L2',s.limit(L2,epscut,0)==2*s.pi*R)
    ck('scalar supersymmetry partner gradient diverges',s.limit(energy,epscut,0)==s.oo)
    ck('generic root quartic and undressed Yukawa diverge logarithmically',s.limit(logenergy,epscut,0)==s.oo)
    primitive=rad*(s.log(rad)**2-2*s.log(rad)+2)
    ck('dressed residual r minus half log is square integrable',clean(s.diff(primitive,rad)-s.log(rad)**2)==0 and s.limit(primitive,rad,0)==0)
    ck('dressed Green lower terms vanish',s.limit(s.sqrt(rad)*s.log(rad),rad,0)==0 and s.limit(rad*s.log(rad)**2,rad,0)==0)
    normal=s.zeros(2);normal[0,1]=normal[1,0]=1;root=s.Matrix([[0,1],[0,0]])
    ck('normal compact local Higgs moment zero',zero(normal*normal.H-normal.H*normal))
    ck('single root local Higgs moment nonzero',not zero(root*root.H-root.H*root))
    records={'internal_cliffords':[enc(c) for c in cs],'J4_linear':enc(b4),'JX_linear':enc(bx),'J10_linear':enc(b10),
        'Weyl_tensor_sign':-1,'actual_form_slots':slots,'critical_trace_laws':laws,
        'full_E8_roots':[list(r) for r in roots],'tau_permutation':tau,'tau_signs':sign,'coefficient_parities':parity,
        'complete_nonzero_E8_brackets':tensor,'normal_dressing':dress,
        'local_norms':{'critical_L2':'2*pi*(R-epsilon)','scalar_gradient':'pi*(1/epsilon-1/R)',
                       'quartic_or_undressed_Yukawa':'2*pi*log(R/epsilon)'},
        'status':'fermion reality/current and local Higgs-dressed graph controls; NOT a complete interacting global boundary law, index or SM'}
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(cs,setup_valid,engine):
    out=run(cs,setup_valid,engine);print(json.dumps(out,indent=2));return 0 if out['all_passed'] else 1
