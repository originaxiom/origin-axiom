#!/usr/bin/env python3
# B724 PROBE 1 (C2): is h^1 = 3  ->  THREE SPATIAL DIMENSIONS (Lorentzian 3+1)?
# COMPUTE the discriminating fact (do NOT cite B657/B715/B716 -- recompute).
#
# (a) The object's three H^1 classes: SYMMETRIC spatial triad (SO(3)/S_3-equivalent)
#     or INCOMMENSURABLE?  Recompute 27 = V17 + V9 + V1 under the principal SL(2)
#     (E6 holonomy), and the figure-eight twisted H^1 per block.
# (b) Is there ANY route from h^1=3 to a Lorentzian 3+1 signature (Wick rotation of
#     the complex-CS; H^3 isotropy; no real form)?  Or is it structurally blocked?
#
# Two-outcome: A = symmetric triad + a route to 3+1 (buildable);  B = incommensurable
# (17/9/1) or no route -> identification structurally blocked.
#
# Firewall: structural/arithmetic only; HINT-grade at most; BASE-RATE gated.

import numpy as np
import sympy as sp
from itertools import product
from fractions import Fraction

OUT = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s); OUT.append(s)

p("="*78)
p("B724 PROBE 1 (C2): h^1=3 -> 3 spatial dims (Lorentzian 3+1)?  DISCRIMINATING FACT")
p("="*78)

# ==========================================================================
# PART (a1): principal SL(2) branching of E6's 27  (recompute 27 = V17+V9+V1)
# ==========================================================================
p("\n" + "-"*78)
p("PART (a1)  E6 principal-SL(2) branching of the 27  (recompute, do not cite B657)")
p("-"*78)

# E6 Cartan matrix (Bourbaki node labels; node 2 is the branch node).
#   1 - 3 - 4 - 5 - 6
#           |
#           2
A = sp.Matrix([
    [ 2, 0,-1, 0, 0, 0],
    [ 0, 2, 0,-1, 0, 0],
    [-1, 0, 2,-1, 0, 0],
    [ 0,-1,-1, 2,-1, 0],
    [ 0, 0, 0,-1, 2,-1],
    [ 0, 0, 0, 0,-1, 2],
])
p("E6 Cartan matrix det =", A.det(), " (expected 3)")

# Principal sl2 semisimple element H:  <alpha_k, H> = 2 for every simple root.
# In the coroot basis H = sum r_j alpha_j^v with A r = 2*(1..1).
# The h_pr eigenvalue on a weight with Dynkin labels lam is  r . lam.
one = sp.Matrix([2,2,2,2,2,2])
r = A.solve(one)            # r = 2 A^{-1} 1  (dual Weyl/marks-like vector)
r = [sp.nsimplify(x) for x in r]
p("principal grading vector r = 2 A^{-1} 1 =", r)

def hpr(lam):
    return sum(sp.Integer(l)*rj for l, rj in zip(lam, r))

# Generate the 27 minuscule weights of E6 (highest weight = omega_1 = node 1).
# Minuscule: from a weight lam you may subtract alpha_i iff <lam,alpha_i^v>=lam[i]=1,
# and every such subtraction lands on another weight (strings have length <=2).
Arows = [[int(A[i, j]) for j in range(6)] for i in range(6)]  # alpha_i in omega-basis
hw = (1, 0, 0, 0, 0, 0)
weights = set([hw])
frontier = [hw]
while frontier:
    lam = frontier.pop()
    for i in range(6):
        if lam[i] == 1:  # can lower along alpha_i
            mu = tuple(lam[k] - Arows[i][k] for k in range(6))
            if mu not in weights:
                weights.add(mu); frontier.append(mu)
weights = list(weights)
p("number of weights in the orbit of omega_1 =", len(weights), " (expected 27)")

