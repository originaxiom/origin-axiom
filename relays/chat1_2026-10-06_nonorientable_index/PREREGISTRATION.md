# PREREGISTRATION — the class index on m000's non-orientable levels (web seat, 2026-10-06). Sealed BEFORE computing.
## Definitions (B1297 §1, with the orientation made explicit)
For a cusped 3-manifold X with cusp group P and a local system V over F_p:
  a_k = h^k(X;V), t_k = h^k(P;V), r1 = rank(H^1(X;V) -> H^1(P;V)),  n(V) := a_1 - r_1   (orientation-free).
Orientable X:      I(V)   := n(V) - n(V*)                (B1297).
Non-orientable N:  I_w(V) := n(V) - n(V* (x) w)          (w = the orientation character; Lefschetz duality pairs V with V*(x)w).
Objects: N = m000 (its orientation cover is m004) and N = N3, m000's 3-fold cyclic cover (non-orientable, H1 = Z/2+Z/2+Z;
its orientation cover is M3, m004's 3-fold level). w from the O(3,1) holonomy: m000 (1,1); N3 (0,1,1). Cusp of N: the Klein
bottle <m, x | m x m^-1 x> with m orientation-reversing (m000: m = a; N3: m = bAcb), found by search and checked on the
holonomy. Cusp of M = ker w (Reidemeister-Schreier): the torus <x, y = m^2>.
Field F_13. Test systems V on N: every character of H1(N) into F_13^x, and every reducible non-split 2-dim extension
[[chi1, c],[0, chi2]] of two such characters (c a cocycle not a coboundary), all of them.
## Predictions
L1a (twisted half-lives-half-dies, from duality on (N, Klein bottle), boundary orientation character = w|cusp):
    r1(V) + r1(V*(x)w) = t1(V) for EVERY test V on both N. KILL: any failure.
L1b (the untwisted partner is the wrong one): r1(V) + r1(V*) = t1(V) FAILS for at least one test V. If it never fails on this
    test set, the distinction is reported as unwitnessed here (not a kill of L1a).
L2 (the register lemma; Shapiro for the pair, (p*V)* = p*(V*)):
    I(M; p*V) = I_w(N; V) + I_w(N; V(x)w) for EVERY test V, both N. KILL: any failure.
Controls: Euler characteristics a0 - a1 + a2 = 0 on N and M, t0 - t1 + t2 = 0 on the cusps; on M the orientable annihilator
r1(V) + r1(V*) = t1(V) (B1297's own check) for every pulled-back V.
L3 (reported, not predicted): which test V have I_w(N;V) != 0, and whether any pulled-back count I(M; p*V) is non-zero.
## Scope
frame F-CI (B1297's index), extended to non-orientable spaces by the definition above; object m000, N3, m004, M3; reach single;
hypotheses: F_13 coefficients, the test families named. Not a chirality statement on N: chirality is not definable there.
