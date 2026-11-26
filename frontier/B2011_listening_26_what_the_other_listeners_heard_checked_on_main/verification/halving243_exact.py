"""B2011, A3 (main, 2026-11-26; data-free): the halving identity at mod 243, exactly over the integers:
p_neutral(2x) = 2^d (x^2 - 9) x S(x), with S the q = 1 charged sector's polynomial (sectors_exact.py; CRT to the bound).
    python3 -B halving243_exact.py > halving243_exact_run.txt"""
import pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import flint
from sectors_exact import sector_data, exact_charpolys, halved_monic
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
data = sector_data(243)
log("mod 243, orbit of (3,3,3): %d points; C fixes %d; neutral dimension %d, charged (q = 1) dimension %d" % (data["n"], data["fixed"], data["d0"], data["d1"]))
pn, pc = exact_charpolys(data, log)
h = halved_monic(pn)
rhs = flint.fmpz_poly([-9, 0, 1]) * flint.fmpz_poly([0, 1]) * pc
log("p_neutral(2x) / 2^d == (x^2 - 9) x S(x) exactly over Z: %s" % (h == rhs))
log("p_neutral: x^0..x^2 coefficients %s; S: x^0..x^2 coefficients %s" % ([int(c) for c in pn.coeffs()[:3]], [int(c) for c in pc.coeffs()[:3]]))
