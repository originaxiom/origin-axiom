"""B1641 -- W46 on main and the two objects.  Sealed instrument unchanged; the stored results; live: the central sign at
Delta^4 (the moves give -I on T; the geometric lift of conj(a b^-1 a^-1 b) gives +I), and the bite -- the record's lift of
conj(a) is not the identity on V (it is the parity signs)."""
import contextlib, hashlib, importlib.util, io, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1641_w46_on_main_and_the_two_objects"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 99975fb63")
    assert hashlib.sha256(open(A / "verification" / "w46_on_main.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "w46_on_main.json"))
    assert d["O1"]["a"]["record_is_plus_parity"] and d["O1"]["aBAb"]["record_is_minus_parity"]
    assert all(d["O1"][c]["geometric_is_identity"] for c in ("a", "b", "aBAb"))
    assert d["O2"]["moves_Delta4_on_T_is_minus_I"] and d["O2"]["geometric_conj_c_on_T_is_plus_I"]
    assert d["O3"]["T^2_invariant_dim"] == 3 and d["O3"]["T^3_invariant_dim"] == 6 and d["O3"]["c_uuu_over_24eta6_max_rel_err"] < 1e-20
    assert d["W1"]["exponents_rho6_T_in_eighths"] == [1, 1, 3, 5, 7, 7] and d["W1"]["piece_dims"] == [2, 4]
    assert all(v["all_match"] for v in d["W3"].values())
    assert all(sum(len(x) for r in v.values() for x in r.values()) == 0 for v in d["H"].values())
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def _om():
    spec = importlib.util.spec_from_file_location("om", ROOT / "frontier" / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
    om = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(om)
    return om


def test_the_central_sign_live_and_its_bite():
    om = _om(); W, cp = om.W, om.cp
    inv = np.linalg.inv
    T3 = lambda M: cp.restrict(M, cp.TB)
    MD = W.ML @ inv(W.MR) @ W.ML
    assert np.allclose(T3(np.linalg.matrix_power(MD, 4)), -np.eye(3), atol=1e-9)          # the moves: -I on T
    def blockwise(m, c):
        Mx = np.zeros((6, 6), dtype=complex)
        for ip, p in enumerate(W.PAR):
            q = W.act_parity(m, p); iq = W.PAR.index(q)
            bp, _ = W.BASES[p]; bq, Pq = W.BASES[q]
            gi = inv(W.rep(c, p))
            for k in range(2):
                z = {"a": bp[:2, k], "b": bp[2:, k]}
                w = np.concatenate([gi @ W.cocycle_value(z, m["a"], p), gi @ W.cocycle_value(z, m["b"], p)])
                Mx[2 * iq:2 * iq + 2, 2 * ip + k] = bq.conj().T @ (Pq @ w)
        return Mx
    conj = lambda c: {x: om.red(c + x + om.inv(c)) for x in "ab"}
    assert np.allclose(T3(blockwise(conj("aBAb"), "aBAb")), np.eye(3), atol=1e-9)        # the geometric lift: +I
    rec = W.move_matrix(conj("a"), om.lift_of(conj("a")))
    assert not np.allclose(rec, np.eye(6), atol=1e-6)                                       # bite: the record's lift is not trivial


def test_post_seal_rho_T_S_squared_is_i():
    """B1641 2b (post-seal, labelled): rho_T(S)^2 = i I on main's rho_T, the scalar W56's parity argument rests on."""
    om = _om(); W, cp = om.W, om.cp
    inv = np.linalg.inv
    T3 = lambda M: cp.restrict(M, cp.TB)
    rS = inv(T3(W.MR @ inv(W.ML) @ W.MR))
    assert np.allclose(rS @ rS, 1j * np.eye(3), atol=1e-9)
    assert not np.allclose(rS @ rS, -1j * np.eye(3), atol=1e-6)                             # bite: not the conjugate's scalar

