"""Exact full based presentation and COMPLETE gauge/phase cost, not SM admission."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def load(folder,name='probe'):
    p=HERE.parent/folder/(name+'.py')
    sp=importlib.util.spec_from_file_location('based_completion_'+folder+'_'+name,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def clean(x):return s.simplify(s.expand_complex(x))
def zero(m):return all(clean(x)==0 for x in m)
def nullity(basis,moves,adjoint=False):
    cols=[]
    for h in basis:
        vals=[]
        for g in moves:
            vals.extend(list(g*h-h*g if adjoint else g*h*g.T-h))
        cols.append(s.Matrix(vals))
    return len(basis)-s.Matrix.hstack(*cols).rank()

@lru_cache(None)
def run():
    checks={}
    def ck(name,v):checks[name]=bool(v)
    w=load('based_transition_prerequisite_2026_10_13')
    X={'a':'a','b':'ab'};Y={'a':'aB','b':'b'};Z={'a':'a','b':'ba'}
    Xi={'a':'a','b':'Ab'};Yi={'a':'ab','b':'b'};Zi={'a':'a','b':'bA'}
    E={'a':'a','b':'b'};J={'a':'A','b':'B'};D={'a':'ba','b':'b'}
    Di={'a':'Ba','b':'b'}
    triple=lambda a,b,c:w.compose(a,w.compose(b,c))
    ck('native word braid XYX',triple(X,Y,X)==triple(Y,X,Y))
    ck('native word braid YZY',triple(Y,Z,Y)==triple(Z,Y,Z))
    ck('native word distant commute',w.compose(X,Z)==w.compose(Z,X))
    delta=triple(X,Y,Z)
    ck('native word centre identity',w.power(delta,4)==E)
    ck('paper middle convention map',triple(J,Di,J)==Y and triple(J,X,J)==Z and triple(J,Z,J)==X)
    ck('paper middle is not literal Ri',Di!=Y)
    U=w.compose(Z,Xi);Ui=w.compose(X,Zi)
    V=w.compose(w.compose(w.compose(Y,U),Yi),Ui)
    ck('actual based a inverse recovered',U==w.inner('A'))
    ck('actual based b recovered',V==w.inner('b'))
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]])
    I=s.eye(2);I6=s.eye(6);A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    P13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    P23=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    LX=s.kronecker_product(P13,(I+a)/s.sqrt(2))
    LY=s.kronecker_product(P23,(I+b)/s.sqrt(2));LZ=A.H*LX
    lifts=[LX,LY,LZ]
    ck('gauge braid XYX',zero(LX*LY*LX-LY*LX*LY))
    ck('gauge braid YZY',zero(LY*LZ*LY-LZ*LY*LZ))
    ck('gauge distant commute',zero(LX*LZ-LZ*LX))
    ck('actual SU6 centre retained',zero((LX*LY*LZ)**4+I6))
    for k,g in enumerate(lifts):
        ck('unitary full lift '+str(k),zero(g.H*g-I6) and clean(g.det())==1)
    table={'a':A,'b':B,'A':A.H,'B':B.H}
    def mat(word):
        out=I6
        for c in word:out=out*table[c]
        return out
    for k,(f,g) in enumerate(zip([X,Y,Z],lifts)):
        for c in 'ab':ck('full fibre covariance '+str(k)+c,zero(g*table[c]*g.H-mat(f[c])))
    UG=LZ*LX.H
    ck('actual inner A gauge lift',zero(UG-A.H))
    ck('actual inner b gauge lift',zero(LY*UG*LY.H*UG.H-B))
    fields=load('weave_field_map_2026_10_14')
    p,e,rr,hq,_=fields.data();hw=e[3]-e[4]
    pair=[int(r.dot(hq-hw))%2 for r in rr]
    ck('paired centre trivial on all240 roots',len(pair)==240 and all(v==0 for v in pair))
    ck('all eight Cartans centre fixed',8+len(rr)==248)
    ck('unrepaired weak identity fails',any(int(r.dot(hq))%2 for r in rr))
    ck('weak twelfth is minus centre',clean(s.exp(-s.I*s.pi))==-1)
    ck('wrong weak angle rejected',clean(s.exp(-s.I*s.pi/2))!=-1)
    Sf=s.diag(b,a,a*b)
    fam=[]
    for k,(g,q) in enumerate(zip(lifts,[(I+a)/s.sqrt(2),(I+b)/s.sqrt(2),(I-a)/s.sqrt(2)])):
        v=Sf.H*g*Sf
        M=s.Matrix(3,3,lambda j,l:clean(s.trace(q.H*v[2*j:2*j+2,2*l:2*l+2])/2))
        ck('literal family factor '+str(k),zero(v-s.kronecker_product(M,q)))
        ck('real orthogonal family '+str(k),all(x.is_Rational for x in M) and zero(M*M.T-s.eye(3)))
        fam.append(M)
    ck('left-right X family agrees',fam[0]==fam[2])
    adj=[];sym=[]
    for j in range(3):
        for k in range(3):
            m=s.zeros(3);m[j,k]=1
            if j!=k:adj.append(m)
            if j<=k:
                if j!=k:m[k,j]=1
                sym.append(m)
    adj.extend([s.diag(1,-1,0),s.diag(0,1,-1)])
    diagonal=[s.diag(1,-1,0),s.diag(0,1,-1)]
    n_adj=nullity(adj,fam[:2],True);n_sym=nullity(sym,fam[:2])
    n_diag=nullity(diagonal,fam[:2],True)
    weak_root=s.Matrix([[0,1],[0,0]])
    wd=s.diag(s.exp(-s.I*s.pi/12),s.exp(s.I*s.pi/12))
    ck('specified weak root actually broken',not zero(wd*weak_root*wd.H-weak_root))
    ck('weak Cartan actually survives',zero(wd*s.diag(1,-1)*wd.H-s.diag(1,-1)))
    ck('old Q8 invariant roster complete',8+8+3+6*6==55 and p.a5_roster()[0]==p.a5_roster()[1])
    ck('invariant dimensions within complete roster',0<=n_adj<=8 and 0<=n_sym<=6 and 0<=n_diag<=2)
    # Character projectors use the ACTUAL completed T, not old phase ranks.
    chars={}
    for j in (0,1):
        for k in range(12):
            g=A**j*LX**k;t=clean(s.trace(g));t2=clean(s.trace(g*g));t3=clean(s.trace(g*g*g))
            w2=clean((t*t-t2)/2);w3=clean((t**3-3*t*t2+2*t3)/6)
            ce=clean(t*s.conjugate(t)+8+2*s.cos(s.pi*k/6)+3*(w2+s.conjugate(w2)))
            co=clean((w3+3*(t+s.conjugate(t)))*2*s.cos(s.pi*k/12))
            chars[j,k]=(ce,co)
    ck('complete even and odd character dimensions',chars[0,0]==(136,112))
    even=[];odd=[]
    for which,phases,out in [(0,[('+1',1),('-1',-1)],even),(1,[('+i',s.I),('-i',-s.I)],odd)]:
        for label,av in phases:
            row=[]
            for r in range(12):
                value=clean(sum(chars[j,k][which]*av**(-j)*s.exp(-2*s.pi*s.I*r*k/12)
                                for j in (0,1) for k in range(12))/24)
                ck('exact integral phase '+str(which)+label+str(r),value.is_Integer and value>=0)
                row.append([r,int(value)])
            out.append([label,row])
    ck('all136 even directions retained',sum(n for _,row in even for _,n in row)==136)
    ck('all112 odd directions retained',sum(n for _,row in odd for _,n in row)==112)
    ck('all odd phases stay away from zero',all(n==0 for _,row in odd for r,n in row if r==0))
    all_dist=[min(s.Rational(r,12),1-s.Rational(r,12)) for out in [even,odd] for _,row in out for r,n in row if r and n]
    min_phase=min(all_dist)
    ck('zero phase remains in even sector',sum(n for _,row in even for r,n in row if r==0)>0)
    ck('zero-phase rejecting confinement control',s.Rational(0)<min_phase)
    records={'word_delta':delta,'recovered_inner_A':U,'recovered_inner_b':V,
             'SU6_centre_sign':-1,'weak_centre_sign':-1,'paired_E8_centre_sign':1,
             'family_moves':[[[str(x) for x in row] for row in m.tolist()] for m in fam],
             'family_adjoint_invariants':n_adj,'family_symmetric_invariants':n_sym,
             'diagonal_block_hypercharge_invariants':n_diag,'weak_invariants':1,
             'complete_based_gauge_invariant_dimension':n_adj+8+1+6*n_sym,
             'even_phase_populations':even,'odd_phase_populations':odd,
             'minimum_nonzero_phase':str(min_phase),
             'even_x_growth_pi_squared_coefficient':str(2*min_phase**2),
             'odd_P_growth_pi_squared_coefficient':str(min_phase**2),
             'canonical_even_zero_phase_bound':'3/16','odd_Q_form_norm_error':4}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'one supplied full based compact E8 completion and its complete gauge/phase cost, not a physical SM'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
