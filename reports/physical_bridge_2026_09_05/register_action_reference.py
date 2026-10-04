"""Same-author separate Fraction/matrix/quadrature route; imports no native code."""
from fractions import Fraction as F
from itertools import product
import json
import mpmath as mp


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def inv(a):
    return [[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def pairing(x,y,z):
    return [[0,2*z-x*y,x*z-2*y],[x*y-2*z,0,2*x-y*z],[2*y-x*z,y*z-2*x,0]]


def transpose(a):
    return list(map(list,zip(*a)))


def matrix_update(A,B,name):
    if name=='L':return A,mul(A,B)
    if name=='R':return mul(A,B),B
    if name=='P':return B,A
    if name=='Li':return A,mul(inv(A),B)
    if name=='Ri':return mul(A,inv(B)),B
    raise ValueError(name)


def trace_update(x,y,z,name):
    if name=='L':return (x,z,x*z-y),[[1,0,0],[0,0,1],[z,-1,x]],1
    if name=='R':return (z,y,y*z-x),[[0,0,1],[0,1,0],[-1,z,y]],1
    if name=='P':return (y,x,z),[[0,1,0],[1,0,0],[0,0,1]],-1
    if name=='Li':return (x,x*y-z,y),[[1,0,0],[y,x,-1],[0,1,0]],1
    if name=='Ri':return (x*y-z,y,x),[[y,x,-1],[0,1,0],[1,0,0]],1
    raise ValueError(name)


def run():
    out={}
    def record(name,predicate):
        if name in out:raise ValueError('duplicate check')
        out[name]=bool(predicate)
    seeds=[(F(2),F(1,2)),(F(3),F(2,3)),(F(5,2),F(3,4))]
    names=('L','R','P','Li','Ri')
    words=[w for n in range(4) for w in product(names,repeat=n)]
    for j,(a,b) in enumerate(seeds):
        x=a+1/a;beta=a-1/a
        initial_A=[[a,F(0)],[F(0),1/a]]
        initial_B=[[x*b/beta,2/beta],[2/beta,x/(beta*b)]]
        for k,word in enumerate(words):
            A,B=initial_A,initial_B
            state=(tr(A),tr(B),tr(mul(A,B)))
            sign=1
            for name in word:
                old=pairing(*state)
                state,J,epsilon=trace_update(*state,name)
                transported=mul(mul(J,old),transpose(J))
                expected=[[epsilon*v for v in row] for row in pairing(*state)]
                if transported!=expected:raise AssertionError(('Poisson',j,k,name))
                sign*=epsilon
                A,B=matrix_update(A,B,name)
            actual=(tr(A),tr(B),tr(mul(A,B)))
            prefix=str(j)+'_'+str(k)
            record('matrix_trace_'+prefix,actual==state)
            X,Y,Z=state
            record('nonlinear_leaf_'+prefix,X*X+Y*Y+Z*Z-X*Y*Z==0)
            record('commutator_'+prefix,tr(mul(mul(mul(A,B),inv(A)),inv(B)))==-2)
            record('sheet_transport_'+prefix,sign==(-1)**word.count('P'))
    mp.mp.dps=80
    def close(a,b,tol='1e-60'):return abs(a-b)<mp.mpf(tol)
    def reconstruction(q,p):
        return (2*mp.cosh(q),2*mp.coth(q)*mp.cosh(p),2*mp.coth(q)*mp.cosh(p+q))
    def pq(q,Q,branch=1):
        u,v=mp.sinh(q),mp.sinh(Q);c,C=mp.cosh(q),mp.cosh(Q)
        h=branch*mp.sqrt(u*u*v*v-1)
        return mp.log((C*u+h)/c)-q,mp.log((c*v+h)/C)
    q0=Q0=mp.log(3)
    def primitive(q,Q):
        return mp.quad(lambda t:pq(t,Q0)[0],[q0,q])+mp.quad(lambda t:pq(q,t)[1],[Q0,Q])
    for j,(q,Q) in enumerate([(q0,Q0),(q0+mp.mpf('.02'),Q0-mp.mpf('.03')),
                              (q0-mp.mpf('.025'),Q0+mp.mpf('.015'))]):
        p,P=pq(q,Q)
        old=reconstruction(q,p);new=reconstruction(Q,P)
        wanted=(old[2],old[0],old[0]*old[2]-old[1])
        for i in range(3):record('real_reconstruct_'+str(j)+'_'+str(i),close(new[i],wanted[i]))
        record('quadrature_Fq_'+str(j),close(mp.diff(lambda t:primitive(t,Q),q),p,'1e-50'))
        record('quadrature_FQ_'+str(j),close(mp.diff(lambda t:primitive(q,t),Q),P,'1e-50'))
        cross=mp.sinh(q)*mp.sinh(Q)/mp.sqrt(mp.sinh(q)**2*mp.sinh(Q)**2-1)
        record('quadrature_mixed_'+str(j),close(mp.diff(lambda t:pq(t,Q)[1],q),cross))
        record('quadrature_wrong_sign_'+str(j),not close(mp.diff(lambda t:pq(t,Q)[1],q),-cross))
    for sign in (1,-1):
        x=(3+sign*mp.j*mp.sqrt(3))/2;y=mp.conj(x)
        q=mp.acosh(x/2);Q=mp.acosh(y/2)
        # Choose h from the actual old y, not independently in each log.
        h=(x*y/2-y)/2;c,C=x/2,y/2;u,v=mp.sinh(q),mp.sinh(Q)
        p=mp.log((C*u+h)/c)-q;P=mp.log((c*v+h)/C)
        old=reconstruction(q,p);new=reconstruction(Q,P)
        for i,value in enumerate((x,y,y)):record('complex_old_'+str(sign)+'_'+str(i),close(old[i],value))
        for i,value in enumerate((y,x,x)):record('complex_new_'+str(sign)+'_'+str(i),close(new[i],value))
        record('complex_nonzero_discriminant_'+str(sign),close(u*u*v*v-1,-mp.mpf(3)/16) and abs(h)>mp.mpf('.1'))
        wrongp=mp.log((C*u-h)/c)-q
        record('wrong_complex_branch_'+str(sign),not close(reconstruction(q,wrongp)[1],y))
    old=pairing(F(3),F(3),F(3));state,J,epsilon=trace_update(F(3),F(3),F(3),'P')
    record('untracked_sheet_rejected',mul(mul(J,old),transpose(J))!=pairing(*state))
    record('correct_tracked_sheet',mul(mul(J,old),transpose(J))==[[-v for v in row] for row in pairing(*state)])
    record('singular_origin_not_symplectic',pairing(0,0,0)==[[0]*3 for _ in range(3)])
    p,P=pq(q0,Q0)
    record('wrong_DEL_has_nonzero_matching_residual',abs(2*P)>mp.mpf('.1'))
    failed=[name for name,value in out.items() if not value]
    return dict(checks=out,total=len(out),passed=sum(out.values()),failed=failed,
                finite_word_seeds=len(seeds),finite_words_per_seed=len(words),
                author_independent=False,analytic_proof_by_sampling=False,physical_goal_achieved=False)


if __name__=='__main__':
    data=run()
    print(json.dumps(data,sort_keys=True))
    raise SystemExit(0 if not data['failed'] else 1)
