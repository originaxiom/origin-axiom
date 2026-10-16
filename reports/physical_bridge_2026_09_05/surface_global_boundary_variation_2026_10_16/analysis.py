"""Actual global-tube residual-sector variation; no science on import."""
# BANKED IDENTITY: fresh source/geometry replays. PRIOR ART: DESIGN/PROOF.
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def simp(v):
    return s.factor(s.cancel(v))

def cm(m):
    return s.SparseMatrix(m.applyfunc(simp))

def zero(m):
    return all(simp(v) == 0 for v in m.todok().values())

def enc(m):
    return [[i, j, str(simp(v))] for (i, j), v in sorted(m.todok().items()) if simp(v) != 0]

def antecedent(folder, label):
    child = subprocess.run([sys.executable, '-B', str(HERE.parent/folder/(label+'.py'))],
        cwd=ROOT, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'),
        capture_output=True, text=True, timeout=1200)
    if child.returncode:
        raise RuntimeError(folder+' failed\n'+child.stderr+'\n'+child.stdout)
    obj = json.loads(child.stdout)
    if not obj['all_passed']:
        raise RuntimeError('Antecedent did not pass: '+folder)
    return obj

def run(method):
    checks, records = {}, {}
    def ck(name, value):
        checks[name] = bool(value)
        print(('PASS ' if checks[name] else 'FAIL ')+name, file=sys.stderr, flush=True)
    label = 'probe' if method == 'native' else 'reference'
    for folder, count in [('surface_arena_boundary_2026_10_16', 44),
        ('surface_curved_boson_2026_10_16', 53),
        ('surface_same_action_transmission_2026_10_16', 144)]:
        prior = antecedent(folder, label)
        records[folder] = prior
        ck('fresh complete antecedent '+folder, len(prior['checks']) == count)
    curved = load(HERE.parent/'surface_curved_boson_2026_10_16/analysis.py', 'global_boundary_words')

    # Rational parameter of the complete circle except one point; the
    # polynomial identities extend there by continuity, not sampling.
    x, t = s.symbols('x circle_parameter', real=True)
    y, r, ell = s.symbols('y r ell', positive=True)
    fx, fy = s.symbols('log_sigma_x log_sigma_y', real=True)
    c, sn = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    if method == 'native':
        coords = (x, y, r, t)
        derivative = lambda q, p: s.diff(q, p)*((1+t*t)/2 if p == t else 1)
        v = r*sn/s.sqrt(y)
        u = r*s.sqrt(y)*c-x*v
        C = cm(s.Matrix([[ell/y, 0, 0, 0], [0, ell/y, 0, 0],
            [(derivative(u, p)+x*derivative(v, p))/s.sqrt(y) for p in coords],
            [s.sqrt(y)*derivative(v, p) for p in coords]]))
        inv = cm(C.inv())
    else:
        C = s.Matrix([[ell/y, 0, 0, 0], [0, ell/y, 0, 0],
            [-r*sn/y, r*c/(2*y), c, -r*sn], [0, -r*sn/(2*y), sn, r*c]])
        inv = s.Matrix([[y/ell, 0, 0, 0], [0, y/ell, 0, 0],
            [r*c*sn/ell, r*(sn*sn-c*c)/(2*ell), c, sn],
            [-sn*sn/ell, c*sn/ell, -sn/r, c/r]])
    ck('actual coframe inverse in both orders and oriented volume',
       zero(C*inv-s.eye(4)) and zero(inv*C-s.eye(4)) and simp(C.det()-ell*ell*r/y**2) == 0)
    J = s.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
    df = s.Matrix([-fx, -fy, 1/r, 0])
    N = cm(inv.T*df)
    target = s.Matrix([(c*sn-y*fx)/ell, ((sn*sn-c*c)/2-y*fy)/ell, c/r, sn/r])
    Q = simp(N.dot(N))
    ck('full variable normal retains horizontal geometry and radius gradient', zero(N-target))
    ck('normal norm has nonzero positive vertical contribution',
       simp(Q-1/r**2-target[0]**2-target[1]**2) == 0)
    ck('vertical normal approximation rejected even at fixed radius',
       not zero(N.subs({fx: 0, fy: 0})-s.Matrix([0, 0, c/r, sn/r])))
    graph = s.Matrix([[1, 0, 0], [0, 1, 0], [r*fx, r*fy, 0], [0, 0, 1]])
    beta = cm(graph.T*C.T*J*N)
    ck('actual CR form pulled back with the full normal', zero(beta-s.Matrix([1/(2*y)+fy, -fx, 1])))
    induced = cm(graph.T*C.T*C*graph)
    density_squared = ell**4*r**4*Q/y**4
    ck('induced density agrees with actual graph metric determinant', simp(induced.det()-density_squared) == 0)
    Ncoord = cm(inv*N)
    flux = simp(C.det()*(Ncoord[2]-r*fx*Ncoord[0]-r*fy*Ncoord[1]))
    ck('coarea and oriented flux retain every horizontal term', simp(flux-ell*ell*r*r*Q/y**2) == 0)
    xx = s.Matrix(s.symbols('current0:4', real=True))
    flux_density = simp(ell*ell*r*r*xx.dot(N)/y**2)
    vertical_flux = ell*ell*r*(xx[2]*c+xx[3]*sn)/y**2
    ck('wrong vertical scalar current and same-normal joining are detected',
       simp(flux_density-vertical_flux) != 0 and simp(flux_density+flux_density) != 0)
    records['actual_tube'] = {'normal': enc(N), 'norm_squared': str(Q), 'CR_form': enc(beta),
        'induced_density_squared': str(simp(density_squared)), 'oriented_current_density': str(flux_density)}

    n = s.Matrix(s.symbols('normal0:4', real=True))
    variation = s.Matrix(s.symbols('a0:4')+s.symbols('delta_U delta_V'))
    fields = s.symbols('F01 F02 F03 F12 F13 F23 DU0:4 DV0:4 commUV')
    F01,F02,F03,F12,F13,F23 = fields[:6]
    du,dv,uv = fields[6:10],fields[10:14],fields[14]
    residual = s.Matrix([F01+F23+uv,F02-F13,F03+F12,
        du[0]-dv[1],dv[0]+du[1],du[2]-dv[3],dv[2]+du[3]])
    jets = list(fields[:14])
    pairs = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    derivative_jet = s.Matrix([n[i]*variation[j]-n[j]*variation[i] for i,j in pairs]
        +[ni*variation[4] for ni in n]+[ni*variation[5] for ni in n])
    expected = s.Matrix([[-n[1],n[0],-n[3],n[2],0,0],[-n[2],n[3],n[0],-n[1],0,0],
        [-n[3],-n[2],n[1],n[0],0,0],[0,0,0,0,n[0],-n[1]],
        [0,0,0,0,n[1],n[0]],[0,0,0,0,n[2],-n[3]],[0,0,0,0,n[3],n[2]]])
    L = (residual.jacobian(jets)*derivative_jet).jacobian(variation) if method == 'native' else expected
    ck('normal symbol derived from all actual seven residuals', zero(residual.jacobian(jets)*derivative_jet-L*variation) and zero(L-expected))
    n2 = n.dot(n)
    gram = s.diag(n2*s.eye(4)-n*n.T,n2*s.eye(2))
    ck('all-normal rank-five symbol and only normal-gauge kernel', zero(L.T*L-gram) and zero(L*s.Matrix(list(n)+[0,0])))
    energy = 2*residual.dot(residual)
    direct = sum(s.diff(energy, z)*dz for z,dz in zip(jets,derivative_jet))
    momentum = cm(4*L.T*residual)
    ck('actual nonlinear residual momenta from full first variation', simp(direct-momentum.dot(variation)) == 0)
    ck('wrong source factor and discarded derivative term are detected',
       simp(direct-(momentum/2).dot(variation)) != 0 and not zero(L[:,4:]))
    ck('source momentum is tangential in gauge slots', simp(n.dot(momentum[:4,:])) == 0)
    ck('commutator retained rather than dropped from actual source momentum', not zero(momentum.diff(uv)))
    # An actual jet with F01=F23=1, n=E0, delta A1=1 gives
    # source work8, rough2E work4. The topological primitive supplies4.
    at = dict(zip(n,[1,0,0,0]));at.update({z:0 for z in fields});at.update({F01:1,F23:1})
    rough_gauge = 2*sum(z*z for z in fields[:6])
    rough_variation = sum(s.diff(rough_gauge,z)*dz for z,dz in zip(fields[:6],derivative_jet[:6]))
    aa = dict(zip(variation,[0,1,0,0,0,0]))
    ck('rough Yang Mills momentum is not the source momentum', simp(direct.subs(at).subs(aa)) == 8 and simp(rough_variation.subs(at).subs(aa)) == 4)
    rr = s.Matrix(s.symbols('residual0:7'))
    ck('zero residual gives natural momenta without Dirichlet values', zero((4*L.T*rr).subs(dict.fromkeys(rr,0))) and not zero(L.T*rr))
    records['source_boundary'] = {'seven_residuals':enc(residual),'normal_symbol':enc(L),
        'Theta_positive_potential_momenta':enc(momentum),'Theta_static_source_momenta':enc(-momentum),
        'rank_per_coefficient':5,'kernel':'normal gauge derivative jet only; not particles',
        'raw_component_primitives':'retained fresh transmission record; add delta B for each actual representative, not discarded'}

    # Generic noncommuting coefficient proof, not scalar trace inference.
    alg = curved.a
    ep = alg.letter('gauge_parameter')
    covariance = {}
    for i in range(7):
        R,A = alg.letter('C'+str(i)),alg.letter('variation'+str(i))
        covariance = alg.add(covariance,curved.B(alg.comm(R,ep),A),curved.B(R,alg.comm(A,ep)))
    ck('full nonlinear boundary pairing gauge covariance before interpretation', not alg.trace(covariance))
    forms = curved.Forms
    A,dA,a,da = map(alg.letter,('fA','dA','fa','da'))
    F = alg.add(dA,alg.mul(A,A))
    cs = alg.scale(alg.trace(alg.add(alg.mul(A,dA),alg.scale(alg.mul(alg.mul(A,A),A),s.Rational(2,3)))),-1)
    dcs = alg.add(alg.scale(curved.B(a,F),2),alg.scale(forms.d(curved.B(A,a)),-1))
    ck('actual CS first variation retains the corner derivative', curved.eq(forms.variation(cs),dcs))
    ck('deleting the CS corner term is detected', not curved.eq(forms.variation(cs),alg.scale(curved.B(a,F),2)))
    pure = alg.add(alg.mul(A,alg.scale(alg.mul(A,A),-1)),alg.scale(alg.mul(alg.mul(A,A),A),s.Rational(2,3)))
    purecs = alg.scale(alg.trace(pure),-1)
    ck('flat pure gauge CS cubic is nonzero and has the correct coefficient',
       bool(purecs) and curved.eq(purecs,alg.scale(alg.trace(alg.mul(alg.mul(A,A),A)),s.Rational(1,3))))
    U,V = map(alg.letter,('U','V'))
    DU = [alg.letter('U_'+str(i)) for i in range(4)]
    DV = [alg.letter('V_'+str(i)) for i in range(4)]
    currents=[]
    for i,j in ((0,1),(2,3)):
        currents += [alg.add(curved.B(U,DV[j]),alg.scale(curved.B(V,DU[j]),-1)),
            alg.add(alg.scale(curved.B(U,DV[i]),-1),curved.B(V,DU[i]))]
    normalJ = alg.add(*(alg.scale(q,ni) for q,ni in zip(currents,n)))
    dnormalJ = alg.sf.variation(normalJ)
    ck('full nonlinear scalar end flux and derivative variations retained',
       bool(normalJ) and bool(dnormalJ) and any(':' in token for word in dnormalJ for token in word))
    ck('both endpoint primitive signs are required', not curved.eq(normalJ,alg.scale(normalJ,-1)))
    records['end_primitive'] = {'CS':curved.encoded(cs),'delta_CS':curved.encoded(dcs),
        'pure_gauge_CS':curved.encoded(purecs),'scalar_normal_flux':curved.encoded(normalJ),
        'scalar_flux_variation':curved.encoded(dnormalJ),
        'energy_rewrite':'2CS_B-2i_Jdvol, not added again to V',
        'caps_corners_and_patch_descent_required':True,'quantum_level_derived':False}

    parent = load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py','global_boundary_source_frame')
    vv, ext, cs0, engine, valid, old = parent.setup(method)
    eye=s.eye(16);CC=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8))
    vn=cm(sum((ni*v for ni,v in zip(n,vv[:4])),s.zeros(16)))
    jn=J*n
    vj=cm(sum((ni*v for ni,v in zip(jn,vv[:4])),s.zeros(16)))
    R=-s.I*vv[4]*vv[5]
    Z=cm(s.I*R*vn*vj)
    ck('actual full source Clifford and symmetric Majorana normal pairing',valid and zero(vn*vn-n2*eye) and zero((CC.H*vn).T-CC.H*vn))
    ck('full source real normal map retains both conjugate blocks',zero(CC*vn.conjugate()*CC-vn) and zero(CC*Z.conjugate()*CC-Z))
    ck('both intrinsic half planes are real Green null but unselected',zero(Z*Z-n2*n2*eye) and zero(Z*vn+vn*Z) and s.trace(Z)==0 and zero(Z.H-Z))
    ck('unrestricted fermion pairing nondegenerate not a half-rank condition',zero(vn*vn-n2*eye) and not zero(vn) and zero((n2*eye+Z)*vn*(n2*eye+Z)))
    records['fermion_trace']={'normal_velocity':enc(vn),'Majorana_pairing':enc(CC.H*vn),
        'intrinsic_involution_numerator':enc(Z),'both_signs_retained':True,
        'source_surface_sign':'+i/2, opposite the normal-Hamiltonian convention; both normals',
        'old_pointwise_principal_failure_repaired':False,'full_SUSY_domain_selected':False}
    records['meaning']={'residual_source_boundary_variation_on_actual_global_tube':True,
        'regulator_held_fixed':True,'true_end_state_selected':False,'global_stationary_SM_phase_derived':False,
        'physical_three_parameters_gravity_derived':False,'full_raw_curved_superfield_completion_derived':False}
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}

def emit(method):
    obj=run(method)
    print(json.dumps(obj,indent=2))
    return 0 if obj['all_passed'] else 1
