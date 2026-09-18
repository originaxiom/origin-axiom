"""The DGG 3d index of m004 -- the one item in the 3d-3d lane the record itself concedes was
never computed.

The record's own caveat, quoted twice in `outside_bench/`:  *"the 3d index of T[m004] was NOT
computed."*  It is registered as speculation S026 in `speculations/PHYSICS_BRIDGE_MAP.md` with its
cost named ("quantum-dilogarithm machinery cost").  So this is not a gap anyone hid; it is a gap
priced and deferred.  It is also cheap enough to close, so it is closed here.

DEFINITIONS, from the primary sources, not paraphrased:

  Garoufalidis, "The 3D index of an ideal triangulation and angle structures" (arXiv:1208.1663),
  eq. (1.2) -- the TETRAHEDRON INDEX:

      I_D(m,e)(q) = sum_{n = max(0,-e)}^{oo}  (-1)^n q^{ n(n+1)/2 - (n + e/2) m } / ( (q)_n (q)_{n+e} )

      with (q)_n = prod_{i=1}^{n} (1 - q^i).

  Garoufalidis-Gu-Marino, "The descendants of the 3d-index" (arXiv:2301.00098), eq. (29) -- the
  figure-eight's state sum from its TWO-tetrahedron ideal triangulation:

      I^rot_{4_1}(n,n')(q) = sum_{k1,k2 in Z} q^{k2(n+n')/2}
                               I_D(k1, k1+k2) I_D(k1+k2-n+n', k1-n+n')

  At (n,n') = (0,0) the prefactor is 1 and, substituting a = k1, b = k1+k2 (a bijection of Z^2),

      I_{4_1}(0,0)(q) = sum_{a,b in Z} I_D(a,b) I_D(b,a).

  Convergence (same paper): for 1-efficient triangulations the degree of the summand is bounded
  below by a positive constant times max{|k1|,|k2|}, so the sum lies in Z((q^{1/2})).  That is what
  makes truncation legitimate, and it is checked here by raising the cutoff until the coefficients
  stop moving.

Series are carried exactly, as integer dictionaries in powers of q^{1/2}.  No floats anywhere.
"""
import sys

HALF = 2          # exponents are stored doubled, so q^{1/2} has stored exponent 1


def trunc(s, cap):
    return {k: v for k, v in s.items() if k <= cap and v}


def mul(s1, s2, cap):
    out = {}
    for k1, v1 in s1.items():
        if k1 > cap:
            continue
        for k2, v2 in s2.items():
            k = k1 + k2
            if k > cap:
                continue
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v}


def add_scaled(dst, src, shift, coeff, cap):
    for k, v in src.items():
        kk = k + shift
        if kk > cap:
            continue
        dst[kk] = dst.get(kk, 0) + coeff * v


_inv_poch_cache = {}


def inv_pochhammer(n, cap):
    """1/(q)_n = prod_{i=1}^n 1/(1-q^i), as a series in q (stored doubled)."""
    key = (n, cap)
    if key in _inv_poch_cache:
        return _inv_poch_cache[key]
    s = {0: 1}
    for i in range(1, n + 1):
        # multiply by 1/(1-q^i) = sum_{j>=0} q^{ij}
        geo = {}
        j = 0
        while j * i * HALF <= cap:
            geo[j * i * HALF] = 1
            j += 1
        s = mul(s, geo, cap)
    _inv_poch_cache[key] = s
    return s


def I_tet(m, e, cap):
    """Garoufalidis eq (1.2).  Returns a dict {2*exponent: coefficient}."""
    out = {}
    nmin = max(0, -e)
    vertex = (2 * m - 1) / 2.0        # exponent2(n) = n^2 + n(1-2m) - e*m is minimal here
    n = nmin
    while True:
        exp2 = n * (n + 1) - (2 * n + e) * m     # 2 * [ n(n+1)/2 - (n + e/2) m ]
        if n > vertex and exp2 > cap:
            break
        if exp2 <= cap:
            p = mul(inv_pochhammer(n, cap - exp2 if cap - exp2 >= 0 else 0),
                    inv_pochhammer(n + e, cap - exp2 if cap - exp2 >= 0 else 0),
                    cap - exp2 if cap - exp2 >= 0 else 0)
            add_scaled(out, p, exp2, (-1) ** n, cap)
        n += 1
        if n > nmin + 4000:
            raise RuntimeError("tetrahedron index sum did not terminate")
    return {k: v for k, v in out.items() if v}


def show(s, upto, label=""):
    """print as a q-series (only integer powers expected for the manifold index)"""
    terms = []
    for k in sorted(s):
        if k > upto:
            break
        c = s[k]
        if not c:
            continue
        if k == 0:
            terms.append(f"{c:+d}")
        elif k % 2 == 0:
            terms.append(f"{c:+d}q^{k // 2}" if k != 2 else f"{c:+d}q")
        else:
            terms.append(f"{c:+d}q^({k}/2)")
    return (label + " ".join(terms)) if terms else (label + "0")


