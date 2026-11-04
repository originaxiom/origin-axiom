"""Shared loader: MAIN's FR-FIB functions (B1656's four-channel frame as rebuilt in B1691's b1656_funcs), loaded through
main's own loader frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py::mods().
No agy-lane code is imported anywhere in these checks.

Conventions (declared): a line (a, b) means w = a*tau + b (B1726/B1742's compute convention; main's line_w is a*tau - b,
the same class up to b -> -b); twist_of(z, tau) = (Im z/Im tau, 2(Re z - a Re tau)), i.e. z = a tau + b'/2; sector charges
(6Y) up (1, -4), down (1, 2), leptons (-3, 6); channels s in {1, i, j, k}; residues by main's circle mean (rad 0.01, N 256);
regularised norm c_s by main's cA; channel weights u_s = sqrt(2 pi L + c_s) R_s; the Higgs matrix S = h0 QI + h1 QJ + h2 QK
(reading S); Y = coupling(S, weighted_M(u))."""
import contextlib, io, pathlib, sys, importlib.util

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
_CM = None


def cm():
    global _CM
    if _CM is None:
        p = ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py"
        sys.path.insert(0, str(p.parent))
        spec = importlib.util.spec_from_file_location("cm_zero_line_main", p)
        m = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
        _CM = m
    return _CM


def B():
    return cm().mods()["B"]


SECT = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
