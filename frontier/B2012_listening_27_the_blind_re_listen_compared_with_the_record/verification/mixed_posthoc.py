"""B2012, POST HOC (labelled; written after mixed_levels_run.txt showed the halving holding at mod 54 and failing at 189): the halving at mod 108 = 27 * 4 and mod 162 = 81 * 2, exactly
over Z, with B2011's sector module (imported from its committed folder): the orbit of (3,3,3), C's fixed points, the
gcd of p_neutral(2x)/2^d with the charged polynomial, and what is left unpaired, factored.
    python3 -B mixed_posthoc.py > mixed_posthoc_run.txt"""
import pathlib, sys, time
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(next(ROOT.glob("frontier/B2011_*/verification"))))
import flint
from sectors_exact import leaf, sector_data, exact_charpolys, halved_monic
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
for N, q in ((108, 4), (162, 2)):
    d = sector_data(N)
    pts27 = set(leaf(N // q)[0]); ptsq = set(leaf(q)[0]); pts = leaf(N)[0]
    log("mod %d = (N/q) * %d, orbit of (3,3,3): %d points (mod N/q: %d, mod %d: %d, product %d); C fixes %d; neutral dimension %d, charged %d" % (
        N, q, d["n"], len(pts27), q, len(ptsq), len(pts27) * len(ptsq), d["fixed"], d["d0"], d["d1"]))
    pn, pc = exact_charpolys(d, log)
    h = halved_monic(pn)
    rhs = flint.fmpz_poly([-9, 0, 1]) * flint.fmpz_poly([0, 1]) * pc
    g = h.gcd(pc); unc, r = divmod(pc, g); assert r == 0
    fac = lambda f: [([int(c) for c in u.coeffs()], e) for u, e in f.factor()[1]] if f.degree() > 0 else []
    log("    halving identity p_neutral(2x)/2^d == (x^2 - 9) x S(x) exactly: %s; gcd degree %d of the charged %d; charged unpaired: degree %d, factors %s" % (
        h == rhs, g.degree(), pc.degree(), unc.degree(), fac(unc)))
