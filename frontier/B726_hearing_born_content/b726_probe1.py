#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B726 / PROBE 1 -- is "being=diagonal/collapse vs hearing=off-diagonal/unitary" a
genuine structural dichotomy?

Prereg (B726, probe 1): B725 found the BEING face (Q(sqrt-3), CMR/thermal KMS) gives
the Born FORM + classical DIAGONAL Gibbs weights but NOT the Born CONTENT (interference
+ non-uniform pure |amp|^2). Hypothesis: the hearing face (Q(sqrt5), the golden
monodromy A with A^2=M; the Fibonacci MTC) supplies the missing OFF-DIAGONAL/coherent
structure. Two-outcome:
   A = the hearing is the unitary/coherent OFF-DIAGONAL face the being (diagonal) is not;
   B = no genuine split (hearing also effectively diagonal, or being also off-diagonal).

Firewall (binding): structural / operator-algebra / MTC ONLY. No physics claim beyond
the structural QM-composition account; no SM value; observer's choice free (B701).
COMPUTE-NOT-CITE: every discriminating fact recomputed here in-sandbox to machine
precision; no B-number asserted as proof. BASE-RATE DISCIPLINE: a real quadratic field
having an S-matrix-like object, or a squaring identity resembling |psi|^2, is NOT
automatically a match -- state the discriminating operation and reject look-elsewhere.

The four computations
---------------------
 (a) BEING is DIAGONAL. Gibbs/KMS state rho_beta = e^{-beta H}/Z. Verify [rho,H]=0 so
     rho is diagonal in the energy/pointer basis (zero off-diagonal coherence), that
     its diagonal entries are REAL Gibbs probabilities (a STATE), and contrast with a
     coherent superposition whose off-diagonal l1-coherence is strictly > 0. Re-verify
     the B725 structure, non-vacuously.

 (b) The bare 2x2 golden monodromy A=[[1,1],[1,0]]. Verify A^2 = M=[[2,1],[1,1]] (cat
     map), det A = -1, A real symmetric. Eigenvalues phi, -1/phi (REAL, OFF the unit
     circle); eigenvectors orthogonal. DISCRIMINATOR/BASE-RATE GUARD: is A unitary or
     conjugate-to-unitary? A matrix is conjugate to a unitary iff diagonalizable with
     ALL eigenvalues on the unit circle. Test it. If A's spectrum is off the unit
     circle, A is Anosov/hyperbolic (a CLASSICAL chaotic map) -- NOT the unitary face.
     This guards against the false pattern-match "A^2=M ~ |psi|^2".

 (c) The Fibonacci MTC braid representation (the REAL locus of "unitary/coherent"). On
     the 2-dim fusion space of three tau anyons, build sigma1 = R-matrix
     diag(e^{-4pi i/5}, e^{3pi i/5}) and sigma2 = F sigma1 F with the Fibonacci
     F-matrix. Verify: sigma1, sigma2 UNITARY; sigma2 genuinely OFF-DIAGONAL (nonzero
     off-diagonal entries -> mixes fusion channels -> interference); [sigma1,sigma2]!=0
     (non-abelian mixing); Yang-Baxter sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2 (a
     genuine braid-group rep). This is where the unitary OFF-DIAGONAL coherence lives.

 (d) THE DISCRIMINATING CONTRAST. Coherence measure C_l1(X) = sum_{i!=j}|X_ij| in the
     pointer basis. Being (thermal rho): C=0, diagonal REAL probabilities. Bare A: real,
     hyperbolic, diagonal in its OWN eigenbasis, NOT unitary. Braid sigma2: unitary with
     C>0, complex entries -> genuine off-diagonal coherence the diagonal being lacks.
     Verdict on the two-outcome, honestly bounded.

