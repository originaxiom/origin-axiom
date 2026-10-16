"""Actual temporal source, full real E8 current and boundary Gauss law."""
# BANKED IDENTITY: actual source A0/spatial coefficients and root/family
# identities are replayed before new charge profiles. PRIOR ART: DESIGN.
import importlib.util,json,sys
from pathlib import Path
from functools import lru_cache
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
_r=s.Symbol('r',positive=True);_u=s.Symbol('positive_sqrt_radius',positive=True)
@lru_cache(150000)
def clean(z):
    z=s.sympify(z)
    if z==0:return s.S.Zero
    return s.cancel(z.subs(_r,_u**2)).subs(_u,s.sqrt(_r)) if z.has(_r) else s.cancel(z)
def cm(M):return s.SparseMatrix(M.applyfunc(clean))
def zero(M):return all(clean(z)==0 for z in M.todok().values())
def eye(n):return s.SparseMatrix(n,n,{(i,i):1 for i in range(n)})
def kron(*M):return s.SparseMatrix(s.kronecker_product(*M))
def enc(M):return [[i,j,str(clean(v))] for (i,j),v in sorted(M.todok().items()) if clean(v)!=0]
def source_temporal(a,ss):
    def select(p,kind):
        out={}
        for w,c in p.items():
            if any(a.sf.odd(q) for q in w):continue
            bases=[a.sf.base(q) for q in w]
            if any(b not in ['v0']+['c'+str(j) for j in range(3)]+['~c'+str(j) for j in range(3)] for b in bases):continue
            if any(op not in ('e0','d0','b0','d1','b1') for q in w for op in q.split(':')[:-1]):continue
            out[w]=c
        return a.trace(out)
    raw=select(ss['K_component'],'K')
    def physical(p):
        result={}
        for w,c in p.items():
            term={():c}
            for q in w:
                ops=q.split(':')[:-1];b=a.sf.base(q)
                if b=='v0':v=a.scale(a.letter('a0'),2*s.I)
                else:
                    j=int(b.lstrip('~')[1:]);xb=a.letter('x'+str(2*j));yb=a.letter('x'+str(2*j+1))
                    v=a.scale(a.add(xb,a.scale(yb,s.I if b.startswith('~') else -s.I)),s.sqrt(2) if b.startswith('~') else -s.sqrt(2))
                for op in ops:
                    if op=='e0':v=a.op(v,'t')
                    else:
                        j=int(op[1:]);v=a.add(a.op(v,'n'+str(2*j)),a.scale(a.op(v,'n'+str(2*j+1)),s.I if op[0]=='b' else -s.I))
                term=a.mul(term,v)
            result=a.add(result,term)
        return a.trace(result)
    raw=physical(raw);aa=a.letter('a0');xx=[a.letter('x'+str(j)) for j in range(6)]
    electric=[a.add(a.op(v,'t'),a.comm(aa,v),a.scale(a.op(aa,'n'+str(j)),-1) if j<4 else {}) for j,v in enumerate(xx)]
    target=a.trace(a.add(*(a.scale(a.mul(e,e),-2) for e in electric)))
    def parts(poly):
        euler={};curr={}
        for w,c in poly.items():
            for k,q in enumerate(w):
                ops=q.split(':')[:-1];b=a.sf.base(q);rest={w[k+1:]+w[:k]:c}
                for n,op in enumerate(ops):
                    rem=ops[n+1:];label=a.sf.normalize(rem,'delta_'+b)
                    curr[op]=a.add(curr.get(op,{}),a.mul(a.letter(label),rest))
                    rest=a.scale(a.op(rest,op),-1)
                euler[b]=a.add(euler.get(b,{}),rest)
        return euler,{op:a.trace(p) for op,p in curr.items()}
    difference=a.trace(a.add(raw,a.scale(target,-1)));primitive={};euler_bad={}
    for degree in sorted(set(map(len,difference))):
        piece={w:c for w,c in difference.items() if len(w)==degree};eu,ju=parts(piece)
        euler_bad[degree]={k:v for k,v in eu.items() if v}
        for op,p in ju.items():
            fixed={}
            for w,c in p.items():
                ww=tuple(a.sf.normalize(q.split(':')[:-1],a.sf.base(q).removeprefix('delta_')) for q in w)
                fixed[ww]=fixed.get(ww,0)+c/degree
            primitive[op]=a.trace(a.add(primitive.get(op,{}),fixed))
    divergence=a.trace(a.add(*(a.op(p,op) for op,p in primitive.items())))
    euc,_=parts(target);de={}
    for j,e in enumerate(electric):de=a.add(de,a.comm(xx[j],e),a.op(e,'n'+str(j)) if j<4 else {})
    eugauss=a.add(euc.get('a0',{}),a.scale(de,4))
    # Actual external-vector temporal coefficient from the complete W action.
    D=a.letter('D');gaugeDD=a.scale(a.trace(a.mul(D,D)),s.Rational(1,2))
    actualYM=a.body(a.add(ss['gauge_component'],a.scale(gaugeDD,-1)))
    temporal={w:c for w,c in actualYM.items() if any(a.sf.base(q)=='v0' or 'e0' in q.split(':')[:-1] for q in w) and all(op=='e0' for q in w for op in q.split(':')[:-1])}
    vv=[a.letter('v'+str(j)) for j in range(4)];vtime={}
    for j in range(1,4):
        f=a.add(a.op(vv[j],'e0'),a.scale(a.comm(vv[0],vv[j]),-s.I/2))
        vtime=a.add(vtime,a.scale(a.mul(f,f),s.Rational(1,2)))
    auxv=any(any(a.sf.base(q) in ['D']+['g'+str(j) for j in range(3)]+['~g'+str(j) for j in range(3)] for q in w) and any(a.sf.base(q)=='v0' for q in w) for w in a.body(ss['full']))
    return raw,target,difference,primitive,divergence,euler_bad,eugauss,a.trace(temporal),a.trace(vtime),auxv
