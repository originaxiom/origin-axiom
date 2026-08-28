"""Lock: the mirror involution IS the Galois generator c, re-derived inside the test."""
import json, pathlib, sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8154_mirror_is_c/results.json").read_text())

def test_the_identification_re_derived_here():
    t = sp.Rational(1, 2) - sp.sqrt(-3) / 2
    assert sp.simplify(t**2 - (t - 1)) == 0            # t = zeta_6
    w = sp.simplify(t**2)
    assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0   # omega primitive cube root
    assert sp.simplify(w**2 + w + 1) == 0              # Phi3(omega) = 0
    assert sp.simplify(w**2 - sp.conjugate(w)) == 0    # the swap IS conjugation

def test_the_control_distinguishes_maps():
    t = sp.Rational(1, 2) - sp.sqrt(-3) / 2
    w = sp.simplify(t**2)
    assert sp.simplify(w**3 - w) != 0                  # u -> u^3 is not the swap

def test_all_five_links_are_recorded():
    assert len(R["the_five_links"]) == 5

def test_scope_keeps_B1200_faces_cited_not_claimed():
    assert "CITED and NOT re-derived" in R["scope"]
    assert any("are cited" in x for x in R["not_claimed"])

def test_it_claims_no_residue_closure():
    assert any("does not supply the missing marking" in x for x in R["not_claimed"])
