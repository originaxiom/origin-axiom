"""Round 5, part 2 of the independent check of B1431 (S26): does the 3D index, taken over ALL honest
boundary classes, separate m004 from m003?

Uses r12's validated implementation (all eight published figure-eight classes reproduce; pin-independent).
Honest classes only: p*mu + q*lambda with p, q integers -- no half-classes.  The comparison is between
SETS of series, so no identification of one boundary with the other is assumed.

The k-range is adaptive: `index` refuses to return unless every term on the boundary of its k-box has a
degree lower bound strictly above the order requested, so no contribution can be cut off by the box.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r12_3d_index_classes as T
import snappy


def safe_index(E, M, L, n, p, q2, D):
    K = 12
    while True:
        try:
            return T.index(E, M, L, n, p, q2, D, K=K)
        except AssertionError as err:
            if "k-range too small" not in str(err) or K > 200:
                raise
            K *= 2


def class_lower_bound(E, M, L, n, p, q2, Kmax=60):
    """min over the pinned k-line of the exact term lower bound -- a lower bound on deg I(class)"""
    base = [p * M[t] + (q2 * L[t]) // 2 for t in range(3 * n)]
    best = None
    for kk in range(-Kmax, Kmax + 1):
        k = [kk] + [0] * (n - 1)
        vec = [base[t] + k[0] * E[0][t] for t in range(3 * n)]
        lb = 2 * sum(k) + sum(T.J_lower(vec[3*j], vec[3*j+1], vec[3*j+2]) for j in range(n))
        best = lb if best is None else min(best, lb)
    return best


def main():
    D = 8          # through q^4; B1431 says its witnesses differ from every competitor already at q^1
    B = 10
    data = {}
    for name in ("m004", "m003"):
        E, M, L, n = T.rows(snappy.Manifold(name))
        tab = {}
        for p in range(-B, B + 1):
            for q in range(-B, B + 1):
                tab[(p, q)] = tuple(sorted(safe_index(E, M, L, n, p, 2 * q, D).items()))
        ring = [(p, q) for p in range(-B, B + 1) for q in range(-B, B + 1) if max(abs(p), abs(q)) == B]
        outer = [(p, q) for r in (B + 1, B + 2, B + 3)
                 for p in range(-r, r + 1) for q in range(-r, r + 1) if max(abs(p), abs(q)) == r]
        lb_ring = min(class_lower_bound(E, M, L, n, p, 2 * q) for p, q in ring)
        lb_out = min(class_lower_bound(E, M, L, n, p, 2 * q) for p, q in outer)
        data[name] = (tab, lb_ring, lb_out, (E, M, L, n))

    t4, lb4r, lb4o, _ = data["m004"]
    t3, lb3r, lb3o, _ = data["m003"]
    zero = tuple()
    S4, S3 = set(t4.values()) - {zero}, set(t3.values()) - {zero}
    print("=" * 78)
    print(f"honest classes |p|,|q| <= {B}: {(2*B+1)**2} per manifold;  series through q^{D//2}")
    print("=" * 78)
    print(f"   distinct non-zero series:  m004 {len(S4)}   m003 {len(S3)}")
    print(f"   occurring for m004 and at NO class of m003: {len(S4 - S3)}")
    print(f"   occurring for m003 and at NO class of m004: {len(S3 - S4)}")
    mu4, lam3 = t4[(1, 0)], t3[(0, 1)]
    print(f"   m004 meridian  I(mu)     = {T.ser(dict(mu4), D):<40s} present for m003: {mu4 in S3}")
    print(f"   m003 longitude I(lambda) = {T.ser(dict(lam3), D):<40s} present for m004: {lam3 in S4}")
    print(f"   trivial class equal (B1428): {t4[(0, 0)] == t3[(0, 0)]}")

    # does a witness differ from EVERY competitor already at q^1?  compare truncations through q^1
    def trunc1(s):
        return tuple((k, v) for k, v in s if k <= 2)
    c3 = {trunc1(s) for s in S3}
    c4 = {trunc1(s) for s in S4}
    print(f"   I_m004(mu) through q^1 matches some m003 class through q^1: {trunc1(mu4) in c3}")
    print(f"   I_m003(lambda) through q^1 matches some m004 class through q^1: {trunc1(lam3) in c4}")

    print()
    print("   COMPLETENESS.  A class whose index has degree > D cannot carry a series of degree <= D,")
    print("   so the comparison is complete if every class OUTSIDE the box has degree lower bound > D.")
    print(f"   smallest class lower bound on the ring |.| = {B}:           m004 {lb4r:>4}   m003 {lb3r:>4}")
    print(f"   smallest class lower bound on the rings {B+1}..{B+3}:       m004 {lb4o:>4}   m003 {lb3o:>4}")
    print(f"   (degree of the witnesses: 2 half-units = q^1; D = {D})")
    ok = lb4o > D and lb3o > D
    print(f"   rings beyond the box all exceed D: {ok}  -- growth is checked on three further rings,")
    print("   not proved for every class; B1431 states an exact bound, this check does not reach that.")


if __name__ == "__main__":
    main()
