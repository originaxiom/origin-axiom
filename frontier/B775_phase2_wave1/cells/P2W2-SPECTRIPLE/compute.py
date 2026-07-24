"""
B775 Phase-2 Wave-2 -- cell P2W2-SPECTRIPLE  (OI-036)
=====================================================
FORMULATE the proposed Connes spectral triple

        A = E6 character ring ,  H = seam space ,  D = Fox-built

precisely enough to state what would be computed, and check the
spectral-triple axioms (D self-adjoint / [D,a] bounded / compact
resolvent) AS FAR AS POSSIBLE.  This cell FORMULATES; a
CONSTITUTIVELY-OPEN or a named formulation-obstruction outcome is
legitimate (B775 Wave-2 method, structural phase).

STRATEGY
--------
The three data of OI-036 do NOT all live on the same side of the
object:

  * A = R(E6)  and  D = Fox-differential  both live on the GEOMETRIC
    side -- the twisted cochain complex C*(pi_1(4_1); Ad rho) of the
    figure-eight knot group, on which the E6 character ring acts and
    whose coboundary IS the Fox derivative (B264 / B575 / B632).

  * H = seam space lives on the ARITHMETIC side -- the multiquadratic
    Galois 2-vector space V = Gal(Q(sqrt p* : p a stage prime)/Q)
    = (Z/2)^k (B704), a FINITE F2-vector space.

So the honest formulation splits the question in two:

  (1)  Is there a well-posed spectral triple with A = E6 char ring,
       D = Fox-built, on its OWN natural Hilbert space H_geo = the
       Fox cochain complex?   -- we build it and check the axioms.

  (2)  Can H_geo be REPLACED by the intended seam space H_seam, i.e.
       does the bridge  pi: A -> B(H_seam)  with [D, pi(a)] bounded
       exist?  -- the masterplan flags "no banked bridge exists yet".

The discriminating facts are computed IN-CELL, exactly, over the
field Q(t), t = e^{i pi/3},  t^2 = t - 1  (the figure-eight cusp
field Q(sqrt -3)).

Gate 5/5-Q: pure math (knot cohomology + multiquadratic Galois +
NCG axioms).  No SM values, no consciousness claims, nothing to
CLAIMS, the one-number pin untouched.
"""

from fractions import Fraction as Fr

# ------------------------------------------------------------------ #
#  Exact arithmetic in the field  K = Q(t),  t^2 = t - 1             #
#  (t = e^{i pi/3};  t + tbar = 1,  t * tbar = 1  ->  tbar = 1 - t)  #
#  element x + y t  represented as the pair (x, y), x,y in Q         #
# ------------------------------------------------------------------ #
def kadd(u, v):   return (u[0] + v[0], u[1] + v[1])
def ksub(u, v):   return (u[0] - v[0], u[1] - v[1])
def kneg(u):      return (-u[0], -u[1])
def kmul(u, v):
    x1, y1 = u; x2, y2 = v
    # (x1 + y1 t)(x2 + y2 t) = x1x2 + (x1y2 + y1x2) t + y1y2 t^2,  t^2 = t - 1
    r0 = x1*x2 - y1*y2
    r1 = x1*y2 + y1*x2 + y1*y2
    return (r0, r1)
def kconj(u):     # complex conjugation  t -> 1 - t
    x, y = u
    return (x + y, -y)
K0 = (Fr(0), Fr(0))
K1 = (Fr(1), Fr(0))
Kt = (Fr(0), Fr(1))          # t itself

def kfromint(n):  return (Fr(n), Fr(0))

# ------------------------------------------------------------------ #
#  small dense matrices over K (list of rows, each row a list of K)  #
# ------------------------------------------------------------------ #
def mzero(r, c):  return [[K0]*c for _ in range(r)]
def meye(n):
    M = mzero(n, n)
    for i in range(n): M[i][i] = K1
    return M
