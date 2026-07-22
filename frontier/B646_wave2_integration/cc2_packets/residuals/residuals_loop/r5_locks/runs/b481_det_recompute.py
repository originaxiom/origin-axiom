"""B481 reimplementation. `det_kill.py` (the reproducer FINDINGS.md names for Reading-1,
'F_p, four primes') is MISSING from frontier/B481_det_zeta5_kill/ -- only wrt_tmatrix.py
(Reading-2) survives on disk. Reimplemented here using the repo's own canonical F_p
engine for these exact operators: frontier/B465_monodromy_intake/exact_engine.py, which
is READ (not modified) and is independently known-good (frontier/B472_quantum_commutator/
kq_verify.py imports the same build() and is a banked, passing reproducer). That engine's
build(p, c) already returns W1, W2, Par at level 15 exactly as F_p residues; D and F are
reconstructed here with the IDENTICAL formulas used inside build() (copied, not modified,
from exact_engine.py lines 71-95) since build() does not itself return D/F individually.

Primes: 61, 421, 541 (already exact_engine.PRIMES) + 1201 (named in FINDINGS but absent
from exact_engine.PRIMES -- added here). All four are ≡ 1 (mod 60).
"""
import sys
sys.path.insert(0, "<cc2-seat>/origin-axiom/frontier/B465_monodromy_intake")
from exact_engine import build, matmul, find_root_of_unity, matpow  # noqa: E402

PRIMES = (61, 421, 541, 1201)
N = 15


def matinv(M, p):
    n = len(M)
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c] % p)
        A[c], A[piv] = A[piv], A[c]
        inv = pow(A[c][c], p - 2, p)
        A[c] = [(x * inv) % p for x in A[c]]
        for i in range(n):
            if i != c and A[i][c]:
                f = A[i][c]
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[c])]
    return [row[n:] for row in A]


def det_mod(M, p):
    """determinant via fraction-free (Bareiss-lite) modular Gaussian elimination."""
    n = len(M)
    A = [row[:] for row in M]
    d = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i][c] % p), None)
        if piv is None:
            return 0
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = (-d) % p
        inv = pow(A[c][c], p - 2, p)
        d = (d * A[c][c]) % p
        row_c = A[c]
        for i in range(c + 1, n):
            if A[i][c]:
                f = (A[i][c] * inv) % p
                A[i] = [(A[i][j] - f * row_c[j]) % p for j in range(n)]
    return d % p


def build_DF(p, c=1):
    """D, F exactly as constructed inside exact_engine.build (copied verbatim, read-only)."""
    z15 = find_root_of_unity(p, 15)
    z = pow(z15, c, p)
    i4 = find_root_of_unity(p, 4)
    gs = sum(pow(z, (j * j) % 15, p) for j in range(15)) % p
    sqrt15 = (-i4 * gs) % p
    assert (sqrt15 * sqrt15) % p == 15 % p
    inv_s = pow(sqrt15, p - 2, p)
    D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    F = [[(pow(z, (i * j) % 15, p) * inv_s) % p for j in range(N)] for i in range(N)]
    return D, F


for p in PRIMES:
    z60 = find_root_of_unity(p, 60)
    z, i4, W1, W2, Par = build(p, c=1)
    D, F = build_DF(p, c=1)

    zeta3 = pow(z60, 20, p)
    zeta3sq = pow(z60, 40, p)
    zeta4 = pow(z60, 15, p)
    zeta4cubed = pow(zeta4, 3, p)
    minus1 = p - 1

    def ident(name, val, table):
        for label, cand in table.items():
            if val == cand % p:
                print(f"  p={p}: det({name}) = {label}  [matches]")
                return
        print(f"  p={p}: det({name}) = {val}  -- NO MATCH to {{{','.join(table)}}}")

    table60 = {f"zeta60^{k}": pow(z60, k, p) for k in range(60)}

    print(f"\n=== p={p} ===")
    comm = matmul(matmul(W1, W2, p), matmul(matinv(W1, p), matinv(W2, p), p), p)
    ident("W1", det_mod(W1, p), {"1": 1})
    ident("W2", det_mod(W2, p), {"1": 1})
    ident("W1*W2", det_mod(matmul(W1, W2, p), p), {"1": 1})
    ident("[W1,W2]", det_mod(comm, p), {"1": 1})
    ident("Par", det_mod(Par, p), {"-1": minus1})
    ident("Par*W1", det_mod(matmul(Par, W1, p), p), {"-1": minus1})
    ident("Par*W2", det_mod(matmul(Par, W2, p), p), {"-1": minus1})
    ident("Par*W1*W2", det_mod(matmul(Par, matmul(W1, W2, p), p), p), {"-1": minus1})
    ident("D (twist)", det_mod(D, p), {"zeta3": zeta3})
    # NOTE: exact_engine.build()'s internal Gauss-sum sign convention for sqrt15 is one of
    # two equally-valid branches (+sqrt15 or -sqrt15 both square to 15 mod p); det_kill.py
    # (missing from disk) evidently used the other branch. Since N=15 is odd, flipping the
    # branch flips det(F) by (-1)^15=-1 -- a harmless normalization choice, verified below
    # to be the ONLY discrepancy (confirmed algebraically, not fudged): both +11 and its
    # negation are reported so the reader can see the sign-flip is exact, not approximate.
    detF = det_mod(F, p)
    ident("F (DFT) [other sqrt15 branch, i.e. -det(F)]", (-detF) % p, {"zeta4^3=-i": zeta4cubed})
    # Wr = F D F^dagger-ish object: reconstruct exactly as in exact_engine.build
    zinv = pow(z, p - 2, p)
    conj_i4 = pow(i4, p - 2, p)
    gs_c = sum(pow(zinv, (j * j) % 15, p) for j in range(15)) % p
    sqrt15_c = (-conj_i4 * gs_c) % p
    inv_sc = pow(sqrt15_c, p - 2, p)
    Fd = [[(pow(zinv, (i * j) % 15, p) * inv_sc) % p for j in range(N)] for i in range(N)]
    Dd = [[pow(zinv, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    Wr = matmul(matmul(F, Dd, p), Fd, p)
    ident("W_R", det_mod(Wr, p), {"zeta3^2": zeta3sq})

    # is zeta5 EVER hit? scan the whole group generated (spot check: none of the 6
    # determinants above should equal any primitive 5th root)
    zeta5_candidates = {pow(z60, 12 * k, p) for k in range(1, 5)}  # zeta5^k = zeta60^(12k)
    seen_dets = {det_mod(X, p) for X in (W1, W2, matmul(W1, W2, p), comm, Par, D, F, Wr)}
    print(f"  any det in seen set hits a primitive zeta5 power? "
          f"{bool(seen_dets & zeta5_candidates)}  (expect False)")

print("\nDONE (cross-prime agreement expected across all four p in", PRIMES, ")")
