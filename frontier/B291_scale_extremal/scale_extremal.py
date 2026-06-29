"""B291 -- is any closing SCALE-DISTINGUISHED? Run with sage-python (SnapPy + Regina). Phase III (wall #5, scale).

B290 showed the seam generates a scale ladder but does not identify filling<->level. New question: independently of
n=k, is there a closing that is SCALE-EXTREMAL (minimal volume / shortest geodesic / systolic extremum), and does it
coincide with the dynamical (B287, the fiber/Sol closing) or arithmetic (B288) distinguished closing?

  1. MIN-VOLUME closing EXISTS and is stable: m004(+-5,1) = m003(-2,3), vol = 0.98136883 (the figure-eight's smallest
     hyperbolic filling; NOT the Weeks manifold 0.94271). Two methods agree (volume() = Re(complex_volume)); the
     min-volume slope is invariant across randomized triangulations.
  2. SYSTOLE gives NO finite distinguished closing: the shortest geodesic ~ |core| ~ 2*pi/n -> 0 as the slope grows,
     so the systolic infimum over all fillings is 0 (not attained).
  3. AXIS-STRATIFIED. The min-volume closing m004(5,1) is NON-arithmetic (trace field x^4-x-1, B288) and is NOT the
     fiber/Sol closing (B287's (0,1) is non-hyperbolic, vol 0). So the SCALE-extremal axis selects a DIFFERENT closing
     than the DYNAMICAL (A=LR) and ARITHMETIC (Q(sqrt-3)) axes -- 'selective along WHICH axis'.

FIREWALL: pure geometry. A clean extremum exists; it does NOT pick a unique distinguished world (different axes ->
different closings). 'min-volume = our universe' is a [HOOK]. Nothing to CLAIMS.
"""
import snappy
import regina
from math import pi, gcd


def volume_landscape(pmax=8, qmax=8):
    vols = []
    for p in range(-pmax, pmax + 1):
        for q in range(1, qmax + 1):
            if gcd(abs(p), q) != 1:
                continue
            M = snappy.Manifold('m004'); M.dehn_fill((p, q))
            if 'positively' not in M.solution_type():
                continue
            vols.append((float(M.volume()), p, q))
    return sorted(vols)


def min_volume_slope_stable(trials=5):
    """re-randomize the triangulation; confirm the min-volume slope is stable."""
    out = []
    for _ in range(trials):
        vols = []
        for p in range(-8, 9):
            for q in range(1, 9):
                if gcd(abs(p), q) != 1:
                    continue
                N = snappy.Manifold('m004'); N.randomize(); N.dehn_fill((p, q))
                if 'positively' not in N.solution_type():
                    continue
                vols.append((round(float(N.volume()), 6), abs(p), q))   # abs(p): (5,1)/(-5,1) mirror, same vol
        out.append(min(vols)[1:])
    return out


def volume_two_ways(p, q):
    M = snappy.Manifold('m004'); _ = float(M.chern_simons()); M.dehn_fill((p, q))
    return float(M.volume()), complex(M.complex_volume()).real


if __name__ == "__main__":
    vols = volume_landscape()
    print("smallest-volume hyperbolic fillings of m004:")
    for v, p, q in vols[:4]:
        print(f"  ({p},{q}): vol={v:.8f}")
    v, p, q = vols[0]
    M = snappy.Manifold('m004'); M.dehn_fill((p, q))
    print(f"\nMIN-VOLUME closing ({p},{q}) = {M.identify()}  vol={v:.8f}  (Weeks=0.94271, so NOT Weeks)")
    v1, v2 = volume_two_ways(5, 1)
    print(f"two methods: volume()={v1:.9f}  Re(complex_volume)={v2:.9f}  match={abs(v1-v2)<1e-7}")
    print("min-volume slope across randomized triangulations:", min_volume_slope_stable())
    print("\nsystole |core| -> 0 with slope (no finite systole-distinguished closing):")
    for n in (5, 20, 100):
        N = snappy.Manifold('m004'); N.dehn_fill((1, n))
        print(f"   (1,{n}): |core|={abs(complex(N.cusp_info(0)['core_length'])):.6f}")
    print("\nVERDICT: a scale extremum EXISTS (min-vol m004(5,1)=m003(-2,3)) but is NON-arithmetic (B288) and not the")
    print("fiber closing (B287) -- selection is axis-stratified; the scale axis picks yet another closing. Firewalled.")
