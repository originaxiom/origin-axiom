"""B787 Phase 2 -- DOOR D4  (E6(78) decomposed under V4).

Question (prereg D4 / MASTERPLAN row D4):
  The E6 adjoint (78-dim) under the observer V4 = {1, c, theta, c.theta}.  Use the McKay
  correspondence V4 subset Aut(E6 Dynkin).  The E6 diagram has an order-2 automorphism
  (the E6->F4 folding reflection).  Determine whether that diagram automorphism corresponds
  to c, to theta, or to NEITHER (compute, do not assert).  Then sort the torsion spectrum
  {U_m(3/2) : m in E6 exponents {1,4,5,7,8,11}} into the +-1 eigenspaces of each V4 element
  (c-even/c-odd, theta-even/theta-odd).  Determine if the parity assignment is FORCED by the
  McKay action or is base-rate.

  PRE-STATED HIT CRITERION: a FORCED c/theta-parity assignment of the E6 cascade (not base-rate),
  each exponent's eigenspace determined by the McKay V4 action, not chosen.  OUTCOME B (MISS):
  base-rate OR the diagram automorphism is neither c nor theta.

Everything EXACT (sympy rationals / integers).  Gate 5 + Gate 5-Q: structural labels only,
nothing to CLAIMS; no SM value emitted.
"""
import itertools, json
import sympy as sp

R = {}
def head(s): print("=" * 88); print(s); print("=" * 88)


# ===========================================================================
head("0.  E6 Dynkin diagram, Cartan matrix (Bourbaki-style labelling)")
# ===========================================================================
#         1 - 3 - 4 - 5 - 6         edges: (1,3)(3,4)(4,5)(5,6)(2,4)
#                 |
#                 2
nodes = [1, 2, 3, 4, 5, 6]
edges = {frozenset(e) for e in [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]}
idx = {n: i for i, n in enumerate(nodes)}
A = sp.zeros(6, 6)
for i in range(6):
    A[i, i] = 2
for e in edges:
    a, b = tuple(e)
    A[idx[a], idx[b]] = A[idx[b], idx[a]] = -1
print("Cartan matrix A(E6):")
sp.pprint(A)
print("det A =", A.det(), " (E6 index of connection = 3)")
assert A.det() == 3


# ===========================================================================
head("1.  Aut(E6 Dynkin) computed by brute force  ->  is V4 a subgroup?")
# ===========================================================================
# a diagram automorphism = a permutation of the 6 nodes preserving the Cartan matrix.
autos = []
for p in itertools.permutations(range(6)):
    P = sp.zeros(6, 6)
    for j in range(6):
        P[p[j], j] = 1
    if P.T * A * P == A:
        autos.append(p)
print("all node-permutations preserving A:")
for p in autos:
    lab = tuple(nodes[p[i]] for i in range(6))
    print("   ", lab)
aut_order = len(autos)
print("=> |Aut(E6 Dynkin)| =", aut_order, " (group =", "Z/2)" if aut_order == 2 else "?)")
R["aut_e6_dynkin_order"] = aut_order

# the unique non-trivial diagram automorphism tau:
tau = next(p for p in autos if p != tuple(range(6)))
tau_cycles = []
seen = set()
for i in range(6):
    if i in seen:
        continue
    j = tau[i]
    if j == i:
        tau_cycles.append((nodes[i],)); seen.add(i)
    else:
        tau_cycles.append((nodes[i], nodes[j])); seen.add(i); seen.add(j)
print("tau (the E6->F4 folding reflection) acts on nodes as:", tau_cycles)
R["tau_node_action"] = str(tau_cycles)

# CAN V4 (order 4, Klein) embed in Aut = Z/2 (order 2) ?  A group hom V4 -> Z/2 has |image|
# dividing gcd; a FAITHFUL (injective) map needs |V4| <= |Z/2|.  4 > 2 => impossible.
v4_embeds = (4 <= aut_order) and (aut_order % 4 == 0)
print(f"V4 (order 4) injects into Aut(E6 Dynkin) (order {aut_order})?  {v4_embeds}")
print("  => at most ONE non-trivial V4 element can be realised as tau; the map V4->Z/2 has")
print("     a kernel of order 2.  The three involutions {c, theta, c.theta} cannot be told")
print("     apart by the diagram: exactly ONE of them is in the kernel (acts trivially on the")
print("     diagram), the OTHER TWO both act as the SAME tau.")
R["V4_embeds_in_aut"] = bool(v4_embeds)

