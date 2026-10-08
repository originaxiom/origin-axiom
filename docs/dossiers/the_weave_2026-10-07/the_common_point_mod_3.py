#!/usr/bin/env python3
"""Main's B1601 (T-COMMON-POINT-MOD-3), verified with this seat's code: the fibre's trace ideal at the geometric point.

Main's law: for a primitive word w in L and R with both letters, the traces (x, y, z) = (tr a, tr b, tr ab) of the
fibre's hyperbolic holonomy are algebraic integers, and the ideal I = (x, y, z) of the ring of integers of
K = Q(x, y, z) is
  - for odd trace: one prime of residue degree one above 3 (norm 3), with x, y and z each of valuation exactly one there;
  - for even trace: a power of one prime above 2, nothing above 3.
So the holonomy reduced at that prime is the weave's common point, and W3's forced cover is each odd-trace thread's own
congruence cover there. The ideal is unchanged by the moves ((x, z, xz - y) generates the same ideal as (x, y, z)), so
the marking does not matter, and the sign of the state does not change the traces.

This seat's route, independent of main's code:
  (1) the geometric point from sm:B1527's family_lib (sm:B1523's route F, matched to SnapPy's cusp shape), at 60 digits;
  (2) polished by Newton on the Fricke fixed-point equations T_w(v) = v with the cusp condition x^2 + y^2 + z^2 = xyz,
      at the precision named below;
  (3) PARI: the minimal polynomial of a generic linear combination theta of x, y, z (algdep), x, y and z as polynomials
      in theta (lindep), checked EXACTLY in K (the Fricke equations and the cusp condition), and the ideal (x, y, z):
      its norm, its factorization and the valuations of x, y and z at each prime factor. The ideal is supported on the
      primes q dividing g = gcd(N(x), N(y), N(z)); at each q the order is made maximal (nfinit([T, [q]])), and the
      ideal's exponent at each prime above q is the least of the valuations of x, y and z. The full maximal order
      would need the polynomial discriminant factored, which stalled on the long words (a first pass read 26 words
      with the full maximal order, all agreeing, before stalling on the 27th).

The words: every primitive word in L and R with both letters to length 8, up to rotation and the exchange of L and R
(37 geometries, main's population).

    python3 the_common_point_mod_3.py   ->  the_common_point_mod_3.json beside it
"""
import json
import os
import sys
import time
from math import gcd
from pathlib import Path

import mpmath as mp
import sympy as sp
from cypari import pari

# PARI is set up here, before SnapPy (loaded by family_lib) first touches it: a larger stack for the long words, once
pari.allocatemem(10 ** 9, silent=True)
sys.set_int_max_str_digits(0)          # numbers of thousands of digits pass between Python and PARI as strings

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"))
import the_common_point as CP  # noqa: E402
import the_weaves_laws as WL  # noqa: E402
import family_lib as FL  # noqa: E402

DPS = 1200
X, Y, Z = CP.x, CP.y, CP.z


def fricke(word, v):
    """the state's trace map at v: CP.trace_map(word) is TR_{c1} o ... o TR_{cn}, so the last letter acts first. Composed
    letter by letter (no expansion), which works the same on mpmath numbers and on PARI elements of a number field."""
    x, y, z = v
    for c in reversed(word):
        x, y, z = (x, z, x * z - y) if c == "L" else (z, y, y * z - x)
    return x, y, z


def fricke_jac(word, v):
    """the trace map and its Jacobian at v, by the chain rule through the letters"""
    x, y, z = v
    J = mp.eye(3)
    for c in reversed(word):
        if c == "L":
            D = mp.matrix([[1, 0, 0], [0, 0, 1], [z, -1, x]])
            x, y, z = x, z, x * z - y
        else:
            D = mp.matrix([[0, 0, 1], [0, 1, 0], [-1, z, y]])
            x, y, z = z, y, y * z - x
        J = D * J
    return (x, y, z), J


