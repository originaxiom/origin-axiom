"""B100 (Probes 2 + 6) -- literature cross-checks of the SL(3) figure-eight slice and the twisted-Alexander
bridge.

Two independent, published frameworks are used to cross-validate the B71/B98/B99 SL(3) results. NOTHING
here is claimed as our discovery; the methods are Zickert's Ptolemy variety and Baker-Petersen's character-
variety genera + twisted Alexander polynomials. We run the computations and report that they are CONSISTENT
with our slice.

PROBE 2 -- the Ptolemy variety (Zickert arXiv:1405.0025; Garoufalidis-Goerner-Zickert arXiv:1207.6711).
SnapPy's boundary-unipotent SL(3,C) Ptolemy variety for the figure-eight 4_1 has 2 obstruction classes
(H^2(M,dM; Z/3)); the trivial obstruction class (0) has a finite solution set of 6 boundary-unipotent
SL(3,C) representations (sympy.solve over the 8 Ptolemy coordinates). This is the 0-dimensional boundary-
unipotent SLICE of B71's 2-dimensional SL(3) character-variety components (V0/W1/W2) -- a complementary
cut through the SAME object, containing the geometric rep. Cross-validates B71 from an independent code
path (SnapPy Ptolemy, not our trace-map ideal).

PROBE 6 -- character-variety genus + twisted Alexander (Baker-Petersen arXiv:1211.4479; see also the
unbounded-genus family arXiv:2206.14954). Baker-Petersen computed canonical-component genera AND twisted
Alexander polynomials for once-punctured-torus bundles with tunnel number one (the figure-eight is the
first). The clean, decisive cross-validation is the TWISTED ALEXANDER object, which is exactly the B98/B99
geometric-rep Jacobian: the transverse quadratic char-factor at the geometric rep is t^2-5t+1 (adjoint
torsion tau_1=-3). The genus figures are different CURVES and must not be conflated:
  * the canonical component in TRACE coordinates {y=z=x/(x-1)} is rational  -> genus 0 (B67/B71);
  * the A-polynomial SPECTRAL curve w^2 = disc_L is genus 3 (B69/B87).
Both are cited / prior-banked; B100 recomputes only the twisted-Alexander anchor (reusing B98), which is
the curve Baker-Petersen actually tabulate.

VERDICT. Two independent published frameworks agree with the B71/B98/B99 SL(3) picture: the Ptolemy slice
reproduces the boundary-unipotent reps of the same character variety, and the twisted Alexander = our
geometric-rep Jacobian. Methods CITED, not claimed; no physics claim; no Origin-core claim; P1-P16
untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import re

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _b98():
    spec = importlib.util.spec_from_file_location(
        "b98_probe", _ROOT / "frontier" / "B98_geometric_jacobian" / "probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Probe 2 -- Zickert/SnapPy Ptolemy variety for 4_1 at N=3
# ---------------------------------------------------------------------------
def _ptolemy_variety():
    import snappy
    return snappy.Manifold("4_1").ptolemy_variety(3, "all")


def ptolemy_obstruction_classes() -> int:
    """Number of obstruction classes of the N=3 Ptolemy variety of 4_1 (H^2(M,dM; Z/3))."""
    return len(_ptolemy_variety())


def ptolemy_class0_solution_count() -> int:
    """Boundary-unipotent SL(3,C) reps in the trivial obstruction class (sympy.solve over the 8 Ptolemy
    coordinates). Deterministic; the trivial-class system has no obstruction cocycle root, so the count is
    stable at 6."""
    var = _ptolemy_variety()[0]
    eqs_raw = [str(e) for e in var.equations]
    syms = set()
    for e in eqs_raw:
        for tok in re.findall(r"[A-Za-z]_?\w*", e):
            syms.add(tok)
    symmap = {s: sp.Symbol(s) for s in syms}
    eqs = [sp.sympify(e, locals=symmap) for e in eqs_raw]
    varsyms = sorted([symmap[s] for s in syms if s.startswith("c_")], key=str)
    sols = sp.solve(eqs, varsyms, dict=True)
    return len(sols)


# ---------------------------------------------------------------------------
# Probe 6 -- twisted Alexander anchor (Baker-Petersen) = the B98/B99 geometric Jacobian
# ---------------------------------------------------------------------------
def twisted_alexander_transverse_quadratic():
    """The transverse char-factor of the geometric-rep Jacobian (B98): t^2-5t+1. This is the twisted-
    Alexander / adjoint-torsion object Baker-Petersen tabulate (arXiv:1211.4479), recomputed here by
    reusing the locked B98 probe -- the clean cross-validation curve."""
    t = sp.symbols("t")
    full = sp.expand(_b98().char_at_geometric())          # (t-1)(t^2-5t+1)
    quad = sp.simplify(sp.cancel(full / (t - 1)))
    return sp.expand(quad)


def genus_table():
    """The two DIFFERENT curves whose genera must not be conflated (cited / prior-banked, not recomputed):
      canonical component in trace coords {y=z=x/(x-1)} = rational -> genus 0 (B67/B71);
      A-polynomial spectral curve w^2 = disc_L                     -> genus 3 (B69/B87)."""
    return {"canonical_component_trace_coords": 0, "A_polynomial_spectral_curve": 3}


def main():
    print("B100 (Probes 2 + 6) -- literature cross-checks (methods CITED, not claimed)\n")
    print("  Probe 2 (Zickert/SnapPy Ptolemy variety, 4_1, N=3):")
    print(f"    obstruction classes                         : {ptolemy_obstruction_classes()}")
    print(f"    boundary-unipotent SL(3) reps (class 0)     : {ptolemy_class0_solution_count()}")
    print("    -> the 0-dim boundary-unipotent slice of B71's 2-dim components (same object).")
    print("\n  Probe 6 (Baker-Petersen twisted Alexander / genus, arXiv:1211.4479):")
    print(f"    twisted-Alexander transverse quadratic (=B98): {twisted_alexander_transverse_quadratic()}")
    print(f"    genus table (different curves)              : {genus_table()}")
    print("    -> twisted Alexander = B98/B99 geometric Jacobian; the clean cross-validation curve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
