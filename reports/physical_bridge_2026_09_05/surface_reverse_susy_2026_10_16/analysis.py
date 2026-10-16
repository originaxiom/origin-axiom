"""Actual source reverse supersymmetry and a boundary gauge partner."""
import json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
import importlib.util
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def clean(z):return s.cancel(s.expand(z))
def cm(M):return s.SparseMatrix(M.applyfunc(clean))
def zero(M):return all(clean(z)==0 for z in M.todok().values())
def eye(n):return s.SparseMatrix(n,n,{(j,j):1 for j in range(n)})
def kron(*M):return s.SparseMatrix(s.kronecker_product(*M))
def enc(M):return [[i,j,str(clean(z))] for (i,j),z in sorted(M.todok().items()) if clean(z)!=0]
def source_maps(method,twist,cs,C):
    a=twist.prior.a;sig=twist.prior.frame(cs)['sig'];P=[0,1,8,9]
    if method=='native':
        full=a.construct(sig);V=full['V'];chirals=full['C']
    else:
        V={((0,2,3),('f0_1',)):2*s.I,((1,2,3),('f0_0',)):-2*s.I,
           ((0,1,2),('~f0_1',)):-2*s.I,((0,1,3),('~f0_0',)):2*s.I}
    S=s.Matrix(4,4,lambda n,mu:sig[mu][n//2,n%2]);Sinv=S.inv();vectors=[s.zeros(16) for j in range(4)]
    for alpha in range(2):
        if method=='native':d=a.left(V,alpha)
        else:
            d={}
            for (th,w),v in V.items():
                if alpha in th:
                    k=th.index(alpha);d[th[:k]+th[k+1:],w]=(-1)**k*v
        for beta in range(2):
            coeff=s.Matrix([d.get(((p,q+2),('~f0_'+str(beta),)),0) for p in range(2) for q in range(2)])
            delta=Sinv*coeff/(2*s.I)
            for mu in range(4):vectors[mu][alpha,8+beta]=delta[mu]
    out=[cm(v-C.T*v.conjugate()*C) for v in vectors]
    internal=[]
    for j in range(3):
        M=s.zeros(16)
        for alpha in range(2):
            if method=='native':
                d=a.component(a.left(chirals[j],alpha),(),1)
                for beta in range(2):M[alpha,2*(j+1)+beta]=d.get(('f'+str(j+1)+'_'+str(beta),),0)/s.sqrt(2)
            else:
                for beta in range(2):M[alpha,2*(j+1)+beta]=s.Matrix([[0,-1],[1,0]])[alpha,beta]
        Mb=C*M*C;internal.extend([cm((Mb-M)/2),cm((Mb+M)/(2*s.I))])
    return out+internal
def run(method):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    parent=load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py','reverse_actual_parent')
    root=load(HERE.parent/'surface_root_gauge_sector_2026_10_16/analysis.py','reverse_actual_root')
    work=load(HERE.parent/'surface_real_fermion_work_2026_10_16/analysis.py','reverse_real_frame')
    twist=load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','reverse_superfield_reader')
    vv,ext,cs,engine,valid,old=parent.setup(method);I=eye(16);C=kron(s.Matrix([[0,1],[1,0]]),eye(8))
    velocities=[I]+[s.SparseMatrix(v) for v in ext+vv]
    lam=s.SparseMatrix(s.diag(*[int(f==0) for bar in range(2) for f in range(4) for spin in range(2)]))
    R=cm(-s.I*vv[4]*vv[5]);B=cm(s.I*vv[2]*vv[3])
    ck('actual all nine source velocities and full Majorana reality',valid and all(zero(v-v.H) and zero(C*v.conjugate()*C-v) for v in velocities) and all(zero(v*w+w*v-2*int(i==j)*I) for i,v in enumerate(velocities[1:]) for j,w in enumerate(velocities[1:])))
    raw=json.loads((HERE.parent/'surface_full_real_parent_2026_10_16/results/gauge_frame_run/probe.stdout.log').read_text())['records']['complete_action_matrices']
    A0=twist.strip(twist.read(raw['external_derivative'][0]));Aa=[twist.strip(twist.read(a)) for a in raw['external_derivative'][1:]+raw['internal_background']]
    ck('actual positive time and all spatial source action signs',zero(A0-s.I*C) and zero(-s.I*C*A0-I) and all(zero(a-A0*v) for a,v in zip(Aa,velocities[1:])))
    maps=source_maps(method,twist,cs,C);T=cm((maps[0]*C/s.I).T)
    lower=[velocities[0]]+[-v for v in velocities[1:]]
    ck('single earned Noether parameter map all ten actual bosons',all(zero(a-T.T*s.I*C*v) for a,v in zip(maps,lower)))
    ck('actual Noether factor and full real parameter subspace',zero(T-s.I*R*lam/2) and zero(C*T.conjugate()-T*C) and zero(T.H*T-lam/4))
    ck('all actual boson maps have graded rather than commuting reality',all(zero(-C.T*a.conjugate()*C-a) and zero(lam*a-a) for a in maps) and any(not zero(C.T*a.conjugate()*C-a) for a in maps))
    ck('wrong Noether factor and missing odd reversal rejected',any(not zero(a-2*T.T*s.I*C*v) for a,v in zip(maps,lower)) and any(not zero(C.T*a.conjugate()*C-a) for a in maps))
    if not all(checks.values()):return {'checks':checks,'records':{'source_maps':[enc(a) for a in maps],'parameter_map':enc(T),
        'expected_maps':[enc(T.T*s.I*C*v) for v in lower],
        'map_residuals':[enc(a-T.T*s.I*C*v) for a,v in zip(maps,lower)]},'all_passed':False}
    # Earn source lambda identification in the actual complementary MW map.
    op=twist.opposite(cs);ph=[1,1,-1,-s.I];ph+=list(map(s.conjugate,ph));L=cm(op['S']*s.diag(*[v for p in ph for v in [p]*2]))
    gh=kron(eye(4),s.I*cs[0]*cs[1],eye(2));gv=kron(eye(4),s.I*cs[2]*cs[3],eye(2))
    Pi=cm(op['MW']*(eye(32)+op['R']*gh)/2*(eye(32)+op['R']*gv)/2)
    extG=[kron(s.I*cs[j],eye(4),s.diag(1,-1)) for j in range(1,4)]
    covariant=[-op['G0']]+extG+op['G']
    ck('full Lorentzian lowered current not Hamiltonian velocity',zero(op['G0']*op['G0']+eye(32)) and all(zero(L.H*op['G0']*gam*L-w) for gam,w in zip(covariant,lower)))
    ck('old all velocity reverse formula rejected in every spatial direction',all(not zero(a-T.T*s.I*C*v) for a,v in zip(maps[1:],velocities[1:])))
    ck('named scalar supercharge is actual source lambda by its full map',zero(L*lam*L.H-Pi) and zero(L.H*Pi*L-lam) and s.trace(lam)==4)
    active=(2,3,4,5);vnorm=[s.SparseMatrix(vv[j]) for j in active]
    # Three independent selfdual curvature coefficients in source indices.
    fcoeff=[{(0,1):1,(2,3):-1},{(0,2):1,(1,3):1},{(0,3):1,(1,2):-1}]
    curv=[cm(sum((sign*vnorm[a]*vnorm[b] for (a,b),sign in fc.items()),s.zeros(16))) for fc in fcoeff]
    ck('all BPS curvature matrices annihilate actual scalar supercharge',all(zero(lam*q) and zero(q*lam) for q in curv))
    ward=True
    for N,w in enumerate(velocities):
        normal=active.index(N-4) if N>=4 and N-4 in active else None
        for fc,q in zip(fcoeff,curv):
            rhs=s.zeros(16)
            if normal is not None:
                for (a,b),sign in fc.items():
                    if a==normal:rhs+=2*sign*lam*vnorm[b]
                    if b==normal:rhs-=2*sign*lam*vnorm[a]
            ward &= zero(lam*w*q-rhs)
    ck('every independent curvature coefficient in local Euler Ward identity',ward)
    ck('wrong normal BPS curvature sign fails annihilation',not zero(lam*(vnorm[0]*vnorm[1]+vnorm[2]*vnorm[3])))
    inds=[0,1,8,9];fr,_=work.fixed_frame(C.extract(inds,inds));Epar=s.SparseMatrix(16,4,{(inds[i],j):v for (i,j),v in fr.todok().items()});J=cm(Epar.H*s.I*R*Epar)
    ck('complete normalized real four parameter source frame',zero(Epar.H*Epar-eye(4)) and zero(Epar*Epar.H-lam) and zero(C*Epar.conjugate()-Epar) and zero(T*(-2*s.I*R*Epar)-Epar))
    ck('real parameter complex structure not species count',zero(J.conjugate()-J) and zero(J.T+J) and zero(J*J+eye(4)))
    roots,up,dn,hvec,Ep,Em,H,P,Q,G,eta,tau,parity,pair=root.gauge(engine,old)
    unit=lambda j:s.SparseMatrix(248,1,{(j,0):1});hr=s.SparseMatrix(248,1,{(j,0):v for j,v in hvec.items()});Wt=s.SparseMatrix.hstack(unit(up),-hr/s.sqrt(2),unit(dn))
    Et=s.SparseMatrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]]);Ht=s.diag(2,0,-2);std=[Et,-Ht/s.sqrt(2),-Et.T]
    actual=[Ep,-H/s.sqrt(2),Em]
    ck('actual normalized E8 root map all generators metric parity reality',len(roots)==240 and zero(Wt.H*G*Wt-eye(3)) and all(zero(A*Wt-Wt*a) for A,a in zip(actual,std)) and zero(eta*Wt-Wt*s.diag(-1,1,-1)) and zero(tau*Wt.conjugate()-Wt*s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])))
    ad=[cm(Wt.H*G*A*Wt) for A in actual] if method=='native' else std
    r,g=s.symbols('r g',positive=True);z=s.Symbol('zeta',nonzero=True);ss=1-g*g*r
    co=(z*z+z**-2)/2;si=(z*z-z**-2)/(2*s.I)
    conj=lambda M:cm(M.conjugate().subs(s.conjugate(z),1/z))
    th=lambda M:cm(s.I*z*M.diff(z)/2)
    plain=lambda M,j:cm(co*M.diff(r)-si*th(M)/r) if j==0 else cm(si*M.diff(r)+co*th(M)/r) if j==1 else s.zeros(*M.shape)
    q=g/(z*s.sqrt(r)*ss);qb=g*z/(s.sqrt(r)*ss)
    bg=[s.Matrix([0,s.I*g*g*si/(s.sqrt(2)*ss),0]),s.Matrix([0,-s.I*g*g*co/(s.sqrt(2)*ss),0]),s.Matrix([q,0,qb])/2,s.Matrix([q,0,-qb])/(2*s.I)]
    advec=lambda v:cm(sum((v[j]*ad[j] for j in range(3)),s.zeros(3)))
    ads=[advec(v) for v in bg]
    D=lambda v,j:cm(plain(v,j)+ads[j]*v)
    Fs={(a,b):cm(plain(bg[b],a)-plain(bg[a],b)+ads[a]*bg[b]) for a in range(4) for b in range(a+1,4)}
    Cbg=[Fs[0,1]+Fs[2,3],Fs[0,2]-Fs[1,3],Fs[0,3]+Fs[1,2]]
    ck('same exact full noncommuting BPS background',all(zero(v) for v in Cbg) and not zero(Fs[0,1]) and not zero(Fs[2,3]))
    if method=='native':ag=[cm(v.diff(g)) for v in bg]
    else:
        qg=(1+g*g*r)/(z*s.sqrt(r)*ss**2);qgb=(1+g*g*r)*z/(s.sqrt(r)*ss**2)
        ag=[s.Matrix([0,s.I*s.sqrt(2)*g*si/ss**2,0]),s.Matrix([0,-s.I*s.sqrt(2)*g*co/ss**2,0]),s.Matrix([qg,0,qgb])/2,s.Matrix([qg,0,-qgb])/(2*s.I)]
    phase=[ag[1],-ag[0],ag[3],-ag[2]]
    reality=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    ck('all background tangent and phase fields compact real',all(zero(reality*conj(v)-v) for v in bg+ag+phase))
    def tangent_eq(a):
        df={(j,k):cm(D(a[k],j)-D(a[j],k)) for j in range(4) for k in range(j+1,4)}
        return [df[0,1]+df[2,3],df[0,2]-df[1,3],df[0,3]+df[1,2]],cm(sum((D(a[j],j) for j in range(4)),s.zeros(3,1)))
    for label,a in (('amplitude',ag),('phase',phase)):
        cc,gf=tangent_eq(a);ck('complete BPS and covariant gauge tangent '+label,all(zero(v) for v in cc) and zero(gf))
    removed=ag.copy();removed[0]=s.zeros(3,1);removed[1]=s.zeros(3,1)
    cc,gf=tangent_eq(removed);ck('omitting tangent connection fails true linearized equations',any(not zero(v) for v in cc))
    # Full spin and all real parameters; exact invariant E8 triplet map above.
    psi=cm(-sum((kron(v*Epar,a) for v,a in zip(vnorm,ag)),s.zeros(48,4)))
    def Dpsi(V,j):
        return cm(plain(V,j)+kron(I,ads[j])*V)
    slash=cm(sum((kron(v,eye(3))*Dpsi(psi,j) for j,v in enumerate(vnorm)),s.zeros(48,4)))
    ck('complete actual amplitude fermion solves Dirac equation',zero(slash) and zero(kron(C,reality)*conj(psi)-psi))
    reverse=[];allimages=True;outside=True
    for N,v in enumerate(velocities):
        row=[]
        for rr in range(4):
            m=cm(kron(Epar[:,rr].H*v,eye(3))*psi)
            expected=s.zeros(3,4)
            if N>=4 and N-4 in active:
                j=active.index(N-4)
                for k in range(4):expected[:,k]=-int(rr==k)*ag[j]-J[rr,k]*phase[j]
            else:outside &= zero(m)
            allimages &= zero(m-expected);row.append(enc(-m))
        reverse.append(row)
    ck('every reverse image equals amplitude plus phase not rank matching',allimages and outside)
    ck('two independent bosonic directions with four real parameters',not zero(ag[0]*phase[2].T-phase[0]*ag[2].T) and any(J[i,j]!=0 for i in range(4) for j in range(4) if i!=j))
    eps=s.Matrix([0,-s.I*(1+g*g*r)/(s.sqrt(2)*g*ss),0]);deps=[D(eps,j) for j in range(4)]
    ck('entire phase partner equals actual covariant gauge variation',all(zero(a-b) for a,b in zip(phase,deps)))
    lap=cm(sum((D(D(eps,j),j) for j in range(4)),s.zeros(3,1)))
    ck('phase gauge parameter covariantly harmonic including scalar terms',zero(lap))
    ck('dropping scalar gauge Laplace terms rejected',not zero(D(D(eps,0),0)+D(D(eps,1),1)))
    def curvature(a,b):return Fs[a,b] if a<b else -Fs[b,a] if b<a else s.zeros(3,1)
    for label,a in (('amplitude',ag),('phase',phase)):
        div=cm(sum((D(a[j],j) for j in range(4)),s.zeros(3,1)));eu=[]
        for n in range(4):
            val=sum((D(D(a[n],m),m)-2*advec(curvature(m,n))*a[m] for m in range(4)),s.zeros(3,1))-D(div,n)
            eu.append(cm(val))
        ck('actual full linearized boson Euler '+label,all(zero(v) for v in eu))
    norm=lambda v:clean((conj(v).T*v)[0])
    ng=clean(sum(norm(a) for a in ag));np=clean(sum(norm(a) for a in phase));cross=clean(sum((conj(a).T*b)[0] for a,b in zip(ag,phase)))
    expected=(1+4*g*g*r+g**4*r*r)/(r*ss**4);f=r*(1+g*g*r)/ss**3
    ck('positive finite local coefficient norm and orthogonal equal partner',clean(ng-expected)==0 and clean(np-ng)==0 and cross==0 and clean(r*ng-s.diff(f,r))==0)
    flux=clean(r*(conj(eps).T*eps.diff(r))[0]);inner=eps.applyfunc(lambda v:s.limit(v,r,0));Rout,cut=s.symbols('R epsilon',positive=True)
    ck('actual covariant Green flux equals full gauge direction norm',clean(flux-f)==0 and clean(s.diff(flux,r)-r*np)==0 and s.limit(flux,r,0)==0)
    ck('gauge parameter nonzero at both ends not proper redundancy',not zero(inner) and not zero(eps.subs(r,Rout)) and zero(inner-s.Matrix([0,-s.I/(s.sqrt(2)*g),0])))
    end=2*s.pi*(f.subs(r,Rout)-f.subs(r,cut))
    ck('both oriented endpoints and no discarded outer norm',clean(end-2*s.pi*(flux.subs(r,Rout)-flux.subs(r,cut)))==0 and clean(end-2*s.pi*(flux.subs(r,Rout)+flux.subs(r,cut)))!=0 and not zero(eps.subs(r,Rout)))
    ck('normalizable near inner end not a claim across outer pole',s.limit(f,r,0)==0 and s.limit(f,r,1/g**2,dir='-')==s.oo)
    records['source']={'boson_order':['time','external1','external2','external3','internal0','internal1','internal2','internal3','scalar4','scalar5'],
      'actual_reverse_maps':[enc(a) for a in maps],'Noether_parameter_map':enc(T),'full_real_parameter_frame':enc(Epar),'J':enc(J),'source_action_static_sign':-1,
      'Lorentzian_lowered_current_signs':[1]+[-1]*9,'Hermitian_even_factor_for_returned_normal_profiles':'+i epsilon_odd xi_odd'}
    records['root']={'actual_E8_triplet_map':enc(Wt),'full_root_coordinates':list(roots[up-8]),'triplet_adjoint_matrices':[enc(a) for a in ad]}
    records['family']={'background':[enc(a) for a in bg],'amplitude':[enc(a) for a in ag],'phase':[enc(a) for a in phase],
      'actual_fermion_all_parameters':enc(psi),'all_returned_boson_images':reverse,'gauge_parameter':enc(eps),'inner_gauge_parameter':enc(inner),
      'norm_density':str(ng),'phase_norm_density':str(np),'cross':str(cross),'primitive':str(f),'end_flux':str(flux),'both_end_norm':str(end)}
    records['meaning']={'real_bosonic_profile_span':2,'all_real_supercharge_parameters':4,'not_physical_generations':True,
      'proper_gauge_definition':'parameters vanish at BOTH ends','phase_is_proper_gauge':False,'larger_quotient_is_a_different_ensemble':True,
      'complete_physical_boundary_law':False,'full_physical_SM_three_gravity':False,'shared_author_not_independent_acceptance':True}
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(method):
    data=run(method);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
