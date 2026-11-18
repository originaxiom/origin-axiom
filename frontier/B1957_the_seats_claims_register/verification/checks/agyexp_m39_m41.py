"""agy-exp's answers to M39 to M41 and its harvest review (its status page at 224dc6253), held against main's computations.
 K1  its five slips confirmed: K J K^-1 = J^-1 for J = [[2, 1], [1, 1]], K = [[0, -1], [1, 0]]; F (1, 2) = (11, 2) = (1, 2) mod 5 for
     F = [[-1, 6], [0, 1]]; W12 - 1 = [[96, 57], [17, 9]] with gcd 1 and |det| 105; C = 5 S + 6 F on dP9 has C^2 = 35, g = 16;
     agyexp-xown-05 SUPERSEDED and agyexp-xown-03 standing.
 K2  its 3A: each of the 26 narrowed lines it names is printed by a committed script of main's (the run line quoted).
 K3  its lane at f1efc59dd; the 12 lines of its 3B, each VERIFIED there in the record it names."""
import json, subprocess, pathlib
from fractions import Fraction
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
mul = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
J, K, Ki = [[2, 1], [1, 1]], [[0, -1], [1, 0]], [[0, 1], [-1, 0]]; Jinv = [[1, -1], [-1, 2]]
F = [[-1, 6], [0, 1]]; v = [F[0][0] * 1 + F[0][1] * 2, F[1][0] * 1 + F[1][1] * 2]
L, R = [[1, 1], [0, 1]], [[1, 0], [1, 1]]; W = [[1, 0], [0, 1]]
for x in "LLLLLRLLRRLR": W = mul(W, L if x == "L" else R)
from math import gcd
Wm = [[W[0][0] - 1, W[0][1]], [W[1][0], W[1][1] - 1]]
S2, SF, F2 = -1, 1, 0; C2 = 25 * S2 + 2 * 5 * 6 * SF + 36 * F2; CK = -(5 * SF + 6 * F2); g = (C2 + CK) // 2 + 1   # K = -F
V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r, at="f1efc59dd": json.loads(git("show", "%s:%srecords/%s.json" % (at, V, r)))
print("K1: K J K^-1 = J^-1: %s; F (1, 2) = %s = (1, 2) mod 5: %s; W12 = %s, W12 - 1 gcd %d, |det| %d; C^2 = %d, C.K = %d, genus %d; agyexp-xown-05 %s, agyexp-xown-03 %s"
      % (mul(mul(K, J), Ki) == Jinv, v, [x % 5 for x in v] == [1, 2], W, gcd(gcd(Wm[0][0], Wm[0][1]), gcd(Wm[1][0], Wm[1][1])), abs(Wm[0][0] * Wm[1][1] - Wm[0][1] * Wm[1][0]), C2, CK, g, rec("agyexp-xown-05")["verdict"], rec("agyexp-xown-03")["verdict"]))
HERE = pathlib.Path(__file__).resolve().parent; B = HERE.parents[2] / "B1939_the_agy_seats_unharvested_claims_recomputed" / "verification"
run = lambda p: p.read_text()
older, wc2, wf17 = run(HERE / "agyexp_older_notes_run.txt"), run(HERE / "web_wc2_census_and_lattices_run.txt"), run(HERE / "web_wf17_on_main_run.txt")
flat, cover, lat = run(B / "xc2_flat_su5_lines_run.txt"), run(B / "xc2_cover_degrees_run.txt"), run(B / "torsion_lattice_run.txt")
cites = {"X_C2 41": ("|det(LR - 1)| = 1 and |det(RL - 1)| = 1" in older and "fact1                                         True" in flat),
         "X_C2 46 to 50": "counts_as_claimed_all_conventions             True" in flat and "separation_holds_all_conventions              True" in flat,
         "X_C2 52": "the order of LR modulo 2, 5, 10, 25, 30: [3, 10, 30, 50, 60]" in older,
         "X_C2 53": "fact3_as_claimed                              True" in flat,
         "X_C2 55": "fixes 2 of the 4 points of order dividing 2" in older and "fixed points in (1/2 Z/Z)^2: 2 of 4" in cover,
         "X_C2 66": "lines of exact order at most 12 up to sign: 266" in older,
         "P781 28": "J L J = L^T and J R J = R^T: True; J (1, 2) = [2, 1] = 2 (1, 3) modulo 5: True" in older,
         "P781 45, 46": "Smith invariants of W10 + 1: [1, 45], of W12 - 1: [1, 105]" in older and "W12 = W10 L R to [1, 2]" in older,
         "P781 87, 88": "W1: 285 members; oriented classes 228" in wc2,
         "P781 106": "(0,0,0,0,0,1,1,1) in E8: False; H = twice it in E8: True" in wc2 and "Fraction(3, 1): 16" in wc2 and "Fraction(-1, 1): 48" in wc2,
         "P781 113, 114; phase-4 100": "I_{1,9}: det = -1 ; signature (pos, neg) = (1, 9)" in lat and "chi_top = 12  sigma = -8  chi(O) = (K^2 + chi)/12 = 1" in lat and "E8(-1) complement: True" in lat and "12/2 = 6" in lat and "N=3: min sum h^2 = 12, k_min = 6" in lat,
         "P781 115": "C^2 = 35, C.K = -5, genus 16, and the ramification over the base is 2g - 2 + 10 = 40" in older,
         "P781 130, 131": "2 + 2 - 2 - 2 = 0; 2 + q - 2 = 0 and 2q = 0 modulo 5 force q = [0]" in older,
         "X_NEVER 52, 53": "Q1: all eighteen counts equal the note's: True" in wf17 and "m369 -> 2I (order 120): homomorphisms 2400, surjections 480" in wf17 and "s639 -> 2O (order 48): homomorphisms 192, surjections 0" in wf17,
         "F3 33, 34": "the first is odd and enters the frame as a product of two, the other three are even" in older}
print("K2: the lines of its 3A, each printed by main's committed run: %s; all: %s" % (cites, all(cites.values())))
sm = json.loads(git("show", "f1efc59dd:" + V + "SUMMARY.json"))["lanes"]["agy-exp"]
X = "agy-exp:AGY_EXP_TO_MAIN_2026-11-18_X_L5_RESULTS_AND_M37_M38_ANSWERS:"
three_b = {"agyexp-xl5-02": [X + str(n) for n in (25, 26, 48, 36, 38, 47, 49, 59, 64)], "agyexp-wc2a-01": ["agy-exp:AGY_EXP_TO_CC_2026-11-11_W_C2_ANSWERS:16"], "agyexp-b36-01": ["agy-exp:AGY_EXP_TO_CC_2026-11-14_B1936_COLD_READ:23", "agy-exp:AGY_EXP_TO_CC_2026-11-14_B1936_COLD_READ:30"]}
print("K3: agy-exp's lane at f1efc59dd: %s; its 3B lines each VERIFIED there in the record it names: %s"
      % ({k: sm[k] for k in ("files", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, all(rec(r)["verdict"] == "VERIFIED" and all(u in rec(r)["units"] for u in us) for r, us in three_b.items())))