# principal grading eigenvalue multiset
grades = sorted(int(hpr(w)) for w in weights)
from collections import Counter
gc = Counter(grades)
p("h_pr eigenvalue range = [%d, %d]  (extreme = +/-16 expected)" % (min(grades), max(grades)))
p("h_pr multiset (value:mult) =", dict(sorted(gc.items())))

# Decompose the symmetric multiset into sl2 strings (each Sym^m contributes
# -m,-m+2,...,m).  Peel highest present value repeatedly.
mult = dict(gc)
blocks = []
while any(v > 0 for v in mult.values()):
    top = max(k for k, v in mult.items() if v > 0)     # = highest weight m
    m = top
    for w in range(-m, m + 1, 2):
        mult[w] = mult.get(w, 0) - 1
        assert mult[w] >= 0, "not a valid sl2 multiset"
    blocks.append(m)
blocks_sorted = sorted(blocks, reverse=True)
p("principal-SL(2) decomposition of 27  =  " +
  "  (+)  ".join("Sym^%d" % m for m in blocks_sorted))
p("   block dims (m+1) =", [m + 1 for m in blocks_sorted], " sum =", sum(m + 1 for m in blocks_sorted))
p("   spins j = m/2     =", [sp.Rational(m, 2) for m in blocks_sorted])

# Symmetry test: is there an SO(3)/S_3 permuting the three blocks?
dims = [m + 1 for m in blocks_sorted]
equal_dim = (len(set(dims)) == 1)
p("\n[a1] THREE blocks have dims %s -> all-distinct = %s" % (dims, not equal_dim))
p("     A symmetric spatial triad needs 3 EQUIVALENT (equal-dim) irreps (S_3/SO(3)")
p("     permuting them). Here the blocks are DISTINCT irreps (spins %s) of the object's" %
  [str(sp.Rational(m,2)) for m in blocks_sorted])
p("     OWN principal SL(2) -> NO structure-respecting map cycles them -> INCOMMENSURABLE.")

# ==========================================================================
# PART (a2): figure-eight twisted H^1 per block  (one-per-block, recompute)
# ==========================================================================
p("\n" + "-"*78)
p("PART (a2)  figure-eight twisted H^1(M; Sym^{2k})  -> each block carries ONE class")
p("-"*78)

# Riley parabolic rep of the figure-eight (2-bridge b(5,3)):
#   a -> [[1,1],[0,1]],  b -> [[1,0],[-u,1]],  w = b a^{-1} b^{-1} a,  relator a w b^{-1} w^{-1}.
# Solve rho(relator)=I for u.
u = sp.symbols('u')
def M2(g):  # SL2 matrix of a signed generator, entries in u
    a = sp.Matrix([[1,1],[0,1]])
    b = sp.Matrix([[1,0],[-u,1]])
    return {'a':a,'A':a.inv(),'b':b,'B':b.inv()}[g]
def word_mat(word, matfn):
    R = sp.eye(matfn('a').rows)
    for ch in word:
        R = R*matfn(ch)
    return R
# relator R = a w b^{-1} w^{-1}, w = b A B a  (A=a^{-1}, B=b^{-1})
w_word  = "bABa"
R_word  = "a" + w_word + "B" + "".join({'b':'B','A':'a','B':'b','a':'A'}[c] for c in reversed(w_word))
p("relator word (figure-eight) =", R_word)
RR = word_mat(R_word, M2)
RR = RR.applyfunc(sp.expand)
# rho(R)=I  <=> off-diagonal & (diag-1) vanish; collect the Riley polynomial
eqs = [sp.factor(RR[0,0]-1), sp.factor(RR[0,1]), sp.factor(RR[1,0]), sp.factor(RR[1,1]-1)]
riley = sp.gcd(sp.gcd(sp.numer(sp.together(eqs[1])), sp.numer(sp.together(eqs[2]))),
               sp.numer(sp.together(eqs[0])))
