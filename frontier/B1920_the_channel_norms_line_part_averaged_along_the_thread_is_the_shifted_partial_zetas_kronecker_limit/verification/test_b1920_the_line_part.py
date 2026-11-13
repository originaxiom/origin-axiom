"""B1920's lock: the kept runs say what the page says; the shifted Hecke formula recomputed at one shift; a planted
unshifted orbit sum fails. It writes nothing."""
import sys, pathlib, warnings, io, contextlib, re
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import hecke_shifted_s2 as HS


def test_the_kept_runs():
    run = (HERE / "hecke_shifted_s2_run.txt").read_text()
    rels = [float(x) for x in re.findall(r"rel ([0-9.e+-]+)", run)]
    assert len(rels) == 8 and max(rels) < 3e-6
    g = (HERE / "golden_average_run.txt").read_text()
    assert "<F_u> over the centred period: 8.906783" in g and "<F_u> over the centred period: 8.906779" in g


def test_the_shifted_formula_recomputed_and_a_plant_fails():
    SL = HS.H.B._sl()
    with contextlib.redirect_stdout(io.StringIO()):
        N, F, S = SL.exact_slopes(1, "LR", 2)
    M = HS.H.B.abel_M(SL, 1, "LR", 2)
    u = (0.2, 0.4)
    L = HS.lhs_shift(M, u, Mmax=120, Nmax=2000); R = HS.rhs_shift(M, u, X=4000.0)
    assert abs(L - HS.H.H(2) * R) / abs(L) < 5e-5
    R0 = HS.rhs_shift(M, (0.0, 0.0), X=4000.0)                 # planted: the unshifted lattice's orbit sum
    assert abs(L - HS.H.H(2) * R0) / abs(L) > 1e-2
