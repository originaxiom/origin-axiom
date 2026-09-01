"""R13 blind — FULL exact Jacobi over all basis triples (int64 einsum after clearing
denominators; overflow-guarded), + planted-positive control.
Covers all C(78,3) = 76,076 unordered distinct triples (and repeats).
"""
from fractions import Fraction as F
import pickle, os, math, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = pickle.load(open(os.path.join(HERE, "my_bs_tensor.pkl"), "rb"))["tensor"]
NB = 78

# common denominator
den = 1
for d in T.values():
    for v in d.values():
        den = den * v.denominator // math.gcd(den, v.denominator)
print("common denominator:", den)

C = np.zeros((NB, NB, NB), dtype=np.int64)
for (p, q), d in T.items():
    for k, v in d.items():
        iv = v * den
        assert iv.denominator == 1
        C[p, q, k] = int(iv)
        C[q, p, k] = -int(iv)

mx = np.abs(C).max()
print("max |scaled constant|:", mx, " overflow bound:", 78 * mx * mx, "(int64 ok)" if 78*mx*mx < 2**62 else "OVERFLOW RISK")

def jacobi_zero(C):
    T1 = np.einsum('bdc,ace->abde', C, C)  # [e_a,[e_b,e_d]]_e
    J = T1 + T1.transpose(1, 2, 0, 3) + T1.transpose(2, 0, 1, 3)
    return int(np.count_nonzero(J.reshape(NB * NB * NB, NB).any(axis=1))), J

nfail, J = jacobi_zero(C)
n_unordered = 0
if nfail == 0:
    print("FULL JACOBI: 0 failing ordered triples out of", NB ** 3)
else:
    print("JACOBI FAILURES (ordered triples):", nfail)
# count over unordered distinct triples explicitly for the banked-number comparison
bad_unordered = 0
tot = 0
nz = J.any(axis=3)
for a in range(NB):
    for b in range(a + 1, NB):
        for c in range(b + 1, NB):
            tot += 1
            if nz[a, b, c]:
                bad_unordered += 1
print(f"unordered distinct triples: {tot}  failures: {bad_unordered}")

# antisymmetry sanity: C[p,p,:] = 0 built in; check bilinear antisym
assert np.array_equal(C, -C.transpose(1, 0, 2))
print("antisymmetry: OK")

# simplicity/nondegeneracy quick check: Killing form rank (float estimate + exact det later)
ad = C.transpose(0, 2, 1).astype(np.float64)  # ad_p[e_k -> coeff e_?]: ad[p][k, q]? build properly below
AD = np.zeros((NB, NB, NB))
for p in range(NB):
    AD[p] = C[p].T  # (ad_p)_{k,q} = coeff of e_k in [e_p, e_q]
K = np.einsum('pij,qji->pq', AD, AD)
r = np.linalg.matrix_rank(K)
print("Killing form rank (float):", r, "/ 78")

# ---------------- planted-positive control ----------------
Cbad = C.copy()
# find a nonzero entry and corrupt it
idx = np.argwhere(Cbad)
p, q, k = idx[len(idx) // 3]
Cbad[p, q, k] += den  # shift by 1 in original units
Cbad[q, p, k] -= den
nf_bad, _ = jacobi_zero(Cbad)
print(f"planted control: corrupted C[{p},{q},{k}] by +1 -> failing ordered triples = {nf_bad} (must be > 0)")
assert nf_bad > 0

ok = (nfail == 0 and bad_unordered == 0 and tot == 76076 and r == 78)
print("VERDICT full Jacobi:", "PASS" if ok else "FAIL")
np.save(os.path.join(HERE, "my_C_int.npy"), C)
with open(os.path.join(HERE, "full_jacobi_result.txt"), "w") as f:
    f.write(f"den={den} ordered_failures={nfail} unordered_triples={tot} "
            f"unordered_failures={bad_unordered} killing_rank_float={r} "
            f"planted_control_failures={nf_bad}\n")
