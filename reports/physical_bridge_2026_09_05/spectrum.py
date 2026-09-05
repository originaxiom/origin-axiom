"""Conditional 4d spectrum -> exact indices, anomalies and one-loop betas.

Q = T3 + Y. For alpha_1 = k alpha_Y the U(1) index is Y^2/k.
Standard physics assumptions are explicit: Weyl fermions, complex scalars,
canonical kinetic normalization. Representation data alone does not supply them.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import math

import numpy as np


@dataclass(frozen=True)
class Field:
    name: str
    color: tuple  # SU(3) highest weight (p,q)
    weak: int     # SU(2) dimension
    y: F
    kind: str = "weyl"
    copies: int = 1

    def __post_init__(self):
        if (len(self.color) != 2 or any(type(a) is not int or a < 0 for a in self.color)
                or type(self.weak) is not int or self.weak < 1
                or type(self.copies) is not int or self.copies < 1
                or self.kind not in ("weyl", "complex_scalar")):
            raise ValueError("invalid representation, statistics or multiplicity")
        object.__setattr__(self, "y", F(self.y))

    @property
    def color_dim(self):
        p, q = self.color
        return (p + 1) * (q + 1) * (p + q + 2) // 2

    @property
    def color_index(self):
        p, q = self.color
        return F(self.color_dim * (p*p + q*q + p*q + 3*p + 3*q), 24)

    @property
    def weak_index(self):
        n = self.weak
        return F(n * (n*n - 1), 12)

    @property
    def color_anomaly(self):
        p, q = self.color
        return F(self.color_dim * (p-q) * (2*p+q+3) * (p+2*q+3), 60)

    def indices(self, k=F(5, 3)):
        k = F(k)
        if k <= 0:
            raise ValueError("hypercharge normalization k must be positive")
        return (self.y**2 * self.color_dim * self.weak / k,
                self.weak_index * self.color_dim,
                self.color_index * self.weak)


ONE_FAMILY = (
    Field("Q", (1, 0), 2, F(1, 6)),
    Field("uc", (0, 1), 1, F(-2, 3)),
    Field("dc", (0, 1), 1, F(1, 3)),
    Field("L", (0, 0), 2, F(-1, 2)),
    Field("ec", (0, 0), 1, F(1)),
    Field("Nc", (0, 0), 1, F(0)),
)
HIGGS = Field("H", (0, 0), 2, F(1, 2), "complex_scalar")
D_PAIR = (Field("D", (1, 0), 1, F(-1, 3)),
          Field("Dbar", (0, 1), 1, F(1, 3)))
L_PAIR = (Field("Lextra", (0, 0), 2, F(-1, 2)),
          Field("Lbar", (0, 0), 2, F(1, 2)))
SINGLET = Field("S", (0, 0), 1, F(0))


def matter_beta(fields, k=F(5, 3)):
    result = [F(0), F(0), F(0)]
    for f in fields:
        coefficient = F(2, 3) if f.kind == "weyl" else F(1, 3)
        for i, index in enumerate(f.indices(k)):
            result[i] += f.copies * coefficient * index
    return tuple(result)


def beta(fields, k=F(5, 3)):
    matter = matter_beta(fields, k)
    return tuple(matter[i] - F(11, 3) * adj for i, adj in enumerate((0, 2, 3)))


def anomalies(fields):
    """Perturbative anomalies and the SU(2) global mod-two obstruction."""
    a = {key: F(0) for key in ("SU3_cubic", "SU3_squared_Y", "SU2_squared_Y",
                               "Y_cubic", "gravity_Y")}
    mod2 = 0
    for f in fields:
        if f.kind != "weyl":
            continue
        n, dc, dw, y = f.copies, f.color_dim, f.weak, f.y
        a["SU3_cubic"] += n * dw * f.color_anomaly
        a["SU3_squared_Y"] += n * dw * f.color_index * y
        a["SU2_squared_Y"] += n * dc * f.weak_index * y
        a["Y_cubic"] += n * dc * dw * y**3
        a["gravity_Y"] += n * dc * dw * y
        mod2 += int(n * dc * 2 * f.weak_index)
    a["SU2_global_mod2"] = mod2 % 2
    return a


def threshold_requirement(x_ir, baseline, delta_d):
    """Inverse match: infer t_U and r=sum log(M_L/M_D) from ALL three x_IR.

Degenerate 5+5bar pairs have equal beta shifts. Thus their common mass drops
out of coupling DIFFERENCES. This computes a requirement for a mass mechanism,
not a forward prediction of an observed quantity.
"""
    x, b, d = (np.asarray(a, dtype=float) for a in (x_ir, baseline, delta_d))
    if any(a.shape != (3,) or not np.isfinite(a).all() for a in (x, b, d)):
        raise ValueError("expected finite vectors of length three")
    matrix = np.array([[b[0]-b[1], d[0]-d[1]],
                       [b[1]-b[2], d[1]-d[2]]])
    target = 2 * math.pi * np.array([x[0]-x[1], x[1]-x[2]])
    t, r = np.linalg.solve(matrix, target)
    return float(t), float(r)
