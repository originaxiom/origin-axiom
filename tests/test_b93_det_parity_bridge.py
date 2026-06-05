"""B93 (Paper 0, Phase C) -- locking tests: det=-1 <=> the tower's parity (MyCalc-1), and the parity
involution (m->-m) is distinct from the field Galois involution (MyCalc-4)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b93", _ROOT / "frontier" / "B93_det_parity_bridge" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_mycalc1_det_minus1_iff_negative_eigenvalue():
    """det N = -1 <=> N has a negative eigenvalue (-1/lambda) <=> the parity sectors char(-N^k) exist;
    det N = +1 => both eigenvalues positive => no sign sectors."""
    Ns = {"M1": [[1, 1], [1, 0]], "M2": [[2, 1], [1, 0]],
          "M1sq": [[2, 1], [1, 1]], "N32": [[3, 2], [1, 1]]}
    out = B.mycalc1_det_iff_parity(Ns)
    for name, (det, evs, has_neg, ok) in out.items():
        assert ok is True                         # has-negative-eigenvalue == (det == -1)
    assert out["M1"][2] is True and out["M1sq"][2] is False   # det=-1 negative; det=+1 not


def test_mycalc4_parity_is_not_galois():
    """Parity P (m->-m): L_k(-m)=(-1)^k L_k (permutes char(M^k)<->char(-M^k)). Galois (sqrt->-sqrt):
    FIXES every L_k (within-factor root swap). They are distinct involutions."""
    par = B.parity_action_on_Lk(4)
    gal = B.galois_fixes_Lk(4)
    assert all(par.values())                      # parity acts by (-1)^k on L_k
    assert all(gal.values())                      # Galois fixes every L_k
    # distinctness: parity is non-trivial on odd k (L_k(-m) != L_k), Galois is trivial on L_k -> different
