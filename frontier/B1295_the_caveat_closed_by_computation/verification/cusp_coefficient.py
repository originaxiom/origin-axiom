"""B1295 / D4(a) -- THE COEFFICIENT c_(+-2,0) AND THE SIGN PARTITION OF THE CUSP.

Runs the collocation solver (harmonic_generator.py) at three resolutions, finds the eight cusp isometries of m004
numerically (elements of the normaliser of Gamma fixing infinity), DERIVES the symmetry-allowed Fourier subspace
from those maps, checks the solved coefficients against it (every forbidden mode at noise, every allowed orbit
populated), and computes the sign partition of the radial component g = d_t psi on the horotorus at the maximal
cusp height t = 1 (and above/below), with the Euler characteristic of each sign region computed on the torus.

Index convention here: mode (m1, m2) <-> exp(2 pi i (m1 x + m2 y / (2 sqrt 3))), m1 along the MERIDIAN
(x, translation A), m2 along the LONGITUDE (y, translation T = 2 sqrt3 i).  The SM seat's addendum indexes
(k along lambda, l along mu), so the seat's (+-2, 0) is (m1, m2) = (0, +-2) here.
"""
import json, sys, itertools
import numpy as np
from scipy.special import k0, k1
from scipy import ndimage
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import harmonic_generator as H

OUT = {}
FAIL = []
def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)

tau, chiT, w0, nfound = H.find_cusp_lattice()
lat = H.Lattice(tau, chiT)
moves = H.build_moves()
print(f"cusp: tau = {tau.imag:.12f} i (word {w0}), chi(T) = {chiT}; {len(moves)} moves")
ok(abs(tau - 2j * np.sqrt(3)) < 1e-9 and chiT == 0, "tau = 2 sqrt3 i and chi(T) = 0 (T is the longitude: class 0 in H_1)")

# ------------------------------------------------------------------ 1. convergence
print("\n1. collocation at four resolutions (Rcut, Y, npts); the R=10 solve is final, R=6 -> R=10 gives the error bar")
runs = {}
for (R, Y, n) in [(4.0, 0.55, 500), (5.0, 0.5, 900), (6.0, 0.5, 1400), (10.0, 0.45, 3200)]:
    c, modes, info = H.solve(lat, moves, Y, R, n, seed=int(R))
    runs[(R, Y, n)] = (c, info)
    print(f"  R={R} Y={Y} n={n}: eq {info['n_eq']} unk {info['n_unknown']} rank {info['rank']} resid_rms {info['resid_rms']:.2e} max {info['resid_max']:.2e}")
key_final = (10.0, 0.45, 3200)
c, info = runs[key_final]
OUT["solve"] = {str(k): v[1] for k, v in runs.items()}
ok(info["resid_rms"] < 1e-9, "final solve (R=10) residual rms < 1e-9")
watch = [(0, 2), (1, 2), (1, -2), (1, 4), (1, -4), (0, 6), (2, 2), (2, -2), (0, 1), (1, 0), (0, 4), (2, 0), (2, 1), (1, 6), (0, 3), (1, 1)]
print("  mode      " + "   ".join(f"R={k[0]}" .ljust(26) for k in runs))
for m in watch:
    print(f"  {str(m):9s} " + "   ".join(f"{runs[k][0][m].real:+.7f}{runs[k][0][m].imag:+.7f}i" for k in runs))
OUT["coefficients_final"] = {f"{k[0]},{k[1]}": [v.real, v.imag] for k, v in sorted(c.items())}
c02 = c[(0, 2)]
d45 = abs(runs[(4.0, 0.55, 500)][0][(0, 2)] - runs[(5.0, 0.5, 900)][0][(0, 2)])
d56 = abs(runs[(5.0, 0.5, 900)][0][(0, 2)] - runs[(6.0, 0.5, 1400)][0][(0, 2)])
d610 = abs(runs[(6.0, 0.5, 1400)][0][(0, 2)] - c02)
print(f"  c_(0,2): {c02.real:+.10f} {c02.imag:+.10f} i ;  |delta| R4->R5 {d45:.1e}, R5->R6 {d56:.1e}, R6->R10 {d610:.1e}")
print(f"  ==> c_0 = c_(0,2) = {c02.imag:+.9f} i  +- {max(d610, 1e-9):.0e}   (seat convention c_(+-2,0) = -+ {abs(c02.imag):.9f} i)")
OUT["c0"] = {"value_imag": c02.imag, "error_bar": float(max(d610, 1e-9)), "deltas": {"R4_R5": d45, "R5_R6": d56, "R6_R10": d610}}
ok(d56 < 1e-6, "c_(0,2) stable to 1e-6 between R=5 and R=6")
ok(d610 < 1e-7, "c_(0,2) stable to 1e-7 between R=6 and R=10 (the error bar)")
ok(abs(c02) > 1.0 and abs(c02.real) < 1e-4, "c_(0,2) is O(1) and pure imaginary (a sine in the longitude coordinate)")

