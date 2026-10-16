"""Full real local action/operator test; no science executes on import."""
import importlib.util,json,sys
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import sympy as s
import superfield as a
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
source=load(HERE.parent/'surface_source_operator_2026_10_16/analysis.py','full_real_phase_instrument')
def cm(m):return m.applyfunc(s.expand)
def zero(m):return all(v==0 or s.simplify(v)==0 for v in m)
def eq(p,q):return not a.trace(a.add(p,a.scale(q,-1)))
def encoded(p):return a.sf.encoded(a.trace(p))
def adj_word(p):return a.adj(p)
def fvec(j):return tuple(a.letter('f'+str(j)+'_'+str(k)) for k in range(2))

def frame(cs):
    I2=s.eye(2);I4=s.eye(4);I32=s.eye(32);p3=s.diag(1,-1)
    g=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]];g5=cm(s.I*s.prod(g))
    L=s.Matrix.hstack(*((I4+g5)/2).columnspace())
    sig=[-I2]+[cm((L.H*g[0]*g[j]*L).T) for j in range(1,4)]
    G0=s.kronecker_product(g[0],I4,p3)
    ext=[s.kronecker_product(g[j],I4,p3) for j in range(1,4)]
    G=[s.kronecker_product(g5,s.I*c,p3) for c in cs]+[s.kronecker_product(I4,I4,s.Matrix([[0,1],[1,0]])),s.kronecker_product(I4,I4,s.Matrix([[0,-s.I],[s.I,0]]))]
    B=cm(s.kronecker_product(g[0]*g[1]*g[3],cs[1]*cs[3],s.Matrix([[0,-s.I],[s.I,0]])))
    MW=cm((I32-s.kronecker_product(g5,-s.prod(cs),p3))/2)
    W=s.Matrix.hstack(*[s.kronecker_product(L,s.eye(4)[:,i],s.eye(2)[:,r]) for i,r in ((3,1),(1,0),(2,0),(0,1))])
    S=W.row_join(B*W.conjugate());Bn=cm(S.T*B.H*S);J=source.J
    can=[cm(s.kronecker_product(-s.I*S.T*B.H*G0*x*S,J)) for x in G]
    cext=[cm(s.I*s.kronecker_product(Bn,J))]+[cm(s.kronecker_product(-s.I*S.T*B.H*G0*x*S,J)) for x in ext]
    return {'sig':sig,'G0':G0,'G':G,'B':B,'MW':MW,'S':S,'Bn':Bn,'can':can,'ext':cext}

pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
T=[s.I*p/s.sqrt(2) for p in pauli];X=s.I*(pauli[0]+pauli[2])/2;J=source.J
Td=[sum((J[k,j]*T[k] for k in range(3)),s.zeros(2)) for j in range(3)]
@lru_cache(None)
def trace_matrices(keys):
    out=s.eye(2)
    for tag,j in keys:out*= X if tag=='x' else Td[j] if tag=='d' else T[j]
    return s.simplify(s.trace(out))

def read_matrix(p,kind,direction):
    """A coefficient reader, after universal bracket/form checks."""
    out=s.MutableSparseMatrix(48,48,{})
    for w,cc in a.trace(p).items():
        positions=[j for j,q in enumerate(w) if a.sf.odd(q)]
        if len(positions)!=2:raise ValueError('not quadratic fermion density')
        maps=[];factor=cc;bad=False
        for pos,q in enumerate(w):
            pp=q.split(':');ops=pp[:-1];b=pp[-1];bar=b.startswith('~');b=b.lstrip('~')
            if b.startswith('f'):
                species,alpha=map(int,b[1:].split('_'));coeff=-s.Integer(1) if bar else s.Integer(1);tag='t'
                if len(ops)>1:raise ValueError('unexpected higher fermion derivative')
                if ops:
                    op=ops[0];coeff0=0
                    if op.startswith('e') and kind=='external_derivative' and int(op[1:])==direction:coeff0=1
                    if op.startswith(('d','b')) and kind=='internal_derivative' and direction<4 and int(op[1:])==direction//2:
                        coeff0=1 if direction%2==0 else (s.I if op[0]=='b' else -s.I)
                    coeff*=coeff0;tag='d'
                if coeff==0:bad=True;break
                factor*=coeff;maps.append(('f',species,alpha,bar,tag))
            else:
                coeff=0
                if not ops and b.startswith('c') and kind=='internal_background' and int(b[1:])==direction//2:
                    coeff=-s.sqrt(2) if direction%2==0 else s.I*s.sqrt(2)
                    if bar:coeff=-s.conjugate(coeff)
                if not ops and b.startswith('v') and kind=='external_background' and int(b[1:])==direction:
                    coeff=2*s.I
                if coeff==0:bad=True;break
                factor*=coeff;maps.append(('b',))
        if bad:continue
        for i in range(3):
            for j in range(3):
                colors=iter((i,j));keys=[];ids=[]
                for m in maps:
                    if m[0]=='b':keys.append(('x',0));continue
                    color=next(colors);_,species,alpha,bar,tag=m
                    keys.append((tag,color));ids.append(((4*int(bar)+species)*2+alpha)*3+color)
                v=s.expand(factor*trace_matrices(tuple(keys)))
                if not v:continue
                ii,jj=ids
                if ii==jj:continue
                out[ii,jj]+=v;out[jj,ii]-=v
    return cm(out)

