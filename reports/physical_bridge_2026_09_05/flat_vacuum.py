"""R76 fixed algebra controls for an authored analytic argument, not physics."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s


def norm2(a):
    return s.expand(s.re(s.trace(a.H*a)))


def clean(a):
    return a.applyfunc(s.cancel) if isinstance(a,s.MatrixBase) else s.cancel(a)


@lru_cache(None)
def metric_controls():
    x,y=s.symbols('x y',real=True)
    u=x*x+y
    h=s.Matrix([[1,u],[u,1+u*u]])
    hi=h.inv(); ts=[clean(hi*h.diff(z)) for z in (x,y)]
    a=[v/2 for v in ts]; psi=[-v/2 for v in ts]
    comm=lambda b,c:b*c-c*b
    fa=clean(a[1].diff(x)-a[0].diff(y)+comm(a[0],a[1]))
    dp=clean(psi[1].diff(x)-psi[0].diff(y)
             +comm(a[0],psi[1])-comm(a[1],psi[0]))
    mu=clean(-sum((psi[i].diff(z)+comm(a[i],psi[i])
                   for i,z in enumerate((x,y))),s.zeros(2)))
    tau=clean(h.diff(x,2)+h.diff(y,2)
              -h.diff(x)*hi*h.diff(x)-h.diff(y)*hi*h.diff(y))
    endtau=clean(hi*tau)
    energy=clean(sum(s.trace(v*v) for v in ts)/2)
    pnorm=clean(sum(s.trace(v*v) for v in psi))
    bienergy=clean(s.trace(endtau*endtau)/2)
    munorm=clean(s.trace(mu*mu))
    wrong=clean(hi*(h.diff(x,2)+h.diff(y,2)))
    checks={'positive_shear':h.det()==1 and h[0,0]==1,
            'nonconstant_metric':h.diff(x)!=s.zeros(2),
            'unitary_connection':all(clean(v.H*h+h*v-h.diff(z))==s.zeros(2)
                                     for v,z in zip(a,(x,y))),
            'hermitian_higgs':all(clean(v.H*h-h*v)==s.zeros(2) for v in psi),
            'flat_split_curvature':clean(fa+comm(psi[0],psi[1]))==s.zeros(2),
            'flat_split_derivative':dp==s.zeros(2),
            'moment_tension':clean(2*mu-endtau)==s.zeros(2),
            'energy_factor':clean(energy-2*pnorm)==0,
            'bienergy_factor':clean(bienergy-2*munorm)==0,
            'wrong_tension_rejected':wrong!=endtau,
            'nonzero_tension_control':endtau!=s.zeros(2)}
    return {'checks':checks,'energy':str(energy),'bienergy':str(bienergy)}


@lru_cache(None)
def curvature_controls():
    # General Hermitian 2x2, trace-free: already a noncommuting target sector.
    a,b,c,d,e,f=s.symbols('a b c d e f',real=True)
    u=s.Matrix([[a,b+s.I*c],[b-s.I*c,-a]])
    v=s.Matrix([[d,e+s.I*f],[e-s.I*f,-d]])
    k=u*v-v*u; r=-(k*v-v*k)/4
    pairing=s.expand(s.re(s.trace(r*u)))
    target=-norm2(k)/4
    x=s.symbols('x',real=True); z=x*x
    tension=s.diff(z,x,2); bitension=s.diff(z,x,4)
    alpha=s.diff(z,x)*tension
    # Formal boundary variation for arbitrary endpoint variation data.
    dv,ddv=s.symbols('dv ddv')
    boundary=tension*ddv-s.diff(z,x,3)*dv
    return {'checks':{
        'npc_contraction':s.expand(pairing-target)==0,
        'wrong_sign_rejected':s.expand(pairing+target)!=0,
        'commuting_curvature_zero':pairing.subs({b:0,c:0,e:0,f:0})==0,
        'nonharmonic_interval':tension==2 and bitension==0,
        'interval_current_retained':s.diff(alpha,x)==tension*tension,
        'interval_flux_nonzero':alpha.subs(x,1)-alpha.subs(x,0)==4,
        'fixed_end_variations_zero':boundary.subs(ddv,0)==0,
        'free_end_variation_nonzero':boundary.subs(ddv,1)==2},
        'curvature_pairing':str(s.factor(pairing)),
        'interval_boundary':str(boundary)}


@lru_cache(None)
def peripheral_controls():
    # Explicit reuse of our own frozen R75 exact-field/word primitives.
    p=Path(__file__).with_name('cross_branch_positives.py')
    spec=importlib.util.spec_from_file_location('r76_own_r75',p)
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    k=c.MonogenicFiniteExtension(s.Poly(c.Q**6-34*c.Q**3+1,c.Q,domain=s.QQ))
    m,n=c.literal(); vx=c.dm(n*m.inv(),k);vy=c.dm(-m*n*m.inv()**2,k)
    vz=c.dm(-m**3,k);v={'x':vx,'y':vy,'z':vz}
    cv=c.kernel(c.dm(c.cycle((0,1)),k)+c.eye(8,k)).extract(list(range(8)),[0])
    cs=cv.vstack(c.zero(4,1,k))
    def lift(mat,col):
        return mat.hstack(col).vstack(c.zero(1,4,k).hstack(c.eye(1,k)))
    w={g:lift(mat,cs.extract(list(range(i*4,i*4+4)),[0]))
       for i,(g,mat) in enumerate(v.items())}
    vl,j=c.field_word('yXYx',v);cell=j*cs
    wl,_=c.field_word('yXYx',w)
    u=c.inv(vl-c.eye(4,k))*cell
    b=lift(c.eye(4,k),-u);bi=c.inv(b)
    splitell=lift(vl,c.zero(4,1,k));splitz=lift(vz,c.zero(4,1,k))
    stacked=(vx-c.eye(4,k)).vstack(vy-c.eye(4,k),vz-c.eye(4,k))
    checks={'actual_longitude_cocycle':c.same(wl,lift(vl,cell)),
            'actual_peripheral_commutes':c.same(wl*w['z'],w['z']*wl),
            'longitude_primitive':c.same((vl-c.eye(4,k))*u,cell),
            'stable_primitive':c.same((vz-c.eye(4,k))*u,c.zero(4,1,k)),
            'longitude_splits':c.same(bi*wl*b,splitell),
            'stable_splits':c.same(bi*w['z']*b,splitz),
            'globally_nonsplit':c.rank(stacked.hstack(cs))>c.rank(stacked),
            'nonzero_class':c.rank(stacked)==4 and c.rank(stacked.hstack(cs))==5,
            'q_one_inverse_fails':(c.sym_word('nMNmmNMn',{'m':m,'n':n})
                                  .subs(c.Q,1)-s.eye(4)).det()==0}
    return {'checks':checks,'peripheral_primitive':[str(z) for row in u.to_list() for z in row]}


@lru_cache(None)
def scaling_controls():
    t,r=s.symbols('t r',positive=True)
    br=s.symbols('b0:4',real=True);bi=s.symbols('c0:4',real=True)
    lr=s.symbols('l0:4',real=True);li=s.symbols('j0:4',real=True)
    beta=s.Matrix([x+s.I*y for x,y in zip(br,bi)])
    lv=s.Matrix([x+s.I*y for x,y in zip(lr,li)])
    off=s.zeros(5);off[:4,4]=beta
    af=(off-off.H)/2;pf=(off+off.H)/2
    block=beta*beta.H;n=s.expand((beta.H*beta)[0])
    q=s.diag(0,0,0,0,0);q[:4,:4]=-block/2;q[4,4]=n/2
    l=s.zeros(5);l[:4,4]=lv;l[4,:4]=lv.H
    mu=t*l+t*t*q;xi=s.diag(1,1,1,1,-4)
    aa=norm2(l);cc=norm2(q);potential=norm2(mu)
    g=s.diag(r,r,r,r,r**-4)
    # Direct independent commutator, rather than assigning Q by name.
    inferred=clean(-(af*pf-pf*af))
    dist=sum(z*z for z in [-2,-2,-2,-2,8])*s.log(r)**2
    # A rank-two multi-form positive comparator.
    fixture=s.diag(2,3,0,0)
    fixture_c=s.trace(fixture*fixture)/4+s.trace(fixture)**2/4
    substitutions=dict.fromkeys(br+bi,0)
    return {'checks':{
        'actual_quadratic_moment':clean(inferred-q)==s.zeros(5),
        'traceless_moment':s.expand(s.trace(mu))==0,
        'hermitian_moment':clean(mu.H-mu)==s.zeros(5),
        'orthogonal_linear_quadratic':s.expand(s.trace(l*q))==0,
        'potential_even_polynomial':s.expand(potential-aa*t*t-cc*t**4)==0,
        'positive_rank_one_coefficient':s.expand(cc-n*n/2)==0,
        'positive_multiform_control':fixture_c==s.Rational(19,2),
        'source_projector':s.expand(s.trace(xi*(-2*mu))-5*t*t*n)==0,
        'higgs_energy_increment':s.expand(norm2(pf)-n/2)==0,
        'same_extension_conjugacy':clean(g*off*g.inv()-r**5*off)==s.zeros(5),
        'determinant_one_gauge':g.det()==1,
        'noncompact_gauge':g.T*g!=s.eye(5),
        'split_zero_comparator':cc.subs(substitutions)==0,
        'strict_scaling_derivative':s.expand(s.diff(potential,t)-2*t*aa-4*t**3*cc)==0,
        'target_distance_factor':dist==80*s.log(r)**2,
        'wrong_cubic_detected':s.expand(potential-aa*t*t-cc*t**4+t**3)!=0},
        'quartic_coefficient':str(s.factor(cc)),
        'scaling_potential':'a*t^2+c*t^4, c>0 for nonzero beta',
        'target_distance':str(dist)}


def run():
    groups=[]
    for name,fn in [('metric',metric_controls),('curvature',curvature_controls),
                    ('peripheral',peripheral_controls),('scaling',scaling_controls)]:
        out=fn();groups.append(out)
        print(json.dumps({'group':name,**out},sort_keys=True),flush=True)
    checks=[v for group in groups for v in group['checks'].values()]
    summary={'passed':sum(checks),'total':len(checks),'all_checks_pass':all(checks)}
    print(json.dumps(summary,sort_keys=True),flush=True)
    return summary


if __name__=='__main__':
    raise SystemExit(0 if run()['all_checks_pass'] else 1)