# ------------------------------------------------------------------ 2. the eight cusp isometries
print("\n2. cusp isometries: normaliser elements fixing infinity, z -> alpha z + beta or alpha conj(z) + beta")
def gmap(alpha, conj, beta):
    def f(z, t):
        zz = np.conj(z) if conj else z
        return alpha * zz + beta, t
    def finv(z, t):
        zz = alpha * (z - beta)
        return (np.conj(zz) if conj else zz), t
    return f, finv

rng = np.random.default_rng(11)
test_pts = [(complex(rng.uniform(-0.5, 0.5), rng.uniform(-1.7, 1.7)), rng.uniform(1.05, 1.3)) for _ in range(6)]
def same_orbit(P, Q):
    z1, t1, _ = H.reduce_pt(lat, moves, P[0], P[1])
    z2, t2, _ = H.reduce_pt(lat, moves, Q[0], Q[1])
    if abs(t1 - t2) > 1e-8:
        return False
    d = lat.coords(z1 - z2)
    return np.abs(d - np.round(d)).max() < 1e-7

isos = []
for alpha in (1, -1):
    for conj in (False, True):
        for i in range(8):
            for j in range(8):
                beta = i / 8 + (j / 8) * tau
                f, finv = gmap(alpha, conj, beta)
                good = True
                for gen in (H.B, H.Bi):
                    for P in test_pts:
                        Q = f(*H.apply_m(gen, *finv(*P)))
                        if not same_orbit(P, Q):
                            good = False
                            break
                    if not good:
                        break
                if good:
                    isos.append((alpha, conj, i / 8, j / 8))
print(f"  found {len(isos)} isometries (beta searched on the (1/8)-grid of the torus):")
for a, cj, bx, by in isos:
    kind = ("conj " if cj else "     ")
    print(f"    alpha={a:+d} {kind} beta = {bx} + {by} tau     (H_1 action: mu -> {a:+d} mu, lambda -> {(-a if cj else a):+d} lambda)")
OUT["isometries"] = [{"alpha": a, "conj": cj, "beta_x": bx, "beta_y_over_tau": by} for a, cj, bx, by in isos]
ok(len(isos) == 8, "exactly eight cusp isometries (D_4)")
n_or_rev = sum(1 for a, cj, bx, by in isos if cj)
ok(n_or_rev == 4, "four of them orientation-reversing (conjugating type)")
# T = the half-translation (alpha=1, no conj, beta != 0)
T_half = [(bx, by) for a, cj, bx, by in isos if a == 1 and not cj and (bx, by) != (0.0, 0.0)]
print(f"  the half-translation (period-2 rotation r^2 on the cusp): beta = {T_half}")
ok(T_half == [(0.0, 0.5)], "r^2 acts on the cusp as translation by tau/2 (half the LONGITUDE)")

# ------------------------------------------------------------------ 3. the allowed subspace, derived
print("\n3. symmetry-allowed Fourier subspace derived from the eight maps (c_{g.nu} e^{2 pi i <g.nu, beta>} = alpha c_nu)")
Rsym = 3.0
allm = [(m1, m2) for (m1, m2, mu) in lat.modes(Rsym)]
idx = {m: i for i, m in enumerate(allm)}
def act(g, m):
    a, cj, bx, by = g
    m1, m2 = m
    if cj:
        m2 = -m2
    return (a * m1, a * m2)
