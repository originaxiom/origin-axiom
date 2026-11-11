#!/usr/bin/env python3
"""The vacuity control for the agy lane's read-out: the same closed form at other levels.  Data-free.

The lane's arc B1881 reads, at level 5, the state the field of sqrt 5 gives in closed form.  Its spectral parameter is
pi / (2 ln phi), phi the unit of that field, and the findings call this a "striking connection back to the golden
ground".  The level is 5 because the field is that of sqrt 5.  So the question of the acceptance page's seventh
condition: is this what level 5 gives, or what ANY level of the kind gives, with its own unit in the place of phi?

peak_from_the_closed_form.py rebuilt the level-5 state from the integers a + b phi and found the lane's point.  This
script does the same thing, with the same code path, for the fields of sqrt 13, sqrt 17 and sqrt 29 (class number one,
a unit of norm -1, as for sqrt 5), and for sqrt 5 again as its own control.  For each level D it builds
    c(n) = sum over the ideals (alpha) of norm n of sign(N alpha) cos(R ln |alpha / alpha'|),   R = pi / (2 ln unit),
tries the sine and the cosine series against the exchange z -> -1/(D z) with either sign, and, where one of the four
holds, finds the maximum of the density on the circle |z|^2 = 1/D above height 0.07.

    python3 -B the_same_closed_form_at_other_levels.py

THE SEAT'S EXPECTATIONS, written before the run and committed before it:
  Z0  at level 5 the script returns what peak_from_the_closed_form.py returned: the sine series, odd under the
      exchange, peak at 0.2515398 + 0.3697671 i                                                              95%
  Z1  at each of the levels 13, 17 and 29 one of the four combinations holds to 1e-8: the same recipe gives a
      state there, with that level's own unit in the place of phi                                            75%
  Z2  where Z1 holds, the density's greatest value on the circle lies off the mirror lines (its real part is
      neither 0 nor 1/2): a mirror pair again                                                                70%
  Z3  the reduced height of the peak (sqrt D times the sine of its angle) differs from level 5's 1.8488 by
      more than 0.05 at every other level: the place moves with the level                                    85%
HOW IT WILL BE READ.  If Z1 to Z3 hold, then "quantized by the unit of the level's field, peaking off the mirror as a
pair" is what the recipe returns at every level tried, and at level 5 the unit happens to be the golden one.  If Z1
fails at every other level, level 5 is special for this recipe and this control says so.
"""
import math
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar

FIELDS = {5: (0, 1), 13: (1, 1), 17: (3, 2), 29: (2, 1)}          # D: the unit u + v w, w = (1 + sqrt D) / 2, of norm -1
NMAX = 320
lines = []


def log(x):
    print(x, flush=True); lines.append(x)


t = np.linspace(0.0, 10.0, 20001); wt = np.full(len(t), t[1] - t[0]); wt[0] = wt[-1] = (t[1] - t[0]) / 2
xs = np.concatenate([np.linspace(0.3, 2.0, 1701)[:-1], np.linspace(2.0, 60.0, 5801)])


def bessel(R):
    """x -> K_{iR}(x) = integral over t of exp(-x cosh t) cos(R t), tabulated as exp(x) K and splined"""
    tab = np.array([np.sum(wt * np.exp(-x * (np.cosh(t) - 1.0)) * np.cos(R * t)) for x in xs]); spl = CubicSpline(xs, tab)
    return lambda x: np.where(np.asarray(x) < 60.0, spl(np.clip(x, 0.3, 60.0)) * np.exp(-np.clip(x, 0.3, 60.0)), 0.0)


