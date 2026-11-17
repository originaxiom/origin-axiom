"""B1957: agy-002's note M34, Part 0, section 2.2: the left Gramian H_f(tau) = (1/24) sum over the 24 points of order 5
of Y_f Y_f^dagger, on main's frame code with the norms, in extended precision.  Data-free; no value is set beside a
measured number (the mixing's moduli are not printed; only invariance, unitarity, one invariant and one structural
entry are).
 G1  the Gramian's eigenvalue ratios and the moduli of the mixing between the up and down Gramians are the same at
     tau + 1; the mixing is unitary.
 G2  the invariant J = Im(V11 V22 conj(V12) conj(V21)) at tau0 = 0.13 + 1.70 i for the two pairings of readings.
 G3  at height 30 the heaviest-to-heaviest entry of that mixing is tiny for mixed readings and 1 for equal readings.
 G4  main's canonical end (B1927's canon) is held constant above its table's top height; the seat's own end goes on to
     its cusp limit pi + ln pi - 3 ln 2.  With main's end replaced by that limit at height 30, main's tiny entry
     becomes the seat's: the 2 percent between the two figures is that difference of the end and nothing else."""
import sys, pathlib, functools
from fractions import Fraction as Fr
import mpmath as mp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1957_the_seats_claims_register/verification/checks"))
import wb2_stage3_on_main as W
P5 = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]


def gram(tx, ty, ql, qr):
    H = {"S": mp.zeros(3, 3), "St": mp.zeros(3, 3)}
    for (a, b) in P5:
        Y = W.coupling(tx, ty, a, b, ql, qr, False, as_mp=True)
        for rd in H: H[rd] += Y[rd] * Y[rd].H / 24
    return H


def mixing(Hu, Hd):
    eu, Uu = mp.eigh(Hu); ed, Ud = mp.eigh(Hd); V = Uu.H * Ud          # eigenvalues ascending
    J = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])); un = mp.norm(V * V.H - mp.eye(3)); return eu, ed, V, J, un


if __name__ == "__main__":
    out = {}
    for tx in ("0.13", "1.13"):
        up, dn = gram(tx, 1.70, 1, -4), gram(tx, 1.70, 1, 2)
        for lab, (ru, rd) in (("W- (up S~, down S)", ("St", "S")), ("W+ (up S, down S~)", ("S", "St"))):
            out[(tx, lab)] = mixing(up[ru], dn[rd])
    for lab in ("W- (up S~, down S)", "W+ (up S, down S~)"):
        a, b = out[("0.13", lab)], out[("1.13", lab)]
        dr = max(abs(mp.log((a[k][i] / a[k][2]) / (b[k][i] / b[k][2]))) for k in (0, 1) for i in (0, 1)); dv = max(abs(abs(a[2][i, j]) - abs(b[2][i, j])) for i in range(3) for j in range(3))
        print("G1 %s: tau against tau + 1: the Gramians' eigenvalue ratios differ by %s in the logarithm, the mixing's moduli by %s; unitarity %s; J at tau %s, at tau + 1 %s" % (lab, mp.nstr(dr, 3), mp.nstr(dv, 3), mp.nstr(a[4], 3), mp.nstr(a[3], 6), mp.nstr(b[3], 6)))
    up, dn = gram("0.13", 30.0, 1, -4), gram("0.13", 30.0, 1, 2)
    for lab, (ru, rd) in (("mixed readings (up S~, down S)", ("St", "S")), ("equal readings (S, S)", ("S", "S")), ("equal readings (S~, S~)", ("St", "St"))):
        eu, ed, V, J, un = mixing(up[ru], dn[rd]); print("G3 height 30, %s: |V33| = %s (unitarity %s)" % (lab, mp.nstr(abs(V[2, 2]), 6), mp.nstr(un, 3)))

    CR = W.FM.CR; orig = CR.canon; lim = float(mp.pi + mp.log(mp.pi) - 3 * mp.log(2)); here = orig(complex(0.13, 30.0))
    print("G4 main's end at height 30: L_2 = %.10f (held constant above the table: %s); the cusp limit pi + ln pi - 3 ln 2 = %.10f" % (here["L_2"], here["_extrapolated"], lim))
    CR.canon = lambda z: {**orig(z), "L_2": lim}
    up, dn = gram("0.13", 30.0, 1, -4), gram("0.13", 30.0, 1, 2); eu, ed, V, J, un = mixing(up["St"], dn["S"]); CR.canon = orig
    print("G4 height 30, mixed readings, with the end at its cusp limit: |V33| = %s (the seat's sealed figure: 8.876e-21)" % mp.nstr(abs(V[2, 2]), 6))
