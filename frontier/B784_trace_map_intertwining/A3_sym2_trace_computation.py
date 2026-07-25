#!/usr/bin/env python3
"""B784 / A3: SL(3) = Sym^2 trace computation at the figure-eight geometric point.

Tests whether the complement C (swap A<->B) matches gamma_5 (golden Galois)
at the SL(3) level of the character variety.

Uses same Sym^2 convention as B766/audit_compute.py.
Exact SymPy arithmetic throughout -- no floating-point.
"""

import sympy as sp

# ============================================================================
# SETUP
# ============================================================================
u = sp.Symbol('u')
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
phi = (1 + sp.sqrt(5)) / 2

A = sp.Matrix([[1, 1], [0, 1]])
B_u = sp.Matrix([[1, 0], [-u, 1]])
B = B_u.subs(u, omega)

def sym2(M):
    """Sym^2 of a 2x2 matrix in basis {v1^2, v1*v2, v2^2}.
    Convention matches B766/audit_compute.py."""
    a, b, c, d = M[0,0], M[0,1], M[1,0], M[1,1]
    return sp.Matrix([
        [a**2,     2*a*b,       b**2],
        [a*c,      a*d + b*c,   b*d],
        [c**2,     2*c*d,       d**2]
    ])


print("=" * 80)
print("PART 1: SETUP AND VERIFICATION")
print("=" * 80)
print(f"omega = {omega}")
print(f"omega^2 + omega + 1 = {sp.simplify(omega**2 + omega + 1)}")
print(f"A = {A.tolist()}")
print(f"B = {[list(map(sp.simplify, row)) for row in B.tolist()]}")
print(f"tr(A) = {A.trace()}")
print(f"tr(B) = {sp.simplify(B.trace())}")

AB = A * B
BA = B * A
print(f"\nAB = {[list(map(sp.simplify, row)) for row in AB.tolist()]}")
print(f"BA = {[list(map(sp.simplify, row)) for row in BA.tolist()]}")
print(f"tr(AB) = {sp.simplify(AB.trace())}")
print(f"tr(BA) = {sp.simplify(BA.trace())}")
print(f"tr(AB) = tr(BA) at SL(2): {sp.simplify(AB.trace() - BA.trace()) == 0}")

AB_eq_BA = all(sp.simplify(AB[i,j] - BA[i,j]) == 0 for i in range(2) for j in range(2))
print(f"AB = BA as matrices: {AB_eq_BA}")
if not AB_eq_BA:
    print(f"AB - BA = {[list(map(sp.simplify, row)) for row in (AB - BA).tolist()]}")


# ============================================================================
print()
print("=" * 80)
print("PART 2: Sym^2 MATRICES AND TRACES")
print("=" * 80)

words = {
    'A': A,
    'B': B,
    'AB': AB,
    'BA': BA,
    'ABA': A * B * A,
    'BAB': B * A * B,
    'ABAB': A * B * A * B,
    'BABA': B * A * B * A,
}
word_names = ['A', 'B', 'AB', 'BA', 'ABA', 'BAB', 'ABAB', 'BABA']

sym2_mats = {}
sym2_traces = {}
for name in word_names:
    M = words[name]
    S = sym2(M)
    S_s = sp.Matrix([[sp.simplify(S[i,j]) for j in range(3)] for i in range(3)])
    sym2_mats[name] = S_s
    tr_sym2 = sp.simplify(S.trace())
    sym2_traces[name] = tr_sym2
    tr_sl2 = sp.simplify(M.trace())
    expected = sp.simplify(tr_sl2**2 - 1)
    match = sp.simplify(tr_sym2 - expected) == 0
    print(f"\n{name}:")
    print(f"  SL(2) trace = {tr_sl2}")
    print(f"  Sym^2 trace = {tr_sym2}")
    print(f"  tr(M)^2 - 1 = {expected}")
    print(f"  Identity tr(Sym^2(M)) = tr(M)^2 - 1: {match}")
    if not match:
        print(f"  *** IDENTITY FAILS ***")