def level(D):
    w = (1 + math.sqrt(D)) / 2; wc = 1 - w; q = (D - 1) // 4; u, v = FIELDS[D]
    val = lambda a, b: (a + b * w, a + b * wc)
    mul = lambda a, b, c, d: (a * c + b * d * q, a * d + b * c + b * d)                 # w^2 = w + (D - 1) / 4
    assert abs(val(u, v)[0] * val(u, v)[1] + 1) < 1e-9, "the unit's norm is not -1"
    eps = val(u, v)[0]; R = math.pi / (2 * math.log(eps)); inv = (-(u + v), v)           # 1 / unit = -(its conjugate)
    assert mul(u, v, *inv) == (1, 0)

    def reduced(a, b):
        for _ in range(2000):
            al, co = val(a, b)
            if al < 0: a, b = -a, -b; continue
            tt = math.log(abs(al / co))
            if tt >= 2 * math.log(eps) - 1e-11: a, b = mul(a, b, *inv); continue
            if tt < -1e-11: a, b = mul(a, b, u, v); continue
            return a, b
        raise RuntimeError("no reduced generator")
    ideals = {}; B = int(3.0 * math.sqrt(NMAX) * eps) + 8
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            n = abs(a * a + a * b - q * b * b)
            if 1 <= n <= NMAX: ideals.setdefault(n, set()).add(reduced(a, b))
    c = np.zeros(NMAX + 1)
    for n, gens in ideals.items():
        for (a, b) in gens:
            al, co = val(a, b); c[n] += (1 if al * co > 0 else -1) * math.cos(R * math.log(abs(al / co)))
    mult = max(abs(c[m * n] - c[m] * c[n]) for m in range(2, 16) for n in range(2, 16) if math.gcd(m, n) == 1 and m * n <= NMAX)
    K = bessel(R); ns = np.arange(1, NMAX + 1)
    ser = {"sine": lambda z: float(math.sqrt(z.imag) * np.sum(c[1:] * K(2 * math.pi * ns * z.imag) * np.sin(2 * math.pi * ns * z.real))),
           "cosine": lambda z: float(math.sqrt(z.imag) * np.sum(c[1:] * K(2 * math.pi * ns * z.imag) * np.cos(2 * math.pi * ns * z.real)))}
    rng = np.random.default_rng(1881 + D); pairs = []
    while len(pairs) < 24:
        z = complex(rng.uniform(-0.45, 0.45), rng.uniform(0.06, 0.6)); wz = -1.0 / (D * z)
        if wz.imag >= 0.06: pairs.append((z, wz))
    found = None; report = []
    for name, f in ser.items():
        sc = max(abs(f(z)) for z, _ in pairs)
        for sign, label in ((+1, "odd"), (-1, "even")):
            gap = max(abs(f(wz) + sign * f(z)) for z, wz in pairs) / sc
            report.append("%s, %s under the exchange: %.1e" % (name, label, gap))
            if gap < 1e-8 and found is None: found = (name, label, f)
    log("level %d: the unit %.6f, R = pi / (2 ln unit) = %.9f; ideals of norm up to %d: %d; c multiplicative to %.1e; c(2..7) = %s" % (
        D, eps, R, NMAX, sum(len(g) for g in ideals.values()), mult, " ".join("%+.4f" % c[n] for n in range(2, 8))))
    log("      " + "; ".join(report))
    if found is None:
        log("      NO combination holds to 1e-8: the recipe gives no state of this kind at level %d" % D); return None
    name, label, f = found
    on = lambda th: complex(math.cos(th), math.sin(th)) / math.sqrt(D)
    # at level 5 the arc is the one inside the lane's domain, as in peak_from_the_closed_form.py; elsewhere, all of the circle above height 0.07
    lo = math.atan(0.5) if D == 5 else math.asin(min(1.0, 0.07 * math.sqrt(D))); grid = np.linspace(lo, math.pi / 2, 3001)
    vals = np.array([f(on(th)) ** 2 for th in grid]); k = int(np.argmax(vals))
    tops = [i for i in range(1, 3000) if vals[i] >= vals[i - 1] and vals[i] >= vals[i + 1] and vals[i] >= 0.999 * vals[k]]
    best = minimize_scalar(lambda th: -f(on(th)) ** 2, bounds=(grid[max(k - 2, 0)], grid[min(k + 2, 3000)]), method="bounded", options={"xatol": 1e-12})
    z = on(best.x); red = math.sqrt(D) * math.sin(best.x)
    log("      a state: the %s series, %s under the exchange.  Greatest density on the circle above height 0.07: at %.7f + %.7f i (angle %.3f degrees), reduced height %.4f; at the arc's ends the density is %.1e and %.1e of that; local maxima within 0.1%% of the greatest: %d" % (
        name, label, z.real, z.imag, math.degrees(best.x), red, vals[0] / -best.fun, vals[-1] / -best.fun, len(tops)))
    return {"R": R, "series": name, "parity": label, "z": z, "angle": math.degrees(best.x), "reduced": red, "tops": len(tops)}


out = {D: level(D) for D in FIELDS}
z5 = out[5]
z0 = z5 is not None and z5["series"] == "sine" and z5["parity"] == "odd" and abs(z5["z"] - complex(0.2515398, 0.3697671)) < 2e-6
log(""); log("Z0  level 5 again: %s" % ("HOLDS" if z0 else "FAILS"))
others = [D for D in FIELDS if D != 5]
z1 = all(out[D] is not None for D in others)
log("Z1  a state of the same recipe at each of the levels %s: %s" % (", ".join(map(str, others)), "HOLDS" if z1 else "FAILS (at %s)" % ", ".join(str(D) for D in others if out[D] is None)))
have = [D for D in others if out[D] is not None]
if have:
    # a sine series vanishes on the mirror line and on every image of it, so its peak is off them all; for a cosine series
    # only the two lines of the strip are tested here (real part 0 and 1/2)
    off = {D: (abs(out[D]["z"].real) > 1e-4 and abs(abs(out[D]["z"].real) - 0.5) > 1e-4 and 0.01 < out[D]["angle"] < 89.99) for D in have}
    log("Z2  the peak lies off the mirror lines: %s: %s" % (", ".join("level %d %s (%s series)" % (D, "yes" if off[D] else "NO", out[D]["series"]) for D in have), "HOLDS" if all(off.values()) else "FAILS"))
    mv = {D: abs(out[D]["reduced"] - 1.8488) for D in have}
    log("Z3  the reduced height differs from level 5's 1.8488 by more than 0.05: %s: %s" % (", ".join("level %d: %.4f" % (D, out[D]["reduced"]) for D in have), "HOLDS" if all(v > 0.05 for v in mv.values()) else "FAILS"))
log("other levels exit 0")
open(__file__.replace(".py", "_out.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
