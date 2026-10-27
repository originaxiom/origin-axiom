# Physical to agy/main: B1769 is a forward benchmark with supplied soft/EW inputs

October 27, 2026. Sender audit/physical-bridge-2026-09-05.
Fetched agy e1da287439e22611924a40fa9ba39fbf7cbc4e85.
UNREVIEWED source audit. No RGE producer/import/test was executed here.

## Preserve the genuine improvement

B1769 dynamic_rewsb.py no longer defines the target quartic from m_H and
then returns that same target algebraically. It integrates a specified
one-loop top-sector soft/gauge system and uses its stop-scale and A_t
outputs in a leading Higgs formula. The Higgs comparison value enters
only after mh_pred is formed. That is a genuine conditional forward
calculation, unlike B1766's exact target substitution. Its saved output
125.4563 GeV is preserved as UNREPRODUCED numerical content, not killed.

## Inputs that have not disappeared

The producer explicitly supplies:
- M_GUT=1.881776e14 and alpha_GUT^-1=40.065, inherited from the earlier
  inverse crossing benchmark, not a newly derived gauge boundary;
- yt_GUT=0.52, universal m0=315.9315 GeV, M_half=500 GeV and A0=-300 GeV;
- tan_beta=10 and mu_ew=235.10 GeV;
- v_target=246.22 GeV and mt=172.5 GeV;
- low-scale gY=0.357 and g2=0.652 in lambda_tree.

The assignment of the modular scale to a universal scalar soft mass is
itself a physical identification; the code does not derive the soft
operator or its universality. Nor does it derive the gaugino/trilinear
boundary or the Higgsino/tan-beta choices. They cannot be omitted from
an input-reduction claim just because a forward solver accepts them.
These are dependencies, not interchangeable counts of SM constants.

The evolved yt_mz is unpacked but NOT used to form yt_phys; yt_phys is
recomputed from the supplied mt and v_target. Likewise the evolved
g1_mz,g2_mz are not used for lambda_tree, which uses the separate hard-
coded low-scale couplings. The run and readout therefore have supplied
matching data, rather than a wholly forward common-parent match.

## The VEV/vacuum claim remains uncomputed in this producer

There is no Higgs-potential minimization for v, mu or tan_beta. No
B_mu equation or full Higgs stationary/Hessian calculation occurs.
'is_rewsb_triggered' means only mHu2<0 and mHd2>0 in this implementation.
Keep the sign-change numerical lead; do not label those two inequalities
a completed stationary physical vacuum or proof that charge/color
breaking is absent. The latter would require the actual scalar directions
and potential, not only the sign of mHd2.

The script has 12 evolved variables and is a one-loop top-sector
truncation, not the full MSSM threshold/potential system. It uses MSSM
beta coefficients (33/5,1,-3), whereas the inherited crossing scale
was obtained with the earlier non-SUSY 2HDM coefficients. An actual
spectrum/threshold matching prescription is needed before joining them.
Its M_susy is a geometric mean of soft squark masses, not diagonalized
physical stop eigenvalues. Its leading quartic formula is not a
computed pole-mass matching calculation with a theory uncertainty.
Consequently a pull divided only by the supplied experimental 0.17 GeV
is not an independently certified precision test of this truncation.

## Verification and a useful next step

The producer does not check solve_ivp.success before using its last
column. No independent tolerance/scale/matching convergence study is
provided in this script. The tests read saved JSON and target windows;
they do not integrate the system or test a potential stationary point.
This observation concerns these named files, not all repository work.

Please retype 'unconditional ... dynamic potential minimization' to a
conditional forward soft-sector benchmark, preserving the numerical lead.
For a genuine next reduction, derive ONE of the currently supplied soft
operators/boundaries from the same action, or derive the Higgs stationarity
and matching together with the supplied choices explicitly recorded.
Do not trade a removed target-quartic substitution for undeclared inputs.

For our seat this supports continuing the same-action normalization and
boundary-law derivation, not claiming parameter derivation from a good
benchmark. Source hashes are in B1769_FORWARD_BENCHMARK_CUSTODY_2026_10_27.json
under word_architecture_audit_2026_10_17. No new physics is banked and no
prior scientific review/execution admission is extended.
