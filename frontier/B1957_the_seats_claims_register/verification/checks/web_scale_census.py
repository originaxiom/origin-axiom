"""B1957: the web seat's sealed check 'the scale on the weave and at the cusp' (2026-10-14), run again on main's own
script.  Main verified it at the time (B1650); this is a second run by main, written from the seal's definitions.
Data-free.
 C1  the 745 threads of length 2 to 12 (SnapPy, b++ words): how many have Chern-Simons invariant not 0 modulo pi^2;
     the swap-symmetric ones (the least rotation of the exchanged word is the word, or its reversal's) and their CS;
     whether CS = 0 exactly on those; mirror pairs: equal volume, opposite CS; every solution geometric.
 C2  Gueritaud and Futer's bound 2 n v3 <= Vol < 2 n v8 (n the number of R-syllables) on all 745; the least volumes.
 C3  Vol(L^a R^b) for a, b up to 25: below 2 v8 = 7.3277, increasing in a and in b; the diagonal values.
 C4  the local model (sympy, exact): for theta = E12 dz/z, h = diag(1/(L + b), L + b) with L = -log|z|^2 solves
     Hitchin's equation for every b; the residue's norm is 1/(L + b); a unit vector of the complete metric has
     |dz/z| = L/2, so the field's pointwise norm is L/(2(L + b)), 1/2 at b = 0.
 C5  the central charges of the cosets g_1 x g_1 / g_2: 1/2 (A1, E8), 4/5 (A2), 6/7 (E6), 7/10 (E7); c((E6)_1) = 6."""
import functools, math, warnings
from fractions import Fraction as Fr
print = functools.partial(print, flush=True)
import pathlib as _pl, sys as _sys
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))          # the sibling below is found in isolated mode too (the web seat's section 9, 2026-11-18)
import web_selection_exact as S
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); import snappy
PI2 = math.pi ** 2; V3 = 1.0149416064096536; V8 = 3.6638623767088760
sw = str.maketrans("LR", "RL"); least = lambda w: min(w[i:] + w[:i] for i in range(len(w)))


def data(w):
    M = snappy.Manifold("b++" + w); cv = M.complex_volume(); cs = float(cv.imag()); cs = (cs + PI2 / 2) % PI2 - PI2 / 2
    return float(cv.real()), cs, M.solution_type()


