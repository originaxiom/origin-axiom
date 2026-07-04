import json, os
HERE=os.path.join(os.path.dirname(__file__),"..","frontier","B419_tw5_quantum")
def test_volume_conjecture_no_sm():
    R=json.load(open(os.path.join(HERE,"track_quantum.json")))
    gs=[R["growth"][k]["growth"] for k in ("20","60","100","180")]
    assert all(a>b for a,b in zip(gs,gs[1:]))  # descending toward Vol
    assert R["bar"]["any_exact_SM_match"] is False
