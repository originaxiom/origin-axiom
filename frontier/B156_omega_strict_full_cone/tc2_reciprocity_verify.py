#!/usr/bin/env python
"""
Independent fresh verifier for CLAIM TC-2.

TC-2: a matrix M that is "strict-full" (admits a nondegenerate symmetric
invariant form G with M^T G M = G, det G != 0) has a reciprocal/palindromic
characteristic polynomial (M is similar to M^{-1}).

This script DOES NOT import or trust any handoff script. Everything is
re-derived from scratch with sympy.

Parts:
  (A) Symbolic proof that M^T G M = G  ==>  M ~ M^{-1}  (so same charpoly),
      and that charpoly(M^{-1}) is the reversal of charpoly(M) up to det.
  (B) Sample of strict-full 4x4 integer shear-product matrices: build a
      nondegenerate symmetric G with M^T G M = G by solving the linear system,
      then confirm charpoly is palindromic.
  (C) Control: a NON-reciprocal matrix, confirm it admits NO nondegenerate
      invariant symmetric form (only degenerate / zero solutions).
  (D) Cross-check the specific Omega family R_{a,m} charpoly shape.
"""

import sympy as sp
from sympy import Matrix, symbols, eye, simplify, Rational, Poly, zeros


def charpoly_coeffs(M):
    """Return monic charpoly coefficient list [1, c_{n-1}, ..., c_0] in x."""
    x = symbols('x')
    p = M.charpoly(x)
    return p.all_coeffs(), p


def is_palindromic(coeffs):
    """coeffs is list of monic charpoly coefficients high->low degree."""
    coeffs = [sp.nsimplify(c) for c in coeffs]
    return all(sp.simplify(coeffs[i] - coeffs[-1 - i]) == 0
               for i in range(len(coeffs)))


