"""B970 / L134 -- SCOUT-SUPPORT COMPUTATION (support for a prior-art scout; NOT a sealed cell).

QUESTION ANSWERED IN-SANDBOX, from the E6 Cartan matrix alone:

  Which directions can give a gauge-invariant mass to the EXOTIC states of
  27 = 16 + 10 + 1, and what does supplying one of those directions do to the rank?

METHOD (nothing below is cited; everything is rebuilt here):
  1. Build the 27 as the Weyl orbit of omega_1. The 27 is MINUSCULE, so every weight
     has multiplicity 1 and the orbit algorithm is exact and complete (asserted).
  2. Grade by the alpha_1 and alpha_2 coefficients.  Deleting node 1 from E6
     (Bourbaki: chain 1-3-4-5-6, node 2 attached to node 4) leaves D5 = so(10);
     deleting node 2 as well leaves A4 = su(5).  A U(1) annihilating the so(10)
     simple roots is therefore an AFFINE function of n_1 alone, and one annihilating
     the su(5) simple roots is an affine function of (n_1, n_2) alone.  This is a
     derivation, not an ansatz.
  3. FIT psi and chi to the standard physics normalisation on a STRICT SUBSET of the
     blocks, then CHECK the remaining blocks -- so the assignment is PREDICTED.
  4. Hypercharge lies in the su(5) Cartan, i.e. in the span of the su(5) coroots, so
     Y(mu) = sum_{j in su(5)} y_j <mu, alpha_j^vee> with NO constant term.  Fit y_j on
     the 16 only; S and the whole exotic 10 are then PREDICTED.
  5. Test the mass-term selection rules by charge arithmetic, and confirm which cubic
     monomials actually occur by the weight-sum-zero test (Sym^3(27) contains the E6
     singlet once, so x_a x_b x_c occurs iff mu_a + mu_b + mu_c = 0).

SCOPE: every statement below is scoped to the GUT chain E6 > SO(10) x U(1)_psi >
SU(5) x U(1)_chi x U(1)_psi.  "The exotics" means the 10 + 1 of that SO(10).
"""
from fractions import Fraction as Fr
from itertools import combinations_with_replacement
from collections import Counter
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]      # E6, Bourbaki numbering
N = 6
A = [[0]*N for _ in range(N)]
for i in range(N): A[i][i] = 2
for i, j in EDGES: A[i-1][j-1] = -1; A[j-1][i-1] = -1

# ---------- 1. the 27 weights (Weyl orbit of omega_1) ----------
start = (1, 0, 0, 0, 0, 0)
seen = {start: (0,)*N}                       # Dynkin labels -> (n_1..n_6)
frontier = [(start, (0,)*N)]
while frontier:
    nxt = []
    for lab, n in frontier:
        for i in range(N):
            if lab[i] > 0:                                    # minuscule string test
                nl = tuple(lab[j] - A[i][j] for j in range(N))
                nn = tuple(n[j] + (1 if j == i else 0) for j in range(N))
                if nl not in seen:
                    seen[nl] = nn; nxt.append((nl, nn))
    frontier = nxt
W = list(seen.items())
assert len(W) == 27, len(W)
assert all(all(-1 <= c <= 1 for c in lab) for lab, _ in W)     # minuscule, confirmed

blocks_so10 = sorted(Counter(n[0] for _, n in W).items())      # -> (0,1) (1,16) (2,10)
blocks_su5  = sorted(Counter((n[0], n[1]) for _, n in W).items())

# ---------- 2. U(1)_psi and U(1)_chi ----------
# psi = a*n1 + b: FIT on the n1=0 block (so(10) singlet, psi=4) and n1=1 (the 16, psi=1).
psi = lambda k: Fr(4) - 3*k[0]
assert psi((2,)) == Fr(-2)                     # the 10 PREDICTED at -2 = standard value
# chi = p*n1 + q*n2 + r: FIT on the three sub-blocks of the 16 and on the so(10) singlet.
chi = lambda k: 3*k[0] - 4*k[1]
for k, v in [((1,0), 3), ((1,1), -1), ((1,2), -5), ((0,0), 0)]: assert chi(k) == v
assert (chi((2,1)), chi((2,2))) == (Fr(2), Fr(-2))   # the 10's two pieces PREDICTED

