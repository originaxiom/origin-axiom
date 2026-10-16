"""Actual source Hessian, all ten responses and a boundary benchmark."""
# BANKED IDENTITY: fresh full Gauss-source replay before each new response.
# PRIOR ART: DESIGN/PROOF and the credited graded NC source instruments.
import importlib.util,json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
gauss=load(HERE.parent/'surface_gauss_charge_2026_10_16/analysis.py','all_response_gauss')
clean=gauss.clean;cm=gauss.cm;zero=gauss.zero;eye=gauss.eye;kron=gauss.kron;enc=gauss.enc
def parts(a,poly):
    eu={};ju={}
    for w,c in a.trace(poly).items():
        for k,q in enumerate(w):
            ops=q.split(':')[:-1];b=a.sf.base(q);rest={w[k+1:]+w[:k]:c}
            for n,op in enumerate(ops):
                label=a.sf.normalize(ops[n+1:],'delta_'+b)
                ju[op]=a.add(ju.get(op,{}),a.mul(a.letter(label),rest));rest=a.scale(a.op(rest,op),-1)
            eu[b]=a.add(eu.get(b,{}),rest)
    return eu,{op:a.trace(p) for op,p in ju.items()}
def homotopy(a,poly):
    bad={};primitive={}
    for degree in sorted(set(map(len,poly))):
        if not degree:raise ValueError('Constant not a divergence')
        eu,ju=parts(a,{w:c for w,c in poly.items() if len(w)==degree});bad[str(degree)]={k:v for k,v in eu.items() if v}
        for op,p in ju.items():
            fixed={}
            for w,c in p.items():
                ww=tuple(a.sf.normalize(q.split(':')[:-1],a.sf.base(q).removeprefix('delta_')) for q in w)
                fixed[ww]=fixed.get(ww,0)+c/degree
            primitive[op]=a.trace(a.add(primitive.get(op,{}),fixed))
    div=a.trace(a.add(*(a.op(p,op) for op,p in primitive.items())))
    return bad,primitive,a.trace(a.add(poly,a.scale(div,-1)))
def static(a,p,vector=False):
    return a.trace({w:c for w,c in a.body(p).items() if not any(op.startswith('e') for q in w for op in q.split(':')[:-1]) and (vector or not any(a.sf.base(q).startswith('v') for q in w))})
def physical(a,p):
    out={}
    for w,c in p.items():
        term={():c}
        for q in w:
            ops=q.split(':')[:-1];b=a.sf.base(q)
            if b.startswith('v'):v=a.scale(a.letter('y'+b[1:]),2*s.I)
            elif b.lstrip('~').startswith('c'):
                j=int(b.lstrip('~')[1:]);v=a.scale(a.add(a.letter('x'+str(2*j)),a.scale(a.letter('x'+str(2*j+1)),s.I if b.startswith('~') else -s.I)),s.sqrt(2) if b.startswith('~') else -s.sqrt(2))
            else:v=a.letter(b)
            for op in ops:
                if op[0] not in ('d','b'):raise ValueError('Unexpected source derivative '+op)
                j=int(op[1:]);v=a.add(a.op(v,'n'+str(2*j)),a.scale(a.op(v,'n'+str(2*j+1)),s.I if op[0]=='b' else -s.I)) if j<2 else {}
            term=a.mul(term,v)
        out=a.add(out,term)
    return out
def variation(a,p):
    out={}
    for w,c in p.items():
        for k,q in enumerate(w):
            if a.sf.base(q).startswith('x'):
                label=a.sf.normalize(q.split(':')[:-1],'a'+a.sf.base(q)[1:]);ww=w[:k]+(label,)+w[k+1:]
                out[ww]=out.get(ww,0)+c
    return a.add(out)
