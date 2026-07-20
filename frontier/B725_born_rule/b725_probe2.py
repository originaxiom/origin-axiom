#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B725 / PROBE 2 -- are the beta=1 SSB decomposition WEIGHTS the Born probabilities?

Prereg (B725, probe 2): at the beta=1 SSB (B723), the symmetric KMS/Gibbs state
decomposes into extremal broken vacua (pointer states) P_i. Are the decomposition
WEIGHTS the Born-rule probabilities p_i = Tr(rho P_i)?
Two-outcome:  A = SSB weights ARE Tr(rho P_i) (Born);   B = they differ.

Firewall: structural / operator-algebra ONLY. Finite-dim von-Neumann-algebra model
(M_n = n x n complex matrices). COMPUTE-NOT-CITE: every discriminating fact is
recomputed here in-sandbox to machine precision; no B-number asserted as proof.

What "SSB decomposition" means in this finite model
---------------------------------------------------
Genuine SSB / a nontrivial central decomposition needs the thermodynamic limit
(M_n is a factor -> trivial center -> the Gibbs state is the *unique* KMS state and
is itself extremal-KMS). We model the phenomenon the way a measurement realises it:
the pointer / broken-vacuum sector is a MAXIMAL ABELIAN SUBALGEBRA A (a "center at
infinity"). SSB = the choice of that pointer MASA (which orthonormal basis the
apparatus breaks toward). The extremal states of A are its rank-1 pointer projectors
P_i, and the decomposition of rho over A is  rho |-> sum_i (Tr rho P_i) P_i  with the
off-diagonal (in the pointer basis) killed. The WEIGHTS of that decomposition are the
object of this probe.

The four computations
---------------------
 1. Gibbs/KMS state on M_n, pointer basis = eigenbasis of H (made nontrivial by a
    random unitary so it is NOT the computational basis). Verify
        p_i (Gibbs weight) = e^{-beta E_i}/Z  ==  Tr(rho P_i) (Born)   exactly,
    p_i >= 0, sum p_i = 1.  Plus an explicit KMS-condition check that rho_beta is THE
    KMS state (so "SSB decomposition weight" is being read off the right state).
 2. THE DISCRIMINATING FACT. A mixed rho has MANY pure-state decompositions
    (Gisin-Hughston-Jozsa-Wootters). Only the ORTHOGONAL one -- the pointer/spectral
    decomposition selected by the SSB MASA -- has weight_i = Tr(rho P_i). A
    non-orthogonal ensemble reproducing the SAME rho has weights != Tr(rho P_i)
    (and its Tr(rho P_i) do not even sum to 1). So the equality "weight = Born" is
    NOT automatic for any decomposition; it holds SPECIFICALLY for the SSB one, and
    that is exactly what singles the SSB decomposition out as the Born one.
 3. beta-sweep incl. beta=1: the equality weight = Tr(rho P_i) is EXACT at every beta
    (it is just the spectral identity). Born weighting is the SAME rule at all beta;
    beta only sets the VALUES. So beta=1 is not special for the weighting RULE.
 4. Z_2 symmetric-vacua model: a symmetric state built from two symmetry-related
    broken vacua decomposes with weights = Tr(rho P_i) = Born.

