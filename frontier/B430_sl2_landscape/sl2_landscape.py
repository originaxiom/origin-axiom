"""B430 -- the sl2 landscape of the 27: fermionic content EXISTS but is UNFORCED.

Completes the delivered Chat-1 ask ("a different SL(2) in E6 might work -- identify and
compute"). Answer, exact:

  ROOT sl2 (the A1 class, e.g. a single-root sl2):  27 = 6 doublets (spin 1/2) + 15 singlets
    -- the standard A1 x A5 branching 27 = (2, 6bar) + (1, 15). SPINORIAL content exists.
  PRINCIPAL sl2 (the object's unique forced embedding): 27 = Sym^16 + Sym^8 + Sym^0 --
    all integer spin, bosonic (B428).

VERDICT (the three-part wall):
  (1) fermionic spin assignments exist in the sl2 landscape of e6 (root class: 6 spin-1/2
      doublets in the 27);
  (2) the object forces only the principal embedding (B428) -- every other sl2 is a CHOICE;
  (3) no first-order deformation of the object's E6 rep reaches any other sl2-factoring
      (B429, Whitehead rigidity).
  => the fermion door via sl2 choice is OPEN AS MATHEMATICS and CLOSED AS DERIVATION: it
  fails bar leg (i) FORCED. The landscape exists; the object does not point into it.

Criterion used (exact): for an sl2 with semisimple element h, the 27 carries half-integer
spin iff some weight mu has ODD mu(h). Principal: mu(h) = <mu, 2 rho^v> all even. Root sl2:
mu(alpha^v) in {-1, 0, +1} (minuscule), odd values present.

Firewall: Lie-theoretic branching. No physics claim; this bud PRICES the fermion door
(choice, not forcing). Prior art: the branchings are standard (flagged).
"""
import os, json
import sympy as sp
from collections import Counter

C = sp.Matrix([
    [ 2,  0, -1,  0,  0,  0], [ 0,  2,  0, -1,  0,  0], [-1,  0,  2, -1,  0,  0],
    [ 0, -1, -1,  2, -1,  0], [ 0,  0,  0, -1,  2, -1], [ 0,  0,  0,  0, -1,  2]])

def weights_27():
    hw = [1, 0, 0, 0, 0, 0]; seen = {tuple(hw)}; fr = [tuple(hw)]
    while fr:
        mu = fr.pop()
        for i in range(6):
            nu = [mu[j] - mu[i]*C[i, j] for j in range(6)]
            t = tuple(nu)
            if t not in seen: seen.add(t); fr.append(t)
    return list(seen)

def h_eigenvalues(dlabels):
    """eigenvalues of h (alpha_i(h) = d_i) on the 27."""
    CI = C.inv(); W = weights_27()
    wh = [sum(CI[i, j]*dlabels[j] for j in range(6)) for i in range(6)]
    return [int(sp.nsimplify(sum(mu[i]*wh[i] for i in range(6)))) for mu in W]

def root_sl2():
    """h = alpha_1^v: alpha_i(h) = Cartan row; 27 eigenvalues and content."""
    eig = h_eigenvalues([C[0, j] for j in range(6)])
    c = Counter(eig)
    return dict(eigs=dict(sorted(c.items())), doublets=c.get(1, 0), singlets=c.get(0, 0),
                spinorial=any(e % 2 for e in eig))

def principal_sl2():
    eig = h_eigenvalues([2]*6)
    return dict(all_even=all(e % 2 == 0 for e in eig))

if __name__ == "__main__":
    r = root_sl2(); p = principal_sl2()
    print("ROOT sl2:", r, " -> 27 = (2,6bar)+(1,15) under A1xA5: 6 spin-1/2 doublets EXIST")
    print("PRINCIPAL sl2 all-even (bosonic):", p["all_even"])
    json.dump(dict(root=r, principal=p),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sl2_landscape.json"), "w"),
              indent=1)
    print("[written] sl2_landscape.json")
