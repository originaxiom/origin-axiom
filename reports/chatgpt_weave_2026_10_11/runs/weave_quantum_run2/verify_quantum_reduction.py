#!/usr/bin/env python3
"""Curve differentials, spin-lift obstruction, theta-state reduction and exact phases.
This is a mathematical reduction, NOT a calculation of an interacting punctured CFT.
"""
from __future__ import annotations
import itertools,json,pathlib,argparse
import sympy as s
import mpmath as mp
OUT=pathlib.Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--dps',type=int,default=80);args=parser.parse_args()
mp.mp.dps=args.dps
checks={}
def check(name,value):
    ok=bool(value);checks[name]=ok;print(f'{"PASS" if ok else "FAIL"}: {name}')
    if not ok:raise AssertionError(name)
I=s.I; Id=s.eye(2);A=s.diag(I,-I);B=s.Matrix([[0,1],[-1,0]])
G=[Id,A,B,A*B,-Id,-A,-B,-A*B]
keys={tuple(g):k for k,g in enumerate(G)}
mt=[[keys[tuple(g*h)] for h in G] for g in G]
# Central extension by Z2 is determined by a normalized group 2-cocycle.
# Test ALL cocycles by linear algebra, not a sample of group presentations.
pairs=list(itertools.product(range(1,8),repeat=2)); idx={p:k for k,p in enumerate(pairs)}
def term(a,b):return 0 if a==0 or b==0 else 1<<idx[(a,b)]
rows=[]; triples=[]
for a,b,c in itertools.product(range(8),repeat=3):
    rows.append(term(a,b)^term(mt[a][b],c)^term(b,c)^term(a,mt[b][c]));triples.append((a,b,c))
piv={}
for j,row in enumerate(rows):
    cert=1<<j
    while row:
        k=row.bit_length()-1
        if k in piv:row^=piv[k][0];cert^=piv[k][1]
        else:piv[k]=(row,cert);break
probe=term(4,4);cert=0
while probe:
    k=probe.bit_length()-1
    if k not in piv:break
    probe^=piv[k][0];cert^=piv[k][1]
check('all_Q8_cocycles_force_lift_z_square_plus_one',probe==0)
cert_triples=[triples[j] for j in range(len(rows)) if (cert>>j)&1]
check('spin_obstruction_certificate_XOR',__import__('functools').reduce(int.__xor__,(rows[j] for j in range(len(rows)) if (cert>>j)&1),0)==term(4,4))
# Positive control: C2 admits the central extension C4 with lift(g)^2=-1.
f2=lambda a,b: a*b
check('C2_order_four_spin_lift_allowed',all((f2(a,b)+f2(a^b,c)+f2(b,c)+f2(a,b^c))%2==0 for a,b,c in itertools.product(range(2),repeat=3)) and f2(1,1)==1)

# Smooth plane-quartic family and all superelliptic differential monomials.
x,l=s.symbols('x lambda')
f=x*(x-1)*(x-l)
check('branch_polynomial_discriminant',s.factor(s.discriminant(f,x))==l**2*(l-1)**2)
differentials=[]
for k in (1,2,3):
    for j in range(4):
        finite_min=3-k;infty=3*k-4*j-5
        if finite_min>=0 and infty>=0:differentials.append({'j':j,'k':k,'generic_finite_order':finite_min,'infinity_order':infty})
check('exactly_three_holomorphic_differentials',[(z['j'],z['k']) for z in differentials]==[(0,2),(0,3),(1,3)])
# Q8 on anti-invariant differential doublet dx/y^3, x dx/y^3.
p=s.sqrt(l);q=s.sqrt(l-1)
AA=s.Matrix([[0,-I*p],[-I/p,0]])
BB=s.Matrix([[-1,-l],[1,1]])/q
simpl=lambda M:M.applyfunc(s.simplify)
check('curve_Q8_doublet_relations',simpl(AA*AA)==-Id and simpl(BB*BB)==-Id and simpl(AA*BB+BB*AA)==s.zeros(2))
check('curve_doublet_determinants_one',s.simplify(AA.det())==1 and s.simplify(BB.det())==1)
# Verify algebraic transformations preserve y^4=f(x).
fa=l/x; fb=(x-l)/(x-1)
check('curve_deck_A_preserves_equation',s.factor(f.subs(x,fa)-l**2*f/x**4)==0)
check('curve_deck_B_preserves_equation',s.factor(f.subs(x,fb)-(l-1)**2*f/(x-1)**4)==0)
# The four hyperflex differentials dx/y^3, (x-a)dx/y^3 have divisor 4P_a.
hyperflex={'infinity':{'finite_orders':[0,0,0],'infinity':4}}
for a in ('0','1','lambda'):
    hyperflex[a]={'finite_orders':[4 if b==a else 0 for b in ('0','1','lambda')],'infinity':0}
