"""B1115 lock -- the spending DAG (a synthesis arc; the lock pins its
load-bearing structure and the falsifier, and that its computed facts cite B1114)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
F = " ".join((ROOT / "frontier/B1115_spending_order/FINDINGS.md")
             .read_text(encoding="utf-8").split())


def test_dag_nodes_present():
    for node in ("D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7"):
        assert node in F, f"DAG node {node} missing"


def test_fork_exclusivity_cites_b1114():
    assert "EXCLUSIVE by B1114" in F or "exclusivity is B1114" in F
    assert "electroweak sector" in F and "external" in F


def test_cosmological_falsifier_stated():
    assert "zero inversions" in F.lower() or "ZERO inversions" in F
    assert "Falsifier stated" in F or "falsifier" in F.lower()


def test_double_duty_and_fences():
    assert "(1,1)⊗1_c" in F
    assert "matter in the gauge reading" in F and "geometry" in F
    assert "no graviton dynamics claimed" in F.lower() or "Representation-level only" in F
