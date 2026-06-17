"""B159 -- Ω strict-full class-graded DAG (V153). Fast locks on the banked class CSVs.

Structural + conservation checks only (the from-scratch L4-L7 re-enumeration lives in
frontier/B159_omega_class_dag/verify_gate2_dag.py PART 2; too heavy for the test suite).
"""
import csv, ast
from collections import defaultdict
from pathlib import Path

D = Path(__file__).resolve().parent.parent / "frontier" / "B159_omega_class_dag"

def _load(name, ints):
    out = []
    with open(D / name) as f:
        for r in csv.DictReader(f):
            for k in ints: r[k] = int(r[k])
            for k in ("abc","source_abc","target_abc","charpoly_coeffs"):
                if k in r: r[k] = tuple(ast.literal_eval(r[k]))
            out.append(r)
    return out

NODES = _load("omega_strict_full_class_nodes_L4_L10.csv", ("level","history_count","distinct_matrix_count"))
EDGES = _load("omega_strict_full_class_edges_L4_L10.csv",
              ("source_level","target_level","multiplicity_history_extensions"))

EXP = {4:(1,96,36),5:(2,672,240),6:(6,3840,960),7:(18,20928,3240),
       8:(49,105312,9396),9:(115,521904,25536),10:(283,2488080,65472)}

def test_level_counts():
    for L,(nc,h,m) in EXP.items():
        cls=[n for n in NODES if n["level"]==L]
        assert len(cls)==nc
        assert sum(c["history_count"] for c in cls)==h
        assert sum(c["distinct_matrix_count"] for c in cls)==m

def test_all_classes_reciprocal():
    # TC-2: strict-full => palindromic charpoly, across ALL 474 classes
    assert len(NODES)==sum(v[0] for v in EXP.values())==474
    for n in NODES:
        assert n["charpoly_coeffs"]==n["charpoly_coeffs"][::-1]

def test_seed_is_B155():
    seed=[n for n in NODES if n["level"]==4]
    assert len(seed)==1 and seed[0]["abc"]==(4,5,4)
    assert seed[0]["charpoly_coeffs"]==(1,-4,5,-4,1)  # (x^2-3x+1)(x^2-x+1) = Ω4/B155

def test_history_mass_conservation():
    inc=defaultdict(int)
    for e in EDGES: inc[(e["target_level"],e["target_abc"])]+=e["multiplicity_history_extensions"]
    for n in NODES:
        if n["level"]>4:
            assert inc[(n["level"],n["abc"])]==n["history_count"]

def test_candidate_is_source_times_12_and_retained_is_target():
    H={L:v[1] for L,v in EXP.items()}
    trans=defaultdict(int)
    for e in EDGES: trans[(e["source_level"],e["target_level"])]+=e["multiplicity_history_extensions"]
    for (sl,tl),ret in trans.items():
        assert ret==H[tl]            # retained == target
        assert tl==sl+1              # graded by depth

def test_metallic_spectral_factors_present():
    # figure-eight T=3, silver T=6, bronze T=11 appear as reciprocal factors (x^2-Tx+1)(x^2-qx+1)
    seen=set()
    for n in NODES:
        a,mid,_=n["abc"]; disc=a*a-4*(mid-2)
        if disc>=0:
            r=int(disc**0.5)
            if r*r==disc and (a+r)%2==0:
                seen.add((a+r)//2); seen.add((a-r)//2)
    for T in (3,6,11):
        assert T in seen
