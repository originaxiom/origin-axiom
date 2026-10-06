"""B1509 lock -- THE JOIN ON THE PROJECTIVE VACUUM (2026-10-01).  The minimal non-split SU(5) extension of the audit lane's harmonic
vacuum (Ballas' projective holonomy of m004 with a central twist, at the four exceptional backgrounds) carries main's index: -1 / +1 at
q = 17 +- 12 sqrt2 (mu = -1), 0 at q = 7 +- 4 sqrt3 (mu = +-i), and the 5bar' sector (Lambda^2) is vector-like everywhere.  Locked
here: the index (live mod p at all six points, live exact at two), the double root and the fibre monodromy's Jordan block, every end
condition's count, the family classification's inputs, R41's balance on this flag, the records, and the findings' load-bearing
sentences.  The full exact run, the symbolic fibre check and the pre-seal control are marked slow."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1509_the_join_on_the_projective_vacuum"
VER = ARC / "verification"


def _load(name):
    spec = importlib.util.spec_from_file_location(f"b1509_{name}", VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _record(name):
    return json.loads((VER / f"{name}_run.txt").read_text(encoding="utf-8"))


def test_the_index_mod_p_live():
    """index_lib over GF(1009), GF(1033), GF(1129), both square-root choices (its own identity checks run inside): I(W1) = -1 and
    I(W2) = +1 at mu = -1; 0 at +-i; I(Lambda^2 W1) = I(Lambda^2 W2) = 0 and h1(A) = h1(A*) = 1 everywhere"""
    rows = _load("extension_index").modp_run()
    assert len(rows) == 18
    for r in rows:
        assert (r["h1(A)"], r["h1(A*)"], r["I(L2W1)"], r["I(L2W2)"]) == (1, 1, 0, 0)
        assert (r["I(W1)"], r["I(W2)"]) == ((-1, 1) if r["mu"] == "-1" else (0, 0))


def test_the_index_exact_live():
    """exact over Q(sqrt2, sqrt3, i): at (17 - 12 sqrt2, -1) W1 has (a0, a1, t0, r1) = (0, 1, 1, 1), W1* (1, 2, 1, 1), I(W1) = -1,
    I(W2) = +1, so N(10') = 1, N(5bar') = 0; at (7 - 4 sqrt3, i) the index is 0 (q1 = 2); the block's U(1)_T charge is 5"""
    import sympy as sp
    E = _load("extension_index")
    a = E.exact_point(17 - 12 * sp.sqrt(2), -1)
    assert (a["I(W1)"], a["I(W2) = -I(W1[A*])"], a["I(Lambda2 W1)"], a["I(Lambda2 W2) = -I(Lambda2 W1[A*])"]) == (-1, 1, 0, 0)
    assert tuple(a["W1 data (a0,a1,t0,r1)"]) == (0, 1, 1, 1) and tuple(a["W1* data"]) == (1, 2, 1, 1)
    assert (a["N(10') = -I(W1)"], a["N(5bar') = -I(Lambda2 W1)"], a["U(1)_T charge of the extension block"]) == (1, 0, 5)
    b = E.exact_point(7 - 4 * sp.sqrt(3), sp.I)
    assert (b["I(W1)"], b["I(W2) = -I(W1[A*])"], b["I(Lambda2 W1)"]) == (0, 0, 0)
    assert tuple(b["W1 data (a0,a1,t0,r1)"]) == (0, 0, 1, 0) and tuple(b["W1* data"]) == (1, 2, 1, 2)


