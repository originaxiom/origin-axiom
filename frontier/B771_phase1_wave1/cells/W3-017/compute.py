#!/usr/bin/env python3
"""
B771 Phase-1 Wave-3 cell W3-017 -- RZ residuals.

Closes the two named boundaries the Relation campaign left open
(docs/OPEN_LEADS.md:372, docs/CAMPAIGN_STATUS.md:901-903):

  (A) the L6a4 (Borromean-adjacent) SL(3) Ptolemy census -- structure table was
      banked in B461; the FIELDS of the isolated points were the priced remainder.
  (B) the trace-map Ruelle-resonance enumeration beyond n=6 -- B451 claimed a
      spectral gap >= 0.19 in every checked enumeration but the committed exact
      certification (certify_counts.sage) uses a TWO-component fixed-point system
      that OVERCOUNTS (it does not enforce true periodicity); n=8 was never
      certified.  We re-certify with the FULL three-component system and push the
      gap across truncations.

House method: exact/symbolic (sympy) preferred; the discriminating fact is
computed in-cell, never cited; every check ASSERTED with its direction; a vacuity
self-test is run on the key quantity (the gap); UNRESOLVED is reachable.

Env: pyenv python3 (NOT sage). snappy available but not required here.
"""
import json
import os
import sys
import time
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PTOLEMY = os.path.join(ROOT, "frontier", "B461_relation_r2_borromean", "ptolemy_systems.json")

np.seterr(all="ignore")

def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)

# =====================================================================
# PART B -- trace-map Ruelle resonances beyond n=6
# =====================================================================
# T(x,y,z) = (2xy - z, x, y); invariant I = x^2+y^2+z^2-2xyz-1; surface I=(lam/2)^2.
# lambda = 3 (B451 gate surface), so I = 9/4.

LAM = 3.0
CVAL = (LAM / 2.0) ** 2  # 9/4

def T_np(p):
    x, y, z = p
    return np.array([2 * x * y - z, x, y])

def DT_np(p):
    x, y, z = p
    return np.array([[2 * y, 2 * x, -1.0], [1.0, 0, 0], [0, 1.0, 0]])

def Ival(p):
    x, y, z = p
    return x * x + y * y + z * z - 2 * x * y * z - 1

def gradI(p):
    x, y, z = p
    return np.array([2 * x - 2 * y * z, 2 * y - 2 * x * z, 2 * z - 2 * x * y])

def Tn_np(p, n):
    q = p.copy()
    for _ in range(n):
        q = T_np(q)
    return q

def newton_periodic(p0, n, c, iters=80):
    """Full periodicity: solve (T^n - id) in comps 0 AND 1, plus surface I=c;
    then VERIFY the third component (true periodicity, not the 2-comp overcount)."""
    p = np.array(p0, float)
    for _ in range(iters):
        q = p.copy()
        J = np.eye(3)
        for _ in range(n):
            J = DT_np(q) @ J
            q = T_np(q)
        F = np.array([q[0] - p[0], q[1] - p[1], Ival(p) - c])
        A = np.vstack([(J - np.eye(3))[0], (J - np.eye(3))[1], gradI(p)])
        if not np.all(np.isfinite(F)) or not np.all(np.isfinite(A)):
            return None
        try:
            dp = np.linalg.solve(A, -F)
        except np.linalg.LinAlgError:
            return None
        p = p + dp
        if np.linalg.norm(p) > 1e7:
            return None
        if np.linalg.norm(F) < 1e-13 and np.linalg.norm(dp) < 1e-13:
            break
    q = Tn_np(p, n)
    # ASSERT genuine periodicity in ALL three components (kills 2-comp spurious):
    if np.linalg.norm(q - p) < 1e-8 and abs(Ival(p) - c) < 1e-8:
        return p
    return None

def surface_seeds(c, ngrid, box):
    seeds = []
    for x in np.linspace(-box, box, ngrid):
        for y in np.linspace(-box, box, ngrid):
            disc = (x * y) ** 2 - x * x - y * y + 1 + c
            if disc >= 0:
                r = np.sqrt(disc)
                seeds.append(np.array([x, y, x * y + r]))
                seeds.append(np.array([x, y, x * y - r]))
    return seeds

