"""B1141 lock -- THE SPIN PAYMENT: the object's own beat selects the spin structure; the
freedom ledger's last free discrete bit is assigned, not free. Hostile-verified two-bench
(cloud memo 28 + this bench's own re-derivation: own relator search, own exact intertwiner
rank, own norm-form + chi-parity proofs; SnapPy + exact-symbolic + 50-digit-numeric).

Fast tests pin b1141_results.json (the three load-bearing claims + the two errata + the
relator census). The full re-derivation (~24s) re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1141_spin_payment"
RESULTS = ARC / "b1141_results.json"
FINDINGS = ARC / "FINDINGS.md"
VERIF = ARC / "verification"
REPO = Path(__file__).resolve().parents[1]


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- setup
def test_object_and_two_spin_structures():
    d = _load()
    assert d["snappy_H1"] == "Z"
    assert d["n_spin_structures"] == 2
    assert abs(d["snappy_volume"] - 2.0298832128) < 1e-6
    assert d["relator_holds_exactly"] is True
    # the two lifts (the spin structures): +I on the even signs, -I on the mixed
    c = d["relator_census"]
    assert c["R(A,B)"] == "+I" and c["R(-A,-B)"] == "+I"
    assert c["R(-A,B)"] == "-I" and c["R(A,-B)"] == "-I"


# ---------------------------------------------------------------- claim 1: the crux
def test_intertwiner_space_exactly_one_dimensional():
    d = _load()
    assert d["intertwiner_system_rank"] == 3
    assert d["intertwiner_space_dimension"] == 1          # every implementation is a scalar lambda*W0
    assert d["intertwiner_rank_numeric_crosscheck"] == 3  # 50-digit SVD agrees


# ---------------------------------------------------------------- claim 2: the twisted lift is impossible
def test_beat_closes_and_twisted_lift_impossible():
    d = _load()
    eqs = d["beat_closure_equations"]
    assert all(v is True for v in eqs.values())           # W0 closes every sign +
    assert d["N_positive_definite"] is True
    assert d["twisted_lift_shares_i_ii"] is True          # (i),(ii) cannot distinguish the lifts
    assert d["twisted_lift_square_unsatisfiable"] is True  # |lambda|^2 = -1 has no solution


# ---------------------------------------------------------------- claim 3: chi is beat-invariant
def test_chi_beat_invariant():
    d = _load()
    assert d["beat_word_lengths"] == {"beat_a": 1, "beat_b": 5}   # both odd
    assert d["chi_beat_invariance_spotcheck"] == "20/20"
    assert d["beat_respects_relator"] is True
    # a,b are the same meridian in H1 -> chi(a)=chi(b)
    assert d["H1_abelianized_relator"] == {"e_a": 1, "e_b": -1}


# ---------------------------------------------------------------- the two errata (caught + honest)
def test_errata_caught_nonloadbearing():
    d = _load()
    assert d["omega_minpoly_x2+x+1_holds"] is True        # correct minpoly
    assert d["omega_minpoly_x2-x+1_holds"] is False       # the brief/memo's stated one is wrong
    assert "erratum" in d["erratum_1"].lower() or "FALSE" in d["erratum_1"]
    assert "X^2-XY+Y^2" in d["N_XY_arithmetic_lattice"]   # not X^2+XY+Y^2
    assert d["verdict"].startswith("CONFIRMED")


# ---------------------------------------------------------------- the FINDINGS claims
def test_findings_states_the_selection_and_fences():
    t = FINDINGS.read_text(encoding="utf-8")
    assert "EXACTLY ONE" in t                             # the selection
    assert "assigned, not free" in t or "assigned" in t
    assert "NEEDS-CERT" in t                              # the honest scope
    assert "fermionic *kinematics*" in t or "not a fermion" in t.lower() or "unpaid verb" in t
    assert "SP-2" in t                                    # the live hinge


def test_findings_holds_the_spin_count_family_scope_clause():
    # cc3 B8132, verified this bench: the spin-structure COUNT (2) is family-level
    # (rank-1 + odd torsion), NOT a separating property of m004 -- the selection is untouched.
    t = FINDINGS.read_text(encoding="utf-8")
    assert "family fact, not m004" in t.lower() or "FAMILY fact" in t
    assert "Hom(H₁,ℤ/2)" in t or "kills ODD torsion" in t
    assert "NOT a refutation" in t                        # the selection stays object-level


# ---------------------------------------------------------------- reproduction present
def test_verification_present():
    assert (VERIF / "verify_spin_payment.py").exists()


# ---------------------------------------------------------------- full re-derivation (OA_SLOW, ~24s)
@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="full spin-payment re-derivation ~24s (SnapPy + symbolic + 50-digit); set OA_SLOW=1")
def test_spin_payment_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(VERIF / "verify_spin_payment.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=600)
    assert r.returncode == 0, r.stderr[-2000:]
    assert "CONFIRMED: the spin payment holds" in r.stdout
