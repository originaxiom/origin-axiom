#!/usr/bin/env python3
"""Independent check of the s958 positive: the same module (chi = the order-3 torsion character of H_1 = Z/3 + Z, rho_chi the
reducible non-split extension, V = Sym^3(rho_chi) (x) chi) computed on THREE different presentations of pi_1(s958) (SnapPy's
default and two randomized triangulations), where the character is transported by its defining property (values on generators
read off from the abelianisation). The index is an invariant of (pi_1, module) and must agree."""
import sys, pathlib, itertools, snappy
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import *
K=NF([1,0,-1,0,1]); z=K.alpha(); S=[K.pw(z,k) for k in range(12)]
def order3_chars(K,gens,rels):
    out=[]
    for vals in itertools.product([K.const(1),K.pw(z,4),K.pw(z,8)],repeat=len(gens)):   # zeta_12^4 = zeta_3
        chi=dict(zip(gens,vals))
        if all(K.is_zero(K.sub(char_on_word(K,r,chi),K.const(1))) for r in rels) and not all(K.is_zero(K.sub(chi[g],K.const(1))) for g in gens): out.append(chi)
    return out
res=[]
for trial in range(3):
    M=snappy.Manifold('s958')
    for _ in range(trial): M.randomize()
    G=M.fundamental_group(); gens=G.generators(); rels=G.relators(); mu,lam=G.peripheral_curves()[0]
    print(f'presentation {trial}:', gens, rels, (mu,lam), 'H1', M.homology())
    chars=order3_chars(K,gens,rels); print('  order-3 characters:', len(chars))
    for chi in chars:
        chi2={g:K.mul(chi[g],chi[g]) for g in gens}; c,h1=nonsplit_cocycle(K,gens,rels,chi2)
        print('  chi on mu, lambda:', char_on_word(K,mu,chi), char_on_word(K,lam,chi), ' h1(chi^2) =', h1)
        if c is None: continue
        r=run_module(K,'s958',gens,rels,mu,lam,chi,c,3,chi,f'pres{trial} Sym3(rho_chi)(x)chi')
        res.append((trial,r['I'],r['I_ss']))
print('RESULTS (presentation, I, I_ss):', res)
print('PASS' if len(res)>=3 and len(set(abs(x[1]) for x in res))==1 and all(x[2]==0 for x in res) and res[0][1]!=0 else 'CHECK')
