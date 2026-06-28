"""B265 locks -- integrability + Zariski-density: genuine E6-irreducible flat connections on the figure-eight exist.
Density (sage): principal sl(2) + exp-{4,8} generates e6 (78); + exp-{5,7,11} stays in f4 (52). Integrability:
dim H^2(Sym^{2k})=1 (=H^1, chi=0); geometric rep smooth. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B265_e6_integrability" / "e6_integrability.py"
_spec = importlib.util.spec_from_file_location("b265", _PATH)
b265 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b265)


def test_density_split_e6_vs_f4():
    # the 6-dim tangent space splits by F4/E6: {4,8} are E6-dense, {5,7,11} trapped in F4
    assert b265.zariski_dense_exponents() == [4, 8]
    assert b265.trapped_exponents() == [5, 7, 11]
    assert sorted(set(b265.E6_EXPONENTS) - set(b265.F4_EXPONENTS)) == [4, 8]


def test_generation_dims():
    # principal sl(2)+exp generates: e6 (78) for {4,8}; f4 (52) for {5,7,11}; sl(2) (3) for the principal curve
    assert b265.GENERATION_DIM[4] == b265.GENERATION_DIM[8] == b265.DIM_E6 == 78
    assert b265.GENERATION_DIM[5] == b265.GENERATION_DIM[7] == b265.GENERATION_DIM[11] == b265.DIM_F4 == 52
    assert b265.GENERATION_DIM[1] == 3


def test_obstruction_space_dim():
    # dim H^2(Sym^{2k}) = 1 for all k (= H^1, chi=0); obstruction space = 6, but geometric rep is smooth
    for k in range(1, 12):
        assert b265.H2_sym(k) == 1
    assert b265.obstruction_dim() == 6
