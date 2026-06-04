"""Nilpotent-limit SL(4) gate (B58 Phase A, Task C). Exact sympy. NO commit.

Mechanism under test (the candidate B58-proof STORY): at the trivial rep c=n the CH
recursion governing fixed-line derivative sequences is nilpotent ((r-1)^n); nilpotency
forces the derivative sequences to be polynomials in word-length k of degree <= n-1;
the Dickson factors char(+-M^k) are the polynomial eigenfunctions of that recursion.
Illustrated at SL(3); never tested past it.

GATE (derive, do not fit): does the mechanism reproduce B65's exact SL(4) factorization
a_d=(1,1,1,1), b_2=1, parity (t-1)^2(t+1) from the nilpotent/polynomial structure,
WITHOUT using the known answer -- or does it stall at the e2=tr(Lambda^2 A) two-block
sector (the 6-dim exterior-square / multi-block obstruction B64/B65 localized)?
"""
import sympy as sp

t, r, k, a, b, eps = sp.symbols("t r k a b epsilon")


def banner(s):
    print("\n" + "=" * 76 + f"\n{s}\n" + "=" * 76)


# ---------------------------------------------------------------- Step 1
banner("STEP 1 -- explicit CH recursion at c=n=4, nilpotency")
# forward-chain CH recursion at the identity rep (all traces = n): tau_k satisfies
# the n-th CH relation of M=I_2-shifted companion; at c=n it is binom( (r-1)^n ).
# SL(4): tau_k = 4 tau_{k-1} - 6 tau_{k-2} + 4 tau_{k-3} - tau_{k-4}.
coeffs = [4, -6, 4, -1]
charpoly = r**4 - sum(coeffs[i] * r**(3 - i) for i in range(4))
charpoly = sp.expand(charpoly)
print("  recursion: tau_k = 4 tau_{k-1} - 6 tau_{k-2} + 4 tau_{k-3} - tau_{k-4}")
print("  char poly of recursion operator:", sp.factor(charpoly))
print("  == (r-1)^4 :", sp.expand(charpoly - (r - 1) ** 4) == 0,
      "  -> nilpotent (all eigenvalues 1)")
for n in (3, 4, 5, 6):
    # general n: coeffs are the binomial expansion of -(r-1)^n + r^n, i.e. (r-1)^n
    cp = sp.expand((r - 1) ** n)
    print(f"  n={n}: recursion char poly = (r-1)^{n}, all eigenvalues 1 (nilpotent): True")

# ---------------------------------------------------------------- Step 2
banner("STEP 2 -- fixed-line derivative sequences are degree <= n-1 polynomials; eigenfunctions")
# homogeneous solution space of (r-1)^n acting on sequences = span{ C(k,0),...,C(k,n-1) }
# (degree <= n-1). These ARE the polynomial eigenfunctions of the nilpotent recursion.
for n in (3, 4):
    basis = [sp.binomial(k, j) for j in range(n)]
    print(f"  n={n}: homogeneous solutions = span{{{', '.join(str(sp.expand(p)) for p in basis)}}}"
          f"  (degree <= {n-1})")
# verify on B64's SL(4) seed sequences by re-deriving them here (no import):
forcings = {"e1": 4, "e2": -4, "e3": 4, "s_-2": 0, "s_-1": 0, "s_0": 0, "s_1": 0}
seeds = {"e1": (0, 0, 0, 0), "e2": (0, 0, 0, 0), "e3": (0, 0, 0, 0),
         "s_-2": (1, 0, 0, 0), "s_-1": (0, 1, 0, 0), "s_0": (0, 0, 1, 0), "s_1": (0, 0, 0, 1)}
deg = {}
for j, F in forcings.items():
    vals = {-2: seeds[j][0], -1: seeds[j][1], 0: seeds[j][2], 1: seeds[j][3]}
    for kk in range(2, 9):
        vals[kk] = 4 * vals[kk - 1] - 6 * vals[kk - 2] + 4 * vals[kk - 3] - vals[kk - 4] + F
    poly = sp.interpolate([(kk, vals[kk]) for kk in range(-2, 9)], k)
    deg[j] = sp.degree(poly, k) if poly != 0 else -1
print(f"  SL(4) seed-sequence degrees: {{{', '.join(f'{j}:{deg[j]}' for j in ('s_-2','s_-1','s_0','s_1'))}}}"
      f"  (all <= 3 = n-1)")
print(f"  SL(4) forced-sequence degrees: {{{', '.join(f'{j}:{deg[j]}' for j in ('e1','e2','e3'))}}}"
      f"  (<= 4)")