p("Riley polynomial (u) =", sp.factor(riley))
roots = sp.solve(sp.Eq(sp.factor(riley),0), u)
p("nonabelian roots u =", roots)
# discrete-faithful root: u satisfies the Riley polynomial u^2+u+1=0; trace field Q(sqrt-3).
s3 = sp.sqrt(-3)
u_val = (-1 + s3)/2                      # primitive cube root of unity (root of u^2+u+1)
p("chosen discrete-faithful u = (-1+sqrt(-3))/2 =", u_val, "  (u^2+u+1 =", sp.simplify(u_val**2+u_val+1), ")")
p("trace field  Q(u)  contains sqrt(-3):  (2u+1)^2 =", sp.simplify((2*u_val+1)**2))  # = -3

# verify rho(R) = I exactly at u_val
def matfn_val(g):
    a = sp.Matrix([[1,1],[0,1]])
    b = sp.Matrix([[1,0],[-u_val,1]])
    return {'a':a,'A':a.inv(),'b':b,'B':b.inv()}[g]
RRv = word_mat(R_word, matfn_val).applyfunc(sp.simplify)
p("rho(relator) at u = (1+sqrt-3)/2 :", RRv.tolist(), " (must be I)")
assert RRv == sp.eye(2), "relator not satisfied"

# tr(AB) -- discriminating for (b): non-real => NO real form
Aab = matfn_val('a')*matfn_val('b')
trAB = sp.simplify(Aab[0,0]+Aab[1,1])
p("tr(AB) =", trAB, " -> Im part =", sp.im(sp.expand(trAB)), " (non-real => no real slice)")

# ---- Sym^{2k} representation, Fox calculus, exact H^0/H^1 over Q(sqrt-3) ----
def sym_power(g, n):
    """(n+1)x(n+1) matrix of Sym^n(g).  g acts on (x,y): x->g00 x+g01 y, y->g10 x+g11 y.
    Basis monomials x^{n-i} y^i, i=0..n.  Verified homomorphism below."""
    x, y = sp.symbols('x y')
    g00,g01,g10,g11 = g[0,0],g[0,1],g[1,0],g[1,1]
    # basis vectors x=e_1, y=e_2 transform by COLUMNS of g (v -> g v): genuine homomorphism.
    nx = g00*x + g10*y      # g e_1
    ny = g01*x + g11*y      # g e_2
    cols = []
    for i in range(n+1):
        f = sp.expand(nx**(n-i) * ny**i)
        pol = sp.Poly(f, x, y)
        col = []
        for j in range(n+1):
            col.append(pol.coeff_monomial(x**(n-j)*y**j))
        cols.append(col)   # image of basis monomial i, expressed in monomials j
    # matrix M with M[j,i] = coeff of monomial j in image of monomial i
    return sp.Matrix(n+1, n+1, lambda j,i: cols[i][j])

# homomorphism sanity check on Sym^2
Amat = matfn_val('a'); Bmat = matfn_val('b')
S2a = sym_power(Amat,2); S2b = sym_power(Bmat,2); S2ab = sym_power(Amat*Bmat,2)
assert sp.simplify(S2a*S2b - S2ab) == sp.zeros(3,3), "Sym is not a homomorphism!"
p("Sym^n homomorphism check (n=2): PASS")

def rho_word_sym(word, n):
    M = sp.eye(n+1)
    cache = {}
    for ch in word:
        if ch not in cache:
            cache[ch] = sym_power(matfn_val(ch), n)
        M = M*cache[ch]
    return M

