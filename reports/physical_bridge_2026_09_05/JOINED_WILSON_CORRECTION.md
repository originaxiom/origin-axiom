# R93 post-first-run proof-sign repair, before corrected execution

Original pre-run a19e6c783c2da3bf1040e54aa8dda43f5e64665c passed81 native,
65 separate reference and18 focused checks. Those raw logs/exits and
original six science hashes are retained. No science run failed. A
subsequent personal proof review caught an untested analytic sign:

    T in exterior2(E) tensor chi^w invariant means
    chi^w rho T rho^T=T,
    so (chi^w rho)T=T rho^-T.

The target is E tensor chi^w, NOT chi^-w. The first proof's sign is
wrong; the conclusion that H0 vanishes stays true because BOTH twists
are simple and a nonzero intertwiner would be invertible, impossible
for odd-dimensional skew T. This is not a hidden retraction of the SM
phase or an excuse to keep the displayed map wrong.

Added native and separate reference two-sided rank-two control:
rho=diag(2,3), T=((0,1),(-1,0)), chi=1/6. The invariant equation and
positive-twist intertwiner hold; inverse-twist intertwiner fails.
Extend the existing LIVE alternating-tensor test with this covariance.
No old acceptance criterion weakened or field/phase replaced. All three
actual joins, complete248/kernel/action and physical limits unchanged.

Corrected design/proof/producers/test plus this disclosure are to be
committed, pushed, server-confirmed and byte-checked before corrected
import/collection/run. Original81/65 controls DID NOT test this sign;
do not cite them as having done so. Analytic independence is still owed.
No full-suite/main-bank/physical SM or TOE acceptance is claimed.
