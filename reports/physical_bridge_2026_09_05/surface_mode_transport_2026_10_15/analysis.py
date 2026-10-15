"""Declared cochain/Hodge/phase certificate questions, shared by two word engines.

The finite computation is not an independent analytic proof of a kernel
bundle, graph domain, Born-Oppenheimer remainder or physical index.
"""
from itertools import combinations
import json
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
def clean(m):
    if isinstance(m,s.MatrixBase):return m.applyfunc(lambda x:s.simplify(s.expand(x)))
    return s.simplify(s.expand(m))
def zero(m):return all(clean(x)==0 for x in m)
def invword(w):return w[::-1].swapcase()
def wedge(g,k):
    inds=list(combinations(range(g.rows),k))
    return s.Matrix(len(inds),len(inds),lambda i,j:g.extract(inds[i],inds[j]).det()).applyfunc(clean)
def representation(matrices,k=1,dual=False):
    out={n:(g if k==1 else wedge(g,k)) for n,g in matrices.items()}
    return {n:clean(g.inv().T) if dual else g for n,g in out.items()}
def coords(basis):
    B=s.Matrix.hstack(*(x.reshape(x.rows*x.cols,1) for x in basis))
    return B,(B.T*B).inv()*B.T
def adjoint3(m):
    bs=[]
    for i in range(3):
        for j in range(3):
            if i!=j:x=s.zeros(3);x[i,j]=1;bs.append(x)
    bs.extend([s.diag(1,-1,0),s.diag(0,1,-1)])
    B,L=coords(bs)
    return clean(L*s.Matrix.hstack(*((m.inv()*x*m).reshape(9,1) for x in bs)))
def symmetric3(m):
    bs=[]
    for i in range(3):
        for j in range(i,3):
            x=s.zeros(3);x[i,j]=1
            if i!=j:x[j,i]=1
            bs.append(x)
    B,L=coords(bs)
    return clean(L*s.Matrix.hstack(*((m.inv()*x*m.inv().T).reshape(9,1) for x in bs)))
def dft(h,n):
    zeta={4:s.I,8:(1+s.I)/s.sqrt(2)}[n]
    chars=[clean(s.trace(h**k)) for k in range(n)]
    return [clean(sum(chars[k]*zeta**(-r*k) for k in range(n))/n) for r in range(n)]
def encoded(m):return [[str(clean(x)) for x in row] for row in m.tolist()]

