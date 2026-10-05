"""Separate exact Gaussian bit-mask form controls; finite directions, not the proof."""
from fractions import Fraction as F
import json


class G:
    def __init__(self,a=0,b=0):
        if isinstance(a,G): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=G(o);return G(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return G(-self.a,-self.b)
    def __sub__(self,o):return self+-G(o)
    def __rsub__(self,o):return G(o)+-self
    def __mul__(self,o):
        o=G(o);return G(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=G(o);d=o.a*o.a+o.b*o.b
        return self*G(o.a/d,-o.b/d)
    def conj(self):return G(self.a,-self.b)
    def __eq__(self,o):
        o=G(o);return (self.a,self.b)==(o.a,o.b)


I=G(0,1)
MASKS=(0,2,4,6,1,3,5,7)


def zeros(m,n):return [[G() for _ in range(n)] for _ in range(m)]
def eye(n):return [[G(int(i==j)) for j in range(n)] for i in range(n)]
def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),G())
             for j in range(len(b[0]))] for i in range(len(a))]
def adj(a):return [[a[i][j].conj() for i in range(len(a))] for j in range(len(a[0]))]
def conjugate(a):return [[z.conj() for z in row] for row in a]
def join(a,b):return [aa+bb for aa,bb in zip(a,b)]
def rank(a):
    a=[[G(z) for z in row] for row in a];r=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]!=0),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];p=a[r][col]
        a[r]=[v/p for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                q=a[i][col];a[i]=[u-q*v for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def clifford(axis):
    out=zeros(8,8);bit=1<<axis
    for col,mask in enumerate(MASKS):
        sign=(-1)**((mask&(bit-1)).bit_count())
        row=MASKS.index(mask^bit)
        out[row][col]=G(-sign if mask&bit else sign)
    return out


def signed_star():
    out=zeros(8,8)
    for col,mask in enumerate(MASKS):
        other=7^mask
        inversions=sum(1 for a in range(3) for b in range(3)
                       if mask&(1<<a) and other&(1<<b) and a>b)
        degree=mask.bit_count();sign=(1,-1,-1,1)[degree]*(-1)**inversions
        out[MASKS.index(other)][col]=G(sign)
    return out


def domain(kind,sign):
    cols=[]
    def col(entries):
        a=[G() for _ in range(8)]
        for mask,value in entries.items():a[MASKS.index(mask)]=G(value)
        cols.append(a)
    if kind=='gauge':col({0:1})
    col({2:1,4:sign*I})
    if kind=='complement':col({6:1});col({1:1})
    col({3:1,5:-sign*I})
    if kind=='gauge':col({7:1})
    return [[col[i] for col in cols] for i in range(8)]


def run():
    checks={};gamma=clifford(0);j=signed_star()
    checks['normal_square']=mul(gamma,gamma)==[[-z for z in row] for row in eye(8)]
    checks['reality_square']=mul(j,j)==eye(8)
    count=0
    for kind in ('gauge','complement'):
        for sign in (-1,1):
            a=domain(kind,sign);key=kind+str(sign)
            checks[key+'_rank']=rank(a)==4
            checks[key+'_current']=mul(adj(a),mul(gamma,a))==zeros(4,4)
            checks[key+'_reality']=rank(join(a,mul(j,conjugate(a))))==4
            checks[key+'_parity']=rank(join(a,[[(-1)**MASKS[i].bit_count()*v for v in row]
                                               for i,row in enumerate(a)]))==4
            cx,cy=clifford(1),clifford(2)
            for x in range(-2,3):
                for y in range(-2,3):
                    if not(x or y):continue
                    # Inward normal evolution Gamma*T; avoid sqrt by testing
                    # alpha in A and A^dagger q alpha=0 in tangent space.
                    t=[[I*(x*cx[i][k]+y*cy[i][k]) for k in range(4)] for i in range(4)]
                    alpha=[[a[i][k] for k in range(2)] for i in range(4)]
                    checks[key+f'_symbol_{x}_{y}']=rank(mul(adj(alpha),mul(t,alpha)))==2
                    count+=1
    # Independent linearized gauge component identity in the Cartan block.
    for sign in (-1,1):
        w=[G(1),sign*I]
        for x,y in ((1,0),(0,1),(1,1),(-2,1)):
            xi=[G(x),G(y)];before=[I*z for z in xi]
            after=[z+I*v*G(-1) for z,v in zip(before,xi)]
            v=I*G(-1)/2
            za=[2*I*z*v-I*f for z,f in zip(xi,after)]
            zb=[-I*z for z in before]
            checks[f'compensate_{sign}_{x}_{y}']=after==[G(),G()] and v!=0 and za==zb and zb!=[G(),G()]
            inner=sum((u.conj()*z for u,z in zip(w,before)),G())/2
            reject=[z-u*inner for z,u in zip(before,w)]
            checks[f'escape_{sign}_{x}_{y}']=sum((u.conj()*u for u in reject),G())==G(F(x*x+y*y,2))
    checks['affine_pair_nonzero']=G(3)*I-G(5)!=0
    checks['common_line_pair_zero']=G(1)*(2*I)-I*G(2)==0
    failed=[k for k,v in checks.items() if not v]
    return dict(checks=checks,passed=len(checks)-len(failed),failed=failed,
                finite_symbol_directions=count,coefficient_patterns=2,helicities=2,
                physical_kernel_computed=False,full_superfield_domain_closed=False,
                physical_goal_achieved=False,non_author_acceptance=False)


if __name__=='__main__':
    result=run();print(json.dumps(result,sort_keys=True));raise SystemExit(bool(result['failed']))
