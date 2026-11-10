#!/usr/bin/env python3
"""
P-756(b), THE TAU SIDE: DOES ANYTHING CONCENTRATE UNDER THE MOVE COUNT?
The web seat (chat1), 2026-11-10, at the owner's choice ("P-756(b), tau side"). Data-free. This header is the sealed
rule: it was committed, with this script's sha256, before any run of the full card.

KIND: weave. All threads at once, counted by moves: every letter L or R with probability 1/2, the grammar's measure of
maximal entropy (B1813's "by moves", Minkowski's measure lifted to the geodesic flow; B1663, B1815). No thread is
chosen. Two inputs are CHOSEN and stated: the counting rule (the move count is the reading of "upon its execution"
that P-755 puts to the owner) and tau placed by arclength along each history (B1815). Nothing of the nineteen, no
coupling, no frame output and no data enter. No value is compared with anything outside this card.

THE QUESTION (P-756(b), as main narrowed it at S306n): under the executed weave's measure, does any tau-side quantity
concentrate, at an atom or at a stationary point? Here that means the tau-law mu_M on the modular surface S, its
heights and Re tau, the line's class, and the walk's position at level 5.

ON RECORD: B1813 (the height marginal by moves; tail C Y^(-1/2) 4^(-Y); mean length per move 0.7924); B1815 (the exit
law is singular to area); B1629 (no atom at the cusp; the time in runs of length >= k is (k+1)/2^k); P-474 (the
endpoint law's dimension, log 2/0.7924 = 0.8747); P-480 (Pollicott's 0.792425...); P-473 (no finitely supported walk
has an absolutely continuous exit law); B1813's lines (Burnside). NOT on record: the tau-law's density near points.

HAND WORK BEFORE THIS CARD (disclosed; it is why the cells are what they are):
 H1 No atom. A flow-invariant probability measure gives no point positive mass. If the circle of directions over a
    point carried mass c > 0, its images under the flow at small distinct times would be disjoint, each of mass c.
    So the tau-law has no atom at any point or height. [theorem]
 H2 Absolute continuity. The lifted measure has dimension 1 + 2(0.8747) = 2.749 > 2, so its projection to the surface
    is absolutely continuous to area (Ledrappier-Lindenstrauss 2003). [cited, not proved here]
 H3 At i. Geodesics crossing the edge (0, inf) carry the section measure nu x nu on (xi, zeta): xi is the forward
    endpoint and -zeta the backward one, and nu is Minkowski's measure on (0, inf) (fair letters). Such a geodesic
    passes within delta of i iff |xi' - zeta| <~ delta (1 + xi' zeta), with xi' = 1/xi. nu is invariant under
    xi -> 1/xi (L <-> R). So the mass of geodesics within delta of i is nu's correlation integral, ~ delta^D2, with D2
    <= D1 = 0.8747 < 1. The tau-law's mass in B(i, eps) is then ~ eps^(1 + D2) against the area's eps^2. Its density
    relative to area diverges at i like eps^(D2 - 1). [a hand argument; C2 tests it]
 H4 At every point. The same mass at z is a cross-correlation of nu with its image under z's half-turn sigma_z. By
    Cauchy-Schwarz it is at most ~ delta^D2, so no point is more singular than i. [hand]
 H5 Jensen. At z the mass is at least delta^(alpha_z + o(1)), where alpha_z is nu's mean local dimension at the
    sigma_z-images of nu-typical endpoints. alpha_z < 1 makes the density diverge at z; alpha_i = D1. sigma_z is a
    rational map exactly when z is a CM point (imaginary quadratic), where alpha_z may fall below 1. Where sigma_z is
    irrational it is expected to be large. [hand; C5 measures alpha_z]
 H6 Level 5 and the line's class. The walk's position in SL(2, F5) is a walk with steps L and R, which generate the
    group. It is aperiodic: SL(2, F5) = 2I has normal subgroups {1}, {+-1} and itself only, and L, R are not in one
    coset of {+-1}. So it converges to uniform, and its joint law with tau factorizes asymptotically (a mixing finite
    extension). Line classes of every order equidistribute over their orbit (B1813's Burnside). [theorem]
 H7 Runs. The fraction of letters in runs of exactly k is k/2^(k+1), which ties at k = 1, 2 and then decreases. No run
    length, 6 included, is singled out (B1629). [theorem; not computed]
 H8 Area. Under the geometric count the tau-law is hyperbolic area (B1813), with density 1 everywhere, so nothing
    concentrates. [on record; not computed]

SMOKE RUNS BEFORE THE SEAL (on unrelated or reduced copies only; disclosed):
 - The smooth control on 2e5 samples (2 chunks): every slope within 0.02 of 0, and the images check passed.
 - The move law on 1e4 samples: it ran; its numbers were not read.
 - The pressure's code on an unrelated target, log 3 instead of 2 log 2, at depths 8-12. It gave beta_n = 0.5000 there,
   so P(-1/2) = log 3 (Stern's rows sum to about 3^n), and lambda_12 = 0.79242.
   - With P(0) = log 2 and P(-1) = log 4.5616 (by hand, from rows 1-3), a quadratic through the three points gives
     D2 ~ 0.845. That is the basis of C2's windows.
 - The Jensen exponent at i on 100 and 200 samples: the raw ratio read 0.93 at 1e-12; the increment read 0.872.
 - Level 5 at n = 2 only.

THE INSTRUMENT.
 - Section samples (xi, zeta) i.i.d. nu: [a0; a1, ...], with a0 >= 0 at P = 2^-(a0+1) and a_k >= 1 at P = 2^-a_k,
   to 48 digits.
   The geodesic from -zeta to xi enters D0 = (0, 1, inf) through (0, inf) at i sqrt(xi zeta). It leaves through
   Re z = 1 (xi > 1) or |z - 1/2| = 1/2 (xi < 1).
 - The coordinate is s = log|M(z)|, with M(z) = (z + zeta)/(xi - z). Then s_in = (1/2) log(zeta/xi), and s_out is
   (1/2) log((1 + zeta)/(xi - 1)) for xi > 1 or (1/2) log(zeta(1 + zeta)/(xi(1 - xi))) for xi < 1.
 - One segment is one move. Let lam0 be the segments entering D0 through (0, inf). D0 covers S three times, and
   rho(z) = 1/(1 - z) in PSL(2, Z) cycles its edges, so lam0 projects to the tau-law mu_M.
 - f_eps(z) = [lam0(U)/lam0(D0)] / [area(U)/pi]. Here U is the union of B(w, eps) n D0 over the distinct images w of z
   (those in D0's closure and those outside it whose balls reach in), and area(U) = 3 * 2 pi (cosh eps - 1)/|Stab(z)|.
 - A segment's chord in B(w, eps). Write M(w) = u + iv and d = asinh(|u|/v). If d < eps, the chord is
   [s_w - h, s_w + h] n [s_in, s_out], with s_w = (1/2) log(u^2 + v^2) and
   h = 2 asinh(sqrt((sinh^2(eps/2) - sinh^2(d/2))/cosh d)).
 - The move law: N = 4e7 section samples in 40 chunks of 1e6 (seeds 7560001 + k). The smooth control: xi, zeta i.i.d.
   with density (1 + x)^-2 (xi = U/(1 - U)), 1e7 samples in 10 chunks (seeds 7569001 + k). The control measure is not
   Gamma-invariant; it tests the instrument only.
 - eps = 2^-2 ... 2^-12. The slope is the weighted least squares of log f_eps on log eps over eps = 2^-5 ... 2^-11.
   Standard errors are by jackknife over chunks.
 - Points (exact; chosen before any run):
   - P1 = i; P2 = e^(i pi/3), omega's orbit and the centre of D0; P3 = i sqrt 2; P4 = i sqrt 3; P5 = (1 + i sqrt 7)/2.
   - Q1 = 0.42 + 1.23i; Q2 = 0.08 + 1.32i; Q3 = 0.12 + 1.86i; Q4 = 1.34i.
   - The Q's were picked by geometry alone, as grid points far from CM points of discriminant |D| <= 50: at least
     0.054 in S for Q4, at least 0.09 for Q1-Q3.
 - D2 by the pressure. S_n(beta) is the sum, over the Stern-Brocot intervals [p/q, p'/q'] of depth n in [0, 1], of
   (q q')^beta. beta_n solves log(S_{n+1}(beta)/S_n(beta)) = 2 log 2, for n = 12 ... 21. D2 is Aitken's limit of
   beta_19, beta_20, beta_21. Also lambda_n, the mean of log(q q') at depth n + 1 less that at depth n.
 - Jensen's exponent. 4000 nu-samples per point at 60-digit precision. zeta = -sigma_w(xi) for the point's image w in
   D0's closure, keeping zeta > 0. n(delta) is the number of Stern-Brocot letters until zeta's interval has length
   <= delta. The exponent is the increment alpha_inc = log 2 * (mean n(1e-24) - mean n(1e-12))/(mean log(q q') at
   1e-24 - at 1e-12), which removes the first letters' offset; the raw ratios at 1e-6, 1e-12, 1e-24 are read-outs.
   (A smoke run of the raw ratio at i, on 100 samples, read 0.93 at 1e-12 against D1 = 0.8747: the offset of the
   first run, which leaves the interval unbounded. Hence the increment.)
 - Level 5. The exact law of the walk on SL(2, F5) after n = 10, 20, 40, 80 steps, and its total-variation distance
   to uniform. The same for the walk's image of (1, 0) among the 24 non-zero vectors of F5^2.
 - Heights and Re tau. One point per segment, uniform in arclength and weighted by the segment's length, reduced to
   the standard domain F. Report P(Im tau > Y) for Y = 1.5, 2, 3, 4. Read-outs (no prediction): the marginal ratio to
   area in bins about y = 1, and about x = 0 and x = +-1/2.

CELLS, PREDICTIONS, PRIORS (pass rules):
 C0 The instrument.
    (a) |mean segment length - 0.792425| < 0.002. 97%.
    (b) |P(Im > 2) - 0.1676| < 0.003 and |P(Im > 3) - 0.03462| < 0.0012 (B1813's limit row). 93%.
    (c) The smooth control: |slope| < 0.04 at all nine points. 90%.
 C1 Atoms. H1's theorem, and the read-out mu_M(B_S(z, 2^-12)) < 1e-5 at all nine points. 99%.
 C2 At i.
    (a) |lambda_21 - 0.792425| < 0.003, and D2 in [0.80, 0.87]. 88%.
    (b) slope(i) in [-0.22, -0.10]. 85%.
    (c) |slope(i) - (D2 - 1)| <= 0.04. 65%.
 C3 The CM points P2-P5. Each slope >= slope(i) - 0.03, so none is more singular than i (H4). 90%.
    Read-out, no prediction: which have slope < -0.03 with slope + 2 SE < 0 (prior 50% each).
 C4 The points away from small CM points, Q1-Q4. |slope| < 0.04 at each. 70%.
 C5 Jensen (alpha_inc from 1e-12 to 1e-24).
    (a) alpha_inc(i) in [0.86, 0.89] (the control: D1). 90%.
    (b) alpha_inc > 1 at Q1-Q4. 80%.
    (c) Every point with alpha_inc < 0.97 has slope + 2 SE < 0. 90%.
 C6 Level 5 and lines. On SL(2, F5) and on the 24 vectors, the total variation falls at n = 10, 20, 40, 80, and is
    below 1e-3 at 80. 92%. (By hand: on the two-dimensional representations the step operator has modulus
    sqrt(3)/2 = 0.866, since L R^-1 has order 6, so the fall is about 0.866 per step. That is too slow for 40 steps to
    reach 1e-3, and enough for 80.)

WHAT THE OUTCOMES MEAN (fixed now):
 - C2(b) and C4 hold. Under the move count the tau-law singles out i: its density diverges there as a power, and
   stays finite at the points away from small CM points. No mass concentrates (C1). The law read as the move count then
   has a peak at i, but no place where the whole concentrates. Under area nothing is singled out (H8).
 - Some of P2-P5 are also singular. Then the singular set reaches CM points beyond i's orbit. If the pattern is
   general, the density is unbounded on a dense set, strongest at i (H4).
 - C2(b) fails, with no singularity at i. Then H3 is wrong, and that is diagnosed before anything else.
 - C4 fails. Either CM points reach the Q's at these scales, or the instrument is biased; C0(c) decides.
 - Any cell fails: the failure is the finding, and it is diagnosed before anything else is said.

STAYS OUT: the s-family between the two clocks; points other than the nine; the frames' outputs; any comparison with
data or with any value on record outside this card's controls.

0 of 19.
"""
import sys, os, json, math, time, hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EPS = [2.0 ** (-k) for k in range(2, 13)]           # 2^-2 ... 2^-12
FIT = [2.0 ** (-k) for k in range(5, 12)]           # 2^-5 ... 2^-11
K_DIG = 48
S3 = math.sqrt(3.0)
POINTS = {
    'P1_i': complex(0.0, 1.0),
    'P2_e^(i pi/3)': complex(0.5, S3 / 2),
    'P3_i sqrt2': complex(0.0, math.sqrt(2.0)),
    'P4_i sqrt3': complex(0.0, S3),
    'P5_(1+i sqrt7)/2': complex(0.5, math.sqrt(7.0) / 2),
    'Q1': complex(0.42, 1.23),
    'Q2': complex(0.08, 1.32),
    'Q3': complex(0.12, 1.86),
    'Q4': complex(0.0, 1.34),
}
CM = ['P2_e^(i pi/3)', 'P3_i sqrt2', 'P4_i sqrt3', 'P5_(1+i sqrt7)/2']
AWAY = ['Q1', 'Q2', 'Q3', 'Q4']


