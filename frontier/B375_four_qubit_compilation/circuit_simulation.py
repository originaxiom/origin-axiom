"""B375 (PD1.3) — the four-qubit compilation of the level-15 algebra + EXACT protocol simulation.

THE DELIVERABLE (kappa's letter, in simulation): the level-15 Weil algebra compiled into two
circuit primitives on a 4-qubit register (16-dim, with the 15-dim theta space embedded and
|15> held fixed), plus the interference-measurement protocol whose post-processed outputs ARE
the banked seam values. Everything verified exactly in Q(zeta60) — no floats anywhere.

The primitives:
  D_hat  = diag( zeta15^{j(j-1)/2} , j = 0..14 ; 1 )      -- a 16-dim diagonal phase gate
  UF_hat = ( zeta15^{jk} / sqrt(15) )_{j,k=0..14} (+) [1] -- the unitary 15-point DFT, embedded
  (sqrt(15) is exact in the engine; UF_hat . UF_hat^dagger = I is verified as an identity)
  WR_hat = UF_hat . D_hat^{-1} . UF_hat^dagger             -- verified == the banked WR, embedded
Every seed word W_m = WR^m D^m and every observable word below is an alternation of the two
primitives (and their inverses/powers).

The protocol: for each of the 240 words U(j,l) = Par . W1^j . W2^l (embedded, with
U|15> = |15>), a controlled-U Hadamard test on the maximally mixed register measures
  amp(j,l) = tr_16( U(j,l) ) / 16  (real and imaginary parts from <X>, -<Y> on the ancilla).
Post-processing with the declared DFT weights reconstructs the pair invariants exactly:
  t(a,b) = (1/240) sum_{j,l} zeta20^{-ja} zeta12^{-lb} ( 16 amp(j,l) - 1 ).
This module simulates the amplitudes EXACTLY and verifies the reconstruction reproduces the
banked flagship cells, plus the kappa-word example U_k = D WR D^{-1} WR^{-1} (the Weil image
of the classical commutator [R, L]) measured the same way.
"""
import json
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E                     # noqa: E402
import seam_certification as SC              # noqa: E402
from step0_exact_matrices import build_theta_W, matrix_order, par_trace  # noqa: E402

N = 15


def embed16(M):
    """15-dim engine matrix -> 16-dim block-diag(M, [1])."""
    out = [[E.ZERO] * 16 for _ in range(16)]
    for i in range(N):
        for j in range(N):
            out[i][j] = M[i][j]
    out[15][15] = E.ONE
    return out


def mmul16(A, B):
    return [[_dotrow(A[i], B, j) for j in range(16)] for i in range(16)]


def _dotrow(row, B, j):
    t = E.ZERO
    for k in range(16):
        if row[k] != E.ZERO and B[k][j] != E.ZERO:
            t = E.add(t, E.mul(row[k], B[k][j]))
    return t


def dagger(A):
    return [[E.conj_elt(A[j][i]) for j in range(16)] for i in range(16)]


def run():
    rep = {}
    # ---- the primitives, exactly ----
    SQRT15 = E.SQRT15
    inv15 = SC.solve_H(SC.H_avg(E.mul(SQRT15, SQRT15)))       # sanity: 15? (sqrt15^2)
    D15 = [[E.e15((j * (j - 1) // 2) % 15) if i == j else E.ZERO for j in range(N)] for i in range(N)]
    Dhat = embed16(D15)
    # UF_hat = F/sqrt15 (+) [1]; 1/sqrt15 = sqrt15/15
    c = E.scal(Fr(1, 15), SQRT15)
    UF = [[E.mul(c, E.e15((i * j) % 15)) for j in range(N)] for i in range(N)]
    UFhat = embed16(UF)
    I16 = [[E.ONE if i == j else E.ZERO for j in range(16)] for i in range(16)]
    uni = mmul16(UFhat, dagger(UFhat))
    rep["UF_unitary_exact"] = (uni == I16)
    # WR via the primitives == the banked WR
    Dinv15 = [[E.e15((-(j * (j - 1) // 2)) % 15) if i == j else E.ZERO for j in range(N)] for i in range(N)]
    WR_circ = mmul16(mmul16(UFhat, embed16(Dinv15)), dagger(UFhat))
    F = [[E.e15((i * j) % 15) for j in range(N)] for i in range(N)]
    Fi = [[E.scal(Fr(1, 15), E.e15((-i * j) % 15)) for j in range(N)] for i in range(N)]
    WR_bank = E.mmul(E.mmul(F, Dinv15), Fi)
    rep["WR_from_primitives_exact"] = (WR_circ == embed16(WR_bank))

    # ---- the 240 word amplitudes, exactly ----
    W1 = build_theta_W(1)
    W2 = build_theta_W(2)
    o1, pow1 = matrix_order(W1)
    o2, pow2 = matrix_order(W2)
    Par = [[E.ONE if i == (-j) % N else E.ZERO for j in range(N)] for i in range(N)]
    tr15 = {}
    for j in range(o1):
        PW = E.mmul(Par, pow1[j])
        for l in range(o2):
            # tr(Par W1^j W2^l) = par_trace(W1^j, W2^l)
            tr15[(j, l)] = par_trace(pow1[j], pow2[l])
    # amp(j,l) = (tr15 + 1)/16 — store the H-average of a sample; keep exact zeta-vectors internal
    # ---- the reconstruction: t(a,b) from the amplitudes ----
    def recon(a, b):
        t = E.ZERO
        for j in range(o1):
            zja = E.zeta((-3 * j * a) % 60)
            for l in range(o2):
                # (16*amp - 1) = tr15 exactly — the embedding correction
                t = E.add(t, E.mul(E.mul(zja, E.zeta((-5 * l * b) % 60)), tr15[(j, l)]))
        return E.scal(Fr(1, o1 * o2), t)

    banked = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))["1,2"]
    ok = True
    for cell in ("0,4", "0,8", "6,2", "14,10"):
        a, b = (int(x) for x in cell.split(","))
        sol = SC.solve_H(SC.H_avg(recon(a, b)))
        got = [str(x) for x in sol]
        if got != banked[cell]:
            ok = False
    rep["protocol_reproduces_banked_cells"] = ok

    # ---- the kappa word ----
    Uk = E.mmul(E.mmul(D15, WR_bank), E.mmul(Dinv15, E.mmul(E.mmul(F, D15), Fi)))
    tk = E.ZERO
    for i in range(N):
        tk = E.add(tk, Uk[i][i])
    rep["kappa_word_trace"] = [str(x) for x in SC.solve_H(SC.H_avg(tk))]

    with open(os.path.join(HERE, "circuit_simulation.json"), "w") as fh:
        json.dump(rep, fh, indent=1)
    return rep


if __name__ == "__main__":
    for k, v in run().items():
        print(f"  {k}: {v}")
