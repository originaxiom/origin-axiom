"""B1300 — the lines that would split the doublets from the triplets: the structural model of Y_9's Wilson lines (the
weight table in the (Q, u^c, L) basis, the eleven cubic couplings as zero-sum triples, the alphabet, B1278's counts, the
survival histogram of the SM lines, 0 split lines, the triplet's protection psi_D = psi_Q^-2) — fast, ~20 s; the weight
table re-derived from B1278's loaders (~2 min) and the pipeline's re-enumeration with survival bookkeeping (~18 min) — slow."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1300_the_doublet_triplet_lines" / "verification"))


def test_the_model_reproduces_b1278_and_no_line_splits_the_doublets_from_the_triplets():
    import dt_structure as S
    out = S.main()
    assert out['ok']
    assert out['expr']['D'] == (-2, 0, 0) and out['twice'] == ['D']                      # w_D = -2 w_Q, and only D
    assert out['expr']['H_u'] == (-1, -1, 0) and out['expr']['Dbar'] == (-1, 0, -1) and out['expr']['S'] == (3, 0, 1)
    assert out['dist'] == {0: 5628, 2: 3, 3: 145}
    assert out['counts'] == dict(k3=145, k2=3, three_gen=758593, su5_broken=737568, sm_vacua=706464, full=568656)
    assert out['hist'] == S.B1300A_HIST and out['n_split'] == 0 and out['n_nonfull'] == 137808
    assert out['ever'] == {'Q': 0, 'u^c': 0, 'd^c': 0, 'L': 0, 'e^c': 0, 'H_u': 30240, 'H_d': 29376, 'D': 0, 'Dbar': 29376, 'S': 28512, 'nu^c': 28512}
    assert out['hist_SNu'] == {(2, 2): 1296, (2, 3): 27216, (3, 2): 27216, (3, 3): 650736}
    assert out['theorem'] == dict(squares_in_alphabet=True, square_is_family=False)
    assert set(out['nonsm_spectra']) == {'(3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0)'} and out['nonsm_spectra']['(3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0)'] == 31104


@pytest.mark.slow
def test_the_weight_table_is_b1278s():
    import dt_structure as S
    ok, table = S.verify_against_pipeline()
    assert ok and table == S.SMITH_COORDS


@pytest.mark.slow
def test_the_pipeline_finds_no_split_line_and_keeps_d_everywhere():
    import dt_splitting as P
    out, ok = P.main()
    assert ok and out['n_sm'] == 706464 and out['n_full'] == 568656 and out['n_split'] == 0
    assert set(k[2] for k in out['hist_HuHdDDbar']) == {3}                                  # D total always 3
    assert out['ever_projected']['D'] == 0 and out['n_nonfull'] == 137808
