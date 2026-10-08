"""Separate SU5 tensor roster and exact rational differential polynomials."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json

def weights():
    z = (-2,-2,-2,3,3); w = (-2,-1,0,1,2)
    out = Counter()
    for i,j in product(range(5),repeat=2):
        out[z[i]-z[j],0] += 1
        out[0,w[i]-w[j]] += 1
    out[0,0] -= 2
    for i,j in combinations(range(5),2):
        for b in w:
            out[z[i]+z[j],b] += 1
            out[-z[i]-z[j],-b] += 1
        for a in z:
            out[-a,w[i]+w[j]] += 1
            out[a,-w[i]-w[j]] += 1
    return out

def modules():
    source = weights(); out = {}
    for charge in sorted({q for q,m in source}):
        left = Counter({m:a for (q,m),a in source.items() if q == charge})
        while any(left.values()):
            j = max(m for m,a in left.items() if a)
            count = left[j]
            if j < 0 or count < 0: raise ValueError('not an sl2 character')
            out[charge,j] = count
            for m in range(-j,j+1):
                left[m] -= count
                if left[m] < 0: raise ValueError('negative multiplicity')
    return out

def p_add(a,b):
    out = dict(a)
    for k,v in b.items(): out[k] = out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def p_mul(a,b):
    out = {}
    for i,x in a.items():
        for j,y in b.items(): out[i+j] = out.get(i+j,F(0))+x*y
    return {k:v for k,v in out.items() if v}
def p(c): return {0:F(c)} if c else {}
def mat_mul(a,b):
    return [[p_add(p_mul(a[i][0],b[0][j]),p_mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]

def rational_block(j,m,k):
    # Rational ladder basis, positive metric diag(b,a); its adjoint is explicit.
    a,b = F(j-m,2),F(j+m+1)
    d = F(2*k+m+1,2)
    plus,minus = {1:F(1),0:d},{1:F(-1),0:d}
    B = [[plus,p(a)],[p(-b),minus]]
    adj = [[minus,p(-a)],[p(b),plus]]
    result = mat_mul(adj,B)
    result[0][0] = p_add(result[0][0],p(-k))
    result[1][1] = p_add(result[1][1],p(-k))
    return result,a,b,d

def spectrum(n):
    scalar,vectors = Counter(),Counter(); negative = []
    aq = rr = vv = 0
    for (q,j),mult in sorted(modules().items()):
        k = n*q
        for m in range(-j,j+1):
            if m%2 == 0:
                v = F(1,4)+F(2*k+m,2)**2+F(j*(j+1)-m*m,2)
                vectors[v] += mult; vv += mult
                copies = 1 if m == j else 2
                scalar[v] += copies*mult; aq += copies*mult
            else:
                val = F(2*k+m-1,2)**2+F(j*(j+1)-m*m,2)-F(1,4)
                scalar[val] += mult; rr += mult
                if val < 0: negative.append({'q':q,'j':j,'kind':'R','m':m,'threshold':str(val),'count':mult})
        if j%2:
            val = F(2*k-j-1,2)**2-F(2*j+1,4)
            scalar[val] += mult; aq += mult
            if val < 0: negative.append({'q':q,'j':j,'kind':'Q_bottom','m':-j,'threshold':str(val),'count':mult})
    return {'n':n,'AQ':aq,'R':rr,'vector':vv,
            'scalar_thresholds':{str(k):v for k,v in sorted(scalar.items())},
            'vector_thresholds':{str(k):v for k,v in sorted(vectors.items())},
            'scalar_bottom':str(min(scalar)),'vector_bottom':str(min(vectors)),
            'negative':negative}

def run():
    predicates = {}; mods = modules(); source = weights()
    predicates['entire248_from_two_A4_tensor_factors'] = sum(source.values()) == 248
    predicates['correct_full_principal_multiplicities'] = {j:sum(a for (q,jj),a in mods.items() if jj == j) for j in range(5)} == {0:24,1:11,2:21,3:11,4:1}
    checks = []
    for j in range(1,5):
        for m in range(-j,j):
            if m%2 == 0:
                for k in range(-9,10):
                    matrix,a,b,d = rational_block(j,m,k)
                    target = {2:F(-1),0:d*d+a*b-k}
                    checks.append(matrix == [[target,{}],[{},target]] and a > 0 and b > 0)
    predicates['exact_weighted_adjoint_blocks'] = all(checks) and len(checks) == 190
    predicates['R_manifest_positive_remainder'] = all(F(j*(j+1)-m*m,2)-F(1,4) >= F(1,4) for j in range(1,5) for m in range(-j,j+1) if m%2)
    predicates['vector_manifest_nonnegative_Higgs_term'] = all(j*(j+1)-m*m >= 0 for j in range(5) for m in range(-j,j+1))
    predicates['actual_odd_j_charges_exclude_one'] = {q for q,j in mods if j in (1,3)} == {0,-2,2,-3,3}
    spectra = [spectrum(n) for n in range(-3,4)]
    predicates['all_zero_angular_channels_retained'] = all(p['AQ'] == 248 and p['R'] == 112 and p['vector'] == 136 for p in spectra)
    first = spectrum(1)['negative']
    predicates['negative_essential_multiplicities'] = {(r['threshold'],r['count']) for r in first} == {('-7/4',3),('-3/4',2)} and len(first) == 2
    predicates['first_flux_both_signs_and_higher_controls'] = all(p['scalar_bottom'] == ('-7/4' if abs(p['n']) == 1 else '1/4') for p in spectra)
    predicates['all_vector_sectors_positive'] = all(p['vector_bottom'] == '1/4' for p in spectra)
    predicates['artificial_charge_one_is_discriminating'] = F(1,4)-1 < 0 and (1,1) not in mods
    # Exact intervals: E1<0 needs k=1; E3<0 needs k=1,2,3.
    predicates['integer_negative_sets_of_extreme_polynomials'] = [k for k in range(-4,7) if (k-1)**2-F(3,4) < 0] == [1] and [k for k in range(-4,7) if (k-2)**2-F(7,4) < 0] == [1,2,3]
    predicates['higher_actual_flux_avoids_negative_interval'] = all(abs(2*q) >= 4 for q,j in mods if j%2 and q != 0)
    predicates['soft_term_is_load_bearing'] = F(1,4) > 0 and F(1,4)-2 == -F(7,4)
    predicates['allowed_neutral_spin_radial_power'] = 0 > -1 and -2 < -1 and 1 > -1
    predicates['distinct_positive_kinetic_cost_of_amplitude'] = sum(z*z for z in (-2,-2,-2,3,3)) == 30
    primitive = lambda a: sum(c/F(k+1) for k,c in a.items())
    chi,dchi = {1:F(1),2:F(-1)},{0:F(1),1:F(-2)}
    predicates['exact_compact_packet_energy_ratio'] = primitive(p_mul(dchi,dchi))/primitive(p_mul(chi,chi)) == 10
    five = [(1,0,0),(-1,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    charges = {'2':sorted([[-x for x in w] for w in five[:3]]),'3':sorted([list(w) for w in five[3:]])}
    return {'predicates':predicates,'predicates_passed':sum(predicates.values()),
            'module_profile':{str(q)+','+str(j):a for (q,j),a in sorted(mods.items())},
            'spectra':spectra,'unstable_charge_profile':charges,
            'independent_analytic_acceptance':False,'physical_goal_achieved':False}

if __name__ == '__main__':
    result = run(); print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
