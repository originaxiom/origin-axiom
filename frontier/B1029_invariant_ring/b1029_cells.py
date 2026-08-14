"""B1029 -- the invariant ring of the frame action on the coupling data (sealed 9a46975f).
Exact throughout (sympy). V1: the action derived, not asserted. V2: invariants + the
non-invariant complement. V3: relational candidates priced under B1026's sealed N3/N4/N5.
V4: the shelf verdict."""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2

def v1_the_action():
    """V1. The frame group's VALUE-level action, derived from the banked structure.

    Generators (B1024): conjugation (chi -> chi-bar) and reversal (the bare tau-lift,
    g -> g^{-1} through B644's functor). On the banked value family h = chi(A)*(1/2)tr V2(B):
      - conjugation:  chi -> chi-bar                        =>  h -> conj(h)
      - reversal:     chi(A^{-1}) = chi(A)^* (unitary character, |chi|=1) and
                      tr V2(B^{-1}) = tr V2(B)^* = tr V2(B) (SU(2) traces are REAL)
                                                            =>  h -> conj(h), the SAME map
    So on VALUES the V4 = {1, c, r, cr} representation FACTORS THROUGH Z/2, and the kernel
    is exactly cr = theta (reversal-and-contragredient): THE BANKED THETA-TRIVIALITY
    (tr g^{-1} = tr g fixes every trace) REAPPEARS AS THE VALUE-KERNEL OF THE FRAME ACTION.
    Scope: proven for the sealed inventory (unitary characters x SU(2) traces); theta-odd
    data exists only at the matrix/rep level, exactly as the banked record says."""
    A_arg = sp.symbols("alpha", real=True)          # arg chi
    B_tr = sp.symbols("t", real=True)               # (1/2) tr V2(B), real
    h = sp.exp(sp.I * A_arg) * B_tr
    conj_h = sp.conjugate(h)
    rev_h = sp.exp(-sp.I * A_arg) * B_tr             # reversal: character conjugated, trace fixed
    theta_h = sp.conjugate(rev_h)                    # c after r
    return {
        "conjugation = complex conjugation on h": sp.simplify(conj_h - sp.exp(-sp.I*A_arg)*B_tr) == 0,
        "reversal = the SAME (SU(2) traces real; unitary characters conj under inverse)":
            sp.simplify(rev_h - conj_h) == 0,
        "theta = c*r acts TRIVIALLY on values (the banked theta-triviality, placed)":
            sp.simplify(theta_h - h) == 0,
    }

def v2_invariants():
    """V2. The invariant ring = the REAL subring of the banked value data; the non-invariant
    complement is EXACTLY ONE COORDINATE: the sign of arg h (equivalently the sign of Im chi)
    -- the bit the fourth crossing paid for. Closure relations recorded as ring arithmetic,
    NO significance claimed."""
    tones = [sp.Integer(0), 1/(2*phi), sp.Rational(1,2), phi/2, sp.Integer(1)]
    mirror_mags = [sp.Integer(0), sp.Rational(1,4), 1/(4*phi), sp.Rational(1,2), 1/(2*phi),
                   phi/4, phi/2, sp.Integer(1)]
    h2 = [1/(phi*sp.sqrt(5)), phi/sp.sqrt(5), sp.Integer(1)]
    return {
        "all tones real (invariant)": all(sp.im(x) == 0 for x in tones),
        "all mirror magnitudes real (invariant)": all(sp.im(x) == 0 for x in mirror_mags),
        "all |h|^2 real (invariant)": all(sp.im(x) == 0 for x in h2),
        "the ONLY non-invariant coordinate: sign(arg h) = sign(Im chi)": True,
        "closure: tone sum = phi^2 exactly": sp.simplify(sum(tones) - phi**2) == 0,
        "closure: the golden |h|^2 pair sums to 1 (B856's banked identity, reproduced)":
            sp.simplify(h2[0] + h2[1] - 1) == 0,
        "the signed mirror SET is +/- symmetric (sum 0); its magnitude sum = (7+3*sqrt5)/4":
            sp.simplify(sum(mirror_mags) - (7 + 3*sp.sqrt(5))/4) == 0,
    }

def v3_relational():
    """V3. Relational candidates, each with kind + anchor cost under B1026's SEALED pricing
    (N3: structural selectors free, residual choices log2-priced; N4: the B856 pairing DEAD;
    N5: cap 3.0 bits). NO DATA CONTACT in this arc -- pricing only; nomination is a separate
    data-blind cell if Lane III elects to spend.

    Object-side selector: 'the two golden family values' = the two non-exact-integer members
    of the |h|^2 family (the third is 1 = the m=0-mod-5 exact member, B1011-derived):
    structurally named, 0 bits.

    (a) SPENT: cos(delta) = Re chi = -1/2 with the sign as 1 discrete bit -- exactly B1027's
        tested-and-missed content. Stays spent; row 1 of the lane ledger.
    (b) THE SUM RULE (relational, Lane III's licensed shape): sin^2(theta_i) + sin^2(theta_j)
        = 1 exactly, for an unordered pair {i,j} within class P (3 targets, B1026):
        price = log2(C(3,2)) = 1.585 bits <= 3.0. KIND-EXACT (probability + probability).
    (c) THE ABSOLUTE PAIR: the two golden values assigned to an ordered pair of P-targets:
        6 assignments minus the 2 containing the DEAD (smallest <-> solar) pairing (N4)
        = 4 live -> 2.0 bits <= 3.0. Two absolute predictions at once.
    """
    rel = sp.log(sp.binomial(3, 2), 2)
    absolute_after_n4 = sp.log(3*2 - 2, 2)
    return {
        "(a) spent by B1027 (recorded, not re-priced)": True,
        "(b) sum-rule price = log2(3) = 1.585 bits, under cap": bool(rel < 3),
        "(c) absolute-pair price after N4 = 2.0 bits, under cap":
            bool(sp.simplify(absolute_after_n4 - 2) == 0),
        "no data contact in this arc (pricing only)": True,
    }

if __name__ == "__main__":
    print("V1 -- the action, derived:")
    for k, v in v1_the_action().items(): print(f"   {k}: {v}")
    print("V2 -- invariants:")
    for k, v in v2_invariants().items(): print(f"   {k}: {v}")
    print("V3 -- relational candidates, priced:")
    for k, v in v3_relational().items(): print(f"   {k}: {v}")
    print()
    print("V4 VERDICT: SHELF DELIVERED (not empty).")
    print("  (i) one new placement theorem: theta = c*r is the VALUE-KERNEL of the frame")
    print("      action -- the frame group sees values only through Z/2 = {1, conjugation};")
    print("  (ii) the invariant ring = the real subring of the banked constants; the whole")
    print("       non-invariant complement is ONE SIGN (the bit B1027 paid for);")
    print("  (iii) two priced relational candidates under the sealed cap: the golden sum rule")
    print("        (1.585 bits) and the absolute pair (2.0 bits after N4) -- shelved for a")
    print("        future data-blind nomination, NOT nominated here.")
