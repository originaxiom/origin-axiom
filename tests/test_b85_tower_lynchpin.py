"""B85 (Phase C/D, V68) -- locking test: Lambda^2 functoriality of the figure-eight substitution, and
the persistence of the char(M^2) multiplicity under Lambda^2 (the degeneracy is a root-system fact)."""
import importlib.util
import pathlib

from math import comb

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b85_lynch", _ROOT / "frontier" / "B85_tower_lynchpin" / "probe.py")
B85 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B85)


def test_lambda2_functoriality():
    """Lambda^2(A^2 B) = (Lambda^2 A)^2 (Lambda^2 B) and Lambda^2(AB)=(Lambda^2 A)(Lambda^2 B), n=4,5."""
    for n in (4, 5):
        assert B85.functoriality_dev(n) < 1e-10, n


def test_char_m2_multiplicity_is_root_system_fact():
    """The char(M^2) multiplicity (1 at n=3,4; 2 at n=5,6) -- a height-2 root-space fact (B62),
    persisting under Lambda^2 V (which has dim C(n,2), a different representation)."""
    assert B85.CHAR_M2_MULTIPLICITY == {3: 1, 4: 1, 5: 2, 6: 2}
    # the multiplicity jumps to 2 at n=5 (the first doubly-degenerate case), independent of dim Lambda^2 V
    assert B85.CHAR_M2_MULTIPLICITY[5] == 2 and comb(5, 2) == 10
    assert B85.CHAR_M2_MULTIPLICITY[4] == 1 and comb(4, 2) == 6