# enumerate the homomorphisms V4 -> Z/2 = {0, tau} and show tau <-> a 2-element COSET, not a
# single generator.  V4 = <c, theta> with elements {id, c, theta, c.theta}.
v4 = {"id": (0, 0), "c": (1, 0), "theta": (0, 1), "c.theta": (1, 1)}
homs = []
for (ac, ath) in itertools.product([0, 1], repeat=2):   # images of c, theta in Z/2
    h = {name: (ac * b0 + ath * b1) % 2 for name, (b0, b1) in v4.items()}
    homs.append(((ac, ath), h))
print("\nall homomorphisms V4 -> Z/2 (0=trivial-on-diagram, 1=acts-as-tau):")
for (ac, ath), h in homs:
    ker = sorted(k for k, v in h.items() if v == 0)
    img = sorted(k for k, v in h.items() if v == 1)
    print(f"   c->{ac}, theta->{ath}:  kernel={ker}   act-as-tau={img or '[]'}")
print("In EVERY non-trivial hom the fibre over tau has TWO elements => the diagram automorphism")
print("corresponds to a COSET (a pair), never to a single named involution c or theta alone.")
R["tau_is_single_involution_not_c_or_theta"] = True


# ===========================================================================
head("2.  E6 exponents from the Coxeter element (self-contained, not asserted)")
# ===========================================================================
def simple_reflections(Cmat):
    n = Cmat.rows
    Ms = []
    for i in range(n):
        M = sp.eye(n)
        for j in range(n):
            M[i, j] = M[i, j] - Cmat[i, j]     # s_i : e_j -> e_j - A_ij e_i  (simply-laced)
        Ms.append(M)
    return Ms

def exponents_from_coxeter(Cmat, h):
    """exponents m in 1..h-1 such that exp(2 pi i m/h) is an eigenvalue of the Coxeter element."""
    Ms = simple_reflections(Cmat)
    Cox = sp.eye(Cmat.rows)
    for M in Ms:
        Cox = Cox * M
    # numeric eigenvalues (arguments) -> exponents; verified exact via order of the Coxeter elt.
    evs = list(Cox.eigenvals().keys())
    exps = []
    for e in evs:
        theta = sp.arg(sp.N(e, 40))
        m = theta / (2 * sp.pi / h)
        mr = int(round(float(m)))
        if mr <= 0:
            mr += h
        exps.append(mr)
    # Coxeter element has order h: confirm C^h = I (exact) so the eigenvalues really are h-th roots.
    order_ok = sp.simplify(Cox**h - sp.eye(Cmat.rows)) == sp.zeros(Cmat.rows, Cmat.rows)
    return sorted(set(exps)), order_ok

h_cox = 12
E6_exps, e6_order_ok = exponents_from_coxeter(A, h_cox)
print("Coxeter number h =", h_cox, "  Coxeter element order == h (C^12 = I, exact):", e6_order_ok)
print("E6 exponents (arguments of Coxeter eigenvalues) =", E6_exps)
assert e6_order_ok and E6_exps == [1, 4, 5, 7, 8, 11], E6_exps
R["E6_exponents"] = E6_exps
# Coxeter pairing m <-> h-m :
print("Coxeter pairs (m, h-m):", [(m, h_cox - m) for m in E6_exps if m < h_cox - m])


# ===========================================================================
head("3.  The folding tau on the ROOT SYSTEM: 78 = 52 (+1, F4) + 26 (-1)")
# ===========================================================================
# generate all 72 roots as integer vectors in the simple-root basis via the Weyl orbit.
simple = [tuple(int(k == i) for k in range(6)) for i in range(6)]
def reflect(vec, i):
    # s_i(v) = v - <v, alpha_i^vee> alpha_i ; in simple-root coords <v,a_i^vee> = (A v)_i
    Av_i = sum(A[i, j] * vec[j] for j in range(6))
    return tuple(vec[j] - (Av_i if j == i else 0) for j in range(6))
roots = set(simple) | set(tuple(-x for x in s) for s in simple)
frontier = set(roots)
while frontier:
    nxt = set()
    for v in frontier:
        for i in range(6):
            w = reflect(v, i)
            if w not in roots:
                roots.add(w); nxt.add(w)
    frontier = nxt
