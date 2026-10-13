"""Exact raw-bilinear/rank audit, not a physical vertex or contour replay."""
import json
import sympy as s

def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    i=s.diag(s.I,-s.I);j=s.Matrix([[0,1],[-1,0]]);k=i*j
    blocks=[j,i,k];rr=s.symbols('r00 r01 r11')
    def residue(M):return M[0,0]*rr[0]+(M[0,1]+M[1,0])*rr[1]+M[1,1]*rr[2]
    Y=s.Matrix(3,3,lambda p,q:residue(blocks[p].T*j*blocks[q]))
    ck('actual quaternion epsilon skew',j.T==-j)
    ck('actual bilinear residue skew in every slot',Y.T==-Y)
    ck('actual residue determinant zero polynomial',s.expand(Y.det())==0)
    ar,ai,br,bi,cr,ci=s.symbols('ar ai br bi cr ci',real=True)
    a,b,c=ar+s.I*ai,br+s.I*bi,cr+s.I*ci
    skew=s.Matrix([[0,a,b],[-a,0,c],[-b,-c,0]])
    q=s.Matrix([c,-b,a]);m=s.expand(a*s.conjugate(a)+b*s.conjugate(b)+c*s.conjugate(c))
    ck('whole complex Hermitian outer product',all(s.expand(v)==0 for v in skew.H*skew-m*s.eye(3)+q*q.H))
    lam=s.Symbol('lambda')
    ck('generic squared singular polynomial',s.expand((skew.H*skew).charpoly(lam).as_expr()-lam*(lam-m)**2)==0)
    sym=s.Matrix([[0,a,b],[a,0,c],[b,c,0]])
    ck('symmetric opposing tensor genuinely different',s.expand(sym.det()-2*a*b*c)==0 and sym.subs({ar:1,ai:0,br:2,bi:0,cr:3,ci:0}).det()!=0)
    ck('no golden all-nonzero spectrum for raw tensor',s.prod([1,(s.sqrt(5)-1)/2,(3-s.sqrt(5))/2])!=0 and skew.det()==0)
    ck('raw entry residues need not vanish',any(v!=0 for v in Y))
    return {'checks':checks,'all_passed':all(checks.values()),'records':{'raw_rank_upper_bound':2,'raw_normalized_singular_values':[1,1,0],'symmetric_control_determinant':12},
            'scope':'literal B1642 raw pairing; no physical route exclusion'}
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));raise SystemExit(0 if r['all_passed'] else 1)
