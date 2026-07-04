import json, os
HERE=os.path.join(os.path.dirname(__file__),"..","frontier","B424_gateB_hessian")
R=json.load(open(os.path.join(HERE,"hessian.json")))
def test_hessian_golden_no_sm():
    assert R["sm_matches"]==[]
    assert R["prime_content"]==[2,3,5,7,11,13,17,19,29,41,47,89,199]
    assert R["spectrum"]["1"]=="-5"
