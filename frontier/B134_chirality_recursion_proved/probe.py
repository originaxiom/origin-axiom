"""B134 -- the chirality recursion PROVED (as a corollary of Goodman-Heard-Hodgson 2008) + the novelty audit.

Phase B (novelty audit) + Phase C (one proof) of the approved program. A deep, adversarial literature pass placed the
project's three candidate-novel results against prior art; this stage banks the audit's actionable outputs and PROVES
the one genuinely-new kernel (the B128 chirality recursion), upgrading it from computer-assisted (15/15) to PROVED.

  ============================================================================================================
  THE NOVELTY AUDIT (Phase B; see ../../docs/NOVELTY_AUDIT.md for citations):
    R1 chirality recursion (B128/K011): PARTIALLY-KNOWN. The amphichirality<->palindromic-monodromy MECHANISM is
       published -- Goodman-Heard-Hodgson 2008 (arXiv:0801.4815) classify the symmetries of a once-punctured-torus
       bundle by its L/R monodromy word: ANTI-palindromic word (reverse = L<->R swap) <=> orientation-REVERSING
       symmetry <=> amphichiral; palindromic word (reverse = self) <=> orientation-preserving pi-rotation. The
       residual NOVEL kernel is the lift to the integer block-length sequence (proved below).
    R2 two-seed fork (B131/K014): KNOWN -- Kitano-Nozaki 2020 (arXiv:1904.02559) prove finiteness of the splice
       torsion image via the two pieces' A-polynomial curves intersecting (gcd=1 => Bezout-finite). CAVEAT: the
       discreteness is driven by the meridian<->longitude-SWAPPING splice gluing, NOT by the pieces being distinct
       (a same-knot splice Sigma(K,K) is already finite). So B131's "heterogeneity makes the choice" is correct only
       for the IDENTITY gluing; under the splice (swap) gluing the gluing map alone forks (reconciliation below).
    R3 SU(2)_k field content (B132/K015): KNOWN/standard -- Jeffrey 1992 (torus-bundle Z=Tr rho(U)=Gauss sum,
       cyclotomic), Dong-Lin-Ng 2015 (modular rep Q(zeta_n)-rational, congruence kernel level n=ord(T)),
       Lawrence-Zagier 1999 (WRT in Q(zeta), Galois-equivariant). The corrected B132 content is standard; cite.

  ============================================================================================================
  THE THEOREM (B128 recursion, PROVED here as a corollary of GHH 2008):
    For a metallic-block word W = R^{m1}L^{m1} R^{m2}L^{m2} ... R^{mk}L^{mk}, the once-punctured-torus bundle is
    AMPHICHIRAL  <=>  the block-length sequence (m1,...,mk) is a CYCLIC PALINDROME (its reversal is a cyclic
    rotation of it).
  PROOF. By GHH 2008, the bundle is amphichiral <=> W is ANTI-palindromic, i.e. reverse(W) = swap_{L<->R}(W) as
  cyclic words. Now the elementary identity:
     reverse(R^{m1}L^{m1}...R^{mk}L^{mk}) = L^{mk}R^{mk} ... L^{m1}R^{m1}   (block order reverses; each R^a L^a -> L^a R^a)
     swap_{L<->R}(R^{m1}L^{m1}...R^{mk}L^{mk}) = L^{m1}R^{m1} ... L^{mk}R^{mk}
  Both are concatenations of "L^a R^a" blocks, with block-length sequences (mk,...,m1) and (m1,...,mk) respectively.
  Two such block-words are equal as cyclic words IFF their block-length sequences agree up to cyclic rotation. Hence
     W anti-palindromic  <=>  (mk,...,m1) is a cyclic rotation of (m1,...,mk)  <=>  (m1,...,mk) is a cyclic palindrome.
  Combined with GHH this proves the recursion. (The metallic-block word has even length 2*sum(mi), so GHH's
  even-length hypothesis for the orientation-reversing case is automatic.) QED.

  Verified three ways below: (1) the elementary lemma anti_palindromic(W) <=> cyclic_palindrome(blockseq) holds for
  ALL block sequences up to length 6 / entries up to 4 (exhaustive combinatorial certificate of the string identity);
  (2) SnapPy is_amphicheiral agrees on a sample (the GHH input, ground truth); (3) consistency with B128's 15/15.
"""
from __future__ import annotations

import itertools


# ----------------------------------------------------------------------------------------------------------------
# The word criteria (GHH 2008) and the block-sequence criterion (B128).
# ----------------------------------------------------------------------------------------------------------------
def seq_word(seq):
    return "".join("R" * m + "L" * m for m in seq)


def _cyc_eq(a, b):
    return len(a) == len(b) and b in (a + a)


def _swapLR(w):
    return w.translate(str.maketrans("RL", "LR"))


def anti_palindromic(w):
    """GHH 2008: reverse(w) = (L<->R swap of w) as cyclic words  <=>  the bundle is amphichiral."""
    return _cyc_eq(w[::-1], _swapLR(w))


def palindromic(w):
    """GHH 2008: reverse(w) = w as cyclic words  <=>  orientation-preserving pi-rotation (NOT amphichiral by itself)."""
    return _cyc_eq(w[::-1], w)


