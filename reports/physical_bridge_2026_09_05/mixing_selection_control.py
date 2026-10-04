"""R83 separately coded Fraction comparators; no native imports or writes."""
from fractions import Fraction as F
import itertools
import json


def run():
    checks=[]
    for a,d,x in itertools.product((F(0),F(1)),(F(-1),F(0),F(3)),(F(-2),F(1),F(4))):
        y=F(0);j1=F(2);j2=F(-3);c=F(1)
        gy=2*a*y+4*c*y**3+2*d*x*x*y-j2
        gx_yaxis=2*a*y+4*c*y**3+2*d*y*x*x-j1
        checks.extend((gy==-j2,gx_yaxis==-j1))
    scalar_count=len(checks)
    for u,v,w in itertools.product(map(F,range(-2,3)),repeat=3):
        b1=-(u+v)/2;b2=(-u+v)/2
        residual=(b1+b2+u,b1-b2+v,w)
        frozen=u*u+v*v+w*w;relaxed=sum(z*z for z in residual)
        normal=(residual[0]+residual[1],residual[0]-residual[1])
        checks.extend((residual==(F(0),F(0),w),relaxed==w*w and relaxed<=frozen,normal==(F(0),F(0))))
    projection_count=len(checks)-scalar_count
    diag=(F(2),F(3),F(5),F(7),F(1,210))
    determinant=F(1)
    for z in diag:determinant*=z
    checks.extend((determinant==1 and len(set(diag))==5,all(z!=1 and 1/z!=1 for z in diag)))
    return {'passed':sum(checks),'total':len(checks),'scalar_predicates':scalar_count,'projection_predicates':projection_count,'flag_predicates':2,'all_checks_pass':all(checks),'scope':'separate same-author exact implementation, not independent analytic acceptance'}


if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if out['all_checks_pass'] else 1)
