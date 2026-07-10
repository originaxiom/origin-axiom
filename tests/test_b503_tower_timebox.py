"""B503 -- locking test: the tower time-box (Closure Campaign Phase 4; pre-registered enum).
VERDICT LOCKED: SHARPER-REDUCTION. The filtration theorem char(T*|m/m^2) = prod_d char(N|G_{n,d})
turns the catalog conjecture into STATIC invariant theory (indecomposables of two traceless
matrices): n=2,3 towers re-derived (fifth route); n=4 catalog = the canonical quotient by F^{>=6};
n=5's contested doubled Sym^2 (B62 char(M^2)^2) EXISTS in the static module but collides with the
first extra in one graded piece -- the located wall. Character layer (W-form == mu_d) closed for
ALL n. NO promotion; no physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b503", _ROOT / "frontier" / "B503_tower_timebox" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_character_layer_closed_for_all_n():
    c = B.character_layer_all_n(amax=10, nmax=30)
    assert c["telescope_ok"] is True     # h_a(x,y,1) = sum_{k<=a} h_k(x,y): the all-n gen.-fn. lemma
    assert c["bookkeeping_ok"] is True   # => W-form == two-sequence mu_d for ALL n (was n<=8, B122)


def test_engine_control_sl2_maps_exact():
    assert B.sl2_maps_validated() is True   # coordinate maps == direct 2x2 substitution (exact)


def test_theorem_at_n2_both_det_signs():
    r = B.theorem_at_n2()
    assert r["all_ok"] is True              # char(DT@trivial) == char(Sym^2 N), all words
    dets = {d for _, d, _ in r["cases"]}
    assert dets == {1, -1}                  # metallic AND non-metallic (foreign control) covered


def test_n3_static_module_and_lawton_embdim():
    s = B.n3_structure()
    assert s["matches_expected"] is True    # G_3 = Sym^2 (+) Sym^3 (+) D^2 (+) D^3 (degrees 2,3,4,6)
    assert s["equals_lawton_embdim_9"] is True   # total 9 = Lawton's embedding dimension


def test_n3_intrinsic_equals_banked_catalog_times_det_line():
    s = B.n3_structure()
    r = B.n3_banked_reconciliation(s["modules"])
    assert r["symbolic_m_ok"] is True       # symbolic in m against the banked exact J(m) (B103)
    assert all(ok for _, _, ok in r["word_cases"])   # incl. the det=+1 non-metallic control


def test_n4_carriers_are_exactly_the_catalog():
    s = B.n4_structure()
    assert s["carriers_ok"] is True         # degrees 2..5: Sym^2, Sym^3, Sym^4+D^2, V D^2
    assert s["carrier_dim_15"] is True      # = n^2-1: the full n=4 catalog
    assert s["extras_ok"] is True           # extras start at degree 6: the clean split (n<=4 only)


def test_n4_carrier_identity_symbolic_both_dets():
    i = B.n4_carrier_identity()
    assert i["det_plus_ok"] is True and i["det_minus_ok"] is True
    assert B.n4_banked_spot_checks(ms=(1,)) is True   # banked proved B80 J(m) spot-check


def test_n5_contested_doubled_sym2_exists_and_collides():
    s = B.n5_structure()
    assert s["matches_expected"] is True    # all 24 catalog carriers present at degrees 2..6
    # the contested B62 char(M^2)^2 sector: CERTIFIED (unconditional rank certificate)
    assert s["contested_sym2D2_mult2_certified_lb"] is True
    # the located wall: mult 2 at Sym^2 D^2 @ degree 6 (carrier + extra in ONE graded piece)
    assert s["modules"][6] == {(2, 2): 2, (0, 3): 1}


def test_n5_catalog_divides_intrinsic():
    i = B.n5_divisibility_identity()
    assert i["det_plus_ok"] is True and i["det_minus_ok"] is True


def test_n6_pattern_persists():
    s = B.n6_structure()
    assert s["first_arm_ok"] is True        # Sym^2..Sym^6 exactly: the Cayley-Hamilton cutoff at d=n
    assert s["carriers_present"] is True    # doubled Sym^2@6 and Sym^3@7 present (each colliding)
