"""B1391 lock -- THE GENERATIONS' FLAVOUR (test 4, structural).

The frame's generations are a virtual representation of the isometries fixing the Higgs class, with character the Lefschetz number
of the pair (M_T, d+M_T).  On cube~3.24: L(e) = 2, L(R) = 3 - 4 = -1, L(swap) = 4 - 4 = 0, i.e. D3's doublet E.  With a Higgs in a
one-dimensional representation the covariant Yukawa forms on E have one singular value twice (degenerate generations); for the
pullback three (Z/3's regular representation) every symmetric texture with a Higgs of definite charge has a degenerate pair (B1362's
circulant)."""
import importlib.util
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1391_the_generations_flavour" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1391_flavour", VER / "flavour.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_generations_are_the_doublet_of_D3():
    F = _load()
    table, chi, dec = F.equivariant_index()
    assert chi == (2, -1, 0) and dec == {"A1": 0, "A2": 0, "E": 1}
    assert sorted(t[2] for t in table) == [-1, -1, 0, 0, 0, 2]


def test_the_symmetric_point_is_degenerate():
    F = _load()
    E = F.yukawa_E()
    assert len(E["A1"][1]) == 1 and len(E["A2"][1]) == 1          # one singular value, twice
    assert E["A1"][2] and not E["A2"][2]                             # 10 10 5_H needs the Higgs in A1
    for q, (Ysym, ev, nfree) in F.yukawa_regular().items():
        assert sorted(ev.values()) == [1, 2] and nfree == 3          # a degenerate pair; the 10 5bar texture is a permutation


def test_the_character_arithmetic():
    F = _load()
    assert F.decompose((2, -1, 0)) == {"A1": 0, "A2": 0, "E": 1}
    assert F.decompose((3, 0, 1)) == {"A1": 1, "A2": 0, "E": 1}      # S3's "2 + 1": a singlet and the doublet
    assert F.decompose((6, 0, 0)) == {"A1": 1, "A2": 1, "E": 2}      # the regular representation of S3
