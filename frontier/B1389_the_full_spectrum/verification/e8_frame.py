#!/usr/bin/env python3
"""B1389, post-seal (not part of the sealed test) -- the E8 frame and the parity law behind the fuller frames' failure.

E8 > E6 x SU(3): 248 = (78,1) + (1,8) + (27,3) + (27bar,3bar).  The Higgs direction is H = aY + b gamma inside E6 plus (h1, h2, h3),
h1 + h2 + h3 = 0, on the SU(3) Cartan; copy i of the 27 has charges <H, w> + h_i.  The (1,8) is SM-neutral.  Same rule as the sealed
test: a spin-0 sector mu carries sign(q_mu) N, doublets 0 (B1372 Lemma A).

The two facts checked:
(i)  every open region (a != 0) has the 78's X,Y partners (3,2)_{-+5/6} chiral: an exotic, so no region is pure generations;
(ii) on the slice a = 0 (the only way to avoid (i)), every region's SU(5)^3 anomaly (read as [SU(3)]^3 / A(3)) is ODD: the 78's
     gamma-charged 5bar contributes +-1 and every copy of the 27's spin-0 15 contributes 0 (a generation) or +-2 (a whole 15).
Usage: python3 e8_frame.py"""
import itertools
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import full_spectrum as FS                      # the sealed test's vectors and functions


def states_e8(a, b, h):
    st = []
    for i in range(3):
        for w in FS.W0:
            q = a * FS.dot(FS.Y, w) + b * FS.dot(FS.gamma, w) + h[i]
            st.append((w, (q > 0) - (q < 0)))
    for r in FS.Rplus:
        q = a * FS.dot(FS.Y, r) + b * FS.dot(FS.gamma, r)
        st.append((r, (q > 0) - (q < 0)))
    return st


def su5_anomaly(st):
    return FS.anomalies(st)["SU3^3"] / FS.anomalies([(w, 1) for w in FS.W0 if FS.dot(FS.Y, w) == Fr(-1, 3)])["SU3^3"]


if __name__ == "__main__":
    rnd = random.Random(1)
    # (i) open regions: random rational directions with a != 0
    n_open, xy = 0, 0
    for _ in range(4000):
        a, b, h1, h2 = (Fr(rnd.randint(-999, 999), rnd.randint(1, 999)) for _ in range(4))
        if a == 0:
            continue
        st = states_e8(a, b, (h1, h2, -h1 - h2))
        n, named = FS.generations(FS.content(st))
        n_open += 1
        xy += any(k in named for k in (str(("3", "2", Fr(-5, 6))), str(("3b", "2", Fr(5, 6)))))
        assert n is None
    print("E8 frame, open regions: %d random directions with a != 0; X,Y partners chiral in %d; pure generations in none" % (n_open, xy))
    # (ii) the slice a = 0: every region of the arrangement in (b, h1, h2), exact signs round every intersection line
    normals = [(FS.dot(FS.gamma, w), c1, c2) for w in FS.W0 for (c1, c2) in ((1, 0), (0, 1), (-1, -1))]
    normals += [(Fr(1), Fr(0), Fr(0))]
    uniq = []
    for n in normals:
        n = tuple(Fr(x) for x in n)
        if n not in uniq and tuple(-x for x in n) not in uniq:
            uniq.append(n)
    def cross(u, v): return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    lines = []
    for u, v in itertools.combinations(uniq, 2):
        L = cross(u, v)
        if any(x != 0 for x in L):
            lines += [L, tuple(-x for x in L)]
    eps = Fr(1, 10 ** 6)
    regions = {}
    for L in lines:
        base = (Fr(1), Fr(0), Fr(0)) if (L[1] != 0 or L[2] != 0) else (Fr(0), Fr(1), Fr(0))
        P1 = cross(L, base); P2 = cross(L, P1)
        s, n1, n2 = max(abs(x) for x in L), max(abs(x) for x in P1), max(abs(x) for x in P2)
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i == 0 and j == 0:
                    continue
                H = tuple(L[k] / s + eps * (i * P1[k] / n1 + j * P2[k] / n2) for k in range(3))
                sig = tuple((sum(n[k] * H[k] for k in range(3)) > 0) - (sum(n[k] * H[k] for k in range(3)) < 0) for n in uniq)
                if 0 not in sig:
                    regions.setdefault(sig, H)
    odd = 0
    gens = 0
    for sig, (b, h1, h2) in regions.items():
        st = states_e8(Fr(0), b, (h1, h2, -h1 - h2))
        A = su5_anomaly(st)
        odd += (A.denominator == 1 and A.numerator % 2 == 1)
        gens += FS.generations(FS.content(st))[0] is not None and FS.anomaly_free(FS.anomalies(st))
    print("E8 frame, the slice a = 0: %d regions; SU(5)^3 anomaly odd in %d; anomaly-free generations in %d" % (len(regions), odd, gens))
    # the same law on the sealed fuller frames' gamma ray
    for frame in ("F27+78", "F133"):
        H = (Fr(0), Fr(1)) if frame == "F27+78" else (Fr(0), Fr(1), Fr(1, 7))
        print("%s on the gamma ray: SU(5)^3 anomaly %s" % (frame, su5_anomaly(FS.states_for(frame, H))))
    print("DONE")
