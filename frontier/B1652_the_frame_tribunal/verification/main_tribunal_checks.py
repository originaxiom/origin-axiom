#!/usr/bin/env python3
"""B1652 (THE FRAME TRIBUNAL) -- main's verification records (not sealed tests; recomputations of seat and lane results).

  V1  lemma A's two halves, recomputing the SM seat's W82 L1 on the audit lane's background: the commutant in gl(3) of the
      family moves alone (S3 by P13, P23: predicted 2, a democratic split), of the holonomy's V4 alone (the family signs
      of the lane's A = diag(-1, 1, -1) (x) a and B = diag(1, -1, -1) (x) b: predicted 3, the diagonal), of both
      (predicted 1), and of a non-transitive control (P13 with V4: predicted 2)
  V2  the audit lane's count on main's code: the invariants of its generators L_g (x) wd in each summand of
      248 = (35,1,1) + (1,3,1) + (1,1,8) + (20,2,1) + (15,1,3bar) + (15bar,1,3) + (6,2,3) + (6bar,2,3bar)
      (the lane: 15 = 0 + 1 + 8 + 0 + 6 + 0); the (1,1,8) term is an input (colour untouched), not a check

    python3 -B main_tribunal_checks.py      # writes main_tribunal_checks.json beside itself
"""
import itertools, json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
I2 = np.eye(2, dtype=complex)
a = np.diag([1j, -1j]); b = np.array([[0, 1], [-1, 0]], dtype=complex)
s2 = np.sqrt(2)
qX, qY, qZ = (I2 + a) / s2, (I2 + b) / s2, (I2 - a) / s2
P13 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex)
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
DA = np.diag([-1, 1, -1]).astype(complex); DB = np.diag([1, -1, -1]).astype(complex)   # the family signs of A, B
FAM = {"X": P13, "Y": P23, "Z": DA @ P13}
wd = np.diag([np.exp(-1j * np.pi / 12), np.exp(1j * np.pi / 12)])


def null_dim(rows, tol=1e-10):
    S = np.linalg.svd(np.vstack(rows), compute_uv=False); return int(rows[0].shape[1] - np.sum(S > tol))


def commutant_dim(mats):
    n = mats[0].shape[0]; E = np.eye(n)
    return null_dim([np.kron(E, M) - np.kron(M.T, E) for M in mats])


def invariants_dim(mats):
    n = mats[0].shape[0]; return null_dim([M - np.eye(n) for M in mats])


def wedge(A, k):
    n = A.shape[0]; subs = list(itertools.combinations(range(n), k))
    return np.array([[np.linalg.det(A[np.ix_(r, c)]) for c in subs] for r in subs])


out = {}
out["V1"] = {"S3_alone": commutant_dim([P13, P23]), "V4_alone": commutant_dim([DA, DB]),
             "S3_and_V4": commutant_dim([P13, P23, DA, DB]), "control_P13_with_V4": commutant_dim([P13, DA, DB])}
L6 = {g: np.kron(FAM[g], q) for g, q in zip("XYZ", (qX, qY, qZ))}
A6, B6 = np.kron(DA, a), np.kron(DB, b)
rel = {"XYX-YXY": float(np.linalg.norm(L6["X"] @ L6["Y"] @ L6["X"] - L6["Y"] @ L6["X"] @ L6["Y"])),
       "YZY-ZYZ": float(np.linalg.norm(L6["Y"] @ L6["Z"] @ L6["Y"] - L6["Z"] @ L6["Y"] @ L6["Z"])),
       "XZ-ZX": float(np.linalg.norm(L6["X"] @ L6["Z"] - L6["Z"] @ L6["X"])),
       "central_word_plus_I6": float(np.linalg.norm(np.linalg.matrix_power(L6["X"] @ L6["Y"] @ L6["Z"], 4) + np.eye(6))),
       "inner_A_recovered": float(np.linalg.norm(L6["Z"] @ np.linalg.inv(L6["X"]) - A6.conj().T)),
       "inner_B_recovered": float(np.linalg.norm(L6["Y"] @ (L6["Z"] @ np.linalg.inv(L6["X"])) @ np.linalg.inv(L6["Y"]) @ np.linalg.inv(L6["Z"] @ np.linalg.inv(L6["X"])) - B6))}
gens = [(L6[g], wd) for g in "XYZ"]
summ = {"(35,1,1)": commutant_dim([A for A, _ in gens]) - 1, "(1,3,1)": commutant_dim([W for _, W in gens]) - 1,
        "(1,1,8) [input]": 8, "(20,2,1)": invariants_dim([np.kron(wedge(A, 3), W) for A, W in gens]),
        "(15,1,3bar)+(15bar,1,3)": 2 * 3 * invariants_dim([wedge(A, 2) for A, _ in gens]),
        "(6,2,3)+(6bar,2,3bar)": 2 * 3 * invariants_dim([np.kron(A, W) for A, W in gens])}
out["V2"] = {"lane_relations": rel, "summands": summ, "total": int(sum(summ.values()))}
json.dump(out, open(HERE / "main_tribunal_checks.json", "w"), indent=1)
print(json.dumps(out, indent=1))
