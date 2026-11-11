#!/usr/bin/env python3
"""Re-audit 6, the finding E5: the walls on the line of the second measurement, checked again by this seat.

Main's mend (a3e20450b; B892's verification/walls_on_the_line.py) says: s1 = x8 + t1 x16, x14, x16 and x22 commute and are
diagonalised together; on the 46 joint eigenvectors that s1 kills, 12 weights vanish on x14 and x16 and 30 on x16; the
joint nullity of ad(s1) and ad(x14 + t x16) jumps at finite t only at t = +-0.0464130116 i (to 18) and t = +-0.0515261607 i
(to 14); so at every real t it is 12.  Main's run is in double precision, on matrices it first balances over fourteen
orders of magnitude, with "vanishes" meaning below 1e-7 of the largest weight.

WHAT IS SHARED WITH MAIN: the algebra itself.  E6's structure constants and the four invariants are B854's, built over Q
and loaded here as main loads them.  Nothing of walls_on_the_line.py is used.
WHAT IS DIFFERENT: (1) the two counts that do not involve t1 are computed EXACTLY, as ranks over Q; (2) the weights are
computed at 60 digits with no balancing, so "vanishes" is below 1e-30 and not below 1e-7; (3) a control shows that the
same machinery finds a REAL wall where one is known.

    python3 e5_independent.py --main DIR          (DIR: a scratch checkout of main; B854's module writes a file there)

WHY TWO COUNTS ARE RATIONAL.  s1 = x8 + t1 x16, so an element commutes with s1 and x16 exactly when it commutes with x8
and x16.  The nullity at pure x16 is dim(z(x8) ∩ z(x16)), and the generic nullity is dim(z(x8) ∩ z(x14) ∩ z(x16)).

EXPECTATIONS, written before the first run (main's numbers; v9 is this seat's own control).
  v1  the six brackets among x8, x14, x16, x22 vanish exactly
  v2  dim(z(x8) ∩ z(x16)) = 30, exactly over Q                  (the plane stratum at pure x16)
  v3  dim(z(x8) ∩ z(x14) ∩ z(x16)) = 12, exactly over Q         (the generic nullity)
  v4  at 60 digits one change of basis diagonalises all four ad-matrices: the off-diagonal part of each is below 1e-30
      of its diagonal
  v5  46 weights vanish on s1 (below 1e-30 of the largest); the smallest that does not is above 1e-6 of the largest
  v6  of those 46, 30 vanish on x16, and 12 on x14 and x16
  v7  the other 16 give t = -weight(x14)/weight(x16) in four groups: six at +0.0464130116 i, six at -0.0464130116 i, two at
      +0.0515261607 i, two at -0.0515261607 i (to 1e-9), each with a real part below 1e-30 of its modulus
  v8  (follows from v5 to v7; printed, not computed again) at every real t the joint nullity is 12
  v9  CONTROL, a real wall the machinery must find: on the line x8 + t x16, with no s1, 30 weights vanish on x8 and x16
      and exactly 16 more vanish at the real point t = t1 (46 = 30 + 16), where -weight(x8)/weight(x16) equals t1 to 1e-30.
      The other real walls of that line are printed with no expectation
"""
import sys, os, io, contextlib, time
from fractions import Fraction

main_dir = os.path.abspath(sys.argv[sys.argv.index("--main") + 1])
B854 = os.path.join(main_dir, "frontier", "B854_centralizer_exact", "e6_centralizer.py")
CUBIC = [500716339200, -159667200, -28224, 1]            # main's: t1 = 13 x its smallest real root
t0 = time.time()
g = {"__file__": B854, "__name__": "b854_for_the_reaudit"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(B854).read(), B854, "exec"), g)
DIM, N, br, hvec, evec, ROOTS, INV = g["DIM"], g["N"], g["br"], g["hvec"], g["evec"], g["ROOTS"], g["INV"]
basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
NS = (8, 14, 16, 22)
results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-3s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


def ad_exact(v):
    """ad(v) as a DIM x DIM matrix of Fractions: column q holds [v, basis_q]"""
    cols = [[Fraction(c) for c in br(v, basis[q])] for q in range(DIM)]
    return [[cols[q][r] for q in range(DIM)] for r in range(DIM)]


