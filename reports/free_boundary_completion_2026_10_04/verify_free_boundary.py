"""Finite exact controls for the separately authored analytic argument."""
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parent
SILVER = ROOT.parent/'silver_boundary_admission_2026_10_04'/'NATIVE_SECOND.jsonl'
SILVER_SHA = 'dafc582013645226f5edb22325bb800ce0cd8f1a84e7305775bba229880b058b'
x,y,z,e = s.symbols('x y z epsilon', real=True)
XYZ = (x,y,z)
SIGMA = [s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]


def clean(m):
    return m.applyfunc(s.expand)


def comm(a,b):
    return a*b-b*a


def d0(a,v):
    return [v.diff(t)+comm(ai,v) for t,ai in zip(XYZ,a)]


def adjoint(a,one):
    return -sum((vi.diff(t)+comm(ai,vi) for t,ai,vi in zip(XYZ,a,one)),s.zeros(2))


def curvature(c):
    return [c[j].diff(XYZ[i])-c[i].diff(XYZ[j])+comm(c[i],c[j])
            for i in range(3) for j in range(i+1,3)]


def norm(m):
    return s.expand(s.trace(m.conjugate().T*m))


def covariance():
    a = [s.I*y*SIGMA[1],s.I*z*SIGMA[2],s.I*x*SIGMA[0]]
    psi = [(1+x)*SIGMA[0],y*SIGMA[1],z*SIGMA[2]]
    u = x*SIGMA[2]+(y+z)*SIGMA[0]
    du = d0(a,u)
    da = [comm(p,u) for p in psi]
    c = [ai+pi for ai,pi in zip(a,psi)]
    dc = [ai+pi for ai,pi in zip(da,du)]
    checks = {}
    checks['Hermitian_and_compact_types'] = (
        all(clean(ai+ai.conjugate().T)==s.zeros(2) for ai in a+da)
        and all(clean(pi-pi.conjugate().T)==s.zeros(2) for pi in psi+du)
        and clean(u-u.conjugate().T)==s.zeros(2))
    raw_moment = adjoint([ai+e*dai for ai,dai in zip(a,da)],
                         [pi+e*dpi for pi,dpi in zip(psi,du)])
    derivative = clean(raw_moment.diff(e).subs(e,0))
    lap = adjoint(a,du)
    potential = sum((comm(p,comm(p,u)) for p in psi),s.zeros(2))
    ell = clean(lap+potential)
    checks['full_moment_derivative'] = derivative == ell
    checks['omitted_commutator_rejected'] = clean(derivative-lap) != s.zeros(2)
    checks['wrong_commutator_sign_rejected'] = clean(derivative-(lap-potential)) != s.zeros(2)
    df = [clean(m.diff(e).subs(e,0)) for m in curvature([ci+e*di for ci,di in zip(c,dc)])]
    checks['full_curvature_derivative'] = all(
        clean(di-comm(fi,u))==s.zeros(2) for di,fi in zip(df,curvature(c)))
    checks['positive_adjoint_potential'] = s.expand(s.trace(u*potential)-sum(norm(v) for v in da)) == 0
    # Unitary directions differentiate both the connection and the Higgs field too.
    xi = s.I*u
    gauged_a = [ai+e*di for ai,di in zip(a,d0(a,xi))]
    gauged_psi = [pi+e*comm(pi,xi) for pi in psi]
    dmu_gauge = adjoint(gauged_a,gauged_psi).diff(e).subs(e,0)
    checks['compact_gauge_covariance'] = clean(dmu_gauge-comm(adjoint(a,psi),xi))==s.zeros(2)
    # Pointwise Green identity, then integrate independently on the unit cube.
    energy = s.expand(sum(norm(v) for v in du+da))
    lhs = s.expand(s.trace(u*ell))
    flux = [s.expand(s.trace(u*v)) for v in du]
    divergence = sum(v.diff(t) for v,t in zip(flux,XYZ))
    checks['pointwise_Green_identity'] = s.expand(lhs-energy+divergence)==0
    integrated = s.integrate(lhs-energy,(x,0,1),(y,0,1),(z,0,1))
    boundary = 0
    for t,v in zip(XYZ,flux):
        face = v.subs(t,1)-v.subs(t,0)
        for other in XYZ:
            if other != t:
                face = s.integrate(face,(other,0,1))
        boundary += face
    checks['integrated_Green_identity'] = s.simplify(integrated+boundary)==0
    checks['wrong_outward_sign_rejected'] = boundary != 0 and s.simplify(integrated-boundary)!=0
    assert all(checks.values()),checks
    return {'checks':checks,'cube_outward_flux':str(boundary),
            'cube_bulk_difference':str(integrated)}


