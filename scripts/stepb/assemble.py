"""STEP B's generator, the assembly of discrete choices and their tau cells over the whole band (data-free).

A discrete choice is (line class, direction, radius, reading); c is applied by shifting the target.  Only rows with the
mixing defined enter (the third review's B4: S, K, p2 and the CKM leg refer to one address set).  Its tau cells are
the census's right half (Re tau in [0, 1/2]) for its own line, and the mirror partner's right half read as its left half
(B1821: (-x + iy, (a, -b)) = (x + iy, (a, b)) with J -> -J).  Each half's cells carry half their area weight, so the
weights sum to one over the band Re in [-1/2, 1/2].  A self-mirror line counts its own cells twice at half weight each.

The six's code and the mixtures on continuous tau are kten.py's (through cells.py).  Rows of an error configuration are
absent from both the data's and the null's code."""
from __future__ import annotations

import math

import numpy as np

import compression as K
import grid as G
import stepb_core as C
from census_io import mirror_partner


class Choices:
    def __init__(self, census: C.Census, F: np.ndarray, tau_points):
        """tau_points: the census grid's points (re, im) in a fixed order; census.tau gives each configuration's point"""
        pts = [tuple(p) for p in tau_points]
        pidx = {p: i for i, p in enumerate(pts)}
        self.n_tau = len(pts)
        self.w_half = G.area_weights(pts) / 2.0
        cfg_line = census.lines
        cfg_tau = [pidx[(round(float(t[0]), 4), round(float(t[1]), 4))] for t in census.tau]
        keys = {}
        rows_of = {}
        vdef = np.asarray(census.vdef, bool)
        for i in range(len(census.cfg)):
            if not vdef[i]:
                continue
            ci = int(census.cfg[i])
            q = (cfg_line[ci], int(census.d[i]), int(census.r[i]), int(census.k[i]))
            rows_of.setdefault(q, np.full(self.n_tau, -1, dtype=np.int64))[cfg_tau[ci]] = i
        self.keys = sorted(rows_of, key=lambda q: (str(q[0]), q[1], q[2], q[3]))
        R = np.stack([rows_of[q] for q in self.keys])
        P = np.stack([rows_of.get((mirror_partner(q[0]),) + q[1:], np.full(self.n_tau, -1, dtype=np.int64)) for q in self.keys])
        self.R, self.P = R, P
        self.A = K.A_DISCRETE