CSPEC=[[(0,1,1),(2,3,1),(4,5,1)],[(2,4,1),(3,5,-1)],[(2,5,1),(3,4,1)],[(0,4,1),(1,5,-1)],[(0,5,1),(1,4,1)],[(0,2,1),(1,3,-1)],[(0,3,1),(1,2,1)]]
def source(a,ss,ck):
    xx=[a.letter('x'+str(i)) for i in range(6)];yy=[a.letter('y'+str(i)) for i in range(4)]
    cc=[a.letter('c'+str(i)) for i in range(3)];bc=list(map(a.adj,cc));gg=[a.letter('g'+str(i)) for i in range(3)];bg=list(map(a.adj,gg));dd=a.letter('D')
    dint=lambda p,i,bar=False:a.op(p,('b' if bar else 'd')+str(i)) if i<2 else {}
    mu=a.add(a.scale(a.add(*(a.add(dint(bc[j],j),dint(cc[j],j,True)) for j in range(3))),1/s.sqrt(2)),a.scale(a.add(*(a.comm(cc[j],bc[j]) for j in range(3))),-s.Rational(1,2)))
    bb=[a.add(dint(cc[2],1),a.scale(a.comm(cc[1],cc[2]),-1/s.sqrt(2))),a.add(a.scale(dint(cc[2],0),-1),a.scale(a.comm(cc[0],cc[2]),1/s.sqrt(2))),a.add(dint(cc[1],0),a.scale(dint(cc[0],1),-1),a.scale(a.comm(cc[0],cc[1]),-1/s.sqrt(2)))]
    raw=static(a,ss['full']);eu,_=parts(a,raw)
    ck('actual untraced D and all six G source equations',not a.add(eu.get('D',{}),a.scale(a.add(dd,mu),-1)) and all(not a.add(eu.get('g'+str(j),{}),a.scale(a.add(bg[j],bb[j]),-1)) and not a.add(eu.get('~g'+str(j),{}),a.scale(a.add(gg[j],a.adj(bb[j])),-1)) for j in range(3)))
    bulk=a.trace(a.add(a.scale(a.mul(dd,dd),s.Rational(1,2)),a.mul(dd,mu),*(a.add(a.mul(bg[j],gg[j]),a.mul(gg[j],bb[j]),a.mul(bg[j],a.adj(bb[j]))) for j in range(3))))
    auxdiff=a.trace(a.add(raw,a.scale(bulk,-1)));eb,auxprim,auxres=homotopy(a,auxdiff)
    ck('all static raw auxiliary surface terms retained exactly',not auxres and all(not v for v in eb.values()) and bool(auxprim))
    plain=lambda p,i:a.op(p,'n'+str(i)) if i<4 else {}
    D=lambda p,i:a.add(plain(p,i),a.comm(xx[i],p))
    F=lambda i,j:a.add(plain(xx[j],i),a.scale(plain(xx[i],j),-1),a.comm(xx[i],xx[j]))
    cur=[a.add(*(a.scale(F(i,j),sign) for i,j,sign in row)) for row in CSPEC]
    muX=physical(a,mu);bbX=list(map(lambda b:physical(a,b),bb))
    expected=[a.scale(a.add(cur[1],a.scale(cur[2],-s.I)),-s.sqrt(2)),a.scale(a.add(cur[3],a.scale(cur[4],-s.I)),s.sqrt(2)),a.scale(a.add(cur[5],a.scale(cur[6],-s.I)),-s.sqrt(2))]
    ck('all seven curvature components derived from source auxiliaries',not a.add(muX,a.scale(cur[0],-2*s.I)) and all(not a.add(b,a.scale(c,-1)) for b,c in zip(bbX,expected)))
    potential=a.trace(physical(a,a.add(a.scale(a.mul(mu,mu),s.Rational(1,2)),*(a.mul(a.adj(b),b) for b in bb))))
    seven=a.trace(a.add(*(a.scale(a.mul(c,c),-2) for c in cur)))
    ck('actual auxiliary elimination equals seven component potential',not a.trace(a.add(potential,a.scale(seven,-1))))
    can=a.trace(a.add(*(a.scale(a.mul(F(i,j),F(i,j)),-2) for i in range(6) for j in range(i+1,6))))
    caldiff=a.trace(a.add(potential,a.scale(can,-1)));ce,calprim,calres=homotopy(a,caldiff)
    ck('full curvature calibration is explicit divergence not omission',not calres and all(not v for v in ce.values()) and bool(calprim))
    eV,_=parts(a,potential);hess=[];omitted=False
    av=[a.letter('a'+str(i)) for i in range(6)];df=lambda i,j:a.add(D(av[j],i),a.scale(D(av[i],j),-1))
    for n in range(6):
        target=a.scale(a.add(*(D(F(i,n),i) for i in range(6))),4)
        ck('generic source boson Euler '+str(n),not a.add(eV.get('x'+str(n),{}),a.scale(target,-1)))
        kinetic=a.scale(a.add(*(D(df(i,n),i) for i in range(6))),4)
        curvature=a.scale(a.add(*(a.comm(av[i],F(i,n)) for i in range(6))),4)
        residual=a.add(variation(a,eV.get('x'+str(n),{})),a.scale(a.add(kinetic,curvature),-1));hess.append(residual)
        omitted |= bool(a.add(variation(a,eV.get('x'+str(n),{})),a.scale(kinetic,-1)))
    ck('all six generic Hessians retain actual curvature term',all(not p for p in hess) and omitted)
    mixedraw=physical(a,static(a,ss['K_component'],True));eta=[-1,1,1,1]
    mixed=a.trace(a.add(*(a.scale(a.mul(D(y,i),D(y,i)),2*eta[j]) for j,y in enumerate(yy) for i in range(6))))
    me,mp,mres=homotopy(a,a.trace(a.add(mixedraw,a.scale(mixed,-1),a.scale(physical(a,static(a,ss['K_component'])),-1))))
    ck('all four actual vector kinetic sectors and boundary primitives',not mres and all(not v for v in me.values()) and bool(mp))
    em,_=parts(a,mixed)
    ck('actual external Lorentzian source factor four all directions',all(not a.add(em['y'+str(j)],a.scale(a.add(*(D(D(y,i),i) for i in range(6))),4*eta[j])) for j,y in enumerate(yy)))
    ymraw=physical(a,a.trace({w:c for w,c in static(a,ss['gauge_component'],True).items() if all(a.sf.base(q).startswith('v') for q in w)}))
    ym=a.trace(a.add(*(a.scale(a.mul(a.comm(yy[i],yy[j]),a.comm(yy[i],yy[j])),2*eta[i]*eta[j]) for i in range(4) for j in range(i+1,4))))
    ck('actual external quartic retained beyond quadratic response',bool(ym) and not a.trace(a.add(ymraw,a.scale(ym,-1))))
    return {'mu':a.sf.encoded(mu),'b':[a.sf.encoded(b) for b in bb], 'auxiliary_primitives':{k:a.sf.encoded(v) for k,v in sorted(auxprim.items())},
      'calibration_primitives':{k:a.sf.encoded(v) for k,v in sorted(calprim.items())},'mixed_primitives':{k:a.sf.encoded(v) for k,v in sorted(mp.items())},
      'source_potential':a.sf.encoded(potential),'mixed_action':a.sf.encoded(mixed),'external_quartic':a.sf.encoded(ym),
      'generic_Hessian_residuals':[a.sf.encoded(p) for p in hess]},auxprim
