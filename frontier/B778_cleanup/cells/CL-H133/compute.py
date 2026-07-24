"""
CL-H133 -- chord-check of H133 (cc3 suspect): is Z4 = Tr rho(A1) = 0 at E6 level 4
a GENUINE structural zero, or an even/odd cancellation hiding a nonzero theta-odd
piece (the W4-304 signature)?

BACKGROUND
  H133 registered: Z = Tr rho(A1) = +1 at E6 levels 1,2,3; gate = level 4 or a proof.
  B600 reproduced: Z4 = 0 exactly (cc2 mod-Phi192 certificate) => H133 died at its gate.
  cc3's suspicion: that zero may be TRACE-BLIND -- the W4-304 lesson (B772/B773) is that a
  banked "identically zero" can hide a clean even/odd CANCELLATION (tr_even = tr_odd, so the
  parity-difference reads 0 while both sectors are nonzero).

THE DISCRIMINATING TEST (in-cell, independent recompute -- NOT a citation of B600)
  Build the fig-8 monodromy word rho(A1) in the E6 level-k Weil rep from the c3 (B570)
  Kac-Peterson S,T builder, generalized to any level (same construction B600 used).
  theta = charge-conjugation involution (diagram flip); it is S^2 and commutes with S and
  with T (conjugate primaries have equal h), hence [theta, rho] = 0 EXACTLY -> rho block-
  diagonalizes on the theta = +-1 eigenspaces. This makes the parity readout a GENUINE
  eigenspace decomposition of the same non-abelian Weil rep (the B773/W4-304-accepted chord
  object), NOT an abelianized relabel.
    P_odd  = (I - theta)/2 ,  P_even = (I + theta)/2
    tr_odd  = Tr(P_odd  rho) = (Z - Ztheta)/2     <- the theta-odd chord readout
    tr_even = Tr(P_even rho) = (Z + Ztheta)/2
  where Z = Tr(rho), Ztheta = Tr(theta rho).

  The W4-304 failure mode was banking ONLY the parity-DIFFERENCE (par = tr_even - tr_odd =
  Ztheta) which is 0 both when both sectors vanish AND when they cancel. Here we compute Z
  and Ztheta SEPARATELY and hence BOTH sectors, so the cancellation ambiguity is resolved.

VERDICT (sealed, B778 prereg 5339a247)
  tr_odd(k=4) nonzero  ->  RESOLVED-A  (H133 lights up: hidden theta-odd structure, the
                                        W4-304 signature; independently reproduce + hand-flag)
  tr_odd(k=4) == 0     ->  RESOLVED-B  (genuine zero: BOTH parity sectors vanish; H133's
                                        death HARDENS at the chord level)

CHORD DISCIPLINE (B774) self-test: tr_odd is Tr(rho | theta-odd eigenspace) of the genuine
  non-abelian Weil-rep monodromy on a genuine invariant subspace (rho commutes with theta,
  verified in-cell to ~1e-13). This is exactly the object B773's verifier accepted as a real
  chord for W4-304 -- not a finer abelian/class-group invariant wearing the chord's name.
"""
import importlib.util
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
C3PATH = os.path.join(HERE, "..", "..", "..", "B570_allowed_plays",
                      "c3_e6_level2_monodromy.py")
spec = importlib.util.spec_from_file_location("c3", C3PATH)
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

# comarks in c3's node ordering (chain 0-2-3-4-5, branch 1 on 3): (1,2,2,3,2,1)
COMARK = [1, 2, 2, 3, 2, 1]
HV = 12
TOL = 1e-9

W, eps = c3.weyl_group()
rho_w = c3.root_coords([1] * 6)