def phase(g, m):
    a, cj, bx, by = g
    m1, m2 = m
    beta = bx + by * tau
    mu = m1 * lat.u1 + m2 * lat.u2
    return np.exp(2j * np.pi * (mu.real * beta.real + mu.imag * beta.imag))
# unknowns: complex c_m for all m (both signs); constraints over C: c_{g m} phase(g, g m) - alpha c_m = 0; reality: c_{-m} = conj(c_m) handled by
# working over R with (Re, Im) blocks.
N = len(allm)
rows = []
def cplx_row(coeffs):
    """coeffs: dict m -> complex a_m meaning sum a_m c_m = 0; returns two real rows over (Re c, Im c)."""
    r1 = np.zeros(2 * N); r2 = np.zeros(2 * N)
    for m, a in coeffs.items():
        i = idx[m]
        r1[2 * i] += a.real; r1[2 * i + 1] += -a.imag     # real part of a c
        r2[2 * i] += a.imag; r2[2 * i + 1] += a.real      # imag part
    return [r1, r2]
for g in isos:
    for m in allm:
        gm = act(g, m)
        if gm not in idx:
            continue
        coeffs = {}
        coeffs[gm] = coeffs.get(gm, 0) + phase(g, gm)
        coeffs[m] = coeffs.get(m, 0) - g[0]                  # accumulate: gm == m for the identity, T and self-mapped modes
        rows += cplx_row(coeffs)
for m in allm:
    mm = (-m[0], -m[1])
    if mm in idx:
        # c_{-m} - conj(c_m) = 0 : Re: Re c_{-m} - Re c_m = 0 ; Im: Im c_{-m} + Im c_m = 0
        r1 = np.zeros(2 * N); r2 = np.zeros(2 * N)
        r1[2 * idx[mm]] += 1; r1[2 * idx[m]] -= 1
        r2[2 * idx[mm] + 1] += 1; r2[2 * idx[m] + 1] += 1
        rows += [r1, r2]
Msys = np.array(rows)
u, s, vt = np.linalg.svd(Msys)
null = vt[np.sum(s > 1e-9):]
print(f"  modes |mu| <= {Rsym}: {N}; constraint rows {Msys.shape[0]}; allowed real dimension = {null.shape[0]}")
# orbits under the group generated by the maps m -> g.m and m -> -m
def orbit(m):
    seen = {m}; stack = [m]
    while stack:
        x = stack.pop()
        for g in isos:
            y = act(g, x)
            if y not in seen:
                seen.add(y); stack.append(y)
        y = (-x[0], -x[1])
        if y not in seen:
            seen.add(y); stack.append(y)
    return tuple(sorted(seen))
orbits = sorted({orbit(m) for m in allm}, key=lambda o: abs(o[0][0] * lat.u1 + o[0][1] * lat.u2))
allowed = {}
for o in orbits:
    cols = [2 * idx[m] + k for m in o if m in idx for k in (0, 1)]
    sub = null[:, cols]
    dim = int(np.linalg.matrix_rank(sub, tol=1e-9)) if sub.size else 0
    allowed[o] = dim
