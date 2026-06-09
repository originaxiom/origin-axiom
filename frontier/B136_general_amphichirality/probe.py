"""B136 -- the amphichirality criterion for ALL once-punctured-torus bundles (general LR words).

Phase B-generalization of the approved program: extend the now-proved metallic chirality recursion (B134) from the
metallic locus (R^m L^m blocks, B128/K011) to ANY once-punctured-torus bundle (any LR monodromy word). Re-derived
in-sandbox; provable the same way (it is Goodman-Heard-Hodgson's anti-palindromic criterion in block-pair form).

ONE-LINE RESULT. A once-punctured-torus bundle with monodromy W = R^{a1}L^{b1} R^{a2}L^{b2} ... R^{ak}L^{bk} is
AMPHICHIRAL  <=>  the block-pair sequence ((a1,b1),...,(ak,bk)) is invariant under (REVERSE the order AND SWAP each
pair's components (a,b)->(b,a)) up to CYCLIC ROTATION. The metallic case a_i=b_i reduces this to "the block-length
sequence is a cyclic palindrome" (B134), so B136 is the strict generalization.

  ============================================================================================================
  THE THEOREM (proved, as a corollary of GHH 2008):
    By GHH 2008 (arXiv:0801.4815), amphichiral <=> W is ANTI-palindromic, i.e. reverse(W) = swap_{L<->R}(W) cyclically.
      reverse(R^{a1}L^{b1}...R^{ak}L^{bk}) = L^{bk}R^{ak} ... L^{b1}R^{a1}    (order reverses; each R^aL^b -> L^bR^a)
      swap_{L<->R}(R^{a1}L^{b1}...)        = L^{a1}R^{b1} ... L^{ak}R^{bk}
    Both are "L^x R^y" block-words; reading the (L-exp, R-exp) pairs gives ((b_k,a_k),...,(b_1,a_1)) and
    ((a_1,b_1),...,(a_k,b_k)). Equal cyclically  <=>  the first is a cyclic rotation of the second  <=>  the pair
    sequence ((a_i,b_i)) is fixed (up to rotation) by "reverse order + swap components". QED.
    SPECIALIZATION: a_i=b_i=m_i => swap is trivial => (m_k,...,m_1) a cyclic rotation of (m_1,...,m_k) = cyclic
    palindrome = B134. So B134 is the a_i=b_i corner of B136.

  Verified: the pair-sequence criterion == anti_palindromic(W) (string) == SnapPy is_amphicheiral, on metallic AND
  genuinely-non-metallic words (a_i != b_i), e.g. (1,2),(2,1) amphichiral; (1,3),(3,1) amphichiral; (1,2),(1,2) chiral.
"""
from __future__ import annotations

import itertools


def pairs_to_word(ps):
    return "".join("R" * a + "L" * b for a, b in ps)


def _cyc_eq(a, b):
    a, b = list(a), list(b)
    n = len(a)
    return n == len(b) and any(a == b[i:] + b[:i] for i in range(n))


def pair_criterion(ps):
    """((a_i,b_i)) fixed up to cyclic rotation by (reverse order + swap components)  <=>  amphichiral (GHH)."""
    transformed = [(b, a) for (a, b) in reversed(list(ps))]
    return _cyc_eq(transformed, list(ps))


def anti_palindromic(w):
    sw = w.translate(str.maketrans("RL", "LR"))
    return len(w) == len(sw) and sw in (w[::-1] + w[::-1])


def lemma_exhaustive(max_blocks=4, max_exp=3):
    """anti_palindromic(W) <=> pair_criterion(pairs), for ALL block-pair sequences (combinatorial certificate)."""
    checked = 0
    for k in range(1, max_blocks + 1):
        for ps in itertools.product(itertools.product(range(1, max_exp + 1), repeat=2), repeat=k):
            if anti_palindromic(pairs_to_word(ps)) != pair_criterion(ps):
                return {"holds": False, "counterexample": ps, "checked": checked}
            checked += 1
    return {"holds": True, "checked": checked}


def specializes_to_metallic(max_len=5, max_m=4):
    """Check B136 reduces to B134 on the metallic locus a_i=b_i: pair_criterion == cyclic-palindrome(m-seq)."""
    def cyc_pal(seq):
        seq = tuple(seq); rev = tuple(reversed(seq)); n = len(seq)
        return rev in {seq[i:] + seq[:i] for i in range(n)}
    ok = True
    for k in range(1, max_len + 1):
        for seq in itertools.product(range(1, max_m + 1), repeat=k):
            if pair_criterion([(m, m) for m in seq]) != cyc_pal(seq):
                ok = False
    return {"reduces_to_B134": ok}


def snappy_threeway(samples=None):
    try:
        import snappy
    except Exception:
        return None
    if samples is None:
        samples = [[(1, 1)], [(1, 2)], [(2, 1)], [(1, 2), (2, 1)], [(1, 3), (3, 1)], [(1, 2), (1, 2)],
                   [(2, 1), (1, 1), (1, 2)], [(2, 3), (3, 2)], [(1, 1), (2, 2)], [(2, 2), (3, 1), (2, 2)]]
    rows = []
    allok = True
    for ps in samples:
        w = pairs_to_word(ps)
        M = snappy.Manifold("b++" + w)
        sg = M.symmetry_group()
        amph = sg.is_amphicheiral() if sg.is_full_group() else None
        pc, ap = pair_criterion(ps), anti_palindromic(w)
        ok = (pc == ap == bool(amph))
        allok = allok and ok
        rows.append((ps, pc, ap, amph, ok))
    return {"rows": rows, "all_agree": allok}


def main():
    print("=" * 96)
    print("B136 -- amphichirality for ALL once-punctured-torus bundles (general LR words)")
    print("=" * 96)
    print("\n[lemma -- anti_palindromic(W) == pair_criterion(pairs), exhaustive]")
    print("    ", lemma_exhaustive())
    print("[specializes to B134 on the metallic locus a_i=b_i]", specializes_to_metallic())
    print("\n[SnapPy three-way: pair-criterion == anti-palindromic == is_amphicheiral]")
    s = snappy_threeway()
    if s is None:
        print("    SnapPy absent -- the lemma + GHH 2008 give the theorem.")
    else:
        for ps, pc, ap, amph, ok in s["rows"]:
            print(f"    {str(ps):26} crit={pc!s:5} anti-pal={ap!s:5} amphi={amph!s:5} {'OK' if ok else 'XX'}")
        print("    all agree:", s["all_agree"])
    print("\nTHEOREM (proved): bundle amphichiral <=> block-pair seq fixed (up to rotation) by reverse+component-swap.")
    print("Generalizes B134 (metallic a_i=b_i = cyclic palindrome) to all LR words. MATH tier.")


if __name__ == "__main__":
    main()
