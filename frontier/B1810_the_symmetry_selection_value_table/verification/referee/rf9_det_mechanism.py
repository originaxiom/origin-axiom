"""rf9: B1659's det Y = 4 det S det M tr(eps S M^T); at (i,(1/2,1/2)) the third factor vanishes for every a = (1,1,i kappa)."""
import numpy as np
from rf_common import *
for cn, p in (("(i,0)", (0, 0)), ("(i,(1/2,1/2))", (0.5, 0.5))):
    L = RADII[I][1]; M = B.weighted_M(weights(I, p, 1, -4, L))
    for k in (2 ** -0.5, 2 ** 1.5, -2 ** 2.5, 1.7):
        a = np.array([1, 1, 1j * k]); S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK; Y = B.coupling(S, M)
        rhs = 4 * np.linalg.det(S) * np.linalg.det(M) * np.trace(B.EPS @ S @ M.T)
        print(cn, "kappa=%.3f" % k, "det Y=%.3e" % abs(np.linalg.det(Y)), " |4 detS detM tr(eps S M^T)|=%.3e" % abs(rhs),
              " |tr(eps S M^T)|=%.3e" % abs(np.trace(B.EPS @ S @ M.T)), " detS=a.a=%.3f" % abs(np.linalg.det(S)))
