"""B118 -- locking test: the theta=-w0 fixed-root sign closed form (-1)^{h+1} (NOT the anticipated uniform +1).
The contragredient involution tau(X)=-J X^T J^{-1} acts as B112's reversal and carries sign (-1)^{h+1} on the lone
fixed root (odd m=n-h): +1 for ODD h, -1 for EVEN h -- a refinement/correction of B112's unsigned-permutation
"fixed root is always +1". The sign equals the inversion-identity parity (char(M^{-h})=char(-M^h) iff h odd), a
non-circular link. B112's char(M^h)=ceil labeling is tower-verified n<=5; B118 supplies the all-n SIGN, not an
independent all-n labeling proof. HONEST SCOPE: the theta-split is NOT the tower (B117; diverges n>=6). NO physics;
P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b118", _ROOT / "frontier" / "B118_theta_fixed_root_sign" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_tau_is_involution_and_reversal():
    ir = B.is_involution_and_reversal(6)
    assert ir["involution"] is True          # tau^2 = id
    assert ir["acts_as_reversal"] is True     # same permutation as B112's reversal lemma (now signed)


def test_fixed_root_sign_closed_form():
    sc = B.sign_closed_form(12)
    assert sc["all_match_minus1_pow_hplus1"] is True   # numeric == (-1)^{h+1} for all n<=12
    assert sc["symbolic_residual_zero"] is True         # the eps-form derivation gives (-1)^{h+1} symbolically


def test_sign_is_not_uniform_plus_one():
    nu = B.sign_is_not_uniform_plus_one(12)
    assert nu["uniform_plus_one"] is False     # the correction: NOT a uniform +1 (the handoff's anticipation)
    assert nu["tracks_h_parity"] is True        # it is (-1)^{h+1}
    assert nu["plus_one_all_odd_h"] is True and nu["minus_one_all_even_h"] is True


def test_sign_matches_inversion_parity_noncircular():
    smp = B.sign_matches_inversion_parity(12, 12)
    assert smp["match_all_nh"] is True         # (fixed-root sign==+1) <=> (inversion identity holds), all (n,h)
    assert smp["mismatches"] == []


def test_fixed_root_in_char_Mh_tower_labeling():
    fc = B.fixed_root_in_char_Mh_tower(6)
    assert fc["all_fixed_root_in_char_Mh"] is True   # B112's tower-verified labeling: fixed root in char(M^h)=ceil


def test_inversion_identity_odd_h_only():
    ii = B.inversion_identity(6)
    assert ii["holds_for_odd_h"] is True       # char(M^{-h}) = char(-M^h) for ODD h (M^{-1} ~ -M, det=-1)
    assert ii["fails_for_even_h"] is True       # and NOT for even h -- the emergent inversion/det identity
