"""B1957: agy-002's note M34 (card A2-AMP), Parts 1 and 2, recomputed by main.  Data-free.
The definitions are read from the note and from the text of the seat's script (never run): the Siegel function's
Kubert-Lang logarithm L_a(z), analytic on the upper half plane; for the two generators (bit 0: z -> z/(z+1),
a -> (a1 + a2, a2); bit 1: z -> z + 1, a -> (a1, a1 + a2)) the step constant c = L_a(g z) - L_{a g}(z) and the step of
the twisted eta invariant, d eta = -(2/pi) Im c (B1929's constant); a word's eta is the sum of its steps, plus the
constant L_{-a} - L_a if the word sends the mark to its negative.
 P1.1  c does not depend on z, and 15 d eta is an integer, at all 24 points for both generators.
 P1.2  the 24 x 24 transfer matrix: spectral radius 1/sqrt 2 at alpha = 1/2 and 0.728399602070 at alpha = 1.
 P1.3  the words that keep the mark (2, 4)/5 up to sign: their number, the variance of eta and the two cosine sums, at
       the lengths the note prints.
 P1.4  the automaton against main's own winding of the Siegel function along the word's geodesic (B1929's code).
 P1.5  eta changes sign under the exchange of the two letters with the mark reflected.
 P2.1  odd ticks M0 P: a point of order 5 is kept up to sign exactly when 5 divides the trace; the counts.
 P2.2  on the double cover (the word followed by its letter-exchange) eta is exactly zero."""
import sys, pathlib, functools, math, cmath
import numpy as np, mpmath as mp
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1929_*")) / "verification")); import main_siegel as MS
mp.mp.dps = 40
PTS = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]; IDX = {p: i for i, p in enumerate(PTS)}
STEP = {0: lambda p: ((p[0] + p[1]) % 5, p[1]), 1: lambda p: (p[0], (p[0] + p[1]) % 5)}
MOVE = {0: lambda z: z / (z + 1), 1: lambda z: z + 1}


def L(p, z, terms=70):
    a1, a2 = mp.mpf(p[0]) / 5, mp.mpf(p[1]) / 5; q = mp.exp(2j * mp.pi * z); qa = mp.exp(2j * mp.pi * (a1 * z + a2)); B2 = a1 * a1 - a1 + mp.mpf(1) / 6
    r = 1j * mp.pi + 2j * mp.pi * z * B2 / 2 + 2j * mp.pi * a2 * (a1 - 1) / 2 + mp.log(1 - qa); qn = q
    for _ in range(terms): r += mp.log(1 - qn * qa) + mp.log(1 - qn / qa); qn *= q
    return r


def cocycle():
    z1, z2 = mp.mpc("0.23", "1.31"), mp.mpc("-0.41", "0.97"); K = np.zeros((2, 24), dtype=np.int64); NEG = np.zeros(24, dtype=np.int64); NXT = np.zeros((2, 24), dtype=np.int64); const = integ = 0
    for p in PTS:
        for bit in (0, 1):
            n = STEP[bit](p); c1 = L(p, MOVE[bit](z1)) - L(n, z1); c2 = L(p, MOVE[bit](z2)) - L(n, z2); const = max(const, abs(c1 - c2)); v = -(2 / mp.pi) * mp.im(c1) * 15
            integ = max(integ, abs(v - mp.nint(v)), abs(mp.re(c1))); K[bit, IDX[p]] = int(mp.nint(v)); NXT[bit, IDX[p]] = IDX[n]
        m = ((-p[0]) % 5, (-p[1]) % 5); c1 = L(m, z1) - L(p, z1); c2 = L(m, z2) - L(p, z2); const = max(const, abs(c1 - c2)); v = -(2 / mp.pi) * mp.im(c1) * 15; integ = max(integ, abs(v - mp.nint(v))); NEG[IDX[p]] = int(mp.nint(v))
    return K, NEG, NXT, const, integ


def etas(n, K, NEG, NXT, start, bits=None):
    """15 eta for every word of length n (or the given ones), and where the mark ends: +1 kept, -1 negated, 0 neither"""
    b = np.arange(1 << n, dtype=np.int64) if bits is None else np.asarray(bits, dtype=np.int64); cur = np.full(len(b), IDX[start]); k = np.zeros(len(b), dtype=np.int64)
    for pos in range(n):
        bit = (b >> pos) & 1; k += K[bit, cur]; cur = NXT[bit, cur]
    neg = IDX[((-start[0]) % 5, (-start[1]) % 5)]; end = np.where(cur == IDX[start], 1, np.where(cur == neg, -1, 0)); k = k + np.where(end == -1, NEG[IDX[start]], 0)
    return b, k, end