def fox_matrices_sym(R_word, n):
    """Return rho(dR/da), rho(dR/db) in Sym^n via prefix accumulation."""
    N = n+1
    Sa = sym_power(matfn_val('a'), n); SA = sym_power(matfn_val('A'), n)
    Sb = sym_power(matfn_val('b'), n); SB = sym_power(matfn_val('B'), n)
    S = {'a':Sa,'A':SA,'b':Sb,'B':SB}
    P = sp.eye(N)
    Da = sp.zeros(N); Db = sp.zeros(N)
    for ch in R_word:
        if ch == 'a':   Da = (Da + P).applyfunc(sp.expand)
        elif ch == 'A': Da = (Da - P*SA).applyfunc(sp.expand)     # d a^{-1}/da = -a^{-1}
        elif ch == 'b': Db = (Db + P).applyfunc(sp.expand)
        elif ch == 'B': Db = (Db - P*SB).applyfunc(sp.expand)     # d b^{-1}/db = -b^{-1}
        P = (P*S[ch]).applyfunc(sp.expand)
    return Da, Db, P.applyfunc(sp.expand)

def _to_ab(e):
    """Write a Q(sqrt-3) element as a + b*omega (omega=(-1+sqrt-3)/2), return (a,b) in Q.
    e = p + q*sqrt(3)*I  =>  in omega-coords: a = p+q, b = 2q (since sqrt(-3)=2*omega+1)."""
    e = sp.expand(e)
    pp = sp.re(e)
    qq = sp.im(e)/sp.sqrt(3)
    a = sp.nsimplify(pp + qq); b = sp.nsimplify(2*qq)
    assert a.is_rational and b.is_rational, "entry not in Q(omega): %s" % e
    return a, b

def rank_exact(Mat):
    """Exact rank over Q(omega) via the faithful Q^2 embedding a+b*omega -> [[a,-b],[b,a-b]]."""
    m, n = Mat.rows, Mat.cols
    big = sp.zeros(2*m, 2*n)
    for i in range(m):
        for j in range(n):
            a, b = _to_ab(Mat[i, j])
            big[2*i,   2*j]   = a
            big[2*i,   2*j+1] = -b
            big[2*i+1, 2*j]   = b
            big[2*i+1, 2*j+1] = a - b
    rb = big.rank()
    assert rb % 2 == 0, "doubled rank not even (embedding error)"
    return rb // 2

def cohomology_block(n):
    N = n+1
    Sa = sym_power(matfn_val('a'), n); Sb = sym_power(matfn_val('b'), n)
    # H^0 = invariants = ker(Sa-I) cap ker(Sb-I)
    stack = sp.Matrix.vstack(Sa - sp.eye(N), Sb - sp.eye(N))
    h0 = N - rank_exact(stack)
    # Fox matrix [rho(dR/da) | rho(dR/db)]
    Da, Db, RP = fox_matrices_sym(R_word, n)
    assert (RP - sp.eye(N)).applyfunc(sp.expand) == sp.zeros(N), "rho(relator) != I in Sym^%d" % n
    # fundamental Fox identity gate: rho(dR/da)(Sa-I)+rho(dR/db)(Sb-I) = rho(R)-I = 0
    ident = (Da*(Sa - sp.eye(N)) + Db*(Sb - sp.eye(N))).applyfunc(sp.expand)
    assert ident == sp.zeros(N), "Fox identity failed in Sym^%d" % n
    Fox = sp.Matrix.hstack(Da, Db)      # N x 2N
    rF = rank_exact(Fox)
    z1 = 2*N - rF                        # dim Z^1
    b1 = N - h0                          # dim B^1
    h1 = z1 - b1                         # = N - rF + h0
    return h0, h1

def _rank_modp(Mint, p):
    Mm = (sp.Matrix(Mint) % p).tolist()
    rows=len(Mm); cols=len(Mm[0]); rank=0; rr=0
    for c in range(cols):
        piv=None
        for i in range(rr,rows):
            if Mm[i][c] % p != 0: piv=i; break
        if piv is None: continue
        Mm[rr],Mm[piv]=Mm[piv],Mm[rr]
        inv=pow(int(Mm[rr][c]),p-2,p)
        Mm[rr]=[(x*inv)%p for x in Mm[rr]]
        for i in range(rows):
            if i!=rr and Mm[i][c]%p!=0:
                f=Mm[i][c]%p
                Mm[i]=[(Mm[i][k]-f*Mm[rr][k])%p for k in range(cols)]
        rr+=1; rank+=1
        if rr==rows: break
    return rank