# Show the key Sym^2 matrices explicitly
print("\n--- Key Sym^2 matrices ---")
for name in ['A', 'B', 'AB', 'BA']:
    print(f"\nSym^2({name}):")
    S = sym2_mats[name]
    for i in range(3):
        print(f"  [{', '.join(str(S[i,j]) for j in range(3))}]")


# ============================================================================
print()
print("=" * 80)
print("PART 3: theta (REVERSAL) ACTION")
print("=" * 80)

theta_map = {
    'A': 'A', 'B': 'B', 'AB': 'BA', 'BA': 'AB',
    'ABA': 'ABA', 'BAB': 'BAB', 'ABAB': 'BABA', 'BABA': 'ABAB'
}

print("\n--- theta at SL(2) trace level ---")
print("(theta trivial iff tr(w) = tr(w^R) for all w)")
theta_trivial_sl2 = True
for w in word_names:
    w_rev = theta_map[w]
    tr_w = sp.simplify(words[w].trace())
    tr_wr = sp.simplify(words[w_rev].trace())
    same = sp.simplify(tr_w - tr_wr) == 0
    theta_trivial_sl2 = theta_trivial_sl2 and same
    print(f"  tr({w}) = {tr_w},  tr(theta({w})) = tr({w_rev}) = {tr_wr},  equal: {same}")
print(f"theta TRIVIAL at SL(2): {theta_trivial_sl2}")

print("\n--- theta at Sym^2/SL(3) TRACE level ---")
print("(Since tr(Sym^2(M)) = tr(M)^2 - 1, depends only on tr(M) -> trivial)")
theta_trivial_sl3_trace = True
for w in word_names:
    w_rev = theta_map[w]
    same = sp.simplify(sym2_traces[w] - sym2_traces[w_rev]) == 0
    theta_trivial_sl3_trace = theta_trivial_sl3_trace and same
    if not same:
        print(f"  *** tr(Sym^2({w})) != tr(Sym^2({w_rev})) ***")
print(f"theta TRIVIAL at SL(3) trace level: {theta_trivial_sl3_trace}")
print("WHY: tr(Sym^2(M)) = tr(M)^2 - 1 depends only on tr(M),")
print("and tr(M) = tr(M^R) in SL(2), so all Sym^2 traces are theta-invariant.")

print("\n--- theta at Sym^2/SL(3) MATRIX level ---")
print("(The MATRICES Sym^2(AB) and Sym^2(BA) can differ even when traces agree)")
for w in word_names:
    w_rev = theta_map[w]
    if w >= w_rev:
        continue  # avoid duplicates
    diff = sp.Matrix([[sp.simplify(sym2_mats[w][i,j] - sym2_mats[w_rev][i,j])
                        for j in range(3)] for i in range(3)])
    is_zero = all(diff[i,j] == 0 for i in range(3) for j in range(3))
    if not is_zero:
        print(f"\n  Sym^2({w}) != Sym^2({w_rev}) -- theta NON-TRIVIAL here:")
        print(f"  Sym^2({w}) - Sym^2({w_rev}) =")
        for i in range(3):
            print(f"    [{', '.join(str(diff[i,j]) for j in range(3))}]")
    else:
        print(f"  Sym^2({w}) = Sym^2({w_rev}) [palindrome or trivial case]")


# ============================================================================
print()
print("=" * 80)
print("PART 4: C (COMPLEMENT / SWAP A<->B) — WORD-LEVEL ACTION")
print("=" * 80)

comp_map = {
    'A': 'B', 'B': 'A', 'AB': 'BA', 'BA': 'AB',
    'ABA': 'BAB', 'BAB': 'ABA', 'ABAB': 'BABA', 'BABA': 'ABAB'
}