mu_of = lambda m: abs(m[0] * lat.u1 + m[1] * lat.u2)
print("  orbit (representative, meridian-first)   |mu|    allowed dim   observed max|c| in orbit (R=10 solve)")
seat_table = {(0, 1): 0, (0, 2): 1, (0, 3): 0, (1, 0): 0, (1, 1): 0, (1, 2): 1}   # seat's table transcribed to meridian-first
import divisor_law as DL
NOISE = 1e-6
forbidden_populated, vanishing = [], []
obs_of = {}
for o in orbits:
    rep = max(o)
    obs = max(abs(c[m]) if m in c else abs(c[(-m[0], -m[1])]) for m in o if (m in c or (-m[0], -m[1]) in c))
    obs_of[o] = obs
    flag = ""
    if allowed[o] == 0 and obs >= NOISE:
        flag = "   <-- FORBIDDEN BUT POPULATED"; forbidden_populated.append((rep, obs))
    if allowed[o] > 0 and obs < NOISE:
        # symmetry allows it, the solution does not use it: the divisor law predicts S(nu) = 0 exactly when sqrt(-3) | nu
        nu = (rep[1] // 2, -rep[0]) if rep[1] % 2 == 0 else None
        Snu = DL.S(nu) if nu is not None else None
        flag = f"   allowed but vanishing: nu = {nu}, S(nu) = {Snu}"; vanishing.append((rep, nu, Snu, obs))
    print(f"  {str(rep):10s} (orbit size {len(o):2d})   {mu_of(rep):.4f}    {allowed[o]}             {obs:.3e}{flag}")
OUT["allowed_orbits"] = [{"rep": list(max(o)), "size": len(o), "abs_mu": mu_of(max(o)), "allowed_dim": allowed[o], "observed_max_abs_c": obs_of[o]} for o in orbits]
OUT["allowed_but_vanishing"] = [{"rep": list(r), "nu": list(nu) if nu else None, "S": Snu, "observed": obs} for r, nu, Snu, obs in vanishing]
ok(not forbidden_populated, f"every symmetry-forbidden orbit is at noise (|c| < {NOISE:g}) for |mu| <= 3")
ok(len(vanishing) >= 1 and all(nu is not None and Snu == 0.0 and DL.divides((0, 1), nu) for _, nu, Snu, _ in vanishing),
   f"the {len(vanishing)} allowed-but-vanishing orbits are exactly the ones the divisor law predicts zero (sqrt(-3) | nu): "
   + ", ".join(f"{r}->nu={nu}" for r, nu, _, _ in vanishing))
for m, d in seat_table.items():
    ok(allowed[orbit(m)] == d, f"seat's table entry (meridian-first {m}) allowed dim = {d} reproduced by the derived subspace")
# also: the solved coefficient vector lies in the allowed subspace
vec = np.zeros(2 * N)
for m in allm:
    cm = c[m] if m in c else np.conj(c[(-m[0], -m[1])])
    vec[2 * idx[m]] = cm.real; vec[2 * idx[m] + 1] = cm.imag
proj = null.T @ (null @ vec)
print(f"  |c - P_allowed c| / |c| = {np.linalg.norm(vec - proj) / np.linalg.norm(vec):.2e}")
ok(np.linalg.norm(vec - proj) / np.linalg.norm(vec) < 1e-5, "the solved coefficient vector lies in the derived allowed subspace")

# ------------------------------------------------------------------ 4. the sign partition of the radial component
print("\n4. sign partition of g = d_t psi on the horotorus (t = maximal cusp height 1, and around it)")
def radial_grid(c, t, n1=192, n2=None):
    if n2 is None:
        n2 = int(round(n1 * abs(tau)))
    x = (np.arange(n1) + 0.5) / n1
    y = (np.arange(n2) + 0.5) / n2 * tau.imag
    X, Yg = np.meshgrid(x, y, indexing="ij")
    g = np.zeros_like(X)
    for (m1, m2), cm in c.items():
        mu = m1 * lat.u1 + m2 * lat.u2
        a = 2 * np.pi * abs(mu)
        th = 2 * np.pi * (mu.real * X + mu.imag * Yg)
        g += 2 * (cm.real * np.cos(th) - cm.imag * np.sin(th)) * (-a * t * k0(a * t))
    return g
def torus_components(S):
    lab, n = ndimage.label(S)
    parent = list(range(n + 1))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)
    for a, b in zip(lab[0, :], lab[-1, :]):
        if a and b:
            union(a, b)
    for a, b in zip(lab[:, 0], lab[:, -1]):
        if a and b:
            union(a, b)
    roots = {}
    out = np.zeros_like(lab)
    for l in range(1, n + 1):
        r = find(l)
        roots.setdefault(r, len(roots) + 1)
        out[lab == l] = roots[r]
    return out, len(roots)
def torus_chi(S):
    F = int(S.sum())
    adj = int((S & np.roll(S, 1, 0)).sum() + (S & np.roll(S, 1, 1)).sum())
    V = int((S | np.roll(S, 1, 0) | np.roll(S, 1, 1) | np.roll(np.roll(S, 1, 0), 1, 1)).sum())
    return V - 3 * F + adj
