#!/usr/bin/env python3
"""B523 cell 1 (C3 / Malament) — CORRECTED after the B525 'Are You Sure' audit.

The original version classified causal type from a Lyapunov MAGNITUDE convention that sent genuine
ZERO eigenvalues to 'spacelike' (|0|<1 -> +1), so it mislabelled the det-0 TM verb as '(3,1) proper,
preserves 1.000' and drove a buggy cone-PRESERVATION reading. That was a proxy-for-object error
(a magnitude count substituted for the real discriminator). The real discriminator is the
SIGNATURE (# expanding directions) with degeneracy flagged. The CONCLUSION is unchanged and sound.
"""
import numpy as np

F = np.array([[1, 1], [1, 0]], float)      # evolution    (det -1, unimodular)
D = np.array([[2, 0], [0, 2]], float)      # decimation   (det 4)
Dpd = np.array([[1, 2], [1, 0]], float)    # decimation   (det -2, pd variant)
T = np.array([[1, 1], [1, 1]], float)      # TM / erasure (det 0, rank 1)


def boot(v):
    return np.block([[v, v], [v @ v, v]])


def causal_type(M):
    """timelike = expanding (|lambda|>1); flag degeneracy (a zero eigenvalue / det 0) explicitly."""
    aw = np.abs(np.linalg.eigvals(M))
    degenerate = bool(abs(np.linalg.det(M)) < 1e-9 or np.any(aw < 1e-9))
    n_time = int((aw > 1 + 1e-9).sum())     # expanding directions
    n_space = int(((aw < 1 - 1e-9) & (aw > 1e-9)).sum())
    return n_time, n_space, degenerate


if __name__ == "__main__":
    print("verb            det     causal type (timelike, spacelike)")
    for name, v in [("evolution", F), ("decimation-2I", D), ("decimation-pd", Dpd), ("TM/erasure", T)]:
        nt, ns, deg = causal_type(boot(v))
        typ = "DEGENERATE (det=0, non-invertible)" if deg else f"({nt}, {ns})"
        print(f"{name:15s} {np.linalg.det(boot(v)):+6.2f}   {typ}")
    print()
    print("Four DIFFERENT causal types: (1,3) / (2,2) / (3,1-inverted) / degenerate.")
    print("Only the unimodular EVOLUTION verb gives a proper single-timelike (1,3) Lorentzian cone.")
    print("decimation-2I is genuinely (2,2) -> cannot preserve any single-timelike cone.")
    print("TM/erasure is det=0, non-invertible -> Malament's premise (a causal AUTOMORPHISM) fails.")
    print("=> the four-verb monoid preserves NO single causal cone. (Signature, not a preservation %.)")
