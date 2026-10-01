"""B1435 lock -- the interaction census.

Sealed before any coupling was computed on a generation-shaped background. Live: the relative fundamental chain, the
product control with its bite, and the complete pipeline on the state that fires at its own level. Recorded: the eight
predictions as read from the sealed run, and the exact check.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1435_the_interaction_census"
V = ARC / "verification"
sys.path.insert(0, str(V))


def test_the_seal_is_the_file_that_was_sealed():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text()
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() in hashes
    for name in ("relcup.py", "interaction_census.py"):
        assert hashlib.sha256((V / name).read_bytes()).hexdigest() in hashes, f"{name} changed after the seal"


def test_the_relative_fundamental_chain_is_a_chain_identity():
    import interaction_census as ic
    from relcup import Bundle
    for eps, word, k in [(1, "LR", 1), (1, "LR", 3), (-1, "LR", 2), (-1, "LLRLR", 1), (1, "LLRR", 2)]:
        B = Bundle(ic.Phi_of(eps, word, k))
        C, z, sigma = B.fundamental()          # asserts d sigma = -[lam], dE = w, dC = z
        assert B.boundary(C) == z and B.boundary(z) == {} and len(z) == 2


def test_the_two_term_chain_is_not_a_relative_cycle():
    """the bite: the chain the web seat withdrew"""
    from relcup import Bundle, X, Y
    B = Bundle({X: (X,), Y: (Y,)})
    bad = B.norm({(B.F((X,)), B.F((Y,))): 1, (B.F((Y,)), B.F((X,))): -1})
    assert B.boundary(bad) == {(B.F((Y, X)),): 1, (B.F((X, Y)),): -1}
    assert B.boundary(bad) != {(B.F(B.lam),): -1}


def test_the_product_bundle_gives_plus_minus_one():
    from relcup import Bundle, Module, Cocycle, relative_lift, triple, X, Y
    p = 10007
    B = Bundle({X: (X,), Y: (Y,)})
    C, z, _ = B.fundamental()
    V1 = Module(B, [[1]], [[1]], [[1]], p)
    xs, ys, ts = Cocycle(V1, [1], [0], [0]), Cocycle(V1, [0], [1], [0]), Cocycle(V1, [0], [0], [1])
    T = lambda u, v, w: u[0] * v[0] * w[0] % p
    val = lambda a, b, h: triple(B, C, z, a, b, h, T, relative_lift(a))
    assert val(xs, ys, ts) in (1, p - 1)
    assert (val(xs, ys, ts) + val(ys, xs, ts)) % p == 0
    assert val(xs, xs, ts) == 0 and val(xs, ys, xs) == 0


def test_the_own_level_state_live():
    """-LLRLR at level one: eight backgrounds; the ten.ten couplings are non-zero and every coupling touching the
    five-bar vanishes, at three primes, symmetric in the two matter slots"""
    import interaction_census as ic
    lv = ic.run_level(-1, "LLRLR", 1, verbose=False)
    assert len(lv["backgrounds"]) == 8
    for row in lv["backgrounds"]:
        for name, r in row["pairs"].items():
            assert len(set(r["nonzero"])) == 1 and all(r["symmetric"]) and r["h1"] == [1, 1, 1]
            if r["allowed"]:
                assert r["nonzero"][0] == (name in ("Q.Q", "Q.uc", "uc.ec")), name


def test_the_predictions_as_read_from_the_sealed_run():
    r = json.loads((V / "interaction_census_summary.json").read_text())
    assert r["levels"] == 30 and r["backgrounds"] == 8800 and r["prime_disagreements"] == 0
    assert r["own_level_backgrounds"] == 24
    assert r["predictions"] == json.loads((V / "predictions_read.json").read_text())
    assert r["allowed_pairs_with_fibre_trivial_higgs"] == 0


def test_the_exact_check_agrees_with_the_three_primes():
    """Q(zeta_N), a second implementation, cell by cell, on the two own-level states and on the root's three-fold cover"""
    cols = {"Q.Q", "Q.uc", "Q.dc", "Q.L", "uc.ec", "uc.dc", "ec.L", "dc.dc", "dc.L", "L.L", "Q.nuc", "uc.nuc", "ec.nuc", "dc.nuc", "L.nuc"}
    for name, nb in (("mLLRLR_1", 8), ("mLLLRLR_1", 16), ("pLR_3", 48)):
        ex = json.loads((V / f"exact_{name}.json").read_text())
        pf = json.loads((V / f"couplings_{name}.json").read_text())
        assert len(ex["backgrounds"]) == nb == len(pf["backgrounds"])
        pfk = {json.dumps(b["key"]): b["pairs"] for b in pf["backgrounds"]}
        for b in ex["backgrounds"]:
            for pair, v in b["pairs"].items():
                assert pair in cols
                assert v[0] == pfk[json.dumps(b["key"])][pair][3], (name, pair)
