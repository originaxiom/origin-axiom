import json, os
HERE=os.path.join(os.path.dirname(__file__),"..","frontier","B420_tw6_lfunctions")
def test_L_identities_no_sm():
    R=json.load(open(os.path.join(HERE,"track_lfunctions.json")))
    assert R["entropy_eq_4Reg"] is True and R["entropy_eq_2sqrt5_L1chi5"] is True
    assert R["bar"]["any_exact_SM_match"] is False