def run(cs,valid,method):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    fr=frame(cs);sig=fr['sig'];ss=a.construct(sig);ref=a.ordered_components(sig)
    ck('actual frame supplied',valid)
    ck('actual MW frame normalized',zero(fr['S'].H*fr['S']-s.eye(16)) and zero(fr['S']*fr['S'].H-fr['MW']))
    ck('actual spatial sigma Pauli frame',all(zero(sig[i]*sig[j]+sig[j]*sig[i]-2*int(i==j)*s.eye(2)) for i in range(1,4) for j in range(1,4)) and zero(sig[1]*sig[2]-s.I*sig[3]))
    ck('full WZ vector reality and inverse',a.eq(a.dag(ss['V']),ss['V']) and a.eq(a.nmul(ss['G'],ss['Gi']),a.one))
    ck('nonzero V squared retained V cubed zero',bool(ss['V2']) and not a.nmul(ss['V'],ss['V2']))
    ck('all actual chirals satisfy barD',all(not ss['BD'](c,j) for c in ss['C'] for j in range(2)))
    ck('actual real K density',a.eqtr(a.dag(ss['K']),ss['K']))
    ck('actual F action real',eq(ss['F_component'],a.adj(ss['F_component'])))
    # Universal full-component equality modulo EXPLICIT retained divergences.
    native=a.fermions(ss['full']);component_ref=ref['full']
    qn,jn=a.jet_quotient(native);qr,jr=a.jet_quotient(component_ref)
    ck('actual full fermion action equals ordered components',eq(qn,qr))
    ck('native fermion IBP keeps all currents',eq(native,a.add(qn,a.current_div(jn))))
    ck('reference fermion IBP keeps all currents',eq(component_ref,a.add(qr,a.current_div(jr))))
    ck('derivative current not silently zero',bool(jn) and bool(jr))
    wrong=a.add(component_ref,a.scale(ref['raw_K_chiral'],-2),a.scale(a.adj(ref['raw_K_chiral']),-2))
    ck('wrong gaugino sign changes bulk action',not eq(qn,a.jet_quotient(wrong)[0]))
    ck('no higher fermion derivative or unpriced field',all(len(w)<=3 and sum(not a.sf.odd(t) for t in w)<=1 and sum(len(t.split(':'))-1 for t in w)<=1 and all(a.sf.odd(t) or a.sf.base(t).lstrip('~').startswith(('c','v')) for t in w) for w in native))
    # Independent D/moment extraction, and its retained first derivative current.
    D=a.letter('D');ci=[a.letter('c'+str(j)) for j in range(3)];bc=[a.adj(c) for c in ci]
    draw={};mu={};jD={}
    for j in range(3):
        draw=a.add(draw,a.scale(a.mul(D,a.comm(ci[j],bc[j])),-s.Rational(1,2)))
        mu=a.add(mu,a.scale(a.comm(ci[j],bc[j]),-s.Rational(1,2)))
        if j<2:
            draw=a.add(draw,a.scale(a.mul(a.op(D,'b'+str(j)),ci[j]),-1/s.sqrt(2)),a.scale(a.mul(bc[j],a.op(D,'d'+str(j))),-1/s.sqrt(2)))
            mu=a.add(mu,a.scale(a.add(a.op(bc[j],'d'+str(j)),a.op(ci[j],'b'+str(j))),1/s.sqrt(2)))
            jD['b'+str(j)]=a.scale(a.trace(a.mul(D,ci[j])),-1/s.sqrt(2))
            jD['d'+str(j)]=a.scale(a.trace(a.mul(bc[j],D)),-1/s.sqrt(2))
    actualD=a.trace({w:c for w,c in ss['K_component'].items() if any(a.sf.base(t)=='D' for t in w)})
    ck('actual K D terms before IBP',eq(actualD,draw))
    ck('actual D moment with retained boundary',eq(draw,a.add(a.mul(D,mu),a.current_div(jD))))
    ck('D commutator cannot be dropped',not eq(draw,a.add(a.mul(D,a.add(mu,a.scale(a.add(*(a.comm(ci[j],bc[j]) for j in range(3))),s.Rational(1,2)))),a.current_div(jD))))
    gaugeDD=a.trace({w:c for w,c in ss['gauge_component'].items() if all(a.sf.base(t)=='D' for t in w)})
    ck('actual vector D Gaussian half',eq(gaugeDD,a.scale(a.trace(a.mul(D,D)),s.Rational(1,2))))
    for j in range(3):
        gj=a.letter('g'+str(j));bg=a.adj(gj)
        actual=a.trace({w:c for w,c in ss['K_component'].items() if len(w)==2 and {a.sf.base(t) for t in w}=={'g'+str(j),'~g'+str(j)}})
        ck('actual chiral auxiliary unit metric '+str(j),eq(actual,a.trace(a.mul(bg,gj))))
    # Actual gauge-vector bosonic field strength, all quartic terms.
    vv=[a.letter('v'+str(j)) for j in range(4)];eta=(-1,1,1,1);YM={}
    for i in range(4):
        for j in range(i+1,4):
            ff=a.add(a.op(vv[j],'e'+str(i)),a.scale(a.op(vv[i],'e'+str(j)),-1),a.scale(a.comm(vv[i],vv[j]),-s.I/2))
            YM=a.add(YM,a.scale(a.trace(a.mul(ff,ff)),-s.Rational(1,2)*eta[i]*eta[j]))
    actualYM=a.body(a.add(ss['gauge_component'],a.scale(gaugeDD,-1)))
    ck('actual full vector Yang Mills action',eq(actualYM,YM))
    # A genuine compact coefficient realizes J. Not a gauge algebra truncation.
    ck('coefficient reader actual compact trace and adjoint',all(s.simplify(s.trace(T[i]*T[j])+int(i==j))==0 for i in range(3) for j in range(3)) and all(zero(X*T[j]-T[j]*X-Td[j]) for j in range(3)))
    rho=native if method=='superfield' else component_ref
    ext=[read_matrix(rho,'external_derivative',j) for j in range(4)]
    extbg=[read_matrix(rho,'external_background',j) for j in range(4)]
    deriv=[read_matrix(rho,'internal_derivative',j) for j in range(4)]
    bg=[read_matrix(rho,'internal_background',j) for j in range(6)]
    for j in range(4):
        ck('actual external gauge covariance '+str(j),zero(ext[j]-extbg[j]))
        ck('actual internal gauge covariance '+str(j),zero(deriv[j]-bg[j]))
    clock=fr['ext'][0];h=[]
    for j in range(4):
        i=j*6;k=(4+j)*6+1;h.append(s.simplify(ext[0][i,k]/clock[i,k]))
    positive=all(x.is_positive is True for x in h)
    ck('actual signed time weights positive',positive)
    M=s.diag(*[v for bar in range(2) for j in range(4) for v in [h[j]]*6])
    ck('complete signed time metric',zero(ext[0]-M*clock))
    N=s.diag(*[v for bar in range(2) for j in range(4) for v in [1/s.sqrt(h[j]) if positive else 1]*6])
    exn=[cm(N*a0*N) for a0 in ext];dn=[cm(N*a0*N) for a0 in deriv];bn=[cm(N*a0*N) for a0 in bg]
    maps=[];chosen=None
    for perm in permutations(range(4)):
        P=s.zeros(48)
        for bar in range(2):
            for j in range(4):
                for k in range(6):P[(4*bar+perm[j])*6+k,(4*bar+j)*6+k]=1
        target=[cm(P.T*x*P) for x in fr['can']]
        phases,why=source.phase_map(bn,target)
        if phases is None:continue
        U=s.diag(*[v for ph in phases+[s.conjugate(z) for z in phases] for v in [ph]*6]);V=P*U
        full=all(zero(x-V.T*y*V) for x,y in zip(bn,fr['can'])) and all(zero(x-V.T*y*V) for x,y in zip(exn,fr['ext'])) and all(zero(x-V.T*y*V) for x,y in zip(dn,fr['can'][:4]))
        maps.append({'permutation':list(perm),'phases':[str(z) for z in phases],'all_conjugates_and_external':full})
        if perm==tuple(range(4)) and full and positive:chosen=(phases,U)
    ck('full positive identity flavour Clifford map',chosen is not None)
    if chosen is not None:
        phases,U=chosen
        # 16 Nambu spin/flavour version and actual physical MW map.
        u16=s.diag(*[v for ph in phases+[s.conjugate(z) for z in phases] for v in [ph]*2])
        phys=cm(fr['S']*u16*fr['S'].H+s.eye(32)-fr['MW'])
        rr=s.kronecker_product(s.eye(4),s.eye(4),s.diag(1,-1));vv0=s.kronecker_product(s.eye(4),s.I*cs[2]*cs[3],s.eye(2))
        ck('actual map full MW C and time isometry',zero(phys.H*phys-s.eye(32)) and zero(fr['B']*phys.conjugate()-phys*fr['B']))
        u2=[cs[0]*cs[1],cs[2]*cs[3],cs[0]*cs[2]+cs[1]*cs[3],cs[0]*cs[3]-cs[1]*cs[2]]
        ck('actual map U2 and R compatible',all(zero(phys*s.kronecker_product(s.eye(4),z,s.eye(2))-s.kronecker_product(s.eye(4),z,s.eye(2))*phys) for z in u2) and zero(phys*rr-rr*phys))
        for ep in (-1,1):
            plane=cm(fr['MW']*(s.eye(32)+ep*rr*vv0)/2)
            ck('actual paired current plane preserved '+str(ep),zero(phys*plane-plane*phys) and zero(plane.H*phys.H*(s.I*fr['G0']*fr['G'][2])*phys*plane))
    # Universal actual normal potential, with full compact curvature.
    xs=[a.letter('X'+str(j)) for j in range(2,6)]
    dx=lambda p:a.op(p,'n2');dy=lambda p:a.op(p,'n3')
    CP=a.scale(a.add(xs[0],a.scale(xs[1],-s.I)),-s.sqrt(2));HP=a.scale(a.add(xs[2],a.scale(xs[3],-s.I)),-s.sqrt(2))
    def xadj(p):return a.clean({tuple(reversed(w)):(-1)**len(w)*s.conjugate(c) for w,c in p.items()})
    BC=xadj(CP);BH=xadj(HP)
    dd=lambda p:a.add(dx(p),a.scale(dy(p),-s.I));bd=lambda p:a.add(dx(p),a.scale(dy(p),s.I))
    mun=a.add(a.scale(a.add(dd(BC),bd(CP)),1/s.sqrt(2)),a.scale(a.add(a.comm(CP,BC),a.comm(HP,BH)),-s.Rational(1,2)))
    Fxy=a.add(dx(xs[1]),a.scale(dy(xs[0]),-1),a.comm(xs[0],xs[1]));C1=a.add(Fxy,a.comm(xs[2],xs[3]))
    DX=lambda p:a.add(dx(p),a.comm(xs[0],p));DY=lambda p:a.add(dy(p),a.comm(xs[1],p))
    C2=a.add(DX(xs[2]),a.scale(DY(xs[3]),-1));C3=a.add(DX(xs[3]),DY(xs[2]))
    bb=a.add(dd(HP),a.scale(a.comm(CP,HP),-1/s.sqrt(2)))
    ck('actual normal moment equals canonical curvature',not a.add(mun,a.scale(C1,-2*s.I)))
    ck('actual normal F source equals canonical derivative',not a.add(bb,a.scale(a.add(C2,a.scale(C3,-s.I)),s.sqrt(2))))
    VN=a.trace(a.add(a.scale(a.mul(mun,mun),s.Rational(1,2)),a.mul(xadj(bb),bb)))
    residual=a.scale(a.trace(a.add(*(a.mul(z,z) for z in (C1,C2,C3)))),-2)
    ck('actual complete normal potential twice residual action',eq(VN,residual))
    noquart=a.add(VN,a.scale(a.trace(a.mul(a.comm(xs[2],xs[3]),a.comm(xs[2],xs[3]))),2))
    ck('normal quartic omission detected',not eq(noquart,residual))
    records['source']={'signed_time_weights':[str(x) for x in h],'all_local_flavour_maps':maps,
        'direct_and_component_bulk_residual':encoded(a.add(qn,a.scale(qr,-1))),
        'native_retained_currents':{k:encoded(v) for k,v in sorted(jn.items())},
        'component_retained_currents':{k:encoded(v) for k,v in sorted(jr.items())},
        'actual_D_moment':encoded(mu),'actual_D_current':{k:encoded(v) for k,v in sorted(jD.items())}}
    records['complete_action_matrices']={'external_derivative':[source.sparse(x) for x in ext],
        'external_background':[source.sparse(x) for x in extbg],'internal_derivative':[source.sparse(x) for x in deriv],
        'internal_background':[source.sparse(x) for x in bg]}
    records['normal']={'source_potential':encoded(VN),'canonical_residual':encoded(residual),
        'factor':'2','scope':'same local normal real action including inherited BOTH-end rough-energy current, not new global vacuum'}
    records['status']='explicit supplied real parent and tested full local dictionary; no printed BHV, singular gauge/domain, global spectrum, SM/three/gravity or genesis acceptance'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(cs,valid,method):
    data=run(cs,valid,method);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