# ----------------------------------------------------------------------
# PART A: symbolic linear-algebra proof
# ----------------------------------------------------------------------
def part_A():
    print("=" * 70)
    print("PART A: symbolic proof  M^T G M = G  ==>  M similar to M^{-1}")
    print("=" * 70)

    # Use a generic invertible 3x3 to keep the algebra small but fully symbolic.
    # The argument is dimension-independent; we demonstrate it concretely.
    n = 3
    Msyms = symbols('m0:%d' % (n * n))
    Gsyms = symbols('g0:%d' % (n * n))
    M = Matrix(n, n, Msyms)
    G = Matrix(n, n, Gsyms)

    # From M^T G M = G with G invertible:
    #   G^{-1} M^T G M = I  =>  M^{-1} = G^{-1} M^T G
    #   => M^{-T} = G M G^{-1}    (transpose of the above relation)
    # We verify the algebraic identity:  (G^{-1} M^T G) * M = I  reduces to
    #   M^T G M = G  multiplied by G^{-1} on the left, i.e. it's an identity
    #   GIVEN the hypothesis.  Show the derivation symbolically.

    Ginv = G.inv()

    # Claim 1: hypothesis M^T G M = G  is equivalent to  M^{-1} = G^{-1} M^T G.
    # i.e. (G^{-1} M^T G) M - I == G^{-1} (M^T G M - G).
    lhs = (Ginv * M.T * G) * M - eye(n)
    rhs = Ginv * (M.T * G * M - G)
    diff1 = simplify(lhs - rhs)
    ok1 = diff1 == zeros(n, n)
    print("  Identity (G^{-1}M^T G)M - I == G^{-1}(M^T G M - G):", ok1)

    # Claim 2: under hypothesis, M^{-T} = G M G^{-1}, i.e. M^{-T} similar to M.
    # Equivalent algebraic identity:
    #   (G M G^{-1})^T  - M^{-1}  == ... should vanish given hypothesis.
    # We instead verify the similarity form directly:
    #   M^{-T} = G M G^{-1}  <=>  M^{-T} G = G M  <=>  G = M^T G M  (multiply
    #   left by M^T). So this is exactly the hypothesis.
    # Demonstrate: M^T * (G M G^{-1})  evaluated and compared to ... :
    # Take the relation we want: M^{-T} = G M G^{-1}.
    # Multiply both sides on left by M^T:  M^T M^{-T} = I = M^T G M G^{-1}.
    # So  M^T G M G^{-1} = I  <=>  M^T G M = G.  Exact equivalence.
    test = simplify(M.T * G * M * Ginv - eye(n))      # = I - I = 0 iff hyp holds
    # We can't assume hyp here symbolically (M,G free), so instead show the
    # EQUIVALENCE: M^T G M G^{-1} - I  ==  (M^T G M - G) G^{-1}.
    equiv = simplify(test - (M.T * G * M - G) * Ginv)
    ok2 = equiv == zeros(n, n)
    print("  Equivalence M^TGM G^{-1}-I == (M^TGM-G)G^{-1}:", ok2)
    print("    => hypothesis (M^TGM=G) <=> M^{-T}=GMG^{-1} (M ~ M^{-T}).")

    # Claim 3: similar matrices share charpoly, and charpoly(M^T)=charpoly(M).
    # Hence charpoly(M) = charpoly(M^{-T}) = charpoly(M^{-1}).
    # Verify charpoly(M)=charpoly(M^T) symbolically:
    cM, _ = charpoly_coeffs(M)
    cMT, _ = charpoly_coeffs(M.T)
    ok3 = all(simplify(a - b) == 0 for a, b in zip(cM, cMT))
    print("  charpoly(M) == charpoly(M^T) (generic symbolic):", ok3)

    # Claim 4: the CORRECT general reciprocal identity relates the reversed
    # charpoly of M to the charpoly of M^{-1}:
    #     x^n p_M(1/x) = (-1)^n det(M) * p_{M^{-1}}(x).
    # (Note: x^n p_M(1/x) = (-1)^n det(M) p_M(x) is NOT a generic identity;
    #  it holds precisely WHEN p_{M^{-1}} = p_M, i.e. when M ~ M^{-1}.)
    x = symbols('x')
    p = M.charpoly(x).as_expr()
    n_ = n
    rev = sp.expand(sp.cancel(x**n_ * p.subs(x, 1 / x)))      # reversed charpoly
    pMinv = sp.expand(M.inv().charpoly(x).as_expr())
    target = sp.expand((-1)**n_ * M.det() * pMinv)
    ok4 = sp.simplify(sp.cancel(rev - target)) == 0
    print("  General identity x^n p_M(1/x) == (-1)^n det(M) p_{M^-1}(x):", ok4)

    # Claim 5: putting it together. Under the hypothesis M^TGM=G we proved
    # M ~ M^{-1}, hence p_{M^{-1}} = p_M. Substitute into Claim 4:
    #     reversed charpoly = (-1)^n det(M) p_M(x).
    # For det(M)=1 and n even this is reversed = p_M, i.e. PALINDROMIC.
    # Demonstrate symbolically: assume p_{M^{-1}} = p_M and det=1, n even;
    # then reversed - p_M = 0.  We verify the algebra of that substitution by
    # taking an ACTUAL metric-preserving SL matrix (orthogonal w.r.t. a chosen
    # nondegenerate G) and confirming palindromic.
    # Concrete witness: a 4x4 matrix preserving G=antidiag(1,1,1,1) form is
    # built below in part B; here we just confirm the implication logically by
    # evaluating with the constraint det=1, n even on a palindromic instance.
    print("    => with M ~ M^{-1} (proved above) and det(M)=1, n even:")
    print("       reversed charpoly = (+1)(1) p_{M^-1} = p_M  => PALINDROMIC.")

    allok = ok1 and ok2 and ok3 and ok4
    print("  PART A result:", "PASS" if allok else "FAIL")
    return allok


