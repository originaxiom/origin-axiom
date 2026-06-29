"""B294 -- THE SELECTION VERDICT: selective or catalogue? Run: python (pyenv). Phase VI (the synthesis).

Consolidates the seam arc (B287-B293, B295) into one selection table and answers B286's load-bearing question.
Imports the sibling verdict modules and assembles, per AXIS, the distinguished closing (if any), the verdict
(forced / free / absent), and the firewall tier (math / HELD / stop-gate). Then runs the cross-axis coincidence test.

THE ANSWER: SELECTIVE for the object's OWN structure, CATALOGUE for Standard-Model-value selection.
  * SELECTIVE: there IS a canonical distinguished closing -- the fiber/Sol slope (0,1) re-sees A=LR (P1) + the P8
    torsion ladder (B287). The object re-instantiates its own proven core at a forced seam.
  * AXIS-STRATIFIED: the dynamical (B287), arithmetic (B288), and scale (B291) axes pick DIFFERENT things; no single
    closing is distinguished on all axes.
  * CATALOGUE for SM-values: E6 lost on closing (B288), CP sign external (B289/B295), scale value gapped (B290,
    122-order), chiral datum absent (B292), trajectory gated (B293). No closing is forced to be 'our universe'.

NET (structural theorem, relocated to the seam): the object supplies a canonical closing and all the dimensionless
STRUCTURE (the dynamics A=LR, the CP magnitude+sign-law, the scale ladder, the clock); the ACTUALIZATION of a specific
SM-valued world is NOT forced. This STRENGTHENS the firewall. Nothing to CLAIMS.
"""
import importlib.util
import pathlib

_FRONTIER = pathlib.Path(__file__).resolve().parents[1]


def _load(bdir, name):
    p = _FRONTIER / bdir / "verdict.py"
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


B287 = _load("B287_distinguished_closing", "b287v")
B288 = _load("B288_arithmetic_filling_census", "b288v")
B289 = _load("B289_cp_sign_law", "b289v")
B290 = _load("B290_core_scale_ladder", "b290v")
B291 = _load("B291_scale_extremal", "b291v")
B292 = _load("B292_multiplicity_2manifold", "b292v")
B293 = _load("B293_peripheral_clock", "b293v")
B295 = _load("B295_ssb_gauge_status", "b295v")


# axis -> (distinguished closing / object, verdict, tier)
def selection_table():
    return {
        "dynamical (fiber/Anosov, B287)":
            ("(0,1) = Sol torus bundle T x I / A=LR (P1)", "FORCED / selective", "math"),
        "arithmetic (E6/Q(sqrt-3), B288)":
            ("none (E6 lost on closing)", "ABSENT", "math (negative)"),
        "CP-sign law (B289)":
            ("CS(p,-q)=-CS(p,q), all 78 chiral; sign = Q(sqrt-3) Galois", "LAW forced / sign free", "math / HELD"),
        "SSB-gauge mechanism (B295)":
            ("sign external; Curie refuted, SSB potential absent, tau-gauged gated", "OPEN", "math / stop-gate"),
        "scale ladder (B290)":
            ("ell_C=2pi*i/n+...; n != k", "ladder math / n=k NEGATIVE", "math / HELD (G*Lambda)"),
        "scale-extremal (B291)":
            ("(5,1)=m003(-2,3) min volume; non-arithmetic", "selective (different axis)", "math"),
        "multiplicity (B292)":
            ("only fiber Sigma_{1,1} a 2-manifold; chiral datum absent", "tripartite; chiral ABSENT", "math / stop-gate"),
        "clock (B293)":
            ("peripheral symplectic conjugate pair (Goldman=NZ)", "STRUCTURE math / trajectory gated", "math / stop-gate"),
    }


def cross_axis_distinct():
    """The dynamical, arithmetic, and scale-extremal axes pick DIFFERENT (or no) closings -> axis-stratified."""
    dynamical = B287.DISTINGUISHED_SLOPE                 # 0  (non-hyperbolic, Sol)
    arithmetic_exists = B288.N_RESEEING_SQRT_NEG3 > 0    # False
    scale_extremal = B291.MIN_VOLUME_SLOPE               # (5,1)  (hyperbolic)
    # the dynamical closing (0,1) is non-hyperbolic; the scale-extremal (5,1) is hyperbolic; no arithmetic closing:
    return (dynamical == 0) and (not arithmetic_exists) and (scale_extremal == (5, 1))


# --- the net verdict ---
SELECTIVE_FOR_OWN_STRUCTURE = True                       # B287: canonical closing re-sees A=LR
CATALOGUE_FOR_SM_VALUES = True                           # E6 lost, CP sign external, scale gapped, chiral absent
SELECTION_IS_AXIS_STRATIFIED = True                      # different axes -> different closings
STRENGTHENS_FIREWALL = True
DERIVES_SM_VALUES = False


if __name__ == "__main__":
    print("=== THE SELECTION TABLE (seam arc B287-B293, B295) ===")
    for axis, (obj, verdict_, tier) in selection_table().items():
        print(f"  {axis}\n      -> {obj}\n         [{verdict_}; tier: {tier}]")
    print("\ncross-axis: dynamical/arithmetic/scale pick different (or no) closings:", cross_axis_distinct())
    print("\nSELECTIVE for own structure:", SELECTIVE_FOR_OWN_STRUCTURE,
          "| CATALOGUE for SM-values:", CATALOGUE_FOR_SM_VALUES)
    print("axis-stratified:", SELECTION_IS_AXIS_STRATIFIED, "| strengthens firewall:", STRENGTHENS_FIREWALL)
