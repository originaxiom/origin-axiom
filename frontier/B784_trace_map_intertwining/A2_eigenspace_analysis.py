#!/usr/bin/env python3
"""B784 Agent A2: Incidence-matrix eigenspace analysis.

Tests whether C = gamma_5 at the linear (incidence-matrix) level.
Negatives first: reports what FAILS before what passes.
"""

from sympy import (Matrix, sqrt, Rational, simplify, eye, symbols,
                   factor, expand, S, nsimplify)

phi = Rational(1,2) + sqrt(5)/2
phi_bar = Rational(1,2) - sqrt(5)/2  # = -1/phi

results = {}  # label -> (bool, detail)

def record(label, val, detail=""):
    results[label] = (val, detail)
    tag = "PASS" if val else "FAIL"
    print(f"  [{tag}]  {label}")
    if detail:
        for line in detail.strip().split('\n'):
            print(f"         {line}")

print("=" * 72)
print("B784  INCIDENCE-MATRIX EIGENSPACE ANALYSIS")
print("=" * 72)

# ──────────────────────────────────────────────────────────────────────
# 1. Define matrices
# ──────────────────────────────────────────────────────────────────────
print("\n--- 1. INCIDENCE MATRICES ---")
M_sigma = Matrix([[1, 1], [1, 0]])
M_CsC   = Matrix([[0, 1], [1, 1]])
C       = Matrix([[0, 1], [1, 0]])  # complement swap

print(f"  M_sigma = {M_sigma.tolist()}")
print(f"  M_CsC   = {M_CsC.tolist()}")
print(f"  C        = {C.tolist()}")

# ──────────────────────────────────────────────────────────────────────
# 2. Reversal invisibility
# ──────────────────────────────────────────────────────────────────────
print("\n--- 2. REVERSAL INVISIBILITY ---")
M_sigma_mirror = Matrix([[1, 1], [1, 0]])
M_RCsCR = Matrix([[0, 1], [1, 1]])
record("2a: M_sigma == M_sigma_mirror", M_sigma == M_sigma_mirror,
       "WHY trivial: abelianisation kills word order.")
record("2b: M_CsC == M_RCsCR", M_CsC == M_RCsCR,
       "Same reason: reversal permutes letters within a word, not counts.")

# ──────────────────────────────────────────────────────────────────────
# 3. Eigenvalues
# ──────────────────────────────────────────────────────────────────────
print("\n--- 3. EIGENVALUES ---")
lam = symbols('lambda')
cp_sigma = M_sigma.charpoly(lam).as_expr()
cp_CsC   = M_CsC.charpoly(lam).as_expr()
record("3a: same char poly", simplify(cp_sigma - cp_CsC) == 0,
       f"Both = {cp_sigma}")

evals_sigma = sorted(M_sigma.eigenvals().keys(), key=lambda x: float(x.evalf()))
evals_CsC   = sorted(M_CsC.eigenvals().keys(), key=lambda x: float(x.evalf()))

check_phi = simplify(evals_sigma[1] - phi) == 0 and simplify(evals_sigma[0] - phi_bar) == 0
record("3b: eigenvalues are phi, phi_bar", check_phi,
       f"phi = {phi},  phi_bar = {phi_bar}")
record("3c: -1/phi == phi_bar", simplify(-1/phi - phi_bar) == 0)

# ──────────────────────────────────────────────────────────────────────
# 4. Eigenvectors
# ──────────────────────────────────────────────────────────────────────
print("\n--- 4. EIGENVECTORS ---")

def get_evec(M, eigenval):
    """Return ONE eigenvector of M for the given eigenvalue."""
    for ev, mult, vecs in M.eigenvects():
        if simplify(ev - eigenval) == 0:
            return vecs[0]
    raise ValueError(f"No eigenvector for {eigenval}")

v_sigma_phi    = get_evec(M_sigma, phi)
v_sigma_phibar = get_evec(M_sigma, phi_bar)
v_CsC_phi     = get_evec(M_CsC, phi)
v_CsC_phibar  = get_evec(M_CsC, phi_bar)

def proportional(u, v):
    """Check if 2-vectors u and v are proportional (2D cross product = 0)."""
    return simplify(u[0]*v[1] - u[1]*v[0]) == 0

