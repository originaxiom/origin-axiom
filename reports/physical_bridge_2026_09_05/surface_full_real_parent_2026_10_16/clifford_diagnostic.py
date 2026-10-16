"""Sealed coefficient/orientation diagnostic; no superspace producer on import."""
import hashlib,json,sys
from itertools import permutations,product
from pathlib import Path
import sympy as s
from analysis import source,cm,zero,frame
HERE=Path(__file__).resolve().parent
INPUT=HERE/'results/gauge_frame_run/probe.stdout.log'
HASH='cc5b961ae78eb458e031d93f993e2899ee0e91d82f187dc68e2a5fe816f60143'
def mat(rows):return s.SparseMatrix(48,48,{(i,j):s.sympify(v) for i,j,v in rows})
def strip(m):
    a=s.Matrix(16,16,lambda i,j:m[3*i,3*j+1])
    if not zero(m-s.kronecker_product(a,source.J)):raise ValueError('coefficient reader not uniform tensor')
    return a
def exterior():
    from itertools import combinations
    basis=[v for n in range(3) for v in combinations(range(2),n)];es=[]
    for j in range(2):
        e=s.zeros(4)
        for k,v in enumerate(basis):
            if j not in v:e[basis.index(tuple(sorted((j,)+v))),k]=(-1)**sum(x<j for x in v)
        es.append(e)
    return [es[0]-es[0].H,s.I*(es[0]+es[0].H),es[1]-es[1].H,s.I*(es[1]+es[1].H)]
def run():
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    raw=INPUT.read_bytes();ck('frozen complete action record hash',hashlib.sha256(raw).hexdigest()==HASH)
    data=json.loads(raw);mm=data['records']['complete_action_matrices']
    ea=[mat(x) for x in mm['external_derivative']];ia=[mat(x) for x in mm['internal_background']]
    ec=[mat(x) for x in mm['canonical_external']];ic=[mat(x) for x in mm['canonical_internal']]
    flat=[strip(x) for x in ea+ia+ec+ic]
    ck('all twenty coefficient tensors factor exactly',len(flat)==20)
    va=[cm(flat[0].inv()*x) for x in flat[1:10]]
    vc=[cm(flat[10].inv()*x) for x in flat[11:20]]
    for name,vv in [('actual',va),('canonical',vc)]:
        ck(name+' nine Hermitian velocities',all(zero(v-v.H) for v in vv))
        ck(name+' all81 Clifford relations',all(zero(vv[i]*vv[j]+vv[j]*vv[i]-2*int(i==j)*s.eye(16)) for i in range(9) for j in range(9)))
        vol=cm(s.prod(vv));sign=s.simplify(vol[0,0])
        ck(name+' signed central volume',sign in (-1,1) and zero(vol-sign*s.eye(16)))
        records[name+'_volume']=str(sign)
    fr=frame(exterior());swap=fr['Bn']
    ck('same actual canonical target frame',all(zero(a-b) for a,b in zip(ec,fr['ext'])) and all(zero(a-b) for a,b in zip(ic,fr['can'])))
    # Velocities are C-even; the Hamiltonian -i velocity*partial is C-odd.
    ck('actual full Nambu reality on all coefficients',all(zero(swap*v.conjugate()*swap-v) for v in va))
    ck('external matrices identical before any new hatch',all(zero(a-b) for a,b in zip(ea,ec)))
    Qsource=s.diag(*[int(j in (2,3)) for bar in range(2) for j in range(4) for alpha in range(2)])
    ck('actual whole cutoff trace half rank and real',Qsource.rank()==8 and zero(swap*Qsource.conjugate()-Qsource*swap))
    ck('actual cutoff both real normal Green forms zero',all(zero(Qsource*v*Qsource) for v in va[5:7]))
    ck('actual cutoff external and internal tangential action invariant',all(zero(Qsource*v-v*Qsource) for v in va[:5]))
    maps=[];rejections=[]
    for r4,r5 in product((-1,1),repeat=2):
        signs=[1,1,1,1,r4,r5];target=[r*m for r,m in zip(signs,ic)]
        for perm in permutations(range(4)):
            P=s.zeros(48)
            for bar in range(2):
                for j in range(4):
                    for k in range(6):P[(4*bar+perm[j])*6+k,(4*bar+j)*6+k]=1
            ph,why=source.phase_map(ia,[cm(P.T*m*P) for m in target])
            if ph is None:
                rejections.append({'scalar_signs':[r4,r5],'permutation':list(perm),'reason':why});continue
            U=P*s.diag(*[v for z in ph+[s.conjugate(x) for x in ph] for v in [z]*6])
            full=all(zero(a-U.T*b*U) for a,b in zip(ia,target)) and all(zero(a-U.T*b*U) for a,b in zip(ea,ec))
            V=s.zeros(16)
            for bar in range(2):
                for j in range(4):
                    for k in range(2):V[(4*bar+perm[j])*2+k,(4*bar+j)*2+k]=(ph+[s.conjugate(x) for x in ph])[4*bar+j]
            phys=cm(fr['S']*V*fr['S'].H+s.eye(32)-fr['MW'])
            R=s.kronecker_product(s.eye(4),s.eye(4),s.diag(1,-1))
            cs=exterior();u2=[cs[0]*cs[1],cs[2]*cs[3],cs[0]*cs[2]+cs[1]*cs[3],cs[0]*cs[3]-cs[1]*cs[2]]
            vv0=s.kronecker_product(s.eye(4),s.I*cs[2]*cs[3],s.eye(2))
            planes=[]
            for ep in (-1,1):
                Q=cm(fr['MW']*(s.eye(32)+ep*R*vv0)/2)
                planes.append({'epsilon':ep,'preserved':zero(phys*Q-Q*phys),
                    'mapped_to_opposite':zero(phys*Q*phys.H-(fr['MW']-Q)),
                    'target_Green_zero':zero(Q.H*phys.H*(s.I*fr['G0']*fr['G'][2])*phys*Q)})
            image=cm(fr['S']*V*Qsource*V.H*fr['S'].H)
            cutoff_image=[ep for ep in (-1,1) if zero(image-fr['MW']*(s.eye(32)+ep*R*vv0)/2)]
            maps.append({'scalar_signs':[r4,r5],'permutation':list(perm),'phases':[str(x) for x in ph],
                'complete_coefficients':full,'unitary':zero(phys.H*phys-s.eye(32)),
                'C_compatible':zero(fr['B']*phys.conjugate()-phys*fr['B']),
                'R_compatible':zero(phys*R-R*phys),
                'same_U2_generators':all(zero(phys*s.kronecker_product(s.eye(4),z,s.eye(2))-s.kronecker_product(s.eye(4),z,s.eye(2))*phys) for z in u2),
                'paired_planes':planes,'actual_whole_cutoff_image_epsilon':cutoff_image})
    records['hatch_maps']=maps;records['hatch_rejections']=rejections
    records['linear_fixed_orientation_intertwiner_obstructed']=records['actual_volume']!=records['canonical_volume']
    ck('full scalar-sign permutation phase census accounted',len(maps)+len(rejections)==96)
    records['scope']='actual local Clifford realization and bounded scalar-frame hatches; not named U2 bundle/domain or global physics'
    return {'checks':checks,'all_passed':all(checks.values()),'records':records}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
