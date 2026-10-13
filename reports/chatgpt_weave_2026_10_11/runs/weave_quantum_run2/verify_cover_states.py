#!/usr/bin/env python3
"""Exact Q8 cover chains, spin structures and mapping-class actions.
Independent of project and Run 1 code. Python >=3.10, SymPy.
All linear algebra is exact. Spin structures are quadratic refinements of
an independently constructed ribbon-graph intersection form, vanishing on
capped boundary cycles. They are NOT assumed to be fermion species.
"""
from __future__ import annotations
import itertools, json, pathlib, argparse
from collections import deque, Counter
import sympy as s
OUT=pathlib.Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--reverse-tree',action='store_true');args=parser.parse_args()
suffix='_alternate_tree' if args.reverse_tree else ''
checks={}
def check(name, result):
    ok=bool(result); checks[name]=ok
    print(f'{"PASS" if ok else "FAIL"}: {name}')
    if not ok: raise AssertionError(name)
# Elements: 1,i,j,k,-1,-i,-j,-k.
NAMES=['1','i','j','k','-1','-i','-j','-k']
def mul(a,b):
    sa=-1 if a>=4 else 1; sb=-1 if b>=4 else 1
    x,y=a%4,b%4
    if x==0: sign,z=1,y
    elif y==0: sign,z=1,x
    elif x==y: sign,z=-1,0
    else:
        z=6-x-y; sign=1 if (x,y) in [(1,2),(2,3),(3,1)] else -1
    return z+(4 if sa*sb*sign<0 else 0)
def inv(g):
    return next(h for h in range(8) if mul(g,h)==0)
def word(g, letters):
    for a in letters: g=mul(g,1 if a=='a' else 2 if a=='b' else inv(1) if a=='A' else inv(2))
    return g
check('Q8 axioms',all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in itertools.product(range(8),repeat=3)))
check('peripheral minus_one',word(0,'abAB')==4)
# Cayley graph vertices g; edges a_g, b_g.
edges=[(g,mul(g,t),t) for t in (1,2) for g in range(8)]
d=s.zeros(8,16)
for e,(u,v,t) in enumerate(edges): d[u,e]-=1; d[v,e]+=1
adj={g:[] for g in range(8)}
for e,(u,v,t) in enumerate(edges):
    adj[u].append((v,e,1)); adj[v].append((u,e,-1))
if args.reverse_tree:
    adj={g:list(reversed(a)) for g,a in adj.items()}
parent={0:None}; rootpaths={0:s.zeros(16,1)}; tree=[]; queue=deque([0])
while queue:
    u=queue.popleft()
    for v,e,sign in adj[u]:
        if v not in parent:
            parent[v]=(u,e,sign); tree.append(e); queue.append(v)
            p=rootpaths[u].copy(); p[e]+=sign; rootpaths[v]=p
nt=[e for e in range(16) if e not in tree]
cols=[]
for e in nt:
    u,v,_=edges[e]; c=rootpaths[u]-rootpaths[v]; c[e]+=1; cols.append(c)
C=s.Matrix.hstack(*cols)
check('graph_H1_dimension_9', d.rank()==7 and C.rank()==9 and d*C==s.zeros(8,9))
check('fundamental_cycle_coordinates',C.extract(nt,range(9))==s.eye(9))
def pathchain(g,letters):
    c=s.zeros(16,1)
    for a in letters:
        t=1 if a.lower()=='a' else 2
        if a.islower():
            e=g+(0 if t==1 else 8); c[e]+=1; g=mul(g,t)
        else:
            g=mul(g,inv(t)); e=g+(0 if t==1 else 8); c[e]-=1
    return g,c
fills=[]
for g in range(4):
    end,c=pathchain(g,'abABabAB'); check(f'cap_loop_{g}_closed',end==g); fills.append(c)
Fill=s.Matrix.hstack(*fills); B=Fill.extract(nt,range(4))
check('four_caps_one_relation',B.rank()==3 and C*B==Fill and sum(fills,s.zeros(16,1))==s.zeros(16,1))
# Ribbon graph cyclic order at each vertex: a+,b+,a-,b-.
# Darts encoded 2e (positive), 2e+1 (negative).
rot=[]
for g in range(8):
    am=mul(g,inv(1)); bm=mul(g,inv(2))
    rot.append([2*g,2*(8+g),2*am+1,2*(8+bm)+1])
rotmap={r[i]:r[(i+1)%len(r)] for r in rot for i in range(len(r))}
seen=set(); facecycles=[]
for h in range(32):
    if h not in seen:
        cc=[]; k=h
        while k not in seen:
            seen.add(k);cc.append(k);k=rotmap[k^1]
        facecycles.append(cc)
