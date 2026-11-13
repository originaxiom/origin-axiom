"""B1917's lock: the identity on the golden level recomputed; the kept runs hold all 601 with no NaN; Hecke at s = 2 as
kept; a planted half-width strip fails by exactly 2. It writes nothing."""
import sys, json, math, pathlib, io, contextlib, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import hecke_value as V
import hecke_s2 as H


def test_the_value_on_the_golden_level_recomputed():
    rows = V.run([("+LR", 2)])
    assert len(rows) == 4 and all(r["diff"] < 1e-12 and r["diff"] == r["diff"] for r in rows)


def test_the_kept_run_holds_all_601_with_no_nan():
    rows = json.loads((HERE / "hecke_value.json").read_text())
    assert len(rows) == 601
    assert all(r["diff"] == r["diff"] for r in rows) and max(r["diff"] for r in rows) < 1e-12


def test_hecke_at_two_as_kept_and_a_planted_half_strip_fails():
    rows = json.loads((HERE / "hecke_s2.json").read_text())
    assert len(rows) == 17 and sum(r["rel"] < 1e-7 for r in rows) == 16
    SL = H.B._sl()
    with contextlib.redirect_stdout(io.StringIO()):
        N, F, S = SL.exact_slopes(1, "LR", 2)
    M = H.B.abel_M(SL, 1, "LR", 2)
    L = H.lhs(M, (1 / N, 2 / N), Mmax=40, Nmax=1500)
    R, _ = H.rhs(M, 1, 2, N, X=4000.0)
    assert abs(L - H.H(2) * R) / abs(L) < 1e-5
    assert abs(L / (H.H(2) * R / 2) - 2) < 1e-4            # planted: half the orbit strip is off by exactly 2


def test_the_page_is_the_run():
    page = " ".join((HERE.parent / "FINDINGS.md").read_text(encoding="utf-8").split())
    run = (HERE / "kronecker_s1_run.txt").read_text()
    assert "-4 int log|g| = -3.097922" in run and "-3.09792 against -3.09774" in page.replace("−", "-")
    assert "2.5 × 10⁻¹³" in page and "601" in page
