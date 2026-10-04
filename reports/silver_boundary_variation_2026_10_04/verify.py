"""Paired boundary isotropy and six-channel invariant-parameter constraints."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
    digest,path=line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
spec=importlib.util.spec_from_file_location('silver_variation_tensor_base',HERE.parent/'silver_boundary_tensors_2026_10_04/verify.py')
t=importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
red,mul,rank,kernel,zero=t.red,t.mul,t.rank,t.kernel,t.zero


def parameter_constraints(A,B,H,T,second=False):
    annihilator=kernel(H.D.row_join(H.L).T).T
    blocks=[]
    for j in range(B.L.cols):
        products=t.action(T,A.H0,B.L[:,j],second=second)
        blocks.append(mul(annihilator,products))
    return s.Matrix.vstack(*blocks) if blocks else s.zeros(0,A.H0.cols)


def surviving_parameters(spaces):
    equations={name:[] for name in spaces}
    for a,b,h,T in t.channels():
        equations[a].append(parameter_constraints(spaces[a],spaces[b],spaces[h],T))
        equations[b].append(parameter_constraints(spaces[b],spaces[a],spaces[h],T,True))
    out={}
    bases={}
    for name,blocks in equations.items():
        A=s.Matrix.vstack(*blocks)
        K=kernel(A)
        assert K.cols+rank(A)==spaces[name].H0.cols and zero(mul(A,K))
        bases[name]=mul(spaces[name].H0,K)
        witness=None
        if rank(A):
            j=next(j for j in range(A.cols) if not zero(A[:,j]))
            witness={'invariant_basis_index':j,'nonzero_constraint':[str(x) for x in A[:,j]]}
        out[name]={'full_H0':spaces[name].H0.cols,'surviving':K.cols,
                   'constraint_rank':rank(A),'kernel_coordinates':[[str(z) for z in K.row(i)] for i in range(K.rows)],
                   'excluded_witness':witness}
    # Verify retained products directly, separately from stacked annihilator equations.
    for a,b,h,T in t.channels():
        allowed=spaces[h].D.row_join(spaces[h].L)
        assert t.quotient(t.action(T,bases[a],spaces[b].L),allowed)['rank']==0
        assert t.quotient(t.action(T,bases[b],spaces[a].L,True),allowed)['rank']==0
    return out


def paired_isotropy(one):
    A,B=one['BE'],one['BD']
    J=t.g.group_cup(one['E'])
    n=J.rows
    O=s.zeros(n).row_join(J).col_join((-J.T).row_join(s.zeros(n)))
    H=s.diag(A.H,B.H)
    L=s.diag(A.L,one['LD'])
    assert rank(mul(mul(H.T,O),H))==H.cols
    assert rank(L)==L.cols and 2*L.cols==H.cols
    assert zero(mul(mul(L.T,O),L))
    # Detect a wrong dual space with the same dimension, not merely a missing vector.
    pairing=mul(mul(A.L.T,J),B.H)
    j=next(j for j in range(B.H.cols) if not zero(pairing[:,j]))
    bad=one['LD'].copy()
    bad[:,0]=B.H[:,j]
    assert rank(bad)==one['LD'].cols
    assert rank(mul(mul(A.L.T,J),bad))>0
    return {'paired_H1_dimension':H.cols,'allowed_dimension':L.cols,
            'symplectic_rank':H.cols,'isotropic':True,'wrong_dual_space_rejected':True}


@lru_cache(None)
def controls():
    spaces={name:t.trivial(5 if name.startswith('E') else 10,s.I)
            for name in ('E','E*','F','F*')}
    common=surviving_parameters(spaces)
    assert all(r['surviving']==r['full_H0'] for r in common.values())
    A,B,H=t.trivial(5,0),t.trivial(10,1),t.trivial(10,0)
    eq=parameter_constraints(A,B,H,t.tensor(1,2))
    assert rank(eq)>0
    h=s.diag(1,-1); e=s.Matrix([[0,1],[0,0]]); f=e.T
    pair=lambda a,b:s.trace(a[0]*b[1]-a[1]*b[0])
    basis=[(h,s.zeros(2)),(e,s.zeros(2)),(f,s.zeros(2)),
           (s.zeros(2),h),(s.zeros(2),e),(s.zeros(2),f)]
    O=s.Matrix([[pair(a,b) for b in basis] for a in basis])
    L=s.eye(6)[:,[0,4,5]]
    assert O.rank()==6 and L.rank()==3 and L.T*O*L==s.zeros(3)
    assert h*e-e*h==2*e
    x,y,z=s.symbols('x y z',real=True)
    Cx,Cy=x*h,y*e
    F=Cx*Cy-Cy*Cx
    I=Cx*Cx.T-Cx.T*Cx+Cy*Cy.T-Cy.T*Cy
    norm=lambda a:s.trace(a.T*a)
    energy=s.expand(2*norm(F)+norm(I)/2)
    assert energy==8*x*x*y*y+y**4
    assert s.hessian(energy,(x,y)).subs({x:0,y:0})==s.zeros(2)
    assert energy.subs({x:z,y:z})==9*z**4
    # Preserving the x-direction Cartan trace excludes both root parameters.
    Z=x*h+y*e+z*f
    condition=Z*h-h*Z
    assert condition[0,1]==-2*y and condition[1,0]==2*z
    G=s.Matrix([[1,2],[3,4]])
    P=s.Matrix([[1,0,0],[0,0,0],[0,0,1]])
    assert s.kronecker_product(G,s.eye(3))*s.kronecker_product(s.eye(2),P)==s.kronecker_product(s.eye(2),P)*s.kronecker_product(G,s.eye(3))
    return {'status':'PASS','common_line_all_parameters':True,
            'distinct_line_constraint_rank':rank(eq),'sl2_Lagrangian_dimension':3,
            'sl2_nonzero_bracket':True,'sl2_residual_energy':str(energy),
            'sl2_zero_Hessian_at_origin':True,'sl2_gauge_stabilizer_dimension':1,
            'gauge_structure_tensor_factors_commute':True}


@lru_cache(None)
def actual_members():
    old,data,records=t.m.inputs()
    out=[]
    for label,state in data['states'].items():
        old.check_marking(label,state)
        f=old.four(state)
        for member in state['members']:
            char=member['nu on a, b, t']
            saved=next(r for r in records if r['signed_word']==label and r['character']==char)
            c=s.Matrix([s.sympify(x) for x in saved['peripherally_zero_cocycle']])
            V={k:char[k]*f[k] for k in t.m.GEN}
            print(json.dumps({'progress':'starting','carrier':state['SnapPy'],'character':char}),flush=True)
            amps={}
            for amplitude in (0,1):
                rep=old.extension(V,amplitude*c)
                one=t.g.analyze(rep,state,saved['splitW' if amplitude==0 else 'W'])
                two=t.g.analyze({k:old.exterior(R) for k,R in rep.items()},state,
                                saved['split_wedge2W' if amplitude==0 else 'wedge2W'])
                spaces=t.make_spaces(one,two)
                params=surviving_parameters(spaces)
                iso={'E_pair':paired_isotropy(one),'F_pair':paired_isotropy(two)}
                amps[str(amplitude)]={'parameters':params,'pairing':iso,
                    'interior_pair':[one['summary']['difference'],two['summary']['difference']]}
            row={'carrier':state['SnapPy'],'character':char,'signed_word':label,'amplitudes':amps}
            print(json.dumps({'member':row},sort_keys=True),flush=True)
            out.append(row)
    return out


if __name__=='__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),
                     'scope':'paired holomorphic cohomology form and six-channel complex parameter screen'}),flush=True)
