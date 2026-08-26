#!/usr/bin/env python3
"""Exact fixed-frame audit of outside Memo 56's E6 cubic/parity table.

Requires SymPy.  The E6/27 construction is branch-local and file-relative.
The conclusion is deliberately representation-theoretic: it does not infer a
physical portal, stable particle, abundance or mass.
"""

from collections import Counter
from fractions import Fraction as F
from pathlib import Path


HERE=Path(__file__).resolve().parent
STACK=HERE/"r006_e6_invariants"/"twisted_double.py"
source=STACK.read_text(encoding="utf-8")
cut=source.index("# ---------------- stage 4")
saved_file=globals()["__file__"]
globals()["__file__"]=str(STACK)
exec(compile(source[:cut],str(STACK),"exec"),globals())
globals()["__file__"]=saved_file

# Fixed D5 x U(1)_psi grading.  The charge convention is
# 27 = 16_(+1) + 10_(-2) + 1_(+4).
charges={index:int(3*ipr(weights[index],omega1)) for index in range(27)}
counts=Counter(charges.values())
assert counts==Counter({1:16,-2:10,4:1})
family={index:("16" if charge==1 else "10" if charge==-2 else "1")
        for index,charge in charges.items()}

# Selected bridge A1 grading.  This A1 is a branch choice, not a proved
# object-native selector (OA-C1087).
r0=ROOTS[0]
h=[F(0)]*DIM
for index in range(N):
    h[index]=F(r0[index])
H=rho27_Q(h)
bridge_weight=[int(H[index][index]) for index in range(27)]
assert Counter(bridge_weight)==Counter({-1:6,0:15,1:6})
root_charge=3*ipr(tuple(sp.Rational(value) for value in r0),omega1)
assert root_charge==-3

# Enumerate the complete 45 weight-zero supports of the fixed normalized
# invariant cubic.  R006 separately proves the invariant line is unique and
# that its normalized representative has these 45 nonzero terms.
weight_vectors=[tuple(sp.Rational(value) for value in weight) for weight in weights]
triples=[]
for a in range(27):
    for b in range(a,27):
        target=tuple(-(weight_vectors[a][k]+weight_vectors[b][k]) for k in range(6))
        for c in range(b,27):
            if weight_vectors[c]==target:
                triples.append((a,b,c))
assert len(triples)==45
types=Counter(tuple(sorted((family[a],family[b],family[c]))) for a,b,c in triples)
assert types==Counter({("10","16","16"):40,("1","10","10"):5})

matter_parity={index:(-1 if family[index]=="16" else 1) for index in range(27)}
assert all(matter_parity[a]*matter_parity[b]*matter_parity[c]==1
           for a,b,c in triples)

lock={index:(-1 if bridge_weight[index]%2 else 1) for index in range(27)}
assert not all(lock[index]==matter_parity[index] for index in range(27))
assert not all(lock[index]==-matter_parity[index] for index in range(27))
cross=Counter((family[index],bridge_weight[index]) for index in range(27))
joint=Counter((matter_parity[index],lock[index]) for index in range(27))

print("D5 x U(1)_psi branching:",dict(counts))
print("cubic support types:",dict(types))
print("matter parity conserved on all 45 supports: True")
for label in ("16","10","1"):
    print(label,"bridge weights:",{weight:cross[(label,weight)] for weight in (-1,0,1)})
print("bridge-root U(1)_psi charge:",root_charge)
print("matter parity equals selected lock up to sign: False")
print("joint parity distribution:",dict(joint))
print("VERDICT: FIXED-FRAME CUBIC HYPERGRAPH/PARITIES PROVED; DARK-MATTER PHYSICS NOT DERIVED")
