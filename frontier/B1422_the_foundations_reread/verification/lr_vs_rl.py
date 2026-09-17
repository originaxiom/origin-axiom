"""S15: which product is the figure-eight monodromy, under the project's own convention?

docs/UNIQUENESS_THEOREM.md A4 fixes L = [[1,1],[0,1]], R = [[1,0],[1,1]]; the golden substitution matrix is
M = [[1,1],[1,0]].  B1083 wrote "M^2 = [[2,1],[1,1]] = RL exactly" -- right matrix, wrong name -- and the name
propagated to THE_LADDER (X23) and THE_FORCED_AND_THE_FREE.  The order LR vs RL is the project's single irreducible
inserted bit (A7), so the label matters even though the two are conjugate.
"""
L = [[1, 1], [0, 1]]
R = [[1, 0], [1, 1]]
M = [[1, 1], [1, 0]]


def mul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


LR, RL, M2 = mul(L, R), mul(R, L), mul(M, M)
if __name__ == "__main__":
    print("L  =", L, " R =", R, " M =", M)
    print("LR =", LR)
    print("RL =", RL)
    print("M^2=", M2)
    print("M^2 == LR :", M2 == LR)
    print("M^2 == RL :", M2 == RL)
    print("conjugate (same trace/det), so trace, determinant, char poly and spectrum cannot see the order:",
          LR[0][0] + LR[1][1] == RL[0][0] + RL[1][1])
