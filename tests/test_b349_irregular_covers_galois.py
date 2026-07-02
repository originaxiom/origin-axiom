"""B349 lock -- gate A extension: irregular covers through index 6.

The cover census per index is a canonical multiset; the cyclic members reproduce B350's
coker(A^n - I) SNF exactly (independent-route cross-validation); and every within-index
invariant multiplicity collapses to a single isometry class -- the object never distinguishes
a member. CONDITIONAL per the C-guardrail (index <= 6 is a computational horizon); nothing to
CLAIMS.md. SnapPy-gated like the other SnapPy locks."""
import importlib.util
import pathlib

import pytest

snappy = pytest.importorskip("snappy")

_PATH = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
         / "B349_irregular_covers_galois" / "irregular_covers.py")
_spec = importlib.util.spec_from_file_location("b349", _PATH)
b349 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b349)


@pytest.fixture(scope="module")
def fig8():
    return snappy.Manifold("4_1")


def test_cyclic_covers_cross_validate_B350(fig8):
    for n, (torsion, betti_one, matches) in b349.cyclic_covers_match_B350(fig8, 6).items():
        assert betti_one, f"n={n}: cyclic cover betti != 1"
        assert matches, f"n={n}: SnapPy torsion {torsion} != B350 SNF"


def test_cover_census_is_the_banked_canonical_multiset(fig8):
    for k in (4, 5, 6):
        assert b349.cover_census(fig8, k) == b349.EXPECTED_CENSUS[k], f"index {k}"


def test_every_multiplicity_group_is_one_isometry_class(fig8):
    for k in (5, 6):
        res = b349.multiplicities_resolved_by_isometry(fig8, k)
        assert res, f"index {k}: expected at least one multiplicity group"
        for key, (size, n_classes) in res.items():
            assert size >= 2
            assert n_classes == 1, f"index {k} {key}: {size} covers in {n_classes} classes"
