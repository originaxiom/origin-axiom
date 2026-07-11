import sympy as sp
from collections import Counter
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
def grow(n,seed='a'):
    w=seed
    for _ in range(n): w=''.join(sub[c] for c in w)
    return w
w=grow(9)

print("=== the couriers are a deterministic sub-machine; project the object onto its DECIDERS {a,A} ===")
dec=''.join(c for c in w if c in 'aA')
print("  decider-word (couriers deleted), first 40:", dec[:40])
print("  decider length / total:", len(dec), "/", len(w), "=", round(len(dec)/len(w),4), " (=1/phi, the golden section)")

# is the decider-word a substitution fixed point on {a,A}? find the induced map:
# under phi, each decider's image, projected to deciders:
print("\n=== induced substitution on the deciders (phi projected to {a,A}) ===")
proj=lambda s:''.join(c for c in s if c in 'aA')
ind={L:proj(sub[L]) for L in 'aA'}
print("  a ->", ind['a'], "   A ->", ind['A'])
# check the decider-word IS the fixed point of this induced map
def growind(n,seed='a'):
    x=seed
    for _ in range(n): x=''.join(ind[c] for c in x)
    return x
di=growind(9)
print("  induced fixed point matches projected word?", di[:len(dec)]==dec[:len(di)] or dec.startswith(di) or di.startswith(dec))
print("  induced abelianization:")
Mi=sp.Matrix([[ind[j].count(i) for j in 'aA'] for i in 'aA'])
sp.pprint(Mi)
x=sp.symbols('x'); print("  induced char poly:", sp.factor(Mi.charpoly(x).as_expr()), " eigenvalues:", Mi.eigenvals())

print("\n=== compare: the ORIGINAL golden cat map / Fibonacci a->ab,b->a has M=[[1,1],[1,0]], eig phi ===")
print("  is the decider-core the golden root A=[[2,1],[1,1]] or the Fibonacci? (check trace/det)")
print("  decider M: trace", Mi.trace(), " det", Mi.det())