# ---------------------------------------------------------------- geometry
def in_D0(w, tol=1e-12):
    return (w.imag > 0 and -tol <= w.real <= 1 + tol and abs(w - 0.5) >= 0.5 - tol)


def reduce_F_scalar(z):
    for _ in range(200):
        z = complex(z.real - math.floor(z.real + 0.5), z.imag)
        if abs(z) < 1 - 1e-15:
            z = -1 / z
        else:
            break
    return z


def stab_order(z):
    zf = reduce_F_scalar(z)
    if abs(zf - 1j) < 1e-12:
        return 2
    if abs(zf - complex(0.5, S3 / 2)) < 1e-12 or abs(zf - complex(-0.5, S3 / 2)) < 1e-12:
        return 3
    return 1


def dist_to_D0(w):
    """0 inside D0's closure; otherwise the largest distance to an edge geodesic that w lies beyond (a lower bound)."""
    if in_D0(w):
        return 0.0
    ds = []
    if w.real < 0:
        ds.append(math.asinh(-w.real / w.imag))
    if w.real > 1:
        ds.append(math.asinh((w.real - 1) / w.imag))
    if abs(w - 0.5) < 0.5:
        ds.append(math.asinh((0.25 - abs(w - 0.5) ** 2) / w.imag))
    return max(ds)


