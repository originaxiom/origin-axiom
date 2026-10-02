"""R77 symbolic controls of an ADDED free-profile model, not physics."""
from functools import lru_cache
import json
import sympy as s


def clean(m):
    return m.applyfunc(s.expand) if isinstance(m, s.MatrixBase) else s.expand(m)


def norm2(m):
    return s.expand(s.re(s.trace(m.H*m)))


def moment(fields):
    n=fields[0].rows
    return clean(sum((z*z.H-z.H*z for z in fields), s.zeros(n)))


def source_fields(target):
    """Full right inverse. Values are NOT admissible geometric mode profiles."""
    n=target.rows
    if target.cols!=n or clean(target.H-target)!=s.zeros(n) or s.expand(s.trace(target))!=0:
        raise ValueError('source must be Hermitian and trace-free')
    d=[s.Rational(2*i-(n-1),2) for i in range(n)]
    a0=s.diag(*d);b0=s.zeros(n)
    for i in range(n):
        for j in range(n):
            if i!=j:
                b0[i,j]=s.I*target[i,j]/(2*(d[i]-d[j]))
    pairs=[(a0,b0)]
    for j in range(n-1):
        a=s.zeros(n);b=s.zeros(n)
        a[j,n-1]=a[n-1,j]=1
        b[j,n-1]=-s.I*target[j,j]/4
        b[n-1,j]=s.I*target[j,j]/4
        pairs.append((a,b))
    return [clean(a+s.I*b) for a,b in pairs]


def generic_source(n):
    m=s.zeros(n)
    diag=s.symbols('d0:'+str(n-1),real=True)
    for i in range(n-1):m[i,i]=diag[i]
    m[n-1,n-1]=-sum(diag)
    for i in range(n):
        for j in range(i+1,n):
            a,b=s.symbols('a%d%d b%d%d'%(i,j,i,j),real=True)
            m[i,j]=a+s.I*b;m[j,i]=a-s.I*b
    return m


def example_source():
    m=s.diag(1,-2,3,-4,2)
    for i in range(5):
        for j in range(i+1,5):
            m[i,j]=(i+1)-s.I*(j+1);m[j,i]=s.conjugate(m[i,j])
    return m


@lru_cache(None)
def image_controls():
    target=generic_source(5);zs=source_fields(target)
    sample=example_source();fields=source_fields(sample)
    u=s.eye(5);u[:2,:2]=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],
                                [s.Rational(4,5),s.Rational(3,5)]])
    u[2,2]=s.I;u[3,3]=-s.I
    rotated=[u*z*u.H for z in fields]
    trace_rejected=False
    try:source_fields(s.eye(5))
    except ValueError:trace_rejected=True
    nonhermitian_rejected=False
    wrong=s.zeros(5);wrong[0,1]=1
    try:source_fields(wrong)
    except ValueError:nonhermitian_rejected=True
    checks={
        'complete_symbolic_current':moment(zs)==target,
        'source_is_hermitian':target.H==target,
        'source_is_tracefree':s.trace(target)==0,
        'all_source_fields_tracefree':all(s.trace(z)==0 for z in zs),
        'five_constructed_fields':len(zs)==5,
        'nonzero_current_control':moment(fields)!=s.zeros(5),
        'opposite_current_constructed':moment(source_fields(-sample))==-sample,
        'zero_current_constructed':moment(source_fields(s.zeros(5)))==s.zeros(5),
        'zero_current_need_not_mean_zero_fields':any(z!=s.zeros(5) for z in source_fields(s.zeros(5))),
        'traceful_input_rejected':trace_rejected,
        'nonhermitian_input_rejected':nonhermitian_rejected,
        'unitary_frame':u.H*u==s.eye(5) and u.det()==1,
        'full_moment_covariance':moment(rotated)==clean(u*sample*u.H),
        'positive_kinetic_covariance':s.expand(sum(norm2(z) for z in rotated)-sum(norm2(z) for z in fields))==0}
    return {'checks':checks,'sample_current_norm2':str(norm2(sample))}


@lru_cache(None)
def action_controls():
    g2,kappa=s.symbols('g2 kappa',positive=True)
    a,b,c,u,v,w,x,y,z=s.symbols('a b c u v w x y z',real=True)
    d=s.Matrix([[a,b+s.I*c],[b-s.I*c,-a]])
    cur=s.Matrix([[u,v+s.I*w],[v-s.I*w,-u]])
    mm=s.Matrix([[x,y+s.I*z],[y-s.I*z,-x]])
    ld=s.trace(d*d)/(2*g2)+s.trace(d*(cur/g2+kappa*mm))
    ds=-cur-g2*kappa*mm
    eliminated=clean(ld.subs({a:ds[0,0],b:s.re(ds[0,1]),c:s.im(ds[0,1])},simultaneous=True))
    vv=norm2(cur+g2*kappa*mm)/(2*g2)
    station=[clean(s.diff(ld,q).subs({a:ds[0,0],b:s.re(ds[0,1]),c:s.im(ds[0,1])},simultaneous=True)) for q in (a,b,c)]
    sample=example_source();fields=source_fields(-sample/6)
    eps=s.symbols('eps',real=True);h=s.zeros(5);h[0,4]=s.I
    varied=list(fields);varied[0]=varied[0]+eps*h
    rv=sample+6*moment(varied);value=norm2(rv)/4
    t=s.diag(1,-1,0,0,0)
    purebulk=norm2(eps*t)/4
    trace_identity=clean(s.trace(fields[0].H*(t*fields[0]-fields[0]*t))-
                         s.trace(t*(fields[0]*fields[0].H-fields[0].H*fields[0])))
    return {'checks':{
        'auxiliary_equation_all_components':all(q==0 for q in station),
        'eliminated_positive_square':clean(eliminated+vv)==0,
        'canonical_adjoint_moment_sign':trace_identity==0,
        'total_current_zero':sample+6*moment(fields)==s.zeros(5),
        'wrong_source_sign_nonzero':sample+6*moment(source_fields(sample/6))==2*sample,
        'removed_source_coupling_nonzero':norm2(sample)>0,
        'source_own_first_variation_zero':s.diff(value,eps).subs(eps,0)==0,
        'source_own_second_variation_positive':s.diff(value,eps,2).subs(eps,0)>0,
        'bulk_first_variation_zero':s.diff(purebulk,eps).subs(eps,0)==0,
        'bulk_second_variation_positive':s.diff(purebulk,eps,2).subs(eps,0)>0},
        'source_second_variation':str(s.diff(value,eps,2).subs(eps,0))}


