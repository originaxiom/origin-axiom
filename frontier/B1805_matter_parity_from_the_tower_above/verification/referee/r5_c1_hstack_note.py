"""Referee B1805, r5 (NOTE on the draft's c1_spin10_checks.py): its centraliser_dim stacks Re and Im of the commutator
matrix as extra COLUMNS (np.hstack), which is not the real rank of X -> [X, M] on a real Lie algebra (that needs the
Re/Im parts as extra ROWS, np.vstack).  It returns 12 for su(5) only because each basis element's commutator with W is
purely real or purely imaginary.  Here the same function is run on a real-linear change of basis of su(5) (same algebra,
same centraliser) and compared with the row-stacked rank."""
import numpy as np
W5 = np.diag([1, 1, 1, -1, -1]).astype(complex)
def cdim_draft(basis, M):
    A = np.array([(X @ M - M @ X).ravel() for X in basis]).T
    return len(basis) - np.linalg.matrix_rank(np.hstack([A.real, A.imag]) if np.iscomplexobj(A) else A, tol=1e-9)
def cdim_right(basis, M):
    A = np.array([(X @ M - M @ X).ravel() for X in basis]).T
    return len(basis) - np.linalg.matrix_rank(np.vstack([A.real, A.imag]), tol=1e-9)
su5 = []
for i in range(5):
    for j in range(5):
        if i < j:
            E = np.zeros((5, 5), complex); E[i, j] = 1; E[j, i] = -1; su5.append(E)
            E = np.zeros((5, 5), complex); E[i, j] = 1j; E[j, i] = 1j; su5.append(E)
for k in range(4):
    E = np.zeros((5, 5), complex); E[k, k] = 1j; E[k + 1, k + 1] = -1j; su5.append(E)
rng = np.random.default_rng(0)
Rm = rng.normal(size=(24, 24))                          # a random REAL change of basis (invertible a.s.)
rot = [sum(Rm[a, b] * su5[b] for b in range(24)) for a in range(24)]
print("draft's basis:   draft function", cdim_draft(su5, W5), "; row-stacked", cdim_right(su5, W5))
print("rotated basis:   draft function", cdim_draft(rot, W5), "; row-stacked", cdim_right(rot, W5), "(the true answer is 12)")
# a minimal real-linear map where column-stacking fails: x -> x1 + i x2 from R^2 to C (injective, kernel 0)
A = np.array([[1, 1j]])
k_draft = 2 - np.linalg.matrix_rank(np.hstack([A.real, A.imag]))
k_right = 2 - np.linalg.matrix_rank(np.vstack([A.real, A.imag]))
print("toy map x -> x1 + i x2 (kernel 0): column-stacked kernel", k_draft, "; row-stacked kernel", k_right)
print("-> the draft's helper is not a real-rank computation in general; it is right for su(5) because the image of X -> [X, W]"
      " (anti-hermitian off-block matrices) is stable under taking real and imaginary parts, so the two ranks coincide."
      " No result changes (r1 recomputes (a) by row-stacking in Spin(10)).")
print("r5 exit 0")
