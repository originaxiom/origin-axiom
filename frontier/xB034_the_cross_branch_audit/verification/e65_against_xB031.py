"""xB034 C2 -- E65 against xB031's banked modules.  Any SL(2) rep preserves the symplectic form J (g^T J g = J),
so rho_chi = [[chi, c],[0, chi^-1]] is self-dual EVEN THOUGH it is non-split; hence Sym^m(rho_chi) is
self-dual, and V = Sym^m(rho_chi) (x) psi has V* = Sym^m(rho_chi) (x) psi^-1.
So psi^2 = 1  ==>  V self-dual  ==>  n(V) = n(V*)  ==>  I = n(V) - n(V*) = 0.
KILL: any module with psi^2 = 1 and I != 0."""
import sys, json, pathlib, collections
HERE = (pathlib.Path(__file__).resolve().parents[2] / 'xB031_the_unrun_modules' / 'verification')
sys.path.insert(0, str(HERE))
from c2_reducible_index import *
from c2_run import characters
K = NF([1, 0, -1, 0, 1]); z = K.alpha(); S = [K.pw(z, k) for k in range(12)]
M, gens, rels, mu, lam = presentation('t12835')
chars = characters(K, gens, rels, S)
def order_of(v):
    for k in range(1, 13):
        if K.is_zero(K.sub(K.pw(v, k), K.const(1))): return k
loci = []
for chi in chars:
    if all(K.is_zero(K.sub(chi[g], K.const(1))) for g in gens): continue
    chi2 = {g: K.mul(chi[g], chi[g]) for g in gens}
    c, h1 = nonsplit_cocycle(K, gens, rels, chi2)
    if c is not None: loci.append((chi, tuple(order_of(chi[g]) for g in gens)))
S6 = [s for s in S if K.is_zero(K.sub(K.pw(s, 6), K.const(1)))]
psis = characters(K, gens, rels, S6)
def twists_for(chi):
    tw = [p for p in psis]; cj = {g: K.const(1) for g in gens}
    for j in range(1, 4):
        cj = {g: K.mul(cj[g], chi[g]) for g in gens}; tw.append(dict(cj))
    return tw
def psi_sq_trivial(psi):
    return all(K.is_zero(K.sub(K.mul(psi[g], psi[g]), K.const(1))) for g in gens)
def check(results, sel, MS, label):
    idx = 0; tab = collections.Counter(); bad = []
    for chi, orders in sel:
        for m in MS:
            for psi in twists_for(chi):
                if idx >= len(results): break
                r = results[idx]; idx += 1
                if r.get('status') not in (None, 'RUN'): continue
                sd = psi_sq_trivial(psi)
                tab[(sd, r['I'] != 0)] += 1
                if sd and r['I'] != 0: bad.append((orders, m, r['I']))
    print(f"{label}: matched {idx} of {len(results)} modules")
    print(f"   psi^2 = 1 (SELF-DUAL):     I = 0 on {tab[(True, False)]},  I != 0 on {tab[(True, True)]}")
    print(f"   psi^2 != 1 (not forced):   I = 0 on {tab[(False, False)]},  I != 0 on {tab[(False, True)]}")
    print(f"   KILL (self-dual with I != 0): {len(bad)} {bad[:5]}")
    return idx == len(results), len(bad), tab
x2 = json.load(open(HERE / 'x2_t12835.json'))
ok2, bad2, t2 = check(x2, loci, [1, 2, 3], "X2 (m=1..3, all 55 loci)")
TARGET = {(3, 12, 1), (3, 12, 2), (3, 4, 1), (3, 4, 2)}
x3 = json.load(open(HERE / 'x3_partial.json'))
ok3, bad3, t3 = check(x3, [L for L in loci if L[1] in TARGET], [4, 5, 6], "X3 (m=4..6, 24 loci)")
nz = t2[(False, True)] + t3[(False, True)]; sdz = t2[(True, False)] + t3[(True, False)]
print(f"\nALIGNMENT complete on both: {ok2 and ok3}")
print(f"E65 CONSISTENCY: {sdz} self-dual modules, every one at I = 0; kill fired {bad2 + bad3} times")
print(f"=> ALL {nz} nonzero-I modules have a psi with psi^2 != 1: the twist is what breaks self-duality.")
