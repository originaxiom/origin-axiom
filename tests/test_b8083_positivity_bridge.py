"""B8083 — the positivity bridge. Reads results.json; never prose."""
import json
import os

import pytest

RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "frontier", "B8083_positivity_bridge", "results.json")


@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)


def test_conjugacy_equals_cyclic_rotation_on_positive_words(r):
    """The bridge the block-sequence argument needs. If this fails, that proof is
    answering a coarser question than the one it was asked."""
    assert r["bridge_holds"] is True
    assert r["collisions"] == 0
    assert r["n_cyclic_classes"] == r["n_conjugacy_invariants"]


def test_the_check_is_exhaustive_and_nontrivial(r):
    assert r["max_length"] >= 10
    assert r["n_words"] > 2000
    assert r["n_cyclic_classes"] > 200


def test_trace_alone_is_not_the_invariant(r):
    """φ₁³ and φ₄ share trace 18 and are not conjugate — the paper says so, and this
    reproduces it with a different instrument. If trace sufficed, the bridge would be
    vacuous rather than proved."""
    assert r["trace18_pair_not_conjugate"] is True


def test_scope_excludes_GL2Z_and_non_positive_words(r):
    s = r["scope"]
    assert "POSITIVE words only" in s and "GL(2,Z)" in s
