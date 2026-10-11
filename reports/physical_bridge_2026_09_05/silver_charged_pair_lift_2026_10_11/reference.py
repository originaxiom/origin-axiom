"""Independent Fraction quadratic arithmetic and degree-bound rank replay.

Uses older literal Fraction reconstruction, never the new native or its outputs.
Family jets are composed directly as truncated exponential word products.
"""
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('charged_lift_cyclic_fraction_reference',HERE.parent/'silver_cyclic_transfer_2026_10_06/reference.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
K=c.K; GEN='abt'
Z,I,tr,mm,add,scale,cat,stack,diag,zero,equal,null=c.Z,c.I,c.tr,c.mm,c.add,c.scale,c.cat,c.stack,c.diag,c.zero,c.equal,c.null


def rank(a):
    return len(c.old.elimination(a)[1]) if a and a[0] else 0


def cols(a):
    piv=c.old.elimination(a)[1] if a[0] else []
    return [[row[j] for j in piv] for row in a]


def subset(a, selected): return [[row[j] for j in selected] for row in a]


def sum_mat(mats, n, m):
    out=Z(n,m)
    for a in mats: out=add(out,a)
    return out


def constant(a): return [a,Z(len(a),len(a[0])),Z(len(a),len(a[0]))]


def product(a,b):
    return [sum_mat([mm(a[i],b[k-i]) for i in range(k+1)],len(a[0]),len(b[0][0])) for k in range(3)]


def rep_jets(rep, direction=1):
    letters={g:constant(m) for g,m in rep.items()}
    letters.update({g.upper():constant(c.inverse(m)) for g,m in rep.items()})
    for letter,d in (('t',direction),('T',-direction)):
        m=letters[letter][0];letters[letter]=[scale(m,Fraction(d**k,factorial(k))) for k in range(3)]
    return letters


def word_fox_jets(rep,text,direction=1):
    n=len(rep['a']);letters=rep_jets(rep,direction);prefix=constant(I(n))
    blocks=[[Z(n) for _ in GEN] for _ in range(3)]
    for letter in text:
        j=GEN.index(letter.lower())
        if letter.islower():
            for k in range(3): blocks[k][j]=add(blocks[k][j],prefix[k])
            prefix=product(prefix,letters[letter])
        else:
            prefix=product(prefix,letters[letter])
            for k in range(3): blocks[k][j]=add(blocks[k][j],prefix[k],-1)
    return prefix,[[sum((block[i] for block in blocks[k]),[]) for i in range(n)] for k in range(3)]


def family_jets(rep,data,direction=1):
    n=len(rep['a']);letters=rep_jets(rep,direction)
    B=[sum((letters[g][k] if k else add(letters[g][k],I(n),-1) for g in GEN),[]) for k in range(3)]
    rel=[word_fox_jets(rep,text,direction) for text in data['relators']]
    cusp=[word_fox_jets(rep,text,direction) for text in data['cusp_words']]
    F=[stack(rel[0][1][k],rel[1][1][k]) for k in range(3)]
    R=[stack(cusp[0][1][k],cusp[1][1][k]) for k in range(3)]
    P,Q=cusp[0][0],cusp[1][0]
    D=[stack(add(P[k],I(n),-1) if k==0 else P[k],add(Q[k],I(n),-1) if k==0 else Q[k]) for k in range(3)]
    G=[cat(add(I(n),Q[k],-1) if k==0 else scale(Q[k],-1),add(P[k],I(n),-1) if k==0 else P[k]) for k in range(3)]
    r2=product(product(Q,[[row[:2*n] for row in x] for x in cusp[0][1]]),[diag(x,x) for x in letters['T']])
    R2=[scale(x,-1) for x in r2]
    return dict(B=B,F=F,R=R,R2=R2,D=D,G=G,P=P,Q=Q)


def integral_coefficients(a):
    powers=[I(len(a))]
    for _ in range(len(a)):
        powers.append(mm(powers[-1],a))
        if zero(powers[-1]):break
    assert zero(powers[-1])
    return [sum_mat([scale(powers[j],Fraction(1,factorial(j)*factorial(k)*(j+k+1))) for j in range(len(powers)-1)],len(a),len(a)) for k in range(3)]


def boundary(a,b):
    n=len(a);d0=stack(a,b);d1=cat(scale(b,-1),a)
    U=cols(tr(d1));H=null(stack(d1,tr(d0)));t0=n-rank(d1)
    return dict(n=n,a=a,b=b,U=U,H=H,t0=t0)


def paired_plane(E,D,L):
    n=E['n'];J=stack(cat(Z(n),I(n)),cat(scale(I(n),-1),Z(n)))
    coeff=null(mm(mm(tr(L),J),D['H'])) if L[0] else I(len(D['H'][0]))
    LD=mm(D['H'],coeff)
    assert zero(mm(mm(tr(L),J),LD)) if L[0] and LD[0] else True
    return LD,coeff


def evaluation_rows(E):
    # One row reduction per point; invertible row operations retain every
    # subsequent column-subspace rank, including noncoordinate dual planes.
    n=E['n'];M=cat(E['U'],E['H'])
    return [c.reduced(mm(cat(add(scale(E['b'],-1),scale(I(n),-value)),E['a']),M))[0] for value in range(n+1)]


def degree_count(E,coeff,evaluations):
    r=len(E['U'][0]);ell=len(coeff[0]) if coeff else 0
    ranks=[]
    for row_matrix in evaluations:
        base=[row[:r] for row in row_matrix];tail=[row[r:] for row in row_matrix]
        transformed=mm(tail,coeff) if ell else Z(E['n'],0)
        ranks.append(rank(cat(base,transformed)))
    value=max(ranks);h=[0,r+ell-value,E['n']-value,0]
    return dict(H=h,J=h[1]-h[2],rank=value,ell=ell)


def place(target,block,row,col):
    for i,line in enumerate(block):target[row+i][col:col+len(line)]=line


def cone_jets(f,E,L,direction=1):
    n=E['n'];M=cat(E['U'],L);m=len(M[0]);sizes=[n,4*n+m,5*n,n]
    jets=[[Z(sizes[j+1],sizes[j]) for _ in range(3)] for j in range(3)]
    ua=c.series(E['a'],True);ub=integral_coefficients(E['b'])
    T1=[diag(ua,ub[0]),diag(Z(n),scale(ub[1],direction)),diag(Z(n),ub[2])]
    T2=[mm(ua,scale(x,direction**k)) for k,x in enumerate(ub)]
    da=[cat(scale(E['b'],-1),E['a']),cat(scale(I(n),-direction),Z(n)),Z(n,2*n)]
    for k in range(3):
        d0,d1,d2=[jets[j][k] for j in range(3)]
        place(d0,f['B'][k],0,0)
        if k==0:place(d0,I(n),3*n+m,0)
        place(d1,f['F'][k],0,0);place(d1,mm(da[k],M),2*n,3*n)
        place(d1,f['R'][k],3*n,0);place(d1,scale(mm(T1[k],M),-1),3*n,3*n)
        place(d1,scale(f['D'][k],-1),3*n,3*n+m)
        place(d2,f['R2'][k],0,0);place(d2,scale(T2[k],-1),0,2*n);place(d2,scale(f['G'][k],-1),0,3*n)
    return jets,sizes


def residuals(jets):
    return [sum_mat([mm(jets[j+1][k-i],jets[j][i]) for i in range(k+1)],len(jets[j+1][0]),len(jets[j][0][0])) for j in range(2) for k in range(3)]


def first_mass(jets,sizes):
    d0,d1,d2=[a[0] for a in jets];r=list(map(rank,(d0,d1,d2)))
    H=[sizes[j]-([0]+r)[j]-(r+[0])[j] for j in range(4)]
    cycles=null(d1);bound=cols(d0);combined=cat(bound,cycles)
    piv=c.old.elimination(combined)[1];h1=subset(combined,[j for j in piv if j>=len(bound[0])])
    assert len(h1[0])==H[1]
    derivative=mm(jets[1][1],h1);induced=rank(cat(d1,derivative))-r[1]
    return dict(H_at_zero=H,first_mass_rank=induced,massless_at_first_order=[H[1]-induced,H[2]-induced]),dict(
        cycles=zero(mm(d2,derivative)),boundaries_descend=zero(add(mm(jets[1][1],d0),mm(d1,jets[0][1]))))


@lru_cache(None)
def run():
    data,w,P,Q,A,B=c.literal();predicates={};blocks={};jets_out={}
    def ck(k,v):predicates[k]=bool(v);assert predicates[k],k
    rows=[[sum(1 if letter.islower() else -1 for letter in text if letter.lower()==g) for g in GEN] for text in data['relators']]
    ck('primitive_time_character_and_wrong_parity_character',rows==[[2,2,0],[2,6,0]] and null(rows)==[[0],[0],[1]] and any(sum(row[j]*data['nu'][g] for j,g in enumerate(GEN)) for row in rows))
    ck('two_actual_cusp_logs',rank(tr([[x for row in a for x in row] for a in (A,B)]))==2)
    reps={'W':w,'F':{g:c.old.exterior(a) for g,a in w.items()}}
    for label,rep in reps.items():
        a,b=(A,B) if label=='W' else (c.wedge_derivative(A),c.wedge_derivative(B))
        E=boundary(a,b);D=boundary(scale(tr(a),-1),scale(tr(b),-1));n=E['n']
        erows,drows=evaluation_rows(E),evaluation_rows(D)
        f=family_jets(rep,data);dualrep={g:tr(c.inverse(x)) for g,x in rep.items()};df=family_jets(dualrep,data,-1)
        ck(label+'_fiber_minor_nonzero_leading_coefficient',equal([row[:2*n] for row in f['F'][1]],diag(rep['t'],rep['t'])))
        ck(label+'_R_maps_constant_through_second_jet',all(zero(f[k][j]) for k in ('R','R2') for j in (1,2)))
        controls=[]
        for value in (1,2,3):
            rq=dict(rep);rq['t']=scale(rep['t'],value);g=family_jets(rq,data)
            rb,rf=rank(g['B'][0]),rank(g['F'][0]);controls.append([n-rb,3*n-rb-rf,2*n-rf])
        ck(label+'_old_and_acyclic_controls',controls[0]==([0,2,2] if label=='W' else [0,4,4]) and controls[1:]==[[0,0,0],[0,0,0]])
        first={};witnesses=[]
        for ell in range(len(E['H'][0])+1):
            for selected in combinations(range(len(E['H'][0])),ell):
                L=subset(E['H'],selected);coeff=subset(I(len(E['H'][0])),selected)
                LD,dualcoeff=paired_plane(E,D,L)
                row=degree_count(E,coeff,erows);other=degree_count(D,dualcoeff,drows)
                ck(label+'_actual_dual_'+('_'.join(map(str,selected)) or 'empty'),row['H']==other['H'][::-1] and row['J']==-other['J'])
                row.update(subset=list(selected),dual=other);witnesses.append(row)
                if row['H']==[0,max(row['J'],0),max(-row['J'],0),0] and ell not in first:first[ell]=list(selected)
        ck(label+'_all_dimensions_have_fixed_protected_witnesses',set(first)==set(range(len(E['H'][0])+1)) and len(witnesses)==2**len(E['H'][0]))
        hist={str(ell):{','.join(map(str,k)):v for k,v in sorted(Counter(tuple(row['H']) for row in witnesses if row['ell']==ell).items())} for ell in first}
        blocks[label]=dict(n=n,t0=E['t0'],bulk_H_controls=controls,witness_count=len(witnesses),witness_histograms=hist,
                           protected_only_witnesses={str(k):v for k,v in first.items()},rows=witnesses)
        for J in (1,2):
            L=subset(E['H'],first[E['t0']+J]);LD,_=paired_plane(E,D,L)
            for tag,fam,e,plane,direction in ((label,f,E,L,1),(label+'dual',df,D,LD,-1)):
                jets,sizes=cone_jets(fam,e,plane,direction);key=tag+'_J'+str(J)
                ck(key+'_literal_family_chain_second_jet',all(zero(x) for x in residuals(jets)))
                result,descend=first_mass(jets,sizes)
                for name,value in descend.items():ck(key+'_'+name,value)
                ck(key+'_charged_endpoints_and_index',result['H_at_zero'][0]==result['H_at_zero'][3]==0 and result['H_at_zero'][1]-result['H_at_zero'][2]==(J if direction==1 else -J))
                jets_out[key]=result
        ck(label+'_opposite_phase_dual_first_mass_rank',all(jets_out[label+'_J'+str(J)]['first_mass_rank']==jets_out[label+'dual_J'+str(J)]['first_mass_rank'] for J in (1,2)))
    ck('every_common_index_protected_example',all(str(2+J) in blocks['W']['protected_only_witnesses'] and str(3+J) in blocks['F']['protected_only_witnesses'] for J in range(-2,3)))
    def polynomial(x):
        value=1
        for j in range(5):value*=x-j
        return value
    ck('five_bad_samples_but_sixth_detects_degree_five_polynomial',all(polynomial(j)==0 for j in range(5)) and polynomial(5)==120)
    ck('twist_after_exterior_is_not_squared',equal(c.old.exterior(scale(w['t'],2)),scale(c.old.exterior(w['t']),4)) and not equal(c.old.exterior(scale(w['t'],2)),scale(c.old.exterior(w['t']),2)))
    return dict(predicates=predicates,predicates_passed=len(predicates),blocks=blocks,first_mass_maps=jets_out,
                common_generation_indices=list(range(-2,3)),conditional_small_v_charged_lift=True,
                new_native_imported=False,degree_bound_certificate=True,actual_normalized_mass_values=False,
                global_PDE_solved=False,Higgs_complete=False,generated_selection=False,three_generations=False,
                outside_review=False,full_goal_achieved=False)


if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