def images_in_D0(z, depth=12, near=None):
    """Distinct Gamma-images of z in the closure of D0 (breadth-first over T, T^-1, S). With near = r, also the images
    outside it within r of it, whose balls reach into D0."""
    seen = {}
    frontier = [z]
    key = lambda w: (round(w.real, 9), round(w.imag, 9))
    seen[key(z)] = z
    for _ in range(depth):
        new = []
        for w in frontier:
            for g in (w + 1, w - 1, -1 / w):
                if g.imag < 0.02 or abs(g.real) > 4:
                    continue
                k = key(g)
                if k not in seen:
                    seen[k] = g
                    new.append(g)
        frontier = new
    if near is None:
        return [w for w in seen.values() if in_D0(w)]
    return [w for w in seen.values() if dist_to_D0(w) < near]


def on_edge(w, tol=1e-9):
    return abs(w.real) < tol or abs(w.real - 1) < tol or abs(abs(w - 0.5) - 0.5) < tol


def check_images(name, z, imgs):
    """Each image inside D0 counts 1, each on an edge 1/2; the total must be 3/|Stab|."""
    tot = sum(0.5 if on_edge(w) else 1.0 for w in imgs)
    want = 3.0 / stab_order(z)
    assert abs(tot - want) < 1e-9, (name, tot, want, imgs)


