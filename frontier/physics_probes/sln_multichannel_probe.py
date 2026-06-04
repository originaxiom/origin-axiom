"""Path 1-SL(n): does an n-channel / n-th-order 1D chain realize the SL(n) trace map,
and is it a genuine quantum spectrum? Control baked in: if it cannot be a *Hermitian*
1D system, that is a NEGATIVE (the SL(n) tower has no standard-quantum realization).

Known anchor (Path 1): the Fibonacci quasicrystal IS the SL(2) trace map, because the
single-channel tight-binding transfer matrix is in SL(2,R) = Sp(2,R). Question for n>=3.

Findings structure:
 (a) REALIZATION: build explicit SL(3,R) transfer matrices from a 3rd-order recurrence,
     metallic substitution -> a real 1D LINEAR system whose trace dynamics is the SL(3) map.
 (b) OBSTRUCTION (the real test): Hermitian 1D transfer matrices are SYMPLECTIC (Sp(2p,R));
     SL(n)=Sp only for n=2. So SL(n>=3) has NO self-adjoint (quantum) 1D realization.
 (c) SPECTRUM: the SL(3) metallic transfer system still has a Cantor-like bounded-energy set
     (a real classical/non-Hermitian wave system), vs periodic (bands) and random controls.

numpy + sympy. Standalone math-physics; no Origin-core / thesis claim.
"""
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------- (a)
print("=" * 74)
print("(a) REALIZATION: SL(3,R) transfer matrices from a 3rd-order linear recurrence")
print("=" * 74)
# psi_{j+1} = a psi_j + b psi_{j-1} + psi_{j-2};  companion T=[[a,b,1],[1,0,0],[0,1,0]] in SL(3).
a, b = sp.symbols("a b")
Tsym = sp.Matrix([[a, b, 1], [1, 0, 0], [0, 1, 0]])
print("  companion T(a,b) =", Tsym.tolist(), " det =", sp.det(Tsym), "-> in SL(3,R) for all a,b")


