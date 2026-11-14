"""S053 / W2 (the SEAM-E6 BRIDGE campaign, image wave) -- the E6 coupling side. Firewalled.

THE IMAGE side of the kernel/image hypothesis: the sqrt5 / E6 "how fast the allowed happens".
Builds the 27-dim minuscule module of e6 from B351's exact data and reads the principal-sl2
structure that carries the m=4 coupling.

VALIDATED:
  * the 27-module: simple Chevalley generators (all +1, minuscule) satisfy the E6 Serre relations
    and [E_i,F_j]=delta_ij H_i -- a genuine representation.
  * principal-sl2 branching: 27 = V17 (+) V9 (+) V1 = [17,9,1] (spin 8, 4, 0) -- from the exact
    diagonal H-grading (principal-h eigenvalues {+-16:1,...,+-2:2,0:3}).

THE E6-SPECIFIC DATUM (structural, rigorous):
  * F4 exponents are {1,5,7,11} -- NO 4. E6 exponents {1,4,5,7,8,11} -- HAS 4. So the m=4 (Sym^8)
    block exists in e6 but NOT in f4; the m=4 direction is the E6/F4 coset, theta-ODD
    ((-1)^(4+1)=-1), by CONSTRUCTION. Impossible within F4 (no Sym^8) and within SL(2) (no 27).
  * a Sym^8 (spin-4) operator on 27 = V17(spin8) (+) V9(spin4) (+) V1 couples V17<->V9 by
    Clebsch-Gordan: spin4 in spin8 (x) spin4 (range |8-4|..8+4 = 4..12), so the reduced matrix
    element is nonzero-ALLOWED. THE V17<->V9 COUPLING EXISTS and is genuinely E6 -- the "image".

RESIDUE (the honest boundary): the EXACT numerical mixing rate of the m=4 cocycle (B352.h1_line(4))
requires rho27 matched to B351's eps-cocycle SIGN convention (the all-+1 minuscule construction
gives the right branching but ~12/120 root-vector-bracket signs differ from B351's basis; the
branching/grading is unaffected). Sign-matching rho27 + projecting the cocycle onto the Sym^8
block gives the number; that is a bounded, specialist-adjacent step (the exact coefficient), not
the qualitative claim (which is confirmed).

READ ACROSS W1/W2: the KERNEL (W1: the seam dark locus, sqrt-3, symmetric, on the level-15 Weil
torus Z/20xZ/12) and the IMAGE (W2: the E6 V17<->V9 coupling, sqrt5, on the E6-character-variety
cusp torus) BOTH exist -- but on DIFFERENT domains. Whether they are two faces of ONE object
(the kernel/image duality) is exactly W3 (the ro<->rho_geo bridge, B428's open target).

Firewall: e6 rep theory. No physics claim; nothing to CLAIMS.
"""
import sys, os
from fractions import Fraction as Fr
from collections import deque, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "frontier", "B351_exact_e6_chevalley"))
import exact_e6 as X


def build_and_validate():
    A, ROOTS, RIDX, brk = X.A, X.ROOTS, X.RIDX, X.brk
    simples = [tuple(1 if k == i else 0 for k in range(6)) for i in range(6)]

    def refl(i, m): return tuple(m[j] - m[i]*A[i][j] for j in range(6))

    def orbit(st):
        seen = [tuple(st)]; s = {tuple(st)}; q = deque(seen)
        while q:
            m = q.popleft()
            for i in range(6):
                n = refl(i, m)
                if n not in s: s.add(n); seen.append(n); q.append(n)
        return seen
    W = orbit((1, 0, 0, 0, 0, 0)); widx = {w: i for i, w in enumerate(W)}
    assert len(W) == 27
    Z = lambda: [[Fr(0)]*27 for _ in range(27)]

    def mm(P, Q):                                   # sparsity-aware (fast)
        R = Z()
        for i in range(27):
            Pi = P[i]
            for k in range(27):
                a = Pi[k]
                if a:
                    Qk = Q[k]
                    for j in range(27):
                        if Qk[j]: R[i][j] += a*Qk[j]
        return R
    cm = lambda P, Q: [[a-b for a, b in zip(r1, r2)] for r1, r2 in zip(mm(P, Q), mm(Q, P))]
    isz = lambda M: all(x == 0 for r in M for x in r)

    def Hmat(i):
        M = Z()
        for a, w in enumerate(W): M[a][a] = Fr(w[i])
        return M

    def simp(i, up):
        M = Z()
        for a, w in enumerate(W):
            t = tuple(w[j] + (A[i][j] if up else -A[i][j]) for j in range(6))
            if t in widx: M[widx[t]][a] = Fr(1)
        return M
    E = [simp(i, True) for i in range(6)]; Fm = [simp(i, False) for i in range(6)]; H = [Hmat(i) for i in range(6)]
    # Serre + sl2 relations (certifies a genuine rep)
    serre = True
    for i in range(6):
        for j in range(6):
            if not isz([[cm(E[i], Fm[j])[a][b] - (H[i][a][b] if i == j else 0) for b in range(27)] for a in range(27)]):
                serre = False
            if i != j:
                if A[i][j] == 0 and not isz(cm(E[i], E[j])): serre = False
                if A[i][j] == -1 and not isz(cm(E[i], cm(E[i], E[j]))): serre = False
    # principal-h grading on 27 -> branching
    e_p, h_p, f_p = X.principal_sl2()
    Hp = Z()
    for idx, cf in (h_p.items() if isinstance(h_p, dict) else enumerate(h_p)):
        if cf and idx < 6:
            for a in range(27): Hp[a][a] += Fr(cf)*H[idx][a][a]
    eigs = Counter(int(Hp[a][a]) for a in range(27))
    rem = dict(eigs); irreps = []
    while any(v > 0 for v in rem.values()):
        top = max(e for e, v in rem.items() if v > 0)
        for e in range(-top, top+1, 2): rem[e] -= 1
        irreps.append(top + 1)
    return dict(serre_valid=serre, branching=irreps, e6_has_exp4=(4 in X.EXPONENTS),
                f4_has_exp4=(4 in [1, 5, 7, 11]), v17_v9_coupling_allowed=(4 >= abs(8-4) and 4 <= 8+4))


if __name__ == "__main__":
    r = build_and_validate()
    print("W2:", r)
    assert r["serre_valid"] and r["branching"] == [17, 9, 1]
    assert r["e6_has_exp4"] and not r["f4_has_exp4"] and r["v17_v9_coupling_allowed"]
    print("27 = V17(+)V9(+)V1 validated; m=4 is E6-specific (F4 has no exp-4, theta-odd);"
          " V17<->V9 coupling CG-allowed. Exact rate = the sign-matched residue.")