# ---------------------------------------------------------------- samplers
def cf_value(dig):
    """dig: (n, K) array; dig[:,0] = a0 >= 0, dig[:,1:] >= 1. Returns [a0; a1, ...] by backward recursion."""
    v = dig[:, -1].astype(np.float64)
    for k in range(dig.shape[1] - 2, 0, -1):
        v = dig[:, k] + 1.0 / v
    return dig[:, 0] + 1.0 / v


def sample_nu(rng, n):
    dig = rng.geometric(0.5, size=(n, K_DIG)).astype(np.int64)
    dig[:, 0] -= 1
    return cf_value(dig)


def sample_smooth(rng, n):
    u = rng.random(n)
    return u / (1.0 - u)


def segment(xi, zeta):
    s_in = 0.5 * np.log(zeta / xi)
    big = xi > 1.0
    s_out = np.empty_like(xi)
    s_out[big] = 0.5 * np.log((1.0 + zeta[big]) / (xi[big] - 1.0))
    sm = ~big
    s_out[sm] = 0.5 * np.log(zeta[sm] * (1.0 + zeta[sm]) / (xi[sm] * (1.0 - xi[sm])))
    return s_in, s_out


def reduce_F(z):
    z = z.copy()
    for _ in range(120):
        z = z - np.round(z.real)
        m = np.abs(z) < 1.0
        if not m.any():
            break
        z[m] = -1.0 / z[m]
    z = z - np.round(z.real)
    return z


def area_bins():
    """Normalized hyperbolic area (S has area pi/3) of the read-out bins in F."""
    c = 3.0 / math.pi
    def wy(y):
        return 1.0 if y >= 1 else max(0.0, 1.0 - 2.0 * math.sqrt(1.0 - y * y))
    def integ(a, b, n=20000):
        h = (b - a) / n
        return sum(wy(a + (k + 0.5) * h) / (a + (k + 0.5) * h) ** 2 for k in range(n)) * h
    out = {'y_below_1': [], 'y_above_1': [], 'y_ref_1.5': [], 'x_0': [], 'x_half': [], 'x_ref_0.25': []}
    for b in HB:
        out['y_below_1'].append(c * integ(max(1 - b, S3 / 2), 1.0))
        out['y_above_1'].append(c * (1.0 - 1.0 / (1.0 + b)))
        out['y_ref_1.5'].append(c * (1.0 / 1.5 - 1.0 / (1.5 + b)))
        out['x_0'].append(c * 2.0 * math.asin(b))
        out['x_half'].append(c * 2.0 * (math.asin(0.5) - math.asin(0.5 - b)))
        out['x_ref_0.25'].append(c * 2.0 * (math.asin(0.25 + b) - math.asin(0.25 - b)))
    return out