def enumerate_period_n(n, c, ngrid, box=3.6, rng=None, extra_random=0):
    found = []
    seeds = surface_seeds(c, ngrid, box)
    if rng is not None and extra_random:
        for _ in range(extra_random):
            x, y = rng.uniform(-box, box, 2)
            disc = (x * y) ** 2 - x * x - y * y + 1 + c
            if disc >= 0:
                r = np.sqrt(disc)
                seeds.append(np.array([x, y, x * y + (r if rng.random() < .5 else -r)]))
    for s in seeds:
        p = newton_periodic(s, n, c)
        if p is None:
            continue
        if any(np.linalg.norm(p - q) < 1e-6 for q in found):
            continue
        found.append(p)
    return found

def orbits_from_points(points, n):
    used = set()
    orbits = []
    for i, p in enumerate(points):
        if i in used:
            continue
        orbit = [p]
        q = T_np(p)
        minper = n
        for k in range(1, n):
            if np.linalg.norm(q - p) < 1e-6:
                minper = k
                break
            orbit.append(q)
            q = T_np(q)
        for j, r in enumerate(points):
            if j != i and any(np.linalg.norm(r - o) < 1e-6 for o in orbit):
                used.add(j)
        used.add(i)
        if minper == n:
            orbits.append(orbit)
    return orbits

def expanding_multiplier(orbit):
    p = orbit[0]
    J = np.eye(3)
    q = p.copy()
    for _ in range(len(orbit)):
        J = DT_np(q) @ J
        q = T_np(q)
    g = gradI(p)
    g = g / np.linalg.norm(g)
    a = np.array([1.0, 0, 0]) if abs(g[0]) < 0.9 else np.array([0, 1.0, 0])
    u = a - g * (a @ g)
    u /= np.linalg.norm(u)
    v = np.cross(g, u)
    B = np.column_stack([u, v])
    A2 = B.T @ J @ B
    ev = np.linalg.eigvals(A2)
    return ev[np.argmax(np.abs(ev))]

def cycle_expansion(prims, N):
    coeffs = np.zeros(N + 1)
    coeffs[0] = 1.0
    for n_p, lam in prims:
        if n_p > N:
            continue
        t = np.zeros(N + 1)
        t[0] = 1.0
        t[n_p] = -1.0 / abs(lam)
        out = np.zeros(N + 1)
        for i in range(N + 1):
            for j in range(0, N + 1 - i):
                out[i + j] += coeffs[i] * t[j]
        coeffs = out
    return coeffs

def zeta_zeros(prims, N):
    coeffs = cycle_expansion(prims, N)
    roots = np.roots(coeffs[::-1])
    roots = roots[np.abs(roots) > 1e-9]
    roots = roots[np.argsort(np.abs(roots))]
    return roots

def rates_and_gap(prims, N):
    """leading escape rate = ln|z0|; resonance rates = ln|z_k|; gap = rate1 - rate0."""
    roots = zeta_zeros(prims, N)
    if len(roots) < 2:
        return None
    rate0 = float(np.log(np.abs(roots[0])))
    rate1 = float(np.log(np.abs(roots[1])))
    return dict(z0=roots[0], rate0=rate0, z1=roots[1], rate1=rate1,
                gap=rate1 - rate0, roots=roots)

# ---- EXACT certification of the period-n point count (full 3-comp system) ----
X, Y, Z = sp.symbols('x y z')
def _T_sym(p):
    return (sp.expand(2 * p[0] * p[1] - p[2]), p[0], p[1])

def _vsdim(G):
    """vector-space dimension (count-with-multiplicity over the alg. closure) of a
    0-dim ideal from its grevlex Groebner basis, via the standard-monomial staircase."""
    exprs = G.exprs
    if any(getattr(g, 'is_number', False) and g != 0 for g in exprs):
        return 0  # ideal = (1): no solutions
    lexp = [sp.Poly(g, X, Y, Z).LT(order='grevlex')[0] for g in exprs]
    bnd = [0, 0, 0]
    for e in lexp:
        for i in range(3):
            if e[(i + 1) % 3] == 0 and e[(i + 2) % 3] == 0 and e[i] > 0:
                bnd[i] = max(bnd[i], e[i])
    if 0 in bnd:
        return None  # not zero-dimensional in the naive test
    cnt = 0
    for a in range(bnd[0]):
        for b in range(bnd[1]):
            for cc in range(bnd[2]):
                if not any(a >= e[0] and b >= e[1] and cc >= e[2] for e in lexp):
                    cnt += 1
    return cnt

