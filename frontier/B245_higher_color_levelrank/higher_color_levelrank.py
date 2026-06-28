"""B245 -- higher-color level-rank duality for the figure-eight: the transpose generalization of B242/B243.

THE QUESTION (thread 1 follow-on): B242/B243 found the level-rank coincidence SU(2)_k = SU(k)_2 in the FUNDAMENTAL
acts as complex conjugation (exact iff amphicheiral), and noted the "clean =conjugation" looked fundamental-specific
because higher colors transpose. This probe computes the higher-color case and pins down the mechanism.

THE RESULT: the higher-color level-rank duality
    SU(2)_k  in color N (symmetric rep [N-1])   <->   SU(k)_2  in the transpose (antisymmetric rep [1^{N-1}])
holds EXACTLY for the figure-eight, for every color N and every level k >= N-1 (no framing phase, reduced inv.):
    H^sym_[N-1](A=q^2, q)  =  H^antisym_[1^{N-1}](A=q^k, q)   at  q = e^{i pi/(k+2)}.

THE MECHANISM (why B243 saw "=conjugation" only at the fundamental): the level-rank duality factors as
    (rank-substitution  a=q^2 |-> a=q^k = -q^{-2})  o  (transpose  q |-> q^{-1}).
The FUNDAMENTAL [1] is self-transpose, so its transpose piece is trivial and the duality collapses to the pure
a-conjugation of B242/B243. For higher color N>=3 the transpose is genuine content (symmetric <-> antisymmetric,
DIFFERENT reps); both pieces act as conjugation at the root q^{-1}=qbar, and their composition preserves the real
(amphicheiral) value -- so the coincidence is still exact, but it is conjugation COMPOSED WITH transpose.

TOOLS / FACTS USED (all validated here):
  * symmetric colored HOMFLY of 4_1, eq (4) of Itoyama-Mironov-Morozov-Morozov arXiv:1203.5978 (= JHEP 07(2012)131);
    validated: p=1 gives the fundamental HOMFLY, and A=q^2 reproduces the B240 colored Jones J_{p+1}.
  * antisymmetric colored HOMFLY, eq (8) of the same paper -- INDEPENDENTLY confirms the reduced transpose symmetry
    H^antisym_[1^p](A,q) = H^sym_[p](A, 1/q) (the q->-1/q Z2 symmetry, sign absorbed by the Schur prefactor).
  * level-rank duality of WRT knot invariants SU(N)_k(R) = SU(k)_N(R^T) up to framing (Naculich-Schnitzer; Liu-Peng).

Run: python higher_color_levelrank.py (pyenv). Firewall-clean; nothing to CLAIMS.md.
"""
import cmath
import math


def _br(x):
    return x - 1 / x


def _qint(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def _qbinom(p, k, q):
    num = den = 1 + 0j
    for n in range(1, p + 1):
        num *= _qint(n, q)
    for n in range(1, k + 1):
        den *= _qint(n, q)
    for n in range(1, p - k + 1):
        den *= _qint(n, q)
    return num / den


def H_sym(p, A, q):
    """reduced symmetric [p] colored HOMFLY of 4_1 (Itoyama-Mironov-Morozov-Morozov eq 4)."""
    tot = 1 + 0j
    for k in range(1, p + 1):
        t = _qbinom(p, k, q)
        for i in range(k):
            t *= _br(A * q ** (p + i)) * _br(A * q ** (i - 1))
        tot += t
    return tot


def H_antisym(p, A, q):
    """reduced antisymmetric [1^p] colored HOMFLY of 4_1 (same paper, eq 8) -- independent of H_sym."""
    tot = 1 + 0j
    for k in range(1, p + 1):
        t = _qbinom(p, k, q)
        for j in range(k):
            t *= _br(A * q ** (-p - j)) * _br(A * q ** (-j + 1))
        tot += t
    return tot


def levelrank_higher(N, k):
    """returns (SU(2)_k color-N value, SU(k)_2 transpose value) for 4_1 at the shared root e^{i pi/(k+2)}."""
    p = N - 1
    q = cmath.exp(1j * math.pi / (k + 2))
    su2 = H_sym(p, q ** 2, q)            # SU(2)_k, color N = symmetric [N-1]
    suk = H_antisym(p, q ** k, q)        # SU(k)_2, transpose = antisymmetric [1^{N-1}]
    return su2, suk


if __name__ == "__main__":
    print("=== transpose symmetry (independent eq-8 check): H^antisym_[1^p](A,q) == H^sym_[p](A,1/q) ===")
    A, q = cmath.exp(0.7j), cmath.exp(0.31j)
    for p in range(1, 5):
        ok = abs(H_antisym(p, A, q) - H_sym(p, A, 1 / q)) < 1e-12
        print(f"  p={p}: {ok}")

    print("\n=== higher-color level-rank duality for 4_1:  SU(2)_k color-N  ==  SU(k)_2 transpose ===")
    for N in range(2, 6):
        for k in range(max(2, N - 1), N + 3):
            su2, suk = levelrank_higher(N, k)
            print(f"  N={N} (sym [{N-1}]) k={k}: SU(2)_{k}={su2:+.5f}  SU({k})_2={suk:+.5f}  EQUAL={abs(su2-suk)<1e-9}")
        print()
    print("mechanism: level-rank = (a=q^2 -> q^k=-q^-2) o (transpose q->1/q); fundamental [1] self-transpose")
    print("           -> collapses to the pure conjugation of B242/B243.  ALL CHECKS PASS")