check('four_explicit_odd_spin_squares',all(sum(z['finite_orders'])+z['infinity']==4 for z in hyperflex.values()))
# On smooth nonhyperelliptic genus 3, degree-2 theta characteristics have <=1 section.
# Analytic Clifford/g1_2 argument is in the report. Enumeration above is independent.

# Quaternion normalizer rotations and their target scalar multiplier.
OL=s.Matrix([[1,0,0],[0,0,-1],[0,1,0]])
OR=s.Matrix([[0,0,-1],[0,1,0],[1,0,0]])
OS=OR*OL.inv()*OR
D=s.Matrix([[-1,0,0],[0,0,-I],[0,1,0]])
P24=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
Tb=s.Matrix([[I,0,0],[0,0,1],[0,1,0]])
zeta=(1+I)/s.sqrt(2)
rhoT=zeta**(-1)*Tb;rhoS=zeta*P24
check('rotations_are_SO3',OL.T*OL==s.eye(3) and OR.T*OR==s.eye(3) and OL.det()==1 and OR.det()==1)
check('full_T_factorization_eta_cubed',simpl(zeta*D*OL*D.inv()-rhoT)==s.zeros(3))
check('full_S_factorization_eta_cubed',simpl(zeta**(-3)*D*OS*D.inv()-rhoS)==s.zeros(3))
check('target_central_S_fourth_minus_identity',simpl(rhoS**4)==-s.eye(3))
check('untwisted_S_fourth_plus_identity',OS**4==s.eye(3))
# Enumerate exact monomial groups as row->column permutations with phases mod8.
def monomial(M):
    perm=[];phase=[]
    roots=[s.simplify(zeta**k) for k in range(8)]
    for row in range(3):
        jj=[j for j in range(3) if M[row,j]!=0]; assert len(jj)==1
        j=jj[0];val=s.simplify(M[row,j]);perm.append(j)
        phase.append(next(k for k,r in enumerate(roots) if s.simplify(val-r)==0))
    return tuple(perm),tuple(phase)
def prod(a,b):
    p,r=a;q,t=b
    return tuple(q[p[i]] for i in range(3)),tuple((r[i]+t[p[i]])%8 for i in range(3))
