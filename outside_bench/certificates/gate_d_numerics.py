#!/usr/bin/env python3
"""GATE D -- the first numerics at the object's own kappa.
Seal: seals/GATE_D_FIRST_NUMERICS_PREREG.md.  Nothing from memos 137/143-147 is reused:
that machinery is Hermitian and the record warns it does not transfer.  Gate 5: no measured value.
"""
import numpy as np, cmath, math

print("="*78); print("GATE D -- FIRST NUMERICS AT THE OBJECT'S OWN KAPPA"); print("="*78)

# ---------------- D-0: arithmetic check, binding ----------------
w = cmath.exp(1j*math.pi/3)                      # omega
kappa = 1 + w
tgt = math.sqrt(3)*cmath.exp(1j*math.pi/6)
print(f"\nD-0  kappa = 1+omega = {kappa:.12f}")
print(f"     sqrt(3)*e^(i pi/6) = {tgt:.12f}")
print(f"     |kappa| = {abs(kappa):.12f}  arg = {cmath.phase(kappa):.12f} (pi/6 = {math.pi/6:.12f})")
ok_k = abs(kappa - tgt) < 1e-13
print(f"     MATCH: {ok_k}")

def I(x, y, z): return x*x + y*y + z*z - x*y*z - 2
def T(v):
    x, y, z = v; return (x*y - z, x, y)
rng = np.random.default_rng(0)
err = 0.0
for _ in range(200):
    v = tuple(complex(a, b) for a, b in rng.normal(size=(3, 2)))
    err = max(err, abs(I(*T(v)) - I(*v)))
print(f"     trace-map invariance of I on 200 random complex points: max err {err:.2e}")
ok_inv = err < 1e-9
assert ok_k and ok_inv, "D-0 FAILED -- cell voids"
print("     D-0 PASSES; proceeding.")

# ---------------- the detector, rebuilt ----------------
# SECOND INSTRUMENT CORRECTION, and the control caught this one too. Sampling "is the orbit
# bounded" on a grid CANNOT see the spectrum: it is a Cantor set of ZERO Lebesgue measure, so
# the grid fraction is ~0 for every lambda and the control passed VACUOUSLY -- satisfied by an
# instrument that finds nothing, which is exactly the MB12 failure the corpus names.
# The standard method instead uses the PERIODIC APPROXIMANTS: sigma_n = {E : |x_n(E)| <= 2},
# where x_n is the trace of the transfer matrix over the n-th Fibonacci block, obtained by
# iterating the trace map. Each sigma_n has positive measure, is a union of BANDS whose count
# is a Fibonacci number, and shrinks to the spectrum. That is detectable.

def traces(E, lam, n):
    """x_k(E) = tr M_{F_k} for k = 1..n, by the full-trace map."""
    x, y, z = (E - lam), E, 2.0 + 0j
    out = []
    for _ in range(n):
        out.append(x)
        x, y, z = x*y - z, x, y
    return out

def sigma_n(lam, grid, n):
    """|x_n(E)| <= 2 on the grid."""
    xs = np.empty(len(grid), dtype=complex)
    x = (grid - lam); y = grid.astype(complex); z = np.full(len(grid), 2.0+0j)
    for _ in range(n):
        x, y, z = x*y - z, x, y
        with np.errstate(over='ignore', invalid='ignore'):
            x = np.where(np.isfinite(x), x, np.inf)
    return np.abs(x) <= 2.0

def components(mask):
    d = np.diff(np.concatenate(([0], mask.astype(np.int8), [0])))
    return int((d == 1).sum())

# ---------------- D-1: positive control at REAL lambda ----------------
print("\nD-1  POSITIVE CONTROL -- real lambda, the Damanik-Gorodetski regime")
print("     the approximant spectra sigma_n must be unions of FIBONACCI-many bands with")
print("     measure shrinking to zero. A control that only checks 'measure is small' is")
print("     vacuous -- an instrument returning nothing would pass it.")
FIB = [1,2,3,5,8,13,21,34,55,89]
grid = np.linspace(-6, 6, 400001)
lam = 2.0
band_ok = True; meas = []
print(f"     lambda = {lam}:")
for n in range(3, 10):
    m = sigma_n(lam, grid, n)
    c = components(m); f = m.mean()*12.0
    hit = c in FIB
    band_ok &= hit
    meas.append(f)
    print(f"        n={n}  bands={c:<4} {'(Fibonacci)' if hit else '(NOT Fibonacci)'}   measure={f:.5f}")
shrink = all(meas[i+1] <= meas[i] + 1e-9 for i in range(len(meas)-1)) and meas[-1] < meas[0]/4
nonempty = meas[-1] > 0
print(f"     bands are Fibonacci: {band_ok} | measure shrinks: {shrink} | NON-EMPTY: {nonempty}")
D1 = "D1-REPRODUCES" if (band_ok and shrink and nonempty) else "D1-FAILS"
print(f"     OUTCOME: {D1}")
assert D1 == "D1-REPRODUCES", "control failed -- no object result may be reported"

