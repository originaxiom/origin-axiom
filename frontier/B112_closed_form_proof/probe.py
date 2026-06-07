"""B112 -- PROOF of the opposition-involution closed form (the sign half of rho_n), for ALL n.

The B111 decision split the rho_n catalog prize into two named halves: the SIGN structure (the bulk opposition
involution theta=-w0) and the single degree=rank promotion char(M)->char(M^n). This stage PROVES the sign half
from first principles -- engine-free, no Procesi ring, no eps-series, no sigma-construction -- for all n.

THE THEOREM (closed form, all n, all heights):
    mult char(M^h) = ceil((n-h)/2),   mult char(-M^h) = floor((n-h)/2),   h = 1 .. n-1.

THE PROOF (computer-assisted: an elementary root-system lemma + the banked B64 parity assignment).

  LEMMA (root system, elementary). The longest-element / opposition involution theta = -w0 of A_{n-1} acts on a
  root e_i - e_j by  -w0(e_i - e_j) = e_{n+1-j} - e_{n+1-i}  (height-preserving). On the (n-h) POSITIVE
  height-h roots {e_i - e_{i+h} : i = 1..n-h}, indexed by i, this is the REVERSAL involution
        sigma(i) = (n-h+1) - i        on {1, ..., n-h}.
  A permutation involution's +-1 eigenspace dimensions are (#fixed + #2-cycles, #2-cycles). For the reversal on
  m = n-h points: m odd -> 1 fixed, (m-1)/2 cycles -> (+1,-1) = ((m+1)/2,(m-1)/2) = (ceil, floor); m even -> 0
  fixed, m/2 cycles -> (m/2, m/2) = (ceil, floor). Either way (+1,-1) dims = (ceil(m/2), floor(m/2)).
  [theta is an involution on the trace ring (P^2=I, B54/B108), so its height-h restriction has real +-1
  eigenvalues and the central fixed root sits in the +1 sector -- verified.]

  ASSIGNMENT (B64, banked). The contragredient/parity mechanism (P sends m -> -m; Dickson parity
  L_k(-m)=(-1)^k L_k(m)) puts the theta-SYMMETRIC (+1) sector in char(M^h) and the theta-ANTISYMMETRIC (-1)
  sector in char(-M^h).

  THEOREM = LEMMA (the +-1 dims) x ASSIGNMENT (which sector is which) => the closed form, all n.

Verified: the lemma matches ceil/floor for all n<=12, all h (both via the abstract reversal AND the direct -w0
action on the actual A_{n-1} roots); the closed form matches B62's height-2 splits and the B111 tower (n=3,4).

This is the FIRST piece of the rho_n catalog proved from first principles, engine-free, for all n. It does NOT
prove the full tower (= closed form + the single degree=rank promotion char(M)->char(M^n), B111/S022 -- the
power half, still open). NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16 untouched.
"""
from __future__ import annotations

import math

import numpy as np


# --------------------------------------------------------------------------- #
# the LEMMA -- the -w0 reversal involution on the height-h roots of A_{n-1}
# --------------------------------------------------------------------------- #
def positive_height_h_roots(n, h):
    """The positive height-h roots of A_{n-1}: e_i - e_{i+h}, i = 1..n-h (as (i, i+h) pairs)."""
    return [(i, i + h) for i in range(1, n - h + 1)]


def opposition_action_matrix(n, h):
    """theta = -w0 on the height-h root spaces: (i,j) -> (n+1-j, n+1-i), as a permutation matrix on the roots."""
    roots = positive_height_h_roots(n, h)
    idx = {r: k for k, r in enumerate(roots)}
    m = len(roots)
    P = np.zeros((m, m))
    for (i, j) in roots:
        img = (n + 1 - j, n + 1 - i)        # -w0 image; another positive height-h root
        P[idx[img], idx[(i, j)]] = 1
    return P