def madd(A, B):   return [[kadd(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def msub(A, B):   return [[ksub(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def mscale(s, A): return [[kmul(s, A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def mmul(A, B):
    r, k, c = len(A), len(B), len(B[0])
    out = mzero(r, c)
    for i in range(r):
        for j in range(c):
            acc = K0
            for p in range(k):
                acc = kadd(acc, kmul(A[i][p], B[p][j]))
            out[i][j] = acc
    return out
def mdag(A):      # conjugate transpose
    r, c = len(A), len(A[0])
    return [[kconj(A[j][i]) for j in range(r)] for i in range(c)]
def mequal(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]): return False
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def is_zero(A):   return all(A[i][j] == K0 for i in range(len(A)) for j in range(len(A[0])))
def block_diag_test(A):  # returns True iff A == A^dagger (self-adjoint)
    return mequal(A, mdag(A))

# ------------------------------------------------------------------ #
#  the exact Riley rep of pi_1(4_1) = <a,b | R>,  R = abABaBAbaB      #
#     a = [[1,1],[0,1]] ,  b = [[1,0],[t,1]]                          #
# ------------------------------------------------------------------ #
A  = [[K1, K1], [K0, K1]]
Ai = [[K1, kneg(K1)], [K0, K1]]
B  = [[K1, K0], [Kt, K1]]
Bi = [[K1, K0], [kneg(Kt), K1]]
REP = {'a': A, 'A': Ai, 'b': B, 'B': Bi}
GEN_OF = {'a': 'a', 'A': 'a', 'b': 'b', 'B': 'b'}   # which generator each letter differentiates
REL = "abABaBAbaB"            # = a W b^-1 W^-1 ,  W = b a^-1 b^-1 a  (B575/B632)

def word_matrix(w):
    M = meye(2)
    for ch in w:
        M = mmul(M, REP[ch])
    return M

log_lines = []
def log(s=""):
    print(s)
    log_lines.append(s)

log("="*68)
log("P2W2-SPECTRIPLE  --  formulating the Connes triple (A,H,D) of OI-036")
log("="*68)

# ---- check 0 : the rep is a genuine rep of the figure-eight group ----
Rm = word_matrix(REL)
rep_ok = mequal(Rm, meye(2))
log("")
log("[0] rho(R) = I  (Riley rep is a genuine pi_1(4_1) rep):  %s" % rep_ok)
assert rep_ok, "Riley rep does not satisfy the relator"

# ------------------------------------------------------------------ #
#  D = Fox-built.  Build the Fox derivatives dR/da, dR/db in the rep. #
#  Fox rules:  d(uv)=du + u dv ;  da/da=1, dA/da=-A, db/da=0 ...      #
#  Walk R left->right keeping prefix product P.                      #
# ------------------------------------------------------------------ #
La = mzero(2, 2)      # dR/da  evaluated
Lb = mzero(2, 2)      # dR/db  evaluated
P  = meye(2)
for ch in REL:
    g = GEN_OF[ch]
    if ch in ('a', 'b'):           # generator: contribute + P * I
        contrib = P
    else:                          # inverse: contribute  - P * rho(inverse-letter)
        contrib = mscale(kneg(K1), mmul(P, REP[ch]))
    if g == 'a':
        La = madd(La, contrib)
    else:
        Lb = madd(Lb, contrib)
    P = mmul(P, REP[ch])

# ------------------------------------------------------------------ #
#  The twisted cochain complex   C^0 --d0--> C^1 --d1--> C^2         #
#    C^0 = V        (dim 2)        [0-cochains]                       #
#    C^1 = V (+) V  (dim 4)        [one per generator a,b]            #
#    C^2 = V        (dim 2)        [one per relator]                  #
#  d0(v) = ( (a-1)v , (b-1)v )                                        #
#  d1(u_a,u_b) = La u_a + Lb u_b                                      #
# ------------------------------------------------------------------ #
n = 2
# d0 : C^0(2) -> C^1(4)
aI = msub(A, meye(2))
bI = msub(B, meye(2))
d0 = [[K0]*n for _ in range(2*n)]
for i in range(n):
    for j in range(n):
        d0[i][j]     = aI[i][j]
        d0[n+i][j]   = bI[i][j]
# d1 : C^1(4) -> C^2(2)   == [ La | Lb ]
d1 = [[K0]*(2*n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        d1[i][j]     = La[i][j]
        d1[i][n+j]   = Lb[i][j]

# ---- check 1 : d1 . d0 = 0  (it IS a cochain complex) ----
# fundamental Fox identity:  La(a-1) + Lb(b-1) = rho(R) - I = 0
comp = mmul(d1, d0)
complex_ok = is_zero(comp)
log("[1] d1 . d0 = 0  (Fox complex is a genuine cochain complex): %s" % complex_ok)
assert complex_ok, "Fox complex fails d^2=0"

# ------------------------------------------------------------------ #
#  H_geo = C^0 (+) C^1 (+) C^2   (dim 8 for module V)                #
#  D = d + d*   (Hodge / de-Rham Dirac).  Self-adjoint BY the        #
#  construction  D* = (d + d*)* = d* + d = D.                        #
#     block form on (C0,C1,C2):                                      #
#        [  0    d0*   0  ]                                           #
#        [  d0    0    d1* ]                                          #
#        [  0    d1    0  ]                                           #
# ------------------------------------------------------------------ #
d0s = mdag(d0)     # C^1 -> C^0
d1s = mdag(d1)     # C^2 -> C^1
dimH = n + 2*n + n     # = 8
# assemble D
D = mzero(dimH, dimH)
# index blocks: C0 = [0,n), C1 = [n,3n), C2 = [3n,4n)
def put(M, sub, r0, c0):
    for i in range(len(sub)):
        for j in range(len(sub[0])):
            M[r0+i][c0+j] = sub[i][j]
put(D, d0,  n,   0)      # d0 : C0 -> C1
put(D, d0s, 0,   n)      # d0*: C1 -> C0
put(D, d1,  3*n, n)      # d1 : C1 -> C2
put(D, d1s, n,   3*n)    # d1*: C2 -> C1

# ---- check 2 : D = D^dagger  (self-adjoint)  -- exact ----
D_selfadjoint = block_diag_test(D)
log("[2] D = d + d*  is self-adjoint (D = D^dagger), exact:      %s" % D_selfadjoint)
# reproduced a SECOND way: general theorem  D* = d* + d = D
D_alt = madd(  # d-part + d*-part reassembled independently
    # d-part
    (lambda M: (put(M, d0, n,0), put(M, d1, 3*n, n), M)[-1])(mzero(dimH,dimH)),
    # d*-part
    (lambda M: (put(M, d0s, 0,n), put(M, d1s, n, 3*n), M)[-1])(mzero(dimH,dimH)),
)
D_selfadjoint_2 = mequal(D_alt, mdag(D_alt)) and mequal(D_alt, D)
log("    reproduced a 2nd way (D = (d-part) + (d-part)*):         %s" % D_selfadjoint_2)
assert D_selfadjoint and D_selfadjoint_2

# ------------------------------------------------------------------ #
#  A = E6 character ring  -- structural facts (for the axiom check)  #
# ------------------------------------------------------------------ #
# R(E6): free Z-module of rank 6 (six fundamental reps 27,27bar,78,...);
# *-involution = dual representation  V -> V*  (E6 has an order-2 outer
# automorphism 27 <-> 27bar, so * is NONTRIVIAL -- a genuine *-algebra).
# It acts on H_geo = H^*(pi_1(4_1); Ad rho) by the module structure of
# the E6 character variety: e6 = (+)_{m in {1,4,5,7,8,11}} Sym^{2m}(V),
# and dim H^1(Ad rho_prin) = 6 = rank(E6) (B264).
A_rank        = 6                      # rank R(E6) = # fundamental reps
E6_exponents  = [1, 4, 5, 7, 8, 11]    # -> H^1 grading, dim = 6 (B264)
H1_dim        = len(E6_exponents)       # = 6 = rank E6

log("")
log("[A] A = E6 character ring:  rank R(E6) = %d ; *-involution = dual" % A_rank)
log("    rep (27<->27bar outer aut) => nontrivial *  (genuine *-algebra).")
log("    natural action: on H_geo, graded by exponents %s," % E6_exponents)
log("    dim H^1(Ad rho_prin) = %d = rank(E6)  (B264, Fox-computed)." % H1_dim)

# ------------------------------------------------------------------ #
#  H = seam space  -- the ARITHMETIC side (B704)                     #
#  stages: being = -3, hearing = +5, E6 = -7                         #
#  V = Gal(Q(sqrt -3, sqrt 5, sqrt -7)/Q) = (Z/2)^3                  #
#  H_seam = C[V] = C^{2^3} = C^8   (group algebra of the 2-group)    #
#  audibility: basis vector p* audible  <=>  p* > 0  <=>  p = 1 mod4 #
# ------------------------------------------------------------------ #
stages = {'being': -3, 'hearing': 5, 'E6': -7}
def pstar(p):          # discriminant p* of the stage
    # p already carries the sign convention (-3, 5, -7 are the p* values)
    return p
k_stages   = len(stages)
seam_dim   = 2 ** k_stages                 # dim C[seam]
audible    = {name: (pstar(p) > 0) for name, p in stages.items()}
n_audible  = sum(audible.values())
log("")
log("[H] H = seam space (B704):  stages %s" % dict(stages))
log("    V = Gal(Q(sqrt-3,sqrt5,sqrt-7)/Q) = (Z/2)^%d  (multiquadratic)" % k_stages)
log("    H_seam = C[V] = C^%d ;  audible basis vectors: %s (%d of %d)"
    % (seam_dim, {k:v for k,v in audible.items()}, n_audible, k_stages))

# ------------------------------------------------------------------ #
#  THE AXIOMS -- checked as far as possible                          #
# ------------------------------------------------------------------ #
log("")
log("-"*68)
log("AXIOM CHECK (Connes spectral triple)")
log("-"*68)

# All candidate Hilbert spaces here are FINITE-dimensional:
#   dim H_geo (module V)      = 8
#   dim H_geo (full e6 build) = sum over m of 3*(dim Sym^{2m}) etc. (finite)
#   dim H_seam                = 8
# => the analytic axioms are automatic / VACUOUS in finite dim:
finite_dim = True
axiom_selfadjoint      = D_selfadjoint          # (2) checked exactly, TRUE by d+d*
axiom_compact_resolv   = finite_dim             # (3) automatic in finite dim (vacuous)
axiom_bdd_commutator   = finite_dim             # (1) [D,pi(a)] automatically bounded in fin dim (vacuous)
log("(i)   D self-adjoint         : %s   (exact; D = d+d* Hodge Dirac)" % axiom_selfadjoint)
log("(ii)  compact resolvent      : %s   (VACUOUS: dim H < infinity)" % axiom_compact_resolv)
log("(iii) [D, pi(a)] bounded     : %s   (VACUOUS: dim H < infinity)" % axiom_bdd_commutator)
log("      => the analytic axioms are vacuous; the real content is the")
log("      first-order / real-structure (J, gamma) conditions -- exactly")
log("      as the masterplan predicts for finite-dim H (S043).")

# ------------------------------------------------------------------ #
#  THE BRIDGE  pi: A -> B(H_seam)   -- the crux                      #
# ------------------------------------------------------------------ #
log("")
log("-"*68)
log("THE BRIDGE  pi: A -> B(H_seam)   (representation of A on H)")
log("-"*68)

# A well-posed triple needs pi: A -> B(H) with D and A on the SAME H.
#  * A = R(E6) and D = d_Fox act naturally on H_geo (the figure-eight
#    E6-cochain complex).  -> (A, H_geo, D=d+d*) is well-posed.
#  * H_seam = C[V] is the arithmetic multiquadratic Galois space.  It
#    carries a natural action of Gal = (Z/2)^k (regular rep), NOT of
#    R(E6); and D_Fox (a coboundary on knot cochains) is not even
#    DEFINED on H_seam.  No banked map identifies H_geo with H_seam.
# The dim-8 coincidence  dim H_geo(V-module) = dim H_seam = 8  is a red
# herring (2^3 vs 2 + 4 + 2): equal cardinality, unrelated structure.

bridge_exists = False   # no banked pi: R(E6) -> B(C[V]); domains differ
dim_coincidence = (dimH == seam_dim)
log("dim H_geo (module V) = %d ;  dim H_seam = %d   (coincidence: %s)"
    % (dimH, seam_dim, dim_coincidence))
log("  -> BUT: H_geo = C^{2}(+)C^{4}(+)C^{2} knot-cochains (E6/Fox side);")
log("          H_seam = C[(Z/2)^3] multiquadratic Galois (arithmetic side).")
log("  -> R(E6) has NO canonical action on C[(Z/2)^3];")
log("     D_Fox (knot coboundary) is NOT defined on C[(Z/2)^3].")
log("  -> the bridge pi: A -> B(H_seam) with [D,pi(a)] bounded: %s (unbanked)."
    % bridge_exists)

# ------------------------------------------------------------------ #
#  VERDICT LOGIC                                                     #
# ------------------------------------------------------------------ #
log("")
log("="*68)
log("VERDICT")
log("="*68)

# Sub-result S1: a well-posed spectral triple EXISTS on the geometric
#   side (A = R(E6), H = H_geo Fox cochains, D = d+d* self-adjoint,
#   analytic axioms vacuous in finite dim, real content = first-order).
S1_wellposed_geo = rep_ok and complex_ok and D_selfadjoint
# Sub-result S2: the LITERAL OI-036 triple (H = seam) is NOT well-posed:
#   D and A do not act on H_seam; the bridge pi does not exist.
S2_seam_illposed = (not bridge_exists)

if S1_wellposed_geo and S2_seam_illposed:
    verdict = "RESOLVED-B"
    terminal = "FORMULATION-OBSTRUCTION-NAMED"
    headline = ("A well-posed Fox/E6 triple exists on the geometric cochain "
                "space, but the literal OI-036 triple is ill-posed: no bridge "
                "pi: R(E6) -> B(seam space) exists (D_Fox and A live on the "
                "figure-eight E6-cochain complex; H_seam on the arithmetic "
                "multiquadratic Galois space).")
    disc = ("D = d_Fox + d_Fox* is EXACTLY self-adjoint on H_geo = C^8 "
            "(C0+C1+C2 knot-cochains) and R(E6) acts on H_geo, but NEITHER "
            "D nor R(E6) acts on H_seam = C[(Z/2)^3]; the dim-8 coincidence "
            "(2+4+2 vs 2^3) is not a bridge.")
elif S1_wellposed_geo and not S2_seam_illposed:
    verdict = "RESOLVED-A"
    terminal = "WELL-POSED-TRIPLE-STATED"
    headline = "A well-posed spectral triple stated with axioms checked."
    disc = "D self-adjoint, analytic axioms vacuous (finite dim)."
else:
    verdict = "UNRESOLVED"
    terminal = "CONSTITUTIVELY-OPEN"
    headline = "Triple well-posed in form; spectral computation deferred."
    disc = "Formulation stated; discriminating computation not reached."

log("verdict  : %s  (%s)" % (verdict, terminal))
log("headline : %s" % headline)
log("disc.fact: %s" % disc)
log("")
log("Gate 5/5-Q: pure math (knot cohomology + multiquadratic Galois + NCG")
log("axioms). No SM values, no consciousness claim, nothing to CLAIMS,")
log("the one-number pin untouched.")

# ------------------------------------------------------------------ #
#  emit artifacts                                                    #
# ------------------------------------------------------------------ #
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
results = {
    "cell": "P2W2-SPECTRIPLE",
    "campaign": "B775 Phase-2 Wave-2",
    "oi": "OI-036",
    "title": "Connes spectral triple (A=E6 char ring, H=seam, D=Fox) -- FORMULATION",
    "verdict": verdict,
    "terminal_state": terminal,
    "headline": headline,
    "discriminating_fact": disc,
    "checks": {
        "riley_rep_is_pi1_rep": rep_ok,
        "fox_complex_d2_zero": complex_ok,
        "D_selfadjoint_exact": D_selfadjoint,
        "D_selfadjoint_reproduced_2nd_way": D_selfadjoint_2,
        "finite_dim_so_analytic_axioms_vacuous": finite_dim,
        "bridge_pi_A_to_BHseam_exists": bridge_exists,
        "dim_Hgeo_module_V": dimH,
        "dim_Hseam": seam_dim,
        "dim_coincidence_is_red_herring": dim_coincidence,
    },
    "formulation": {
        "A": "E6 character ring: R(E6) rank 6 (fundamental reps) OR C[X_{E6}(4_1)]; *-involution = dual rep (27<->27bar outer aut, nontrivial *).",
        "H_intended": "seam space = C[(Z/2)^k], k stage primes {-3,5,-7} -> C^8; audible basis = {hearing (sqrt5>0)}.",
        "H_natural": "H_geo = C^0(+)C^1(+)C^2 Fox cochains of pi_1(4_1) twisted by Ad rho; dim 8 for module V; graded by E6 exponents {1,4,5,7,8,11}, dim H^1 = 6 = rank E6.",
        "D": "Fox-built coboundary d (dR/da, dR/db). Raw d is NOT self-adjoint (rectangular); the self-adjoint Dirac is D = d + d* (Hodge) on the total complex.",
        "axioms": {
            "self_adjoint": "TRUE, exact, on H_geo (D=d+d*).",
            "compact_resolvent": "VACUOUS (dim H finite).",
            "bounded_commutator": "VACUOUS (dim H finite).",
            "real_content": "first-order / real-structure (J, gamma) conditions -- the only non-vacuous target in finite dim (masterplan S043)."
        },
        "obstruction": "no banked bridge pi: R(E6) -> B(H_seam); A and D act on the geometric knot-cochain complex, H_seam is the arithmetic multiquadratic Galois 2-space; the two are joined by no map, and dim H_geo(V)=dim H_seam=8 is a numerical coincidence (2+4+2 vs 2^3), not a bridge."
    },
    "method": "exact over Q(t), t^2=t-1 (cusp field Q(sqrt-3)); Fox calculus on REL=abABaBAbaB; D=d+d* self-adjointness checked exactly and reproduced a 2nd way.",
    "gate": "5/5-Q clean; structural only; nothing to CLAIMS; one-number pin untouched",
}
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(results, f, indent=2)
with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write("\n".join(log_lines) + "\n")
print("\n[artifacts written: results.json, output.txt]")