record("4a: v_phi(M_sigma) ~ [phi, 1]", proportional(v_sigma_phi, Matrix([phi, 1])),
       f"SymPy returns {v_sigma_phi.T.tolist()[0]}")
record("4b: v_phibar(M_sigma) ~ [phi_bar, 1]", proportional(v_sigma_phibar, Matrix([phi_bar, 1])),
       f"SymPy returns {v_sigma_phibar.T.tolist()[0]}")
record("4c: v_phi(M_CsC) ~ [1, phi]", proportional(v_CsC_phi, Matrix([1, phi])),
       f"SymPy returns {v_CsC_phi.T.tolist()[0]}")
record("4d: v_phibar(M_CsC) ~ [1, phi_bar]", proportional(v_CsC_phibar, Matrix([1, phi_bar])),
       f"SymPy returns {v_CsC_phibar.T.tolist()[0]}")

# ──────────────────────────────────────────────────────────────────────
# 5. Conjugation M_CsC = C M_sigma C
# ──────────────────────────────────────────────────────────────────────
print("\n--- 5. CONJUGATION AND INTERTWINING ---")
record("5a: M_CsC = C * M_sigma * C", C * M_sigma * C == M_CsC)

Cv_phi = C * Matrix([phi, 1])
Cv_phibar = C * Matrix([phi_bar, 1])
record("5b: C * v_phi(sigma) ~ v_phi(CsC)", proportional(Cv_phi, Matrix([1, phi])),
       f"C * [phi,1] = {Cv_phi.T.tolist()[0]}")
record("5c: C * v_phibar(sigma) ~ v_phibar(CsC)", proportional(Cv_phibar, Matrix([1, phi_bar])),
       f"C * [phi_bar,1] = {Cv_phibar.T.tolist()[0]}")

print("\n  => C maps eigenvectors of M_sigma to eigenvectors of M_CsC,")
print("     PRESERVING the eigenvalue label (phi stays phi, phi_bar stays phi_bar).")

# ──────────────────────────────────────────────────────────────────────
# 6. The critical test: C in the eigenbasis
# ──────────────────────────────────────────────────────────────────────
print("\n--- 6. C IN THE EIGENBASIS OF M_sigma (THE CRITICAL TEST) ---")

P = Matrix([[phi, phi_bar], [1, 1]])
P_inv = P.inv()
C_eig = simplify(P_inv * C * P)

print(f"  P (eigenvector columns) = [[phi, phi_bar], [1, 1]]")
print(f"  det(P) = {simplify(P.det())} = sqrt(5)")
print(f"  P^(-1) * C * P =")
for i in range(2):
    row = [simplify(C_eig[i,j]) for j in range(2)]
    print(f"    {row}")

swap = Matrix([[0,1],[1,0]])
is_swap = simplify(C_eig - swap) == Matrix.zeros(2,2)
record("6a: C in eigenbasis == swap [[0,1],[1,0]]", is_swap,
       "THIS IS THE CLAIM 'C = gamma_5'.  If FALSE, C does NOT simply swap eigenspaces.")

# Detailed analysis of what C_eig actually is
print("\n  DETAILED ANALYSIS of C in eigenbasis:")
print(f"  tr(C_eig) = {simplify(C_eig.trace())}")
print(f"  det(C_eig) = {simplify(C_eig.det())}")
print(f"  C_eig^2 = {simplify(C_eig**2)}")
is_involution = simplify(C_eig**2 - eye(2)) == Matrix.zeros(2,2)
record("6b: C_eig is an involution (C_eig^2 = I)", is_involution)

print(f"\n  Since tr=0, det=-1: eigenvalues of C_eig are +1 and -1.")
print(f"  C_eig IS a reflection/involution, but NOT the swap of eigenspaces.")

# What IS the +1 eigenvector of C_eig?
# C fixes [1,1] in the standard basis.  In the eigenbasis:
# P^(-1) [1,1]^T
v_fixed_eig = simplify(P_inv * Matrix([1,1]))
print(f"\n  +1 eigenvector of C (i.e. [1,1]) in eigenbasis: {v_fixed_eig.T.tolist()[0]}")
# And the -1 eigenvector [1,-1]:
v_neg_eig = simplify(P_inv * Matrix([1,-1]))
print(f"  -1 eigenvector of C (i.e. [1,-1]) in eigenbasis: {v_neg_eig.T.tolist()[0]}")