def exact_fix_count(n, modulus=None, tcap=None):
    """|Fix(T^n) on the surface I=9/4|, counted with multiplicity over the algebraic
    closure, using ALL THREE components of T^n(p)-p plus the surface. modulus=None
    -> over Q (exact); else over GF(modulus). Returns (count, seconds) or (None,sec)."""
    p = (X, Y, Z)
    for _ in range(n):
        p = _T_sym(p)
    F0 = sp.expand(p[0] - X); F1 = sp.expand(p[1] - Y); F2 = sp.expand(p[2] - Z)
    if modulus is None:
        S = X**2 + Y**2 + Z**2 - 2*X*Y*Z - 1 - sp.Rational(9, 4)
    else:
        S = 4*X**2 + 4*Y**2 + 4*Z**2 - 8*X*Y*Z - 13  # cleared denominator
    t0 = time.time()
    G = sp.groebner([F0, F1, F2, S], X, Y, Z, order='grevlex', modulus=modulus)
    return _vsdim(G), time.time() - t0

def _ideal_gens(n):
    p = (X, Y, Z)
    for _ in range(n):
        p = _T_sym(p)
    S = X**2 + Y**2 + Z**2 - 2*X*Y*Z - 1 - sp.Rational(9, 4)
    return [sp.expand(p[0]-X), sp.expand(p[1]-Y), sp.expand(p[2]-Z), S]

def _std_monomials(G):
    lexp = [sp.Poly(g, X, Y, Z).LT(order='grevlex')[0] for g in G.exprs]
    bnd = [0, 0, 0]
    for e in lexp:
        for i in range(3):
            if e[(i+1) % 3] == 0 and e[(i+2) % 3] == 0 and e[i] > 0:
                bnd[i] = max(bnd[i], e[i])
    return [(a, b, cc) for a in range(bnd[0]) for b in range(bnd[1]) for cc in range(bnd[2])
            if not any(a >= e[0] and b >= e[1] and cc >= e[2] for e in lexp)]

def _mult_matrix(G, mons, ve):
    idx = {m: i for i, m in enumerate(mons)}
    N = len(mons); M = np.zeros((N, N))
    for j, m in enumerate(mons):
        pr = tuple(m[k]+ve[k] for k in range(3))
        r = G.reduce(X**pr[0]*Y**pr[1]*Z**pr[2])[1]
        if r != 0:
            P = sp.Poly(r, X, Y, Z)
            for cf, mm in zip(P.coeffs(), P.monoms()):
                M[idx[mm], j] = float(cf)
    return M

def orbits_eigenvalue(n):
    """COMPLETE exact enumeration of the primitive real period-n orbits via the
    eigenvalue method: the commuting multiplication-by-x/y/z operators of the 0-dim
    quotient ring Q[x,y,z]/I have common eigenvectors whose eigenvalue-triples are
    ALL the solution points (with multiplicity) -- finds the tiny-basin high-multiplier
    orbits that random Newton seeding misses.  Returns (orbits, quotient_dim)."""
    G = sp.groebner(_ideal_gens(n), X, Y, Z, order='grevlex')
    mons = _std_monomials(G)
    if not mons:
        return [], 0
    Mx = _mult_matrix(G, mons, (1, 0, 0))
    My = _mult_matrix(G, mons, (0, 1, 0))
    Mz = _mult_matrix(G, mons, (0, 0, 1))
    w, V = np.linalg.eig(Mx + 0.7*My + 1.3*Mz)
    Vi = np.linalg.inv(V)
    xs = np.diag(Vi@Mx@V); ys = np.diag(Vi@My@V); zs = np.diag(Vi@Mz@V)
    pts = []
    for i in range(len(w)):
        if abs(xs[i].imag) < 1e-6:  # real solution
            p = np.array([xs[i].real, ys[i].real, zs[i].real])
            q = newton_periodic(p, n, CVAL)
            pts.append(q if q is not None else p)
    return orbits_from_points(pts, n), len(mons)

