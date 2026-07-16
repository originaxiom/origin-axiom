"""B639 repair (disclosed, prereg G1-adjudication branch): the lambda->+lambda
CONJUGATE gluing is incompatible (banked). D_conjtheta needs the
CONTRAGREDIENT-conjugate: side 2 = W . conj((rho^T)^-1) . W^-1 (theta maps
27 -> 27bar = the contragredient). Solve the SL(2) intertwiner for both
lambda-signs; on success rerun the pipeline.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
kconj = mod["kconj"]
nullspace = mod["nullspace"]
lets2, wmat2, lam2 = mod["lets2"], mod["wmat2"], mod["lam2"]
LONG = mod["LONG"]

def t_inv(M):
    # contragredient of 2x2: (M^T)^-1 = adj(M)^T / det (det = 1)
    return [[M[1][1], K0 - M[1][0]], [K0 - M[0][1], M[0][0]]]

Ag = lets2['a']
lam2i = [[lam2[1][1], K0 - lam2[0][1]], [K0 - lam2[1][0], lam2[0][0]]]
Ag_ct = [[kconj(x) for x in row] for row in t_inv(Ag)]
lam_ct = [[kconj(x) for x in row] for row in t_inv(lam2)]
for sign, target_lam in (("+", lam2), ("-", lam2i)):
    rows_u = []
    for (X, Y_) in ((Ag_ct, Ag), (lam_ct, target_lam)):
        for i in range(2):
            for j in range(2):
                row = [K0] * 4
                for kk in range(2):
                    row[i * 2 + kk] = row[i * 2 + kk] + X[kk][j]
                    row[kk * 2 + j] = row[kk * 2 + j] - Y_[i][kk]
                rows_u.append(row)
    solu = nullspace(rows_u)
    inv_found = False
    for s_ in solu:
        cand = [[s_[0], s_[1]], [s_[2], s_[3]]]
        det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
        if not det.is_zero():
            inv_found = True
            print(f"  lambda -> {sign}lambda contragredient-conjugate: "
                  f"dim {len(solu)}, INVERTIBLE u = {cand}, det = {det}",
                  flush=True)
            break
    if not inv_found:
        print(f"  lambda -> {sign}lambda contragredient-conjugate: "
              f"dim {len(solu)}, NO invertible element", flush=True)
print("repair probe DONE", flush=True)
