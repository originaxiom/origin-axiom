"""Phase 1 -- locking test: the metallic-mean quasicrystals are genuinely DISTINCT real materials, even though the
trace-map algebra (the Sym two-sequence mu_d) is m-universal (B120). The gap-labeling module Z+Z*alpha_m lives in
Q(sqrt(m^2+4)) -- distinct fields {Q(sqrt5),Q(sqrt2),Q(sqrt13)} for m=1,2,3; gap labels confirmed on the lattice;
phi_m and the spectral box-dimension differ. 1D condensed matter, firewalled; NO new fundamental physics; nothing
to CLAIMS.md; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "metallic_spectra", _ROOT / "frontier" / "physics_probes" / "metallic_spectra.py")
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)


def test_gap_label_fields_distinct():
    fields = {m: M.gap_label_field(m)["squarefree"] for m in (1, 2, 3)}
    assert fields == {1: 5, 2: 2, 3: 13}        # Q(sqrt5), Q(sqrt2), Q(sqrt13) -- three distinct quadratic fields
    assert len(set(fields.values())) == 3


def test_gap_labels_on_lattice_each_m():
    for m in (1, 2, 3):
        g = M.gap_labels_fit(m)
        assert g["confirmed"] is True            # IDOS gap labels fall on Z + Z*alpha_m for every metallic mean


def test_phi_and_spectral_dimension_m_distinct():
    a = M.algebra_universal_physics_distinct()
    assert a["fields_all_distinct"] is True
    assert a["phi_m_all_distinct"] is True        # phi_1<phi_2<phi_3 distinct RG scales
    dims = a["spectral_box_dim"]
    assert dims[1] != dims[2] != dims[3]          # distinct spectral fractal dimension (finite-size, but separated)
    assert all(0.5 < d < 0.8 for d in dims.values())   # Cantor spectrum (dim < 1)


def test_metallic_phi_exact():
    import sympy as sp
    assert sp.simplify(M.metallic_phi(2) - (1 + sp.sqrt(2))) == 0     # silver mean = 1+sqrt2 (Q(sqrt2))
    assert sp.simplify(M.letter_frequency_a(1) - (sp.sqrt(5) - 1) / 2) == 0   # golden alpha = 1/phi
