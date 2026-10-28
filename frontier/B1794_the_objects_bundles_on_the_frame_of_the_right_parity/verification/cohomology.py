"""P-401 (data-free): the rational cohomology of L250's frame X = Gamma\\PSL(2,C) for the object m004 and its closed fillings.
M is an orientable 3-manifold, hence parallelisable, so its orthonormal frame bundle is X = M x SO(3); rationally SO(3) ~ S^3
(Betti numbers 1, 0, 0, 1).  Kunneth then gives X's rational Betti numbers from M's.  For a closed M, Poincare duality; for the
cusped m004 (interior of a compact manifold with torus boundary), Poincare-Lefschetz: H^k_c(X) ~ H_{6-k}(X).
Prints every number it reports.  No measured value.
    python3 -B cohomology.py"""
import snappy

S3 = [1, 0, 0, 1]                                   # rational Betti numbers of SO(3) (= those of S^3)


def betti_M(N):
    """rational Betti numbers b0..b3 of N (closed or one-cusped), from H_1 via snappy and duality"""
    H1 = N.homology()
    b1 = sum(1 for c in H1.elementary_divisors() if c == 0)
    if N.num_cusps() == 0 or all(not N.cusp_info(i)["filling"] == (0.0, 0.0) for i in range(N.num_cusps())):
        pass
    closed = all(N.cusp_info(i)["filling"] != (0.0, 0.0) for i in range(N.num_cusps()))
    if closed:
        return [1, b1, b1, 1], H1                    # Poincare duality, orientable closed
    # one-cusped, interior of a compact M with torus boundary: b2 = b1 - 1 (half lives, half dies: chi(M) = 0)
    return [1, b1, b1 - 1, 0], H1


def kunneth(bM):
    out = [0] * 7
    for i, a in enumerate(bM):
        for j, b in enumerate(S3):
            out[i + j] += a * b
    return out


if __name__ == "__main__":
    M = snappy.Manifold("m004")
    bM, H1 = betti_M(M)
    bX = kunneth(bM)
    print("m004 (cusped): H_1 =", H1, "| rational Betti of M:", bM, "| chi(M) =", sum((-1) ** k * b for k, b in enumerate(bM)))
    print("  X = M x SO(3), rational Betti b0..b6:", bX)
    bXc = [bX[6 - k] for k in range(7)]             # compactly supported: H^k_c(X) ~ H_{6-k}(X) (Poincare-Lefschetz)
    print("  compactly supported Betti (Poincare-Lefschetz) b^c_0..b^c_6:", bXc)
    print("  H^2(X;Q) =", bX[2], "(no absolute line-bundle class); H^2_c(X;Q) =", bXc[2], "(a relative class, trivial at the end);",
          "H^4(X;Q) =", bX[4], "; H^6_c(X;Q) =", bXc[6])
    print("  the pairing H^2_c x H^4 -> H^6_c = Q is Poincare-Lefschetz duality, perfect: ranks", bXc[2], "x", bX[4])
    print()
    print("closed fillings m004(p, q): homology, solution type, rational Betti of M and of X")
    rows = []
    for p, q in [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (-5, 1), (5, 2), (7, 2), (5, 3), (1, 2), (3, 2)]:
        N = snappy.Manifold("m004"); N.dehn_fill((p, q))
        try:
            st = N.solution_type()
        except Exception as ex:
            st = "error: %s" % ex
        hyp = st == "all tetrahedra positively oriented"      # a geometric solution; (1, 0) is S^3 and the exceptional slopes are not hyperbolic
        bN, H = betti_M(N)
        rows.append((p, q, str(H), st, hyp, bN, kunneth(bN)))
        print("  (%3d, %d) H_1 = %-8s %-42s hyperbolic=%-5s b(M) = %s  b(X) = %s" % (p, q, H, st[:42], hyp, bN, kunneth(bN)))
    hyp_b1 = [r for r in rows if r[4] and r[5][1] > 0]
    print()
    print("hyperbolic fillings with b1(M) > 0 among those listed:", len(hyp_b1))
    print("every listed hyperbolic filling has H^2(X;Q) = H^4(X;Q) = 0:", all(r[6][2] == 0 and r[6][4] == 0 for r in rows if r[4]))
    print("cohomology exit 0")