def test_the_double_root_and_the_jordan_block_live():
    """T3: mu is a double root of the palindromic Q at the mu = -1 points and simple at +-i; on the fibre the monodromy S_A has a
    Jordan block of size exactly two at eigenvalue 1 at mu = -1 and none at +-i; generic q = 2 has no eigenvalue 1"""
    import sympy as sp
    mult = [r["multiplicity_of_mu_in_Q"] for r in _load("extension_index").multiplicities()]
    assert mult == [2, 2, 1, 1, 1, 1]
    W = _load("wang_monodromy")
    j = W.jordan_at_point(17 + 12 * sp.sqrt(2), -1)
    assert j == {"h0(F;A)": 0, "dim ker(S_A-1) on H1(F;A)": 1, "dim ker(S_A-1)^2": 2, "dim ker(S_A-1)^3": 2}
    k = W.jordan_at_point(7 + 4 * sp.sqrt(3), -sp.I)
    assert (k["dim ker(S_A-1) on H1(F;A)"], k["dim ker(S_A-1)^2"]) == (1, 1)
    assert W.jordan_at_point(sp.Integer(2), -1)["dim ker(S_A-1) on H1(F;A)"] == 0
    rw, lev = W.rs_rewrite(W.WORD_R)
    assert rw == [(1, 1), (0, -1), (0, -1), (-1, 1), (0, -1)] and lev == 0


def test_every_end_condition_live():
    """Proposition E on W1: N_W = dim W - 2 at all six points (formula matches the run's data); the 10' count over all end
    conditions is {0, 1, 2}; the interior choice dim W = q1 gives -1 at mu = -1 and 0 at +-i"""
    rows = _load("end_conditions").main()
    assert len(rows) == 6
    for r in rows:
        assert r["N_W by dim W"] == {0: -2, 1: -1, 2: 0} and r["formula_matches"]
        assert r["10' count = -N_W, over all end conditions"] == [0, 1, 2]
        interior = [v for key, v in r.items() if key.startswith("interior")][0]
        assert interior == (-1 if r["mu"] == "-1" else 0)


def test_the_family_classification_inputs_live():
    """Corollary C's inputs: Q(q, 1) = (q - 1)^2; Q(q, -1) = q^2 - 34 q + 1 and Q(q, +-i) = -(q^2 - 14 q + 1), positive roots
    17 +- 12 sqrt2 and 7 +- 4 sqrt3; the record has H^0(F; rho_q) = H^0(F; rho_q*) = 0 for every q > 0"""
    F = _load("family_classification")
    t = F.q_at_twists()
    assert t["1"] == {"Q(q, mu)": "(q - 1)**2", "positive_roots_q_not_1": []}
    assert t["-1"]["Q(q, mu)"] == "q**2 - 34*q + 1" and sorted(t["-1"]["positive_roots_q_not_1"]) == ["12*sqrt(2) + 17", "17 - 12*sqrt(2)"]
    assert t["i"] == t["-i"] and sorted(t["i"]["positive_roots_q_not_1"]) == ["4*sqrt(3) + 7", "7 - 4*sqrt(3)"]
    rec = _record("family_classification")
    assert rec["H0(F; rho_q)"]["gcd_of_numerators"] == "1" and rec["H0(F; rho_q)"]["nonzero_maximal_minors"] == 70
    assert rec["H0(F; rho_q*)"]["gcd_of_numerators"] == "q**2 + q + 1" and rec["H0(F; rho_q*)"]["positive_roots_other_than_1"] == []


def test_the_balance_on_this_flag_live():
    """R41's balance read on the 4 c 5 flag: xi = 5P - 4 = T; the local identity tr(Psi [omega_A, xi]) = -(5/2)|b|^2 (rank five)
    and its rank-four control -2|eta|^2; R41's table for R40's flags reproduced; this flag pairs T -> 20, U -> 0, [E04, E04^+] -> 5"""
    B = _load("balance_transpose")
    assert B.local_identity(5, 4) and all(B.local_identity(4, k) for k in (1, 2, 3))
    p = B.pairings()
    assert p["xi_for_4_in_5_equals_T"] and p["R41_table_reproduced"] and p["T_charge_of_E04"] == 5
    assert p["this_flag"] == {"T": 20, "U": 0, "-U": 0, "[E04,E04^+]": 5}
    rec = _record("balance_transpose")
    assert [r["dim_algebra_generated_by_A"] for r in rec["irreducible_at_points"]] == [16] * 6