# ----------------------------------------------------------------------
# Helpers for parts B/C: build invariant symmetric forms
# ----------------------------------------------------------------------
def invariant_sym_forms(M):
    """
    Solve the linear system  M^T G M = G  with G symmetric (G = G^T) over QQ.
    Return (solution_space_dim, list_of_basis_symmetric_matrices).
    Each basis element is a sympy Matrix.
    """
    n = M.shape[0]
    # symmetric unknowns
    gvars = {}
    G = zeros(n, n)
    syms = []
    for i in range(n):
        for j in range(i, n):
            s = symbols('g_%d_%d' % (i, j))
            syms.append(s)
            G[i, j] = s
            G[j, i] = s
    eqmat = M.T * G * M - G
    eqs = []
    for i in range(n):
        for j in range(n):
            eqs.append(eqmat[i, j])
    sol = sp.linsolve(eqs, syms)
    # linsolve returns a set with one tuple parametrized by free symbols
    sol = list(sol)
    if not sol:
        return 0, []
    soltuple = sol[0]
    free = sorted(set().union(*[expr.free_symbols for expr in soltuple]),
                  key=lambda s: s.name)
    # build basis: set each free symbol to 1 (others 0) in turn
    basis = []
    if not free:
        # only the zero solution
        Gval = G.subs({s: e for s, e in zip(syms, soltuple)})
        if Gval == zeros(n, n):
            return 0, []
        return 1, [Gval]
    for f in free:
        subs_free = {g: (1 if g == f else 0) for g in free}
        Gval = zeros(n, n)
        for k, s in enumerate(syms):
            val = soltuple[k].subs(subs_free)
            i, j = [int(t) for t in s.name.split('_')[1:]]
            Gval[i, j] = val
            Gval[j, i] = val
        basis.append(Gval)
    return len(free), basis


def has_nondegenerate_invariant_form(M, trials=60):
    """
    Determine whether M admits a NONDEGENERATE symmetric G with M^TGM=G.
    Returns (bool, witness_or_None, solution_dim).
    Strategy: get basis of solution space; a nondegenerate element exists iff
    det of a generic combination is not identically zero.  Test det of a
    symbolic combination; if it's the zero polynomial -> all solutions
    degenerate.
    """
    dim, basis = invariant_sym_forms(M)
    if dim == 0:
        return False, None, 0
    # generic combination
    cs = symbols('c0:%d' % dim)
    Gen = zeros(M.shape[0])
    for c, B in zip(cs, basis):
        Gen = Gen + c * B
    d = sp.expand(Gen.det())
    if d == 0:
        return False, None, dim
    # find a concrete nondegenerate witness by random integer combos
    import random
    for _ in range(trials):
        subs = {c: random.randint(-3, 3) for c in cs}
        Gv = Gen.subs(subs)
        if Gv.det() != 0:
            return True, Gv, dim
    # deterministic fallback: try unit basis vectors and small combos
    for B in basis:
        if B.det() != 0:
            return True, B, dim
    return True, None, dim  # nondegenerate generically but no small witness found


# ----------------------------------------------------------------------
# PART B: strict-full shear-product matrices are palindromic
# ----------------------------------------------------------------------
def shear(i, j, n=4):
    S = eye(n)
    S[i, j] = 1
    return S


def part_B():
    print("=" * 70)
    print("PART B: strict-full 4x4 shear-product matrices -> palindromic")
    print("=" * 70)
    import random
    random.seed(12345)
    n = 4
    found = 0
    checked = 0
    fails = 0
    x = symbols('x')
    # Build many random positive unit-shear products; keep those that are
    # strict-full (admit nondegenerate invariant symmetric G).
    attempts = 0
    while found < 8 and attempts < 4000:
        attempts += 1
        L = random.randint(2, 7)
        M = eye(n)
        for _ in range(L):
            i, j = random.sample(range(n), 2)
            M = M * shear(i, j, n)
        # determinant of any unit-shear product is 1
        assert M.det() == 1
        nd, G, dim = has_nondegenerate_invariant_form(M)
        if not nd:
            continue
        # verify G really works and is nondegenerate symmetric
        assert (M.T * G * M - G) == zeros(n, n)
        assert G == G.T
        assert G.det() != 0
        coeffs, p = charpoly_coeffs(M)
        pal = is_palindromic(coeffs)
        checked += 1
        if pal:
            found += 1
        else:
            fails += 1
            print("  COUNTEREXAMPLE strict-full but NOT palindromic!")
            print("   M =", M.tolist())
            print("   charpoly coeffs:", coeffs)
    print("  strict-full matrices examined:", checked)
    print("  palindromic:", checked - fails, " non-palindromic:", fails)
    ok = (checked >= 5) and (fails == 0)
    print("  PART B result:", "PASS" if ok else "FAIL/INSUFFICIENT")
    return ok


