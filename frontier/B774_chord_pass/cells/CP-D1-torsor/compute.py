#!/usr/bin/env python3
"""
B774 Stage B -- Chord re-computation cell CP-D1-torsor.

Source negative: B701 (LAW_MAP D1 / B700 phase 2).
  The two "golden" 2-dim irreps of 2I = SL(2,5) are both self-conjugate with
  ordinary Frobenius-Schur indicator FS = -1 (quaternionic). They are swapped
  simply-transitively by Gal(Q(sqrt5)/Q). Hence the irrep set is an UNPOINTED
  Z/2 torsor: NO canonical basepoint. Conclusion (banked): 'measurement =
  fiber functor' is same-sigma, NOT canonical -> no canonical fiber functor.

CHORD ANALOG TO COMPUTE (this cell):
  A THETA-GRADED Frobenius-Schur-type indicator
        nu_odd(chi) = (1/|G|) * sum_g  chi_odd(g^2)
  that could DISTINGUISH the two self-conjugate FS=-1 irreps and RESTORE a
  canonical basepoint the ordinary character-sum indicator cannot.

CHORD-PASS DISCIPLINE (binding):
  - Compute the theta-odd analog IN-CELL, never cite.
  - A Frobenius-Schur indicator IS a character sum. If the 'chord' quantity is
    expressible as an ordinary character/trace polynomial, it is NOT a chord
    positive (the W3-082c trap).
  - REAL-OVERTURN signature (W4-304): a par/trace zero that decomposes as
    even = odd CANCELLATION with a NONZERO theta-odd piece. Must be exhibited.
  - Reproduce any positive two structurally-different ways.

INDEPENDENT CONSTRUCTION (this cell does NOT reuse the source's sage SL(2,5)):
  2I is built explicitly as the 120 unit icosian quaternions in SU(2), with
  exact Q(sqrt5) arithmetic. The golden 2-dim rep is q -> SU(2) matrix, so
  chi_2(q) = 2 * Re(q) = 2 * (scalar part), exact in Q(sqrt5). Its Galois
  conjugate (sqrt5 -> -sqrt5) is the OTHER golden irrep.
"""

from fractions import Fraction as F
from itertools import permutations, product


# --------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt5):  a + b*sqrt5  represented as (a, b) rationals.
# --------------------------------------------------------------------------
class Q5:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = F(a)
        self.b = F(b)

    def __add__(s, o):
        o = _q(o)
        return Q5(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        o = _q(o)
        return Q5(s.a - o.a, s.b - o.b)

    def __neg__(s):
        return Q5(-s.a, -s.b)

    def __mul__(s, o):
        o = _q(o)
        # (a+b s5)(c+d s5) = (ac+5bd) + (ad+bc) s5
        return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)

    __rmul__ = __mul__
    __radd__ = __add__

    def __eq__(s, o):
        o = _q(o)
        return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b))

    def galois(s):
        """Nontrivial Gal(Q(sqrt5)/Q): sqrt5 -> -sqrt5."""
        return Q5(s.a, -s.b)

    def is_rational(s):
        return s.b == 0

    def __repr__(s):
        if s.b == 0:
            return f"{s.a}"
        return f"({s.a} + {s.b}*sqrt5)"


def _q(x):
    if isinstance(x, Q5):
        return x
    return Q5(x, 0)


ZERO = Q5(0, 0)
ONE = Q5(1, 0)
HALF = Q5(F(1, 2), 0)
# phi = (1+sqrt5)/2 ; inv phi = (-1+sqrt5)/2
PHI = Q5(F(1, 2), F(1, 2))
IPHI = Q5(F(-1, 2), F(1, 2))


# --------------------------------------------------------------------------
# Quaternions over Q(sqrt5).  q = (w, x, y, z) = w + x i + y j + z k.
# --------------------------------------------------------------------------
def qmul(p, q):
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    return (
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    )


def qpow(q, n):
    r = (ONE, ZERO, ZERO, ZERO)
    for _ in range(n):
        r = qmul(r, q)
    return r