# ──────────────────────────────────────────────────────────────────────
# 6'. Direct gamma_5 vs C comparison on eigenvectors
# ──────────────────────────────────────────────────────────────────────
print("\n--- 6'. DIRECT COMPARISON: C vs gamma_5 ON EIGENSPACES ---")

print("  gamma_5 acts on Q(sqrt(5)) by sqrt(5) -> -sqrt(5), i.e. phi -> phi_bar.")
print("  It maps eigenvector [phi, 1] of M_sigma to [phi_bar, 1] of M_sigma.")
print("  gamma_5 SWAPS eigenvalues: the phi-eigenvector becomes the phi_bar-eigenvector.")
print()
print("  C acts on R^2 by [x,y] -> [y,x].")
print("  It maps eigenvector [phi, 1] of M_sigma to [1, phi], which is the")
print("  phi-eigenvector of M_CsC (a DIFFERENT matrix).")
print("  C PRESERVES eigenvalues: the phi-eigenvector stays a phi-eigenvector.")

# Are the IMAGE LINES the same?
# gamma_5([phi,1]) = [phi_bar, 1] -> line with slope 1/phi_bar = -phi
# C([phi,1]) = [1, phi] -> line with slope phi
print(f"\n  Image of [phi, 1]:")
print(f"    under gamma_5: [phi_bar, 1],  slope = 1/phi_bar = -phi")
print(f"    under C:       [1, phi],      slope = phi")
print(f"    These are DIFFERENT lines (slopes -phi vs phi).")

record("6c: C([phi,1]) ~ gamma_5([phi,1])",
       proportional(Matrix([1, phi]), Matrix([phi_bar, 1])),
       "gamma_5([phi,1]) = [phi_bar,1], C([phi,1]) = [1,phi]. NOT proportional.")

# ──────────────────────────────────────────────────────────────────────
# 6''. Check the frequency claim from the task
# ──────────────────────────────────────────────────────────────────────
print("\n--- 6''. FREQUENCY VECTOR UNDER C vs gamma_5 ---")

freq_a = 1/phi           # = (sqrt(5)-1)/2
freq_b = 1/phi**2        # = (3-sqrt(5))/2

print(f"  PF frequencies of M_sigma: freq(a) = 1/phi = {simplify(freq_a)}")
print(f"                              freq(b) = 1/phi^2 = {simplify(freq_b)}")

# Under C: swap a <-> b
c_freq_a = freq_b
c_freq_b = freq_a
print(f"  Under C: freq(a) -> {simplify(c_freq_a)}, freq(b) -> {simplify(c_freq_b)}")

# Under gamma_5: sqrt(5) -> -sqrt(5)
g5_freq_a = simplify(freq_a.subs(sqrt(5), -sqrt(5)))
g5_freq_b = simplify(freq_b.subs(sqrt(5), -sqrt(5)))
print(f"  Under gamma_5: freq(a) -> {g5_freq_a}, freq(b) -> {g5_freq_b}")

record("6d: C on frequencies == gamma_5 on frequencies",
       simplify(c_freq_a - g5_freq_a) == 0 and simplify(c_freq_b - g5_freq_b) == 0,
       f"C gives ({simplify(c_freq_a)}, {simplify(c_freq_b)}), "
       f"gamma_5 gives ({g5_freq_a}, {g5_freq_b}). "
       f"gamma_5(1/phi) = -phi (negative!), not 1/phi^2.")

# ──────────────────────────────────────────────────────────────────────
# 7. What IS true: C * P_sigma = P_CsC
# ──────────────────────────────────────────────────────────────────────
print("\n--- 7. WHAT IS TRUE: STRUCTURAL INTERTWINING ---")

P_sigma = Matrix([[phi, phi_bar], [1, 1]])
P_CsC = Matrix([[1, 1], [phi, phi_bar]])
CP = simplify(C * P_sigma)
record("7a: C * P_sigma == P_CsC (row swap of eigenvector matrix)",
       simplify(CP - P_CsC) == Matrix.zeros(2,2),
       "C acts on P by swapping rows <=> swapping generators a,b.")

record("7b: C^2 = I (involution)", C * C == eye(2))