# ---------------- D-2: the object ----------------
lam_obj = cmath.sqrt(kappa - 2)
print(f"\nD-2  THE OBJECT -- lambda forced by kappa = lambda^2 + 2: {lam_obj:.10f}")
print(f"     kappa - 2 = {kappa-2:.12f}   omega^2 = {w**2:.12f}   match: {abs((kappa-2)-w**2)<1e-13}")
print(f"     => lambda = omega EXACTLY, |lambda| = {abs(lam_obj):.12f} -- a sixth root of unity")
E0 = complex(0.3, 0.2)
print(f"     I at the initial point equals kappa: {abs(I(E0-lam_obj, E0, 2+0j) - kappa):.2e}")

def sigma_grid(lam, n, lo=-6, hi=6, N=600):
    re = np.linspace(lo, hi, N); im = np.linspace(lo, hi, N)
    RE, IM = np.meshgrid(re, im); E = RE + 1j*IM
    x = (E - lam); y = E.astype(complex); z = np.full(E.shape, 2.0+0j)
    for _ in range(n):
        with np.errstate(over='ignore', invalid='ignore'):
            x, y, z = x*y - z, x, y
            x = np.where(np.isfinite(x), x, np.inf)
    return np.abs(x) <= 2.0

def boxdim2(M):
    n = M.shape[0]; pts = []
    for s in (2,3,4,6,8,12,16,24):
        if n % s: continue
        b = M[:n//s*s,:n//s*s].reshape(n//s, s, n//s, s).any(axis=(1,3)).sum()
        if b > 0: pts.append((math.log(1.0/s), math.log(b)))
    if len(pts) < 3: return float('nan')
    xs = np.array([p[0] for p in pts]); ys = np.array([p[1] for p in pts])
    # SIGN: N(eps) ~ eps^-d, so log N vs log(1/eps) has slope +d. The minus sign was a bug
    # (it reported negative dimensions, which is what made D-2 read DEGENERATE).
    return float(np.polyfit(xs, ys, 1)[0])

for n in (6, 8, 10):
    M = sigma_grid(lam_obj, n)
    print(f"     n={n}: area fraction {M.mean():.5f}   box-dim {boxdim2(M):.3f}")
Mobj = sigma_grid(lam_obj, 10)
frac = Mobj.mean(); d_obj = boxdim2(Mobj)
inter = (Mobj[1:-1,1:-1] & Mobj[:-2,1:-1] & Mobj[2:,1:-1] & Mobj[1:-1,:-2] & Mobj[1:-1,2:]).sum()
print(f"     n=10 final: fraction {frac:.5f}  interior cells {inter}  box-dim {d_obj:.3f}")
D2 = "D2-STRUCTURED" if (0 < frac < 0.5 and 0.0 < d_obj < 2.0) else "D2-DEGENERATE"
print(f"     OUTCOME: {D2}")

# ---------------- D-3: same-modulus controls ----------------
print(f"\nD-3  SAME-MODULUS CONTROLS -- kappa = sqrt(3) e^(i theta); the object is theta = pi/6")
rows = []
for name, th in [("0 (real)",0.0),("pi/12",math.pi/12),("pi/6 = OBJECT",math.pi/6),
                 ("pi/4",math.pi/4),("pi/3",math.pi/3),("pi/2",math.pi/2),("2pi/3",2*math.pi/3)]:
    k = math.sqrt(3)*cmath.exp(1j*th); l = cmath.sqrt(k-2)
    Mc = sigma_grid(l, 10, N=400)
    rows.append((name, Mc.mean(), boxdim2(Mc)))
    print(f"     theta = {name:<14} fraction {rows[-1][1]:.5f}   box-dim {rows[-1][2]:.3f}")
dims = [r[2] for r in rows if not math.isnan(r[2])]
obj = [r for r in rows if "OBJECT" in r[0]][0]
med = float(np.median(dims)); spread = max(dims)-min(dims)
outlier = abs(obj[2]-med) > spread/2 if spread > 1e-9 else False
print(f"     object box-dim {obj[2]:.3f} | control median {med:.3f} | spread {spread:.3f}")
D3 = "D3-SPECIFIC" if outlier else "D3-GENERIC"
print(f"     OUTCOME: {D3}")

print("\n" + "="*78)
print(f"SUMMARY: D-0 PASS | {D1} | {D2} | {D3}")
print("FENCE: a numerical picture is not a theorem. This says whether the object's cocycle")
print("has the SHAPE a Damanik-Gorodetski result describes, which nobody had looked at.")
print("="*78)
