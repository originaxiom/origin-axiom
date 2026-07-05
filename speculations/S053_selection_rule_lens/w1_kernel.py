"""S053 / W1 (the SEAM-E6 BRIDGE campaign, kernel wave) -- reconcile S053 + characterize the
proper seam kernel. Firewalled.

THE RECONCILIATION (the first guard, and it FIRED). S053's headline was a DIRECTED selection
rule: the raw matrix W1.Par.W2 has 45 nonzero entries, W2.Par.W1 has 225 -- an "arrow-shaped"
asymmetry flagged as the only possible Bin A. B385 warned this is the WRONG object: darkness is
SPECTRUM-cancellation in the H-projected seam, NOT raw cell-vanishing. Re-derived at the proper
seam (the DFT-eigenprojector pair table, seam_certification.solve_H -> s*sqrt(-15) coeff):

    order (W1,W2): 49 nonzero cells / 240, 44 seam-bearing (s != 0)
    order (W2,W1): 49 nonzero cells / 240, 44 seam-bearing (s != 0)  -- IDENTICAL

=> the S053 directionality DISSOLVES at the proper seam. It was raw cell-vanishing (B385's exact
warning); the seam kernel is ORDER-SYMMETRIC. The "arrow/CP" residue is DEAD. (Consistent with
B427: exchange = sigma_17, a Galois symmetry, which preserves the seam-count by construction.)

THE PROPER KERNEL (banked, symmetric, forced). What survives is the real seam selection rule --
and it is the already-banked EISENSTEIN GATE: the dark locus is gated by chi_{-3} (sqrt(-3)):
  * P68/B404: 3 | ord(C) <=> chi_{-3}(det(gamma'-I)) = -1 (142/142, exact).
  * B431: the boundary-torus split ACTIVE 120 / DARK 120, with y == 0 mod 3 ALL dark (the
    Eisenstein character gates the spatial support), x == 0 mod 10 all dark.
  * B402: seam intensity = f(gcd(address,15)) = {1:44, 3:32, 5:36, 15:0}.
So the KERNEL (what the seam forbids) is real and it is the sqrt(-3) / chi_{-3} Eisenstein gate --
a genuine selection rule, but FORCED arithmetic (the character of a determinant), symmetric, no
arrow. The kernel side of the hypothesis lands as: the dark locus IS a selection rule, and it is
the Eisenstein gate; not a new physical rule, and not directed.

VERDICT (W1): the directed-rule residue is retracted (raw-cell artifact); the seam kernel = the
banked symmetric chi_{-3} gate. Bin B for the directionality. The kernel is sqrt(-3)-carried,
which is the correct HALF of the kernel/image split (the coupling half = sqrt(5) is W2's E6
mixing). No physics claim; firewalled.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "frontier", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "frontier", "B358_seam_certification"))
import step0_exact_matrices as S0
import cyclo_engine as E


def _powers(W, o):
    I = [[E.ONE if i == j else E.ZERO for j in range(15)] for i in range(15)]
    out = [I]
    for _ in range(o - 1):
        out.append(E.mmul(out[-1], W))
    return out


def reconcile():
    """proper-seam pair tables for both orders; returns the (nonzero, seam-bearing) counts."""
    W1, W2 = S0.build_theta_W(1), S0.build_theta_W(2)
    P1, P2 = _powers(W1, 20), _powers(W2, 12)
    t12 = S0.pair_smatrix(P1, P2)
    t21 = S0.pair_smatrix(P2, P1)
    seam = lambda t: sum(1 for (p, q, r, s) in t.values() if s != 0)
    return dict(order12=(len(t12), seam(t12)), order21=(len(t21), seam(t21)),
                directed=(len(t12) != len(t21) or seam(t12) != seam(t21)))


if __name__ == "__main__":
    r = reconcile()
    print("proper-seam reconciliation:", r)
    assert r["order12"] == r["order21"] == (49, 44)
    assert not r["directed"]
    print("S053 directionality DISSOLVES at the proper seam (raw-cell artifact, per B385);"
          " kernel = symmetric chi_{-3} Eisenstein gate. Directed residue RETRACTED.")
