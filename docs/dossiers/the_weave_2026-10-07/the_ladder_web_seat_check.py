# Post hoc check (2026-10-24) of the web seat's group and diagram facts in its ladder opinion (chat1 relay 61f63feac), on this seat's own code. Not a sealed run.
import itertools, networkx as nx
from networkx.algorithms import isomorphism
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup
def T(p,q,r):
    G=nx.Graph(); G.add_node(0); n=1
    for arm in (p,q,r):
        prev=0
        for _ in range(arm-1):
            G.add_edge(prev,n); prev=n; n+=1
    return G
fin={'D5':T(2,2,3),'E6':T(2,3,3),'E7':T(2,3,4),'E8':T(2,3,5)}
aff={'D5~':None,'E6~':T(3,3,3),'E7~':T(2,4,4),'E8~':T(2,3,6)}
D=nx.Graph(); D.add_edges_from([(0,1),(0,2),(0,3),(3,4),(3,5)]); aff['D5~']=D
def induced_copies(H,G):
    GM=isomorphism.GraphMatcher(G,H)
    return len({frozenset(m) for m in GM.subgraph_isomorphisms_iter()})
for a,b in [('D5','E6'),('E6','E7'),('E7','E8')]:
    print('finite',a,'in',b,induced_copies(fin[a],fin[b]))
for a,b in [('D5~','E6~'),('E6~','E7~'),('E7~','E8~')]:
    print('affine',a,'in',b,induced_copies(aff[a],aff[b]))
S3,A4,S4,A5=SymmetricGroup(3),AlternatingGroup(4),SymmetricGroup(4),AlternatingGroup(5)
def has_subgroup_iso(G,H):
    # brute force: subgroups of G of order |H| isomorphic to H (by order profile and abelian-ness is enough here)
    n=H.order()
    if G.order()%n: return False
    els=list(G.elements)
    from sympy.combinatorics import PermutationGroup
    for a in els:
        for b in els:
            K=PermutationGroup([a,b])
            if K.order()==n and K.is_abelian==H.is_abelian and sorted(x.order() for x in K.elements)==sorted(x.order() for x in H.elements):
                return True
    return False
print('S3 in A4',has_subgroup_iso(A4,S3)); print('A4 in S4',has_subgroup_iso(S4,A4)); print('S4 in A5',has_subgroup_iso(A5,S4))
print('A5 simple', all(A5.normal_closure(g).order() == 60 for g in A5.elements if not g.is_Identity))
print('2O in 2I by order', 120 % 48 == 0)