roots = sorted(roots)
print("number of E6 roots =", len(roots), "(expected 72)")
assert len(roots) == 72

# tau on the root space: permute the simple-root basis by the node map tau, i.e. e_i -> e_tau(i).
sigma = {i: tau[i] for i in range(6)}   # tau as 0-indexed node permutation
def apply_tau(vec):
    out = [0] * 6
    for i in range(6):
        out[sigma[i]] += vec[i]
    return tuple(out)
fixed_roots = [r for r in roots if apply_tau(r) == r]
# count 2-orbits
seen = set(); two_orbits = 0
for r in roots:
    if r in seen:
        continue
    tr = apply_tau(r)
    if tr == r:
        seen.add(r)
    else:
        two_orbits += 1; seen.add(r); seen.add(tr)
n_fixed = len(fixed_roots)
n_orbits = n_fixed + two_orbits
print("tau-fixed roots     =", n_fixed, "(expected 24)")
print("tau 2-orbits        =", two_orbits, "(expected 24)")
print("total tau-orbits    =", n_orbits, "(expected 48 = #roots of F4)")
# fixed subalgebra dim = dim(h^tau) + (#tau-orbits on roots)  [standard folding, all-plus signs]
dim_h_fix = sum(1 for _ in range(6)) - 0  # compute below properly
# h^tau: +1 eigenspace of the linear map e_i->e_sigma(i) on R^6
Ptau = sp.zeros(6, 6)
for i in range(6):
    Ptau[sigma[i], i] = 1
plus_h = (Ptau - sp.eye(6)).nullspace()
minus_h = (Ptau + sp.eye(6)).nullspace()
dim_h_fix = len(plus_h)
dim_h_anti = len(minus_h)
dim_fixed_alg = dim_h_fix + n_orbits
dim_anti_alg = dim_h_anti + two_orbits
print(f"dim h^tau (+1 on Cartan)   = {dim_h_fix}  (= rank F4 = 4)")
print(f"dim h^-tau (-1 on Cartan)  = {dim_h_anti}")
print(f"dim FIXED subalgebra       = {dim_h_fix} + {n_orbits} = {dim_fixed_alg}  (= F4, 52)")
print(f"dim (-1)-eigenspace        = {dim_h_anti} + {two_orbits} = {dim_anti_alg}  (= the 26)")
print(f"check 52 + 26 = {dim_fixed_alg + dim_anti_alg} (= 78, dim E6)")
assert dim_fixed_alg == 52 and dim_anti_alg == 26 and dim_fixed_alg + dim_anti_alg == 78
R["tau_fixed_roots"] = n_fixed
R["tau_two_orbits"] = two_orbits
R["dim_plus1_eigenspace_F4"] = dim_fixed_alg
R["dim_minus1_eigenspace_26"] = dim_anti_alg


# ===========================================================================
head("4.  tau-parity of the EXPONENTS is FORCED by F4-folding invariant degrees")
# ===========================================================================
# E6 degrees = exponents + 1 ; F4 (the tau-fixed subalgebra) basic degrees are standard.
E6_degrees = sorted(e + 1 for e in E6_exps)          # {2,5,6,8,9,12}
F4_degrees = [2, 6, 8, 12]                            # F4 basic invariant degrees
F4_exps    = sorted(d - 1 for d in F4_degrees)        # {1,5,7,11}
# verify F4 exponents independently via an F4 Coxeter element (h=12):
F4_C = sp.Matrix([[2, -1, 0, 0],                      # F4 Cartan matrix (one double bond)
                  [-1, 2, -1, 0],
                  [0, -2, 2, -1],
                  [0, 0, -1, 2]])
F4_exps_chk, f4_order_ok = exponents_from_coxeter(F4_C, 12)
print("F4 basic degrees   =", F4_degrees, " -> F4 exponents =", F4_exps, " (Coxeter-check:", F4_exps_chk, ")")
assert F4_exps_chk == F4_exps == [1, 5, 7, 11]

