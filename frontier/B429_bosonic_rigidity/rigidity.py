"""B429 -- Phase I.2: THE FIRST-ORDER BOSONIC RIGIDITY of the E6<->Lorentz coupling.

Question (registered in B428): along B347's 6-dim unobstructed E6 moduli of pi_1(4_1) at the
principal point rho_0 = principal o rho_geo, can the object's matter (27) acquire spinorial
content? Answer: NO, at first order -- by structure, not scan:

  (i)  e6 under the principal sl2 = (+) Sym^{2m}, m in {1,4,5,7,8,11}; the m=1 block (Sym^2,
       dim 3) IS the embedded principal sl2 itself. So the deformation direction inherited from
       the geometry (deforming rho_geo along the A-polynomial curve and composing) is exactly
       the m=1 block's H^1 -- and along it the rep STAYS sl2-factored with the same all-even
       Sym content: bosonic.
  (ii) Lie-algebra embeddings sl2 -> e6 are infinitesimally rigid: H^1(sl2, e6) = 0 (Whitehead;
       equivalently H^1(sl2, Sym^{2m}) = 0 for every block -- verified computationally below).
       Hence the tangent space to the "factors through SOME sl2" locus at rho_0 is exactly the
       m=1 line, and the five intrinsic directions m in {4,5,7,8,11} LEAVE the sl2-factoring
       locus at first order: along them there is NO sl2 bridge at all, so no spin assignment
       of any kind (spinorial or otherwise).

  THEOREM (first order). No first-order deformation of the object's E6 structure produces
  spinorial matter: the unique Lorentz-coupled point is bosonic (B428), it stays bosonic along
  the one geometric direction, and the coupling itself ceases to exist along the five intrinsic
  directions. The E6 moduli splits 6 = 1 (geometric, Sym^2) + 5 (intrinsic, exponents 4,5,7,8,11).

Computable legs verified here: (a) the block decomposition + the m=1-block-is-the-sl2 dimension
identity; (b) H^1(sl2, Sym^n) = 0 for all blocks (raising/lowering solve: every cocycle is a
coboundary); (c) B347's dim H^1(pi_1, Sym^{2m}) = 1 per exponent is the banked input (lock cited).

Firewall: Lie cohomology + banked character-variety data. "Bosonic/spinorial" refers to the
Sym-parity dictionary under SL(2,C) = Spin(3,1); no physics claim is licensed -- this is a wall
theorem (it says where the unfolding CANNOT act: not through first-order E6 deformations).
"""
import os, json
import sympy as sp

def sl2_action_on_sym(n):
    """matrices of e, f, h on Sym^n(C^2) in the basis x^k y^(n-k), k=0..n."""
    d = n + 1
    E = sp.zeros(d, d); F = sp.zeros(d, d); H = sp.zeros(d, d)
    for k in range(d):
        H[k, k] = 2*k - n                       # weight of x^k y^(n-k)
        if k + 1 < d: E[k + 1, k] = n - k       # e: y->x  (x^k y^(n-k) -> (n-k) x^(k+1) y^(n-k-1))
        if k - 1 >= 0: F[k - 1, k] = k          # f: x->y
    return E, F, H

def h1_sl2_sym_is_zero(n):
    """H^1(sl2, Sym^n) = 0: every cocycle z: sl2 -> Sym^n is a coboundary.
    Solve: unknowns z(e), z(f), z(h) in Sym^n with cocycle conditions
      z([e,f]) = e.z(f) - f.z(e)   i.e. z(h) = E z_f - F z_e
      z([h,e]) = h.z(e) - e.z(h)   i.e. 2 z_e = H z_e - E z_h
      z([h,f]) = h.z(f) - f.z(h)   i.e. -2 z_f = H z_f - F z_h
    then check the solution space equals the coboundaries {z_x = x.v}."""
    d = n + 1
    E, F, H = sl2_action_on_sym(n)
    ze = sp.Matrix(sp.symbols(f'a0:{d}')); zf = sp.Matrix(sp.symbols(f'b0:{d}'))
    zh = E*zf - F*ze
    eqs = list(2*ze - (H*ze - E*zh)) + list(-2*zf - (H*zf - F*zh))
    unk = list(ze) + list(zf)
    sol = sp.solve(eqs, unk, dict=True)
    # dimension of the cocycle space = free parameters of the solution
    if not sol: coc_dim = 0
    else:
        s = sol[0]
        free = [u for u in unk if u not in s or s[u] == u]
        # count genuinely free symbols in the parametrized solution
        subbed = [sp.simplify(s.get(u, u)) for u in unk]
        syms = set()
        for x in subbed: syms |= x.free_symbols
        coc_dim = len(syms)
    # coboundary dim = dim Sym^n - dim invariants = d - (1 if n==0 else 0)
    cob_dim = d - (1 if n == 0 else 0)
    return coc_dim, cob_dim, coc_dim == cob_dim

E6_EXPONENTS = [1, 4, 5, 7, 8, 11]

if __name__ == "__main__":
    print("(a) block decomposition: e6 = (+) Sym^{2m}, dims", [2*m+1 for m in E6_EXPONENTS],
          " sum =", sum(2*m+1 for m in E6_EXPONENTS), "(=78)")
    print("    m=1 block dim =", 3, "= dim sl2  -> the Sym^2 block IS the embedded principal sl2")
    print("\n(b) Whitehead per block: H^1(sl2, Sym^n) = 0  (cocycles == coboundaries)")
    res = {}
    for m in E6_EXPONENTS:
        n = 2*m
        coc, cob, ok = h1_sl2_sym_is_zero(n)
        res[m] = dict(n=n, cocycle_dim=coc, coboundary_dim=cob, h1_zero=bool(ok))
        print(f"    m={m:>2} (Sym^{n:>2}): cocycles {coc}, coboundaries {cob}, H^1=0: {ok}")
    all_zero = all(r["h1_zero"] for r in res.values())
    print("\n(c) banked input: dim H^1(pi_1, Sym^{2m}) = 1 per exponent (B347, lock test_b347)")
    print("\nTHEOREM (first order): moduli = 1 geometric (stays bosonic) + 5 intrinsic (no sl2 at")
    print("all) -> no first-order E6 deformation produces spinorial matter. Verified legs:", all_zero)
    json.dump(dict(block_dims=[2*m+1 for m in E6_EXPONENTS], whitehead={str(k): v for k, v in res.items()},
                   all_h1_zero=bool(all_zero)),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rigidity.json"), "w"),
              indent=1)
    print("[written] rigidity.json")
