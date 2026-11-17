"""B1957: agy-002's gate 5 (mixing and the lepton-down split in the closed-fibre triple overlap), recomputed by main on
main's closed form (cim_closed.py, itself checked against main's quadrature).  Data-free.
The seat's objects, read in its card and its script's text (not run): the Wilson-line difference of a sector at a point w is
xi = Delta w / 2 with Delta = q_L - q_R; 'pure 6Y' is Delta = +5 (up), -1 (down), -9 (lepton); '3(B - L)' is +2, +2, -6;
both together +1 (down) and -15 (lepton).  A Yukawa matrix is Y_ijk contracted with a Higgs vector:
the single mode e_0, or v_6(tau) = the six modes evaluated at the origin."""
import sys, pathlib, itertools, functools
from fractions import Fraction as Fr
from math import gcd
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import cim_closed as CC, cim_overlap as C
prim = lambda N: [(Fr(a, N), Fr(b, N)) for a in range(N) for b in range(N) if gcd(gcd(a, b), N) == 1]
pt = lambda tau, a, b: float(a) * tau + float(b)


def vtb(Yu, Yd):
    Uu = np.linalg.svd(Yu)[0]; Ud = np.linalg.svd(Yd)[0]; return abs(np.vdot(Uu[:, 0], Ud[:, 0]))


def v6(tau): return C.psi(6, 0.0, 0.0, np.array([0j]), tau, 0.0)[:, 0]


