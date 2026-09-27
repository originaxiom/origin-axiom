"""B1385 lock -- THE STATES TOGETHER: T1 no word state has a free cusp; T2 the swap is the mirror (amphichiral iff swap-symmetric up
to reversal); T3 the divide (the Q(sqrt-3) word states are the P-fixed +-(LR)^k, m010 is arithmetic over Q(sqrt-7), integral volume
ratios); L1 the Eisenstein cusp lemma (an order-3-symmetric hexagonal first shell is never annular: chi(d+) = +-1); L2 and the pilot on
o10_150725 (the rotation-invariant free class exists and is negated by the cusp's mirrors); L3 on ocube06_08812 (the first locally
open pair, closed by a cusp swap).  Word length 5 here; the run record has 8."""
import importlib.util
import math
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1385_the_states_together" / "verification"


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, VER / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S = _load("b1385_states_together", "states_together.py")
EP = _load("b1385_eisenstein_partition", "eisenstein_partition.py")

ROWS = S.census(5)


def test_no_word_state_has_a_free_cusp_and_the_swap_is_the_mirror():
    out = S.s1_no_free_cusp(ROWS)
    assert out["states"] == 26 and out["free cusps"] == 0
    out = S.s2_swap_is_mirror(ROWS, 5)
    assert out["criterion agrees with SnapPy"] == "26/26" and out["mirror pairs checked (w, swap w)"] == 20


def test_the_divide():
    out = S.s4_divide(ROWS)
    assert [w for w, _ in out["Q(sqrt-3) states (every shape in Q(omega))"]] == ["+LR", "-LR", "+LRLR", "-LRLR"]
    assert out["chiral states in m004's class"] == 0 and out["chiral states"] == 20
    arith = out["arithmetic states by discriminant"]
    assert ("-LLR", "m010", "chiral") in arith[-7] and ("+LLR", "m009", "chiral") in arith[-7]
    assert sorted(arith) == [-7, -4, -3]
    ratios = S.s3b_volume_ratios(ROWS)
    assert ratios["+LR"] == ("m004", -3, 12) and ratios["-LLR"] == ("m010", -7, 3) and ratios["+LLRR"] == ("m136", -4, 12)


def test_the_eisenstein_cusp_lemma():
    for deg in (0, 45, 100, 135, 180, -60):
        phi = math.radians(deg)
        c = EP.chi_positive(EP.symmetric_field(phi), 120)
        assert c == EP.morse_prediction(phi) and c in (1, -1)
    assert EP.chi_positive(lambda s, t: math.cos(2 * math.pi * s + 0.4), 90) == 0


def test_the_transfer_lemma_and_the_mirror_on_o10_150725():
    import snappy
    E = _load("b1385_eisenstein_cusps", "eisenstein_cusps.py")
    FM = E.StateMember(snappy.Manifold("o10_150725"), "o10_150725")
    rows = {r["cusp"]: r for r in E.eisenstein_analysis(FM)}          # asserts the transfer lemma on every rotation cusp
    for c in (0, 2):
        r = rows[c]
        assert r["rotation3"] and r["dimV"] == 1 and r["V_negated_by_one_fixer"] and not r["open"]
        assert "order-2 (det -1)*" in r["torus_types"]


def test_the_first_locally_open_pair_is_closed_by_the_swap():
    """ocube06_08812 (o10_150725's degree-3 cover no. 4): chiral; on cusps 0 and 2 the order-9 stabiliser fixes the class, B1370's
    instrument puts the leading allowed shell at |k|^2 = 1/3 (one rotation orbit: L1 gives N = -+1 at each), and every isometry
    swapping the two cusps negates the class -- L3, total index 0"""
    EC = _load("b1385_eisenstein_candidate", "eisenstein_candidate.py")
    out = EC.analyse()
    assert out["identify"] == "ocube06_08812" and out["isometries"] == 18 and out["amphichiral"] is False
    for c in (0, 2):
        row = out["cusps"][c]
        assert row["signs on the free class"] == [1] and row["rotations"] == 6
        nrm, ks, ndirs, dim = row["leading allowed shell"]
        assert abs(nrm - 1 / 3) < 1e-6 and len(ks) == 6 and ndirs == 3 and dim == 2
    assert out["cusps where it is cusp-fixed"] == [0, 2]
    negs = out["isometries negating it (cusp permutation, orientation)"]
    assert len(negs) == 9 and all(p[0] == 2 and p[2] == 0 and o == "preserving" for p, o in negs)
