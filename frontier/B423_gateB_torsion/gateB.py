"""B423 -- GATE B: compute the E6 adjoint Reidemeister torsion of the figure-eight, blind."""
import json, os
from fractions import Fraction as Fr
import sympy as sp

phi = (1+sp.sqrt(5))/2
A = sp.Matrix([[2,1],[1,1]])            # figure-eight monodromy, eigenvalues phi^2, phi^-2
# Sym^{2m}(A) eigenvalues: (phi^2)^(2m-k) (phi^-2)^k = phi^{2(2m-2k)} = phi^{4(m-k)}, k=0..2m
def tau_m(m):
    # det(I - Sym^{2m}(A)) = prod_{k=0}^{2m} (1 - phi^{4(m-k)})
    p = sp.Integer(1)
    for k in range(0, 2*m+1):
        p *= (1 - phi**(4*(m-k)))
    return sp.simplify(sp.expand(sp.nsimplify(p, [sp.sqrt(5)])))
exps = [1,4,5,7,8,11]                   # E6 exponents
taus = {}
for m in exps:
    t = tau_m(m)
    taus[m] = t
    print(f"tau_{m} = {t}")
tauE6 = sp.simplify(sp.prod([taus[m] for m in exps]))
print("\ntau_E6 (adjoint torsion) =", tauE6)
# characterize: is it a pure power-of-phi / integer with only prime 5? factor it.
val = sp.nsimplify(tauE6, [sp.sqrt(5)])
# rational part and sqrt5 part
a = sp.simplify((val + val.subs(sp.sqrt(5), -sp.sqrt(5)))/2)   # rational part
b = sp.simplify((val - val.subs(sp.sqrt(5), -sp.sqrt(5)))/(2*sp.sqrt(5)))  # sqrt5 coeff
print("rational part a =", a, "  sqrt5 coeff b =", b)
def prime_content(x):
    x = sp.Rational(x)
    prs = set()
    for n in (sp.Integer(x.p).__abs__(), sp.Integer(x.q)):
        for pr in sp.factorint(int(n)): prs.add(int(pr))
    return sorted(prs)
try:
    pc_a = prime_content(a) if a.is_rational else "non-rational"
    pc_b = prime_content(b) if b.is_rational else "non-rational"
except Exception as e:
    pc_a = pc_b = str(e)
print("prime content of a:", pc_a, "  of b:", pc_b)
non_golden = any(p not in (2,5) for p in (pc_a if isinstance(pc_a,list) else []) + (pc_b if isinstance(pc_b,list) else []))
res = dict(taus={str(m): str(taus[m]) for m in exps}, tauE6=str(tauE6),
           rational_part=str(a), sqrt5_coeff=str(b),
           prime_content_a=pc_a, prime_content_b=pc_b,
           non_golden_primes=bool(non_golden),
           verdict=("STRUCTURE: non-golden primes present -- computation produces what symmetry hid"
                    if non_golden else
                    "GOLDEN/FLAT: pure phi/Fibonacci-Lucas -- computation confirms the symmetry verdict"))
print("\nVERDICT:", res["verdict"])
json.dump(res, open("gateB.json","w"), indent=1)
print("DONE")