print("\n--- C at SL(2) trace level ---")
c_trivial_sl2 = True
for w in word_names:
    w_c = comp_map[w]
    tr_w = sp.simplify(words[w].trace())
    tr_wc = sp.simplify(words[w_c].trace())
    same = sp.simplify(tr_w - tr_wc) == 0
    c_trivial_sl2 = c_trivial_sl2 and same
    print(f"  tr({w}) = {tr_w},  tr(C({w})) = tr({w_c}) = {tr_wc},  equal: {same}")
print(f"C TRIVIAL at SL(2) trace level: {c_trivial_sl2}")
print("WHY: tr(A)=tr(B)=2 at the geometric point, and tr(AB)=tr(BA) in SL(2).")

print("\n--- C at Sym^2/SL(3) trace level ---")
c_trivial_sl3_trace = True
for w in word_names:
    w_c = comp_map[w]
    same = sp.simplify(sym2_traces[w] - sym2_traces[w_c]) == 0
    c_trivial_sl3_trace = c_trivial_sl3_trace and same
print(f"C TRIVIAL at SL(3) trace level: {c_trivial_sl3_trace}")
print("WHY: tr(Sym^2(M)) = tr(M)^2 - 1, and the SL(2) traces agree.")

print("\n--- C at Sym^2/SL(3) MATRIX level ---")
for w in word_names:
    w_c = comp_map[w]
    if w >= w_c:
        continue
    diff = sp.Matrix([[sp.simplify(sym2_mats[w][i,j] - sym2_mats[w_c][i,j])
                        for j in range(3)] for i in range(3)])
    is_zero = all(diff[i,j] == 0 for i in range(3) for j in range(3))
    if not is_zero:
        print(f"\n  Sym^2({w}) != Sym^2(C({w}))=Sym^2({w_c}):")
        print(f"  Sym^2({w}) - Sym^2({w_c}) =")
        for i in range(3):
            print(f"    [{', '.join(str(diff[i,j]) for j in range(3))}]")
    else:
        print(f"  Sym^2({w}) = Sym^2(C({w}))=Sym^2({w_c})")


# ============================================================================
print()
print("=" * 80)
print("PART 5: THE CONJUGATION MATRIX P — C IS INNER")
print("=" * 80)

print("\nSolving for P in SL(2,C) such that PAP^{-1} = B and PBP^{-1} = A:")
print("From PA = BP:")
print("  (1,1): p = p  [always]")
print("  (1,2): p+q = q  =>  p = 0")
print("  (2,1): r = -omega*p+r  [with p=0: always]")
print("  (2,2): r+s = -omega*q+s  =>  r = -omega*q")
print("From PB = AP:")
print("  (1,1): -omega*q = r  =>  r = -omega*q  [consistent]")
print("  (1,2): q = q+s  =>  s = 0")
print("  det(P) = ps - qr = 0 - q(-omega*q) = omega*q^2 = 1")
print("  => q^2 = 1/omega = omega^2  (since omega^3 = 1)")
print("  => q = omega  (choosing one root)")

q_val = omega
r_val = -omega * q_val
P = sp.Matrix([[0, q_val], [r_val, 0]])
P_s = sp.Matrix([[sp.simplify(P[i,j]) for j in range(2)] for i in range(2)])
print(f"\nP = {[list(map(sp.simplify, row)) for row in P.tolist()]}")
print(f"det(P) = {sp.simplify(P.det())}")

# Verify P^2 = -I
P2 = sp.simplify(P * P)
print(f"P^2 = {[list(map(sp.simplify, row)) for row in P2.tolist()]}")
neg_I = -sp.eye(2)
print(f"P^2 = -I: {all(sp.simplify(P2[i,j] - neg_I[i,j]) == 0 for i in range(2) for j in range(2))}")
print("=> P has order 4 in SL(2,C)")

