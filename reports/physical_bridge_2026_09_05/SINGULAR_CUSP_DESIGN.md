# Path-local R14 — construct the singular cusp field retained by R72

STATUS 2026-09-07: before the first run of this source/tests. No B number.
Original scientific seal: SHA256 and local commit before execution.
R13 is reported at 1c46049f; its result is not a global chirality kill.

P0: rank-two complete hyperbolic cusp ENDS with prescribed constant line
charge densities, including the hexagonal torus of m202 and the three
fixed points of its order-three cusp rotation. NOT a global m202 solution,
all backgrounds, physical source selection, or a chiral-spectrum proof.

P6 prior: a torus Green function plus an explicit radial zero mode should
solve the sourced BPS equation on the end and support outward cusp flux
for equal positive charges. The tube boundary is expected to be INWARD
for positive charge; R72's empty inward-boundary sentence likely omits
the tubes even though their Euler characteristic is zero. Retain the
conditional nonzero index; do not call the route disproved by this repair.

## Prior art and physical scope

WORKING_RULES/P0--P6/CC relay, campaign stop rules and X33 remain read.
R71/R72 bodies and relay at physics pin 124c2466cb80f597f4447f1a6f0e8c259681ee58
read fully; all r72/r72b/r72c/r72d producers read (not executed here).
R72 explicitly leaves the global singular harmonic F unconstructed;
this cell addresses its necessary cusp-end piece, not an alleged absence
of all other work. The new-source packet is not merged or modified.

Local search: `line source harmonic` flags 1290 corpus hits, 120 settled
two-term matches (generic 'line'/'source' terms); atlas card Higgs boundary
has the known recent-epoch limitations. Code search for log(tanh), line
source, cusp/source and Poisson locates the existing B739/B1007/R13 kernels;
no universal absence verdict is taken from that sample. R12 already has
the required relative-Euler and arc-excision theorem: use it, not another
claim that topology is missing. New computation is the sourced field.

Primary sources re-read: Pantev--Wijnholt arXiv:0905.1968 section 3.2
(3.20--3.25: beta is prescribed line-charge density, Poisson equation,
flux balance) and 3.5 (relative topology); Braun et al. arXiv:1812.06072
eq. 2.18 (BPS equations) and Appendix B (parent adjoint and kinetic data);
NIST DLMF 20.2.1/20.2.6 (theta series/quasiperiods). Accessed 2026-09-07.

This is the ABELIAN specialization W=0, phi=u dF on the cusp, where u is
a fixed commuting Lie direction and its length/charge normalization is
declared, not derived. It does not identify this W with principal Riley
holonomy, select an E8/E6 parent, or derive an ADE-fibre lift. The latter
data are required before identifying any count with physical generations.

## Formula and conventions before execution

Metric ds^2=(|dw|^2+dz^2)/z^2, w modulo Z+tau Z, A=Im(tau)>0.
Curvature length set to one. Points p_i have line densities beta_i per
unit hyperbolic length; Q=sum beta_i. In particular these are not finite
total point charges: a line running to infinite cusp height has infinite
proper length. Divergence constraints use integrated density/flux, not
an unweighted sum of labels on arbitrary closed curves.

    U(w) = log|theta_1(pi w | tau)| - pi (Im w)^2/A,
    Delta_T U = 2 pi (delta_0 - 1/A),
    F(w,z) = sum beta_i U(w-p_i)
           + (pi Q/A) z^2 log(z/z0) + c z^2.

Here z0=1 and c=0 are declared representatives of the free radial flux
data; also test c=-20,0,+20 and Q=0. With Delta_H=z^2(Delta_T+partial_z^2
-z^-1 partial_z), Delta_H F=2 pi z^2 sum beta_i delta_(p_i).
Phi=dF is closed, and coclosed off the prescribed lines; no nonabelian
commutator is silently discarded in a noncommuting background.

1. Verify theta quasiperiods and elliptic Green-function periodicity by
   two series cutoffs (12 and 18 terms), independent mpmath theta, and
   translations 1,tau,1+tau on three test points. Tolerance 2e-11.
2. Exact symbolic zero-mode derivative and local straight-geodesic
   log(tanh distance) control. The latter is NOT the global periodic
   Green function. Omit the z^2 log(z) term as a negative control: its
   residual must be nonzero for Q!=0. For Q=0 the torus Green sum alone
   is harmonic off its sources (positive control).
3. Verify full off-source PDE using independent centered differences of
   F in three coordinates at steps 3e-4,1e-4 on three points and heights
   1,1.7,2.4. Tolerance 3e-3 at both steps; analytic Laplacian cancellation
   <2e-10. Numerical derivatives supplement, not replace, the proof.
4. For tau=exp(i pi/3), reconstruct fixed points of the order-three
   integer matrix [[-1,-1],[1,0]]: (0,0),(1/3,1/3),(2/3,2/3).
   Check order-six rotation orbits {0},{1,2}; equal charges on all three
   and the less restrictive beta=(2,1,1) both preserve that rotation.
   The asymmetric beta=(1,2,1) must break it. Source locations are the
   actual cusp rotation's fixed points after translating its fixed center
   to zero, NOT a global identification of the three axes or source signs.
5. Integrate the actual gradient on radius .01 tubes about each source,
   2048 angular nodes, heights 1..3. Outward normal of the EXCISED domain
   points toward the line. It must give NEGATIVE tube flux for beta_i>0.
   Include punctures in the outer torus area and check total upper+lower+
   tube flux <2e-9. Dropping the tubes must fail (>1). Use both signs and
   a zero-total-density control. Preserve the finite-radius correction.
6. Verify c changes the flux at a fixed height without changing the
   Poisson equation. Positive total density eventually gives positive
   radial flux for any fixed finite c in this solution family. This is
   not source selection or a global existence/uniqueness theorem.

R12 already shows why A=all positive tubes and A=empty can have the SAME
Euler number but different H0. R72's plus/minus-three Euler can survive
correcting its empty-inward-boundary assertion. Do not infer all Betti
numbers or a physical zero-mode domain from an Euler cancellation.

No empirical value, new B number, main merge or external write is elected.
Keep first execution output/failures and all earlier seals. After the end
field, match across the actual compact core and examine the charged
operator/parent representation before declaring chirality solved.