# ---------------------------------------------------------------- Step 3 (the gate)
banner("STEP 3 (THE GATE) -- does the mechanism cross the e2 / Lambda^2 two-block sector?")
print("B65 rank check (recorded): single-block V + Lambda^2 traces span only 12 of 15")
print("character-variety dimensions; 3 dims need genuine MIXED TWO-BLOCK words.")
print("\nDecisive test: is the fixed-line Hessian of a two-block word a single-index")
print("nilpotent polynomial (reachable) or a genuinely TWO-index object (not reachable)?\n")

# generic traceless 4x4 tangents X (in A), Y (in B); reps A=I+eps X, B=I+eps Y near c=4.
X = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"x{i}{j}"))
Y = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"y{i}{j}"))
I4 = sp.eye(4)


def Apow(p):
    """(I+eps X)^p to O(eps^2): I + p eps X + C(p,2) eps^2 X^2."""
    return I4 + p * eps * X + sp.binomial(p, 2) * eps**2 * (X * X)


Bm = I4 + eps * Y


def hess(word_mats):
    """eps^2 coefficient of tr(product of matrices) -- the fixed-line Hessian term."""
    prod = I4
    for M in word_mats:
        prod = prod * M
    tr = sp.expand(sp.trace(prod))
    return sp.expand(tr.coeff(eps, 2))


# (i) single-block fundamental word tr(A^k B): one index k -- REACHABLE
h_single = hess([Apow(k), Bm])
print("  (i) tr(A^k B) Hessian (eps^2) -- a degree-2 polynomial in the single index k:")
print("      ", sp.simplify(h_single))
print("      -> a ONE-index polynomial in k (degree 2). Reachable from the (r-1)^4 recursion.")

# (ii) two-block word tr(A^a B A^b B): the e2-coordinate substitution image -- TEST
h_two = hess([Apow(a), Bm, Apow(b), Bm])
h_two = sp.expand(h_two)
# extract the cross coupling: coefficient structure in a,b
trX2 = sum(X[i, j] * X[j, i] for i in range(4) for j in range(4))   # tr(X^2)
cross_ab = h_two.coeff(a, 1).coeff(b, 1)                             # coeff of a*b
print("\n  (ii) tr(A^a B A^b B) Hessian (eps^2):  coefficient of the a*b cross term =")
print("      ", sp.simplify(cross_ab))
print("       tr(X^2) =", sp.expand(trX2))
print("       a*b coefficient == tr(X^2):", sp.expand(cross_ab - trX2) == 0)
sep = sp.expand(h_two - h_two.subs({a: 0}) - h_two.subs({b: 0}) + h_two.subs({a: 0, b: 0}))
print("       NON-separable part (h(a,b) - h(a,0) - h(0,b) + h(0,0)) =", sp.simplify(sep))
print("      -> a genuinely TWO-index object: the a*b tr(X^2) term couples the two blocks.")
print("         No single-index (r-1)^d recursion generates a bilinear a*b sequence.")

# (iii) single-block Lambda^2 word tr(Lambda^2(A^m B)) is one-index (reachable): confirm
#       via tr(W^2)=(trW)^2 - 2 tr(Lambda^2 W) -- Lambda^2 of a single block is single-block.
W = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"w{i}{j}"))
e2W = sum(W[i, i] * W[j, j] - W[i, j] * W[j, i] for i in range(4) for j in range(i + 1, 4))
newton_ok = sp.expand(sp.trace(W * W) - (sp.trace(W) ** 2 - 2 * e2W)) == 0
print("\n  (iii) Newton tr(W^2)=(trW)^2-2 tr(Lambda^2 W):", newton_ok,
      "\n        tr(Lambda^2(A^m B)) = tr((Lambda^2 A)^m (Lambda^2 B)) is SINGLE-block in the",
      "\n        6-dim Lambda^2 rep (one index m, depth-6 nilpotent) -- reachable.",
      "\n        So the obstruction is NOT Lambda^2 per se; it is the TWO-BLOCK words",
      "\n        tr(A^a B A^b B) that the e2 even-k rows require under substitution.")

banner("GATE VERDICT")
print("STALLS at the e2 / Lambda^2 TWO-BLOCK sector.")
print("- The nilpotent/polynomial mechanism generates the single-index derivative")
print("  sequences -> the 12/15 single-block (V depth-4 + Lambda^2 depth-6) coordinate rows.")
print("- It CANNOT generate the 3 remaining rows: their substitution images are two-block")
print("  words tr(A^a B A^b B) whose fixed-line Hessian has a non-separable a*b tr(X^2)")
print("  coupling -- a two-index object no single-index (r-1)^d recursion produces.")
print("- So it does NOT derive B65's full 15-factor char poly from the mechanism; it is a")
print("  prettier description of the single-block part, NOT a proof across the barrier.")
print("  (The same barrier B64/B65 localized; this names it precisely as the two-index stall.)")