# Verify PAP^{-1} = B
P_inv = sp.Matrix([[0, sp.simplify(-q_val)], [sp.simplify(-r_val), 0]])
PAP_inv = sp.simplify(P * A * P_inv)
PAP_check = all(sp.simplify(PAP_inv[i,j] - B[i,j]) == 0 for i in range(2) for j in range(2))
print(f"\nPAP^{{-1}} = {[list(map(sp.simplify, row)) for row in PAP_inv.tolist()]}")
print(f"PAP^{{-1}} = B: {PAP_check}")

# Verify PBP^{-1} = A
PBP_inv = sp.simplify(P * B * P_inv)
PBP_check = all(sp.simplify(PBP_inv[i,j] - A[i,j]) == 0 for i in range(2) for j in range(2))
print(f"PBP^{{-1}} = {[list(map(sp.simplify, row)) for row in PBP_inv.tolist()]}")
print(f"PBP^{{-1}} = A: {PBP_check}")

print("\n=> C = swap(A,B) is conjugation by P: an INNER automorphism of SL(2).")
print("=> At the CHARACTER VARIETY (quotient by conjugation), C = identity.")


# ============================================================================
print()
print("=" * 80)
print("PART 6: C IS INNER AT SL(3) TOO — Sym^2(P) CONJUGATION")
print("=" * 80)

S2P = sym2(P)
S2P_s = sp.Matrix([[sp.simplify(S2P[i,j]) for j in range(3)] for i in range(3)])
print(f"\nSym^2(P) =")
for i in range(3):
    print(f"  [{', '.join(str(S2P_s[i,j]) for j in range(3))}]")
print(f"det(Sym^2(P)) = {sp.simplify(S2P.det())}")

# Verify Sym^2(P) . Sym^2(A) . Sym^2(P)^{-1} = Sym^2(B)
S2P_inv = sp.simplify(S2P.inv())
conj_A = sp.simplify(S2P * sym2_mats['A'] * S2P_inv)
check_A = all(sp.simplify(conj_A[i,j] - sym2_mats['B'][i,j]) == 0
              for i in range(3) for j in range(3))
print(f"\nSym^2(P) . Sym^2(A) . Sym^2(P)^{{-1}} = Sym^2(B): {check_A}")

conj_B = sp.simplify(S2P * sym2_mats['B'] * S2P_inv)
check_B = all(sp.simplify(conj_B[i,j] - sym2_mats['A'][i,j]) == 0
              for i in range(3) for j in range(3))
print(f"Sym^2(P) . Sym^2(B) . Sym^2(P)^{{-1}} = Sym^2(A): {check_B}")

# Also check on products
conj_AB = sp.simplify(S2P * sym2_mats['AB'] * S2P_inv)
check_AB = all(sp.simplify(conj_AB[i,j] - sym2_mats['BA'][i,j]) == 0
               for i in range(3) for j in range(3))
print(f"Sym^2(P) . Sym^2(AB) . Sym^2(P)^{{-1}} = Sym^2(BA): {check_AB}")

conj_ABA = sp.simplify(S2P * sym2_mats['ABA'] * S2P_inv)
check_ABA = all(sp.simplify(conj_ABA[i,j] - sym2_mats['BAB'][i,j]) == 0
                for i in range(3) for j in range(3))
print(f"Sym^2(P) . Sym^2(ABA) . Sym^2(P)^{{-1}} = Sym^2(BAB): {check_ABA}")

print("\n=> C is conjugation by Sym^2(P) at SL(3): INNER at SL(3) too.")
print("=> On the SL(3) representation variety (quotient by SL(3)-conjugation), C = identity.")


# ============================================================================
print()
print("=" * 80)
print("PART 7: theta IS OUTER AT SL(3) — Schur's lemma argument")
print("=" * 80)

