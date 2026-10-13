#!/usr/bin/env python3
"""Independent, local verification of the first weave quantum-realization tests.

Dependencies: Python >=3.10, sympy, mpmath. No project code or experimental data.
Run: python verify.py --output results.json
Exact tests use rational/algebraic arithmetic. Numerical checks are separately labelled.
"""
from __future__ import annotations
import argparse
from collections import deque
from itertools import product
import json
import math
from pathlib import Path
import platform
import sys
import sympy as sp
import mpmath as mp

I = sp.I
R = sp.Rational
CHECKS: list[dict] = []


def check(name: str, condition: bool, detail=None) -> None:
    ok = bool(condition)
    CHECKS.append({'name': name, 'passed': ok, 'detail': detail})
    if not ok:
        raise AssertionError(name + (': ' + str(detail) if detail is not None else ''))


def simp(x):
    return sp.simplify(sp.expand_complex(x))


def matrix_zero(M) -> bool:
    return all(simp(x) == 0 for x in M)


def serial(x):
    if isinstance(x, sp.MatrixBase):
        return [[str(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x, sp.Basic):
        return str(x)
    if isinstance(x, dict):
        return {str(k): serial(v) for k,v in x.items()}
    if isinstance(x, (list,tuple)):
        return [serial(v) for v in x]
    return x


def fusion(S: sp.Matrix):
    n = S.rows
    return [[[sp.simplify(sum(S[a,l]*S[b,l]*sp.conjugate(S[c,l])/S[0,l]
                               for l in range(n)))
              for c in range(n)] for b in range(n)] for a in range(n)]


def fs_indicators(S: sp.Matrix, twists, N):
    n = S.rows
    twists = [sp.sympify(t) for t in twists]  # Avoid Python true-division floats.
    dims = [sp.simplify(S[0,a]/S[0,0]) for a in range(n)]
    D2 = sum(d*d for d in dims)
    return [sp.simplify(sum(N[a][b][c]*dims[a]*dims[b]*(twists[a]/twists[b])**2
                            for a in range(n) for b in range(n))/D2)
            for c in range(n)]


def conv(a,b,n):
    out = [0]*(n+1)
    for i,ai in enumerate(a[:n+1]):
        if ai:
            for j,bj in enumerate(b[:n+1-i]):
                if bj:
                    out[i+j] += ai*bj
    return out


def product_coeffs(steps, power, sign, n):
    out = [1]+[0]*n
    for step in steps:
        factor = [0]*(n+1)
        for j in range(power+1):
            if step*j <= n:
                factor[step*j] = math.comb(power,j)*sign**j
        out = conv(out,factor,n)
    return out


def theta_eta(tau, dps):
    """Direct tau-series, avoiding theta_2 fourth-root branch errors after T."""
    q = mp.exp(2*mp.pi*1j*tau)
    nt = math.ceil(mp.sqrt((dps+15)*mp.log(10)/(mp.pi*tau.imag)))+4
    ne = math.ceil((dps+15)*mp.log(10)/(2*mp.pi*tau.imag))+4
    th2 = 2*sum(mp.exp(mp.pi*1j*tau*(mp.mpf(n)+mp.mpf('0.5'))**2)
                  for n in range(nt))
    th3 = 1+2*sum(mp.exp(mp.pi*1j*tau*n*n) for n in range(1,nt))
    th4 = 1+2*sum((-1)**n*mp.exp(mp.pi*1j*tau*n*n) for n in range(1,nt))
    eta = mp.exp(mp.pi*1j*tau/12)*mp.fprod(1-q**n for n in range(1,ne))
    return [th2,th3,th4], eta


def main(output: Path, dps: int) -> None:
    # 1: four distinct sectors; the equality of spinor characters is NOT a quotient.
    labels = ['O','V','S','C']
    S4 = sp.Matrix([[1,1,1,1],[1,1,-1,-1],
                    [1,-1,-1,1],[1,-1,1,-1]])/2
    twists4 = [sp.Integer(1),-sp.Integer(1),I,I]
    t0 = sp.sqrt(3)/2-I/2  # exp(-pi i/6), c=2 vacuum multiplier
    T4 = t0*sp.diag(*twists4)
    check('S4 unitary', matrix_zero(S4*S4.T-sp.eye(4)))
    check('S4^2 = 1', matrix_zero(S4*S4-sp.eye(4)))
    check('(S4 T4)^3 = 1', matrix_zero((S4*T4)**3-sp.eye(4)))
    N4 = fusion(S4)
    check('all 64 four-sector fusion coefficients nonnegative integers',
          all(v.is_integer and v >= 0 for plane in N4 for row in plane for v in row))
    onepoint4 = [sum(N4[a][b][b] for b in range(4)) for a in range(4)]
    check('ordinary torus one-point dimensions [4,0,0,0]',onepoint4 == [4,0,0,0])
    nu4 = fs_indicators(S4,twists4,N4)
    check('four-sector indicators [1,1,-1,-1]', nu4 == [1,1,-1,-1])

    # Complete pointed associator and braiding data: semion x semion.
    G = [(0,0),(1,1),(1,0),(0,1)]
    add = lambda a,b: tuple(x^y for x,y in zip(a,b))
    dot = lambda a,b: sum(x*y for x,y in zip(a,b))
    assoc = lambda a,b,c: (-1)**sum(x*y*z for x,y,z in zip(a,b,c))
    braid = lambda a,b: I**dot(a,b)
    pentagon = 0
    for a,b,c,d in product(G,repeat=4):
        lhs = assoc(b,c,d)*assoc(a,add(b,c),d)*assoc(a,b,c)
        rhs = assoc(add(a,b),c,d)*assoc(a,b,add(c,d))
        assert lhs == rhs
        pentagon += 1
    hexagon = 0
    wrong_hexagon = 0
    for a,b,c in product(G,repeat=3):
        r1 = braid(a,b)*braid(a,c)*assoc(b,a,c)*assoc(a,b,c)*assoc(b,c,a)
        r2 = braid(b,c)*braid(a,c)*assoc(a,b,c)*assoc(a,c,b)*assoc(c,a,b)
        assert sp.simplify(braid(a,add(b,c))-r1) == 0
        assert sp.simplify(braid(add(a,b),c)-r2) == 0
        hexagon += 2
        wrong_hexagon += int(sp.simplify(braid(a,add(b,c))-braid(a,b)*braid(a,c)) != 0)
        wrong_hexagon += int(sp.simplify(braid(add(a,b),c)-braid(a,c)*braid(b,c)) != 0)
    check('all pointed pentagon and hexagon identities',pentagon == 256 and hexagon == 128)
    check('deliberately incorrect trivial associator detected',wrong_hexagon > 0,wrong_hexagon)
    check('pointed braiding reproduces S4', all(
        sp.simplify(braid(a,b)*braid(b,a)/2-S4[ia,ib]) == 0
        for ia,a in enumerate(G) for ib,b in enumerate(G)))

    # 2: symmetric restriction to (O,V,(S+C)/sqrt2).
    embed = sp.Matrix([[1,0,0],[0,1,0],[0,0,1/sp.sqrt(2)],[0,0,1/sp.sqrt(2)]])
    S3 = sp.simplify(embed.T*S4*embed)
    T3 = sp.simplify(embed.T*T4*embed)
    check('three-dimensional subspace invariant under S and T',
          matrix_zero(S4*embed-embed*S3) and matrix_zero(T4*embed-embed*T3))
    N3 = fusion(S3)
    check('projected Verlinde fusion is Ising-type',
          N3[1][1] == [1,0,0] and N3[1][2] == [0,0,1]
          and N3[2][2] == [1,1,0])
    nu3 = fs_indicators(S3,[1,-1,I],N3)
    check('rank-three candidate fails FS with nu_X=-sqrt(2)',nu3[2] == -sp.sqrt(2))
    check('rank-three still obeys genus-one matrix relations',
          matrix_zero(S3*S3-sp.eye(3)) and matrix_zero((S3*T3)**3-sp.eye(3)))
    # Valid Ising twists are a control with the same S and same fusion.
    isig = (sp.sqrt(2+sp.sqrt(2))+I*sp.sqrt(2-sp.sqrt(2)))/2  # exp(pi i/8)
    nu_valid = [sp.simplify(sp.expand_complex(v)) for v in fs_indicators(S3,[1,-1,isig],N3)]
    check('ordinary Ising positive control nu_X=1',nu_valid[2] == 1)

    # 3: quaternion matrices on the underlying real four-dimensional module.
    A = sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    B = sp.Matrix([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
    eye4 = sp.eye(4)
    check('quaternion orthogonality and determinant',
          A.T*A == eye4 and B.T*B == eye4 and A.det() == B.det() == 1)
    check('A^2=B^2=-1; AB=-BA',[A*A,B*B,A*B] == [-eye4,-eye4,-B*A])
    check('quaternion puncture commutator -1',A*B*A.inv()*B.inv() == -eye4)
    xs = sp.symbols('x0:16')
    X = sp.Matrix(4,4,xs)
    comm_equations = list(X*A-A*X)+list(X*B-B*X)
    comm_matrix,_ = sp.linear_eq_to_matrix(comm_equations,xs)
    comm_dim = 16-comm_matrix.rank()
    check('real commutant dimension four',comm_dim == 4)
    sym_equations = comm_equations + list(X-X.T)
    sym_matrix,_ = sp.linear_eq_to_matrix(sym_equations,xs)
    sym_dim = 16-sym_matrix.rank()
    check('symmetric invariant bilinear form dimension one',sym_dim == 1)
    # Local SO(4) spin fields with helicity charges +/-1/2.
    spin_charges = [(R(a,2),R(b,2)) for a,b in product([-1,1],repeat=2)]
    check('all four Ramond spin components have h=1/4',
          all(sum(t*t for t in charge)/2 == R(1,4) for charge in spin_charges))
    check('all four spin components give fermion branch monodromy -1',
          all(sp.simplify(sp.exp(2*sp.pi*I*x)) == -1
              for charge in spin_charges for x in charge))
    # Categorical balancing: V x S = C, twist_C/(twist_V twist_S) = -1.
    check('both spinor sectors have monodromy -1 against V',
          sp.simplify(twists4[3]/(twists4[1]*twists4[2])) == -1
          and sp.simplify(twists4[2]/(twists4[1]*twists4[3])) == -1)

    # 4: exact oscillator expansions. x=q^(1/2) for NS modes.
    n = 16
    nsp = product_coeffs(range(1,2*n+2,2),4,+1,2*n+1)
    nsm = product_coeffs(range(1,2*n+2,2),4,-1,2*n+1)
    O = [(nsp[2*k]+nsm[2*k])//2 for k in range(n+1)]
    V = [(nsp[2*k+1]-nsm[2*k+1])//2 for k in range(n+1)]
    spin = [2*v for v in product_coeffs(range(1,n+1),4,+1,n)]
    eta_poly = product_coeffs(range(1,n+1),1,-1,n)
    # Independently solve the Ising one-point null-vector differential equation.
    recur = [sp.Integer(1)]+[sp.Integer(0)]*n
    for m in range(1,n+1):
        recur[m] = -sum(sp.divisor_sigma(k,1)*recur[m-k] for k in range(1,m+1))/m
    check('eta oscillator product equals Ising one-point MLDE recurrence through q^16',
          recur == eta_poly)
    eta23 = product_coeffs(range(1,n+1),23,-1,n)
    dressed = {'O':conv(O,eta23,n),'V':conv(V,eta23,n),'S':conv(spin,eta23,n)}
    check('dressed functions have negative coefficients, not ordinary state counts',
          dressed['O'][1] == -17 and dressed['V'][1] == -84 and dressed['S'][1] == -38)

    # Independent bosonic D2-lattice coefficient computation (not theta products).
    boson_osc = [1]+[0]*n
    for step in range(1,n+1):
        factor = [0]*(n+1)
        for kk in range(n//step+1):
            factor[kk*step] = kk+1  # (1-q^step)^(-2)
        boson_osc = conv(boson_osc,factor,n)
    lattice = {label:[0]*(n+1) for label in labels}
    bound = math.ceil(math.sqrt(2*(n+1)))+2
    for aa,bb in product(range(-bound,bound+1),repeat=2):
        lbl = 'O' if (aa+bb)%2==0 else 'V'
        base = 0 if lbl=='O' else R(1,2)
        exponent = R(aa*aa+bb*bb,2)-base
        if exponent.is_integer and 0<=exponent<=n:
            lattice[lbl][int(exponent)] += 1
        lbl = 'S' if (aa+bb)%2==0 else 'C'
        exponent = ((aa+R(1,2))**2+(bb+R(1,2))**2)/2-R(1,4)
        if exponent.is_integer and 0<=exponent<=n:
            lattice[lbl][int(exponent)] += 1
    lattice_chars = {lbl:conv(vals,boson_osc,n) for lbl,vals in lattice.items()}
    check('independent D2 lattice enumeration reproduces four fermion characters through q^16',
          lattice_chars['O']==O and lattice_chars['V']==V
          and lattice_chars['S']==spin and lattice_chars['C']==spin)
    check('symbolic modular, fusion and indicator data contain no floating-point constants',
          not any(sp.sympify(v).has(sp.Float) for v in list(S4)+list(S3)+nu4+nu3+nu_valid))

    # Tensor control Ising^23 x SO(4)_1, insertion psi^23 x 1.
    h_op = R(23,2)
    c_total = R(23,2)+2
    internal_h = [R(23,16)+h for h in [0,R(1,2),R(1,4),R(1,4)]]
    tensor_exponents = [sp.simplify(h-c_total/24) for h in internal_h]
    check('tensor control exact exponents',tensor_exponents == [R(7,8),R(11,8),R(9,8),R(9,8)])
    # Ising fusion from the already-computed Ising S matrix.
    onepoint_ising = [sum(N3[a][b][b] for b in range(3)) for a in range(3)]
    check('Ising puncture dimensions [3,1,0]',onepoint_ising == [3,1,0])
    tensor_block_count = int(onepoint_ising[1]**23*onepoint4[0])
    check('four labelled tensor-product one-point blocks',tensor_block_count == 4)
    check('adding one ordinary SO4 spinor insertion kills factorized tensor blocks',
          onepoint_ising[1]**23*onepoint4[2] == 0 and onepoint_ising[1]**23*onepoint4[3] == 0)

    # 5: exact finite metaplectic multiplier. A monomial is rows -> (column, zeta8 exponent).
    ident = ((0,1,2),(0,0,0))
    Sm = ((2,1,0),(1,1,1))
    Tm = ((0,2,1),(1,7,7))
    def mmul(a,b):
        p,e = a; q,f = b
        return (tuple(q[p[i]] for i in range(3)),tuple((e[i]+f[p[i]])%8 for i in range(3)))
    seen = {ident}; queue = deque([ident])
    while queue:
        cur = queue.popleft()
        for gen in (Sm,Tm):
            nxt = mmul(cur,gen)
            if nxt not in seen:
                seen.add(nxt);queue.append(nxt)
        if len(seen) > 10000:
            raise RuntimeError('Unexpected group size')
    check('Phi multiplier group order 96',len(seen) == 96)
    Sm4 = mmul(mmul(Sm,Sm),mmul(Sm,Sm))
    check('genuine metaplectic central action S^4=-1',Sm4 == ((0,1,2),(4,4,4)))
    center = [g for g in seen if mmul(g,Sm)==mmul(Sm,g) and mmul(g,Tm)==mmul(Tm,g)]
    check('four scalar central elements',len(center)==4 and all(g[0]==(0,1,2) and len(set(g[1]))==1 for g in center))

    # 6: independent numerical functional checks with direct tau-series.
    mp.mp.dps = dps
    taus = [mp.mpc('0.19','0.72'),mp.mpc('0.37','1.13'),mp.mpc('-0.41','0.88'),
            mp.mpc('0','1'),mp.mpc('-0.5',mp.sqrt(3)/2),mp.mpc('0.63','0.44')]
    maxerrs = {'F_equals_2Z':mp.mpf(0),'jacobi':mp.mpf(0),
               'Psi_S':mp.mpf(0),'Psi_T':mp.mpf(0),'Phi_S':mp.mpf(0),'Phi_T':mp.mpf(0)}
    def residual(a,b):
        return max(abs(x-y) for x,y in zip(a,b))/max(mp.mpf(1),*(abs(y) for y in b))
    for tau in taus:
        th,eta = theta_eta(tau,dps)
        psi = [(v/eta)**2 for v in th]
        phi = [eta**21*v*v for v in th]
        chars = [(psi[1]+psi[2])/2,(psi[1]-psi[2])/2,psi[0]/2,psi[0]/2]
        ff = sum(abs(x)**2 for x in psi)
        zz = sum(abs(x)**2 for x in chars)
        maxerrs['F_equals_2Z']=max(maxerrs['F_equals_2Z'],abs(ff-2*zz)/max(1,abs(ff)))
        maxerrs['jacobi']=max(maxerrs['jacobi'],abs(th[1]**4-th[0]**4-th[2]**4)/max(1,abs(th[1]**4)))
        for move in ('S','T'):
            tx = -1/tau if move=='S' else tau+1
            tth,ee=theta_eta(tx,dps)
            pp=[(v/ee)**2 for v in tth]
            ph=[ee**21*v*v for v in tth]
            if move=='S':
                targetpsi=[psi[2],psi[1],psi[0]]
                targetphi=[(-1j*tau)**mp.mpf('11.5')*phi[j] for j in (2,1,0)]
            else:
                fac=mp.exp(-mp.pi*1j/6)
                targetpsi=[fac*1j*psi[0],fac*psi[2],fac*psi[1]]
                facphi=mp.exp(mp.pi*1j*mp.mpf('1.75'))  # exp(7 pi i /4)
                targetphi=[facphi*1j*phi[0],facphi*phi[2],facphi*phi[1]]
            maxerrs['Psi_'+move]=max(maxerrs['Psi_'+move],residual(pp,targetpsi))
            maxerrs['Phi_'+move]=max(maxerrs['Phi_'+move],residual(ph,targetphi))
    threshold=mp.mpf(10)**(-(dps-12))
    check('all numerical residuals below working tolerance (not a rigorous error bound)',
          all(v<threshold for v in maxerrs.values()),{k:mp.nstr(v,8) for k,v in maxerrs.items()})

    result = {
        'title':'Quantum realization of the complete weave — run 1',
        'date':'2026-10-10',
        'versions':{'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__},
        'scope':'Independent bounded verification; no project code, no experimental data, no repository modifications.',
        'four_sector_control':{'labels':labels,'S':S4,'T':T4,'twists':twists4,'fusion':N4,
             'FS_indicators':nu4,'one_point_dimensions':onepoint4,
             'pentagon_identities_checked':pentagon,'hexagon_identities_checked':hexagon,
             'wrong_associator_hexagon_failures':wrong_hexagon},
        'three_function_projection':{'S':S3,'T':T3,'fusion':N3,'FS_indicators':nu3,
             'status':'EXACT OBSTRUCTION to this interpretation as three simple sectors of a bosonic UMTC; not an obstruction to a subrepresentation or punctured/spin blocks.',
             'merged_spinor_leading_coefficient':2*sp.sqrt(2)},
        'quaternion_realization':{'A':A,'B':B,'commutator':-eye4,'commutant_real_dimension':comm_dim,
             'symmetric_invariant_forms_dimension':sym_dim,'spinor_weights':[R(1,4)]*4,
             'status':'Exact classical/OPE symmetry realization. Noncommuting twisted-background conformal blocks NOT computed.'},
        'series':{'q_order':n,'O_prefactor':'q^(-1/12)','O_coefficients':O,
             'V_prefactor':'q^(5/12)','V_coefficients':V,
             'S_prefactor':'q^(1/6)','S_coefficients':spin,
             'eta_coefficients':eta_poly,'eta23_dressed_coefficients':dressed},
        'eta23_existence_control':{'theory':'Ising^23 tensor SO(4)_1',
             'insertion':'psi tensor ... tensor psi (23 copies), tensor identity_SO4',
             'central_charge_per_chiral_half':c_total,'insertion_chiral_weight':h_op,
             'internal_weights':internal_h,'q_exponents':tensor_exponents,
             'labelled_one_point_block_count':tensor_block_count,
             'independent_unrefined_function_count':3,
             'status':'CONDITIONAL EXACT CFT BLOCK REALIZATION of Phi; it does NOT implement quaternion puncture in SO4 factor.'},
        'metaplectic':{'order':len(seen),'center':sorted(center),'S4_monomial':Sm4,
             'T_exponents_mod_1':[R(1,8),R(3,8),R(7,8)]},
        'numerics':{'precision_decimal_digits':dps,'number_base_points':len(taus),
             'maximum_relative_residuals':{k:mp.nstr(v,15) for k,v in maxerrs.items()},
             'status':'Numerical checks only; no interval-arithmetic error bound.'},
        'checks':CHECKS,
        'still_open':['Q8-twisted puncture blocks and their sewing',
             'matching the original geometric cohomology construction, beyond multiplier coincidence',
             'selection or elimination of spectator sectors','quantum anomaly analysis for the faithful defect',
             'gravity, four-dimensional gauge chirality, Standard Model observables'],
    }
    output.write_text(json.dumps(serial(result),indent=2,ensure_ascii=False)+'\n')
    print(f'{len(CHECKS)} grouped checks passed; {pentagon} pentagons, {hexagon} hexagons; wrong-associator control: {wrong_hexagon} failures.')
    print('Three-function projected FS indicators:',nu3)
    print('Four-sector ordinary one-point dimensions:',onepoint4)
    print('Tensor eta23 control: c=',c_total,', h=',h_op,', exponents=',tensor_exponents)
    print('Finite multiplier image order:',len(seen))
    print('Numeric max residuals:',{k:mp.nstr(v,6) for k,v in maxerrs.items()})
    print('Wrote',output)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    parser.add_argument('--dps',type=int,default=80)
    args=parser.parse_args()
    if args.dps < 40:
        parser.error('--dps must be at least 40')
    main(args.output,args.dps)