Outputs mirrored to b725_probe2_out.txt.
"""

import numpy as np

np.random.seed(725)
np.set_printoptions(precision=6, suppress=True, linewidth=110)

_LINES = []
def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    _LINES.append(s)

def rule(t=""):
    out("\n" + "=" * 78)
    if t:
        out(t)
        out("=" * 78)

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def haar_unitary(n):
    """Random Haar-ish unitary via QR of a complex Gaussian."""
    z = (np.random.randn(n, n) + 1j * np.random.randn(n, n)) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph  # columns fixed to a canonical phase

def gibbs(H, beta):
    """rho_beta = exp(-beta H)/Z on M_n."""
    w, V = np.linalg.eigh(H)
    ex = np.exp(-beta * (w - w.min()))      # shift for numerical stability (Z scalar)
    Z = ex.sum()
    rho = (V * (ex / Z)) @ V.conj().T
    return rho, w, V

def herm(n):
    A = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    return (A + A.conj().T) / 2.0

# ===========================================================================
rule("PART 1 -- Gibbs/KMS state; pointer=eigenbasis; weight_i == Tr(rho P_i)")
# ===========================================================================
out("Pointer basis is the EIGENBASIS of H (rotated by a random unitary, so it is")
out("NOT the computational basis). P_i = |v_i><v_i|. The SSB/pointer decomposition")
out("of the Gibbs state is  rho = sum_i p_i P_i.  Test p_i == Tr(rho P_i).\n")

for n in (2, 3, 5):
    U = haar_unitary(n)
    E = np.sort(np.random.randn(n) * 1.3)          # energies
    H = (U * E) @ U.conj().T                        # H = U diag(E) U^dagger
    beta = 1.0                                      # the B723 critical point
    rho, w, V = gibbs(H, beta)

    # Gibbs weights (KMS weights) in the pointer/eigen basis
    p_gibbs = np.exp(-beta * (w - w.min())); p_gibbs /= p_gibbs.sum()

    # Born weights Tr(rho P_i), P_i = |v_i><v_i|
    Pi = [np.outer(V[:, i], V[:, i].conj()) for i in range(n)]
    p_born = np.array([np.real(np.trace(rho @ P)) for P in Pi])

    # reconstruct rho from the SSB/pointer decomposition sum_i p_i P_i
    rho_rec = sum(p * P for p, P in zip(p_born, Pi))

    out(f"n={n}:")
    out(f"   Gibbs weights p_i          = {p_gibbs}")
    out(f"   Born weights Tr(rho P_i)   = {p_born}")
    out(f"   max|p_gibbs - p_born|      = {np.max(np.abs(p_gibbs - p_born)):.3e}")
    out(f"   all p_born >= 0            = {bool(np.all(p_born >= -1e-14))}")
    out(f"   sum p_born                 = {p_born.sum():.15f}")
    out(f"   ||rho - sum p_i P_i||      = {np.linalg.norm(rho - rho_rec):.3e}")
    out("")

# --- KMS-condition check: confirm rho_beta is THE KMS state (not just any diag) ---
out("KMS-condition check (finite-dim): with alpha_t(A)=e^{iHt}A e^{-iHt},")
out("the KMS relation at t=0 reads  Tr(rho A alpha_{i beta}(B)) = Tr(rho B A),")
out("i.e.  Tr(rho A e^{-beta H} B e^{beta H}) = Tr(rho B A).  Random A,B:")
n = 4
U = haar_unitary(n); E = np.sort(np.random.randn(n)); H = (U * E) @ U.conj().T
for beta in (0.5, 1.0, 2.0):
    rho, w, V = gibbs(H, beta)
    eNbH = V @ np.diag(np.exp(-beta * w)) @ V.conj().T
    ePbH = V @ np.diag(np.exp(+beta * w)) @ V.conj().T
    kmax = 0.0
    for _ in range(6):
        A = herm(n) + 1j * herm(n)   # arbitrary (non-Hermitian) operators
        B = herm(n) + 1j * herm(n)
        lhs = np.trace(rho @ A @ eNbH @ B @ ePbH)
        rhs = np.trace(rho @ B @ A)
        kmax = max(kmax, abs(lhs - rhs))
    out(f"   beta={beta}:  max|KMS_lhs - KMS_rhs| over 6 random A,B = {kmax:.3e}")

# ===========================================================================
rule("PART 2 -- THE DISCRIMINATING FACT: only the ORTHOGONAL (SSB) decomposition")
rule("           has weight == Tr(rho P).  Non-orthogonal ensembles do NOT.")
# ===========================================================================
out("A mixed rho has MANY pure-state decompositions (GHJW). If 'weight = Tr(rho P)'")
out("held for ANY decomposition it would be vacuous. It does NOT: it is exactly the")
out("ORTHOGONAL / pointer / spectral decomposition -- the one the SSB MASA selects --")
out("that has weight_i = Tr(rho P_i). This is what makes the SSB decomposition the")
out("Born decomposition (rather than merely A decomposition).\n")

# Work in the eigenbasis of a qubit rho = diag(l0, l1), l0=0.7
l0, l1 = 0.70, 0.30
rho = np.diag([l0, l1]).astype(complex)

# (a) ORTHOGONAL (SSB / pointer / spectral) decomposition -> weights = eigenvalues
Pz = [np.diag([1, 0]).astype(complex), np.diag([0, 1]).astype(complex)]
w_orth = np.array([l0, l1])
born_orth = np.array([np.real(np.trace(rho @ P)) for P in Pz])
out("(a) ORTHOGONAL pointer decomposition rho = 0.7|0><0| + 0.3|1><1|")
out(f"    decomposition weights      = {w_orth}")
out(f"    Tr(rho P_i) (Born)         = {born_orth}")
out(f"    max|weight - Born|         = {np.max(np.abs(w_orth - born_orth)):.3e}  <-- EQUAL")
out(f"    sum P_i = I ?              = {np.allclose(Pz[0]+Pz[1], np.eye(2))}   (resolution of identity)")
out("")

# (b) NON-ORTHOGONAL ensemble reproducing the SAME rho, equal weights 1/2
#     |psi_pm> = cos a |0> +/- sin a |1>, cos^2 a = l0 -> rho = 1/2(P+ + P-)
a = np.arccos(np.sqrt(l0))
psi_p = np.array([np.cos(a),  np.sin(a)], dtype=complex)
psi_m = np.array([np.cos(a), -np.sin(a)], dtype=complex)
Pp, Pm = np.outer(psi_p, psi_p.conj()), np.outer(psi_m, psi_m.conj())
rho_chk = 0.5 * (Pp + Pm)
w_non = np.array([0.5, 0.5])
born_non = np.array([np.real(np.trace(rho @ Pp)), np.real(np.trace(rho @ Pm))])
overlap = abs(np.vdot(psi_p, psi_m))
out("(b) NON-ORTHOGONAL ensemble rho = 1/2|psi+><psi+| + 1/2|psi-><psi-|,")
out(f"    <psi+|psi-> overlap        = {overlap:.4f}  (non-orthogonal)")
out(f"    reproduces the SAME rho?   = {np.allclose(rho_chk, rho)}")
out(f"    decomposition weights      = {w_non}")
out(f"    Tr(rho P_j) (Born)         = {born_non}")
out(f"    max|weight - Born|         = {np.max(np.abs(w_non - born_non)):.3e}  <-- DIFFER")
out(f"    sum Tr(rho P_j)            = {born_non.sum():.4f}  (P+ + P- != I, so not a probability rule)")
out("")
out("=> 'decomposition weight = Tr(rho P)' is FALSE for a generic (non-orthogonal)")
out("   decomposition and TRUE for the orthogonal pointer one. The SSB selection of")
out("   the pointer MASA is precisely what makes the weights Born.")

# ===========================================================================
rule("PART 3 -- beta-sweep incl beta=1: the equality is EXACT at every beta")
rule("           (Born weighting is beta-independent as a RULE; beta sets values)")
# ===========================================================================
n = 4
U = haar_unitary(n); E = np.sort(np.random.randn(n) * 1.5); H = (U * E) @ U.conj().T
V = np.linalg.eigh(H)[1]
Pi = [np.outer(V[:, i], V[:, i].conj()) for i in range(n)]
out(f"{'beta':>8} | {'max|Gibbs - Born|':>18} | {'sum p':>10} | weights (Tr rho P_i)")
out("-" * 78)
for beta in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 16.0):
    rho, w, _ = gibbs(H, beta)
    pg = np.exp(-beta * (w - w.min())); pg /= pg.sum()
    pb = np.array([np.real(np.trace(rho @ P)) for P in Pi])
    tag = "  <-- CRITICAL (B723)" if beta == 1.0 else ""
    out(f"{beta:8.2f} | {np.max(np.abs(pg-pb)):18.3e} | {pb.sum():10.6f} | {np.round(pb,5)}{tag}")
out("")
out("The RULE weight_i = Tr(rho P_i) holds to ~1e-16 at every beta, including beta=0")
out("(rho = I/n, uniform Born weights) and beta->inf (ground-state projector).")
out("beta=1 is NOT special for the weighting rule; it is special (in B723) only as")
out("the symmetric->broken transition point -- which in finite dim has no phase")
out("transition, so no beta plays a distinguished role for the WEIGHTS themselves.")

# ===========================================================================
rule("PART 4 -- Z_2 symmetric-vacua model: symmetric state = Born mixture of vacua")
# ===========================================================================
out("Two symmetry-related broken vacua |L>,|R> (orthonormal pointer states), a Z_2")
out("swap S:|L><->|R>. The symmetric (S-invariant) mixed state is the Gibbs state of")
out("a Hamiltonian with the degenerate doublet; it decomposes over the {|L>,|R>}")
out("pointer MASA with weights = Tr(rho P_L,R) = Born.\n")

L = np.array([1, 0], dtype=complex)
R = np.array([0, 1], dtype=complex)
S = np.array([[0, 1], [1, 0]], dtype=complex)     # Z_2 swap
# degenerate doublet -> symmetric Gibbs state is maximally mixed on the doublet
for (wL, wR) in [(0.5, 0.5), (0.62, 0.38)]:
    rho = wL * np.outer(L, L.conj()) + wR * np.outer(R, R.conj())
    sym = np.allclose(S @ rho @ S.conj().T, rho) if (wL == wR) else False
    PL, PR = np.outer(L, L.conj()), np.outer(R, R.conj())
    bL, bR = np.real(np.trace(rho @ PL)), np.real(np.trace(rho @ PR))
    out(f"  vacua weights (wL,wR)=({wL},{wR}):  Born Tr(rho P_L,R)=({bL:.3f},{bR:.3f})"
        f"  equal? {np.allclose([wL,wR],[bL,bR])}"
        + (f"  [S-symmetric: {sym}]" if wL == wR else "  [S-broken bias]"))
out("")
out("The equal-weight (S-symmetric) case gives the two vacua weight 1/2 each = Born;")
out("a biased Gibbs state gives Gibbs-weighted vacua, still = Tr(rho P). The SSB")
out("decomposition weight IS the Born probability in every case.")

# ===========================================================================
rule("VERDICT")
# ===========================================================================
out("Discriminating fact (recomputed in-sandbox, all parts):")
out("  * SSB/pointer (orthogonal, central-MASA) decomposition weights EQUAL the Born")
out("    probabilities Tr(rho P_i) to machine precision (~1e-16), with p_i>=0,")
out("    sum p_i = 1, at every beta including the B723 critical beta=1.  [Parts 1,3,4]")
out("  * This is NON-vacuous: a non-orthogonal decomposition of the SAME rho has")
out("    weights that DIFFER from Tr(rho P) (and whose Tr(rho P) do not sum to 1).")
out("    The SSB selection of the orthogonal pointer MASA is exactly what makes the")
out("    decomposition weights Born.                                        [Part 2]")
out("  * beta=1 is NOT special for the weighting RULE (holds identically at all beta;")
out("    a genuine transition needs the thermodynamic limit, absent in finite M_n).")
out("")
out("OUTCOME: A  -- the beta=1 SSB decomposition WEIGHTS ARE the Born probabilities")
out("             Tr(rho P_i), exactly, and non-vacuously (the orthogonal/central")
out("             pointer decomposition is the one selected).")
out("Bounded honesty: 'weight = Tr(rho P)' for the ORTHOGONAL decomposition is the")
out("spectral identity (structural, not a new theorem); the added content is that the")
out("SSB/central decomposition is precisely that orthogonal one, so its weights are")
out("Born -- and that this is beta-independent as a rule (finite dim has no critical")
out("beta). Genuine SSB/central-measure content lives in the thermodynamic limit,")
out("here modelled by the pointer MASA. Firewall: structural only; choice free (B701).")

# write mirror
with open(__file__.replace(".py", "_out.txt"), "w") as f:
    f.write("\n".join(_LINES) + "\n")
out("\n[written b725_probe2_out.txt]")