def word_matrix(b, n):
    M = np.eye(2, dtype=object)
    for pos in range(n - 1, -1, -1):
        M = M @ (np.array([[1, 0], [1, 1]], dtype=object) if (b >> pos) & 1 else np.array([[1, 1], [0, 1]], dtype=object))
    return M


def eta_by_winding(M, a1, a2):
    """main's B1929 route: the Siegel function's winding along the geodesic of gamma = M^T"""
    (a, b), (c, d) = [[int(x) for x in r] for r in M]; tr = a + d; D = tr * tr - 4
    r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b); cen, R = (r1 + r2) / 2, abs(r1 - r2) / 2
    zs = lambda s: complex(cen + R * math.tanh(s), R / math.cosh(s)); ell = 2 * math.log((abs(tr) + math.sqrt(D)) / 2); g = lambda z: (a * z + c) / (b * z + d); s0 = -ell / 2
    s1 = s0 + ell if abs(g(zs(s0)) - zs(s0 + ell)) < 1e-7 * (1 + abs(zs(s0))) else s0 - ell
    Dl = MS.winding_arc(a1, a2, zs, s0, s1); return -(2 / math.pi) * Dl.imag, abs(Dl.real)


if __name__ == "__main__":
    K, NEG, NXT, const, integ = cocycle()
    print("P1.1: the step constant at two base points differs by at most %s; 15 d eta is an integer and Re c = 0 to %s; the steps 15 d eta take the values %s" % (mp.nstr(const, 3), mp.nstr(integ, 3), sorted(set(K.flatten().tolist()))))
    for al, lab in ((mp.mpf(1) / 2, "1/2"), (mp.mpf(1), "1")):
        T = mp.zeros(24, 24)
        for i in range(24):
            for bit in (0, 1): T[i, int(NXT[bit, i])] += mp.exp(1j * mp.pi * al * int(K[bit, i]) / 15) / 2
        ev = mp.eig(T, left=False, right=False); rho = max(abs(e) for e in ev); lead = [e for e in ev if abs(abs(e) - rho) < mp.mpf(10) ** -25]
        print("P1.2: alpha = %s: spectral radius %s; rho^2 - 1/2 = %s; eigenvalues on that circle: %d, of which real: %d" % (lab, mp.nstr(rho, 15), mp.nstr(rho ** 2 - mp.mpf(1) / 2, 3), len(lead), sum(abs(mp.im(e)) < mp.mpf(10) ** -25 for e in lead)))
    note = {6: (5, 0.4580, 0.2618, -0.2854), 8: (21, 0.6305, 0.3125, 0.0725), 10: (85, 0.9422, 0.1626, 0.0418), 12: (345, 1.2661, -0.0049, -0.0035), 14: (1325, 1.6684, 0.0009, -0.0083), 16: (5453, 1.9319, 0.0094, 0.0019), 17: (10976, 2.0774, -0.0027, -0.0048), 18: (21865, 2.2346, 0.0046, -0.0017)}
    worst = 0.0; allrows = {}
    for n in range(4, 19):
        b, k, end = etas(n, K, NEG, NXT, (2, 4)); keep = (end != 0) & (b != 0) & (b != (1 << n) - 1); e = k[keep] / 15.0
        if not len(e): continue
        row = (int(keep.sum()), float(np.var(e)), float(np.mean(np.cos(0.5 * math.pi * e))), float(np.mean(np.cos(math.pi * e)))); allrows[n] = (b[keep], e)
        if n in note:
            d = max(abs(row[0] - note[n][0]), *(abs(round(x, 4) - y) for x, y in zip(row[1:], note[n][1:]))); worst = max(worst, d)
            print("P1.3: n = %2d: %6d words keep the mark; variance %.4f; mean cos(pi eta/2) %+.4f; mean cos(pi eta) %+.4f; against the note's row: %s" % (n, *row, "same" if d < 1e-12 else "DIFFERS by %.4f" % d))
    print("P1.3: largest difference from the note's eight rows, at the four decimals it prints: %.1e" % worst)
    dv = dr = 0.0; cnt = 0
    for n in range(4, 12):
        if n not in allrows: continue
        for b, e in zip(*allrows[n]):
            ev, re = eta_by_winding(word_matrix(int(b), n), 0.4, 0.8); dv = max(dv, abs(ev - e)); dr = max(dr, re); cnt += 1
    print("P1.4: the automaton against main's own winding along the geodesic (B1929's code), all %d words of lengths 4 to 11: largest difference %.1e; Re of the winding at most %.1e" % (cnt, dv, dr))
    ms = 0
    for n in range(4, 15):
        b, k, end = etas(n, K, NEG, NXT, (2, 4)); keep = (end != 0) & (b != 0) & (b != (1 << n) - 1); b2, k2, end2 = etas(n, K, NEG, NXT, (4, 2), bits=((1 << n) - 1) ^ b[keep]); ms = max(ms, int(np.abs(k[keep] + k2).max()) if keep.any() else 0); assert (end2 != 0).all()
    print("P1.5: eta(word, (2,4)) + eta(letters exchanged, (4,2)), lengths 4 to 14: largest |15 sum| = %d (an exact integer)" % ms)
    P = np.array([[0, 1], [1, 0]], dtype=object); mism = 0; counts = {}; zero = 0; pairs = 0; half = 0
    for n in range(1, 15):
        tw = un = 0; bs = np.arange(1 << n, dtype=np.int64); A = np.zeros((len(bs), 2, 2), dtype=np.int64); A[:, 0, 0] = 1; A[:, 1, 1] = 1
        for pos in range(n - 1, -1, -1):
            one = ((bs >> pos) & 1) == 1; A[one, :, 0] += A[one, :, 1]; A[~one, :, 1] += A[~one, :, 0]
        Mo = A[:, :, ::-1].copy(); tr = Mo[:, 0, 0] + Mo[:, 1, 1]; any_ = np.zeros(len(bs), dtype=bool)
        for (a5, b5) in PTS:
            u0 = (Mo[:, 0, 0] * a5 + Mo[:, 0, 1] * b5) % 5; u1 = (Mo[:, 1, 0] * a5 + Mo[:, 1, 1] * b5) % 5; t = (u0 == (-a5) % 5) & (u1 == (-b5) % 5); u = (u0 == a5) & (u1 == b5); tw += int(t.sum()); un += int(u.sum()); any_ |= t | u
            if 5 <= n <= 11 and (t | u).any():
                sel = bs[t | u]; bits2 = (sel << n) | (((1 << n) - 1) ^ sel); _, k2, end2 = etas(2 * n, K, NEG, NXT, (a5, b5), bits=bits2); assert (end2 == 1).all(); zero = max(zero, int(np.abs(k2).max())); pairs += len(sel) if n <= 9 else 0
                _, kh, _ = etas(n, K, NEG, NXT, (a5, b5), bits=((1 << n) - 1) ^ sel); half = max(half, int(np.abs(kh).max()))
        mism += int((any_ != (tr % 5 == 0)).sum()); counts[n] = (tw, un, int((tr % 5 == 0).sum()), int(tr.min()))
    print("P2.1: odd ticks M0 P, lengths 1 to 14: words where 'a point of order 5 is kept up to sign' and '5 divides the trace' disagree: %d; least trace over all words %d" % (mism, min(c[3] for c in counts.values())))
    print("P2.1: (negated, kept) points by length: %s" % ", ".join("%d: (%d, %d)" % (n, counts[n][0], counts[n][1]) for n in sorted(counts)))
    print("P2.1: the note's (40, 40), (48, 48), (112, 112), (256, 256), (504, 504) at lengths 5 to 9 and (15792, 15792) at 14: %s; each is 4 times the number of words whose trace 5 divides: %s" % ([counts[n][:2] for n in (5, 6, 7, 8, 9, 14)] == [(40, 40), (48, 48), (112, 112), (256, 256), (504, 504), (15792, 15792)], all(counts[n][0] == counts[n][1] == 4 * counts[n][2] for n in counts)))
    print("P2.2: eta on the double cover, by the automaton (exact integers), lengths 5 to 11: largest |15 eta| = %d; pairs at lengths 5 to 9: %d (the note: 1,920); the first half-word's own step sum reaches |15 sum| = %d, so the halves are not zero separately" % (zero, pairs, half))