def partition(c, t):
    g = radial_grid(c, t)
    res = {}
    for name, S in (("plus", g > 0), ("minus", g < 0)):
        lab, n = torus_components(S)
        chis = [torus_chi(lab == k) for k in range(1, n + 1)]
        res[name] = {"components": n, "chi_each": chis, "chi_total": int(sum(chis)), "area_fraction": float(S.mean())}
    return res, g
parts = {}
for t in (0.6, 0.7, 0.8, 0.9, 1.0, 1.25, 1.5, 2.0, 3.0):
    res, g = partition(c, t)
    parts[t] = res
    print(f"  t = {t:4.2f}: {{g>0}}: {res['plus']['components']} components, chi {res['plus']['chi_each']} ; {{g<0}}: {res['minus']['components']} components, chi {res['minus']['chi_each']} ; max|g| {np.abs(g).max():.3e}")
OUT["partition"] = {str(t): v for t, v in parts.items()}
p1 = parts[1.0]
ok(p1["plus"]["components"] == 2 and p1["plus"]["chi_each"] == [0, 0] and p1["minus"]["components"] == 2 and p1["minus"]["chi_each"] == [0, 0],
   "at the maximal cusp (t = 1): {g>0} = two annuli, {g<0} = two annuli  =>  chi(d+M) = 0")
ok(all(parts[t]["plus"]["chi_total"] == 0 and parts[t]["plus"]["components"] == 2 for t in (1.0, 1.25, 1.5, 2.0, 3.0)),
   "the annular partition persists on every embedded horotorus t >= 1")
# amplitude ratio at t=1 of the first mixed pair to the leading mode, in the radial component
def amp(m, t):
    mu = m[0] * lat.u1 + m[1] * lat.u2; a = 2 * np.pi * abs(mu)
    return 2 * abs(c[m]) * a * t * k0(a * t)
ratio = (amp((1, 2), 1.0) + amp((1, -2), 1.0)) / amp((0, 2), 1.0)
print(f"  radial amplitude ratio at t=1: [(1,2)+(1,-2)] / (0,2) = {ratio:.4f}   (seat's convention: (+-2,+-1) pair / (+-2,0))")
OUT["mixed_over_leading_at_t1"] = ratio
# zero set through the corners: g(x, y) at the inversion fixed points (0,0),(1/2,0),(0,tau/2),(1/2,tau/2) and the theta' corners at y = tau/4, 3tau/4
corner_vals = []
for bx in (0.0, 0.25, 0.5, 0.75):
    for by in (0.0, 0.5):
        pass
g1 = radial_grid(c, 1.0, n1=64, n2=None)
# evaluate exactly at the corners instead of on the grid
def g_at(z, t):
    return H.radial(lat, c, z, t)
corners = [(bx, by) for bx in (0.0, 0.5) for by in (0.0, 0.25, 0.5, 0.75)]   # meridian coordinate bx, longitude fraction by
vals = [g_at(bx + by * tau, 1.0) for bx, by in corners]
print(f"  g at the eight corners (x in {{0,1/2}}, y/|tau| in {{0,1/4,1/2,3/4}}) at t=1: max |g| = {max(abs(v) for v in vals):.2e} (max on torus {np.abs(g1).max():.3e})")
ok(max(abs(v) for v in vals) < 1e-6 * np.abs(g1).max(), "the zero set of g passes through all eight corners (the inversions' fixed points on the cusp)")

