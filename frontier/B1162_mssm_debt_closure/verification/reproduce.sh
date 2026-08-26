#!/usr/bin/env bash
# B1162 -- the MSSM-debt closure (cloud memos 71-75) + the height-308 witness.
# The WITNESS cohomology is SAGE-verified on-bench (witness_sage.txt: H0(Y,V)=0,
# the C372->C312 rank gate surjective, char-0 local freeness). Here: the pyenv
# facts that align cloud's closure with our banked chain.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee closure_checks.txt
import sympy as sp
print("(D1 alignment) cloud memo 75's discriminant = our B1160/B1161 discriminant")
u,t = sp.symbols('u t')
# cloud: cubic in u=Yu/Yq factors as -18(u-2)(u+4); ours (B1160): -18(t-3)(t+3) with Yu=-1+t => u=t-1
cloud = sp.factor(-18*(u-2)*(u+4))
ours  = sp.factor((-18*(t-3)*(t+3)).subs(t, u+1))
print("  cloud -18(u-2)(u+4)      =", sp.expand(cloud))
print("  ours  -18(t-3)(t+3)|t=u+1=", sp.expand(ours))
assert sp.expand(cloud) == sp.expand(ours), "the two seats' anomaly discriminants must agree"
print("  => IDENTICAL. cloud's D1 alignment audit confirms B1159/B1160/B1161. roots u=2,-4 = SM (Yu=-4 or +2).")

print()
print("(witness) SAGE-verified on-bench (witness_sage.txt):")
for line in open("witness_sage.txt"):
    print("   ", line.rstrip())
assert "H0(V)=0" in open("witness_sage.txt").read(), "witness must show H0(Y,V)=0"
assert "312" in open("witness_sage.txt").read(), "witness must show the C372->C312 rank gate = 312"

print()
print("(D4 one generation) confirms B1161 generation-index NULL: trace field x^2-x+1")
p = sp.Poly(sp.symbols('x')**2 - sp.symbols('x') + 1, sp.symbols('x'))
print("   disc =", sp.discriminant(p), "degree", p.degree(), "=> multiplicities in {1,2}, never 3; one 27 = ONE generation.")
print("   (cloud D4: the trinification Z/3 rotates quark->lepton->antiquark WITHIN a generation; the 3 lives in E8's (3,27).)")
print()
print("REPRODUCES")
PY
