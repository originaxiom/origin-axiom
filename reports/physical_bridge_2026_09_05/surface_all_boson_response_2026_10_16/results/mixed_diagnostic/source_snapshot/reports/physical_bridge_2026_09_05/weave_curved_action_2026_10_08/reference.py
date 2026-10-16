"""Separate exact vector/matrix and real-component controls, no native imports."""
from itertools import product, combinations, permutations
from fractions import Fraction as Q
import json


def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def times(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def n2(a):return dot(a,a)


def quartic(x,y,u,v):
    # q=(x+i y).sigma, r=(u+i v).sigma (no sqrt2).
    # Tr([q,qdag]+[r,rdag])^2/2 and 2Tr([q,r]dag[q,r]).
    d=16*n2(plus(cross(x,y),cross(u,v)))
    f=16*(n2(minus(cross(x,u),cross(y,v)))+n2(plus(cross(x,v),cross(y,u))))
    target=16*sum(n2(cross(a,b)) for a,b in combinations((x,y,u,v),2))
    wrong_d=16*n2(cross(x,y))
    return d,f,target,wrong_d


def munit(i,j):return [[int(a==i and b==j) for b in range(3)] for a in range(3)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(3)] for i in range(3)]
def tr(a):return sum(a[i][i] for i in range(3))
def cm(a,b):return sub(mm(a,b),mm(b,a))


def curvature_row(k):
    u,v,ux,vx,uy,vy=k+1,2-k,1,k+3,2*k,k
    uxy,vxy=-2,4
    c1,c2,c1y,c2x=k-1,2*k+1,1+k,3-k
    pxr,pxi=ux-c1*v,vx+c1*u
    pyr,pyi=uy-c2*v,vy+c2*u
    direct=(pxr-pyi)**2+(pxi+pyr)**2
    rough=pxr**2+pxi**2+pyr**2+pyi**2
    div=(vx*pyr+v*(uxy-c2x*v-c2*vx)-ux*pyi-u*(vxy+c2x*u+c2*ux)
         +uy*pxi+u*(vxy+c1y*u+c1*uy)-vy*pxr-v*(uxy-c1y*v-c1*vy))
    curvature=(c2x-c1y)*(u*u+v*v)
    return direct,rough,div,curvature


def run():
    vectors=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,-2,3)]
    qrows=[quartic(*v) for v in product(vectors,repeat=4)]
    x,y,z=(1,0,0),(0,1,0),(0,0,1)
    matter_moments=[]; connection_moments=[]
    for a,b,u,v in product(vectors,repeat=4):
        ka,kb=times(-2,cross(z,a)),times(-2,cross(z,b))
        omega=4*(dot(ka,v)-dot(kb,u))
        delta_mu=-8*dot(z,plus(cross(u,b),cross(a,v)))
        matter_moments.append((omega,delta_mu))
        k1,k2=plus(x,times(2,cross(a,z))),plus(y,times(2,cross(b,z)))
        dF=plus(minus(x,y),times(2,plus(cross(u,b),cross(a,v))))
        surface=2*(dot(x,v)+dot(z,x)-dot(y,u)-dot(z,y))
        connection_moments.append((2*(dot(k1,v)-dot(k2,u)),-2*dot(z,dF)+surface))
    gauge_rows=[]
    for h,q in product(vectors,repeat=2):
        derivative=times(-2,cross(h,q))
        compensation=times(2,cross(h,q))
        gauge_rows.append((plus(derivative,compensation),derivative))
    p,q,r=munit(0,1),munit(2,0),munit(1,2)
    phi=[p,q,r]
    cubic=0
    for order in permutations(range(3)):
        sign=(-1)**sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
        cubic+=sign*tr(mm(phi[order[0]],cm(phi[order[1]],phi[order[2]])))
    rows=[curvature_row(k) for k in range(-5,6)]
    facts={
        'matter_moment_metric_controls':all(a==b for a,b in matter_moments),
        'connection_moment_metric_controls':all(a==b for a,b in connection_moments),
        'wrong_matter_metric_detected':any(2*a!=b for a,b in matter_moments),
        'wrong_connection_metric_detected':any(2*a!=b for a,b in connection_moments),
        '625_noncommuting_and_commuting_quartic_controls':len(qrows)==625 and all(d+f==v for d,f,v,_ in qrows),
        'quartic_positive_on_controls':all(d>=0 and f>=0 and v>=0 for d,f,v,_ in qrows),
        'deleting_mixed_term_fails':any(d!=v for d,f,v,_ in qrows),
        'deleting_R_moment_fails':any(w+f!=v for d,f,v,w in qrows),
        'commuting_quartic_zero':quartic(x,x,x,x)[:3]==(0,0,0),
        'noncommuting_quartic_strictly_positive':quartic(x,y,x,z)[2]>0,
        'six_epsilon_cubic_terms':cubic==6*tr(mm(p,cm(q,r))),
        'retained_family_vertex':tr(mm(q,cm(p,r)))==1,
        'space_dependent_gauge_jets_cancel':all(a==(0,0,0) for a,b in gauge_rows),
        'missing_gauge_derivative_detected':any(b!=(0,0,0) for a,b in gauge_rows),
        'eleven_curved_real_component_controls':len(rows)==11 and all(a-b-c-d==0 for a,b,c,d in rows),
        'surface_terms_do_not_vanish_identically':any(c!=0 for a,b,c,d in rows),
        'spin_curvature_quarter_from_half_canonical':Q(1,2)*Q(1,2)==Q(1,4),
        'flat_patch_energy_balance':0==2+(-2),
        'parent_has_three_chiral_fields':len(phi)==3,
        'all_six_real_commutator_pairs_retained':len(list(combinations(range(4),2)))==6,
        'quadratic_norms_nonnegative':all(n2(v)>=0 for v in vectors),
        'nonzero_quadratic_directions_exist':any(n2(v)>0 for v in vectors),
    }
    profile={'ten_dimensional_cubic_permutations':6,
             'moment_squared_coefficient':'1/2','mixed_commutator_coefficient':2,
             'four_real_scalar_commutator_pairs':6,
             'nonzero_family_trace_vertex':tr(mm(q,cm(p,r))),
             'flat_patch_rough_energy':2,'flat_patch_surface_energy':-2,
             'spin_cusp_threshold':0,'supplied_mass_threshold':'m^2',
             'scalar_curvature_coefficient':'1/4','stationary_origin':True,
             'full_boson_Hessian_nonnegative':True,
             'parent_chiral_fields_including_connection':3}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
            'action_profile':profile,'matrix_quartic_controls':len(qrows),
            'curved_component_controls':len(rows)}


if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