def polish(word, v0):
    """Newton on (T_w(v) - v)_1, (T_w(v) - v)_2 and the cusp condition x^2 + y^2 + z^2 = xyz; the third fixed-point
    equation is checked"""
    v = mp.matrix([mp.mpc(c) for c in v0])
    for _ in range(200):
        (tx, ty, tz), J = fricke_jac(word, v)
        x, y, z = v
        F = mp.matrix([tx - x, ty - y, x ** 2 + y ** 2 + z ** 2 - x * y * z])
        Jm = mp.matrix([[J[0, 0] - 1, J[0, 1], J[0, 2]], [J[1, 0], J[1, 1] - 1, J[1, 2]],
                        [2 * x - y * z, 2 * y - x * z, 2 * z - x * y]])
        step = mp.lu_solve(Jm, F)
        v = v - step
        if mp.norm(step) < mp.mpf(10) ** (-(DPS - 20)):
            break
    (tx, ty, tz) = fricke(word, v)
    x, y, z = v
    res = max(abs(tx - x), abs(ty - y), abs(x ** 2 + y ** 2 + z ** 2 - x * y * z))
    # the origin (the common point itself) is also a fixed point; Newton must stay at the geometric point it started from
    assert max(abs(c) for c in v) > mp.mpf("0.1") and max(abs(a - b) for a, b in zip(v, v0)) < mp.mpf(10) ** -30, \
        ("Newton left the seed", word)
    return [v[0], v[1], v[2]], res, abs(tz - z)


def seed(word, A, B):
    """the 60-digit point in the weave's marking: route F's pair may be the transposed one, so the candidates are the
    traces of (A, B), (B, A), (A, B^-1) and (B, A^-1) (as the_joined_vacuum.py's marked_holonomy), and the one the
    state's Fricke map fixes is kept"""
    x, y = A[0, 0] + A[1, 1], B[0, 0] + B[1, 1]
    z = (A * B)[0, 0] + (A * B)[1, 1]
    best = None
    for v in ((x, y, z), (y, x, z), (x, y, x * y - z), (y, x, x * y - z)):
        d = max(abs(a - b) for a, b in zip(fricke(word, v), v))
        if best is None or d < best[0]:
            best = (d, list(v))
    assert best[0] < mp.mpf(10) ** -40, best[0]
    return best[1]


