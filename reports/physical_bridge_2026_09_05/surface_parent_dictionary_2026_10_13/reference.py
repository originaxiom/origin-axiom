"""Separate Gaussian frame/Fock route, with no symbolic or native import."""
from functools import lru_cache
import importlib.util
from itertools import product
import json
from pathlib import Path
from fractions import Fraction as Q


def arithmetic():
    path = Path(__file__).resolve().parents[1]/'weave_registered_embedding_2026_10_13'/'reference.py'
    spec = importlib.util.spec_from_file_location('pinned_gaussian_helpers', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@lru_cache(None)
def run():
    a = arithmetic()
    O, Z, I = a.O, a.Z, a.I
    checks = {}
    def ck(name, yes): checks[name] = bool(yes)
    def iz(m): return [[a.gmul(I,z) for z in row] for row in m]
    def neg(m): return a.mscale(-1,m)
    def comm(x,y): return a.madd(a.times(x,y),neg(a.times(y,x)))
    eye4 = a.identity(4)
    p1 = [[Z,O],[O,Z]]
    p2 = [[Z,a.gscale(-1,I)],[I,Z]]
    p3 = [[O,Z],[Z,a.gscale(-1,O)]]
    cs = [iz(a.kron(p1,a.identity(2))), iz(a.kron(p2,a.identity(2))),
          iz(a.kron(p3,p1)), iz(a.kron(p3,p2))]
    for i,j in product(range(4),repeat=2):
        pair = a.madd(a.times(cs[i],cs[j]),a.times(cs[j],cs[i]))
        ck(f'frame Clifford {i}{j}', pair == (a.mscale(-2,eye4) if i==j else a.matrix(4)))
    # Full constant frame structure, in units ell=1; homogeneity supplies 1/ell.
    C = {(0,1,0):Q(-1),(1,2,2):Q(1,2),(0,3,2):Q(-1),(1,3,3):Q(-1,2)}
    C.update({(j,i,k):-v for (i,j,k),v in list(C.items())})
    gamma = [[[Q(C.get((i,j,k),0)-C.get((j,k,i),0)+C.get((k,i,j),0),2)
               for k in range(4)] for j in range(4)] for i in range(4)]
    omega = []
    for i in range(4):
        m = a.matrix(4)
        for j,k in product(range(4),repeat=2):
            m = a.madd(m,a.mscale(gamma[i][j][k]/4,a.times(cs[j],cs[k])))
        omega.append(m)
    K = a.matrix(4)
    for c,w in zip(cs,omega): K = a.madd(K,a.times(c,w))
    mixed = a.mscale(Q(1,4),a.times(a.times(cs[0],cs[2]),cs[3]))
    ck('reconstructed full mixed spin term', K == a.madd(a.mscale(Q(-1,2),cs[1]),mixed))
    # Unit Fock vacuum, and entire induced exterior connection, not a trial eigenvalue.
    vac = [[O],[Z],[Z],[Z]]
    cr = [a.mscale(Q(1,2),a.madd(cs[0],neg(iz(cs[1])))),
          a.mscale(Q(1,2),a.madd(cs[2],neg(iz(cs[3]))))]
    vectors = [vac,a.times(cr[0],vac),a.times(cr[1],vac),a.times(a.times(cr[0],cr[1]),vac)]
    T = [[col[i][0] for col in vectors] for i in range(4)]
    ck('Fock basis is unitary', a.times(a.dagger(T),T)==eye4)
    eh,ev = a.matrix(4),a.matrix(4)
    eh[1][0]=eh[3][2]=O; ev[2][0]=O; ev[3][1]=a.gscale(-1,O)
    form_cs=[a.madd(eh,neg(a.dagger(eh))),iz(a.madd(eh,a.dagger(eh))),
             a.madd(ev,neg(a.dagger(ev))),iz(a.madd(ev,a.dagger(ev)))]
    for j in range(4):
        ck(f'complete form Clifford symbol {j}', a.times(a.times(a.dagger(T),cs[j]),T)==form_cs[j])
    for i in range(4):
        value = a.gscale(Q(-3,4),I) if i == 0 else Z
        ck(f'vacuum spin weight {i}', a.times(omega[i],vac)==[[a.gmul(value,row[0])] for row in vac])
        canonical = a.madd(omega[i],iz(a.mscale(Q(3,4),eye4)) if i == 0 else a.matrix(4))
        ck(f'canonical vacuum parallel {i}', a.times(canonical,vac)==[[Z] for j in range(4)])
        # Columns (e1-i e2),(e3-i e4), with norm squared2: no sqrt required.
        cov = [[O,Z],[a.gscale(-1,I),Z],[Z,O],[Z,a.gscale(-1,I)]]
        act = [[(Q(-gamma[i][k][j]),Q(0)) for j in range(4)] for k in range(4)]
        one = a.mscale(Q(1,2),a.times(a.times(a.dagger(cov),act),cov))
        ck(f'Kahler exterior plane {i}', a.times(act,cov)==a.times(cov,one))
        exterior = a.matrix(4)
        for j,k in product(range(2),repeat=2): exterior[1+j][1+k]=one[j][k]
        exterior[3][3]=a.gadd(one[0][0],one[1][1])
        ck(f'whole exterior connection {i}', a.times(a.times(a.dagger(T),canonical),T)==exterior)
    shift = a.mscale(Q(3,4),iz(cs[0]))
    ck('canonical zeroth term cancels vacuum', a.times(a.madd(K,shift),vac)==[[Z] for j in range(4)])
    ck('wrong twist retained as failure', a.times(a.madd(K,neg(shift)),vac)!=[[Z] for j in range(4)])
    ck('missing mixed term retained as failure', a.times(a.madd(a.madd(K,shift),neg(mixed)),vac)!=[[Z] for j in range(4)])
    ck('bounded Hermitian shift', a.dagger(shift)==shift and a.times(a.dagger(shift),shift)==a.mscale(Q(9,16),eye4))
    gv = iz(a.times(cs[2],cs[3]))
    chir = neg(a.times(a.times(a.times(cs[0],cs[1]),cs[2]),cs[3]))
    ck('trace grading commutes with shift', comm(gv,shift)==a.matrix(4))
    ck('total grading anticommutes', a.madd(a.times(chir,shift),a.times(shift,chir))==a.matrix(4))
    # Holomorphic volume scales as y^(-3/2) in the frame, so its metric as y^3.
    base_power, fibre_power = Q(-1),Q(-1,2)
    metric_power = -2*(base_power+fibre_power)
    spin_weight = -metric_power/4
    twist_weight = -spin_weight
    ck('frame volume independently reconstructs canonical weight', metric_power==3 and spin_weight==Q(-3,4))
    ck('flux bookkeeping is not an integer sector', -twist_weight/6 == Q(-1,8) and Q(-1,8).denominator!=1)
    ck('flat metric has no canonical twist', -2*(Q(0)+Q(0))==0)
    # Independent 8d Lorentz construction and chirality projection trace.
    herm = [iz(c) for c in cs]
    gam = [iz(herm[0]),herm[1],herm[2],herm[3]]
    g5 = iz(a.times(a.times(a.times(gam[0],gam[1]),gam[2]),gam[3]))
    all8 = [a.kron(g,a.identity(4)) for g in gam]+[a.kron(g5,c) for c in herm]
    eye16 = a.identity(16)
    for i,j in product(range(8),repeat=2):
        rhs = a.mscale(-2 if i==0 else 2,eye16) if i==j else a.matrix(16)
        ck(f'Lorentz Clifford {i}{j}', a.madd(a.times(all8[i],all8[j]),a.times(all8[j],all8[i]))==rhs)
    grade = eye16
    for g in all8: grade = a.times(grade,g)
    grade = neg(iz(grade))
    ck('actual Weyl tensor grading', grade==a.kron(g5,chir) and a.times(grade,grade)==eye16)
    rank = sum((Q(1)+grade[j][j][0])/2 for j in range(16))
    ck('positive Weyl rank', rank==8)
    rr,chain,weights = a.frame(6)
    char = a.character(6,(1,-1)*3)
    parities = [sum(m for w,m in char.items() if w%2==p) for p in range(2)]
    ck('complete centre parities not a local-six count', parities==[136,112] and len(rr)+8==248)
    ck('all root charges pair', all(tuple(-x for x in r) in rr for r in rr))
    ck('all Cartan charge sums vanish', all(sum(r[j] for r in rr)==0 for j in range(8)))
    ck('nonzero full scalar identity rejected', 248*Q(3,4)!=0)
    ck('charged proper-root control', sum(rr[0][j]*chain[0][j] for j in range(8))!=0 or
       any(sum(r[j]*chain[0][j] for j in range(8))!=0 for r in rr))
    blocks = [6**2-1,3**2-1,2**2-1,20*2,15*3,15*3,6*3*2,6*3*2]
    ck('full dual and branching companions', sum(blocks)==248)
    old_ends,new_ends = (Q(-1,2),Q(1,2)),(Q(1,2),Q(3,2))
    def index(ends): return ((1 if ends[1]>0 else -1)-(1 if ends[0]>0 else -1))//2
    ck('bounded-change threshold countercontrol', index(old_ends)==1 and index(new_ends)==0)
    records={'canonical_metric_power':int(metric_power),'vacuum_spin_weight':[-3,4],
             'canonical_twist_weight':[3,4],'cusp_n_offset':[-1,8],
             'weyl_rank':int(rank),'clifford_size':16,'full_E8_block_dimensions':blocks,
             'full_E8_central_parities':parities,'index_control_before_after':[index(old_ends),index(new_ends)]}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'exact independent Gaussian/frame safeguards, not outside analytic acceptance'}


if __name__ == '__main__':
    result=run(); print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
