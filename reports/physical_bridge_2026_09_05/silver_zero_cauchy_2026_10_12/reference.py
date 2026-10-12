"""Four reduced2-systems and Euler-integral controls; no native import.

Same author, no independent analytic acceptance. Separate exact/numeric.
"""
import json
import sympy as s
import mpmath as mp

def run():
    checks={};numeric={};mp.mp.dps=50
    def ck(name,value):
        checks[name]=bool(value)
        if not checks[name]:raise AssertionError(name)
    def nc(name,error,tol=mp.mpf('1e-38'),grade='precision'):
        numeric[name]={'passed':bool(error<tol),'residual':mp.nstr(error,20),
                       'tolerance':mp.nstr(tol,20),'grade':grade}
        if not numeric[name]['passed']:raise AssertionError(name)
    r=s.symbols('r',real=True);ell,beta,K=s.symbols('ell beta K',positive=True)
    f=s.Function('f')(r);L=K*s.exp(r/ell)/ell
    pot=beta**2*s.exp(4*r/ell)+ell**-2+L**2
    for sign in (1,-1):
        W=sign*beta*s.exp(2*r/ell)
        A0=lambda t:s.diff(t,r)+(W+1/ell)*t
        Ad0=lambda t:-s.diff(t,r)+(W+1/ell)*t
        A1=lambda t:s.diff(t,r)+W*t
        Ad1=lambda t:-s.diff(t,r)+W*t
        A2=lambda t:s.diff(t,r)+(W-1/ell)*t
        Ad2=lambda t:-s.diff(t,r)+(W-1/ell)*t
        systems=[(f,s.I*A0(f)/L),(A0(f),s.I*L*f),(s.I*L*f,Ad2(f)),(s.I*Ad2(f)/L,f)]
        a,b=systems[0];res0=(A0(a)+s.I*L*b,s.I*L*a+Ad1(b))
        a,b=systems[1];res1=(Ad0(a)-s.I*L*b,-s.I*L*a+A1(b))
        a,b=systems[2];res2=(Ad1(a)-s.I*L*b,-s.I*L*a+A2(b))
        a,b=systems[3];res3=(A1(a)+s.I*L*b,s.I*L*a+Ad2(b))
        for j,res in enumerate((res0,res1,res2,res3)):
            ck('reduced_complete_system_'+str(sign)+'_'+str(j),
               all(s.simplify(s.expand(v).subs(s.diff(f,r,2),pot*f))==0 for v in res))
        ck('both_scalar_factorizations_'+str(sign),
           s.simplify(Ad0(A0(f))+L**2*f-(-s.diff(f,r,2)+pot*f))==0 and
           s.simplify(A2(Ad2(f))+L**2*f-(-s.diff(f,r,2)+pot*f))==0)
    F=s.symbols('F',positive=True);G,W=s.symbols('G W',real=True);l=s.symbols('l',positive=True)
    c=G+(W+1/ell)*F;d=-G+(W-1/ell)*F
    # Independent2-system trace rows, not full8 creation matrices.
    even0=(F,s.I*c/l);odd0=(c,s.I*l*F)
    evenY=(s.I*l*F,d);oddY=(s.I*d/l,F)
    inner=lambda x,y:sum(s.conjugate(a)*b for a,b in zip(x,y))
    ck('first_actual_Green_pair_cancels',s.simplify(inner(even0,(-odd0[0],odd0[1])))==0)
    ck('second_actual_Green_pair_cancels',s.simplify(inner(evenY,(oddY[0],-oddY[1])))==0)
    ck('nonzero_mixed_components_retained',even0[1]!=0 and oddY[0]!=0)
    ck('trace_scalar_invertibility',F!=0 and l!=0)
    # Euler U integral: a=1+delta,b=2. No whitw call in this method.
    rows=[]
    for beta0,ell0,k0 in ((mp.mpf('.4'),mp.mpf(1),mp.mpf('.6')),
                          (mp.mpf('.4'),mp.mpf(1),mp.mpf('1e-6'))):
        x=beta0*ell0;delta=k0*k0/(4*beta0*ell0)
        base=lambda y:4*y**(3+4*delta)*(1+y**4)**(-delta)*mp.exp(-x*y**4)/mp.gamma(1+delta)
        U=mp.quad(base,[0,1,mp.inf]);Up=-mp.quad(lambda y:y**4*base(y),[0,1,mp.inf])
        G0=2*x/ell0*(mp.mpf('.5')/x-mp.mpf('.5')+Up/U)
        for sign in (1,-1):
            mu=sign*beta0;LL=k0/ell0;c0=G0+mu+1/ell0;d0=-G0+mu-1/ell0
            pairs=[(1,1j*c0/LL),(c0,1j*LL),(1j*LL,d0),(1j*d0/LL,1)]
            P=mp.matrix(8);supports=((0,3),(1,2),(5,6),(4,7))
            for pair,indices in zip(pairs,supports):
                norm=sum(abs(v)**2 for v in pair)
                for a,ia in enumerate(indices):
                    for b,ib in enumerate(indices):P[ia,ib]=pair[a]*mp.conj(pair[b])/norm
            nc('Euler_projector_trace_'+str(sign)+'_'+str(k0),abs(sum(P[j,j] for j in range(8))-4))
            nc('Euler_projector_idempotent_'+str(sign)+'_'+str(k0),max(abs(v) for v in P*P-P))
            if k0<mp.mpf('.01'):
                target=mp.matrix(8)
                for j in ((0,2,4,6) if sign==1 else (1,3,5,7)):target[j,j]=1
                nc('Euler_fixed_wall_zero_angle_'+str(sign),max(abs(v) for v in P-target),mp.mpf('1e-3'),'finite_limit')
            rows.append({'sign':sign,'K':str(k0),'scalar_log_derivative':mp.nstr(G0,24),
                         'projector':[[{'re':mp.nstr(P[i,j].real,24),'im':mp.nstr(P[i,j].imag,24)}
                                       for j in range(8)] for i in range(8)]})
    # Zero-wall positive angular control: scalar modified-Bessel equation.
    z=mp.mpf('.7');ell0=mp.mpf('1.3');f0=lambda t:mp.besselk(1,z*mp.exp(t/ell0))
    t=mp.mpf('.2')
    res=-mp.diff(f0,t,2)+(1/ell0**2+(z/ell0)**2*mp.exp(2*t/ell0))*f0(t)
    nc('zero_wall_Bessel_scalar_control',abs(res)/(1+abs(f0(t))))
    nc('zero_angular_scalar_log_derivative_control',abs(mp.diff(lambda rr:mp.exp(-rr/ell0-mp.mpf('.4')*ell0/2*(mp.exp(2*rr/ell0)-1)),0)+mp.mpf('.4')+1/ell0))
    return {'exact_checks':checks,'exact_passed':sum(checks.values()),'numerical_checks':numeric,
            'numeric_projectors':rows,'method':'reduced2-systems/Euler integration, no native or whitw import',
            'outside_review':False,'global_core_or_particles':False,'SM_selection_derived':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,default=str))