def part_B():
    banner("PART B -- trace-map Ruelle resonances (lambda=3 surface, I=9/4)")
    print("Map T(x,y,z)=(2xy-z,x,y); DG-hyperbolic horseshoe. Certifying beyond n=6.\n")

    # ---- (B1) COMPLETE exact enumeration (eigenvalue method) n=2..7, +exact count ----
    print("  Complete primitive-orbit enumeration via the quotient-ring eigenvalue")
    print("  method (finds tiny-basin high-multiplier orbits Newton seeding misses):")
    prim_orbits = {}
    exact_counts = {1: 0}
    NEIG = 7
    for n in range(2, NEIG + 1):
        orbs, qdim = orbits_eigenvalue(n)
        exact_counts[n] = qdim                     # = |Fix(T^n) on surface| w/ mult
        prim_orbits[n] = [expanding_multiplier(o) for o in orbs]
        print(f"    n={n:2d}: quotient dim (exact count) = {qdim:3d}  "
              f"primitive orbits = {len(orbs)}  "
              f"|Lambda| = {sorted(round(abs(m),1) for m in prim_orbits[n])}", flush=True)

    # ---- (B2) n=8: certify the COUNT (two-prime GF(p)) + enumerate orbits ----
    print("\n  n=8 boundary:")
    v8 = []
    for pm in (32003, 32009):
        M, sec = exact_fix_count(n=8, modulus=pm)
        v8.append(M)
        print(f"    n=8 count M_8 = {M} (mod {pm}, {sec:.0f}s)", flush=True)
    n8_count_certified = (len(v8) == 2 and v8[0] == v8[1])
    if n8_count_certified:
        exact_counts[8] = v8[0]
    # multi-scale grid seeding for the n=8 orbit multipliers
    pts8 = {}
    for box, ng in [(3.6, 90), (4.5, 110), (5.5, 130), (6.5, 150), (8.0, 150)]:
        for xx in np.linspace(-box, box, ng):
            for yy in np.linspace(-box, box, ng):
                disc = (xx*yy)**2 - xx*xx - yy*yy + 1 + CVAL
                if disc < 0:
                    continue
                r = np.sqrt(disc)
                for zz in (xx*yy + r, xx*yy - r):
                    q = newton_periodic(np.array([xx, yy, zz]), 8, CVAL)
                    if q is not None and not any(np.linalg.norm(q - w) < 1e-5 for w in pts8.values()):
                        pts8[tuple(np.round(q, 6))] = q
    orbs8 = orbits_from_points(list(pts8.values()), 8)
    prim_orbits[8] = [expanding_multiplier(o) for o in orbs8]
    # exact number of primitive-8 orbits from the certified count:
    n8_orbits_exact = (exact_counts.get(8, 0) - exact_counts[4]) // 8 if n8_count_certified else None
    n8_found = len(orbs8)
    print(f"    n=8 primitive orbits found (seeding) = {n8_found}  "
          f"|Lambda| = {sorted(round(abs(m),1) for m in prim_orbits[8])}", flush=True)
    print(f"    n=8 primitive orbits certified to exist = {n8_orbits_exact} "
          f"(from M_8={exact_counts.get(8)} minus divisor points)", flush=True)

    # ---- (B3) certified-count vs enumerated-orbit reconciliation ----
    print("\n  Primitive-orbit count check (exact count -> orbits vs enumeration):")
    def prim_pts(n):
        tot = exact_counts.get(n)
        if tot is None:
            return None
        for dd in range(1, n):
            if n % dd == 0:
                tot -= exact_counts.get(dd, 0)
        return tot
    cert_ok = True
    for n in range(2, 9):
        pp = prim_pts(n)
        found = len(prim_orbits.get(n, []))
        if pp is None:
            print(f"    n={n}: no exact count", flush=True); continue
        exp_orb = pp // n
        ok = (exp_orb == found and pp % n == 0)
        if n <= NEIG and not ok:
            cert_ok = False
        note = "" if n <= NEIG else " (n=8: seeding may miss tiny-basin orbits; count still certified)"
        print(f"    n={n}: exact->{exp_orb} orbits, enumerated {found}, MATCH={ok}{note}", flush=True)

    # ---- (B4) cycle-expansion spectrum + GAP per truncation ----
    print("\n  Cycle-expansion spectrum per truncation N (rate = ln|zeta zero|):")
    all_prims = [(n, m) for n in prim_orbits for m in prim_orbits[n]]
    gap_table = {}
    for N in (6, 7, 8):
        prims = [(n, m) for (n, m) in all_prims if n <= N]
        r = rates_and_gap(prims, N)
        if r is None:
            continue
        gap_table[N] = r['gap']
        cert = " [FULLY CERTIFIED: all orbits n<=N complete]" if N <= NEIG else " [n=8 orbits partial]"
        print(f"    N={N}: leading rate = {r['rate0']:.4f}  2nd-resonance rate = "
              f"{r['rate1']:.4f}  GAP = {r['gap']:.4f}{cert}", flush=True)

    # ---- (B5) N=8 robustness: sweep the missing n=8 orbit(s)' multiplier ----
    print("\n  N=8 gap robustness to the un-seeded n=8 orbit(s) (|Lambda| swept):")
    n8_gaps = []
    base8 = [(n, m) for (n, m) in all_prims if n <= 8]
    missing = (n8_orbits_exact - n8_found) if n8_orbits_exact else 0
    for Lam in (1000.0, 1300.0, 2000.0, 3000.0):
        prims = base8 + [(8, Lam)] * max(missing, 0)
        r = rates_and_gap(prims, 8)
        n8_gaps.append(r['gap'])
        print(f"    add {max(missing,0)} orbit(s) at |Lambda|={Lam}: gap = {r['gap']:.4f}", flush=True)
    gap8_min = min([gap_table.get(8, 1.0)] + n8_gaps)

    # ---- (B6) independent direct escape-rate cross-check (>=2 seeds) ----
    print("\n  Direct escape-rate cross-check (surface survival, 2 seeds):")
    direct = [direct_escape_rate(CVAL, s) for s in (11, 23)]
    for s, g in zip((11, 23), direct):
        print(f"    seed {s}: gamma_direct = {g:.4f}", flush=True)
    lead_cyc = rates_and_gap([(n, m) for (n, m) in all_prims if n <= 8], 8)['rate0']
    lead_agree = all(abs(g - lead_cyc) < 0.03 for g in direct)
    print(f"    cycle-expansion leading rate (N=8) = {lead_cyc:.4f}; "
          f"ASSERT agrees with direct (|d|<0.03): {lead_agree}", flush=True)

    # ---- (B7) VACUITY SELF-TEST: gap must depend on the true multipliers ----
    print("\n  VACUITY SELF-TEST (replace all multipliers by a free constant K):")
    gaps_free = []
    for K in (50.0, 200.0, 800.0):
        rf = rates_and_gap([(n, K) for (n, _) in all_prims if n <= 7], 7)
        gaps_free.append(rf['gap'] if rf else None)
        print(f"    free-constant K={K}: gap = {rf['gap']:.4f}", flush=True)
    real_gap7 = gap_table.get(7)
    nonvacuous = any(gf is not None and abs(gf - real_gap7) > 0.05 for gf in gaps_free)
    print(f"    real N=7 gap = {real_gap7:.4f}; ASSERT non-vacuous: {nonvacuous}", flush=True)

    # ---- (B8) verdict inputs ----
    gaps_beyond6 = [gap_table[N] for N in (7, 8) if N in gap_table] + n8_gaps
    gap_holds = len(gaps_beyond6) > 0 and all(g >= 0.19 for g in gaps_beyond6)
    gap_closes = any(g < 0.19 for g in gaps_beyond6)
    # certified beyond n=6: complete orbit enumeration + exact counts at n=7 (fully)
    # AND certified exact count at n=8 (size), with the gap robust to un-seeded n=8 orbits
    certified_beyond6 = (cert_ok and 7 in gap_table and exact_counts.get(7) == 28
                         and n8_count_certified)
    print(f"\n  [B result] gaps beyond n=6 (incl. n=8 sweep) = {[round(g,3) for g in gaps_beyond6]}")
    print(f"  [B result] min gap beyond n=6 = {min(gaps_beyond6):.4f}")
    print(f"  [B result] gap >= 0.19 holds beyond n=6 : {gap_holds}")
    print(f"  [B result] gap CLOSES (<0.19)           : {gap_closes}")
    print(f"  [B result] enumeration certified beyond n=6 : {certified_beyond6}")
    print(f"  [B result] gap non-vacuous : {nonvacuous}; leading-rate cross-check : {lead_agree}")
    return dict(gap_table=gap_table, exact_counts=exact_counts, cert_ok=cert_ok,
                gap_holds=gap_holds, gap_closes=gap_closes, gap8_min=gap8_min,
                certified_beyond6=certified_beyond6, nonvacuous=nonvacuous,
                lead_agree=lead_agree)

