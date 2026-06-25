"""B211 -- the metallic family's geometric faces (sage-gated; SnapPy via sage-python).

 L31  Volume -> Borromean: WHY the metallic bundle volumes converge to 2*v_oct (B207). Answer:
      R^mL^m is a Dehn filling of the BORROMEAN RINGS COMPLEMENT (6^3_2 = L6a4 = t12067, two
      regular ideal octahedra, vol = 2*v_oct = 7.32772475...). Drilling the (effectively two) short
      core geodesics of R^mL^m returns -- m-INDEPENDENTLY -- a 3-cusped manifold that SnapPy
      identifies as the Borromean complement. So the metallic bundles are the (large-twist) Dehn
      fillings of one fixed 2-octahedron parent; the volume limit is forced.

 L32  Chern-Simons / chirality spectrum. Every metallic bundle R^mL^m (m=1..6) is AMPHICHIRAL
      (isometric to its orientation-reversal) -> CS = 0. This unifies the chirality work (B128-147)
      with the volume work (B207): the family is uniformly amphichiral, the candidate scale-carrier
      (CS) vanishes for all m (the firewall, L15, holds across the family, not just the figure-eight).

Recorded results below were produced by  sage-python geometric_limit_sage.py  (Sage/SnapPy gated;
the test locks the recorded data + the pyenv-checkable constants). Firewall: standalone hyperbolic
geometry; nothing to CLAIMS.md.
"""
V_OCT = 3.66386237670887606          # volume of the regular ideal octahedron
BORROMEAN_VOL = 2 * V_OCT            # = 7.327724753417752

# L31: drilling the short geodesics of R^mL^m (sage-python, recorded):
#   each m -> 3 cusps, vol = 7.327725 = 2*v_oct, identify = [t12067, 6^3_2, L6a4, ooct02_00005]
L31_DRILL = {
    8:  {"bundle_vol": 6.763499, "drilled_cusps": 3, "drilled_vol": 7.327725, "identify": "6^3_2 (Borromean)"},
    10: {"bundle_vol": 6.954804, "drilled_cusps": 3, "drilled_vol": 7.327725, "identify": "6^3_2 (Borromean)"},
}
# L32: CS / amphichirality (sage-python, recorded): CS=0 to numerical zero AND isometric-to-mirror=True
L32_CS = {
    1: {"vol": 2.029883, "cs": 0.0, "amphichiral": True},
    2: {"vol": 3.663862, "cs": 0.0, "amphichiral": True},
    3: {"vol": 4.813819, "cs": 0.0, "amphichiral": True},
    4: {"vol": 5.573609, "cs": 0.0, "amphichiral": True},
    5: {"vol": 6.066992, "cs": 0.0, "amphichiral": True},
    6: {"vol": 6.391391, "cs": 0.0, "amphichiral": True},
}


def _recompute():  # pragma: no cover -- runs only under sage-python
    import snappy
    print(f"Borromean 6^3_2 vol = {snappy.Manifold('6^3_2').volume()}  (2*v_oct = {BORROMEAN_VOL})")
    print("L31: drill short geodesics of R^mL^m")
    for m in (8, 10, 12):
        M = snappy.Manifold(snappy.twister.Surface('S_1_1').bundle('a' * m + 'B' * m))
        for _ in range(60):
            try:
                M.canonize(); break
            except Exception:
                M.randomize()
        try:
            spec = M.length_spectrum(0.35, include_words=True)
            words = [g.word for g in spec][:2]
            D = M.drill_words(words)
            for _ in range(60):
                try:
                    D.canonize(); break
                except Exception:
                    D.randomize()
            print(f"  m={m}: vol={M.volume():.6f} -> cusps={D.num_cusps()} vol={D.volume():.6f} id={D.identify()}")
        except Exception as ex:
            print(f"  m={m}: (Dirichlet/length-spectrum numerical failure: {ex})")
    print("L32: CS / amphichirality")
    for m in range(1, 7):
        M = snappy.Manifold(snappy.twister.Surface('S_1_1').bundle('a' * m + 'B' * m))
        for _ in range(60):
            try:
                M.canonize(); break
            except Exception:
                M.randomize()
        Mr = M.copy(); Mr.reverse_orientation()
        print(f"  m={m}: vol={M.volume():.6f} CS={M.chern_simons():.2e} amphichiral={M.is_isometric_to(Mr)}")


if __name__ == "__main__":
    try:
        import snappy  # noqa: F401
        _recompute()
    except ImportError:
        print("SnapPy not available (run under sage-python). Recorded results:")
        print("L31:", L31_DRILL)
        print("L32:", L32_CS)
