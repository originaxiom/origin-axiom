"""B1298 (b): fc R72's inner lift on B1296's own rational E6.  rho^vee = the Weyl coweight (<rho^vee, alpha> = ht alpha);
Ad(exp(pi i rho^vee)) acts on the root alpha by (-1)^ht: fixed roots, fixed subalgebra type, fixed Cartan; the order-3 inner
lift e^(2 pi i ht/3) likewise.  Prediction (DESIGN P2): 32 fixed roots, A5+A1 (dim 38), all of h fixed; order 3: 18 roots, A2^3."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e6_rational import *          # roots, S (simple roots), omega, coords, theta, W27, W27bar, dot, add, sub, scale, Fr
def height(r): return sum(coords(r))
assert all(height(r) == int(height(r)) for r in roots)
def subsystem_type(rs):
    """Dynkin type of a closed root subsystem: simple roots via a generic functional, then the Cartan matrix's components."""
    pos = [r for r in rs if height(r) > 0]          # height is a positivity functional on every closed subsystem (no root has height 0)
    possum = {key(add(a, b)) for a in pos for b in pos}
    simple = [r for r in pos if key(r) not in possum]
    n = len(simple); adj = {i: [j for j in range(n) if j != i and dot(simple[i], simple[j]) != 0] for i in range(n)}
    seen, comps = set(), []
    for i in range(n):
        if i in seen: continue
        stack, comp = [i], []
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x); comp.append(x); stack += adj[x]
        comps.append(sorted(comp))
    def name(comp):
        m = len(comp); degs = sorted(len([j for j in adj[i] if j in comp]) for i in comp)
        if m == 1: return "A1"
        if max(degs) <= 2 and degs.count(1) == 2: return f"A{m}"
        if m >= 4 and degs.count(3) == 1 and degs.count(1) == 3: return f"D{m}" if m > 4 else "D4"
        return f"rank{m}:{degs}"
    return sorted(name(c) for c in comps), n
def lift(order):
    fixed = [r for r in roots if height(r) % order == 0]
    types, rank = subsystem_type(fixed)
    return fixed, types, rank
fixed2, types2, rank2 = lift(2)
print(f"inner lift Ad(exp(pi i rho^vee)) = (-1)^ht: fixed roots {len(fixed2)} of 72, fixed subalgebra rank {rank2} type {types2}, dim {len(fixed2) + 6}")
print("   fixed Cartan: all of h (an inner lift by a torus element acts trivially on h): True")
fixed3, types3, rank3 = lift(3)
print(f"order-3 inner lift e^(2 pi i ht/3): fixed roots {len(fixed3)} of 72, type {types3}, dim {len(fixed3) + 6}")
# the outer lift for comparison: theta_D fixes 24 roots + a 4-dim Cartan = F4 (dim 52)
fixed_theta = [r for r in roots if theta(r) == r]
print(f"outer lift theta_D: fixed roots {len(fixed_theta)}, fixed Cartan dim 4 -> F4 (dim 52)  [B1296]")
# the T3 configuration under the inner lift: theta_G u = u for every u, so the parity lock's condition is vacuous on every direction;
# on u = omega_1^vee the (+,+) singular-frame content is 2 x (16 + 10 + 1) (B1296 T3) and it is now equivariant.
u = omega[0]
q27 = {}
for w in W27: q27[dot(w, u)] = q27.get(dot(w, u), 0) + 1
print("u = omega_1^vee: 27 charges", {str(k): v for k, v in sorted(q27.items())}, " (16 at 1/3, 10 at -2/3, 1 at 4/3 -- B1296 T3's two 16's, equivariant under the inner lift)")
ok = (len(fixed2) == 32 and sorted(types2) == ["A1", "A5"] and len(fixed3) == 18 and types3 == ["A2", "A2", "A2"])
json.dump(dict(inner2=dict(fixed=len(fixed2), type=types2), inner3=dict(fixed=len(fixed3), type=types3), outer=dict(fixed=len(fixed_theta))), open("b1298_inner_lift.json", "w"), indent=1)
print("P2:", "PASS" if ok else "FAIL")
