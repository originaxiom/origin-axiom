"""B207 part 2 -- the metallic family's dimensionless 'scale spectrum' (firewall-clean MATH).

The object is scale-free, so it makes no ABSOLUTE scale -- but it carries dimensionless invariants
(regulators, dilatations, conformal dimensions, WRT periods). This tabulates them and asks the honest
hierarchy question: is there an intrinsic exponentially-large/small RATIO (a hierarchy seed), or are
all intrinsic invariants polynomial in m (=> any hierarchy must come from the quantization LEVEL via
the volume conjecture, not the geometry)? FIREWALL: dimensionless invariants only; NO physical scale,
NO claim a scale emerges (B151 stands). Nothing to CLAIMS.md. Cited by speculations/S038."""
import numpy as np
from math import gcd


def lam(m):
    return (m + np.sqrt(m*m + 4)) / 2


def regulator(m):           # = log of the fundamental unit = geodesic length / 4 = entropy
    return np.log(lam(m))


def dilatation(m):          # larger eigenvalue of R^m L^m = geodesic multiplier = dynamical degree
    return lam(m)**2


def conformal_dim(m):       # B196: Delta = -(ln lambda/pi)^2  (dimensionless, non-unitary)
    return -(np.log(lam(m)) / np.pi)**2


def wrt_period(m):          # B204: per|Z(m,m)| = m(m^2+4)/gcd(m^2+4,4)
    D = m*m + 4
    return m * D // gcd(D, 4)


def spectrum(mmax=8):
    rows = []
    for m in range(1, mmax + 1):
        rows.append(dict(m=m, lam=lam(m), reg=regulator(m), dil=dilatation(m),
                         Delta=conformal_dim(m), period=wrt_period(m)))
    return rows


def hierarchy_diagnostics(mmax=12):
    regs = np.array([regulator(m) for m in range(1, mmax + 1)])
    # growth: regulator ~ log(m) (slow); ratio of consecutive -> 1 (NO exponential hierarchy in m)
    ratios = regs[1:] / regs[:-1]
    # fit reg(m) vs log(m)
    ms = np.arange(1, mmax + 1)
    slope = np.polyfit(np.log(ms[1:]), regs[1:], 1)[0]
    return dict(reg_consecutive_ratio_tail=float(ratios[-1]),
                reg_vs_logm_slope=float(slope),  # ~1 => regulator ~ log m, polynomial not exponential
                golden_reg=float(regs[0]), largest_reg=float(regs[-1]),
                max_over_min_ratio=float(regs[-1] / regs[0]))


if __name__ == "__main__":
    print(f"{'m':>2} {'lambda_m':>9} {'regulator':>10} {'dilatation':>11} {'Delta(B196)':>12} {'WRT period':>11}")
    for r in spectrum():
        print(f"{r['m']:>2} {r['lam']:>9.4f} {r['reg']:>10.4f} {r['dil']:>11.4f} {r['Delta']:>12.5f} {r['period']:>11}")
    h = hierarchy_diagnostics()
    print(f"\nhierarchy diagnostics:")
    print(f"  regulator(m) ~ {h['reg_vs_logm_slope']:.3f} * log(m)  (slope ~1 => LOGARITHMIC growth, no exp hierarchy in m)")
    print(f"  consecutive regulator ratio -> {h['reg_consecutive_ratio_tail']:.4f} (->1)")
    print(f"  max/min regulator over m=1..12: {h['max_over_min_ratio']:.2f}  (O(1), NOT a large hierarchy)")
    print("  => the family's intrinsic scale-spectrum is polynomial/logarithmic; any EXPONENTIAL")
    print("     hierarchy must come from the quantization LEVEL N (volume conjecture e^{N*entropy}),")
    print("     i.e. from quantization, not the object's geometry -- the firewall (B151) holds.")
    print("  golden has the SMALLEST regulator (log phi) -> the 'least hierarchical' / extremal point.")
