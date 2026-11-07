"""B1855 -- the committed run: every counterexample verified, the S = {5} control above, Lemma A, the gapped corroboration."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_the_committed_run():
    t = (HERE / "charge_law_check_run.txt").read_text(encoding="utf-8")
    assert t.count("-> COUNTEREXAMPLE") == 6 and "premise True" in t
    assert "the control: above, as the proof says" in t
    assert "max difference 7.1e-18" in t and "none below (corroborates the proof)" in t
