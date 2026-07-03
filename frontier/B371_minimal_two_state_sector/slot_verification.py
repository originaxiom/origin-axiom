"""B371 -- the minimal two-state sector of the level-15 quantization: exact verification.

Origin: the owner's question "can we try to compute a photon?" -- answered NO at the physics
level (no gauge field, spacetime, mass, or coupling exists here; K020 governs), and translated
into the well-posed probe (pre-registered cross-session before computation): does the level-15
quantization contain a minimal TWO-state invariant sector whose states carry opposite unit
quarter-turn weights? This module is the in-repo independent verification (the relayed
computation is the second path; both exact, different engines).

Verified facts (all exact, Fraction arithmetic over Q(zeta60)):
  V1  the slot P = P_6 + P_14 (eigenprojectors of W_1 = theta-lift of R L) is invariant
      under the full Weil image (both generators D, WR).
  V2  metallic traces on the slot: tr rho(A_1) = tr rho(A_4) = (1-sqrt5)/2 = 1-phi exactly
      (a 108-degree rotation -- the pentagon angle, order 10); tr rho(A_2) = tr rho(A_3) = 1
      (60 degrees, order 6).
  V3  helicity pairing: tr rho(S_hat) = 0 with (P S_hat P)^2 = zeta60^18 P, i.e. eigenvalues
      exactly +-zeta60^9 -- opposite unit quarter-turn weights modulo a common center phase.
  V4  the dihedral mechanism: S_hat W_1 S_hat^{-1} = W_1^{-1} holds GLOBALLY (the quarter-turn
      element swaps the two states -- irreducibility follows from the two distinct eigenvalues).
  V5  the TRUE parity: J = S_hat^2 (S_hat = D^{-1} WR D^{-1}, the palindrome lift of
      S = R^{-1} L R^{-1}) is monomial with support j -> 1-j and commutes exactly with both
      generators. (The naive parities j -> -j and j -> 1-j-without-phases do NOT commute in
      this half-characteristic model -- the relayed probe's own honest first failure.)
  E3  the Weyl identity: J . Par = zeta6^{-1} . X . Z exactly (X = one-step translation,
      Z = clock). COROLLARY: the banked Par-inserted pair observable inserts, up to the
      block-parity sign and a fixed sixth root, the elementary Weyl operator XZ -- the seam
      is a parity-signed one-step hopping amplitude between spectral projectors.
  E5  (against the banked (1,2) table) the slot's seam cells are exactly
      {6,14} x {2,10} at values +-1/48: the seam couples the sector to itself at the rigid value.

FIREWALL: this is a "photon-shaped slot" only in the strict sense of state count and weight
pair. No physics noun is earned; any future number extracted from this sector faces the full
null-hypothesis gauntlet.
"""
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E                     # noqa: E402
import seam_certification as SC              # noqa: E402
from step0_exact_matrices import build_theta_W, matrix_order  # noqa: E402

N = 15
I15 = [[E.ONE if i == j else E.ZERO for j in range(N)] for i in range(N)]


def msub(A, B):
    return [[E.sub(A[i][j], B[i][j]) for j in range(N)] for i in range(N)]


def mzero(A):
    return all(A[i][j] == E.ZERO for i in range(N) for j in range(N))


def trace(A):
    t = E.ZERO
    for i in range(N):
        t = E.add(t, A[i][i])
    return t


def _gens():
    D = [[E.e15((j * (j - 1) // 2) % 15) if i == j else E.ZERO for j in range(N)] for i in range(N)]
    Di = [[E.e15((-(j * (j - 1) // 2)) % 15) if i == j else E.ZERO for j in range(N)] for i in range(N)]
    F = [[E.e15((i * j) % 15) for j in range(N)] for i in range(N)]
    Fi = [[E.scal(Fr(1, 15), E.e15((-i * j) % 15)) for j in range(N)] for i in range(N)]
    WR = E.mmul(E.mmul(F, Di), Fi)
    WRi = E.mmul(E.mmul(F, D), Fi)
    return D, Di, WR, WRi


def build_all():
    D, Di, WR, WRi = _gens()
    W1 = build_theta_W(1)
    o1, pow1 = matrix_order(W1)

    def proj(a):
        M = [[E.ZERO] * N for _ in range(N)]
        for j in range(o1):
            c = E.scal(Fr(1, o1), E.zeta((-3 * j * a) % 60))
            for i in range(N):
                for k in range(N):
                    if pow1[j][i][k] != E.ZERO:
                        M[i][k] = E.add(M[i][k], E.mul(c, pow1[j][i][k]))
        return M

    P = [[E.add(proj(6)[i][j], proj(14)[i][j]) for j in range(N)] for i in range(N)]
    Sh = E.mmul(E.mmul(Di, WR), Di)
    Shi = E.mmul(E.mmul(D, WRi), D)
    J = E.mmul(Sh, Sh)
    return dict(D=D, WR=WR, W1=W1, W1i=pow1[o1 - 1], P=P, Sh=Sh, Shi=Shi, J=J)


def run():
    ctx = build_all()
    D, WR, P, Sh, Shi, J = ctx["D"], ctx["WR"], ctx["P"], ctx["Sh"], ctx["Shi"], ctx["J"]
    Pc = msub(I15, P)
    out = {}
    out["V1_invariant"] = (mzero(E.mmul(E.mmul(Pc, D), P))
                           and mzero(E.mmul(E.mmul(Pc, WR), P)))
    tr_slot = {m: SC.solve_H(SC.H_avg(trace(E.mmul(P, build_theta_W(m))))) for m in (1, 2, 3, 4)}
    out["V2_traces"] = {m: tuple(str(x) for x in v) for m, v in tr_slot.items()}
    out["V3_helicity"] = trace(E.mmul(P, Sh)) == E.ZERO
    PSP = E.mmul(E.mmul(P, Sh), P)
    tgt = [[E.mul(E.zeta(18), P[i][j]) for j in range(N)] for i in range(N)]
    out["V3b_square"] = mzero(msub(E.mmul(PSP, PSP), tgt))
    out["V4_dihedral_global"] = mzero(msub(E.mmul(E.mmul(Sh, ctx["W1"]), Shi), ctx["W1i"]))
    out["V5_J_commutes"] = (mzero(msub(E.mmul(J, D), E.mmul(D, J)))
                            and mzero(msub(E.mmul(J, WR), E.mmul(WR, J))))
    out["V5b_J_monomial_1_minus_j"] = all(
        (J[i][j] == E.ZERO) or (i == (1 - j) % 15) for i in range(N) for j in range(N))
    Par = [[E.ONE if i == (-j) % 15 else E.ZERO for j in range(N)] for i in range(N)]
    X = [[E.ONE if i == (j + 1) % 15 else E.ZERO for j in range(N)] for i in range(N)]
    Z = [[E.e15(j) if i == j else E.ZERO for j in range(N)] for i in range(N)]
    rhs = [[E.mul(E.zeta(50), E.mmul(X, Z)[i][j]) for j in range(N)] for i in range(N)]
    out["E3_weyl_identity"] = mzero(msub(E.mmul(J, Par), rhs))
    return out


if __name__ == "__main__":
    for k, v in run().items():
        print(f"  {k}: {v}")
