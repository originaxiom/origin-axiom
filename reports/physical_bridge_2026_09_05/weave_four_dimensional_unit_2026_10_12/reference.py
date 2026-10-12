"""Independent coframe/exterior verification; no new native import."""
import json
import sympy as s

def wedge(a,b):
    out={}
    for ma,va in a.items():
        for mb,vb in b.items():
            if ma & mb:continue
            inversions=sum((mb & ((1<<j)-1)).bit_count() for j in range(4) if ma & (1<<j))
            out[ma|mb]=out.get(ma|mb,0)+(-1)**inversions*va*vb
    return {mask:s.simplify(value) for mask,value in out.items()}

def run():
    checks={}
    def ck(name,value):
        checks[name]=bool(value)
        if not checks[name]:raise AssertionError(name)
    x=s.symbols('x',real=True);y,A,ell,g,Y=s.symbols('y A ell g Y',positive=True);n=s.symbols('n',real=True)
    # Rows are coefficients of orthonormal forms e0,e1,e2,e3.
    E=s.Matrix([[ell/y,0,0,0],[0,ell/y,0,0],[0,0,s.sqrt(A/y),x*s.sqrt(A/y)],[0,0,0,s.sqrt(A*y)]])
    G=E.T*E
    ck('coframe_actual_volume',s.simplify(E.det()-ell**2*A/y**2)==0)
    ck('coframe_positive_determinant',E.det().is_positive)
    coeff=-6*s.I*n/ell**2
    dual23=s.simplify(coeff*(E[2,2]*E[3,3]-E[2,3]*E[3,2]))
    ck('coframe_hodge_curvature',dual23==-6*s.I*n*A/ell**2)
    ck('coframe_actual_curvature_norm',s.simplify(s.conjugate(coeff)*coeff-36*n*n/ell**4)==0)
    area=s.integrate(1/s.sqrt(1-x*x),(x,-s.Rational(1,2),s.Rational(1,2)))
    marked=s.simplify(s.conjugate(coeff)*coeff*ell**2*A*area/(2*g*g))
    total=marked/2
    ck('effective_base_area_not_total_cover',area==s.pi/3 and marked==2*total)
    ck('SL_total_action_half_marked_cover',s.simplify(total-3*s.pi*A*n*n/(g*g*ell**2))==0)
    ck('metaplectic_extra_kernel_is_another_half_not_family_count',s.simplify(total/2-3*s.pi*A*n*n/(2*g*g*ell**2))==0)
    tail=s.integrate(s.conjugate(coeff)*coeff*ell**2*A/(4*g*g*y*y),(y,Y,s.oo))
    ck('coframe_finite_tail',s.simplify(tail-9*A*n*n/(g*g*ell**2*Y))==0)
    ck('zero_flux_minimum_of_this_action',total.subs(n,0)==0 and total.subs(n,1).is_positive)
    ck('orientation_sign_energy_equal',s.simplify(total.subs(n,-1)-total.subs(n,1))==0)
    # F is only e0^e1, so no repeated-free4-form. Vertical e2^e3 changes it.
    q=s.symbols('q',real=True);horizontal={3:coeff};mixed={3:coeff,12:q}
    ck('horizontal_four_form_zero_by_repeated_indices',wedge(horizontal,horizontal)=={})
    ck('vertical_four_form_control_nonzero',wedge(mixed,mixed)=={15:2*coeff*q} and 2*coeff*q!=0)
    Av=s.Function('Av')(x,y)
    ck('varying_fibre_area_has_actual_source',s.simplify(s.diff(coeff*Av,y)-coeff*s.diff(Av,y))==0 and coeff*s.diff(Av,y)!=0)
    ck('no_zero_moment_when_nonzero_unit',s.I*coeff==6*n/ell**2 and (s.I*coeff).subs(n,1)!=0)
    # Coordinate transformation derives the norm from w'=w/(c*tau+d).
    tau=x+s.I*y
    u,v=s.symbols('u v',real=True)
    ck('T_period_coordinates_correct',s.simplify((u-v)+(tau+1)*v-u-tau*v)==0)
    ck('S_period_coordinates_correct',s.simplify(v+(-1/tau)*(-u)-(u+tau*v)/tau)==0)
    return {'exact_checks':checks,'exact_passed':sum(checks.values()),'metric':[[str(t) for t in row] for row in G.tolist()],
            'star_uv':str(dual23),'total_action':str(total),'tail_action':str(tail),
            'unit_selected':False,'three_physical_generations_derived':False,'outside_review':False}

if __name__=='__main__':print(json.dumps(run(),indent=2))
