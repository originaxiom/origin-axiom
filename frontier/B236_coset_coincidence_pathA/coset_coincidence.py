"""B236 -- Path A CLOSED (the H21 gate): the ordinary/super coset coincidence at SU(2)_3, with the
literature references found (chat1) and verified here by central charges. Nothing to CLAIMS.md.

The question (Path A / H21, the gate on the paper's originality claim): is the coset-coincidence
MECHANISM -- that the ordinary GKO minimal-model coset and the N=1 super GKO coset are literally the SAME
coset, uniquely at SU(2)_3 = the TCI -- stated in the literature, or is the framing ours?

References (chat1, 2026-06-27):
  ordinary  M(m,m+1) = (SU(2)_{m-2} x SU(2)_1)/SU(2)_{m-1}        [Goddard-Kent-Olive 1986]
  super     SM_k     = (SU(2)_k    x SU(2)_2)/SU(2)_{k+2}          [Lashkevich, hep-th/9301093, eq.3]
  uniqueness: "TCI is the unique model both conformal & superconformal" [Qiu 1986, via Johnson-Clifford
              hep-th/0311129]. The MECHANISM (same coset at SU(2)_3) is NOT stated as a proposition
              [absence-of-evidence, chat1's lit search] -> our framing is the modest original observation.

VERIFIED HERE (verify-don't-trust, central charges via Verlinde c=sum 3k_i/(k_i+2) - 3K/(K+2)):
  - ordinary M(m,m+1) coset c == 1-6/(m(m+1));  super SM_k coset c == (3/2)(1-8/((k+2)(k+4)));
  - the coincidence: ordinary M(4,5) and super SM_1 are LITERALLY the same coset (SU(2)_1 x SU(2)_2)/SU(2)_3,
    both c=7/10;
  - UNIQUENESS: sweeping (ordinary m, super k), the ONLY pair sharing the same coset DATA (numerator
    level-multiset + denominator) is (m=4, k=1) = the TCI.
  - BONUS: the TCI ALSO equals the coset (E_7)_1 (+) (E_7)_1 / (E_7)_2 (c=7/10) [hep-th/0301229] -- so E_7
    appears in the TCI ITSELF as a coset algebra, even though E_7=2O is EXCLUDED from the object's McKay /
    congruence structure (B210/B234). A different ROLE for E_7 (coset algebra vs McKay group); it does not
    contradict the exclusion, and is a genuine nuance for the paper's E_7 discussion.

Firewall: dimensionless CFT coset data / central charges; nothing to CLAIMS.md. Run: python
coset_coincidence.py (pyenv).
"""
from fractions import Fraction as Fr


def c_su2(k):
    """WZW central charge c(SU(2)_k) = 3k/(k+2)."""
    return Fr(3 * k, k + 2)


def c_grp(dim, hdual, k):
    return Fr(k * dim, k + hdual)


def c_ordinary(m):
    """ordinary GKO M(m,m+1) = (SU(2)_{m-2} x SU(2)_1)/SU(2)_{m-1}."""
    return c_su2(m - 2) + c_su2(1) - c_su2(m - 1)


def c_super(k):
    """super (Lashkevich) SM_k = (SU(2)_k x SU(2)_2)/SU(2)_{k+2};  p=k+2."""
    return c_su2(k) + c_su2(2) - c_su2(k + 2)


def ordinary_coset_data(m):
    """(numerator level-multiset, denominator level) of the ordinary coset."""
    return tuple(sorted([m - 2, 1])), m - 1


def super_coset_data(k):
    return tuple(sorted([k, 2])), k + 2


def coincidences(mmax=60):
    """all (ordinary m, super k) whose coset DATA (num multiset + denom) literally coincide."""
    out = []
    for m in range(3, mmax + 1):
        od = ordinary_coset_data(m)
        for k in range(1, mmax + 1):
            if super_coset_data(k) == od:
                out.append((m, k, c_ordinary(m)))
    return out


def c_e7_tci_coset():
    """TCI as (E_7)_1 (+) (E_7)_1 / (E_7)_2 : 2*c((E7)_1) - c((E7)_2)."""
    return 2 * c_grp(133, 18, 1) - c_grp(133, 18, 2)


if __name__ == "__main__":
    print("B236 -- Path A: the ordinary/super coset coincidence at SU(2)_3 (H21 gate)\n")

    print("(1) coset central charges match their minimal-model formulas:")
    for m in range(3, 7):
        cf = Fr(1) - Fr(6, m * (m + 1))
        print(f"    ordinary M({m},{m+1}): coset c={c_ordinary(m)}  formula {cf}  ok={c_ordinary(m)==cf}")
        assert c_ordinary(m) == cf
    for k in range(1, 5):
        cf = Fr(3, 2) * (Fr(1) - Fr(8, (k + 2) * (k + 4)))
        print(f"    super SM_{k} (p={k+2}): coset c={c_super(k)}  formula {cf}  ok={c_super(k)==cf}")
        assert c_super(k) == cf

    print("\n(2) THE COINCIDENCE -- ordinary M(4,5) and super SM_1 are the SAME coset:")
    print(f"    ordinary M(4,5): data {ordinary_coset_data(4)} (num multiset, denom), c={c_ordinary(4)}")
    print(f"    super    SM_1  : data {super_coset_data(1)} (num multiset, denom), c={c_super(1)}")
    assert ordinary_coset_data(4) == super_coset_data(1) == ((1, 2), 3)
    assert c_ordinary(4) == c_super(1) == Fr(7, 10)
    print("    => LITERALLY the same coset (SU(2)_1 x SU(2)_2)/SU(2)_3, c=7/10.")

    print("\n(3) UNIQUENESS -- the only (ordinary m, super k) sharing the same coset data:")
    co = coincidences(60)
    print(f"    {co}")
    assert co == [(4, 1, Fr(7, 10))]
    print("    => unique at the TCI. (Mechanism for B228's coincidence; references GKO/Lashkevich/Qiu.)")

    print("\n(4) BONUS -- E_7 appears in the TCI itself as a coset algebra:")
    ce7 = c_e7_tci_coset()
    print(f"    (E_7)_1 (+) (E_7)_1 / (E_7)_2 : c = {ce7}  (=7/10? {ce7 == Fr(7,10)})")
    assert ce7 == Fr(7, 10)
    print("    => E_7 has a *coset-algebra* role in the TCI, distinct from the McKay/congruence role where")
    print("       E_7=2O is EXCLUDED (B210/B234). No contradiction; a nuance for the paper's E_7 discussion.")

    print("\nPath A CLOSED: mechanism verified, references found; the 'mechanism-unstated' is chat1's lit")
    print("absence-of-evidence -> our coset-coincidence framing is the modest original observation. H21 gate cleared.")
    print("\nALL CHECKS PASS")