Outputs mirrored to b726_probe1_out.txt.
"""

import numpy as np
import sympy as sp

np.random.seed(726)
np.set_printoptions(precision=6, suppress=True, linewidth=120)

_LINES = []
def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    _LINES.append(s)

def herm(n):
    """random Hermitian n x n"""
    X = np.random.randn(n, n) + 1j*np.random.randn(n, n)
    return (X + X.conj().T) / 2

def l1_coherence(X, basis=None):
    """l1 off-diagonal coherence in the given orthonormal basis (cols of `basis`).
       If basis given, express X in that basis first: B^dag X B."""
    if basis is not None:
        X = basis.conj().T @ X @ basis
    n = X.shape[0]
    off = X.copy()
    for i in range(n):
        off[i, i] = 0.0
    return np.abs(off).sum()

out("="*78)
out("B726 / PROBE 1 -- being=diagonal/collapse  vs  hearing=off-diagonal/unitary")
out("="*78)

# ============================================================================
# PART (a) -- BEING is DIAGONAL: thermal KMS state has zero off-diagonal coherence
# ============================================================================
out("")
out("="*78)
out("PART (a) -- BEING (thermal KMS / Q(sqrt-3), B725): DIAGONAL, no coherence")
out("="*78)
out("Gibbs/KMS state rho_beta = e^{-beta H}/Z. Structural claim: [rho,H]=0 so rho is")
out("diagonal in the ENERGY/POINTER basis -> zero off-diagonal coherence; its diagonal")
out("entries are REAL Gibbs probabilities (a decohered STATE). Non-vacuous: contrast a")
out("coherent superposition whose off-diagonal l1-coherence is strictly > 0.")
out("")

for n in (2, 3, 5):
    H = herm(n)
    E, V = np.linalg.eigh(H)          # V columns = energy eigenbasis (pointer basis)
    beta = 1.0
    w = np.exp(-beta * E)
    Z = w.sum()
    p = w / Z                          # Gibbs probabilities
    # rho in the ORIGINAL basis:
    rho = V @ np.diag(p) @ V.conj().T
    # commutator with H:
    comm = rho @ H - H @ rho
    # rho expressed in the ENERGY/POINTER basis:
    rho_pb = V.conj().T @ rho @ V
    offdiag_pb = l1_coherence(rho, basis=V)
    diag_pb = np.real(np.diag(rho_pb))
    out(f"n={n}:")
    out(f"   ||[rho,H]||                       = {np.linalg.norm(comm):.3e}   (=> commutes)")
    out(f"   l1 off-diag coherence in POINTER  = {offdiag_pb:.3e}   (=> DIAGONAL)")
    out(f"   diag(rho) in pointer basis (p_i)  = {np.round(diag_pb,6)}")
    out(f"   diag real & = Gibbs p_i?          = {np.allclose(diag_pb, p) and np.allclose(np.imag(np.diag(rho_pb)),0)}")
    out(f"   sum p_i                           = {diag_pb.sum():.15f}")
    # contrast: a coherent superposition of energy eigenstates
    c = (np.random.randn(n) + 1j*np.random.randn(n)); c /= np.linalg.norm(c)
    psi = V @ c                         # equal-ish superposition in energy basis
    rho_pure = np.outer(psi, psi.conj())
    out(f"   [contrast] pure superposition l1 off-diag coherence in POINTER = {l1_coherence(rho_pure, basis=V):.4f}  (>0 => coherent)")
    out("")

out(">> (a) CONFIRMED: the being's thermal KMS state is DIAGONAL in the pointer basis")
out("   ([rho,H]=0, off-diagonal coherence = 0), carrying REAL Gibbs probabilities --")
out("   a decohered STATE. A coherent superposition (nonzero off-diagonals) is a")
out("   DIFFERENT object the thermal being does not contain. (Re-verifies B725.)")

# ============================================================================
# PART (b) -- the bare 2x2 golden cat map A: real, hyperbolic, NOT unitary
# ============================================================================
out("")
out("="*78)
out("PART (b) -- the bare 2x2 golden monodromy A=[[1,1],[1,0]]  (BASE-RATE GUARD)")
out("="*78)

A = sp.Matrix([[1, 1], [1, 0]])
M = sp.Matrix([[2, 1], [1, 1]])
A2 = A*A
out(f"A          = {A.tolist()}")
out(f"A^2        = {A2.tolist()}")
out(f"M          = {M.tolist()}")
out(f"A^2 == M ?                 {A2 == M}")
out(f"det A                      = {A.det()}")
out(f"A symmetric (A == A^T)?    {A == A.T}   (real symmetric => self-adjoint)")
out(f"trace A                    = {A.trace()}")

phi = sp.Rational(1,2) + sp.sqrt(5)/2
eigs = A.eigenvects()          # list of (eigenvalue, mult, [eigvecs])
out("")
out("Eigenstructure (exact):")
lam_list = []
for val, mult, vecs in eigs:
    val_s = sp.simplify(val)
    lam_list.append(val_s)
    v = vecs[0]
    out(f"   eigenvalue = {val_s}   (~ {float(val_s):+.6f}),  eigenvector = {v.T.tolist()}")
# name them
out(f"   phi = (1+sqrt5)/2 ~ {float(phi):.6f} ;  -1/phi = (1-sqrt5)/2 ~ {float(1-phi):.6f}")
out(f"   product of eigenvalues = det = {sp.simplify(sp.prod(lam_list))}")
# orthogonality of eigenvectors
v1 = eigs[0][2][0]; v2 = eigs[1][2][0]
dot = sp.simplify((v1.T * v2)[0])
out(f"   eigenvectors orthogonal? <v1|v2> = {dot}   (=> {dot==0})")

# unit-circle test / conjugate-to-unitary test
out("")
out("BASE-RATE GUARD -- is A unitary, or CONJUGATE to a unitary?")
out("A matrix is conjugate to a unitary  <=>  diagonalizable with ALL eigenvalues on")
out("the unit circle |lambda|=1. Test A's spectrum:")
mods = [sp.Abs(l) for l in lam_list]
on_circle = [sp.simplify(m-1)==0 for m in mods]
for l, m, oc in zip(lam_list, mods, on_circle):
    out(f"   |{l}| = {sp.nsimplify(m)} ~ {float(m):.6f}   on unit circle? {oc}")
Anum = np.array(A.tolist(), dtype=float)
# is A^T A = I (orthogonal/unitary on standard inner product)?
out(f"   A^T A == I (unitary on std inner product)?  {np.allclose(Anum.T@Anum, np.eye(2))}")
out(f"   => A conjugate to a unitary?  {all(on_circle)}   (spectrum OFF the unit circle)")
out("")
out(">> (b) A is REAL SYMMETRIC, det=-1, eigenvalues phi & -1/phi OFF the unit circle:")
out("   A is ANOSOV/HYPERBOLIC (a CLASSICAL chaotic cat map), NOT unitary and NOT")
out("   conjugate to any unitary. Being self-adjoint it is diagonal in its OWN")
out("   orthonormal eigenbasis -- just like the thermal being. So the BARE A does NOT")
out("   by itself supply 'off-diagonal unitary coherence'. BASE-RATE VERDICT: 'A^2=M ~")
out("   |psi|^2' is a FALSE pattern-match at the matrix level (A is not unitary; A*A is")
out("   a real squeeze, not amp*conj(amp)). The unitary face must live elsewhere -> (c).")

# ============================================================================
# PART (c) -- the Fibonacci MTC braid representation: UNITARY + OFF-DIAGONAL
# ============================================================================
out("")
out("="*78)
out("PART (c) -- Fibonacci MTC braid rep (Q(sqrt5) golden): UNITARY + OFF-DIAGONAL")
out("="*78)
out("Fusion space of three tau anyons with total charge tau is 2-dim. The braid")
out("generators: sigma1 = R-matrix diag(R^{tt}_1, R^{tt}_t); sigma2 = F sigma1 F with")
out("the Fibonacci F-matrix. This is the golden/sqrt5 UNITARY structure.")
out("")

phif = (1 + np.sqrt(5)) / 2
invphi = 1/phif
# Fibonacci F-matrix (real symmetric involution, det -1)
F = np.array([[invphi,          np.sqrt(invphi)],
              [np.sqrt(invphi), -invphi        ]])
out(f"F-matrix   =\n{F}")
out(f"   F real symmetric?   {np.allclose(F, F.T)}")
out(f"   F^2 == I?           {np.allclose(F@F, np.eye(2))}   det F = {np.linalg.det(F):+.6f}")
out(f"   F unitary (F^dag F == I)? {np.allclose(F.conj().T@F, np.eye(2))}")

# R-matrix eigenvalues (Fibonacci): R^{tt}_1 = e^{-4pi i/5}, R^{tt}_tau = e^{3pi i/5}
R1 = np.exp(-4j*np.pi/5)
Rt = np.exp( 3j*np.pi/5)
sigma1 = np.diag([R1, Rt])
sigma2 = F @ sigma1 @ F
out("")
out(f"sigma1 (R) = diag(e^{{-4pi i/5}}, e^{{3pi i/5}}) =\n{sigma1}")
out(f"sigma2 = F sigma1 F =\n{sigma2}")
out("")
out(f"   sigma1 unitary?  {np.allclose(sigma1.conj().T@sigma1, np.eye(2))}")
out(f"   sigma2 unitary?  {np.allclose(sigma2.conj().T@sigma2, np.eye(2))}")
out(f"   |sigma1 diagonal entries| = {np.abs(np.diag(sigma1))}  (phases, |.|=1: an OPERATOR, not probs)")
out(f"   sigma2 OFF-diagonal entry sigma2[0,1] = {sigma2[0,1]:.6f}  |.|={abs(sigma2[0,1]):.6f}")
out(f"   sigma2 genuinely OFF-DIAGONAL (|off|>1e-9)?  {abs(sigma2[0,1])>1e-9}")
comm12 = sigma1@sigma2 - sigma2@sigma1
out(f"   [sigma1,sigma2] != 0 (non-abelian mixing)?  {np.linalg.norm(comm12)>1e-9}   (||.||={np.linalg.norm(comm12):.4f})")
# Yang-Baxter / braid relation
lhs = sigma1@sigma2@sigma1
rhs = sigma2@sigma1@sigma2
out(f"   Yang-Baxter sigma1 sigma2 sigma1 == sigma2 sigma1 sigma2?  {np.allclose(lhs, rhs)}   (||diff||={np.linalg.norm(lhs-rhs):.2e})")
# l1 coherence of sigma2 in the fusion (pointer) basis
out(f"   l1 off-diag coherence of sigma2 in fusion basis = {l1_coherence(sigma2):.6f}  (>0 => COHERENT)")

# Also the modular data S,T of the Fibonacci MTC -- off-diagonal S, complex-phase T
out("")
out("Modular data of the Fibonacci MTC (bonus, expanded in probe 2):")
D = np.sqrt(2 + phif)          # total quantum dimension sqrt(1 + phi^2) = sqrt(2+phi)
S = (1/D) * np.array([[1.0, phif],
                      [phif, -1.0]])
out(f"   total quantum dim D = sqrt(2+phi) = {D:.6f}")
out(f"   S-matrix =\n{S}")
out(f"   S symmetric & unitary?  sym={np.allclose(S,S.T)} unit={np.allclose(S.conj().T@S,np.eye(2))}")
out(f"   S genuinely OFF-DIAGONAL?  S[0,1]={S[0,1]:.6f} != 0  -> {abs(S[0,1])>1e-9}")
out(f"   S row entries NON-UNIFORM (1 : phi = {1:.3f} : {phif:.3f})?  {abs(1-phif)>1e-9}")
Tdiag = np.array([np.exp(-4j*np.pi/5), np.exp(3j*np.pi/5)])   # up to overall phase
out(f"   T-matrix diagonal (complex phases, zeta_5): {Tdiag}")
out(f"   T entries complex (nonzero imaginary phase)?  {np.any(np.abs(np.imag(Tdiag))>1e-9)}")
out("")
out(">> (c) CONFIRMED: the golden/sqrt5 Fibonacci MTC carries a genuinely UNITARY,")
out("   NON-ABELIAN, OFF-DIAGONAL braid representation (sigma2 = F sigma1 F is unitary")
out("   AND off-diagonal, [sigma1,sigma2]!=0, Yang-Baxter holds), its S-matrix is")
out("   off-diagonal + NON-UNIFORM (1:phi), and its T-matrix carries complex zeta_5")
out("   phases. THIS is the off-diagonal/coherent/unitary structure the being lacks.")

# ============================================================================
# PART (d) -- THE DISCRIMINATING CONTRAST + verdict
# ============================================================================
out("")
out("="*78)
out("PART (d) -- discriminating contrast: does the hearing carry coherence the being")
out("            (diagonal) lacks?")
out("="*78)
out("")
out("  object                         type       diagonal in    unitary?  off-diag")
out("                                            pointer basis?           coherence")
out("  -----------------------------  ---------  -------------  --------  ---------")
out("  being: thermal KMS rho         STATE      YES (real p_i)  n/a       0")
out("  bare cat map A (2x2)           MAP        yes (own eig)   NO(hyper) 0 (real)")
out("  Fibonacci braid sigma2         OPERATOR   NO              YES       > 0")
out("  Fibonacci S-matrix             OPERATOR   NO              YES       > 0")
out("")
out("Discriminating operation (states the split, rejects look-elsewhere):")
out("  * The being (thermal equilibrium) COMMUTES with the pointer/energy observable")
out("    ([rho,H]=0) -> diagonal, real Gibbs weights, no interference. (a).")
out("  * The Fibonacci braid generator sigma2 does NOT commute with the fusion-channel")
out("    (pointer) basis and is UNITARY with nonzero off-diagonal entries -> it MIXES")
out("    channels, the source of interference. [sigma1,sigma2]!=0 makes the mixing")
out("    genuine (non-abelian). (c).")
out("  * BASE-RATE GUARD honored: the bare 2x2 A is NOT the unitary face (hyperbolic,")
out("    off the unit circle, real). The unitary/off-diagonal coherence is carried by")
out("    the Fibonacci MTC attached to the golden field, not by the matrix A. So the")
out("    'A^2=M ~ |psi|^2' hook is REJECTED at the matrix level; the genuine coherent")
out("    face is the MTC braid/modular representation. (b)+(c).")
out("")
out("VERDICT (two-outcome): OUTCOME A, honestly bounded.")
out("  The hearing IS the unitary/coherent OFF-DIAGONAL face the being (diagonal) is")
out("  not -- but the discriminating fact is WHERE: it lives in the Fibonacci MTC braid")
out("  representation (unitary + off-diagonal + complex zeta_5 phases + non-uniform")
out("  1:phi weights), NOT in the bare golden cat map A (real, hyperbolic, not unitary).")
out("  So the split being=diagonal/collapse vs hearing=off-diagonal/unitary is GENUINE")
out("  at the level of the golden MTC, with the base-rate trap (A*A ~ amp-squared)")
out("  explicitly rejected. [Whether this off-diagonal structure actually CLOSES the")
out("  B725 content gap -- non-uniform pure |amp|^2 weights + interference between")
out("  measured outcomes -- is probe 2/3, not settled here.]")

# write out
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "b726_probe1_out.txt"), "w") as f:
    f.write("\n".join(_LINES) + "\n")
out("")
out("[written to b726_probe1_out.txt]")