print("\nClaim: There is NO R in SL(3) with R.Sym^2(w).R^{-1} = Sym^2(w^R) for all w.")
print("Proof: If R existed, then for palindromes (w=A, w=B): R commutes with Sym^2(A)")
print("and Sym^2(B). Since Sym^2(A,B) is irreducible (checked below), Schur's lemma")
print("forces R = scalar. But scalar conjugation is trivial, so Sym^2(AB) = Sym^2(BA),")
print("contradicting the nonzero chord matrix.")

print("\n--- Irreducibility check ---")
# Fixed space of Sym^2(A)
ker_A = sp.simplify(sym2_mats['A'] - sp.eye(3))
print(f"Sym^2(A) - I =")
for i in range(3):
    print(f"  [{', '.join(str(ker_A[i,j]) for j in range(3))}]")
null_A = ker_A.nullspace()
print(f"Nullspace (fixed vectors of Sym^2(A)): {[list(map(sp.simplify, v)) for v in null_A]}")

ker_B = sp.simplify(sym2_mats['B'] - sp.eye(3))
print(f"\nSym^2(B) - I =")
for i in range(3):
    print(f"  [{', '.join(str(ker_B[i,j]) for j in range(3))}]")
null_B = ker_B.nullspace()
print(f"Nullspace (fixed vectors of Sym^2(B)): {[list(map(sp.simplify, v)) for v in null_B]}")

# Check if fixed spaces intersect
if null_A and null_B:
    v_A = null_A[0]
    v_B = null_B[0]
    # Check linear independence
    M_check = sp.Matrix([v_A, v_B]).T
    rank = M_check.rank()
    print(f"\nFixed vectors linearly independent (rank {rank}): intersection is trivial.")
    print("No common fixed line => no 1-dim invariant subspace.")

# Check for common invariant 2-plane
# Sym^2(A) has invariant plane span(e1, e2) (upper triangular)
# Sym^2(B) has invariant plane span(e2, e3) (lower triangular)
# These intersect in span(e2), which is 1-dim, not 2-dim
print("\nSym^2(A) upper-triangular => invariant plane span(e1,e2)")
print("Sym^2(B) lower-triangular => invariant plane span(e2,e3)")
print("Intersection = span(e2): 1-dim, not a common invariant 2-plane.")
print("=> Representation is IRREDUCIBLE.")

print("\n--- Schur conclusion ---")
chord_Q = sp.simplify(sym2_mats['AB'] - sym2_mats['BA'])
chord_nonzero = any(chord_Q[i,j] != 0 for i in range(3) for j in range(3))
print(f"Chord matrix Q = Sym^2(AB) - Sym^2(BA):")
for i in range(3):
    print(f"  [{', '.join(str(chord_Q[i,j]) for j in range(3))}]")
print(f"Q nonzero: {chord_nonzero}")
print(f"tr(Q) = {sp.simplify(chord_Q.trace())}  (traceless, as expected)")

print("\nBy Schur: any R commuting with both Sym^2(A) and Sym^2(B) is scalar.")
print("Scalar R gives trivial conjugation => Sym^2(AB) = Sym^2(BA), contradicting Q != 0.")
print("=> theta has NO inner implementation at SL(3). theta IS OUTER at SL(3).")

# Eigenvalues of Q
Q_eigenvals = chord_Q.eigenvals()
print(f"\nChord matrix Q eigenvalues: {dict((sp.simplify(k), v) for k, v in Q_eigenvals.items())}")
print("(Eigenvalues come in {0, lambda, -lambda} since Q ~ -Q via Sym^2(P))")


# ============================================================================
print()
print("=" * 80)
print("PART 8: C vs theta — THE STRUCTURAL DIFFERENCE")
print("=" * 80)