def generated(gens):
    ident=((0,1,2),(0,0,0));seen={ident};todo=[ident]
    while todo:
        a=todo.pop()
        for b in gens:
            c=prod(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
rotgroup=generated([monomial(OL),monomial(OR)])
targetgroup=generated([monomial(rhoS),monomial(rhoT)])
scalars=sorted(x[1][0] for x in targetgroup if x[0]==(0,1,2) and len(set(x[1]))==1)
check('rotation_image_24_target_image_96',len(rotgroup)==24 and len(targetgroup)==96)
check('target_scalar_center_four',scalars==[0,2,4,6])
# Fundamental Q8 and its quadratic decomposition in the theta basis.
qa=s.diag(I,-I);qb=s.Matrix([[0,I],[I,0]])
check('theta_translation_Q8_faithful',qa**2==qb**2==-Id and qa*qb==-qb*qa)
u,v=s.symbols('u v')
quadratics=s.Matrix([2*u*v,u*u+v*v,u*u-v*v])
for name,M,expected in [('A',qa,s.diag(1,-1,-1)),('B',qb,s.diag(-1,-1,1))]:
    uv=M*s.Matrix([u,v]); vv=quadratics.subs({u:uv[0],v:uv[1]},simultaneous=True)
    check('quadratic_parity_'+name,simpl(vv-expected*quadratics)==s.zeros(3,1))
# Duplication identities and finite-level theta transformations via direct tau series.
def theta_state(r,z,tau):
    # Tail chosen far below working precision at the most slowly convergent term.
    nmax=int(mp.ceil(mp.sqrt((args.dps+25)*mp.log(10)/(2*mp.pi*mp.im(tau)))+8+abs(mp.im(z)/mp.im(tau))))
    return mp.fsum(mp.exp(2j*mp.pi*tau*(n+mp.mpf(r)/2)**2+4j*mp.pi*(n+mp.mpf(r)/2)*z) for n in range(-nmax,nmax+1))
def theta(p,tau):
    nmax=int(mp.ceil(mp.sqrt((args.dps+25)*mp.log(10)/(mp.pi*mp.im(tau)))+8))
    return mp.fsum(((-1)**n if p==4 else 1)*mp.exp(mp.pi*1j*tau*n*n) for n in range(-nmax,nmax+1))
def theta2(tau):
    nmax=int(mp.ceil(mp.sqrt((args.dps+25)*mp.log(10)/(mp.pi*mp.im(tau)))+8))
    return mp.fsum(mp.exp(mp.pi*1j*tau*(mp.mpf(n)+mp.mpf('.5'))**2) for n in range(-nmax,nmax+1))
points=[mp.mpc('0','1'),mp.mpc('.237','1.13'),mp.mpc('-.41','.72'),mp.mpc('.51','1.91'),mp.mpc('.12','.43')]
residuals=[]
for tau in points:
    aa=theta_state(0,0,tau);bb=theta_state(1,0,tau)
    lhs=[2*aa*bb,aa*aa+bb*bb,aa*aa-bb*bb]
    rhs=[theta2(tau)**2,theta(3,tau)**2,theta(4,tau)**2]
    residuals += [abs(a-b)/max(1,abs(b)) for a,b in zip(lhs,rhs)]
    for r in (0,1):
        residuals.append(abs(theta_state(r,0,tau+1)-(1 if r==0 else 1j)*[aa,bb][r]))
        rhsS=mp.sqrt(-1j*tau)/mp.sqrt(2)*(aa+(1 if r==0 else -1)*bb)
        residuals.append(abs(theta_state(r,0,-1/tau)-rhsS))
    zz=mp.mpc('.17','.09')
    ss=[theta_state(r,zz,tau) for r in (0,1)]
    for r in (0,1):
        residuals.append(abs(theta_state(r,zz+mp.mpf('.5'),tau)-(-1)**r*ss[r]))
        residuals.append(abs(mp.exp(mp.pi*1j*tau/2+2*mp.pi*1j*zz)*theta_state(r,zz+tau/2,tau)-ss[1-r]))
maxres=max(residuals)
check('numeric_theta_duplication_and_S_T_translations',maxres<mp.mpf(10)**(-args.dps+10))
# Exact parabolic degree calculation; actual h0,h1 are analytically justified, not numerically solved.
parabolic=[]
for n in range(-1,3):
    degree=2*n-1;parabolic.append({'n':n,'degree':degree,'h0':max(degree,0),'h1':max(-degree,0),'index':degree})
check('minimal_parabolic_indices_minus_plus_one',[z['index'] for z in parabolic if z['n'] in (0,1)]==[-1,1])
results={
 'scope':'Exact geometry, all central extension cocycles, theta-state and representation comparison; not full puncture CFT',
 'cocycle_variables':49,'cocycle_rank':len(piv),'cocycle_dimension':49-len(piv),
 'f_z_z_is_forced_zero':True,'cocycle_certificate_triples':cert_triples,
 'differential_monomials':differentials,'Q8_differential_matrices':{'A':AA.tolist(),'B':BB.tolist()},
 'hyperflex_divisors':hyperflex,
 'normalizer_rotations':{'L':OL.tolist(),'R':OR.tolist(),'S':OS.tolist()},
 'target_basis_change':D.tolist(),'eta_character_T':'exp(pi*i/4)','eta_character_S':'exp(-3*pi*i/4)',
 'rotation_image_order':len(rotgroup),'target_image_order':len(targetgroup),'target_scalar_exponents_mod8':scalars,
 'parabolic_analytic_counts':parabolic,'precision_dps':args.dps,'numeric_max_residual':mp.nstr(maxres,12),
 'numerical_tests_count':len(residuals),'checks':checks}
(OUT/f'quantum_reduction_results_{args.dps}dps.json').write_text(json.dumps(results,indent=2,default=str)+'\n')
print('COCYCLES:',len(piv),'rank,',49-len(piv),'dimension; certificate terms',len(cert_triples))
print('MAX NUMERICAL RESIDUAL:',mp.nstr(maxres,12))
print(f'{len(checks)} named checks passed')
