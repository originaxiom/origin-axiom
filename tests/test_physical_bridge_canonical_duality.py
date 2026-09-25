"""R48 two-sided finite controls; global analytic premises remain external."""
from pathlib import Path
import importlib.util

import sympy as s

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/canonical_duality.py'
spec = importlib.util.spec_from_file_location('r48_duality',path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_presented_group_automorphism_and_literal_peripheral_word():
    r = v.v.RELATOR
    assert v.reduce_word(r.swapcase()) == v.reduce_word('N'+v.inverse_word(r)+'n')
    assert v.v.LONGITUDE.swapcase() == v.inverse_word(v.v.LONGITUDE)
    for word in (r,v.v.LONGITUDE,'mnMnnMN'):
        assert word.swapcase().swapcase() == word
        assert v.reduce_word(word+v.inverse_word(word)) == ''
    assert v.reduce_word('mnMN') != ''


def test_literal_pairing_all_central_twists_and_noncommuting_words():
    assert all(v.representation_checks().values())


def test_conormal_frame_pairings_positive_metric_and_orientation():
    f,dual,h,hd,signs = v.conormal_frames()
    assert f.T*dual == signs
    assert hd == h.inv()
    assert all(h[:j,:j].det() > 0 and hd[:j,:j].det() > 0 for j in range(1,5))
    assert f.det() == 1 and dual.det() == -1
    # Without the tangent minus signs, it is not the conormal differential.
    wrong = f.inv().T
    assert f.T*wrong != signs


def test_metric_compatibility_of_the_actual_fiber_map_is_a_pullback():
    _,_,h,_,_ = v.conormal_frames()
    b = v.v.pairing_witness().subs(v.q,2)
    pulled = b.T*h.inv()*b
    assert all(pulled[:j,:j].det() > 0 for j in range(1,5))
    assert v.zeros(b.inv().T*pulled*b.inv()-h.inv())
    assert not v.zeros(b.T*h*b-pulled)
    # This pointwise identity does NOT prove existence of the global base map.


def test_nonselfdual_domain_rejects_algebraic_shortcut():
    inside,outside = v.ellipse_countercontrol()
    assert inside == s.Rational(9,25)
    assert outside == -s.Rational(231,25)
    ident = s.eye(4)
    witness = s.diag(1,-1,-1,-1)
    assert ident.inv().T*witness == witness*ident


def test_product_conormal_and_radial_coordinate():
    normal,expected,rad,coords = v.product_conormal()
    assert v.zeros(8*rad*normal/3-expected)
    x0,z,y = coords
    image = s.Matrix([x0,2*rad/(3*z),-y])
    assert s.cancel(image[0]-image[2]**2/2-rad) == 0
    twice = image.subs(dict(zip(coords,image)),simultaneous=True)
    assert v.zeros(twice-s.Matrix(coords))


def test_leading_cusp_isometry_needs_longitudinal_shear():
    h,j = v.leading_metric(),v.shear_jacobian()
    assert v.zeros(j.T*h*j-h)
    assert j*j == s.eye(3) and j.det() == 1
    assert not v.zeros(v.shear_jacobian(False).T*h*v.shear_jacobian(False)-h)
    assert s.factor(h.det()-27*v.k**2/(128*v.R)) == 0
    assert all(h.subs({v.k:2,v.R:3})[:i,:i].det() > 0 for i in range(1,4))


def test_full_coordinate_shear_is_involutive_not_only_its_derivative():
    r,x,t,c = s.symbols('r x t c',real=True)
    coordinates = (r,x,t)
    phi = s.Matrix([r,-x,-t-r/(4*v.k)-c])
    twice = phi.subs(dict(zip(coordinates,phi)),simultaneous=True)
    assert v.zeros(twice-s.Matrix(coordinates))
    assert phi.jacobian(coordinates) == v.shear_jacobian()


def test_exterior_volume_factor_and_unit_normalization():
    assert all(v.vertex_checks().values())
    assert v.volume_tensor()**2 == s.eye(6)


def test_full_parent_weyl_lift_and_wrong_single_sign_flip():
    assert all(v.parent_weyl_checks().values())


def test_response_pairs_source_and_complete_mediator():
    first,paired,wrong = v.response_control()
    assert first == paired and first > 0
    assert wrong != first


def test_native_evidence_grade_is_not_a_global_PDE_certificate():
    data = v.run()
    assert data['all_checks_pass'] and all(data['checks'].values())
    assert not data['global_PDE_numerically_solved']
    assert not data['independent_global_proof_review']
    assert not data['actual_nonzero_coupling_computed']
    assert not data['physical_chirality_derived']
