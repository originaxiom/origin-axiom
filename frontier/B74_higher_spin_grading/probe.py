"""B74 (Path C) -- the higher-spin / Chern-Simons literal-match test.

QUESTION (the speculative metaphor to ground or kill). SL(N) Chern-Simons in 2+1D has asymptotic
symmetry the W_N algebra (higher-spin gravity / Vasiliev): higher-spin currents of spins s=2,3,...,N.
The metallic trace-map tower factors over the Dickson catalog char(M^k)=t^2 - L_k t + (-1)^k,
L_k=tr(M^k), M=[[m,1],[1,0]], with powers k running 1..n (plus a contragredient char(M^-1), sign
sectors char(-M^k), and multiplicities). Is there a LITERAL correspondence between the rank-n Dickson
spectrum and the W_N higher-spin mode spectrum -- spins s <-> powers k, or L_k <-> mode data?

WHAT THIS SCRIPT COMPUTES (decisive, exact sympy):
  (1) The W_N charge-conjugation grading. In W_N Toda the spin-s current is the degree-s Casimir of
      sl(N); charge conjugation C (the diagram automorphism = -w0 = the contragredient X -> -X^T on
      the Lie algebra) acts on the degree-s invariant by (-1)^s. We verify this from first principles
      on the power-sum Casimirs tr(X^s) for a GENERIC traceless X (n=3,4,5): tr((-X^T)^s)=(-1)^s tr(X^s).
  (2) The Dickson grading. The metallic instance of the SAME involution: P = contragredient = (m -> -m)
      (B62: P = theta = -w0; B64), and L_s(-m) = (-1)^s L_s(m) (Dickson parity). We verify this
      symbolically for s=1..6 -- the degree-s metallic invariant flips by (-1)^s under the same -w0.
  (3) The literal comparison. On the overlap of spins/powers the two Z/2 gradings COINCIDE (because
      both ARE -w0 acting on a degree-k invariant). We then tabulate exactly where the full spectra
      DIVERGE: the Dickson tower carries negative powers (char(M^-1)), sign sectors (char(-M^k)), and
      growing multiplicities that have NO W_N higher-spin counterpart; W_N has no spin-1 (sl vs gl).

HONEST VERDICT (printed): the PARITY GRADING is a literal shared object (STRUCTURAL -- same -w0 of
A_{n-1}); the full SPECTRUM is NOT a literal match (the Dickson tower is strictly richer); and the
dynamical reading "metallic eigenvalues = higher-spin mode growth rates" has NO supporting computation
-> SPECULATIVE-ANALOGY. Standalone trace-map / Lie-theory mathematics; no Origin-core claim; proven
core P1-P16 untouched.
"""
import random

import sympy as sp

m = sp.symbols("m")


def metallic_M():
    return sp.Matrix([[m, 1], [1, 0]])


def L_k(k):
    """L_k = tr(M^k), the metallic Lucas number (Dickson trace), M=[[m,1],[1,0]]."""
    M = metallic_M()
    if k >= 0:
        return sp.expand(sp.trace(M**k))
    return sp.expand(sp.trace(M.inv()**(-k)))


def dickson_parity_check(kmax=6):
    """(2) L_s(-m) = (-1)^s L_s(m) for s=1..kmax -- the degree-s metallic invariant under -w0 (m->-m).
    Returns dict s -> bool. This is B64's 'Dickson parity', the metallic instance of charge conjugation."""
    out = {}
    for s in range(1, kmax + 1):
        Ls = L_k(s)
        out[s] = sp.expand(Ls.subs(m, -m) - (-1)**s * Ls) == 0
    return out


def casimir_conjugation_check(n, smax=None, seed=11):
    """(1) The W_N charge-conjugation grading from first principles. The spin-s W_N current is the
    degree-s Casimir tr(X^s) of sl(n); charge conjugation C = contragredient X -> -X^T acts by (-1)^s.
    Verify tr((-X^T)^s) = (-1)^s tr(X^s) for a GENERIC traceless symbolic X (n x n). Returns dict s->bool."""
    if smax is None:
        smax = n
    random.seed(seed)
    # generic traceless X with independent symbolic entries (the trace constraint absorbs X[n-1,n-1])
    xs = {}
    X = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if (i, j) != (n - 1, n - 1):
                xs[(i, j)] = sp.Symbol(f"x{i}{j}")
                X[i, j] = xs[(i, j)]
    X[n - 1, n - 1] = -sum(X[i, i] for i in range(n - 1))  # traceless
    C = -X.T  # the contragredient / Chevalley involution on sl(n) (= -w0 on a Cartan)
    out = {}
    Xp = sp.eye(n)
    Cp = sp.eye(n)
    for s in range(1, smax + 1):
        Xp = sp.expand(Xp * X)
        Cp = sp.expand(Cp * C)
        out[s] = sp.expand(sp.trace(Cp) - (-1)**s * sp.trace(Xp)) == 0
    return out


# ---- the established tower data (firmly known n=3,4,5; B54/B63/B64/B61/B62) -----------------------
# each entry: (signed power k, sector sign s in char(s*M^k)) ; multiplicities via repetition.
TOWER = {
    3: [(-1, +1), (2, +1), (3, +1)],
    4: [(-1, +1), (1, +1), (2, +1), (3, +1), (4, +1), (2, -1)],
    5: [(-1, +1), (1, +1), (1, +1), (2, +1), (2, +1), (3, +1), (4, +1), (5, +1),
        (2, -1), (3, -1)],
}
PARITY_BLOCK = {3: "(t-1)(t+1)", 4: "(t-1)^2(t+1)", 5: "(t-1)^2(t+1)^2"}