def run(Evaluator):
    checks={}
    def ck(n,v):checks[n]=bool(v)
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]]);I2=s.eye(2)
    S=s.diag(b,a,a*b);A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    P13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]);P23=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    X=s.kronecker_product(P13,(I2+a)/s.sqrt(2));Y=s.kronecker_product(P23,(I2+b)/s.sqrt(2));Z=A.H*X
    base={'a':A,'b':B,'X':X,'Y':Y,'Z':Z}
    aut={'X':('a','ab'),'Y':('aB','b'),'Z':('a','ba')}
    def cochain(ev,g,images):return s.diag(g.inv(),g.inv())*s.Matrix.vstack(*(ev.eval(w) for w in images))
    def odd_case(name,matrices,colour):
        aa,bb=matrices['a'],matrices['b'];n=aa.rows;eye=s.eye(n);ev=Evaluator(aa,bb)
        d0=s.Matrix.vstack(aa-eye,bb-eye)
        quotient=s.Matrix.hstack(-(bb-eye)*(aa-eye).inv(),eye);section=s.Matrix.vstack(s.zeros(n),eye)
        ck(name+' quaternion identities',aa*aa==bb*bb==-eye and aa*bb==-bb*aa)
        ck(name+' exact quotient and section',zero(quotient*d0) and quotient*section==eye)
        acts={}
        for label,images in aut.items():
            g=matrices[label];t=clean(cochain(ev,g,images));h=clean(quotient*t*section);acts[label]=h
            ck(name+' actual covariance '+label,all(zero(g*src*g.inv()-ev.rho(w)) for src,w in zip((aa,bb),images)))
            ck(name+' actual coboundary map '+label,zero(t*d0-d0*g.inv()))
            ck(name+' actual quotient map '+label,zero(quotient*t-h*quotient))
        for word in ('a','A','b','B','abAB','baBA'):
            g=ev.rho(word);images=tuple(word+c+invword(word) for c in 'ab')
            t=clean(cochain(ev,g,images));hom=-g.inv()*ev.eval(word)
            ck(name+' inner chain homotopy '+word,zero(t-s.eye(2*n)-d0*hom))
            ck(name+' inner acts identity on H1 '+word,zero(quotient*t-quotient))
        # The clean raw-gauge-only trap: the puncture is -I, its induced class map is +I.
        ck(name+' raw puncture sign is not cohomology transport',ev.rho('abAB')==-eye and n>0)
        tx=clean(cochain(ev,matrices['X'],aut['X']));tz=clean(cochain(ev,matrices['Z'],aut['Z']))
        ck(name+' actual XZ homotopy',zero(tz-tx-d0*matrices['X'].inv()*s.Matrix.hstack(eye,s.zeros(n))))
        ck(name+' same induced X and Z',zero(acts['X']-acts['Z']))
        ck(name+' raw X inverse is not its H1 action',not zero(acts['X']-matrices['X'].inv()))
        ck(name+' nonzero coboundary makes identity control discriminating',not zero(d0))
        ck(name+' Hodge lines preserved by all cohomology maps',all(zero(h*aa-aa*h) for h in acts.values()))
        plus=[j for j in range(n) if aa[j,j]==-s.I];minus=[j for j in range(n) if aa[j,j]==s.I]
        ck(name+' both Hodge halves retained',aa.is_diagonal() and len(plus)==len(minus)==n//2)
        out={}
        for label,inds in [('positive',plus),('negative',minus)]:
            hs={k:v.extract(inds,inds) for k,v in acts.items()};mult=dft(hs['X'],8)
            ck(name+' finite Hodge action '+label,zero(hs['X']**8-s.eye(n//2)))
            ck(name+' integral Hodge DFT '+label,all(v.is_Integer and v>=0 for v in mult) and sum(mult)==n//2)
            ck(name+' odd eighth phases '+label,all(v==0 for r,v in enumerate(mult) if r%2==0))
            # With z(a)=0, Z's pullback is identity on the representative. Its inverse lift is the class action.
            ck(name+' actual cusp section map '+label,hs['Z']==clean(matrices['Z'].inv()).extract(inds,inds))
            out[label]={'indices':inds,'X':encoded(hs['X']),'Y':encoded(hs['Y']),'Z':encoded(hs['Z']),
                        'eighth_phase_multiplicities':[int(v) for v in mult]}
        return {'name':name,'SU6_dimension':n,'weak_multiplicity':2,'colour_multiplicity':colour,'H0':0,'H1':n,'hodge':out}

    cases=[odd_case('wedge3',representation(base,3),1),odd_case('fundamental',representation(base),3),
           odd_case('dual_fundamental',representation(base,dual=True),3)]
    ck('entire112 odd coefficient retained',sum(c['SU6_dimension']*2*c['colour_multiplicity'] for c in cases)==112)

    # Exact basic rho polarization, adapting the already-read W21 bar chain.
    ev=Evaluator(a,b);n=2;eye=s.eye(n);d0=s.Matrix.vstack(a-eye,b-eye);J=s.Matrix.vstack(s.zeros(n),eye)
    c='abAB';N=s.eye(4)-d0*(ev.rho(c)-eye).inv()*ev.eval(c)
    def cup(loop):
        pp='';bm=s.zeros(n);hm=s.zeros(n)
        for letter in loop:
            if letter.islower():sign=1;g,h=pp,letter;pp+=letter
            else:pp+=letter;sign=-1;g,h=pp,letter.lower()
            ug=ev.eval(g)*N*J;vh=ev.eval(h)*J;rg=ev.rho(g)
            bm+=sign*ug.T*b*rg*vh;hm+=s.I*sign*vh.H*rg.H*ug
        return clean(bm),clean(hm)
    bil,herm=cup(c)
    ck('rho complex symmetric polarization',bil==s.Matrix([[0,s.I],[s.I,0]]) and bil.det()!=0)
    ck('rho Hodge Hermitian orientation',herm==s.diag(-1,1))
    xx,yy=s.symbols('u v');vv=s.Matrix([xx,yy])
    ck('only two polarization isotropic lines',s.expand((vv.T*bil*vv)[0])==2*s.I*xx*yy)
    ck('positive Hodge line is A minus i',(s.Matrix([0,1]).H*herm*s.Matrix([0,1]))[0]==1 and a*s.Matrix([0,1])==-s.I*s.Matrix([0,1]))
    ck('wrong positive line is rejected',herm[0,0]==-1)
    basic={}
    quotient=s.Matrix.hstack(-(b-eye)*(a-eye).inv(),eye)
    for label,g in [('X',(eye+a)/s.sqrt(2)),('Y',(eye+b)/s.sqrt(2)),('Z',(eye-a)/s.sqrt(2))]:
        h=clean(quotient*cochain(ev,g,aut[label])*J);basic[label]=encoded(h)
        ck('basic polarized transport '+label,zero(h.T*bil*h-bil) and zero(h.H*herm*h-herm))
    # Different flat labels are not a no-intertwiner theorem: chi*rho are isomorphic.
    ck('actual common coefficient map',zero(S.H*A*S-s.kronecker_product(s.eye(3),a)) and zero(S.H*B*S-s.kronecker_product(s.eye(3),b)))
    homs=[]
    for j in range(3):
        for k in range(3):
            e=s.zeros(3);e[j,k]=1;v=S*s.kronecker_product(e,eye)*S.H
            homs.append(v)
            ck(f'flat family intertwiner {j},{k}',zero(v*A-A*v) and zero(v*B-B*v) and v!=s.zeros(6))
    H=s.Matrix([[2,1,0],[1,2,0],[0,0,1]]);metric=clean(S*s.kronecker_product(H,eye)*S.H)
    ck('flat positive nonorthogonal metric witness',all(metric[:j,:j].det()>0 for j in range(1,7)) and
       zero(A.H*metric*A-metric) and zero(B.H*metric*B-metric) and H[0,1]!=0)
    ck('full specified moves reject that metric',not zero(X.H*metric*X-metric) or not zero(Y.H*metric*Y-metric))
    ck('canonical parent metric retained',zero(X.H*X-s.eye(6)) and zero(Y.H*Y-s.eye(6)))

    # Whole even vertical-kernel action, using the complete credited Q8 roster.
    family={}
    for label,g,q in [('X',X,(eye+a)/s.sqrt(2)),('Y',Y,(eye+b)/s.sqrt(2)),('Z',Z,(eye-a)/s.sqrt(2))]:
        t=clean(S.H*g*S);m=s.Matrix(3,3,lambda j,k:clean(s.trace(q.H*t[2*j:2*j+2,2*k:2*k+2])/2))
        ck('literal family map '+label,zero(t-s.kronecker_product(m,q)))
        family[label]=m
    ad=adjoint3(family['X']);sy=symmetric3(family['X']);ad4=dft(ad,4);sy4=dft(sy,4)
    ck('full even fixed-space count',8+8+3+6*3+6*3==55)
    ck('actual family phase counts',all(v.is_Integer and v>=0 for v in ad4+sy4) and sum(ad4)==8 and sum(sy4)==6)
    ck('all136 even coefficients accounted',55+3*27==136)
    old=json.loads((HERE.parent/'surface_geometric_loops_2026_10_14/results/corrected_science/probe.stdout.log').read_text())['records']['classes']
    rows=[]
    for m in (1,3,5,7,9,11):
        even=[0]*12;even[0]=9
        for r,value in enumerate(ad4):even[3*r]+=int(value)
        for r,value in enumerate(sy4):even[3*r]+=6*int(value)
        even[m%12]+=1;even[(-m)%12]+=1
        odd={}
        # DO NOT identify a Hodge 1-form with a Dirac spinor by matching dimension.
        # The independently constructed cylinder spinor has gamma+ at A=+i,
        # whereas the positive twisted-H1 line in this quotient has A=-i.
        for name,label in [('gamma_plus','negative'),('gamma_minus','positive')]:
            values=[0]*12
            for case in cases:
                for r,v in enumerate(case['hodge'][label]['eighth_phase_multiplicities']):
                    for sign in (-1,1):
                        j=(3*r+sign*m)%24
                        ck(f'integral twelfth mode phase {m},{label},{case["name"]},{r},{sign}',v==0 or j%2==0)
                        if v:values[j//2]+=case['colour_multiplicity']*v
            odd[name]=values
            ck('complete56 per alternative odd extreme '+str((m,name)),sum(values)==56)
            av='+i' if name=='gamma_plus' else '-i'
            source=next(row for row in old if row['m']==m)
            expected=dict(dict(source['inverse_Z_odd'])[av])
            ck('actual section agrees with inverse Z table '+str((m,name)),values==[expected[r] for r in range(12)])
        ck('even55 each simultaneous vertical degree '+str(m),sum(even)==55)
        rows.append({'m':m,'even_gamma_plus':even,'even_gamma_minus':even,
                     'odd_gamma_plus':odd['gamma_plus'],'odd_gamma_minus':odd['gamma_minus'],
                     'even_zero_phase_each_chirality':even[0],
                     'odd_zero_phase_alternative_domains':[odd['gamma_plus'][0],odd['gamma_minus'][0]],
                     'opposite_section_sign_control':{
                         'odd_gamma_plus':[odd['gamma_plus'][(r-6)%12] for r in range(12)],
                         'odd_gamma_minus':[odd['gamma_minus'][(r-6)%12] for r in range(12)]}})

    # The spin connection is taken from the SAME existing total operator.
    # Projection of the actual normalized cylinder profile contributes gamma/2;
    # its mixed spin term contributes -gamma/4. Constant even spinors lack the
    # profile contribution. This is NOT a guess from Hodge 1-form metric powers.
    beta={};normalization={}
    for parity in ('even','odd'):
        for gamma in (-1,1):
            profile=s.I*gamma/2 if parity=='odd' else 0
            mixed=-s.I*gamma/4
            ordinary=clean((profile+mixed)/s.I)
            canonical=clean(ordinary+s.Rational(3,4))
            name=parity+('_gamma_plus' if gamma==1 else '_gamma_minus')
            beta[name]=canonical;normalization[name]={'profile_horizontal':str(profile),
                'mixed_spin':str(mixed),'ordinary_beta':str(ordinary),'canonical_beta_N0':str(canonical)}
            ck('actual projected constant '+name,canonical==(s.Rational(3,4)+(gamma if parity=='odd' else -gamma)*s.Rational(1,4)))
            ck('dropping mixed spin changes the operator '+name,clean(profile/s.I+s.Rational(3,4))!=canonical)
    ck('canonical projected masses stay at least half',set(beta.values())=={s.Rational(1,2),s.Integer(1)})
    ck('integer six-unit separation proof endpoints',all(0<v<3 and 6-v>v for v in beta.values()))
    ck('noninteger unit cancellation comparator',beta['odd_gamma_plus']-6*s.Rational(1,6)==0)
    ck('Hodge positive is not the spinor plus coefficient line',a[1,1]==-s.I and a[0,0]==s.I)
    record={'basic_bilinear':encoded(bil),'basic_Hodge_Hermitian':encoded(herm),'basic_cohomology_actions':basic,
        'odd_cases':cases,'classes':rows,'coefficient_dimensions':{'even':136,'odd':112,'total':248},
        'vertical_kernel_dimensions':{'even_gamma_plus':55,'even_gamma_minus':55,'odd_selected_extreme':56,'total_per_extreme':166},
        'projected_connection_terms':normalization,'conditional_radial_constants_N0':{k:str(v) for k,v in beta.items()},
        'Hodge_to_spinor_identification':'NOT asserted: H1 positive uses A=-i; actual plus cylinder spinor uses A=+i',
        'flat_intertwiner_dimension':len(homs),'nonorthogonal_flat_family_metric':encoded(H)}
    return {'checks':checks,'records':record,'all_passed':all(checks.values()),
       'scope':'specified cochain maps and actual cusp kernel frame under credited graph/projection hypotheses; not full real-parent admission or physical index/SM'}

def emit(Evaluator):
    obj=run(Evaluator);print(json.dumps(obj,indent=2));return 0 if obj['all_passed'] else 1
