#!/usr/bin/env python3
"""B159 -- independent verification of the Ω strict-full class-graded DAG (L4-L10).

Two layers, both from banked data (the node/edge CSVs) + our own from-scratch counter:

PART 1 (instant, full L4-L10): structural + conservation checks on the class CSVs alone --
  level counts (classes / histories / matrices), every class charpoly palindromic (TC-2),
  the L4 seed class = Ω4 / B155 (golden×phase), incoming edge history-mass == class
  history_count, candidate mass = source x 12, retained == target, and which metallic
  bundle-monodromy traces T_M = M^2+2 appear as reciprocal factors (the B158 spectral image).

PART 2 (re-enumeration L4..MAXLEVEL, default 7): rebuild the class DAG FROM SCRATCH with our
  own counter (frontier/B156 independent_recount.py -- never touched the export pipeline),
  partition survivors by charpoly class, and compare class counts + per-class
  (history_count, distinct_matrix_count) + edge history-multiplicities to the CSVs.
  L4..L7 matching exactly => the class decomposition is a faithful charpoly-partition of the
  already-independently-verified survivor set (whose totals incl. L10=2488080 were re-derived
  in B156). Full export artifact (SHA256 in FINDINGS.md) retained under audit/.

Run:  python verify_gate2_dag.py        # PART 1 + PART 2 to L7 (fast)
      python verify_gate2_dag.py 8      # ... to L8 (heavier)
"""
import sys, csv, ast
from collections import Counter, defaultdict
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
NODES = HERE / "omega_strict_full_class_nodes_L4_L10.csv"
EDGES = HERE / "omega_strict_full_class_edges_L4_L10.csv"
sys.path.insert(0, str(HERE.parent / "B156_omega_strict_full_cone"))
import independent_recount as ir   # our from-scratch counter

ok = True
def check(name, cond, extra=""):
    global ok; ok = ok and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {extra}" if extra else ""))

# ---- load CSVs ----
nodes = []
with open(NODES) as f:
    for r in csv.DictReader(f):
        r["level"]=int(r["level"]); r["abc"]=tuple(ast.literal_eval(r["abc"]))
        r["charpoly_coeffs"]=ast.literal_eval(r["charpoly_coeffs"])
        r["history_count"]=int(r["history_count"]); r["distinct_matrix_count"]=int(r["distinct_matrix_count"])
        nodes.append(r)
edges = []
with open(EDGES) as f:
    for r in csv.DictReader(f):
        r["source_level"]=int(r["source_level"]); r["target_level"]=int(r["target_level"])
        r["source_abc"]=tuple(ast.literal_eval(r["source_abc"])); r["target_abc"]=tuple(ast.literal_eval(r["target_abc"]))
        r["multiplicity_history_extensions"]=int(r["multiplicity_history_extensions"])
        edges.append(r)
def level_nodes(L): return [n for n in nodes if n["level"]==L]

EXPECT_HIST={4:96,5:672,6:3840,7:20928,8:105312,9:521904,10:2488080}
EXPECT_MAT ={4:36,5:240,6:960,7:3240,8:9396,9:25536,10:65472}
EXPECT_CLS ={4:1,5:2,6:6,7:18,8:49,9:115,10:283}

print("== PART 1: structure + conservation of the class CSVs (full L4-L10) ==")
for L in range(4,11):
    cls=level_nodes(L)
    hist=sum(c["history_count"] for c in cls); mat=sum(c["distinct_matrix_count"] for c in cls)
    palin=all(c["charpoly_coeffs"]==c["charpoly_coeffs"][::-1] for c in cls)
    check(f"L{L}: classes={len(cls)}(exp {EXPECT_CLS[L]}) hist={hist}(exp {EXPECT_HIST[L]}) mat={mat}(exp {EXPECT_MAT[L]})",
          len(cls)==EXPECT_CLS[L] and hist==EXPECT_HIST[L] and mat==EXPECT_MAT[L])
    check(f"L{L}: every class charpoly palindromic (TC-2)", palin)

