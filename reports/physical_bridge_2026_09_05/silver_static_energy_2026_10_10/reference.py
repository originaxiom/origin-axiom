"""Jordan-Wigner and real-coordinate reference. No native imports."""
from functools import lru_cache
import json
import sympy as s

@lru_cache(None)
def run():
    ok={}
    def ck(k,v):ok[k]=bool(v)
    I=s.I;E=s.eye(2);Z=s.diag(1,-1);C=s.Matrix([[0,0],[1,0]])
    generators=[s.kronecker_product(*([Z]*j+[C]+[E]*(3-j))) for j in range(4)]
    annihilators=[g.T for g in generators]
    ident=s.eye(16);nil=s.zeros(16)
    ck('Clifford_creation_anticommutators',all(generators[i]*generators[j]+generators[j]*generators[i]==nil for i in range(4) for j in range(4)))
    ck('creation_contraction_pairing',all(annihilators[i]*generators[j]+generators[j]*annihilators[i]==(ident if i==j else nil) for i in range(4) for j in range(4)))
    th=2*generators[0]*generators[1];bar=-2*generators[2]*generators[3];top=th*bar
    # In this tensor ordering bit0 has weight8. theta2 occupies state12;
    # tau occupies state15. This is not the native bit-mask ordering.
    ck('theta_reversed_product_adjoints',2*generators[3]*generators[2]==bar)
    ck('Berezin_top',top[15,0]==-4)
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);T=Z
    p=X+2*I*Y;f=2*X+Y+3*I*T;d=Y+T;jet=X-2*T
    tens=s.kronecker_product
    g=tens(ident,E)+tens(top,d);gi=tens(ident,E)-tens(top,d)
    phi=tens(ident,p)+tens(th,f);barphi=tens(ident,p.H)+tens(bar,f.H)
    zz=gi*tens(top,jet)+I*gi*barphi*g-I*phi
    def block(a,row):return a[2*row:2*row+2,0:2]
    ck('nilpotent_exponential_inverse',g*gi==s.eye(32))
    expected=tens(ident,4*Y)-I*tens(th,f)+I*tens(bar,f.H)+tens(top,jet+I*(p.H*d-d*p.H))
    ck('operator_static_Z',zz==expected)
    kinetic=-s.trace(block(zz*zz,15))/16
    expectedK=s.trace(2*Y*(jet+I*(X*d-d*X)))+s.trace(f*f.H)/2
    ck('operator_kinetic_half',s.expand(kinetic-expectedK)==0)
    ck('operator_wrong_F_coefficient_rejected',s.expand(kinetic-expectedK-3*s.trace(f*f.H)/2)!=0)
    aa=[tens(v,E) for v in annihilators]
    def derivative(a,j,parity):return aa[j]*a-(-1)**parity*a*aa[j]
    ws=[]
    for j in (0,1):
        first=gi*derivative(g,j,0)
        second=-derivative(first,3,1)
        third=-derivative(second,2,0)
        ws.append(third/2)
    ck('operator_W_first_spinor',ws[0]==2*tens(generators[1],d))
    ck('operator_W_second_spinor',ws[1]==-2*tens(generators[0],d))
    w2=ws[0]*ws[1]-ws[1]*ws[0]
    gauge=(s.trace(block(w2,12))/2+s.conjugate(s.trace(block(w2,12))/2))/16
    ck('operator_gauge_half',s.expand(gauge-s.trace(d*d)/2)==0)
    # Independent cubic-only CS expansion with F_i=phi_i.
    ps=[X,Y,T];phis=[tens(ident,p0)+tens(th,p0) for p0 in ps]
    raw=s.zeros(32);source=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                epsilon=s.LeviCivita(i,j,k)
                raw+=I*epsilon*phis[i]*(phis[j]*phis[k]-phis[k]*phis[j])/3
                source+=I*epsilon*s.trace(ps[i]*(ps[j]*ps[k]-ps[k]*ps[j]))
    ck('cubic_CS_source_operator',s.expand(s.trace(block(raw,12))/2-source)==0 and source!=0)
    # Independent real coordinate differentiation: three unlinked choices
    # of positive kinetic coefficient also catch scale drift.
    d0,m,x,y,r,q,k=s.symbols('d0 m x y r q k',real=True)
    ell=d0*d0/2-d0*m+k*(x*x+y*y)+(x*r-y*q)/2
    stationary=s.solve([s.diff(ell,v) for v in (d0,x,y)],(d0,x,y),dict=True)[0]
    ck('general_auxiliary_scale',stationary=={d0:m,x:-r/(4*k),y:q/(4*k)})
    half={key:s.simplify(val.subs(k,s.Rational(1,2))) for key,val in stationary.items()}
    ck('actual_complex_solution',s.expand((x+I*y).subs(half)+(r-I*q)/2)==0)
    ck('wrong_conjugate_fails_real_EOM',s.diff(ell,y).subs({k:s.Rational(1,2),y:-q/2})==-q)
    onshell=s.expand(ell.subs(k,s.Rational(1,2)).subs(half))
    ck('positive_potential_from_real_elimination',onshell==-m*m/2-r*r/8-q*q/8)
    ck('residual_positive_Hessian',s.hessian(-onshell,(m,r,q))==s.diag(1,s.Rational(1,4),s.Rational(1,4)))
    ck('wrong_kinetic_changes_physical_scale',stationary[x].subs(k,2)!=half[x])
    z=s.symbols('z',real=True)
    b=z+z*z;aux=1+z*z
    integral=s.integrate(b*s.diff(aux,z),(z,0,1))
    bulk=-s.integrate(aux*s.diff(b,z),(z,0,1))
    surface=(b*aux).subs(z,1)-(b*aux).subs(z,0)
    ck('real_surface_exact_IBP',integral==bulk+surface and surface!=0)
    ck('omitted_surface_is_not_same_action',integral!=bulk)
    ck('parallel_flux_integral_zero',s.integrate(2*z-1,(z,0,1))==0)
    ck('nonparallel_D_flux_nonzero',s.integrate((2*z-1)**2,(z,0,1))==s.Rational(1,3))
    ck('positive_and_zero_residual_directions',(-onshell).subs({m:1,r:0,q:0})==s.Rational(1,2) and (-onshell).subs({m:0,r:0,q:0})==0)
    out={'predicates':ok,'predicates_passed':sum(ok.values()),
         'normalizations':{'F_kinetic':'1/2','D_kinetic':'1/2','Fc_source':'1/4','F_solution':'-c_dagger/2','V':'norm(mu)^2/2+norm(c)^2/8'},
         'same_author_different_method':True,'physical_kernel_computed':False,
         'full_dynamical_stability_proved':False,'physical_goal_achieved':False}
    assert all(ok.values()),[k for k,v in ok.items() if not v]
    return out

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