def fourier():
    r,length = s.symbols('r L',positive=True)
    k = s.symbols('k',positive=True,integer=True)
    beta = s.symbols('beta',positive=True)
    h = s.sinh(k*r)/s.sinh(k*length)
    f = h*s.cos(k*x)
    lap = f.diff(r,2)+f.diff(x,2)
    density = h.diff(r)**2+k**2*h**2  # trace(T^2)=2 and cos/sin averages=1/2
    primitive = h*h.diff(r)
    kinetic = s.simplify(primitive.subs(r,length)-primitive.subs(r,0))
    checks = {
        'harmonic_all_positive_integer_k':s.simplify(lap)==0,
        'correct_end_data':s.simplify(h.subs(r,0))==0 and s.simplify(h.subs(r,length)-1)==0,
        'kinetic_primitive':s.simplify(primitive.diff(r)-density)==0,
        'kinetic_formula':s.simplify(kinetic-k/s.tanh(k*length))==0,
        'nonzero_Hermitian_Higgs':f.diff(x)!=0,
        'compact_gauge_at_zero_has_no_Higgs_variation':comm(s.zeros(2),s.I*SIGMA[0])==s.zeros(2),
    }
    # Curvature of T df vanishes exactly, including the nonlinear commutator.
    c = [e*SIGMA[2]*f.diff(t) for t in (r,x)]
    checks['nonlinear_Cartan_flatness'] = clean(c[1].diff(r)-c[0].diff(x)+comm(c[0],c[1]))==s.zeros(2)
    bad = r**2*s.cos(k*x)
    checks['nonharmonic_control_rejected'] = s.simplify(bad.diff(r,2)+bad.diff(x,2))!=0
    for i in range(1,5):
        hi = h.subs(k,i)
        checks[f'exact_mode_{i}'] = s.simplify(hi.diff(r,2)-i*i*hi)==0
    for i,j in ((1,2),(2,3),(1,4)):
        checks[f'orthogonal_modes_{i}_{j}'] = (
            s.integrate(s.cos(i*x)*s.cos(j*x),(x,0,2*s.pi))==0
            and s.integrate(s.sin(i*x)*s.sin(j*x),(x,0,2*s.pi))==0)
    # Boundary penalty on the mode, normalized torus area and both ends retained.
    penalty = s.simplify(beta*e**2*k**2*(h.subs(r,0)**2+h.subs(r,length)**2)/2)
    checks['boundary_penalty'] = penalty == beta*e**2*k**2/2
    checks['normal_constant_mode_survives'] = (r/length).diff(x)==0
    zero_norm = s.integrate(2*(s.diff(r/length,r))**2,(r,0,length))
    checks['normal_constant_norm'] = s.simplify(zero_norm-2/length)==0
    q = s.symbols('q')
    relative_cells = s.Poly(q*(1+2*q+q*q),q)
    checks['relative_comparator_H1_one'] = relative_cells.coeff_monomial(q)==1
    # Nonzero periodic modes on a closed flat torus are not harmonic.
    checks['closed_periodic_control'] = s.diff(s.cos(k*x),x,2)==-k*k*s.cos(k*x)
    # Gauge invariance of tr(Psi_t^dagger Psi_t) on a nontrivial exact unitary rotation.
    rotation = s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],
                         [s.Rational(4,5),s.Rational(3,5)]])
    checks['penalty_compact_gauge_invariance'] = norm(rotation.T*SIGMA[2]*rotation)==norm(SIGMA[2])
    assert all(checks.values()),checks
    return {'checks':checks,'kinetic':str(kinetic),'added_penalty':str(penalty),
            'normal_constant_kinetic':str(zero_norm),
            'scope':'Exact comparator and symbolic formulas; no physical mass or silver profile solve'}


def full_degrees():
    raw = SILVER.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SILVER_SHA
    members = [json.loads(line)['member'] for line in raw.splitlines() if b'"member"' in line]
    out = []
    omission_seen = False
    for m in members:
        for coefficient in ('W','wedge2W'):
            pair = m[coefficient]
            for order,other in (('E','dual'),('dual','E')):
                p,d = pair[order],pair[other]
                a = [p['h0_absolute'],p['h1_absolute'],p['h1_absolute']-p['h0_absolute'],0]
                rel = [0,p['h1_relative'],d['h1_absolute'],d['h0_absolute']]
                image = [0,p['h1_interior'],d['h1_interior'],0]
                count = lambda b: b[1]+b[3]-b[0]-b[2]
                assert rel[1]==d['h1_absolute']-d['h0_absolute']
                assert count(a)==count(rel)==0
                assert count(image)==p['h1_interior']-d['h1_interior']
                omission_seen |= a[1]-a[2]!=count(a) or rel[1]-rel[2]!=count(rel)
                out.append({'carrier':m['carrier'],'character':m['character'],
                            'coefficient':coefficient,'order':order,
                            'absolute_degrees':a,'relative_degrees':rel,'interior_image_degrees':image,
                            'odd_minus_even':{'absolute':count(a),'relative':count(rel),'interior_image':count(image)}})
    assert len(out)==16 and omission_seen
    return {'rows':out,'h0_h3_omission_rejected':omission_seen}


def run():
    results = {'nonabelian':covariance(),'fourier':fourier(),'silver_degrees':full_degrees()}
    print(json.dumps({'status':'PASS','results':results},sort_keys=True),flush=True)
    return results


if __name__=='__main__':
    run()
