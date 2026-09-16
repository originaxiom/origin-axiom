#!/usr/bin/env python3
"""B1418 cell 2 driver. For a manifold, a number field K (given by its minimal polynomial) and a finite set S of candidate
character values, enumerate every character chi: pi -> K^x with values in S (relators checked), keep those with
H^1(pi; K_{chi^2}) != 0 (the reducible non-split locus), build rho_chi, and for m in MS and twists psi in {characters of
H_1 with values in S} u {chi^j} compute I. Every module run is recorded; NOT RUN is never folded into zero."""
import sys, json, time, itertools, pathlib
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import *
def characters(K,gens,rels,S):
    out=[]
    for vals in itertools.product(S,repeat=len(gens)):
        chi=dict(zip(gens,vals))
        if all(K.is_zero(K.sub(char_on_word(K,r,chi),K.const(1))) for r in rels): out.append(chi)
    return out
def run(name,K,S,MS,budget_s,tag,skip_trivial=True):
    M,gens,rels,mu,lam=presentation(name); t0=time.time(); results=[]
    chars=characters(K,gens,rels,S)
    print(f'{name}: {len(gens)} generators, {len(rels)} relators, {len(chars)} characters into S', flush=True)
    loci=[]
    for chi in chars:
        if skip_trivial and all(K.is_zero(K.sub(chi[g],K.const(1))) for g in gens): continue
        chi2={g:K.mul(chi[g],chi[g]) for g in gens}
        c,h1=nonsplit_cocycle(K,gens,rels,chi2)
        if c is not None: loci.append((chi,c,h1))
    print(f'  reducible non-split loci (h^1(chi^2) > 0, chi non-trivial): {len(loci)}', flush=True)
    S6=[s for s in S if K.is_zero(K.sub(K.pw(s,6),K.const(1)))]     # order | 6 only (the design: order 2 and 3 twists)
    psis=characters(K,gens,rels,S6)
    for li,(chi,c,h1) in enumerate(loci):
        lab=f'chi#{li}=' + ','.join(f'{g}:{tuple(map(str,chi[g]))}' for g in gens) + f' h1={h1}'
        print('  locus', lab, flush=True)
        twists=[('psi='+','.join(f'{g}:{tuple(map(str,p[g]))}' for g in gens), p) for p in psis]
        cj={g:K.const(1) for g in gens}
        for j in range(1,4):
            cj={g:K.mul(cj[g],chi[g]) for g in gens}; twists.append((f'psi=chi^{j}',dict(cj)))
        for m in MS:
            for tl,psi in twists:
                if time.time()-t0>budget_s: results.append({'name':name,'locus':lab,'m':m,'twist':tl,'status':'NOT RUN (budget)'}); continue
                r=run_module(K,name,gens,rels,mu,lam,chi,c,m,psi,f'{lab} m={m} {tl}')
                r.update({'locus':lab,'m':m,'twist':tl,'status':'RUN','tag':tag}); results.append(r)
        json.dump(results,open(pathlib.Path(__file__).with_name(f'c2_partial_{name}.json'),'w'),indent=1,default=str)
    nz=[r for r in results if r.get('status')=='RUN' and r['I']!=0]
    print(f'{name}: modules run {sum(1 for r in results if r["status"]=="RUN")}, not run {sum(1 for r in results if r["status"]!="RUN")}, NONZERO I: {len(nz)}', flush=True)
    for r in nz: print('   NONZERO:', r['locus'], 'm=',r['m'], r['twist'], 'I=',r['I'], 'I_ss=',r['I_ss'], flush=True)
    return results
if __name__=='__main__':
    which=sys.argv[1]; out=[]
    if which=='m004':
        K=NF([-1,-1,1]); phi=K.alpha(); ip=K.inv(phi)     # x^2 - x - 1: phi
        S=[K.const(1),K.const(-1),phi,K.neg(phi),ip,K.neg(ip)]
        out=run('m004',K,S,[1,2,3,4],3600,'golden locus over Q(phi)')
    elif which=='class12':
        K=NF([1,0,-1,0,1]); z=K.alpha()                   # x^4 - x^2 + 1: zeta_12
        S=[K.pw(z,k) for k in range(12)]
        names=sys.argv[2:] or ['s958','v2873','t12833','o10_150697','o10_150700','o10_150701','t12837','s956','t11365','t12835','m208']
        for n in names: out+=run(n,K,S,[1,2,3],1800,'roots of unity of order | 12 over Q(zeta_12)')
    elif which=='covers':
        # POST-SEAL EXTENSION (labelled): the one-cusped covers of m004 inside the class whose H_1 torsion admits characters into mu_12
        K=NF([1,0,-1,0,1]); z=K.alpha(); S=[K.pw(z,k) for k in range(12)]
        for n in ['s961','t12839']: out+=run(n,K,S,[1,2,3],1800,'POST-SEAL: covers of m004 over Q(zeta_12)')
    elif which=='m004z12':
        # compositum Q(phi, zeta_12): primitive element theta = phi + zeta_12, minimal polynomial computed by sympy
        import sympy as sp
        x=sp.symbols('x'); phi_=(1+sp.sqrt(5))/2; z_=sp.exp(2*sp.pi*sp.I/12)
        mp=sp.Poly(sp.minimal_polynomial(phi_+z_,x),x); co=[Fr(int(c)) for c in reversed(mp.all_coeffs())]
        K=NF(co); th=K.alpha(); print('compositum degree', K.d)
        # express phi and zeta_12 in terms of theta: solve numerically then rationalise via the field: use sympy's to_number_field
        from sympy.polys.numberfields import to_number_field
        el_phi=to_number_field(phi_, phi_+z_); el_z=to_number_field(z_, phi_+z_)
        def fromalg(a):
            cs=[Fr(int(c.p),int(c.q)) for c in reversed(sp.Poly(a.as_expr(),x).all_coeffs())] if False else None
            v=[Fr(0)]*K.d
            for i,cf in enumerate(a.coeffs()[::-1]): v[i]=Fr(int(sp.Rational(cf).p),int(sp.Rational(cf).q))
            return K.el(v)
        phi=fromalg(el_phi); z=fromalg(el_z); ip=K.inv(phi)
        assert K.is_zero(K.sub(K.mul(phi,phi),K.add(phi,K.const(1)))) and K.is_zero(K.sub(K.pw(z,12),K.const(1)))
        S=[K.mul(K.pw(z,k),p) for k in range(12) for p in (K.const(1),phi,ip)]
        out=run('m004',K,S,[1,2,3],5400,'golden locus with order-12 twists over Q(phi,zeta_12)')
    json.dump(out,open(pathlib.Path(__file__).with_name(f'c2_results_{which}.json'),'w'),indent=1,default=str)
