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


def test_one_unit_means_the_same_unit_on_three_lines_and_a_unit_on_one_line_gives_one():
    """2026-11-11 (raised by agy-002's second derivation; checked on main's own formula and numbers).  The record writes the
    cusp's twist as one integer n.  The cusp has three lines with distinct exponents, so there are three integers, and the
    index is their sum above its value at no unit.  What could fail: the exponents not being distinct (then a line would not
    be canonical); the index at no unit not being 0; the unit on all three lines not giving 3; or the formula's shift law
    failing on the one case where every dimension is classical."""
    import cmath
    import json as _json
    import math
    import pathlib as _pl
    root = _pl.Path(__file__).resolve().parents[1]
    w50 = _json.loads((root / "frontier" / "B1634_w50_on_main" / "verification" / "w50_on_main.json").read_text(encoding="utf-8"))
    ch = w50["V4"]["allowed_weights_chi"]
    assert abs(ch["1.5"]) < 1e-9                                        # no unit: the index is 0
    assert abs(ch["13.5"] - ch["1.5"] - 3) < 1e-9                       # the unit on all three lines is the cusp's divisor, weight + 12: 3
    b1634 = (root / "frontier" / "B1634_w50_on_main" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "T's exponents (⅛, ⅜, ⅞)" in b1634 and len({1, 3, 7}) == 3   # three distinct exponents: three canonical lines

    # the shift law, on the trivial character, where every dimension is classical: B1632's formula with d = 1
    def alpha(z):
        a = (cmath.phase(z) / (2 * math.pi)) % 1          # the exponent in [0, 1) ...
        return 0.0 if a > 1 - 1e-9 else a                 # ... a root of unity computed in floating point may sit a hair below 1

    def chi(k, shift=0):
        return 1 + k / 12 - alpha(cmath.exp(1j * math.pi * k / 2)) - alpha(1 / cmath.exp(1j * math.pi * k / 3)) - (0 - shift)

    classical = {0: 1, 4: 1, 6: 1, 8: 1, 10: 1, 12: 2, 14: 1, 16: 2}       # dim M_k of the full modular group
    for k, dim in classical.items():
        assert round(chi(k)) == dim, k
        assert round(chi(k, shift=1)) == classical.get(k + 12, dim + 1) == dim + 1     # one more order of pole on the one line: + 1
    # so on three lines the index above its value at no unit is m1 + m2 + m3
    index = lambda m: round(ch["1.5"]) + sum(m)
    assert index((1, 1, 1)) == 3 and index((1, 0, 0)) == 1 and index((0, 0, 1)) == 1 and index((0, 0, 0)) == 0
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8") if "ARC" in globals() else (root / "frontier" / "B1641_w46_on_main_and_the_two_objects" / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("A unit on one line, (1, 0, 0), gives 1.", "Main finds no such sentence"):
        assert s in f, s
    # CORRECTED the same evening: the note said the foundation left this unsaid and that main had not computed it.  Both were
    # wrong.  The foundation's row FK10 has the three-component form since version 1.59, and B1796 computed the dimensions
    # on main.  The lock now reads that computation and that row, and fails if the note loses its correction.
    run = (root / "frontier" / "B1796_the_cusp_unit_from_the_field_checked_on_main" / "verification" / "w123_check_run.txt").read_text(encoding="utf-8")
    import re as _re
    m = _re.search(r"d\(1,0,0\), d\(0,1,0\), d\(0,0,1\) = (\d+) (\d+) (\d+) \| uniform: d\(1,1,1\) = (\d+)", run)
    assert m and [int(x) for x in m.groups()] == [index((1, 0, 0)), index((0, 1, 0)), index((0, 0, 1)), index((1, 1, 1))]
    gen = (root / "GENESIS.md").read_text(encoding="utf-8")
    assert "The least datum on one eigenline gives one dimension" in gen and "the least uniform datum gives three" in gen and "uniform end data; and the least remainder" in gen
    assert "CORRECTED the same evening. This note was wrong about the foundation" in f

