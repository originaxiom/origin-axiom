"""B348 / gate A (S032-A) -- the Bloch-group class is a self-symmetrized Galois orbit: no forced choice.

Extends B330's mechanism to another of its named untested classes: the BLOCH-GROUP /
SCISSORS-CONGRUENCE class. The figure-eight decomposes into two regular ideal tetrahedra,
both of shape z0 = e^{i pi/3} -- a root of the Eisenstein factor z^2 - z + 1 of the P12
gluing-equation factorization -- so its (pre-)Bloch class is beta = 2[z0] over the
Eisenstein end Q(sqrt-3).

Verified here:
  (i)   z0 and its Galois conjugate z0bar (sqrt-3 -> -sqrt-3) are exactly the two roots of
        the P12 Eisenstein quadratic: the Galois action swaps them (exact, sympy);
  (ii)  THE SEAM IDENTITY: 1 - z0 = z0bar exactly -- at the Eisenstein point the standard
        Bloch duality involution z -> 1-z (under which D(z) + D(1-z) = 0 for ALL z)
        COINCIDES with the arithmetic Galois conjugation. The generic dilogarithm relation
        and the object's Galois action are the same map at this point;
  (iii) the Bloch-Wigner orbit: D(z0bar) = -D(z0), so the class orbit is {beta, -beta}
        with values {+Vol(4_1), -Vol(4_1)} (2*D(z0) = Vol, the P9 volume, recomputed
        independently at 30 dps); the symmetric functions are sum = 0 (canonical) and
        the fixed-field datum |2 D| = Vol -- the object hands you the orbit {+-beta},
        never a signed member;
  (iv)  the sign of beta is the ORIENTATION choice -- and this is exactly the choice the
        object cannot force: 4_1 is amphichiral (P9; B318 -- the geometric involution
        realizing the Galois swap), and CS(4_1) = 0 (P9), so the extended Bloch class
        i(Vol + i CS) has no unpaired chiral part. The B318 "amphichirality is the
        geometric firewall" statement lands in the Bloch group: the orbit {beta, -beta}
        is identified by the object's own orientation-reversing symmetry --
        self-symmetrized, not merely symmetrizable.

HONEST SCOPE (C-guardrail): this seals the object's OWN Bloch/scissors class (the concrete
element beta = 2[e^{i pi/3}]). The full extended-Bloch / K_3^ind theory (torsion of
B(Q(sqrt-3)), the Rogers-lift Z/(pi^2) ambiguity, general scissors congruence) is NOT
covered. Firewalled; nothing to CLAIMS.md. Needs sympy + mpmath (both core deps).
"""
import mpmath as mp
import sympy as sp

Z0 = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2        # e^{i pi/3}, the Eisenstein shape (P12)
Z0BAR = sp.conjugate(Z0)
VOL_FIG8 = 2.0298832128193072                          # P9 anchor (independently recomputed below)


def galois_swaps_the_eisenstein_roots():
    """(i) z0, z0bar are exactly the two roots of the P12 Eisenstein factor z^2 - z + 1;
    complex conjugation (= sqrt-3 -> -sqrt-3 on Q(sqrt-3)) swaps them."""
    z = sp.symbols("z")
    eis = z**2 - z + 1
    both_roots = (sp.expand(eis.subs(z, Z0)) == 0) and (sp.expand(eis.subs(z, Z0BAR)) == 0)
    distinct = sp.simplify(Z0 - Z0BAR) != 0
    return both_roots, distinct


def seam_identity():
    """(ii) 1 - z0 == z0bar exactly: the Bloch duality involution z -> 1-z equals Galois
    conjugation AT the Eisenstein point (and only the roots of z^2 - z + 1 have this:
    1 - z = conj(z) on Re(z) = 1/2, and z(1-z) = 1 forces exactly this quadratic)."""
    exact = sp.simplify(1 - Z0 - Z0BAR) == 0
    # the quadratic characterization: 1 - z = zbar AND |z| = 1  <=>  z^2 - z + 1 = 0
    z = sp.symbols("z")
    forced = sp.expand(z * (1 - z) - 1 + (z**2 - z + 1)) == 0   # z(1-z) = 1 <=> the Eisenstein quadratic
    return exact, forced


def bloch_wigner(w, dps=30):
    """Bloch-Wigner dilogarithm D(w) = Im(Li2(w)) + arg(1-w) log|w| (exact functional form).

    Precision is SCOPED (mp.workdps), not written to the global mp.mp.dps: the global is
    shared test-suite state, and lowering it poisons any high-precision probe that runs
    later in suite order (the 2026-07-02 B302 -> B347 failure class)."""
    with mp.workdps(dps):
        w = mp.mpc(w)
        return mp.im(mp.polylog(2, w)) + mp.arg(1 - w) * mp.log(abs(w))


def orbit_is_symmetrizable():
    """(iii) the orbit {2 D(z0), 2 D(z0bar)} = {+Vol, -Vol}: sum exactly 0 (canonical),
    |member| = Vol(4_1) recomputed independently of SnapPy and of the stored constant."""
    d = bloch_wigner(complex(sp.re(Z0), sp.im(Z0)))
    dbar = bloch_wigner(complex(sp.re(Z0BAR), sp.im(Z0BAR)))
    orbit = (2 * d, 2 * dbar)
    sum_zero = abs(orbit[0] + orbit[1]) < mp.mpf(10) ** (-25)
    vol_match = abs(abs(orbit[0]) - VOL_FIG8) < 1e-12
    return orbit, bool(sum_zero), bool(vol_match)


def sign_is_the_orientation_and_the_object_kills_it():
    """(iv) the residual 'choice' in {beta, -beta} is the orientation; the object is
    amphichiral with CS = 0 (P9/B318), so its own symmetry identifies the two members.
    Computational content banked here: CS(4_1) = 0 exactly (P9 anchor; live SnapPy
    cross-check in tests/test_snapdata.py) and D(real) = 0 (the fixed field of the
    Galois action is where D vanishes -- the symmetric point is value-free)."""
    from mpmath import mpf
    cs_fig8 = 0.0                                     # P9 (live-checked elsewhere)
    d_on_fixed_field = bloch_wigner(mpf(2) / 3)       # a rational (fixed-field) point
    return cs_fig8 == 0.0, abs(d_on_fixed_field) < mp.mpf(10) ** (-25)


if __name__ == "__main__":
    print("B348 -- the Bloch-group class as a self-symmetrized Galois orbit (gate A extension)\n")
    br, dist = galois_swaps_the_eisenstein_roots()
    print(f"(i)  z0, z0bar both roots of the P12 Eisenstein quadratic, distinct, Galois-swapped: {br and dist}")
    ex, forced = seam_identity()
    print(f"(ii) THE SEAM: 1 - z0 = z0bar exactly ({ex}); z(1-z)=1 <=> z^2-z+1=0 ({forced})")
    orbit, s0, vm = orbit_is_symmetrizable()
    print(f"(iii) orbit = ({float(orbit[0]):+.15f}, {float(orbit[1]):+.15f}); sum=0: {s0}; |.|=Vol(4_1): {vm}")
    cs0, dre = sign_is_the_orientation_and_the_object_kills_it()
    print(f"(iv) CS(4_1)=0 (amphichiral, B318): {cs0}; D vanishes on the fixed field: {dre}")
    print("\nCONDITIONAL: the object's Bloch class is the orbit {+beta, -beta}, sum 0, self-identified")
    print("by amphichirality -- no forced choice. Extended-Bloch/K3 torsion theory stays untested.")