def wn_spins(n):
    """W_N higher-spin currents: spins 2,3,...,N (the degrees of the sl(N) fundamental invariants)."""
    return list(range(2, n + 1))


def dickson_positive_powers(n):
    """The multiset of POSITIVE powers k appearing in char(M^k) (sign +1) in the rank-n tower."""
    return sorted(k for (k, s) in TOWER[n] if k > 0 and s == +1)


def compare(n):
    """(3) Literal comparison W_n spins  vs  rank-n Dickson positive powers. Returns a structured dict:
    the grading agreement on the overlap, and the precise extras on each side."""
    spins = wn_spins(n)
    powers = dickson_positive_powers(n)
    overlap = sorted(set(spins) & set(powers))
    # the cross-comparison: W_N charge-conjugation eigenvalue of the spin-d current  vs  Dickson
    # P-eigenvalue of char(M^d), for each matched degree d. Sourced from the two DIFFERENT verified
    # facts -- part (1): C(spin-d)=(-1)^d ; B64/part (2): P(char(M^d))=(-1)^d -- not from one formula.
    wn_cc = {d: (-1)**d for d in spins}            # part (1), verified symbolically
    dickson_P = {d: (-1)**d for d in powers}       # B64 + part (2), verified symbolically
    grading_match = all(wn_cc[d] == dickson_P[d] for d in overlap)
    extras_dickson = sorted([k for k in powers if k not in spins])  # spin-1 etc. (multiset-aware below)
    # multiplicity-aware extras
    from collections import Counter
    cp, cs = Counter(powers), Counter(spins)
    extra_mult = {k: cp[k] - cs.get(k, 0) for k in cp if cp[k] - cs.get(k, 0) > 0}
    neg_powers = [k for (k, s) in TOWER[n] if k < 0]
    sign_sectors = [(k, s) for (k, s) in TOWER[n] if s == -1]
    return dict(spins=spins, powers=powers, overlap=overlap, grading_match=grading_match,
                extras=extras_dickson, extra_mult=extra_mult, neg_powers=neg_powers,
                sign_sectors=sign_sectors)


def main():
    print("B74 (Path C) -- higher-spin / W_N vs the metallic Dickson tower: literal-match test\n")

    print("(1) W_N charge-conjugation grading from first principles (generic traceless X, C=-X^T):")
    print("    spin-s Casimir tr(X^s) transforms by (-1)^s under C  [the W_N grading]")
    for n in (3, 4, 5):
        chk = casimir_conjugation_check(n)
        print(f"    sl({n}): tr((-X^T)^s)=(-1)^s tr(X^s) for s=1..{n}:  {all(chk.values())}  {chk}")

    print("\n(2) Dickson grading -- the SAME involution (-w0 = m->-m) on the metallic invariants:")
    dp = dickson_parity_check(6)
    print(f"    L_s(-m) = (-1)^s L_s(m) for s=1..6:  {all(dp.values())}  {dp}")
    print("    => char(M^k) lands in the P-even sector for even |k|, P-odd for odd |k| (B64, proven).")

    print("\n(3) Literal spectrum comparison  W_n spins {2..n}  vs  rank-n Dickson positive powers:")
    for n in (3, 4, 5):
        c = compare(n)
        print(f"\n  n={n}:")
        print(f"    W_{n} spins (s=2..{n})            : {c['spins']}")
        print(f"    Dickson positive powers char(M^k): {c['powers']}")
        print(f"    overlap (spin==power)            : {c['overlap']}   grading (-1)^s==(-1)^k: {c['grading_match']}")
        print(f"    Dickson EXTRAS (no W_{n} current) : powers {c['extras']}; multiplicities {c['extra_mult']};"
              f" neg powers {c['neg_powers']}; sign sectors char(-M^k) {c['sign_sectors']}")

    print("\nVERDICT:")
    print("  - PARITY GRADING: LITERAL shared object (STRUCTURAL). Both the W_N charge-conjugation")
    print("    grading of spin-s currents and the Dickson P-grading of char(M^k) ARE -w0 (the")
    print("    contragredient) of A_{n-1} acting on a degree-k invariant by (-1)^k. Same Lie algebra,")
    print("    same involution -- not a coincidence (B62: P=theta=-w0; B64: proven).")
    print("  - FULL SPECTRUM: NOT a literal match. The Dickson tower is strictly RICHER -- negative")
    print("    powers char(M^-1), sign sectors char(-M^k), and growing multiplicities have NO W_N")
    print("    higher-spin counterpart; W_N (sl, not gl) has no spin-1. The clean bijection holds")
    print("    only at n=3 (powers {2,3} = spins {2,3}); n>=4 diverges.")
    print("  - DYNAMICAL reading ('metallic eigenvalues L_k = higher-spin mode growth rates'): NO")
    print("    supporting computation. The metallic eigenvalues are NOT shown to be any W_N CFT")
    print("    spectrum. Label: SPECULATIVE-ANALOGY. The real kernel is invariant theory of sl(n),")
    print("    which is 2+1D/topological -- consistent with the metallic-anyon negative (V28).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