if __name__ == "__main__":
    words = [w for n in range(2, 13) for w in S.lyndon(n)]; D = {w: data(w) for w in words}
    nz = [w for w in words if abs(D[w][1]) > 1e-6]; sym = [w for w in words if least(w.translate(sw)) in (w, least(w[::-1]))]
    two = [w for w in words if min(abs(2 * D[w][1]) % PI2, PI2 - abs(2 * D[w][1]) % PI2) < 1e-6]
    mir = max(max(abs(D[w][0] - D[least(w.translate(sw))][0]), abs(D[w][1] + D[least(w.translate(sw))][1])) if abs(abs(D[w][1]) - PI2 / 2) > 1e-6 else 0.0 for w in words)
    print("C1: threads %d; CS not 0 modulo pi^2: %d (%.1f%%); swap-symmetric: %d, all with CS = 0: %s (largest |CS| among them %.1e); the threads with 2 CS = 0 are exactly the swap-symmetric ones: %s; mirror pairs: volumes equal and CS opposite to %.1e; every solution 'all tetrahedra positively oriented': %s" % (
        len(words), len(nz), 100 * len(nz) / len(words), len(sym), all(abs(D[w][1]) < 1e-6 for w in sym), max(abs(D[w][1]) for w in sym), sorted(two) == sorted(sym), mir, all(D[w][2] == "all tetrahedra positively oriented" for w in words)))
    print("C1: the root: volume %.10f, |CS| %.1e; CS(LLR) = %.6f, -pi^2/24 = %.6f; |CS| median %.2f, largest %.2f" % (D["LR"][0], abs(D["LR"][1]), D["LLR"][1], -PI2 / 24, sorted(abs(D[w][1]) for w in words)[len(words) // 2], max(abs(D[w][1]) for w in words)))
    syl = lambda w: sum(1 for i in range(len(w)) if w[i] == "R" and w[i - 1] == "L")
    gf = all(2 * syl(w) * V3 - 1e-9 <= D[w][0] < 2 * syl(w) * V8 for w in words); order = sorted(words, key=lambda w: D[w][0])
    print("C2: Gueritaud and Futer's bound on all 745: %s; the least volumes: %s; the least among threads with two or more syllable pairs: %.4f (4 v3 = %.4f)" % (gf, [(w, round(D[w][0], 4)) for w in order[:3]], min(D[w][0] for w in words if syl(w) >= 2), 4 * V3))
    vol = {(a, b): float(snappy.Manifold("b++" + "L" * a + "R" * b).volume()) for a in range(1, 26) for b in range(1, 26)}
    inc = all(vol[(a + 1, b)] > vol[(a, b)] for a in range(1, 25) for b in range(1, 26)) and all(vol[(a, b + 1)] > vol[(a, b)] for a in range(1, 26) for b in range(1, 25))
    print("C3: Vol(L^a R^b), a, b up to 25: the largest %.4f at %s, below 2 v8 = %.4f: %s; increasing in a and in b: %s; the diagonal at a = 1, 2, 3, 5, 10, 25: %s (v8 = %.4f)" % (
        max(vol.values()), max(vol, key=vol.get), 2 * V8, max(vol.values()) < 2 * V8, inc, [round(vol[(a, a)], 4) for a in (1, 2, 3, 5, 10, 25)], V8))
    import sympy as sp
    z, zb, b = sp.symbols("z zb b"); Lh = -sp.log(z * zb) + b; h1, h2 = 1 / Lh, Lh
    # Hitchin: -d_zbar d_z log h_i (the curvature's diagonal) plus the commutator [theta, theta^*] = (h1/h2)(E11 - E22)/|z|^2
    eq1 = sp.simplify(-sp.diff(sp.log(h1), z, zb) + (h1 / h2) / (z * zb)); eq2 = sp.simplify(-sp.diff(sp.log(h2), z, zb) - (h1 / h2) / (z * zb))
    # CHANGED 2026-11-18 (the web seat's own reading of the second reading, its rows 58 and 59): the norms below were printed
    # as fixed text; they are computed now.  On the circle |z| = r, L = -log r^2; the cusp metric is 4|dz|^2/(|z|^2 L^2).
    Lp, th, rr = sp.symbols("L theta r", positive=True)                                               # L = -log r^2 > 0 on the punctured disc r < 1
    res_norm = sp.simplify(sp.sqrt((h1 / h2).subs(b, 0).subs(sp.log(z * zb), -Lp)))                    # |E12|_h = sqrt(h1/h2)
    horo = sp.integrate(sp.Integer(2) / (rr * Lp) * rr, (th, 0, 2 * sp.pi))                             # ds = 2|dz|/(|z| L), |dz| = r dtheta on |z| = r
    unit = sp.simplify((rr * Lp / 2) / rr)                                                             # a unit vector has |v| = r L/2; |dz/z|(v) = |v|/r
    point = sp.simplify(sp.sqrt((h1 / h2).subs(sp.log(z * zb), -Lp)) * unit)
    la, lb = sp.symbols("la lb", real=True); lam = la + sp.I * lb; Th = lam * sp.diag(1, -1); Ths = sp.conjugate(lam) * sp.diag(1, -1)         # the semisimple control: theta = lambda diag(1, -1) dz/z
    semis = (Th * Ths - Ths * Th).applyfunc(sp.simplify) == sp.zeros(2, 2) and sp.simplify(-sp.diff(sp.log(sp.Integer(1)), z, zb)) == 0 and sp.simplify(sp.sqrt(sp.expand((Th * Ths)[0, 0])) - sp.sqrt(la ** 2 + lb ** 2)) == 0
    print("C4: Hitchin's equation for h = diag(1/(L + b), L + b), both diagonal entries: %s, %s (zero for every b); the residue's norm at b = 0: %s, so 1/L; the horocycle |z| = r has length %s, so the norm is the length over 4 pi: %s; |dz/z| on a unit vector: %s; the field's pointwise norm: %s, which is 1/2 at b = 0: %s; the semisimple control (theta = lambda diag(1, -1) dz/z): [theta, theta*] = 0, h = 1 flat, and the residue's norm |lambda| in h, constant: %s"
          % (eq1, eq2, res_norm, horo, sp.simplify(res_norm - horo / (4 * sp.pi)) == 0, unit, point, sp.simplify(point.subs(b, 0) - sp.Rational(1, 2)) == 0, semis))
    c = lambda dim, hv, k: Fr(k * dim, k + hv); alg = {"A1": (3, 2), "A2": (8, 3), "E6": (78, 12), "E7": (133, 18), "E8": (248, 30)}
    print("C5: 2 c(g_1) - c(g_2): %s; c((E6)_1) = %s" % ({g: str(2 * c(d, h, 1) - c(d, h, 2)) for g, (d, h) in alg.items()}, c(78, 12, 1)))