def exact(word, vals, mix=(2, 3), by_factor=False):
    """K = Q(theta), theta = x + 2y + 3z, in the PARI variable t; x, y, z in the power basis of theta (lindep), then
    checked EXACTLY in K: the Fricke fixed-point equations T_w(v) = v and the cusp condition x^2 + y^2 + z^2 = xyz. The
    ideal (x, y, z) of O_K: its norm, its prime factors, and the valuations of x, y and z at each.

    The minimal polynomial is found degree by degree (algdep, required to agree at two precisions), or, with by_factor,
    by one algdep at degree 64 whose irreducible factor vanishing at theta is taken; either way the exact check in K
    is the certificate."""
    pari.set_real_precision(DPS)
    assert int(pari.default("realprecision")) >= DPS

    def to_pari(c):
        # mpmath writes exponents with a lower-case e, which PARI would read as a variable
        re, im = (mp.nstr(u, DPS - 10).replace("e", "E") for u in (mp.re(c), mp.im(c)))
        return pari(re) + pari("I") * pari(im)
    x, y, z = vals
    th = to_pari(x + mix[0] * y + mix[1] * z)
    xs = [to_pari(c) for c in vals]
    tiny = pari("1E-%d" % (DPS // 2))                     # compared in PARI: a Python float would underflow
    P = coords = None

    def certify(cand, d):
        """x, y, z in the power basis of theta (lindep) and the exact Fricke check in K, or None"""
        Pt = pari.subst(cand, "x", pari("t"))
        cs = []
        for c in xs:
            vec = pari.lindep([c] + [th ** k for k in range(d)])
            if vec[0] == 0:
                return None
            cs.append(pari.Mod(sum(-vec[k + 1] / vec[0] * pari("t") ** k for k in range(d)), Pt))
        image = fricke(word, cs)
        cx, cy, cz = cs
        if all(image[i] == cs[i] for i in range(3)) and cx ** 2 + cy ** 2 + cz ** 2 - cx * cy * cz == 0:
            return cs
        return None

    if by_factor:
        cand = pari.algdep(th, 64)
        fa = pari.factor(cand)
        best = None
        for i in range(int(pari.matsize(fa)[0])):
            f = fa[i, 0]
            if pari.poldegree(f) < 1:
                continue
            r = pari.abs(pari.subst(f, "x", th))
            if best is None or r < best[0]:
                best = (r, f)
        f = best[1] if pari.pollead(best[1]) > 0 else -best[1]
        d = int(pari.poldegree(f))
        if pari.polisirreducible(f) and best[0] < tiny:
            cs = certify(f, d)
            if cs is not None:
                P, coords = f, cs
    else:
        pari.set_real_precision(DPS // 2)
        th_lo = to_pari(x + mix[0] * y + mix[1] * z)            # the same number at half the precision
        pari.set_real_precision(DPS)
        for d in range(1, 61):
            try:
                cand = pari.algdep(th, d)
                cand_lo = pari.algdep(th_lo, d)
            except Exception:                 # PARI refuses degree one for a non-real number
                continue
            # the true minimal polynomial is found alike at both precisions; a spurious relation is not
            if cand != cand_lo and cand != -cand_lo:
                continue
            if not (pari.poldegree(cand) == d and pari.polisirreducible(cand)
                    and pari.abs(pari.subst(cand, "x", th)) < tiny):
                continue
            # below the true degree LLL also returns relations with huge coefficients that pass the residual test;
            # a candidate is accepted only when x, y, z expressed in its field satisfy the Fricke equations EXACTLY
            cs = certify(cand, d)
            if cs is not None:
                P, coords = cand, cs
                break
    assert P is not None, "no minimal polynomial found"
    d = int(pari.poldegree(P))
    Pt = pari.subst(P, "x", pari("t"))
    exact_fixed = True                       # checked above, exactly in K
    integral = [all(pari.denominator(cf) == 1 for cf in pari.Vec(pari.charpoly(c))) for c in coords]
    # The ideal (x, y, z) is supported on the primes dividing g = gcd(N(x), N(y), N(z)): at a prime l not dividing g
    # one of x, y, z has a unit norm, and an element with a unit norm is a unit in any order at l (Cayley-Hamilton).
    # So an order maximal at the primes of g suffices, and the full maximal order (whose discriminant PARI would
    # factor, which stalls on the long words) is not needed.
    norms = [abs(int(pari.norm(c))) for c in coords]
    g = 0
    for n_ in norms:
        g = gcd(g, n_)
    assert g > 0
    gprimes = [int(q) for q in pari.factor(g)[0]] if g > 1 else []
    # x, y and z have denominators in theta's power basis (the index of Z[theta]), so the ideal is not built in PARI:
    # at each prime q of g the order is maximal, idealprimedec lists the primes above q, and the ideal's exponent at
    # each is the least of the three valuations (v(x) is v(numerator) - v(denominator), the denominator an integer)
    lifts = [pari.lift(c) for c in coords]
    primes, norm = [], 1
    for q in gprimes:
        nf = pari.nfinit([Pt, [q]])
        for pr in pari.idealprimedec(nf, q):
            vals = [int(pari.idealval(nf, c, pr)) for c in lifts]
            e = min(vals)
            if e > 0:
                f = int(pr[3])
                primes.append({"p": q, "residue degree": f, "exponent": e, "valuations of x, y, z": vals})
                norm *= q ** (f * e)
    assert g % norm == 0
    return {"theta": "x + %d y + %d z" % mix, "degree of K": d, "minimal polynomial of theta": str(Pt),
            "exactly a fixed point on the cusp surface":
            bool(exact_fixed), "x, y, z integral": integral, "norms of x, y, z": norms, "their gcd": g,
            "order maximal at": gprimes, "norm of (x, y, z)": norm, "prime factors": primes}


def one(w):
    """one geometry: the point, the field, the ideal; DPS is this worker's own"""
    global DPS
    t0 = time.time()
    mp.mp.dps = 60
    tr = int(CP.mat(w, 1).trace())
    A, B, _, _ = FL.hyperbolic_sl2("+", w)
    v0 = seed(w, A, B)
    mp.mp.dps = DPS
    vals, res, res3 = polish(w, v0)
    info, dps0 = None, DPS
    # theta = x + a y + b z is tried first at the working precision; a field of high degree whose theta is far
    # from monogenic needs more, and a theta in a proper subfield needs another combination
    # after the first attempt the minimal polynomial is found as the factor at theta of one degree-64 relation, at
    # rising precision (a field of degree 38 has a theta whose minimal polynomial needs more digits than a
    # half-precision filter has); then other thetas, and last the coordinate x itself (theta = x + 0 y + 0 z): on
    # LLRLRLRR, where y is the complex conjugate of x, x + 2y + 3z needs coordinates of more than a hundred digits in
    # its power basis, and x alone generates the field with a small polynomial
    for prec, mix, by_factor in ((dps0, (2, 3), False), (2 * dps0, (2, 3), True), (4 * dps0, (2, 3), True),
                                 (8 * dps0, (2, 3), True), (4 * dps0, (3, 7), True), (8 * dps0, (5, 11), True),
                                 (2 * dps0, (0, 0), True), (4 * dps0, (0, 0), True)):
        if prec != DPS:
            DPS = prec
            mp.mp.dps = DPS
            vals, res, res3 = polish(w, vals)
        try:
            info = exact(w, vals, mix, by_factor)
            info["precision used (digits)"] = DPS
            info["minimal polynomial found by"] = "one degree-64 relation, factored" if by_factor else "degree by degree"
            break
        except AssertionError:
            pass
    DPS = dps0
    if info is None:
        mp.mp.dps = 60
        return {"word": w, "trace": tr, "odd trace": tr % 2 == 1, "failed": "no primitive element found",
                "main's law holds": False, "seconds": round(time.time() - t0, 1), "prime factors": [],
                "degree of K": None, "norm of (x, y, z)": None}
    mp.mp.dps = 60
    odd = tr % 2 == 1
    ps = info["prime factors"]
    law = (len(ps) == 1 and ps[0]["p"] == 3 and ps[0]["residue degree"] == 1 and ps[0]["exponent"] == 1
           and ps[0]["valuations of x, y, z"] == [1, 1, 1]) if odd else \
        (len(ps) == 1 and ps[0]["p"] == 2)
    return {"word": w, "trace": tr, "odd trace": odd, "Newton residual (log10)": float(mp.log10(res + 10 ** -(DPS + 50))),
            "third equation (log10)": float(mp.log10(res3 + 10 ** -(DPS + 50))), **info,
            "main's law holds": law, "seconds": round(time.time() - t0, 1)}


def run():
    from multiprocessing import Pool
    words = [w for w in WL.states(8)]
    order = sorted(words, key=lambda w: -abs(int(CP.mat(w, 1).trace())))     # the long fields first
    # a long run may resume from a cache of finished rows (one JSON line each), named by the environment variable
    # B1601_CACHE; every row in the record is produced by this code
    cache = os.environ.get("B1601_CACHE")
    done = {}
    if cache and Path(cache).exists():
        for ln in Path(cache).read_text(encoding="utf-8").splitlines():
            r = json.loads(ln)
            if not r.get("failed"):
                done[r["word"]] = r
    todo = [w for w in order if w not in done]
    with Pool(4) as pool:
        for row in pool.imap_unordered(one, todo, chunksize=1):
            done[row["word"]] = row
            if cache:
                with open(cache, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(row["word"], row["trace"], row["degree of K"], row["norm of (x, y, z)"],
                  [(q["p"], q["residue degree"], q["exponent"]) for q in row["prime factors"]], row["main's law holds"],
                  row["seconds"], flush=True)
    rows = [done[w] for w in words]
    return {"precision (digits)": DPS, "words": len(rows), "rows": rows,
            "failed": [r["word"] for r in rows if r.get("failed")],
            "main's law holds on every word": all(r["main's law holds"] for r in rows),
            "odd-trace words": sum(r["odd trace"] for r in rows), "even-trace words": sum(not r["odd trace"] for r in rows)}


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_common_point_mod_3.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}))