x=sp.symbols('x'); seed=level_nodes(4)[0]
seedpoly=sum(co*x**(4-i) for i,co in enumerate(seed["charpoly_coeffs"]))
check("L4 seed class charpoly = (x^2-3x+1)(x^2-x+1) = Ω4/B155",
      sp.expand(seedpoly-sp.expand((x**2-3*x+1)*(x**2-x+1)))==0, extra=str(seed["abc"]))

inc=defaultdict(int)
for e in edges: inc[(e["target_level"],e["target_abc"])]+=e["multiplicity_history_extensions"]
for L in range(5,11):
    check(f"L{L}: incoming edge history-mass per class == class history_count",
          all(inc[(L,c["abc"])]==c["history_count"] for c in level_nodes(L)))
trans=defaultdict(int)
for e in edges: trans[(e["source_level"],e["target_level"])]+=e["multiplicity_history_extensions"]
for (sl,tl),ret in sorted(trans.items()):
    check(f"L{sl}->L{tl}: retained {ret}==target {EXPECT_HIST[tl]}; candidate {EXPECT_HIST[sl]*12}={EXPECT_HIST[sl]}x12",
          ret==EXPECT_HIST[tl])

print("  -- metallic monodromy traces T_M=M^2+2 as reciprocal factors --")
T_met={M*M+2:M for M in range(1,8)}; present=defaultdict(set)
for n in nodes:
    a,mid,_=n["abc"]; disc=a*a-4*(mid-2)
    if disc>=0:
        r=sp.sqrt(disc)
        if r==int(r) and (a+int(r))%2==0:
            for t in ((a+int(r))//2,(a-int(r))//2):
                if t in T_met: present[t].add((n["level"],n["abc"]))
for T in sorted(T_met):
    h=present.get(T); print(f"     T_{T_met[T]}={T}: "+(f"{len(h)} class(es), e.g. {sorted(h)[0]}" if h else "absent (this depth range)"))

MAX=int(sys.argv[1]) if len(sys.argv)>1 else 7
print(f"\n== PART 2: re-enumerate class DAG from scratch, compare L4..L{MAX} ==")
cache={}; counter=ir.initial_seed_counter(cache)
def classify(cnt):
    h=Counter(); ms=defaultdict(set)
    for M,mu in cnt.items():
        abc=ir.charpoly_abc(M); h[abc]+=mu; ms[abc].add(M)
    return {abc:(h[abc],len(ms[abc])) for abc in h}
def cmp_nodes(L,mine):
    exp={c["abc"]:(c["history_count"],c["distinct_matrix_count"]) for c in level_nodes(L)}
    same=mine==exp; check(f"L{L} nodes: {len(mine)} classes, per-class (hist,mat) match CSV", same)
    if not same:
        for k in sorted(set(mine)|set(exp)):
            if mine.get(k)!=exp.get(k): print(f"        MISMATCH {k}: mine={mine.get(k)} csv={exp.get(k)}")
cmp_nodes(4,classify(counter))
for L in range(5,MAX+1):
    nxt=Counter(); eh=defaultdict(int)
    for M,mu in counter.items():
        sabc=ir.charpoly_abc(M)
        for (i,j) in ir.EDGES:
            T=ir.apply_shear(M,i,j)
            if ir.is_full_metric_exact(T,cache):
                nxt[T]+=mu; eh[(sabc,ir.charpoly_abc(T))]+=mu
    counter=nxt; cmp_nodes(L,classify(counter))
    exp_e={(e["source_abc"],e["target_abc"]):e["multiplicity_history_extensions"] for e in edges if e["target_level"]==L}
    check(f"L{L-1}->L{L} edges: {len(eh)} edges, history-multiplicities match CSV", dict(eh)==exp_e)

print("\n"+("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
sys.exit(0 if ok else 1)