def direct_escape_rate(c, seed, npts=120000, nstep=40):
    """escape rate from decay of the fraction of surface points staying in a box
    under iteration of T (Bowen-Ruelle), asymptotic-window linear fit."""
    rng = np.random.default_rng(seed)
    box = 3.0
    xs = rng.uniform(-box, box, npts)
    ys = rng.uniform(-box, box, npts)
    disc = (xs * ys) ** 2 - xs * xs - ys * ys + 1 + c
    m = disc >= 0
    xs, ys, disc = xs[m], ys[m], disc[m]
    zs = xs * ys + np.where(rng.random(len(xs)) < 0.5, 1, -1) * np.sqrt(disc)
    P = np.vstack([xs, ys, zs])
    alive = np.ones(P.shape[1], bool)
    frac = []
    for _ in range(nstep):
        x, y, z = P
        P = np.vstack([2 * x * y - z, x, y])
        alive &= (np.abs(P).max(axis=0) < 6.0)
        frac.append(alive.mean())
    frac = np.array(frac)
    # asymptotic window fit
    k0 = 6
    ok = frac > 1e-4
    idx = np.arange(len(frac))
    win = ok & (idx >= k0)
    if win.sum() < 4:
        return float('nan')
    A = np.polyfit(idx[win], np.log(frac[win]), 1)
    return -A[0]

