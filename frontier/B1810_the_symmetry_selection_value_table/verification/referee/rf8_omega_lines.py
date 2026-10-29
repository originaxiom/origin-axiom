"""rf8: at omega = e^{i pi/3} every listed direction lies on one of the order-3 stabiliser's three eigenlines."""
import numpy as np
from rf_common import *
dr = direction("DR", W)
for d in ("DR", "a0", "R", "t", "F_6", "F_10", "F_14", "F_22"):
    a = direction(d, W)
    print(d, "normalised a(omega)/a_I =", np.round(a / a[0], 8), " |<a,DR>|/|a||DR| = %.12f" % (abs(np.vdot(dr, a)) / np.linalg.norm(a) / np.linalg.norm(dr)))