AD = {n: ad_exact(INV[n]) for n in NS}
assert all(len(INV[n]) == DIM == 78 for n in NS)
pairs = [(a, b) for a in NS for b in NS if a < b]
nonzero = [(a, b) for a, b in pairs if any(c != 0 for c in br(INV[a], INV[b]))]
line("v1", not nonzero, "brackets among the four invariants that do not vanish: %s of %d" % (nonzero if nonzero else "none", len(pairs)))


def rank_exact(rows):
    """rank over Q by elimination on integers (each row cleared of denominators and of its common factor)"""
    from math import gcd
    M = []
    for r in rows:
        den = 1
        for c in r:
            den = den * c.denominator // gcd(den, c.denominator)
        ints = [int(c * den) for c in r]
        if any(ints):
            M.append(ints)
    rank, ncols = 0, len(rows[0])
    for col in range(ncols):
        piv = next((i for i in range(rank, len(M)) if M[i][col]), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        p = M[rank]
        for i in range(rank + 1, len(M)):
            if M[i][col]:
                f = M[i][col]
                row = [p[col] * x - f * y for x, y in zip(M[i], p)]
                gg = 0
                for x in row:
                    gg = gcd(gg, x)
                M[i] = [x // gg for x in row] if gg > 1 else row
        rank += 1
        M = M[:rank] + [r for r in M[rank:] if any(r)]
    return rank


n_plane = DIM - rank_exact(AD[8] + AD[16])
line("v2", n_plane == 30, "dim(z(x8) ∩ z(x16)), exactly over Q: %d" % n_plane)
n_generic = DIM - rank_exact(AD[8] + AD[14] + AD[16])
line("v3", n_generic == 12, "dim(z(x8) ∩ z(x14) ∩ z(x16)), exactly over Q: %d" % n_generic)
print("    (the algebra loaded and the exact part done in %.0f s)" % (time.time() - t0), flush=True)

# ---- the weights, at 60 digits
import mpmath as mp
mp.mp.dps = 60
X = {n: mp.matrix([[mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in row] for row in AD[n]]) for n in NS}


def norm1(M):
    return max(sum(abs(M[i, j]) for i in range(M.rows)) for j in range(M.cols))


scale = {n: norm1(X[n]) for n in NS}
coef = {8: mp.mpf(7) / 11, 14: mp.mpf(5) / 13, 16: mp.mpf(3) / 17, 22: mp.mpf(1)}          # a generic combination, this seat's own
G = sum((coef[n] / scale[n]) * X[n] for n in NS) + mp.mpf(9) / 7 * mp.eye(DIM)    # shifted: the eigenvectors are the same, and none belongs to 0
E, V = mp.eig(G)
Vi = mp.inverse(V)
W, off = {}, {}
for n in NS:
    Dn = Vi * X[n] * V
    diag = [Dn[i, i] for i in range(DIM)]
    off[n] = max(abs(Dn[i, j]) for i in range(DIM) for j in range(DIM) if i != j) / max(abs(d) for d in diag)
    W[n] = diag
worst = max(off.values())
line("v4", worst < mp.mpf(10) ** -30, "the largest off-diagonal part, over the largest weight, for x8, x14, x16, x22: %s; the eigenvectors' matrix times its inverse, in the 1-norm: %s"
     % (", ".join(mp.nstr(off[n], 3) for n in NS), mp.nstr(norm1(V) * norm1(Vi), 4)))
print("    (the weights done at %.0f s)" % (time.time() - t0), flush=True)

roots = mp.polyroots([mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=200)             # highest power first, as main passes it to numpy
real_roots = sorted(r.real for r in roots if abs(r.imag) < mp.mpf(10) ** -40 * max(1, abs(r)))
t1 = 13 * real_roots[0]
s1 = [W[8][i] + t1 * W[16][i] for i in range(DIM)]
big = {n: max(abs(w) for w in W[n]) for n in NS}
s1big = max(abs(w) for w in s1)
TINY = mp.mpf(10) ** -30
Z = [i for i in range(DIM) if abs(s1[i]) < TINY * s1big]
gap = min(abs(s1[i]) for i in range(DIM) if i not in Z) / s1big
line("v5", len(Z) == 46 and gap > mp.mpf(10) ** -6, "weights that vanish on s1: %d; the smallest that does not is %s of the largest; the largest that does is %s of it"
     % (len(Z), mp.nstr(gap, 4), mp.nstr(max(abs(s1[i]) for i in Z) / s1big, 3)))
zero = lambda n, i: abs(W[n][i]) < TINY * big[n]
plane = [i for i in Z if zero(16, i)]
generic = [i for i in Z if zero(16, i) and zero(14, i)]
line("v6", (len(plane), len(generic)) == (30, 12), "of those, vanish on x16: %d; on x14 and x16: %d" % (len(plane), len(generic)))
ts = [-W[14][i] / W[16][i] for i in Z if i not in plane]
want = {(+1, "0.0464130116"): 6, (-1, "0.0464130116"): 6, (+1, "0.0515261607"): 2, (-1, "0.0515261607"): 2}
got = {}
for t in ts:
    near = [ref for ref in ("0.0464130116", "0.0515261607") if abs(abs(t.imag) - mp.mpf(ref)) < mp.mpf("1e-9")]
    key = (1 if t.imag > 0 else -1, near[0] if near else "elsewhere: " + mp.nstr(t, 12))
    got[key] = got.get(key, 0) + 1
realpart = max(abs(t.real) / abs(t) for t in ts) if ts else mp.mpf(1)
line("v7", got == want and realpart < TINY, "the %d finite walls t = -w14/w16: %s; the largest real part over the modulus: %s"
     % (len(ts), "; ".join("%d at %s%s i" % (v, "+" if k[0] > 0 else "-", k[1]) for k, v in sorted(got.items(), key=lambda kv: (kv[0][1], -kv[0][0]))), mp.nstr(realpart, 3)))
if ts:
    for label, sel in (("the walls of nullity 18", [t for t in ts if abs(abs(t.imag) - mp.mpf("0.0464130116")) < mp.mpf("1e-9")]),
                       ("the walls of nullity 14", [t for t in ts if abs(abs(t.imag) - mp.mpf("0.0515261607")) < mp.mpf("1e-9")])):
        if sel:
            print("    %s, |t| to 40 digits: %s" % (label, mp.nstr(abs(sel[0]), 40)))
v8 = all(results[4:7])
line("v8", v8, "so, at every real t, no weight beyond the generic %d vanishes on s1 and on x14 + t x16: the nullity is %d there (it is %d at pure x16)" % (len(generic), len(generic), len(plane)))

# ---- control: a real wall the machinery must find.  On the line x8 + t x16, s1 itself is the point t = t1.
both = [i for i in range(DIM) if zero(8, i) and zero(16, i)]
cand = {}
for i in range(DIM):
    if i in both or zero(16, i):
        continue
    t = -W[8][i] / W[16][i]
    if abs(t.imag) < TINY * abs(t):
        key = mp.nstr(t.real, 25)
        cand.setdefault(key, []).append(t.real)
at_t1 = [k for k, v in cand.items() if abs(v[0] - t1) < TINY * abs(t1)]
others = sorted((k, len(v)) for k, v in cand.items() if k not in at_t1)
n_at = len(cand[at_t1[0]]) if at_t1 else 0
line("v9", len(at_t1) == 1 and n_at == 16 and len(both) == 30,
     "control, the line x8 + t x16: at the real point t1 = %s vanish %d weights beyond the %d that vanish on both (z(s1) = %d)"
     % (mp.nstr(t1, 20), n_at, len(both), len(both) + n_at))
print("    read-out, no expectation: the other real walls of that line, with how many weights vanish at each: %s"
      % ("; ".join("t = %s: %d" % (mp.nstr(mp.mpf(k), 12), n) for k, n in others) if others else "none"))
print("    read-out: the cubic's roots times 13: %s" % ", ".join(mp.nstr(13 * r, 15) for r in roots))
print()
print("expectations that hold: %d of %d      (%.0f s)" % (sum(results), len(results), time.time() - t0))
sys.exit(0 if all(results) else 1)
