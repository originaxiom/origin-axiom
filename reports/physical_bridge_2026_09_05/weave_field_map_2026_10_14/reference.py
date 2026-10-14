"""Separate Fraction/Gaussian centre and overlap reconstruction."""
from collections import Counter
from functools import lru_cache
from itertools import product
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def prior():
    p=HERE.parent/'weave_registered_embedding_2026_10_13/reference.py'
    sp=importlib.util.spec_from_file_location('field_map_gaussian_helpers',p)
    h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h);return h

@lru_cache(None)
def run():
    h=prior();checks={}
    def ck(n,v):checks[n]=bool(v)
    rr,chain,ws=h.frame(6);e,_=h.root_data()
    def vec(coeff):return tuple(sum(a*w[j] for a,w in zip(coeff,ws)) for j in range(8))
    q,alt=vec((1,-1)*3),vec((1,1,-1,-1,0,0));weak=h.add(e[3],h.neg(e[4]))
    def joint(x):
        out=Counter((int(h.dot(r,q))%2,int(h.dot(r,x))%2) for r in rr);out[(0,0)]+=8;return out
    orig,other=joint(weak),joint(alt)
    ck('Fraction root centre equality',all(h.dot(r,h.add(q,h.neg(weak)))%2==0 for r in rr))
    ck('whole original centre population',orig==Counter({(0,0):136,(1,1):112}) and len(rr)==240)
    ck('alternative is a nonuniversal counterexample',other[(0,1)]>0 and other[(1,0)]>0 and sum(other.values())==248)
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]];b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]];I=h.identity(2)
    C={(0,0):I,(1,0):b,(0,1):a,(1,1):h.times(a,b)};par=[(1,0),(0,1),(1,1)]
    def transpose(m):return list(map(list,zip(*m)))
    def equalinv(B,herm=False):
        return all(h.times(h.times(h.dagger(g) if herm else transpose(g),B),g)==B for g in [a,b])
    allowed_count=0;diags=[]
    for c1,c2,p in product(C,C,par):
        BB=h.times(h.times(h.times(transpose(C[c1]),b),C[p]),C[c2])
        HH=h.times(h.times(h.dagger(C[c2]),C[p]),C[c1])
        allowed=tuple((c1[j]+c2[j])%2 for j in (0,1))==p
        ck(f'full exact channel {c1},{c2},{p}',equalinv(BB)==equalinv(HH,True)==allowed)
        if allowed:
            allowed_count+=1
            ck(f'skew and scalar channel {c1},{c2},{p}',BB==h.mscale(-1,transpose(BB)) and HH in [I,h.mscale(-1,I)])
    for w in par:
        Y=[[h.Z for _ in par] for _ in par]
        for j,r in enumerate(par):
            for k,t in enumerate(par):
                c1=tuple((r[n]+w[n])%2 for n in (0,1))
                if tuple((c1[n]+t[n])%2 for n in (0,1))==w:
                    Y[j][k]=h.times(h.times(h.dagger(C[t]),C[w]),C[c1])[0][0]
        ck('separate unitary overlap '+str(w),h.times(h.dagger(Y),Y)==h.identity(3))
        diags.append([int(Y[j][j][0]) for j in range(3)])
    ck('four flat twists keep odd puncture centre',all(h.times(h.times(h.times(h.mscale(sa,a),h.mscale(sb,b)),h.dagger(h.mscale(sa,a))),h.dagger(h.mscale(sb,b)))==h.mscale(-1,I) for sa,sb in product((-1,1),repeat=2)))
    ck('added tensor factor comparator changes centre',h.kron(h.mscale(-1,I),h.mscale(-1,I))==h.identity(4))
    # Reconstruct the alternative family sl2 before its literal conjugation.
    H=h.block_diag([I,h.mscale(-1,I),h.mscale(0,I)]);Ep=h.matrix(6)
    Ep[0][2]=Ep[1][3]=h.O;Em=h.dagger(Ep)
    sub=lambda x,y:h.madd(x,h.mscale(-1,y))
    ck('actual alternative Lie brackets',sub(h.times(H,Ep),h.times(Ep,H))==h.mscale(2,Ep) and sub(h.times(Ep,Em),h.times(Em,Ep))==H)
    compatibility={k:(-1)**p==-1 for k,p in {'Q':1,'L':1,'u^c':0,'d^c':0,'e^c':0,'neutral_singlet':0}.items()}
    ck('necessary sign test not all matter',sum(compatibility.values())==2)
    pack=lambda c:[[list(k),v] for k,v in sorted(c.items())]
    records={'original_joint_parities':pack(orig),'alternative_joint_parities':pack(other),
             'uniform_rho_necessary_compatibility':compatibility,'allowed_overlap_channels':allowed_count,
             'normalized_Hermitian_diagonals':diags}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'separate exact roots and overlaps; the upstream numerical functions are not executed by this route'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
