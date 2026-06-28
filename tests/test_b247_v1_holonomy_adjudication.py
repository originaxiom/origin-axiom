"""B247 locks -- the V1 adjudication: C_E6(SU(2)_long)=SU(6) dim35 / C_E6(SU(2)_short)=SU(3)xSU(2) dim11 (neither
is dim 13); the geometric holonomy has complex traces (not SU(2)); the SU(2) arc at x=0 is in Q(sqrt5) (golden),
distinct from the geometric Q(sqrt-3). FIREWALLED math; nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B247_v1_holonomy_adjudication" / "adjudication.py"
_spec = importlib.util.spec_from_file_location("b247", _PATH)
b247 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b247)


def test_branching_dims():
    # 78 = (8,1)+(8,7)+(1,14); 7 and 14 decompositions sum correctly
    assert 8 * 1 + 8 * 7 + 1 * 14 == 78
    assert sum(b247.a1_dim(a) * b247.a1_dim(b) for a, b in b247.SEVEN_A1A1) == 7
    assert sum(b247.a1_dim(a) * b247.a1_dim(b) for a, b in b247.FOURTEEN_A1A1) == 14


def test_centralizer_corrected():
    # long-root A1 (index 1) -> SU(6) dim 35; short (index 3) -> SU(3)xSU(2) dim 11
    assert b247.embedding_index(2) == 1 and b247.centralizer_dim(2) == 35
    assert b247.embedding_index(1) == 3 and b247.centralizer_dim(1) == 11
    # neither is the dim-13 SU(3)xSU(2)xU(1)^2 both handoffs claimed
    assert 13 not in (b247.centralizer_dim(1), b247.centralizer_dim(2))


def test1_geometric_holonomy_is_not_su2():
    # complex word-traces => not SU(2)-conjugable; the CORRECT rep (u=e^{2 i pi/3}) gives the Eisenstein
    # commutator trace [a,b] = (3-sqrt(-3))/2 = 1.5 - sqrt3/2 i  (matches SnapPy's discrete-faithful holonomy)
    tr = b247.test1_traces()
    assert all(abs(t.imag) > 1e-9 for t in tr.values())
    assert abs(tr["[a,b]"] - complex(1.5, -3 ** 0.5 / 2)) < 1e-9


def test_chat2_matrices_used_the_wrong_root():
    # verify-don't-trust catch: chat2's u=e^{i pi/3} is NOT a root of the figure-eight Riley poly u^2+u+1
    assert b247.chat2_matrices_are_invalid_rep()


def test_snappy_ground_truth_relator_discriminator():
    # clinching record: only u=e^{2i pi/3} satisfies the 2-bridge relator a w = w b (chat2's e^{i pi/3} fails);
    # SnapPy meridian-pair tr(ac)=2.5+0.866i => u=e^{+-2i pi/3}, real(tr(ab))=2.5 (chat2's would give 1.5)
    import cmath
    assert b247.satisfies_figure_eight_relator(cmath.exp(2j * cmath.pi / 3))
    assert not b247.satisfies_figure_eight_relator(cmath.exp(1j * cmath.pi / 3))
    assert abs(b247.SNAPPY_MERIDIAN_TR_AB.real - 2.5) < 1e-9
    assert abs(b247.test1_traces()["ab"].real - b247.SNAPPY_MERIDIAN_TR_AB.real) < 1e-9
    # the trap: tr[a,b]=u^2+2 = 1.5 +- 0.866i for BOTH roots (does NOT discriminate)
    for u in (cmath.exp(2j * cmath.pi / 3), cmath.exp(1j * cmath.pi / 3)):
        assert abs((u ** 2 + 2).real - 1.5) < 1e-9


def test2_su2_arc_is_golden_and_distinct_field():
    s5 = sp.sqrt(5)
    r0 = set(b247.riley_roots(sp.I))
    assert r0 == {sp.Rational(-5, 2) - s5 / 2, sp.Rational(-5, 2) + s5 / 2}     # Q(sqrt5), golden
    # geometric point x=2 is Q(sqrt-3) (complex), a different field
    rg = b247.riley_roots(1)
    assert all(complex(sp.N(r)).imag != 0 for r in rg)                          # complex => Q(sqrt-3)
    # the x=0 reps are SU(2): tr(ab) = -2-u real in [-2,2]
    for r in r0:
        tab = complex(-2 - r)
        assert abs(tab.imag) < 1e-9 and -2 <= tab.real <= 2
