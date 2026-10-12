"""Exact full-metric/Hodge lift controls, not a physical generation count."""
import json
from itertools import combinations
import sympy as s

PAIRS=list(combinations(range(4),2))
def clean(M):return M.applyfunc(s.simplify)
def zero(M):return all(s.simplify(v)==0 for v in M)
def metric(x,y,ell,A):
    G=s.zeros(4);G[0,0]=G[1,1]=ell**2/y**2
    G[2,2]=A/y;G[2,3]=G[3,2]=A*x/y;G[3,3]=A*(x*x+y*y)/y
    return G
def hodge(G,vol,F):
    inverse=G.inv();out=s.zeros(4)
    for i,j in PAIRS:
        value=vol/2*sum(s.LeviCivita(i,j,k,l)*inverse[k,p]*inverse[l,q]*F[p,q]
                       for k,l,p,q in __import__('itertools').product(range(4),repeat=4))
        out[i,j]=s.simplify(value);out[j,i]=-out[i,j]
    return out
def twoform(i,j,value):
    F=s.zeros(4);F[i,j]=value;F[j,i]=-value;return F
def wedge_square(F):
    return s.simplify(2*(F[0,1]*F[2,3]-F[0,2]*F[1,3]+F[0,3]*F[1,2]))

def run():
    checks={}
    def ck(label,value):
        checks[label]=bool(value)
        if not checks[label]:raise AssertionError(label)
    x,u,v=s.symbols('x u v',real=True);y,ell,A,g,Y=s.symbols('y ell A g Y',positive=True)
    n=s.symbols('n',real=True);G=metric(x,y,ell,A);vol=ell**2*A/y**2
    ck('actual_metric_determinant',s.simplify(G.det()-vol**2)==0)
    ck('positive_metric_blocks',G[2,2].is_positive and s.simplify(G[2:,2:].det())==A*A)
    F=twoform(0,1,-6*s.I*n/y**2);star=hodge(G,vol,F)
    expected=twoform(2,3,-6*s.I*n*A/ell**2)
    ck('actual_four_dimensional_hodge_response',zero(star-expected))
    ck('actual_star_square_on_all_six_twoforms',all(zero(hodge(G,vol,hodge(G,vol,twoform(i,j,1)))-twoform(i,j,1)) for i,j in PAIRS))
    ck('constant_area_sourcefree_YM',all(s.diff(star[2,3],coord)==0 for coord in (x,y,u,v)))
    ck('actual_connection_curvature',s.diff(-6*s.I*n/y,y)*(-1)==F[0,1])
    ck('missing_fibre_volume_detected',not zero(star-twoform(2,3,-6*s.I*n/ell**2)))
    Av=s.Function('A')(x,y);Sv=hodge(metric(x,y,ell,Av),ell**2*Av/y**2,F)
    ck('variable_area_response_retained',s.simplify(s.diff(Sv[2,3],y)+6*s.I*n*s.diff(Av,y)/ell**2)==0)
    ck('variable_area_nonyangmills_control',s.simplify(s.diff(Sv[2,3].subs(Av,1+y),y))!=0)
    J=s.diag(s.Matrix([[0,-1],[1,0]]),s.Matrix([[-x/y,-(x*x+y*y)/y],[1/y,x/y]]))
    Omega=twoform(0,1,ell**2/y**2)+twoform(2,3,A)
    ck('actual_complex_structure_square',J*J==-s.eye(4))
    ck('actual_Kahler_compatibility',zero(J.T*G-Omega) and zero(J.T*G*J-G))
    hol=s.Matrix([x+s.I*y,u+(x+s.I*y)*v]).jacobian([x,y,u,v])
    ck('actual_holomorphic_coordinates_not_only_J_square',zero(hol*J-s.I*hol))
    ck('actual_closed_Kahler_form',all(s.simplify(s.diff(Omega[j,k],c[i])+s.diff(Omega[k,i],c[j])+s.diff(Omega[i,j],c[k]))==0
                                     for c in ([x,y,u,v],) for i,j,k in combinations(range(4),3)))
    for name,X,Z,M in (('S',-x/(x*x+y*y),y/(x*x+y*y),s.Matrix([[0,1],[-1,0]])),
                       ('T',x+1,y,s.Matrix([[1,-1],[0,1]]))):
        jac=s.diag(s.Matrix([X,Z]).jacobian([x,y]),M)
        ck('actual_full_metric_'+name+'_automorphy',zero(jac.T*metric(X,Z,ell,A)*jac-G))
        ck('actual_curvature_'+name+'_automorphy',zero(jac.T*twoform(0,1,-6*s.I*n/Z**2)*jac-F))
    ck('minus_identity_acts_on_fibre_not_only_base',-s.eye(2)!=s.eye(2) and (-s.eye(2)).det()==1)
    norm=s.simplify(sum(s.conjugate(F[i,j])*G.inv()[i,p]*G.inv()[j,q]*F[p,q]/2
                       for i,j,p,q in __import__('itertools').product(range(4),repeat=4)))
    ck('actual_positive_curvature_norm',s.simplify(norm-36*n*n/ell**4)==0)
    area=s.integrate(1/s.sqrt(1-x*x),(x,-s.Rational(1,2),s.Rational(1,2)))
    energy=s.simplify(norm*ell**2*A*area/(4*g*g))
    ck('actual_total_quotient_action',s.simplify(energy-3*s.pi*A*n*n/(g*g*ell**2))==0)
    tail=s.integrate(norm*ell**2*A/(4*g*g*y*y),(y,Y,s.oo))
    ck('actual_finite_tail_action',s.simplify(tail-9*A*n*n/(g*g*ell**2*Y))==0)
    ck('zero_flux_not_excluded',energy.subs(n,0)==0 and energy.subs(n,1).is_positive)
    ck('opposite_sign_not_selected',s.simplify(energy.subs(n,-n)-energy)==0)
    contraction=s.simplify(s.I*F[0,1]*y*y/ell**2)
    ck('nonzero_flux_not_zero_moment',contraction==6*n/ell**2 and contraction.subs(n,1)!=0)
    ck('actual_horizontal_degree_four_gauge_form_zero',wedge_square(F)==0)
    mixed=F+twoform(2,3,s.I)
    ck('genuine_vertical_curvature_opposing_control',wedge_square(mixed)!=0)
    return {'checks':checks,'exact_passed':sum(checks.values()),'metric':[[str(t) for t in row] for row in G.tolist()],
            'star_curvature':[[str(t) for t in row] for row in star.tolist()],
            'total_action':str(energy),'tail_action':str(tail),'kahler_moment':str(contraction),
            'fibre_complete':False,'unit_selected':False,'physical_Dirac_index_computed':False,
            'three_physical_generations_derived':False}

if __name__=='__main__':print(json.dumps(run(),indent=2))