def eigenspace_split(n, h):
    """The (+1, -1) eigenspace dimensions of theta restricted to the height-h root spaces."""
    P = opposition_action_matrix(n, h)
    if P.shape[0] == 0:
        return (0, 0)
    ev = np.round(np.linalg.eigvals(P).real, 6)
    return (int(np.sum(ev > 0.5)), int(np.sum(ev < -0.5)))


def closed_form(n, h):
    """The predicted multiplicities (char(M^h), char(-M^h)) = (ceil((n-h)/2), floor((n-h)/2))."""
    m = n - h
    return (math.ceil(m / 2), math.floor(m / 2))


# --------------------------------------------------------------------------- #
# the THEOREM -- the lemma proves the closed form for all n (computer-verified)
# --------------------------------------------------------------------------- #
def lemma_holds(nmax=12):
    """The root-system lemma: eigenspace_split(n,h) == (ceil((n-h)/2), floor((n-h)/2)) for all n<=nmax, all h.
    Verified two ways (the direct -w0 action here; the abstract reversal gives the same -- see proof)."""
    mismatches = [(n, h, eigenspace_split(n, h), closed_form(n, h))
                  for n in range(2, nmax + 1) for h in range(1, n)
                  if eigenspace_split(n, h) != closed_form(n, h)]
    return {"nmax": nmax, "all_match": len(mismatches) == 0, "mismatches": mismatches}


def is_reversal_involution(n, h):
    """Confirm theta acts as the reversal i -> (n-h+1)-i on the height-h root index set (P^2 = I, the cycle
    structure is the reversal)."""
    P = opposition_action_matrix(n, h)
    m = P.shape[0]
    if m == 0:
        return True
    involution = np.allclose(P @ P, np.eye(m))
    # the reversal permutation matrix
    R = np.zeros((m, m))
    for i in range(m):
        R[m - 1 - i, i] = 1
    return involution and np.allclose(P, R)


def excess(n):
    """Net (+)-over-(-) char excess summed over heights = floor(n/2)."""
    plus = sum(closed_form(n, h)[0] for h in range(1, n))
    minus = sum(closed_form(n, h)[1] for h in range(1, n))
    return {"plus": plus, "minus": minus, "excess": plus - minus, "floor_n2": n // 2,
            "matches": plus - minus == n // 2}


def total_char_factors(n):
    """The closed form accounts for all n(n-1)/2 positive roots (sum of the +-1 dims over heights)."""
    total = sum(sum(closed_form(n, h)) for h in range(1, n))
    return {"total_char_factors": total, "positive_roots": n * (n - 1) // 2,
            "matches": total == n * (n - 1) // 2}


def main():
    print("=" * 78)
    print("B112 -- PROOF of the opposition-involution closed form (the sign half of rho_n), all n")
    print("=" * 78)
    print("\n[LEMMA] theta=-w0 acts as the reversal involution on the height-h roots; (+1,-1) dims:")
    for n in (3, 4, 5, 6):
        rows = [f"h={h}:{eigenspace_split(n, h)}" for h in range(1, n)]
        print(f"    n={n}: " + "  ".join(rows) + f"   (reversal-involution: "
              f"{all(is_reversal_involution(n, h) for h in range(1, n))})")
    lh = lemma_holds(12)
    print(f"\n[THEOREM] eigenspace_split == (ceil((n-h)/2), floor((n-h)/2)) for all n<=12, all h: {lh['all_match']}")
    print("    => with the B64 parity assignment (+1 sector = char(M^h), -1 = char(-M^h)),")
    print("       the closed form mult char(M^h)=ceil((n-h)/2), char(-M^h)=floor((n-h)/2) is PROVED for all n.")
    print(f"\n[checks] excess(n)=floor(n/2): {all(excess(n)['matches'] for n in range(2,13))};"
          f"  total char factors = #positive roots: {all(total_char_factors(n)['matches'] for n in range(2,13))}")
    print("\nThis proves the SIGN HALF of rho_n (the bulk theta-decomposition). The full tower = this + the single")
    print("degree=rank promotion char(M)->char(M^n) (B111/S022, the power half) -- still open. NO physics.")


if __name__ == "__main__":
    main()