def main():
    CAP = 24                     # keep coefficients through q^12
    print("=" * 78)
    print("(1) THE TETRAHEDRON INDEX, and its published triality")
    print("=" * 78)
    print("   I_D(0,0) =", show(I_tet(0, 0, CAP), 16))
    print("   I_D(1,0) =", show(I_tet(1, 0, CAP), 16))
    print("   I_D(0,1) =", show(I_tet(0, 1, CAP), 16))
    print()
    print("   CONTROL -- the S3 triality of the tetrahedron's three edge parameters.")
    print("   The bare cyclic form I_D(m,e) = I_D(-m-e,m) is FALSE; it holds up to a unit, and")
    print("   the unit was read off this implementation's own output and then tested globally:")
    print("        I_D(m,e) = (-q^{1/2})^m  I_D(-m-e, m)")
    print("   The three prefactor exponents around the cycle are m, -m-e, e, summing to 0 --")
    print("   so the relation closes, which a wrong unit would not.")
    ok, tested = True, 0
    for m in range(-3, 4):
        for e in range(-3, 4):
            a = trunc(I_tet(m, e, CAP), CAP - 8)
            b = I_tet(-m - e, m, CAP)
            sgn = -1 if (m % 2) else 1            # (-q^{1/2})^m = (-1)^m q^{m/2}
            shifted = {}
            add_scaled(shifted, b, m, sgn, CAP)
            shifted = trunc(shifted, CAP - 8)
            tested += 1
            if a != shifted:
                ok = False
                print(f"      FAILS at (m,e) = ({m},{e})")
    print(f"      holds on all {tested} pairs with |m|,|e| <= 3 : {ok}")
    if not ok:
        print("      -> implementation is WRONG; not proceeding to the manifold index")
        return

    print()
    print("=" * 78)
    print("(2) THE 3d INDEX OF m004 -- I_{4_1}(0,0) = sum_{a,b in Z} I_D(a,b) I_D(b,a)")
    print("=" * 78)
    prev = None
    for Rr in (4, 6, 8, 10, 12):
        tot = {}
        for a in range(-Rr, Rr + 1):
            Ia = {}
            for b in range(-Rr, Rr + 1):
                t = mul(I_tet(a, b, CAP), I_tet(b, a, CAP), CAP)
                for k, v in t.items():
                    tot[k] = tot.get(k, 0) + v
        tot = {k: v for k, v in tot.items() if v}
        stable = "" if prev is None else ("  (stable through q^8: %s)" %
                                          (trunc(prev, 16) == trunc(tot, 16)))
        print(f"   |a|,|b| <= {Rr:>2} : {show(tot, 16)}{stable}")
        prev = tot

    print()
    print("   PUBLISHED COMPARISON -- and getting the right target mattered.")
    print("   There are TWO published figure-eight series and they are different objects:")
    print("     * the UN-rotated DGG 3d-index      I_T(0) = 1 - 2q - 3q^2 + 2q^3 + 8q^4 + 18q^5")
    print("                                                 + 18q^6 + 14q^7 - 12q^8 - 52q^9 ...")
    print("     * the ROTATED index matrix's (0,0) entry, which is what eq (29) computes:")
    print("       Garoufalidis-Gu-Marino 2301.00098 section 4.3 prints")
    print("         1 - 8q - 9q^2 + 18q^3 + 46q^4 + 90q^5 + 62q^6 + 10q^7 + ...")
    print("   Checking against the second, since that is the formula implemented:")
    target = {0: 1, 2: -8, 4: -9, 6: 18, 8: 46, 10: 90, 12: 62, 14: 10}
    got = trunc(prev, 14)
    match = all(got.get(k, 0) == v for k, v in target.items())
    print(f"   MATCHES the published series through q^8 : {match}")
    if not match:
        print("   differences (published vs computed):")
        for k in sorted(set(target) | set(got)):
            if k <= 16 and target.get(k, 0) != got.get(k, 0):
                print(f"      q^{k//2}: published {target.get(k,0):+d}  computed {got.get(k,0):+d}")

    print()
    print("=" * 78)
    print("(3) WHAT IT IS AND WHAT IT IS NOT")
    print("=" * 78)
    print("   The 3d index is an element of Z((q^{1/2})) -- a q-SERIES, not an integer.  DGG")
    print("   1112.5179 defines it as Tr_{H_m} (-1)^F q^{R/2 + j3} z^e: a weighted count of BPS")
    print("   states of the 3d N=2 theory T[M] on S^2, per magnetic flux m and electric charge e.")
    print("   The programme's index is I = n(V) - n(V*) = t0 - r1: an INTEGER, the difference of")
    print("   two twisted-cohomology dimensions on M itself.")
    print("   These are not rival computations of one quantity.  A nonzero 3d index does not")
    print("   supply a generation count, and does not bear on I = 0.")


if __name__ == "__main__":
    main()
