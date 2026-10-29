"""rf2: the coupling's structure at the i-configurations.  Y(a) = a_I Y_I + a_J Y_J + a_K Y_K (linear in the direction).
Is Y diagonal / block-diagonal in the generation (BLOCKS) basis for every a?  Is there a fixed unitary pair (P, Q) with
Y(a~) = P Y(a) Q (a~ = conj components = the reading S~), explaining equal spectra at (i,(1/2,1/2))?"""
import numpy as np
from rf_common import *
np.set_printoptions(precision=4, suppress=True, linewidth=160)
for cn, p in (("(i, 0)", (0, 0)), ("(i, (1/2, 1/2))", (0.5, 0.5))):
    L = RADII[I][1]
    basis = [Ymat(e, I, p, 1, -4, L) for e in np.eye(3, dtype=complex)]
    print("==", cn, "L_2")
    for nm, Yb in zip("IJK", basis): print(" Y_%s =\n" % nm, Yb)
    for d in ("DR", "a0", "R", "t", "F_6", "F_10"):
        a = direction(d, I); print(" ", d, "a(i) =", np.round(a / a[np.argmax(abs(a))], 6))
