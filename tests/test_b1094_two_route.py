"""B1094 lock: the two-route wall + hatch on the kill graph."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_kill_node_carries_two_route_and_hatch():
    kg = json.load(open(ROOT / "frontier/B738_pathfinder_compiler/kill_graph.json"))
    nodes = kg["nodes"] if isinstance(kg, dict) and "nodes" in kg else kg
    node = next(n for n in nodes if n["id"] == "B1094")
    assert "two step-disjoint proofs" in node["kill_form"]
    assert "NON-ABELIAN holonomy" in node["hatch"]
    assert "B955" in node["faces_consulted"] and "B1079" in node["faces_consulted"]

def test_census_source_exists():
    v = json.load(open(next((ROOT / "frontier").glob("B1079_*")) / "arc_verdict.json"))
    assert "15,624" in v["claim_one_line"] or "15624" in v["claim_one_line"]