tau_even_exps = sorted(F4_exps)                       # survive the folding => tau-EVEN
tau_odd_exps  = sorted(set(E6_exps) - set(F4_exps))   # lost by F4 => tau-ODD (degrees 5,9)
tau_odd_degs  = sorted(d for d in E6_degrees if d - 1 in tau_odd_exps)
print("\ntau-EVEN exponents (F4-shared, degrees 2,6,8,12):", tau_even_exps, "  count =", len(tau_even_exps))
print("tau-ODD  exponents (E6-only, degrees", tau_odd_degs, ")      :", tau_odd_exps, "  count =", len(tau_odd_exps))
# the counting is the forcing: #even must equal dim(h^tau)=rank F4=4, #odd = dim(h^-tau)=2.
# CLOSE THE JACOBIAN GAP: '#even basic invariants = dim h^tau' uses that the basic invariants'
# differentials at a generic point of h^tau are a basis of tau-eigenvectors -- which needs a
# generic point of h^tau to be E6-regular, i.e. NO E6 root vanishes on h^tau.  A root vanishes
# on h^tau iff it lies in h^{-tau}, i.e. iff tau(alpha) = -alpha.  Check there are NONE:
anti_fixed_roots = [r for r in roots if apply_tau(r) == tuple(-x for x in r)]
print(f"E6 roots with tau(alpha) = -alpha (would vanish on h^tau): {len(anti_fixed_roots)}  (expected 0)")
print("  => a generic point of h^tau is E6-regular; the basic invariants' Jacobian is a basis of")
print("     tau-eigenvectors, so #(tau-even basic invariants) = dim h^tau EXACTLY.  No free choice.")
assert len(anti_fixed_roots) == 0
R["roots_tau_antifixed"] = len(anti_fixed_roots)

forced = (len(tau_even_exps) == dim_h_fix == 4) and (len(tau_odd_exps) == dim_h_anti == 2)
print(f"\nFORCING CHECK: #even={len(tau_even_exps)} == dim h^tau={dim_h_fix}, "
      f"#odd={len(tau_odd_exps)} == dim h^-tau={dim_h_anti}:  {forced}")
print("=> the tau-parity of the cascade is FORCED (not chosen): {1,5,7,11} even, {4,8} odd.")
R["tau_even_exps"] = tau_even_exps
R["tau_odd_exps"] = tau_odd_exps
R["tau_parity_forced"] = bool(forced)
assert forced


# ===========================================================================
head("5.  The torsion spectrum U_m(3/2) at the six exponents  ->  even-Fibonacci")
# ===========================================================================
# Chebyshev U via recurrence U_{m+1}=3 U_m - U_{m-1} (since 2*(3/2)=3), exact integers.
def U(m):
    a, b = sp.Integer(1), sp.Integer(3)   # U0=1, U1=3
    if m == 0: return a
    for _ in range(m - 1):
        a, b = b, 3 * b - a
    return b
x = sp.Rational(3, 2)
tor = {m: U(m) for m in E6_exps}
# identity: U_m(3/2) = F_{2m+2}  (phi^2 + phi^-2 = 3 => lambda=phi^2, U_m = (l^{m+1}-l^-{m+1})/(l-1/l) = F_{2m+2})
fib = {m: sp.fibonacci(2 * m + 2) for m in E6_exps}
id_ok = all(tor[m] == fib[m] for m in E6_exps)
# double-check U against sympy's chebyshevu:
cheb_ok = all(U(m) == sp.chebyshevu(m, x) for m in E6_exps)
print("m      U_m(3/2)     F_{2m+2}   match   (2m+2 = 2*degree)")
for m in E6_exps:
    print(f"{m:<3d}  {int(tor[m]):>10d}  {int(fib[m]):>10d}     {tor[m]==fib[m]}       {2*m+2}")
print(f"\nU_m(3/2) == F_(2m+2) for all exponents:      {id_ok}   (EXACT identity)")
print(f"U_m(3/2) == sympy.chebyshevu(m,3/2):         {cheb_ok}")
assert id_ok and cheb_ok
R["torsion_U_m_three_halves"] = {int(m): int(tor[m]) for m in E6_exps}
R["torsion_equals_F_2m_plus_2"] = bool(id_ok)


