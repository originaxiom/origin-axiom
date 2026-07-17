"""B657 — the invariant-line campaign locks (cc2 packet, verified on receipt).

W0a reproduced bit-identically on this machine; W0b identically up to
runtime_s; W2a re-run end-to-end here; W1's sealed matrix re-derived
with independent linear algebra. See
frontier/B657_invariant_line/FINDINGS.md.
"""
import json
import os

import sympy as sp

_PK = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B657_invariant_line", "packet")


def _load(*p):
    return json.load(open(os.path.join(_PK, *p)))


def test_w0a_conflation_refuted():
    d = _load("w0a_singlet", "w0a_v0.json")
    assert d["v0_support_indices"] == [12, 13, 14]
    assert [c for c in d["v0_coordinates_full"] if c != ["0", "0"]] == [
        ["1", "0"], ["-1", "0"], ["1", "0"]]
    assert d["v0_is_h_pr_null"] is True
    # both valid branchings: the GUT singlet sits at h_pr = +-16 and
    # v0's coefficient there is EXACTLY zero (v0 is h_pr-null)
    sing = d["decisive_numbers"]
    assert sorted(int(b["h_pr_eigenvalue_at_singlet"].strip("()"))
                  for b in sing) == [-16, 16]
    assert all(b["v0_coeff_at_singlet_zero"] is True for b in sing)
    assert d["verdict"] == "CONFLATION-REFUTED"


def test_w0b_one_per_block():
    d = _load("w0b_blocks", "w0b_blocks.json")
    assert d["block_dims"] == [17, 9, 1]
    assert d["block_diagonal_exact"] is True
    table = [(b["h0"], b["h1"]) for b in d["per_block"]]
    assert table == [(0, 1), (0, 1), (1, 1)]
    assert d["sum_h0"] == 1 and d["sum_h1"] == 3
    assert d["one_per_block"] is True


def _mat(d):
    s3 = sp.sqrt(-3)

    def parse(e):
        if isinstance(e, list) and len(e) == 2:
            return sp.Rational(e[0]) + sp.Rational(e[1]) * s3
        return sp.Rational(e)

    return sp.Matrix(5, 5, lambda i, j: parse(d["portal_matrix"][i][j]))


def test_w1_portal_rank5_block_diagonal():
    d = _load("w1_portal", "portal_matrix.json")
    M = _mat(d)
    assert M.rank() == 5 and sp.simplify(M.det()) != 0
    off = ([(i, j) for i in (0, 1) for j in (2, 3, 4)]
           + [(i, j) for i in (2, 3, 4) for j in (0, 1)])
    assert all(sp.simplify(M[i, j]) == 0 for i, j in off)
    assert M[4, 2] == 1 and M[2, 4] == -2
    assert M[3, 3] == sp.Rational(-15, 11)


def test_w2a_silver_form_match():
    d = _load("w2_silver", "silver_portal.json")
    assert d["rank"] == 5 and d["kernel_dim"] == 0
    assert all(v is True for v in d["gates"].values())
    assert d["v0_silver"]["support_size"] == 3
    table = [(b["h0"], b["h1"]) for b in d["w0b_analog"]["per_block"]]
    assert d["w0b_analog"]["block_dims"] == [17, 9, 1]
    assert table == [(0, 1), (0, 1), (1, 1)]
    assert d["rank_verdict"] == "RANK-5-ISOMORPHISM"
