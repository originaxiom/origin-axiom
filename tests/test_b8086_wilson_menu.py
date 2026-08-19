"""B8086 — the Wilson-line menu cannot reach the SM. Reads results.json, never prose."""
import json, os, pytest
RES=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","frontier",
                 "B8086_wilson_menu","results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh: return json.load(fh)

def test_the_sweep_is_exhaustive(r):
    assert r["n_elements"]==5**6-1==15624

def test_every_row_has_rank_six(r):
    """The load-bearing fact: rank 6 everywhere, SM is rank 4. Re-derives B955 by census."""
    assert r["every_row_rank_6"] is True
    assert all(row["total_rank"]==6 for row in r["rows"])

def test_the_mode_is_a_tie_so_generic_collapse_does_not_select(r):
    assert r["mode_is_unique"] is False
    assert len(r["modal_rows"])==2 and r["modal_count"]==4320

def test_the_rarest_row_is_so10_and_is_unique(r):
    """Their strongest claim, and it holds."""
    ra=r["rarest"]
    assert ra["type"]=="D5" and ra["count"]==108 and ra["dim"]==46
    assert 108==27*4

def test_union_is_e6_and_intersection_is_the_cartan(r):
    assert r["union_is_e6"] is True and r["intersection_roots"]==0

def test_scope_limits_the_kill_to_abelian_holonomy(r):
    assert "NON-abelian" in r["scope"] or "non-abelian" in r["scope"]