# ------------------------------------------------------------------ 5. the divisor law (CONJECTURE; found here, pre-registered out-of-sample PASS)
print("\n5. the divisor law c(nu) = c0 S(nu), nu = a + b sqrt(-3) <-> (m1, m2) = (-b, 2a)   [CONJECTURE -- divisor_law.py]")
NMAX, TOL = 200, 5e-3
nt, nf, worst, rows = DL.compare(c, c02, NMAX, TOL)
zeros = [r for r in rows if r[3] == 0.0]
worst_zero = max((r[6] for r in zeros), default=0.0)
print(f"  even-m2 modes with N(nu) <= {NMAX}: {nt}; |c/c0 - S(nu)| > {TOL:g}: {nf}; worst {worst:.1e}; predicted exact zeros: {len(zeros)} (worst {worst_zero:.1e})")
print("  spot values: " + ", ".join(f"S({n})={DL.S(n):+.4f}" for n in [(1,0),(3,0),(5,0),(7,0),(9,0),(2,0),(4,0),(0,1),(1,1),(2,1),(1,2)]))
ok(nt >= 150 and nf == 0, f"the divisor law holds on all {nt} solved even-m2 modes with N(nu) <= {NMAX} to {TOL:g} (zero fitted parameters)")
ok(len(zeros) >= 20 and worst_zero < TOL, f"all {len(zeros)} predicted zeros (sqrt(-3) | nu or nu a power of 2) vanish to {TOL:g}")
J = json.load(open(Path(__file__).with_name("law_outofsample.json")))
print(f"  pre-registered out-of-sample test on file: {J['n_out']} modes 108 < N <= 200 at R=10, eps_in {J['eps_in']:.1e}, tol {J['tol']}, worst {J['worst_out']:.1e}: {J['verdict']}")
ok(J["verdict"] == "PASS" and J["n_out"] == 88 and J["worst_out"] < J["tol"], "the pre-registered out-of-sample test (law_outofsample.py) is PASS on file, 88/88")
OUT["divisor_law"] = {"status": "CONJECTURE", "n_tested": nt, "n_fail": nf, "worst": worst, "n_predicted_zeros": len(zeros), "worst_zero": worst_zero,
                      "tol": TOL, "nmax": NMAX, "preregistered": {k: J[k] for k in ("n_out", "eps_in", "tol", "worst_out", "verdict")}}
# bounded attempt at a closed form for |c0| -- LINEAR integer relations only (PSLQ), small coefficients.
# (mpmath.identify's default fractional-power search returns dozens of numerological "forms" at 10 digits; refused.)
import mpmath as mp
mp.mp.dps = 20
x = mp.mpf(repr(abs(c02.imag)))
L2 = mp.dirichlet(2, [0, 1, -1])                    # L(2, chi_{-3}) = 0.78130241289648...
consts = {"pi": mp.pi, "sqrt3": mp.sqrt(3), "pi^2": mp.pi**2, "log2": mp.log(2), "log3": mp.log(3),
          "L2chi3": L2, "zetaK2": mp.pi**2 / 6 * L2, "G": mp.catalan, "zeta3": mp.zeta(3), "vol_m004": mp.mpf("2.029883212819307")}
MAXC, PTOL = 12, mp.mpf("1e-9")
hits = []
for k in (1, 2):
    for names in itertools.combinations(consts, k):
        vec = [x, mp.mpf(1)] + [consts[n] for n in names]
        r = mp.pslq(vec, tol=PTOL, maxcoeff=MAXC, maxsteps=10000)
        if r and r[0] != 0:
            hits.append((names, [int(v) for v in r]))
    for names in itertools.combinations(consts, k):     # also x * const = rational combination (x/c linear)
        for n0 in names:
            vec = [x * consts[n0], mp.mpf(1)] + [consts[n] for n in names if n != n0]
            r = mp.pslq(vec, tol=PTOL, maxcoeff=MAXC, maxsteps=10000)
            if r and r[0] != 0:
                hits.append((("x*" + n0,) + tuple(n for n in names if n != n0), [int(v) for v in r]))
print(f"  closed form for |c0| = {mp.nstr(x, 11)}: PSLQ over [x or x*c, 1, <= 2 of {list(consts)}], |coeff| <= {MAXC}, tol 1e-9: "
      + (f"{len(hits)} relation(s): {hits}" if hits else "NONE -- c0 closed form OPEN (bounded search, negative)"))
OUT["c0_identify"] = {"value": float(x), "constants": list(consts), "maxcoeff": MAXC, "tol": 1e-9,
                      "hits": [[list(n), r] for n, r in hits], "verdict": "OPEN" if not hits else "CANDIDATES"}

OUT["c_02_seat_pm20"] = [c02.real, c02.imag]
OUT["FAIL"] = FAIL
json.dump(OUT, open(Path(__file__).with_name("cusp_coefficient.json"), "w"), indent=1, default=str)
print("\nSELFTEST:", "PASS" if not FAIL else f"FAIL ({len(FAIL)})")