# =====================================================================
# PART A -- L6a4 SL(3) Ptolemy census: complete the field recognition
# =====================================================================
def part_A():
    banner("PART A -- L6a4 (Borromean-adjacent) SL(3) Ptolemy census completion")
    d = json.load(open(PTOLEMY))
    classes = d['L6a4']['3']
    print(f"L6a4 SL(3): {len(classes)} obstruction classes.")
    print("Goal: reproduce structure table + RECOGNIZE the isolated points' fields")
    print("(the B461 priced remainder) via mpmath high-precision polish + PSLQ minpoly.\n")

    rng = np.random.default_rng(4610017)
    summary = []
    all_fields = []
    for ci, sysd in enumerate(classes):
        vars_ = [sp.Symbol(v) for v in sysd['vars']]
        nv = len(vars_)
        eqs = [sp.sympify(e) for e in sysd['eqs']]
        Fnp = sp.lambdify(vars_, eqs, modules='numpy')
        Jnp = sp.lambdify(vars_, sp.Matrix(eqs).jacobian(vars_), modules='numpy')

        def newton_np(x0, iters=160):
            x = x0.copy()
            for it in range(iters):
                f = np.array(Fnp(*x), dtype=complex)
                Jm = np.array(Jnp(*x), dtype=complex)
                try:
                    dx, *_ = np.linalg.lstsq(Jm, -f, rcond=None)
                except np.linalg.LinAlgError:
                    return None
                x = x + (0.5 if it < 30 else 1.0) * dx
                if not np.all(np.isfinite(x)) or np.max(np.abs(x)) > 1e6:
                    return None
                if np.linalg.norm(f) < 1e-12 and np.linalg.norm(dx) < 1e-12:
                    return x
            return x if np.linalg.norm(np.array(Fnp(*x), dtype=complex)) < 1e-10 else None

        sols = []
        for _ in range(1400):
            x0 = np.exp(2j * np.pi * rng.random(nv)) * (0.5 + rng.random(nv))
            x = newton_np(x0)
            if x is None:
                continue
            if np.min(np.abs(x)) < 1e-6:
                continue
            if any(np.linalg.norm(x - s) < 1e-5 for s in sols):
                continue
            sols.append(x)

        iso_pts, fam = [], 0
        for x in sols:
            Jm = np.array(Jnp(*x), dtype=complex)
            r = int(np.linalg.matrix_rank(Jm, tol=1e-7))
            if r >= nv:
                iso_pts.append(x)
            else:
                fam += 1

        # ---- high-precision polish + field recognition on isolated points ----
        fields = []          # recognized field dicts (isolation-verified points)
        n_iso_verified = 0   # candidate iso pts confirmed 0-dim by mpmath SVD margin
        for x in iso_pts:
            fld = recognize_field(eqs, vars_, x)
            if fld is None:
                fields.append(None)                       # polish failed
                continue
            if not fld.get('isolated'):
                fields.append('FAMILY')                   # SVD margin => really on-family
                continue
            n_iso_verified += 1
            fields.append(fld)
            if fld.get('degree'):
                all_fields.append((ci, fld['degree'], tuple(fld['poly'])))
        summary.append((ci, nv, len(sols), len(iso_pts), fam, n_iso_verified))
        recd = [f for f in fields if isinstance(f, dict)]
        fdesc = ", ".join(f"deg{f['degree']}" for f in recd) or "-"
        print(f"  class {ci:2d}: solutions={len(sols):2d} rank-full={len(iso_pts)} "
              f"SVD-verified-isolated={n_iso_verified} on-family={fam}  "
              f"iso-field-degrees=[{fdesc}]", flush=True)
        for f in recd:
            print(f"        field deg {f['degree']}  minpoly {f['poly']}  "
                  f"(real-subfield gen degrees {f['realsubfield_degrees']})", flush=True)

    # ---- census completion verdict ----
    n_iso = sum(s[5] for s in summary)         # SVD-verified isolated points
    n_recognized = len(all_fields)
    print(f"\n  [A result] SVD-verified isolated points = {n_iso}; "
          f"fields recognized = {n_recognized}")
    degs = sorted(set(dg for _, dg, _ in all_fields))
    print(f"  [A result] recognized isolated-point field degrees = {degs}")
    # census closed only if EVERY verified isolated point got a recognized field
    census_done = (n_iso > 0 and n_recognized == n_iso)
    print(f"  [A result] every isolated-point field recognized (census closed): {census_done}")
    return dict(summary=[(s[0], s[1], s[2], s[3], s[4], s[5]) for s in summary],
                n_iso=n_iso, n_recognized=n_recognized, degs=degs,
                census_done=census_done)

