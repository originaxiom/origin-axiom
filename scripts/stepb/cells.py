"""STEP B's generator, the continuous-tau cell index (main's rulings after the interpolant's diagnosis, 2026-10-30; it
replaces exact_tau's W x rho bound and the 4 x 4 rule; data-free).

THE INTERPOLANT.  A row of a choice (line, direction, radius, reading) at a census node is extended over the node's cell
(grid.cell) by the biquadratic Lagrange polynomial through its 3 x 3 stencil (exact_tau.GridStencils) of the same choice's
rows, in the INTERPOLATION COORDINATES: the natural logs of the nine positive outputs (the six, |V_us|, |V_cb|, |V_ub|) and
J SIGNED; |J| is taken after interpolating (J's zero set is a curve, on which ln|J| is singular; on the mini patch J's
interpolation failures fall from 23% to 9%).  A row whose stencil is incomplete (the mixing undefined at a stencil node) or
carries a non-finite value is scored at its node alone (its enclosure is its node value).

THE ENCLOSURE.  On a rectangle R inside the stencil's range each coordinate is a polynomial of degree <= 2 in each variable;
in R's tensor Bernstein basis (non-negative, summing to one) its range over R lies within [min b, max b] of its nine
coefficients, which follow from its values at R's 3 x 3 points {0, 1/2, 1}^2: per axis b0 = p(0), b1 = 2 p(1/2) -
(p(0) + p(1))/2, b2 = p(1).  For J the signed range gives |J|'s (from zero when it changes sign), hence ln|J|'s (unbounded
below then).  The enclosure is rigorous for the interpolant and tightens quadratically under subdivision.

USES.  (a) per row, the sigma-scaled radius of its cell's enclosure about its node value, for k-d trees bucketed by radius
(a row can reach chi2 < T only if its node lies within sqrt(T) + radius of the target in the space queried); (b) exact lower
bounds on chi2 over a cell (component-wise distance from the target to the enclosure); (c) S: a branch-and-bound on the
candidate cells deciding chi2 < T on the interpolant (an inclusion is a point evaluated below T, an exclusion an enclosure
above it); (d) K: rigorous upper bounds on a cell's likelihood integral, for the windows and the quadrature tiers.

Feature space (the chi2's): natural logs of the ten, |J| last; targets and c shifts as in stepb_core."""
from __future__ import annotations

import heapq
import math

import numpy as np
from scipy.spatial import cKDTree

import grid as G
import stepb_core as C
from exact_tau import GridStencils
from census_io import mirror_partner

_M3 = np.array([[1.0, 0.0, 0.0], [-0.5, 2.0, -0.5], [0.0, 0.0, 1.0]])            # values at 0, 1/2, 1 -> Bernstein
KM = np.kron(_M3, _M3)
_DL = np.array([[1.0, 0.0, 0.0], [0.5, 0.5, 0.0], [0.25, 0.5, 0.25]])             # de Casteljau: the left half's coefficients
_DR = np.array([[0.25, 0.5, 0.25], [0.0, 0.5, 0.5], [0.0, 0.0, 1.0]])             # and the right half's
KIDS = np.array([np.kron(A, B) for A in (_DL, _DR) for B in (_DL, _DR)])         # (x half, y half): LL, LR, RL, RR
CENTRE = np.kron([0.25, 0.5, 0.25], [0.25, 0.5, 0.25])                           # the basis at (1/2, 1/2)
BUCKETS = (0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, math.inf)
SPACES = {"six": tuple(range(6)), "nine": tuple(range(9)), "ckm3": (6, 7, 8)}
CHUNK = 1 << 20
SLACK = 1e-6                 # the ball bound's slack against float rounding (the fifth review's N6)
BNB_MIN_SIZE = 1e-7          # a sub-rectangle smaller than this (in tau) is not split again: reported as undecided
FLOOR = 1e-12                # an output below this at EVERY node of its choice is a structural zero (roundoff: on the mini
                             # patch the zeros of m1/m3, |V_us|, |V_ub| and J lie below 1e-13, the physical values above 1e-11)