def test_the_records():
    """the recorded runs: all six points agree exact and mod three primes; the fibre check's symbolic facts; the control's
    reproduction; the pre-repair output differs from the record in the rank-four control only"""
    run = _record("extension_index")
    assert len(run["exact"]) == 6 and len(run["mod_p"]) == 18
    assert sorted(r["I(W1)"] for r in run["exact"]) == [-1, -1, 0, 0, 0, 0]
    assert all(r["U(1)_T charge of the extension block"] == 5 for r in run["exact"])
    w = _record("wang_monodromy")
    s = w["symbolic"]
    assert s["charpoly_on_H1(F;rho_q)_equals_monic_Q"] and s["S_on_B1_equals_A(m)^-1"]
    assert s["phi_relation_u2=u1_u0^-1_u1^2_in_rho_q"] and s["relator_rewrite_u1_u0^-2_u-1_u0^-1"]
    assert all(p["block_iff_a1(W1)=1"] for p in w["exceptional_points"])
    c = _record("control_exceptional")
    assert c["relator_holds"] and c["longitude_charpoly_is_(X-q)^3(X-q^-3)"]
    pre = json.loads((VER / "balance_transpose_prerepair_run.txt").read_text(encoding="utf-8"))
    post = _record("balance_transpose")
    assert pre["local_identity_rank4_flags_control(R41)"] is False and post["local_identity_rank4_flags_control(R41)"] is True
    pre.pop("local_identity_rank4_flags_control(R41)")
    post.pop("local_identity_rank4_flags_control(R41)")
    assert pre == post


@pytest.mark.slow
def test_the_full_exact_run_reproduces_the_record():
    """extension_index.main() equals the committed record (exact route, three primes, multiplicities)"""
    res = _load("extension_index").main()
    assert json.loads(json.dumps(res, sort_keys=True, default=str)) == _record("extension_index")


@pytest.mark.slow
def test_the_fibre_check_and_the_control_reproduce():
    """wang_monodromy's symbolic checks and the pre-seal control reproduce their records"""
    W = _load("wang_monodromy")
    assert W.checks_symbolic() == _record("wang_monodromy")["symbolic"]
    C = _load("control_exceptional")
    assert json.loads(json.dumps(C.main(), sort_keys=True, default=str)) == _record("control_exceptional")


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED, declares its law (corrected 2026-10-02), keeps 0 of 19; the findings carry the theorems, the
    table, the disclosures and the reading; the predictions file is unchanged since its commit"""
    import hashlib
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1509" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["instrument"] is False
    cl = v["creates_law_corrected"]
    assert (cl["date"], cl["was"], cl["registry_row"]) == ("2026-10-02", False, "T-PROJECTIVE-JOIN")
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**T1 (the matter is boundary-acyclic).**", "**T2 (the extension's index).**", "**T3 (when e ∪ c vanishes).**",
                   "**Proposition E (every end condition).**", "**Corollary C (the rank-five extensions of the family).**",
                   "I(W₁) = (0 − 1) + 1 − r1 = −r1", "| D1 | I(W₁) = −1 at (17 ± 12√2, −1) | **holds**",
                   "The control's slip.", "balance_transpose_prerepair_run.txt", "AUD NEUTRAL_CENSUS.md:7, :52",
                   "AUD CURRENT_BALANCE.md:92–96", "**T → 20, U → 0**", "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    assert term not in f.lower() and term not in v["claim_one_line"].lower()
    sha = hashlib.sha256((ARC / "PREDICTIONS.md").read_bytes()).hexdigest()
    assert sha == "1c34a70c9da368645811cee52f0f2988e7c88085f65f64b61690d6bb694bcf5a"
