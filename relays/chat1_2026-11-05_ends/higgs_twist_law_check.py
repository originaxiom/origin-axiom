"""The web seat, 2026-11-05: THE HIGGS-TWIST LAW (cc's ask 3, P-687), the numerical checks of the proof's three lemmas.
Data-free: frame functions only; no mass, ratio, chi2 or data; no line on the family's slope (2/5, 3/5).

The law (B1839's design): the exact twisted norms of K_{X,s} = P_{X,s}/R_{X,s} over the cell minus a horoball depend on the
line and the sector only through the Higgs twist +-3w mod the lattice. The proof (the relay) rests on three lemmas:
  L1 (uniqueness): a residue-1 meromorphic section with one simple pole at 0 and a given non-trivial character is unique,
     so K_{X,s} depends only on its character, chi((qL + qR)_X w) K_s (T-KERNEL-SUM-TWIST);
  L2 (inversion): the inverse character's kernel is z -> -K(-z), so |K_{chi^-1}(z)| = |K_chi(-z)|;
  L3 (the region's symmetry): the cell is centrally symmetric and the horoball {log 1/|z| - Re g(z) > L} is invariant
     under z -> -z, because the Frobenius series of y'' + (wp/4 + c) y = 0 has only even powers (wp is even), so g is even.
Checked here:
  (a) L3: B1667's frobenius coefficients at odd orders, and g(-z) - g(z) at sample points, at five of B1667's points;
  (b) L1 and L2 pointwise on census lines with chi(6w) != 1 at two tau: K_lep,s(z) = K_down,s(z) (same summed twist +3w);
      K_up,s(z) = -K_down,s(-z) (summed twist -3w);
  (c) the line class pointwise: K_down,s on the lines (a + 1/3, b) and (a, b + 1/3), whose 3w differs by a lattice vector,
      against the line (a, b); and on (-a, -b) (3w -> -3w) against -K_down,s(-z) of (a, b).

    python3 higgs_twist_law_check.py <main checkout>     (main at 88c577896 for the frame module; B1667 from the same tree)
"""
import contextlib
import importlib.util
import io
import json
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
DENS = HERE.parent / "chat1_2026-11-04_density" / "density_higgs_check.py"
src = DENS.read_text().split('if __name__ == "__main__":')[0]
exec(compile(src, str(DENS), "exec"))

SRC = ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py"
_spec = importlib.util.spec_from_file_location("b1667", SRC)
C = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(C)
PTS = json.loads((SRC.parent / "the_canonical_cusp.json").read_text())["points"]
ZS = np.array([0.11 + 0.07j, -0.19 + 0.13j, 0.07 - 0.21j, 0.23 + 0.31j, -0.29 - 0.17j, 0.37 + 0.05j])
TAUS = (complex(0.2, 2.5), complex(0.45, 3.1))


def kern(a, b, tau, ql, qr, z):
    x, y = twists(a, b, tau, ql, qr)
    with contextlib.redirect_stdout(io.StringIO()):
        R = B.residues(x, y, tau)
    P = B.pairs(x, y, z, tau)
    return {s: (P[s] / R[s] if abs(R[s]) > CUT else None) for s in CH}


def rel(A, Bv):
    return float(np.max(np.abs(A - Bv)) / np.max(np.abs(Bv)))


if __name__ == "__main__":
    print("(a) L3, the evenness of the Frobenius series (five of B1667's points)")
    for p in PTS[::13][:5]:
        tau = complex(*p["tau"]); c = complex(*p["c"])
        with contextlib.redirect_stdout(io.StringIO()):
            lat, z0, Aa, Ab = C.monodromy(tau, c)
            al, be = C.frobenius(lat, c)
        odd = float(max(np.max(np.abs(al[1::2])), np.max(np.abs(be[1::2]))))
        ev = float(max(abs(C.g_local(al, be, -z) - C.g_local(al, be, z)) for z in ZS))
        print("    tau %s: largest odd-order coefficient %.1e; largest |g(-z) - g(z)| at the samples %.1e" % (tau, odd, ev))

    census = own_lines(range(1, 13))
    gen = [l for l in census if l[0] % 1 not in FAMILY and not ((6 * l[0]).denominator == 1 and (6 * l[1]).denominator == 1)]
    lines = [l for l in gen[7::19] if all((x % 1) not in FAMILY for x in (Fr(l[0]) + Fr(1, 3), -Fr(l[0])))][:12]
    wl, wu, wc, wn, n = 0.0, 0.0, 0.0, 0.0, 0
    for tau in TAUS:
        for (a, b) in lines:
            guard(a)
            Kd = kern(a, b, tau, 1, 2, ZS); Kdm = kern(a, b, tau, 1, 2, -ZS)
            Kl = kern(a, b, tau, -3, 6, ZS); Ku = kern(a, b, tau, 1, -4, ZS)
            shifted = [kern(Fr(a) + Fr(1, 3), b, tau, 1, 2, ZS), kern(a, Fr(b) + Fr(1, 3), tau, 1, 2, ZS)]
            neg = kern((-Fr(a)) % 1, (-Fr(b)) % 1, tau, 1, 2, ZS)
            for s in CH:
                if Kd[s] is None:
                    continue
                n += 1
                if Kl[s] is not None:
                    wl = max(wl, rel(Kl[s], Kd[s]))
                if Ku[s] is not None:
                    wu = max(wu, rel(Ku[s], -Kdm[s]))
                for S in shifted:
                    if S[s] is not None:
                        wc = max(wc, rel(S[s], Kd[s]))
                if neg[s] is not None:
                    wn = max(wn, rel(neg[s], -Kdm[s]))
    print("(b), (c) on %d census lines with chi(6w) != 1 x %d tau, %d live channel-points, %d sample points each:" % (len(lines), len(TAUS), n, len(ZS)))
    print("    L1, leptons against down (summed twist +3w both): largest relative difference %.1e" % wl)
    print("    L2, up against -K_down(-z) (summed twist -3w): largest relative difference %.1e" % wu)
    print("    the class: (a + 1/3, b) and (a, b + 1/3) against (a, b): largest relative difference %.1e" % wc)
    print("    the sign: (-a, -b) against -K_down(-z) of (a, b): largest relative difference %.1e" % wn)