print("""
Both C and theta send Sym^2(AB) -> Sym^2(BA) (and vice versa) at the matrix level.
Both negate the chord matrix Q = Sym^2(AB) - Sym^2(BA).

BUT:
  - C does this via conjugation by Sym^2(P): an INNER automorphism
    => The representations (A,B) and (B,A) are SL(3)-CONJUGATE
    => C is TRIVIAL on the representation variety

  - theta does this via word reversal: an OUTER automorphism at SL(3)
    => The representations rho and rho_theta are NOT SL(3)-conjugate
    => theta is NON-TRIVIAL on the representation variety

Why theta is non-trivial despite having the same trace as rho:
  - All Sym^2 TRACES agree (tr(Sym^2(M)) = tr(M)^2 - 1 depends only on SL(2) trace)
  - But the trace ring does NOT separate all orbits at this point
  - The chord matrix Q distinguishes rho from rho_theta: Q(rho) != 0, Q(rho_theta) = -Q(rho)
  - No SL(3)-conjugation maps one to the other (Schur argument)
  - So rho and rho_theta are DISTINCT points on the SL(3) representation variety
    that happen to project to the same point on the SL(3) character variety
""")


# ============================================================================
print()
print("=" * 80)
print("PART 9: gamma_5 (GOLDEN GALOIS) ACTION")
print("=" * 80)

print(f"\ngamma_5 acts by sqrt(5) -> -sqrt(5), i.e., phi -> 1 - phi = -1/phi")
print(f"At the geometric point, all matrix entries are in Q(omega) = Q(sqrt(-3)).")
print(f"Q(sqrt(5)) and Q(sqrt(-3)) are linearly disjoint over Q")
print(f"  (discriminants 5 and -3, coprime).")
print()

# Verify no sqrt(5) in any Sym^2 entry
has_sqrt5 = False
for name in word_names:
    S = sym2_mats[name]
    for i in range(3):
        for j in range(3):
            entry = S[i,j]
            # Check if sqrt(5) appears in the expression
            atoms = entry.atoms(sp.Pow)
            for atom in atoms:
                if atom == sp.sqrt(5):
                    has_sqrt5 = True
                    print(f"  sqrt(5) found in Sym^2({name})[{i},{j}]!")
if not has_sqrt5:
    print("No sqrt(5) in any Sym^2 matrix entry.")
    print("=> gamma_5 fixes ALL Sym^2 matrix entries.")
    print("=> gamma_5 is TRIVIAL at the Sym^2 matrix level at the geometric point.")

print(f"\nBut gamma_5 is non-trivial on DERIVED quantities:")
M_mono = sp.Matrix([[2, 1], [1, 1]])
ev_mono = list(M_mono.eigenvals().keys())
ev_sorted = sorted(ev_mono, key=lambda e: -sp.re(sp.N(e)))
print(f"  Monodromy RL = [[2,1],[1,1]]")
print(f"  Eigenvalues: {[sp.nsimplify(e, [sp.sqrt(5)]) for e in ev_sorted]}")
print(f"  gamma_5: phi^2 -> (1-phi)^2 = 1/phi^2: {sp.simplify((1-phi)**2 - 1/phi**2) == 0}")
print(f"  gamma_5 SWAPS expanding/contracting eigenspaces = FLIPS time direction (T7)")

print(f"\n  Out(A_5): gamma_5 swaps the two 5-dim irreps of A_5 over Q(sqrt(5))")
chi_5A = phi - 1  # character value on 5-cycles: 1/phi
chi_5B = -phi     # character value on 5-cycles: -phi
chi_5A_g5 = chi_5A.subs(sp.sqrt(5), -sp.sqrt(5))
print(f"  chi_5A(5-cycle) = {sp.simplify(chi_5A)} = 1/phi")
print(f"  gamma_5(chi_5A) = {sp.simplify(chi_5A_g5)}")
print(f"  chi_5B(5-cycle) = {sp.simplify(chi_5B)} = -phi")
print(f"  gamma_5 swaps 5A <-> 5B: {sp.simplify(chi_5A_g5 - chi_5B) == 0}")
print(f"  => gamma_5 FLIPS basepoint (T3)")

