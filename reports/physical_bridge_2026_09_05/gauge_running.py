"""Boundary-value gauge running; physical inputs are explicit arguments.

Index order is (GUT-normalized U(1), SU(2), SU(3)); x = 1/alpha.
The two-loop option includes gauge terms ONLY, with Yukawa matrices set to zero.
It does not claim the full two-loop Standard Model. No measured comparison
value is imported into the forward solver.
"""
from dataclasses import dataclass
from functools import lru_cache
import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, root

SM_B = np.array([41 / 10, -19 / 6, -7.0])
SM_B2 = np.array([[199 / 50, 27 / 10, 44 / 5],
                  [9 / 10, 35 / 6, 12],
                  [11 / 10, 9 / 2, -26]])


class InvalidTrajectory(ValueError):
    """An integration or boundary solve failed; this is not a physics verdict."""


def inverse_couplings(inv_alpha_em, sin2theta, alpha_s):
    if not (math.isfinite(inv_alpha_em) and inv_alpha_em > 0
            and 0 < sin2theta < 1 and math.isfinite(alpha_s) and alpha_s > 0):
        raise ValueError("require positive finite couplings and 0 < sin2theta < 1")
    return np.array([3 / 5 * (1 - sin2theta) * inv_alpha_em,
                     sin2theta * inv_alpha_em, 1 / alpha_s])


def evolve(x, t_start, t_end, *, loops=2, b=None, matrix=None,
           rtol=2e-11, atol=2e-12):
    """Run inverse couplings between logarithmic scales, checking actual arrival.

At one loop this is an exact affine solution (up to floating arithmetic).
A pole or invalid numerical trajectory raises InvalidTrajectory, never returns
a partial solve as if it were the requested endpoint.
"""
    x = np.asarray(x, dtype=float)
    b = SM_B if b is None else np.asarray(b, dtype=float)
    matrix = SM_B2 if matrix is None else np.asarray(matrix, dtype=float)
    if x.shape != (3,) or b.shape != (3,) or matrix.shape != (3, 3):
        raise ValueError("expected three couplings, three betas and a 3x3 matrix")
    if not (np.isfinite(x).all() and (x > 1e-6).all()
            and np.isfinite(b).all() and np.isfinite(matrix).all()
            and math.isfinite(t_start) and math.isfinite(t_end)):
        raise InvalidTrajectory("nonfinite input or nonpositive inverse coupling")
    if loops == 1:
        end = x - b * (t_end - t_start) / (2 * math.pi)
        if (end <= 1e-6).any():
            raise InvalidTrajectory("one-loop path crosses a coupling pole")
        return end
    if loops != 2:
        raise ValueError("loops must be 1 or 2")
    if t_start == t_end:
        return x.copy()

    def rhs(_t, state):
        return -b / (2 * math.pi) - matrix @ (1 / state) / (8 * math.pi**2)

    def pole(_t, state):
        return min(state) - 1e-6

    pole.terminal = True
    pole.direction = 0
    sol = solve_ivp(rhs, (t_start, t_end), x, method="DOP853",
                    rtol=rtol, atol=atol, events=pole)
    if not sol.success or abs(sol.t[-1] - t_end) > 1e-9:
        raise InvalidTrajectory(f"integration did not reach endpoint: {sol.message}")
    end = sol.y[:, -1]
    if not np.isfinite(end).all() or (end <= 1e-6).any():
        raise InvalidTrajectory("invalid endpoint")
    return end


@dataclass(frozen=True)
class BoundaryPoint:
    t: float
    inverse_uv: float
    inverse_ir: tuple

    @property
    def inv_alpha_em(self):
        return 5 / 3 * self.inverse_ir[0] + self.inverse_ir[1]

    @property
    def sin2theta(self):
        return self.inverse_ir[1] / self.inv_alpha_em

    @property
    def alpha_s(self):
        return 1 / self.inverse_ir[2]

    @property
    def observables(self):
        return np.array([self.sin2theta, self.alpha_s])