def rect_points(x0, x1, y0, y1):
    """R's 3 x 3 points, row-major over x then y (the Bernstein conversion's order)"""
    xs = (x0, 0.5 * (x0 + x1), x1); ys = (y0, 0.5 * (y0 + y1), y1)
    return [(x, y) for x in xs for y in ys]


def ln_abs_range(jlo, jhi):
    """ln|J| over J in [jlo, jhi], elementwise: (lo, hi); lo = -inf when the interval reaches zero"""
    jlo = np.asarray(jlo, float); jhi = np.asarray(jhi, float)
    a, b = np.abs(jlo), np.abs(jhi)
    cross = (jlo <= 0) & (jhi >= 0)
    with np.errstate(divide="ignore"):
        lo = np.where(cross, -np.inf, np.log(np.minimum(a, b)))
        hi = np.log(np.maximum(a, b))
    return lo, hi


def _down32(x):
    """float32 at or below x (a rigorous lower end after storage)"""
    x = np.asarray(x, float); y = x.astype(np.float32)
    return np.where(y.astype(float) > x, np.nextafter(y, np.float32(-np.inf)), y).astype(np.float32)


def _up32(x):
    x = np.asarray(x, float); y = x.astype(np.float32)
    return np.where(y.astype(float) < x, np.nextafter(y, np.float32(np.inf)), y).astype(np.float32)


def interval_dist(t, lo, hi):
    """distance from t to [lo, hi], elementwise (0 inside; inf-safe)"""
    return np.maximum(np.maximum(lo - t, t - hi), 0.0)