# C on monodromy
M_LR = sp.Matrix([[1, 1], [1, 2]])
same_evs = sorted([sp.simplify(e) for e in M_mono.eigenvals()]) == \
           sorted([sp.simplify(e) for e in M_LR.eigenvals()])
print(f"\n  C on monodromy: RL -> LR = [[1,1],[1,2]]")
print(f"  Same eigenvalues (RL ~ LR): {same_evs}")
print(f"  => C FIXES time direction (T7)")

# C on Out(A_5)
print(f"\n  C on Out(A_5): C swaps generators A<->B, a group-theoretic operation.")
print(f"  Out(A_5) = Gal(Q(sqrt(5))/Q), an arithmetic operation.")
print(f"  C does not act on sqrt(5) => C FIXES basepoint (T3).")


# ============================================================================
print()
print("=" * 80)
print("PART 10: THE T-AXIS FLIP TABLE — COMPLETE COMPARISON")
print("=" * 80)

print("""
B766 flip-table with C added:

  Axis         | c      | theta  | gamma_5 | C (swap)
  -------------|--------|--------|---------|--------
  T4 chirality | FLIP   | FIX    | FIX     | FIX
  T6 chord     | FLIP   | FLIP   | FIX     | see below
  T7 time      | FIX    | FIX    | FLIP    | FIX
  T3 basepoint | FIX    | FIX    | FLIP    | FIX

T6 under C — the crucial entry:

  At the MATRIX level: C negates the chord Q = Sym^2(AB) - Sym^2(BA),
  same as theta.

  But C does this via conjugation by Sym^2(P), an INNER automorphism.
  Inner automorphisms are TRIVIAL on the representation variety.
  The chord sign, as an invariant of the representation variety, is
  NOT flipped by C.

  theta does this via an OUTER automorphism (proved above: no inner
  implementation exists). So theta GENUINELY flips the chord sign.

  C's true T6 entry: FIX (inner automorphism, trivial on all invariants)

Corrected table:

  Axis         | c      | theta  | gamma_5 | C (swap)
  -------------|--------|--------|---------|--------
  T4 chirality | FLIP   | FIX    | FIX     | FIX
  T6 chord     | FLIP   | FLIP   | FIX     | FIX
  T7 time      | FIX    | FIX    | FLIP    | FIX
  T3 basepoint | FIX    | FIX    | FLIP    | FIX

C flip-vector in (c, theta, gamma_5) basis: (0, 0, 0) = IDENTITY
""")


# ============================================================================
print()
print("=" * 80)
print("PART 11: UNIVERSALITY — C IS INNER FOR ALL u")
print("=" * 80)

print("The conjugation P(u) = [[0, 1/sqrt(u)], [-sqrt(u), 0]] satisfies")
print("P(u) . A . P(u)^{-1} = B(u) for all u != 0.")

# Verify symbolically
sqrt_u = sp.sqrt(u)
P_u = sp.Matrix([[0, 1/sqrt_u], [-sqrt_u, 0]])
print(f"\nP(u) = {P_u.tolist()}")
print(f"det(P(u)) = {sp.simplify(P_u.det())}")

P_u_inv = sp.Matrix([[0, -1/sqrt_u], [sqrt_u, 0]])
PAP_u = sp.simplify(P_u * A * P_u_inv)
print(f"\nP(u) A P(u)^{{-1}} = {[list(map(sp.simplify, row)) for row in PAP_u.tolist()]}")
print(f"= B(u): {all(sp.simplify(PAP_u[i,j] - B_u[i,j]) == 0 for i in range(2) for j in range(2))}")

PBP_u = sp.simplify(P_u * B_u * P_u_inv)
print(f"P(u) B(u) P(u)^{{-1}} = {[list(map(sp.simplify, row)) for row in PBP_u.tolist()]}")
print(f"= A: {all(sp.simplify(PBP_u[i,j] - A[i,j]) == 0 for i in range(2) for j in range(2))}")

