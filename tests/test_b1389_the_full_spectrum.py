"""B1389 lock -- THE FULL SPECTRUM (kill test 2, sealed 8d9498d2; outcome MIXED).

Exact group theory on the record's own E6 vectors (B1368), under the frame's rule for a cuspidal Higgs class (spin-0 sector mu: index
sign(<H, mu>) N; doublets 0 by B1372 Lemma A):
- F27 passes: for Higgs directions H = aY + b gamma with -1 < a/b < 2/3 (the cone round gamma), the 27's spin-0 sector -- the 15 =
  10 + 5, the 5 at the opposite gamma-charge -- gives exactly one complete, SM-anomaly-free generation per unit N (the 5 enters as a
  5bar);
- F78, F27+78 and F133 fail in every cone: the 78's broken roots add an X,Y-type exotic (3,2)_{-5/6} whenever a != 0, and a lone 5bar
  at a = 0;
- the passing cone's U(1)_gamma mixed anomalies are universal (normalised SU(3)^2 gamma = SU(2)^2 gamma = 5/3)."""
import importlib.util
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1389_the_full_spectrum" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1389_full_spectrum", VER / "full_spectrum.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_banked_identity_and_controls():
    FS = _load()
    ok, _ = FS.banked_identity()
    assert ok


def test_the_27_frame_gives_whole_generations_round_gamma():
    FS = _load()
    for a, b in ((Fr(0), Fr(1)), (Fr(1, 2), Fr(1)), (Fr(-9, 10), Fr(1)), (Fr(0), Fr(-1))):
        st = FS.states_for("F27", (a, b))
        n, named = FS.generations(FS.content(st))
        assert abs(n) == 1 and FS.anomaly_free(FS.anomalies(st))
    for a, b in ((Fr(1), Fr(1)), (Fr(-2), Fr(1)), (Fr(1), Fr(0))):          # outside the cone: the 10 splits
        st = FS.states_for("F27", (a, b))
        assert FS.generations(FS.content(st))[0] is None and not FS.anomaly_free(FS.anomalies(st))
    g = FS.gamma_anomalies(FS.states_for("F27", (Fr(0), Fr(-1))))
    assert g["SU3^2 g"] / 28 == g["SU2^2 g"] and abs(g["SU2^2 g"]) == Fr(5, 3)   # universal (Tr_3 t^2 = 14 = 28 x 1/2)
    assert g["g Y^2"] * Fr(3, 5) == g["SU2^2 g"]                              # and with Y in SU(5) normalisation


def test_the_78s_broken_roots_spoil_every_frame():
    FS = _load()
    for frame in ("F78", "F27+78"):
        for kind, where, H in FS.cones_2d(frame):
            st = FS.states_for(frame, H)
            assert not (FS.anomaly_free(FS.anomalies(st)) and FS.generations(FS.content(st))[0] is not None), (frame, where)
    st = FS.states_for("F78", (Fr(0), Fr(1)))                               # pure gamma: the 78 gives a lone 5bar (L + d^c)
    n, named = FS.generations(FS.content(st))
    assert named == {"L": 1, "d^c": 1} and not FS.anomaly_free(FS.anomalies(st))


def test_the_parity_law_on_the_gamma_slice():
    """post-seal (FINDINGS section 7): with a = 0 the 78's gamma-charged roots give one 5bar (SU(5)^3 anomaly odd) and each 27-copy
    an even amount, so no frame containing the 78 is anomaly-free there -- checked on F27+78, F133 and E8's (27,3) + 78"""
    spec = importlib.util.spec_from_file_location("b1389_e8_frame", VER / "e8_frame.py")
    E8 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(E8)
    FS = E8.FS
    for st in (FS.states_for("F27+78", (Fr(0), Fr(1))), FS.states_for("F133", (Fr(0), Fr(1), Fr(1, 7))),
               E8.states_e8(Fr(0), Fr(1), (Fr(1, 5), Fr(-1, 3), Fr(2, 15))), E8.states_e8(Fr(0), Fr(-2), (Fr(3), Fr(-1), Fr(-2)))):
        A = E8.su5_anomaly(st)
        assert A.denominator == 1 and A.numerator % 2 == 1
