"""B428 -- the two upstairs spin walls, cross-validated (three seats agree): the E6 floor gives
ANYONS not fermions, and the principal sl2 makes ALL E6 content integer-spin (bosonic).

Wall 1 (E6 level-1 modular data, from the Cartan matrix -- no memory, no parameters):
  integrable weights at level 1: {0, w1, w6} (3 objects, torus Verlinde dim 3);
  h(27) = <w1, w1+2rho>/(2(1+12)) = 2/3  => twist theta = e^{4 pi i/3}, a Z/3 ANYON.
  NO object has theta = -1: zero fermions at level 1. (Chat-2 prereg CONFIRMED; matches the
  in-session E6 TQFT computation; the modular data itself is standard prior art -- flagged.)

Wall 2 (the principal sl2 in E6, the unique embedding the object supplies for free):
  27 = Sym^16 + Sym^8 + Sym^0   (dims [17, 9, 1]; spins 8, 4, 0)   -- ALL INTEGER SPIN
  78 = + Sym^{2m}, m in {1,4,5,7,8,11}                             -- ALL INTEGER SPIN
  Under SL(2,C) = Spin(3,1), integer spin = tensorial = bosonic. The canonical bridge
  rho = principal o rho_geo gives matter (27) NO spinorial content: the spin-statistics
  coupling via the only forced sl2 is bosonic-only. (Chat-2's weight-poset route agrees with
  the in-session Weyl-orbit route -- two independent methods, same [17,9,1].)

Consequence for the spacetime chain (the honest disposition, three seats aligned):
  steps 1-4 (holonomy = Spin(3,1), H^3 = mass shell) are true group theory but fail the
  CONTROL leg of the bar (every hyperbolic 3-manifold has them); step 5 (the E6<->Lorentz
  spin coupling) FAILS for the principal sl2. The open computation: the actual relationship
  between the E6 rep and rho_geo as reps of the one pi_1 (the character-variety map) --
  the registered next interface target.

Firewall: Lie-theoretic branching + modular-category arithmetic. Anyons are 2+1d exchange
statistics, not 3+1d spin. No physics claim licensed.
"""
import os, json
import sympy as sp

# E6 Cartan matrix (Bourbaki: chain 1-3-4-5-6, node 2 on 4)
C = sp.Matrix([
    [ 2,  0, -1,  0,  0,  0],
    [ 0,  2,  0, -1,  0,  0],
    [-1,  0,  2, -1,  0,  0],
    [ 0, -1, -1,  2, -1,  0],
    [ 0,  0,  0, -1,  2, -1],
    [ 0,  0,  0,  0, -1,  2]])
CI = C.inv()                       # <w_i, w_j> (simply laced, alpha^2 = 2)
MARKS = [1, 2, 2, 3, 2, 1]         # highest-root marks; h^v = 12
HV = 12

def level1_modular_data():
    """integrable weights at level 1 and their conformal weights h = <l, l+2rho>/(2(k+12))."""
    out = []
    # dominant weights n (Dynkin labels) with sum(marks*n) <= 1: 0, e1, e6
    for n in ([0]*6, [1,0,0,0,0,0], [0,0,0,0,0,1]):
        nv = sp.Matrix(n)
        norm = (nv.T * CI * nv)[0]                          # <l,l>
        rho_pair = sum(CI.row(i)[j]*n[i] for i in range(6) for j in range(6))  # <l, 2rho>/1? see below
        # <l, 2rho> = 2<l, rho> = 2 * sum_j (CI n)_j  (rho = sum w_j)
        l_rho2 = 2*sum((CI*nv)[j] for j in range(6))
        h = sp.Rational(sp.nsimplify(norm + l_rho2), 2*(1 + HV))
        out.append((tuple(n), sp.nsimplify(h)))
    return out

def principal_grades_27():
    """the 27's principal-sl2 decomposition via the minuscule Weyl orbit (independent of the
    weight-poset route): heights <mu, rho^v> over the orbit, peeled into Sym blocks."""
    r = [sum(CI.row(j)) for j in range(6)]                  # principal height of w_j
    hw = [1, 0, 0, 0, 0, 0]
    seen = {tuple(hw)}; frontier = [tuple(hw)]
    while frontier:
        mu = frontier.pop()
        for i in range(6):
            nu = [mu[j] - mu[i]*C[i, j] for j in range(6)]
            t = tuple(nu)
            if t not in seen:
                seen.add(t); frontier.append(t)
    heights = {}
    for mu in seen:
        h = sp.nsimplify(sum(mu[j]*r[j] for j in range(6)))
        heights[h] = heights.get(h, 0) + 1
    hs = dict(heights); tops = []
    while hs:
        top = max(hs)
        for w in range(int(-top), int(top) + 1):
            k = sp.Integer(w)
            hs[k] -= 1
            if hs[k] == 0: del hs[k]
        tops.append(int(top))
    return sorted([2*t + 1 for t in tops], reverse=True)    # dims of the Sym blocks

if __name__ == "__main__":
    md = level1_modular_data()
    print("E6 level-1 primaries (weight, h):", [(w, str(h)) for w, h in md])
    hs = [h for _, h in md]
    print("  any fermion (h = 1/2 mod 1, theta = -1)?", any(sp.nsimplify(h - sp.Rational(1,2)) == int(h - sp.Rational(1,2)) for h in hs if h != 0))
    dims = principal_grades_27()
    print("27 under principal sl2, Sym-block dims:", dims, " [claim [17,9,1] = spins 8,4,0, all integer]")
    json.dump(dict(level1=[(list(w), str(h)) for w, h in md],
                   dims_27=dims, all_odd_dims=bool(all(d % 2 == 1 for d in dims))),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "spin_walls.json"), "w"),
              indent=1)
    print("[written] spin_walls.json")