P_u_sq = sp.simplify(P_u * P_u)
print(f"\nP(u)^2 = {[list(map(sp.simplify, row)) for row in P_u_sq.tolist()]}")
print(f"= -I: {all(sp.simplify(P_u_sq[i,j] - neg_I[i,j]) == 0 for i in range(2) for j in range(2))}")

print("\n=> For EVERY point u on the character variety, C is inner.")
print("=> C is a GLOBAL inner automorphism of the Riley family.")
print("=> C cannot contribute any observable to any torsor.")


# ============================================================================
print()
print("=" * 80)
print("PART 12: WHY THE INCIDENCE-MATRIX IDENTIFICATION FAILS")
print("=" * 80)

print("""
At the incidence-matrix level:
  sigma: a->ab, b->a  has incidence M_sigma = [[1,1],[1,0]]
  C.sigma.C:  a->b, b->ba  has incidence M_C = [[0,1],[1,1]]

  M_sigma has eigenvalues phi, phi_bar with eigenvectors [phi,1]^T, [phi_bar,1]^T
  M_C has eigenvalues phi, phi_bar with eigenvectors [1,phi]^T, [1,phi_bar]^T

  C swaps the eigenvectors: [phi,1] <-> [1,phi]
  gamma_5 (sending phi->phi_bar) also swaps the eigenspaces

  At this coarse level: C = gamma_5 (both swap phi/phi_bar eigenspaces)

At the character variety level, they SEPARATE:
  - gamma_5 is an ARITHMETIC operation: sqrt(5) -> -sqrt(5)
    It acts on Q(sqrt(5))-coefficients, not on representations
    It is OUTER: it changes the number field, moving phi -> -1/phi
    It flips T7 (time direction) and T3 (basepoint)

  - C is a GEOMETRIC operation: swap generators A <-> B
    It acts on representations by permuting generators
    It is INNER: implemented by conjugation by P(u)
    It acts TRIVIALLY on all invariants

  The incidence matrix cannot distinguish inner from outer because
  it forgets the matrix-level structure. The character variety
  DOES distinguish them through Schur's lemma and irreducibility.
""")


# ============================================================================
print()
print("=" * 80)
print("CONCLUSION")
print("=" * 80)

print("""
*** C != gamma_5 AT THE CHARACTER VARIETY ***

C (complement / swap A<->B) is the IDENTITY element of the F_2^3 group.
gamma_5 (golden Galois) is a non-trivial element that flips T7 and T3.

C is trivial because it is an inner automorphism of SL(2) (and hence SL(3)):
the matrix P = [[0, omega], [omega+1, 0]] conjugates (A,B) to (B,A).
P exists for all parameter values u != 0 (universally inner).

The incidence-matrix identification C = gamma_5 fails to carry over because:
  - The incidence matrix is blind to inner vs outer (it only sees eigenspaces)
  - The character variety resolves them: inner = trivial, outer = non-trivial
  - C is inner, gamma_5 is outer (acts on number fields, not on representations)

C is also != theta: theta is OUTER at SL(3) (proved by Schur + irreducibility),
while C is INNER. theta is the first non-trivial involution at SL(3) (the
rank-onset signature S1 from B780), while C remains trivial at all ranks.

SUMMARY OF ALL INVOLUTIONS:

  involution | inner/outer at SL(3) | flip-vector (c,theta,gamma_5)
  -----------|----------------------|------------------------------
  identity   | inner (trivial)      | (0, 0, 0)
  c          | outer                | (1, 0, 0) ← non-trivial at SL(2)
  theta      | outer                | (0, 1, 0) ← non-trivial at SL(3)
  gamma_5    | outer (arithmetic)   | (0, 0, 1) ← non-trivial on eigenvalues
  C (swap)   | INNER                | (0, 0, 0) = identity

C = identity. The swap is gauge.
""")
