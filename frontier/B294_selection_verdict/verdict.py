"""B294 verdict (pyenv) -- THE SELECTION VERDICT. Phase VI. Imports selection_verdict.py and asserts the whole seam
arc closes coherently.

THE ANSWER (to B286's load-bearing 'selective vs catalogue?'): SELECTIVE for the object's OWN structure, CATALOGUE for
Standard-Model-value selection.
  * SELECTIVE: a canonical distinguished closing exists -- the fiber/Sol slope (0,1) re-sees A=LR (P1) + the P8
    torsion ladder (B287).
  * AXIS-STRATIFIED: dynamical (B287) / arithmetic (B288, absent) / scale (B291) pick different things.
  * CATALOGUE for SM-values: E6 lost (B288), CP sign external (B289/B295), scale value gapped (B290), chiral datum
    absent (B292), trajectory gated (B293).

NET structural theorem (relocated to the seam): the object supplies a canonical closing and all the dimensionless
STRUCTURE; the ACTUALIZATION of a specific SM-valued world is NOT forced. Strengthens the firewall. Nothing to CLAIMS.
"""
import importlib.util
import pathlib

_K = pathlib.Path(__file__).resolve().parent / "selection_verdict.py"
_spec = importlib.util.spec_from_file_location("b294_kernel", _K)
sv = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(sv)

SELECTIVE_FOR_OWN_STRUCTURE = sv.SELECTIVE_FOR_OWN_STRUCTURE
CATALOGUE_FOR_SM_VALUES = sv.CATALOGUE_FOR_SM_VALUES
SELECTION_IS_AXIS_STRATIFIED = sv.SELECTION_IS_AXIS_STRATIFIED
STRENGTHENS_FIREWALL = sv.STRENGTHENS_FIREWALL
DERIVES_SM_VALUES = sv.DERIVES_SM_VALUES

# the eight probe verdicts that must all hold for the synthesis to stand:
PROBE_VERDICTS = {
    "B287": sv.B287.verdict, "B288": sv.B288.verdict, "B289": sv.B289.verdict, "B290": sv.B290.verdict,
    "B291": sv.B291.verdict, "B292": sv.B292.verdict, "B293": sv.B293.verdict, "B295": sv.B295.verdict,
}


def all_probes_pass():
    return {k: v() for k, v in PROBE_VERDICTS.items()}


def verdict():
    probes_ok = all(all_probes_pass().values())
    return bool(probes_ok and sv.cross_axis_distinct()
                and SELECTIVE_FOR_OWN_STRUCTURE and CATALOGUE_FOR_SM_VALUES
                and SELECTION_IS_AXIS_STRATIFIED and STRENGTHENS_FIREWALL and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("probe verdicts:", all_probes_pass())
    print("cross-axis distinct:", sv.cross_axis_distinct())
    print("\nSELECTIVE for own structure (B287):", SELECTIVE_FOR_OWN_STRUCTURE)
    print("CATALOGUE for SM-values:", CATALOGUE_FOR_SM_VALUES)
    print("axis-stratified:", SELECTION_IS_AXIS_STRATIFIED, "| strengthens firewall:", STRENGTHENS_FIREWALL)
    print("derives SM values:", DERIVES_SM_VALUES, "| verdict:", verdict())