# ---------- 3. hypercharge, constrained to the su(5) Cartan ----------
# su(5) = nodes {3,4,5,6}; su(3)_c x su(2)_L = {3,4} x {6}; Y is the remaining direction.
byn = {}
for lab, n in W: byn.setdefault((n[0], n[1], n[4]), []).append(lab)
tenY   = {6: Fr(1,6), 3: Fr(-2,3), 1: Fr(1)}         # the 10 of su(5): Q, u^c, e^c
fivebY = {3: Fr(1,3),  2: Fr(-1,2)}                  # the 5bar of su(5): d^c, L
rowsM, rhs = [], []
for key, labs in byn.items():
    n1, n2, _ = key
    y = tenY[len(labs)] if (n1, n2) == (1, 1) else (fivebY[len(labs)] if (n1, n2) == (1, 0) else None)
    if y is None: continue                            # FIT ON THE 16 ONLY
    for lab in labs:
        rowsM.append([lab[2], lab[3], lab[4], lab[5]]); rhs.append(float(y))
sol, *_ = np.linalg.lstsq(np.array(rowsM, float), np.array(rhs), rcond=None)
yc = [Fr(round(x*30), 30) for x in sol]
Yf = lambda lab: yc[0]*lab[2] + yc[1]*lab[3] + yc[2]*lab[4] + yc[3]*lab[5]
assert max(abs(float(yc[0]*r[0]+yc[1]*r[1]+yc[2]*r[2]+yc[3]*r[3]) - t)
           for r, t in zip(rowsM, rhs)) == 0.0

NAME = {(0,0): "S", (1,1): "10_SU5", (1,0): "5bar_SU5", (1,2): "nu^c",
        (2,1): "5_SU5", (2,2): "5bar_ex"}
ROLE = {"S": "EXOTIC (the 1 of 16+10+1)", "10_SU5": "SM matter (16)",
        "5bar_SU5": "SM matter (16)", "nu^c": "SM matter (16), the right-handed neutrino",
        "5_SU5": "EXOTIC (in the 10)", "5bar_ex": "EXOTIC (in the 10)"}
SU32 = {1: "(1,1)", 2: "(1,2)", 3: "(3,1)", 6: "(3,2)"}

table = []
for key in sorted(byn):
    labs = byn[key]; n1, n2, n5 = key
    ys = {Yf(l) for l in labs}; assert len(ys) == 1, (key, ys)
    Y = ys.pop(); d = len(labs)
    qem = [Y + Fr(1,2), Y - Fr(1,2)] if d in (2, 6) else [Y]
    table.append(dict(n=list(key), dim=d, piece=NAME[(n1,n2)], role=ROLE[NAME[(n1,n2)]],
                      su3_su2=SU32[d], Y=str(Y), Qem=[str(q) for q in qem],
                      psi=str(psi(key)), chi=str(chi(key))))

# ---------- 4. state counting ----------
tot = sum(r["dim"] for r in table)
n16 = sum(r["dim"] for r in table if r["piece"] in ("10_SU5", "5bar_SU5", "nu^c"))
nnu = sum(r["dim"] for r in table if r["piece"] == "nu^c")
n10 = sum(r["dim"] for r in table if r["piece"] in ("5_SU5", "5bar_ex"))
n1_ = sum(r["dim"] for r in table if r["piece"] == "S")
counts = {"27": tot, "16": n16, "nu_R": nnu, "SM_15_fermion_generation": n16 - nnu,
          "10_of_SO10": n10, "1_of_SO10": n1_,
          "exotics_beyond_the_16  (= 10 + 1)": n10 + n1_,
          "states_beyond_a_15_fermion_generation (= 27 - 15)": tot - (n16 - nnu)}

# ---------- 5. THE SELECTION RULES ----------
PIECES = {k: [l for l, n in W if (n[0], n[1]) == k] for k in NAME}
Q = {k: (psi(k), chi(k)) for k in PIECES}
# MB12 vacuity note: the bare-mass test CAN pass (a self-conjugate rep such as the 26 of
# F4 contains charge-conjugate pairs) and CAN fail.  It is a real test.
bare = [(NAME[x], NAME[y]) for x, y in combinations_with_replacement(PIECES, 2)
        if (Q[x][0]+Q[y][0], Q[x][1]+Q[y][1]) == (0, 0)]
