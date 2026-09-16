#!/usr/bin/env python3
"""Aggregate cell 2's results: per member, modules run / not run / nonzero, the loci that fire (orders of chi on the generators,
chi on mu and lambda), the m values and the index values."""
import json, glob, re, sys, pathlib
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import NF, presentation, char_on_word
from math import gcd
K12=NF([1,0,-1,0,1]); z=K12.alpha(); pw12={tuple(map(str,K12.pw(z,k))):k for k in range(12)}
summary={}
for f in sorted(glob.glob('c2_partial_*.json')):
    name=f[len('c2_partial_'):-5]; d=json.load(open(f))
    run=[r for r in d if r.get('status')=='RUN']; nr=[r for r in d if r.get('status')!='RUN']; nz=[r for r in run if r['I']!=0]
    loci={}
    for r in run: loci.setdefault(r['locus'],[]).append(r)
    fire=[]
    if name!='m004':
        M,gens,rels,mu,lam=presentation(name)
        for lab,rs in loci.items():
            n=[r for r in rs if r['I']!=0]
            if not n: continue
            vals=dict(re.findall(r"([a-z]):\(('[^)]*)\)",lab))
            chi={g:K12.el([Fraction(x.strip("'")) for x in vals[g].split("', '")]) for g in gens}
            ords=[12//gcd(12,pw12[tuple(map(str,chi[g]))]) for g in gens]
            cusp=(pw12[tuple(map(str,char_on_word(K12,mu,chi)))],pw12[tuple(map(str,char_on_word(K12,lam,chi)))])
            fire.append({'orders_on_generators':ords,'chi_mu_lambda_as_zeta12_powers':cusp,'cusp_trivial':cusp==(0,0),'modules':len(rs),'nonzero':len(n),'m_values':sorted(set(r['m'] for r in n)),'I_values':sorted(set(r['I'] for r in n))})
    summary[name]={'run':len(run),'not_run':len(nr),'nonzero':len(nz),'I_values':sorted(set(r['I'] for r in nz)),'I_ss_all_zero':all(r['I_ss']==0 for r in run),'loci_total':len(loci),'loci_firing':len(fire),'firing':fire}
    print(f"{name:12s} run {len(run):5d} not run {len(nr):5d} nonzero {len(nz):4d} I in {sorted(set(r['I'] for r in nz))} I_ss all zero {all(r['I_ss']==0 for r in run)} loci {len(loci)} firing {len(fire)}")
    for x in fire: print('    ',x)
json.dump(summary,open('c2_summary.json','w'),indent=1)