check('ribbon_graph_four_boundary_components',len(facecycles)==4)
# Contract the spanning tree. This produces a one-vertex chord diagram.
rot=[r[:] for r in rot]
for e in tree:
    a,b=2*e,2*e+1
    ia=next(i for i,r in enumerate(rot) if a in r)
    ib=next(i for i,r in enumerate(rot) if b in r)
    assert ia!=ib
    ra,rb=rot[ia],rot[ib]; pa,pb=ra.index(a),rb.index(b)
    merged=ra[pa+1:]+ra[:pa]+rb[pb+1:]+rb[:pb]
    rot=[r for i,r in enumerate(rot) if i not in (ia,ib)]+[merged]
assert len(rot)==1 and len(rot[0])==18
cyclic=rot[0]
J=s.zeros(9)
for p,e in enumerate(nt):
    k=cyclic.index(2*e); r=cyclic[k:]+cyclic[:k]; end=r.index(2*e+1)
    inside=set(r[1:end])
    for q,f in enumerate(nt):
        if p==q:continue
        # Oriented chord intersection (global sign immaterial for spin).
        J[p,q]=int(2*f in inside)-int(2*f+1 in inside)
check('intersection_rank_6_and_caps_radical',J.T==-J and J.rank()==6 and J*B==s.zeros(9,4))
# Compact quotient basis over Q, and all exact actions.
bb=B.columnspace(); hb=bb[:]
for j in range(9):
    ee=s.eye(9)[:,j]
    if s.Matrix.hstack(*(hb+[ee])).rank()>len(hb):hb.append(ee)
H=s.Matrix.hstack(*hb); Hi=H.inv(); Jclosed=H[:,3:].T*J*H[:,3:]
check('compact_H1_dimension_6',len(hb)==9 and Jclosed.rank()==6)

def autoQ(ai,bj):
    imgs=[0,ai,bj,mul(ai,bj)]
    return imgs+[mul(4,x) for x in imgs]
alphaL=autoQ(1,3);alphaR=autoQ(3,2)
def chain_map(vertexmap, aword,bword):
    M=s.zeros(16)
    for e,(u,v,t) in enumerate(edges):
        end,c=pathchain(vertexmap[u],aword if t==1 else bword)
        assert end==vertexmap[v];M[:,e]=c
    V=s.zeros(8)
    for i,j in enumerate(vertexmap):V[j,i]=1
    assert d*M==V*d
    Z=(M*C).extract(nt,range(9))
    assert C*Z==M*C
    assert (Hi*Z*H)[3:,:3]==s.zeros(6,3)
    return Z,(Hi*Z*H)[3:,3:]
actions={}
for name, vm,aw,bw in [('L',alphaL,'a','ab'),('R',alphaR,'ab','b')]:
    Z,K=chain_map(vm,aw,bw);actions[name]=(Z,K)
    check(f'{name}_preserves_intersection',Z.T*J*Z==J)
for g in range(8):
    vm=[mul(g,h) for h in range(8)]; Z,K=chain_map(vm,'a','b');actions[NAMES[g]]=(Z,K)
    check(f'deck_{NAMES[g]}_preserves_intersection',Z.T*J*Z==J)
# Decompose Q8 character of compact H1.
characters={name:int(actions[name][1].trace()) for name in NAMES}
chirows={
 'trivial':[1]*8,
 'chi_i':[1,1,-1,-1,1,1,-1,-1],
 'chi_j':[1,-1,1,-1,1,-1,1,-1],
 'chi_k':[1,-1,-1,1,1,-1,-1,1],
 'rho_2':[2,0,0,0,-2,0,0,0]}
