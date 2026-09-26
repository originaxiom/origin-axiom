"""B1380 lock -- THE PUNCTURE IS THE WORD'S.  The carrier axiom as P019 states it (the description realized as a mapping
class of a carrier whose fundamental group is F2) implies the puncture: no closed surface has fundamental group F2, and of the
four surfaces that do, only the once-punctured torus realizes the golden substitution.  F6's sibling (the closed torus bundle,
Sol) abelianizes the carrier's group -- the word replaced by its letter counts.  Orientation (sigma against sigma^2, Gieseking
against m004) is untouched."""
import importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1380_the_puncture_is_the_words" / "verification"
_spec = importlib.util.spec_from_file_location("b1380_puncture", VER / "puncture.py")
P = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P)


def test_sigma_is_an_automorphism_and_the_commutator_dichotomy():
    ok, M1, M2 = P.s1_automorphisms()
    assert ok and M1.det() == -1 and M2.det() == 1
    s1, s2, good, dets = P.s2_orientation()
    assert s1 == (True, False) and s2 == (True, False)          # sigma: [a,b] -> ~[a,b]^-1; sigma^2: [a,b] -> ~[a,b]
    assert good == 300 and dets[1] > 0 and dets[-1] > 0          # Nielsen's commutator theorem, instrument control


def test_no_closed_surface_has_group_F2():
    rows = P.s3_closed_surfaces()
    assert all("Z/2" in h for name, h, _ in rows if name.startswith("N_"))
    assert [name for name, h, _ in rows if h == "Z^2"] == ["S_1"]       # the torus: Z^2, abelian, not free


def test_only_the_once_punctured_torus_carries_sigma():
    found, classes = P.s4_the_four()
    assert len(found) == 4 and classes["S(1,1) once-punctured torus"] == [(0, 0)]
    no_root, verdict, controls = P.s5_realizability()
    assert no_root and controls == (True, True)
    assert [k for k, v in verdict.items() if v.startswith("sigma realizable")] == ["S(1,1) once-punctured torus"]


def test_the_word_against_its_letter_counts():
    rows, inject_F2, inject_Z2, nwords, nimages, freq = P.s6_word_against_shadow()
    assert all(p == n + 1 and q == 2 for n, p, q in rows) and len(rows) == 60
    assert inject_F2 and not inject_Z2 and (nwords, nimages) == (8190, 90)
    assert abs(freq - 2 / (1 + 5 ** 0.5)) < 1e-3


def test_the_three_siblings_in_snappy():
    out = P.s7_snappy()
    assert out["b++LR = m004"] and out["b-+L = m000"] and out["cover(m000) = m004"] and not out["m000 orientable"]
    assert out["m004(0,1)"][1] == "Z" and out["b1 = 1 fillings"] == [(0, 1)]