# ---------------------------------------------------------------- one chunk
YTH = [1.5, 2.0, 3.0, 4.0]
HB = [2.0 ** (-k) for k in range(3, 10)]   # half-widths of the marginal read-out bins


def run_chunk(sampler, seed, n, imgs_by_pt, heights):
    rng = np.random.Generator(np.random.PCG64(seed))
    xi = sampler(rng, n)
    zeta = sampler(rng, n)
    ok = (xi > 0) & (zeta > 0) & np.isfinite(xi) & np.isfinite(zeta) & (np.abs(xi - 1.0) > 1e-15)
    xi, zeta = xi[ok], zeta[ok]
    s_in, s_out = segment(xi, zeta)
    seglen = s_out - s_in
    out = {'n': int(xi.size), 'seglen_sum': float(seglen.sum()), 'chord': {}}
    emax = EPS[0]
    for name, imgs in imgs_by_pt.items():
        acc = np.zeros(len(EPS))
        for w in imgs:
            Mw = (w + zeta) / (xi - w)
            u, v = Mw.real, Mw.imag
            d = np.arcsinh(np.abs(u) / v)
            idx = np.nonzero(d < emax)[0]
            if idx.size == 0:
                continue
            dd = d[idx]
            sw = 0.5 * np.log(u[idx] ** 2 + v[idx] ** 2)
            si, so = s_in[idx], s_out[idx]
            for j, e in enumerate(EPS):
                m = dd < e
                if not m.any():
                    continue
                num = np.sinh(e / 2) ** 2 - np.sinh(dd[m] / 2) ** 2
                h = 2.0 * np.arcsinh(np.sqrt(np.maximum(num, 0.0) / np.cosh(dd[m])))
                lo = np.maximum(sw[m] - h, si[m])
                hi = np.minimum(sw[m] + h, so[m])
                acc[j] += np.maximum(hi - lo, 0.0).sum()
        out['chord'][name] = acc.tolist()
    if heights:
        s = s_in + rng.random(xi.size) * seglen
        wv = 1j * np.exp(s)
        p = (wv * xi - zeta) / (1.0 + wv)
        t = reduce_F(p)
        y, x = t.imag, t.real
        out['h_tail'] = [float(seglen[y > Y].sum()) for Y in YTH]
        out['h_y_lo'] = [float(seglen[(y >= 1 - b) & (y < 1)].sum()) for b in HB]
        out['h_y_hi'] = [float(seglen[(y >= 1) & (y < 1 + b)].sum()) for b in HB]
        out['h_y_ref'] = [float(seglen[(y >= 1.5) & (y < 1.5 + b)].sum()) for b in HB]
        out['h_x0'] = [float(seglen[np.abs(x) < b].sum()) for b in HB]
        out['h_xhalf'] = [float(seglen[np.abs(np.abs(x) - 0.5) < b].sum()) for b in HB]
        out['h_xref'] = [float(seglen[np.abs(np.abs(x) - 0.25) < b].sum()) for b in HB]
    return out


def area_U(z, e):
    return 3.0 * 2.0 * math.pi * (math.cosh(e) - 1.0) / stab_order(z)


def assemble(chunks, names):
    """f_eps per point with jackknife SE; slope over FIT with jackknife SE."""
    C = len(chunks)
    seg = np.array([c['seglen_sum'] for c in chunks])
    res = {}
    fit_idx = [EPS.index(e) for e in FIT]
    lx = np.log(np.array(FIT))
    for name in names:
        z = POINTS[name]
        ch = np.array([c['chord'][name] for c in chunks])      # C x len(EPS)
        A = np.array([area_U(z, e) for e in EPS])

        def fvals(mask):
            return (ch[mask].sum(0) / seg[mask].sum()) / (A / math.pi)
        allm = np.ones(C, bool)
        f = fvals(allm)
        jk = []
        for k in range(C):
            m = allm.copy(); m[k] = False
            jk.append(fvals(m))
        jk = np.array(jk)
        se = np.sqrt((C - 1) / C * ((jk - jk.mean(0)) ** 2).sum(0))

        def slope_of(fv, sev):
            yy = np.log(fv[fit_idx]); ww = 1.0 / np.maximum((sev[fit_idx] / fv[fit_idx]) ** 2, 1e-12)
            X = np.vstack([np.ones_like(lx), lx]).T
            W = np.diag(ww)
            beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ yy)
            return float(beta[1])
        sl = slope_of(f, se)
        sjk = np.array([slope_of(jk[k], se) for k in range(C)])
        sl_se = float(math.sqrt((C - 1) / C * ((sjk - sjk.mean()) ** 2).sum()))
        local = [float((math.log(f[j + 1]) - math.log(f[j])) / (math.log(EPS[j + 1]) - math.log(EPS[j])))
                 if f[j] > 0 and f[j + 1] > 0 else None for j in range(len(EPS) - 1)]
        mu_small = float(ch[:, -1].sum() / seg.sum())
        res[name] = {'f': f.tolist(), 'f_se': se.tolist(), 'slope': sl, 'slope_se': sl_se,
                     'local_slopes': local, 'mu_M_ball_2^-12': mu_small, 'stab': stab_order(z)}
    return res


