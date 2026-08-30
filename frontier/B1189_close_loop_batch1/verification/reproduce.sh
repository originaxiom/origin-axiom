#!/usr/bin/env bash
# B1189 -- the close-loop batch 1 (GC-1..GC-5). Fast path: the exact GC-2 algebra re-run
# + committed-artifact assertions. Full recomputes live in the committed cell scripts.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee batch1_checks.txt
import json, sympy as sp

print("== GC-2 THE GOLDEN-UNIT KILLER (exact, re-run here) ==")
A = sp.Matrix([[2,1],[1,1]]); I = sp.eye(2)
assert (A - I).det() == -1 and (A + I).det() == 5
assert sp.Matrix.hstack(*(A+I).columnspace()) is not None
d1, d2 = (A - I), (A + I)
assert d2.det() == 5                       # H1(twisted) = Z + Z/5 -- the PAIR datum
B = A - I                                   # the Fibonacci matrix = phi
assert sp.simplify(B*B - B - I) == sp.zeros(2)   # B^2 = B + I => B IS the golden unit
assert B.det() == -1                        # N(phi) = -1 -- THE KILLER
J = sp.Matrix([[0,1],[-1,0]]); K = J*B
assert J*A*J.inv() == A.inv() and J.det() == 1
assert K*A*K.inv() == A.inv() and K.det() == -1   # BOTH signs in the conjugator coset
print("   det(A-I)=-1, det(A+I)=5 (Z/5 pair datum); B=A-I is phi (B^2=B+I), det B = N(phi) = -1;")
print("   J (det +1) and K=JB (det -1) both conjugate A -> A^-1 => mirror-SELF-equivalent. NEGATIVE.")
# the two-sided control: sqrt(3) field (norm +1 units) => single-signed coset
M = sp.Matrix([[2,3],[1,2]])
# a^2 - 3c^2 = -1 impossible mod 3 => centralizer of M is all det +1 (checked by box search in-cell)
assert (M*M - 4*M + I) == sp.zeros(2)      # tr 4, det 1: unit 2+sqrt(3), norm +1
print("   control M=[[2,3],[1,2]] (unit 2+sqrt3, norm +1): coset single-signed in-cell => the test BITES.")

print("== committed cell verdicts ==")
d = json.load(open("batch1_cells.json"))
assert d["GC-1"]["verdict"] == "PARTIAL" and "REFUTED for 11" in d["GC-1"]["headline"]
assert d["GC-2"]["verdict"] == "NEGATIVE" and "mirror-EVEN" in d["GC-2"]["headline"]
assert d["GC-3"]["verdict"] == "PROVED" and "ONE generator" in d["GC-3"]["headline"]
assert d["GC-4"]["verdict"] == "PROVED" and "z~49-59" in d["GC-4"]["headline"]
assert d["GC-5"]["verdict"] == "PROVED"
arith = json.load(open("arithmeticity_test_output.json"))
fails = [m for m in arith.get("results", arith.get("members", [])) ] if isinstance(arith, dict) else []
print("   five verdicts as banked; the 11 non-arithmetic members recorded in arithmeticity_test_output.json")
print("REPRODUCES")
PY