if __name__ == "__main__":
    # A: no poles at the points of order 3
    tr = 2j * 3 ** 0.5; mn = min(np.linalg.norm(CC.Y(tr, 2.5 * pt(tr, a, b))) for a, b in prim(3))
    cont = max(np.abs(CC.Y(tr, 2.5 * (pt(tr, a, b) + 1e-6 * (1 + tr))) - CC.Y(tr, 2.5 * pt(tr, a, b))).max() for a, b in prim(3))
    print("A: at the eight points of order 3 (tau = 2 sqrt(3) i, Delta = 5): least norm %.3f, change under a step of 1e-6: %.1e; the tensor is a theta function of xi, entire: no pole anywhere" % (mn, cont))
    # B: hypercharge alone, the single Higgs mode e_0, height 8
    tc = 0.13 + 8j
    def classify(Yu, Yd):
        """basis-free: the rows of a monomial matrix carry its singular values; the top row of the down matrix against the top row(s) of the up matrix"""
        ru = np.abs(Yu).max(axis=1); rd = np.abs(Yd).max(axis=1); top_u = [i for i in range(3) if ru[i] > ru.max() * (1 - 1e-9)]; top_d = [i for i in range(3) if rd[i] > rd.max() * (1 - 1e-9)]
        if len(top_u) > 1 or len(top_d) > 1: return "degenerate, inside" if set(top_d) <= set(top_u) or set(top_u) <= set(top_d) else "degenerate, outside"
        return "aligned" if top_u == top_d else "orthogonal"
    for lab, lift in (("representatives in the unit cell (the seat's)", (0, 0)), ("the lift a + 1", (1, 0)), ("the lift b + 1", (0, 1)), ("the lift (a + 1, b + 1)", (1, 1))):
        cnt = {}
        for a, b in prim(5):
            w = pt(tc, a + lift[0], b + lift[1]); c = classify(CC.Y(tc, 2.5 * w)[:, :, 0], CC.Y(tc, -0.5 * w)[:, :, 0]); cnt[c] = cnt.get(c, 0) + 1
        print("B: hypercharge alone, mode e_0, tau = 0.13 + 8i, the 24 points of order 5, %s: %s" % (lab, ", ".join("%s %d" % kv for kv in sorted(cnt.items()))))
    print("   (the seat's 4 aligned and 20 deranged come from a singular-value routine's choice inside the up matrix's degenerate pair; its second computation reports the degeneracy)")
    for lab, lift in (("representatives in the unit cell", (0, 0)), ("the lift a + 1", (1, 0))):
        vs = []
        for a, b in prim(5):
            w = pt(tc, a + lift[0], b + lift[1]); v = v6(tc); vs.append(vtb(np.einsum("ijk,k->ij", CC.Y(tc, 2.5 * w), v), np.einsum("ijk,k->ij", CC.Y(tc, -0.5 * w), v)))
        print("B: the same with the Higgs vector v_6(tau) (each matrix then has rank one, so only the top direction exists), %s: |V_tb| > 0.99 at %d of 24, < 0.01 at %d, largest %.3f" % (lab, sum(x > 0.99 for x in vs), sum(x < 0.01 for x in vs), max(vs)))
    w1 = pt(tc, Fr(1, 5), Fr(2, 5)); print("B: planted (the seat's PF5.1): the up matrix on mode e_2 and the down matrix on e_0 at one point under 3(B - L): |V_tb| = %.1e" % vtb(CC.Y(tc, w1)[:, :, 2], CC.Y(tc, w1)[:, :, 0]))
    Yu = CC.Y(tc, 2.5 * pt(tc, Fr(1, 5), Fr(2, 5)))
    print("   with one Higgs mode every Yukawa matrix has one entry in each row and column (cim_closed.py), so the mixing matrix is a permutation: |V_tb| is 0 or 1 and no angle is small")
    same = max(np.abs(CC.Y(tc, 2.5 * pt(tc, a, b)) - CC.Y(tc, 2.5 * pt(tc, a2, b2))).max() for (a, b), (a2, b2) in itertools.product(prim(5)[:6], prim(5)[6:12]) if (5 * a) % 2 == (5 * a2) % 2 and (5 * b) % 2 == (5 * b2) % 2)
    print("   the up sector: Delta = 5, so xi = 5 w / 2 is a half-lattice point for every w of order 5: |Y_u| is the same tensor at all points whose (5a, 5b) agree mod 2, up to phases: %.1e in |.|" % max(np.abs(np.abs(CC.Y(tc, 2.5 * pt(tc, a, b))) - np.abs(CC.Y(tc, 2.5 * pt(tc, a2, b2)))).max() for (a, b), (a2, b2) in itertools.product(prim(5), prim(5)) if (5 * a) % 2 == (5 * a2) % 2 and (5 * b) % 2 == (5 * b2) % 2))
    s = np.linalg.svd(CC.Y(tc, 2.5 * pt(tc, Fr(2, 5), Fr(1, 5)))[:, :, 0], compute_uv=False); print("   and at even 5a its two largest singular values are equal: %.3e, %.3e, %.3e" % tuple(s))
    # C: the 288 'aligned' points
    print("C: under 3(B - L) the up and the down sector have the same Delta = 2, so the seat's two matrices are one matrix (its script evaluates the same expression twice): |V_tb| = 1 at every point, every modulus, for any tensor whatever")
    # D: periodicity and the lepton-down split with e_0
    tp = 0.23 + 1.5j; xp = 0.2 * tp + 0.4; sv = lambda t, x: np.linalg.svd(CC.Y(t, x)[:, :, 0], compute_uv=False)
    print("D: singular values of the e_0 matrix under xi + 1/3 and xi + tau/3: unchanged to %.1e, %.1e; also under xi + 1/6: %.1e; under xi + tau/4 they change by %.2f, under xi + tau/6 by %.2f" % (
        np.abs(sv(tp, xp + 1 / 3) - sv(tp, xp)).max(), np.abs(sv(tp, xp + tp / 3) - sv(tp, xp)).max(), np.abs(sv(tp, xp + 1 / 6) - sv(tp, xp)).max(), np.abs(sv(tp, xp + tp / 4) - sv(tp, xp)).max(), np.abs(sv(tp, xp + tp / 6) - sv(tp, xp)).max()))
    for yy in (4, 8):
        t4 = 0.13 + yy * 1j; w = pt(t4, Fr(1, 5), Fr(2, 5)); sd, sl = sv(t4, w), sv(t4, -3 * w)
        print("   3(B - L) at w = (1/5, 2/5), height %d: s3/s1 down over lepton = %.1f (the seat: > 28 at height 4, > 800 at height 8)" % (yy, (sd[2] / sd[0]) / (sl[2] / sl[0])))
    t4 = 0.13 + 4j; r = lambda x: (lambda s: s[2] / s[0])(sv(t4, x))
    for N in (5, 10, 15):
        P = prim(N); d = {}
        for lab, (dd, dl) in (("hypercharge alone", (-0.5, -4.5)), ("3(B - L) alone", (1, -3)), ("both", (0.5, -7.5))):
            d[lab] = max(abs(x - y) for x, y in zip(sorted(r(dd * pt(t4, a, b)) for a, b in P), sorted(r(dl * pt(t4, a, b)) for a, b in P)))
        print("   order %2d, the multiset of s3/s1 over the orbit, down against lepton: hypercharge alone %.1e, 3(B - L) alone %.1e, both %.1e" % (N, d["hypercharge alone"], d["3(B - L) alone"], d["both"]))
    # E: the cocycle, the family Gramian with v_6, even and odd Delta
    tau = 0.23 + 1.5j; xi0 = 0.37 * tau + 0.41; Y0 = CC.Y(tau, xi0)
    print("E: Y(xi + 1) = exp(6 pi i alpha) Y(xi): %.1e; Y(xi + tau) = exp(-6 pi i beta) Y(xi): %.1e; the moduli |Y_ijk| under xi + 1/2: unchanged to %.1e; under xi + tau/2: changed by %.2f, and equal to the moduli with the Higgs modes k and k + 3 exchanged to %.1e" % (
        np.abs(CC.Y(tau, xi0 + 1) - np.exp(6j * np.pi * 0.37) * Y0).max(), np.abs(CC.Y(tau, xi0 + tau) - np.exp(-6j * np.pi * 0.41) * Y0).max(), np.abs(np.abs(CC.Y(tau, xi0 + 0.5)) - np.abs(Y0)).max(), np.abs(np.abs(CC.Y(tau, xi0 + tau / 2)) - np.abs(Y0)).max(), np.abs(np.abs(CC.Y(tau, xi0 + tau / 2)) - np.abs(np.roll(Y0, 3, axis=2))).max()))
    UT = C.transport(3, 0.5, 0.5, tau, 0.0, "T"); US = C.transport(3, 0.5, 0.5, tau, 0.0, "S")
    zdep = max(max(np.abs(C.transport(3, 0.5, 0.5, tau, z, "T") - UT).max(), np.abs(C.transport(3, 0.5, 0.5, tau, z, "S") - US).max()) for z in (0.2 * tau + 0.4, 0.4 * tau + 0.6, tau / 3 + 2 / 3))
    print("   the matter modes' transport under tau + 1 and -1/tau does not depend on the Wilson line: %.1e (it cannot: the modes are functions of z + zeta, and the transport is an integral over z)" % zdep)
    def gram(t, dq, lifts=((0, 0),)):
        v = v6(t); G = np.zeros((3, 3), complex)
        for a, b in prim(5):
            for m, n in lifts:
                Mx = np.einsum("ijk,k->ij", CC.Y(t, dq / 2 * pt(t, a + m, b + n)), v); G += Mx @ Mx.conj().T
        return G / (24 * len(lifts))
    rk = np.linalg.svd(np.einsum("ijk,k->ij", CC.Y(tau, pt(tau, Fr(1, 5), Fr(2, 5))), v6(tau)), compute_uv=False)
    print("   one matrix contracted with v_6(tau) has singular values %.3e, %.1e, %.1e: rank one (the six modes at a point reproduce the product of the two matter sections there)" % tuple(rk))
    ALL = ((0, 0), (1, 0), (0, 1), (1, 1))
    for dq in (2, -6, -1, 5, -9):
        G0 = gram(tau, dq); eT = np.abs(gram(tau + 1, dq) - UT @ G0 @ UT.conj().T).max(); eS = np.abs(gram(-1 / tau, dq) - US @ G0 @ US.conj().T).max(); ev = np.linalg.eigvalsh(G0)
        line = "   Delta = %+d: the Gramian over the 24 points with v_6: under tau + 1 %.1e, under -1/tau %.1e; eigenvalues %s" % (dq, eT, eS, np.round(ev, 4).tolist())
        if dq % 2:
            GL = gram(tau, dq, ALL); eT = np.abs(gram(tau + 1, dq, ALL) - UT @ GL @ UT.conj().T).max(); eS = np.abs(gram(-1 / tau, dq, ALL) - US @ GL @ US.conj().T).max()
            line += "; over the four lifts of each point: %.1e, %.1e; eigenvalues %s" % (eT, eS, np.round(np.linalg.eigvalsh(GL), 4).tolist())
        print(line)
    Gu = sum(np.einsum("ijk,ljk->il", CC.Y(tau, pt(tau, a, b)), CC.Y(tau, pt(tau, a, b)).conj()) for a, b in prim(5)) / 24; ev = np.linalg.eigvalsh(Gu)
    print("   traced over all six Higgs modes the Gramian is a multiple of the identity: spread of eigenvalues %.1e (B1727's collapse, and the same Parseval identity as in level6_higgs.py)" % (ev[2] - ev[0]))
    X3 = np.roll(np.eye(3), 1, axis=0); Z3 = np.diag(np.exp(2j * np.pi * np.arange(3) / 3)); G2 = gram(tau, 2)
    Gs = sum((np.linalg.matrix_power(X3, a) @ np.linalg.matrix_power(Z3, b)).conj().T @ G2 @ (np.linalg.matrix_power(X3, a) @ np.linalg.matrix_power(Z3, b)) for a in range(3) for b in range(3)) / 9
    print("   averaged over the nine clock-and-shift matrices it is a multiple of the identity: %.1e (Schur's lemma)" % np.ptp(np.linalg.eigvalsh(Gs)))
    lin = lambda t: (lambda sv_: sv_ / sv_[0])(np.linalg.svd(sum(np.einsum("ijk,k->ij", CC.Y(t, pt(t, a, b)), v6(t)) for a, b in prim(5)), compute_uv=False))
    print("   planted (the seat's PF5.5): the plain sum of the 24 contracted matrices: its singular-value ratios move by %.2f under tau + 1" % np.abs(lin(tau) - lin(tau + 1)).max())
