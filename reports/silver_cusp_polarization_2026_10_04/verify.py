"""Exact actual-silver boundary-subspace test, not a physical-domain claim."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from math import factorial
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = HERE.parent/'silver_boundary_admission_2026_10_04'
FIELD = s.QQ.algebraic_field(s.sqrt(2),s.I)
GEN = 'abt'


def dm(m):
    return DomainMatrix.from_Matrix(m).convert_to(FIELD)


def red(m):
    return dm(m).to_Matrix()


def mul(a,b):
    return (dm(a)*dm(b)).to_Matrix()


def power(a,n):
    return (dm(a)**n).to_Matrix()


def rank(m):
    return dm(m).rank()


def zero(m):
    return rank(m)==0


def inverse(m):
    return dm(m).inv().to_Matrix()


def kernel(m):
    return dm(m).nullspace().to_Matrix().T


def dual(rep):
    return {g:inverse(m).T for g,m in rep.items()}


def independent_modulo(D,C):
    current, chosen, r = D, [], rank(D)
    for j in range(C.cols):
        trial = current.row_join(C[:,j])
        nr = rank(trial)
        if nr>r:
            chosen.append(j)
            current,r = trial,nr
    return C[:,chosen] if chosen else s.zeros(C.rows,0)


@lru_cache(None)
def inputs():
    for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
        digest,path = line.split(maxsplit=1)
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
    spec = importlib.util.spec_from_file_location('silver_input_construction',OLD/'verify.py')
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    data = json.loads((OLD/'members.json').read_text())
    records = [json.loads(line)['member'] for line in (OLD/'NATIVE_SECOND.jsonl').read_text().splitlines()
               if 'member' in json.loads(line)]
    assert len(records)==4
    return old,data,records


class Global:
    def __init__(self,rep,state):
        self.rep,self.n = rep,rep['a'].rows
        n = self.n
        self.letters = dict(rep)
        self.letters.update({g.upper():inverse(m) for g,m in rep.items()})
        for m in rep.values():
            assert dm(m).det()==FIELD.one
        for w in state['relators']:
            assert zero(self.word(w)-s.eye(n)),('relator',w)
        self.P,self.Q = [self.word(w) for w in state['cusp words']]
        assert zero(mul(self.P,self.Q)-mul(self.Q,self.P))
        self.B = s.Matrix.vstack(*(rep[g]-s.eye(n) for g in GEN))
        self.F = s.Matrix.vstack(*(self.fox(w) for w in state['relators']))
        self.R = s.Matrix.vstack(*(self.fox(w) for w in state['cusp words']))
        self.D = s.Matrix.vstack(self.P-s.eye(n),self.Q-s.eye(n))
        self.Z = kernel(self.F)
        self.RZ = mul(self.R,self.Z)
        self.br,self.dr = rank(self.B),rank(self.D)
        self.h0,self.h1,self.t0 = n-self.br,self.Z.cols-self.br,n-self.dr
        self.interior = self.Z.cols+self.dr-rank(self.RZ.row_join(self.D))-self.br
        assert zero(mul(self.F,self.B)) and zero(mul(self.R,self.B)-self.D)
        assert zero(mul((s.eye(n)-self.Q).row_join(self.P-s.eye(n)),self.RZ))

    def word(self,w):
        m=s.eye(self.n)
        for c in w:
            m=mul(m,self.letters[c])
        return m

    def fox(self,w):
        pre=s.eye(self.n)
        blocks={g:s.zeros(self.n) for g in GEN}
        for c in w:
            if c.islower():
                blocks[c]=red(blocks[c]+pre)
                pre=mul(pre,self.letters[c])
            else:
                pre=mul(pre,self.letters[c])
                blocks[c.lower()]=red(blocks[c.lower()]-pre)
        return s.Matrix.hstack(*(blocks[g] for g in GEN))

    def profile(self):
        return {'h0_absolute':self.h0,'h0_boundary':self.t0,'h1_absolute':self.h1,
                'h1_interior':self.interior,'h1_relative':self.t0-self.h0+self.interior,
                'restriction_rank':self.h1-self.interior}

    def allowed(self,C):
        S=self.D.row_join(C)
        value=self.Z.cols+rank(S)-rank(self.RZ.row_join(S))-self.br
        assert self.interior<=value<=self.h1
        return value


class Boundary:
    def __init__(self,P,Q):
        self.P,self.Q,self.n=P,Q,P.rows
        n=self.n
        assert zero(mul(P,Q)-mul(Q,P)), 'noncommuting peripheral pair'
        sectors=[]
        self.sector_dimensions={}
        for ep,eq in ((1,1),(1,-1),(-1,1),(-1,-1)):
            basis=kernel(s.Matrix.vstack(power(P-ep*s.eye(n),n),power(Q-eq*s.eye(n),n)))
            sectors.append(basis)
            self.sector_dimensions[f'{ep},{eq}']=basis.cols
        assert sum(b.cols for b in sectors)==n and rank(s.Matrix.hstack(*sectors))==n
        self.basis=B=sectors[0]
        self.k=k=B.cols
        self.log_embed=s.diag(B,B)
        self.fullD=s.Matrix.vstack(P-s.eye(n),Q-s.eye(n))
        if k==0:
            self.X=self.Y=self.d0=self.d1=s.zeros(0,0)
            self.group_embed=s.zeros(2*n,0)
            self.h0=self.h1=0
            return
        rows=dm(B.T).rref()[1]
        left=inverse(B.extract(rows,list(range(k))))
        U=mul(left,mul(P,B).extract(rows,list(range(k))))
        V=mul(left,mul(Q,B).extract(rows,list(range(k))))
        assert zero(mul(B,U)-mul(P,B)) and zero(mul(B,V)-mul(Q,B))
        self.X=X=self.log(U)
        self.Y=Y=self.log(V)
        assert zero(mul(X,Y)-mul(Y,X))
        TX,TY=self.exponential_quotient(X),self.exponential_quotient(Y)
        assert rank(TX)==rank(TY)==k
        self.d0=s.Matrix.vstack(X,Y)
        self.d1=(-Y).row_join(X)
        groupD=s.Matrix.vstack(U-s.eye(k),V-s.eye(k))
        groupF=(s.eye(k)-V).row_join(U-s.eye(k))
        J=s.diag(TX,TY)
        assert zero(groupD-mul(J,self.d0))
        assert zero(mul(groupF,J)-mul(mul(TX,TY),self.d1))
        assert zero(U-s.eye(k)-mul(X,TX)) and zero(V-s.eye(k)-mul(Y,TY))
        self.group_embed=s.diag(mul(B,TX),mul(B,TY))
        self.h0=k-rank(self.d0)
        self.h1=2*k-rank(self.d0)-rank(self.d1)
        assert self.h0==n-rank(self.fullD)
        fullF=(s.eye(n)-Q).row_join(P-s.eye(n))
        assert self.h1==2*n-rank(self.fullD)-rank(fullF)

    @staticmethod
    def log(U):
        n=U.rows
        N=U-s.eye(n)
        assert zero(power(N,n))
        return red(sum((s.Rational((-1)**(j+1),j)*power(N,j) for j in range(1,n)),s.zeros(n)))

    @staticmethod
    def exponential_quotient(X):
        n=X.rows
        return red(sum((power(X,j)/factorial(j+1) for j in range(n)),s.zeros(n)))

    def pure(self,tau):
        if self.k==0:
            return s.zeros(0,0)
        K=kernel(self.Y-tau*self.X)
        C=K.col_join(tau*K)
        assert zero(mul(self.d1,C))
        out=independent_modulo(self.d0,C)
        assert out.cols==self.h0
        return out

    def group(self,C):
        return mul(self.group_embed,C)

    def full_log(self,C):
        return mul(self.log_embed,C)

    def cohom_rank(self,C):
        return rank(self.d0.row_join(C))-rank(self.d0)


def cup(n):
    return s.zeros(n).row_join(s.eye(n)).col_join((-s.eye(n)).row_join(s.zeros(n)))


def annihilator(E,D,C):
    Z=kernel(D.d1)
    constraint=mul(mul(E.full_log(C).T,cup(E.n)),D.full_log(Z))
    result=mul(Z,kernel(constraint))
    assert zero(mul(mul(E.full_log(C).T,cup(E.n)),D.full_log(result)))
    assert E.cohom_rank(C)+D.cohom_rank(result)==E.h1
    return result


def pair_space(E,D,tau):
    L,LD=E.pure(tau),D.pure(tau)
    assert E.h1==D.h1==E.h0+D.h0
    assert zero(mul(mul(E.full_log(L).T,cup(E.n)),D.full_log(LD)))
    assert E.cohom_rank(L)+D.cohom_rank(LD)==E.h1
    return L,LD


def shear_check(E,tau,L):
    n=E.n
    new=Boundary(E.P,mul(E.P,E.Q))
    T=s.eye(n).row_join(s.zeros(n)).col_join(s.eye(n).row_join(E.P))
    transported=mul(T,E.group(L))
    newL=new.group(new.pure(tau+1))
    left,right=new.fullD.row_join(transported),new.fullD.row_join(newL)
    assert rank(left)==rank(right)==rank(left.row_join(right))


def shape(state):
    matrices={g:s.Matrix([[s.Rational(a)+s.I*s.Rational(b) for a,b in row] for row in entries])
              for g,entries in state['holonomy (PGL(2, Q(i)); entries [re, im])'].items()}
    letters=dict(matrices)
    letters.update({g.upper():inverse(m) for g,m in matrices.items()})
    def evaluate(w):
        m=s.eye(2)
        for c in w:
            m=mul(m,letters[c])
        return m
    for w in state['relators']:
        R=evaluate(w)
        assert R[0,0]!=0 and zero(R-R[0,0]*s.eye(2))
    P,Q=[red(2*evaluate(w)/s.trace(evaluate(w)))-s.eye(2) for w in state['cusp words']]
    assert not zero(P) and not zero(Q) and zero(mul(P,P)) and zero(mul(Q,Q))
    at=next((i,j) for i in range(2) for j in range(2) if P[i,j]!=0)
    tau=s.cancel(Q[at]/P[at])
    assert zero(Q-tau*P) and s.simplify(tau-s.conjugate(tau))!=0
    return tau


def analyze(rep,state,tau,expected=None,drop=False):
    E,D=Global(rep,state),Global(dual(rep),state)
    assert all(zero(dual(dual(rep))[g]-rep[g]) for g in GEN)
    if expected is not None:
        assert E.profile()==expected['E'],(E.profile(),expected['E'])
        assert D.profile()==expected['dual'],(D.profile(),expected['dual'])
    BE,BD=Boundary(E.P,E.Q),Boundary(D.P,D.Q)
    rows=[]
    for z in (tau,s.conjugate(tau)):
        L,LD=pair_space(BE,BD,z)
        counts=(E.allowed(BE.group(L)),D.allowed(BD.group(LD)))
        expected_difference=BE.cohom_rank(L)-BE.h0+E.h0-D.h0
        assert counts[0]-counts[1]==expected_difference==E.h0-D.h0
        shear_check(BE,z,L)
        shear_check(BD,z,LD)
        row={'tau':str(z),'allowed_H1':counts,'difference':counts[0]-counts[1],
             'boundary_dimensions':[BE.h0,BD.h0],'polar_dimensions':[L.cols,LD.cols]}
        if drop:
            assert L.cols>0
            small=L[:,:-1]
            ann=annihilator(BE,BD,small)
            changed=(E.allowed(BE.group(small)),D.allowed(BD.group(ann)))
            assert changed[0]-changed[1]==expected_difference-1
            row['supplied_codimension_one_control']={'allowed_H1':changed,
                'difference':changed[0]-changed[1],
                'dimensions':[BE.cohom_rank(small),BD.cohom_rank(ann)]}
        rows.append(row)
    return {'profile':{'E':E.profile(),'dual':D.profile()},
            'primary_sector_dimensions':BE.sector_dimensions,'rows':rows}


@lru_cache(None)
def comparators():
    eye=s.eye(3)
    P,Q=eye.copy(),eye.copy()
    P[0,1]=1
    Q[0,2]=1
    E,D=Boundary(P,Q),Boundary(inverse(P).T,inverse(Q).T)
    assert (E.h0,D.h0,E.h1)==(1,2,3)
    for tau in (s.I,-s.I,0,1+s.I):
        L,LD=pair_space(E,D,tau)
        assert (L.cols,LD.cols)==(1,2)
    tr=Boundary(s.eye(1),s.eye(1))
    assert (tr.h0,tr.h1,tr.pure(s.I).cols)==(1,2,1)
    ac=Boundary(-s.eye(1),s.eye(1))
    assert (ac.h0,ac.h1,ac.pure(s.I).cols)==(0,0,0)
    bad=s.eye(3)
    bad[1,0]=1
    try:
        Boundary(P,bad)
    except AssertionError as ex:
        assert str(ex)=='noncommuting peripheral pair'
    else:
        raise AssertionError('noncommuting pair accepted')
    X=s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
    U=s.eye(3)+X+X*X/2
    V=s.eye(3)+2*X+2*X*X
    b=Boundary(U,V)
    assert not zero(b.fullD-b.d0)
    return {'status':'PASS','unequal_dual_H0':[1,2],'unequal_dual_H1':3,
            'noncommuting_rejected':True,'log_group_difference_visible':True}


@lru_cache(None)
def actual_members():
    old,data,records=inputs()
    out=[]
    for label,state in data['states'].items():
        old.check_marking(label,state)
        tau=shape(state)
        f=old.four(state)
        for spec in state['members']:
            char=spec['nu on a, b, t']
            record=next(r for r in records if r['signed_word']==label and r['character']==char)
            V={g:char[g]*f[g] for g in GEN}
            c=s.Matrix([s.sympify(x) for x in record['peripherally_zero_cocycle']])
            W=old.extension(V,c)
            wedge={g:old.exterior(m) for g,m in W.items()}
            result={'carrier':state['SnapPy'],'signed_word':label,'character':char,'tau':str(tau),
                    'W':analyze(W,state,tau,record['W']),
                    'wedge2W':analyze(wedge,state,tau,record['wedge2W'],drop=True)}
            assert all(r['difference']==-1 for r in result['W']['rows'])
            assert all(r['difference']==0 for r in result['wedge2W']['rows'])
            split=old.extension(V,s.zeros(12,1))
            result['splitW']=analyze(split,state,tau,record['splitW'])
            result['split_wedge2W']=analyze({g:old.exterior(m) for g,m in split.items()},state,tau,record['split_wedge2W'])
            assert all(r['difference']==0 for key in ('splitW','split_wedge2W') for r in result[key]['rows'])
            if not out:
                G=s.eye(5)
                G[0,4]=1+s.sqrt(2)
                G[3,4]=2
                WG={g:mul(mul(G,m),inverse(G)) for g,m in W.items()}
                result['gauge_controls']={
                    'W':analyze(WG,state,tau,record['W']),
                    'wedge2W':analyze({g:old.exterior(m) for g,m in WG.items()},state,tau,record['wedge2W'])}
                for key in ('W','wedge2W'):
                    assert [r['allowed_H1'] for r in result['gauge_controls'][key]['rows']]==[r['allowed_H1'] for r in result[key]['rows']]
            out.append(result)
            print(json.dumps({'member':result},sort_keys=True),flush=True)
    return out


if __name__=='__main__':
    print(json.dumps({'comparators':comparators()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),
                      'scope':'pure-form subspaces of boundary cohomology, not physical operator domains'}),flush=True)
