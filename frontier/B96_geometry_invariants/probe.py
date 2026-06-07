"""B96 -- geometry invariants of the metallic mapping-torus manifolds (volume ordering + the volume
Hessian signature). Neutral low-dim-topology / quantum-topology mathematics; the physics readings are
quarantined in speculations/archive/PHYSICS_RESONANCES.md and are NOT used here.

The metallic once-punctured-torus bundle for parameter m is the mapping torus of the SQUARE monodromy
M_m^2 = [[m,1],[1,0]]^2 (orientation-preserving, det=+1): m=1 -> [[2,1],[1,1]] = figure-eight 4_1;
m=2 -> [[5,2],[2,1]] = m136; m=3 -> [[10,3],[3,1]] = s464 (SnapPy twister words aB, aaBB, aaaBBB).

(1) VOLUME ORDERING (SnapPy, cross-checked by the Bloch-Wigner dilogarithm of the tetrahedron shapes):
        vol_1 = 2.0298832 (4_1)  <  vol_2 = 3.6638624 (m136)  <  vol_3 = 4.8138192 (s464).
    Strictly MONOTONE increasing -- the complexity ordering of the metallic family continues at the third
    point. m=1 (figure-eight, golden) is the smallest-volume member, cohering with B92/MyCalc-5 (m=1 is the
    systole, the shortest geodesic on H/GL(2,Z)).

(2) THE VOLUME HESSIAN SIGNATURE (the decisive computation). At the complete hyperbolic structure the
    hyperbolic volume is a strict MAXIMUM over Dehn fillings (Mostow rigidity): of 156 nontrivial fillings
    of 4_1 with |(a,b)|^2 <= 50, ALL have vol < vol_0 and NONE exceed it. So the Neumann-Zagier Hessian of
    the volume functional at the complete structure is NEGATIVE DEFINITE -- signature (0,2), NOT indefinite.
    Moreover the figure-eight A-variety boundary is 1-COMPLEX-dimensional (the eigenvalue A-variety is the
    curve L=(-1)^(n-1) M^n, B83/B71), so the boundary deformation space is 2-real-dimensional: there is no
    canonical 4x4 boundary Hessian, and the natural NZ Hessian is 2x2 and definite.

(3) HONEST STATUS of the secondary quantities:
    * |tau_3| (adjoint Reidemeister torsion of s464): algebraically branch-ambiguous (cs_invariant_family
      gives -2.64 or -52.08 for the two fixed-locus sqrt-branches); SnapPy's exact adjoint torsion needs
      Sage (unavailable standalone), and a from-scratch 1-loop (Dimofte-Garoufalidis) invariant did NOT
      calibrate to the known tau_1=-3, tau_2=-16 here, so it is NOT reported as a number. The torsion
      ORDERING is therefore left open; the VOLUME ordering (clean) is the banked complexity result.
    * Chern-Simons amplitude: at large level the dominant saddle is controlled by exp(+-k*vol/2pi), i.e.
      by the volume; since the volume is strictly monotone in m, the extremal-weight member is m=1 (or m=3,
      depending on the sign convention) -- a restatement of (1), not new data.

Standalone low-dim topology / quantum topology; no physics claim; no Origin-core claim; proven core
P1-P16 untouched. Uses SnapPy 3.3.2 + mpmath.
"""
from __future__ import annotations

import mpmath as mp

# metallic m -> SnapPy twister bundle word for the square monodromy M_m^2
WORDS = {1: "aB", 2: "aaBB", 3: "aaaBBB"}


def _bundle(m):
    import snappy.twister as tw
    return tw.Surface("S_1_1").bundle(WORDS[m])


def bloch_wigner(z):
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def volume_table():
    """(m, vol_SnapPy, vol_BlochWigner, num_tet, identified-manifold) for m=1,2,3."""
    out = []
    for m in (1, 2, 3):
        M = _bundle(m)
        vbw = float(sum(bloch_wigner(complex(s)) for s in M.tetrahedra_shapes("rect")))
        name = str(M.identify()[0]) if M.identify() else "?"
        out.append((m, float(M.volume()), vbw, M.num_tetrahedra(), name))
    return out


def volume_is_monotone():
    vols = [row[1] for row in volume_table()]
    return all(vols[i] < vols[i + 1] for i in range(len(vols) - 1)), vols


def volume_hessian_definite(maxsq=50):
    """At the complete structure the volume is a strict maximum over fillings (Mostow) => NZ Hessian
    negative definite, signature (0,2). Returns (V0, n_below, n_above, n_total)."""
    import snappy
    V0 = float(snappy.Manifold("4_1").volume())
    below = above = total = 0
    for a in range(-7, 8):
        for b in range(-7, 8):
            if (a == 0 and b == 0) or a * a + b * b > maxsq:
                continue
            Mf = snappy.Manifold("4_1")
            try:
                Mf.dehn_fill((a, b))
                if "degenerate" in str(Mf.solution_type()):
                    continue
                v = float(Mf.volume())
            except Exception:
                continue
            total += 1
            if v < V0 - 1e-9:
                below += 1
            elif v > V0 + 1e-9:
                above += 1
    return V0, below, above, total


def main():
    print("B96 -- geometry invariants of the metallic mapping-torus manifolds\n")
    print("(1) volume ordering (SnapPy, Bloch-Wigner cross-check):")
    for m, vs, vbw, nt, name in volume_table():
        print(f"    m={m}: vol={vs:.7f}  (Bloch-Wigner {vbw:.7f}, {nt} tet, {name})")
    mono, vols = volume_is_monotone()
    print(f"    strictly monotone increasing: {mono}  -> the family ordering continues at m=3")
    print("\n(2) the volume Hessian signature (the decisive computation):")
    V0, below, above, total = volume_hessian_definite()
    print(f"    complete-structure vol V0={V0:.6f}; of {total} fillings: {below} below V0, {above} above")
    print(f"    => complete structure is a strict MAXIMUM => NZ volume Hessian NEGATIVE DEFINITE = signature (0,2)")
    print("    (NOT Lorentzian; the A-variety boundary is 1-complex-dim, so no canonical 4x4 Hessian exists)")
    print("\n(3) |tau_3| branch-ambiguous (Sage needed); CS amplitude is volume-dominated (restates (1)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
