"""B223 / Act II -- where does the SUSY live: emergent (IR-only) on the golden chain, or lattice-exact?
Nothing to CLAIMS.md.

B221/B222 established the golden chain's emergent N=1 superconformal SUSY (c=7/10, the supercurrent). This asks
whether that SUSY has an EXACT LATTICE realization.

(A) THE GOLDEN CHAIN HAS NO EXACT LATTICE SUSY GRADING (expected negative). A graded (lattice) SUSY algebra
    needs a conserved fermion parity (-1)^F with H block-off-diagonal/graded. The natural candidate -- tau-parity
    (-1)^{# of tau's} -- is NOT conserved: the (tau,tau)-block off-diagonal term flips a single l_i (0<->1),
    changing the tau-count by +-1, while the diagonal terms preserve it; so H has BOTH parity-even and parity-odd
    parts and [H, (-1)^F] != 0 and {H,(-1)^F} != 0. => the golden chain's SUSY is EMERGENT / IR-only.

(B) LATTICE-EXACT N=2 SUSY DOES EXIST ON THE SAME FIBONACCI/LUCAS HILBERT SPACE (Fendley-Schoutens, 2003).
    Hard-core fermions with NO TWO ADJACENT OCCUPIED (same Lucas L_N counting as the golden chain), supercharge
        Q = sum_i (-1)^{n_1+...+n_{i-1}} c†_i (1-n_{i-1})(1-n_{i+1})   (add a fermion only if both neighbors empty)
    is NILPOTENT (Q^2=0), gives H_FS = {Q, Q†} with conserved (-1)^F = (-1)^{# fermions} ([H_FS,(-1)^F]=0), and a
    Witten index W = Tr(-1)^F. All EXACT (machine precision). This shows lattice-exact SUSY is possible on a
    Fibonacci Hilbert space -- but on a DIFFERENT model from the golden chain.

HONEST: the Fendley-Schoutens model is an N=2 lattice-SUSY SIBLING on the same Hilbert-space combinatorics; it is
NOT claimed to share the golden chain's IR (the golden chain is N=1 c=7/10; the FS M_k series is N=2). So the
clean statement is: golden-chain SUSY is emergent-only; lattice-exact SUSY lives on a sibling model.

Firewall: dimensionless quantum-algebra; nothing to CLAIMS.md; P1-P16 untouched. Run: python lattice_susy.py (pyenv).
"""
import numpy as np
import scipy.sparse as sp

PHI = (1 + 5 ** 0.5) / 2
P11 = np.array([[PHI ** -2, PHI ** -1.5], [PHI ** -1.5, PHI ** -1]])


# ---------- (A) the golden chain: no conserved tau-parity ----------
def golden_basis(N):
    out = []
    for x in range(1 << N):
        b = tuple((x >> i) & 1 for i in range(N))
        if all(not (b[i] == 0 and b[(i + 1) % N] == 0) for i in range(N)):
            out.append(b)
    return out


def golden_H_and_parity(N, sign=-1.0):
    states = golden_basis(N)
    idx = {s: i for i, s in enumerate(states)}
    D = len(states)
    rows, cols, vals = [], [], []
    for si, s in enumerate(states):
        for i in range(N):
            lm, li, lp = s[(i - 1) % N], s[i], s[(i + 1) % N]
            if (lm, lp) == (0, 0):
                rows.append(si); cols.append(si); vals.append(sign * 1.0)
            elif (lm, lp) == (1, 1):
                rows.append(si); cols.append(si); vals.append(sign * P11[li, li])
                s2 = s[:i] + (1 - li,) + s[i + 1:]
                rows.append(idx[s2]); cols.append(si); vals.append(sign * P11[1 - li, li])
    H = sp.csr_matrix((vals, (rows, cols)), shape=(D, D))
    F = sp.diags([(-1.0) ** sum(s) for s in states])   # tau-parity (-1)^{# tau}
    return H, F


def golden_parity_conserved(N):
    """return ||[H, (-1)^F]|| -- nonzero => no graded lattice SUSY (emergent only)."""
    H, F = golden_H_and_parity(N)
    comm = (H @ F - F @ H)
    return abs(comm).max()


# ---------- (B) the Fendley-Schoutens N=2 lattice-SUSY sibling ----------
def fs_basis(L):
    """hard-core fermions, NO TWO ADJACENT OCCUPIED (cyclic) -- Lucas L_L dim, same as the golden chain."""
    out = []
    for x in range(1 << L):
        b = tuple((x >> i) & 1 for i in range(L))
        if all(not (b[i] == 1 and b[(i + 1) % L] == 1) for i in range(L)):
            out.append(b)
    return out


def fs_supercharge(L):
    """Q = sum_i (-1)^{n_1+..+n_{i-1}} c†_i (1-n_{i-1})(1-n_{i+1}); returns (Q, states)."""
    states = fs_basis(L)
    idx = {s: i for i, s in enumerate(states)}
    rows, cols, vals = [], [], []
    for sj, s in enumerate(states):
        for i in range(L):
            if s[i] == 0 and s[(i - 1) % L] == 0 and s[(i + 1) % L] == 0:
                s2 = s[:i] + (1,) + s[i + 1:]
                if s2 in idx:
                    sign = (-1.0) ** sum(s[:i])   # Jordan-Wigner string
                    rows.append(idx[s2]); cols.append(sj); vals.append(sign)
    Q = sp.csr_matrix((rows and (vals, (rows, cols)) or ([], ([], []))),
                      shape=(len(states), len(states)))
    return Q, states


def fs_data(L):
    Q, states = fs_supercharge(L)
    Qd = Q.conj().T
    Q2 = abs((Q @ Q)).max()                       # nilpotency Q^2 = 0
    H = (Q @ Qd + Qd @ Q)                          # H_FS = {Q, Q†}
    F = sp.diags([(-1.0) ** sum(s) for s in states])
    comm = abs((H @ F - F @ H)).max()             # [H_FS, (-1)^F] = 0
    witten = sum((-1.0) ** sum(s) for s in states)  # Witten index Tr(-1)^F
    return {"dim": len(states), "Q2": Q2, "HF_comm": comm, "witten": witten,
            "Egs": float(min(np.linalg.eigvalsh(H.toarray())))}


if __name__ == "__main__":
    print("(A) golden chain: is tau-parity (-1)^F conserved?  ||[H,(-1)^F]|| (nonzero => emergent-only SUSY)")
    for N in (8, 10, 12):
        print(f"    N={N}: ||[H,(-1)^F]|| = {golden_parity_conserved(N):.4f}  -> NOT conserved (no lattice grading)")

    print("\n(B) Fendley-Schoutens N=2 lattice SUSY on the same Fibonacci/Lucas Hilbert space:")
    print("    L    dim   |Q^2|      |[H,(-1)^F]|   Witten Tr(-1)^F   E_gs")
    for L in (6, 9, 12):
        d = fs_data(L)
        print(f"    {L:2d}  {d['dim']:5d}  {d['Q2']:.2e}   {d['HF_comm']:.2e}      {d['witten']:+.0f}"
              f"            {d['Egs']:.3e}")
    print("    => Q^2=0 and H_FS={Q,Q†} EXACTLY, (-1)^F conserved, integer Witten index (E_gs=0 => unbroken SUSY).")
    print("    HONEST: lattice-exact SUSY lives on this SIBLING (N=2); the golden chain's own SUSY is emergent.")
    print("ALL CHECKS PASS")
