"""Full8-component zero Cauchy plane; frozen prior arithmetic, no old run.

Exact/numerical grades separate. Not a global core join or particle census.
"""
import importlib.util,json
from pathlib import Path
import sympy as s
import mpmath as mp

HERE=Path(__file__).resolve().parent; REPO=HERE.parents[2]

def arithmetic():
    spec=importlib.util.spec_from_file_location('pinned_end_arithmetic',
        HERE.parent/'silver_gauge_end_transport_2026_10_12/probe.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def columns(F,G,W,L,ell):
    c=G+(W+1/ell)*F;d=-G+(W-1/ell)*F;B=s.zeros(8,4)
    B[0,0]=F;B[3,0]=s.I*c/L
    B[1,1]=c;B[2,1]=s.I*L*F
    B[5,2]=s.I*L*F;B[6,2]=d
    B[4,3]=s.I*d/L;B[7,3]=F
    return B

def physical_maps():
    odd=s.zeros(8,4);even=s.zeros(8,4)
    for row,col in ((7,0),(1,1),(2,2),(4,3)):odd[row,col]=1
    for row,col,sign in ((0,0,-1),(6,1,1),(5,2,-1),(3,3,1)):even[row,col]=sign
    return odd,even

def projector(mu,K,ell=1):
    ell=mp.mpf(ell);mu=mp.mpf(mu);K=mp.mpf(K)
    beta=abs(mu);x=beta*ell;delta=K*K/(4*beta*ell)
    f=lambda t:mp.whitw(-delta,mp.mpf('0.5'),t)/mp.sqrt(t)
    G=2*x/ell*mp.diff(f,x)/f(x);L=K/ell;W=mu
    c=G+W+1/ell;d=-G+W-1/ell
    B=mp.matrix(8,4)
    B[0,0]=1;B[3,0]=1j*c/L;B[1,1]=c;B[2,1]=1j*L
    B[5,2]=1j*L;B[6,2]=d;B[4,3]=1j*d/L;B[7,3]=1
    # Disjoint column supports make this normalization stable near K=0.
    P=mp.matrix(8)
    for j in range(4):
        norm=sum(abs(B[i,j])**2 for i in range(8))
        for i in range(8):
            for k in range(8):P[i,k]+=B[i,j]*mp.conj(B[k,j])/norm
    return G,P

def run():
    p=arithmetic();checks={};numeric={};mp.mp.dps=50
    def ck(name,value):
        checks[name]=bool(value)
        if not checks[name]:raise AssertionError(name)
    def nc(name,error,tolerance=mp.mpf('1e-38'),grade='precision'):
        numeric[name]={'passed':bool(error<tolerance),'residual':mp.nstr(error,20),
                       'tolerance':mp.nstr(tolerance,20),'grade':grade}
        if not numeric[name]['passed']:raise AssertionError(name)
    r=s.symbols('r',real=True);ell,beta,K=s.symbols('ell beta K',positive=True)
    phi=s.Function('phi',real=True)(r);L=K*s.exp(r/ell)/ell
    v0=beta**2*s.exp(4*r/ell)+ell**-2+L**2
    for sign in (1,-1):
        W=sign*beta*s.exp(2*r/ell)
        _,_,q,square=p.full_operator(r,ell,sign*beta,K,0)
        B=columns(phi,s.diff(phi,r),W,L,ell)
        residual=(q[0]*B.diff(r)+q[1]*B).applyfunc(s.expand)
        reduced=residual.applyfunc(lambda v:s.simplify(v.subs(s.diff(phi,r,2),v0*phi)))
        ck('all_full_Q_columns_'+str(sign),p.mz(reduced))
        ck('actual_scalar_potential_'+str(sign),s.simplify(square[2][0,0]-v0)==0)
        So,Se=physical_maps()
        odd_profiles=So.T*B[:,[1,3]];even_profiles=Se.T*B[:,[0,2]]
        for label,left,right,profiles in (('R',Se,So,odd_profiles),('R_adjoint',So,Se,even_profiles)):
            res=left.T*q[0]*right*profiles.diff(r)+left.T*q[1]*right*profiles
            ck('actual_physical_'+label+'_columns_'+str(sign),
               p.mz(res.applyfunc(lambda v:s.simplify(s.expand(v).subs(s.diff(phi,r,2),v0*phi)))))
        # Removing a mixed component really violates the SAME operator.
        bad=B.copy();bad[3,0]=0
        wrong=(q[0]*bad.diff(r)+q[1]*bad).applyfunc(lambda v:s.simplify(s.expand(v).subs(s.diff(phi,r,2),v0*phi)))
        ck('dropped_mixed_component_rejected_'+str(sign),not p.mz(wrong[:,0]))
        phase=beta*ell/2*(s.exp(2*r/ell)-1)
        Z=s.zeros(8,4)
        supports=[0,2,6,4] if sign==1 else [3,1,5,7]
        offsets=[-1,0,1,0] if sign==1 else [0,1,0,-1]
        for j,(ix,g) in enumerate(zip(supports,offsets)):Z[ix,j]=s.exp(g*r/ell-phase)
        q0=p.full_operator(r,ell,sign*beta,0,0)[2]
        ck('angular_zero_full_profiles_'+str(sign),p.mz(q0[0]*Z.diff(r)+q0[1]*Z))
        ck('angular_zero_four_independent_'+str(sign),Z.rank()==4)
        ck('angular_zero_parities_two_each_'+str(sign),sum(i.bit_count()%2==0 for i in supports)==2)
    F=s.symbols('F',positive=True);G,W=s.symbols('G W',real=True)
    B=columns(F,G,W,K/ell,ell);Cr=p.exterior(0)-p.exterior(0).T
    ck('actual_Cauchy_rank_four',B.rank()==4)
    ck('actual_Cauchy_maximal_Green_null',p.mz(B.H*Cr*B))
    ck('odd_even_complete_two_each',B.extract([1,2,4,7],[1,3]).rank()==2 and B.extract([0,3,5,6],[0,2]).rank()==2)
    bad=B.copy();bad[1,0]=s.I*F
    ck('wrong_green_plane_rejected',not p.mz(bad.H*Cr*bad))
    So,Se=physical_maps()
    ck('actual_physical_isometries',So.T*So==s.eye(4) and Se.T*Se==s.eye(4))
    odd=So.T*B[:,[1,3]];even=Se.T*B[:,[0,2]]
    ck('actual_physical_odd_trace_formula',odd==s.Matrix([[0,F],[G+(W+1/ell)*F,0],[s.I*K/ell*F,0],[0,s.I*(-G+(W-1/ell)*F)/(K/ell)]]))
    ck('physical_even_and_odd_complete',odd.rank()==2 and even.rank()==2)
    # Joint neutral corner: two L2 exponentials; four constant resonances.
    neutral=p.full_operator(r,ell,0,0,0)[2]
    N=s.zeros(8,2);N[0,0]=s.exp(-r/ell);N[7,1]=s.exp(-r/ell)
    ck('neutral_two_L2_profiles',p.mz(neutral[0]*N.diff(r)+neutral[1]*N) and N.rank()==2)
    constants=s.zeros(8,4)
    for j,ix in enumerate((2,3,4,5)):constants[ix,j]=1
    ck('neutral_constant_threshold_profiles',p.mz(neutral[1]*constants) and constants.rank()==4)
    x,delta=s.symbols('x delta',positive=True);Y=s.Function('Y')(x)
    transformed=Y/s.sqrt(x)
    scalar=-4*(x*x*s.diff(transformed,x,2)+x*s.diff(transformed,x))+(x*x+1+4*delta*x)*transformed
    whittaker=-4*x**s.Rational(3,2)*(s.diff(Y,x,2)+(-s.Rational(1,4)-delta/x)*Y)
    ck('actual_scalar_Whittaker_reduction',s.simplify(scalar-whittaker)==0)
    nc_data=[]
    for sign in (1,-1):
        mu=mp.mpf(sign)*mp.mpf('0.4')
        for kk in (mp.mpf('.6'),mp.mpf('1e-4'),mp.mpf('1e-6')):
            logder,P=projector(mu,kk)
            nc('projector_idempotent_'+str(sign)+'_'+str(kk),max(abs(x) for x in P*P-P))
            nc('projector_Hermitian_'+str(sign)+'_'+str(kk),max(abs(x) for x in P-P.H))
            target=mp.matrix(8);indices=(0,2,4,6) if sign==1 else (1,3,5,7)
            for ix in indices:target[ix,ix]=1
            if kk<mp.mpf('.01'):
                nc('fixed_wall_zero_angular_subspace_'+str(sign)+'_'+str(kk),max(abs(x) for x in P-target),mp.mpf('1e-3'),'finite_limit')
            nc_data.append({'sign':sign,'K':str(kk),'scalar_log_derivative':mp.nstr(logder,24),
                            'projector':[[{'re':mp.nstr(P[i,j].real,24),'im':mp.nstr(P[i,j].imag,24)}
                                          for j in range(8)] for i in range(8)]})
    return {'checks':checks,'exact_passed':sum(checks.values()),'numerical_checks':numeric,
            'Cauchy_matrix':[[str(v) for v in row] for row in B.tolist()],
            'physical_odd_Cauchy':[[str(v) for v in row] for row in odd.tolist()],
            'numeric_projectors':nc_data,'complete_end_dimension':4,'odd_even_dimensions':[2,2],
            'neutral_corner_L2_dimension':2,'global_particles_or_chirality':False,
            'frequency_response_solved':False,'core_join_solved':False,'SM_selection_derived':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,default=str))