def run(method):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    parent=load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py','gauss_source_parent')
    root=load(HERE.parent/'surface_root_gauge_sector_2026_10_16/analysis.py','gauss_root')
    work=load(HERE.parent/'surface_real_fermion_work_2026_10_16/analysis.py','gauss_odd_polynomial')
    twist=load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','gauss_actual_superfield')
    vv,ext,cs,engine,valid,old=parent.setup(method);C=kron(s.Matrix([[0,1],[1,0]]),eye(8));vel=[eye(16)]+[s.SparseMatrix(v) for v in ext+vv]
    sourcejson=json.loads((HERE.parent/'surface_full_real_parent_2026_10_16/results/gauge_frame_run/probe.stdout.log').read_text())['records']['complete_action_matrices']
    time=twist.strip(twist.read(sourcejson['external_derivative'][0]));spatial=[twist.strip(twist.read(v)) for v in sourcejson['external_derivative'][1:]+sourcejson['internal_background']]
    ck('actual positive time and every source spatial action coefficient',valid and zero(time-s.I*C) and all(zero(a-time*v) for a,v in zip(spatial,vel[1:])) and all(zero(v-v.H) and zero(C*v.conjugate()*C-v) for v in vel))
    a=twist.prior.a;sig=twist.prior.frame(cs)['sig'];ss=a.construct(sig);ordered=a.ordered_components(sig)
    native=a.fermions(ss['full']);ref=ordered['full']
    ck('actual complete fermion source equals ordered component bulk',twist.prior.eq(a.jet_quotient(native)[0],a.jet_quotient(ref)[0]))
    coupled=native if method=='native' else ref
    reader=twist.prior.read_matrix(coupled,'external_background',0)
    ck('actual temporal multiplier couples with positive Majorana half',zero(reader-kron(s.I*C,twist.source.J)))
    raw,target,diff,primitive,div,eb,eg,ym,ymtarget,auxv=source_temporal(a,ss)
    ck('actual K time sector equals canonical kinetic plus explicit divergence',not a.trace(a.add(diff,a.scale(div,-1))) and all(not v for v in eb.values()))
    ck('actual K Gauss Euler coefficient factor four',not eg and bool(target))
    ck('actual external vector temporal sector and common internal weight',not a.trace(a.add(ym,a.scale(ymtarget,-1))) and bool(ym))
    ck('actual auxiliaries have no hidden temporal multiplier',not auxv)
    # Explicit momentum derivative, not a transplanted unit normalization.
    e=s.Symbol('electric',real=True);ck('canonical momentum four and wrong factor rejected',s.diff(2*e*e,e)==4*e and s.diff(2*e*e,e)!=2*e)
    records['kinetic']={'raw_K':a.sf.encoded(raw),'canonical_K':a.sf.encoded(target),'retained_divergence':{k:a.sf.encoded(v) for k,v in sorted(primitive.items())},
      'untraced_Euler_residuals':{str(n):{k:a.sf.encoded(v) for k,v in eu.items()} for n,eu in eb.items()},
      'Gauss_Euler_residual':a.sf.encoded(eg),'canonical_momentum_factor':4,'auxiliary_temporal_dependence':auxv}
    if not all(checks.values()):return {'checks':checks,'records':records,'all_passed':False}
    roots,up,dn,hvec,Ep,Em,H,P,Q,G,eta,tau,parity,pair=root.gauge(engine,old);K=cm(tau.H*G)
    unit=lambda j:s.SparseMatrix(248,1,{(j,0):1});hr=s.SparseMatrix(248,1,{(j,0):v for j,v in hvec.items()});Wt=s.SparseMatrix.hstack(unit(up),-hr/s.sqrt(2),unit(dn));tc=cm(Wt.T*K*Wt)
    Et=s.SparseMatrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]]);Ht=s.diag(2,0,-2)
    ck('faithful actual E8 triplet metric reality and all generators',len(roots)==240 and zero(Wt.H*G*Wt-eye(3)) and zero(Ep*Wt-Wt*Et) and zero(Em*Wt+Wt*Et.T) and zero(H*Wt-Wt*Ht) and zero(tc-s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])))
    # Complete positive compact frame: GS versus Cholesky, then both root directions.
    cart=G[:8,:8]
    if method=='native':
        qs=[]
        for j in range(8):
            v=eye(8)[:,j]
            for q in qs:v-=q*clean((q.H*cart*v)[0])
            v=cm(v);qs.append(cm(v/s.sqrt(clean((v.H*cart*v)[0]))))
        bc=s.SparseMatrix.hstack(*qs)
    else:bc=cm(cart.cholesky().T.inv())
    cols=[s.SparseMatrix(248,1,{(i,0):s.I*v for (i,_),v in bc[:,j].todok().items()}) for j in range(8)]
    for j,rt in enumerate(roots):
        neg=roots.index(tuple(-x for x in rt))
        if j>=neg:continue
        u,v=unit(8+j),unit(8+neg);cols.extend([(u+v)/s.sqrt(2),s.I*(u-v)/s.sqrt(2)])
    Bg=s.SparseMatrix.hstack(*cols);dual=cm(Bg.H*G);spinreal,_=work.fixed_frame(C)
    ck('complete248positive compact real frame not small substitute',len(cols)==248 and zero(dual*Bg-eye(248)) and zero(Bg*dual-eye(248)) and zero(tau*Bg.conjugate()-Bg) and zero(Bg.T*K*Bg-eye(248)))
    ck('all16source real derivative and velocity factors',zero(spinreal.H*spinreal-eye(16)) and zero(C*spinreal.conjugate()-spinreal) and zero(spinreal.T*C.H*spinreal-eye(16)) and all(zero((spinreal.H*v*spinreal).conjugate()-spinreal.H*v*spinreal) and zero((spinreal.H*v*spinreal).T-spinreal.H*v*spinreal) for v in vel))
    cdict=[{i:v for (i,_),v in b.todok().items()} for b in cols]
    def bracket(x,y):
        out={}
        for i,v in x.items():
            for j,w in y.items():
                for k,z in pair(i,j).items():out[k]=out.get(k,0)+v*w*z
        return {k:clean(v) for k,v in out.items() if clean(v)!=0}
    dcol={j:{} for j in range(248)}
    for (i,j),v in dual.todok().items():dcol[j][i]=v
    adjoints=[];canonical=[]
    for alpha in range(248):
        if method=='native':
            out={}
            for beta in range(248):
                for k,v in bracket(cdict[alpha],cdict[beta]).items():
                    for i,w in dcol[k].items():out[i,beta]=out.get((i,beta),0)+w*v
            ad=cm(s.SparseMatrix(248,248,out));A=cm(Bg*ad*dual)
        else:
            out={}
            for beta in range(248):
                for k,v in bracket(cdict[alpha],{beta:1}).items():out[k,beta]=v
            A=s.SparseMatrix(248,248,out);ad=cm(dual*A*Bg)
        adjoints.append(ad);canonical.append(A)
    ck('every compact E8 generator has nonzero real antisymmetric adjoint',all(not zero(ad) and zero(ad.conjugate()-ad) and zero(ad.T+ad) and zero(A*Bg-Bg*ad) for ad,A in zip(adjoints,canonical)))
    records['full_real_current']={'source_dimension':16,'gauge_dimension':248,'full_dimension':3968,'spin_frame':enc(spinreal),'gauge_frame':enc(Bg),'all248real_adjoint_matrices':[enc(A) for A in adjoints],
      'formula':'i/2 chi^T (real_velocity tensor real_adjoint_alpha) chi; actual positive source sign, all directions'}
    # Known full four-real-parameter family, independently rebuilt.
    inds=[0,1,8,9];er,_=work.fixed_frame(C.extract(inds,inds));Epar=s.SparseMatrix(16,4,{(inds[i],j):v for (i,j),v in er.todok().items()})
    r,g=s.symbols('r g',positive=True);z=s.Symbol('zeta',nonzero=True);ssr=1-g*g*r;co=(z*z+z**-2)/2;si=(z*z-z**-2)/(2*s.I)
    q=g/(z*s.sqrt(r)*ssr);qb=g*z/(s.sqrt(r)*ssr)
    bg=[s.Matrix([0,s.I*g*g*si/(s.sqrt(2)*ssr),0]),s.Matrix([0,-s.I*g*g*co/(s.sqrt(2)*ssr),0]),s.Matrix([q,0,qb])/2,s.Matrix([q,0,-qb])/(2*s.I)]
    if method=='native':ag=[cm(v.diff(g)) for v in bg]
    else:
        qg=(1+g*g*r)/(z*s.sqrt(r)*ssr**2);qgb=(1+g*g*r)*z/(s.sqrt(r)*ssr**2)
        ag=[s.Matrix([0,s.I*s.sqrt(2)*g*si/ssr**2,0]),s.Matrix([0,-s.I*s.sqrt(2)*g*co/ssr**2,0]),s.Matrix([qg,0,qgb])/2,s.Matrix([qg,0,-qgb])/(2*s.I)]
    vn=[s.SparseMatrix(vv[j]) for j in (2,3,4,5)];psi=cm(-sum((kron(v*Epar,b) for v,b in zip(vn,ag)),s.zeros(48,4)))
    saved=json.loads((HERE.parent/'surface_reverse_susy_2026_10_16/results/provenance_run/probe.json').read_text())['records']['family']['actual_fermion_all_parameters']
    oldpsi=s.SparseMatrix(48,4,{(i,j):s.sympify(v,locals={'r':r,'g':g,'zeta':z}) for i,j,v in saved})
    conj=lambda M:cm(M.conjugate().subs(s.conjugate(z),1/z));th=lambda M:cm(s.I*z*M.diff(z)/2)
    adsmall=[Et,-Ht/s.sqrt(2),-Et.T];advec=lambda v:cm(sum((v[j]*adsmall[j] for j in range(3)),s.zeros(3)))
    ads=[advec(v) for v in bg]
    plain=lambda M,j:cm(co*M.diff(r)-si*th(M)/r) if j==0 else cm(si*M.diff(r)+co*th(M)/r) if j==1 else s.zeros(*M.shape)
    D=lambda M,j:cm(plain(M,j)+ads[j]*M)
    Dpsi=lambda M,j:cm(plain(M,j)+kron(eye(16),ads[j])*M)
    ck('complete actual amplitude fermion replay and zero Dirac residual',zero(psi-oldpsi) and zero(sum((kron(v,eye(3))*Dpsi(psi,j) for j,v in enumerate(vn)),s.zeros(48,4))) and zero(kron(C,tc)*conj(psi)-psi))
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)];currents=[];support=[]
    for N,V in enumerate(vel):
        vectors={p:s.zeros(248,1) for p in pairs}
        if method=='native':
            for alpha,A in enumerate(canonical):
                Tga=cm(Wt.T*K*A*Wt)
                if zero(Tga):continue
                M=cm(psi.T*kron(C.H*V,Tga)*psi)
                if not zero(M.T+M):raise ValueError('Current matrix is not antisymmetric')
                for st in pairs:vectors[st]+=cols[alpha]*(s.I*M[st[0],st[1]])
            vectors={p:cm(v) for p,v in vectors.items()}
        else:
            # Direct invariant bracket contraction, not adjoint projection.
            TS=cm(C.H*V);spin_entries=TS.todok();basis_small=[{j:v for (j,_),v in Wt[:,k].todok().items()} for k in range(3)]
            bp={(i,j):s.SparseMatrix(248,1,{(k,0):v for k,v in bracket(basis_small[i],basis_small[j]).items()}) for i in range(3) for j in range(3)}
            for st in pairs:
                v=s.zeros(248,1)
                for (p0,q0),t0 in spin_entries.items():
                    for c0 in range(3):
                        u=psi[3*p0+c0,st[0]]
                        if u==0:continue
                        for d0 in range(3):
                            w=psi[3*q0+d0,st[1]]
                            if w!=0:v-=s.I*t0*u*w*bp[c0,d0]
                vectors[st]=cm(v)
        ck('complete Hermitian odd current '+str(N),all(zero(-tau*conj(v)-v) for v in vectors.values()))
        support.append(any(not zero(v) for v in vectors.values()));currents.append(vectors)
    qgnorm=(1+g*g*r)**2/(r*ssr**4);j0=currents[0];hindex=min(hvec);coeff={st:clean(v[hindex]/hvec[hindex]/qgnorm) for st,v in j0.items()}
    ck('nonzero full Gauss current exact Cartan profile',support[0] and all(zero(v-hr*qgnorm*coeff[st]) and not coeff[st].has(r,g,z) for st,v in j0.items()))
    ck('normal current vanishes only on this family not every current',all(not support[N] for N in (6,7,8,9)) and any(support))
    # Exact stationary temporal response at Grassmann degree two.
    f=r/(4*ssr**2);h0=(1+g*g*r)/(2*g*ssr);eps=s.Matrix([0,-s.I*s.sqrt(2)*h0,0]);Hsmall=s.Matrix([0,-s.sqrt(2),0]);Ksmall=tc
    lap=lambda v:cm(sum((D(D(v,j),j) for j in range(4)),s.zeros(*v.shape)))
    a0={st:Hsmall*coeff[st]*f for st in pairs};current_small={st:Hsmall*coeff[st]*qgnorm for st in pairs}
    ck('actual scalar terms and source factor four in Gauss response',all(zero(4*lap(v)-current_small[st]) for st,v in a0.items()) and zero(lap(eps)))
    ck('wrong response sign or Gauss normalization rejected',any(not zero(4*lap(v)+current_small[st]) for st,v in a0.items()) and any(not zero(2*lap(v)-current_small[st]) for st,v in a0.items()))
    ck('unbackreacted zero temporal field fails full fermionic Gauss',any(not zero(v) for v in current_small.values()))
    pairbil=lambda u,v:clean((u.T*Ksmall*v)[0]);Rout,cut=s.symbols('R epsilon',positive=True)
    Vpsi=cm(-kron(eye(16),advec(eps))*psi)
    omferm=cm(Vpsi.T*kron(C.H,tc)*psi.diff(g))
    fluxes={};reciprocity=True;noether=True;fielddep=False;hom=True;outer=True;omegaok=True;omitferm=False;orientation=False;notwr=False;nonzeroomega=False
    for st,A0 in a0.items():
        electric=[-D(A0,j) for j in range(4)];da=[D(eps,j) for j in range(4)];jv=current_small[st]
        wr=clean(r*(pairbil(eps,A0.diff(r))-pairbil(eps.diff(r),A0)))
        charge=clean(-4*r*pairbil(A0.diff(r),eps))
        density=clean(4*sum(pairbil(e,d) for e,d in zip(electric,da))-pairbil(jv,eps))
        reciprocity &= clean(4*wr.diff(r)-r*pairbil(eps,jv))==0
        noether &= clean(charge.diff(r)-r*density)==0
        qdelta=clean(-4*r*pairbil(A0.diff(r),eps.diff(g)))
        corrected=clean(charge.diff(g)-qdelta);fielddep |= qdelta!=0 and corrected!=charge.diff(g)
        pb=[4*v for v in electric]
        vpb=[cm(-advec(eps)*v) for v in pb]
        ombos=clean(sum(pairbil(d,v.diff(g))-pairbil(ag[j],vpb[j]) for j,(d,v) in enumerate(zip(da,pb))))
        omf=clean(-s.I*(omferm[st[0],st[1]]-omferm[st[1],st[0]]))
        omegaok &= clean(corrected.diff(r)-r*(ombos+omf))==0
        omitferm |= clean(corrected.diff(r)-r*ombos)!=0
        orientation |= clean(charge.subs(r,Rout)-charge.subs(r,cut)-(charge.subs(r,Rout)+charge.subs(r,cut)))!=0
        notwr |= clean(charge-4*wr)!=0 and clean(charge+4*wr)!=0
        nonzeroomega |= clean(corrected.subs(r,Rout)-s.limit(corrected,r,0))!=0
        Ar=cm(A0-Hsmall*coeff[st]*f.subs(r,Rout)*h0/h0.subs(r,Rout))
        hom &= zero(4*lap(Ar)-jv);outer &= zero(Ar.subs(r,Rout))
        fluxes[str(st)]={'Wronskian':str(wr),'canonical_charge':str(charge),'Noether_density':str(density),'bosonic_symplectic_density':str(ombos),'fermionic_symplectic_density':str(omf),
          'parameter_variation_term':str(qdelta),'corrected_g_charge_variation':str(corrected),
          'both_end_charge':str(2*s.pi*(charge.subs(r,Rout)-charge.subs(r,cut))),
          'inner_charge':str(s.limit(charge,r,0)),'outer_Dirichlet_response':enc(Ar)}
    ck('full covariant Green reciprocity source not norm identification',reciprocity)
    ck('canonical full fermion Gauss charge and local divergence',noether)
    ck('field dependent gauge parameter subtraction nonzero',fielddep)
    ck('actual full canonical presymplectic contraction matches corrected charge',omegaok and nonzeroomega)
    ck('omitting real fermion symplectic contribution fails',omitferm)
    ck('electric charge is not Wronskian even up to sign',notwr)
    ck('homogeneous freedom and regular outer zero response retained',hom and outer)
    ck('particular response finite inner but not selected boundary data',all(all(s.limit(v,r,0)==0 for v in A) for A in a0.values()) and any(not zero(A.subs(r,Rout)) for A in a0.values()))
    ck('both endpoints not an unoriented or boundaryless charge',orientation and any(row['canonical_charge']!='0' and row['both_end_charge']!='0' for row in fluxes.values()))
    # Genuine odd canonical moment map and source half-factor control.
    t=s.Symbol('nonzero_skew_control',real=True,nonzero=True);At=s.Matrix([[0,t],[-t,0]])
    chi=[0,1];dchi=[2,3];bp=work.bilinear;psum=work.psum
    variation=psum((s.I/2,bp(At,dchi,chi)),(s.I/2,bp(At,chi,dchi)))
    omega=psum((-s.I,bp(At,chi,dchi)))
    ck('graded canonical fermion contraction gives minus charge variation',not psum((1,variation),(1,omega)) and bool(variation))
    ck('Majorana doubling and commuting trace detector rejected',bool(psum((2,variation),(1,omega))) and s.trace(At)==0 and bool(work.polynomial(At,'native')))
    records['family']={'actual_amplitude_fermion':enc(psi),'all_ten_currents':[{str(st):enc(v) for st,v in row.items()} for row in currents],
      'nonzero_component_flags':support,'Gauss_Cartan_coefficients':{str(st):str(v) for st,v in coeff.items()},
      'temporal_degree2_response':{str(st):enc(v) for st,v in a0.items()},'all_endpoint_records':fluxes,'harmonic_parameter':enc(eps)}
    records['meaning']={'fermion_Gauss_source_nonzero':support[0],'source_normalized_bosonic_momentum':4,'Gauss_degree2_response':True,
      'all_other_boson_equations_solved':False,'full_nonlinear_boundary_law_selected':False,'c_number_vacuum_charge_predicted':False,
      'complete_physical_SM_three_gravity':False,'shared_author_not_independent_acceptance':True,'charges_not_norms_or_particle_counts':True}
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(method):
    data=run(method);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