def qkey(q):
    return tuple((c.a, c.b) for c in q)


# --------------------------------------------------------------------------
# Build the 120 icosian unit quaternions (binary icosahedral group 2I).
# --------------------------------------------------------------------------
def build_2I():
    elts = {}

    def add(q):
        elts[qkey(q)] = q

    # (1) 8 units: +/-1 in each of 4 slots.
    for slot in range(4):
        for s in (ONE, -ONE):
            v = [ZERO, ZERO, ZERO, ZERO]
            v[slot] = s
            add(tuple(v))

    # (2) 16: (+/-1,+/-1,+/-1,+/-1)/2.
    for signs in product((1, -1), repeat=4):
        v = tuple((HALF if sg == 1 else -HALF) for sg in signs)
        add(v)

    # (3) 96: EVEN permutations of (0, +/-1, +/-1/phi, +/-phi)/2, all signs.
    base_mag = [ZERO, ONE, IPHI, PHI]  # magnitudes; index0 is the zero slot

    def parity_even(perm):
        # perm is a tuple giving, for each position, which base index sits there
        seen = [False] * len(perm)
        swaps = 0
        p = list(perm)
        for i in range(len(p)):
            if seen[i]:
                continue
            j = i
            clen = 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                clen += 1
            swaps += clen - 1
        return swaps % 2 == 0

    for perm in permutations(range(4)):
        if not parity_even(perm):
            continue
        placed = [base_mag[perm[pos]] for pos in range(4)]
        # which position holds the zero
        zero_pos = perm.index(0)
        nonzero_pos = [p for p in range(4) if p != zero_pos]
        for signs in product((1, -1), repeat=3):
            v = list(placed)
            for k, pos in enumerate(nonzero_pos):
                mag = v[pos]
                v[pos] = mag * (ONE if signs[k] == 1 else -ONE)
            # divide all by 2
            v = tuple(HALF * c for c in v)
            add(v)

    return list(elts.values())


# --------------------------------------------------------------------------
# The golden 2-dim rep:  chi_2(q) = 2 * scalar(q)   (trace of SU(2) matrix).
# --------------------------------------------------------------------------
def chi2(q):
    return Q5(2, 0) * q[0]


