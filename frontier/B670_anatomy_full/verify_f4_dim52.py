"""B670 spot-verify: dim stab_e6(v0) = 52 (the F4 skeleton's core claim),
via the banked 78-basis machinery (cellB's construction)."""
import importlib.util
import os
import sys
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

HERE = _REPO + "/frontier/B662_successor_campaign/cellB"
sys.path.insert(0, HERE)
src = open(os.path.join(HERE, "qblock_78.py")).read()
# reuse its apparatus-building head (through the 78 basis, before Fox)
marker = "gate 1a"
head = src[:src.index(marker)] if marker in src else src
head = head[:head.rfind("\n", 0, head.rfind("log("))]
ns = {"__name__": "b670_f4", "__file__": os.path.join(HERE, "qblock_78.py")}
exec(compile(head, "qblock_head", "exec"), ns)
K0, K1 = ns["K0"], ns["K1"]
basis78 = ns.get("basis78") or ns.get("E6_BASIS") or ns.get("basis")
apply_ = ns.get("apply") or ns.get("apply27")
nullspace = ns["nullspace"]
print("keys sample:", [k for k in ns if "basis" in k.lower() or "78" in k][:6])
v0 = [K0] * 27
for i, c in ((12, K1), (13, K0 - K1), (14, K1)):
    v0[i] = c
# rows: for each basis element X (27x27), the 27 entries of X.v0 -> a 78-col system
cols = []
for X in basis78:
    Xv = [sum((X[r][c2] * v0[c2] for c2 in range(27)), K0) for r in range(27)]
    cols.append(Xv)
rows = [[cols[j][r] for j in range(len(basis78))] for r in range(27)]
sol = nullspace(rows)
print(f"dim stab_e6(v0) = {len(sol)}  (F4 = 52?)", len(sol) == 52)