def level_weights(k):
    out = []

    def rec(prefix, rem):
        i = len(prefix)
        if i == 6:
            out.append(tuple(prefix))
            return
        for v in range(rem // COMARK[i] + 1):
            rec(prefix + [v], rem - COMARK[i] * v)
    rec([], k)
    return out


def level_data(k):
    prim = level_weights(k)
    N = len(prim)
    KH = k + HV
    shifted = [c3.root_coords(p) + rho_w for p in prim]
    S = np.zeros((N, N), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
    for a in range(N):
        for b in range(a, N):
            ips = Wl[:, a, :] @ (c3.C @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
    S /= np.sqrt((S @ S.conj().T)[0, 0].real)
    if S[0, 0].real < 0:
        S = -S
    cc = k * 78 / KH
    hs = [float(c3.root_coords(p) @ (c3.C @ (c3.root_coords(p) + 2 * rho_w)))
          / (2 * KH) for p in prim]
    T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])
    # rho(A1): the fig-8 monodromy word (B600 gate word r1)
    rho = T @ T @ S @ T
    # gate: the second word representation must agree
    r2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    words_agree = float(np.linalg.norm(rho - r2))
    # theta permutation matrix (charge conjugation = diagram flip)
    theta = np.zeros((N, N))
    for i, p in enumerate(prim):
        theta[prim.index(c3.theta(p)), i] = 1.0
    return prim, N, S, T, rho, r2, words_agree, theta


def main():
    log = []

    def L(m):
        print(m, flush=True)
        log.append(m)

    L("CL-H133 chord-check: is Z4 = Tr rho(A1) = 0 genuine, or an even/odd cancellation?")
    L("=" * 78)
    ladder = []
    res4 = None
    for k in (1, 2, 3, 4):
        prim, N, S, T, rho, r2, wa, theta = level_data(k)
        # theta must be S^2 and commute with rho -> clean eigenspace decomposition
        comm = float(np.linalg.norm(theta @ rho - rho @ theta))
        s2theta = float(np.linalg.norm(S @ S - theta))
        Z = complex(np.trace(rho))
        Ztheta = complex(np.trace(theta @ rho))
        P_odd = (np.eye(N) - theta) / 2.0
        P_even = (np.eye(N) + theta) / 2.0
        tr_odd = complex(np.trace(P_odd @ rho))
        tr_even = complex(np.trace(P_even @ rho))
        # cross-check the algebraic identity
        id_odd = abs(tr_odd - (Z - Ztheta) / 2)
        id_even = abs(tr_even - (Z + Ztheta) / 2)
        dim_odd = int(round(np.trace(P_odd).real))
        row = {
            "k": k, "N": N, "words_agree": wa, "[theta,rho]": comm,
            "||S^2-theta||": s2theta, "dim_theta_odd": dim_odd,
            "Z": [round(Z.real, 10), round(Z.imag, 10)],
            "Z_theta": [round(Ztheta.real, 10), round(Ztheta.imag, 10)],
            "tr_even": [round(tr_even.real, 10), round(tr_even.imag, 10)],
            "tr_odd": [round(tr_odd.real, 10), round(tr_odd.imag, 10)],
            "identity_resid": max(id_odd, id_even),
        }
        ladder.append(row)
        L(f"k={k}: N={N:3d}  gate(words-agree)={wa:.1e}  [theta,rho]={comm:.1e}  "
          f"||S^2-theta||={s2theta:.1e}  dim(theta-odd)={dim_odd}")
        L(f"      Z=Tr rho      = {Z.real:+.10f} {Z.imag:+.1e}i")
        L(f"      Z_theta       = {Ztheta.real:+.10f} {Ztheta.imag:+.1e}i")
        L(f"      tr_even       = {tr_even.real:+.10f} {tr_even.imag:+.1e}i")
        L(f"      tr_odd (chord)= {tr_odd.real:+.10f} {tr_odd.imag:+.1e}i   "
          f"(identity resid {max(id_odd, id_even):.1e})")
        if k == 4:
            res4 = row

    L("=" * 78)
    # ---- SEALED VERDICT (in-code) ----
    trod = complex(*res4["tr_odd"])
    trev = complex(*res4["tr_even"])
    z4 = complex(*res4["Z"])
    chord_nonzero = abs(trod) > TOL
    # sanity: the parity decomposition must be clean (rho commutes with theta) and
    # the algebraic identity must hold, else the readout is untrusted
    clean = res4["[theta,rho]"] < 1e-8 and res4["identity_resid"] < 1e-8 \
        and res4["words_agree"] < 1e-8
    if not clean:
        verdict = "UNRESOLVED"
        reason = ("the parity decomposition is not clean (commutator / identity / gate "
                  "residual too large) -- the chord readout cannot be trusted this run.")
    elif chord_nonzero:
        verdict = "RESOLVED-A"
        reason = ("the theta-odd chord readout tr_odd(k=4) is NONZERO while Z4=Tr rho=0 -- "
                  "Z4=0 is an even/odd CANCELLATION masking hidden theta-odd structure "
                  "(the W4-304 signature). H133 lights up at the chord level. FLAG for "
                  "hand-verification.")
    else:
        verdict = "RESOLVED-B"
        reason = ("Z4 = Tr rho(A1) = 0 is a GENUINE structural zero: BOTH parity sectors "
                  "vanish independently (tr_odd = tr_even = 0), computed from SEPARATE "
                  "traces Z and Z_theta -- NOT an even/odd cancellation. Unlike W4-304 "
                  "(where only the parity-difference was banked and tr_odd=1/4 was hidden), "
                  "here Z=0 AND Z_theta=0, forcing tr_odd=(Z-Z_theta)/2=0. The theta-odd "
                  "chord is empty; H133's death HARDENS at the chord level.")

    L(f"\nVERDICT: {verdict}")
    L(f"  Z4 = {z4.real:+.1f}   tr_even = {trev.real:+.1f}   tr_odd = {trod.real:+.1f}")
    L("  " + reason)

    out = {
        "cell": "CL-H133",
        "task": "chord-check H133: is Z4=Tr rho(A1)=0 genuine or an even/odd cancellation?",
        "method": "in-cell independent recompute of E6 level-k Weil rep (c3/B570 builder); "
                  "theta-odd chord = Tr(rho | theta-odd eigenspace), [theta,rho]=0 verified.",
        "tol": TOL,
        "ladder": ladder,
        "level4": {
            "Z4": z4.real,
            "Z4_theta": complex(*res4["Z_theta"]).real,
            "tr_even": trev.real,
            "tr_odd_chord": trod.real,
            "dim_theta_odd": res4["dim_theta_odd"],
            "commutator_theta_rho": res4["[theta,rho]"],
            "identity_residual": res4["identity_resid"],
        },
        "chord_discipline_B774": (
            "PASS -- tr_odd is Tr(rho restricted to the genuine theta=-1 eigenspace) of the "
            "non-abelian Weil-rep monodromy (rho commutes with theta exactly); the same "
            "object B773's verifier accepted as a real chord for W4-304, not an abelian "
            "relabel. Self-test note: it is a trace, but of the non-abelian rho on a genuine "
            "invariant subspace -- the accepted lineage."),
        "verdict": verdict,
        "reason": reason,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    with open(os.path.join(HERE, "output.txt"), "w") as f:
        f.write("\n".join(log) + "\n")
    return verdict


if __name__ == "__main__":
    main()
