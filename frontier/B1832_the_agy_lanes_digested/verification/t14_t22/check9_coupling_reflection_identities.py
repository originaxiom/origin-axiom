"""CHECK 9 (closes the proof of agy Theorem 21 Part A in MAIN's frame).  B1644's coupling Y(S, M) = coupling(S, weighted_M(u))
is bilinear in (S, u), so an identity checked on all 4 x 4 basis pairs holds for all (S, u).  Identities (D = diag(1, -1, 1)
in main's BLOCKS order QJ, QI, QK):
  (T) Y(S, u with u_i -> -u_i)          = D Y(S with h_i -> -h_i, u)^T D      [order 10: transposed]
  (P) Y(S, u with u_j, u_k -> -u_j, -u_k) = D Y(S with h_j, h_k -> -h_j, -h_k, u) D   [order 8: plain]
With check 5's residue laws (R^e = lam10 (+, +, -, +) R^d in (1, j, i, k) at order 10; R^e = lam8 (+, -, +, -) R^d at order 8,
both derived from the difference-twist theta constants) and c_s sector-blind (check 1), these give
Y_e(S) = lam D Y_d(Sigma S)^T D (order 10) and Y_e(S) = lam D Y_d(Sigma S) D (order 8) on all 40 half-lifts."""
import itertools, json, pathlib
import numpy as np
import mainB
B = mainB.B(); HERE = pathlib.Path(__file__).resolve().parent
D = np.diag([1, -1, 1]); keys = ["1", "i", "j", "k"]
Sb = {"1": B.UNITS["1"], "i": B.QI, "j": B.QJ, "k": B.QK}
def Y(S, u): return B.coupling(S, B.weighted_M(u))
def unit(k): return {s: (1.0 if s == k else 0.0) for s in keys}
errT = errP = 0.0; ctrlT = ctrlP = 0.0
for sk, uk in itertools.product(keys, keys):
    S = Sb[sk]; u = unit(uk)
    uT = dict(u); uT["i"] = -uT["i"]; uP = dict(u); uP["j"] = -uP["j"]; uP["k"] = -uP["k"]
    sT = -1 if sk == "i" else 1; sP = -1 if sk in ("j", "k") else 1
    errT = max(errT, float(np.abs(Y(S, uT) - D @ (sT * Y(S, u)).T @ D).max()))
    errP = max(errP, float(np.abs(Y(S, uP) - D @ (sP * Y(S, u)) @ D).max()))
    ctrlT = max(ctrlT, float(np.abs(Y(S, uT) - D @ (sT * Y(S, u)) @ D).max()))     # wrong form: no transpose
    ctrlP = max(ctrlP, float(np.abs(Y(S, uP) - D @ (sP * Y(S, u)).T @ D).max()))   # wrong form: transposed
out = {"identity_T_max_err_16_basis_pairs": errT, "identity_P_max_err_16_basis_pairs": errP,
       "control_T_without_transpose": ctrlT, "control_P_with_transpose": ctrlP}
print(out); (HERE / "check9_coupling_reflection_identities_out.json").write_text(json.dumps(out, indent=1))
