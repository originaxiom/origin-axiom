"""P-229 (B1652's F2 D7 cell): main's check of the SM seat's W74 (the surface frame is CP-invariant), from its rule.
V1 exactly (sympy): C L C = L^-1, C P C = P with L the quarter-turn about e_i (i -> i, j -> k, k -> -j) and P the i-j swap
(W64's definitions); the S-phase condition e^{-i pi k} e^{-i pi/4} = e^{i pi/4} for rho_R at k = -1/2, 3/2, 7/2, its rho'
form at 5/2, its failure at 1/2 and 1; C conj B[l] = B[l] on e_i, v+ = e_j - i e_k, v- = e_j + i e_k; and the T and S laws of
f*(tau) = C conj f(-conj tau) re-derived (in FINDINGS).  V2 and V3 read from the seat's stored W72 output (its commit
e1724317), not recomputed.  The step 'each one-unit space is one-dimensional' is W64's K5, registered and not verified."""
import json, pathlib, subprocess
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
I = sp.I
L = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]); P = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); C = sp.diag(1, 1, -1)
out = {"CLC_is_Linv": C * L * C == L.inv(), "CPC_is_P": C * P * C == P,
       "L_quarter_turn": L ** 4 == sp.eye(3) and L ** 2 != sp.eye(3)}
def cond(k, ph): return sp.simplify(sp.exp(-I * sp.pi * k) * sp.exp(-I * ph) - sp.exp(I * ph)) == 0
out["S_condition_rhoR"] = {str(k): cond(k, sp.pi / 4) for k in (sp.Rational(-1, 2), sp.Rational(3, 2), sp.Rational(7, 2), sp.Rational(1, 2), 1)}
out["S_condition_rhoprime_5/2"] = cond(sp.Rational(5, 2), 3 * sp.pi / 4)
ei = sp.Matrix([1, 0, 0]); vp = sp.Matrix([0, 1, -I]); vm = sp.Matrix([0, 1, I])
out["eigenlines"] = {"e_i": L * ei == ei, "v+": sp.simplify(L * vp - I * vp) == sp.zeros(3, 1), "v-": sp.simplify(L * vm + I * vm) == sp.zeros(3, 1)}
out["C_conj_fixes"] = {n: C * v.conjugate() == v for n, v in (("e_i", ei), ("v+", vp), ("v-", vm))}
out["minus_P_in_O"] = (-P).det() == 1
# V2, V3: the seat's stored Y (W72, Y0 = 2.0), read
raw = subprocess.run(["git", "-C", str(ROOT), "show", "e1724317:docs/dossiers/the_weave_2026-10-07/the_surface_yukawa.json"],
                     capture_output=True, text=True, check=True).stdout
d = json.loads(raw)
Y = d["X4"]["Y (Y0 = 2.0)"]
Yc = sp.Matrix([[complex(a, b) for a, b in row] for row in Y])
import numpy as np
Yn = np.array([[complex(a, b) for a, b in row] for row in Y])
out["Y_max_abs_im_over_max_abs"] = float(np.abs(Yn.imag).max() / np.abs(Yn).max())
out["Y_symmetric"] = bool(np.allclose(Yn, Yn.T, rtol=1e-10))
dY = np.linalg.det(Yn.real); out["det_Y_real_part"] = float(dY)
out["eigenvalues_real_part"] = sorted(float(x) for x in np.linalg.eigvalsh((Yn.real + Yn.real.T) / 2))
out["arg_det_YY_over_pi"] = float(np.angle(np.linalg.det(Yn @ Yn)) / np.pi)
h = d["read-outs"]["h's first coefficients"]
out["h_max_abs_im"] = max(abs(v[1]) for v in h.values()); out["h_max_abs_re"] = max(abs(v[0]) for v in h.values())
# with one coupling M_u = M_d (up to a real factor): the CKM matrix is the identity and J = 0
U = np.linalg.svd(Yn @ Yn.conj().T)[0]; V = U.conj().T @ U
out["CKM_one_coupling_is_identity"] = bool(np.allclose(np.abs(V), np.eye(3)))
print(json.dumps(out, indent=1, default=str))
json.dump(out, open(HERE / "main_w74.json", "w"), indent=1, default=str)
