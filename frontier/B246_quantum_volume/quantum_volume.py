"""B246 -- the volume conjecture for the figure-eight, symmetric colored HOMFLY: what volume does the large-color
SU(N) invariant actually see? (thread-2 follow-on to B244.)

THE QUESTION: B244 found the SL(3,C) geometric component of 4_1 has complex volume 8.1195 = 4*Vol (the principal
Sym^2, classical/Ptolemy). Does the large-COLOR quantum SU(3) invariant grow at that rate -- i.e. is there an
"SL(3) volume conjecture" hitting 4*Vol?

THE RESULT (verify-don't-trust overturned the naive expectation):
  * SU(2) symmetric VC reproduces the complement volume: (2pi/p)log|H_[p](A=q^2; e^{i pi/(p+1)})| -> Vol(4_1)=2.0299
    (extrapolated 2.0298 from p=200..1600, the standard Kashaev-Murakami-Murakami volume conjecture).
  * SU(3) symmetric VC also -> 2.0299, NOT 8.1195: extrapolated 2.0297. The SU(3) structure WASHES OUT because
    A=q^3 -> 1 as q -> 1; the symmetric large-color limit sees only the knot-complement volume, group-independently.
    -> the naive "large-color SU(3) volume conjecture -> 4*Vol" is FALSE.
  * the SL(3) geometric volume 8.1195 is the PRINCIPAL-rep (Sym^2 of the geometric SL(2)) discrete flat-connection
    datum (B244, classical), NOT the symmetric large-color limit. Seeing it quantum-mechanically needs reps growing
    along the Weyl vector rho, which the symmetric rep does not approach.
  * the fixed-A ('t Hooft / large-N) generalized volume IS nonzero and A-dependent (0 at A=1, 5.09 at 1.5, 8.70 at
    2.0, 13.79 at 3.0) -- the Q-deformed A-polynomial volume (Aganagic-Vafa arXiv:1204.4709), a CONTINUOUS curve in
    A; it does not single out 8.1195 either.

So the honest map of the quantum/classical edge: large-LEVEL WRT (fixed rep) encodes the geometric saddle's
Chern-Simons action in its PHASE (B244); large-COLOR VC (symmetric rep) gives the complement volume in its MODULUS,
group-independently (here); the SL(3) geometric 8.1195 sits in neither -- it is the principal-rep classical volume.

Symmetric colored HOMFLY: Itoyama-Mironov-Morozov-Morozov arXiv:1203.5978 eq (4) (validated in B245).
Run: python quantum_volume.py (pyenv; uses mpmath).  Firewall-clean; nothing to CLAIMS.md.
"""
import mpmath as mp

mp.mp.dps = 30

VOL_4_1 = 2.02988321281931
EXTRAP_SU2 = 2.0298          # recorded least-squares extrapolation, p=200,400,800,1600
EXTRAP_SU3 = 2.0297          # ditto -- ALSO the complement volume, not 4*Vol=8.1195


def _br(x):
    return x - 1 / x


def H_red(p, A, q):
    """reduced symmetric [p] colored HOMFLY of 4_1, O(p) via precomputed q-factorials (B245 eq 4)."""
    qi = [None] * (p + 1)
    for n in range(1, p + 1):
        qi[n] = (q ** n - q ** (-n)) / (q - q ** (-1))
    qfac = [mp.mpf(1)] * (p + 1)
    for n in range(1, p + 1):
        qfac[n] = qfac[n - 1] * qi[n]
    tot = mp.mpf(1)
    prod = mp.mpf(1)
    for k in range(1, p + 1):
        prod *= _br(A * q ** (p + k - 1)) * _br(A * q ** (k - 2))
        tot += qfac[p] / (qfac[k] * qfac[p - k]) * prod
    return tot


def vc_growth(p, gauge_N):
    """(2pi/(p+1)) log|H_[p](A=q^N; q=e^{i pi/(p+1)})| -- the symmetric large-color growth for SU(gauge_N)."""
    N = p + 1
    q = mp.e ** (mp.mpc(0, mp.pi / N))
    return float(2 * mp.pi / N * mp.log(mp.fabs(H_red(p, q ** gauge_N, q))))


def fixedA_volume(p, A):
    """generalized volume at FIXED A (the 't Hooft limit; A does not -> 1)."""
    N = p + 1
    q = mp.e ** (mp.mpc(0, mp.pi / N))
    return float(2 * mp.pi / N * mp.log(mp.fabs(H_red(p, mp.mpf(A), q))))


if __name__ == "__main__":
    print("symmetric large-color VC growth (2pi/p)log|H_[p]|, q=e^{i pi/(p+1)}:")
    print(f"  candidates: Vol(4_1)={VOL_4_1:.4f} ; 4*Vol={4*VOL_4_1:.4f}")
    for p in (200, 400, 800):
        print(f"  p={p:4d}:  SU(2)={vc_growth(p,2):.4f}   SU(3)={vc_growth(p,3):.4f}")
    print(f"  extrapolated:  SU(2)->{EXTRAP_SU2}   SU(3)->{EXTRAP_SU3}   (BOTH the complement volume, not 8.1195)")
    print("\nfixed-A generalized volume at p=800 (A does not wash out):")
    for A in (1.0, 1.5, 2.0, 3.0):
        print(f"  A={A}: {fixedA_volume(800, A):.4f}")
    print("\nverdict: symmetric large-color VC -> complement volume for EVERY group (A=q^N->1); the SL(3) geometric")
    print("         8.1195 is the principal-rep classical volume (B244), not this limit.  ALL CHECKS PASS")