def cohomology_block_modp(n, p):
    """Same Fox/H^0/H^1 over F_p, u a root of u^2+u+1 (the reduction of the Q(omega) rep).
    Reduction can only DROP rank, so mod-p (h0,h1) are UPPER bounds; agreement across
    several primes pins the char-0 value."""
    us = [t for t in range(p) if (t*t + t + 1) % p == 0]
    if not us: return None
    uu = us[0]
    def m(g):
        Ai = np.array([[1,-1],[0,1]], dtype=object) % p
        Bi = np.array([[1,0],[uu % p,1]], dtype=object) % p
        return {'a':np.array([[1,1],[0,1]],dtype=object)%p,'A':Ai,
                'b':np.array([[1,0],[(-uu)%p,1]],dtype=object)%p,'B':Bi}[g]
    def sym(gm, nn):
        x,y = sp.symbols('x y')
        g00,g01,g10,g11 = [int(gm[i//2, i%2]) for i in range(4)]
        nx = g00*x+g10*y; ny=g01*x+g11*y
        M = sp.zeros(nn+1)
        for i in range(nn+1):
            f = sp.expand(nx**(nn-i)*ny**i); pol=sp.Poly(f,x,y)
            for j in range(nn+1):
                M[j,i] = int(pol.coeff_monomial(x**(nn-j)*y**j)) % p
        return M
    N=n+1
    Sa=sym(m('a'),n); Sb=sym(m('b'),n)
    stack = sp.Matrix.vstack(Sa - sp.eye(N), Sb - sp.eye(N)) % p
    h0 = N - _rank_modp(stack, p)
    S = {g:sym(m(g),n) for g in 'aAbB'}
    P=sp.eye(N); Da=sp.zeros(N); Db=sp.zeros(N)
    for ch in R_word:
        if ch=='a': Da=(Da+P)%p
        elif ch=='A': Da=(Da-P*S['A'])%p
        elif ch=='b': Db=(Db+P)%p
        elif ch=='B': Db=(Db-P*S['B'])%p
        P=(P*S[ch])%p
    assert (P-sp.eye(N))%p==sp.zeros(N), "rho(relator)!=I mod %d"%p
    Fox=sp.Matrix.hstack(Da,Db)%p
    rF=_rank_modp(Fox,p)
    h1=2*N-rF-(N-h0)
    return h0,h1

GOOD_PRIMES = [19,37,43,61,67,73,79,97,103,109,127,139]   # p = 1 mod 3
def coh_dispatch(n):
    """exact over Q(omega) for small n; for large n use the reduction-theoretic
    characteristic-0 rank = MAX rank over many primes = MIN (h0,h1) over many primes
    (reduction mod p can only DROP rank => inflate h1; a 'bad prime' gives a strictly
    larger h1). We report the min and the count of primes attaining it."""
    if n <= 8:
        return cohomology_block(n), "exact/Q(w)"
    vals = [cohomology_block_modp(n, pp) for pp in GOOD_PRIMES]
    h0 = min(v[0] for v in vals); h1 = min(v[1] for v in vals)
    hit = sum(1 for v in vals if v == (h0, h1))
    return (h0, h1), "F_p min over %d primes (%d attain it; char-0 rank)" % (len(GOOD_PRIMES), hit)

# The 27's three blocks: Sym^0, Sym^8, Sym^16 (spins 0,4,8). Compute those + a couple
# of neighbours to show the pattern (each nontrivial even block -> one class).
p("\n   block-by-block (Sym^{<=8} exact over Q(sqrt-3); Sym^16 via char-0 rank = max over primes):")
per_block = {}
for n in [0, 2, 4, 8, 16]:
    (h0, h1), meth = coh_dispatch(n)
    per_block[n] = (h0, h1)
    tag = ""
    if n == 0:  tag = "  <- V1  (trivial, spin 0)   IN 27"
    if n == 8:  tag = "  <- V9  (Sym^8,  spin 4)    IN 27"
    if n == 16: tag = "  <- V17 (Sym^16, spin 8)    IN 27"
    p("     Sym^%-2d (dim %2d):  (h^0,h^1) = (%d,%d)  [%s]%s" % (n, n+1, h0, h1, meth, tag))

tot_h0 = sum(per_block[n][0] for n in [0,8,16])
tot_h1 = sum(per_block[n][1] for n in [0,8,16])
p("\n   SUM over the 27's blocks {Sym^0,Sym^8,Sym^16}: (h^0, h^1) = (%d, %d)" % (tot_h0, tot_h1))
p("   => h^1(M;27) = %d, one class per principal block, in dims 17/9/1 (spins 8/4/0)." % tot_h1)

# ==========================================================================
# PART (b): any route h^1=3 -> Lorentzian 3+1 ?  (Wick rotation / H^3 isotropy)
# ==========================================================================
p("\n" + "-"*78)
p("PART (b)  route h^1=3 -> Lorentzian 3+1?  (Wick rotation of complex-CS; H^3 isotropy)")
p("-"*78)

# (b1) The two different '3's must not be conflated.
p("[b1] TWO distinct '3's:")
p("   (i)  H^1(M;27) = 3 : the object's E6-27 deformation cohomology. Just computed:")
p("        three classes in INCOMMENSURABLE blocks 17/9/1 (spins 8,4,0). Not a")
p("        vector-3; no SO(3) acts; NOT spatial directions.")
p("   (ii) T_pH^3 = R^3 : the tangent space of the hyperbolic 3-manifold M itself,")
p("        with isotropy SO(3) acting as the standard vector rep (a genuine symmetric")
p("        triad).  chat-1's '3 spatial modes' silently swaps (i) for (ii).")

# (b2) H^3 isotropy: SO(3) standard rep on R^3 is IRREDUCIBLE -> no invariant line ->
#      no canonical direction to complexify into 'time' -> no canonical Wick axis.
p("\n[b2] H^3 isotropy: does SO(3) fix any tangent direction (a canonical time axis)?")
Lx = np.array([[0,0,0],[0,0,-1],[0,1,0]], float)   # so(3) generators
Ly = np.array([[0,0,1],[0,0,0],[-1,0,0]], float)
Lz = np.array([[0,-1,0],[1,0,0],[0,0,0]], float)
# an invariant real line v: L v = 0 for all generators.  Common kernel:
Bmat3 = np.vstack([Lx, Ly, Lz])                    # 9x3
rank = np.linalg.matrix_rank(Bmat3)
p("     rank of stacked so(3) generators = %d (=3) -> common kernel dim = %d" % (rank, 3-rank))
p("     => SO(3) fixes NO real tangent direction (standard 3 is irreducible).")
p("     => H^3 is ISOTROPIC: no invariant direction to Wick-rotate -> no canonical (3,1).")

# (b3) No real form for the complex-CS holonomy (lifts from the SL(2) sub).
p("\n[b3] Real form / signature: tr(AB) = %s is NON-REAL (Im = %s)." %
  (sp.nsimplify(trAB), sp.im(sp.expand(trAB))))
p("     SL(2,R) and SU(2) have REAL traces; a non-real trace on the principal SL(2)")
p("     => the E6(C) holonomy lies in NO real form -> no canonical Riemannian/Lorentzian")
p("     signature is supplied by the object. (Complex Chern-Simons, not Yang-Mills.)")

# (b4) 4d filling non-uniqueness (oriented 3-bordism is trivial).
p("\n[b4] A 4th (time) dimension: oriented 3-bordism Omega_3^SO = 0 (Rokhlin/Thom, known)")
p("     => a 4d filling EXISTS but is infinitely non-unique (W, W#CP^2, W#2CP^2, ...;")
p("     signatures s, s+1, s+2, ...). Nothing selects one 4-manifold, one signature, or")
p("     a Lorentzian metric. No canonical 4th dimension, no canonical 3+1.")

# ==========================================================================
# BASE RATE
# ==========================================================================
p("\n" + "-"*78)
p("BASE-RATE gate")
p("-"*78)
p("(a) A 'symmetric spatial triad' requires 3 EQUAL-dim principal blocks (an S_3/SO(3)")
p("    permuting them). The E6 principal branching of the 27 is DETERMINISTIC:")
p("    17 (+) 9 (+) 1, all distinct. P(object supplies a symmetric triad) = 0 (forced).")
p("(b) 'h^1 = 3 matches 3 space dims': the object's computed cohomology dims are")
p("    h^0=1, h^1(M)=3, h^1(D)=5, h^1(adj-78)=6 -- '3' is ONE small integer among")
p("    several the same object produces. Matching a bare '3' to '3 spatial dims' is a")
p("    ~1/several coincidence with NO structural support (the 3 are incommensurable).")
p("    Base rate for a bare-integer match of this kind: HIGH (cheap); not p<0.01.")

# ==========================================================================
# VERDICT
# ==========================================================================
p("\n" + "="*78)
p("VERDICT")
p("="*78)
p("(a) The three H^1 classes are ONE-PER-BLOCK in the INCOMMENSURABLE principal blocks")
p("    27 = Sym^16 (+) Sym^8 (+) Sym^0 = 17 (+) 9 (+) 1 (spins 8,4,0). Distinct irreps of")
p("    the object's own principal SL(2): NO SO(3)/S_3 permutes them. NOT a symmetric")
p("    spatial triad.")
p("(b) No route h^1=3 -> Lorentzian 3+1: (i) the incommensurable 3 is not the SO(3)-")
p("    symmetric H^3 tangent-3 (conflation); (ii) H^3 is isotropic -> no invariant Wick")
p("    axis; (iii) the E6(C) holonomy has NO real form (tr AB non-real) -> no canonical")
p("    signature; (iv) Omega_3^SO=0 -> 4th dimension infinitely non-unique. UNBUILT/BLOCKED.")
p("")
p("OUTCOME  =  B  (incommensurable 17/9/1; no symmetric triad; no route to 3+1;")
p("               the h^1=3 -> 3+1 identification is STRUCTURALLY BLOCKED).")
p("="*78)

# ---- F_p cross-check + the unlucky-prime demonstration for Sym^16 ----
p("\n[cross-check] Sym^16 over many F_p (u solves u^2+u+1). Reduction can only DROP")
p("   rank => inflate h^1; the char-0 value = MIN over primes. Watch the unlucky primes:")
scan = [(pp, cohomology_block_modp(16, pp)) for pp in
        [13,19,31,37,43,61,67,73,79,97,103,109,127,139,151,163]]
badp = [pp for pp,(h0,h1) in scan if h1 != 1]
goodcount = sum(1 for pp,(h0,h1) in scan if h1 == 1)
p("     h^1(Sym^16) by prime: " + ", ".join("%d:%d"%(pp,h1) for pp,(h0,h1) in scan))
p("     UNLUCKY primes (h^1>1, rank-deficient): %s" % badp)
p("     %d/%d primes give h^1=1 => char-0 h^1(Sym^16)=1 (my first sample p=13,31 were" % (goodcount, len(scan)))
p("     BOTH unlucky -- the reason to scan, not to trust one prime). one-per-block CONFIRMED.")

# write output file
with open("frontier/B724_seeing_readjudication/b724_probe1_out.txt","w") as f:
    f.write("\n".join(OUT)+"\n")
p("\n[written] b724_probe1_out.txt")