# ---------------------------------------------------------------- D2 by the pressure
def stern(nmax):
    N = 2 ** (nmax + 1) + 2
    s = np.zeros(N, dtype=np.int64)
    s[1] = 1
    for k in range(1, N // 2):
        s[2 * k] = s[k]
        if 2 * k + 1 < N:
            s[2 * k + 1] = s[k] + s[k + 1]
    return s


def logsumexp(a):
    m = a.max()
    return float(m + math.log(np.exp(a - m).sum()))


def pressure_D2(nlo, nhi, target):
    s = stern(nhi + 1)
    L = {}
    for n in range(nlo, nhi + 2):
        row = s[2 ** n: 2 ** (n + 1) + 1].astype(np.float64)
        L[n] = np.log(row[:-1] * row[1:])
    betas, lams = {}, {}
    for n in range(nlo, nhi + 1):
        a, b = L[n], L[n + 1]
        g = lambda be: logsumexp(be * b) - logsumexp(be * a) - target
        lo, hi = 0.0, 1.5
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if g(mid) > 0:
                hi = mid
            else:
                lo = mid
        betas[n] = 0.5 * (lo + hi)
        lams[n] = float(b.mean() - a.mean())
    ks = sorted(betas)
    x0, x1, x2 = betas[ks[-3]], betas[ks[-2]], betas[ks[-1]]
    den = (x2 - x1) - (x1 - x0)
    aitken = x2 - (x2 - x1) ** 2 / den if abs(den) > 1e-15 else x2
    return {'beta_n': betas, 'lambda_n': lams, 'D2_aitken': aitken}


# ---------------------------------------------------------------- Jensen's exponent
def jensen(name, z, nsamp, seed, deltas, dps=60):
    import mpmath as mp
    mp.mp.dps = dps
    imgs = images_in_D0(z)
    w = min(imgs, key=lambda q: q.real)            # the image nearest the edge (0, inf)
    x, y = mp.mpf(w.real), mp.mpf(w.imag)
    if name == 'P2_e^(i pi/3)':
        x, y = mp.mpf(1) / 2, mp.sqrt(3) / 2
    if name == 'P5_(1+i sqrt7)/2':
        x, y = mp.mpf(1) / 2, mp.sqrt(7) / 2
    if name == 'P3_i sqrt2':
        x, y = mp.mpf(0), mp.sqrt(2)
    if name == 'P4_i sqrt3':
        x, y = mp.mpf(0), mp.sqrt(3)
    if name == 'P1_i':
        x, y = mp.mpf(0), mp.mpf(1)
    r2 = x * x + y * y
    rng = np.random.Generator(np.random.PCG64(seed))
    tots = {dl: [0, 0.0, 0] for dl in deltas}      # letters, log(qq'), samples
    kept = 0
    capped = 0
    for _ in range(nsamp):
        dig = rng.geometric(0.5, size=110).astype(np.int64)
        dig[0] -= 1
        v = mp.mpf(int(dig[-1]))
        for k in range(len(dig) - 2, 0, -1):
            v = int(dig[k]) + 1 / v
        xi = int(dig[0]) + 1 / v
        if xi == x:
            continue
        zeta = (r2 - x * xi) / (xi - x)
        if zeta <= 0:
            continue
        kept += 1
        # continued fraction digits of zeta
        digs = []
        t = zeta
        qa, qb = 0, 1                    # convergent denominators q_(k-2), q_(k-1)
        for _ in range(400):
            a = int(mp.floor(t))
            digs.append(a)
            qa, qb = qb, a * qb + qa
            fr = t - a
            if qb > 10 ** 25 or fr < mp.mpf(10) ** (-(dps - 15)):
                break
            t = 1 / fr
        for dl in deltas:
            target = 1 / mp.mpf(dl)
            # Stern-Brocot walk by runs: left = p0/q0, right = p1/q1, start [0/1, 1/0]
            p0, q0, p1, q1 = 0, 1, 1, 0
            letters = 0
            done = False
            for j, a in enumerate(digs):
                if a == 0:
                    continue
                if j % 2 == 0:      # R-run: the left endpoint moves: left = (p0 + k p1)/(q0 + k q1)
                    if q1 > 0 and (q0 + a * q1) * q1 >= target:
                        k = int(mp.ceil((target / q1 - q0) / q1))
                        k = max(1, min(k, a))
                        while (q0 + k * q1) * q1 < target:
                            k += 1
                        letters += k
                        q0n = q0 + k * q1
                        tots[dl][0] += letters
                        tots[dl][1] += float(mp.log(mp.mpf(q0n) * q1))
                        tots[dl][2] += 1
                        done = True
                        break
                    p0, q0 = p0 + a * p1, q0 + a * q1
                else:               # L-run: the right endpoint moves: right = (p1 + k p0)/(q1 + k q0)
                    if q0 > 0 and (q1 + a * q0) * q0 >= target:
                        k = int(mp.ceil((target / q0 - q1) / q0))
                        k = max(1, min(k, a))
                        while (q1 + k * q0) * q0 < target:
                            k += 1
                        letters += k
                        q1n = q1 + k * q0
                        tots[dl][0] += letters
                        tots[dl][1] += float(mp.log(mp.mpf(q1n) * q0))
                        tots[dl][2] += 1
                        done = True
                        break
                    p1, q1 = p1 + a * p0, q1 + a * q0
                letters += a
            if not done:
                capped += 1
    res = {'kept': kept, 'capped': capped}
    for dl in deltas:
        L, G, c = tots[dl]
        res[f'alpha_J({dl:g})'] = (math.log(2) * L / G) if G > 0 else None
        res[f'mean_letters({dl:g})'] = L / c if c else None
        res[f'mean_logqq({dl:g})'] = G / c if c else None
        res[f'n({dl:g})'] = c
    ds = sorted(deltas, reverse=True)
    for d1, d2 in zip(ds[:-1], ds[1:]):
        L1, G1, c1 = tots[d1]
        L2, G2, c2 = tots[d2]
        if c1 and c2 and (G2 / c2 - G1 / c1) > 0:
            res[f'alpha_inc({d1:g}->{d2:g})'] = math.log(2) * (L2 / c2 - L1 / c1) / (G2 / c2 - G1 / c1)
    return res


# ---------------------------------------------------------------- level 5
def level5(steps):
    els = [(a, b, c, d) for a in range(5) for b in range(5) for c in range(5) for d in range(5)
           if (a * d - b * c) % 5 == 1]
    idx = {g: i for i, g in enumerate(els)}
    mul = lambda g, h: ((g[0] * h[0] + g[1] * h[2]) % 5, (g[0] * h[1] + g[1] * h[3]) % 5,
                        (g[2] * h[0] + g[3] * h[2]) % 5, (g[2] * h[1] + g[3] * h[3]) % 5)
    Lm, Rm = (1, 0, 1, 1), (1, 1, 0, 1)
    tL = [idx[mul(g, Lm)] for g in els]
    tR = [idx[mul(g, Rm)] for g in els]
    vecs = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    vidx = {v: i for i, v in enumerate(vecs)}
    gv = [vidx[((g[0] * 1 + g[1] * 0) % 5, (g[2] * 1 + g[3] * 0) % 5)] for g in els]
    p = np.zeros(len(els)); p[idx[(1, 0, 0, 1)]] = 1.0
    out = {'order': len(els)}
    for n in range(1, max(steps) + 1):
        q = np.zeros_like(p)
        np.add.at(q, tL, 0.5 * p)
        np.add.at(q, tR, 0.5 * p)
        p = q
        if n in steps:
            pv = np.zeros(len(vecs)); np.add.at(pv, gv, p)
            out[n] = {'tv_group': float(0.5 * np.abs(p - 1 / len(els)).sum()),
                      'tv_vectors': float(0.5 * np.abs(pv - 1 / len(vecs)).sum())}
    return out


# ---------------------------------------------------------------- main
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'full'
    outpath = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'out_p756b.json')
    t0 = time.time()
    me = open(os.path.abspath(__file__), 'rb').read()
    R = {'mode': mode, 'script_sha256': hashlib.sha256(me).hexdigest(), 'eps': EPS, 'fit': FIT}
    imgs = {}
    for name, z in POINTS.items():
        check_images(name, z, images_in_D0(z))
        imgs[name] = images_in_D0(z, near=EPS[0] + 0.01)
    R['images'] = {k: [[w.real, w.imag] for w in v] for k, v in imgs.items()}

    if mode == 'smoke_control':
        chunks = [run_chunk(sample_smooth, 999001 + k, 100000, imgs, False) for k in range(2)]
        R['control'] = assemble(chunks, list(POINTS))
    elif mode == 'smoke_reduced':
        chunks = [run_chunk(sample_nu, 999101 + k, 5000, imgs, True) for k in range(2)]
        R['reduced_ran'] = True
    elif mode == 'smoke_pressure':
        R['pressure_unrelated_target_log3'] = pressure_D2(8, 12, math.log(3.0))
    elif mode == 'smoke_jensen':
        R['jensen_i_200'] = jensen('P1_i', POINTS['P1_i'], 200, 999201, [1e-6, 1e-12, 1e-24])
    elif mode == 'smoke_level5':
        R['level5_n2'] = level5([2])
    elif mode == 'full':
        mv = []
        for k in range(40):
            mv.append(run_chunk(sample_nu, 7560001 + k, 1000000, imgs, True))
            print(f'move chunk {k} done, {time.time() - t0:.0f} s', flush=True)
        R['move'] = assemble(mv, list(POINTS))
        nt = sum(c['n'] for c in mv)
        seg = sum(c['seglen_sum'] for c in mv)
        R['mean_seglen'] = seg / nt
        R['area_bins'] = area_bins()
        R['heights'] = {
            'P(Im>Y)': {str(Y): sum(c['h_tail'][j] for c in mv) / seg for j, Y in enumerate(YTH)},
            'bins_halfwidths': HB,
            'mass_y_below_1': [sum(c['h_y_lo'][j] for c in mv) / seg for j in range(len(HB))],
            'mass_y_above_1': [sum(c['h_y_hi'][j] for c in mv) / seg for j in range(len(HB))],
            'mass_y_ref_1.5': [sum(c['h_y_ref'][j] for c in mv) / seg for j in range(len(HB))],
            'mass_x_0': [sum(c['h_x0'][j] for c in mv) / seg for j in range(len(HB))],
            'mass_x_half': [sum(c['h_xhalf'][j] for c in mv) / seg for j in range(len(HB))],
            'mass_x_ref_0.25': [sum(c['h_xref'][j] for c in mv) / seg for j in range(len(HB))],
        }
        ctl = []
        for k in range(10):
            ctl.append(run_chunk(sample_smooth, 7569001 + k, 1000000, imgs, False))
            print(f'control chunk {k} done, {time.time() - t0:.0f} s', flush=True)
        R['control'] = assemble(ctl, list(POINTS))
        R['pressure'] = pressure_D2(12, 21, 2.0 * math.log(2.0))
        print(f'pressure done, {time.time() - t0:.0f} s', flush=True)
        R['jensen'] = {}
        for j, (name, z) in enumerate(POINTS.items()):
            R['jensen'][name] = jensen(name, z, 4000, 7565001 + j, [1e-6, 1e-12, 1e-24])
            print(f'jensen {name} done, {time.time() - t0:.0f} s', flush=True)
        R['level5'] = level5([10, 20, 40, 80])
        # ---------------- cells
        mvr, cr, pr, jr, l5 = R['move'], R['control'], R['pressure'], R['jensen'], R['level5']
        D2 = pr['D2_aitken']
        lam = pr['lambda_n'][21]
        si, si_se = mvr['P1_i']['slope'], mvr['P1_i']['slope_se']
        cells = {}
        cells['C0a'] = abs(R['mean_seglen'] - 0.792425) < 0.002
        cells['C0b'] = (abs(R['heights']['P(Im>Y)']['2.0'] - 0.1676) < 0.003 and
                        abs(R['heights']['P(Im>Y)']['3.0'] - 0.03462) < 0.0012)
        cells['C0c'] = all(abs(cr[n]['slope']) < 0.04 for n in POINTS)
        cells['C1'] = all(mvr[n]['mu_M_ball_2^-12'] < 1e-5 for n in POINTS)
        cells['C2a'] = abs(lam - 0.792425) < 0.003 and 0.80 <= D2 <= 0.87
        cells['C2b'] = -0.22 <= si <= -0.10
        cells['C2c'] = abs(si - (D2 - 1.0)) <= 0.04
        cells['C3'] = all(mvr[n]['slope'] >= si - 0.03 for n in CM)
        cells['C3_readout_singular'] = [n for n in CM if mvr[n]['slope'] < -0.03 and
                                        mvr[n]['slope'] + 2 * mvr[n]['slope_se'] < 0]
        cells['C4'] = all(abs(mvr[n]['slope']) < 0.04 for n in AWAY)
        aJ = {n: jr[n].get('alpha_inc(1e-12->1e-24)') for n in POINTS}
        cells['C5a'] = aJ['P1_i'] is not None and 0.86 <= aJ['P1_i'] <= 0.89
        cells['C5b'] = all(aJ[n] is not None and aJ[n] > 1.0 for n in AWAY)
        cells['C5c'] = all(mvr[n]['slope'] + 2 * mvr[n]['slope_se'] < 0 for n in POINTS
                           if aJ[n] is not None and aJ[n] < 0.97)
        falls = all(l5[a][k] > l5[b][k] for k in ('tv_group', 'tv_vectors')
                    for a, b in ((10, 20), (20, 40), (40, 80)))
        cells['C6'] = falls and l5[80]['tv_group'] < 1e-3 and l5[80]['tv_vectors'] < 1e-3
        R['cells'] = cells
    else:
        raise SystemExit('unknown mode')
    R['seconds'] = time.time() - t0
    with open(outpath, 'w') as fh:
        json.dump(R, fh, indent=1, default=str)
    print('written', os.path.basename(outpath), f'{R["seconds"]:.0f} s', flush=True)


if __name__ == '__main__':
    main()