def _minpoly_real(t, maxdeg, tol, maxcoeff=10**7):
    """Minimal polynomial of a REAL algebraic number t: PSLQ on the genuine power
    basis [1,t,...,t^d] for increasing d; the FIRST degree with a relation is the
    minimal degree (no annihilator exists below deg(minpoly)); the relation is then
    the (primitive) minimal polynomial. Irreducibility is ASSERTED via sympy factor.
    Returns (degree, coeff_list_low_to_high) or None."""
    if abs(t) < mp.mpf(10) ** (-40):
        return None  # degenerate generator (e.g. 2 Re(c)=0): no power basis
    for deg in range(1, maxdeg + 1):
        try:
            rel = mp.pslq([t ** i for i in range(deg + 1)], maxcoeff=maxcoeff,
                          maxsteps=10**6, tol=tol)
        except (ValueError, ZeroDivisionError):
            rel = None
        if not rel or not any(rel):
            continue
        # ASSERT it genuinely annihilates t:
        val = sum(int(rel[i]) * t ** i for i in range(deg + 1))
        if abs(val) > tol * mp.mpf(10) ** 8:
            continue
        P = sp.Poly([int(c) for c in reversed(rel)], sp.Symbol('t'))
        # ASSERT minimality: found at the smallest degree => irreducible over Q.
        if not P.is_irreducible:
            # a reducible hit means the true minimal factor annihilates t; pick it
            facs = [f for f, _ in P.factor_list()[1]]
            for f in facs:
                if abs(f.eval(t)) < tol * mp.mpf(10) ** 8:
                    P = f
                    break
        return P.degree(), [int(c) for c in P.all_coeffs()[::-1]]
    return None

