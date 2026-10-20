"""B1672 -- the wordings-weave claims of 18 October, verified (NEGATIVE). Live: the two wording discrepancies are inner
automorphisms (free-group code), and, with the repo's own weave module, the puncture module L6 is REDUCIBLE under the
moves (commutant 2, group order 48) and irreducible only with the parity matrices added by hand (commutant 1, order
192) -- the received claim's failure, and the bite. Stored: RL^2R = P_a on W10's V with order 96; Gate 12 closes to
shear-word length 7 after the eta-twist (2 950 conflicts untwisted, 0 twisted)."""
import contextlib, importlib.util, io, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1672_discharging_triplet_index_gauge_frontier"


def _red(w):
    o = []
    for c in w:
        if o and o[-1] == c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)


def _apply(f, w):                                        # f applied to a word; capitals are inverses
    out = ""
    for c in w:
        img = f[c.lower()]
        out += img if c.islower() else "".join(x.swapcase() for x in reversed(img))
    return _red(out)


def _comp(f, g): return {k: _apply(f, g[k]) for k in "ab"}          # f after g


def test_the_wording_discrepancies_are_inner():
    Lab, Lba, Rab, Rba = {"a": "a", "b": "ab"}, {"a": "a", "b": "ba"}, {"a": "ab", "b": "b"}, {"a": "ba", "b": "b"}
    Lab_inv, Rba_inv = {"a": "a", "b": "Ab"}, {"a": "Ba", "b": "b"}
    assert _comp(Lab_inv, Lab) == {"a": "a", "b": "b"} and _comp(Rba_inv, Rba) == {"a": "a", "b": "b"}
    assert _comp(Lab_inv, Lba) == {"a": "a", "b": "Aba"}              # conj by a^-1
    assert _comp(Rba_inv, Rab) == {"a": "Bab", "b": "b"}              # conj by b^-1


def _weave():
    spec = importlib.util.spec_from_file_location("om", ROOT / "frontier" / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
    om = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(om)
    return om.W


def _commutant(gens):
    n = gens[0].shape[0]
    M = np.vstack([np.kron(g.T, np.eye(n)) - np.kron(np.eye(n), g) for g in gens])
    return int(sum(np.linalg.svd(M, compute_uv=False) < 1e-8))


def _order(gens, cap=500):
    seen = {tuple(np.round(np.eye(6), 5).flatten())}; frontier = [np.eye(6, dtype=complex)]
    while frontier and len(seen) <= cap:
        c = frontier.pop()
        for g in gens:
            n = c @ g; k = tuple((np.round(n, 5) + 0).flatten())
            if k not in seen: seen.add(k); frontier.append(n)
    return len(seen)


def test_L6_is_reducible_under_the_moves():
    W = _weave()
    def blocks(m, g):
        X = np.zeros((6, 6), dtype=complex)
        for i, u in enumerate(W.PAR):
            j = W.PAR.index(W.act_parity(m, u)); X[2 * i:2 * i + 2, 2 * j:2 * j + 2] = g
        return X
    TL, TR = blocks({"a": "a", "b": "ab"}, W.gL), blocks({"a": "ab", "b": "b"}, W.gR)
    Pa = np.diag([W.chi(p, "a") for p in W.PAR for _ in range(2)]).astype(complex)
    Pb = np.diag([W.chi(p, "b") for p in W.PAR for _ in range(2)]).astype(complex)
    assert (_commutant([TL, TR]), _order([TL, TR])) == (2, 48)          # reducible: the received "irreducible" fails
    assert (_commutant([TL, TR, Pa, Pb]), _order([TL, TR, Pa, Pb])) == (1, 192)   # only with the parity grading added
    w1 = TR @ TL @ TL @ TR
    assert not np.allclose(w1, Pa) and np.allclose(w1, np.diag(np.diag(w1)))


def test_stored_pieces_that_hold():
    mc = A / "verification" / "main_check"
    v1 = (mc / "v1_run.txt").read_text(); v3 = (mc / "v3_N7_run.txt").read_text()
    assert "RL2R==Pa True" in v1 and "LR2L==Pb True" in v1 and "order <ML,MR> = 96" in v1
    assert "commutant dim <ML,MR>: 2" in v1
    assert "N 7 (128661, 67284, 2950, 0, None)" in v3                    # Gate 12 to shear-word length 7
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "NEGATIVE"