mults={name:sum(characters[g]*ch[k] for k,g in enumerate(NAMES))//8 for name,ch in chirows.items()}
check('compact_decomposition_2trivial_plus_2rho',mults=={'trivial':2,'chi_i':0,'chi_j':0,'chi_k':0,'rho_2':2})
# Quadratic refinements q on H1(graph;F2). q must vanish on caps.
J2=[[int(J[i,j])%2 for j in range(9)] for i in range(9)]
def bits(n):return [(n>>i)&1 for i in range(9)]
def qvalue(qbits,v):
    x=[int(t)%2 for t in v]
    return (sum(qbits[i]*x[i] for i in range(9))+sum(J2[i][j]*x[i]*x[j] for i in range(9) for j in range(i+1,9)))%2
spin=[];parity={}
for n in range(512):
    qb=bits(n)
    if all(qvalue(qb,B[:,j])==0 for j in range(4)):
        spin.append(n)
        zeros=sum(qvalue(qb,bits(v))==0 for v in range(512))
        assert zeros in (224,288)
        parity[n]=0 if zeros==288 else 1
check('64_spins_36even_28odd',len(spin)==64 and Counter(parity.values())=={0:36,1:28})
perms={}
for name,(Z,K) in actions.items():
    pp={}
    for n in spin:
        vals=[qvalue(bits(n),Z[:,j]) for j in range(9)]
        m=sum(x<<j for j,x in enumerate(vals))
        assert m in spin and parity[m]==parity[n];pp[n]=m
    assert len(set(pp.values()))==64;perms[name]=pp
check('all_spin_actions_preserve_Arf',True)
fixed_Q=[n for n in spin if perms['i'][n]==n and perms['j'][n]==n]
check('no_Q8_invariant_spin_structure',len(fixed_Q)==0)
fixed_LR=[n for n in spin if perms['L'][n]==n and perms['R'][n]==n]
check('chosen_LR_lifts_fix_exactly_one_odd_spin',len(fixed_LR)==1 and parity[fixed_LR[0]]==1)
# Determine the four peripheral-point permutations directly from capped cycles.
cap_perms={}
for name,(Z,K) in actions.items():
    cap_perms[name]=[next(j for j in range(4) if Z*B[:,i]==B[:,j]) for i in range(4)]
fixed_caps=[i for i in range(4) if cap_perms['L'][i]==i and cap_perms['R'][i]==i]
check('chosen_LR_lifts_fix_one_peripheral_point',len(fixed_caps)==1)
ZL=actions['L'][0];ZR=actions['R'][0]
check('exact_braid_relation_on_cover',ZL*ZR.inv()*ZL==ZR.inv()*ZL*ZR.inv())
def orbits(gens):
    unseen=set(spin);out=[]
    while unseen:
        start=min(unseen);orbit={start};todo=[start]
        while todo:
            n=todo.pop()
            for gg in gens:
                m=perms[gg][n]
                if m not in orbit:orbit.add(m);todo.append(m)
        unseen-=orbit;out.append({'size':len(orbit),'parity':parity[start],'members':sorted(orbit)})
    return sorted(out,key=lambda z:(z['parity'],z['size'],z['members'][0]))
orbQ=orbits(['i','j']);orbLR=orbits(['L','R']);orbFull=orbits(['i','j','L','R'])
# central deck z is allowed to fix spin structures individually (lift still order four).
fixed={name:sum(perms[name][n]==n for n in spin) for name in perms}
# Closed Hodge decomposition by holomorphic Lefschetz: deck 1 has trace 3,
# central -1 has four fixed points derivative -1 -> trace -1;
# all other deck transformations are free -> trace 1.
holochar=[3,1,1,1,-1,1,1,1]
holomults={name:s.Rational(sum(holochar[k]*ch[k] for k in range(8)),8) for name,ch in chirows.items()}
check('holomorphic_forms_trivial_plus_rho',holomults=={'trivial':1,'chi_i':0,'chi_j':0,'chi_k':0,'rho_2':1})
results={
 'scope':'Exact cover topology and compact spin structures, not a quantum determinant calculation',
 'group_labels':NAMES,'edges':edges,'tree_edges':tree,'cycle_edges':nt,
 'cycle_basis':C.tolist(),'cap_coordinates':B.tolist(),'intersection_punctured':J.tolist(),
 'compact_basis_change':H.tolist(),'intersection_compact':Jclosed.tolist(),
 'compact_character':characters,'compact_multiplicities':mults,
 'holomorphic_character':holochar,'holomorphic_multiplicities':holomults,
 'actions':{name:{'punctured':Z.tolist(),'compact':K.tolist()} for name,(Z,K) in actions.items()},
 'spin_count':64,'even_count':36,'odd_count':28,'fixed_spins_by_generator':fixed,
 'fixed_under_deck_Q8':fixed_Q,'fixed_under_chosen_LR_lifts':fixed_LR,
 'Q8_spin_orbits':orbQ,'LR_spin_orbits':orbLR,'full_spin_orbits':orbFull,
 'spin_action':{name:{str(n):m for n,m in pp.items()} for name,pp in perms.items()},
 'tree_variant':suffix,'cap_permutations':cap_perms,'fixed_peripheral_point_under_LR':fixed_caps,'checks':checks}
(OUT/f'cover_states_results{suffix}.json').write_text(json.dumps(results,indent=2,default=str)+'\n')
print('CHARACTER:',characters,'MULTIPLICITIES:',mults)
print('FIXED:',fixed,'LR common:',fixed_LR)
print('Q8 ORBITS:',[(x['parity'],x['size']) for x in orbQ])
print('LR ORBITS:',[(x['parity'],x['size']) for x in orbLR])
print('FULL ORBITS:',[(x['parity'],x['size']) for x in orbFull])
print(f'{len(checks)} named checks passed')
