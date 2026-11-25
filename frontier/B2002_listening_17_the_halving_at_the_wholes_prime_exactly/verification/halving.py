"""B2002, listening card 17 (main, 2026-11-25; data-free): the halving between the covariant unfolding's neutral and charged
sectors, exactly. FLINT characteristic polynomials of the six-move symmetric unfolding (full, on points) and of its neutral
part (on C-orbits); the charged pair's polynomial as the quotient; factorisations; for each neutral factor f, whether f(2x)
made primitive divides the charged polynomial; PARI nfisincl for the field question.
    python3 -B halving.py > halving_run.txt"""
import pathlib, subprocess, time
import numpy as np, flint
HERE = pathlib.Path(__file__).resolve().parent
t0 = time.time()
def leaf(N, start):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    C = lambda v: (v[1], v[2], v[0]); Ci = lambda v: (v[2], v[0], v[1])
    if start is None:
        pts = [(x, y, z) for x in range(N) for y in range(N) for z in range(N) if (x*x + y*y + z*z - x*y*z) % N == 0 and (x, y, z) != (0, 0, 0)]
    else:
        seen, todo = {start}, [start]
        while todo:
            v = todo.pop()
            for g in (L, R, Li, Ri):
                u = g(v)
                if u not in seen: seen.add(u); todo.append(u)
        pts = sorted(seen)
    moves = [L, R, lambda v: C(L(Ci(v))), lambda v: C(R(Ci(v))), lambda v: Ci(L(C(v))), lambda v: Ci(R(C(v)))]
    return pts, moves, C
def polys(N, start):
    pts, moves, C = leaf(N, start); idx = {v: i for i, v in enumerate(pts)}; n = len(pts)
    W = [[0] * n for _ in range(n)]
    for v in pts:
        for m in moves: W[idx[m(v)]][idx[v]] += 1
    sym = all(W[i][j] == W[j][i] for i in range(n) for j in range(n))
    orb, rep = {}, []
    for v in pts:
        if v in orb: continue
        o = len(rep); rep.append(v)
        u = v
        for _ in range(3): orb[u] = o; u = C(u)
    k = len(rep); Q = [[0] * k for _ in range(k)]
    for o, v in enumerate(rep):
        for m in moves: Q[orb[m(v)]][o] += 1
    pW = flint.fmpz_mat(W).charpoly(); pQ = flint.fmpz_mat(Q).charpoly()
    pC, r = divmod(pW, pQ); assert r == 0
    return n, k, sym, pQ, pC
def fac(p):
    c, fs = p.factor(); return fs
def halved(f):
    cs = [int(c) * 2 ** i for i, c in enumerate(f.coeffs())]
    g = flint.fmpz_poly(cs); from math import gcd
    cont = 0
    for c in cs: cont = gcd(cont, c)
    return flint.fmpz_poly([c // cont for c in cs])
def roots_mod(f):
    return sorted((abs(z) for z in np.roots([int(c) for c in reversed(f.coeffs())])), reverse=True) if f.degree() > 0 else []
summary = {}
for N, start, lab in ((27, (3, 3, 3), "mod 27, orbit of (3,3,3)"), (81, (3, 3, 3), "mod 81, orbit of (3,3,3)"), (5, None, "mod 5, leaf"), (7, None, "mod 7, leaf")):
    n, k, sym, pQ, pC = polys(N, start)
    fQ = fac(pQ); fC = fac(pC)
    square = all(e % 2 == 0 for _, e in fC)
    paired, total, rows = 0, 0, []
    slow = None
    for f, e in fQ:
        rts = roots_mod(f); top = max(rts) if rts else 0
        is_top = any(abs(rr - 6) < 1e-9 for rr in rts)
        g = halved(f); div = (pC % g) == 0 if g.degree() > 0 else False
        mult_in_C = 0
        if div:
            q = pC
            while (q % g) == 0: q = q // g; mult_in_C += 1
        if not is_top:
            total += f.degree() * e
            if div: paired += f.degree() * e
        rows.append((f.degree(), e, round(top, 6), is_top, div, mult_in_C))
        if not is_top and (slow is None or top > slow[0]): slow = (top, f)
    print("%s: %d points, %d C-orbits; symmetric: %s; charged polynomial a perfect square over Z (all multiplicities even): %s  [%.0f s]" % (lab, n, k, sym, square, time.time() - t0))
    print("    neutral factors (degree, multiplicity, largest |root|, carries the top, halved version divides the charged polynomial, its multiplicity there):")
    for r in sorted(rows, key=lambda r: -r[2])[:12]: print("      ", r)
    print("    of the neutral non-top degree %d, paired by halving: %d" % (total, paired))
    s = slow[1]; print("    the neutral slowest mode (|root| %.9f) lies on the factor (constant first) %s; its halved version divides the charged polynomial: %s" % (slow[0], [int(c) for c in s.coeffs()], (pC % halved(s)) == 0))
    summary[lab] = (paired, total, slow, (pC % halved(s)) == 0)
    if N == 81:
        poly = " + ".join("(%d)*x^%d" % (int(c), i) for i, c in enumerate(s.coeffs()))
        gp = subprocess.run(["/usr/local/bin/gp", "-q", "-f"], input="f = %s; print(poldegree(f)); print(nfisincl(y^3 - 3*y + 1, polredabs(f)) != 0); print(factor(nfdisc(f)));\n" % poly.replace("x^0", "1").replace("x", "x"), capture_output=True, text=True, timeout=600).stdout
        print("    H5 (PARI): degree, Q(cos 2pi/9) inside its field, discriminant of its field: %s" % gp.split())