D, Dbar = (2, 2), (2, 1)
need = (-(Q[D][0]+Q[Dbar][0]), -(Q[D][1]+Q[Dbar][1]))
givers = [NAME[k] for k in PIECES if Q[k] == need]
# do the exotics pair up under the SM?  under U(1)_chi?  under U(1)_psi?
sm_vectorlike = True                       # 5 + 5bar of su(5): trivially SM-vector-like
chi_vectorlike = (Q[D][1] + Q[Dbar][1] == 0)
psi_vectorlike = (Q[D][0] + Q[Dbar][0] == 0)

# ---------- 6. which cubic monomials actually occur ----------
allw = [lab for lab, _ in W]; nof = {lab: n for lab, n in W}; zero = tuple([0]*N)
mono = Counter()
for i in range(27):
    for j in range(i, 27):
        for k in range(j, 27):
            if all(allw[i][t] + allw[j][t] + allw[k][t] == 0 for t in range(N)):
                mono[tuple(sorted(NAME[(nof[allw[x]][0], nof[allw[x]][1])]
                                  for x in (i, j, k)))] += 1

out = {
 "cell": "B970 / L134 scout-support computation", "sealed": False,
 "scope": "the GUT chain E6 > SO(10) x U(1)_psi > SU(5) x U(1)_chi x U(1)_psi; "
          "'the exotics' = the 10 + 1 of that SO(10)",
 "n_weights_27": len(W), "minuscule_confirmed": True,
 "so10_grading_by_alpha1_(level,dim)": blocks_so10,
 "su5_grading_by_(alpha1,alpha2)": [[list(k), v] for k, v in blocks_su5],
 "psi": "psi = 4 - 3*n1   [fit on the 1 and the 16; the 10 PREDICTED at -2]",
 "chi": "chi = 3*n1 - 4*n2 [fit on the 16's 3 pieces + the singlet; the 10's 2 pieces PREDICTED at +2,-2]",
 "Y":   {"form": "Y = sum_j y_j * <mu, alpha_j^vee> over the su(5) nodes 3,4,5,6 (no constant term)",
         "coeffs_on_(lab3,lab4,lab5,lab6)": [str(x) for x in yc],
         "fitted_on": "the 16 only", "residual": 0.0,
         "predicted_and_correct": "Y(S) = 0, Y(nu^c) = 0, and the whole exotic 10 -> "
                                  "(3,1)_{-1/3} + (3,1)_{+1/3} + (1,2)_{+1/2} + (1,2)_{-1/2}"},
 "SM_table_of_the_27": table,
 "STATE_COUNTS": counts,
 "R1_bare_mass_bilinears_inside_one_27": bare,
 "R2_charge_any_VEV_must_carry_to_give_the_exotic_pair_a_mass": {"psi": str(need[0]), "chi": str(need[1])},
 "R3_directions_inside_the_27_that_supply_it": givers,
 "R4_that_direction_is_the_highest_weight_omega_1": (Q[(0,0)] == need),
 "R5_exotic_pair_is_vectorlike_under": {"SM": sm_vectorlike, "U(1)_chi": chi_vectorlike,
                                        "U(1)_psi": psi_vectorlike},
 "R6_rep_independent": "the operator (exotic x exotic) carries psi = -4, so ANY field in ANY "
                       "E6 rep whose VEV gives it a mass carries psi = +4 != 0 and therefore "
                       "BREAKS U(1)_psi.  Exotic mass != 0  ==>  U(1)_psi broken.",
 "R7_cubic_monomials_present_in_the_E6_invariant_(weight_sum_zero)":
     [[list(t), c] for t, c in sorted(mono.items())],
}
with open(os.path.join(HERE, "exotics_charges.json"), "w") as f:
    json.dump(out, f, indent=1)
for k in ("STATE_COUNTS", "R1_bare_mass_bilinears_inside_one_27",
          "R2_charge_any_VEV_must_carry_to_give_the_exotic_pair_a_mass",
          "R3_directions_inside_the_27_that_supply_it",
          "R4_that_direction_is_the_highest_weight_omega_1",
          "R5_exotic_pair_is_vectorlike_under",
          "R7_cubic_monomials_present_in_the_E6_invariant_(weight_sum_zero)"):
    print(k, "=", json.dumps(out[k]))
print("\nSM TABLE")
for r in table:
    print(f"  {r['piece']:9} {r['su3_su2']:6} dim{r['dim']:>3}  Y={r['Y']:>5}  Q={str(r['Qem']):18} "
          f"psi={r['psi']:>3} chi={r['chi']:>3}  {r['role']}")