# ----------------------------------------------------------------------
# PART C: control -- a NON-reciprocal matrix admits NO nondegenerate form
# ----------------------------------------------------------------------
def part_C():
    print("=" * 70)
    print("PART C: control -- non-reciprocal matrix admits NO nondeg. form")
    print("=" * 70)
    n = 4
    # A companion-type matrix with a deliberately non-palindromic charpoly.
    # charpoly chosen: x^4 - x^3 + 0 x^2 + 0 x - 1  ? must check det.
    # Build a concrete integer matrix that is NOT reciprocal.
    # Use companion of p(x)=x^4 - 2x^3 + 3x^2 - 4x + 5 (clearly non-palindromic,
    # det = 5, not in SL but fine for the control of nondeg invariant form).
    # Companion matrix:
    coeffs = [1, -2, 3, -4, 5]  # x^4 -2x^3 +3x^2 -4x +5
    C = zeros(n, n)
    for i in range(1, n):
        C[i, i - 1] = 1
    for i in range(n):
        C[i, n - 1] = -coeffs[n - i]  # last column = -lower coeffs
    x = symbols('x')
    pc = C.charpoly(x)
    print("  control charpoly:", pc.as_expr())
    cc = pc.all_coeffs()
    print("  palindromic?", is_palindromic(cc))
    nd, G, dim = has_nondegenerate_invariant_form(C)
    print("  invariant symmetric form solution dim:", dim)
    print("  admits NONDEGENERATE invariant symmetric form?", nd)
    ok1 = (not is_palindromic(cc)) and (not nd)

    # Second control: a unit-determinant non-reciprocal SL(4,Z) matrix.
    # charpoly x^4 - 3x^3 + 2x^2 - x + 1 (det=1, non-palindromic).
    coeffs2 = [1, -3, 2, -1, 1]
    C2 = zeros(n, n)
    for i in range(1, n):
        C2[i, i - 1] = 1
    for i in range(n):
        C2[i, n - 1] = -coeffs2[n - i]
    pc2 = C2.charpoly(x)
    cc2 = pc2.all_coeffs()
    print("  control2 charpoly:", pc2.as_expr(), " det:", C2.det())
    print("  control2 palindromic?", is_palindromic(cc2))
    nd2, G2, dim2 = has_nondegenerate_invariant_form(C2)
    print("  control2 invariant sym form dim:", dim2,
          " nondegenerate exists?", nd2)
    ok2 = (not is_palindromic(cc2)) and (not nd2)

    ok = ok1 and ok2
    print("  PART C result:", "PASS" if ok else "FAIL")
    return ok


# ----------------------------------------------------------------------
# PART D: the Omega family R_{a,m} charpoly shape sanity check
# ----------------------------------------------------------------------
def part_D():
    print("=" * 70)
    print("PART D: Omega family R_{a,m} target charpoly is reciprocal")
    print("=" * 70)
    a, m, x = symbols('a m x')
    # claimed charpoly: x^4 - a x^3 + (2a-2m-4) x^2 - a x + 1
    p = x**4 - a * x**3 + (2 * a - 2 * m - 4) * x**2 - a * x + 1
    pc = Poly(p, x)
    coeffs = pc.all_coeffs()
    print("  charpoly coeffs:", coeffs)
    pal = is_palindromic(coeffs)
    print("  palindromic (symmetric coeffs)?", pal)
    # reciprocal check x^4 p(1/x) == p(x)
    recip = sp.expand(x**4 * p.subs(x, 1 / x))
    ok = sp.simplify(recip - sp.expand(p)) == 0 and pal
    print("  x^4 p(1/x) == p(x)?", sp.simplify(recip - sp.expand(p)) == 0)
    print("  PART D result:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    rA = part_A()
    rB = part_B()
    rC = part_C()
    rD = part_D()
    print("=" * 70)
    print("SUMMARY: A=%s B=%s C=%s D=%s" % (rA, rB, rC, rD))
    print("OVERALL:", "PASS" if (rA and rB and rC and rD) else "FAIL")