class CellIndex:
    """census rows on continuous tau.  F: (n, 10) natural-log features (|J| last); Js: (n,) signed J; points: the grid's
    (re, im); choices: assemble.Choices (R: choice x node -> row, -1 if absent; keys); sigma: (10,) natural log."""

    def __init__(self, F, Js, points, choices, sigma):
        self.F = F; self.Js = np.asarray(Js)
        self.sig = np.asarray(sigma, float); assert self.sig.shape == (10,)
        self.gs = GridStencils(points); self.ch = choices
        nn = len(self.gs.pts); n = len(F)
        self.ST = np.full((nn, 9), -1, np.int64)
        self.cellr = np.zeros((nn, 4))
        self.BM = np.zeros((nn, 9, 9))
        for i, p in enumerate(self.gs.pts):
            self.cellr[i] = G.cell(*p)
            if self.gs.st[i] is not None:
                self.ST[i] = self.gs.st[i][2]
                self.BM[i] = KM @ np.array([self.gs.weights(i, x, y) for x, y in rect_points(*self.cellr[i])])
        R = choices.R
        jj, nd = np.nonzero(R >= 0)
        rows = R[jj, nd]
        self.node = np.full(n, -1, np.int32); self.choice = np.full(n, -1, np.int32)
        self.node[rows] = nd; self.choice[rows] = jj
        key_index = {q: j for j, q in enumerate(choices.keys)}
        pch = np.array([key_index.get((mirror_partner(q[0]),) + tuple(q[1:]), -1) for q in choices.keys], np.int32)
        self.partner = np.full(n, -1, np.int32); self.partner[rows] = pch[jj]
        self.rows = np.sort(rows)
        self.ok = np.zeros(n, bool)
        self.rad = {s: np.zeros(n, np.float32) for s in SPACES}
        self.jlo = np.zeros(n, np.float32); self.jhi = np.zeros(n, np.float32)       # ln|J|'s enclosure over the cell
        self.lo = np.zeros((n, 10), np.float32); self.hi = np.zeros((n, 10), np.float32)  # the enclosure, rounded outward
        for a in range(0, len(self.rows), CHUNK):
            r = self.rows[a:a + CHUNK]
            st = self.stencil_rows(r)
            okr = (st >= 0).all(axis=1)
            Xs = self.coords(np.where(st >= 0, st, 0))                                 # (m, 9, 10)
            okr &= np.isfinite(Xs).all(axis=(1, 2)) & np.isfinite(self.coords(r)).all(axis=1)
            self.ok[r] = okr
            lo, hi = self._enclose(r, st, okr)
            self.lo[r] = _down32(lo); self.hi[r] = _up32(hi)
            X0 = self.coords(r)
            for s, comps in SPACES.items():
                c = list(comps)
                dev = np.maximum(hi[:, c] - X0[:, c], X0[:, c] - lo[:, c]) / self.sig[c]
                self.rad[s][r] = _up32(np.where(np.isfinite(dev).all(axis=1), np.linalg.norm(dev, axis=1), np.inf))
            l9, h9 = ln_abs_range(lo[:, 9], hi[:, 9])
            self.jlo[r] = _down32(l9); self.jhi[r] = _up32(h9)
        # per choice: which of the four (|V_us|, |V_cb|, |V_ub|, |J|) is a structural zero (below FLOOR at every node); a
        # choice is PHYSICAL when none is (the null's CKM marginal and its normalisation use the physical choices only)
        lf = math.log(FLOOR); nch = R.shape[0]
        zero4 = np.ones((nch, 4), bool)
        F4 = self.F[:, 6:10]
        okF = np.where(np.isfinite(F4[rows]), F4[rows] >= lf, False)                    # (len(rows), 4): above the floor
        np.logical_and.at(zero4, jj, ~okF)
        self.zero4 = zero4; self.physical_choice = ~zero4.any(axis=1)
        self.phys = np.zeros(n, bool); self.phys[rows] = self.physical_choice[jj]
        self._trees = {}
        self._gauss = {}

    # ---- coordinates, stencils, enclosures ----
    def coords(self, rows):
        """interpolation coordinates (..., 10): ln of the nine, J signed"""
        rows = np.asarray(rows)
        return np.concatenate([self.F[rows][..., :9].astype(np.float64), self.Js[rows][..., None].astype(np.float64)], axis=-1)

    def feat(self, X):
        """interpolation coordinates -> features (ln|J| last)"""
        out = np.array(X, dtype=np.float64, copy=True)
        with np.errstate(divide="ignore"):
            out[..., 9] = np.log(np.abs(out[..., 9]))
        return out

    def stencil_rows(self, rows):
        rows = np.asarray(rows, np.int64)
        st = self.ST[self.node[rows]]                                                  # (m, 9) node indices
        out = self.ch.R[self.choice[rows][:, None], np.where(st >= 0, st, 0)]
        return np.where(st >= 0, out, -1)

    def _enclose(self, rows, st, okr, BM=None):
        """(lo, hi) (m, 10) in interpolation coordinates over each row's cell (BM: per-row (m, 9, 9) for sub-rectangles)"""
        X0 = self.coords(rows)
        lo = X0.copy(); hi = X0.copy()
        if okr.any():
            idx = np.nonzero(okr)[0]
            Xs = self.coords(st[idx])
            B = self.BM[self.node[rows[idx]]] if BM is None else BM[idx]
            coef = np.einsum("mab,mbk->mak", B, Xs)
            lo[idx] = coef.min(axis=1); hi[idx] = coef.max(axis=1)
        return lo, hi

    def enclosure(self, rows):
        rows = np.asarray(rows, np.int64)
        return self._enclose(rows, self.stencil_rows(rows), self.ok[rows])

    def chi2_lower(self, rows, t, comps):
        """exact lower bounds on chi2 over each row's cell (the stored enclosures, rounded outward); t: one target (10,) or
        one per row (m, 10), features, already c-shifted"""
        rows = np.asarray(rows, np.int64); t = np.asarray(t, float)
        tk = (lambda k: t[k]) if t.ndim == 1 else (lambda k: t[:, k])
        tot = np.zeros(len(rows))
        for k in comps:
            if k == 9:
                d = interval_dist(tk(9), self.jlo[rows].astype(float), self.jhi[rows].astype(float))
            else:
                d = interval_dist(tk(k), self.lo[rows, k].astype(float), self.hi[rows, k].astype(float))
            tot += (d / self.sig[k]) ** 2
        return tot

    # ---- the k-d trees (one per space, bucketed by the rows' radii) ----
    def trees(self, space):
        """the space's k-d trees, one per radius bucket: (rows, tree, the bucket's largest radius, the bucket's sigma-scaled
        float64 data, which the tree references without a copy).  Memory: one float64 copy of the space's columns over the
        rows with finite values and radii (no full-size temporary; finiteness checked chunk by chunk on the float32 data)."""
        if space not in self._trees:
            comps = list(SPACES[space]); sc = self.sig[comps]
            keep = np.zeros(len(self.rows), bool)
            for a in range(0, len(self.rows), CHUNK):
                r = self.rows[a:a + CHUNK]
                keep[a:a + CHUNK] = np.isfinite(self.F[r][:, comps]).all(axis=1) & np.isfinite(self.rad[space][r])
            fin = self.rows[keep]; rr = self.rad[space][fin]
            out = []
            for lo_, hi_ in zip(BUCKETS[:-1], BUCKETS[1:]):
                sel = fin[(rr >= lo_) & (rr < hi_)]
                if len(sel):
                    Yb = np.ascontiguousarray(self.F[sel][:, comps].astype(np.float64) / sc)
                    out.append((sel, cKDTree(Yb, copy_data=False), float(self.rad[space][sel].astype(np.float64).max()), Yb))
            self._trees[space] = (None, out)
        return self._trees[space]

    def candidates(self, space, t, x2max):
        """rows whose cells can reach chi2 <= x2max in the space's components (the ball bound; a superset of the exact
        lower-bound filter, which the caller applies)"""
        _, buckets = self.trees(space); comps = list(SPACES[space]); y = t[comps] / self.sig[comps]
        out = []
        for sel, tree, rmax, Yb in buckets:
            hit = tree.query_ball_point(y, math.sqrt(x2max) + rmax + SLACK)
            if hit:
                h = np.asarray(hit, np.int64); c = sel[h]
                d = np.linalg.norm(Yb[h] - y, axis=1)
                out.append(c[d <= math.sqrt(x2max) + self.rad[space][c].astype(np.float64) + SLACK])
        return np.concatenate(out) if out else np.zeros(0, np.int64)

    # ---- point values ----
    def _axes(self):
        if not hasattr(self, "_NX"):
            nn = len(self.gs.pts); self._NX = np.zeros((nn, 3)); self._NY = np.zeros((nn, 3))
            for i in range(nn):
                if self.gs.st[i] is not None:
                    self._NX[i] = self.gs.st[i][0]; self._NY[i] = self.gs.st[i][1]
        return self._NX, self._NY

    @staticmethod
    def _lag3(v, N):
        """Lagrange weights at v (m,) for node triples N (m, 3): (m, 3)"""
        a, b, c = N[:, 0], N[:, 1], N[:, 2]
        return np.stack([(v - b) * (v - c) / ((a - b) * (a - c)), (v - a) * (v - c) / ((b - a) * (b - c)),
                         (v - a) * (v - b) / ((c - a) * (c - b))], axis=1)

    def interp_many(self, rows, xs, ys):
        """features (m, 10) of rows[i] at (xs[i], ys[i]) (one point per row; node-only rows give their node)"""
        rows = np.asarray(rows, np.int64); X = self.coords(rows)
        okr = self.ok[rows]
        if okr.any():
            idx = np.nonzero(okr)[0]; NX, NY = self._axes(); nd = self.node[rows[idx]]
            wx = self._lag3(np.asarray(xs, float)[idx], NX[nd]); wy = self._lag3(np.asarray(ys, float)[idx], NY[nd])
            W = (wx[:, :, None] * wy[:, None, :]).reshape(len(idx), 9)
            X[idx] = np.einsum("mk,mkf->mf", W, self.coords(self.stencil_rows(rows[idx])))
        return self.feat(X)

    def sample_prior(self, rng, n, physical=True):
        """n draws from the frame's unconditional measure on (row, tau): a row by its cell's measure (each row once; with
        physical, only the PHYSICAL choices' rows: a world with a structurally zero CKM entry is not a world of our kind),
        then tau in the cell by dx dy / y^2 (x uniform; 1/y uniform); returns (rows, xs, ys)"""
        pool = self.rows[self.phys[self.rows]] if physical else self.rows
        lm = self.log2_cell_measure(pool); p = np.exp2(lm - lm.max()); p /= p.sum()
        rows = pool[rng.choice(len(pool), size=n, p=p)]
        x0, x1, y0, y1 = self.cellr[self.node[rows]].T
        xs = rng.uniform(x0, x1); u = rng.uniform(0.0, 1.0, n)
        ys = 1.0 / (1.0 / y0 - u * (1.0 / y0 - 1.0 / y1))
        return rows, xs, ys

    def values_at(self, row, pts):
        """features at points (k, 2) of the row's cell (the node's values when the row is node-only)"""
        if not self.ok[row]:
            return np.repeat(self.feat(self.coords([row]))[0][None], len(pts), axis=0)
        nd = self.node[row]; Xs = self.coords(self.stencil_rows([row])[0])
        W = np.array([self.gs.weights(nd, x, y) for x, y in pts])
        return self.feat(W @ Xs)

    # ---- S: the branch-and-bound on one cell (de Casteljau on the Bernstein coefficients) ----
    def _x2(self, f, t, comps):
        t = np.asarray(t, float)
        z = (f[..., list(comps)] - t[..., list(comps)]) / self.sig[list(comps)]
        out = np.einsum("...k,...k->...", z, z)
        return np.where(np.isfinite(out), out, np.inf)

    def _lb(self, coef, t, comps):
        """chi2 lower bounds from Bernstein coefficients (m, 9, 10) in interpolation coordinates"""
        lo, hi = coef.min(axis=1), coef.max(axis=1)
        tot = np.zeros(len(coef))
        for k in comps:
            if k == 9:
                jl, jh = ln_abs_range(lo[:, 9], hi[:, 9]); d = interval_dist(t[9], jl, jh)
            else:
                d = interval_dist(t[k], lo[:, k], hi[:, k])
            tot += (d / self.sig[k]) ** 2
        return tot

    def cell_min(self, row, t, comps, T=None, tol=1e-4, max_nodes=200000):
        """the least chi2 over the row's cell on the interpolant (best-first branch-and-bound; each sub-rectangle's Bernstein
        coefficients by de Casteljau's halving, its centre value by the basis at 1/2).  With T: stops at the first point
        below T ('below'), or when every enclosure is at least T ('above').  Without T: the minimum within the relative
        tolerance tol (lower bound >= best - tol max(1, best)).  A sub-rectangle below BNB_MIN_SIZE is not split: its bound
        is kept and the status is 'undecided' if it matters.  Returns (status, best chi2, best point, lower bound)."""
        comps = tuple(comps); t = np.asarray(t, float)
        best = float(self._x2(self.feat(self.coords([row]))[0], t, comps)); bp = tuple(self.gs.pts[self.node[row]])
        if T is not None and best < T:
            return "below", best, bp, best
        if not self.ok[row]:
            return ("above" if T is not None else "min"), best, bp, best
        cf0 = self.BM[self.node[row]] @ self.coords(self.stencil_rows([row])[0])
        rect0 = tuple(self.cellr[self.node[row]])
        thr = lambda b: tol * max(1.0, b)
        # a box is kept while it can still matter: in the decision (T given) while its bound is below T -- never pruned
        # against the best value, which would lose points between T - tol and T; in the minimum while its bound is below
        # best - tol.  The lower bound returned covers the boxes discarded on the tolerance (>= best - tol).
        keep = (lambda kl: kl < T) if T is not None else (lambda kl: kl < best - thr(best))
        heap = [(float(self._lb(cf0[None], t, comps)[0]), 0, rect0, cf0)]; cnt = 1; n_done = 0; floor = []
        while heap:
            lb, _, rc, cf = heapq.heappop(heap)
            if not keep(lb):
                heapq.heappush(heap, (lb, -1, rc, cf)); break
            x0, x1, y0, y1 = rc; xm, ym = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
            v = float(self._x2(self.feat(CENTRE @ cf), t, comps))
            if v < best:
                best, bp = v, (xm, ym)
                if T is not None and best < T:
                    return "below", best, bp, lb
            if max(x1 - x0, y1 - y0) < BNB_MIN_SIZE:
                floor.append(lb); continue
            kc = np.einsum("kab,bf->kaf", KIDS, cf)
            rects = ((x0, xm, y0, ym), (x0, xm, ym, y1), (xm, x1, y0, ym), (xm, x1, ym, y1))
            for kl, kr, kf in zip(self._lb(kc, t, comps), rects, kc):
                if keep(kl):
                    heapq.heappush(heap, (float(kl), cnt, kr, kf)); cnt += 1
            n_done += 1
            if n_done > max_nodes:
                floor.extend(h[0] for h in heap); heap = []; break
        live = [f for f in floor if keep(f)]
        if T is not None:
            lb_all = min([h[0] for h in heap] + floor + [best, T])
            return ("undecided" if live else "above"), best, bp, lb_all
        lb_all = min([h[0] for h in heap] + floor + [best - thr(best)])
        return ("undecided" if live else "min"), best, bp, lb_all

    def cell_find2(self, row, t, compsA, boundA, compsB, TB, max_nodes=200000):
        """is there a point of the row's cell with chi2_A <= boundA and chi2_B < TB (the CKM leg's clause: an address the six
        support, within 2^-10 of the posterior's top, reaching the four)?  Branch-and-bound on both enclosures; returns
        ('found' | 'none' | 'undecided', the best chi2_B among points meeting A, the point)"""
        t = np.asarray(t, float)
        f0 = self.feat(self.coords([row]))[0]
        a0, b0 = float(self._x2(f0, t, compsA)), float(self._x2(f0, t, compsB))
        bestB = (b0, tuple(self.gs.pts[self.node[row]])) if a0 <= boundA else (math.inf, None)
        if a0 <= boundA and b0 < TB:
            return "found", b0, bestB[1]
        if not self.ok[row]:
            return "none", bestB[0], bestB[1]
        cf0 = self.BM[self.node[row]] @ self.coords(self.stencil_rows([row])[0])
        stack = [(tuple(self.cellr[self.node[row]]), cf0)]; n_done = 0; und = False
        while stack:
            rc, cf = stack.pop()
            if self._lb(cf[None], t, compsA)[0] > boundA or self._lb(cf[None], t, compsB)[0] >= TB:
                continue
            x0, x1, y0, y1 = rc; xm, ym = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
            f = self.feat(CENTRE @ cf); a, b = float(self._x2(f, t, compsA)), float(self._x2(f, t, compsB))
            if a <= boundA:
                if b < bestB[0]:
                    bestB = (b, (xm, ym))
                if b < TB:
                    return "found", b, (xm, ym)
            if max(x1 - x0, y1 - y0) < BNB_MIN_SIZE:
                und = True; continue
            kc = np.einsum("kab,bf->kaf", KIDS, cf)
            for kr, kf in zip(((x0, xm, y0, ym), (x0, xm, ym, y1), (xm, x1, y0, ym), (xm, x1, ym, y1)), kc):
                stack.append((kr, kf))
            n_done += 1
            if n_done > max_nodes:
                und = True; break
        return ("undecided" if und else "none"), bestB[0], bestB[1]

    # ---- S over the frame ----
    def support(self, t, c_values, T=C.SUPPORT_THRESHOLD, comps=tuple(range(10)), space="nine"):
        """S on continuous tau: the first cell found with chi2 < T (any c), else 'above' when every candidate's enclosure
        is at least T; 'undecided' cells (below BNB_MIN_SIZE) are counted"""
        best = (math.inf, None, None, None); und = 0
        for cv in c_values:
            tt = np.asarray(t, float) - C.c_shift(cv)
            cand = self.candidates(space, tt, T)
            if not len(cand):
                continue
            lb = self.chi2_lower(cand, tt, comps)
            cand = cand[lb < T]; lb = lb[lb < T]
            for i in cand[np.argsort(lb)]:
                st, v, p, _ = self.cell_min(int(i), tt, comps, T=T)
                if v < best[0]:
                    best = (v, int(i), cv, p)
                if st == "below":
                    return {"in_support": True, "min_chi2_found": v, "row": int(i), "c": cv, "point": p, "undecided": und}
                und += st == "undecided"
        return {"in_support": False, "min_chi2_found": best[0], "row": best[1], "c": best[2], "point": best[3], "undecided": und}

    def support_batch(self, T10, c_values, T=C.SUPPORT_THRESHOLD, comps=tuple(range(10)), space="nine") -> dict:
        """S for many worlds (n, 10) at once: per c and bucket one batched ball query; the exact filter on (world, row)
        pairs; a node below T decides at once; the rest by branch-and-bound, world by world, until one cell is below T.
        Returns in_support (n,) and the count of undecided searches."""
        T10 = np.asarray(T10, float); n = len(T10); ins = np.zeros(n, bool); und = 0
        _, buckets = self.trees(space); compsl = list(SPACES[space])
        for cv in c_values:
            todo = np.nonzero(~ins)[0]
            if not len(todo):
                break
            TT = T10[todo] - C.c_shift(cv)
            yq = TT[:, compsl] / self.sig[compsl]
            W, R_ = [], []
            for sel, tree, rmax, Yb in buckets:
                hits = tree.query_ball_point(yq, math.sqrt(T) + rmax + SLACK)
                lens = np.fromiter((len(h) for h in hits), np.int64, len(hits))
                if not lens.sum():
                    continue
                w = np.repeat(np.arange(len(todo)), lens); loc = np.concatenate([np.asarray(h, np.int64) for h in hits if len(h)])
                r = sel[loc]
                d = np.linalg.norm(Yb[loc] - yq[w], axis=1)
                keep = d <= math.sqrt(T) + self.rad[space][r].astype(np.float64) + SLACK
                W.append(w[keep]); R_.append(r[keep])
            if not W:
                continue
            w = np.concatenate(W); r = np.concatenate(R_)
            lb = self.chi2_lower(r, TT[w], comps); keep = lb < T; w, r, lb = w[keep], r[keep], lb[keep]
            if not len(w):
                continue
            fz = self.feat(self.coords(r)); x2n = self._x2(fz, TT[w], comps)
            hit = np.unique(w[x2n < T]); ins[todo[hit]] = True
            rest = ~np.isin(w, hit); w, r, lb = w[rest], r[rest], lb[rest]
            order = np.lexsort((lb, w))
            w, r = w[order], r[order]
            for a in np.unique(w):
                for i in r[w == a]:
                    st, v, _, _ = self.cell_min(int(i), TT[a], comps, T=T)
                    if st == "below":
                        ins[todo[a]] = True; break
                    und += st == "undecided"
        return {"in_support": ins, "undecided": und}

    def global_min(self, t, c_values, comps=tuple(range(10)), space="nine", tol=1e-3):
        """the least chi2 over every cell and the c values (the data's read-out), within the relative tolerance tol: the
        least node chi2 (an attained value) seeds the result; then every candidate whose enclosure can go below it is
        searched by branch-and-bound, best first (the fifth review's B1: the seed was missing, so a node-only argmin or a
        target at a node returned inf or a minimum too high)"""
        best = (math.inf, None, None, None)
        for cv in c_values:
            tt = np.asarray(t, float) - C.c_shift(cv)
            x2max, ub, arg = 4.0, math.inf, None
            while True:                                   # the least node chi2: any node below x2max is a candidate
                cand = self.candidates(space, tt, x2max)
                if len(cand):
                    vals = self._x2(self.feat(self.coords(cand)), tt, comps)
                    k = int(np.argmin(vals))
                    if vals[k] < ub:
                        ub, arg = float(vals[k]), int(cand[k])
                if ub <= x2max or x2max > 1e12:
                    break
                x2max = ub if math.isfinite(ub) else x2max * 16.0
            if arg is None:
                continue
            if ub < best[0]:
                best = (ub, arg, cv, tuple(self.gs.pts[self.node[arg]]))
            cand = self.candidates(space, tt, ub)
            lb = self.chi2_lower(cand, tt, comps)
            order = np.argsort(lb)
            for i, l in zip(cand[order], lb[order]):
                if l >= best[0] * (1 - tol) - tol:
                    break
                st, v, p, _ = self.cell_min(int(i), tt, comps, tol=tol)
                if v < best[0]:
                    best = (v, int(i), cv, p)
        return {"min_chi2": best[0], "row": best[1], "c": best[2], "point": best[3]}

    # ---- K: Gauss tables per node, n x n points, weights dx dy / y^2 normalised over the band ----
    def gauss_table(self, n):
        """per node: the n x n Gauss points' stencil weights (nn, n*n, 9; point index i*n + j over x then y, weight index
        a*3 + b over the stencil's x then y) and log2 weights dx dy / y^2 normalised over the band (nn, n*n); vectorised"""
        if n not in self._gauss:
            gx, gw = np.polynomial.legendre.leggauss(n); nn = len(self.gs.pts); NX, NY = self._axes()
            x0, x1, y0, y1 = self.cellr.T
            xs = (x1 - x0)[:, None] / 2 * gx[None, :] + ((x1 + x0) / 2)[:, None]            # (nn, n)
            ys = (y1 - y0)[:, None] / 2 * gx[None, :] + ((y1 + y0) / 2)[:, None]
            wxq = ((x1 - x0)[:, None] / 2) * gw[None, :]
            wyq = ((y1 - y0)[:, None] / 2) * gw[None, :] / ys ** 2
            LW = np.log2((wxq[:, :, None] * wyq[:, None, :]).reshape(nn, n * n) / (2 * G.band_area()))
            has = np.array([s_ is not None for s_ in self.gs.st])
            Wt = np.zeros((nn, n * n, 9))
            if has.any():
                h = np.nonzero(has)[0]
                lx = self._lag3(xs[h].ravel(), np.repeat(NX[h], n, axis=0)).reshape(len(h), n, 3)
                ly = self._lag3(ys[h].ravel(), np.repeat(NY[h], n, axis=0)).reshape(len(h), n, 3)
                Wt[h] = np.einsum("hia,hjb->hijab", lx, ly).reshape(len(h), n * n, 9)
            self._gauss[n] = (Wt, LW)
        return self._gauss[n]

    def gauss(self, rows, n):
        """(features (m, n*n, 10), log2 weights (m, n*n)) at each row's cell's n x n Gauss points; node-only rows carry their
        node's features at every point with the cell's weights"""
        Wt, LW = self.gauss_table(n)
        rows = np.asarray(rows, np.int64); nd = self.node[rows]
        X = np.repeat(self.coords(rows)[:, None, :], n * n, axis=1)
        okr = self.ok[rows]
        if okr.any():
            idx = np.nonzero(okr)[0]
            X[idx] = np.einsum("mpk,mkf->mpf", Wt[nd[idx]], self.coords(self.stencil_rows(rows[idx])))
        return self.feat(X), LW[nd]

    def log2_cell_measure(self, rows):
        x0, x1, y0, y1 = self.cellr[self.node[np.asarray(rows, np.int64)]].T
        return np.log2((x1 - x0) * (1.0 / y0 - 1.0 / y1) / (2 * G.band_area()))

    def measure_totals(self):
        """(log2 of the largest cell measure over the rows, log2 of the physical rows' total measure), cached"""
        if not hasattr(self, "_mt"):
            lm = self.log2_cell_measure(self.rows); ph = self.phys[self.rows]
            top = lm[ph].max() if ph.any() else -np.inf
            tot = float(top + np.log2(np.exp2(lm[ph] - top).sum())) if ph.any() else -np.inf
            self._mt = (float(lm.max()), tot)
        return self._mt
