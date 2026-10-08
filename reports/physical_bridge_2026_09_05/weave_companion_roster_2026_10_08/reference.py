"""Separate integer weight-convolution route, not a separate author or PDE proof."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement
import json

ZERO=(0,0,0,0,0)
ONE=Counter({ZERO:1})
C=Counter({(1,0,0,0,0):1,(0,1,0,0,0):1,(-1,-1,0,0,0):1})
F=Counter({(0,0,1,0,0):1,(0,0,0,1,0):1,(0,0,-1,-1,0):1})
W=Counter({(0,0,0,0,1):1,(0,0,0,0,-1):1})


def dual(a):
    return Counter({tuple(-v for v in k):n for k,n in a.items()})


def tensor(a,b):
    out=Counter()
    for k,n in a.items():
        for l,m in b.items():
            out[tuple(x+y for x,y in zip(k,l))]+=n*m
    return out


def scale(a,n):
    return Counter({k:n*v for k,v in a.items() if n*v})


def adjoint(a):
    b=tensor(a,dual(a))
    b[ZERO]-=1
    return +b


def sym2(a):
    values=list(a.elements())
    out=Counter()
    for i,j in combinations_with_replacement(range(len(values)),2):
        out[tuple(x+y for x,y in zip(values[i],values[j]))]+=1
    return out


def pack(a):
    return [[list(k),v] for k,v in sorted(a.items()) if v]


def run():
    # End(rho)=1+chi1+chi2+chi3; Sym2(rho)=chi1+chi2+chi3;
    # Lambda2(rho)=1; Lambda3(rho tensor3)=rho tensor8+2rho.
    V1=adjoint(C)+adjoint(W)+adjoint(F)+tensor(C,sym2(F))+tensor(dual(C),dual(sym2(F)))
    Vchi=ONE+adjoint(F)+tensor(C,dual(F))+tensor(dual(C),F)
    Vrho=tensor(W,tensor(C,dual(F))+tensor(dual(C),F)+adjoint(F)+scale(ONE,2))
    m=[V1,Vchi,Vchi,Vchi,Vrho]
    dims=[sum(x.values()) for x in m]
    selection=[[int(s==c) for c in range(4)] for s in range(4)]
    spin_dim=dims[:4]
    form=V1+Vrho
    profiles,full_weights={},{}
    for a,b in product((-1,0,1),repeat=2):
        rows=[]
        for i,spin in enumerate(m[:4]):
            charges=[1+a,1-a,b-1,-b-1]
            pieces=[]
            for q in charges:
                pieces.append(V1 if q==0 else form if q in (-2,2) else spin)
            full=sum(pieces,Counter())
            n0=sum(q==0 for q in charges)
            nf=sum(q in (-2,2) for q in charges)
            ns=4-n0-nf
            p={'charges':charges,'scalar_slots':n0,'form_slots':nf,'spin_slots':ns,
               'left_zero_dimension':sum(sum(x.values()) for x in pieces),
               'neutral_supercharge_slots':n0,'R_copies':nf,
               'R_symmetric_mass_parameters':sum(1 for u in range(nf) for v in range(u+1,nf)),
               'ordinary_spin_zero_angular_fibre_channels':2*sum(Vrho.values())*ns,
               'all_weights_self_conjugate':full==dual(full),'dimension_from_weights':sum(full.values())}
            rows.append(p)
            full_weights[f'{a},{b}:{i}']=pack(full)
        profiles[f'{a},{b}']=rows
    # Direct coefficient integration of (x-x^2)^2 and (1-2x)^2.
    norm=Q(1,3)-Q(2,4)+Q(1,5)
    derivative=1-Q(4,2)+Q(4,3)
    facts={
        'modules_dimensions':dims==[55,27,27,27,56],
        'reconstructed_full_adjoint_dimension':dims[0]+3*dims[1]+2*dims[4]==248,
        'all_modules_self_dual':all(x==dual(x) for x in m),
        'all_four_spin_selections':all(sum(x)==1 for x in selection) and len({tuple(x) for x in selection})==4,
        'spin_zero_modules_have_no_doublets':all(not any(abs(k[-1])==1 for k in p) for p in m[:4]),
        'rho_module_has_weak_doublets':any(abs(k[-1])==1 for k in Vrho),
        'nine_twist_choices':len(profiles)==9,
        'all_four_spin_lines_retained':all(len(x)==4 for x in profiles.values()),
        'single_twist_dimensions':[x['left_zero_dimension'] for x in profiles['1,0']]==[276,220,220,220],
        'double_twist_dimensions':[x['left_zero_dimension'] for x in profiles['1,1']]==[332]*4,
        'untwisted_dimensions':[x['left_zero_dimension'] for x in profiles['0,0']]==[220,108,108,108],
        'all_charge_rosters_self_dual':all(x['all_weights_self_conjugate'] for v in profiles.values() for x in v),
        'complex_control_not_self_dual':C!=dual(C),
        'single_twist_one_protected_copy':all(x['R_copies']==1 and x['R_symmetric_mass_parameters']==0 for x in profiles['1,0']),
        'double_twist_one_pairing':all(x['R_copies']==2 and x['R_symmetric_mass_parameters']==1 for x in profiles['1,1']),
        'single_twist_continuum_channels':all(x['ordinary_spin_zero_angular_fibre_channels']==224 for x in profiles['1,0']),
        'double_twist_spin_channels_removed':all(x['ordinary_spin_zero_angular_fibre_channels']==0 for x in profiles['1,1']),
        'bump_residual_exact':derivative/norm==10,
        'equal_parabolic_weights_negative_slope':-2*Q(1,2)/2==Q(-1,2),
        'canonical_dual_also_negative':-2*Q(1,2)==-1 and -(-2*Q(1,2))==1,
    }
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
            'module_weights':[pack(x) for x in m],'module_dimensions':dims,
            'spin_line_selection':selection,'spin_kernel_dimensions':spin_dim,
            'twist_profiles':profiles,'complete_zero_weights':full_weights,
            'spin_Weyl_residual_coefficient':int(derivative/norm)}


if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