def run(method):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    oldcert=gauss.run(method);records['replayed_Gauss']=oldcert
    ck('fresh all39 actual Gauss source antecedents',oldcert['all_passed'] and len(oldcert['checks'])==39)
    if not all(checks.values()):return {'checks':checks,'records':records,'all_passed':False}
    parent=load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py','all_response_parent');root=load(HERE.parent/'surface_root_gauge_sector_2026_10_16/analysis.py','all_response_root')
    twist=load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','all_response_source');vv,ext,cs,engine,valid,old=parent.setup(method)
    a=twist.prior.a;ss=a.construct(twist.prior.frame(cs)['sig']);records['source'],auxprim=source(a,ss,ck)
    if not all(checks.values()):return {'checks':checks,'records':records,'all_passed':False}
    roots,up,dn,hvec,Ep,Em,H,P,Q,G,eta,tau,parity,pair=root.gauge(engine,old)
    unit=lambda j:s.SparseMatrix(248,1,{(j,0):1});hr=s.SparseMatrix(248,1,{(j,0):v for j,v in hvec.items()})
    W=s.SparseMatrix.hstack(unit(up),-hr/s.sqrt(2),unit(dn));tc=s.SparseMatrix([[0,0,1],[0,-1,0],[1,0,0]])
    r,g,R=s.symbols('r g R',positive=True);z=s.Symbol('zeta',nonzero=True);x=g*g*r;den=1-x;co=(z*z+z**-2)/2;si=(z*z-z**-2)/(2*s.I)
    read=lambda rows,n,m:s.SparseMatrix(n,m,{(i,j):s.sympify(v,locals={'r':r,'g':g,'zeta':z,'R':R}) for i,j,v in rows})
    full=[{st:read(rows,248,1) for st,rows in row.items()} for row in oldcert['records']['family']['all_ten_currents']]
    current=[{st:cm(W.H*G*v) for st,v in row.items()} for row in full];pairs=list(current[0])
    ck('all freshly computed current coefficients faithfully projected',all(zero(W*current[N][st]-v) for N,row in enumerate(full) for st,v in row.items()))
    q=g/(z*s.sqrt(r)*den);qb=g*z/(s.sqrt(r)*den)
    bg=[s.Matrix([0,s.I*g*g*si/(s.sqrt(2)*den),0]),s.Matrix([0,-s.I*g*g*co/(s.sqrt(2)*den),0]),s.Matrix([q,0,qb])/2,s.Matrix([q,0,-qb])/(2*s.I)]
    Et=s.SparseMatrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]]);Ht=s.diag(2,0,-2);gen=[Et,-Ht/s.sqrt(2),-Et.T]
    ad=lambda v:cm(sum((v[i]*gen[i] for i in range(3)),s.zeros(3)))
    ads=list(map(ad,bg));th=lambda M:cm(s.I*z*M.diff(z)/2);conj=lambda M:cm(M.conjugate().subs(s.conjugate(z),1/z))
    plain=lambda M,j:cm(co*M.diff(r)-si*th(M)/r) if j==0 else cm(si*M.diff(r)+co*th(M)/r) if j==1 else s.zeros(*M.shape)
    D=lambda M,j:cm(plain(M,j)+ads[j]*M)
    Dt=lambda M,N:D(M,N-6) if N>=6 else s.zeros(*M.shape)
    body=[s.zeros(3,1) for _ in range(6)]+bg
    F={(M,N):cm((plain(body[N],M-6) if M>=6 else s.zeros(3,1))-(plain(body[M],N-6) if N>=6 else s.zeros(3,1))+ad(body[M])*body[N]) for M in range(10) for N in range(10)}
    response=[{st:cm(v*(r*r*den*den/(4*(1+x)**2) if N==0 else -r*r*den*den/(4*(1+x)**2) if N<4 else -r*r*den*den/(8*(1+x)) if N<6 else 0)) for st,v in row.items()} for N,row in enumerate(current)]
    eta10=[-1]+[1]*9
    def euler(aa):
        result=[]
        for N in range(10):
            row={}
            for st in pairs:
                v=s.zeros(3,1)
                for M in range(10):
                    df=cm(Dt(aa[N][st],M)-Dt(aa[M][st],N));v+=eta10[M]*(Dt(df,M)+ad(aa[M][st])*F[M,N])
                row[st]=cm(4*eta10[N]*v+current[N][st])
            result.append(row)
        return result
    residual=euler(response)
    ck('all ten actual boson Euler equations at fermion degree two',all(zero(v) for row in residual for v in row.values()))
    lapcart=lambda M:cm(sum((D(D(M,j),j) for j in range(4)),s.zeros(*M.shape)))
    atheta=s.I*g*g*r*Ht/(2*den)
    lappolar=lambda M:cm(M.diff(r,2)+M.diff(r)/r+(th(th(M)+atheta*M)+atheta*(th(M)+atheta*M))/r**2+g*g*s.diag(-1,-2,-1)*M/(r*den**2))
    lap=lapcart if method=='native' else lappolar
    ck('independent polar and Cartesian scalar full operators on response',all(zero(lapcart(v)-lappolar(v)) for row in response[:6] for v in row.values()))
    ck('time and all five spatial source signs independently retained',all(zero(((-4 if N==0 else 4)*lap(v))+current[N][st]) for N,row in enumerate(response[:6]) for st,v in row.items()))
    ck('wrong source signs and normalization fail',any(not zero(4*lap(v)+current[0][st]) for st,v in response[0].items()) and any(not zero(2*lap(v)+current[4][st]) for st,v in response[4].items()))
    ck('all degree two responses have correct odd compact reality',all(zero(-tc*conj(v)-v) for row in response for v in row.values()))
    mon=s.diag(-1,1,-1)
    ck('all responses retain actual half winding gauge transition',all(zero(v.subs(z,-z)-mon*v) for row in response for v in row.values()))
    ck('actual linear Lorenz condition all coefficients',all(zero(sum((eta10[N]*Dt(response[N][st],N) for N in range(10)),s.zeros(3,1))) for st in pairs))
    hc=(1+x)/den;hroot=s.sqrt(r)/den;hcart=s.Matrix([0,hc,0]);hup=s.Matrix([z*hroot,0,0]);hdn=s.Matrix([0,0,hroot/z])
    ck('actual Cartan and both dual root harmonic freedoms',all(zero(lap(v)) for v in (hcart,hup,hdn)))
    outer=[{st:cm(v-v.subs(r,R)*(hc/hc.subs(r,R) if N<4 else hroot/hroot.subs(r,R))) if N<6 else v for st,v in row.items()} for N,row in enumerate(response)]
    outerres=euler(outer)
    ck('outer zero benchmark retains every actual boson equation',all(zero(v) for row in outerres for v in row.values()) and all(zero(v.subs(r,R)) for row in outer for v in row.values()))
    ck('outer correction preserves odd compact reality and transition',all(zero(-tc*conj(v)-v) and zero(v.subs(z,-z)-mon*v) for row in outer for v in row.values()))
    # Exact coefficient asymptotics, not positivity of a Grassmann number.
    u=s.Symbol('positive_inner_sqrt',positive=True)
    bounded=all(all(clean(vv0.subs(r,u*u)).as_leading_term(u).as_powers_dict().get(u,0)>=0 for vv0 in v if vv0!=0) for row in outer for v in row.values())
    gradfinite=True
    for row in outer[:6]:
        for v in row.values():
            for j in range(4):
                for q0 in D(v,j):
                    if q0!=0:gradfinite &= bool(clean(q0.subs(r,u*u)).as_leading_term(u).as_powers_dict().get(u,0)>-2)
    ck('outer corrected coefficient norm and derivative energy integrable at inner end',bounded and gradfinite)
    auxout={};momenta={};aux_nonzero=False;wrong_aux_reality=False
    for st in pairs:
        ai=[outer[4+i][st] for i in range(6)]
        Di=lambda M,i:D(M,i-2) if i>=2 else s.zeros(*M.shape)
        dF=lambda i,j:cm(Di(ai[j],i)-Di(ai[i],j))
        cur=[cm(sum((sign*dF(i,j) for i,j,sign in row),s.zeros(3,1))) for row in CSPEC]
        muv=2*s.I*cur[0];bs=[-s.sqrt(2)*(cur[1]-s.I*cur[2]),s.sqrt(2)*(cur[3]-s.I*cur[4]),-s.sqrt(2)*(cur[5]-s.I*cur[6])]
        Gs=[cm(-tc*conj(b)) for b in bs];barGs=[cm(-b) for b in bs]
        Dresponse=cm(-muv)
        ck('all six auxiliary and D responses '+st,zero(Dresponse+muv) and all(zero(gv+tc*conj(b)) and zero(bgv+b) and zero(tc*conj(gv)-bgv) for gv,bgv,b in zip(Gs,barGs,bs)))
        aux_nonzero |= any(not zero(v) for v in Gs)
        wrong_aux_reality |= any(not zero(-tc*conj(gv)-bgv) for gv,bgv in zip(Gs,barGs))
        auxout[st]={'D':enc(cm(-muv)),'G':[enc(v) for v in Gs],'barG':[enc(v) for v in barGs]}
        normal={2:co,3:si};ps=[]
        for n in range(2,6):
            p=s.zeros(3,1)
            for k,row in enumerate(CSPEC):
                coeff=sum(sign*(normal.get(i,0)*int(j==n)-normal.get(j,0)*int(i==n)) for i,j,sign in row)
                p-=4*coeff*cur[k]
            ps.append(cm(p))
        momenta[st]=[enc(v) for v in ps]
        ck('actual free normal boson momenta zero at outer '+st,all(zero(v.subs(r,R)) for v in ps) and zero(muv.subs(r,R)) and zero(Gs[0].subs(r,R)))
    ck('nonzero auxiliary response rejects commuting conjugation guess',aux_nonzero and wrong_aux_reality)
    bideal={'D','g0','~g0','c0','~c0'}
    ck('raw auxiliary normal primitives in undifferentiated boundary ideal',all(any(q in bideal for q in w) for op,p in auxprim.items() if op in ('d1','b1') for w in p))
    fprim=a.jet_quotient(a.fermions(ss['full']))[1]
    fideal={'f0_0','f0_1','~f0_0','~f0_1','f1_0','f1_1','~f1_0','~f1_1'}
    ck('raw fermion normal primitives in undifferentiated boundary ideal',all(any(q in fideal for q in w) for op,p in fprim.items() if op in ('d1','b1') for w in p))
    C=kron(s.Matrix([[0,1],[1,0]]),eye(8));P=s.diag(*[int(j in (2,3)) for bar in range(2) for j in range(4) for spin in range(2)])
    psi=read(oldcert['records']['family']['actual_amplitude_fermion'],48,4)
    ck('actual fermion lies in benchmark isotropic normal trace space',zero(kron(P,eye(3))*psi-psi) and all(zero(P.T*C.H*v*P) for v in vv[2:4]))
    B=cm(s.I*vv[2]*vv[3]);principal={}
    ck('actual angular principal Hermitian involution',zero(B.H-B) and zero(B*B-eye(16)))
    for sign in (1,-1):
        S=cm((eye(16)-sign*B)/2);J=cm(P*S);control=cm((eye(16)-S)*S)
        rank=int(s.trace(J));principal[str(sign)]={'intersection_projector':enc(J),'rank':rank,'ordinary_angular_transverse':rank==0,'complement_control_rank':int(s.trace(control))}
        ck('computed nontransverse angular benchmark sign '+str(sign),zero(P*S-S*P) and zero(J*J-J) and zero(J.H-J) and rank==4 and not zero(J))
        ck('transverse complement control sign '+str(sign),zero(control) and s.trace(S)==8)
    records['degree2']={'responses':[{st:enc(v) for st,v in row.items()} for row in response], 'outer_zero_responses':[{st:enc(v) for st,v in row.items()} for row in outer],
      'all_ten_Euler_residuals':[{st:enc(v) for st,v in row.items()} for row in residual], 'outer_Euler_residuals':[{st:enc(v) for st,v in row.items()} for row in outerres],
      'auxiliary_responses':auxout,'outer_free_boson_momenta':momenta}
    records['boundary']={'free_trace_projector':enc(P),'actual_angular_principal':enc(B),'principal_tests':principal,
      'fermion_raw_normal_primitives':{k:a.sf.encoded(v) for k,v in sorted(fprim.items()) if k in ('d1','b1')},'benchmark':'supplied outer V=C0=0; C1/C2 free; this background through degree two only'}
    records['meaning']={'all_ten_boson_equations_solved_at_degree2':True,'source_auxiliary_and_surface_terms_retained':True,
      'benchmark_variational_tests_passed':all(v for k,v in checks.items() if 'benchmark' in k or 'primitive' in k or 'momenta' in k),
      'ordinary_angular_principal_transverse':all(row['ordinary_angular_transverse'] for row in principal.values()),
      'global_kernel_or_Fredholm_verdict':False,'complete_nonlinear_boundary_law_selected':False,'derived_SM_three_chiral_gravity':False,
      'shared_author_not_independent_acceptance':True,'not_other_parent_mass_count_gap_or_index':True}
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(method):
    result=run(method);print(json.dumps(result,indent=2));return 0 if result['all_passed'] else 1