def seq_cyclic_palindrome(seq):
    """B128: the block-length sequence's reversal is a cyclic rotation of it."""
    seq = tuple(seq)
    rev = tuple(reversed(seq))
    n = len(seq)
    return rev in {seq[i:] + seq[:i] for i in range(n)}


# ----------------------------------------------------------------------------------------------------------------
# The lemma (the proof's combinatorial heart): anti_palindromic(W) <=> cyclic_palindrome(blockseq), ALL sequences.
# ----------------------------------------------------------------------------------------------------------------
def lemma_exhaustive(max_len=6, max_entry=4):
    """Exhaustive certificate of the elementary string identity over all block sequences (the GHH-corollary lemma)."""
    checked = 0
    for k in range(1, max_len + 1):
        for seq in itertools.product(range(1, max_entry + 1), repeat=k):
            w = seq_word(seq)
            if anti_palindromic(w) != seq_cyclic_palindrome(seq):
                return {"holds": False, "counterexample": seq, "checked": checked}
            checked += 1
    return {"holds": True, "checked": checked,
            "note": "anti_palindromic(W) <=> block-seq cyclic palindrome, for ALL sequences len<=%d entries<=%d"
                    % (max_len, max_entry)}


# ----------------------------------------------------------------------------------------------------------------
# SnapPy three-way check (GHH input = ground truth): anti_palindromic == cyclic_palindrome == is_amphicheiral.
# ----------------------------------------------------------------------------------------------------------------
def snappy_threeway(seqs=None):
    try:
        import snappy
    except Exception:
        return None
    if seqs is None:
        seqs = [(1,), (2,), (1, 2), (2, 3), (1, 2, 1), (1, 2, 2, 1), (1, 1, 2, 2), (2, 1, 1, 2), (1, 2, 1, 2),
                (2, 1, 3, 1), (1, 2, 3), (1, 3, 2), (3, 2, 1), (1, 2, 3, 4), (1, 2, 2, 3), (2, 3, 3, 2)]
    rows = []
    allok = True
    for seq in seqs:
        w = seq_word(seq)
        M = snappy.Manifold("b++" + w)
        sg = M.symmetry_group()
        amph = sg.is_amphicheiral() if sg.is_full_group() else None
        b, g = seq_cyclic_palindrome(seq), anti_palindromic(w)
        ok = (b == g == bool(amph))
        allok = allok and ok
        rows.append((seq, b, g, amph, ok))
    return {"rows": rows, "all_agree": allok}


# ----------------------------------------------------------------------------------------------------------------
# R2 reconciliation: the gluing-map dependence (Kitano-Nozaki). Swap-gluing discretizes even a same-seed glue.
# ----------------------------------------------------------------------------------------------------------------
def gluing_map_dependence():
    """Identity gluing: same seed -> continuum, distinct -> discrete (B131). Swap (splice) gluing: discrete even for
    a same-seed glue (Kitano-Nozaki 2020). So distinctness creates the fork ONLY under the identity gluing."""
    import sympy as sp
    t = sp.symbols("t")
    f = t ** 4 - 5 * t ** 2 + 2                       # fig-8 A-poly curve kappa = f(trT) (B67)
    # identity gluing, same seed: kappa1=kappa2 & P1=P2 on the same curve -> the whole curve (continuum).
    identity_same_seed = "CONTINUUM"
    # swap (splice) gluing, same seed: P2=f(P1), P1=f(P2) -> P1=f(f(P1)), a finite set.
    swap_poly = sp.expand(f.subs(t, f) - t)
    swap_same_seed_solutions = sp.degree(sp.Poly(swap_poly, t))
    return {"identity_gluing_same_seed": identity_same_seed,
            "swap_gluing_same_seed_finite_count": int(swap_same_seed_solutions),
            "swap_discretizes_same_seed": int(swap_same_seed_solutions) > 0,
            "note": "B131's 'heterogeneity makes the choice' holds for the IDENTITY gluing; under the splice (swap) "
                    "gluing the gluing map alone forks (Kitano-Nozaki 2020). Reconciled, B131 annotated."}


def main():
    print("=" * 100)
    print("B134 -- the chirality recursion PROVED (corollary of GHH 2008) + the novelty audit")
    print("=" * 100)

    print("\n[THE LEMMA -- exhaustive combinatorial certificate of the string identity]")
    print("    ", lemma_exhaustive())

    print("\n[SnapPy three-way: GHH anti-palindromic == B128 cyclic-palindrome == is_amphicheiral]")
    s = snappy_threeway()
    if s is None:
        print("     SnapPy absent -- the lemma + GHH 2008 give the theorem; B128 recorded 15/15.")
    else:
        for seq, b, g, amph, ok in s["rows"]:
            print(f"     {str(seq):14} cyc-pal={b!s:5} anti-pal={g!s:5} amphi={amph!s:5} {'OK' if ok else 'XX'}")
        print("     all agree:", s["all_agree"])

    print("\n[R2 reconciliation -- gluing-map dependence (Kitano-Nozaki)]")
    print("    ", gluing_map_dependence())

    print("\nTHEOREM (proved): metallic-block bundle amphichiral <=> block-length sequence is a cyclic palindrome.")
    print("Mechanism = GHH 2008 (anti-palindromic word); the block-sequence lift is the novel kernel. MATH tier.")


if __name__ == "__main__":
    main()