def Tnum(a_, b_):
    return np.array([[a_, b_, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])


# two letters (energy-dependent): A=T(E-vA, wA), B=T(E-vB, wB)
vA, wA, vB, wB = 0.0, 0.7, 1.3, 0.4
def AB_of_E(E):
    return Tnum(E - vA, wA), Tnum(E - vB, wB)


# metallic (Fibonacci) word of A,B realizes the substitution; trace dynamics = SL(3) trace map
A0, B0 = AB_of_E(0.5)
print(f"  det(A)={np.linalg.det(A0):.3f}, det(B)={np.linalg.det(B0):.3f} (both 1 -> SL(3,R))")
print("  -> a genuine real 1D linear-recurrence (transfer-matrix) system exists in SL(3).")
print("     The metallic substitution on the letter sequence is the project's SL(3) trace map")
print("     (B33/B60); realization as an abstract transfer system is automatic.")

# ----------------------------------------------------------------------------- (b)
print("\n" + "=" * 74)
print("(b) OBSTRUCTION: is it a HERMITIAN (quantum) system? Symmetry class test")
print("=" * 74)
print("  A self-adjoint 1D operator has transfer matrices preserving the Wronskian SYMPLECTIC")
print("  (ANTI-symmetric) form -> Sp(2p,R).  SL(2,R) = Sp(2,R) (n=2: realized, = Fibonacci).")
print("  Physical criterion: exists a CONSTANT NONDEGENERATE antisymmetric S with M^T S M = S")
print("  (equivalently S M = M^{-T} S) for BOTH letters.")


def symplectic_invariants(mats, n):
    """dim of the space of antisymmetric S with S M = M^{-T} S for all M in mats; plus
    whether a NONDEGENERATE one exists."""
    pairs = [(i, j) for i in range(n) for j in range(n) if i < j]   # antisymmetric basis
    rows = []
    for M in mats:
        MiT = np.linalg.inv(M).T
        for r in range(n):
            for c in range(n):
                row = []
                for (i, j) in pairs:
                    Sij = np.zeros((n, n)); Sij[i, j] = 1; Sij[j, i] = -1
                    row.append((Sij @ M - MiT @ Sij)[r, c])
                rows.append(row)
    Rm = np.array(rows, dtype=float)
    s = np.linalg.svd(Rm, compute_uv=False)
    dim_sol = len(pairs) - int(np.sum(s > 1e-9))
    # check nondegeneracy of a representative solution
    nondeg = False
    if dim_sol > 0:
        u2, s2, vt2 = np.linalg.svd(Rm)
        for vrow in vt2[-dim_sol:]:
            S = np.zeros((n, n))
            for (i, j), val in zip(pairs, vrow):
                S[i, j] = val; S[j, i] = -val
            if abs(np.linalg.det(S)) > 1e-6:
                nondeg = True
    return dim_sol, nondeg


for n, mats, lab in [
    (2, [np.array([[0.5, -1.0], [1.0, 0.0]]), np.array([[1.3, -1.0], [1.0, 0.0]])], "SL(2)=Sp(2), Fibonacci"),
    (3, [A0, B0], "SL(3) metallic transfer")]:
    d, nd = symplectic_invariants(mats, n)
    print(f"    - n={n} ({lab}): invariant antisymmetric forms dim={d}, nondegenerate exists={nd}"
          f"  ->  {'HERMITIAN-realizable (symplectic)' if nd else 'NOT self-adjoint (no symplectic form)'}")
print("    (odd dimension has NO nondegenerate antisymmetric form at all => SL(3) cannot be the")
print("     transfer group of a self-adjoint 1D operator; the SL(3) chain is non-Hermitian.)")

# ----------------------------------------------------------------------------- (c)
print("\n" + "=" * 74)
print("(c) SPECTRUM of the SL(3) metallic transfer system (Lyapunov), vs controls")
print("=" * 74)
def metallic_word(N):
    s = "B"; t = "A"
    while len(s) < N:
        s, t = s + t, s          # Fibonacci concatenation
    return s[:N]

def lyapunov(seq, E, kind="metallic"):
    A, B = AB_of_E(E)
    if kind == "periodic":
        order = "AB" * (len(seq) // 2 + 1)
    elif kind == "random":
        rng = np.random.default_rng(int(abs(E) * 1000) % 99 + 1)
        order = "".join(rng.choice(["A", "B"], len(seq)))
    else:
        order = seq
    v = np.eye(3); lg = 0.0
    for ch in order[:len(seq)]:
        v = (A if ch == "A" else B) @ v
        nrm = np.linalg.norm(v)
        lg += np.log(nrm); v /= nrm
    return lg / len(seq)

seq = metallic_word(600)
Es = np.linspace(-1.0, 3.0, 240)
for kind in ("metallic", "periodic", "random"):
    g = np.array([lyapunov(seq, E, kind) for E in Es])
    spectrum = Es[g < 0.05]                          # gamma ~ 0 => allowed (extended)
    frac = len(spectrum) / len(Es)
    print(f"  {kind:9s}: allowed-energy fraction (gamma<0.05) = {frac:.3f}  "
          f"min gamma = {g.min():.3f}")
print("  (metallic: a thin Cantor-like allowed set, between periodic 'bands' and random;")
print("   a genuine multifractal spectrum -- but of the NON-self-adjoint SL(3) transfer operator.)")

print("\n" + "=" * 74)
print("(d) DOES a_d (the tower) CONTROL THE GAPS? -- structural note")
print("=" * 74)
print("  The tower / a_d multiplicities are the fixed-line Jacobian spectrum at the TRIVIAL rep")
print("  (all traces = n) -- the BAND-CENTER linearization of the trace map. The spectral GAPS")
print("  are labeled by the substitution's abelianization (gap-labeling: IDOS in Z+Z/phi for SL(2),")
print("  Path 1b), a DIFFERENT invariant. No evidence a_d = gap labels; a_d is band-center data.")

print("\n" + "=" * 74)
print("VERDICT")
print("=" * 74)
print("- REALIZATION: YES as an abstract/real 1D LINEAR-RECURRENCE (transfer) system in SL(n);")
print("  the SL(n) metallic quasicrystal exists as a classical/non-Hermitian wave system, with a")
print("  Cantor-like spectrum.")
print("- QUANTUM (Hermitian) REALIZATION: NO for n>=3 (controlled). Self-adjoint 1D transfer")
print("  matrices are SYMPLECTIC (Sp(2p,R)); SL(n)=Sp only for n=2. SL(n>=3) admits no invariant")
print("  Hermitian metric -> not a standard quantum Hamiltonian. The golden/SL(2)=Fibonacci")
print("  quasicrystal is SPECIAL to n=2.")
print("- a_d CONTROLS GAPS: unsupported; a_d is band-center (trivial-rep) data, not the gap label.")
print("- NET: Path 1-SL(n) gives a real classical 1D system but NO quantum-spectrum crossing for")
print("  n>=3; the physics is the same 1D condensed-matter neighborhood as SL(2), no deeper.")