@lru_cache(maxsize=2048)
def boundary_down(t, inv_alpha_em, loops=2):
    """One UV coupling, evolved down; fit only the specified EM normalization.

Only t and inv_alpha_em enter the forward prediction. The trial UV coupling
is a numerical unknown, not a second physical input.
"""
    if not (math.isfinite(t) and t >= 0 and math.isfinite(inv_alpha_em)
            and inv_alpha_em > 0):
        raise ValueError("require finite t >= 0 and inverse EM coupling > 0")
    seed = (inv_alpha_em - (5 / 3 * SM_B[0] + SM_B[1]) * t / (2 * math.pi)) / (8 / 3)

    def point(uv):
        ir = evolve(np.repeat(uv, 3), t, 0, loops=loops)
        return BoundaryPoint(t, float(uv), tuple(float(a) for a in ir))

    if loops == 1:
        return point(seed)
    if loops != 2:
        raise ValueError("loops must be 1 or 2")

    valid = {}
    # Bracketing uses no low-energy strong coupling or weak-angle datum.
    for width in (0, .25, .5, 1, 2, 4, 8, 16, 32, 64, 128):
        for uv in (seed - width, seed + width):
            if uv <= 1e-6 or uv in valid:
                continue
            try:
                valid[uv] = point(uv).inv_alpha_em - inv_alpha_em
            except InvalidTrajectory:
                continue
        ordered = sorted(valid)
        for left, right in zip(ordered, ordered[1:]):
            if valid[left] * valid[right] <= 0:
                uv = brentq(lambda u: point(u).inv_alpha_em - inv_alpha_em,
                            left, right, xtol=1e-11)
                result = point(uv)
                if abs(result.inv_alpha_em - inv_alpha_em) > 1e-7:
                    raise InvalidTrajectory("EM boundary residual exceeds tolerance")
                return result
        if seed in valid and abs(valid[seed]) < 1e-10:
            return point(seed)
    raise InvalidTrajectory("no valid positive-coupling normalization bracket found")


def boundary_up(t, inv_alpha_em, *, guess=(.23, .1), loops=2):
    """Independent simultaneous solve of BOTH UV matching equations."""
    def equations(y):
        x = inverse_couplings(inv_alpha_em, y[0], 1 / y[1])
        end = evolve(x, 0, t, loops=loops)
        return np.diff(end)

    sol = root(equations, (guess[0], 1 / guess[1]), tol=1e-10)
    residual = equations(sol.x)
    if not np.isfinite(residual).all() or max(abs(residual)) > 1e-7:
        raise InvalidTrajectory(f"simultaneous boundary solve failed: {sol.message}")
    return np.array([sol.x[0], 1 / sol.x[1]])


def legacy_box(point):
    """The actual B915 root brackets, disclosed separately from its scale interval."""
    return .18 <= point.sin2theta <= .30 and .06 <= point.alpha_s <= .30


def piecewise_one_loop(x_ir, t_end, thresholds):
    """Explicit masses as logarithmic thresholds: iterable (log(M/MZ), delta_b).

All thresholds must lie in [0,t_end]. The particle content is an input. This
function does not silently select masses, intermediate groups or multiplicity.
"""
    if not math.isfinite(t_end) or t_end < 0:
        raise ValueError("require finite t_end >= 0")
    events = sorted(((float(t), np.asarray(db, dtype=float)) for t, db in thresholds),
                    key=lambda event: event[0])
    if any(not math.isfinite(t) or t < 0 or t > t_end or db.shape != (3,)
           or not np.isfinite(db).all() for t, db in events):
        raise ValueError("thresholds must lie between the IR and UV scales")
    x = np.asarray(x_ir, dtype=float)
    b = SM_B.copy()
    previous = 0.
    for t, db in events:
        x = evolve(x, previous, t, loops=1, b=b)
        b += db
        previous = t
    return evolve(x, previous, t_end, loops=1, b=b)
