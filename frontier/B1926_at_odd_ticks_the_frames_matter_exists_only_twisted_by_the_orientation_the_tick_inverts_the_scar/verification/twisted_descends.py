"""B1926's addendum (main, 2026-11-14): the orientation-twisted classes at an odd tick level are the double cover's
sector-module data seen from below.

At level n (odd), take each fibre-torsion character (x, y) with the twisted value of t (l(mu) = -1). Pull it back to the
orientation double cover, level 2n (t_2n = t_n^2). Expectation, written before the run: it is a character of level 2n,
trivial on that level's meridian, and it carries a class non-zero on the scar, so it is the record's sector-module data
upstairs. Uses B1926's verification code (odd_ticks_no_modules.py); run from that folder."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import odd_ticks_no_modules as O

P = 19141


def check(n, p=P):
    g3, _ = O.find_g(n); g6, _ = O.find_g(2 * n)
    ex = O.torsion_exponent(n)[0]
    z = next(x for x in range(2, p) if all(pow(pow(x, (p - 1) // ex, p), ex // q, p) != 1 for q in range(2, ex + 1) if ex % q == 0 and O.isprime(q)))
    zeta = pow(z, (p - 1) // ex, p)
    rels = [O.red((O.T, O.A, -O.T) + O.inv(O.sigma_n((O.A,), 2 * n))), O.red((O.T, O.B, -O.T) + O.inv(O.sigma_n((O.B,), 2 * n)))]
    tw = ok = mu1 = cls = 0
    for i in range(ex):
        for j in range(ex):
            x, y = pow(zeta, i, p), pow(zeta, j, p)
            if (x, y) == (1, 1):
                continue
            ch = {O.A: x, O.B: y, O.T: 1}
            if O.char_val(ch, O.sigma_n((O.A,), n), p) != x or O.char_val(ch, O.sigma_n((O.B,), n), p) != y:
                continue
            tn = (-O.char_val(ch, g3, p)) % p
            tw += 1
            ch2 = {O.A: x, O.B: y, O.T: tn * tn % p}
            ok += O.char_val(ch2, O.sigma_n((O.A,), 2 * n), p) == x and O.char_val(ch2, O.sigma_n((O.B,), 2 * n), p) == y
            mu1 += O.char_val(ch2, O.inv(g6), p) * ch2[O.T] % p == 1
            F = [[O.fox(r, gen, ch2, p) for gen in (O.A, O.B, O.T)] for r in rels]
            lam = [O.fox(O.LAM, gen, ch2, p) for gen in (O.A, O.B, O.T)]
            cls += any(sum(a * b for a, b in zip(lam, v)) % p for v in O.nullspace(F, p, 3))
    return tw, ok, mu1, cls


if __name__ == "__main__":
    for n in (3, 5, 7):
        tw, ok, mu1, cls = check(n)
        print("level %d -> level %d: twisted characters %d; characters upstairs %d; trivial on the meridian upstairs %d; with a class non-zero on the scar upstairs %d" % (n, 2 * n, tw, ok, mu1, cls), flush=True)
