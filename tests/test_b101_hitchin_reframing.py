"""B101 -- locking tests for the Hitchin-component reframing of V0.

R1  V0 = Fuchsian locus: the Anosov hallmark (loxodromic + unipotent cusp + complex elliptic control) and
    the unique SO(2,1) invariant form, signature (2,1).
R2  the symmetric-space ladder: Lorentzian only at k=2 (SO(2,1)); split-form pattern (Sp odd / SO even) ->
    the spacetime-tower KILL.
R3  sl(3) = V2 (+) V4 under the principal sl(2): weights {+-4,+-2,+-2,0,0}; dims 3,5; degrees 2 (quad), 3
    (cubic); V0 = {cubic = 0}.
R4  the cubic deformation off V0: H^1 splits 8 = 3 (+) 5; the finite witness stays Anosov, leaves V0, and
    breaks the SO(2,1) form, at >= 2 Fuchsian seeds x 2 cubic directions.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b101", _ROOT / "frontier" / "B101_hitchin_reframing" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- R1 -----------------------------------------------------------------
def test_v0_anosov_hallmark():
    h = B.v0_anosov_hallmark()
    assert h["all_loxodromic"] is True            # every non-peripheral word loxodromic (3 distinct pos reals)
    assert h["cusp_unipotent"] is True            # the cusp [a,b] is unipotent
    assert h["elliptic_control_complex"] is True  # an elliptic generator -> complex spectrum (off V0)


def test_v0_so21_certificate():
    nd, sig, inv = B.v0_so21_certificate()
    assert nd == 1                                # the invariant symmetric form is UNIQUE
    assert sig == (2, 1)                          # signature (2,1) -> SO(2,1)
    assert inv < 1e-10                            # exact invariance to machine precision


# --- R2 -----------------------------------------------------------------
def test_ladder_lorentzian_only_at_k2():
    assert B.lorentzian_rungs(8) == [2]           # Lorentzian (one timelike) ONLY at k=2 -> no spacetime tower


def test_ladder_split_form_pattern():
    """Sp(k+1,R) for odd k, SO(p,p+-1) for even k -- the principal sl(2) in the SPLIT real forms."""
    table = {k: (kind, sig) for (k, kind, amb, sig, lor) in B.ladder_signatures(8)}
    for k in (1, 3, 5, 7):
        assert table[k][0] == "symplectic"
    for k, expect in {2: (2, 1), 4: (3, 2), 6: (4, 3), 8: (5, 4)}.items():
        assert table[k] == ("symmetric", expect)  # SO(2,1),SO(3,2),SO(4,3),SO(5,4): balanced split, not Lorentzian for k>2


# --- R3 -----------------------------------------------------------------
def test_principal_sl3_branching_cubic_structure():
    weights, degree = B.principal_sl3_branching()
    assert weights == [-4, -2, -2, 0, 0, 2, 2, 4]  # sl(3) = V2 (+) V4 under the principal sl(2)
    assert degree == {3: 2, 5: 3}                  # dim-3 block = quadratic (deg 2); dim-5 = CUBIC (deg 3)


# --- R4 -----------------------------------------------------------------
def test_tangent_space_split_cubic_transverse():
    """H^1(F_2, sl(3)_Ad) = 8 = 3 (V2/Teichmuller, tangent V0) (+) 5 (V4/cubic, transverse), at >=2 seeds."""
    for seed in B.SEEDS:
        h1, v2, v4 = B.tangent_space_split(seed)
        assert (h1, v2, v4) == (8, 3, 5)


def test_cubic_deformation_witness_leaves_v0_stays_anosov():
    """The finite cubic deformation stays Anosov, leaves V0 (x1!=x4), and breaks the SO(2,1) form, at every
    (seed x direction)."""
    results = B.cubic_deformation_witness(t=0.05)
    assert len(results) == 4                        # 2 Fuchsian seeds x 2 cubic directions
    for r in results:
        assert r["off_V0"] > 1e-3                   # genuinely off the Sym^2 / V0 locus
        assert r["anosov"] is True                  # Anosov is open -> small cubic deformation preserves it
        assert r["so21_nulldim"] == 0               # no invariant symmetric form survives (left SO(2,1))