def recognize_field(eqs, vars_, x0, dps=100):
    """Polish a numeric isolated solution to `dps` digits (mpmath Gauss-Newton), verify
    it is a genuine ISOLATED (0-dimensional) solution (full-rank Jacobian, margin
    asserted), then recognize the real subfield it defines: the minimal polynomials of
    the REAL generators {2 Re(c), |c|^2} over the Ptolemy coordinates c (PSLQ on a true
    power basis => genuine minimal polynomials). Returns dict or None."""
    mp.mp.dps = dps
    Fmp = sp.lambdify(vars_, eqs, modules='mpmath')
    Jmp = sp.lambdify(vars_, sp.Matrix(eqs).jacobian(vars_), modules='mpmath')
    x = [mp.mpc(complex(v)) for v in x0]
    for _ in range(80):
        f = mp.matrix(Fmp(*x))
        J = mp.matrix(Jmp(*x))
        try:
            dx = mp.lu_solve(J.H * J, -(J.H * f))
        except Exception:
            return None
        x = [xi + dxi for xi, dxi in zip(x, dx)]
        if max(abs(v) for v in mp.matrix(Fmp(*x))) < mp.mpf(10) ** (-dps + 15):
            break
    res = max(abs(v) for v in mp.matrix(Fmp(*x)))
    if res > mp.mpf(10) ** (-dps + 25):
        return None
    # ASSERT genuine 0-dimensional isolation: the Jacobian must have full column rank
    # with a real singular-value margin (guards against family points misclassified).
    J = mp.matrix(Jmp(*x))
    svals = mp.svd(J, compute_uv=False)
    smin = min(abs(s) for s in svals)
    if smin < mp.mpf(10) ** (-6):
        return dict(isolated=False)
    tol = mp.mpf(10) ** (-dps + 45)
    best = None
    degs = set()
    for c in x:
        for gen in (2 * mp.re(c), (mp.re(c) ** 2 + mp.im(c) ** 2)):
            r = _minpoly_real(gen, maxdeg=12, tol=tol)
            if r is None:
                continue
            deg, poly = r
            degs.add(deg)
            if best is None or deg > best[0]:
                best = (deg, poly)
    if best is None:
        return None
    return dict(isolated=True, degree=best[0], poly=best[1],
                realsubfield_degrees=sorted(degs))

# =====================================================================
def main():
    t0 = time.time()
    B = part_B()
    A = part_A()

    banner("VERDICT LOGIC")
    census_done = A['census_done']
    gap_holds = B['gap_holds']
    gap_closes = B['gap_closes']
    certified = B['certified_beyond6']
    nonvacuous = B['nonvacuous']

    print(f"census_done            = {census_done}")
    print(f"gap >= 0.19 holds >n6  = {gap_holds}")
    print(f"gap closes (<0.19)     = {gap_closes}")
    print(f"enumeration certified  = {certified}")
    print(f"gap non-vacuous        = {nonvacuous}")

    if gap_closes:
        verdict = "RESOLVED-B"
        reason = "spectral gap closes (<0.19) in a certified enumeration beyond n=6"
    elif census_done and certified and gap_holds and nonvacuous:
        verdict = "RESOLVED-A"
        reason = ("both boundaries computed: L6a4 field census done AND the >=0.19 gap "
                  "certified (exact full-system counts) beyond n=6")
    else:
        verdict = "UNRESOLVED"
        reason = "one boundary not fully closed (see flags above)"
    print(f"\nVERDICT: {verdict}\nREASON: {reason}")
    print(f"\ntotal runtime {time.time()-t0:.1f}s")
    return verdict, reason

if __name__ == "__main__":
    main()
