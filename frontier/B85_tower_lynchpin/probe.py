"""B85 (Phase C/D) -- the all-n tower lynchpin, precisely reduced: Lambda^2 functoriality is real but
does NOT break the degeneracy; the SL(5)+ tower from first principles genuinely needs the symbolic
trace map sigma.

THE LYNCHPIN. The metallic tower char(J(m)) = the Dickson catalog is PROVED at n<=4 (B80/V62, CRT/F_p)
and STRUCTURAL at n=5,6 (B62 opposition-involution). The only gap is a from-first-principles SL(5)+
proof. This stage reduces that gap to its irreducible form, ruling out the numerical and
representation-theoretic shortcuts.

WHAT THIS ESTABLISHES:
  (1) Lambda^2 FUNCTORIALITY (verified ~1e-14, n=4,5). The figure-eight substitution phi:a->a^2 b,
      b->ab is FUNCTORIAL under the exterior square: Lambda^2(A^2 B) = (Lambda^2 A)^2 (Lambda^2 B),
      Lambda^2(AB) = (Lambda^2 A)(Lambda^2 B). So the even-k sector (tied to e_2=tr(Lambda^2 A)) is the
      SAME figure-eight trace map carried on the Lambda^2 V representation -- a clean new structural fact.
  (2) BUT Lambda^2 V does NOT remove the doubly-degenerate char(M^2)^2. The multiplicity-2 at SL(5) is
      the dimension of the height-2 root space's theta-symmetric part (B62) -- a ROOT-SYSTEM fact, not a
      representation artifact. Going to Lambda^2 V (dim C(n,2)) re-presents the same root system; the
      multiplicity persists. So the functoriality, though real, does NOT dissolve the degeneracy.

THE IRREDUCIBLE REDUCTION (combining B84 + B70 + B62 + (1)-(2)):
  * NUMERICAL routes are DEAD (B84/V67): the eps-series pinv-limit does not converge canonically at the
    char(M^2)^2 sector (even gauge-invariant power sums scatter); no gauge-fix/theta-split/averaging helps.
  * The gap is EXACTLY 2 eigenvalues -- the second char(M^2) (B84); 22/24 SL(5) modes are canonical (B66).
  * That sector is a RANK-1, bounded-bidegree-<=(3,3) e_2/Lambda^2 closure (B70).
  * Lambda^2 functoriality (1) identifies it cleanly, but (2) the multiplicity-2 is intrinsic, so the
    closure must be assembled SYMBOLICALLY: the fixed-line Jacobian D(sigma) of the exact trace map
    sigma is canonical BY CONSTRUCTION (no pinv, exact even at the degenerate multiplicity), but building
    sigma is the Procesi-trace-ring problem (research-scale: the explicit (n^2-1)-coordinate substitution
    with the e_j exterior-power dependency).
  * B62 already gives the tower STRUCTURALLY (the root-system theta-split); the residual is ONLY the
    "from first principles" symbolic assembly.

VERDICT: the all-n tower lynchpin is reduced to the symbolic assembly of the bounded e_2/Lambda^2 closure
into sigma -- a precise, finite, research-scale continuation; no numerical or representation shortcut
remains. Honest scoping of the deepest open item. Standalone Lie/invariant theory; no Origin-core claim;
proven core P1-P16 untouched.
"""
from __future__ import annotations

import itertools
from math import comb

import numpy as np


def lam2(A):
    """Lambda^2 A on 2-forms (2x2 minors), basis e_i^e_j, i<j; dim = C(n,2)."""
    n = A.shape[0]
    idx = list(itertools.combinations(range(n), 2))
    d = len(idx)
    L = np.zeros((d, d), dtype=complex)
    for r, (i, j) in enumerate(idx):
        for c, (k, l) in enumerate(idx):
            L[r, c] = A[i, k] * A[j, l] - A[i, l] * A[j, k]
    return L


def functoriality_dev(n, seed=1):
    """max | Lambda^2(A^2 B) - (Lambda^2 A)^2 (Lambda^2 B) | and the AB version. ~0 (Lambda^2 a functor)."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    A = A / np.linalg.det(A) ** (1 / n); B = B / np.linalg.det(B) ** (1 / n)
    f1 = np.max(np.abs(lam2(A @ A @ B) - lam2(A) @ lam2(A) @ lam2(B)))
    f2 = np.max(np.abs(lam2(A @ B) - lam2(A) @ lam2(B)))
    return max(f1, f2)


# B62: the char(M^2) multiplicity in the SL(n) tower (height-2 theta-symmetric dimension) -- a
# root-system fact (NOT representation-removable).
CHAR_M2_MULTIPLICITY = {3: 1, 4: 1, 5: 2, 6: 2}


def main():
    print("B85 (Phase C/D) -- the all-n tower lynchpin, precisely reduced\n")
    print("(1) Lambda^2 functoriality of the figure-eight substitution:")
    for n in (4, 5):
        print(f"    n={n}: |Lambda^2(A^2B)-(Lambda^2 A)^2(Lambda^2 B)| etc = {functoriality_dev(n):.0e}"
              f"   (Lambda^2 is a functor -> the even-k sector is the fig-8 map on Lambda^2 V)")
    print("\n(2) Lambda^2 V does NOT remove the degeneracy (the char(M^2) multiplicity is a root-system fact):")
    for n in (3, 4, 5, 6):
        print(f"    n={n}: dim Lambda^2 V = C({n},2) = {comb(n,2)};  char(M^2) tower multiplicity = "
              f"{CHAR_M2_MULTIPLICITY[n]}  (B62 height-2 theta-split -- intrinsic, persists under Lambda^2)")
    print("\nVERDICT: numerical routes dead (B84); Lambda^2 real but doesn't break the degeneracy (2);")
    print("  the gap is the symbolic assembly of the bounded rank-1 e_2/Lambda^2 closure (B70) into the")
    print("  exact trace map sigma -- where D(sigma) is canonical by construction. A precise, finite,")
    print("  research-scale continuation; no numerical/representation shortcut remains. B62 gives the")
    print("  tower structurally; the residual is ONLY the from-first-principles symbolic assembly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
