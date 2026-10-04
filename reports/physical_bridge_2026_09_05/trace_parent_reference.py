"""R95 separate Fraction route: no native/R94 import and no file writes.

Same author, not independent analytic acceptance. Rational seeds are
representation controls, NOT certified complete hyperbolic holonomies.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
import json


def ident(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def trans(A):return [list(x) for x in zip(*A)]
def mult(A,B):return [[sum(x*y for x,y in zip(a,b)) for b in zip(*B)] for a in A]
def plus(A,B,scale=1):return [[a+scale*b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(A,c):return [[c*x for x in row] for row in A]
def tr(A):return sum(A[i][i] for i in range(len(A)))
def bracket(A,B):return plus(mult(A,B),mult(B,A),-1)
def zeros(n,m=None):return [[Q(0) for j in range(m or n)] for i in range(n)]


def rank(A):
    a=[row[:] for row in A];n=len(a);m=len(a[0]);r=0
    for j in range(m):
        p=next((i for i in range(r,n) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r


def sy(A,n=4):
    a,b=A[0];c,d=A[1]
    return [[sum(Q(comb(n-j,i)*comb(j,k-i))*a**(n-j-i)*c**i*b**(j-k+i)*d**(k-i)
                 for i in range(max(0,k-j),min(k,n-j)+1))
             for j in range(n+1)] for k in range(n+1)]


def gens(n=4):
    E=zeros(n+1);F=zeros(n+1);H=zeros(n+1)
    for j in range(n):E[j][j+1]=Q(j+1);F[j+1][j]=Q(n-j)
    for j in range(n+1):H[j][j]=Q(n-2*j)
    return E,F,H


def exterior(X):
    n=len(X);pairs=list(combinations(range(n),2));W=zeros(len(pairs))
    for col,(i,j) in enumerate(pairs):
        for k in range(n):
            for a,b,v in ((k,j,X[k][i]),(i,k,X[k][j])):
                if a!=b:W[pairs.index(tuple(sorted((a,b))))][col]+=(v if a<b else -v)
    return W


def ad(X):
    n=len(X);A=zeros(n*n)
    for i,j in product(range(n),repeat=2):
        B=zeros(n);B[i][j]=1;v=bracket(X,B)
        for a,b in product(range(n),repeat=2):A[a*n+b][i*n+j]=v[a][b]
    return A


def kernels(G):
    n=len(G[0]);stack=lambda mats:[row for M in mats for row in M]
    return n-rank(stack(G)),n*(n-1)//2-rank(stack([exterior(X) for X in G])),n*n-rank(stack([ad(X) for X in G]))-1


def checks():
    out={};E,F,H=gens();e,f,h=gens(1);G=(E,F,H);small=(e,f,h)
    out['Lie_HE']=bracket(H,E)==scale(E,2)
    out['Lie_HF']=bracket(H,F)==scale(F,-2)
    out['Lie_EF']=bracket(E,F)==H
    out['PSL_descent']=sy(scale(ident(2),-1))==ident(5)
    out['odd_power_control']=sy(scale(ident(2),-1),3)==scale(ident(4),-1)
    # Exact derivative of a degree<=4 curve, derived by interpolation.
    weights=[-Q(25,12),Q(4),-Q(3),Q(4,3),-Q(1,4)]
    derivative=zeros(5)
    for t,w in enumerate(weights):derivative=plus(derivative,scale(sy(plus(ident(2),scale(e,Q(t)))),w))
    out['tensor_derives_E']=derivative==E
    seeds=[([[Q(1),Q(1)],[Q(0),Q(1)]],[[Q(1),Q(0)],[Q(1),Q(1)]]),
           ([[Q(2),Q(0)],[Q(0),Q(1,2)]],[[Q(1),Q(1)],[Q(1),Q(2)]]),
           ([[Q(0),Q(-1)],[Q(1),Q(0)]],[[Q(2),Q(3)],[Q(1),Q(2)]])]
    for i,(A,B) in enumerate(seeds):
        out['homomorphism_'+str(i)]=sy(mult(A,B))==mult(sy(A),sy(B))
        x,y,z=tr(A),tr(B),tr(mult(A,B))
        AP,BP=A,mult(A,B)
        out['Nielsen_L_'+str(i)]=(tr(AP),tr(BP),tr(mult(AP,BP)))==(x,z,x*z-y)
        AT,BT=mult(A,B),A
        out['Nielsen_T_'+str(i)]=(tr(AT),tr(BT),tr(mult(AT,BT)))==(z,x,x*z-y)
        for a,b in product((-1,1),repeat=2):
            out['lost_lift_'+str(i)+str(a)+str(b)]=sy(scale(A,a))==sy(A) and sy(scale(B,b))==sy(B)
    metric=zeros(5);inverse_metric=zeros(5);J=zeros(5)
    for j in range(5):
        metric[j][j]=Q(1,comb(4,j));inverse_metric[j][j]=Q(comb(4,j));J[j][4-j]=(-1)**j*Q(1,comb(4,j))
    out['binomial_dagger']=mult(inverse_metric,mult(trans(E),metric))==F
    out['actual_dual_metric']=mult(trans(J),mult(inverse_metric,J))==metric
    out['symmetric_J']=trans(J)==J
    for i,X in enumerate(G):out['duality_'+str(i)]=plus(mult(trans(X),J),mult(J,X))==zeros(5)
    rot=[[Q(3,5),Q(4,5)],[-Q(4,5),Q(3,5)]]
    out['unitary_group_metric']=mult(trans(sy(rot)),mult(metric,sy(rot)))==metric
    for i,j in product(range(3),repeat=2):
        a=tr(mult(G[i],G[j]));b=tr(mult(small[i],small[j]))
        parent=tr(mult(ad(G[i]),ad(G[j])))+20*a+10*tr(mult(exterior(G[i]),exterior(G[j])))
        out['trace20_'+str(i)+str(j)]=a==20*b
        out['trace1200_'+str(i)+str(j)]=parent==1200*b
    roots=[]
    for i,j in combinations(range(8),2):
        for a,b in product((-1,1),repeat=2):
            r=[Q(0)]*8;r[i]=Q(a);r[j]=Q(b);roots.append(r)
    roots.extend([[Q(a,2) for a in signs] for signs in product((-1,1),repeat=8) if sum(a<0 for a in signs)%2==0])
    for i,j in product(range(8),repeat=2):
        out['E8_trace_tensor_'+str(i)+str(j)]=sum(r[i]*r[j] for r in roots)==Q(60 if i==j else 0)
    out['full_sectors_gauge24']=kernels(G)==(0,0,0)
    fake=[]
    for X in gens(3):
        Y=zeros(5)
        for i,j in product(range(4),repeat=2):Y[i][j]=X[i][j]
        fake.append(Y)
    k=kernels(fake);out['four_plus_line_gauge55']=24+20*k[0]+10*k[1]+k[2]==55
    norm=(tr(mult(plus(E,F),plus(E,F)))-tr(mult(plus(E,F,-1),plus(E,F,-1)))+tr(mult(H,H)))/4
    out['positive_geometry_norm30']=norm==30
    out['moment_commutator_cancellation']=plus(scale(H,-2),scale(bracket(E,F),2))==zeros(5)
    out['missing_commutator_fails']=scale(H,-2)!=zeros(5)
    # Derive leaf and boundary scales rather than insert an empirical target.
    ratio=tr(mult(H,H))/tr(mult(h,h))
    root_ratio=Q(60);goldman_trace_factor=Q(2);cs_variation_factor=Q(-2)
    out['relative_form2400']=ratio*root_ratio*goldman_trace_factor==2400
    out['boundary_form_minus4800']=cs_variation_factor*ratio*root_ratio*goldman_trace_factor==-4800
    out['half_trace_control_rejected']=cs_variation_factor*ratio*root_ratio!=-4800
    return out


def report():
    values=checks()
    return dict(scope='R95 bounded Fraction tensor/root/kernel controls; same author',checks=values,
                passed=sum(values.values()),total=len(values),failed=[k for k,v in values.items() if not v],
                non_author_acceptance=False,physical_goal_achieved=False)


if __name__=='__main__':
    d=report();print(json.dumps(d,sort_keys=True));raise SystemExit(0 if not d['failed'] else 1)
