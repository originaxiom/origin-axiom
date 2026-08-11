"""B1035 locks — the shadow library, the orphaned core, and the recorded non-finding.

Every assertion recounts over the tree at test time, so the numbers move with the repository
rather than going stale as a transcript.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1035", _ROOT / "frontier" / "B1035_shadow_library" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)
N = v.R["numbers"]


def test_every_check_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_shadow_library_exists__the_no_shared_library_premise_is_false():
    """THE CORRECTION. frontier/ is not 1,687 unconnected scripts: 227 files do sys.path surgery,
    and two arc directories are imported by ~100 cells each while filed as ordinary research."""
    assert N["sys_path_manipulators"] > 200
    assert N["hub_importers"]["cyclo_engine"] > 40
    assert N["hub_importers"]["step0_exact_matrices"] > 30
    assert v.R["checks"]["and_both_are_filed_as_ordinary_research_arcs"]["pass"]


def test_the_certified_core_is_orphaned__and_it_is_adoption_debt_not_missing_code():
    """6 of 1,687 frontier files import origin_axiom, and NOT ONE of the 220 that redefine
    L/R/A inline does — while src/origin_axiom/algebra.py has defined them all along."""
    assert N["core_importers"] < 10
    assert N["inline_LRA_redefiners"] > 150
    assert N["of_which_import_the_core"] == 0
    assert v.R["checks"]["the_core_defines_L_R_and_A"]["pass"]


def test_the_cores_only_consumers_are_the_original_probes():
    """No new consumer between B9 and B1034 — a thousand arcs. If this ever stops holding, the
    adoption debt is being paid and the lock should be revisited, not deleted."""
    arcs = N["core_importer_arcs"]
    assert all(a.startswith(("B1_", "B5_", "B6_", "B8_", "B9_", "B1034_")) for a in arcs), arcs


def test_the_trace_map_has_no_canonical_home_anywhere():
    """The substrate the atlas measures at 45% of probes: re-derived across frontier, absent
    from src/ entirely."""
    assert N["trace_map_files"] > 50
    assert N["trace_map_in_src"] == 0


def test_copying_is_not_independence():
    """Two arcs in the dense band share a byte-identical exact-arithmetic kernel, so agreement
    between them is weaker evidence than it looks. A limit on evidence, not a defect in an arc."""
    c = v.R["checks"]["two_arcs_in_the_dense_band_share_a_byte_identical_kernel"]
    assert c["pass"] and c["n_shared_functions"] > 30 and c["shared_lines"] > 300


def test_the_instrument_index_froze_at_B370_and_omits_the_maass_solver():
    assert N["toolbox_highest_arc"] < 500
    assert v.R["checks"]["and_it_omits_the_repos_most_precise_instrument"]["pass"]
    assert v.R["checks"]["while_that_instrument_is_real_and_on_main"]["pass"]


def test_the_unresolvable_paths_are_NOT_a_defect():
    """The recorded non-finding. 31 files carry sys.path inserts that cannot resolve here — all
    inside verbatim-preserved harvest packets whose manifest is a sha256 of every file AS
    RECEIVED, and whose reruns were done with packet-local imports. Editing them would break the
    manifest. Locked so a future sweep does not re-raise it as rot."""
    assert N["unresolvable_syspath_files"] > 20
    assert all(a.startswith(("B646_", "B651_", "B656_", "B663_", "B670_"))
               for a in N["harvest_arcs"]), N["harvest_arcs"]
    assert v.R["checks"]["and_the_harvest_arc_states_the_policy_and_how_it_reran_them"]["pass"]


def test_the_measurement_excludes_this_arcs_own_files():
    """Eighth instance of one hazard, first predicted in advance: verify.py imports origin_axiom
    to check the core, which would otherwise make it the 7th importer of the thing whose six
    importers are the finding."""
    assert not any("B1035" in str(p) for p in v.OTHERS)
    assert "B1035_shadow_library" not in " ".join(N["core_importer_arcs"])
