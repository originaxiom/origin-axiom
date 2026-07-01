"""B315 lock -- H14: the object's E8+E6-E7 exclusion vs heterotic's E7-skip. The exceptional trichotomy (E6 27 complex/
chiral, E7 56 pseudoreal/non-chiral, E8 248 real) => only E6 is chiral-capable. Heterotic's E7-skip = non-chirality
(pseudoreal 56) = ONE of the object's three independent obstructions (Diophantine + rep-theoretic + arithmetic,
B234/H20). The trace-1 law reaches {-3 (E6), 5 (E8)}; E7's disc 8 needs even trace (silver m=2). Verdict: SHARED (the
rep-theoretic obstruction), the object CONTAINS heterotic's; NOT the same single obstruction (B234/H30 independent); the
shared ROOT is E7's pseudoreality FS(56)=-1. Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B315_e7_exclusion_vs_heterotic" / "e7_exclusion_vs_heterotic.py"
_spec = importlib.util.spec_from_file_location("b315", _PATH)
b315 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b315)


def test_trichotomy_only_e6_chiral():
    assert b315.chiral_capable("E6") and not b315.chiral_capable("E7") and not b315.chiral_capable("E8")
    assert b315.EXCEPTIONAL["E7"]["fs"] == -1                      # 56 pseudoreal (B234 Sage)
    assert b315.ONLY_E6_IS_CHIRAL_CAPABLE


def test_arithmetic_reachability():
    assert b315.trace1_reaches() == [-3, 5]                        # E6 (cusp) + E8 (monodromy)
    assert b315.e7_needs_even_trace()                              # disc 8 only at silver m=2


def test_shared_but_not_same_obstruction():
    assert b315.HETEROTIC_SKIP_IS_NONCHIRALITY
    assert b315.OBJECT_E7_OVERDETERMINED_THREEFOLD                 # B234/H20
    assert b315.SHARED_OBSTRUCTION_IS_NONCHIRALITY                 # heterotic's = one of the three
    assert b315.SAME_SINGLE_OBSTRUCTION is False                   # B234/H30: independent
    assert b315.OBJECT_CONTAINS_HETEROTIC


def test_shared_root_is_pseudoreality():
    assert b315.SHARED_ROOT_IS_PSEUDOREALITY                       # FS(56)=-1
    assert b315.TWO_ENDS_MIRROR_HETEROTIC_CHAIN_IS_HOOK            # firewalled [HOOK]
    assert b315.DERIVES_SM_VALUES is False
    assert b315.verdict()