# ──────────────────────────────────────────────────────────────────────
# 8. The precise relationship: C and gamma_5 implement DIFFERENT Z/2 actions
# ──────────────────────────────────────────────────────────────────────
print("\n--- 8. PRECISE RELATIONSHIP ---")

print("  The eigenspace decomposition of M_sigma gives two invariant lines:")
print(f"    L_phi     = span([phi, 1])     slope = 1/phi = {simplify(1/phi)}")
print(f"    L_phibar  = span([phi_bar, 1]) slope = 1/phi_bar = {simplify(1/phi_bar)}")
print()
print("  gamma_5 acts WITHIN M_sigma's eigenspaces:")
print("    L_phi -> L_phibar  (swaps the two lines of the SAME matrix)")
print("    Eigenvalue label CHANGES: phi -> phi_bar")
print()
print("  C acts BETWEEN the two substitutions:")
print("    L_phi(M_sigma) -> L_phi(M_CsC)  (maps to eigenvector of DIFFERENT matrix)")
print("    Eigenvalue label PRESERVED: phi -> phi")
print()
print("  These are different Z/2 actions on the eigenspace data.")
print("  gamma_5 is 'vertical' (moves between eigenvalue strata).")
print("  C is 'horizontal' (moves between substitution matrices).")

# ──────────────────────────────────────────────────────────────────────
# 9. Where C = gamma_5 MIGHT hold
# ──────────────────────────────────────────────────────────────────────
print("\n--- 9. WHERE C = gamma_5 MIGHT STILL HOLD ---")
print("  The incidence matrix is a SHADOW (abelianisation) of the substitution.")
print("  At higher levels:")
print("    - SL(2) trace map T_sigma(x,y,z) = (z, x, xz-y): C and gamma_5")
print("      could coincide on the Suto surface x^2+y^2+z^2-2xyz-1 = 0.")
print("    - Character variety of m004: the geometric point has")
print("      tr(A)=tr(B)=2, so C (swapping A,B) is trivially the identity.")
print("      gamma_5 might act non-trivially on other points of the variety.")
print("    - SL(3) Sym^2 traces: reversal theta becomes non-trivial,")
print("      which could change the C-vs-gamma_5 comparison.")

# ──────────────────────────────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)

passes = sum(1 for v, _ in results.values() if v)
fails  = sum(1 for v, _ in results.values() if not v)

print(f"\n  {passes} PASS, {fails} FAIL out of {len(results)} checks.\n")

if fails > 0:
    print("  FAILURES (negatives first):")
    for label, (val, detail) in results.items():
        if not val:
            print(f"    [FAIL] {label}")

print()
for label, (val, detail) in results.items():
    tag = "PASS" if val else "FAIL"
    print(f"  [{tag}]  {label}")

print(f"""
  CONCLUSION:
  -----------
  PROVED:
    (a) Reversal R is invisible at incidence-matrix level (trivial).
    (b) C conjugates M_sigma to M_CsC, preserving eigenvalues phi, phi_bar.
    (c) C * P_sigma = P_CsC: C swaps generator labels (rows of eigenvector matrix).
    (d) C is an involution, as is gamma_5.

  NOT PROVED (NEGATIVE):
    (e) C in the eigenbasis of M_sigma is NOT the swap matrix.
        It is a reflection with tr=0, det=-1, but its axis is [1,1]
        (the fixed point of the generator swap), not the diagonal of the
        eigenbasis.  C does not swap the phi and phi_bar eigenspaces.
    (f) C and gamma_5 act differently on eigenvectors:
        gamma_5([phi,1]) = [phi_bar, 1]  (swaps eigenvalue labels)
        C([phi,1])       = [1, phi]      (preserves eigenvalue labels)
        These map to DIFFERENT lines in R^2.
    (g) C and gamma_5 act differently on frequencies:
        gamma_5(1/phi) = -phi (negative, not a frequency)
        C(1/phi) = 1/phi^2 (positive, the other frequency)

  STATUS: The claim "C = gamma_5 at the incidence-matrix level" is FALSE
  in the precise sense of eigenspace-swapping.  C and gamma_5 are
  genuinely different Z/2 actions.  The question "C = gamma_5 at the
  character variety?" remains OPEN and cannot be settled at this level.
""")
