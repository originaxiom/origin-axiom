"""LR and RL generate the commutator subgroup of SL(2,Z) (a check for the paper's Section 2).

SL(2,Z) = <s, t | s^4, (st)^3 s^-2> with s = [[0,-1],[1,0]], t = L = [[1,1],[0,1]], and R = s^-1 t^-1 s.
(1) The abelianisation SL(2,Z) -> Z/12 sends t to 1 and s to 9, so L to 1 and R to -1: LR and RL lie in its kernel.
(2) A coset enumeration gives [SL(2,Z) : <LR, RL>] = 12, the kernel's index. Hence <LR, RL> is the whole kernel.
(3) The matrices: LR = [[2,1],[1,1]], RL = [[1,1],[1,2]], [LR,RL] = [[-7,6],[-6,5]] (trace -2), [L,R] has trace 3.
"""
import sympy as sp
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.coset_table import coset_enumeration_r

F, s, t = free_group("s t")
G = FpGroup(F, [s**4, (s*t)**3 * s**-2])
L, R = t, s**-1 * t**-1 * s
ab = {"s": 9, "t": 1}
def image(w):
    return sum(ab[str(g)] * e for g, e in w.array_form) % 12
assert (4 * ab["s"]) % 12 == 0 and (3 * (ab["s"] + ab["t"]) - 2 * ab["s"]) % 12 == 0
assert image(L * R) == 0 and image(R * L) == 0 and image(L) == 1
C = coset_enumeration_r(G, [L * R, R * L], max_cosets=5000); C.compress()
print("[SL(2,Z) : <LR, RL>] =", len(C.table))
assert len(C.table) == 12
Lm, Rm = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])
A, B = Lm * Rm, Rm * Lm
comm = A * B * A.inv() * B.inv()
assert comm.tolist() == [[-7, 6], [-6, 5]] and comm.trace() == -2
assert (Lm * Rm * Lm.inv() * Rm.inv()).trace() == 3
print("[LR,RL] =", comm.tolist(), " tr[L,R] = 3; all checks pass")
