"""B1024 -- L153's computation (sealed dc823e86). Exact, from banked characters.

The class map (B936, Q_A_module): a sign character chi in X = T_ad[2] = (Z/2)^6 has
H^1 class (chi at node 1, chi at node 3) -- the two tau-fixed Bourbaki nodes.
A STRUCTURE H(sigma_chi o tau) has torsor coordinate chi.chi+ (B936 Q_A_torsor),
so its class is the class of chi.chi+.
"""
CHI_P = (1, -1, 1, -1, 1, 1)      # B907, banked (chi+)
CHI_M = tuple(-x for x in CHI_P)  # chi-
ALL_MINUS = (-1,) * 6
CHI_C = (1, -1, -1, 1, -1, 1)     # B907 inner sweep: the compact-flip = sigma_c (conjugation)
ALL_ONES = (1,) * 6

def cls(chi):
    """H^1 class of an INNER sign automorphism sigma_chi."""
    return (0 if chi[1] == 1 else 1, 0 if chi[3] == 1 else 1)

def cls_structure(chi):
    """H^1 class of the STRUCTURE H(sigma_chi o tau): coordinate chi.chi+."""
    coord = tuple(a * b for a, b in zip(chi, CHI_P))
    return cls(coord)

def main():
    print("-- consistency checks against banked B936/B939 --")
    print(f"  chi- (wall, -> D2):     class {cls(CHI_M)}   [B936 says D2 is a COBOUNDARY -> must be (0,0)]")
    assert cls(CHI_M) == (0, 0)
    print(f"  all-minus (-> D):       class {cls(ALL_MINUS)}   [B936: D carries the nonzero class]")
    assert cls(ALL_MINUS) != (0, 0)
    print()
    print("-- the two torsor generators' shadows --")
    c_conj = cls(CHI_C)
    print(f"  CONJUGATION  sigma_c (CHI_C = {CHI_C}): class {c_conj}")
    # REVERSAL: constructed from the banked chain. Word reversal |-> inverse word (the
    # object's anti-automorphism); through B644's group functor the stage sees g |-> g^-1;
    # on the 27 the induced structure-map is the CONTRAGREDIENT = the bare tau-lift
    # (chi = ALL_ONES: no sign dressing -- any dressing would be an unforced choice with
    # no banked source). Its structure-class is the class of the coordinate chi.chi+ = chi+.
    c_rev_bare = cls_structure(ALL_ONES)
    print(f"  REVERSAL     bare tau-lift (chi = 1): structure class {c_rev_bare}")
    # sensitivity: the phi+ dressing (chi = CHI_P) -- the one banked dressed lift that
    # acts diagonally -- would give:
    c_rev_phip = cls_structure(CHI_P)
    print(f"  (sensitivity: phi+ dressing would give {c_rev_phip})")
    print()
    span = {(0, 0), c_conj, c_rev_bare,
            tuple((a + b) % 2 for a, b in zip(c_conj, c_rev_bare))}
    print(f"-- generation test (primary construction) --")
    print(f"  span{{conj, rev}} = {sorted(span)}  -> "
          f"{'FULL H^1: SAME (d = 2)' if len(span) == 4 else 'proper subgroup'}")
    print()
    print("-- the unconditional half --")
    print(f"  conjugation's class {c_conj} is NONZERO under the BANKED character CHI_C:")
    print(f"  INDEPENDENT (d = 4) is REFUTED regardless of the reversal convention; d <= 3.")
    return c_conj, c_rev_bare, len(span) == 4

if __name__ == "__main__":
    main()
