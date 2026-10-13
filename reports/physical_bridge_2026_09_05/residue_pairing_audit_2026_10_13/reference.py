"""Separate exact Gaussian rank/norm controls without symbolic imports."""
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

def run():
    p=Path(__file__).resolve().parents[1]/'weave_registered_embedding_2026_10_13/reference.py'
    sp=importlib.util.spec_from_file_location('gaussian_helpers',p);a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
    O,Z,I=a.O,a.Z,a.I
    checks={}
    def ck(n,v):checks[n]=bool(v)
    def neg(m):return a.mscale(-1,m)
    def trans(m):return [list(r) for r in zip(*m)]
    i=[[I,Z],[Z,a.gscale(-1,I)]];j=[[Z,O],[a.gscale(-1,O),Z]];k=a.times(i,j)
    blocks=[j,i,k]
    matrices=[[a.times(a.times(trans(cp),j),cq) for cq in blocks] for cp in blocks]
    for p,q in [(p,q) for p in range(3) for q in range(3)]:
        ck(f'actual coefficient transpose {p}{q}',matrices[p][q]==neg(trans(matrices[q][p])))
    def det3(m):
        import itertools
        out=Z
        for perm in itertools.permutations(range(3)):
            t=O
            for row,col in enumerate(perm):t=a.gmul(t,m[row][col])
            sign=(-1)**sum(perm[x]>perm[y] for x in range(3) for y in range(x+1,3))
            out=a.gadd(out,a.gscale(sign,t))
        return out
    for n,(aa,bb,cc) in enumerate([(O,a.gscale(2,O),a.gscale(3,O)),(I,O,a.gadd(O,I)),(a.gscale(Q(1,3),I),a.gscale(Q(2,5),O),a.gscale(Q(-3,7),I))]):
        m=[[Z,aa,bb],[a.gscale(-1,aa),Z,cc],[a.gscale(-1,bb),a.gscale(-1,cc),Z]]
        ck(f'skew determinant control {n}',det3(m)==Z)
        q=[[cc],[a.gscale(-1,bb)],[aa]]
        norm=a.gadd(a.gadd(a.gmul(aa,a.conj(aa)),a.gmul(bb,a.conj(bb))),a.gmul(cc,a.conj(cc)))
        gram=a.times(a.dagger(m),m)
        rhs=a.madd([[norm if r==c else Z for c in range(3)] for r in range(3)],neg(a.times(q,a.dagger(q))))
        ck(f'exact Hermitian spectrum identity {n}',gram==rhs)
    sym=[[Z,O,a.gscale(2,O)],[O,Z,a.gscale(3,O)],[a.gscale(2,O),a.gscale(3,O),Z]]
    ck('symmetric opposing determinant twelve',det3(sym)==a.gscale(12,O))
    return {'checks':checks,'all_passed':all(checks.values()),'records':{'raw_rank_upper_bound':2,'raw_normalized_singular_values':[1,1,0],'symmetric_control_determinant':12},'scope':'finite Gaussian safeguards, no contour or physical vertex reconstruction'}
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));raise SystemExit(0 if r['all_passed'] else 1)