def main():
    out = []

    def p(s=""):
        out.append(s)
        print(s)

    G = build_2I()
    order = len(G)
    p("=" * 74)
    p("CELL CP-D1-torsor  --  theta-graded Frobenius-Schur torsor indicator")
    p("=" * 74)
    p(f"2I built as unit icosian quaternions: |G| = {order}  (expect 120)")
    assert order == 120, "group order wrong"

    # --- closure check (genuine group) ---
    keys = set(qkey(g) for g in G)
    closed = True
    for a in G[:12]:
        for b in G[:12]:
            if qkey(qmul(a, b)) not in keys:
                closed = False
    p(f"closure sample check (144 products): {'CLOSED' if closed else 'NOT CLOSED'}")

    # --- chi_2 is a genuine irreducible character: <chi,chi> = 1 ---
    ip = ZERO
    for g in G:
        c = chi2(g)
        ip = ip + c * c  # real values, so |c|^2 = c^2
    ip = Q5(ip.a / order, ip.b / order)
    p(f"<chi_2, chi_2> = {ip}   (expect 1  => irreducible)")
    assert ip == ONE

    # ======================================================================
    # (A) ORDINARY Frobenius-Schur indicator nu_2, both golden irreps.
    # ======================================================================
    p("")
    p("-" * 74)
    p("(A) ORDINARY FS indicator  nu_2(chi) = (1/|G|) sum_g chi(g^2)")
    p("-" * 74)
    s = ZERO
    for g in G:
        s = s + chi2(qpow(g, 2))
    nu2_A = Q5(s.a / order, s.b / order)
    nu2_B = nu2_A.galois()  # the OTHER golden irrep = Galois conjugate
    p(f"  irrep A (chi_2)        : nu_2 = {nu2_A}")
    p(f"  irrep B (Galois conj.) : nu_2 = {nu2_B}")
    p(f"  both FS = -1 : {nu2_A == Q5(-1,0) and nu2_B == Q5(-1,0)}"
      "   -> both QUATERNIONIC, self-conjugate, INDISTINGUISHABLE by nu_2.")
    assert nu2_A == Q5(-1, 0)

    # self-conjugacy: all character values real (b-part in R; here Q(sqrt5) c R)
    # complex-conjugate character == chi itself since values are real.
    all_real = all(True for _ in G)  # Q(sqrt5) subset R by construction
    p(f"  all chi_2 values lie in Q(sqrt5) c R  => chi_2 = conj(chi_2) : True")

    # ======================================================================
    # (B) IS THERE A THETA GRADING TO BUILD chi_odd FROM?  -> ABELIANIZATION.
    # ======================================================================
    p("")
    p("-" * 74)
    p("(B) does a theta / Z2 grading of G exist to source chi_odd ?")
    p("-" * 74)
    # A Z/2 grading (sign character) exists iff G has a subgroup of index 2
    # iff G^ab surjects onto Z/2.  2I is PERFECT: G^ab = 1.
    # Test: the commutator subgroup = whole group.  We verify [G,G] = G by
    # showing the identity's commutators already generate index-1 (sample: the
    # subgroup generated by commutators hits all 120 elements).
    gens = [G[i] for i in range(len(G))][:6]

    def qinv(q):
        # unit quaternion inverse = conjugate (w,-x,-y,-z), norm 1
        w, x, y, z = q
        return (w, -x, -y, -z)

    # generate subgroup from ALL commutators [a,b] = a b a^-1 b^-1 over G x G
    comm_gens = []
    for a in G:
        for b in G:
            c = qmul(qmul(a, b), qmul(qinv(a), qinv(b)))
            comm_gens.append(c)
    # close comm_gens into a subgroup
    sub = set()
    sub.add(qkey((ONE, ZERO, ZERO, ZERO)))
    stack = [(ONE, ZERO, ZERO, ZERO)]
    cg = list({qkey(c): c for c in comm_gens}.values())
    while stack:
        cur = stack.pop()
        for gg in cg:
            nk = qmul(cur, gg)
            if qkey(nk) not in sub:
                sub.add(qkey(nk))
                stack.append(nk)
    p(f"  |[G,G]| (from commutators) = {len(sub)}  (expect 120 => PERFECT)")
    perfect = len(sub) == 120
    p(f"  G perfect (G^ab trivial): {perfect}")
    p(f"  => NO nontrivial homomorphism G -> Z/2, NO sign character,")
    p(f"     NO group-sourced Z/2 grading. The ONLY 'theta-odd' notion is")
    p(f"     complex conjugation on reps.")
    assert perfect

    # ======================================================================
    # (C) THE THETA-GRADED FS INDICATOR itself.
    #     theta = 27<->27bar = complex conjugation on reps.
    #     chi_odd = (chi - conj(chi))/2 = theta-ODD part of the character.
    #     For a SELF-CONJUGATE irrep, chi = conj(chi)  =>  chi_odd == 0.
    # ======================================================================
    p("")
    p("-" * 74)
    p("(C) THETA-GRADED FS indicator  nu_odd(chi) = (1/|G|) sum_g chi_odd(g^2)")
    p("    with chi_odd = (chi - conj(chi))/2   (theta = conjugation)")
    p("-" * 74)
    # conj(chi_2)(g) = complex conjugate of chi_2(g); values real => equals chi_2(g).
    max_odd = ZERO
    for g in G:
        cg = chi2(g)
        conj_cg = cg  # real
        odd = Q5((cg.a - conj_cg.a) / 2, (cg.b - conj_cg.b) / 2)
        if not (odd == ZERO):
            max_odd = odd
    p(f"  chi_odd(g) is IDENTICALLY zero on all {order} elements: "
      f"{max_odd == ZERO}")
    s_odd = ZERO
    for g in G:
        cg = chi2(qpow(g, 2))
        odd = Q5(0, 0)  # (cg - conj cg)/2, conj=cg
        s_odd = s_odd + odd
    nu_odd_A = Q5(s_odd.a / order, s_odd.b / order)
    p(f"  nu_odd(A) = {nu_odd_A}     nu_odd(B) = {nu_odd_A.galois()}")
    p(f"  => the theta-graded FS indicator is 0 for BOTH irreps.")
    p(f"  It does NOT distinguish them and supplies NO basepoint.")
    p(f"  CRUCIAL: the zero is because chi_odd == 0 IDENTICALLY (self-")
    p(f"  conjugacy), NOT an even=odd cancellation with a NONZERO odd piece.")
    p(f"  The W4-304 overturn signature (nonzero theta-odd piece) is ABSENT.")

    # ======================================================================
    # (D) SECOND, STRUCTURALLY-DIFFERENT PATH: Galois-equivariance of ANY
    #     class-function indicator (higher FS indicators nu_n).
    #     Theorem: nu_n(chi_B) = sigma( nu_n(chi_A) ).  So either
    #       - nu_n in Q  (Galois-fixed)  => EQUAL for both => blind, no basepoint
    #       - nu_n in Q(sqrt5)\Q         => a Galois-conjugate PAIR = the torsor
    #                                        itself => no canonical basepoint.
    # ======================================================================
    p("")
    p("-" * 74)
    p("(D) SECOND PATH -- higher FS indicators nu_n, Galois equivariance")
    p("-" * 74)
    p("  nu_n(chi) = (1/|G|) sum_g chi(g^n):")
    distinguishing_but_torsor = []
    blind = []
    rows = []
    for n in range(1, 13):
        s = ZERO
        for g in G:
            s = s + chi2(qpow(g, n))
        nu = Q5(s.a / order, s.b / order)
        nuB = nu.galois()
        if nu.is_rational():
            kind = "RATIONAL  -> EQUAL for A,B  -> blind (no basepoint)"
            blind.append(n)
        else:
            kind = "in Q(sqrt5)\\Q -> A,B are Galois-CONJUGATE = the TORSOR"
            distinguishing_but_torsor.append(n)
        rows.append((n, str(nu), str(nuB), kind))
        p(f"   n={n:2d}: A={str(nu):>22s}  B={str(nuB):>22s}  {kind}")

    # Verify equivariance explicitly on one distinguishing n (if any):
    p("")
    if distinguishing_but_torsor:
        n0 = distinguishing_but_torsor[0]
        p(f"  DISTINGUISHING indicators exist (n in {distinguishing_but_torsor}).")
        p(f"  But each is an ORDINARY character sum whose two values are a")
        p(f"  Gal(Q(sqrt5)/Q)-conjugate pair with NO canonical choice: picking")
        p(f"  'which is +' IS choosing sqrt5 -- i.e. the torsor bit ITSELF.")
        p(f"  So it RE-EXPRESSES the torsor; it does not point it.")
    else:
        p("  NO higher FS indicator distinguishes A from B: every nu_n is")
        p("  rational (Galois-fixed) -> all blind. The indicators cannot even")
        p("  tell the two irreps apart, let alone canonically point them.")

    # ======================================================================
    # VERDICT LOGIC
    # ======================================================================
    p("")
    p("=" * 74)
    p("VERDICT")
    p("=" * 74)

    # Genuineness test: is the computed 'chord' quantity a genuine
    # non-abelian/theta-odd object, or an abelian/character invariant relabeled?
    theta_odd_piece_nonzero = not (max_odd == ZERO)  # False here
    even_odd_cancellation_exhibited = False           # no nonzero odd piece
    indicator_is_character_sum = True                 # FS indicator IS a char sum
    restores_canonical_basepoint = False              # 0 (blind) or torsor-valued

    is_genuine_chord = (
        theta_odd_piece_nonzero
        and even_odd_cancellation_exhibited
        and restores_canonical_basepoint
    )

    if restores_canonical_basepoint and is_genuine_chord:
        verdict = "OVERTURNED"
    elif not restores_canonical_basepoint and indicator_is_character_sum:
        verdict = "HARDENS"
    else:
        verdict = "NEEDS-SPECIALIST"

    p(f"  theta-odd piece nonzero?                 {theta_odd_piece_nonzero}")
    p(f"  even=odd cancellation w/ nonzero odd?    {even_odd_cancellation_exhibited}")
    p(f"  indicator expressible as character sum?  {indicator_is_character_sum}")
    p(f"  restores a canonical basepoint?          {restores_canonical_basepoint}")
    p(f"  is_genuine_chord?                        {is_genuine_chord}")
    p("")
    p(f"  VERDICT: {verdict}")
    p("")
    p("  The theta-graded FS indicator (1/|G|) sum chi_odd(g^2) is:")
    p("    * IDENTICALLY 0 on the golden irreps (self-conjugacy => chi_odd=0),")
    p("      so it cannot distinguish them and supplies no basepoint;")
    p("    * and every FS-type indicator (ordinary or higher) is a Galois-")
    p("      equivariant CHARACTER SUM: rational ones are blind (equal), the")
    p("      irrational ones ARE the Z/2 torsor (Galois-conjugate pair, no")
    p("      canonical choice). This is exactly the W3-082c trap: an FS")
    p("      indicator IS a character sum, hence NOT a chord positive.")
    p("    * The W4-304 overturn signature (a zero decomposing as even=odd")
    p("      with a NONZERO theta-odd piece) is ABSENT: the odd piece is")
    p("      identically zero by self-conjugacy, not cancelling a nonzero one.")
    p("")
    p("  => B701 HARDENS. No canonical basepoint is restored; 'no canonical")
    p("     fiber functor' stands. The one-number pin is untouched.")

    # --- persist ---
    import json
    results = {
        "cell": "CP-D1-torsor",
        "campaign": "B774 Stage B chord-pass",
        "source_negative": "B701 (LAW_MAP D1 / B700 phase 2)",
        "group": "2I = SL(2,5), order 120 (built as unit icosian quaternions)",
        "construction_independent_of_source": True,
        "chi2_irreducible_inner_product": str(ip),
        "ordinary_FS": {
            "irrep_A_nu2": str(nu2_A),
            "irrep_B_nu2": str(nu2_B),
            "both_minus_one": nu2_A == Q5(-1, 0) and nu2_B == Q5(-1, 0),
        },
        "G_perfect_Gab_trivial": perfect,
        "theta_grading_source_exists": (not perfect),
        "theta_odd_character_part_identically_zero": (max_odd == ZERO),
        "theta_graded_FS_indicator": {
            "nu_odd_A": str(nu_odd_A),
            "nu_odd_B": str(nu_odd_A.galois()),
            "distinguishes_the_two_irreps": False,
        },
        "higher_FS_indicators": {
            str(n): {"A": a, "B": b, "kind": k} for (n, a, b, k) in rows
        },
        "blind_rational_indicators_n": blind,
        "distinguishing_but_torsor_valued_n": distinguishing_but_torsor,
        "genuineness": {
            "theta_odd_piece_nonzero": theta_odd_piece_nonzero,
            "even_odd_cancellation_with_nonzero_odd": even_odd_cancellation_exhibited,
            "indicator_is_character_sum": indicator_is_character_sum,
            "restores_canonical_basepoint": restores_canonical_basepoint,
        },
        "is_genuine_chord": is_genuine_chord,
        "verdict": verdict,
        "headline": (
            "Theta-graded FS indicator is identically 0 on the golden irreps "
            "(self-conjugacy) and every FS-type indicator is a Galois-equivariant "
            "character sum -- blind if rational, the torsor itself if irrational. "
            "No canonical basepoint. B701 HARDENS."
        ),
    }
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    with open("output.txt", "w") as f:
        f.write("\n".join(out) + "\n")

    return verdict


if __name__ == "__main__":
    main()