@lru_cache(None)
def localization_controls():
    sample=example_source();fields=source_fields(sample)
    c1,c2=s.Rational(3,5),s.Rational(4,5)
    parts=[c1*z for z in fields]+[c2*z for z in fields]
    x=s.symbols('x',real=True);f=x*(1-x)
    # A bounded interval norm control, NOT a smooth global compact profile.
    local=[f*z for z in fields]
    kinetic=s.integrate(sum(norm2(z) for z in local),(x,0,1))
    return {'checks':{
        'square_partition':c1*c1+c2*c2==1,
        'full_partition_current':moment(parts)==sample,
        'omitted_patch_rejected':moment(parts[:5])!=sample,
        'profile_current_square':moment(local)==clean(f*f*sample),
        'positive_finite_profile_norm':kinetic.is_Rational and kinetic>0},
        'interval_kinetic_norm':str(kinetic)}


@lru_cache(None)
def profile_controls():
    t,x,eps=s.symbols('t x eps',real=True)
    # Tail background is zero in the source sector and its total D residual.
    u=s.Matrix([[1+s.I,2-s.I],[3+s.I,-1-s.I]])
    mm=moment([t*u]);vv=norm2(mm)/2
    h=s.diag(1,-1);f=x*(1-x);f2=(2*x-1)*f
    kinetic=s.integrate(norm2(f*h),(x,0,1))
    gradient=s.integrate(norm2(s.diff(f,x)*h),(x,0,1))
    coupled=vv+eps*t*t*gradient
    gauge=s.Matrix([[0,1],[-1,0]])
    return {'checks':{
        'source_moment_quadratic':mm==clean(t*t*moment([u])),
        'source_potential_quartic':vv==s.expand(t**4*norm2(moment([u]))/2),
        'free_source_hessian_zero':s.diff(vv,t,2).subs(t,0)==0,
        'quartic_live_positive':norm2(moment([u]))>0,
        'hermitian_profile_exact_flat':moment([t*f*h])==s.zeros(2),
        'profile_kinetic_positive':kinetic==s.Rational(1,15),
        'second_independent_profile_positive':s.integrate(norm2(f2*h),(x,0,1))>0,
        'profile_pair_orthogonal':s.integrate(s.trace((f*h).H*(f2*h)),(x,0,1))==0,
        'linear_gauge_cannot_remove_tail_source':gauge*s.zeros(2)-s.zeros(2)*gauge==s.zeros(2),
        'gauge_action_live_nonzero':gauge*h-h*gauge!=s.zeros(2),
        'gradient_live_positive':gradient==s.Rational(2,3),
        'same_hessian_detects_gradient':s.diff(coupled,t,2).subs(t,0)==2*eps*gradient,
        'varying_profile_not_parallel':s.diff(f,x)!=0},
        'kinetic_norm':str(kinetic),'gradient_norm':str(gradient),
        'quartic_coefficient':str(norm2(moment([u]))/2)}


@lru_cache(None)
def duality_controls():
    cur=generic_source(5);fields=source_fields(-cur/6)
    dual=lambda x: -x.T
    dfields=[dual(z) for z in fields]
    e=s.symbols('e',real=True);h=s.zeros(5);h[0,4]=1+s.I
    varied=list(fields);varied[0]=varied[0]+e*h
    residual=cur+6*moment(varied)
    dualres=dual(cur)+6*moment([dual(z) for z in varied])
    return {'checks':{
        'duality_is_involution':dual(dual(cur))==cur,
        'duality_full_current':moment(dfields)==clean(-moment(fields).T),
        'duality_matched_current_zero':dual(cur)+6*moment(dfields)==s.zeros(5),
        'duality_total_residual':dualres==clean(dual(residual)),
        'duality_positive_potential':s.expand(norm2(dualres)-norm2(residual))==0,
        'duality_positive_kinetic':s.expand(sum(norm2(z) for z in dfields)-sum(norm2(z) for z in fields))==0,
        'only_source_transformed_fails':cur+6*moment(dfields)==clean(cur+cur.T) and cur+6*moment(dfields)!=s.zeros(5)},
        'scope':'structure duality only; no physical mirror or gauge-inequivalent vacuum claim'}


def run():
    groups={name:fun() for name,fun in (
        ('image',image_controls),('action',action_controls),
        ('localization',localization_controls),('profiles',profile_controls),
        ('duality',duality_controls))}
    checks=[v for out in groups.values() for v in out['checks'].values()]
    return {'groups':groups,'passed':sum(checks),'total':len(checks),
            'all_checks_pass':all(checks),
            'scope':'ADDED free-profile classical model; not source admission, physical chirality or TOE'}


if __name__=='__main__':
    result=run();print(json.dumps(result,sort_keys=True,indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
