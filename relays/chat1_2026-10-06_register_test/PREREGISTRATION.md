# PREREGISTRATION — the register test: m000 (the act) against m004 (the act with its measurer)
Sealed 2026-10-06 by the web seat (chat1) BEFORE any computation below. Hash recorded in PREREG.sha256.

## The reading under test
The golden act LP (det -1) alone gives m000. A one-bit register recording what the act changes
(the orientation, flipped by every tick) closes after two ticks; act + register is the orientation
double cover, monodromy (LP)^2 = LR, i.e. m004. Algebraically: pi1(m004) = ker w, w the orientation
character of pi1(m000). H1(m000) = Z (T-ROOT), so w is the UNIQUE surjection pi1(m000) -> Z/2.
Prediction of the reading: everything m004 carries is m000's data plus the one register bit w.

## Predictions (each with its kill condition)
P1  Tower interleaving. The k-fold cyclic cover of m000 is orientable iff k is even, and its
    2n-fold cyclic cover is isometric to m004's n-fold cyclic level M_n (n = 1..4).
    H1 torsion order of m000's k-level = |1 - tr((LP)^k) + (-1)^k|.
    KILL: any mismatch of orientability, isometry or torsion order.
P2  The 2T door (F-MC's entrance). Surjections onto 2T = SL(2,F3):
    (a) m000 has 48 and m004 has 48 (B1234 re-derived; m004 also via the Reidemeister-Schreier
        presentation of ker w, as a control that ker w is m004's group).
    (b) THEOREM-LEVEL (2T has no index-2 subgroup; its centre is +-1): restriction to ker w is
        exactly 2-to-1, the fibres {rho, rho (x) w}. So EXACTLY 24 of m004's 48 extend to m000.
        KILL: any other number.
    (c) THE REAL TEST — what the other 24 are. Predicted: each non-extendable psi has deck image
        psi o tau (tau = conjugation by an orientation-reversing element) NOT inner-conjugate to
        psi, and related to it by the OUTER automorphism of 2T (the omega <-> omegabar swap).
        Reading: on the 2T door the register's flip acts as the Galois swap.
        Alternative outcome, registered now: psi o tau IS inner-conjugate but obstructed by the
        sign A^2 = -psi(t^2) (a Pin-type obstruction, B1382's shape). Either is reported as found.
P3  Shapiro control (code check, theorem-guaranteed). For each m000 surjection rho and V the
    natural 2-dim rep of SL(2,F3) over F3:
    dim H1(m004; V|) = dim H1(m000; V) + dim H1(m000; V (x) w).  KILL (of the code): any failure.
    The m000 values themselves are new: twisted cohomology of the Gieseking manifold in the
    2T frame, never computed (GENESIS s5/s8 frontier).

## Scope tag (GENESIS s6)
frame: F-MC entrance (the 2T door); object: m000 and m004 (and m004's levels M1..M4 for P1);
reach: single (two states); hypotheses: SnapPy's presentations; 2T realised as SL(2,F3).
## Not claimed, whatever comes out
That the register reading is physics; that m000 is selected; that any count changes. A pass means
only: on these data, m004 = m000 + the register bit, exactly.