# ===========================================================================
head("6.  Sort the torsion into the +-1 eigenspaces -- of tau, of c, of theta")
# ===========================================================================
tau_even_tor = {int(m): int(tor[m]) for m in tau_even_exps}
tau_odd_tor  = {int(m): int(tor[m]) for m in tau_odd_exps}
print("tau-EVEN (F4)  torsion  {m:F_{2m+2}} =", tau_even_tor)
print("tau-ODD  (26)  torsion  {m:F_{2m+2}} =", tau_odd_tor)
print()
print("Now the door asks for c-parity AND theta-parity SEPARATELY.  But (section 1) the diagram")
print("supplies only ONE non-trivial involution tau.  c and theta cannot both act as distinct")
print("diagram involutions: exactly one of {c,theta,c.theta} is in ker(V4->Z/2) and the other two")
print("equal tau on the diagram.  So the McKay/diagram action gives ONE bit (tau-parity), not two.")
print()
print("Consequently there are only the following diagram-consistent scenarios, and NONE of them")
print("is forced by the diagram itself (which of c/theta sits in the kernel is EXTRA input):")
for (ac, ath), hmap in homs:
    if (ac, ath) == (0, 0):
        continue
    ker = [k for k, v in hmap.items() if v == 0 and k != "id"]
    act = [k for k, v in hmap.items() if v == 1]
    # under this scenario: elements acting as tau carry the {1,5,7,11}/{4,8} split; the kernel
    # element acts trivially (its 'parity' is degenerate: everything even).
    print(f"   scenario c->{ac},theta->{ath}: {act} carry the forced split; {ker} act TRIVIALLY "
          f"(all six exponents 'even', 0 odd -- degenerate).")
R["tau_even_torsion"] = tau_even_tor
R["tau_odd_torsion"] = tau_odd_tor


# ===========================================================================
head("7.  BASE-RATE / FORCING verdict")
# ===========================================================================
# Is the tau-parity split base-rate?  No: it is an EXACT invariant-theoretic identity
# (F4 degrees {2,6,8,12} vs the E6-only degrees {5,9}), corroborated by the root-system
# folding 24/24 -> 52/26 and by #even=dim h^tau=4, #odd=dim h^-tau=2.  Zero free choices.
# BUT the door's HIT criterion needs a c/theta-DISTINGUISHED forced assignment.  That requires
# TWO independent diagram involutions; the diagram has only ONE (Aut = Z/2).  So:
print("A) tau-parity split of the cascade                 : FORCED, EXACT (invariant theory).")
print("     even {1,5,7,11} -> torsion", list(tau_even_tor.values()),
      "= [F4,F12,F16,F24]")
print("     odd  {4,8}      -> torsion", list(tau_odd_tor.values()), "= [F10,F18]")
print("B) which of c / theta the diagram automorphism IS  : UNDETERMINED by the diagram.")
print("     Aut(E6 Dynkin)=Z/2 has room for ONE involution; V4 does NOT embed.  tau corresponds")
print("     to a 2-element coset, i.e. to NEITHER c nor theta individually.")
print("C) a c/theta-DISTINGUISHED forced parity assignment : DOES NOT EXIST from the McKay action.")
print("     The action yields ONE parity bit, not two; separating c-parity from theta-parity")
print("     needs extra (antilinear-vs-linear) input the diagram cannot supply.")
print()
verdict = (
 "OUTCOME B (MISS on the pre-stated HIT criterion).  A single, EXACT, forced structure exists\n"
 "-- the tau-parity split {1,5,7,11}(even) / {4,8}(odd), torsion U_m(3/2)=F_{2m+2} splitting as\n"
 "{3,144,987,46368} / {55,2584} -- but it is the parity of the ONE diagram involution tau, not\n"
 "a c/theta-distinguished assignment.  Because Aut(E6 Dynkin)=Z/2 (V4 does NOT embed; brute-force\n"
 "confirmed), the McKay/diagram action cannot separate c from theta: tau corresponds to a\n"
 "2-element coset, i.e. to NEITHER c nor theta individually.  This matches prereg OUTCOME B\n"
 "verbatim ('the assignment is base-rate / the diagram automorphism is neither c nor theta').\n"
 "The forced tau-split is a clean EXACT sub-result (not a numeric coincidence, no look-elsewhere\n"
 "budget spent), recorded -- but it is short of the c/theta-forced cascade the door required."
)
print(verdict)
R["VERDICT"] = ("OUTCOME_B_MISS: tau-parity split {1,5,7,11}/{4,8} is FORCED & EXACT, but "
                "Aut(E6 Dynkin)=Z/2 (V4 does not embed) => diagram automorphism is NEITHER c nor "
                "theta individually; no c/theta-distinguished forced assignment exists.")
R["HIT_or_MISS"] = "MISS"

with open("results.json", "w") as f:
    json.dump(R, f, indent=1, default=str)
print("\nwrote results.json")
